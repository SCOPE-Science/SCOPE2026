# Self-review

**Correctness — PASS.** The token-folding argument proves the lower bound for every multiple; lifting-the-exponent establishes a bijective exponent map modulo arbitrary powers of the odd Mersenne modulus and a witness with exactly the minimum number of bits. The valuation of the central binomial coefficient at two is exactly the binary weight. Explicit base-\(p\) digit witnesses rule out each odd prime from the gcd. The packaged checker verifies both independent arithmetic paths for finite samples, and there is no extrapolation from samples to infinite ranges.

**Originality — PASS, with risk.** OEIS A086342 and a 2015 proof explicitly cover the \(k=1\) lower bound, so that component is prior work. Elsholtz (2016) studies primes with sparse multiples and derives restrictions from Mersenne numbers, without an exact all-powers statement in the inspected manuscript. Clokie et al. (2020) study the same minimum-weight invariant and general algorithms; no inspected theorem yields constant minimum weight through \((2^r-1)^k\) for all \(r,k\). The additional fixed-divisor classification for all these powers is a connected arithmetic corollary, not an independent result. Search results and available earlier claim records yielded no equivalent or stronger exact statement. The possibility of an unlocated equivalent result, or derivation in another literature on multiplicative orders, remains.

**Value — PASS.** Exact minimum-weight multiples are an established invariant. A uniform formula for powers of *every* Mersenne number is structurally significant because the modulus grows without bound while the optimal weight stays fixed, and the proof constructs a witness by a single adjustable exponent rather than an exhaustive automaton. The central-binomial gcd is an exact natural infinite-index invariant, illustrating an arithmetic consequence not captured by the base-case observation.

Limitations: No least-multiple-size claim, classification of all optimal witnesses, or extension to arbitrary moduli is proved. Numerical checks do not replace proof. Priority requires independent literature review.

Self-review: passed. Independent audit: not yet performed.
