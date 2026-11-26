# Independent mathematical audit

## correctness

PASS

For positive shift weights the polar isometry is S and the transformed weights are their adjacent geometric means. Logs are iterated by B=(I+R_theta)/2. The weighted-shift difference norm is the supremum of the weight differences, which, by density, equals the maximum of |exp(B^k g)-1| on the circle; on [-||g||_infty,||g||_infty] this is comparable to ||B^k g||_infty with the frozen constants. Nonzero Fourier modes decay individually since |lambda_m|=|cos(pi m theta)|<1, and mean-zero trigonometric approximations and contractivity extend convergence to continuous g. Under bad approximability the multiplier is bounded by exp(-2c_theta^2 k/m^2), so splitting at u=k^(1/3) yields the upper estimate from the analytic Fourier tail. For the Poisson lower bound one can independently pick a mode by taking the smallest circular gap of the floor(u)+1 distinct points j theta for 0<=j<=floor(u). It gives 1<=m<=u with ||m theta||<1/u, irrespective of continued-fraction initialization. At k>=64 this distance is at most 1/4, where log cos(pi d)>=-10d^2 from the second derivative bound. The m-th Fourier coefficient gives ||B^k g_rho||_infty>=exp(-(rho+10)u); ||g_rho||_infty=M_rho since equality with the sum bound holds at zero. For the Liouville claim, the nested denominators give positive rational approximation errors <=2/q_(j+1) and thus irrationality (contradicting the 1/(b q_j) lower bound for a fixed rational of denominator b) and arbitrarily large Liouville exponents even after reduction. The lacunary log is analytic on the claimed strip and has norm <1 by its absolutely convergent Fourier series. The chosen q_j mode has ||q_j theta||<=1/(50 sqrt(k_j)), leaving an exponential norm lower bound at least e^(-1-10/2500)e^(-q_j)>e^(-q_j)/4>=epsilon_(k_j). The argument uses one mode, so cancellation in pointwise evaluation cannot invalidate it. The frozen verify.py was read, not executed; no finite tests are premises.

## originality

PASS

Pass for the sharp Poisson-profile Aluthge rate with the uniform lower barrier and analytic Liouville slow subsequences, not for the binomial update or using arithmetic to control rotation-walk modes. Su's centered random walk is the same averaging kernel modulo translation and is the strongest methodological antecedent found; its discrepancy estimates are not analytic-observable estimates with matching upper and lower scales.

## value

PASS

The norm identity puts a concrete operator iteration in direct correspondence with analytic smoothing of a quasiperiodic profile. The Poisson example shows a sharp bounded-type exponent and an explicit lower barrier across all irrational rotations, explaining why an a priori faster rate would be wrong. The analytic slow subsequences distinguish qualitative norm convergence from rates uniform over arithmetic regimes. These are complementary quantitative claims, not an exact constant or an all-iterations slow example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
