# Self-review

## Correctness
PASS. The proof derives the fractional-logistic cumulant formula from two independent positive stable variables and an explicit Stieltjes identity. Stieltjes inversion yields a normalized density and its quantiles in elementary trigonometric form. Empirical quantile discretization matches the limiting log-MGF and its derivatives. Chernoff bounds and explicit exponential tilting yield both one-sided logarithmic tail rates. Strict monotonicity of the common Cramér rate and a contradiction at arbitrary quantile levels imply \(W_\infty=o(N)\). The mathematical argument controls extreme quantiles, not just the central limit region. Small finite computations are supplementary only.

## Originality
PASS. Tang and Tang's 2019 full-text Open Problem 4.6 asks for \(o(n)\) strong-Rayleigh approximation to \((2/3)\mathrm{Bin}(3n,1/2)\). Their fixed homogeneous and equispaced Bernoulli constructions have linear errors, and no sublinear approximation is proved there. Mattner's 2022 first-few-moments extremizer theorem does not imply the present full-rate/transport result. The Lamperti ratio law is classical and is cited as such, while its use for the explicit Bernoulli quantile approximation and rate-to-transport upgrade supplies the new theorem. Targeted semantic and equivalent-formulation searches located no dominating assertion. Implicit earlier coverage under generalized stable-ratio terminology remains a bibliographic risk.

## Value
PASS. A specific open asymptotic optimal-transport question is positively answered, with an explicit, reproducible heterogeneous Bernoulli construction and a structural large-deviation mechanism. The result also extends from rational \(2/3\) to all real \(0<\alpha<1\) without changing the argument. It is not an arbitrary narrow parameter calculation or merely a consequence of mean/variance matching.

## Closest literature and limitations
Tang and Tang, arXiv:1908.10024v1, Section 4 Open Problem 4.6, is the direct source. Mattner, arXiv:2204.06040v1, treats finite-moment extremal expectations with primary MSC 60E15. The stable-ratio background appears in James, arXiv:0708.0618. The stronger conjectured \(O(1)\) coupling and its exact optimal constant remain unresolved by this theorem.

Self-review: passed. Independent audit: not yet performed.
