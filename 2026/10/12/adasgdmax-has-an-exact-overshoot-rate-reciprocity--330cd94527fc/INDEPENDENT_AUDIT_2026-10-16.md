# Independent mathematical audit

## correctness

PASS

For the source theoretical AdaSGDMax β=0, no-momentum update on F(x)=λ||x||²/2, the running maximum of gradient norms yields exact x_(t+1)=(1-c/R_t)x_t where c=η sqrt(d), R_t=max_(j≤t)||x_j||>0. For z=c/||x0|| in (0,2), multiplier 1-z has magnitude<1 and R_t=||x0||; z=1 reaches zero. At z=2, multiplier -1 gives a neutral two-cycle. At z>2 the first step gives x1=-(z-1)x0, sets R1=(z-1)||x0||, and subsequent multiplier -1/(z-1) has magnitude<1; by induction R never changes again and x_t=(-1)^t(z-1)^(2-t)x0 for t>=1. Therefore x2=x0 and Aq=1 for A=z-1 and q=1/A; objective ratios A² then 1/A². Checked independently using exact rational recurrence for 6 subcritical/critical/supercritical cases; read bounded source verifier. Scope excludes nonzero β, stochastic gradients and anisotropic curvature.

## originality

PASS

Best-of-knowledge PASS for the exact one-overshoot reset law, x2=x0, and sharp transient/amplification reciprocity. Wang–Wiens proved qualitative AdaSGDMax convergence and max-statistic freezing but their inspected source theorem/proof did not supply this exact closed transient profile.

## value

PASS

An exact first-step objective spike and reciprocal post-reset contraction quantify a concrete safety/performance tradeoff missing from qualitative convergence, including x2=x0 and neutral z=2 resonance. The dimensionless formula is natural for the defined optimizer, potentially useful in learning-rate risk assessment despite a deliberately restricted solvable model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
