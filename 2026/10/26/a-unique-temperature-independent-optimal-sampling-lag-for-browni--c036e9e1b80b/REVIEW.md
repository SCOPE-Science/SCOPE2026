# Scientific assessment: optimal finite-lag circulation measurement

## Correctness — PASS

The stationary covariance is reconstructed from the Lyapunov equation, not inferred from simulation. The lagged covariance is \(C_t=\Sigma e^{A^\top t}\); its antisymmetric part is the mean signed chord. Wick's fourth-moment formula and \(\det(e^{At})=e^{-2t}\) give the full finite-lag variance. The global maximum follows from strict monotonic decrease of \(v\coth(vt)(1-e^{-2t})\), established by a convexity inequality. Differentiating in \(v\) proves monotonicity of the optimizer; an exact exponential identity yields the near-critical logarithm. Independent numerical matrix calculations and Gauss-Hermite integration pass 716 checks. Risks are limited to the stated model: no conclusion is made for dependent multi-pair sampling or measurement noise.

## Originality — PASS, subject to independent priority review

The closest directly relevant source, Viot et al. (arXiv:2307.05248), studies a discrete **Euler-step** angular-momentum observable, derives its probability law and noise-to-signal ratio, and mentions possible optimization of the step size. The new claim instead treats the exact continuous-time Ornstein–Uhlenbeck propagator at arbitrary observation lag and proves the unique bath-temperature-independent optimum with monotonicity and critical asymptotics; those results are not given in the primary text or supplementary Eqs. (S11)-(S16). Du Buisson, Mnyulwa and Touchette (arXiv:2307.06245) treat the **path-integrated** stochastic area; du Buisson and Touchette (arXiv:2212.12022) treat dynamical large deviations of time-integrated functionals. Those stronger frameworks do not explicitly state the finite-lag single-chord optimum. A general Gaussian bilinear-moment identity could enable a separate derivation; exact scholarly priority remains a residual risk, not a claim of proved uniqueness.

## Scientific value — PASS

The motivating Brownian-gyrator fluctuation study identifies poor performance at very short observation intervals and anticipates an intermediate favorable interval. The theorem resolves that experimentally interpretable finite-lag question for exact sampled trajectories: it selects a unique optimal lag by a parameter-free scalar equation and shows surprising universality with respect to temperature asymmetry. The logarithmic divergence as coupling approaches loss of stability identifies a nontrivial critical-slowing prediction. It also separates the maximum-SNR lag from the strictly later maximum-mean-signal lag, with a nonvanishing limiting gap at both ends of the stable coupling interval. This value is restricted to a single-pair moment-based circulation statistic, not to optimizing full experimental inference.

## Closest literature and limitations

- P. Viot et al., arXiv:2307.05248, full 16-page preprint including relevant supplemental model/characteristic-function sections inspected.
- J. du Buisson et al., arXiv:2307.06245, path-integrated area and irreversibility test inspected.
- J. du Buisson and H. Touchette, arXiv:2212.12022, scope and linear-diffusion dynamical-observable sections inspected.

Finite checker execution verifies examples and algebraic identities; it cannot by itself certify the parameter-uniform inequalities. Independent audit and independent priority validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
