"""Finite-field incidence checks for a root-of-unity edge-point configuration.
These are sanity checks, not the infinite-characteristic-zero proof.
"""
from itertools import combinations
from math import comb

def primitive_roots(d,p):
    return [x for x in range(1,p) if pow(x,d,p)==1]

def normalize(v,p):
    pos=next(i for i,x in enumerate(v) if x%p)
    t=pow(v[pos],-1,p)
    return tuple(x*t%p for x in v)

def minor_signature(a,b,p):
    sig=[(a[i]*b[j]-a[j]*b[i])%p for i in range(len(a)) for j in range(i+1,len(a))]
    return normalize(sig,p)

def check(r,d,p):
    roots=primitive_roots(d,p)
    assert len(roots)==d
    points=[]
    for i,j in combinations(range(r),2):
        for z in roots:
            v=[0]*r
            v[i]=1;v[j]=(-z)%p
            points.append(tuple(v))
    line_classes={}
    for a,b in combinations(points,2):
        line_classes[minor_signature(a,b,p)]= (a,b)
    rich=[]
    other_max=0
    for a,b in line_classes.values():
        sig=minor_signature(a,b,p)
        count=0
        for x in points:
            # all 3x3 minors must vanish
            if all((a[i]*(b[j]*x[k]-b[k]*x[j])-a[j]*(b[i]*x[k]-b[k]*x[i])+a[k]*(b[i]*x[j]-b[j]*x[i]))%p==0 for i,j,k in combinations(range(r),3)):
                count+=1
        if count>=d: rich.append(count)
        else: other_max=max(other_max,count)
    assert len(rich)==comb(r,2),(r,d,p,rich)
    assert all(x==d for x in rich),(r,d,rich)
    assert other_max<=3,(r,d,other_max)
    print(f'PASS r={r}, d={d}, p={p}: N={len(points)}; rich={len(rich)}, sizes={set(rich)}, other_max={other_max}')

if __name__=='__main__':
    for triple in [(3,4,17),(4,4,17),(5,4,17),(3,5,11),(4,5,11),(4,6,13)]:
        check(*triple)
    print('VERIFIED')
