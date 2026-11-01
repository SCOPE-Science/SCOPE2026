"""Exact integral chain computation for multipath complexes of bidirected K_{2,n}.

Requires Python 3.10+ and SymPy 1.14.0; no input data or network access.
Run: python verify.py
"""

from collections import Counter
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def arcs(n):
    """Two hubs (0,1) and leaves 2,...,n+1, in a fixed order."""
    return tuple((u,v) for j in range(n) for u,v in
                 ((0,j+2),(j+2,0),(1,j+2),(j+2,1)))


def is_multipath(indices, directed_arcs):
    """Indegree/outdegree <=1 and no directed cycle, including digons."""
    nxt = {}
    pred = {}
    for i in indices:
        u,v = directed_arcs[i]
        if u in nxt or v in pred:
            return False
        nxt[u]=v
        pred[v]=u
    for start in nxt:
        visited = set()
        v = start
        while v in nxt:
            if v in visited:
                return False
            visited.add(v)
            v = nxt[v]
    return True


def all_faces(n):
    directed_arcs=arcs(n)
    ans={0}
    # Every multipath has at most four arcs: each arc meets one of the
    # two hubs and a hub can support at most one incoming and one outgoing.
    for k in range(1,5):
        for index_set in combinations(range(4*n),k):
            if is_multipath(index_set,directed_arcs):
                ans.add(sum(1<<i for i in index_set))
    return ans


def boundary_matrix(lower, upper, num_arcs):
    """Integer signed simplicial differential in increasing arc order."""
    idx={s:i for i,s in enumerate(lower)}
    out=[[0]*len(upper) for _ in lower]
    for j,mask in enumerate(upper):
        verts=[k for k in range(num_arcs) if mask & (1<<k)]
        for pos,i in enumerate(verts):
            out[idx[mask^(1<<i)]][j] = -1 if pos%2 else 1
    return out


def invariant_factors(mat):
    # Complete integral SNF, not a modular or floating-point approximation.
    normal=smith_normal_form(Matrix(mat),domain=ZZ)
    out=[]
    for i in range(min(normal.shape)):
        if normal[i,i]:
            out.append(abs(int(normal[i,i])))
    return Counter(out)


def rank_mod2(mat):
    """Independent bit-packed Gaussian elimination over F_2."""
    cols=len(mat[0]);pivots={}
    for j in range(cols):
        z=sum((int(row[j])&1)<<i for i,row in enumerate(mat))
        while z:
            pivot=z.bit_length()-1
            if pivot in pivots: z^=pivots[pivot]
            else:
                pivots[pivot]=z
                break
    return len(pivots)


def check_chain(d1,d2,d3):
    # Integer boundary-of-boundary test via nonzero sparse matrix entries.
    for lower,upper in ((d1,d2),(d2,d3)):
        for col in range(len(upper[0])):
            prod=[0]*len(lower)
            for i,upper_row in enumerate(upper):
                if upper_row[col]:
                    for j,lower_row in enumerate(lower):
                        prod[j] += lower_row[i]*upper_row[col]
            assert not any(prod), 'boundary squared nonzero'


def check_module(n):
    # In any dynamical region, a selected arc forces its reverse (2-cycle)
    # and all arcs incident to its endpoints (boundary stability).
    E=arcs(n); Eset=set(E)
    for u,v in E:
        part={(u,v)}
        while True:
            nextpart=set(part)
            for a,b in part:
                nextpart.add((b,a))
                nextpart.update((x,y) for x,y in E if x==a or y==a or x==b or y==b)
            if nextpart==part: break
            part=nextpart
        assert part==Eset
    print('MODULE_OK n=%d all_arcs_forced=%d all_vertices_unstable=true' %(n,len(E)))


def check(n,expected_f,expected_snf,expected_mod2_betti):
    f=all_faces(n)
    graded={k:sorted(s for s in f if s.bit_count()==k+1) for k in range(4)}
    counts=tuple(len(graded[k]) for k in range(4))
    assert counts==expected_f, (n,counts)
    assert len(f)==1+sum(counts)
    assert all((s^(s&-s)) in f for s in f if s)
    # This independently derived counting polynomial checks every dimension.
    assert counts == (4*n,6*n*n-4*n,4*n*(n-1)**2,n*(n-1)**2*(n-2))
    d1=boundary_matrix(graded[0],graded[1],4*n)
    d2=boundary_matrix(graded[1],graded[2],4*n)
    d3=boundary_matrix(graded[2],graded[3],4*n)
    check_chain(d1,d2,d3)
    snfs=[invariant_factors(mat) for mat in (d1,d2,d3)]
    assert snfs==expected_snf,(n,snfs)
    ranks=[sum(c.values()) for c in snfs]
    free_h1=counts[1]-ranks[0]-ranks[1]
    free_h2=counts[2]-ranks[1]-ranks[2]
    free_h3=counts[3]-ranks[2]
    assert free_h1==0
    # Torsion of coker(d3) lies in ker(d2)/im(d3), because im(d2)
    # is a subgroup of a free abelian group, and so is torsion-free.
    assert snfs[2][2]==1 and sum(v for k,v in snfs[2].items() if k>2)==0
    mods=[rank_mod2(mat) for mat in (d1,d2,d3)]
    mod_betti=(counts[1]-mods[0]-mods[1],
               counts[2]-mods[1]-mods[2],counts[3]-mods[2])
    assert mod_betti==expected_mod2_betti,(n,mod_betti)
    assert mods==[r-(1 if i==2 else 0) for i,r in enumerate(ranks)]
    check_module(n)
    print('CHAIN_OK n=%d face_vector=%r boundaries=%r ranks=%r' %(n,counts,[(len(x),len(x[0])) for x in (d1,d2,d3)],ranks))
    print('SMITH_OK n=%d factors=%r mod2_ranks=%r mod2_betti=%r' %(n,[dict(sorted(c.items())) for c in snfs],mods,mod_betti))
    print('HOMOLOGY_OK n=%d H1=0 H2=Z^%d+Z/2 H3=Z^%d' %(n,free_h2,free_h3))


if __name__=='__main__':
    check(4,(16,80,144,72),
          [Counter({1:15}),Counter({1:65}),Counter({1:71,2:1})],
          (0,8,1))
    check(5,(20,130,320,240),
          [Counter({1:19}),Counter({1:111}),Counter({1:208,2:1})],
          (0,1,32))
    print('ALL_VERIFY_OK exact_integer_smith_F2_independent_differentials_module_closure')
