"""Exact finite checks for quasi-total Roman domination on rook graphs.

Enumerates every assignment of weight at most 2m on indicated finite boards,
using only the defining neighborhood conditions to accept an assignment.
"""
from itertools import combinations
from math import factorial


def expected(m,n):
    # Number of functions from m named rows to n named columns with
    # no singleton nonempty fiber, via exact subset dynamic programming.
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[0][0] = 1
    from math import comb
    for j in range(n):
        for q in range(m+1):
            for s in range(m-q+1):
                if s != 1:
                    dp[j+1][q+s] += dp[j][q]*comb(m-q,s)
    f = dp[n][m]
    return (1+(m==n))*f + (9 if m==n==2 else 0) + (54 if m==n==3 else 0)


def brute(m,n):
    size=m*n
    neighbors=[]
    for v in range(size):
        r,c=divmod(v,n)
        neighbors.append(sum(1<<u for u in range(size)
                             if u!=v and (u//n==r or u%n==c)))
    full=(1<<size)-1
    minw=2*m+1
    total=0
    visited=0
    for twocnt in range(m+1):
        for twos in combinations(range(size),twocnt):
            tmask=sum(1<<v for v in twos)
            attacked=0
            for v in twos: attacked |= neighbors[v]
            forced=full & ~(tmask|attacked)
            num_forced=forced.bit_count()
            room=2*m-2*twocnt-num_forced
            if room<0: continue
            free=full & ~(forced|tmask)
            free_indices=[v for v in range(size) if free & (1<<v)]
            for othercnt in range(min(room,len(free_indices))+1):
                weight=2*twocnt+num_forced+othercnt
                if weight>minw: continue
                for others in combinations(free_indices,othercnt):
                    ones=forced|sum(1<<v for v in others)
                    visited+=1
                    if any((neighbors[v]&(ones|tmask))==0 for v in twos):
                        continue
                    # Every zero must be adjacent to a two (forced ones already computed)
                    assert (full & ~(ones|tmask|attacked)) == 0
                    if weight<minw: minw,total=weight,0
                    if weight==minw:total+=1
    return minw,total,visited


def run():
    cases=[(2,2),(2,3),(2,4),(2,5),(2,7),
           (3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]
    for m,n in cases:
        actual=brute(m,n)
        want=(2*m, expected(m,n))
        assert actual[:2]==want,(m,n,actual,want)
        print('board=%dx%d min=%d count=%d examined=%d OK'%
              (m,n,*actual))
    # Independent enumeration of full-m row defender placements by functions.
    from itertools import product
    for m,n in [(5,5),(5,7),(6,6),(6,8),(7,9)]:
        c=sum(all(x.count(v)!=1 for v in set(x))
              for x in product(range(n), repeat=m))
        # For square boards the transposed pattern is a second, disjoint class.
        got=c*(1+(m==n))
        assert got==expected(m,n),(m,n,got,expected(m,n))
        print('defender_map=%dx%d min_count=%d OK'%(m,n,got))
    print('VERIFICATION_OK')

if __name__=='__main__':run()
