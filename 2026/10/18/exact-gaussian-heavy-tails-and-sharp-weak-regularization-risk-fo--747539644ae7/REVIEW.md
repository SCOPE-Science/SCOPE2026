# Scientific review

## Correctness — PASS

The update follows directly from the two scalar Gaussian oracle evaluations and the depth-one least-squares minimizer. The joint Gaussian change of variables is nonsingular; its conditional moments and the denominator density are explicit. Local integration around the pole proves the exact \(T^{-1}\) tail and fractional-moment cutoff; conditioning, rescaling, and Gaussian domination prove both \(\lambda^{-1/2}\) ridge risk constants. The verification script checks 375 exact rational realizations and independent Gaussian quadratures, without treating finite tests as proofs.

## Originality — PASS (best knowledge, not independent validation)

The nearest paper on stochastic AA, Lupo Pasini et al. (2021), studies smoothing and safeguards, not exact unregularized heavy-tail laws or sharp ridge asymptotics. Scieur–d'Aspremont–Bach (2017) analyze regularized nonlinear acceleration on *iterates*, with stochastic bounds but without the precise image-mixture variable or risk constant. Ouyang et al. study safeguarded adaptive regularization, and Pollock–Rebholz study deterministic history filtering. The published deterministic Aitken/Steffensen contraction robustness calculation has no random denominator. The standard general ratio-of-Gaussians pole observation is not claimed as a new probability lemma. Unindexed equivalent first-step derivations remain a bibliographic risk.

## Value — PASS

This quantifies a concrete stability blind spot in an established acceleration mechanism: arbitrarily small Gaussian noise can change a deterministic one-step exact solve into a random output without even an absolute mean. Beyond the basic pole observation, the exact \(\lambda^{-1/2}\) risk exponent and normalization-dependent leading constants give mathematically sharp information for choosing ridge strength. The fact is confined to two evaluations and is not promoted to a general convergence theorem.

## Limits of review

This report covers the mathematical claim, assumptions, source comparisons, and the reproducibility artifact supplied with it. No independent scientific validation was performed. The closest primary works were inspected in the applicable algorithm/analysis sections; unindexed literature is a residual risk.

Self-review: passed. Independent audit: not yet performed.
