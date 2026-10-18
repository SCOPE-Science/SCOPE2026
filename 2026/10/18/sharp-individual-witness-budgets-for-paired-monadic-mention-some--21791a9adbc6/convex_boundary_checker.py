from collections import Counter
from math import comb
for n in range(1,5):
    N=1<<n
    rank=Counter()
    for C in range(1,1<<N):
        f=[v for v in range(N) if (C>>v)&1]
        is_convex=True
        for a in f:
            if not is_convex: break
            for b in f:
                if a&b==a:
                    for z in range(N):
                        if (a&z)==a and (z&b)==z and not ((C>>z)&1):
                            is_convex=False;break
                if not is_convex:break
        if not is_convex: continue
        small=[x for x in f if not any(y!=x and (y&x)==y for y in f)]
        large=[x for x in f if not any(y!=x and (y&x)==x for y in f)]
        rank[len(set(small+large))]+=1
    assert max(rank)<=comb(n,n//2)+comb(n,n//2+1)
    print(n,sorted(rank.items()),sum(rank.values()),flush=True)
