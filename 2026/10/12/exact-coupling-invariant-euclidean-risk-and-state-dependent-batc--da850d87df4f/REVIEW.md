# Self-review

## Correctness — PASS

For \(0<\rho<1\), both diagonal Hessian blocks have eigenvalues \(1\pm\rho\). The balance constraints force three opposite-pair probabilities, and conditioning on pairwise selections gives the exact closed recurrences for \(u_k\) and \(z_k\) displayed in `RESULT.md`. Their explicit solution reconstructs all quantifiers and boundary cases, and direct substitution yields the objective ratio and statewise optimizer reversal. The standalone exact-arithmetic verifier passed 1024 checks across finite sample-path enumerations and inequalities; only the analytical recurrences prove the infinite-horizon statement.

## Originality — PASS, with qualified priority risk

Primary motivating source Hanzely–Richtárik (2018), arXiv:1809.09354v1, analyzes arbitrary minibatch coordinate descent and ESO-based rate bounds, and Qu–Richtárik (2014), arXiv:1412.8063v1, develops arbitrary-sampling ESO. Their inspected sections do not give the same exact all-horizon law or starting-state-optimal coupling. Xie–Yang (2026), arXiv:2610.04685v1, uses *exact sampled-block solves*, a different update. Public one-coordinate probability optimization and deterministic Jacobi results were read and compared at the statement level; neither dominates this fixed-size-two initial-state criterion. Nine semantic searches found no equivalent indexed claim, but older unindexed batch-design or stochastic-Jacobi work remains a genuine priority risk.

## Value — PASS

With all inclusion marginals, batch size, diagonal scaling, starting quadratic, and expected Euclidean MSE fixed, joint dependence alone induces opposite objective-optimal extreme designs for aligned versus anti-aligned starts. The contrast is unbounded as \(\rho\) approaches one despite a common exact geometric mean-square rate. This supplies an exact minimal-size comparative benchmark for sampling design rather than a tiny numerical improvement or unmotivated enumeration.

## Limitations and evidence

Scope: four-dimensional pair-coupled SPD quadratic, exact gradient arithmetic, simultaneous pre-update coordinate steps, fixed iid-in-time size-two balanced subsets, arbitrary deterministic start. No statement for exact sampled-block minimization, asynchronous updates, nonlinear objectives, arbitrary Hessians, finite-precision cost, or superiority of the asymptotic exponent. Independent audit has not been performed. Source statements and bibliographic details appear in `RESULT.md`; computational replay command and limits appear in `VERIFICATION.md`.

Self-review: passed. Independent audit: not yet performed.
