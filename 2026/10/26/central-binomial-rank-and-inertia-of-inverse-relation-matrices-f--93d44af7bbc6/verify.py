"""Standalone check of finite chain order-preserving inverse-relation identities.
No optional packages required. Exact rank uses rational Gaussian elimination.
"""
from itertools import combinations, combinations_with_replacement
from math import comb, prod

def parts(n,r):
    for cuts in combinations(range(1,n),r-1):
        bs=(0,)+cuts+(n,)
        yield tuple(tuple(range(bs[j],bs[j+1])) for j in range(r))

def maps(n):return list(combinations_with_replacement(range(n),n))
def comp(f,g):return tuple(f[g[i]] for i in range(len(f)))
def rank(f):return len(set(f))
def partner(f,g):return comp(f,comp(g,f))==f and comp(g,comp(f,g))==g

def exact_rank(a):
    if not a:return 0
    a=[list(map(int,row)) for row in a]
    # Bareiss elimination with integer row operations; if pivot p, use p*row_i - a[i][j]*row_pivot
    m,n=len(a),len(a[0]); row=0
    for j in range(n):
        i=next((i for i in range(row,m) if a[i][j]),None)
        if i is None:continue
        a[row],a[i]=a[i],a[row]
        p=a[row][j]
        for k in range(row+1,m):
            if a[k][j]:
                q=a[k][j]
                for l in range(j+1,n):a[k][l]=p*a[k][l]-q*a[row][l]
                a[k][j]=0
        row+=1
        if row==m:break
    return row

def check(n):
    funcs=maps(n)
    assert len(funcs)==comb(2*n-1,n)
    for r in range(1,n+1):
        p=list(parts(n,r)); q=list(combinations(range(n),r))
        M=[[int(all(len(set(v)&set(block))==1 for block in bs)) for v in q] for bs in p]
        assert exact_rank(M)==len(p)
        farr=[f for f in funcs if rank(f)==r]
        assert len(farr)==len(p)*len(q)
        d={f:i for i,f in enumerate(farr)}
        nind=0
        for f in farr:
            values=tuple(sorted(set(f)))
            blocks=tuple(tuple(i for i in range(n) if f[i]==y) for y in values)
            k=p.index(blocks);i=q.index(values)
            assert f==tuple(values[next(j for j,B in enumerate(blocks) if t in B)] for t in range(n))
            d_expected=prod(len(B) for B in blocks)*prod(values[j+1]-values[j] for j in range(r-1))
            cnt=0
            for g in farr:
                G=tuple(sorted(set(g)))
                C=tuple(tuple(t for t in range(n) if g[t]==y) for y in G)
                actual=partner(f,g)
                predicted=bool(M[k][q.index(G)] and M[p.index(C)][i])
                assert actual==predicted,(n,r,f,g)
                cnt+=actual
            assert cnt==d_expected,(n,r,f,cnt,d_expected)
            nind+=cnt
        t=comb(n+r-1,2*r-1)
        assert nind==t*t,(n,r,nind,t*t)
        idem=sum(1 for f in farr if comp(f,f)==f)
        assert idem==t,(n,r,idem,t)
        print(f'n={n} r={r} |R|={len(farr)} rank(M)={len(p)} edges_oriented={nind} trace={idem}',flush=True)
for n in range(1,6):check(n)
print('VERIFY_OK')
