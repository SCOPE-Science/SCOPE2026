# Independent mathematical audit

## correctness

PASS

For fixed kappa>0, 0<|u|<kappa and unequal positive bath temperatures, the jointly Gaussian forward/reversed two-frame laws have exact conditional KL 2 tr[(Q-H^T P^-1 H)^-1 H^T P^-1 H]. Covariance Lyapunov identity gives the uniform small-lag, small h/t expansion J_h(t)/sigma=1-kappa*t-h/t+O((t+h/t)^2), with sigma=u^2(Tx-Ty)^2/(2*kappa*Tx*Ty). Strict noiseless pair-versus-path data processing (nonzero stochastic-area fluctuation conditional on endpoints), monotonicity under independent noise and exponential large-lag decay localize every global maximizer; minimizing kappa*s+1/s gives t_h/sqrt(h/kappa)->1 and maximum sigma[1-2 sqrt(kappa h)+o(sqrt h)]. I independently checked the exact 4x4 covariance/2x2 Schur form and numerically optimized three nondegenerate parameter choices for h=10^-3 and 10^-4; normalized optimizer/loss ratios approach one. These finite diagnostics do not establish the uniform proof by themselves. Read source RESULT.md and original CHECKER.py for formulas and boundary assumptions.

## originality

PASS

Best-of-knowledge comparison against stronger and equivalent claims, not titles alone; primary texts and known antecedents acknowledged. Earlier exact model distributions and continuous sigma do not directly state or imply the universal sensor-noise scale absent these additional steps. Unresolved historical-priority possibilities are explicitly retained; unsuccessful searches are not proof of novelty.

## value

PASS

The question is a natural experimentally motivated sensor-noise-versus-time-resolution tradeoff for a stationary irreversible Gaussian diffusion, with a sharp universal leading sampling scale and optimal information loss; it resolves a global variational limit not given by the standard Gaussian KL formula. It is explicitly NOT a finite-sample estimator, continuous-path entropy production or arbitrary anisotropic noise theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
