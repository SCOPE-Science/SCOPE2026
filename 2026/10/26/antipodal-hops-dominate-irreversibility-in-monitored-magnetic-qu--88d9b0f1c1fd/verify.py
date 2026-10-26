"""Finite independent checks of a magnetic-cycle entropy-production asymptotic.

Requires Python 3; optional mpmath adds direct finite-time diagnostics.
Analytic asymptotics for arbitrary cycle length are proved in RESULT.md.
"""
from fractions import Fraction
from math import factorial


def add(z, w):
    return (z[0]+w[0], z[1]+w[1])


def mul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def conj(z):
    return (z[0], -z[1])


def matmul(A, B):
    n=len(A)
    return [[tuple(sum(mul(A[i][k],B[k][j])[s] for k in range(n)) for s in range(2))
             for j in range(n)] for i in range(n)]


def powers(n, weights, highest):
    Z=(0,0)
    H=[[Z for _ in range(n)] for _ in range(n)]
    for i,a in enumerate(weights):
        j=(i+1)%n
        edge=(a,0) if i<n-1 else (0,a)  # total phase pi/2
        H[j][i]=edge
        H[i][j]=conj(edge)
    A=[[[ (1,0) if i==j else Z for j in range(n)] for i in range(n)]]
    for _ in range(highest):
        A.append(matmul(A[-1],H))
    return A


def coeff_probability(P, k, i, j):
    # [t^k] |(exp(-i H t))_ij|^2, exact in Gaussian rationals.
    out=Fraction(0)
    powminus=[(1,0), (0,-1),(-1,0),(0,1)]
    powplus=[(1,0), (0,1),(-1,0),(0,-1)]
    for p in range(k+1):
        q=k-p
        term=mul(powminus[p%4], powplus[q%4])
        term=mul(term,mul(P[p][i][j],conj(P[q][i][j])))
        # Conjugate-paired terms cancel their imaginary parts in the sum.
        out+=Fraction(term[0],factorial(p)*factorial(q))
    return out


def exact_tests():
    count=0
    for n in (3,5,7,9):
        m=(n-1)//2
        weights=[2+(3*i)%5 for i in range(n)]
        H=powers(n,weights,n)
        A=1
        for a in weights:A*=a
        for d in range(1,m+1):
            expected=Fraction(4*(-1)**(m+d+1)*A,factorial(d)*factorial(n-d))
            for i in range(n):
                j=(i+d)%n
                for k in range(1,n,2):
                    diff=coeff_probability(H,k,j,i)-coeff_probability(H,k,i,j)
                    assert diff==0,(n,d,i,k,diff)
                    count+=1
                diff=coeff_probability(H,n,j,i)-coeff_probability(H,n,i,j)
                assert diff==expected,(n,d,i,diff,expected)
                count+=1
                if d==m:
                    # Leading symmetric coefficient is the shortest-arc product squared.
                    S=1
                    for h in range(m): S*=weights[(i+h)%n]
                    p0=coeff_probability(H,2*m,j,i)
                    assert p0==Fraction(S*S,factorial(m)**2)
                    count+=1
        # Exact construction of the entropy prefactor from the farthest-pair terms.
        leading=Fraction(0)
        expression=Fraction(0)
        for i in range(n):
            j=(i+m)%n
            d=coeff_probability(H,n,j,i)-coeff_probability(H,n,i,j)
            b=coeff_probability(H,2*m,j,i)
            leading+=d*d/b/n
            L=1
            for h in range(m+1):L*=weights[(i+m+h)%n]
            expression+=Fraction(16*L*L,n*factorial(m+1)**2)
        assert leading==expression,(n,leading,expression)
        count+=1
        print('exact',n,'prefactor',leading)
    return count


def numeric_tests():
    try:
        import mpmath as mp
    except ImportError:
        print('Optional finite-time check omitted: mpmath is not installed.')
        return 0
    mp.mp.dps=55
    count=0
    for n in (3,5,7,9):
        m=(n-1)//2
        weights=[mp.mpf(2+(3*i)%5)/7 for i in range(n)]
        flux=mp.mpf('0.71')
        H=mp.matrix(n)
        for i,a in enumerate(weights):
            j=(i+1)%n
            H[j,i]=a*mp.exp(1j*flux/n)
            H[i,j]=a*mp.exp(-1j*flux/n)
        C=sum(mp.fprod(weights[(i+m+h)%n] for h in range(m+1))**2 for i in range(n))
        C*=16*mp.sin(flux)**2/(n*mp.factorial(m+1)**2)
        ratios=[]
        for tstr in ('0.24','0.12','0.06'):
            t=mp.mpf(tstr)
            U=mp.expm(-1j*t*H)
            Q=[[abs(U[i,j])**2 for j in range(n)] for i in range(n)]
            ep=sum((Q[i][j]-Q[j][i])*mp.log(Q[i][j]/Q[j][i])
                   for i in range(n) for j in range(i+1,n))/n
            r=ep/(C*t**(n+1))
            ratios.append(r)
            assert abs(r-1)<mp.mpf('0.045'),(n,tstr,r)
            count+=1
        assert abs(ratios[2]-1)<abs(ratios[1]-1)<abs(ratios[0]-1)
        count+=1
        print('numeric',n,'ratios',*[mp.nstr(r,12) for r in ratios])
    # Exact even-cycle reciprocity tested directly for arbitrary nontrivial flux.
    for n in (4,6,8):
        H=mp.matrix(n)
        for i in range(n):
            j=(i+1)%n
            z=mp.mpf(i+2)*mp.exp(1j*mp.mpf('0.73')/n)/7
            H[j,i]=z
            H[i,j]=z.conjugate()
        U=mp.expm(-1j*mp.mpf('0.61')*H)
        err=max(abs(abs(U[i,j])**2-abs(U[j,i])**2) for i in range(n) for j in range(n))
        assert err < mp.mpf('1e-48'),(n,err)
        count+=1
    return count

if __name__=='__main__':
    e=exact_tests()
    a=numeric_tests()
    print('PASS exact identities',e,'finite-time diagnostics',a)
