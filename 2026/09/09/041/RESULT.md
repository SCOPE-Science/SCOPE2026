# Certified twin-interarrival census in [1030000000, 1050000000]

## Context

Twin-prime distribution is the leading test case of the Hardy–Littlewood
k-tuple conjecture and the bounded-gaps program. Public data supplies
global twin counts pi_2(10^n) through 1e19 and consecutive-prime record
gaps, but no exhaustive twin-interarrival gap log with a maximal-gap
certificate in the round-boundary window [1030000000, 1050000000] near
the 1e9 calibration region. This record provides that ground-truth point.

## Definitions

- Window: integers n with 1030000000 <= n <= 1050000000 (20,000,001 integers).
- Twin lower member: odd p with p, p+2 both prime and p+2 <= 1050000000.
- T: ordered list of all twin lower members in the window.
- Gaps: g[i] = T[i+1] - T[i].
- Twin-interarrival gap maximum: G = max(g).
- Cousin pair: (n, n+4) both prime; window-first means least n >= 1030000000
  with n, n+4 both prime in the window.

## Result (headline claim)

Let T be as defined above. Then:

- (C1) |T| = C = 61310. First element 1030000259; last element 1049999957
  (upper member 1049999959 <= 1050000000).
- (C2) The gap list has 61309 entries. Its maximum is G = 3870, attained
  exactly once, at gap index 19459, i.e. between consecutive twin pairs
  (1036385639, 1036385641) and (1036389509, 1036389511).
  All four numbers are prime. Maximality holds by exhaustive scan of the
  logged gap table. Gap statistics: all gaps multiples of 6; minimum 6;
  mean ~326.21; median 228; 2571 gaps >= 1000.
  Gap-sum identity: sum(g) = T[-1] - T[0] = 19999698.
- (C3) The window-first cousin pair is (1030000567, 1030000571), both
  prime; minimality by scan (no (0,4) pair starts earlier in the window).

Primality of the six witness primes is by deterministic Miller–Rabin,
bases (2, 7, 61), valid for all n < 2^32 (all witnesses are ~1.03e9).

## Proof / evidence

Computation, not asymptotic proof; the finite census is proved by
exhaustive enumeration plus certificates:

1. Primary enumeration (`sieve.py`): base primes to sqrt(1050000000) by
   mini-sieve; full-window bytearray segmented sieve of the 20M interval;
   twin extraction over odd candidates; gap logging; cousin scan.
   Runtime ~0.6 s in CPython. Output: C=61310, G=3870 at index 19459,
   the stated endpoint pairs and cousin pair.
2. Independent replay (`verify.py`, stdlib only): base primes by trial
   division (independent method); odds-only segmented sieve with
   independent striding; twin/gap/cousin recomputation; deterministic
   Miller–Rabin (2,7,61) on all six witness primes; maximality and
   minimality scans; byte-equality cross-check of the generated tables.
   Prints VERIFY_OK with C=61310 G=3870 idx=19459, six MR True lines,
   and matching SHA256 hashes
   (twins table 4ab6fb9c…1b5c5; gaps table 1b6e0189…4ec9649).
3. Auditor re-execution (2026-09-09): both scripts rerun from scratch;
   sieve.py reproduced the headline values; verify.py printed VERIFY_OK.
   Gap identities rechecked: sum 19999698, all multiples of 6, unique
   maximum, strictly increasing ordered list, correct boundaries.
   All six witnesses independently confirmed prime by trial division;
   Miller–Rabin (d,s,x0) transcripts re-derived exactly as claimed.
   Prefix twins and cousin minimality spot-confirmed by trial division.
   No prime database consulted at any stage.

## Limitations

- Interval-specific finite census only; no inference about twin
  distribution outside [1030000000, 1050000000], and no asymptotic or
  infinitude result, is claimed.
- Correctness rests on agreement of two independent stdlib sieve
  implementations plus deterministic Miller–Rabin replay; no
  machine-checked proof of code correctness beyond mutual byte-agreement
  is offered.
- Heuristic-calibration use (Hardy–Littlewood twin-gap fit near 1e9) is
  conjectural future work, not claimed here.

## Reproducibility

Stdlib-only Python 3. From a clean directory:

1. `python3 output/artifacts/sieve.py` — sieves the window, prints
   C, G, index, witness pairs, cousin, and writes
   summary.json / twins.json / gaps.json (~0.6 s).
2. `python3 output/artifacts/verify.py` — independent resieve, six
   Miller–Rabin certificates, maximality/minimality scans, table
   cross-check; must end with VERIFY_OK.

Boundary note: LO=1030000000 is even so the twin loop over odd
candidates from 1030000001 is complete; twin lower members satisfy
p <= 1049999998 (odd p <= 1049999997), and the last archived pair
(1049999957, 1049999959) respects the upper bound.

## References

- E. W. Weisstein, Twin Primes (MathWorld):
  https://mathworld.wolfram.com/TwinPrimes.html
  — global pi_2(10^n) to 1e19, Hardy–Littlewood asymptotic, Brun theorem,
  bounded gap 246.
- OEIS A007508, Number of twin prime pairs below 10^n:
  https://oeis.org/A007508 — cumulative global counts only.
- C. Caldwell, The Gaps Between Primes (PrimePages):
  https://t5k.org/notes/gaps.html — consecutive-prime gaps, not twin gaps.
- Prime Gap List Project, about the record-gap curation program:
  https://primegap-list-project.github.io/about/
  — consecutive-prime record gaps/merits, not twin-interarrival spectrum.
- X. Gourdon and P. Sebah, Introduction to twin primes and Brun's
  constant computation:
  http://numbers.computation.free.fr/Constants/Primes/twin.html
  — global methods, p2 vs 2C2Li2, Rd factors, Brun extrapolation.
