# Minimal-house Littlewood–Pisot verdict, degrees 2–12 (full census), with enclosed witnesses at 13–14

## Context

Littlewood polynomials (coefficients ±1) with extremal root location feed the
Lehmer/Smyth small-Mahler program and Boyd Pisot tables. Hare–Jankauskas
(arXiv:1910.13994) proves prescribed inside-disk counts for n ≥ 7,
k ∈ [3, n−3] (Newman; less complete for Littlewood) and leaves the
Pisot-related extremal columns k ∈ {1, 2, 3, n−3, n−2, n−1} unproved.
The N = n−1 column (one root outside, none on the unit circle) is the
Littlewood–Pisot column. This record determines it exactly through degree 12,
with certified witnesses at 13–14.

## Definitions

- L_n = monic degree-n polynomials with all coefficients ±1 (constant term
  through leading coefficient; 2^n patterns per degree; mask m ∈ [0, 2^n)
  encodes lower coefficients, bit i = 1 meaning −1).
- A pattern is **Littlewood–Pisot** if it has exactly one zero with |z| > 1,
  no zero with |z| = 1, and the outside zero is real > 1 (hence n−1 zeros in
  |z| < 1). Its **house** is that outside root β > 1. Pisot here is the
  root-location property of the pattern: the outside root is a Pisot number
  because the minimal polynomial of β divides the pattern; irreducibility of
  the pattern is not required and not claimed.
- φ = (1+√5)/2, house of x^2−x−1 ∈ L_2 (mask 3).
- F_n(x) = x^n − x^{n−1} − … − 1 (mask 2^n−1, all lower coefficients −1).

## Result (proved)

1. **Census, 2 ≤ n ≤ 12.** Exactly one of the 2^n patterns of L_n is
   Littlewood–Pisot: F_n. All other patterns are certified non-Pisot.
   Per-degree tallies (E1 = endpoint circle root P(±1) = 0; G = interior
   common-root circle certificate via gcd(R,S) Sturm count ≥ 1 in (−1,1);
   D = circle-free Rouche-disk count; F = fallback = 0 everywhere):
   n=2: D2/G2/E1-0; n=3: D4/G0/E1-4; n=4: D12/G4/E1-0; n=5: D12/G0/E1-20;
   n=6: D56/G8/E1-0; n=7: D64/G12/E1-52; n=8: D188/G68/E1-0;
   n=9: D260/G0/E1-252; n=10: D992/G32/E1-0; n=11: D1160/G164/E1-724;
   n=12: D4032/G64/E1-0. Each sums to 2^n with pisot count 1 at mask 2^n−1.
2. **Minimality through degree 12.** The least house among all
   Littlewood–Pisot patterns of degree ≤ 12 is φ: the degree-2 enclosure of
   width ~8.27e-25 (< 1e-24) lies strictly below every other enclosed house
   (n=3 lower bound exceeds the φ upper bound by > 0.22; houses increase
   monotonically toward 2: 1.618…, 1.839…, 1.927…, 1.965…, 1.983…, 1.991…,
   1.996…, 1.998…, 1.999018…, 1.999510…, 1.999755…).
3. **Witnesses at 13–14 (witness-only).** F_13 and F_14 are certified
   Littlewood–Pisot with houses in [1.9998778327, 1.9998778328] and
   [1.9999389387, 1.9999389388]. Completeness (non-Pisot exclusion) at
   degrees 13–14 was not finished; no minimality is claimed there.

## Proof / evidence

- Circle parametrisation z = e^{it}, t = cos θ: exact integer
  R(t) = Re P(e^{it}), S(t) = Im P(e^{it})/sin θ via corrected Chebyshev
  recurrences T_{k+1} = 2tT_k − T_{k-1}, U_m = 2tU_{m-1} − U_{m-2}, validated
  by the |P(i)|^2 = R(0)^2 + S(0)^2 identity on 510 patterns.
- Circle roots: P(±1) = 0 (endpoint E1), else G = gcd(R,S); a Sturm count ≥ 1
  of the separable part of G in (−1,1) certifies a circle root (G-route).
- Circle-free patterns: exact rational Rouché disks — L(z) = P(c0) +
  P′(c0)(z−c0), E = P − L, |B|ρ − |A| > Kρ^2 checked as
  B^2ρ^2 − (Kρ^2 + A1)^2 > 0 in exact Gaussian rationals (K the standard
  second-order majorant) — plus exact disjointness, strict inside/outside
  location (|c0|^2 vs (1∓ρ)^2), and disk count = n, giving certified
  (N_in, N_out).
- Outside-root realness: exact Sturm count in (1,2) equals 1; house by
  80-step exact bisection with opposite nonzero endpoint signs.
- Machine-checked exact certificates (F = 0 on every completed slice);
  numpy used only for untrusted center guesses, never trusted.

## Limitations

- Completeness proved only through degree 12; degrees 13–14 have certified
  Pisot witnesses but no exclusion census, so minimality is claimed only
  through degree 12.
- Pisot = root-location property of the pattern; irreducibility not required
  or claimed.
- Verifier shares one R/S/Sturm/Rouché implementation between search and
  replay (single codebase risk, mitigated by identity check and from-scratch
  re-derivation but no second independent codebase).

## Reproducibility

- `artifacts/verify.py --pisot-only`: replays all stored Pisot records from
  stored rationals only and checks the φ gap over degrees ≤ 12 (13/14
  witness-only). Returns VERIFY_OK.
- `artifacts/verify.py --tally N A B`: re-derives classification for degree N,
  masks [A,B) from scratch; full-range call asserts equality with stored
  tallies (F = 0 verified for every N = 2..12).
- `artifacts/verify.py --check-identity`: validates Chebyshev R,S tables via
  the |P(i)|^2 identity.
- Data: `artifacts/census_le12.json` (per-degree tallies plus Pisot D-records;
  E1/G non-Pisot verdicts deterministically re-derivable via --tally),
  `artifacts/pisot_13_14.json` (F_13/F_14 witness records).

## References

- K. G. Hare, J. Jankauskas, On Newman and Littlewood polynomials with
  prescribed number of zeros inside the unit disk, arXiv:1910.13994.
- B. Bedert, On the zeros of reciprocal Littlewood polynomials,
  arXiv:2312.04454.
- P. Drungilas et al., On certain multiples of Littlewood and Newman
  polynomials, arXiv:1801.07179.
- O. Yakir, Approximately half of the roots of a random Littlewood polynomial
  are inside the disk, arXiv:2011.06234.
- Pisot Number, MathWorld, https://mathworld.wolfram.com/PisotNumber.html
