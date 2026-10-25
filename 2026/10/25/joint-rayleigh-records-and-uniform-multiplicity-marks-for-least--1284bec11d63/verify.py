"""Exact and asymptotic arithmetic checks for least multiplicity-gap marks."""
from collections import Counter
from math import exp, pi, sqrt

def partition_numbers(N):
    p=[0]*(N+1)
    p[0]=1
    for n in range(1,N+1):
        k=1; total=0
        while k*(3*k-1)//2<=n:
            sign=1 if k%2 else -1
            a=k*(3*k-1)//2
            b=k*(3*k+1)//2
            total += sign*p[n-a]
            if b<=n: total +=sign*p[n-b]
            k+=1
        p[n]=total
    return p

def partitions(n, hi=None):
    if hi is None: hi=n
    if n==0:
        yield []
        return
    for x in range(min(n,hi),0,-1):
        for rest in partitions(n-x,x):
            yield [x]+rest

def gap(mults,s):
    m=1
    while mults.get(m,0)>=s: m+=1
    return m

def exact_mark_count(p,n,s,m,j):
    t=s*m*(m-1)//2+j*m
    return (p[n-t] if 0<=t<=n else 0)-(p[n-t-m] if 0<=t+m<=n else 0)

def exact_survival_count(p,n,rs,Ls):
    t=0
    for k in range(1,max(Ls,default=0)+1):
        t+=k*max((r for r,L in zip(rs,Ls) if k<=L),default=0)
    return p[n-t] if t<=n else 0

def exact_coincidence_count(p,n,r,s):
    tot=0
    for m in range(1,n+2):
        shift=s*m*(m-1)//2
        if shift>n:break
        a=p[n-shift]
        b=p[n-shift-r*m] if shift+r*m<=n else 0
        tot+=a-b
    return tot

def test():
    p=partition_numbers(16000)
    for n in range(0,27):
        enumerated=list(partitions(n))
        assert len(enumerated)==p[n],(n,len(enumerated),p[n])
        for s in range(1,5):
            counts=Counter()
            for part in enumerated:
                mults=Counter(part);m=gap(mults,s)
                counts[m,mults[m]]+=1
            assert sum(counts.values())==p[n]
            for m in range(1,n+2):
                for j in range(s):
                    assert counts[m,j]==exact_mark_count(p,n,s,m,j),(n,s,m,j)
        for rs,Ls in [([1,2],[1,1]),([1,3],[2,1]),([1,2,4],[2,1,1]),([2,3],[1,3])]:
            brute=sum(all(gap(Counter(x),r)>L for r,L in zip(rs,Ls)) for x in enumerated)
            assert brute==exact_survival_count(p,n,rs,Ls),(n,rs,Ls)
        for r,s in [(1,2),(1,3),(2,3),(1,4)]:
            brute=sum(gap(Counter(x),r)==gap(Counter(x),s) for x in enumerated)
            assert brute==exact_coincidence_count(p,n,r,s),(n,r,s)
    c=pi/sqrt(6)
    tests=[]
    for n in [1000,4000,16000]:
        coinc=float(exact_coincidence_count(p,n,1,3)/p[n]);target=1/3
        mark=[sum(exact_mark_count(p,n,3,m,j) for m in range(1,n+2) if 3*m*(m-1)//2+j*m<=n)/p[n] for j in range(3)]
        ls=[int(1.0*n**.25),int(1.7*n**.25)]
        surv=exact_survival_count(p,n,[1,3],ls)/p[n]
        x1=ls[0]/n**.25; x2=ls[1]/n**.25
        exponent=0.5*c*(x2*x2*3) if x2>x1 else None
        # x1 < x2, so event M1>x1 and M3>x2 is just M3>x2
        assert x2>=x1
        approx=exp(-c*3*x2*x2/2)
        tests.append((n,round(coinc,6),[round(z,6) for z in mark],round(surv,6),round(approx,6)))
    assert abs(tests[-1][1]-1/3)<0.03,tests[-1]
    assert max(abs(z-1/3) for z in mark)<0.03
    print('VERIFY_OK')
    for t in tests:print('n, coincidence(1,3), mark(3,j), survival(1,3), prediction:',t)
if __name__=='__main__':test()
