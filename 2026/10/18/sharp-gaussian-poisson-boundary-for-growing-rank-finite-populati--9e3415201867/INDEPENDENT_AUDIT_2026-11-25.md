# Independent mathematical audit

## correctness

PASS

Counting subsets with X_(k)=k+j gives the stated PMF. Equivalently, peeling off the k selected observations up to X_(k) gives the beta-binomial mixture with α=k, β=n−k+1 and m=N−n. Conditional variance plus variance of the conditional mean gives σ²=mpq(A+m)/(A+1), with component variances b²=mpqA/(A+1) and d²=m²pq/(A+1). In the gamma representation of the beta variable the standardized difference is the linear combination of the two standardized gamma sums with coefficients √q and −√p, times √(A(A+1))/(G_α+G_β)→1. This proves normality even at endpoint or oscillating p by compact subsequences. Under the success/failure divergence criterion, relative beta fluctuations vanish (relative variances ≤1/α and 1/β), so the conditional binomial characteristic function centered at mΘ and scaled by b tends in probability to exp(−t²/2); its normalized quadratic coefficient tends to one and its cubic remainder is O_P((mpq)^(-1/2)). Boundedness gives asymptotic independence from the beta fluctuation. Every limiting pair of coefficients b/σ,d/σ has squares summing to one, so the Gaussian conclusion holds even for oscillating variance ratios. For Poisson approximation shared Bernoulli uniforms cost at most mE|Θ−p|≤mp/√α and binomial-to-Poisson costs at most mp². When mp→λ<∞, p→0, m/A=(mp)/α→0 and σ²∼mp. Positive λ gives a non-Gaussian standardized Poisson; λ=0 gives a point mass at zero in distribution despite unit row variance, since Pr(Y≠0)≤mp and μ/σ→0. Reflection gives the other endpoint. Any bounded subsequence of the smaller expectation has a further such subsequence, proving necessity. Independent subset enumeration checked the exact law and variance on 83 finite triples (python -B /workspace/branches/audit-replay.py 4); the limit decisions follow from the proof, not this replay.

## originality

PASS

The supported distinct contribution is the all-path Gaussian iff and quantitative Poisson alternative under the stated growing-rank hypotheses, not the beta-binomial identities, classical component CLTs or previously proved sufficient regimes.

## value

PASS

A growing rank alone does not justify a normal approximation, even with growing reverse rank and missing population. The criterion states exactly which expectations must diverge and tells practitioners what replaces a Gaussian at the other boundary, including the point-mass limit when a variance-normalized rare count loses uniform integrability. The sharp classification is useful for sparse sampling, near-census and oscillating designs without an interior-fraction assumption; the explicit finite-row bound supports choosing a Poisson approximation where appropriate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
