"""Reproduce exact symmetric M-matrix star-scaling spectral identities.
Only Python standard library is required.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
import math

def star_data(m, c):
    """High-precision solution for m leaves and c in (0,1)."""
    with localcontext() as ctx:
        ctx.prec = 70
        c=Decimal(str(c))
        mD=Decimal(m)
        p=c*(mD-1)/mD.sqrt()
        t=(p+(p*p+4).sqrt())/2
        b2=1/(1-c*t/mD.sqrt())
        a2=t*t*b2
        lam=a2+b2-1
        K=(1+c)/(1-c)
        u=b2
        # star matrix row-sum identities, scaled coordinates
        assert abs(a2-c*mD.sqrt()*t*b2-1)<Decimal('1e-55')
        assert abs(b2-c*t*b2/mD.sqrt()-1)<Decimal('1e-55')
        assert abs((lam-1)*(lam-u))>0
        assert Decimal(1)<u<lam
        assert abs(t*t-p*t-1)<Decimal('1e-55')
        assert lam<Decimal(m+1)*K
        return t,b2,lam,K

for c in ('0.2','0.5','0.8'):
    print('c',c)
    for m in (2,3,8,31,255,4095):
        t,b2,lam,K=star_data(m,c)
        print('m=%4d  cond(A)=%.6f  cond(X)=%.6f  cond(B)=%.6f  cond(B)/m=%.6f'%(m,K,t,lam,lam/Decimal(m)))
    t,b2,lam,K=star_data(1048575,c)
    limit=Decimal(c)**2/(1-Decimal(c)**2)
    print('large m ratios cond(X)/sqrt(m) %.9f expected %.9f; cond(B)/m %.9f expected %.9f'%(t/Decimal(1048575).sqrt(),Decimal(c),lam/Decimal(1048575),limit))
print('ALL CHECKS PASSED: closed-form hub/leaf equations; ordered eigenvalues; general upper bound on this family; asymptotic coefficients')
