#!/usr/bin/env python3
"""Independent exact-cover enumeration on the vertex neighborhoods of C8 square Ct.

No column transfer recurrence is used. Each chosen vertex covers precisely
its four neighbors, and the selected neighborhoods must partition the torus.
"""
from collections import Counter

def find_codes(r,t):
    n = r*t
    neighborhoods = []
    for i in range(r):
        for j in range(t):
            vv = [(i-1)%r*t+j, (i+1)%r*t+j,
                  i*t+(j-1)%t, i*t+(j+1)%t]
            assert len(set(vv)) == 4
            neighborhoods.append(sum(1<<v for v in vv))
    inv = [[] for _ in range(n)]
    for v,cover in enumerate(neighborhoods):
        for w in range(n):
            if (cover>>w)&1:
                inv[w].append(v)
    whole = (1<<n)-1
    sols=[]
    def search(covered,chosen):
        if covered == whole:
            sols.append(tuple(sorted(chosen)))
            return
        uncovered = whole ^ covered
        best = None
        cm = uncovered
        while cm:
            low=cm & -cm; w=low.bit_length()-1; cm-=low
            opts=[v for v in inv[w] if neighborhoods[v] & covered == 0]
            if not opts:
                return
            if best is None or len(opts)<len(best):
                best=opts
                if len(best)==1:break
        for v in best:
            search(covered | neighborhoods[v], chosen+[v])
    search(0,[])
    assert len(sols)==len(set(sols))
    return sols

if __name__=='__main__':
    for t,expected in [(3,0),(4,16),(5,0),(6,0),(8,144),(12,16)]:
        sols = find_codes(8,t)
        assert len(sols)==expected, (t,len(sols),expected)
        print('C8 x C'+str(t), len(sols), 'codes')
    print('VERIFY_OK')
