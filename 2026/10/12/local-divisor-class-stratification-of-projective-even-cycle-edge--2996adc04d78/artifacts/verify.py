"""Exact finite regression checks for the local class-group stratification.

No finite check is used to establish the theorem for unbounded parameters.
"""
from itertools import combinations
from math import comb
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def incidence_relations(a, b):
    # Columns give the divisors of the a+b coordinate functions,
    # rows are the a*b prime divisors (u_i,v_j).
    cols = []
    for i in range(a):
        cols.append([int(k == i) for k in range(a) for j in range(b)])
    for j in range(b):
        cols.append([int(l == j) for k in range(a) for l in range(b)])
    return Matrix(a*b, a+b, lambda i, j: cols[j][i])

checks = 0
for a in range(1, 12):
    for b in range(1, 12):
        S=smith_normal_form(incidence_relations(a,b), domain=ZZ)
        invariants=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i] != 0]
        assert len(invariants) == a+b-1, (a,b,invariants)
        assert all(c == 1 for c in invariants), (a,b,invariants)
        assert a*b-len(invariants) == (a-1)*(b-1)
        checks+=1

# Test all combinatorial zero patterns at each m: a pattern is in the
# hypersurface iff both products vanish, or neither does with nonzero
# coordinate values satisfying the product equality.
for m in range(2, 11):
    patterns_total = 0
    singular_patterns = 0
    fixed_points = 0
    maximum_rank = 0
    max_patterns = 0
    component_patterns = 0
    for a in range(m+1):
        for b in range(m+1):
            if a+b == 2*m: continue # all projective coordinates zero
            if (a == 0) != (b == 0): continue
            multiplicity=comb(m,a)*comb(m,b)
            patterns_total += multiplicity
            if a>=2 and b>=2:
                singular_patterns+=multiplicity
                rank=(a-1)*(b-1)
                if rank>maximum_rank:
                    maximum_rank=rank
                    max_patterns=multiplicity
                elif rank==maximum_rank:
                    max_patterns+=multiplicity
                if a==b==2:
                    component_patterns=multiplicity
            if a+b==2*m-1:fixed_points+=multiplicity
            # Euler characteristic of a nonzero-dimensional coordinate torus is 0;
            # dimension zero occurs exactly when a+b==2m-1.
    assert fixed_points==2*m
    if m==2:
        assert singular_patterns==0
    else:
        assert component_patterns==comb(m,2)**2
        assert maximum_rank==(m-1)*(m-2)
        assert max_patterns==2*m
        assert singular_patterns>0
    checks+=1

# Independently compare Jacobian monomial ideal and the displayed
# intersection-of-coordinate-primes ideal on every squarefree monomial.
# Membership of an arbitrary monomial is determined by its squarefree support.
for m in range(2,9):
    blocks = [(i,j,k,l) for i,j in combinations(range(m),2)
              for k,l in combinations(range(m),2)]
    all_u = (1 << m)-1
    all_v = all_u << m
    for mask in range(1 << (2*m)):
        in_jac_u = any((mask & (all_u ^ (1 << i))) == (all_u ^ (1 << i)) for i in range(m))
        in_jac_v = any((mask & (all_v ^ (1 << (m+j)))) == (all_v ^ (1 << (m+j))) for j in range(m))
        in_inter = all(bool(mask & ((1 << i)|(1 << j)|(1 << (m+k))|(1 << (m+l))))
                       for i,j,k,l in blocks)
        assert (in_jac_u or in_jac_v) == in_inter, (m,mask)
        checks += 1
print('VERIFY_OK',checks,'Smith normal forms, zero patterns, radical-Jacobian ideals')
