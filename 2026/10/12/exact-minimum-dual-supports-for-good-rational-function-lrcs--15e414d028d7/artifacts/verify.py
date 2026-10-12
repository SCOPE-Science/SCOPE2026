#!/usr/bin/env python3
import itertools, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

def inv(a,p):
    return pow(a%p,-1,p)

def rank_mod(rows,p):
    A=[[(x%p) for x in row] for row in rows]
    if not A:
        return 0
    m=len(A); n=len(A[0]); rr=0
    for c in range(n):
        piv=next((i for i in range(rr,m) if A[i][c]%p),None)
        if piv is None:
            continue
        A[rr],A[piv]=A[piv],A[rr]
        z=inv(A[rr][c],p)
        A[rr]=[(z*x)%p for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]%p:
                a=A[i][c]%p
                A[i]=[(u-a*v)%p for u,v in zip(A[i],A[rr])]
        rr+=1
        if rr==m:
            break
    return rr

def uvec(x,r,p):
    if x is None:
        return [0]*(r-1)+[1]
    return [pow(x,i,p) for i in range(r)]

def columns_from_fibers(p,r,t,groups,ds):
    cols=[]
    for group,d in zip(groups,ds):
        for x in group:
            u=uvec(x,r,p)
            col=[]
            for j in range(t):
                dj=pow(d,j,p)
                col.extend((dj*a)%p for a in u)
            cols.append(col)
    return cols

def subset_rank(cols,S,p):
    # columns -> transpose to rows for row reduction
    return rank_mod([[cols[j][i] for j in S] for i in range(len(cols[0]))],p)

def check_case(p,r,t,groups,ds,label):
    cols=columns_from_fibers(p,r,t,groups,ds)
    n=len(cols); k=r*t
    assert rank_mod([[c[i] for c in cols] for i in range(k)],p)==k
    for s in range(1,r+1):
        for S in itertools.combinations(range(n),s):
            assert subset_rank(cols,S,p)==s, (label,'small dependent',S)
    deps=[]
    for S in itertools.combinations(range(n),r+1):
        if subset_rank(cols,S,p)<r+1:
            assert subset_rank(cols,S,p)==r
            deps.append(tuple(S))
    want=[]; off=0
    for g in groups:
        want.append(tuple(range(off,off+len(g))))
        off+=len(g)
    assert set(deps)==set(want),(label,deps,want)
    assert len(deps)*(p-1)==len(groups)*(p-1)
    return {'label':label,'n':n,'k':k,'dual_min_distance':r+1,'minimum_supports':len(deps),'minimum_dual_words':len(deps)*(p-1)}

# Exact source instance from Proposition 5.5 with q=11, w=1:
# h(x)=(x^3-3x+1)/(x(x-1)).  Its four full fibers on P^1(F_11)
# are recovered directly; b=0 is not in the image.
p=11
def h11(x):
    if x is None or x in (0,1):
        return None
    return ((x**3-3*x+1)*inv(x*(x-1),p))%p
fib={}
for x in list(range(p))+[None]:
    fib.setdefault(h11(x),[]).append(x)
assert sorted(len(v) for v in fib.values())==[3,3,3,3]
assert 0 not in fib
ordered_t=[None,5,7,9]
groups=[fib[tv] for tv in ordered_t]
ds=[0 if tv is None else inv(tv,p) for tv in ordered_t]
case1=check_case(11,2,2,groups,ds,'source_q11_degree3')
assert case1==CERT['expected']['source_q11_degree3']

# A second exact fiber-Vandermonde instance exercises r=3 and the infinity column.
groups2=[[None,0,1,2],[3,4,5,6],[7,8,9,10]]
case2=check_case(13,3,2,groups2,[3,5,7],'fiber_vandermonde_q13_r3')
assert case2==CERT['expected']['fiber_vandermonde_q13_r3']

# The excluded boundary t=1 is genuinely different: every four-subset is dependent,
# not only the designated fibers.
cols=columns_from_fibers(13,3,1,groups2,[3,5,7])
deps=sum(subset_rank(cols,S,13)<4 for S in itertools.combinations(range(len(cols)),4))
assert deps>len(groups2)

print('VERIFY_OK source_q11=4_fibers_40_minwords q13_r3=3_fibers_36_minwords t1_boundary=nonunique')
