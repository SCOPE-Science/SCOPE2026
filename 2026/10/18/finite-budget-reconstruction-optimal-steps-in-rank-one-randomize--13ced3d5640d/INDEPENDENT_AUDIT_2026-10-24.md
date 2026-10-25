# Independent mathematical audit

## correctness

PASS

For deterministic real coordinate steps on one row A=(1,...,1), b>=2, y≠0, iid uniform coordinate picks, residual r_k=y∏_{j<k}(1−eta_j) is deterministic. Writing effective weights w_k=eta_k∏_{j<k}(1−eta_j), W=Σw_k, independence gives risk/y²=(1−W)²/b+((b−1)/b)Σw_k² exactly. Cauchy–Schwarz minimizes Σw² at fixed W by equal weights and a strictly convex scalar quadratic fixes W=N/(N+b−1). The uniquely realized schedule eta_k=1/(N+b−1−k) has nonzero residual y(b−1)/(N+b−1) and risk y²(b−1)/(b(N+b−1)); W=1 interpolation instead costs y²(b−1)/(bN), unique equal weights. For constant 0<eta<2 geometric weights give risk floor y²(b−1)eta/(b(2−eta)) and one-step difference −y² eta(2−b eta)(1−eta)^(2N)/b, with eta=1 residual-zero exception. Independent direct rational enumeration of all coordinate index paths for (b,N)=(2,4),(3,4),(4,3), y=2 reproduced optimum risks 2/5,4/9,1/2; the algebra covers all real schedules and horizons.

## originality

PASS

Best-of-knowledge PASS for unique finite-budget reconstruction-optimal *deterministic* steps in this rank-one underdetermined example; not for the underlying Jin–Liu block-coordinate method or known least-norm failure of ordinary randomized Gauss–Seidel. The exact sharp sample-budget schedule and noninterpolation law were not found in accessible cited primary theorems, although similar optimal-weight arguments might exist elsewhere.

## value

PASS

A concrete sharp example exhibits the tension between observation-residual convergence and Euclidean reconstruction to the minimum-norm solution. The finite-budget unique schedule, exact bias-variance frontier and stepwise monotonicity transition provide useful calibration for rank-deficient stochastic block algorithms beyond a routine convergence statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
