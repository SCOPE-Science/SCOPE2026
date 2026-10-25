# Scientific review

## Correctness

**PASS (self-review).** The process has a finite-first-moment unique invariant law when \(r>m\), by synchronized-reset Wasserstein contraction. Quadratic generator closure yields a Metzler two-by-two raw-moment system, and its positive Perron mode proves exact necessity and sufficiency for finite stationary second moments. The stationary covariance formula, exact derivative signs, and critical scale are reconstructed algebraically in `RESULT.md`. The program `VERIFY.py` performed 57,501 finite checks with exact fractions and representative floating boundaries. Finite tests do not prove stationarity; the argument for infinite-time behavior is analytic.

## Originality

**PASS, with substantive residual risk.** Bernard et al. (arXiv:2610.22038v1) supply the local-reset growth model and study localization of fractions, not the homogeneous finite-system covariance-locking law. Assefa et al. (arXiv:2610.01363v1) give a broad affine-reset polynomial-moment calculus; Jolakoski et al. (arXiv:2411.12390v1) provide close coupled-moment equations for a related growth/reallocation model. Those are significant precursor and possible implicit-coverage sources, and the moment closure itself is not claimed as new. The distinct assessed claim is the exact covariance-locking/monotonicity phase law together with the sharp invariant second-moment frontier and square-root finite-size crossover. Independent priority review is needed because the older paired system may render portions readily derivable.

## Mathematical value

**PASS.** Exact intersite covariance is a natural measure of common risk. The critical \(m=r/2\) surface yields an unexpected invariance under redistribution even as variance and correlation change, while the sharp \(N\)-dependent threshold quantifies the effectiveness and ultimate limitations of mixing at preventing infinite stationary variability. This is a complete naturally parameterized classification, not a fitted table or a known one-site resetting identity.

## Scope and limitations

The claims require \(N\ge2\), \(0<m<r\), \(\varphi\ge0\), independent rate-\(r\) site clocks, common positive reset level, homogeneous deterministic growth and global mean-field exchange. No tail asymptotics, infinite-population full-law limits, higher-moment boundaries, or heterogeneity are established. Results include no independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
