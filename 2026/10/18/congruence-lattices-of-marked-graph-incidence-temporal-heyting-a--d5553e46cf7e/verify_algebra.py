#!/usr/bin/env python3
"""Second route: count compatible elements of the explicit temporal Heyting algebra."""
from verify_archival import predicted


def count_compatible(n, edges, flags, vertex_flags=0):
    N = n + len(edges)
    full = (1 << N) - 1
    up = []
    for subset in range(1 << N):
        if all(not (subset & (1 << u)) or (subset & (1 << (n+k)))
               for k,(u,v) in enumerate(edges)) and all(
               not (subset & (1 << v)) or (subset & (1 << (n+k)))
               for k,(u,v) in enumerate(edges)):
            up.append(subset)
    # backward existential diamond applied to an upset
    def diamond(s):
        out = 0
        for k,(u,v) in enumerate(edges):
            if (s >> u) & 1 or (s >> v) & 1 or ((flags >> k) & 1 and (s >> (n+k)) & 1):
                out |= (1 << (n+k))
        for u in range(n):
            if (vertex_flags >> u) & 1 and (s >> u) & 1:
                out |= (1 << u)
        return out
    image = {s:diamond(s) for s in up}
    count=0
    for a in up:
        if all((a & image[b]) & ~(image[a & b]) == 0 for b in up):
            count += 1
    return len(up),count

if __name__=='__main__':
    inputs=[(3,[(0,1),(1,2)]),(3,[(0,1),(1,2),(0,2)]),(4,[(0,1),(1,2),(2,3)]),(4,[(0,1),(1,2),(2,3),(0,3)])]
    for n,edges in inputs:
        for flags in range(1 << len(edges)):
            nup,actual=count_compatible(n,edges,flags)
            expect=predicted(n,edges,flags)
            if actual != expect:
                raise AssertionError((n,edges,flags,nup,actual,expect))
        print('PASS',n,'vertices',len(edges),'edges','all',1<<len(edges),'edge-reflexivity patterns',flush=True)
    for n,edges in inputs[:2]:
        for flags in range(1 << len(edges)):
            for vertex_flags in range(1 << n):
                nup,actual=count_compatible(n,edges,flags,vertex_flags)
                expect=predicted(n,edges,flags)
                if actual != expect:
                    raise AssertionError(('vertex flag mismatch',n,edges,flags,vertex_flags,nup,actual,expect))
        print('PASS',n,'all vertex-loop patterns',flush=True)
