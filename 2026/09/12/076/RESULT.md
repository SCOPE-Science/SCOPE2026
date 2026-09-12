# Uniform puncture-number stability for H^2 of punctured-line configuration spaces

## Context

For integers r >= 1 and n >= 1 let C_r = C minus {p_1,...,p_r} be the
r-punctured complex line and F_n(C_r) its ordered n-point configuration
space. Put V_{n,r} = H^2(F_n(C_r); Q) with the S_n-action permuting point
labels. For each fixed r, representation stability gives a character
polynomial, while iterated puncture-splitting (e.g. Huang-type splitting)
produces a general onset bound N(2,r) growing with r. The admitted target
asks whether a single integer N* independent of r and a single two-variable
character polynomial P in cycle counts and r exist for all r >= 1, n >= N*,
or whether instead the minimal onset N(2,r) tends to infinity with r,
witnessed by an infinite sequence of pairs (n_k, r_k) with n_k -> infinity.

## Definitions

- X_m(g): number of m-cycles of g in S_n.
- e_1 = n*r + C(n,2): rank of H^1(F_n(C_r)).
- e_2 = sum_{a<b} (r+a)(r+b) over a,b in {0,...,n-1}: rank of H^2.
- n_rel = C(n,3) + r*C(n,2) + n*C(r,2): number of degree-2 relations.
- Arrangement A_{n,r} = {H_{ij} = {z_i = z_j}} union {H_{i,p} = {z_i = p}}
  in C^n; F_n(C_r) is its complement.
- Orlik-Solomon algebra E/I: E exterior on dlog generators e_{ij} (i<j)
  and f_{i,p}; I the OS ideal. W = wedge^2 H^1.
- Relation families: R_I (Arnold triples rho_{ijk}),
  R_II (mixed rho_{ij,p}), R_III (disjoint-fiber monomials tau_{i,pq}).

## Result

There exist N* = 1 and a single polynomial P in X_1,X_2,X_3,X_4 with
coefficients polynomial in r of degree at most 2 such that for every
r >= 1 and every n >= 1 the S_n-character of V_{n,r} equals P:

  chi_{V_{n,r}}(g) = P(X_1(g),X_2(g),X_3(g),X_4(g); r),

  P = X_1^4/8 + X_1^3 r/2 - 5 X_1^3/12 + X_1^2 X_2/2 + X_1^2 r^2/2
      - X_1^2 r + 3 X_1^2/8 + X_1 X_2 r - X_1 X_2/2 - X_1 r^2/2
      + X_1 r/2 - X_1/12 - X_2^2/2 + X_2/2 - X_3 - X_4.

In particular no divergent witness sequence (n_k, r_k) exists: the minimal
onset does not tend to infinity with r. The r-growing general bound N(2,r)
from iterated puncture-splitting is valid but not sharp for H^2.

## Proof / evidence

1. Arrangement model: F_n(C_r) is the complement of A_{n,r}, strictly
   fiber-type with exponents r, r+1, ..., r+n-1, hence formal with
   cohomology the Orlik-Solomon algebra. S_n permutes hyperplanes and acts
   on generators sign-free; the action descends to E/I.
2. Degree 1: dim H^1 = e_1 and chi_{H^1}(g) = B + r X_1 with
   B = X_1(X_1-1)/2 + X_2, valid for all n >= 1.
3. Rank-2 flats: up to S_n-symmetry the degree-2 OS relations are exactly
   (a) diagonal triples {H_{ij},H_{jk},H_{ik}} giving Arnold boundaries
   rho_{ijk}; (b) concurrent triples {H_{ij},H_{i,p},H_{j,p}} giving mixed
   boundaries rho_{ij,p}; (c) disjoint parallel pairs {H_{i,p},H_{i,q}}
   giving monomials tau_{i,pq} in the affine OS ideal. All other pairs meet
   transversely with no third hyperplane, so (a)-(c) exhaust degree-2
   relations.
4. Signs: transpositions negate rho_{ijk} and rho_{ij,p} (direct wedge
   check); 3-cycles fix rho_{ijk}; R_III is a genuine permutation.
5. Full rank by triangularity for every n >= 1, r >= 1:
   R_III are distinct wedge basis vectors; each R_II vector has a private
   f_{i,p} wedge f_{j,p} component disjoint from R_III; each R_I vector has
   a private lex-maximal pure-e component e_{ik} wedge e_{jk} disjoint from
   mixed terms. Hence rank(R) = n_rel. The degenerate case n = 1 gives
   W/R = 0 = H^2(C_r). The fiber-type Poincare polynomial and the
   hockey-stick identity C(n+r,3) - C(r,3) = n_rel give
   C(e_1,2) - n_rel = e_2, so V_{n,r} = W/R.
6. Characters: chi_W from (chi_1^2 - chi_1(g^2))/2 with the Church-Farb
   lemma X_1(g^2) = X_1 + 2 X_2, X_2(g^2) = 2 X_4; chi_{R_I} the Arnold
   character X_1(X_1-1)(X_1-2)/6 - X_1 X_2 + X_3; chi_{R_II} =
   r(X_1(X_1-1)/2 - X_2); chi_{R_III} = X_1 r(r-1)/2. Subtracting gives P.
   Identity specialization P(n,0,0,0;r) = e_2 holds symbolically.
7. Exact matrix verification (output/artifacts/verify_uniform_poly.py):
   builds wedge^2 H^1 permutation matrices and the relation row-space,
   confirms S_n-invariance, rank = n_rel, quotient dimension = e_2, and
   quotient character = P on all conjugacy classes: exhaustive over S_n for
   n <= 5 across r = 1..5 plus random permutations for (6,3), (6,5), (7,2).

## Limitations

Cohomological degree 2 only; rational coefficients; ordered configurations
of the punctured affine line (genus zero). No claim about H^k for k >= 3,
other curves or surfaces, integral torsion, or unordered configuration
spaces is made.

## Reproducibility

Run `python3 output/artifacts/verify_uniform_poly.py` (requires numpy).
The script exhaustively checks all of S_n for n <= 5 and sampled classes
for n = 6, 7, and prints ALL CHECKS PASSED. Dimension, hockey-stick, and
identity-specialization identities can be checked symbolically as in the
audit record.

## References

- T. Church, J. Ellenberg, B. Farb, FI-modules and stability for
  representations of symmetric groups.
- T. Church, Homological stability for configuration spaces of manifolds.
- Y. Huang, Cohomology of configuration spaces on punctured varieties,
  arXiv:2011.07153 (equivariant splitting; Hodge generating function for
  unordered multi-punctured elliptic-curve spaces).
- Orlik-Solomon theory of hyperplane arrangements (fiber-type
  arrangements, OS ideal, formality).
