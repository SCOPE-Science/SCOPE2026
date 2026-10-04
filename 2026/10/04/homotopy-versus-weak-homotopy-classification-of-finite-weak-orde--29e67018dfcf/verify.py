from itertools import combinations, product
from math import prod

def vertices(levels):
    return [(i,j) for i,r in enumerate(levels) for j in range(r)]

def leq(a,b):
    return a==b or a[0] < b[0]

def beat_points(levels):
    V=vertices(levels)
    out=[]
    for x in V:
        up=[y for y in V if x!=y and leq(x,y)]
        down=[y for y in V if x!=y and leq(y,x)]
        upmins=[y for y in up if not any(z!=y and leq(z,y) for z in up)]
        downmax=[y for y in down if not any(z!=y and leq(y,z) for z in down)]
        if len(upmins)==1 or len(downmax)==1:
            out.append(x)
    return out

def simplices(levels):
    bydim={}
    h=len(levels)
    for q in range(1,h+1):
        arr=[]
        for inds in combinations(range(h),q):
            for pts in product(*[range(levels[i]) for i in inds]):
                arr.append(tuple((i,p) for i,p in zip(inds,pts)))
        bydim[q-1]=arr
    return bydim

def rank_mod2(rows, ncols):
    rows=[sum(1<<j for j in row) for row in rows]
    r=0
    for c in range(ncols):
        pivot=next((i for i in range(r,len(rows)) if (rows[i]>>c)&1),None)
        if pivot is None: continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        for i in range(len(rows)):
            if i!=r and ((rows[i]>>c)&1): rows[i]^=rows[r]
        r+=1
    return r

def betti_mod2(levels):
    S=simplices(levels); h=len(levels)
    ranks={}
    for d in range(1,h):
        low={s:i for i,s in enumerate(S[d-1])}
        rows=[]
        for s in S[d]:
            rows.append([low[s[:j]+s[j+1:]] for j in range(len(s))])
        ranks[d]=rank_mod2(rows,len(S[d-1]))
    b=[]
    for d in range(h):
        nd=len(S[d]); rd=ranks.get(d,0); rnext=ranks.get(d+1,0)
        b.append(nd-rd-rnext)
    return b

def singleton_contraction(levels,j):
    assert levels[j]==1
    V=vertices(levels); c=(j,0)
    def u(x): return c if x[0]<=j else x
    # order preserving
    for x in V:
        for y in V:
            if leq(x,y): assert leq(u(x),u(y))
    assert all(leq(x,u(x)) for x in V)
    assert all(leq(c,u(x)) for x in V)

for levels in ([2,2],[3,3],[2,2,2],[2,4,2],[2,2,4],[3,2,3,2]):
    b=betti_mod2(levels)
    expected=prod(r-1 for r in levels)
    assert not beat_points(levels), (levels,beat_points(levels))
    assert b[:-1]==[1]+[0]*(len(levels)-2), (levels,b)
    assert b[-1]==expected, (levels,b,expected)
    print('NONCONTRACTIBLE', levels, 'betti=',b,'top_rank=',expected)
for levels,j in [([1],0),([1,3],0),([2,1,3],1),([2,3,1],2),([2,1,2,3],1)]:
    singleton_contraction(levels,j)
    print('SINGLETON_CONTRACTION',levels,'level',j)
# Explicit same weak type / different core data example.
a=[2,4,2]; b=[2,2,4]
assert len(a)==len(b) and prod(x-1 for x in a)==prod(x-1 for x in b)==3
assert a!=b
assert betti_mod2(a)==betti_mod2(b)==[1,0,3]
print('PAIR',a,b,'same_weak_signature=(3,3)','ordered_level_vectors_differ')
print('VERIFY_OK')
