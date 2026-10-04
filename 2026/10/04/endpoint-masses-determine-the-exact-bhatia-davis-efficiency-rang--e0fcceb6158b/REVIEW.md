# Review

## Correctness

PASS. Positive affine normalization reduces the problem to support in \([0,1]\). Conditional variance shows that, at fixed interior conditional mean, every spread among the interior atoms can only increase the Bhatia--Davis efficiency. The remaining three-level problem is one-dimensional.

In odds coordinates, maximizing the Bhatia--Davis deficit reduces to minimizing
\[
a(1-a)z+\frac{c(1-c)}{z},
\]
whose unique positive minimizer gives the displayed support ratio and lower constant. Equality requires both this odds condition and zero conditional interior variance, explaining the exact distinction between three atoms and four or more distinct atoms.

The upper endpoint follows from the exact deficit
\[
\mu(1-\mu)-\sigma^2=\mathbb E[X(1-X)],
\]
which is strictly positive in the presence of a genuine interior atom and tends to zero under endpoint collapse. Connectedness supplies the complete attainable intervals.

## Originality

PASS, with an explicit residual risk from older variance and moment-problem literature. Audenaert's complete arXiv text was inspected through its real-variable variance section and classical sharp bound. Sharma--Gupta--Kapoor's complete nine-page article was inspected through its introduction and principal variance refinements. Ellis's open full article text was inspected through the finite-sequence extremal lemmas and theorems.

The prior literature fixes the support interval, or an equal-weight finite universe, or a prescribed mean. None of the inspected statements fixes arbitrary endpoint probabilities and asks for the exact range of the ratio
\[
\frac{\sigma^2}{(M-\mu)(\mu-m)}.
\]
Targeted exact-formula and semantic searches likewise did not locate the endpoint-mass floor or its attainment classification.

## Value

PASS. The Bhatia--Davis inequality is a standard variance bound used when the mean and support range are known. In finite categorical or empirical models, endpoint frequencies may also be fixed. The theorem quantifies exactly how much that additional information prevents the classical bound from being loose, and it identifies the unique three-point geometry that is worst for tightness.

The equal-frequency specialization
\[
\ell=\frac2m
\]
gives an immediate benchmark, while the general formula reveals the unexpected fact that the sharp floor depends only on the two endpoint masses and not on how the remaining probability is split.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK upper_checks=16000 lower_checks=13699 strict_lower_checks=11440 conditional_checks=41097 binary_checks=2301 equality_checks=8000 lower_approach_checks=48 upper_approach_checks=48 equal_mass_checks=48`.
