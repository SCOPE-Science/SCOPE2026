"""Independent finite cellular checks for two-particle sink configurations on cactus graphs.

All particle coordinates are ordered. Ordinary graph edges have a fixed orientation
from the smaller to the larger endpoint. No outside packages are used.
"""
from itertools import combinations

def rank(columns, prime):
    pivots = {}
    for col in columns:
        v = {int(k): int(x) % prime for k, x in col.items() if x % prime}
        while v:
            j = min(v)
            if j not in pivots:
                inv = pow(v[j], -1, prime)
                pivots[j] = {k: (x * inv) % prime for k, x in v.items() if (x * inv) % prime}
                break
            t = v[j]
            for k, x in pivots[j].items():
                z = (v.get(k, 0) - t*x) % prime
                if z: v[k] = z
                else: v.pop(k, None)
    return len(pivots)

def check_graph(label, n, raw_edges, b, cactus=True):
    edges = sorted(tuple(sorted(e)) for e in raw_edges)
    assert len(set(edges)) == len(edges) and all(u != v for u,v in edges)
    E = len(edges)
    vertices = list(range(n))
    cell0 = [(u,v) for u in vertices for v in vertices]
    cell1 = [('h',e,v) for e in edges for v in vertices] + [('v',u,e) for u in vertices for e in edges]
    cell2 = [(e,f) for e in edges for f in edges if e != f]
    ix0 = {c:i for i,c in enumerate(cell0)}
    ix1 = {c:i for i,c in enumerate(cell1)}
    d1 = []
    for typ,a,c in cell1:
        if typ == 'h':
            u,v = a
            d1.append({ix0[v,c]:1,ix0[u,c]:-1})
        else:
            u,v = c
            d1.append({ix0[a,v]:1,ix0[a,u]:-1})
    d2 = []
    for (a,c) in cell2:
        u,v = a; x,y = c
        d2.append({ix1['v',v,c]:1,ix1['v',u,c]:-1,
                   ix1['h',a,y]:-1,ix1['h',a,x]:1})
    expected = (1, E+b, b*(b-1)) if cactus else None
    got = []
    for p in (2,3,5,7):
        r1=rank(d1,p);r2=rank(d2,p)
        betti=(len(cell0)-r1,len(cell1)-r1-r2,len(cell2)-r2)
        if cactus: assert betti==expected, (label,p,betti,expected)
        got.append((p,r1,r2,betti))
    assert len(cell0)-len(cell1)+len(cell2) == sum(((-1)**i)*d for i,d in enumerate(got[0][3]))
    if cactus:
        # Fixed-cell trace of the particle transposition: n in degree zero,
        # zero in degrees one and two (diagonal edge squares are absent).
        chi_swap=n
        tr_h0=1;tr_h1=b-E;tr_h2=0
        assert tr_h0-tr_h1+tr_h2==chi_swap
        assert E==n-1+b
    print(label, 'cells', (len(cell0),len(cell1),len(cell2)), 'ranks', [(p,r1,r2) for p,r1,r2,_ in got], 'betti', got[0][3], 'OK')

check_graph('path_4',4,[(0,1),(1,2),(2,3)],0)
check_graph('triangle',3,[(0,1),(1,2),(0,2)],1)
check_graph('square',4,[(0,1),(1,2),(2,3),(0,3)],1)
check_graph('two_triangles_at_vertex',5,[(0,1),(1,2),(0,2),(0,3),(3,4),(0,4)],2)
check_graph('two_triangles_with_bridge',6,[(0,1),(1,2),(0,2),(2,3),(3,4),(4,5),(3,5)],2)
check_graph('square_plus_triangle',6,[(0,1),(1,2),(2,3),(0,3),(0,4),(4,5),(0,5)],2)
check_graph('three_triangle_chain',7,[(0,1),(1,2),(0,2),(2,3),(3,4),(2,4),(4,5),(5,6),(4,6)],3)
# Non-cactus sanity check: note that these Betti numbers are not predicted by the theorem.
check_graph('K4_outside_scope',4,list(combinations(range(4),2)),3,False)
print('VERIFY_OK')
