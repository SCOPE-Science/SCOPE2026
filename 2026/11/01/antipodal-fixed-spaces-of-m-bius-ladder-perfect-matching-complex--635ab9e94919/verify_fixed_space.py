#!/usr/bin/env python3
"""Independent finite checks for antipodal fixed loci of perfect-matching complexes."""
from itertools import combinations


def model(n):
    edges = sorted({tuple(sorted((i, (i+1) % (2*n)))) for i in range(2*n)} | 
                   {tuple(sorted((i, (i+n) % (2*n)))) for i in range(n)})
    eid = {e:k for k,e in enumerate(edges)}
    antipode = lambda e: tuple(sorted(((e[0]+n)%(2*n), (e[1]+n)%(2*n))))
    seen=set(); orbits=[]
    for k,e in enumerate(edges):
        if k in seen: continue
        orbit=frozenset([k, eid[antipode(e)]])
        seen.update(orbit); orbits.append(orbit)
    # Each orbit is named by the graph edges it comprises, not by formulas.
    matchings=[]
    def rec(free, picked):
        if not free:
            matchings.append(frozenset(picked)); return
        v=min(free)
        for eidx,(a,b) in enumerate(edges):
            if v in (a,b) and a in free and b in free:
                rec(free - {a,b}, picked+[eidx])
    rec(set(range(2*n)),[])
    extendible=set()
    for matching in matchings:
        l=list(matching)
        for m in range(1<<len(l)):
            extendible.add(frozenset(l[i] for i in range(len(l)) if (m>>i)&1))
    fixed=set()
    for mask in range(1<<len(orbits)):
        face=frozenset(k for i,o in enumerate(orbits) if mask>>i&1 for k in o)
        if face in extendible: fixed.add(mask)
    # Independent quotient construction from occupied original graph vertices.
    compatible=set()
    for mask in range(1<<len(orbits)):
        occupied=set(); ok=True
        for i,o in enumerate(orbits):
            if mask>>i&1:
                for k in o:
                    a,b=edges[k]
                    if a in occupied or b in occupied:
                        ok=False;break
                    occupied|={a,b}
            if not ok: break
        if ok: compatible.add(mask)
    assert fixed==compatible, (n, 'orbit model discrepancy',len(fixed),len(compatible))
    return len(orbits),fixed


def betti(faces, nv):
    groups={}
    for f in faces:
        d=f.bit_count()-1
        if d>=0: groups.setdefault(d,[]).append(f)
    ranks={}
    for d in sorted(groups):
        if d==0: ranks[d]=0;continue
        preceding={v:j for j,v in enumerate(groups[d-1])}
        pivots={}
        for f in groups[d]:
            col=0
            for v in range(nv):
                if f>>v&1: col ^= 1<<preceding[f^(1<<v)]
            while col:
                lead=col.bit_length()-1
                if lead in pivots: col ^= pivots[lead]
                else: pivots[lead]=col;break
        ranks[d]=len(pivots)
    return {d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
            for d,fs in groups.items() if len(fs)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)}


def check():
    face_total=0
    for n in range(2,9):
        nv,faces=model(n)
        assert nv==2*n
        face_total += len(faces)
        b=betti(faces,nv)
        expect={} if n%2 else {n//2-1:2}
        assert b==expect,(n,b,expect)
        print('n=%d, fixed faces=%d, reduced Betti=%s'%(n,len(faces),b))
    print('VERIFY_OK: n=2..8, fixed-orbit equality and integral-compatible mod-two ranks; %d orbit faces'%face_total)

if __name__=='__main__':check()
