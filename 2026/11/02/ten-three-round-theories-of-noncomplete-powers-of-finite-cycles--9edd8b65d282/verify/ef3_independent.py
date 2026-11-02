#!/usr/bin/env python3
"""Direct three-round two-sided EF game solver; no transitivity assumption."""
from functools import lru_cache
from itertools import combinations

def edges(n,r):
    return tuple(tuple(a!=b and min((a-b)%n,(b-a)%n)<=r for b in range(n)) for a in range(n))

def ef3(a,b):
    na, nb=len(a),len(b)
    @lru_cache(None)
    def win(t1,t2):
        for i in range(len(t1)):
            for j in range(len(t1)):
                if (t1[i]==t1[j])!=(t2[i]==t2[j]) or a[t1[i]][t1[j]] != b[t2[i]][t2[j]]:
                    return False
        if len(t1)==3: return True
        # Spoiler may play on either side, at every remaining move.
        for u in range(na):
            if not any(win(t1+(u,),t2+(v,)) for v in range(nb)): return False
        for v in range(nb):
            if not any(win(t1+(u,),t2+(v,)) for u in range(na)): return False
        return True
    return win((),()),win.cache_info()

def main():
    reps = [(4,1),(5,1),(6,1),(7,1), (6,2),(7,2),(8,2),(9,2),(10,2),(11,2)]
    for i,j in combinations(range(10),2):
        w,_=ef3(edges(*reps[i]),edges(*reps[j]))
        assert not w, ('indistinguishable classes',reps[i],reps[j])
    print('45 DIFFERENT CLASS PAIRS: SPOILER WINS ALL')
    equals=[((7,1),(8,1)),((11,2),(12,2)),((11,2),(15,3)),((15,3),(19,4))]
    for p,q in equals:
        w,stats=ef3(edges(*p),edges(*q))
        assert w,(p,q)
        print('EQUIVALENT:',p,q,'states',stats.currsize)
    print('INDEPENDENT_EF3_CHECK_PASS')
if __name__=='__main__':main()
