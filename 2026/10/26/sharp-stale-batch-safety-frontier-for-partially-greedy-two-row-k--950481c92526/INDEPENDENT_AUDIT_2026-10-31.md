# Independent mathematical audit

## correctness

PASS

For A=E||r_I u_I||² and B=||E(r_I u_I)||², independence gives exact conditional Δ||e||²=−Kβ{2A−β[A+(K−1)B]}. After residual scaling, B/A is the Rayleigh quotient of [[p,c√(pq)],[c√(pq),q]], maximum R=(1+sqrt(θ²+(1−θ²)c²))/2. The positive top eigenvector is feasible under the greedy residual ordering, including c=0, θ=0 tie, and θ=1 boundaries. Hence the strict universal cutoff is 4/[K+1+(K−1)sqrt(θ²+(1−θ²)c²)]. A≥(1−c)||e||²/2 yields a uniform conditional contraction and geometric mean-square convergence. K=2,θ=1,β=1 yields Householder reflections and a countable union of tie lines, so generic nonconvergence. An independently written checker performed 880 exact outcome and sharp boundary checks.

## originality

PASS

Independent statement/implication comparison including direct mathematical object parameters and available primary material: Two-row cyclic Kaczmarz relaxation (Resultary: SCOPE-exact-finite-horizon-cost-of-asymptotically-optimal-two-row-kacz--d549f7251aa1) uses sequential cyclic row updates, not K independent same-snapshot additive corrections. Standard RK averaging divides corrections by worker count; the exact θ-dependent interference frontier is distinct. Coleman describes row-selection staleness empirically; this statement is exact for a shared snapshot, not a general lock-free schedule. A standard independence second-moment identity is a prerequisite, but the exact constrained Rayleigh maximum, sharp witness and generic reflection obstruction require further analysis.

## value

PASS

Sharp explicit stability frontier separates stale additive concurrent updates from sequential or averaged updates. The singular θ=1 reflection trap and arbitrarily small exploration restoring convergence are meaningful methodological boundary examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
