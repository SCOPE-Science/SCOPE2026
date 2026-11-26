# Independent mathematical audit

## correctness

PASS

For the fixed nonzero PSD matrix and reused probes at budgets 1,2,4, substitution gives T=x-B/(S-c), where B=(y-x)^2, c=3y-x and S=X3+X4 is independent of x,y. The gamma-simplex bound for g, the density of S, is O(s^(rank(A)-1) exp(-cs)) and in particular g is bounded even at rank one. For t>|x-mu| the pole windows on the positive and negative sides have lengths B/(t+x-mu) and B/(t-x+mu). Conditional on c>0 both contribute B g(c) after multiplication by t; for c<0 neither contributes in the limit, and c=0 is a null set. The bound 4B sup(g) on |x-mu|<=t/2 and the exponential complementary x-tail justify averaging. Positivity on x<3y away from x=y gives a nonzero constant, so tail integration gives exactly the stated positive moment range. For the ridge, H=delta*u reduces the rescaled squared correction to the integrable kernel u^2/(1+u^2)^2 of mass pi/2; bounded g and finite E[B^2] dominate it. The uncorrected square vanishes after scaling and the cross term is O(sqrt(delta)) by Cauchy–Schwarz. Independently integrating v^r(2-v) on [-1,2] gives 9/4 and 27/10, and the remaining gamma integrals at rate 2 give J2=27/256 and J4=243/256 for I2. This verifies the two explicit constants. The frozen verifier was inspected, not executed; its finite simulation and historical status are not used as proof.

## originality

PASS

The pole mechanism, Aitken identity, and threshold exponent have close precedents. The supported distinct result is the sharp all-PSD law, including rank one, for the dependent numerator and denominator of the specified nested Gaussian quadratic-form samples, together with the smooth-ridge coefficient and its explicit I2 specialization. Neither the deterministic probing paper nor the inspected indexed Gaussian observation and Anderson models establishes that joint-law-and-ridge result. The conclusion is best-of-evidence, not a priority certification.

## value

PASS

The nested doubling budget is a natural way to reuse costly matrix-vector probes. The result quantifies a real risk of applying deterministic acceleration to those means: even absolute error of order one has no first moment, and smoothing trades the pole for MSE of order 1/delta with an explicit strictly positive coefficient. This is actionable insight about the proposed acceleration and regularization, not merely restatement of the Aitken identity. It does not claim an optimal ridge or discredit deterministic probing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
