"""Exact-rational reproducibility checks for a discrete Fisher-information stability inequality."""
from fractions import Fraction as F
from math import comb
from itertools import product
import random


def binlaw(m):
    return [F(comb(m,i),2**m) for i in range(m+1)]

def balanced_random(m,seed):
    rng=random.Random(seed)
    evens=[i for i in range(m+1) if i%2==0]
    odds=[i for i in range(m+1) if i%2==1]
    v=[F(0) for _ in range(m+1)]
    for idxs in (evens, odds):
        vals=[rng.randint(1,17) for _ in idxs]
        for k,w in zip(idxs, vals): v[k]=F(w,2*sum(vals))
    return v

def score(p):
    A=F(0); s=[]
    for j,f in enumerate(p):
        A=f-A
        s.append(2-4*A/f)
    assert s[0]==-2 and s[-1]==2
    assert sum(x*y for x,y in zip(p,s))==0
    return s

def conv(f,g):
    v=[F(0)]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g):v[i+j]+=x*y
    return v

def J(f):return sum((f_i*s_i*s_i for f_i,s_i in zip(f,score(f))),F(0))

def check(f,g,a,b):
    m,n=len(f)-1,len(g)-1
    sf,sg=score(f),score(g)
    h=conv(f,g)
    sh=score(h)
    lhs=a*a*J(f)+b*b*J(g)-(a+b)**2*J(h)
    allpairs=F(0)
    adjpairs=F(0)
    for k in range(m+n+1):
        pairs=[(i,k-i) for i in range(m+1) if 0<=k-i<=n]
        assert sum(f[i]*g[j]*sf[i] for i,j in pairs)/h[k]==sh[k]
        assert sum(f[i]*g[j]*sg[j] for i,j in pairs)/h[k]==sh[k]
        for z in range(len(pairs)):
            i,j=pairs[z]
            for zz in range(z+1,len(pairs)):
                ii,jj=pairs[zz]
                d=a*(sf[i]-sf[ii])+b*(sg[j]-sg[jj])
                allpairs += f[i]*g[j]*f[ii]*g[jj]*d*d/h[k]
    for i in range(1,m+1):
        for j in range(1,n+1):
            coef=f[i-1]*g[j]*f[i]*g[j-1]/h[i+j-1]
            adjpairs+=coef*(a*(sf[i]-sf[i-1])-b*(sg[j]-sg[j-1]))**2
    c=min(f)**2*min(g)**2
    Ef=sum((sf[i]-sf[i-1]-F(4,m))**2 for i in range(1,m+1))
    Eg=sum((sg[j]-sg[j-1]-F(4,n))**2 for j in range(1,n+1))
    rhs=c*(n*a*a*Ef+m*b*b*Eg+16*m*n*(a/F(m)-b/F(n))**2)
    assert lhs==allpairs,(lhs,allpairs)
    assert lhs>=adjpairs>=rhs,(lhs,adjpairs,rhs)
    return lhs,rhs,Ef,Eg

if __name__=='__main__':
    count=0
    for m,n in product(range(1,6),repeat=2):
        for it in range(16):
            f=balanced_random(m,101+53*m+61*n+it)
            g=balanced_random(n,193+37*m+101*n+it)
            a=F(it%6+1,it%3+2)
            b=F(it%5+1,it%4+2)
            check(f,g,a,b)
            count+=1
    # Exact equality including optimized reciprocal Stam coefficients.
    for m,n in product(range(1,11),repeat=2):
        f,g=binlaw(m),binlaw(n)
        a,b=F(m,4),F(n,4)
        gap,rhs,ef,eg=check(f,g,a,b)
        assert gap==rhs==ef==eg==0
        assert J(f)==F(4,m) and J(g)==F(4,n)
        count+=1
    # Quadratic deficit vs linear total variation at near equality.
    g=binlaw(2)
    for r in (32,64,128,256,512,1024):
        eps=F(1,r)
        f=[F(1,4)+eps,F(1,2),F(1,4)-eps]
        a,b=1/J(f),1/J(g)
        gap,_,ef,_=check(f,g,a,b)
        assert gap>0 and ef>0
        assert sum(abs(x-y) for x,y in zip(f,g))/2==eps
        # Elementary upper bound consistent with quadratic onset.
        assert 0<gap/eps**2 < 200
        count+=1
    print(f'PASS: {count} exact-rational configurations, including full conditional-variance identity, sharp equality, stability, and quadratic onset.')
