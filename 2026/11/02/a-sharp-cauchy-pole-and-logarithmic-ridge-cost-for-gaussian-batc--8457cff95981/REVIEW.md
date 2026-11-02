# Scientific review: Gaussian-batch Polyak ratio singularity

## Correctness — PASS

The probability-one Gaussian projection representation decomposes the update into a Student-ratio term and a reciprocal shifted-normal pole. Conditioning on independent chi-square variables yields an explicit normal-density interval calculation and gamma-integral tail coefficient; the other update term has strictly faster decay for every \(k\ge2\). Tail integration gives the exact moment boundary. A direct ridge identity and dominated logarithmic integral supply the regularization coefficient. The calibrated iteration is an affine recursion with independently refreshed scaled Student innovations; its moment and variance formulas follow from the invariant series. The included standalone verifier checks 690 exact rational update identities, 12 independent quadratures, 16 variance identities, and diagnostic finite samples. Infinite asymptotics rely on proof, not experiments.

## Originality — PASS (qualified)

The 2022 SPS work on loose lower bounds, original capped schemes and safeguards is the closest prior result. It does not establish the uncapped scalar Gaussian ratio's sharp coefficient, the ridge leading logarithm, or the exact batch-calibrated invariant-moment comparison. Classical Gaussian regression, chi-square geometry, Student distributions, and Cauchy ratios are acknowledged as established; the contribution lies in their sharp implication for these particular updates. Published mathematical-record and primary-literature comparisons did not identify a directly covering result, but an independent priority check in specialized ratio-estimation literature is still warranted. The 2009 normalized LMS analysis divides by input energy, not by a near-zero residual gradient with positive batch residual.

## Value — PASS

The result quantifies why a seemingly legitimate nonnegative-loss target can be numerically dangerous even at large finite minibatches, why a small gradient-ridge safeguard has an unavoidable logarithmic expected-cost law, and how exact residual removal changes the moment threshold. The coefficient and precise batch-size dependence are concrete tests for adaptive-step heuristics, not generic textbook deductions.

## Limitations

Scalar Gaussian regression only; the zero-target step is explicitly **uncapped** and thus differs from established capped SPS/DecSPS convergence theorems. Independent audit and publication-priority verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
