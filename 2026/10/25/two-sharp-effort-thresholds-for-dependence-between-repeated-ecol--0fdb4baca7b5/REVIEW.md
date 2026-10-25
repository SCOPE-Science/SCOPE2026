# Self-review: repeated-detection covariance phase diagram

## Correctness — PASS

For closed Poisson site abundance, conditional independence of binary detections gives covariance equal to the variance of conditional site detectability. Its probability-generating-function expression is exact, including endpoint cases. The derivative factorization reduces every interior stationary point to \(R(q)=-\log(1-q)/q^2=\lambda\). An explicit derivative proves that \(R\) has a single minimum, and the envelope theorem applied to the stationary covariance gives a strictly increasing interior-versus-perfect-detection maximum ratio. The limiting ratio crosses one exactly once. Bounds \(q_0<3/4\) and \(\lambda_{\mathrm{loc}}>2\) make the strict monotonicity inequality rigorous. The large-mean asymptotics and the elementary \(\lambda=3\) witness were reconstructed; the packaged Python script passed deterministic and randomized checks. Neither approximate decimal roots nor finite tests are used as infinite proofs.

## Originality — PASS, with residual risk

The 2003 Royle–Nichols original supplies abundance-driven heterogeneity and the detection mechanism, not a novel mechanism in this result. Donovan–Hines Chapter 7 (2007) explains the conditional likelihood and Poisson mixing. Moore et al. (2014) optimize survey allocation for detection probability rather than the covariance of two binary visits. The full published published-finding corpus statement “Two visits identify a nonparametric closed binomial N-mixture” studies repeated numerical counts, estimating parameters by factorial moments; neither its assumptions on the observed count variable nor its conclusion gives the present extrema/transition theorem for binary visit covariance. Statement-level searches for the two numerical thresholds, aliases, and relevant covariance/effect-size objectives yielded no known equivalent result. This absence is not a uniqueness proof. Full text of the 2003 Ecology source could not be inspected, and broader published covariance-optimization literature may contain equivalent statements; priority remains provisional.

## Value — PASS

The covariance of two repeat visit indicators measures the abundance-generated within-site dependence that is used diagnostically in presence–absence modeling. Detectability approaching one saturates binary indicators at abundant sites. This establishes two distinct, explicit and ecologically interpretable thresholds: one where nonmonotonic dependence first emerges and one where intermediate detectability begins to dominate perfect detection. It provides a global classification valid for all Poisson means and exact high-abundance scaling, not just an isolated example or a new name for a known formula. It does not claim that maximizing covariance is an optimal survey design criterion.

## References and limitations

Royle and Nichols (2003), Ecology 84:777–790, DOI 10.1890/0012-9658(2003)084[0777:EAFRPA]2.0.CO;2 (abstract and bibliographic material inspected); Donovan and Hines (2007), *Exercises in Occupancy Estimation and Modeling*, Chapter 7 (relevant original pages inspected); Moore et al. (2014), *The Optimal Number of Surveys when Detectability Varies*, PLOS ONE 9:e115345 (full HTML methods/results inspected); the full published published-finding corpus “Two visits identify a nonparametric closed binomial N-mixture” (main theorem and comparison inspected).

Residual scientific limitations include binary observation, constant closed Poisson abundance, conditional independent visits, no false positives, and one common individual detection probability. No claim is made about optimum estimation efficiency, optimum real survey effort, or finite sample behavior. The original source's full text was unavailable; independent mathematical audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
