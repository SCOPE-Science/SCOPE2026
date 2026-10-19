# Scientific review

## Correctness — PASS

The samplewise quadratic loss and independent additive-gradient model yield the exact conditional risk \(f_b(s)=vs/(v+bs)\). Fractional-map composition and strict concavity establish the finite-budget comparison. Nondegenerate Gaussian noise makes the second-stage Jensen inequality strict. In the high-initial-signal limit, the first update converges to minus its batch noise; chi-square scaling yields \(R_d(t)\). The derivative of this ratio changes sign exactly once because the mean of a monotone-likelihood-ratio tilted gamma law increases from below one to above one. Leave-one-out convex ordering establishes strict dimension monotonicity. The scalar complementary-error-function expression gives the numerical optimum. All required domain and boundary cases are handled in RESULT.md. The extracted `verify.py` passed 704 deterministic checks, which complement rather than certify the analytic proof.

## Originality — PASS, with bounded risk

The motivating equation (3.2) is previous work by Köhne, Kreis, Schiela and Herzog (arXiv:2311.16956). Generic minibatch complexity, including the rate/total-cost optimization of Gower et al. (arXiv:1901.09401), and adaptive batch-size sampling of Lau et al. (arXiv:2402.11215), are also previous work. These sources do not state, in materially inspected relevant sections, the exact sequential oracle-risk ordering together with the unique optimal high-signal Gaussian split and dimension-sharp constant. Searches of semantic mathematical records found closest results concerning fixed-template STORM, OHM, OSGM-SGD and Gaussian likelihood-ratio sample splitting; their claims do not imply this one. Possible unindexed equivalents and uninspected portions remain residual risks, so no publication priority is certified.

## Value — PASS

The problem asks a motivated and precisely budgeted question: does observing and reacting to an intermediate stochastic gradient improve accuracy under the same total number of individual gradients? The answer is exact for arbitrary independent centered additive noise and quantitatively sharp for the natural isotropic Gaussian high-signal limit. The analysis supplies a complete unique batch-ratio optimization and an exact diminishing-dimension advantage, rather than only a numerical case or a rate bound. The benchmark is population-oracle and ignores query overhead and parallelism; it is not advice to choose minibatches of a fixed size in practical training.

## Limitations and closest work

The high-signal 31.958...% constant is not asserted to be a finite-signal bound or a result for more than two blocks. Strictness requires nondegenerate Gaussian noise, and the result does not apply to the sampled estimators of the moment oracle without further analysis. Sources: arXiv:2311.16956 (equation (3.2)); arXiv:1901.09401 (section 4); arXiv:2402.11215 (sections 3–4).

Self-review: passed. Independent audit: not yet performed.
