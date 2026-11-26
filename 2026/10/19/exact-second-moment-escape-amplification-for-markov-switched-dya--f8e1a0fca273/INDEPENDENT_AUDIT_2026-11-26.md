# Independent mathematical audit

## correctness

PASS

A hole is hit exactly when two successive fair bits equal the current environmental bit. For r=1 or 2 replicas conditional on the same environment, if k current bits match, those k next bits must all be opposite the environment for survival (factor 2^-k). The other r-k next bits remain fair. Persistence gives zero known matches at the next step, and a flip gives k; this recovers both substochastic matrices and the binomial initial weights. The first-moment roots, coefficients from a_0=1 and a_1=3/4, and the p=0 Jordan limit agree. For 0<p<1 the two-replica matrix is primitive since the square has positive entries. Exact characteristic-polynomial expansion and reduction modulo the first-moment quadratic give P_p(q²)=4p(p-1)q(q-1)(4q²-3)<0; its positive cubic leading coefficient forces a real root above q². The Perron projection has positive prefactor, giving the stated moment and variance rates. At p=0 and p=1, complementing all bits pairs the two possible environments and Q_n is nonrandom. Independent replay: python3 /workspace/branches/independent_checks.py 3; symbolic polynomial and remainder identities plus 132 exact comparisons using absolute environmental and bit states instead of match-count states.

## originality

PASS

Prior literature supports transfer operators, stochastic escape and the shared-versus-independent environment distinction. The supported distinct claim is the exact two-replica law with the strict Perron gap for the whole interior persistence range, not the transfer recipe, Jensen's inequality, or the fair iid first-moment baseline.

## value

PASS

For the shortest complementary repeated-bit holes, persistence changes the distribution of survival over environments. The result gives a tractable benchmark where relative variance grows strictly exponentially at every stochastic parameter despite being identically zero at either deterministic endpoint. An exact rate and an all-parameter witness are useful for understanding when annealed escape alone hides large dispersion; this is more than applying a transfer matrix or establishing positive finite-time variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
