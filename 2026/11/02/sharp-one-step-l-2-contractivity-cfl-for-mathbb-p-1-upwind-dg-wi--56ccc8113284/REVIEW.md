# Scientific review

## Correctness — PASS

The exact spatial symbol follows from the weak degree-one DG element equations with upwind flux. The third-order SSP Runge–Kutta polynomial and physical mass matrix specify the complete fully discrete linear operator without approximation. Direct polynomial multiplication yields an exact formula for the leading energy decrement and its determinant, with the coefficient identities certified over the rational polynomial ring by `VERIFY.py` and degree-bounded interpolation. All eighteen Bernstein coefficients of the leading decrement are explicitly positive on the relevant parameter rectangle. Factor signs and monotonicity of the quartic establish positive semidefiniteness at all Fourier angles through the stated endpoint. Above the endpoint, the determinant is strictly negative for arbitrarily small nonzero angles, providing genuine real grid-level witnesses. The zero Fourier angle and the zero time step are handled separately. The numerical test supplements a complete infinite-frequency proof; it is not the proof by finite sampling.

## Originality — PASS, subject to residual historical-priority risk

The motivating 2026 article studies nonlinear entropy stability and compact stage-local DG approaches, and does not report this sharp global quadratic-energy boundary for the unmodified, uniform-grid, degree-one upwind symbol advanced by standard SSPRK3. Sun and Shu's general strong-stability theorem implies the existence of useful small-step bounds, not the exact critical algebraic constant or the long-wave necessity construction. The 2010 Zhang–Shu paper has almost exactly the same broad numerical scheme and proves an unspecified sufficiently-small CFL stability condition in its accessible abstract. Its complete text was not available for comparison; if it contains the same sharp uniform constant, priority would be lost. This risk cannot be ruled out by a title-level or abstract-only check. A 2025 paper by Wei and Shu proves cell entropy statements for a different family of third-order methods; its source distinguishes its methods from standard SSPRK3. The theorem is not claimed to be the first RKDG \(L^2\) stability result; it supplies a sharp fixed-degree uniform threshold with constructive necessity.

The compared statements differ substantively: a general existence-of-\(\gamma\) theorem does not entail the maximal universal \(\gamma\) or identify long-wave loss; nonlinear entropy failure does not imply quadratic-energy failure in a linear problem; cellwise entropy estimates for other integrators do not specialize to this full-grid SSPRK3 symbol. Publicly searchable related DG/SSP literature did not reveal an equivalent exact quartic. A missed unpublished, older, or differently formulated Fourier-symbol calculation remains possible.

## Value — PASS

A sharp contractivity threshold is mathematically meaningful because spectral stability or asymptotic consistency alone does not guarantee prefactor-one energy decay of the discrete step. The exact positive boundary and long-wave obstruction quantify the distinction in the canonical degree-one DG example and provide a reproducible benchmark for fully discrete energy/entropy analyses, especially where the motivating work shows nonlinear entropy limitations. The theorem does not overclaim a general nonlinear entropy method, higher-degree boundary, or stability of every fixed grid at every larger CFL.

## Reproducibility and limitations

Execute `python VERIFY.py` to reconstruct exact rational identities and Bernstein certificates using only the standard library. The proof and relevant assumptions are given in `RESULT.md`. The key scientific limitations are the single-dimensional constant-coefficient periodic transport equation, exact spatial integration, unmodified upwind flux, degree-one space and standard SSPRK3. Independent external review and complete inspection of one closely related archival primary text remain outstanding.

Self-review: passed. Independent audit: not yet performed.
