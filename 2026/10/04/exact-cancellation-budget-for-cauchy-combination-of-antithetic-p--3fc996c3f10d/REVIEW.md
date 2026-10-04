# Review: Exact cancellation budget for Cauchy combination of antithetic p-value pairs

## Correctness
**PASS.** Each antithetic pair reduces exactly to one signed standard Cauchy variable. Independence across latent pairs and the characteristic function \(e^{-|t|}\) give the exact scale \(A=\sum_j|w_{j,+}-w_{j,-}|\). The standard-Cauchy p-value map then yields the full cdf and the exactness/conservatism classification. The Gaussian realization and the small-level limit follow directly. Numerical checks are secondary consistency checks only.

Risk: the theorem requires exact complementarity within pairs and independence across latent pairs; it does not cover perturbations of that architecture.

## Originality
**PASS.** The primary CCT paper states exact standard-Cauchy behavior under independence and perfect positive dependence, but the inspected full text does not state this antithetic-block scaled-Cauchy law or its cancellation budget. Later arbitrary-dependence theory broadens asymptotic validity without supplying the exact blockwise classification. The closest Biometrika analysis explicitly observes excessive CCT conservatism for negatively correlated one-sided p-values and discusses perfect-correlation boundaries asymptotically, but the inspected main text does not give the scale \(A\), the exact finite-level cdf, or the iff weight criterion. Targeted searches for antithetic/countermonotone formulations and the scale law found no statement implying the complete claim.

Risk: the stable-law derivation is short, so an equivalent statement could exist in supplementary or unindexed material. This residual risk is recorded rather than treated as proof of absence.

## Value
**PASS.** Opposing one-sided p-values from independent Gaussian contrasts give exactly this dependence architecture, and recent literature identifies negative-correlation conservatism as a practical CCT issue. The theorem converts that issue into a complete finite-level weight classification for any number of independent antithetic pairs: exactness, partial attenuation, and total cancellation are all determined by one interpretable functional \(A\). This is a motivated structural boundary result rather than a routine numerical special case.

## Closest literature and limitations
Closest sources are Liu–Xie (arXiv:1808.09011), Long–Li–Zhang–Li (arXiv:2107.06040), Gui–Jiang–Wang (arXiv:2310.20460), and Ota (arXiv:2603.22668). The theorem should not be extrapolated to imperfect negative correlation, dependent latent blocks, or modified Cauchy transforms.

Same-model review: passed. Independent audit: not yet performed.
