# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The modal characteristic equation was checked against the source model. Writing a positive imaginary root as
\[
K+i\omega=K_p e^{i\alpha}-K_n e^{-i\beta}
\]
and using half-sum/half-difference phases gives the exact modulus identity
\[
\omega^2=4K_pK_n\sin^2 s,
\]
followed by the phase reconstruction of both delays. Reversing the algebra verifies the converse, so the parametrization covers every positive-frequency imaginary root. Negative-frequency roots of a real ring are covered by the conjugate Fourier mode.

For equal delays, the characteristic equation reduces to a scalar one-delay equation. The factorization in RESULT.md gives the closed phase difference and hence the first positive-delay crossing. Implicit differentiation gives a strictly positive real crossing speed. The monotonicity argument for the modal threshold was checked separately in the two ranges \(\tan(\theta/2)\ge1\) and \(<1\). The \(N=2\) edge case is handled directly by a modulus contradiction. A compact verification artifact reproduces the stated \(K_p=2,K_n=1,N=20\) crossing and characteristic residual.

The statement about bounded nonconvergent behavior is deliberately spectral and robust: a finite ring has finitely many modal retarded characteristic equations, and their imaginary-root parameter set is a countable union of analytic curves. Off that set, a transverse spectral abscissa is nonzero. Special histories that annihilate unstable eigendirections, and multiple-root polynomial behavior on switching curves, are explicitly excluded from any stronger claim.

## Originality

**PASS, to the best of our knowledge.** The source paper derives the Fourier-mode characteristic equation and only implicit real/imaginary stability-boundary equations, then uses numerical phase diagrams and names sharper analytical boundary conditions as future work. It also interprets a numerically observed band as a third bounded nonconvergent regime.

Searches by the exact source title, arXiv identifier, signed-ring terminology, switching-curve terminology, common-delay threshold terminology, and equivalent delayed-consensus formulations found no later correction or source-specific derivation of the formulas in RESULT.md. General two-delay frequency-domain/CTCR methods, Lambert-W representations, Fourier diagonalization of rings, and retarded-DDE spectral theory are established tools and are not claimed as new.

A closely related 2026 paper on heterogeneous constant delays and signed Laplacians studies a different graph-theoretic formulation and gives consensusability conditions rather than the present ring-specific switching parametrization and exact common-delay threshold. Its abstract and bibliographic record were inspected; its complete text was not independently inspected, so it remains a low residual originality risk. No evidence of direct coverage was found.

## Value

**PASS.** The result turns the source's implicit switching conditions into a complete source-specific parametrization, supplies a sharp universal frequency bound, and gives an explicit all-\(N\) common-delay consensus margin with strict mode ordering and a large-ring limit. It also removes a potentially misleading qualitative interpretation: for this finite-dimensional linear retarded model, neutral bounded behavior cannot occupy an open region of delay space. These statements sharpen both the analytic boundary problem and interpretation of the numerical phase diagram.

## Limitations

The theorem is restricted to \(K_p>K_n>0\), where the zero-delay transverse system is stable. It does not classify other coupling orderings, nonlinear models, switching graphs, noise, or time-varying delays. The no-open-bounded-phase statement concerns robust transverse spectral behavior, not every specially prepared initial history. The first-loss theorem is for the equal-delay diagonal; the full two-delay formulas parametrize switching curves but do not label every connected stability cell.
