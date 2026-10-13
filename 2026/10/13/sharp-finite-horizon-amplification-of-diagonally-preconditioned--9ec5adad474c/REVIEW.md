# Scientific review: sharp finite-horizon amplification of diagonally preconditioned delta-rule erasures

## Correctness — PASS

For every finite dimension \(d\ge2\), every diagonal \(D\) with entries in \([1,\kappa]\), and every unit \(k\), direct orthogonal decomposition gives \(\|P(k,D)\|_2=\|Dk\|_2/(k^{\mathsf T}Dk)\). The elementary two-endpoint quadratic bound and its exact maximizer give the universal factor \(C_\kappa=(\kappa+1)/(2\sqrt\kappa)\). The explicit two-coordinate alternating pair is a transpose pair of rank-one projectors with matching norm \(C_\kappa\); its products have norm \(C_\kappa^N\) for every positive length. Embedded exact-rational calculations and finite randomized tests passed. The proof, not the tests, establishes the universally quantified result. The dimension-one exception is explicitly excluded.

## Originality — PASS, with residual risk

The motivating diagonal preconditioner and write-side key substitution are not novel, and the paper's Theorem 5.2 already establishes token-local residual contraction. It does not imply a bound on the norm of the *shared* memory state across changing keys. The classical oblique-projector identity and Kantorovich angular inequality cover the one-factor component; they do not alone give a matching every-length switched-product witness. Published weighted-projection convergence results use structurally constrained weighting or aggregation rather than arbitrary products of independently chosen rank-one erasures; orthogonal projection results address factors of norm one. The accepted distinction is an exact finite-horizon minimax law and two-periodic saturation in a restricted family of online memory updates. Research-record and primary-literature searches found no statement that already supplies that law. Equivalent formulations in older oblique-projection product literature remain a residual risk; the full text of one historically relevant SIAM article was unavailable, although a closely related later full-text article was inspected.

## Value — PASS

One-token perfect regression correction is frequently used as a local update diagnostic, but its consequences for repeated shared-state updates are subtler. The theorem gives a sharp condition-ratio-dependent global worst-case growth rate, including an explicit two-step example with unit keys, positive diagonal weights at most two, and scalar gate \(3/4\), so the obstruction is not an artifact of unbounded coefficients. The complete finite-horizon classification identifies the precise nonexpansive boundary and a design-relevant distinction between token-local and sequence-level control. It does not purport to prove instability of the learned preconditioner trajectory in any particular implementation.

## Closest literature and limitations

Zhou et al., arXiv:2605.13473v1, Sections 4 and 5 and Appendix A, is the direct motivating source. The one-factor norm geometry is classical; see Szyld (2006). For comparison with diagonal oblique feasibility iterations see Censor–Elfving (2003, full text) and Censor–Elfving (2002, abstract accessible). Kopecká (2020) treats products of orthogonal projections. These sources do not establish an equivalent sharp switching envelope under the stated diagonal bounds, on the inspected material. The result assumes exact arithmetic and arbitrary admissible switching rather than the specific learning law of a deployed optimizer. Older equivalence remains possible.

Self-review: passed. Independent audit: not yet performed.
