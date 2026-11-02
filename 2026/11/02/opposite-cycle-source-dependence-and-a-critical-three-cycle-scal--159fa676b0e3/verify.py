"""Exact finite checks for cycles and empty indegrees in loopless uniform random mappings.
Use: python verify.py. Python standard library only.
"""
from itertools import product
from fractions import Fraction
from math import factorial

def falling(n,k):
    z=1
    for j in range(k): z *= n-j
    return z

def cycle_counts(f):
    n=len(f); out=[0]*(n+1)
    seen=[False]*n
    for i in range(n):
        if seen[i]: continue
        seen_local={}; path=[]; x=i
        while not seen[x] and x not in seen_local:
            seen_local[x]=len(path); path.append(x); x=f[x]
        if x in seen_local:
            out[len(path)-seen_local[x]]+=1
        for y in path: seen[y]=True
    return out

def theoretical(n,k):
    b=Fraction(n-2,n-1)
    expect=Fraction(falling(n,k),k*(n-1)**k)
    return expect*(Fraction(n-k)*b**(n-k-1)-n*b**(n-1))

def exhaustive(n):
    options=[tuple(j for j in range(n) if j!=i) for i in range(n)]
    count=(n-1)**n
    ztot=0; ctot=[0]*(n+1); mixed=[0]*(n+1)
    for f in product(*options):
        indeg=[0]*n
        for j in f: indeg[j]+=1
        z=indeg.count(0)
        c=cycle_counts(f)
        ztot+=z
        for k in range(2,n+1):
            ctot[k]+=c[k]; mixed[k]+=z*c[k]
    checks=0
    assert Fraction(ztot,count)==n*Fraction(n-2,n-1)**(n-1); checks+=1
    for k in range(2,n+1):
        expected=Fraction(falling(n,k),k*(n-1)**k)
        assert Fraction(ctot[k],count)==expected; checks+=1
        calculated=Fraction(mixed[k],count)-Fraction(ctot[k]*ztot,count**2)
        assert calculated==theoretical(n,k),(n,k,calculated,theoretical(n,k)); checks+=1
        assert (calculated>0)==(k==2);checks+=1
    return checks

def palm_factorial_moment(n,k,t):
    assert 2<=k<=n and 0<=t<=n-k
    return (Fraction(falling(n-k,t))
            *Fraction(n-t,n-1)**t
            *Fraction(n-t-1,n-1)**(n-k-t))

def verify_palm(n,k):
    forced=list(range(1,k))+[0]
    options=[tuple(j for j in range(n) if j!=i) for i in range(k,n)]
    denominator=(n-1)**(n-k)
    total=[0]*(n-k+1)
    for rest in product(*options):
        f=forced+list(rest)
        indeg=[0]*n
        for v in f: indeg[v]+=1
        z=indeg.count(0)
        for t in range(n-k+1):total[t]+=falling(z,t)
    for t in range(n-k+1):
        assert Fraction(total[t],denominator)==palm_factorial_moment(n,k,t),(n,k,t)
    return n-k+1

def run():
    assertions=0
    for n in range(3,8):
        assertions+=exhaustive(n)
    for n in range(3,8):
        for k in range(2,n+1):assertions+=verify_palm(n,k)
    for n in range(3,201):
        for k in range(2,n+1):
            v=theoretical(n,k)
            assert (v>0)==(k==2),(n,k,v);assert v!=0
            assertions+=2
        # exact base threshold algebra
        b=Fraction(n-2,n-1)
        assert (n-2)-n*b*b==Fraction(n-2,(n-1)**2)
        assert (n-3)-n*b*b*b==Fraction(3-2*n,(n-1)**3)
        assertions+=2
    print('PASS',assertions,'exact assertions')
    for n in (3,4,5,6,10):
        print(n,[str(theoretical(n,k)) for k in range(2,min(n,5)+1)])

if __name__=='__main__':run()
