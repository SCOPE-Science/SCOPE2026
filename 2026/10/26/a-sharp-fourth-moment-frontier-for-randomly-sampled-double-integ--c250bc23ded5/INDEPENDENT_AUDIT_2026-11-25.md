# Independent mathematical audit

## correctness

PASS

Integrating the held input gives A(h)=I+hC_1+h^2C_2 with C_2=-e_1(k_p,k_d)/2. Independence gives the homogeneous PSD-positive covariance recursion on real symmetric matrices. A power bound of the covariance map gives the required second-moment bound, while a uniform trace bound on rank-one inputs bounds powers on the whole symmetric space by positivity and signed spectral decomposition. At matching raw moments through degree three, the difference of the maps is exactly Delta m_4 times C_2 X C_2^T, PSD-positive for nonnegative Delta m_4. By composition the powers are ordered, and the spectral operator norm induced by the order unit I for a positive map is its norm on I; Gelfand's formula gives the universal weak spectral ordering without a strictness assertion. My independent exact coefficient-matrix calculation (python /workspace/checks/4.py with SymPy, output /workspace/checks/4.txt) gives the entire S(m), both moment lists and det(I-S)=24/25*(642421/270000-m), and solves the adjoint Lyapunov equation at the smaller feasible m to obtain the printed positive definite P with identity residual. Ordering proves stability below the smaller example. Mixtures of the positive endpoint laws realize every m between them, so the continuous cone-Perron spectral radius stays below 1 until the unique determinant root and equals 1 there. Above it, the monic real characteristic polynomial is negative at 1 and positive for large arguments, forcing an eigenvalue >1 (also for feasible moments beyond the two examples). For that case the PSD dual Perron eigenmatrix W has x^T W x>0 for some deterministic starting state x, and its expectation grows by rho^j, so the second moment has an exponential lower bound. This is a sampled-index result only. The included script was inspected, not executed.

## originality

PASS

The supported distinct content is the fixed-lower-moment fourth-moment order from the double-integrator hold architecture, plus a sharp threshold witnessed on two strictly positive laws with matched lower moments and identical support. The generic covariance/mean-square criterion is not new. Direct local comparisons did not cover the ordering or boundary. The historical control-paper comparison is access-limited; it contributes residual risk, not negative full-text evidence. The verdict is bounded to actual available statements and their implications.

## value

PASS

This answers a natural robustness question for the standard held double integrator: how much of a sampling law must be known to certify mean-square stability? The monotone PSD order at fixed lower moments is structural for all positive gains, and the single realizable class witnesses a sharp failure of lower-moment summaries even on identical support. The particular fraction is useful as a certified matched-moment benchmark, not a general gain-independent performance limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
