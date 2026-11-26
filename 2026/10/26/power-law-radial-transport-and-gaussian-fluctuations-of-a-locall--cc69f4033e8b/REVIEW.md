# Independent mathematical audit

## correctness

PASS

For alpha>1, the commuting finite-flip Hamiltonians converge in norm. Their Born laws factor as Bernoulli bits with probabilities sin^2(tck^(-alpha)); Hilbert-norm convergence implies total-variation convergence of the Born laws, and the independent product has finite support almost surely in the sense of finitely many occupied coordinates, since the probabilities sum. No division by a cosine is used. With N=(ct)^beta, the normalized mean is the Riemann sum of sin^2(x^(-alpha)); the oscillatory portion on (0,epsilon) is bounded by its interval length up to discretization and the tail is dominated by x^(-2alpha). Substitution v=2x^(-alpha) and integration by parts reduce the limiting integral to 2^(beta-1) times the sine transform of v^(-beta), giving the claimed gamma-cosine value for 0<beta<1. The variance identity V_t=mu_(2t)/4 fixes the factor 2^(beta-2). For centered Bernoulli variables sum of third absolute moments is at most V_t; finite Berry–Esseen passes to the countable sum by L^2 convergence at each t and continuity of the Gaussian CDF, giving O(V_t^(-1/2)). Chebyshev gives the stated concentration since V_t/mu_t^2 tends to zero.

## originality

PASS

The locally infinite flip Hamiltonian, finite hypercube laws, and independent-sum fluctuation principles are prior. The supported distinct claim is the power-law Hamming observable's sharp moment equivalents and limiting fluctuation law with explicit Fano ratio. No inspected stronger source or exact indexed result covered that combination.

## value

PASS

Graph distance is a natural transport observable for this infinite weighted model, and the complete power-law scaling separates the spreading exponent, its dimensional prefactor and the asymptotic variance-to-mean ratio. Those quantities identify how spread and fluctuations depend on alpha and do not follow from existence of unitary dynamics or from the generic CLT alone. The contribution is the sharp model-specific calculation, not a new independent-sum limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
