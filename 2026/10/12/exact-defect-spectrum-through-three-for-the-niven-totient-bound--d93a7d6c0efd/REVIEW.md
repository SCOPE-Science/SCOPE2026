# Independent mathematical audit

## correctness

PASS

Let p be the least prime divisor of composite n and h=H(n) its largest exponent. Euler product gives n−φ(n)≥n/p, and any prime occurring to exponent h forces n/p≥2^(h−1), hence Δ_H(n)≥2^(h−1)−h≥0. For Δ≤3, 2^(h−1)−h≤3 forces h≤3; with m=n/p, Δ≥m−h gives m≤6. Since p≤least prime factor of m, the only composite candidates are {4,6,8,9,10,12,15,25}. Exact totient computations show Δ=0 for 4, Δ=1 for 8,9, Δ=2 never, Δ=3 for 6,25, with all primes Δ=0. Tested independently by fresh sieve/factorization for every 2≤n≤3999, without using numerical cutoff as infinity proof. The cutoff-free least-prime argument establishes complete exhaustiveness.

## originality

PASS

At claim/implication level, no inspected prior source states or entails the precise final result; closest frameworks, partial results and source gaps are explicitly distinguished. No failed search is treated as proof of absolute priority.

## value

PASS

The arithmetic gap is the natural quantitative slack in Sándor--Atanassov’s established Niven max-exponent vs totient inequality. Its equality and first consecutive near-equality fibers form a COMPLETE extremal/stability classification rather than arbitrary midrange finite examples: it distinguishes exceptional 4,8,9,6,25 and proves an impossible defect level 2. The exact initial spectrum gives a reusable sharp benchmark for refinements or related multiplicative-defect questions, even though the elementary proof is short and does not classify higher fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
