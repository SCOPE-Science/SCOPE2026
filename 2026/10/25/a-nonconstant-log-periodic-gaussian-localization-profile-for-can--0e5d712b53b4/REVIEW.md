# Scientific review: nonconstant log-periodic Cantor-annulus Gaussian eigenvalue

## Correctness — PASS

The finding is the uniform asymptotic for the **zeroth Hermite eigenvalue**, not a claim about the complete localization norm. The starting finite product is derived by digit factorization and is also documented in Knutsen's 2020 article. Splitting at the integer part of the base-three logarithm of the radial-area parameter yields two convergent products. Each missing tail has an explicit signed logarithmic bound, leading to the two-sided relative error in RESULT.md. The scaling exponent follows from \(3^{\log_3 2}=2\). The infinite series for the logarithmic derivative is locally uniformly convergent. Its strict negativity at one point is confirmed by a finite *rational* inequality, not by rounded floating-point values. The accompanying checker verifies the finite identities and rational certificate. The domain \(A\ge1\), \(A<3^n\) excludes unhandled boundary and denominator limits. The asymptotic conclusion additionally assumes \(A\to\infty\) and \(A/3^n\to0\).

## Originality — PASS (best knowledge, not independently certified)

Relevant searches for Cantor, Gaussian STFT localization, the vacuum eigenvalue, logarithmic periodic modulation, Mellin/Laplace asymptotics, and radial Toeplitz spectral oscillations produced no explicit statement of the same nonconstant leading profile together with its remainder. The closest primary results are Knutsen (arXiv:1907.00848, first posted 2019-07-01) and his sequel (arXiv:2104.10976): the former contains the **exact finite product** and order-of-magnitude bounds for the full operator norm; the latter generalizes to other digit alphabets and establishes some exact Gaussian extremizers, but does not give this middle-third nonconstant asymptotic multiplier. Abreu–Mouayn–Voigtlaender (arXiv:2201.11705) considers a hyperbolic Bergman Cantor analogue and comparable norm bounds, not this Fock Gaussian eigenvalue refinement. Prior exact finite-product knowledge is openly acknowledged and not claimed original.

The main priority risk is that a general older log-periodic Laplace-transform theorem might already imply this particular refinement; a mathematical identity can be derivable from an old finite formula even when its asymptotic structure was not previously spelled out. The special quantitative *nonconstancy* certificate and uniform two-sided remainder provide the distinct content of the reviewed claim. Independent priority review remains needed.

## Mathematical value — PASS

This resolves a natural question left open by constant-factor Cantor concentration estimates at the level of a canonical test vector: whether a single normalization constant describes its leading spectral mass. It does not. Instead the leading coefficient retains a nonzero logarithmic phase dependency for every sequence in a wide double-scaling regime. The explicit product gives its values, while the rational derivative certificate proves the effect cannot be removed. This is a structural boundary on proposed sharp asymptotics, not a renaming of the finite product or an arbitrarily selected numerical case. It may guide analysis of the full norm, but no full-norm consequence beyond the known Gaussian lower bound is claimed.

## Scope and risks

The norm of the operator is only known here to be between this eigenvalue and twice this eigenvalue. Other Hermite modes and the possibility of a different norm-leading phase profile are not settled. The small size of the periodic modulation does not diminish its exact nonconstancy, but applications requiring a large signal should not be inferred. Primary source comparison is strong for the directly relevant works but not an exhaustive audit of the classical fractal-Laplace literature.

Self-review: passed. Independent audit: not yet performed.
