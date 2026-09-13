# Uniform Wilf gap 2 for multiplicity-5 embedding-dimension-3 numerical semigroups

## Context

Let S be a numerical semigroup (a submonoid of N with finite complement),
with multiplicity m(S) = min(S \ {0}), embedding dimension e(S) = number of
minimal generators, conductor c(S) = min{c : c + N subset S}, genus
g(S) = |N \ S|, n(S) = |S cap [0, c(S)-1)| = c(S) - g(S), and Wilf number
W(S) = e(S) n(S) - c(S). Wilf's conjecture (1978) asserts W(S) >= 0 for every
S. It is known that every e = 3 semigroup is Wilf, and that Wilf holds for all
semigroups of multiplicity m <= 18 (Bruns-Garcia-Sanchez-O'Neill-Wilburne).
Those results give only the bound W >= 0. The present result establishes the
sharp uniform gap above Wilf's bound for the natural infinite class m = 5,
e = 3.

## Definitions

For m = 5 write Ap(S,5) = {0, w1, w2, w3, w4} with wi = 5 ki + i, ki >= 1
integers (Kunz coordinates k = (k1,k2,k3,k4)). The Kunz polyhedron P_5 is
defined by the eight facet inequalities (K):

  2k1 >= k2, k1+k2 >= k3, k1+k3 >= k4, 2k2 >= k4,
  k2+k4+1 >= k1, 2k3+1 >= k1, k3+k4+1 >= k2, 2k4+1 >= k3.

For each residue i, wi is a minimal generator (atom) iff both weak
inequalities in row i of (A) are strict:

  w1: 2k3+1 >= k1, k2+k4+1 >= k1;
  w2: 2k1 >= k2, k3+k4+1 >= k2;
  w3: k1+k2 >= k3, 2k4+1 >= k3;
  w4: k1+k3 >= k4, 2k2 >= k4.

Hence e(S) = 1 + #{atoms}, so e(S) = 3 iff exactly two of w1..w4 are atoms.
Standard Kunz theory gives g(S) = k1+k2+k3+k4, F(S) = max wi - 5,
c(S) = max wi - 4, n = c - g, and with M = max wi:

  W(S) = 3(c-g) - c = 2c - 3g = 2M - 8 - 3(k1+k2+k3+k4).  (W)

## Result

Theorem. Every numerical semigroup S with m(S) = 5 and e(S) = 3 satisfies

  W(S) = 3 n(S) - c(S) >= 2.

The bound is best possible: S = <5,6,7> has Ap(S,5) = {0,6,7,13,14},
k = (1,1,2,2), conductor c = 10, genus g = 6, n = 4, and W = 3*4 - 10 = 2.
Its atoms are w1 = 6 and w2 = 7 (w3 = 13 = 6+7, w4 = 14 = 7+7), so e = 3,
m = 5. (DRAFT Sec.1's "<5,6,12>" is a typo: <5,6,12> = <5,6> has e = 2;
the proved sharp witness is <5,6,7> as in DRAFT Sec.6.)

## Proof / evidence

Fix the atom pattern (choice of the two atom residues): 6 patterns. For each
non-atom residue at least one of its two weak inequalities in (A) is an
equality (else it would be an atom): 2 choices per non-atom residue, hence 4
witness combos per pattern, 24 witness pieces. Writing strict u > v over
integers as u >= v+1 gives the integer-strengthened atom rows (A_Z); splitting
by the argmax j of the Apery maximum (M = wj, linearizing (W) as
Wj(k) = 7kj - 3 sum_{i!=j} ki + 2j - 8) yields 6*4*4 = 96 subpieces, each a
rational polyhedron defined by (K) + ki >= 1 + four (A_Z) rows + three
dominance rows + two witness equalities. Every integer e = 3 tuple lies in at
least one subpiece (a non-atom residue always contributes a tight row).

The script verify_piecewise_exact.py (exact Fraction arithmetic, no floating
point) enumerates, per subpiece, all basic solutions (2 equalities + 2 active
inequalities), tests feasibility, tests boundedness via recession directions,
and takes the minimum. All 96 subpiece models have full rank 4 (pointed), so
vertex enumeration is sound. Outcome: 76 infeasible; 6 feasible
non-exceptional subpieces with exact real minima 17/5, 17/5, 11/5, 11/5,
14/5, 14/5, each with a Farkas dual certificate in certificates.json
independently re-verified; 14 subpieces (7 witness pieces x 2 tied argmax
values) with exact real minima 4/5, 6/5 or 8/5 (the EXCEPTIONAL set), closed
by verified integer arguments: each exceptional witness piece is a
2-dimensional lattice plane with closed form W = p s + q t + r
machine-checked identically against the witness equalities and (Wj); even
parity (E1, E2, E6, E7) lifts any even integer above 4/5 (resp. 6/5, 8/5) to
>= 2, and the remaining cases (E3-E5) use the residue class plus the
dominance/atom rows bounding the feasible polygon with verified integer
minima >= 2 attained at listed explicit tuples. verify_exceptional_closedforms.py
checks the closed forms identically and confirms integer minima >= 2.
The scripts exit nonzero on any violation.

Corroboration: verify_kunz_bruteforce.py checks all Kunz/atom/conductor/genus
formulas on all 882 valid tuples with 1 <= ki <= 7 by reconstructing each
semigroup from its Apery set (closure, conductor sharpness, minimal
generators); enumerate_gap.py scans to ki <= 40 with global minimum W = 2;
independent audits confirm per-subpiece integer minima >= 2 to bound 60.

## Limitations

Specific to multiplicity 5 and embedding dimension 3; no generalization to
higher multiplicity is claimed. The 14 exceptional subpieces use case-by-case
closed-form integer arguments rather than one uniform inequality.

## Reproducibility

Standard library only (fractions, itertools); exact rational arithmetic:

  python3 output/artifacts/verify_kunz_bruteforce.py
  python3 output/artifacts/enumerate_gap.py
  python3 output/artifacts/verify_piecewise_exact.py
  python3 output/artifacts/verify_exceptional_closedforms.py
  python3 output/artifacts/audit_exceptional_integers.py
  python3 output/artifacts/audit_subpiece_integers.py

Certificate re-verification uses output/artifacts/certificates.json with
output/artifacts/reverify_certs.py (run with the artifacts directory
importable, since the script imports verify_piecewise_exact).

## References

- W. Bruns, P. Garcia-Sanchez, C. O'Neill, D. Wilburne, Wilf's conjecture in
  fixed multiplicity, arXiv:1903.04342 (proves W >= 0 for m <= 18; e = 3
  always Wilf; equality remarks concern W = 0 only).
- J. I. Garcia-Garcia et al., Semigroups with fixed multiplicity and embedding
  dimension, Ars Math. Contemp. 17(2) (2019) (minimal Frobenius/genus
  algorithms for fixed m, e).
- M. Delgado, S. Eliahou, J. Fromentin, verification of Wilf's conjecture up
  to genus 100; S. Eliahou divset work (Wilf W >= 0 context).
- N. Kaplan, Counting numerical semigroups by genus (enumeration context).
