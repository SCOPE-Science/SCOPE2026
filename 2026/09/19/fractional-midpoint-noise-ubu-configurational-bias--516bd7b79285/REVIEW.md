# Same-model review

## Correctness — PASS

The claimed covariance formulas follow from an exact linear-Gaussian reduction. On a quadratic target, all interpolation values \(\theta\) share the same deterministic transition matrix; only the stochastic forcing changes. The one-step noise covariance is quadratic in \(\theta\), so the stationary covariance is exactly quadratic in \(\theta\) after applying the discrete Lyapunov inverse. Direct series expansion gives the stated \(h^2,h^3,h^4\) coefficients. Independent numerical evaluation of the Lyapunov equation reproduces the endpoint constants, the one-third cancellation, the friction-corrected fourth-order law, the anisotropic multi-mode scaling, and the exact scalar zero-bias branch.

The strongest hidden-hypothesis check is stability: all stationary-covariance statements are restricted to steps for which the common deterministic matrix has spectral radius below one. The higher-order claims are only about invariant position covariance on quadratic Gaussian targets; no higher-order trajectory claim is made.

## Originality — PASS, to the best of our knowledge

The following are prior art and explicitly excluded from the novelty claim: configurational superconvergence of Langevin splitting schemes; harmonic-oscillator stationary-covariance analysis; classical UBU; general invariant-measure error analysis; and the idea of tuning splitting parameters to improve configurational averages.

The accepted contribution is narrower: for the new LC-UBU modification of arXiv:2609.20713, the quadratic-target deterministic transition is unchanged by deleting the noisy midpoint, while the stationary position-covariance bias changes from \(-\alpha h^2/6\) for UBU to \(+\alpha h^2/12\) for LC-UBU; interpolating the midpoint noise yields the universal \(\theta=1/3\) cancellation, the friction-only \(\theta(h)=1/3-\gamma h/9\) fourth-order covariance correction for arbitrary SPD Gaussian targets, and a local exact-variance branch for each scalar mode.

Searches covered the recent LC-UBU paper, UBU stationary covariance and Wasserstein analyses, harmonic/configurational Langevin splitting literature, midpoint-noise interpolation, and configurational superconvergence. No equivalent formulas were located, and no overlapping SCOPE record was found. Leimkuhler–Matthews (2013) and Alamo–Sanz-Serna (2016) were inspected through accessible bibliographic/summary material rather than read end-to-end; they are the older sources most plausibly capable of containing related harmonic invariant-measure calculations. The motivating preprint is extremely recent, so a contemporaneous note or revision remains the principal residual originality risk.

## Value — PASS

The result isolates the precise stochastic mechanism changed by LC-UBU. On Gaussian targets, the low-cost midpoint deletion does not alter deterministic propagation at all; it alters only the discrete fluctuation–dissipation balance. The opposite signs at the two endpoints expose a universal cancellation point and a spectrum-independent fourth-order configurational correction. This is useful both as a diagnostic of LC-UBU bias and as a constructive design rule when the extra midpoint Gaussian is acceptable.

## Limitations

The result does not show improved nonlinear strong/weak order, does not preserve LC-UBU's reduced Gaussian count for \(\theta\ne0\), and does not make all anisotropic modes exactly unbiased at finite step size. The exact zero-bias tuning becomes Hessian-mode dependent at the next order.

Same-model review: passed. Independent audit: not yet performed.
