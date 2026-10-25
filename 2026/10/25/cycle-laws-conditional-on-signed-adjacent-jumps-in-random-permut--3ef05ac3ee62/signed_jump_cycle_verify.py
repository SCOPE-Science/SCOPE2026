"""Exact enumeration of signed positional jumps and cycle counts in permutations."""
from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import factorial

def cyc(p):
    n=len(p); seen=[False]*n; c=0
    for i in range(n):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]:
                seen[j]=True; j=p[j]
    return c

def pk(n,i,d):
    m=n-abs(d)
    if d==1: return {0:Fraction(m-1,m),2:Fraction(1,m)}
    if d>1:
        k=int(i<=n-d)+int(i>=d)
    else:
        h=-d
        k=int(i>=h+1)+int(i<=n-h-1)+int(h==1)
    return {0:Fraction(m-k,m),1:Fraction(k,m)}

def expected(n,i,d):
    base=Counter({0:1})
    for k in range(1,n-1):
        nb=Counter()
        for j,c in base.items():
            nb[j]+=c*(k-1);nb[j+1]+=c
        base=nb
    # rising factorial of n-2, correct C_0=0
    mass=pk(n,i,d)
    out=Counter()
    for j,c in base.items():
        for a,p in mass.items():out[j+a]+=Fraction(c)*p*(n-abs(d))
    return {k:v for k,v in out.items() if v}

def brute(n):
    stats={(i,d):Counter() for i in range(1,n) for d in range(1-n,n) if d}
    for p in permutations(range(n)):
        c=cyc(p)
        for i in range(1,n):
            d=p[i]-p[i-1]
            stats[(i,d)][c]+=1
    for (i,d),h in stats.items():
        mass=expected(n,i,d)
        if h!=mass:
            raise AssertionError((n,i,d,h,mass))
    # pooled expected coefficients via the two-edge contraction law.
    for d in range(1-n,n):
        if not d: continue
        h=abs(d); m=n-h
        pooled=Counter()
        for i in range(1,n): pooled.update(stats[(i,d)])
        if d==1: shifts={0:Fraction(n-2,n-1),2:Fraction(1,n-1)}
        elif d>1: shifts={0:Fraction(n-3,n-1),1:Fraction(2,n-1)}
        elif h==1: shifts={0:Fraction((n-1)**2-(3*n-5),(n-1)**2),1:Fraction(3*n-5,(n-1)**2)}
        else:
            pp=Fraction(2*(m-1),(n-1)*m)
            shifts={0:1-pp,1:pp}
        baseline=Counter({0:1})
        for r in range(1,n-1):
            nxt=Counter()
            for c,v in baseline.items():
                nxt[c]+=(r-1)*v
                nxt[c+1]+=v
            baseline=nxt
        pred=Counter()
        for c,v in baseline.items():
            for sh,pr in shifts.items():pred[c+sh]+=v*pr*(n-1)*m
        pred=Counter({k:v for k,v in pred.items() if v})
        if pooled!=pred: raise AssertionError(('pooled',n,d,pooled,pred))
    # also compare exact global covariances for every signed d
    fact=factorial(n); total=Counter()
    for p in permutations(range(n)): total[cyc(p)]+=1
    ec=Fraction(sum(k*v for k,v in total.items()),fact)
    for d in range(1-n,n):
        if d==0:continue
        count=sum(sum(stats[(i,d)].values()) for i in range(1,n))
        ex=Fraction(sum(k*v for i in range(1,n) for k,v in stats[(i,d)].items()),fact)
        cov=ex-Fraction(count,fact)*ec
        h=abs(d)
        if d>0:pred=Fraction(n-h,n*n*(n-1))
        elif h==1:pred=Fraction(n*n-2*n-1,n*n*(n-1))
        else:pred=Fraction(-(n+h),n*n*(n-1))
        if cov!=pred:raise AssertionError(('cov',n,d,cov,pred))
    return len(stats)

if __name__=='__main__':
    for n in range(2,9):print('n',n,'local_laws',brute(n),'OK')
