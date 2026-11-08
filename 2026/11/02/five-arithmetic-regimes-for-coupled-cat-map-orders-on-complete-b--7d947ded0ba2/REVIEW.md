# Independent mathematical audit

## correctness

PASS

For a,b,s>=1 the bipartite adjacency matrix satisfies A^3=ab A and A^4=ab A^2. Matrix Cayley-Hamilton over integer polynomial ring gives q_{t+1}(z)=(z+2)q_t(z)-q_{t-1}(z) and p_t=(q_t-q_{t-1}-1)/z. Exact T^t-I block expression reduces identity mod 2^s to simultaneous divisibility 2^s|q_t(z) and 2^s|gcd(a,b)p_t(z), so collapsing to a 2x2 z-only cat map would be incorrect. Explicit factorization and parity gives base orders 2,4,3 with exact valuation anchors; binomial lifting from h>=2 gives one extra 2-adic valuation per squaring. This proves all five arithmetic regimes with odd z=3 mod4 s=1 boundary. T is invertible shear product so all states are periodic, and a finite group cannot be union of two proper kernels, giving some primitive cycle of full matrix order. Independent modular exponentiation checked 150 cases a,b<=5,s<=6 and distinguished K1,4 from K2,2 although same ab=4.

## originality

PASS

General symplectic shear construction, matrix-Fibonacci recurrence, and two-dimensional Arnol'd cat-map period theory are prior. The gcd(a,b) congruence and its complete parity-/valuation-stratified exact order for all complete bipartite graphs and powers of two are not implied by cited circulant/complete-graph examples. The same z but different orders directly rules out reducing this classification to a scalar cat-map parameter. Residual risk: earlier modular graph dynamical systems may have an equivalent complete-bipartite formula.

## value

PASS

Complete-bipartite graph cat-map couplings are a natural structured graph family, and exact finite-ring orders control all possible periods and recurrence horizons. The theorem establishes a sharp five-regime arithmetic phase diagram and demonstrates that shore gcd rather than edge count alone changes global dynamics. Its exact orbit-realization result is meaningful, not a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
