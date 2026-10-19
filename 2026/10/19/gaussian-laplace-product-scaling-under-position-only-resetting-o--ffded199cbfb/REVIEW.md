# Self-review

## Correctness — PASS

The law is reconstructed from independent Brownian motions, a homogeneous independent Poisson clock and position-only jumps. The exact finite-time characteristic function follows from a verified harmonic-oscillator Feynman–Kac solution and Gaussian averaging over the Brownian medium at the last reset. A direct Itô-isometry coupling gives the global \(W_2\) bound, with explicit control of Poisson-age truncation. The product-normal/Laplace representation yields all moments and the density integral. A boundary decomposition and a single nondegenerate saddle establish the logarithmic peak and sharp \(2/3\) tail with stated prefactors. The exact finite-time variance and deterministic-medium comparison are independently derived. Numerical checks are supporting, not deductive evidence.

## Originality — PASS (subject to independent priority examination)

The 2022 primary source arXiv:2205.00549 resets the stochastic diffusivity *together with* position, which yields a stationary law, unlike position-only resetting. The 2018 arXiv:1812.05664 study treats position-only resetting with a *deterministic* diffusivity, and its Gaussian propagator does not yield the present stochastic-medium product law. The present full claim includes a quantitative Wasserstein limit, logarithmic center, \(2/3\) tail and kurtosis comparison. Searches for the same object and equivalents in relevant primary sources and mathematical records did not reveal explicit dominating coverage. A general stochastic volatility or renewal theorem may implicitly yield the same specialization; the possibility is not certified away.

## Mathematical value — PASS

The result resolves a natural distinction between resetting the observable and resetting its environment. Both the stochastic Brownian medium and deterministic mean diffusivity have the same first-order transport variance, yet exhibit sharply different limiting fluctuation laws (kurtosis \(18\) versus \(6\)), with an exact convergence-rate bound. The stationary/nonstationary distinction and two endpoint asymptotics are useful diagnostics for fluctuating transport models. This is more than computing a routine parameter specialization or an isolated finite table entry.

## Scope and limitations

Only one-dimensional Brownian-square diffusivity with zero initial medium and independent homogeneous Poisson position-only resets is proved. The endpoint asymptotics concern the limiting density, not uniform finite-time tails. The bound is not claimed optimal; priority and generality beyond this model await independent validation.

Self-review: passed. Independent audit: not yet performed.
