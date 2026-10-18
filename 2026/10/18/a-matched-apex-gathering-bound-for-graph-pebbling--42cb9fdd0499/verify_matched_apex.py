"""Independent finite checks for the matched-apex pebbling bound.

Run: python3 verify_matched_apex.py
Standard library only. Vertices: hub 0, matching edges (1,2), (3,4), ... .
"""
from functools import lru_cache
from itertools import combinations


def compositions(n, total):
    for bars in combinations(range(total+n-1), n-1):
        xs=(-1,)+bars+(total+n-1,)
        yield tuple(xs[i+1]-xs[i]-1 for i in range(n))


def hub_construction(state):
    c=list(state)
    r=(len(c)-1)//2
    n=2*r+1
    assert sum(c)>=4*r
    def move(u,v):
        assert c[u]>=2
        assert u==0 or v==0 or (u-1)//2==(v-1)//2
        c[u]-=2
        c[v]+=1
    # All noncentral loads odd, zero center is the unique exceptional case.
    if c[0]==0 and all(c[v]%2 for v in range(1,n)):
        j=next(v for v in range(1,n) if c[v]>=3)
        k=j+1 if j%2 else j-1
        move(j,k)
        move(k,j)
    for v in range(1,n):
        while c[v]>=2:
            move(v,0)
    occupied=sum(any(c[v] for v in (2*i+1,2*i+2)) for i in range(r))
    assert c[0]>=occupied+1, (state,c)
    for i in range(r):
        a,b=2*i+1,2*i+2
        if c[a]==1 and c[b]==1:
            move(0,a)
            move(a,b)
            move(b,0)
        elif c[a]==1:
            move(0,a)
            move(a,0)
        elif c[b]==1:
            move(0,b)
            move(b,0)
    assert c[0]>=1 and all(x==0 for x in c[1:]), (state,c)
    return c[0]


def stackable(state):
    n=len(state)
    neighbors=[list(range(1,n))]+[
        [0,i+1 if i%2 else i-1] for i in range(1,n)]
    @lru_cache(None)
    def dfs(s):
        if sum(x>0 for x in s)==1:
            return True
        for u,count in enumerate(s):
            if count<2:continue
            for v in neighbors[u]:
                t=list(s);t[u]-=2;t[v]+=1
                if dfs(tuple(t)):
                    return True
        return False
    return dfs(tuple(state))


def main():
    for r in (1,2,3,4):
        count=0
        for state in compositions(2*r+1,4*r):
            hub_construction(state)
            count+=1
        obstruct=((1,1,1) if r==1 else (0,0,2*r+1)+tuple([1]*(2*r-2)))
        assert sum(obstruct)==4*r-1
        assert not stackable(obstruct)
        print('r=%d: %d configurations constructively stacked at hub; '
              'specified size-%d configuration nonstackable'
              % (r,count,4*r-1))
    print('PASS')

if __name__=='__main__':
    main()
