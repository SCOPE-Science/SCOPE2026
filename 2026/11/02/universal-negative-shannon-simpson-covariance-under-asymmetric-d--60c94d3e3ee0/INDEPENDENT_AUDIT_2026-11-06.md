# Independent mathematical audit

## correctness

PASS

Dirichlet monomial moments E prod X_i^{u_i} are gamma-ratios. Differentiation at exponents yields E X_i log X_i X_j^2, with distinct diagonal corrections for i=j. After subtracting EH EQ, exact covariance is -[(A^2-sum alpha_i^2)/(A+1)+2A Cov_w(alpha_i,psi(alpha_i+1))]/[A(A+1)(A+2)]. First numerator part is strictly positive for m>=2 positive alpha, and second nonnegative since digamma is strictly increasing: Cov_w(f,g)=sum_{i<j} w_i w_j (f_i-f_j)(g_i-g_j). Thus universal strict negative sign. For m=2, alpha=(1/2,3/2) weighted digamma covariance=1/8, giving -1/24, compared to -1/36 at (1,1); same A=2. Independent high-precision mixed-moment calculations directly summed derivative terms for five positive vectors including nonsymmetric reals and reproduces exact rational cases. m=1 excluded; no claim about stochastic negative association.

## originality

PASS

Wolpert–Wolf 1994 derive Bayesian Shannon moments; Cerquetti 2014 derives single-order Tsallis diversity moments and limits, with different entropy/Simpson orders. Their inspected full-text results do not supply mixed Shannon-vs-Simpson covariance for arbitrary asymmetric Dirichlet concentration or its strict sign decomposition. A direct moment-differentiation computation uses standard calculus, but the universal sign and fixed-total counterexample are not found in inspected sources. Best-of-knowledge original, with specialized joint-diversity literature remaining priority risk.

## value

PASS

Shannon entropy and Simpson concentration are standard diversity/uncertainty measures with different sensitivity. Their joint posterior-prior dependence under asymmetric Dirichlet laws matters when comparing both indices; an exact strictly negative covariance for *all* concentrations is a nontrivial structural sign theorem. The fixed-total asymmetric example disproves a natural symmetry-maximal dependence heuristic. Useful exact invariant beyond a textbook expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
