# Scientific review: Gaussian spreading–localization trichotomy for scaled-angular Brownian swimmers

## Correctness — PASS

The angular process is a deterministic time change of one-dimensional Brownian motion. The exact two-time complex-velocity correlation reproduces the previously known mean-square displacement. Itô integration by parts produces a weighted martingale plus explicitly bounded remainders. The oscillatory quadratic-covariation defect has an \(L^2\) bound by an exponential convolution and Young's inequality, for all \(\beta>0\). The continuous-martingale central limit theorem therefore has the stated coordinate variances. For \(\beta>2\), the martingale has finite quadratic variation, giving an almost-sure and \(L^2\) endpoint, while a truncated-tail martingale argument yields the isotropic Gaussian terminal-error law. For \(\beta\le2\), nondegenerate Gaussian rescaling excludes convergence in probability to any finite location. The Gamma/Beta moment integral converges precisely above the threshold.

The standalone verifier passed 64 finite tests of the moment identity, plateau constant, angular covariance and asymptotic coefficients. Those finite checks are supporting diagnostics, not substitutes for the analytic proofs.

## Originality — PASS, qualified

The exact mean-square integral and its immediately implied asymptotic consequences belong to Sevilla, Valdés-Gómez and Torres-Carbajal (2024) and are credited. The distinctive theorem is the complete distributional trichotomy, especially almost-sure localization for \(\beta>2\) and the Gaussian *residual-position* law. The motivating paper's inspected model, mean-square, and kurtosis sections discuss power-law spreading and finite-time statistics, with explicit numerical study primarily at \(0<\beta<2\), not an almost-sure terminal-position theorem. The 2020 fractional-angular-Brownian model has stationary-increment correlated angular noise, rather than the required nonstationary independent increments. The 2019 feedback-localization study uses spatially controlled rotational dynamics, not the monotone deterministic power-law angular clock. Closest public research records found concerned unrelated diffusive-simplex, Jacobi-diffusion or oscillator models; their statements do not imply the claim.

Residual risk: a general previously published martingale/inhomogeneous-additive-functional theorem may give these exact asymptotics as an unstated special case. Source coverage and the literature search do not constitute independent proof of publication priority.

## Mathematical value — PASS

The theorem settles a physically motivated question left outside the studied exponent range of an established anomalous-transport model: when accelerating angular fluctuations cause a constant-speed, unconfined particle to stop spreading. The threshold separates power-law Gaussian spreading, logarithmic Gaussian spreading, and almost-sure spatial localization. The counterintuitive localized regime also has an exact isotropic Gaussian law for how its random endpoint is approached. These are structural probabilistic statements not obtainable from checking a finite moment alone and provide concrete benchmarks for stochastic active-matter models.

## Scope and limitations

There is no translational thermal noise, trap, position feedback or resetting. Initial orientation can be fixed or independent of driving Brownian motion. The endpoint itself is not asserted Gaussian. The exact second-moment integral is inherited from prior work. No independent validation, publication-priority certification, or empirical inference guarantee is claimed.

Self-review: passed. Independent audit: not yet performed.
