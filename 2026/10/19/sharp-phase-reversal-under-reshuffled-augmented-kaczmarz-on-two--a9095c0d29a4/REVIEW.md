# Review of the phase-resolved augmented Kaczmarz finding

## Correctness — PASS

The original scalar augmented Kaczmarz update [1, equation (18)] has been reconstructed algebraically. The stable transition matrix has spectral radius \(\sqrt{1-p}\). Exact Lyapunov solutions for independent forcing and two-step epoch forcing yield the displayed covariance matrices. Both variance differences factor over a strictly positive denominator; the unique crossover in \((0,1)\) is \(3-\sqrt5\). The actual standalone symbolic code reproduces the identities. Initial states are arbitrary fixed finite vectors; the expected-error limits are not sample-path results.

## Originality — PASS, with priority risk

The source [1] establishes the algorithm for consistent systems, not this inconsistent two-phase variance comparison. The closest mathematical coverage is [2], which analyzes random reshuffling *including momentum* through stationary power spectra after uniformly randomizing the epoch origin. Its general **phase-averaged** stationary variance cannot, by that stated claim alone, distinguish epoch-boundary from within-epoch error or imply their opposite comparisons. This finding instead reconstructs the cyclostationary two-phase covariance and gives an exact sharp reversal. The white-noise momentum analysis [3] does cover the essential with-replacement covariance mechanism, which is treated only as a benchmark here. No independent novelty audit has occurred; an equivalent phase-aware computation in the broader stochastic-gradient literature remains possible.

## Value — PASS

Random reshuffling is widely recommended as an improvement over with-replacement row selection. The smallest inconsistent Kaczmarz problem with shared dual memory exhibits a genuine **phase-dependence**: every epoch boundary improves, yet intermediate-step mean square is worse above an explicit penalty threshold. This warns against interpreting phase-averaged reshuffling improvements as per-iteration guarantees, and identifies an exact hyperparameter range where such extrapolation fails. The example is the natural smallest epoch, not an arbitrary numerical slice.

## Limitations and nearest work

The result applies only to two inconsistent identical scalar rows and constant penalty, and it compares limiting expected squared error. It does not assess nonstationary penalties, heterogeneous rows, finite-horizon signs, global nonlinear methods, or almost-sure behavior. Source [2] provides general phase-averaged coverage and is the principal residual priority risk.

Self-review: passed. Independent audit: not yet performed.
