"""Standalone exact checks for finite-regime correlated-jury switching theorem.
Uses only the Python standard library; no external data or paths.
The analytic zero-count theorem, not this finite computation, establishes generality.
"""
from fractions import Fraction as F
from math import comb
from decimal import Decimal, localcontext


def poly_mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def construct(m,t):
    q=[F(0),F(1)]
    for j in range(m-1):
        q=poly_mul(q,[-t**(2*j+3),F(1)])
    assert len(q)==m+1 and q[0]==0
    assert all(q[i]!=0 for i in range(1,m+1))
    assert all(q[i]*q[i+1]<0 for i in range(1,m))
    return q


def horner(q,z):
    a=F(0)
    for x in reversed(q): a=a*z+x
    return a


def majority(n,p):
    return sum((Decimal(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n//2+1,n+1)),Decimal(0))


def main():
    t=F(1,3)
    sign_checks=0
    for m in range(2,16):
        q=construct(m,t)
        signs=[]
        for r in range(m+4):
            z=t**(2*(r+1))
            val=horner(q,z)
            assert val!=0
            signs.append(1 if val>0 else -1)
            assert (signs[-1]==(1 if r%2==0 else -1)) if r<m else True
            sign_checks+=1
        assert sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))==m-1
    q=construct(3,t)
    assert q==[F(0),F(1,6561),-F(10,243),F(1)]
    expected=[F(52,59049),F(-4,1594323),F(52,387420489)]
    assert [horner(q,t**(2*(r+1))) for r in range(3)]==expected
    with localcontext() as ctx:
        ctx.prec=100
        td=Decimal(1)/Decimal(3)
        coeff=[Decimal(x.numerator)/Decimal(x.denominator) for x in q[1:]]
        lambdas=[td**(2*i) for i in range(1,4)]
        delta=[(Decimal(1)-4*lam).sqrt() for lam in lambdas]
        raw=[abs(c)/d for c,d in zip(coeff,delta)]
        normal=sum(raw)
        weights=[a/normal for a in raw]
        pp=[(Decimal(1)+(Decimal(1) if c>0 else Decimal(-1))*d)/2 for c,d in zip(coeff,delta)]
        assert sum(weights)==1
        assert sum(w*p for w,p in zip(weights,pp))>Decimal('.5')
        assert sum(w for w,p in zip(weights,pp) if p>Decimal('.5'))>Decimal('.5')
        vals=[sum(w*majority(2*r+1,p) for w,p in zip(weights,pp)) for r in range(5)]
        inc=[vals[r+1]-vals[r] for r in range(4)]
        assert [int(x>0)-int(x<0) for x in inc]==[1,-1,1,1]
        for r,increment in enumerate(inc):
            combfactor=Decimal(comb(2*r+1,r))
            val=Decimal(horner(q,t**(2*(r+1))).numerator)/Decimal(horner(q,t**(2*(r+1))).denominator)
            assert abs(increment-combfactor*val/normal)<Decimal('1e-85')
    print('PASS: exact polynomial factorization, exact alternating signs, and sharp reversal counts for m=2..15')
    print('PASS: three-regime rational example coefficients and first three exact polynomial signs')
    print('PASS: independent 100-digit conditional binomial majority evaluations for jury sizes 1,3,5,7,9')
    print(f'EXACT SIGN CHECKS: {sign_checks}')
    print('LIMIT: these finite checks do not prove the universal real-zero bound or asymptotic high-competence construction')

if __name__=='__main__': main()
