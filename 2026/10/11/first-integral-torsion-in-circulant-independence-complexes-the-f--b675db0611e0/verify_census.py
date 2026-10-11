"""Exact census of integral torsion in independence complexes of small circulants.

Dependencies: Python >=3.9 and SymPy >=1.12. Uses integer Smith normal form,
not finite-field ranks, for all connected circulant graphs with 3 <= n <= 14.
The empty step set is treated separately: its complex is a simplex.
"""
import json
import math
import sys
from collections import defaultdict
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def faces(n, steps):
    """Each face is a bit mask; masks are stored by cardinality including zero."""
    step_set = set(steps)
    forbidden = [sum(1 << j for j in range(n)
                     if min((i-j) % n, (j-i) % n) in step_set)
                 for i in range(n)]
    out = defaultdict(list)

    def extend(available, selected, k):
        out[k].append(selected)
        while available:
            bit = available & -available
            available -= bit
            v = bit.bit_length() - 1
            extend(available & ~forbidden[v], selected | bit, k+1)

    extend((1 << n)-1, 0, 0)
    return out


def boundary_smith(face_dict, size):
    """D_size takes size-element faces to (size-1)-element faces."""
    columns = face_dict[size]
    rows = face_dict[size-1]
    index = {mask: i for i, mask in enumerate(rows)}
    coeffs = {}
    for col, mask in enumerate(columns):
        bits = mask
        sign = 1
        while bits:
            bit = bits & -bits
            bits -= bit
            coeffs[(index[mask ^ bit], col)] = sign
            sign = -sign
    matrix = SparseMatrix(len(rows), len(columns), coeffs)
    diagonal = smith_normal_form(matrix, domain=ZZ)
    nonzero = [abs(int(diagonal[j,j])) for j in range(min(diagonal.rows, diagonal.cols))
               if diagonal[j,j] != 0]
    return len(nonzero), [d for d in nonzero if d > 1]


def compute():
    counts = {}
    census = []
    positive = []
    for n in range(3,15):
        count = 0
        for mask in range(1, 1 << (n//2)):
            steps = tuple(j+1 for j in range(n//2) if (mask >> j) & 1)
            if math.gcd(n, *steps) != 1:
                continue
            count += 1
            fs = faces(n, steps)
            dimensions = max(fs)
            f_vector = [len(fs[k]) for k in range(1,dimensions+1)]
            boundary_ranks = [0] * (dimensions+2)
            boundary_ranks[1] = 1  # Augmentation for reduced H_0.
            smith_torsion = {}
            # size=2: boundary of edges. Its SNF is necessarily torsion-free.
            # size>=3: nonunits yield all possible positive-dimensional torsion.
            for size in range(2, dimensions+1):
                rank, nonunit = boundary_smith(fs,size)
                boundary_ranks[size] = rank
                if nonunit:
                    smith_torsion[str(size-2)] = nonunit
            betti = [f_vector[k-1] - boundary_ranks[k] - boundary_ranks[k+1]
                     for k in range(1,dimensions+1)]
            entry = {"n":n,"steps":list(steps),"f_vector":f_vector,
                     "boundary_ranks":boundary_ranks[2:dimensions+1],
                     "reduced_betti":betti,"integral_torsion":smith_torsion}
            census.append(entry)
            if smith_torsion:
                positive.append(entry)
        # A second, purely arithmetic inclusion-exclusion count of the
        # subsets with gcd(n, steps)=1 checks the completeness of the scan.
        def mobius(d):
            factors=0
            remaining=d
            prime=2
            while prime*prime<=remaining:
                if remaining%prime==0:
                    remaining//=prime
                    factors+=1
                    if remaining%prime==0:
                        return 0
                prime+=1
            if remaining>1:
                factors+=1
            return -1 if factors%2 else 1
        expected_count=sum(mobius(d)*((1 << (n//(2*d)))-1)
                           for d in range(1,n+1) if n%d==0)
        assert count==expected_count,(n,count,expected_count)
        counts[str(n)] = count
    assert len(census) == 338
    expected_steps = {(1,3,4),(2,3,5),(1,5,6),(1,2,5,7),
                      (3,4,5,7),(1,3,6,7)}
    assert len(positive)==6
    assert {tuple(row['steps']) for row in positive} == expected_steps
    for row in positive:
        assert row['n']==14
        assert row['integral_torsion']=={'1':[2]}
        assert row['reduced_betti'][0]==0 and row['reduced_betti'][1]==1
        assert all(x==0 for x in row['reduced_betti'][2:])
    return {"description":"All connected nonempty-step circulants, n=3..14; exact integral Smith forms",
            "connected_counts_by_n":counts,"number_checked":len(census),
            "torsion_cases":positive,"all_connected_cases":census}


def main():
    output=compute()
    if len(sys.argv)==3 and sys.argv[1]=='--write':
        with open(sys.argv[2],'w',encoding='utf-8') as stream:
            json.dump(output,stream,ensure_ascii=False,sort_keys=True,separators=(',',':'))
            stream.write('\n')
    elif len(sys.argv)==2:
        with open(sys.argv[1],encoding='utf-8') as stream:
            assert json.load(stream) == output
    elif len(sys.argv)>1:
        raise ValueError('Usage: python verify_census.py [--write destination.json | census.json]')
    print('CENSUS_PASS: 338 connected cases, six 14-vertex torsion cases, integral SNF.')
    print('Connected graph counts:', output['connected_counts_by_n'])


if __name__=='__main__':
    main()
