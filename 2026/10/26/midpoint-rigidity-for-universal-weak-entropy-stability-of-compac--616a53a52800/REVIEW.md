# Scientific review

## Correctness — PASS

The proof fixes the positive-speed, uniform-grid, degree-one, exact-integration, uncorrected cRKDG setting and writes the two-stage order-two coefficients explicitly. The physical update independence is an exact consequence of linearity and the order condition. For midpoint, the two subinterval averages and a pair of Jensen applications establish the RK-averaged entropy inequality for every finite convex entropy and exactly \(0\leq r\leq1\); constants rule out larger Courant numbers. For every other nonnegative-weight tableau, the quartic hinge with an arbitrarily small quadratic addition provides a \(C^2\), strongly convex counterexample at every \(r>0\). The explicit defect \(-1/3072\) and alternating-mode determinant are verified by rational arithmetic. The proof's limits and assumptions are explicit.

## Originality — PASS, subject to bibliographic risk

The motivating work (arXiv:2610.18837) proves a sufficient weak-entropy result for bounded-curvature-ratio families and sufficiently dissipative Lax–Friedrichs fluxes, not the sharp classification for all convex entropies under upwind flux. The 2024 bound-preserving method (arXiv:2412.16002) identifies the midpoint tableau but proves invariant-domain properties, not the tableau-dependent RK-entropy-flux failure. The 2023 cRKDG construction (arXiv:2307.06471) already relates physically equivalent linear schemes to Lax–Wendroff DG; that equivalence is acknowledged as prior, not presented as new. The assessed claim is that the *same physical map* can have radically different universal cell-entropy certificates solely because of RK stage averaging, with the unique midpoint threshold and explicit strongly convex witnesses. Searches found no covering statement, but a historically unindexed equivalent remains possible; the 2005 Lax–Wendroff DG full text was not inspected.

## Value — PASS

For entropy-stable DG design, tableau choice can alter the RK-averaged entropy budget without changing a single primal solution coefficient in this natural linear benchmark. The theorem gives a complete, sharp RK2 classification, a usable midpoint Courant bound for nonsmooth convex entropies, and an obstruction ruling out an entropy-independent CFL for every other nonnegative-weight RK2 tableau. The alternating Fourier certificate also demonstrates why a weak cell-entropy inequality does not guarantee stability of the full polynomial update. These are substantive scheme-selection and interpretation consequences, not just numerical recomputation or arbitrary parameter substitution.

## Closest literature and limitations

See the four cited primary sources in RESULT.md. The result is confined to the uncorrected scalar advection cRKDG scheme with exact integration, degree one, upwind stage entropy flux and two-stage order-two methods. It does not claim nonlinear or fully strong entropy stability, nor safety for an arbitrary individual entropy at other tableaus. The all-convex classification is not implied by spectral stability results; conversely the spectral comparison is contextual, not a separate originality claim.

Self-review: passed. Independent audit: not yet performed.
