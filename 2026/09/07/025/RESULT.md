# Sharp 8-by-8 point-line incidence ceiling in PG(2,4): M(8,8) = 24

## Context

General finite-field point-line incidence bounds (Vinh-type spectral bounds,
Stevens–de Zeeuw, VC-dimension refinements) are asymptotic and loose at small
orders. The projective plane PG(2,4), with 21 points and 21 lines, is the
smallest plane where Kővári–Sós–Turán-type pair counting and spectral bounds
visibly overshoot. This record pins the exact 8×8 ceiling with extremal-type
classification and a certified neighboring-size census.

## Definitions

- Let F4 = F2[x]/(x²+x+1) = {0, 1, w, w²} with w²+w+1 = 0.
- PG(2,4) = P²(F4): the 21 nonzero vectors of F4³ modulo F4*, each orbit
  represented by scaling so the first nonzero coordinate equals 1. Line
  normals use the same 21 representatives; incidence is dot product n·p = 0.
- Every line contains exactly 5 points; every point lies on exactly 5 lines.
- For a point set P and line set L,
  I(P,L) = |{(p,l) in P × L : p in l}|.
- M(m,n) = max_{|P|=m,|L|=n} I(P,L).
- For fixed P, deg_P(l) = |P ∩ l|; the multiset {deg_P(l) : l in L} is the
  line-degree type (point-side symmetric).

## Result

**Theorem.** In PG(2,4), M(8,8) = 24.

Every 8-point by 8-line configuration satisfies I(P,L) ≤ 24, and 24 is
attained. The 22680 attaining pairs split, by line-degree type (point-side
symmetric), into:

- type (3⁸): 2520 pairs;
- type (4,3⁶,2): 20160 pairs.

No configuration reaches 25.

**Certified side census (both sides agree).** For a point k-set P, the best
any k-line set can do is the top-k line-degree sum; dually for line k-sets:

| k  | max (point-side) | # attaining P | max (line-side) | # attaining L |
|----|------------------|---------------|-----------------|---------------|
| 7  | 21               | 360           | 21              | 360           |
| 8  | 24               | 7560          | 24              | 7560          |
| 9  | 28               | 90720         | 28              | 90720         |
| 10 | 33               | 70560         | 33              | 70560         |

Comparison bounds at m = n = 8: KST pair counting gives
I ≤ (8+√1856)/2 ≈ 25.54 (integer ≤ 25); the expander-mixing/spectral bound
(d|P||L|/N + λ√(|P||L|) with d = 5, N = 21, λ = 2) gives
5·64/21 + 2·8 ≈ 31.24. The ceiling 24 beats the integer KST ceiling by 1 and
the spectral value by about 7.

Full-21-line degree profiles of the 7560 attaining point 8-sets are
(4,3⁶,2⁴,1¹⁰) (5040 sets) and (3⁸,2⁴,1⁸,0) (2520 sets).

## Proof / evidence

**Lemma 1 (KST integer ceiling: I ≤ 25).**
Let r_l = |P ∩ l|. Two distinct points of P span a unique line of PG(2,4), so
counting pairs {p,q} ⊂ P by the line they span gives
∑_l C(r_l,2) ≤ C(8,2) = 28; restricting the sum to l in L only strengthens
the inequality. Hence ∑_{l in L} r_l² ≤ 56 + I, and by Cauchy
I² ≤ 8(56+I), i.e. I² − 8I − 448 ≤ 0, so I ≤ (8+√1856)/2 ≈ 25.54,
hence I ≤ 25 for integer I.

**Lemma 2 (degree-sequence classification for sum 25).**
If I(P,L) = 25 with |P| = |L| = 8, the line degrees are, up to ordering,
(4,3⁷) or (4,4,3⁵,2).
Indeed, write r_l = 3 + d_l; ∑ r_l = 25 gives ∑ d_l = 1. Cauchy gives
∑ r_l² ≥ 25²/8 = 78.125, so ∑ r_l² ≥ 79; pair-disjointness gives
∑ r_l(r_l−1)/2 ≤ 28, i.e. ∑ r_l² ≤ 81. Thus ∑ r_l² ∈ {79, 80, 81}.
Exhaustion over the integer partitions of 25 into 8 parts shows exactly two
multisets have square-sum in this interval: (3⁷,4) with 79 and
(2,3⁵,4²) with 81; none has 80.

**Lemma 3 (25 is not realized; computational certificate).**
For fixed P, I(P,L) = ∑_{l in L} deg_P(l) is maximized by taking the top-8
degrees (prefix optimality), and symmetrically for fixed L. Exhaustive
enumeration over all C(21,8) = 203490 point 8-sets shows the top-8 line-degree
sum is at most 24 (7560 attainers); dual enumeration over all C(21,8) line
8-sets shows the top-8 point-degree sum is at most 24 (7560 attainers).
A sum-25 configuration would exhibit an 8-set with top-8 sum ≥ 25,
contradiction. Hence no 8×8 configuration has I = 25. This is a finite check
over 2·C(21,8) = 406980 sets, replayable in seconds in plain Python.

The theorem follows: Lemma 1 gives I ≤ 25, Lemma 3 excludes 25, and the
examples below show 24 is attained.

**Explicit extremal examples (verified, I = 24).**
Field labels: 0, 1, 2 = w, 3 = w². Points/line-normals are
first-nonzero-normalized triples.

(a) Type (3⁸) on both sides:
P = {(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,2,0),(1,2,3),(1,3,1)},
L-normals = {(0,0,1),(0,1,0),(0,1,3),(1,0,0),(1,0,1),(1,1,1),(1,3,0),(1,3,3)}.
Every chosen line meets P in exactly 3 points; every chosen point lies on
exactly 3 chosen lines.

(b) Type (4,3⁶,2) on both sides:
P = {(0,0,1),(0,1,0),(0,1,1),(0,1,2),(1,0,0),(1,0,1),(1,1,0),(1,1,1)},
L-normals = {(0,0,1),(0,1,0),(0,1,1),(0,1,3),(1,0,0),(1,0,1),(1,1,0),(1,1,1)},
with line-degrees {4,3,3,3,3,3,3,2} summing to 24.

A dynamic-programming subset-sum count over the 7560 attainer profiles
confirms 22680 attaining pairs with the stated 20160/2520 split; the maximum
top-7 degree sum over point 8-sets is 22, so no attaining pair uses a
degree-0 line.

## Limitations

- The final 25-exclusion step is computational (dual C(21,8) enumeration);
  the counting argument reduces sum-25 to two degree sequences but does not
  eliminate them synthetically. A purely synthetic elimination remains open.
- Single-order result (PG(2,4), 8×8); generalization to a q ≤ 16 atlas is a
  conjectural template, not proved here.
- Novelty rests on documented searches plus substantive comparison with
  general asymptotic bounds; an unpublished or differently-indexed small-order
  census cannot be logically excluded.

## Reproducibility

Stdlib-only Python, seconds-scale. `verify.py` rebuilds F4 and PG(2,4) from
scratch, asserts 5/5-regularity, recomputes the dual k = 8 maxima and counts,
checks the EML/KST values, checks the degree-sequence filter, and verifies an
explicit 24-configuration, printing ALL CHECKS PASS. `pair_census.json`
records the attainer profiles, pair-type split, and extremal coordinates.

## References

- L. A. Vinh, Szemerédi–Trotter type theorem and sum-product estimate in
  finite fields. https://arxiv.org/abs/0711.4427 (asymptotic general bound;
  far above 24 at this scale).
- S. Stevens, F. de Zeeuw, An improved point-line incidence bound over
  arbitrary fields. https://arxiv.org/abs/1609.06284 (asymptotic; no
  bounded-order ceiling).
- A. Iosevich, T. Pham, S. Senger, M. Tait, An improved point-line incidence
  bound over arbitrary finite fields via VC-dimension theory.
  https://arxiv.org/abs/2303.00330 (general-range refinement; no PG(2,4)
  8×8 census).
