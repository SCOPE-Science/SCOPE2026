# Uniform rank-3 failure of hereditary freeness for cones over extended Shi arrangements of type B

## Context

Hereditary freeness asks whether every restriction of a free arrangement is free.
Orlik conjectured that restrictions of free arrangements are free; Edelman and
Reiner disproved this, so hereditary freeness must be tested family by family.
Extended Shi arrangements are prominent multi-level deformations of Weyl
arrangements whose cones are free by Abe-Terao and Yoshinaga.
Nakashima-Tsujie determined hereditary freeness for extended Shi arrangements
of type A (hereditarily free if and only if the underlying rank is at most 5).
The type-B analogue was open: its restriction lattice contains extra coordinate
and sum families with no type-A counterpart.

## Definitions

Fix integers 3 <= l <= 6 and k >= 1. Put M_k = {-k+1, ..., k}, so |M_k| = 2k.
The extended Shi arrangement Shi(B_l,k) in C^l has hyperplanes x_i = m,
x_i - x_j = m, and x_i + x_j = m for 1 <= i <= l, 1 <= i < j <= l, m in M_k.
Its cone cShi(B_l,k) in C^{l+1} with coordinates (x,z) has homogenized
hyperplanes x_i = m z, x_i - x_j = m z, x_i + x_j = m z, plus z = 0.
A central arrangement is free if its module of logarithmic derivations is free.
Terao's factorization theorem: a free central arrangement has characteristic
polynomial splitting over Z with nonnegative integer roots. Hence a central
rank-3 arrangement whose characteristic polynomial does not split over Z is not
free. Every central arrangement of rank at most 2 is free.

## Result

For 3 <= l <= 6 and every k >= 1, cShi(B_l,k) is not hereditarily free.
Every restriction of rank at most 2 is free. For every l >= 3 and k >= 1 there
is an explicit 3-dimensional flat X, namely X = {x_2 - x_3 = 0} for l = 3 and
X = {x_2 - x_3 = 0, x_4 = ... = x_l = 0} for l = 4, 5, 6, such that the
restriction R_{l,k} = cShi(B_l,k)^X is a central rank-3 arrangement with

  chi(R_{l,k}, t) = (t-1)(t^2 - 9k t + S(k)),

where S(k) = 41k^2/2 for k even and (41k^2+1)/2 for k odd.
The quadratic factor has discriminant -k^2 (k even) or -(k^2+2) (k odd),
strictly negative for every k >= 1, so chi never splits over Z (indeed not over
R). By Terao's theorem each R_{l,k} is non-free. Thus hereditary freeness fails
at rank 3 uniformly in (l,k); no pair with 3 <= l <= 6 has all restrictions
free. Instances: k=1 gives (t-1)(t^2-9t+21), k=2 gives (t-1)(t^2-18t+82),
k=3 gives (t-1)(t^2-27t+185), k=4 gives (t-1)(t^2-36t+328).

## Proof and evidence

Restrict to H = {x_2 - x_3 = 0} with coordinates (u,w,z) = (x_1, x_2 = x_3, z).
The traces are: 2k lines u = m z; coincident pairs giving 2k lines w = m z;
2k lines u - w = m z; 2k lines u + w = m z; no contribution from
x_2 - x_3 = m z with m != 0; H itself dropped; traces 2w = m z from
x_2 + x_3 = m z, of which even m duplicate existing w-lines and the k odd m in
M_k give genuinely new half-level lines; plus z = 0. With
S_k = M_k union {m/2 : m in M_k} of size 3k, the restriction has
|R| = 9k+1 planes in four deconed line families A (size 2k), B (size 3k),
C (size 2k), D (size 2k) plus infinity. For l > 3 the extra coordinates trace
degenerately and the restriction has the same normal set (verified exactly,
e.g. |R| = 10 for k = 1 at every l in {4,5,6}).

The deconed arrangement has cross-family pair count P_2 = 30k^2. Triple
concurrences: ABC = ABD = 3k^2 (half-integer B-lines cannot contribute since
a - b or a + b would be a strict half-integer), ACD = 2k^2, and
BCD = 7k^2/2 (k even) or (7k^2-1)/2 (k odd). Quadruples Q = 2k^2 by a
same-parity bijection on M_k^2 (M_k has k evens and k odds). Four distinct
slopes force multiplicity at most 4, so Moebius inversion gives
c_2 = P_2 - T_3 + Q = 24k^2 - BCD = S(k). The discriminant computation above
then yields non-splitting for all k >= 1. Exact deletion-restriction over Q
confirms the formula for (l,k) in {3,4,5,6} x {1,2,3,4} and a mod-1009
finite-field complement count confirms c_2 for k <= 4; the analytic count is
valid for all k. Rank-2 restrictions check as (t-1)(t-3), free.

## Limitations

The theorem resolves the threshold clause (uniform rank-3 failure locus with
closed-form non-free witnesses plus freeness below rank 3), not a flat-by-flat
census of every restriction isomorphism type at l = 6. Freeness of the ambient
cone itself is not claimed. Machine verification covers k <= 4 for the witness
characteristic polynomial and k <= 14 for the counting identities; the analytic
proof covers all k >= 1.

## Reproducibility

Scripts: shiarr.py (exact restriction arithmetic and deletion-restriction
characteristic polynomial over Q), scan_codim1.py (all 19 corank-one
restrictions at (3,1)), restrict_flat.py (exact restriction to a flat),
witness_k.py and witness_k2.py (witness chi table), verify_counts.py (exact
rational concurrency counts, multiplicity cap, Moebius identity, mod-1009
check), fam_model2.py and bcd_closed.py (family identification and BCD closed
form). All characteristic-polynomial computations are exact over Q.

## References

- Nakashima-Tsujie, Freeness for restriction arrangements of the extended Shi
  and Catalan arrangements, Discrete Math. 346 (2023); arXiv:2111.03585.
  Type-A hereditary theory used for comparison only.
- Abe-Terao, The freeness of Shi-Catalan arrangements, European J. Combin. 32
  (2011); arXiv:1012.5884. Ambient freeness of Shi-Catalan cones.
- Abe-Tran-Tsujie, Vertex-weighted digraphs and freeness of arrangements
  between Shi and Ish, arXiv:2108.02518. Type-A Shi-Ish interpolation.
- Orlik-Terao, Arrangements of Hyperplanes, Springer, 1992. Terao
  factorization, restriction, and deletion-restriction background.
