"""Exact finite-chain verification for four unordered particles on K_{4,5}."""
from itertools import combinations, combinations_with_replacement, product
from math import comb, prod

A, B, N = 4, 5, 4
VERTICES = tuple(range(A+B))
EDGES = tuple((i,j) for i in range(A) for j in range(A,A+B))
STAR = tuple(tuple(i for i,e in enumerate(EDGES) if v in e) for v in VERTICES)


def make_complex(last_reference=False):
    choices=[]
    for v in VERTICES:
        ordered=list(STAR[v]); ordered=ordered[-1:]+ordered[:-1] if last_reference else ordered
        choices.append(tuple(ordered))
    basis={}
    for degree in range(N+1):
        basis[degree]=[
            (tuple(zip(vertices,halfedges)),edge_multiset)
            for vertices in combinations(VERTICES,degree)
            for halfedges in product(*(choices[v][1:] for v in vertices))
            for edge_multiset in combinations_with_replacement(range(len(EDGES)),N-degree)
        ]
    return choices,basis


def image(choices,domain_cell):
    halfedges, monomial=domain_cell
    counts={}
    for p,(v,edge_index) in enumerate(halfedges):
        sub=halfedges[:p]+halfedges[p+1:]
        for m in (edge_index,choices[v][0]):
            cell=(sub,tuple(sorted(monomial+(m,))))
            counts[cell]=1-counts.get(cell,0)
    return tuple(c for c,n in counts.items() if n)


def rank(choices,source,target,small_pivot=False):
    ids={cell:i for i,cell in enumerate(target)}
    echelon={}
    for cell in source:
        col=0
        for face in image(choices,cell):
            col^=1<<ids[face]
        while col:
            pivot = ((col&-col).bit_length()-1) if small_pivot else (col.bit_length()-1)
            if pivot in echelon:
                col^=echelon[pivot]
            else:
                echelon[pivot]=col
                break
    return len(echelon)


def check_squared_zero(choices,basis):
    for d in (2,3,4):
        for cell in basis[d]:
            boundary={}
            for first in image(choices,cell):
                for second in image(choices,first):
                    boundary[second]=not boundary.get(second,False)
            if any(boundary.values()):
                raise AssertionError(('nonchain',d,cell))


def run():
    expected_dimensions=[8855,47740,89460,68120,17461]
    expected_ranks=[8854,38873,50306,17461]
    for alternate in (False,True):
        choices,basis=make_complex(alternate)
        dims=[len(basis[d]) for d in range(N+1)]
        assert dims==expected_dimensions, dims
        assert dims==[
            sum(prod(len(STAR[v])-1 for v in chosen) for chosen in combinations(VERTICES,d))
            * comb(len(EDGES)+N-d-1,N-d) for d in range(N+1)
        ]
        # Exact binary row-pivot elimination after distinct local reference choices.
        high=[rank(choices,basis[d],basis[d-1],False) for d in range(1,N+1)]
        assert high==expected_ranks,high
        if not alternate:
            check_squared_zero(choices,basis)
        betti=[dims[i]-(high[i-1] if i else 0)-(high[i] if i<N else 0) for i in range(N+1)]
        assert betti==[1,13,281,353,0],betti
        assert sum((-1)**i*betti[i] for i in range(N+1)) == -84
        assert sum((-1)**i*dims[i] for i in range(N+1)) == -84
        # Independent coefficient of t^4 in the Gal Euler series:
        # (1-4t)^4 (1-3t)^5 / (1-t)^20.
        gal=sum(comb(4,i)*(-4)**i*comb(5,j)*(-3)**j *
                comb(20+N-i-j-1,N-i-j)
                for i in range(5) for j in range(6) if i+j<=N)
        assert gal == -84
        print('reference:', 'last' if alternate else 'first','ranks:',high,'betti:',betti)
    print('VERIFY_OK')

if __name__=='__main__':
    run()
