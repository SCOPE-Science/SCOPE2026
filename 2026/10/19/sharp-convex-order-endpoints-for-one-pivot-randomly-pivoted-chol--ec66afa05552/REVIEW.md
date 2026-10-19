# Scientific review

## Correctness — PASS

The exact pivot trace gain is \(G_A=(A^2)_{II}/A_{II}\) with pivot probability \(A_{II}/\operatorname{tr}A\). A size-biased eigenvalue index followed by the eigenvector squared-entry transition realizes precisely this pivot distribution and makes the gain a conditional expectation of the sampled eigenvalue. Conditional and ordinary Jensen inequalities prove the two convex-order bounds. Their upper endpoint is realized in an eigenbasis; their lower endpoint is realized by the inductive real/complex zero-diagonal basis for the traceless Hermitian matrix \(A^2-qA\). A continuity argument establishes every variance between the sharp spectral endpoints. The \(2\times2\) example is exact. The included numerical checks were executed successfully and are supporting checks, not an exhaustive proof.

## Originality — PASS, subject to the documented residual risks

Chen, Epperly, Tropp and Webber, arXiv:2207.06503, establish the RPCholesky pivot law and the expected residual map \(A-A^2/\operatorname{tr}A\). Steinerberger, arXiv:2404.11487, addresses alternative pivot weights and expected trace/Frobenius behavior, and uses a pointwise Cauchy–Schwarz bound sufficient to derive the variance upper inequality. That inequality is credited as prior mathematical coverage; it does not assert all-convex domination, a real zero-variance basis, or simultaneous endpoint attainability. Epperly, Tropp and Webber, arXiv:2410.03969, study accelerated simulation of the pivot law. These examined statements do not imply the present simultaneously attained all-convex risk envelope or the deterministic-gain real orthogonal basis. Targeted mathematical searches did not identify a covering result, although this is not a proof of novelty. A related known one-pivot comparison of sampling exponents controls expected progress only, not dispersion. Classical conditional Jensen and zero-diagonalization principles are used, not claimed as new discoveries. Potential equivalent formulations in stochastic-order literature and incompletely examined appendices remain explicit risks.

## Value — PASS

Expectation guarantees alone cannot decide how variable a single low-rank approximation step will be. Here identical spectra and the identical known mean permit a complete, exact interval of variances; the \(2\times2\) witness changes variance from \(36/25\) to zero merely by orthogonally changing coordinates. The classification of every convex risk functional is motivated by stochastic reliability rather than by selecting an arbitrary parameter. It is finite-dimensional and one-step, but full-dimensional in its quantifiers and sharp at both endpoints.

## Scientific limits

Only one exact diagonal-proportional pivot is covered. Basis-balancing generally needs costly matrix-wide information and is not a plug-in acceleration guarantee. Convex-order comparison does not give ordinary stochastic tail dominance, a pathwise residual-matrix inequality, or multi-step behavior. Literature equivalence risks are recorded in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
