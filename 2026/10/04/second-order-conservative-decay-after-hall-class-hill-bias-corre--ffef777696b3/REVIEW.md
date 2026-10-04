# Review: Second-order conservative decay after Hall-class Hill bias correction

## Correctness

The proof uses the exact exponential-order-statistic representation. The Hall correction has
\[
\mathbb E[\ell_z(Y)]
=
-\frac{\beta z}{1+\beta}
+\frac{\beta z^2}{1+2\beta}
+O(z^3),
\]
so the source paper's first-order correction leaves \(\alpha A(n/k)^2/[\beta(1+2\beta)]\). Threshold fluctuations and centered correction fluctuations are exponentially negligible relative to speed \(k\delta_n^2\), leaving a gamma moderate-deviation lower tail.

Risk: the coefficient is exact-Hall specific; a broader third-order model can alter it.

## Originality

The closest source, arXiv:2609.31127v1, requires \(|A(n/k)|=O(\theta_n)\) for its bias-corrected one-sided moderate-deviation law. That excludes the zero-rescaling case with nonzero second-order amplitude. The accepted result reaches \(\theta_n\asymp A(n/k)^2\), including zero, and produces the fourth-order safety exponent.

Older reduced-bias Hill work inspected for comparison studies dominant-bias removal, asymptotic normality, MSE, or threshold heuristics rather than this one-sided exponent.

Risk: a higher-order bias coefficient may exist elsewhere under different notation. The originality claim is the combined Hall coefficient plus one-sided moderate-deviation exponent, not the mere existence of higher-order bias.

## Value

The motivating paper treats tail-index overestimation as the unsafe error direction. Its first-order bias-corrected theorem becomes silent precisely when explicit rescaling is below \(|A(n/k)|\). The Hall result identifies the next protection scale and yields an explicit target-decay \(k\)-selection law, directly serving that reliability objective.

Same-model review: passed. Independent audit: not yet performed.
