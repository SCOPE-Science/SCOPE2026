# Independent mathematical audit

## correctness

PASS

Stationarity plus the integral velocity relation gives D+Dᵀ=0 by integrating the derivative of XXᵀ and taking expectations (finite stationary second moments suffice for this interchange). Gaussian regression gives V=DᵀC⁻¹X+ε with independent residual of covariance R>0 and JDᵀ=hI. Whitening and diagonalizing yields L in law as Σ_j(hZ_j²+√λ_j Z_jY_j) with independent standard normals. Conditional Gaussian integration gives exactly the two factors and the moments. The maximal real MGF domain is the intersection of the two strict positivity intervals, i.e. endpoints (−h±√(h²+Λ))/Λ for Λ=max λ_j; the MGF diverges at and beyond the relevant endpoints. Conditioning on the two Z's gives an everywhere positive continuous density: the reciprocal standard deviation is bounded by 1/(√(min λ_j)|Z|), integrable in dimension two. For necessity, a density reflection with slope a makes M(s)=M(−a−s); the finite domain contains 0 and −a, hence has an open neighborhood of the midpoint. Thus the quartic denominator is invariant under the same reflection. For unequal λ_j the factor with larger λ_j has both roots strictly closer to zero on their respective sides, so reflection pairs the outer roots and pairs the inner roots. Their midpoints are −h/λ_j, which cannot coincide for h≠0 and unequal λ_j. At h=0 symmetry is immediate; equal λ produces the quoted asymmetric Laplace density by integration, with slope 2h/λ. The sharpness family satisfies the Lyapunov equation, and a drift root z with Re z≥0 would satisfy z²+z+1+ε=±i, forcing |Im z|≤1 and a positive real part for the left-hand side, a contradiction. Its full covariance is positive for ε>0 and the ratio tends to one. In the conservative example exact block substitution gives E=CK+D and −KD−DᵀK−2E+diag(2,6)=0. Since CJRJᵀ=CJEJᵀ−h²I, the discriminant is that of the latter unshifted matrix, whose numerator over 1089 has entries (2062,−474;−1194,2488); this gives 24700/11979 as stated.

## originality

PASS

Credit the general Gaussian quadratic-form law, and credit the prior inertial-gyrator results for the same observable's mean, numerical distribution or time-integrated fluctuation measures. The supported distinct claim is the complete stationary covariance criterion for an exact one-time angular-momentum density ratio, with physically realizable sharpness and obstruction examples. Neither a general determinant transform, a finite-step overdamped law nor the inspected same-observable inertial passages supplies that criterion or its covariance interpretation as stated.

## value

PASS

A nonzero mean current can coexist with or without an exact linear log-density ratio, so inferring a single asymmetry slope from rotation alone is not justified. The criterion isolates the relevant conditional covariance and supplies a conservative two-temperature counterexample and a nondegenerate family approaching the universal SNR bound. These permit interpreting instantaneous rotation laws without mistaking them for integrated fluctuation theorems. The significance is the obstruction and realizations, not rederivation of the Gaussian determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
