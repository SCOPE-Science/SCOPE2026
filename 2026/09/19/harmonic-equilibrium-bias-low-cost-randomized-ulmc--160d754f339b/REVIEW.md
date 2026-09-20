# Review: harmonic equilibrium bias and one-gradient covariance obstruction

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For a quadratic potential, each method becomes a random affine linear recurrence. Its stationary second moments satisfy a closed three-dimensional discrete Lyapunov system obtained by averaging over the random intermediate time and the correlated Brownian integrals. Expanding that exact system gives the stated coefficients.

Several adversarial checks were applied to the formulas. The target covariance is exactly `diag(kappa^{-1}, alpha)` for the source convention. The predictor switches reproduce the source methods: RMM is `(delta,beta)=(1,1)`, ALUM is `(0,1)`, and LC-REI is `(0,0)`. The order-`h^2` formulas specialize to `(+alpha/6,+alpha^2 kappa/3)` for LC-REI, `(-alpha/6,0)` for ALUM, and `(0,0)` for RMM. A finite-step calculation using the exact Brownian covariance and numerical quadrature approaches these coefficients as `h` decreases. The symbolic derivation independently gives the order-`h^3` cross-covariance coefficients `-alpha^2 kappa/12`, `-alpha^2 kappa/12`, and `-alpha^2 kappa/24` for LC-REI, ALUM, and RMM respectively.

The arbitrary-time no-go argument uses only the first two moments of `tau`. Matching covariance through order `h^2` first forces `E[tau]=1/2` from the order-`h` cross term, then `E[tau^2]=1/3` from the order-`h^2` cross term. Under these necessary conditions, the position variance coefficient vanishes only at `beta=1/2`, while the velocity variance coefficient vanishes only at `beta=1`; hence simultaneous cancellation is impossible. The Wasserstein lower bound follows from the reverse triangle inequality for second moments under any coupling and does not assume a Gaussian numerical invariant law.

The stability statement is intentionally restricted to sufficiently small step size. For the quadratic strongly convex system, the second-moment transition operator is a perturbation of the stable continuous underdamped moment generator, so its spectral radius is below one for sufficiently small positive `h`.

## Originality

**PASS, to the best of our knowledge.** The motivating source arXiv:2609.20713 was inspected at the method definitions, unified parameter table, cost comparison, and linear OU experiment. It introduces LC-REI, identifies the RMM/ALUM/LC-REI predictor switches, proves non-asymptotic Wasserstein error bounds, and reports that LC-REI has lower long-time pathwise position RMSE than ALUM in its OU test. The inspected source does not state stationary covariance expansions for those three schemes, arbitrary-time stationary moment conditions, or the one-gradient covariance obstruction.

The original ALUM paper by Hu--Huang--Huang was inspected for its method/cost/error context. He--Balasubramanian--Erdogdu was inspected because it explicitly studies constant-step stationary bias of randomized midpoint Langevin chains; it establishes that stationary-bias analysis for randomized midpoint methods is prior art, so no general novelty is claimed for studying invariant measures. Older Langevin numerical-analysis work on long-run accuracy, splitting methods, and invariant-measure order conditions was also checked conceptually; those works establish the broader technique and phenomena such as superconvergence, not the formulas for the newly introduced LC-REI or the predictor-family no-go theorem here.

Searches for `LC-REI` combined with stationary covariance, invariant measure, harmonic bias, and related formulations returned the new source paper but no separate coverage of the present claims. The SCOPE archive was searched for LC-REI, ALUM, randomized Langevin stationary covariance, and equivalent terminology; no overlapping accepted record was found. Because LC-REI is extremely recent, a contemporaneous or not-yet-indexed follow-up remains the principal originality risk. No inaccessible paper was identified that specifically appeared likely to contain the same LC-REI covariance classification.

## Value

**PASS.** The result adds an equilibrium-sampling axis that is not visible from the source's transient/pathwise RMSE comparison. It gives exact leading constants, separates configurational and kinetic bias, identifies why RMM's extra predictor force cancels second-order covariance error, and proves that this cancellation cannot be recreated inside a natural one-gradient family merely by retuning the random time or predictor-noise amplitude. The LC-REI position variance defect also yields an explicit `Omega(h^2)` stationary configurational Wasserstein lower bound on the harmonic target.

The result is useful both diagnostically and constructively: it provides a sharp harmonic benchmark for the new low-cost randomized schemes and an order-condition obstruction that any attempted one-gradient refinement of this predictor structure must overcome by changing something more substantial than random-time or predictor-noise tuning.

## Limitations

The theorem concerns stationary second moments for a scalar quadratic target. The numerical invariant law need not be Gaussian because the random intermediate time produces a multiplicative-random linear update. No claim is made about general nonquadratic invariant measures, full-distribution weak order, maximal stable step sizes, transient strong error, or practical runtime ranking. The continuous predictor-noise multiplier is an analytic interpolation; only the endpoint choices used by the source are established algorithms. The public verification is numerical/symbolic support for an analytic derivation, not formal proof checking.
