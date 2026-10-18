"""Independent arithmetic spot checks for exact excursion identities.

This is a finite consistency checker; all infinite claims require the accompanying proof.
"""
from fractions import Fraction
from math import comb, exp, pi, sqrt, floor, erfc


def catalan(k):
    return comb(2*k, k)//(k+1)


def polynomials(z, lam, n):
    p0 = Fraction(1)
    p1 = 1-z*lam*(1-lam)
    if n == 0:
        return p0
    if n == 1:
        return p1
    for _ in range(1, n):
        p0, p1 = p1, p1-z*lam*(1-lam)*p0
    return p1


def first_passage_prefix(lam, nmax):
    # Exact paths reaching state 4 on their last step, relative start 5.
    # Intermediate states are capped by nmax+4: before the nth return a
    # path of length <=n can climb at most n-1 units if it returns at n.
    # Dynamic programming tracks *only* first-return sequences.
    totals = []
    previous = {5: Fraction(1)}
    for n in range(1, nmax+1):
        ret = Fraction(0)
        current = {}
        for state, mass in previous.items():
            for r in range(0, nmax+2):
                nxt = state-1+r
                if nxt > nmax+5:
                    continue
                w = mass*(1-lam)*lam**r
                if nxt == 4:
                    ret += w
                elif nxt >=5:
                    current[nxt] = current.get(nxt,Fraction(0))+w
        totals.append(ret)
        previous = current
    return totals


def exact_height_probability(lam, m):
    # Harmonic boundary system from i=5 to i=m-1.
    # Equation: u_i = (1-lam)*u_(i-1)
    # + sum_{r=1}^{m-i} (1-lam) lam**r * u_(i-1+r)
    # + probability of overshooting level m.
    # Direct Gaussian elimination over rational numbers.
    size = m-5
    arr=[]
    for s in range(size):
        state = 5+s
        row = [Fraction(int(k==s)) for k in range(size)]
        b = lam**(m-state+1)
        for r in range(m-state+1):
            dst=state-1+r
            if 5<=dst<m:
                row[dst-5] -= (1-lam)*lam**r
        arr.append(row+[b])
    for k in range(size):
        pivot=next(j for j in range(k,size) if arr[j][k])
        arr[k],arr[pivot]=arr[pivot],arr[k]
        f=arr[k][k]
        arr[k]=[x/f for x in arr[k]]
        for j in range(size):
            if j!=k:
                f=arr[j][k]
                arr[j]=[a-f*b for a,b in zip(arr[j],arr[k])]
    return arr[0][-1]




def bounded_duration_pgf(lam, m, z):
    # Direct independent solution of the finite-state stopped chain.
    size=m-5
    arr=[]
    for i in range(5,m):
        row=[Fraction(int(k==i-5)) for k in range(size)]
        b=Fraction(0)
        for r in range(m-i+1):
            j=i-1+r
            w=z*(1-lam)*lam**r
            if j==4:
                b+=w
            elif 5<=j<m:
                row[j-5]-=w
        arr.append(row+[b])
    for k in range(size):
        pivot=next(i for i in range(k,size) if arr[i][k])
        arr[k],arr[pivot]=arr[pivot],arr[k]
        f=arr[k][k]
        arr[k]=[x/f for x in arr[k]]
        for j in range(size):
            if j!=k:
                f=arr[j][k]
                arr[j]=[a-f*b for a,b in zip(arr[j],arr[k])]
    return arr[0][-1]

def test_exact():
    for lam in [Fraction(1,3),Fraction(1,2),Fraction(3,5)]:
        vals = first_passage_prefix(lam, 9)
        for n,p in enumerate(vals,1):
            expected=Fraction(catalan(n-1))*((1-lam)**n)*(lam**(n-1))
            assert p==expected,(lam,n,p,expected)
        for m in range(6,12):
            for z in [Fraction(1,4),Fraction(2,3),Fraction(1)]:
                closed=z*(1-lam)*polynomials(z,lam,m-6)/polynomials(z,lam,m-5)
                direct=bounded_duration_pgf(lam,m,z)
                assert closed==direct,(lam,m,z,closed,direct)
            q=(1-lam)/lam
            u=Fraction(1,m-3) if q==1 else (q-1)/(q**(m-3)-1)
            actual=exact_height_probability(lam,m)
            assert actual==u,(lam,m,actual,u)
            z=Fraction(1)
            H=z*(1-lam)*polynomials(z,lam,m-6)/polynomials(z,lam,m-5)
            assert H+u==1,(lam,m,H,u)
    for lam in [Fraction(2,5),Fraction(1,2),Fraction(3,5)]:
        for z in [Fraction(1,4),Fraction(2,3),Fraction(1)]:
            previous=Fraction(0)
            for m in range(6,20):
                current=z*(1-lam)*polynomials(z,lam,m-6)/polynomials(z,lam,m-5)
                assert current>=previous
                previous=current
    print('EXACT_CATALAN_HEIGHT_AND_GENERATING_FUNCTION_CHECK_OK')


def test_scaling():
    # Finite-parameter check on both sides, not a proof of limits.
    for sign in (-1,1):
        for eta in (.01,.005):
            lam=.5+sign*eta
            u=.9
            m=floor(u/eta)
            q=(1-lam)/lam
            observed=((q-1)/(q**(m-3)-1))/eta
            predicted=4*sign/(1-exp(-4*sign*u))
            assert abs(observed-predicted)<.17,(eta,sign,observed,predicted)
    # Finite-length first-passage tail near the critical temporal window.
    t=0.25
    integral_profile=exp(-4*t)/sqrt(pi*t)-2*erfc(2*sqrt(t))
    for sign in (-1,1):
        for eta in (0.02,0.01):
            lam=0.5+sign*eta
            threshold=floor(t/eta**2)
            nmax=int(12/eta**2)
            pn=1-lam
            tail=0.0
            for n in range(1,nmax):
                if n>threshold:
                    tail+=pn
                pn*=2*(2*n-1)/(n+1)*lam*(1-lam)
            if nmax>threshold:
                tail+=pn
            if sign==1:
                tail+=(2*lam-1)/lam
            limit=integral_profile+(4 if sign==1 else 0)
            assert abs(tail/eta-limit)<0.20,(eta,sign,tail/eta,limit)
    print('FINITE_SCALING_CHECK_OK')

if __name__=='__main__':
    test_exact()
    test_scaling()
