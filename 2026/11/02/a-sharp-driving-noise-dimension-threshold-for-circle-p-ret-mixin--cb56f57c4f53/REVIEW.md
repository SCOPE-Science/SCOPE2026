# Self-review

**Claim tested.** The exact noise-dimension threshold at \(r=2\) for the scalar circle p-Ret operator, its Fourier contraction, point-started mixing, and mean-zero discrete Poisson inversion, all with fixed positive step and the same diffusion tensor.

## Correctness: PASS

The calculation of the transition from the published p-Ret definition was reconstructed in the circle parameterization: metric one, zero Christoffel symbol, zero drift, \(r\) identical fields with covariance one, and a projected uniform-sphere increment. The sphere density and Bessel Fourier multipliers follow from a beta integral. For \(r\ge2\), absolute continuity, strict characteristic-function inequality and Fourier decay force a strict spectral gap and a bounded Poisson inverse. The Bessel asymptotic guarantees an \(L^2\) two-step density and hence geometric total-variation mixing. For \(r=1\), elementary Fourier arithmetic proves the exact operator norm; a continuous forcing with an unsquare-summable Poisson solution is constructed using distinct near-resonant frequencies. The verifier passed 377 supplementary checks. It is not used as a proof of infinite-frequency statements.

## Originality: PASS with specified limitations

The 2026 p-Ret paper supplies the transition and finite-time weak analysis, not the long-time threshold or the same-generator noise-dimension comparison. Older Su (1998) and Berkes–Borda (2023) study the classical two-point circle walk, so that part is explicitly treated as antecedent, not claimed independently novel. General Fourier theory also underlies the proof. The new classification concerns the factorization-sensitive p-Ret discrete Poisson problem and transition from atomic arithmetic obstructions to geometric mixing while the continuum diffusion tensor is held fixed. indexed mathematical-record and accessible own-history queries found no direct covering result. Risk: more general compact-group convolution results may imply parts of the classification, and complete older full texts were inaccessible.

## Mathematical value: PASS

The diffusion factorization is not merely a notational choice in the numerical scheme: adding one redundant driving coordinate changes long-time numerical ergodicity and invertibility of the discrete Poisson operator even though the local heat generator is identical. This gives a motivated sharp design boundary for stochastic geometric solvers and for using fixed-step walks to compute stationary Poisson responses; it is not a toy unmotivated coefficient calculation. It does not assert an improvement in finite-horizon RQMC error or universal behavior on other manifolds.

## Literature and limits

Main source: He et al., arXiv:2610.23341v1, full HTML Sections 2.1–3. Closest classical references: Su, *Trans. AMS* 1998; Berkes–Borda, *JLMS* 2023. Their accessible abstracts and bibliographic records were inspected; primary full texts could not be retrieved in this execution. Broad Fourier antecedents and any specialized older p-Ret ergodicity analysis remain residual historical risks.

Self-review: passed. Independent audit: not yet performed.
