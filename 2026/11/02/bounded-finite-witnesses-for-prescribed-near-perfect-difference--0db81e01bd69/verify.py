"""Finite checks for a theorem on prescribed positive-difference counts."""
from collections import Counter
from itertools import combinations
from random import Random


def diffs(points):
    return Counter(b-a for a,b in combinations(sorted(points),2))


def extend(seed, upto):
    a=set(seed)
    for u in range(1,upto+1):
        before=diffs(a)
        if before[u]:
            continue
        m=max(a)
        x=2*m+u+1
        a.update((x,x+u))
        after=diffs(a)
        assert after[u] == 1
        for v,count in before.items():
            assert after[v] == count
        assert all(count <= 1 for v,count in after.items() if not before[v])
    return a


def compress(seed, allowed):
    m=max(allowed)
    old=diffs(seed)
    R=sum(old[s] for s in allowed)
    W=2*R*m
    H=4*W+m+1
    adj={x:set() for x in seed}
    for a,b in combinations(sorted(seed),2):
        if b-a in allowed:
            adj[a].add(b);adj[b].add(a)
    components=[]
    seen=set()
    for x in sorted(seed):
        if x in seen: continue
        q=[x];seen.add(x);part=[]
        while q:
            z=q.pop();part.append(z)
            for y in adj[z]:
                if y not in seen:seen.add(y);q.append(y)
        components.append(part)
    out=[]
    for i,comp in enumerate(components):
        z=min(comp)
        out.extend(H*4**i+(x-z) for x in comp)
    return set(out), H*4**(2*R)+W+1


def run():
    for u in (1,2,5,11):
        seed={1,1+u,1+2*u}
        for bound in (8,14,25):
            out=extend(seed,bound)
            ds=diffs(out)
            for v in range(1,bound+1):
                assert ds[v] == (2 if v==u else 1)
    rnd=Random(2402)
    examples=0
    for _ in range(500):
        # Produce a finite seed with at most one collision outside S.
        pts={1}
        for j in range(rnd.randrange(3,10)):
            pts.add(rnd.randrange(2,40))
        before=diffs(pts)
        S={s for s,v in before.items() if v>1}
        if not S:
            continue
        # Allowed S includes every repeated difference, and add a random extra.
        if rnd.randrange(2): S.add(rnd.choice(list(before)))
        out,B=compress(pts,S)
        assert max(out)<=B
        after=diffs(out)
        assert all(after[s]==before[s] for s in S)
        assert all(after[d]<=1 for d in after if d not in S)
        examples+=1
    exhaustive=0
    for mask in range(1,1<<10):
        seed={i+1 for i in range(10) if (mask>>i)&1}
        if len(seed)<3:continue
        old=diffs(seed)
        S={d for d,n in old.items() if n>1}
        if not S:continue
        new,B=compress(seed,S)
        after=diffs(new)
        assert max(new)<=B
        assert all(after[s]==old[s] for s in S)
        assert all(n<=1 for d,n in after.items() if d not in S)
        exhaustive+=1
    print('VERIFY_OK singleton_shifts=4 target_bounds=8,14,25 compressed_random_finite_seeds=',examples,'exhaustive_10point_seeds=',exhaustive)

if __name__ == '__main__':
    run()
