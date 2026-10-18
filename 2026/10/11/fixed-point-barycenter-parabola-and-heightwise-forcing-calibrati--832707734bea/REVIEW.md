# Independent mathematical audit

## correctness

PASS

For any compact invariant measure of xdot=y, ydot=z, zdot=x²-cx-by-az (a,b,c>0), applying the invariant generator to arbitrary C¹ coordinate primitives yields E[y|x]=0, E[z|y]=0, E[x²-cx-by|z]=az. Integrating gives E[y]=E[z]=0 and E[x²]=c m, hence Var(x)=m(c-m), 0≤m≤c and Var(x)≤c²/4. Equilibrium atoms at x=0,c prove sharpness; variance-zero endpoints force x constant along full invariant trajectories, hence y=z=0 and the corresponding atom. Set Q=x²-cx-by=az+zdot: E[zdot|z]=0 gives Var(Q)=a²Var(z)+E[zdot²] and Cov(z,Q)=a Var(z). If E[zdot²]=0, continuity and invariance force zdot≡0 on support, z constant and bounded completeness then y=z=0 and equilibrium support. Thus non-equilibrium measures have 0<Corr(z,Q)<1. Checked exact rational algebra of inspected verify.py; its simple asserts do not prove conditional generator identities, supplied analytic derivation does.

## originality

PASS

The stationary invariant-measure *conditional forcing* and sharp x-barycenter parabola are the final claim; earlier same-system recurrence E[z²]=b E[y²] and period floor are excluded. The inspected 2012 complete Genesio delay-feedback analysis proves stability, Hopf, center-manifold and feedback control, not a stationary moment law. The inspected 2013 jerk paper derives the Newtonian jerk representation, equilibrium/Hopf/chaos diagnostics, not a generator regression. The 2025 Valls global integrability analysis is a plausible stronger result but accessible material does not exhibit stationary conditional moments; full publisher source not read. Comparison is statement-level, not a novelty claim based on title absence.

## value

PASS

Motivation is the actual fixed-point geometry of the Genesio flow: the two distinct fixed points dictate exact barycenter variance for every compact stationary state. The conditional nonlinear-forcing calibration supplies observable height-resolved prediction with mean-square vertical-speed loss; it is a structural stochastic diagnostic absent from scalar recurrence. Sharp equilibrium-mixture envelope and rigid endpoints are useful exact constraints when studying chaotic and periodic invariant distributions, not a trivial numerical slice or already credited E[z²] balance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
