#!/usr/bin/env python3
"""Exact checks of a cyclic root-of-unity filling of bipartite parity-check masks."""
from itertools import combinations, permutations

def mul(a,b,poly=0b1011):
    out=0
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&8: a^=poly
    return out

def inv(a):
    assert a
    for x in range(1,8):
        if mul(x,a)==1:return x
    raise AssertionError

def rank(rows,nc):
    rows=rows[:]
    cur=0
    for c in range(nc):
        pos=next((i for i in range(cur,len(rows)) if rows[i][c]),None)
        if pos is None:continue
        rows[cur],rows[pos]=rows[pos],rows[cur]
        piv=inv(rows[cur][c])
        rows[cur]=[mul(piv,z) for z in rows[cur]]
        for j in range(len(rows)):
            if j!=cur and rows[j][c]:
                factor=rows[j][c]
                rows[j]=[x^mul(factor,y) for x,y in zip(rows[j],rows[cur])]
        cur+=1
        if cur==len(rows):break
    return cur

def main():
    pow7=[1]
    for i in range(6):pow7.append(mul(pow7[-1],2))
    assert len(set(pow7))==7 and mul(pow7[-1],2)==1
    assert pow7 == [1,2,4,3,6,7,5]
    for r,s in [(3,3),(3,7),(6,6),(7,7)]:
        lambdas=[[pow7[(i*j)%7] for j in range(s)] for i in range(r)]
        for i,k in combinations(range(r),2):
            for j,l in combinations(range(s),2):
                assert mul(lambdas[i][j],lambdas[k][l]) != mul(lambdas[i][l],lambdas[k][j])
        cols=[]
        for i in range(r):
            for j in range(s):
                c=[0]*(r+s)
                c[i]=1;c[r+j]=lambdas[i][j]
                cols.append(c)
        matrix=[[c[t] for c in cols] for t in range(r+s)]
        assert rank(matrix,r*s)==r+s
        print('GF8 dimensions',r,s,'rank',r+s,'all nonzero four-cycle minors', flush=True)
    r=s=6
    rows=[[0]*(r*s) for _ in range(r+s)]
    for i in range(r):
        for j in range(s):
            rows[i][i*s+j]=1
            rows[r+j][i*s+j]=pow7[i*j%7]
    # Every two to five edge columns independent (exhaustive 443,703 subsets).
    counts=[]
    for t in range(1,6):
        tested=0
        for inds in combinations(range(r*s),t):
            # No leaf pruning: direct full finite-field Gaussian elimination in dimension t.
            arr=[[rows[k][a] for a in inds] for k in range(r+s)]
            if rank(arr,t)!=t:
                raise AssertionError(('dependent set <= 5', inds))
            tested+=1
        counts.append(tested)
        print('exhaustive subset size',t,'count',tested,flush=True)
    six=[0,1,2,6,7,8]
    assert rank([[rows[k][a] for a in six] for k in range(12)],6)==5
    group=set(range(1,7))
    inverses={x:pow(x,-1,7) for x in group}
    # Normalizing the first two left rows, all possible third-row permutations
    # contradict the required third quotient permutation.
    possible=0
    for perm in permutations(range(1,7)):
        if {perm[j]*inverses[j+1]%7 for j in range(6)}==group:
            possible+=1
    assert possible==0
    print('VALIDATED K66',counts,'six-edge dependent circuit, GF7 720-permutation obstruction; VERIFY_OK')

if __name__=='__main__':main()
