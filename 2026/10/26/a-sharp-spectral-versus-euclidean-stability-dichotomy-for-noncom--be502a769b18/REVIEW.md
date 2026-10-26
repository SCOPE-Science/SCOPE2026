# Scientific review

## Correctness: PASS

For finite-dimensional real symmetric positive-definite \(H,K\), the exponential-Euler map is exactly \(S_h=I-W_hK\), where \(W_h=H^{-1}(I-e^{-hH})\succ0\). Its similarity through \(K^{1/2}\) is symmetric, giving the if-and-only-if \(K\preceq2H\) spectral and common \(K\)-energy contractivity condition via the sharp limit \(W_h\to H^{-1}\). The separate similarity through \(W_h^{1/2}\) gives the Euclidean upper bound. An extreme-eigenvector swap supplies the sharp \(\sqrt{\kappa_2(H)}\) supremum; the rank-one limit and continuity prove positive Euclidean amplification for every fixed positive step when \(H\) is nonscalar. The exact rational two-state witness is separately verified by the included standard-library checker. Finite numerical checks are corroboration, not replacements for the quantified analytical proof.

## Originality: PASS (best-knowledge assessment)

Caliari--Cassini--Einkemmer--Ostermann, arXiv:2303.15861v1, Theorem 2.1, prove scalar Fourier-mode stability for a commuting heat-operator split. D'Autilia--Sgura--Simoncini, arXiv:1903.05030, analyze scalar-mode and matrix-oriented reaction-diffusion integration, not the quantified all-step noncommuting SPD Loewner result and sharp Euclidean amplification theorem. The relevant published-finding corpus records for weighted Jacobi Euclidean damping, two-step Richardson and two-coordinate Gauss-Seidel concern distinct iteration families, and their summaries do not state or logically dominate this combined result. Elementary facts on preconditioned Richardson and symmetric similarity are prior-known and not asserted as original in isolation. The assessed new object is the exact noncommuting exponential-Euler family with a necessary-and-sufficient stability criterion, universal sharp amplification constant and impossibility of a Euclidean-safe positive step under nonscalar splitting. No covering claim was identified in the accessible records, but this is not a uniqueness proof. A 2026 related splitting paper was available only at abstract level; specialized unpublished or uncatalogued results remain a genuine priority risk.

## Value: PASS

The source's scalar stability threshold does not distinguish stability in physical energy from possible one-step amplification in Euclidean solution error. This distinction directly affects damping/step choices for matrix-based exponential time integrators with spatially variable noncommuting SPD operators. A sharp condition \(K\preceq2H\), a dimension-free best possible amplification factor \(\sqrt{\kappa_2(H)}\), and an impossibility result for *every* chosen positive step are structural, testable design information rather than an arbitrary finite parameter slice. The result does not assert higher-dimensional PDE discretization convergence, nor an error-amplification trajectory for one fixed \(K\) at all steps.

## Closest literature and limitations

- Caliari, Cassini, Einkemmer and Ostermann (2023), arXiv:2303.15861v1, Theorem 2.1, commuting scalar spectral criterion; full motivating sections examined.
- D'Autilia, Sgura and Simoncini (2019), arXiv:1903.05030, Sections 2 and 4.1, reaction-diffusion and scalar spectral analysis; relevant primary material inspected.
- Published published-finding corpus statements on weighted-Jacobi Euclidean damping and safe two-step Richardson; summary-level implication comparison only.
- Related arXiv:2610.07989 (2026), available abstract only; full text not inspected. General preconditioning literature may contain equivalent consequences, and independent priority verification is needed.

Self-review: passed. Independent audit: not yet performed.
