# Review of the rank-two random-removal theorem

## Correctness — PASS
The rank-two pseudoinverse normalization, continuous uniform angular law, maximal-feasible rank-one subtraction, exact quadrant integral, and two generalized eigenvalues were reconstructed. The isotropic case and singular ambient directions are covered, and the high-eigenvector projector proves sharpness. The exact-rational and numerical checker passed on its actual packaged source; the analytical proof, not finite checking, establishes the universal quantifiers.

## Originality — PASS, with residual risk
The motivating 2025 preprint/2026 full journal article specifies the stochastic coefficient but uses pointwise eigenvalue bounds and unweighted direction moments; its proof was compared directly against the joint matrix expectation and sharp PSD comparison claimed here. Related published research searches and existing scientific records found spectral, rank-one and Frank–Wolfe results but no covering joint rank-two certificate. The newer deterministic follow-up is a different algorithm. Standard quadratic-form integral literature supplies an analytic ingredient, not an inspected explicit optimizer-direction sharpness statement. A general integral identity published under different terms remains a possible covering prior result and requires human checking.

## Mathematical value — PASS
The exact expected removal matrix is a natural invariant of the randomized pairwise update, not a chosen synthetic statistic. It replaces a factor of order \(\kappa^{-1}\) from separating the stochastic coefficient and direction by the sharp joint factor of order \(\kappa^{-1/2}\). This specifically quantifies directional mass-transfer sensitivity near a rank-deficient state and yields the best certificate for every PSD test matrix. No global algorithmic speed-up is claimed without further proof.

## Scope and risks
The theorem applies only to rank-two states, uniform support-circle sampling and exact maximal feasible deletion. Its potential integration into an end-to-end convergence proof remains unproved. General angular statistics might provide another derivation or equivalent earlier identity; published searches cannot rule that out. The deterministic 2026 companion was accessible in bibliographic abstract only, not full text.

Self-review: passed. Independent audit: not yet performed.
