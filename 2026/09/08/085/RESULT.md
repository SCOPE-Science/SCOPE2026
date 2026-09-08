# Certified nonlinearity / differential-uniformity table for seven committed 4-to-6-bit S-boxes, with bent flat-spectrum certificate and structured-vs-random gap

## Context

S-box nonlinearity (linear-attack resistance), differential uniformity (differential-attack resistance), and bent / almost-bent (AB) extremals are the central Nyberg / Carlet criteria behind AES selection and the Dillon-APN classification program. This record gives a small fully replayable fragment for n = 4..6 contrasting canonical structured power maps (Gold x^3, inverse) against seed-committed pseudorandom baselines, with a flat-spectrum bent certificate at n = 6 and an AB certificate at n = 5.

## Definitions

Field representations (polynomial basis, bit i = coefficient of t^i):

- GF(2^5) = GF(2)[t]/(t^5+t^2+1), elements as integers 0..31.
- GF(2^6) = GF(2)[t]/(t^6+t+1), elements as integers 0..63.

Both polynomials are irreducible (no linear/quadratic factor; no cubic factor for degree 6) and t is primitive (ord 31 in GF(32), ord 63 in GF(64)).

Boxes (list index = input, value = output):

- S1 (n=4, PRESENT): [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2].
- S2 (n=5, Gold): x -> x^3 on GF(2^5).
- S3 (n=5, literal commitment "inverse map x^14", 0->0): x -> x^14 on GF(2^5), i.e. [0,1,29,16,22,13,3,18,7,8,21,10,2,6,28,14,25,27,19,24,5,9,12,15,31,26,4,20,11,17,23,30].
- S3supp (supplement, TRUE Galois inverse): x -> x^30 (0->0) on GF(2^5)*.
- S4 (n=6, Gold): x -> x^3 on GF(2^6). General map, NOT a permutation (gcd(3,63)=3).
- S5 (n=6, true inverse): x -> x^62 (0->0) on GF(2^6)*.
- S6 (n=5, seeded-random permutation): Fisher-Yates of 0..31 driven by word stream SHA256('SCOPE-260-n5-v1' || ':' || uint32be(counter)), counter=0,1,2,..., each digest split into eight big-endian 32-bit words, j = word[k] mod (i+1) for i=n-1 down to 1: [12,18,21,9,23,8,14,31,15,28,5,16,4,3,24,2,22,1,20,10,6,30,26,29,0,17,25,11,19,13,27,7] (sha256 of 32 raw bytes = 782551d9...).
- S7 (n=6, seeded-random permutation): same rule with seed 'SCOPE-260-n6-v1' on 0..63: [31,57,42,22,15,29,13,33,32,58,26,60,9,34,36,62,8,16,44,14,48,6,47,10,5,38,43,17,0,4,50,63,61,25,49,12,39,23,46,18,27,56,2,40,35,41,45,54,7,11,21,52,30,19,28,3,24,51,37,20,53,1,59,55] (sha256 prefix 1606f54a...).
- B (6-variable Boolean bent witness, Maiorana-McFarland): f(v) = x0*y0 XOR x1*y1 XOR x2*y2 with x = bits 0-2, y = bits 3-5 of v.

For an (n,n)-map S, nonlinearity NL(S) = 2^{n-1} - max|W|/2 where max|W| is the maximum absolute Walsh coefficient over all nonzero output components and all input masks; delta(S) = max DDT entry over nonzero input differences (exhaustive pair tally); deg(S) = max algebraic degree over nonzero components (Moebius ANF).

Terminology note: the string "inverse map x^14" is mathematically contradictory — the Galois inverse on GF(2^5)* is x^30. This record takes S3 to be the literal map x^14 (commitment priority) and tabulates the true inverse as separately labelled supplement S3supp. Both readings satisfy every gap inequality.

## Result (exact integers, machine-checked)

| box | n | perm? | max\|W\| | NL | delta | deg | Walsh-magnitude histogram |
|-----|---|-------|---------|----|---|-----|---------------------------|
| S1 PRESENT | 4 | yes | 8 | 4 | 4 | 3 | 0:108, 4:96, 8:36 |
| S2 Gold x^3 | 5 | yes | 8 | 12 | 2 | 2 | 0:496, 8:496 |
| S3 x^14 (literal) | 5 | yes | 8 | 12 | 2 | 3 | 0:496, 8:496 |
| S3supp x^30 (true inv) | 5 | yes | 12 | 10 | 2 | 4 | 0:186, 4:465, 8:310, 12:31 |
| S4 Gold x^3 | 6 | no (map) | 16 | 24 | 2 | 2 | 0:1008, 8:2688, 16:336 |
| S5 x^62 (true inv) | 6 | yes | 16 | 24 | 4 | 5 | 0:819, 4:1134, 8:1008, 12:882, 16:189 |
| S6 random (n5 seed) | 5 | yes | 16 | 8 | 10 | 4 | 0:313, 4:408, 8:188, 12:72, 16:11 |
| S7 random (n6 seed) | 6 | yes | 28 | 18 | 8 | 5 | 0:784, 4:1412, 8:1008, 12:518, 16:212, 20:84, 24:12, 28:2 |
| B bent f | 6 | -- | 8 (all 64 masks) | 28 | -- | 2 | flat signed {(-8):28, (+8):36} |

Each histogram row sums to (2^n-1)*2^n (e.g. 31*32=992, 63*64=4032, 15*16=240).

AB certificate (S2): every one of the 31 nonzero components has signed Walsh spectrum contained in {0,+8,-8} (hence AB: NL = 12 = 2^4-2^2). Aggregate signed counts: (-8):186, (0):496, (+8):310. Observation, not headline: S3 = x^14 has the identical signed profile.

Bent certificate (B): all 64 Walsh values (including mask 0) have magnitude exactly 8, so f is bent with NL = 32-4 = 28.

Structured-vs-random gap (proved inequalities):

- At n=5 (baseline S6: NL 8, delta 10): NL(S2)-NL(S6)=4>=2, delta 2<10; NL(S3)-NL(S6)=4>=2, delta 2<10; NL(S3supp)-NL(S6)=2>=2 (supplement).
- At n=6 (baseline S7: NL 18, delta 8): NL(S4)-NL(S7)=6>=2, delta 2<8; NL(S5)-NL(S7)=6>=2, delta 4<8.

Hence NL(structured) >= NL(random)+2 and delta(structured) < delta(random) at both n=5 and n=6 under the literal commitment and under the true-inverse reading.

## Proof / evidence

Two independent stdlib-only code paths. Builder (`build_final.py`) reconstructs all 9 tables from the above primitives (square-and-multiply field powers; SHA256-DRBG Fisher-Yates) and freezes `truth_tables.json` + `definitions.json`. Verifier (`verify.py`, independent path: repeated-multiplication powers, re-derived DRBG, naive O(N^2) Walsh with no FWHT reuse, exhaustive DDT, Moebius ANF plus ANF re-evaluation round-trip at every (component, point)) checks: field-polynomial irreducibility; ord(t)=31/63; all 9 frozen tables re-derived byte-equal; inverse axioms x*x^30=1 (31 elts), x*x^62=1 (63 elts); Parseval identity per component; exact-integer assertions on all (max|W|,NL,delta,deg) rows; signed AB scan of all 31 S2 components; flat-8 scan of all 64 bent masks; all gap inequalities. Result: VERIFY_OK; transcript in `verify_log.txt`. The auditor independently recomputed all rows, histograms, Parseval identities, per-component AB/bent scans, and seed re-derivations with fresh code and confirmed every integer.

Proof (exact table, AB/bent certificates, gap inequalities) is separated from computed evidence (table.json, verify_log.txt transcripts). Prior art (Gold/inverse APN/AB bounds, PRESENT values, Nyberg/Carlet criteria) is classical background, not claimed. New content: exact triples of the two fresh SHA256-seed-committed random baselines S6/S7 (no theorem implies them) and the single-artifact joint gap conjunction.

## Limitations

1. S3 commitment string is self-contradictory ("inverse" vs exponent 14); resolved by literal-priority + labelled supplement; both readings pass.
2. S4 Gold x^3 at n=6 is not bijective (a map, as permitted); its delta=2 does not make it APN in the permutation sense.
3. "Beats random" is witnessed against two committed draws, not a random-ensemble lower bound.
4. Verifier shares the polynomial-basis representation with the builder but uses independently written arithmetic and naive (non-FWHT) transforms.
5. Scope is the minimal n<=6 replayable cell; no claim beyond it.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only, seconds scale; exits 0 with VERIFY_OK and regenerates `table.json` and `verify_log.txt`).

## References

- K. Nyberg — Differentially uniform mappings for cryptography (EUROCRYPT 1993). https://doi.org/10.1007/3-540-48285-7_55
- C. Carlet — Boolean Functions for Cryptography and Error Correcting Codes (vectorial functions, nonlinearity, bent/AB). https://doi.org/10.1017/CBO9780511780448.007
- A. Canteaut et al. — On the Differential-Linear Connectivity Table of Vectorial Boolean Functions (arXiv:1908.07445). https://arxiv.org/abs/1908.07445
- K. Li et al. — On the Differential Linear Connectivity Table of Vectorial Boolean Functions (arXiv:1907.05986). https://arxiv.org/abs/1907.05986
- J. McLaughlin, J. A. Clark — Using evolutionary computation to create vectorial Boolean functions with low differential uniformity and high nonlinearity (arXiv:1301.6972). https://arxiv.org/abs/1301.6972
- A. Bogdanov et al. — PRESENT: An Ultra-Lightweight Block Cipher (CHES 2007).
- NIST FIPS 197 — Advanced Encryption Standard (AES).
