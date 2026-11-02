# Scientific review

## Correctness — PASS

The centered-Gaussian formula reduces the normalized KL divergence to the three spectral means \(m\), \(h\), and \(\ell\) in equation (1) of RESULT.md. The second derivative in each eigenvalue is strictly positive: Cauchy--Schwarz bounds its mixed terms and AM--GM yields the positive factored lower bound \(a(1-a^{1/3})(2a^{2/3}+2a^{1/3}-1)\) for \(a=(k-1)/k\). Strict coordinate convexity forces every maximizer into the endpoint spectrum; substituting each endpoint multiplicity gives the exact formula and equality classes. A derivative-sign argument gives a unique continuous optimum; expansions yield both stated asymptotic regimes. The standalone verifier uses 2,600 exact-rational curvature tests, 4,180 mixed-spectrum/equality cases, and 207 integer-localization checks. These are consistency checks, not proofs of infinite statements.

## Originality — PASS, with limitations

The closest directly comparable work is Fifen, Karambal and Hennig, arxiv:2609.10080v1, Section 4.4, Theorem 13. Its stated sufficient KL upper bound is \(\tfrac12(\kappa-1)^2\) per dimension under the same trace-match, while the present exact dimension-dependent envelope and its endpoint multiplicities are not implied by that numerical upper bound or stated in the inspected theorem and proof. The Gaussian KL extremal results of Zhang et al. (arxiv:2102.05485) impose a bound on reverse KL rather than a spectral-condition interval. Alyani et al. (arxiv:1608.06613) use matrix diagonality relative to the diagonal part rather than scalar trace-matched isotropy. Research-record comparisons with covariance Riemannian metrics, ellipsoid quantiles and Lanczos matrix-exponential results concern distinct quantities and do not imply the proposed statement. Full historical completeness is not asserted: classical mean-product/entropy inequalities may conceal an equivalent older endpoint theorem; only the abstract of Zhang et al. was examined.

## Mathematical value — PASS

An explicit extremal classification is directly useful when the complement dimension and spectral spread of an inverse-covariance approximation are known. It replaces a generic quadratic-in-contrast sufficient penalty with a sharp spectral bound whose actual contrast growth is linear, identifies the exact worst two-level spectra and their discrete multiplicities, and includes the noncentral optimal proportion for finite contrast. The result does not claim a uniform guarantee for an unconstrained stochastic-Lanczos implementation, nor a new convergence theorem.

## Closest literature and remaining risks

Fifen–Karambal–Hennig (2026), Theorem 13, is the primary direct comparison (https://arxiv.org/html/2609.10080). Zhang et al. (2021, https://arxiv.org/abs/2102.05485), and Alyani–Congedo–Moakher (2016 preprint, https://arxiv.org/html/1608.06613v2) are related but do not specify the same extremal problem in the material examined. An inaccessible or unrecognized general mean-inequality theorem could establish the same spectral optimizer. The exact finite-dimensional sharpness is over all SPD spectra and may overestimate restrictions realizable inside a particular Krylov construction.

Self-review: passed. Independent audit: not yet performed.
