# Scientific review

## Correctness — PASS

The stated constrained problem is exactly reduced to the quadratic norm \(\|qf+F\|_2^2\) on clamped \(H^2_0\) with prescribed \(\|F''\|_2\). The beam spectral inequality and the parity of the cubic forcing supply a genuine global comparison identity. The explicit sine–sinh stationary family gives the unique symmetric optimizer below the first beam eigenvalue, while its simple even eigendirection gives exactly two optimizer branches above the computed critical dissipation. The exact series proves monotonicity of the subcritical energy parameter. Independent quadrature, boundary checks, and polynomial Galerkin tests support the formulas; they are not substituted for proof.

## Originality — PASS (bounded historical uncertainty)

The nearest direct comparison is Marbach–Alim (2019), whose Section III.C and Appendix D.3 obtain an optimal radial pipe flow under fixed mean and an \(L^2\) *velocity-deviation* budget, not a planar no-slip *velocity-gradient* budget. Ng (2010) treats a plane-channel fixed-flow-rate comparison but only within prescribed slip-driven Poiseuille families; it does not optimize all no-slip profiles under a dissipation constraint. Lunasin et al. (2012) treat finite-time scalar mixing on periodic domains rather than long-time Taylor–Aris transport. Taylor (1953) established the original mechanism, not the constrained maximizer classification. An undiscovered equivalent formulation in optimal-control or mixing literature remains a residual priority risk; negative search results alone are not a novelty certificate.

## Value — PASS

A physically motivated power/throughput tradeoff produces a mathematically sharp transition: a unique symmetric maximizing flow becomes a twofold mirror pair beyond only \(3.085\ldots\%\) excess dissipation. Exact formulas quantify the onset amplitude and the optimal high-budget slope, supplying a design boundary that is not merely a numerical optimizer, an arbitrary parameter slice, or a generic restatement of an eigenvalue inequality. Engineered forcing and possible backflow are explicit limitations, and no claim of a pressure-driven realization is made.

## Independent verification and limits

Analytical proof is present in `RESULT.md`; the reproducible `verify_taylor.py` verifies identities and finite approximations. Relative historical priority is not independently established, and the idealized steady linear channel assumptions remain necessary.

Self-review: passed. Independent audit: not yet performed.
