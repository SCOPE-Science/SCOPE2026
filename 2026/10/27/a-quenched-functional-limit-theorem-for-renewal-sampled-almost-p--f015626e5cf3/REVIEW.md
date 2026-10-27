# Scientific review

## Correctness — PASS

The bounded martingale-difference strong law makes each Bohr-almost-periodic covariance function equidistribute along the random renewal times. A second finite-lookahead strong law turns lagged covariances into their renewal-averaged Bohr means. The exponentially integrable collision count makes the variance-profile tail uniform, without a lower cutoff on increments. Conditional finite-range dependence holds with logarithmic index radius almost surely, by Borel–Cantelli. The independent-block FCLT applies with main-block length \(n^{1/3}\), logarithmic gaps, maximal gap \(L^2\)-error \(o(n)\), and fourth-moment Lyapunov ratio \(O(n^{-2/3}\log^2 n)\). These steps prove convergence for the **same** full-measure set of schedules. Uniform-norm lag-continuity was independently included to justify closure of the covariance functions under the renewal integral. The code's finite checks are corroboration only.

## Originality — PASS, qualified

Berger–Strobel, arXiv:2610.23669v1, Theorem 4.5 is scalar and annealed, and its covariance estimates do not assert almost-sure conditioned process convergence. Berger–Mohamed arXiv:2208.08240 treats almost-periodic processes without these renewal-sampling quantifiers; Brandes–Curato arXiv:1804.02254 studies sampled autocovariance; Brandes–Curato–Stelzer arXiv:2007.00574 addresses mixing inheritance for stationary renewal-sampled inputs. Relevant mathematical-record searches were performed under aliases for quenched/conditional functional limits and covariance-almost-periodic processes, with no more general result found to imply the statement. Classical independent-array FCLTs and blocking arguments are not claimed as original. Older specialized or implicit coverage is a residual literature risk; search absence is not an absolute novelty certificate.

## Mathematical value — PASS

Conditioning on the realized observation times answers a different inferential question from averaging over possible observation schedules. The result upgrades an emerging scalar theorem to an environment-wise process law, supplies an explicit computable covariance constant, and allows only covariance-level almost periodicity. The sharp proof obstacle is unbounded clusters of short renewal steps; the exponential collision estimate and logarithmic dependence range resolve it without any lower spacing assumption. The normalizer and a concrete nonstationary Gaussian-increment-sign example are mathematically natural.

## Limitations

Requires bounded \(X\), finite dependence range and sup-norm continuous Bohr-almost-periodic covariance lags. No convergence rate or unconditional extension to L2-only processes follows. A related general conditional FCLT may remain unlocated. Numerical checks cannot establish infinite convergence.

Self-review: passed. Independent audit: not yet performed.
