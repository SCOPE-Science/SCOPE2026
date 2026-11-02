"""Independent exact finite-backtracking recurrence for online dimension on 2-row ladders."""
from functools import lru_cache

def tilings(n):
    def rec(i,mask):
        if i>=n:
            yield mask
        else:
            yield from rec(i+1,mask)
            if i+1<n:
                yield from rec(i+2,mask|(1<<i))
    return tuple(rec(0,0))

def ld(n):
    patterns=tilings(n)
    nb=len(patterns)
    all_h=(1<<nb)-1
    yes=[]
    for i in range(n):
        yes.append(sum(1<<j for j,bits in enumerate(patterns)
            if not((i and bits&(1<<(i-1))) or (i<n-1 and bits&(1<<i)))))
    for i in range(n-1):
        yes.append(sum(1<<j for j,bits in enumerate(patterns) if bits&(1<<i)))
    @lru_cache(None)
    def rank(pool):
        optimum=0
        for q in yes:
            one=pool&q
            zero=pool^one
            if one and zero:
                optimum=max(optimum,1+min(rank(one),rank(zero)))
        return optimum
    return nb,rank(all_h)

expected=((1,0),(2,1),(3,1),(5,2),(8,3),(13,3),(21,4),(34,5),(55,5),(89,6),(144,7))
observed=tuple(ld(n) for n in range(1,12))
assert observed==expected,(observed,expected)
print('FINITE_ONLINE_RECURRENCE_PASS',observed)
