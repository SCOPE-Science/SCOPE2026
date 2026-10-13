# Scientific review: symmetry breaking in expiring-coupon entry flux

## Correctness — PASS

The theorem separates stationary complete-window mass from the new-entry crossing probability. Its exact weighted crossing identity includes the necessary factor \(1-p_i\) for the outgoing draw, and reduces at uniform weights to Long's formula. Pairwise balancing proves the claimed global extrema at the two minimal window lengths. The two-letter optimization follows from an explicitly differentiated one-variable polynomial with a unique interior root. A factorial-moment count derives the full-simplex Hessian at uniform weights, with positive quadratic coefficient for every fixed alphabet size and sufficiently large window. The rare-symbol construction proves the inverse-window lower bound without asserting global optimality for larger alphabets. Exact independent enumerations and rational-coefficient checks passed. The proof concerns stationary entry rates, not nonuniform first-hitting laws.

## Originality — PASS (subject to priority risk)

Long's *The Expiring Coupon Collector* (arXiv:2604.26298, Theorem 3.1) gives the uniform entry formula and rare-entry laws, but does not optimize the flux over nonuniform sampling. Long's *Clumsy and Careless* (arXiv:2605.14511) concerns different loss mechanisms. Berthet's *On Von Schelling Formula* (arXiv:1703.01886) studies monotone, nonuniform coupon waiting times. Published mathematical-record comparisons including a nonuniform reset-coupon result concern another mechanism and do not imply this statement. The distinctive claim is the short-window extremality, complete two-type symmetry-breaking classification, and eventual local instability in every fixed alphabet. An older equivalent binary pattern-arrival or nonuniform scan-statistics theorem might exist; absent a covering statement in the material examined, this remains a residual risk rather than a claim of exhaustive priority.

## Value — PASS

The same iid source maximizes stationary complete coverage but can become a strict local *minimum* for the entry frequency into coverage. The exact two-type threshold at \(M=4\), full optimizer, and the exponential-versus-inverse-window separation establish a sharp and structural difference between occupancy and entrance statistics. This directly addresses how biased coupon frequencies change the most relevant normalization for expiring collection, rather than computing an isolated small instance. Scope is fixed finite alphabet, iid draws and deterministic sliding-window expiration; a sharp transition length for all larger alphabets and first-completion stochastic ordering are not proved.

Self-review: passed. Independent audit: not yet performed.
