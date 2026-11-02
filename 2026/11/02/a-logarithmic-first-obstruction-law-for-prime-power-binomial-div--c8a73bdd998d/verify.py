"""Finite independent checks for the prime-power first-obstruction density theorem.
Only classical integer arithmetic; the theorem is proved separately.
"""
from math import comb, gcd
from fractions import Fraction

def vp_factorial(N,p):
    e=0
    while N:
        N//=p
        e+=N
    return e

def vp(N,p):
    t=0
    while N%p==0:
        t+=1;N//=p
    return t

def residue_count(lo,hi,m,a):
    return (hi-1-a)//m-(lo-1-a)//m

def exact_delay(p,r):
    B=p**r; total=0
    for n in range((p+1)//2,p):
        t=((p-n)*B+n-1)//n
        a=(-pow(n,-1,p))%p
        a2=(-pow(n,-1,p*p))%(p*p)
        total+=residue_count(t,B,p,a)-residue_count(t,B,p*p,a2)
    return total

def direct(p,r):
    B=p**r; d=0; cases=0
    for b in range(1,B):
        if b%p==0: continue
        n=next(n for n in range(1,p) if (b*n+1)%p==0)
        # Independent valuation via Legendre factorial sums.
        N=(B+b)*n; K=B*n
        val=vp_factorial(N,p)-vp_factorial(K,p)-vp_factorial(N-K,p)
        failure=val < vp(b*n+1,p)
        pred=(n+(b*n)//B>=p and (b*n+1)%(p*p)!=0)
        assert (not failure)==pred,(p,r,b,n,val,pred)
        if p<=11 and r<=2:  # Actual full integer divisibility, not just local valuation.
            assert (comb(N,K)%(b*n+1)==0)==pred,(p,r,b,n)
        d+=pred; cases+=1
    assert d==exact_delay(p,r),(p,r,d,exact_delay(p,r))
    return d,cases

if __name__=='__main__':
    cases=0; tests=0
    for p,r in [(2,2),(3,2),(3,3),(5,2),(5,3),(7,2),(11,2),(13,2),(17,2),(19,2),(23,2),(29,2)]:
        a,b=direct(p,r);cases+=b;tests+=1
        rational=Fraction(p-1,p)-sum((Fraction(1,n) for n in range((p+1)//2,p)),Fraction(0)) if p%2 else Fraction(0)
        assert abs(Fraction(a,b)-rational) <=Fraction(2,p**(r-1))
    print('VERIFY_OK configurations=%d coefficients=%d independent_legendre=PASS exact_residue_count=PASS full_binomial_subset=PASS'%(tests,cases))
