"""Exact finite-dimensional checks for the Markov-dimer spectral and inversion formulas.
Run with Python 3; the unrestricted conclusions require the proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

CASES = [(F(1,3),F(-1,2)), (F(-1,2),F(-1,3)), (F(0), F(0)), (F(1,3),F(1,4)),(F(-1,2),F(-1,5)),
         (F(2,5),F(-1,4)),(F(3,4),F(1,2)),(F(1,5),F(0)),
         (F(-2,3),F(3,4)),(F(1,2),F(-1,4))]

def is_admissible(m,r):
    return - (1-abs(m))/(1+abs(m)) <= r < 1 and -1<m<1 and r>-1

def trans(s,t,m,r):
    # P(S_next=t | S=s)
    return (1+t*(m+r*(s-m)))/2

def spin_moment(indices,m,r):
    lo,hi=min(indices),max(indices)
    ans=F(0)
    for vals in product((-1,1),repeat=hi-lo+1):
        pr=(1+m*vals[0])/2
        for a,b in zip(vals,vals[1:]):
            pr*=trans(a,b,m,r)
        p=1
        for ix in indices:p*=vals[ix-lo]
        ans+=pr*p
    return ans

def expected_w(coords,m,r):
    ans=F(0)
    for phase in (0,1):
        ix=[];sgn=1
        for n in coords:
            q=n-phase
            ix.append(q//2)
            if q%2:sgn=-sgn
        ans+=sgn*spin_moment(ix,m,r)/2
    return ans

def predicted_pair(n,m,r):
    k=n//2
    def corr(j):return m*m+(1-m*m)*r**j
    return corr(k) if n%2==0 else -(corr(k)+corr(k+1))/2

def predicted_trip(m,r):
    return m*(1-m*m)*(1-r)**2/2

def test():
    paircount=0;transitions=0;triples=0
    for m,r in CASES:
        assert is_admissible(m,r)
        for s in (-1,1):
            assert trans(s,1,m,r)>=0 and trans(s,-1,m,r)>=0
            assert trans(s,1,m,r)+trans(s,-1,m,r)==1
            transitions+=2
        assert spin_moment([0],m,r)==m
        for lag in range(13):
            actual=expected_w((0,lag),m,r)
            assert actual==predicted_pair(lag,m,r),(m,r,lag,actual,predicted_pair(lag,m,r))
            # Equivalent Fourier coefficients of Bragg+Poisson density.
            base=m*m*((-1)**lag)
            remainder=predicted_pair(lag,m,r)-base
            if lag%2==0:
                assert remainder==(1-m*m)*r**(lag//2)
            else:
                k=lag//2
                assert remainder==-(1-m*m)*(r**k+r**(k+1))/2
            paircount+=1
        assert expected_w((0,1,2),m,r)==0
        actual=expected_w((0,1,3),m,r)
        assert actual==predicted_trip(m,r),(m,r,actual,predicted_trip(m,r))
        assert expected_w((0,2,3),m,r)==-actual
        # Distinct signed biases have identical two-point statistics,
        # while a nonzero third-order correlation has the opposite sign.
        for n in range(9):
            assert predicted_pair(n,m,r)==predicted_pair(n,-m,r)
        assert predicted_trip(-m,r)==-actual
        # Exact inversion from the two-point Bragg weight and eta(2).
        B=m*m
        recovered_r=(predicted_pair(2,m,r)-B)/(1-B)
        assert recovered_r==r
        recovered_m=2*actual/((1-B)*(1-r)**2)
        assert recovered_m==m
        triples+=3
    print(f'VERIFY_OK: {len(CASES)} rational Markov laws; {transitions} transition probabilities; '
          f'{paircount} exact autocorrelation/Fourier identities (including primitive boundary cases); '
          f'{triples} three-site identities; complete signed-parameter inversion at all samples')

if __name__=='__main__':test()
