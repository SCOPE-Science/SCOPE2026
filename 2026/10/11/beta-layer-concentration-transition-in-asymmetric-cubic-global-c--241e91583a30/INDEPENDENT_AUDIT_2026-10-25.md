# Independent mathematical audit

## correctness

PASS

Direct differentiation verifies H=log(1+alpha x²)/alpha+log(1+beta y²)/beta constant, and grad H vanishes only at origin. Positive levels are regular compact closed ovals and dynamics has no critical points on them. On each quadrant 1+alpha x²=e^(Lu), 1+beta y²=e^(qL(1-u)); the physical-time Jacobian equals (L sqrt(q)/2)e^(-qL/2)e^((q-1)Lu/2)/sqrt((1-e^(-Lu))(1-e^(-qL(1-u)))) and the four symmetric quadrants give period T=2L sqrt(q)e^(-qL/2)Z. For fixed q>1, s=L(1-u) yields q^(-1)B((q-1)/(2q),1/2); for q<1, s=Lu yields B((1-q)/2,1/2). Splitting s at L/2 bounds remote endpoints by decaying exponentials times integrable square-root singularities; it supplies tightness, weak convergence and period coefficients. For q=1+gamma/L, dominated convergence under C[u(1-u)]^(-1/2) proves Z→∫exp(gamma u/2)du and the stated tilted law. All displayed ranges, gamma positive/negative and physical-time normalization were rechecked. Independent sympy differentiation and mpmath 45-digit x-quadrature versus u-quadrature show <=6e-14 relative error in two examples; four fixed-q asymptotic and four crossover numerical specializations agree with the claimed limits. They corroborate but do not prove the infinite limits.

## originality

PASS

At the frozen source tree the theorem concerns original-physical-time distributions and the two beta-layer asymptotics for all fixed q!=1 plus q=1+gamma/L. Full text of the direct cubic global-center paper (arXiv:2310.07454) gives precisely the underlying vector field (33) and center classification but not the stated high-energy occupation distributions or crossover. The complete earlier 2020 author preprint classifies global-center existence, while the 2016 Liénard-II source gives general period quadratures and monotonicity, not the beta limits. A published balanced q=1 result shows an explicitly different uniform law. Searches returned the exact mirror (excluded as self-coverage) and adjacent but non-implicative findings. This is best-of-knowledge originality, not a proof that every relevant source was indexed.

## value

PASS

The underlying unequal-coefficient cubic global center is a natural classified polynomial dynamical family; original physical-time occupation of its logarithmic first-integral share is a motivated intrinsic high-energy statistic. The answer includes exact finite-amplitude law, two distinct beta-layer probability measures and physical-period exponents, plus a sharp inverse-log coefficient crossover that changes a delta endpoint limit into a nondegenerate exponential tilt. These are natural precision facts for orbit averages and are not textbook deductions from existence of global centers or a mere relabeling of q=1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
