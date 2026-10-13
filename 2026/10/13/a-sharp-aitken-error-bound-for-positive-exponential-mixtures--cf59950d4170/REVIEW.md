# Self-review

## Correctness
PASS. With current modal weights and \(a=1-\lambda\), the Aitken residual ratio is exactly
\[
1-\frac{\mathbb E[a]^2}{\mathbb E[a^2]}
=
\frac{\operatorname{Var}(a)}{\mathbb E[a^2]}.
\]
For \(m\le a\le M\), \((a-m)(M-a)\ge0\) gives
\[
\mathbb E[a^2]\le(m+M)\mathbb E[a]-mM.
\]
Optimizing the resulting one-variable rational function yields the exact constant
\[
\left(\frac{M-m}{M+m}\right)^2.
\]
Equality requires endpoint support and the displayed endpoint weights. The embedded exact-rational verifier reproduces the identity and equality witness.

## Originality
PASS. The inspected classical full text derives Aitken's transform from a single geometric mode and explicitly analyzes a two-geometric-mode model, but does not state the arbitrary-positive-mixture sharp endpoint bound. Targeted statement-level literature searches covered Aitken/Shanks, positive exponential sums, completely monotone and Hausdorff-moment terminology, spectral measures, no-overshoot behavior, and the displayed endpoint structure. No implication-equivalent statement was located.

Residual risk remains that older extrapolation literature may encode the same inequality through moment-sequence terminology.

## Value
PASS. Positive spectral mixtures are a standard structural error class for self-adjoint positive iterations. The result turns Aitken's qualitative acceleration mechanism into an exact sign-safe finite-index worst-case guarantee and shows that, using the same three scalar values, Aitken strictly improves on the raw two-step worst-case factor in the one-sided spectral case.

## Closest literature and limitations
Weniger's Section 5.1 is the closest full-text source: it contains exact one-mode elimination and a two-mode formula. Pereyra supplies an archive-era Aitken/65B05 field anchor. The theorem assumes positive coefficients and nonnegative rates and concerns one three-point Aitken transformation; signed modes, repeated transformations, and floating-point cancellation are outside scope.

Self-review: passed. Independent audit: not yet performed.
