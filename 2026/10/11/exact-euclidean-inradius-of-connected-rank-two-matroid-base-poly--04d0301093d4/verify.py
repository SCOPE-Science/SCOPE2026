from decimal import Decimal, getcontext
getcontext().prec = 60
D=Decimal

def parts(n, lo=1):
    if n==0:
        yield (); return
    for a in range(lo,n+1):
        for tail in parts(n-a,a): yield (a,)+tail

def data(h):
    n=sum(h); dn=D(n)
    A=(D(n-1)/dn).sqrt()
    B=[(D(x*(n-x))/dn).sqrt() for x in h]
    return n,A,B

def closed(h,A,B):
    n=sum(h)
    r1=D(2)/(D(n)*D(n-1)).sqrt()
    r2=D(len(h)-2)/sum(B)
    r3=min(D(1)/(D(x)*A+b) for x,b in zip(h,B))
    return min(r1,r2,r3)

def feasible(h,A,B,r):
    tol=D('1e-50')
    lows=[D(x)*r*A for x in h]
    highs=[D(1)-r*b for b in B]
    return all(l<=u+tol for l,u in zip(lows,highs)) and sum(lows)<=D(2)+tol and D(2)<=sum(highs)+tol

def numeric(h,A,B):
    lo=D(0); hi=D(1)
    for _ in range(170):
        m=(lo+hi)/2
        if feasible(h,A,B,m): lo=m
        else: hi=m
    return lo

def construct(h,A,B,r):
    lows=[D(x)*r*A for x in h]; highs=[D(1)-r*b for b in B]
    t=lows[:]; rem=D(2)-sum(t)
    for j in range(len(t)):
        add=min(rem,max(D(0),highs[j]-t[j])); t[j]+=add; rem-=add
    assert abs(rem)<D('1e-40')
    return t

count=0
for n in range(3,25):
    for h in parts(n):
        if len(h)<3: continue
        _,A,B=data(h); r=closed(h,A,B); q=numeric(h,A,B)
        if abs(r-q)>D('1e-40'): raise AssertionError((h,r,q))
        if not feasible(h,A,B,r): raise AssertionError(('infeasible',h,r))
        construct(h,A,B,r); count+=1
print(f'VERIFY_OK rank-two-matroid inradius partitions={count} max_n=24')
