"""Independent finite checks for distance-four Boolean-cube graph-state cut spectra.

Only standard-library arithmetic is required for exact ranks. NumPy is used for
one direct partial-trace spectral calculation and declared in requirements.txt.
"""
from itertools import combinations
from math import comb


def rank_binary(rows):
    pivots = {}
    for word in rows:
        while word:
            k = word.bit_length() - 1
            if k not in pivots:
                pivots[k] = word
                break
            word ^= pivots[k]
    return len(pivots)


def predicted(n):
    if n % 4 == 0:
        return 1 << (n-1)
    if n % 4 == 1:
        return (1 << (n-1)) - (1 << ((n-1)//2))
    if n % 4 == 2:
        return (1 << (n-2)) - (1 << ((n-2)//2))
    return 1 << n


def group_convolution_rank(n):
    masks = [sum(1 << k for k in t) for t in combinations(range(n),3)]
    size = 1 << n
    return rank_binary([sum(1 << (x ^ mask) for mask in masks)
                        for x in range(size)])


def truncated_ring_rank(n):
    # g_i=1+x_i. Expand sum over all triple products in the truncated ring.
    # Coefficient at degree t equals C(n-t,3-t) mod 2, for t<=3.
    terms=[]
    for mask in range(1 << n):
        t = mask.bit_count()
        if t<=3 and (comb(n-t,3-t) & 1):
            terms.append(mask)
    return rank_binary([sum(1 << (base | term) for term in terms
                            if base & term == 0)
                        for base in range(1 << n)])


def literal_cut_rank(d,coordinate):
    left=[v for v in range(1 << d) if not ((v >> coordinate)&1)]
    right=[v for v in range(1 << d) if ((v >> coordinate)&1)]
    rows=[]
    for v in left:
        rows.append(sum(1 << j for j,w in enumerate(right)
                        if (v^w).bit_count()==4))
    return rank_binary(rows)


def direct_state_spectrum_d4():
    # 16 qubits, with eight on each side. Construct the normalized coefficient
    # matrix of the graph state from ALL controlled-Z edges, not from C rank.
    import numpy as np
    d=4
    left=[i for i in range(1<<d) if not (i&1)]
    right=[i for i in range(1<<d) if i&1]
    edges=[(v,w) for v in range(1<<d) for w in range(v+1,1<<d)
           if (v^w).bit_count()==4]
    M=np.empty((1<<len(left),1<<len(right)),dtype=np.float64)
    for a in range(1<<len(left)):
        bits_a={left[i] for i in range(len(left)) if (a>>i)&1}
        for b in range(1<<len(right)):
            bits_b={right[i] for i in range(len(right)) if (b>>i)&1}
            occupied=bits_a|bits_b
            M[a,b]=(-1.0 if sum((u in occupied and v in occupied) for u,v in edges)%2 else 1.0)/(1<<8)
    rho=M@M.T
    eigen=np.linalg.eigvalsh(rho)
    r=predicted(3)
    nz=eigen[eigen>1e-9]
    assert len(nz)==2**r,(len(nz),r)
    assert max(abs(nz-2.**(-r)))<2e-12
    assert max(abs(eigen[eigen<1e-9]),default=0)<2e-12
    print(f'direct_state d=4 nonzero={len(nz)} max_error={max(abs(nz-2.**(-r))):.3g}')


def main():
    cases=0
    for n in range(3,11):
        target=predicted(n)
        group=group_convolution_rank(n)
        ring=truncated_ring_rank(n)
        assert group==ring==target,(n,target,group,ring)
        print(f'n={n:2d}, d={n+1:2d}, rank={group:4d}, expected={target:4d}, ring={ring:4d}')
        cases+=2
    for d in range(4,9):
        for coord in range(d):
            got=literal_cut_rank(d,coord)
            assert got==predicted(d-1),(d,coord,got)
            cases+=1
    for d in range(9,12):
        got=literal_cut_rank(d,0)
        assert got==predicted(d-1)
        cases+=1
    direct_state_spectrum_d4()
    print(f'PASS: {cases} independent exact binary-rank comparisons and one direct density-spectrum test.')


if __name__=='__main__':
    main()
