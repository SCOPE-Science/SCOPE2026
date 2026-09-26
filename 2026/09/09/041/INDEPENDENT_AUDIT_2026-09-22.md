# Independent audit — 2026-09-26

Record: `2026/09/09/041`. Verdict: **correctness PASS; originality PASS (window-specific); scientific value PASS (bounded data).** Disposition: retain accepted.

## Correctness
An independently written full bytearray sieve of every integer in [1,030,000,000,1,050,000,000], with primes to floor(sqrt(1,050,000,000)) and composites struck starting at max(p²,ceil(LO/p)p), yielded 61,310 consecutive twin lower members. First 1,030,000,259, last 1,049,999,957; 61,309 gaps, unique maximum 3,870 at zero-based index 19,459, minimum 6, sum 19,999,698, and 2,571 gaps at least 1,000. The first (n,n+4) cousin pair is (1,030,000,567,1,030,000,571). These agree with all material C1–C3 claims. Boundary inclusion was checked against p+2≤HI. The max endpoints follow directly from the recomputed ordered array. The independent implementation did not rely on the package sieve or stored tables.

## Prior work and originality
OEIS A007508 gives global twin counts at powers of ten, and the classical Hardy–Littlewood program concerns distribution rather than this specified interarrival table. A finite sieve in an arbitrarily chosen 20-million-integer window is a window-specific numerical data contribution, not a new twin-prime theorem. No precedence for this exact table was established; originality is credited only to its reproducible local table and maximum certificate.

## Scientific value and limits
The exact table is modest ground truth for a local twin-interarrival study. It does not establish an asymptotic, an exceptional global gap, or any test of a fitted probabilistic model. The package's code agreement and the separate sieve support the finite result, without a formal proof of a machine implementation.

Sources: RESULT.md, output/artifacts/sieve.py and verify.py; https://oeis.org/A007508 and https://t5k.org/notes/gaps.html.
