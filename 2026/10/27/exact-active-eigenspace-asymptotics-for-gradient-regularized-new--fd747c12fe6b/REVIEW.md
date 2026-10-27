# Review

**Correctness — PASS.** The spectral recurrence is exact. Positive denominators preserve every initially active eigenspace; geometric convergence makes the regularization vanish; the component-ratio limit selects the lowest active eigenvalue; and the norm and gradient constants follow by direct limits. Repeated eigenvalues are handled by the orthogonal spectral projector.

**Originality — PASS, with residual risk.** The primary paper's local theorem gives a general upper bound of order \(3/2\), not the exact asymptotic equality or the active-eigenspace direction. The Bregman-regularized and adaptive-power papers inspected likewise give broader convergence results rather than this exact fixed-iteration law. Targeted literature/database searches found related quadratic spectral analyses but no direct implication or exact match. Search absence is not proof of priority.

**Value — PASS.** The law identifies which curvature governs the eventual rate for a particular start, including cases where the globally smallest eigenspace is absent from that start. It sharpens a generic local upper bound into an exact rate constant and directional limit, which is useful for interpreting late-stage convergence on anisotropic quadratic objectives.

**Closest literature and limitations.** Mishchenko (arXiv:2112.02089v1, Theorem 2 and Appendix A.1); Doikov and Nesterov (arXiv:2112.02952v1, Theorem 4); Doikov, Mishchenko, and Nesterov (arXiv:2208.05888v1). The statement is limited to exact arithmetic and SPD quadratics; no exhaustive priority proof is claimed.

Self-review: passed. Independent audit: not yet performed.
