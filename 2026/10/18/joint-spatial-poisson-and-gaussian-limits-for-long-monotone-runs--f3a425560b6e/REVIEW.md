# Self-review

## Correctness — PASS

The proof reconstructs the exact domain (uniform permutations, growing consecutive windows, and \(n/r!\to\lambda\in(0,\infty)\)), determines every compatible overlap case, bounds exceptional overlapping or cross-block windows, and applies independent-block Poisson convergence and a Lindeberg Gaussian descent limit. Explicit mixed-block characteristic-function control gives actual joint independence, not just zero covariance. The finite covariance identities follow from conditioned boundary comparisons; every required boundary case was checked. `verify.py` exactly enumerates 46,232 permutations in orders 2–8 and 414,990 configurations for pair overlaps, for 160 rational assertions. Finite computation supports the identities, not the infinite limit.

## Originality — PASS, with residual priority uncertainty

Csáki–Földes (1996) and Amárioarei (2015) treat maximal monotone runs; Chryssaphinou–Vaggelatou (2001) concerns long-increasing-run compound Poisson approximation. Janson–Nakamura–Zeilberger (2013) proves joint Gaussian fixed-pattern results; Johnson–Fu (2014) develops run-count approximations. The accepted theorem adds simultaneous signed *spatial* Poisson convergence together with independent global Gaussian descents, a statement not implied by the visible scalar or fixed-length results. The older 2001 paper and complete 1996 text were not accessible for full inspection; general historical coverage remains possible, and novelty is not asserted as externally certified.

## Value — PASS

Long increasing/decreasing streaks are motivated extremes of ordered data, while descents are a global distribution-free measure of permutation roughness. Their joint marked-spatial and Gaussian law is a natural multiscale characterization, retaining locations and two competing signs rather than merely the maximum streak length. The finite nonzero covariance identities show why joint independence requires proof.

## Limits and sources

Uniform independent relative ranks, factorial rare-event sequences, weak convergence only; no finite-sample joint error rate or nonuniform-permutation universality is claimed. Primary sources and precise reading limitations are enumerated in the references and structured audit. The earliest precisely verified preprint day used is 2013-12-13, not a fabricated publication date for older journal papers.

Self-review: passed. Independent audit: not yet performed.
