# Review

## Correctness

PASS. The exact outer-cycle matrix is \((1-\alpha)I+\alpha(I-\eta H)^k\). Diagonalization reduces both convergence and minimax rate to the polynomial \(p(\lambda)=1-\alpha+\alpha(1-\eta\lambda)^k\). For even \(k\), positivity of the inner power makes the classical \(\eta L<2\) frontier unavoidable. For odd \(k\), direct solution of \(-1<p(\lambda)<1\) gives the larger sharp ceiling. The minimax proof treats even and odd parity separately; in the odd case the endpoint-balancing factor is bounded below by the standard repeated-gradient factor through the monotonic auxiliary function \(H(x)\). Equality conditions give the stated unique minimizer for \(k\ge2\).

Risk: the theorem is asymptotic and fixed-parameter. It does not compare stochastic variance or finite-horizon objective transients.

## Originality

PASS. The original Lookahead paper contains the algorithm, a noisy quadratic analysis, a general deterministic quadratic state-space construction, and an adaptive line-minimizing slow step. Its deterministic appendix says the relevant eigenvalues can be computed numerically; it does not state the closed fixed-\(\alpha\) parity frontier or solve the robust interval minimax problem. The adaptive line-minimization proposition is explicitly not used as a novelty claim here.

Later convergence and generalization papers address stationary points, excess risk, or broad nonexpansive interpolation guarantees. The strongest broad comparison inspected proves convergence when the base optimizer is quasi-nonexpansive and gives the classical gradient-step sufficient region. That result does not cover the present odd-\(k\) regime where the individual gradient map is expansive, and it does not imply the exact interval minimax no-acceleration theorem.

Focused semantic searches for Lookahead scalar quadratic stability, odd/even synchronization, supercritical inner steps, exact annihilation, and the slow multiplier found no matching published record. Residual risk remains that an equivalent fixed-polynomial minimax observation appears under stationary iterative-method or relaxation terminology outside the Lookahead literature.

## Value

PASS. The source paper explicitly motivates Lookahead partly by its ability to tolerate larger inner learning rates. The parity theorem identifies exactly when that stabilization is mathematically possible on positive-definite quadratics and describes the sharp boundary dynamics. The minimax theorem then separates stability from acceleration: interpolation can enlarge the stable stepsize region for odd \(k\), but cannot beat optimally tuned repeated gradient descent in worst-case spectral contraction. This resolves two practically distinct questions with one exact benchmark.

Same-model review: passed. Independent audit: not yet performed.
