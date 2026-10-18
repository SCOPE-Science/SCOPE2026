#!/usr/bin/env python3
"""Independent signed integral chain cancellation for four bidirected
complete-bipartite multipath complexes. Uses only Python standard library.
"""
from collections import Counter,defaultdict
from itertools import combinations
from functools import reduce
from math import gcd

EXPECTED={3:(1,6,0),4:(8,1,2),5:(1,32,2),6:(0,169,0)}

def faces(n):
    arcs=[]
    for i in range(n):
        arcs += [(0,i+2),(i+2,0),(1,i+2),(i+2,1)]
    result=[()]
    for k in range(1,5):
        for s in combinations(range(4*n),k):
            E=[arcs[v] for v in s]
            if len(set(u for u,v in E))!=k or len(set(v for u,v in E))!=k:continue
            succ=dict(E)
            cyclic=False
            for x in succ:
                seen=set()
                while x in succ:
                    if x in seen:
                        cyclic=True;break
                    seen.add(x);x=succ[x]
                if cyclic:break
            if not cyclic:result.append(s)
    return result

def pairs(faces,n):
    unpaired=set(faces)
    match=[]
    for j in range(4):
        for i in range(n):
            v=4*i+j
            for f in sorted(unpaired):
                if v in f:continue
                bigger=tuple(sorted(f+(v,)))
                if bigger in unpaired:
                    match.append((f,bigger))
                    unpaired.remove(f);unpaired.remove(bigger)
    return match,unpaired

def homology_by_cancel(n):
    F=faces(n);P,crit=pairs(F,n)
    boundary={}
    for f in F:
        boundary[f]={f[:i]+f[i+1:]:(1 if i%2==0 else -1) for i in range(len(f))} if f else {}
    active=set(F)
    # Actual chain cancellation with integer coefficients. The gradient
    # pairs are cancelled independently of the projection method.
    for low,upper in sorted(P,key=lambda ab:(len(ab[0]),ab[0])):
        assert low in active and upper in active
        pivot=boundary[upper].get(low,0)
        assert abs(pivot)==1,(n,low,upper,pivot)
        for high in list(active):
            if high==upper or len(high)!=len(upper):continue
            a=boundary[high].get(low,0)
            if not a:continue
            multiplier=a//pivot
            for face,coeff in boundary[upper].items():
                value=boundary[high].get(face,0)-multiplier*coeff
                if value:boundary[high][face]=value
                else:boundary[high].pop(face,None)
        for high in list(active):
            if len(high)==len(upper)+1:
                boundary[high].pop(upper,None)
        active.remove(low);active.remove(upper)
    assert active==crit
    for f in crit:
        assert all(g in crit for g in boundary[f])
    for f in crit:
        for g in boundary[f]:
            for h,b in boundary[g].items():
                assert sum(a*boundary[g].get(h,0) for g,a in boundary[f].items())==0
    k=1 if n==3 else 2
    lowers=sorted(f for f in crit if len(f)==k+1)
    uppers=sorted(f for f in crit if len(f)==k+2)
    mat=[[boundary[b].get(a,0) for b in uppers] for a in lowers]
    values=[abs(v) for row in mat for v in row]
    content=reduce(gcd,values,0)
    assert (len(lowers),len(uppers),content)==EXPECTED[n]
    print('CANCEL_OK',n,'faces',len(F),'pairs',len(P),'critical',(len(lowers),len(uppers)),
          'matrix_content',content,'matrix_nonzeros',sum(x!=0 for row in mat for x in row))
    return mat

if __name__=='__main__':
    for n in sorted(EXPECTED):homology_by_cancel(n)
