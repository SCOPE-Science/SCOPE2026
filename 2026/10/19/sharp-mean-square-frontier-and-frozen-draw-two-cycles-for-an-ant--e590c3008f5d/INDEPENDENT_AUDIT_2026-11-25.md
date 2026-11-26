# Independent mathematical audit

## correctness

PASS

The ratio of the two Gibbs weights is exp(−2cZx/a), giving the stated odd map. For x>0 set b=cx/a and H=tanh(b|Z|)/(b|Z|). Under the probability tilt dQ=Z²dP, H decreases strictly with Z² and lies strictly between zero and one except on a null set. The independent-copy covariance identity gives E_Q[Z²H]≤E_Q[Z²]E_Q[H]=3E_Q[H]; replacing H by H² makes the bound strict. Thus E[Z²tanh²(bZ)]<3b E[Z tanh(bZ)], proving strict descent even at c=2/3. Expansion of the map gives (1−cZ²)x+c³Z⁴x³/(3a²)+O(c⁵|Z|⁶|x|⁵/a⁴). Gaussian moments justify the squared expansion, yielding the linearized second moment 1−2c+3c² and quartic coefficient 2c³(1−5c)/a², equal to −112/(81a²) at the boundary. Hence above the boundary small nonzero starts fail one-step descent, not necessarily almost-sure convergence. Fresh independent draws give a nonnegative square supermartingale, and telescoping gives finite total expected drift. Continuity and strict positivity of that drift away from zero exclude a positive limit of the squares. For frozen z≠0 the scaled map is v−tanh(dv), d=cz²: strict magnitude decrease at all v≠0 for d≤2 yields global convergence by continuity. For d>2, the slope at zero is below −1; tanh(dv)/v decreases from d to 0 and crosses 2 exactly once at v*>0. Strict concavity of tanh on positive arguments gives 0<d sech²(dv*)<tanh(dv*)/v*=2, so the cycle multiplier is below one in magnitude. The Gaussian two-sided tail of d>2 is erfc(1/√c), not an assertion about all initial points in that regime. The supplied numerical checker does not replace these analytic checks.

## originality

PASS

The underlying Gaussian proximal formula and scalar flip tools are established. The inspected nearby antithetic and period-two records concern different update maps, and the closest primary convergence results concern exact integrals, Monte Carlo estimation error, or independent proposals with variable sample size. None of the compared statements covers the fixed two-point antithetic quadratic estimator's global one-step boundary, neutral endpoint coefficient and contrasting reuse laws. This is a bounded comparison, not historical priority certification.

## value

PASS

An antithetic pair is a natural low-cost Gaussian estimator, and reusing random samples changes the iteration rather than the population proximal map. The sharp all-input step restriction, strict quartic drift at the neutral endpoint and positive-probability frozen instability even where fresh draws converge give an actionable distinction between these policies. A local multiplier alone would miss that distinction and would not resolve the neutral endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
