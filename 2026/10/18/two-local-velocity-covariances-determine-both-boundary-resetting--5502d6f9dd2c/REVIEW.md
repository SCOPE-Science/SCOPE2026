# Scientific review

## Correctness — PASS

The stated model assumes two independent stationary Brownian walls with the same known diffusion constant and finite positive resetting rates. The bulk Fourier response is the exact published starting point, and its cosine integral reduces to an explicitly normalized geometric spatial covariance. Introducing \(y=\rho/(1-\rho^2)\) gives the two measured quantities \(S=y_1+y_2\) and \(T=h(y_1)+h(y_2)\). Strict positivity of \(h''\) proves the full feasible wedge, uniqueness of the unordered pair, and sharpness/nonattainment of its upper boundary. Explicit inverses map recovered positive \(y_i\) to positive finite rates. The equal-rate and infinite-rate boundaries and nonidentification from a lone variance are separately addressed. The 218 independent numerical checks cross-validate the normalized kernel, reconstruction, and finite-chain second-moment limit, without being treated as an all-parameter proof.

## Originality — PASS, subject to independent priority assessment

R. Sarkar and P. Roy, arXiv:2307.06127, Section 4.2 and Appendix B, give the same *forward* velocity correlations; their general physics, spectral kernel, and full forward covariance are not new. Full source material was inspected, including the spatial correlation formulas and discussion. The inspected text does not derive a two-observable inverse, its necessary-and-sufficient attainable set, or the equal-rate identifiability boundary. R. Sarkar, I. Santra and U. Basu, arXiv:2210.09035 and arXiv:2404.00615, consider related but distinct active reservoirs and do not visibly contain this exact inverse result. General two-atom moment/Prony theory is known; the substantive distinction is that the common, known diffusion strength locks the two amplitudes to their rates, allowing *two* covariances rather than extra free-amplitude measurements. Semantic database searches and broad literature searches revealed no equivalent statement, but non-detection is not a uniqueness proof. Residual risk: an already published convex-moment or linear-chain inverse specialization could cover the result implicitly.

## Value — PASS

The motivating physical paper explicitly identifies spatial velocity covariance as a measurable signature of reservoir activity but solves the forward problem. Whether local bulk observations can recover wall-resetting parameters and reject impossible parameter pairs is a natural spectroscopy/identifiability question. The sharp two-number range, exact unlabelled uniqueness, equal-rate diagnostic, and square-root ill-conditioning characterize what can and cannot be inferred with a *minimal* local observable pair. The result is not a mere numerical reformulation of a hypergeometric formula: it produces an exact feasibility region and globally exhaustive inverse classification for a real physical model. No uniqueness of microscopic resetting among matched-covariance stochastic reservoirs is implied.

## Closest literature and remaining limits

The essential forward model and bulk kernel are prior in arXiv:2307.06127, Section 4.2 and Appendix B. arXiv:2210.09035 examines active boundary noise with different high-order statistics, while arXiv:2404.00615 uses an active Rubin bath. Alternative, more general inverse-moment results remain a plausible unruled-out priority source. All finite-chain and unknown-diffusivity extrapolations are excluded.

Self-review: passed. Independent audit: not yet performed.
