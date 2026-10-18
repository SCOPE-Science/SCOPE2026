# Scientific review

## Correctness — PASS

The full model is an admissible specialization of the published higher-order SIS–opinion equations: its quadratic exposure tensors have a single repeated-source entry, and its recovery rate depends affinely on the shifted opinion. The endemic-equilibrium polynomial is exact. Linearization in a fixed common-sign opinion chamber gives the explicit \(2n\)-dimensional block Jacobian, and the spectral theorem reduces it to independent real quadratic characteristic polynomials. The strict Hurwitz inequalities therefore prove the sharp, all-undirected-network classification without relying on finite graph tests.

In the two-community case, the sum and difference of the equilibrium equations give the complete unequal-positive branch within the both-negative-opinion chamber. Positivity and the chamber signs are checked directly. The full Jacobian determinant on this branch is strictly negative. Both its unstable nature and the exact square-root coalescence follow analytically, while the transverse eigenvalue crosses zero simply. The standalone symbolic checker replays the formulas and supplies finite illustrative eigenvalue comparisons. The checker is not treated as an infinite proof.

## Originality — PASS, with specific residual risks

The closest model-specific source is Samadi, Caiza, Gracy and Paré, arXiv:2608.31032v1 (2026-08-31). It establishes bistability relative to the synchronous invariant set and explicitly distinguishes that statement from full-space stability. Its stated theorem does not give the full-space opinion-Laplacian threshold or the unstable unequal branch obtained here. Kouvaris, Hata and Díaz-Guilera (2015) already study graph-mediated activator–inhibitor instabilities, and Iacopini et al. (2019) already study quadratic-transmission bistability; these mechanisms are not claimed as new. The claim is restricted to the specific coupled model, the exact parameter-wide spectral criterion, and a complete two-community nonlinear bifurcation.

Residual risks: a broader reaction–diffusion theorem might yield the spectral criterion on specialization; that observation is already accounted for by making the exact model-specific nonlinear branch essential to the claim. The original preprint's most relevant model and synchronous stability sections were inspected directly; some remaining sections could not be fully reread during a subsequent retrieval failure. No evidence of a previously published equivalent nonlinear branch or exact threshold was found in the inspected source material, literature comparisons and mathematical research records. These searches do not prove unique priority.

## Mathematical value — PASS

The paper's explicit restriction to synchronous stability leaves a practically meaningful question: is endemic bistability robust to heterogeneous community disturbances? The theorem answers that question sharply for a natural self-exposure epidemic subfamily, across arbitrary symmetric opinion networks. Stronger diffusion of a protective opinion is capable of destabilizing synchronized endemic coexistence, even though it damps opinion disagreement in isolation. The two-community example shows that loss of stability occurs through a fully specified subcritical pitchfork and that the nearby nonsynchronous endemic states are unstable; it is not merely a collection of eigenvalue calculations. The bifurcation boundary gives an exact benchmark for network epidemic–behavior simulations and delineates where lower-dimensional epidemic predictions fail.

The graph must be symmetric and the transmission must have the stated local quadratic form. The result is local, does not establish global epidemic outcomes, and does not classify mixed-sign opinions or infection-boundary states. These are limits of the claim, not consequences left unproved.

Self-review: passed. Independent audit: not yet performed.
