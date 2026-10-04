# Review

## Correctness
PASS. The proof starts from the published signed CQR score and empirical-quantile convention. Under the stated noiseless symmetric-band assumptions every score is exactly \(-W_i\); reversing the order converts the conformal quantile into \(-W_{(r)}\). Direct interval algebra shows that the output is empty iff the test width lies below that calibration order statistic. Continuity gives a uniform rank among \(m+1\) widths, yielding the exact marginal formula, while a conditional binomial count yields the exact width-quantile profile. A standalone checker reconstructs these steps on finite rank configurations and checks the reported numerical example.

## Originality
PASS. The primary CQR paper states the signed score, additive conformalization, negative-score interpretation, marginal guarantee, and the empirical order-statistic convention, but its inspected full text does not state an empty-output law. The Sesia--Candès comparison analyzes marginal versus conditional validity and asymptotic efficiency, without this finite-sample rank formula. Sousa--Tomé--Moreira explicitly discuss negative corrections and the global conformal step's lack of adaptiveness, but the inspected text does not derive when shrinkage crosses the fitted endpoints or quantify the resulting conditional profile. General conditional-coverage impossibility results are broader and do not imply this exact mechanism. Searches for the exact empty-set, signed-score, order-statistic, and variable-width formulations found no statement that dominates the claim.

## Value
PASS. The result isolates a concrete operational consequence of a defining CQR feature: signed scores can shorten an overconservative band, yet a single global shrinkage can allocate essentially the entire marginal error budget to literal empty outputs on the smallest-width covariate stratum. The theorem gives an exact finite-sample frequency, an exact conditional profile, and a sharp asymptotic cutoff in a model with no response noise or center error, separating this phenomenon from generic model misspecification. This is useful for interpreting negative CQR corrections and for motivating explicit checks of post-calibration endpoint order or localized calibration when subgroup behavior matters.

## Closest literature and limitations
Closest inspected literature is Romano--Patterson--Candès (arXiv:1905.03222v1), Sesia--Candès (arXiv:1909.05433v1), and Sousa--Tomé--Moreira (arXiv:2207.02808). The claim is restricted to iid continuous fitted widths, exact centers, noiseless responses, and additive split CQR. It does not claim exact conditional validity in general and does not cover ties or other conformal variants.

Same-model review: passed. Independent audit: not yet performed.
