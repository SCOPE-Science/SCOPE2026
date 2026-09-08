# Exact minimal string attractors for Rudin–Shapiro and regular-paperfolding dyadic prefixes (n ≤ 64), with certified bounds to n = 1024

## Context
String-attractor size is the Kempa–Prezza dictionary-compression complexity measure for words. Schaeffer–Shallit made the Theta(1)-vs-Theta(log n) prefix-attractor dichotomy for automatic-sequence prefixes decidable and settled the period-doubling (size 2 for n ≥ 2), Thue–Morse (eventually 4), and Tribonacci (size 3) cases, leaving the other two canonical binary 2-automatic words — Rudin–Shapiro (RS) and regular paperfolding (PF) — without recorded attractor constants. Factor-complexity formulas (RS 8n−8 for n ≥ 8; PF 4n for n ≥ 7) are a distinct invariant and do not imply attractor spans.

## Definitions
- **Rudin–Shapiro (0-indexed):** RS[i] = parity of the number of (possibly overlapping) `11` blocks in the binary expansion of i; RS[0] = 0. Length-64 prefix: `0001001000011101000100101110001000010010000111011110110100011101` (OEIS A020985 0/1 version).
- **Regular paperfolding (0-indexed):** position i = PF(i+1), where m = 2^k·u with u odd gives 0 if u ≡ 1 mod 4, else 1. Length-64 prefix: `0010011000110110001001110011011000100110001101110010011100110110` (OEIS A014577).
- **String attractor:** a set Γ of positions of a word w (|w| = n) such that every distinct factor w[i..j] has at least one occurrence whose span [s, s+ℓ−1] contains a position of Γ. γ*(w) = minimum |Γ|.
- **Dyadic prefixes:** prefixes of length n ∈ {2, 4, 8, 16, 32, 64} (exact), plus {128, 256, 512, 1024} (bounds).

## Result
For dyadic prefixes the exact minima are:

| n  | RS γ* | RS witness | PF γ* | PF witness |
|----|-------|------------|-------|------------|
| 2  | 1 | [0] | 1 | [0] |
| 4  | 2 | [2,3] | 2 | [1,2] |
| 8  | 2 | [0,3] | 2 | [3,5] |
| 16 | 4 | [3,7,11,13] | 3 | [2,7,11] |
| 32 | 5 | [4,10,15,21,25] | 4 | [7,11,17,23] |
| 64 | 8 | [16,24,28,35,41,47,51,55] | 5 | [15,23,35,43,49] |

Certified upper bounds (valid attractors, exact-checked) and lower bounds for larger dyadic prefixes (greedy UB / disjoint-span LB / exact per-length LB):

| n | RS | PF |
|---|----|----|
| 128 | 12 / 7 / 8 | 7 / 4 / 4 |
| 256 | 13 / 7 / 8 | 8 / 4 / 4 |
| 512 | 15 / 7 / 8 | 10 / 4 / 4 |
| 1024 | 16 / 9 / 8 | 9 / 4 / 4 |

Greedy sets and disjoint/per-length bound values are stored in `output/artifacts/results.json`. Exact total distinct-factor counts D: RS: 2, 7, 23, 101, 418, 1730, 7008, 28128, 112608, 450528; PF: 2, 8, 26, 100, 407, 1631, 6479, 25775, 102767, 410351 (n = 2, …, 1024).

## Proof / Evidence
- **Words:** re-derived from the committed definitions above; verified against stored length-1024 words.
- **Exact factor counts:** suffix-array + Kasai LCP per-length counts D_ℓ; totals as above.
- **Upper bounds (validity):** every listed witness and greedy set cover-checked with exact string comparisons (no hashing): each distinct factor's occurrence spans intersect the set.
- **Lower bounds / minimality (n ≤ 64):** complete branch-and-bound minimum hitting-set search over the factor-span family terminated without timeout (node counts 1–940, logged in `results.json`); independently re-proved by a fresh exhaustive hitting-set search (no smaller attractor exists at any of the 12 lengths). Disjoint-span families (pairwise-disjoint occurrence-span unions need distinct attractor positions) and per-length counting (γ ≥ D_ℓ/ℓ) give the stated certified LBs.
- **Soundness cross-check:** discovery-time 64-bit rolling-hash factor grouping confirmed equal in count to exact suffix-array D at all 20 prefix lengths, with within-group exact-equality checks.
- **Transcript:** `python3 output/artifacts/verify.py` prints per-length exact D, witness/UB cover confirmations, and `VERIFY ALL OK` (see `verify.log`).
- The observed growth (RS 2→16, PF 2→~9 over n = 8→1024) is stated only as computed evidence toward the Theta(1)-vs-Theta(log n) side; no infinite-family classification is claimed.

## Limitations
- Finite inventory only: exact minima to n = 64; valid-but-not-necessarily-minimal upper bounds plus certified lower bounds to n = 1024.
- No infinite dichotomy side and no uniform constants c_RS/c_PF are proved.
- Optimality certificates are computational (exhaustive search transcripts), not closed-form proofs.
- Greedy upper bounds for n ≥ 128 are valid attractors but not proved minimal.

## Reproducibility
Stdlib-only Python. Files in `output/artifacts/`: `solver.py` (definitions + solver), `words.json` / `words1024.json` (conventions + length-1024 words), `results.json` (all values and witnesses), `verify.py` + `verify.log` (independent exact replay). Run: `python3 output/artifacts/verify.py` → `VERIFY ALL OK`.

## References
- L. Schaeffer and J. Shallit, String Attractors for Automatic Sequences, arXiv:2012.06840.
- D. Kempa and N. Prezza, At the Roots of Dictionary Compression: String Attractors, arXiv:1710.10964.
- OEIS A020985 (Rudin–Shapiro sequence); OEIS A337120 (paperfolding factor complexity); OEIS A005943 (Rudin–Shapiro factor complexity).
