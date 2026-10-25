# Independent mathematical audit

## correctness

PASS

For H=mu P_E+mu kappa(I-P_E) and W_gamma=I+(gamma-1)P_F, cosine-sine principal planes give a 2x2 positive block of determinant kappa*gamma and trace a+gamma*b, where a=kappa*cos(theta)^2+sin(theta)^2 and b=cos(theta)^2+kappa*sin(theta)^2. The maximum principal angle yields BOTH spectral extrema by trace monotonicity at fixed determinant; uncoupled diagonal eigenvalues lie between the extreme roots. Minimizing a/sqrt(gamma)+b*sqrt(gamma) for gamma>=1 gives unique gamma*=max(1,a/b), strict improvement only theta<pi/4, and exact (sqrt(1+z^2)+z)^2 optimal condition number there. At theta>=pi/4 gamma*=1 and condition=kappa. Bounded high-contrast condition forces theta=O(kappa^-1/2), and the stated critical-window limit follows from z. Valid for d>=2, 1<=k<d, kappa>1, theta in [0,pi/2]; no claimed bound for other spectral levels, anisotropic boosts, or CG iteration cost. Independently assembled 64 matrix spectra at mixed principal angles and compared characteristic roots and optimized gains numerically; bounded checks are not the all-d proof.

## originality

PASS

Best-of-knowledge statement-and-implication originality check after current primary reading and published-Resultary search. Equivalent forms, broader theorems, exact tables, and prior implication are assessed separately; residual risks are not hidden. Prior singular deflation, projection and multilevel coarse corrections do not imply the optimal gamma for W_gamma in a two-level SPD system without an extra spectral calculation.

## value

PASS

Low-rank coarse-space preconditioners require a quantitative tolerance for subspace error. The exact worst-angle reduction, unique optimal boost, pi/4 no-gain boundary, and kappa^-1/2 contrast threshold provide a sharp design criterion rather than a generic spectral approximation estimate; natural two-level test problems and any rank k are covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
