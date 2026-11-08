# Independent mathematical audit

## correctness

PASS

The loss identity follows from the trace of A^T(I-qq^T)A. For one Gaussian column, diagonalizing C makes T=∑t_j Z_j^2 independent of X^2. At every error threshold strictly inside (mb^2, mb^2+a^2-b^2), the event L<=e is T<=k X^2; conditioning gives a strictly convex function of the spectral weights because chi-square-one survival S has positive second derivative for all positive arguments. Distinct weights give a nondegenerate random linear difference almost surely, so symmetry plus strict convexity proves strict Schur-majorization except permutations. Extremal spectra, exact two endpoint distributions, rank-one mean and correlation-matrix sign-extremizers follow. Applies only to real PSD covariance C with trace m, a>b>0, m>=2, one independent Gaussian leading coordinate, and one test column; not general spectral tails or multiple probes.

## originality

PASS

Qualified PASS: neither the inspected covariance-aware RLA bounds nor oversampled Gaussian sketch analyses state the exact one-probe loss CDF with strict *every-threshold* optimal covariance including fixed unit diagonals. Classical Marshall–Proschan majorization is fully acknowledged as the underlying abstract inequality, not claimed novel. The mapping of this particular loss functional into a strictly convex expectation and fixed-marginal covariance solution is the surviving application result, with residual risk of an equivalent direct corollary or earlier weighted-gamma tail result.

## value

PASS

A natural design question in randomized rank-one projection is whether correlation in equally noisy trailing probe coordinates helps/hurts, at every error tolerance rather than only mean error. The strict spectrum law gives a complete distributional answer and unique worst and optimal designs (for covariance spectrum and for correlation matrices) with exact endpoint CDFs; the result has independent practical/mathematical use as an exact benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
