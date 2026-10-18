# Independent mathematical audit

## correctness

PASS

The posterior information matrix P^{-1}+r^{-1}hh^T has trace independent of h in dimension two. Its condition number strictly decreases with its determinant at fixed trace, and the matrix determinant lemma reduces maximal determinant to the simple largest-eigenvalue Rayleigh quotient; hence exactly h=±u_L minimizes conditioning. The posterior variances are Lr/(L+r), mu; division yields q=Lr/[mu(L+r)] and condition max(q,1/q). Solving q=1 gives r*=Lmu/(L-mu), while q<1/(L/mu) is equivalent to r<Lmu^2/(L^2-mu^2). Normalization ||h||=1, positive r and strict L>mu are necessary; exact (4,1) example checks r*=4/3 and r=1/4 gives 17/4. This is an analytic all-parameter proof, not finite extrapolation.

## originality

PASS

The preferred maximum-variance measurement direction is previously recognized in Kalman sensor selection; the candidate cannot claim that alone. Belabbas optimizes estimation error and steady-state Riccati sensor geometry, Tzoumas and others use trace/log determinant, and Wolkowicz (1994) proves condition-oriented quasi-Newton rank-one updates with secant constraints rather than a fixed-noise Bayesian covariance update. Their inspected statements do not explicitly entail the joint optimum posterior anisotropy envelope, unique noise for isotropy and exact prior-worsening frontier. IEEE 1974 Herring–Melsa is a plausible same-subject source but its full text was blocked, so this is a qualified best-of-knowledge PASS with material priority risk.

## value

PASS

The optimum noise strength is a genuine model boundary: one scalar observation can exactly isotropize a 2D uncertainty ellipsoid, whereas improving its precision past a second explicit boundary raises spectral anisotropy above the prior while reducing covariance in Loewner order. The exact direction and thresholds answer a natural sensor-design criterion that is not simply the conventional trace or volume objective; this narrow self-contained closed frontier can inform diagnostic choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
