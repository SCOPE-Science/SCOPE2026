"""Finite verification for projection-visibility rigidity and its census.

Public, standalone Python 3 script. This is corroboration, not an infinite proof.
"""
from itertools import combinations
from functools import lru_cache
from math import comb

@lru_cache(None)
def stirling(n,j):
    if n==j==0: return 1
    if n==0 or j==0 or j>n: return 0
    return j*stirling(n-1,j)+stirling(n-1,j-1)

def sig(t,k,r):
    ans=[]
    for J in combinations(range(k),r):
        x=0
        for v in t:
            p=sum(((v>>i)&1)<<j for j,i in enumerate(J))
            x |= 1 << p
        ans.append(x)
    return tuple(ans)

def invisible(t,v,k,r):
    return sig(t,k,r)==sig((*t,v),k,r)

def predicted(t,v,k,r):
    supports=[{i for i in range(k) if (u^v)&(1<<i)} for u in t]
    return (len(t)==r+1 and all(supports) and
            all(a.isdisjoint(b) for a,b in combinations(supports,2)))

def check(k,r):
    universe=range(1<<k)
    checked=0; ghostpairs=0; minteams=0
    for sz in range(r+2):
        for t in combinations(universe,sz):
            ghosts=[]
            for v in universe:
                if v in t: continue
                actual=invisible(t,v,k,r)
                if sz<=r: assert not actual, (k,r,t,v)
                if sz==r+1:
                    assert actual==predicted(t,v,k,r),(k,r,t,v,actual)
                if actual: ghosts.append(v);ghostpairs+=1
                checked+=1
            if sz==r+1 and ghosts:
                minteams+=1
                if r>=2:assert len(ghosts)==1,(k,r,t,ghosts)
    expected=(1<<k)*(stirling(k,r+1)+(r+2)*stirling(k,r+2))
    assert ghostpairs==expected,(k,r,ghostpairs,expected)
    if r>=2:assert minteams==expected,(k,r,minteams,expected)
    return checked,ghostpairs,minteams

if __name__=='__main__':
    total=0
    for k in range(2,5):
        for r in range(1,k):
            ch,g,t=check(k,r)
            total+=ch
            print(f'k={k} r={r} comparisons={ch} hidden_pairs={g} minimal_teams={t}')
    print('PROJECTION_VISIBILITY_VERIFY_OK comparisons=',total)
