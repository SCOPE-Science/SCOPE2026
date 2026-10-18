# Self-review

## Correctness — PASS

The statement fixes the initial law of the stationary two-state Markov environment, its flip probability \(0<p<1\), physically admissible maturation survival, positive initial populations in both age classes, and even observation times. The exact product of successive off-diagonal projection matrices gives independent cohort log-amplitudes \(cS_N\pm dD_N\), and the logarithm of their sum differs from \(|dD_N|\) by a uniformly bounded constant. The alternating and nonalternating additive environmental sums have a joint martingale central limit theorem with diagonal covariance \(\operatorname{diag}((1-p)/p,p/(1-p))\), and uniform fourth-moment bounds justify convergence of the first two moments, not merely convergence in law. The non-Gaussian characterization and unique minimizer follow by checking centered third moments and strict convexity in \(p/(1-p)\). Direct matrix-product identities and finite-state covariance identities passed the separately included checks; those calculations do not replace the proof.

## Originality — PASS with residual priority risk

Sanz (2019), DOI `10.1016/j.ecolmodel.2019.108797`, analyzes stochastic growth and two-stage Leslie populations, but the relevant age-structure family permits positive retention and does not give the present distributional result. Sanz and Bravo de la Parra (2020), DOI `10.1016/j.ecolmodel.2019.108829`, study scaled logarithmic variance and asymptotic Gaussian/lognormal behavior under eventual positivity of matrix products. For the current semelparous family, every even product is diagonal and every odd product is off-diagonal; the required eventual strict positivity does not hold. Their stated Gaussian conclusion does not apply, and a non-Gaussian cohort-switching limit and interior optimal environmental switching probability are not obtained there. Unterberger (2021), arXiv `2111.04167`, considers continuously switching phenotypes with a mixing composition process rather than the two-cohort parity persistence here. General martingale limit theory is an acknowledged proof technique. Earlier general random-product or semelparous literature could contain an implicit equivalent calculation, so publication priority is not independently established. See the structured comparisons in AUDIT.json.

## Value — PASS

The distinction is meaningful for semelparous population viability assessments: despite the same deterministic exponential growth exponent at all interior environment-switching rates, its projected log-abundance uncertainty is non-Gaussian; the mean has a positive order-\(\sqrt N\) correction and the annual environmental flip rate has a **unique explicit risk-minimizing value** when both common and contrasting environmental sensitivities occur. This closes a genuine modeling gap at the natural nonprimitive boundary of standard scaled-logarithmic-variance theory. No claim is made about actual demographic extinction probabilities or general stage-structured models.

## Boundaries and remaining risks

Even-time limits only; each stage initially positive; stationary symmetric binary environment; no control as the switching probability approaches an endpoint with observation length. Possible equivalent work in older reducible random-matrix literature was not fully exhaustively reviewed. Future independent priority and mathematical validation are appropriate but neither is represented as already performed.

Self-review: passed. Independent audit: not yet performed.
