# Independent mathematical audit

## correctness

PASS

The theorem is intact but the frozen proof sums over integer k<nt: off grid this counts one extra step, so its martingale is not the stated càdlàg one and its exact Y_n identity is false there. The corrected RESULT uses k=0,...,floor(nt)-1 for both the martingale and drift, exhibits the exact discrete integral, and bounds the continuous Volterra error by 2||Y_n||/n. I reconstructed the exact inversion regression and checked the occupancy law with hypergeometric front and complement counts. Continuous coordinate marginals justify product-measure convergence despite the diagonal mass. The front and tail squared counts give (1+2b^3)/9; subtracting b^4/4 yields the bracket integrand. Boundedness and the deterministic-time compactness argument imply uniform bracket convergence in probability, with jumps bounded by 2/sqrt(n). Martingale FCLT and the continuous-input Gronwall map give J1 convergence; Ito isometry gives the displayed covariance. Time zero is the increment check on the diagonal and Y_n(0)=0. The exact finite variance was reconstructed via sign products on pairs, triples and disjoint pairs. Replay is the repaired analytic proof; the frozen checks/check_inversions.py was directly located and inspected, not executed, and only checks finite regression and variance. The scope is identity start and fixed finite T.

## originality

PASS

The supported distinction is an identity-start functional CLT over a fixed discrete-clock window and its model-specific bracket/tightness proof. The one-time law, exact mean, subset description and eigenfunction already appear in prior work. Two-time covariance is also a mechanical consequence of the prior regression and finite or limiting variance, not independent novelty.

## value

PASS

The one-time fluctuation laws do not describe a shuffle trajectory, for example its joint fluctuations or path functionals over a fixed window. The validated process limit, with topology and explicit noise over the nonstationary transient, fills that gap. This rests on a bracket calculation and tightness, not merely restating the already known variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
