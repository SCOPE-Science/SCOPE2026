# Scientific review: Gaussian–Poisson decoupling for local chords and global crossings

## Correctness — PASS
Fixing endpoint-disjoint chords leaves a uniform matching on the remaining endpoints. Each fixed chord with \(j\) intervening endpoints crosses at most \(j\) others, so the crossing count differs from that of the surviving diagram by at most the total fixed short-arc lengths. Combined with Paguyo's quantitative Gaussian crossing theorem and the exact mean/variance, this yields the stated uniform conditional normal approximation. Counting compatible marked short chords and taking factorial moments yields the complete product Gaussian–Poisson limit. For length zero the exact factorial deletion identity holds for arbitrary test functions and all \(0\le k\le n\). Exact enumeration independently checks finite instances through \(n=7\). The asymptotic result is proved analytically, not extrapolated from the enumeration.

## Originality — PASS on inspected evidence, residual historical risk
Acan's Theorem 4.2 (arXiv:1501.01489) gives independence between the Poisson short-length coordinates, but not their joint dependence with the crossing count. Paguyo's Theorems 1.1 and 1.2 (arXiv:2104.01134) give separate Gaussian and simple-chord Poisson approximations; separate marginals do not entail independence. The exact factorial deletion transform and uniform conditional Gaussian conclusion were not found in those inspected full texts or in the searched published finding index. The earlier Flajolet–Noy chapter is highly pertinent but its full text was not accessible; a general earlier joint-marking argument might cover the conclusion. This is a substantive residual priority risk, not a claim that failed search proves novelty.

## Value — PASS
Crossings fluctuate on the \(n^{3/2}\) scale while local short-chord counts have nondegenerate order-one Poisson fluctuations. Simultaneous Gaussian–Poisson inference requires a *joint* law, which separate central limit and Poisson approximation theorems do not supply. Uniformity under arbitrary prescribed local chord locations, the deterministic deletion bound, and an exact finite-sample marking transform explain the structural reason for scale decoupling. This is a natural full distributional phenomenon rather than a routine covariance calculation.

## Boundaries
The fixed-length and fixed-marking hypotheses are essential to the stated bounds. Claims for growing length cutoffs, full joint convergence rates, and exhaustive publication priority are not established. No independent validation or audit is claimed.

Self-review: passed. Independent audit: not yet performed.
