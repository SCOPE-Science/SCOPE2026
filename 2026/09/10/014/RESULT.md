# Sharp minimal obstruction to crank-sliced spt equidistribution for 11-colored partitions at 11n+6

## Context

The admitted target asked whether the crank-sliced spt first moment of
11-colored partitions is independent of the crank residue mod 11 on the
Ramanujan progression 11n+6, via an 11-dissection matched to an
Atkin-Lehner/Hecke eigenform. This sits in the recognized
Ramanujan p(11n+6) / Dyson crank / Andrews-Garvan spt-crank /
Bringmann-Ono mock-modular program at the diagonal prime scope
(11 colors, modulus 11, progression 11n+6), adjacent to the
Borozenets rank/crank-deviation 11-dissections, the Chen-Chen-Yin
crank-ones-difference 11-dissections, and the Lin-Peng-Toh NB_k
mod-5 identities. The target audit plan prescribed a
congruence-or-obstruction branch: prove the infinite equidistribution
or log the least residue-class obstruction.

## Definitions (fixed throughout; NB_k-anchored)

Let k = 11. An 11-colored partition of N is a tuple
pi = (pi^(1), ..., pi^(11)) of ordinary partitions with
|pi^(1)| + ... + |pi^(11)| = N.
Write #(lam) for the number of parts of lam and s(lam) for the
multiplicity of the smallest part of lam (s(empty) = 0).

- Crank (Fu-Tang, as in Lin-Peng-Toh): crank(pi) = #(pi^(1)) - #(pi^(2)).
- s-weight: s(pi) = s(pi^(1)) (first-component smallest-part
  multiplicity, the direct spt-analogue of the NB_k statistic).
- Crank-sliced spt first moment: S(r;N) = sum of s(pi) over
  11-colored partitions pi of N with crank(pi) = r mod 11,
  for r in Z/11.
- Slice series: G_r(q) = sum_N S(r;N) q^N.

## Result

**Theorem.** With the above definitions, the claimed equidistribution
is false, and fails at the first possible index. Exactly:

  S(6;6) = 6,  S(7;6) = 1,  hence  S(6;6) - S(7;6) = 5 != 0 mod 11.

Since 6 = 11*0 + 6 is the first term of 11n+6, N = 6 is the least
obstruction index. Consequently no common 11-dissection component and
no fixed eigenform can match all eleven slice series: already
G_6 - G_7 has first nonzero coefficient 5 at q^6.

Full exact row at N = 6 (29,183 eleven-colored partitions of 6):
S(r;6) = [1894, 5873, 2728, 949, 253, 49, 6, 1, 11, 78, 426],
r = 0..10; mod 11: [2, 10, 0, 3, 0, 5, 6, 1, 0, 1, 8], not constant.

Machine evidence (not part of the proved headline): all 14 residue
rows N = 11n+6 <= 150 are non-constant mod 11 (extended 27 rows to
N <= 300); all 55 slice pairs first differ at n <= 6; the 27x11
mod-11 matrix has rank 11 (trivial nullspace, no universal linear
relation among slices).

## Proof / evidence

Hand proof (no enumeration; machine-audited integer-cell logic).
Only facts used: each part >= 1 (so #(lam) <= |lam|), the definition
of s-weight, and the forcing lemma: c parts summing to c must be
[1^c], whose s-weight is c.

Setup: N = 6 with j = |pi^(1)|, m = |pi^(2)|, rest >= 0,
j + m + rest = 6; c1 = #(pi^(1)) <= j, c2 = #(pi^(2)) <= m,
diff = c1 - c2 in [-6, 6].

- Class 6 mod 11 needs diff in {-5, 6}. diff = 6 forces
  (c1,c2) = (6,0), hence (j,m,rest) = (6,0,0),
  pi^(1) = [1^6], weight 6; all else empty. Contribution 6.
  diff = -5 needs (0,5) (c1 = 0 gives weight 0) or (1,6)
  (needs j+m >= 7 > 6, impossible). Hence S(6;6) = 6.
- Class 7 mod 11 needs diff = -4 (diff 7 unattainable since
  diff <= 6). Cells: (0,4) (weight 0), (2,6) (needs j+m >= 8 > 6,
  impossible), (1,5) (needs j >= 1, m >= 5, j+m <= 6, so
  (j,m) = (1,5), rest = 0, pi^(1) = [1], pi^(2) = [1^5],
  weight 1). Hence S(7;6) = 1.

The verifier machine-checks the integer-cell audit: with c1 >= 1 the
only bound-compatible cells in these classes are (6,0,6,0,0) and
(1,5,1,5,0). Single-cell witness tableau: sizes [1,5,0x9] with
pi^(1) = [1], pi^(2) = [1^5].

Independent machine confirmation (exact integer arithmetic, stdlib
only): three independent N = 6 censuses (29,183 partitions) give the
identical exact row; N = 7 census (100,529) matches the exact table;
two independent DP pipelines agree to 150 (0 mismatches); full exact
big-integer table agrees for all N <= 39; GF cross-checks
(F(1,q) = spt series to 30, bivariate form, sum_c A = spt to 12).

## Limitations

The refutation is tied to the fixed NB_k-anchored reading
(first-component s-weight x Fu-Tang crank). A differently normalized
spt-crank (e.g. min-component/total-parts corner, undecided beyond
small N) could behave differently and is a different claim.
Non-constancy rows beyond N = 6 are certified computation to the
stated bounds (150 admitted depth, 300 extension), not an infinite
theorem. The preset fallback's eta-quotient/theta-identity half is
not supplied because no such explicit combination was stated to
verify against; the obstruction-datum half is delivered in full.

## Reproducibility

  python3 output/artifacts/verify_target.py   # -> OBSTRUCTION_FOUND least-N=6; VERIFY_OK

Stdlib only; ~1 s; byte-deterministic; exit 0.

## References

- N. Borozenets, Deviation of the rank and crank modulo 11,
  arXiv:2305.08751 (ordinary-partition deviations, not this slice).
- D. Chen, R. Chen, S. Yin, On the total number of ones associated
  with cranks of partitions modulo 11, arXiv:2410.08450 (ones-count,
  not smallest-parts over 11-tuples).
- Y. Lin, E. X. W. Xia, X. Yu, Some identities on Lin-Peng-Toh's
  partition statistic of k-colored partitions, arXiv:2308.05931
  (NB_k parts-count at mod 5, different statistic/modulus).
- S.-P. Chen, W. Y. C. Chen, J. Zang, The spt-crank for ordinary
  partitions, arXiv:1308.3012 (moduli 5/7 only).
- Rolen-Tripp-Wagner-Wilson, Cranks for Ramanujan-type congruences
  of k-colored partitions (general framework, no such 11n+6
  spt-moment statement).
