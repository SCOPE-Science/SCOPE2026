# Independent mathematical audit

## correctness

PASS

The exact terminal observable is F(u)=Phi(u_d), gradient phi(u_d)e_d, and E phi(U_d)^2=1/(2pi sqrt3). The centered indicator coefficient is always plus/minus 1/2, so each inner score belongs to the fixed Gaussian endpoint span, has nonzero value a.s. because the d-by-ell endpoint matrix has full column rank, and hence every positive-eigenvalue matrix eigenvector lies in that span. Haar-uniform ell-planes have projection energy Beta(ell/2,(d-ell)/2). Gaussian regression gives E[Phi(U_d)|v^TU]=Phi(cY/sqrt(2-c²)); a bivariate normal orthant identity yields Var=arcsin(c²/2)/(2pi). Monotonicity makes projected e_d the optimal direction; convex arcsine lies below its endpoint chord, proving linear lower bound. For ell=1 outer products equal ZZ^T/4 algebraically. Independent 3 reused-endpoint identity cases and 21 exact risk-floor checks passed. The theorem is explicitly restricted to fresh Gaussian prediction inputs.

## originality

PASS

Best-of-knowledge statement-level comparison supports new combined conclusion within the precise scope; not merely lack of search hits. For an isotropic Gaussian constant-drift SDE and a shared pool of ell<d Brownian endpoints, all positive sensitivity eigendirections belong to the random ell-plane spanned by endpoints; squared alignment bounded by Beta(ell/2,(d-ell)/2), and the optimal single-direction ridge error equals 1/12-arcsin(P/2)/(2pi), bounded below by (1-P)/12 independent of outer sample count; ell=1 makes Khat=ZZ^T/4 for all outer samples. Historical priority remains qualified.

## value

PASS

This quantifies a structural common-random-number failure mode of nested score estimation: arbitrary outer sample budgets cannot overcome a fixed shared inner-path span, even for a genuinely rank-one population sensitivity. Exact alignment distribution and Bayes ridge-risk floor inform sample allocation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
