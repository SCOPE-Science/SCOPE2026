# Self-review

## Correctness

PASS. The theorem uses exact minimization of the RKHS representer error over the chosen node weight, followed by a spectral Rayleigh lower bound for every pivot law. The water-filling feasibility condition is elementary but has fully specified quantifiers. The pairwise harmonic-mean bound produces a global \(r-1\) factor, and the exact rank-two eigenvalue calculation closes the bound. The diagonal witnesses attain the water-filling lower bound; their rational expressions converge to the sharp constant. The standalone verifier checks the identities on actual Gram matrices and rational diagonal families; it does not substitute for the proof.

Scientific limit: the risk is a one-node, target-independent-sampling and target-dependent-optimal-weight metric. The theorem is not a high-probability or multi-pivot statement.

## Originality

PASS. The source RPCholesky expected-residual formula and optimal quadrature weights are explicitly attributed to their originators, not claimed as new. Full primary-paper and closest public multistage-ARP result inspections did not find a theorem implying the new sharp all-rank minimax ratio or rank-two eigenbasis-invariant optimality. The closest pivoting literature concerns distinct Frobenius CSS losses or fixed-distribution error rates. Residual risk: inaccessible or unindexed overlapping work could exist.

## Value

PASS. Exact rank-two minimaxity and a sharp rank-growing failure factor address an inherent choice in a widely used numerical kernel quadrature sampler. The diagonal family gives a natural optimal replacement and shows why trace-optimal pivoting need not remain optimal for the uniform-in-integrand mean-squared criterion.

Self-review: passed. Independent audit: not yet performed.
