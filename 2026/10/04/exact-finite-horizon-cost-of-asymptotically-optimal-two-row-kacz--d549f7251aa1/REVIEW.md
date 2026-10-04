# Same-model review

## Correctness
PASS. In row-normal coordinates the relaxed sweep matrix is explicit. Applying it to \(a^\perp\) gives the lower bound \(\|T_\omega\|_2^2\ge c^2+s^2(\omega-1)^2\), which proves unique one-sweep optimality of \(\omega=1\). The characteristic discriminant factors exactly, the asymptotic optimum \(\omega_\star=2/(1+s)\) has a non-scalar repeated eigenvalue, and the nilpotent decomposition \(T_{\omega_\star}=qI+N\) yields the claimed all-horizon norm formula. The ratio, one-sweep strict inequality, eventual decay, and nearly-parallel crossover expansion follow algebraically. The included symbolic checker independently replays these identities and exact rational test cases.

## Originality
PASS with residual risk. Searches covered relaxed Kaczmarz, two-row Kaczmarz, SOR optimal relaxation, finite-horizon operator norms, Jordan coalescence, residual spikes, alternating projections, and two-coordinate Gauss-Seidel. The closest literature establishes relaxed-Kaczmarz convergence or asymptotic spectral-radius tuning; the closest published neighboring results concern different observables or algorithms. None of the inspected material states the exact Euclidean power norm at the two-row asymptotic optimum, the strict horizon-one reversal, or the \(s^{-1/2}\) crossover law. A historical unindexed derivation remains possible and is not represented as ruled out.

## Value
PASS. Spectral-radius tuning is asymptotic and can obscure nonnormal transients. This result gives an exact, interpretable two-row model in which asymptotic optimization creates a Jordan block and quantifies the finite-horizon price for every sweep count. The crossover law shows that near row degeneracy the horizon needed before overrelaxation pays off diverges on a precise scale, making the distinction relevant to stopping-limited row-action solvers rather than a purely formal two-by-two exercise.

Same-model review: passed. Independent audit: not yet performed.
