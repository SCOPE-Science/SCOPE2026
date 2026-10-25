# Scientific review

## Correctness — PASS

The exact stationary renewal mixture has exponential reset age and a centered Gaussian excursion with covariance \(V(t)=2D(t+\gamma^2t^3/3)\). The positive-endpoint tail is localized by a unique nondegenerate saddle at age \(a\sqrt{x}\); Mills' ratio and Laplace's method yield Gaussian age fluctuations at scale \(x^{1/4}\). Exact Gaussian path regression gives uniform cubic and parabolic conditional paths. At the endpoint, the independent regression residual combines with random age to produce transverse limiting variance \(3Da/4\) and correlation \(-\operatorname{sgn}(\gamma)/\sqrt3\). All assumptions and limits are explicit. A standalone checker passes 177 deterministic kernel/quadrature tests. The numeric tests do not replace the analytic proof.

## Originality — PASS, with priority risk

The closest same mathematical model article, Abdoli–Olsen–Löwen (arXiv:2410.10333v1), provides shear propagators, stationary moments and a perturbative density, but not this conditional entire-excursion law. Singh (arXiv:2007.05576v1) supplies the random-acceleration joint stationary mixture and its marginal stretched-exponential tail; the marginal tail is **not** claimed as independently new. Meerson (arXiv:2302.04029) already obtains the complementary cubic bridge profile in a random-acceleration first-passage setting; the isolated cubic here is consequently **not** counted as original. These sources supply strong antecedents, but no verified theorem was found giving the stationary Poisson-age posterior bivariate Gaussian fluctuation law or its parameter-independent age–transverse correlation. The result follows by additional Gaussian posterior and Laplace analysis of known exact mixture formulas; a general unlocated conditional-mixture theorem might already imply it. Independent priority verification is needed.

## Scientific value — PASS

A large observed longitudinal displacement in a sheared, resetting colloidal model encodes a complete predictable path shape despite broad unconditioned dynamics; the nontrivial universal fluctuation correlation quantifies how longer excursions trade transverse displacement against excursion age. This is a concrete conditional-history prediction unavailable from the stationary variance, skewness or kurtosis studied in the source model. It distinguishes a measurable cross-coordinate rare-event observable from routine tail re-expression. The result is restricted to stationary complete resets and nonzero linear shear, with no claim about finite-sample reconstruction.

Self-review: passed. Independent audit: not yet performed.
