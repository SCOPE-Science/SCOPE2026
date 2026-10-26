# Scientific review: sampling-moment stability threshold

## Correctness — PASS
The sample-and-hold map follows by exact integration; the covariance map is positive and fourth-degree polynomial in the holding interval. Matching raw moments through degree three leaves a single positive rank-one fourth-degree coefficient. A strict rational quadratic Lyapunov matrix certifies the stable five-point anchor, and a one-factor exact determinant proves a unique crossing along a positive mixture segment and excludes stability above it. The standalone exact symbolic script verifies the nonstandard algebra. These checks establish sampled-index mean-square stability only, not continuous-time intersample convergence.

## Originality — PASS, with residual risk
Published work on random networked sampling and mean-square stability was compared by model and conclusion, not title alone. Montestruque–Antsaklis (2003, 2004) give general stochastic stability tests for model-based networked systems and include a double-integrator example. Li et al. (2013) use Markovian sampling/delays and LMI design; the full 2013 text contains neither the fixed-three-moment fourth-moment rank-one order nor this exact rational boundary. Existing indexed findings on mean-square stochastic optimization concern other recursions. Agniel–Jury (1971) is an early relevant article not read in full; full-text inaccessibility leaves nonzero originality risk. The result does not claim originality of covariance lifting, positive-cone order, or the quadratic Lyapunov criterion individually.

## Value — PASS
Sampling jitter is operationally described by lower-order statistics, but this example rigorously proves that mean, variance and skewness—even with common positive support—can yield opposite mean-square control stability. The sharp fourth-moment threshold is valid for every law in the fixed lower-moment class, rather than only a selected finite distribution or simulation, and the general monotonicity explains the structural reason. This is a motivated robustness distinction for sampled-data feedback, beyond an arbitrary determinant computation.

## Scientific limits
Assumes i.i.d. positive intervals, finite fourth moment, sampled-index decay and the stated plant/control architecture; the rational threshold fixes gains and the first three raw moments. It does not characterize almost-sure stability or physical-time behavior for unbounded intervals. Specialized early full-text coverage cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
