# Review: first half-range two-prime residue coverings

## Correctness — PASS
The conclusion is a fully specified finite minimization statement. The provided certificates enumerate every admissible smaller modulus and prime-power modulus, not an informal search sample. Each lower bound is supported by an explicit missing unit independently checked by modular inverse and direct product enumeration. Upper bounds provide all \(32\) and \(128\) residue witnesses. Primality and coprimality are tested exactly, including repeated primes, boundary cutoff, and \(q=2\). The sharp cutoffs follow by checking the adjacent primes and absent classes, not by assuming monotonicity in the modulus. No infinite statement follows from finite testing.

## Originality — PASS, with literature risk
The full HTML of Banks–Shparlinski (2026, arXiv:2610.19597v1) was inspected, including Theorems 1.1–1.4, their explicit restriction to the classical \(X=q\) case, and proofs based on character-sum bounds. It does not furnish the two first half-range thresholds or their precise prime bounds. Szabó (2024) was inspected in full-text HTML at its introduction and principal theorems; it treats asymptotic large-modulus representation results. The Banks 2026 random-model paper addresses an altered stochastic problem. Multiple searches for equivalent least-modulus, residue-covering and exact-table formulations and searches of the available earlier claims found no direct cover. The original 1987 Erdős–Odlyzko–Sárközy paper was identified but its full text was inaccessible; it remains a residual risk. Absence from search results is not presented as a proof of novelty.

## Value — PASS
The minimal modulus and minimal prime-power modulus are canonical extremal quantities for a direct quantitative strengthening of the binary Erdős–Odlyzko–Sárközy covering question: cut each prime-factor range from \(q\) to \(q/2\). The result exactly identifies the first successes, contrasts a composite and prime-power modulus, determines all prime-factor thresholds, and supplies complete small-modulus obstruction data and transparent reusable prime-product witnesses. It can calibrate experimental and analytic work on shorter prime ranges. Its importance is an exact natural finite benchmark, not a claimed solution of the large-modulus conjecture or an unsupported improvement in asymptotic bounds.

## Closest work and limits
Most directly related are Banks–Shparlinski (2026), Szabó (2024), and the original 1987 conjecture. The present claim is finite and covers \(X=q/2\); the inspected sources study predominantly \(X=q\), the large-modulus regime, or more than two prime factors. Earlier undocumented tables could contain the same small data; the complete 1987 source was not inspected. No independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
