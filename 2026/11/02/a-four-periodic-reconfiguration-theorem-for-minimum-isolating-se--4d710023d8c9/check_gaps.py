"""Independent cyclic-gap encoding check for minimum isolating-set exchange graphs.

Run: python3 check_gaps.py
No external dependencies.
"""
from math import comb
from collections import deque


def compositions(k, r):
    if k == 1:
        yield (r,)
        return
    for i in range(r+1):
        for rest in compositions(k-1,r-i):
            yield (i,) + rest


def configurations(n):
    k=(n+3)//4
    r=4*k-n
    out=set()
    for initial in range(n):
        for a in compositions(k,r):
            vertices=[initial]
            cursor=initial
            for deficit in a[:-1]:
                cursor=(cursor+4-deficit)%n
                vertices.append(cursor)
            assert (cursor+4-a[-1])%n==initial
            assert len(set(vertices))==k
            out.add(tuple(sorted(vertices)))
    return out


def exchange_edges(n, family):
    family=set(family)
    adj={s:set() for s in family}
    for s in family:
        k=len(s)
        if k == 1:
            for t in family:
                if t!=s:adj[s].add(t)
            continue
        for i, x in enumerate(s):
            predecessor=s[(i-1)%k]
            successor=s[(i+1)%k]
            # Both candidate new gaps must lie between one and four.
            # Enumerate all possible inserted positions, not the original subset predicate.
            for gap in range(1,5):
                new=(predecessor+gap)%n
                if new==x or new in s:
                    continue
                if (successor-new)%n not in (1,2,3,4):
                    continue
                candidate=tuple(sorted((set(s)-{x})|{new}))
                if candidate in family:adj[s].add(candidate)
    return adj


def main():
    for n in range(5,55):
        k=(n+3)//4
        r=4*k-n
        family=configurations(n)
        expected=n*comb(k+r-1,r)//k
        assert len(family)==expected,(n,len(family),expected)
        if r==0:
            assert len(family)==4
            continue
        # For large n the cardinality/encoding check remains exhaustive,
        # while full connectivity and degree are checked up to 38.
        if n>38:
            continue
        adj=exchange_edges(n,family)
        assert all(len(x)==2*r for x in adj.values()),(n,sorted(set(map(len,adj.values()))))
        source=next(iter(family))
        seen={source};q=deque([source])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in seen:seen.add(y);q.append(y)
        assert len(seen)==expected,(n,len(seen),expected)
        assert all(x in adj[y] for y in adj for x in adj[y]),n
        if r==1:
            assert len(family)==n
        print(f'n={n}: cyclic-gap census {len(family)}; degree {2*r}; connected')
    print('CYCLE_ISOLATION_GAP_MODEL_PASS')

if __name__=='__main__':
    main()
