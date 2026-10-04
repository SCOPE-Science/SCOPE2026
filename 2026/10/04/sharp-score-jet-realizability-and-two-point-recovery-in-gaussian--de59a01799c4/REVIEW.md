# Same-model review of Sharp score-jet realizability and two-point recovery in Gaussian empirical Bayes
## Correctness
**PASS.** The proof differentiates the published Gaussian posterior moment-generating identity to obtain the first four posterior cumulants, then proves Pearson's inequality directly as a nonnegative squared residual. Substitution yields the claimed score-jet inequality, and the same squared-residual proof gives the exact equality condition. Strict positivity of the Gaussian likelihood preserves support from prior to posterior. Exact two-point moments and Bayes odds give the stated reconstruction formulas. The verifier checks representative equality, strictness, and violation cases with rational arithmetic.

Risk: finite fourth posterior moment and local differentiability are assumed. The theorem is necessary, not sufficient, for global Gaussian-convolution realizability.

## Originality
**PASS.** Sugasawa–Zhao (arXiv:2609.11136v1) establishes score-based posterior MGF recovery, Pericchi–Sansó–Smith gives broader posterior-cumulant identities, and the skewness-kurtosis literature gives Pearson's inequality and its two-valued boundary. Targeted searches for Tweedie formulas, posterior skewness/kurtosis, score derivatives, Pearson inequality, and two-point priors did not locate the combined differential constraint, the equality-at-one-observation prior characterization, or the explicit local recovery formulas. Published-record searches returned nearby cumulant and moment results in different models but no dominating statement.

Residual risk remains because the full primary text of the 2026 preprint and the 1993 JASA article were not both accessible during inspection. The claim is therefore limited to the specific score-jet inequality plus equality characterization and recovery formulas established here.

## Value
**PASS.** Conditional score modeling uses score derivatives for posterior uncertainty, so a realizability constraint on those derivatives is directly motivated. The theorem is strictly stronger than the standard nonnegative-variance check, as shown by the explicit smooth-density counterexample. Its sharp boundary is structurally informative: one local equality identifies and reconstructs a global two-point conditional prior.

Same-model review: passed. Independent audit: not yet performed.
