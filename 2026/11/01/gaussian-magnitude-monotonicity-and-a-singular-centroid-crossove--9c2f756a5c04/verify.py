"""Standalone exact tests and high-precision diagnostics for equiradial semimetric Gaussian magnitude."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import math


def solve(A, b):
    n=len(b)
    T=[list(row)+[b[i]] for i,row in enumerate(A)]
    for j in range(n):
        piv=next((i for i in range(j,n) if T[i][j]),None)
        if piv is None:raise ValueError('singular matrix')
        T[j],T[piv]=T[piv],T[j]
        d=T[j][j]
        T[j]=[x/d for x in T[j]]
        for i in range(n):
            if i==j:continue
            c=T[i][j]
            T[i]=[x-c*y for x,y in zip(T[i],T[j])]
    return [row[-1] for row in T]


def check_exact(m, p, q):
    n=m+1
    K=[[F(1) if i==j else (p if i==0 or j==0 else q) for j in range(n)] for i in range(n)]
    w=solve(K,[F(1)]*n)
    d=1+(m-1)*q-m*p*p
    assert d>0
    formula=1+F(m)*(1-p)**2/d
    assert sum(w)==formula
    assert w[1]==(1-p)/d
    assert w[0]==1-m*p*(1-p)/d


def diagnostic(m,r,s):
    with localcontext() as ctx:
        ctx.prec=65
        mD=Decimal(m);rd=Decimal(r.numerator)/Decimal(r.denominator);ss=Decimal(str(s))
        p=(-ss).exp()
        q=(-ss*rd).exp()
        d=Decimal(1)+(mD-1)*q-mD*p*p
        mag=1+mD*(1-p)**2/d
        T=2*p*(1-mD*p)+(mD-1)*q*(rd+(2-rd)*p)
        assert T>0,(m,r,s,T)
        assert mag>1 and mag<m+1
        return mag


def run():
    assertions=0
    for m in range(3,10):
        for p in [F(1,2),F(1,3),F(3,4)]:
            for rr in [1,2]:
                check_exact(m,p,p**rr)
                assertions+=4
    for m,denom,rcrit in [(3,2,F(3)),(4,2,F(8,3)),(5,2,F(5,2)),(6,2,F(12,5)),(7,2,F(7,3))]:
        p=F(1,denom**rcrit.denominator)
        q=F(1,denom**rcrit.numerator)
        check_exact(m,p,q)
        assertions+=4
    for m in list(range(3,30))+[50,100,500]:
        rc=F(2*m,m-1)
        for r in [F(1,3),F(1),F(2),rc-F(1,13),rc]:
            if r<=0:continue
            for ss in ['0.0001','0.003','0.02','0.1','0.5','1','3','10']:
                diagnostic(m,r,ss)
                assertions+=3
    for m in range(3,18):
        # Strict H>0 for rational integer alpha values m=3 (alpha=2); otherwise sample rational p,
        # the general sign follows independently by the exact third-derivative argument.
        with localcontext() as ctx:
            ctx.prec=70
            k=Decimal(m-1); alpha=1+2/k
            for j in range(1,100):
                p=Decimal(j)/100
                H=1-(k+1)*p+(k+1-p)*p**alpha
                assert H>0,(m,j,H)
                assertions+=1
    print('PASS; assertions',assertions)

if __name__=='__main__':run()
