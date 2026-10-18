# Independent mathematical audit

## correctness

PASS

On the first step, the pre-trust coordinates are r_i=A x_i/(B|x_i|+epsilon) with A,B>0, preserving signs and magnitude ordering. Sort magnitudes and decompose r magnitude into nonnegative prefix-indicator vectors; each prefix has dot product with x at least ||x||||prefix||/√d. Summing and using triangle inequality gives C(x)=<x,r>/(||x||||r||)>=1/√d. Family x=(M²,M,...,M), M→∞, makes normalized x→e1 and normalized r→uniform, attaining the infimum in the limit. Exact quadratic expansion then yields 1−2η C+η², sharp supremum and thresholds. This requires epsilon>0, no decay, one layer and only the first step. Independently checked the ratio and sharp family numerically across several dimensions, corroborating rather than proving the inequality.

## originality

PASS

Best-of-knowledge PASS for the dimension-sharp isotropic first-step LAMB threshold under phi(z)=z. You et al provide the base LAMB algorithm; Resultary separately has a sharp 2D *anisotropic* conditioned SPD ascent/angle boundary and a LARS (different optimizer) step threshold, neither entails this dimension-only isotropic universal first-step objective criterion.

## value

PASS

Demonstrates a nontrivial dimension scaling obstruction to guaranteed descent despite perfect quadratic conditioning, attributable to two successive normalizations; supplies a sharp usable safety frontier for a canonical algorithmic first-step regime, with exact extremizing family and boundary interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
