# Independent mathematical audit

## correctness

PASS

Independent reconstruction of the source two-stage update gives Y_(j+1)=Y_j-zY_(j-1)+z^2 U_j Y_(j-2) with fresh iid uniform U_j. The symmetric second-moment operator is A X A^T+(z^4/12)X_33 e1e1^T. The cubic Jury f(z)>0 controls mean convergence; the rank-one positive Lyapunov resolvent and symbolic exact identity 1-z^4 H/12=4q/[3(2-z)(z^2+2z+4)f] locate the sole mean-square crossing rho≈1.144476047, below delta≈1.201045931. For z≥rho but z<delta the adjoint eigenfunctional built from e3^T A^k is positive definite (observability matrix spans R^3) and proves nondecay/growth for every nonzero deterministic state. Exact-rational witness z=7/6; independent SymPy reconstruction verified full transfer and crossing algebra. Finite tests alone do not prove tail. Assumptions h=tau, exact arithmetic, newly reconstructed stages, iid uniform fractions and deterministic initial triple are essential.

## originality

PASS

Best-of-knowledge comparison of the same final mathematical statement and direct implications, including exact-model primary sources, relevant general theorems and named residual priority risks. Absence of a matching search hit is not presented as proof of novelty. Source Difonzo preprint proves finite-horizon convergence under regularity; Bochacik et al treat randomized ODE RK, and stochastic S-ROCK methods use Brownian forcing. None of these stronger-looking settings specializes to this exact algorithmic one-cell mean-square cutoff.

## value

PASS

A sharp one-cell randomized DDE stability frontier and a nonempty mean-stable/mean-square-unstable interval characterize a natural numerical stability failure beyond finite-time accuracy theory. This is a motivated analytic threshold, not simply an experiment or stability restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
