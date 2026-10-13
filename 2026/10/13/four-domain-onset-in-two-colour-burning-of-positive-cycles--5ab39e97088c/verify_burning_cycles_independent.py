#!/usr/bin/env python3
"""Independent recursive enumeration of positive-cycle two-colour burning outcomes.
Uses base-three encoded partial states and direct arithmetic influence to avoid BFS logic.
"""
from functools import lru_cache
from collections import Counter

def code(n):
    trit_to_colour=(0,1,-1)
    pow3=[3**i for i in range(n)]
    def unpack(code):
        return [(code//pow3[i])%3 for i in range(n)]
    @lru_cache(maxsize=None)
    def search(state):
        s=unpack(state)
        if all(s):
            return frozenset([tuple(trit_to_colour[x] for x in s)])
        s2=s.copy()
        for i,x in enumerate(s):
            if x==0:
                t=trit_to_colour[s[(i-1)%n]]+trit_to_colour[s[(i+1)%n]]
                s2[i]=1 if t>0 else 2 if t<0 else 0
        b=sum(s2[j]*pow3[j] for j in range(n))
        if all(s2):
            return frozenset([tuple(trit_to_colour[x] for x in s2)])
        answer=set()
        for i,x in enumerate(s2):
            if x==0:
                answer.update(search(b+pow3[i]))
                answer.update(search(b+2*pow3[i]))
        return frozenset(answer)
    return search(0),search.cache_info()

def main():
    for n in range(3,11):
        r,info=code(n)
        count=Counter(sum(w[i]!=w[(i+1)%n] for i in range(n)) for w in r)
        print(n,len(r),sorted(count.items()),'distinct_partial_states',info.currsize)
        assert count==({0:2} if n==3 else {0:2,2:8} if n==4 else {0:2,2:n*(n-1)} if n<=9 else {0:2,2:90,4:80})
    print('DFS_CERTIFIED')
if __name__=='__main__':main()
