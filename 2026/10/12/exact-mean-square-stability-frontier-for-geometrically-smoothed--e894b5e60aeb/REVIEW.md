# Independent mathematical audit

## correctness

PASS

Independently derived the exact coordinate matrices J0=[[1,M],[0,beta+(1−beta)M]] for missed row, J1=[[0,M],[-(1−beta),beta+(1−beta)M]] for selected row; their covariance map is the printed 3x3 T. Symbolic SymPy determinant factoring reproduces det(I−T)=π(β−1)[2(1−β)^2 M²+LM+C] with printed L,C. Its quadratic has one positive root and T(0) spectral radius<1 for π in (0,1), beta<1; positivity of the map makes its spectral radius a nonnegative eigenvalue, so no crossing of radius 1 without det=0. Above the root the determinant sign produces a real eigenvalue>1. Starting from (u0≠0,v0=0), the one-step covariance diag(1−π,π(1−β)^2) is positive definite, hence excites every positive-semidefinite Perron direction, proving boundary nondecay and supercritical exponential growth of E[u²]. The u-coordinate of any Perron eigenmatrix must be positive for M>0. Verified βcrit=(5−sqrt17)/2 and β=0,π=1/2,M=.9 gives mean-square radius≈1.20656 while signed H spectral radius=√.9. Finite rational spot tests in source are corroboration only.

## originality

PASS

Alderman–Luikart–Marshall arXiv:2401.09415v3 was read at the defining update, Theorem 1.1, Section 3 and Section 4.2: it establishes a signed first-moment 2x2 dynamics and asks for critical mass and Euclidean/absolute expectations. A stable expectation need not imply a stable second moment; the explicit rational KGSM example separates them. Bollapragada–Chen–Ward uses minibatch heavy-ball momentum, not this geometrically smoothed single-row state. Independent Resultary and specific mean-square search found no full orthogonal-diagonal threshold. Best-of-knowledge with residual priority uncertainty.

## value

PASS

The sharp exact stability boundary for every row-norm probability in a natural diagonal benchmark resolves a concrete question posed by the algorithm's source. It diagnoses a physically relevant failure mode hidden by signed means and extends the source's first-moment analysis to a new norm moment; not a routine reparametrization of a known Schur bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
