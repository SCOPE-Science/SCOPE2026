# Independent mathematical audit

## correctness

PASS

In a real Gram factorization A=BB^T with B^TB diagonal, the residual trace is T minus the Rayleigh quotient of B^TB in the chosen row direction, where T=lambda1+lambda2. With t the squared fraction of a nonzero row in the second eigendirection, that gives R=lambda2+(lambda1−lambda2)t. Weighting the rows by squared norm/T gives E[t]=lambda2/T, hence exactly the stated mean. Conversely two rows of norm squared w_j T/2 with second-coordinate fractions t_j and opposite signs of the second coordinate give diagonal covariance contributions w_j T(1−t_j,t_j), without off-diagonal terms. Summing gives the two strictly positive eigenvalues and ensures the two pivots associated to atom j have the prescribed total mass w_j; the endpoint and one-atom cases need no exceptions. Jensen and the secant bound yield attainable convex-order and variance extremes; for m<u<=lambda1 the inequality R−lambda2 >= (u−lambda2)1_{R>=u} is exact on the two-point witness supported at lambda2 and u. The deterministic law handles u=m and lower, and the interval support handles u>lambda1. No fixed-dimension claim is needed.

## originality

PASS

Do not credit the pivot rule, the mean, or a new general convex risk inequality. The supported distinct content is the exact inverse statement: every finite scalar law with the specified interval and mean is attained by real rank-two inputs of the specified spectrum, and the worst-case intermediate tail is attained within that class. The inspected work gives expectations, convex estimates, or different input/sampling restrictions, not this realizability and sharpness.

## value

PASS

A spectrum-only expectation does not quantify the reliability of the randomized numerical step. The converse resolves whether that information can be strengthened to a finer universal distributional constraint: in this base case there is none except finite support, the interval, and the mean. In particular, exact attainable probability at any threshold and actual equal-spectrum witnesses show why the first moment cannot certify typical behavior. The elementary bounds by themselves would not be the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
