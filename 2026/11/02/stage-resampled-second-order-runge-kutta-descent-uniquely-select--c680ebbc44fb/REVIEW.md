# Scientific review

## Correctness

**PASS.** The deterministic-order-two conditions determine the entire tableau family, and an eigenbasis reduction gives the exact stage multiplier. Direct expansion using only the first two moments and stage independence proves the moment polynomial and the strict quadratic coefficient gap. The stability polynomial factor is strictly increasing after removing its zero-step factor; its derivative has a global positive lower bound. The midpoint factorization, Heun root bounds, implicit monotonicity, and Pareto fourth-moment counterexample follow algebraically. Independent exact-rational stage enumeration and rotated-matrix tests are implemented in `verify_rk2.py`. The computation is supporting evidence; the infinite and all-dimensional conclusions are proved analytically.

## Originality

**PASS, qualified.** The closest motivating literature is Stillfjord and Williamson's *SRKCD* (arXiv:2201.12782v1), which reuses a random batch within each Runge–Kutta step and gives general diminishing-step convergence, not a distribution-free comparison of two-stage deterministic-order-two coefficients under independent stage resampling. Mulayoff and Michaeli's *Exact Mean Square Linear Stability Analysis for SGD* (arXiv:2306.07850) supplies a first-order benchmark without a Runge–Kutta tableau optimizer. Saito's 2011 stochastic Heun paper studies Brownian-noise SDE discretization rather than gradient-oracle sampling. A related two-stage Chebyshev stability calculation uses a different deterministic stability polynomial and fixes a different method; it does not imply the universal Heun weight identity. Searches of published mathematical records and the relevant primary literature found no statement dominating this exact result. Publication priority remains qualified pending independent specialist review.

## Value

**PASS.** All explicit two-stage order-two Runge–Kutta tableaux have the same deterministic scalar linear stability polynomial, so deterministic testing cannot distinguish their coefficients on quadratic gradients. Independent minibatch sampling creates a nontrivial selection rule: Heun minimizes one-step and every-horizon squared error for every positive-definite quadratic, with an exact distribution-free variance penalty for every alternative. The sharp root characterizes the entire mean-square stability range and gives a strictly increasing, asymptotically twofold relative advantage over midpoint. The fourth-versus-second oracle-moment contrast explains a concrete failure of batch reuse for heavy-tailed interpolation losses. These are actionable sampling and tableau-design distinctions rather than isolated numerical examples.

## Closest literature and boundaries

The exact model is a centered quadratic with a scalar random gradient multiplier shared across coordinates but resampled across stages; it does not represent all sources of stochastic-gradient uncertainty. The comparison is per iteration, not per unit of gradient-oracle work, and is about mean-square convergence rather than floating-point or almost-sure stability. The source's shared-batch algorithm is not claimed to be incorrect. The principal residual risk is specialized prior stochastic Runge–Kutta literature with an equivalent tableau optimization or heavy-tail moment criterion.

Self-review: passed. Independent audit: not yet performed.
