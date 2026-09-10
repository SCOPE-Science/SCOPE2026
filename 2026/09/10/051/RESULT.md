# Disproof of the deep four-row Kronecker vanishing ray: g((9,7,5,3),(8,7,5,4),(7,6,6,5)) = 134682

## Context

Kronecker coefficients govern symmetric-group tensor multiplicities with
recognized demand from representation theory, algebraic combinatorics, and
geometric complexity theory. Exact formulas exist only in cells with a hook,
two-row, square, or near-rectangular argument. The admitted target conjectured
a first infinite vanishing family plus vanishing cone face in the deep cell
where every partition has 4 rows and at least 3 distinct part sizes, via an
atomic vector-partition chamber route:

For all even integers m >= 6, with
A_m = (m+3,m+1,m-1,m-3), B_m = (m+2,m+1,m-1,m-2), C_m = (m+1,m,m,m-1),
partitions of n = 4m, prove an explicit chamber inequality forcing the atomic
coefficient to zero, transfer to ordinary vanishing g(A_m,B_m,C_m) = 0 along
the whole ray, and span a vanishing face of the Kronecker cone.

## Definitions

For partitions lam, mu, nu of n, with irreducible S_n characters chi and
class centralizer sizes z_mu = prod_i i^{m_i} m_i!:

g(lam,mu,nu) = (1/n!) sum_{w in S_n} chi^lam(w) chi^mu(w) chi^nu(w)
            = sum_{mu |- n} chi^lam_mu chi^mu_mu chi^nu_mu / z_mu.

## Result

**Theorem (counterexample, minimal case m = 6, n = 24).**

g((9,7,5,3), (8,7,5,4), (7,6,6,5)) = 134682 != 0.

Hence the universal vanishing claim over all even m >= 6 is false, as is any
vanishing-face statement built on it. No chamber inequality forcing atomic
(hence ordinary) vanishing can hold at m = 6, since the ordinary coefficient
is large and positive.

Shape check: |A_6| = |B_6| = |C_6| = 24; each has exactly 4 rows; A_6 has 4
distinct parts, B_6 has 4, C_6 = (7,6,6,5) has 3 — all inside the claimed
deep cell.

## Proof / Evidence

Exact character sum from scratch (stdlib-only Python, exact rational
arithmetic via fractions.Fraction):

- Murnaghan–Nakayama rule by recursive rim-hook removal with sign
  (-1)^{height}: rim hooks enumerated as sub-partitions with no-2x2 and
  edge-connectivity checks. Conjugacy classes are the 1575 partitions of 24.
- Sum over all classes gives 134682 over 671 contributing (nonzero-term)
  classes. Full term table committed as output/artifacts/cert_n24.csv
  (sha256 1d209921618b120050a9450777dd5f8aa5beededbf15b8e702af219aeed1fed7);
  its 671 exact terms sum to 134682.

Independent cross-certification (auditor re-executed in the audit
environment):

- Self-tests: g((3,2,1)^3) = 5 at n = 6, g((2,1)^3) = 1 at n = 3.
- Reproduces independently recorded maxima g((4,2,1,1)^3) = 17 at n = 8 and
  g((5,3,2,1,1)^3) = 945 at n = 12.
- Character orthonormality at n = 24: <A,A> = <B,B> = <C,C> = 1,
  <A,B> = <A,C> = <B,C> = 0.
- Hook-length dimensions dim A = 7228208988, dim B = 5205500300,
  dim C = 1262068236 agree with chi at the identity class 1^24.
- Full-row tensor-dimension identity over all 1575 partitions of 24:
  every g(A,B,nu) is a nonnegative integer and
  sum_nu g(A,B,nu) dim nu = dim A . dim B = 37626444055496696400.
- All 6 S_3 argument permutations give 134682; reversed class-traversal
  recompute with cleared caches gives 134682.
- The value 134682 >> 0 is robust against any rounding concern (all
  arithmetic exact integer/rational).

Route logic: ordinary nonvanishing at m = 6 kills (i) chamber-forced atomic
zero (cannot hold where the ordinary coefficient is large positive under the
claimed transfer), (ii) universal ordinary vanishing, and (iii) any vanishing
face built on the ray.

## Limitations

- Disproves the stated even-m ray via its m = 6 member; says nothing about
  other deep 4-row rays or odd-m values outside the target.
- Atomic-coefficient level not separately analyzed; unnecessary since ordinary
  nonvanishing already falsifies the conclusion.
- All cross-checks share one from-scratch Murnaghan–Nakayama implementation;
  independent Sage/GAP/LiE replay not performed (risk mitigated by the five
  logically distinct agreements above).

## Reproducibility

- `python3 output/artifacts/kronecker.py --selftest` (expect SELFTEST OK).
- `python3 output/artifacts/kronecker.py 24 "9,7,5,3" "8,7,5,4" "7,6,6,5"`
  (expect 134682, 671 nonzero-term classes).
- Sum the `term` column of `output/artifacts/cert_n24.csv` as exact rationals
  (expect 134682).
- Full-row / orthonormality / S_3 checks: see `output/artifacts/crosscheck.py`
  (its `sys.path` line must point at the directory containing `kronecker.py`).

## References

- Mishna–Trandafir vector-partition vanishing conditions; checked directly:
  Theorem 4.5 inequalities do not force vanishing on this triple.
  https://arxiv.org/html/2210.12128v1
- Mishna–Rosas–Sundaram atomic Kronecker machinery (transfer source).
  https://doi.org/10.1088/1751-8121/abf45b
- Rosas two-row/hook formula; Briand–Orellana–Rosas stability; Campbell
  Giambelli–Blasiak; Zhao square shapes; Tewari near-rectangular partitions
  (all require a hook/two-row/square/near-rectangular argument this triple
  lacks). https://doi.org/10.1016/j.jalgebra.2015.01.018
- Ressayre vanishing symmetric Kronecker coefficients (different subfamily).
  https://doi.org/10.1007/s13366-019-00466-7
