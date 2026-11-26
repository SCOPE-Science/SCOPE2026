# Independent mathematical audit

## correctness

PASS

Scaling the negative derivative by 1-e^{-z} makes the four Hermite conditions exactly unit mass and two prescribed endpoint values for a nonnegative polynomial. For degree at most one of this derivative polynomial the affine mean is (z/2)coth(z/2)>1. For even derivative degree 2k, the interval square representation fixes the endpoint magnitudes of its unweighted square term. The minimum mass is the endpoint Gram-inverse form; equalizing the sign of the endpoint product with the off-diagonal Gram entry gives the stated smaller value. For odd derivative degree 2k+1 the two independent weighted squares minimize separately, with squared evaluation norms (k+1)(k+2); the stated Jacobi normalization gives per-degree kernel summands 2(j+1). Both optima can be increased to mass 1 by adding a nonnegative multiple of theta(1-theta), which preserves the two slopes and fits the degree. Each cutoff function is strictly increasing on z>0 and crosses 1. At fixed z>0 successive minima strictly decrease: I_o(k)<I_e(k-1) for k>=2 by denominator comparison, and I_e(k)<I_o(k) by a_z+b_z>2 sqrt(a_z b_z). Large-z cutoffs give 2 sqrt(z)+O(1). For complete monotonicity the signed derivatives at theta=1 identify nonnegative Taylor coefficients in 1-theta, sufficient also throughout the interval. The residual coefficient mass S and first moment M require support reaching ceil(M/S), attained on its floor and ceiling (one index at integer equality). Because M/S>2 and M/S=z+O(z^2 e^{-z}), this proves the exact budget and growth. Independent exact monomial moment-matrix inversion checked k=1 through 6, and 55-digit bisection reproduced the printed cutoffs 3–6; replay python3 /workspace/branches/independent_checks.py 5. This does not certify all degrees by enumeration. The supplied checker was inspected, not run.

## originality

PASS

The assessed contribution is the joint sharp degree budget for exact two-state decay Hermite data under ordinary and complete monotonicity. Credit existing cubic monotonicity theory and classical nonnegative-polynomial representations and kernels. In particular the even output degree mass bound is a consequence of classical Gauss–Lobatto quadrature: its two endpoint weights for k interior nodes on [0,1] are 1/[(k+1)(k+2)], and the interior node polynomial squared times a nonnegative affine factor realizes the bound. Neither this subcase nor the kernel method itself is a novelty claim. The compared materials do not establish the full joint budget or its sharp growth separation.

## value

PASS

The exact Hermite stiffness problem is a motivated design benchmark: for a given z it discriminates infeasibility from insufficient construction and identifies an asymptotically different cost of enforcing all derivative signs. The step thresholds and realizable extremizers sharpen that tradeoff beyond fixed cubic tests. No interior accuracy or solver performance is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
