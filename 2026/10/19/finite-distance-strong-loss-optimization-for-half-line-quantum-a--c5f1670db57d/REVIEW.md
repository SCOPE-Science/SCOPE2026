# Review of finite-distance boundary-sink optimization

## Correctness — PASS

The normalized half-line quantum Hamiltonian and sink rates match the source's model. Starting from Riberi's exact absorption integral, differentiation establishes strictly increasing absorption through matched loss, vanishing endpoint probabilities for initial sites beyond the boundary, and a global strong-loss optimizer. A uniform-in-loss bound on the finite-distance correction localizes all global optimizers near the unique infinite-distance maximizer; a curvature estimate proves eventual global uniqueness. The exact beta integral yields the cubic displacement and sixth-order improvement. Separate direct truncated time-domain propagation checks the integral normalization. Numerical checks are not substitutes for the infinite-dimensional premise or asymptotic proof.

## Originality — PASS, with priority uncertainty

Riberi, arXiv:2605.08056v4, explicitly derives the complete absorption integral, leading reciprocal symmetry, and the qualitative convergence of its optimum to matched loss; these are prior facts and are not claimed. The material reviewed does not state strict finite-distance strong-loss optimality, eventual global uniqueness, the exact reciprocal difference, or their sharp \(s^{-3}\) displacement and \(s^{-6}\) improvement coefficients. His Appendix D.2 already supplies a two-term expansion that can be differentiated toward the shift coefficient, so this is a close natural extension, not a new transport model. Two further inspected primary papers treat finite coined walks with projective or programmable leaking boundaries, not the same continuous Lindblad dynamics or infinite-time optimum. Earlier implicit calculations and unindexed manuscripts remain an important residual risk.

## Value — PASS

The single-sink absorption probability is a physically motivated control objective and the matched rate is the published distant-source benchmark. The result determines exactly why that benchmark is never optimal at finite source distance, identifies the direction of optimal detuning, proves a unique optimum for sufficiently remote sources, and quantifies both the cubic adjustment and sixth-order performance gain. That vanishingly small gain is scientifically meaningful as a sharp calibration/error-budget threshold, not presented as a practically large transport improvement. No new general result for arbitrary graphs is claimed.

## Closest literature and limits

Riberi's Eq. (15) and Appendix D.2 are the closest premises and cover most of the model-specific absorption analysis. Ammara et al., arXiv:2508.13318v3, and Stefanutti et al., arXiv:2601.13269v2, study different finite coined/projective measurement protocols. The result does not prove uniqueness for every fixed finite source distance, and no independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
