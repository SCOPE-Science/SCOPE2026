"""Exact rational checks for endpoint projections on products of two stars.

Run: python3 verify_star_product.py
Only Python's standard library is required. Finite tests supplement the all-parameter proof.
"""
from fractions import Fraction as F
from itertools import product


def closed(m, n):
    den = (m + 2) * (n + 2) * (m + n + 2)
    a0 = F(5*m*n + 2*m + 3*n*n + 4*n + 4, (n+2)*(m+n+2))
    b0 = F(5*m*n + 2*n + 3*m*m + 4*m + 4, (m+2)*(m+n+2))
    a1 = F(4*m*m*n + 4*m*n*n + 3*m*m + 3*n*n + 14*m*n + 7*m + 7*n + 12, den)
    pa0 = F(2*n*(3*m + 2*n + 1), (n+2)*(m+n+2))
    pb0 = F(2*m*(2*m + 3*n + 1), (m+2)*(m+n+2))
    pa1 = F(2*(2*m*m*n + m*m + 2*m*n*n + 6*m*n + m + n*n + n + 4), den)
    return {'A0': (a0, pa0), 'A1': (a1, pa1),
            'B0': (b0, pb0), 'B1': (a1, pa1)}


def solve(a, b):
    """Fractional row reduction with an explicitly grounded Laplacian."""
    k = len(b)
    rows = [list(map(F, row)) + [F(z)] for row, z in zip(a, b)]
    for j in range(k):
        pivot = next(i for i in range(j, k) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        t = rows[j][j]
        rows[j] = [z/t for z in rows[j]]
        for i in range(k):
            if i != j and rows[i][j]:
                t = rows[i][j]
                rows[i] = [u-t*v for u, v in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def orbit(m, n, typ):
    """Obtain all 6 or 9 vertex-class potentials without assuming formulas."""
    if typ[0] == 'B':
        q, p, r, ct = orbit(n, m, 'A'+typ[1])
        return q, p, r, ct
    xs = [1, 1, m-1]  # hub, distinguished leaf, remaining leaves
    ys = [1, n] if typ == 'A0' else [1, 1, n-1]
    vertices = list(product(range(3), range(len(ys))))
    idx = {ij: i for i, ij in enumerate(vertices)}
    aa = [[F(0) for _ in vertices] for _ in vertices]
    for ix, (i,j) in enumerate(vertices):
        neighbors = []
        if i == 0:
            neighbors.extend([((u, j), xs[u]) for u in (1, 2)])
        else:
            neighbors.append(((0, j), 1))
        if j == 0:
            neighbors.extend([((i,v), ys[v]) for v in range(1,len(ys))])
        else:
            neighbors.append(((i, 0), 1))
        for v, w in neighbors:
            aa[ix][ix] += w
            aa[ix][idx[v]] -= w
    sink = idx[(0,0 if typ == 'A0' else 1)]
    source = idx[(1,0 if typ == 'A0' else 1)]
    rhs = [F(int(i==source)-int(i==sink)) for i in range(len(vertices))]
    pp = [F(0)] + solve([row[1:] for row in aa[1:]], rhs[1:])
    assert all(sum(row[j]*pp[j] for j in range(len(vertices))) == rhs[i]
               for i, row in enumerate(aa))
    total = F(0)
    for j in range(len(ys)):
        for i in (1,2):
            total += xs[i]*ys[j]*abs(pp[idx[(i,j)]]-pp[idx[(0,j)]])
    for i in range(3):
        for j in range(1,len(ys)):
            total += xs[i]*ys[j]*abs(pp[idx[(i,j)]]-pp[idx[(i,0)]])
    effective = pp[source]-pp[sink]
    return total, 1+total-2*effective, effective, len(vertices)


def full_graph(m, n):
    vs=list(product(range(m+1),range(n+1)))
    ind={v:i for i,v in enumerate(vs)}
    edges=[]
    for j in range(n+1):
        for i in range(1,m+1):
            edges.append(((0,j),(i,j),'A0' if j==0 else 'A1'))
    for i in range(m+1):
        for j in range(1,n+1):
            edges.append(((i,0),(i,j),'B0' if i==0 else 'B1'))
    size=len(vs)
    lap=[[F(0) for _ in range(size)] for _ in range(size)]
    for u,v,_ in edges:
        i,j=ind[u],ind[v]
        lap[i][i]+=1;lap[j][j]+=1;lap[i][j]-=1;lap[j][i]-=1
    return edges, ind, lap


def run():
    orbit_cases=0
    orbit_edge_types=0
    for m in range(2,17):
        for n in range(2,17):
            target=closed(m,n)
            for typ in ('A0','A1','B0','B1'):
                q,p,r,k=orbit(m,n,typ)
                assert (q,p)==target[typ],(m,n,typ,q,p,target[typ])
                assert q>=r>0 and p>0
                orbit_edge_types+=1
            assert max(q for q,p in target.values())==max(target['A0'][0],target['B0'][0])
            assert max(p for q,p in target.values())==max(target['A0'][1],target['B0'][1])
            assert (target['A0'][0]-target['B0'][0])*F((m+2)*(n+2)*(m+n+2),2)==(m-n)*(m*n-2*m-2*n)
            assert (target['A0'][1]-target['B0'][1])*F((m+2)*(n+2)*(m+n+2),2)==(m-n)*(m*n-4*m-4*n-2)
            orbit_cases+=1
    full_cases=0; full_columns=0; full_edges=0
    for m,n in ((2,2),(2,3),(3,2),(3,3),(3,4),(4,3),(3,5),(4,4)):
        edges,ind,L=full_graph(m,n)
        seen=set(); expected=closed(m,n)
        for u,v,typ in edges:
            if typ in seen:continue
            seen.add(typ)
            rhs=[F(0)]*len(ind)
            rhs[ind[u]]=-1;rhs[ind[v]]=1
            potential=[F(0)]+solve([row[1:] for row in L[1:]],rhs[1:])
            assert all(sum(L[i][j]*potential[j] for j in range(len(ind)))==rhs[i] for i in range(len(ind)))
            q=sum(abs(potential[ind[a]]-potential[ind[b]]) for a,b,_ in edges)
            r=potential[ind[v]]-potential[ind[u]]
            assert (q,1+q-2*r)==expected[typ], (m,n,typ,q,r,expected[typ])
            full_columns+=1
        full_edges+=len(edges)
        full_cases+=1
    print('STAR_CARTESIAN_HODGE_EXACT_OK orbit_cases=%d orbit_edge_types=%d full_graphs=%d full_edge_orbits=%d full_graph_edges=%d' %
          (orbit_cases,orbit_edge_types,full_cases,full_columns,full_edges))

if __name__=='__main__':
    run()
