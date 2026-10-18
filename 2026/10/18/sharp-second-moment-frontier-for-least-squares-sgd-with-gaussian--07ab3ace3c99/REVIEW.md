# Self-review

## Correctness — PASS
A stationary AR(1) Gaussian design makes the squared error a positive multiplicative Feynman–Kac recurrence. The finite-horizon second-moment decomposition reduces the question to two weighted powers of one Hilbert–Schmidt selfadjoint operator. Strict kernel positivity gives a simple leading eigenvalue and strictly positive amplitudes, establishing both directions of the variance criterion. Hermite spectral monotonicity is strict because a leading eigenvector divided by the multiplier cannot be square-integrable near its zeros. An analytic eigenvalue perturbation gives the \(\rho^2\) term and the \(16/9\) coefficient. One hundred six deterministic checks support but do not replace these proofs.

## Originality — PASS, with material residual risk
The 2026-10-04 Li–Wu paper (arXiv:2610.05599v1, Sections 2–3 and Appendix E) studies Gaussian-refresh persistence and AR(1) designs with heavy-tailed innovations; it does not state the Gaussian-innovation AR(1) exact mean-square frontier. The 1993 Douglas ICASSP abstract covers exact expectation analysis of LMS with finitely correlated Gaussian inputs; its full text was inaccessible, and an analytic AR(1) critical coefficient could be latent there. A relevant mathematical-results index and published results were compared by mathematical implication, not title matching. No exact \(2/3-(16/9)\rho^2\) statement was identified. This uncertainty remains a real bibliographic risk rather than a claim of uniqueness.

## Value — PASS
The exact variance frontier for Gaussian autoregressive data is a natural diagnostic for selecting a constant step in correlated streaming regression. It distinguishes smooth Ornstein–Uhlenbeck-type dependence, which has a genuine finite-variance window, from Li–Wu's rare long-refresh persistence, which can destroy every stationary moment. The monotonicity and sharp quadratic coefficient quantify a finite penalty that generic worst-case correlated-data bounds cannot resolve.

## Limits
Scalar design; fixed step; stationary Gaussian AR(1); independent observation noise with positive finite variance; mean-square rather than all-tail or pathwise stability. A classical uninspected LMS paper and other unindexed adaptive-filter results remain originality risks.

Self-review: passed. Independent audit: not yet performed.
