"""Exhaustive, dependency-free verification of two 16-vertex neighborhood systems.
Run: python3 verify.py. All vertex coordinates are elements of (Z/4Z)^2.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path

V = tuple((i,j) for i in range(4) for j in range(4))
D = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def edge(kind, u, v):
    if u == v: return False
    if kind == 'rook': return u[0] == v[0] or u[1] == v[1]
    return ((v[0]-u[0])%4, (v[1]-u[1])%4) in D

def trace(kind, tri, w, closed=True):
    return sum((int((closed and w==x) or edge(kind,w,x))<<j) for j,x in enumerate(tri))

def plus(u,v): return ((u[0]+v[0])%4,(u[1]+v[1])%4)

def transl_orbit(tri):
    return {tuple(sorted(plus(x,v) for x in tri)) for v in V}

def main():
    all_reps={}
    for kind in ('rook','shrikhande'):
        adj={u:{v for v in V if edge(kind,u,v)} for u in V}
        assert all(len(adj[u])==6 for u in V)
        pairs=list(combinations(V,2)); assert sum(edge(kind,u,v) for u,v in pairs)==48
        assert all(len(adj[u]&adj[v]) == (2 if edge(kind,u,v) else 2) for u,v in pairs)
        poly=[1]; stats=Counter(); triple_reps=[]
        for s in range(1,5):
            count=0
            for subset in combinations(V,s):
                # Implementation A: direct integer pattern extraction.
                patt={trace(kind,subset,w) for w in V}
                # Implementation B: set intersection, different code path.
                patt2={frozenset(x for x in subset if (w==x or x in adj[w])) for w in V}
                assert patt == {sum((int(x in a)<<j) for j,x in enumerate(subset)) for a in patt2}
                if len(patt)==2**s: count+=1
                if s==3:
                    edges=sum(edge(kind,a,b) for a,b in combinations(subset,2))
                    stats[(edges,len(patt)==8)]+=1
                if s==4:
                    assert len(patt)!=16
            poly.append(count)
        assert poly[:3]==[1,16,120]
        assert poly[4]==0
        assert (poly[3]==288 if kind=='rook' else poly[3]==224)
        # Exhaustiveness of translation quotient: 560 = 35*16.
        seen=set()
        for triple in combinations(V,3):
            if triple in seen:continue
            orbit=transl_orbit(triple)
            assert len(orbit)==16 and orbit.isdisjoint(seen)
            seen |= orbit
            rep=min(orbit)
            mask=sum(1 << j for j in {trace(kind,rep,w) for w in V})
            e=sum(edge(kind,a,b) for a,b in combinations(rep,2))
            triple_reps.append((rep,e,mask))
            assert all((len({trace(kind,t,w) for w in V}) == 8) == (mask == 255) for t in orbit)
        assert len(seen)==560 and len(triple_reps)==35
        all_reps[kind]=sorted(triple_reps)
        print(kind, 'closed polynomial', poly, 'triple edge-type/shattering:',sorted(stats.items()))
        print(kind,'translation orbits',len(triple_reps),'shattered orbits',sum(mask==255 for _,_,mask in triple_reps))
        if kind=='rook':
            assert stats==Counter({(0,False):96,(1,True):288,(2,False):144,(3,False):32})
        else:
            assert stats==Counter({(0,False):96,(1,True):192,(1,False):96,(2,False):144,(3,True):32})
        # Open neighborhood comparison (deliberately separate from main claim).
        op=[1]
        for s in range(1,5):
            op.append(sum(len({trace(kind,c,w,closed=False) for w in V})==2**s for c in combinations(V,s)))
        assert op==[1,16,120,320,0]
        print(kind,'open polynomial',op)
    # Deterministic export of the complete 35-representative quotient tables.
    lines=['graph\ttriple_(0-based_coordinates)\tinduced_edges\ttrace_mask_hex\tshattered']
    for kind in ('rook','shrikhande'):
        for rep,e,mask in all_reps[kind]:
            lines.append(f'{kind}\t{rep}\t{e}\t{mask:02x}\t{int(mask==255)}')
    path=Path(__file__).with_name('triple_orbits.tsv')
    if path.exists():
        assert path.read_text(encoding='utf-8')=='\n'.join(lines)+'\n'
    print('SRG16_CLOSED_SHATTER_PASS 2 graphs 70 triple orbit rows 1120 triples 2*1820 four-supports')

if __name__=='__main__':main()
