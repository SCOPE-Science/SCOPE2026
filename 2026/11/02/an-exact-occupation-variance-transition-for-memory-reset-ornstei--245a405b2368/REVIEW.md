# Correctness, originality and value review

## Correctness — PASS

With stationary OU initial law \(\mathcal N(0,D/\mu)\), every one-time marginal stays identical because both the OU semigroup and uniform mixture of all previous marginals preserve that law. For the integrated path \(B_t=\int_0^t X_s\,ds\), direct conditional reset expectation gives the **closed and exact** equations \(y'=2c\) and \(c'=v-(\mu+r)c+ry/t\). The initial conditions fix a unique regular solution of \(y''+(\mu+r)y'-2ry/t=2v\). Its Laplace inversion gives the stated hypergeometric finite-time law, including the continuous logarithmic limit at the critical rate. Standard negative-real Kummer asymptotics and an elementary critical exponential-integral identity yield all three sharp leading coefficients; \(0<p<2\) and \(0\le y(t)\le vt^2\) justify every boundary and transform. A distinct exact rational coefficient recurrence, an independent finite-precision ODE check, Laplace quadrature and approximate physical-time sample-path experiments passed 349 finite diagnostic assertions in `verify.py`. The proof, not the simulations, establishes infinite-time assertions.

## Originality — PASS (qualified)

The motivating paper Boyer–Majumdar (arXiv:2405.10283v1) determines one-time Gibbs marginals and their slow **one-time** relaxation, but does not determine time-integrated position variance or the threshold \(r=\mu\). The subsequent broader-memory-kernel analysis Boyer–Evans–Majumdar (arXiv:2411.00641v1) likewise studies one-time marginal relaxation. The 2016 unconfined memory-resetting study addresses the **position variance**, which is not the variance of an OU time integral. Stojkoski–Sandev–Kocarev–Pal (arXiv:2107.11686) analyze temporal correlations and ergodicity but under resetting to a single fixed position, not uniform self-history, so their renewal identity does not imply the memory-dependent term \(r y/t\). The exact hypergeometric law for this integrated observable and its sharp three-rate classification were not located in the inspected relevant primary texts. This is best-knowledge originality, not proof of publication priority: generic reinforced stochastic systems might imply a related phase transition.

## Mathematical value — PASS

Stationary one-time Gaussian data alone cannot diagnose the statistical efficiency of trajectory averaging. A complete finite-time variance and exact long-time threshold answer a natural inference question for a reinforced, non-Markovian particle whose Gibbs marginals conceal slow path memory. The critical logarithm and explicit constants distinguish ordinary inverse-time decay from persistent algebraic correlations; this is not a mere substitution into the already known one-time marginal formula.

## Scope and residual uncertainty

Equilibrium Gaussian initialization, continuous-time uniform recollection of the whole past, positive harmonic confinement, independent Poisson resets and independent Brownian noise are essential. The calculation is an unconditional \(L^2\)-variance theorem, not a central limit theorem or an almost-sure law. The closest primary literature was examined at the relevant one-time/two-time distinction; independent review of potential general reinforced-process theorems remains necessary.

Self-review: passed. Independent audit: not yet performed.
