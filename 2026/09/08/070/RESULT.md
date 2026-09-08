# Certified maximal prime gap and constellation census in [10^9, 10^9+2×10^6]

## Context

Empirical maximal prime gaps test Cramér/Granville predictions; prime
k-tuple occurrence counts test Hardy–Littlewood/sieve predictions; and
verified values of π(x) near round-number cutoffs anchor sieve-correctness
and verified-π benchmarking programs. Global record-gap tables store bare
first-occurrence values at worldwide scale and contain no certified
window-maximum, primality-certificate chain, or constellation census for the
fixed round-number window I = [1000000000, 1002000000].

## Definitions

- I = [1000000000, 1002000000] (closed interval, width 2×10^6).
- Gap means q − p for consecutive primes p < q in I (so there are
  q − p − 1 composites strictly between them).
- Prime quadruplet: (p, p+2, p+6, p+8) all prime.
- Prime sextuplet patterns: (0,4,6,10,12,16) and (0,2,6,8,12,18).
- Merit of a gap: (q − p)/ln p.
- Miller–Rabin bases {2,7,61} are deterministic below 2^32 (known theorem;
  I ⊂ [0, 2^32)).

## Result

Let I = [1000000000, 1002000000]. Then:

1. I contains exactly **96417** primes, least 1000000007, greatest 1001999989.
2. The window-maximal consecutive-prime gap is **G* = 196**, occurring
   **exactly once**, between **p* = 1001755423** and **q* = 1001755619**.
   Both endpoints are prime; every one of the 195 integers strictly between
   them is composite with an explicitly archived divisor.
3. I contains exactly **33** prime quadruplets of shape (p,p+2,p+6,p+8);
   the least is **(1000025261, 1000025263, 1000025267, 1000025269)**.
   The full list of 33 base primes is archived in `artifacts/results.json`.
4. I contains **zero** prime sextuplets of shape (0,4,6,10,12,16) and
   **zero** of shape (0,2,6,8,12,18).
5. The complete consecutive-gap spectrum has **86** even values; the counts
   sum to 96416 (= 96417 − 1) and the weighted sum is 1999982
   (= 1001999989 − 1000000007). Full table in `artifacts/results.json`.
6. Hardy–Littlewood heuristic expectations over the window (singular series
   by Euler product to 2×10^5, evaluated at log 10^9): ≈ **45.02**
   quadruplets (observed 33) and ≈ **0.437** sextuplets per pattern
   (observed 0; P(0) = e^{−0.437} ≈ 0.65). These are numerical heuristic
   comparisons, not theorems.
7. Merit G*/ln p* ≈ **9.457**. π cross-check: window count 96417 on top of
   the imported baseline π(10^9) = 50847534 gives implied
   π(1002000000) = 50943951.

Not claimed: global record status (196 is not a global record), infinitude
or density theorems, or anything outside I.

## Proof / evidence

- **Enumeration:** segmented sieve of I with all base primes to √B by two
  independent code paths: full-interval marking (`census.py`) and odd-only
  sieve (`verify.py`). Both agree: 96417 primes, max gap 196 at the same
  endpoints, 33 quadruplets, 0 sextuplets.
- **Primality proofs:** deterministic Miller–Rabin bases {2,7,61} full
  transcripts (d, r, x₀, squaring chains) for both gap endpoints, all four
  first-quadruplet members, and window first/last primes
  (`gap_certs.json`); both gap endpoints additionally proved prime by trial
  division to √n ≈ 31656 (independent method, rechecked by the auditor).
- **Maximality proof:** every one of the 195 integers strictly inside
  (p*,q*) carries an explicit divisor (`gap_interior_factors`, 195 entries;
  evens by 2, odds by archived small factor, re-factored by the auditor), so
  no window prime was missed there; global maximality over I follows from
  the exhaustive independently recomputed gap list (unique occurrence).
- **Replay:** `python3 artifacts/verify.py` re-sieves, recomputes every
  headline number, replays all 8 transcripts and 195 factors, and prints
  VERIFY_OK in seconds. The auditor additionally ran a fresh from-scratch
  sieve and recount confirming all headline integers and checksums.

## Limitations

- Window-specific census; implies nothing outside I.
- Miller–Rabin determinism for bases (2,7,61) below 2^32 assumed as a known
  theorem.
- Hardy–Littlewood figures are heuristic floating-point comparisons
  (truncated Euler product), not proofs.
- π(10^9) = 50847534 is an imported baseline, not recomputed; the new
  contribution is the window count 96417 and consistency arithmetic.
- Gap convention here is q − p = 196 (195 composites between); readers using
  the PrimePages g = q − p − 1 convention should read it as 195.

## Reproducibility

Archived scripts (stdlib only): `artifacts/census.py` (primary sieve +
census), `artifacts/certify.py` (certificate generator),
`artifacts/gap_certs.json` (8 transcripts + 195 interior factors),
`artifacts/results.json` (headline numbers, spectrum, quadruplet list),
`artifacts/verify.py` (independent replay, asserts all headline values,
prints VERIFY_OK). Run: `python3 artifacts/verify.py`.

## References

- C. Caldwell, The Gaps Between Primes — PrimePages.
  https://t5k.org/notes/gaps.html
- C. Caldwell et al., Table of Known Maximal Gaps between Primes — PrimePages.
  https://t5k.org/notes/GapsTable.html
- M. Visser, Verifying the Firoozbakht, Nicholson, and Farhadian conjectures
  up to the 81st maximal prime gap. arXiv:1904.00499.
  https://arxiv.org/abs/1904.00499
- A. Kourbatov, The distribution of maximal prime gaps in Cramer's
  probabilistic model of primes. arXiv:1401.6959.
  https://arxiv.org/abs/1401.6959
