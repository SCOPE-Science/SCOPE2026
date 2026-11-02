# Scientific review

## Correctness — PASS

The exact Dirichlet interpolation identity gives a convex combination of translates for every mass-one nodal-nonnegative polynomial; convexity proves the upper bound. A real Fourier matrix at \(2K+1\) root phases is invertible, and near-grid phase perturbations leave its positive quadrature weights positive; those weights yield moment-feasible nodal Dirichlet mixtures. Localization around separated kernel singularities preserves the full Dirichlet \(L^1\) logarithmic coefficient. Positive analytic Poisson mixtures have identical prescribed moments, and nonexpansiveness of the metric projection gives convergence to the feasible extremizers. The factor converting normalized \(L^1\) mass into negative mass is checked. The standalone verifier exercises the finite identities; the infinite steps are proved, not extrapolated from computation.

## Originality — PASS (qualified)

The classic Dirichlet \(L^1\) asymptotic and the general nodal-positive interpolation representation are prior mathematics, so no novelty is claimed for those components or for the unrestricted \(K=0\) case. Cai, Lin and Lin (2023, arXiv:2304.11847v1, Sections 2, 3, 6 and 8) give the positive-at-nodes moment-preserving optimization and fixed-input accuracy but not this sharp fixed-low-Fourier-moment off-grid negative-mass supremum. The consulted Laiu–Hauck positivity-limiter source concerns a different angular spectral framework; its full mathematical body was not accessible and constitutes a residual overlap risk. The new joint conclusion, including positive moment quadrature and realization by strictly positive analytic data for every degree, was not identified in the inspected literature or mathematical-record searches. Classical Fourier norm inequalities imply the upper bound but do not independently establish matching moment-feasible analytic-input examples. Independent priority assessment remains necessary.

## Value — PASS

This is a motivated and sharp limitation of positivity-at-collocation implementations with conservation constraints. It quantifies the largest possible negative continuous-space mass, shows exactly why a fixed number of conserved Fourier modes cannot improve its leading logarithmic coefficient, and distinguishes uniform fixed-input spectral accuracy from resolution-dependent worst-case input design. The result is structural rather than a single arbitrary counterexample: the coefficient is sharp for every fixed positive number of moments and is realized asymptotically by a family of smooth admissible inputs. It does not claim typical-input failure, failure for kinetic polynomial moments, or relevance to all spectral schemes.

## Closest literature and residual risks

Primary comparison: Cai, Lin and Lin (2023), arXiv:2304.11847v1, fully inspected in relevant sections. Related prior tools: the classical Dirichlet-kernel Lebesgue norm, Hardy (1942); Laiu and Hauck (2018 online/2019 print), DOI:10.1007/s10915-018-0790-y, accessible abstract/preview only; Austin and Xu's trigonometric interpolation stability literature has a different rounding/shifted-grid target. The largest residual risk is a specialized approximation-theory result expressing the same constrained asymptotic through an equivalent norm or positive quadrature representation. The reported originality is qualified rather than a claim of exhaustive historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
