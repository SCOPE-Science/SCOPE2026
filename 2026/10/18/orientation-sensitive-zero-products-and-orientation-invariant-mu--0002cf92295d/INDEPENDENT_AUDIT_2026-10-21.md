# Independent mathematical audit

## correctness

PASS

Writing x=sum d_v e_v+sum b_e a_e and y=sum h_v e_v+sum c_e a_e, the vertex equations are d_v h_v=0. Thus each vertex has exactly three types (0,L,R) with multiplicities 1,q-1,q-1. For an oriented arrow u->v, the xy arrow equation d_u c_e+b_e h_v=0 has rank zero exactly when d_u=h_v=0 and rank one otherwise, yielding W and the orientation-specific matrices WD or W^T D with each vertex weight inserted once; cyclic contraction gives the trace. For xy=yx=0, the two-arrow coefficient matrix has determinant h_v d_v-d_u h_u=0 by the vertex equations, and rank zero only when both endpoint types are zero. Hence each edge contributes q^2 if both endpoints are zero and q otherwise, giving tr(B^n) and the general graph subset sum. The displayed characteristic polynomials and C4 difference are algebraic identities; the bracket q^5+3q^4+8q^3-8q^2-q+1 is positive for q>=2 since q^2(q^3-8)>=0 and the remaining terms are positive. checker.py is finite corroboration only; the universal proof is the rank count and matrix algebra.

## originality

PASS

The same-invariant finite-ring literature and the nearest published path-algebra SCOPE record concern commuting pairs or commutator fibers, not xy=0 and xy=yx=0. The zero-product probability invariant is prior, but the all-field oriented-cycle transfer and all-graph mutual-annihilation formula are not implied by those different equations. A 2022 general zero-product paper remains a real access/priority risk.

## value

PASS

Zero-product and mutual-annihilation densities are natural finite-ring invariants. The theorem provides an all-field transfer law for every oriented cycle and a stronger graph formula for mutual annihilation, with an exact strict C4 orientation contrast. It reveals a structural separation between orientation-sensitive one-sided products and orientation-invariant two-sided annihilation, not an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
