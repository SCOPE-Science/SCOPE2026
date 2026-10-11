from fractions import Fraction
from itertools import combinations


def edges_complete_multipartite(parts):
    clusters=[]; off=0
    for n in parts:
        clusters.append(list(range(off,off+n))); off += n
    edges=[]
    for i,j in combinations(range(len(parts)),2):
        for u in clusters[i]:
            for v in clusters[j]: edges.append((u,v,i,j))
    return off, edges


def check(parts):
    r=len(parts); q=r//2
    assert r>=2 and q>=1
    N, edges=edges_complete_multipartite(parts)
    a={(u,v): Fraction(1, q*parts[i]*parts[j]) for u,v,i,j in edges}
    total=Fraction(1,1)+sum(a.values(), Fraction(0,1))
    expected=Fraction(2*((r+1)//2),1)
    assert total==expected, (parts,total,expected)
    minhat=None
    for mask in range(1<<N):
        cut=Fraction(0,1)
        for u,v,_,_ in edges:
            if ((mask>>u)&1) != ((mask>>v)&1):
                cut += a[(u,v)]
        hat=total-2*cut
        assert hat>=0, (parts,mask,hat)
        minhat=hat if minhat is None or hat<minhat else minhat
    return (1<<N), minhat, total

cases=[(1,1),(2,3),(1,2,3),(2,1,2,1),(2,2,1,1,1),(1,1,1,1,1,1)]
cuts=0
mins=[]
for p in cases:
    c,m,t=check(p); cuts+=c; mins.append(m)
print(f"VERIFY_OK instances={len(cases)} cuts={cuts} min_fourier={min(mins)} formulas=6")
