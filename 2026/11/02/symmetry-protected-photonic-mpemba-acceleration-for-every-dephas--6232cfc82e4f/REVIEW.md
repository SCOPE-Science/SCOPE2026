# Scientific review: symmetry-protected three-site photonic Mpemba acceleration

## Correctness — PASS

The model is the exact single-particle, open-path, continuous-time Lindblad generator in Longhi (2024), with \(J,\gamma>0\). The nine-dimensional Hermitian operator basis yields two scalar blocks, an even cubic, an odd quadratic, and an additional odd quadratic. The cubic has one real and one conjugate eigenvalue pair for all positive \(\gamma/J\), as its discriminant is strictly negative. Routh–Hurwitz applied after shifting by the leading odd quadratic rate proves a *strict* even-to-odd spectral separation across the full parameter range, including the odd exceptional point. Cyclicity of both initial deviations verifies nonzero projection onto the respective leading sector modes. A local entropy Taylor expansion then gives the claimed logarithmic rates and eventual reversal of relative-entropy ordering. Exact symbolic block reconstruction and independent matrix spectra are reproduced in `check.py` (387 checks). The numerical checks support, rather than replace, the algebraic proof.

## Originality — PASS, with explicit residual priority risks

Longhi (2024) supplies the exact underlying model and entropy criterion, reports an example with nine sites, and proves center-mode exclusion in the *strong-dephasing classical limit* for odd chains. The new theorem is the all-positive-rate exact three-site spectral comparison and explicit strict state-pair consequence, with both limiting acceleration constants. The later 2025 continuous-in-space but discrete-in-time quantum-walk study and 2026 three-node Floquet experimental study involve stroboscopic dephasing, a triangular coupling/flux or internal coin and do not imply the continuous Lindblad path's cubic-vs-quadratic inequalities. A 2026 many-body symmetry-filtered Mpemba preprint establishes the broad mechanism elsewhere but does not provide this exact model-specific classification. Targeted searches, including eigenvalue, parity, Liouvillian and three-site aliases, identified no directly covering theorem. The original 2024 supplemental document was described in the main text but could not be fully examined; its stated scope is strong-dephasing classical modes. Exhaustive publication priority is not certified.

## Mathematical value — PASS

The central question is the smallest open-path quantum walk supporting an exact far/near state-pair relaxation reversal. The theorem distinguishes full quantum dephasing from the previously explained classical limit, proves the effect survives *all* positive coherence strengths without a rate threshold, and gives analytic sharp relaxation exponents and a real/oscillatory changeover. This is a motivated, complete three-site classification rather than a minor numerical improvement. It does not claim larger-chain universality, a uniform crossing time, or physical transitions from a sectoral spectral change.

## Limitations and references

The calculation assumes a single particle, a three-site open chain, equal positive hopping, Markovian dephasing and the specified initial states. It does not prove analogous statements for interacting, disordered, or discrete-time models. Principal references: Longhi (2024), arXiv:2408.03296v1; Longhi (2025), arXiv:2508.11947v1; Huang et al. (2026), arXiv:2606.15935; Wei et al. (2026), arXiv:2605.20930.

Self-review: passed. Independent audit: not yet performed.
