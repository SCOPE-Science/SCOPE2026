# Scientific review: exact equal-channel impurity splitting

## Correctness — PASS

The claim concerns the spectrum of the orthogonal compression of a bounded, rank-four positive onsite operator to a spectrally isolated flat band. The compact states form a Riesz basis because their Toeplitz Gram symbol is strictly positive at all allowed fluxes; the inverse Gram kernel is obtained by a directly normalized second-order recurrence. The physical projection and the four-coordinate reduction preserve all nonzero eigenvalues. The resulting Hermitian four-dimensional characteristic polynomial factors into two quadratics, giving the exact four eigenvalues and their two equal splittings. A gapped perturbation reduction then establishes only the first-order full-chain assertion, with its fixed-parameter \(O(\varepsilon^2)\) remainder. Independent symbolic algebra and finite-section diagnostics reproduce the polynomial, flux scaling and coupling ratio. Residual risk: transcription errors in translating the flux gauge or isolating the four eigenvalue branches; these were addressed with independent reconstruction of the Hamiltonian and multiple fluxes and separations.

## Originality — PASS

The closest 2024 primary study by Viedma, Marques, Dias and Ahufinger investigates *two separated* onsite-impurity pairs in Appendix A, extracting a half-gap numerically and reporting exponential separation dependence and approximately equal high/low couplings. Its full Sec. II and Appendix A were read and compared: the exact four-root polynomial, two-channel equality theorem, prefactor and exact ratio are not stated there. The preceding 2024 paper by Marques and collaborators derives a two-eigenvalue problem for *one* impurity pair and supplies the projection framework, not the joint four-mode spectrum. The result does not claim to discover the impurity bands, their qualitative exponential decay, or effective SSH chains. Equivalence and stronger-coverage searches revealed no closer theorem, but an indexed 2024 thesis with a related topic could not be inspected in full; independent priority review remains necessary.

## Value — PASS

The paper explicitly identifies the high-/low-branch near-equality as surprising and reports a numerical coupling ratio near \(0.17\). The new theorem explains the equality as a four-mode Gram-matrix identity, supplies its sharp flux-dependent exponential prefactor, and turns the ratio into \(3-2\sqrt2\). These quantities determine matching between the two effective impurity-channel hopping scales in designed photonic SSH arrays. The result is a motivated exact structural statement, not a parameter substitution or merely a higher-precision numerical fit.

## Limitations

The result concerns a one-particle infinite lattice, two impurity *pairs*, nonzero flux bounded away from endpoint regimes when taking small onsite strength, and first-order physical spectral splitting. It is not a many-impurity SSH spectrum or an exact finite-strength equality. Finite numerical checks are reproducibility aids. An independent literature and proof audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
