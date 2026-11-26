# Independent mathematical audit

## correctness

PASS

For fixed pair parameters write x=1−u and y=1−v. The discounted sums d_1,d_2 of the two players' defection probabilities satisfy d_1=1/2+δx d_2 and d_2=1/2+δy d_1. The donation payoff is (b−c)/(1−δ)+c d_1−b d_2, which verifies the pair formula independently of the four-state inversion. Exchangeability gives the penalty kernel (1+δ(x+y)/2)/(1−δ²xy) multiplied by (b−c)/2. Independence turns its uniformly convergent geometric expansion into Σ_j δ^(2j)(m_j²+δm_jm_(j+1)). Jensen gives nonnegative termwise differences relative to the constant law, and the first possibly nonzero term is δ³μVar(X), with all higher terms bounded by O(δ⁴) as δ→0. Nonconstant nonnegative X has μ>0, so positivity is strict. Convex order increases every entering moment; the endpoint law gives the simultaneous chord bounds at fixed mean. Strict convexity of x² and its positive δ³μ coefficient force endpoint support for equality at a nontrivial maximum. Boundary means admit only a constant law. The exact kernel evaluated at the two endpoints gives the displayed envelope. The stationary multinomial probabilities are geometric in the level index under the stated IGT parameters; the iid comparison uses that one-agent law, not a conditional comparison at a realized finite-population mean. Evaluating the four ordered pairs in the example gives 21/16 versus 4/3, as stated. The finite checks were inspected, not executed; the moment argument establishes the result for arbitrary probability laws on the interval.

## originality

PASS

The exact pair payoff, multinomial stationary law and use of an average-generosity payoff are prior work. The distinct supported claim is the strict iid sign, positive leading variance certificate and sharp distribution-free envelope with its equality laws and convex-order monotonicity. The strongest available prior bound in the same IGT setting concerns a different averaging operation and does not give these sign and extremal statements.

## value

PASS

Replacing heterogeneous generosity by its mean is an approximation already used in the motivating model. A sign-definite nonvanishing bias, explicit positive variance certificate and uniquely sharp worst case give directly useful information not supplied by a numeric example or an unsigned error bound. The convex-order comparison describes which changes in the law can worsen the bias without changing its mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
