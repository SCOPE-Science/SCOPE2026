"""Standalone exact checker for top homology of cycle-free digraph complex.
Enumerates top paths and all signed top-to-codimension-one incidences.
"""
import itertools
import math
from collections import defaultdict


def parity_of_sort(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq)))


def parity_reordering(seq):
    order = {v:i for i,v in enumerate(sorted(seq))}
    return parity_of_sort([order[v] for v in seq])


def check(n):
    verts = tuple(range(n))
    cycles = [(0,) + x for x in itertools.permutations(range(1,n))]
    paths = list(itertools.permutations(verts))
    path_arcs = lambda seq: tuple(sorted(zip(seq[:-1],seq[1:])))
    top = [path_arcs(seq) for seq in paths]
    assert len(top) == len(set(top)) == math.factorial(n)
    top_index = {f:i for i,f in enumerate(top)}
    boundary = defaultdict(list)
    for j,f in enumerate(top):
        for i in range(n-1):
            boundary[f[:i] + f[i+1:]].append((j,(-1)**i))
    # Each cycle is the boundary of the forbidden top simplex on all n cycle arcs.
    cycles_chains = []
    all_used = set()
    for c in cycles:
        cc = c + c[:1]
        ordered_arcs = tuple(zip(cc[:-1], cc[1:]))
        chain = {}
        for i in range(n):
            face = ordered_arcs[:i] + ordered_arcs[i+1:]
            face_sort = tuple(sorted(face))
            j = top_index[face_sort]
            assert j not in all_used
            all_used.add(j)
            chain[j] = (-1)**i * parity_reordering(face)
        cycles_chains.append(chain)
        co = defaultdict(int)
        for j,coef in chain.items():
            for i in range(n-1):
                face=top[j][:i]+top[j][i+1:]
                co[face]+=coef*(-1)**i
        assert all(v==0 for v in co.values()), 'oriented sphere boundary fails'
    assert len(all_used) == len(top)
    # All coefficients within a cycle are constrained by two-coface rows
    # formed by the consecutive (n-2)-edge path and isolated vertex.
    for c,chain in zip(cycles,cycles_chains):
        cc=c+c[:n]
        for i in range(n):
            subset=tuple(sorted(zip(cc[i:i+n-2],cc[i+1:i+n-1])))
            cofaces=boundary[subset]
            assert len(cofaces)==2, (n,c,i,cofaces)
            assert {j for j,_ in cofaces}==set(chain).intersection({j for j,_ in cofaces})
    # Independent GF(2) rank check on the complete boundary matrix.
    # n=6: 720 columns, sparse bitsets; this is exact, not probabilistic.
    rows={f:i for i,f in enumerate(boundary)}
    pivots={}
    for f in top:
        vector=0
        for i in range(n-1):
            vector ^= 1 << rows[f[:i]+f[i+1:]]
        while vector:
            pivot=vector.bit_length()-1
            if pivot in pivots: vector ^= pivots[pivot]
            else: pivots[pivot]=vector;break
    assert len(pivots)==math.factorial(n)-math.factorial(n-1)
    assert len(cycles)==math.factorial(n-1)
    # Representation traces on all permutations; check invariants and sign-invariants
    traces=[]
    for g in itertools.permutations(verts):
        sg=parity_of_sort(g)
        tr=0
        for c in cycles:
            new=tuple(g[v] for v in c)
            k=new.index(0)
            canonical=new[k:]+new[:k]
            if canonical==c:
                tr += (-1)**((n-1)*k)
        traces.append((tr,sg))
    assert sum(t for t,s in traces)//math.factorial(n)==(n%2), (n,traces)
    assert sum(t*s for t,s in traces)//math.factorial(n)==1
    assert (sum(t for t,s in traces)+sum(t*s for t,s in traces))//math.factorial(n)==1+(n%2)
    assert sum(t for t,s in traces)%math.factorial(n)==0
    assert sum(t*s for t,s in traces)%math.factorial(n)==0
    print(f'n={n}; top_faces={len(top)}, Hamiltonian_cycles={len(cycles)}, codim1_faces={len(rows)}, signed_sphere_cycles={len(cycles_chains)}, boundary_rank_mod2={len(pivots)}, S_n_invariants={sum(t for t,s in traces)//math.factorial(n)}, A_n_invariants={1+n%2}')


if __name__=='__main__':
    for n in range(3,7): check(n)
    print('HAMILTONIAN_TOP_CYCLE_INTEGRAL_AND_SYMMETRY_CHECK_OK')
