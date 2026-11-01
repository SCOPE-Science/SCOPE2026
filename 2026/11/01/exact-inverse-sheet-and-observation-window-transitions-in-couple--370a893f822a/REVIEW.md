# Self-review

## Correctness

**PASS.** The proof supplies a global smooth output-coordinate inverse and verifies the exact identity with the Cartesian product of scalar cubics. Scalar derivative sign changes give the complete real-fiber counts, including double-root targets; a block-row elimination establishes the full Jacobian determinant. The bounded-window result is not inferred from examples: it proves the sharp scalar three-root enclosure radius using monotone outer root branches, then constructs attaining targets by setting the original first-coordinate vector to zero. The standard-library checker independently confirms 90 exact rational cases, full Jacobian determinants, and exact exponential-multiplicity examples.

## Originality

**PASS, qualified by historical-priority risk.** The motivating 2026 article introduces this ring update and studies synchronization numerically, not the explicit inverse-coordinate normal form or the observation-window multiplicity thresholds in its inspected model and numerical sections. General critical-curve literature proves the one-dimensional cubic root behavior, which is not presented as new. The new statement combines it with a global network-specific output diffeomorphism and a sharp \(1,2^N,3^N\) window classification. A related published analysis of homogeneous-equilibrium Schur stability concerns forward local stability, not inverse preimages. Full text of some older noninvertible-map references and the related stability analysis was unavailable; priority therefore is not independently established.

## Mathematical value

**PASS.** Inverse multiplicity and location of critical manifolds determine whether backward state reconstruction is unique, a structural issue distinct from the attracting clusters observed in the source. The theorem gives all-target exact fiber counts and a natural finite-data answer: the initial \([-1,1]^{2N}\) range used in the motivating numerical study is one-to-one for both source parameter regimes, yet the unrestricted update has \(3^N\) preimages of zero. The two sharp window thresholds explain why global folding can be invisible on bounded initial-data domains. These are complete classifications for a natural model, not a parameter-specific finite computation.

## Closest sources and limitations

Fatoyinbo–Ghosh, arXiv:2607.03686v1, Sec. II equations (1)–(7), supplies the exact update and experimental ranges. Mira, *Noninvertible maps* (Scholarpedia 2007), supplies general cubic inverse-zone and critical-manifold background. The 2023 paper *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps* treats a different coupled map; available section 3.1 is generic critical-set theory. A published homogeneous-equilibrium classification of the same ring is closer in object but different in claim. Historical coverage is not exhaustively ruled out because some source full texts could not be inspected. The theorem is one-step and says nothing about iteration conjugacy or attractor classification.

Self-review: passed. Independent audit: not yet performed.
