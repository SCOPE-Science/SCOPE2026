# Independent mathematical audit

## correctness

PASS

Uniform 2-adic convergence of 2^k binom(x,k)^2 follows binom(x,k)∈Z_2. Vandermonde gives (B_k(x+h)−B_k(x))/h=Σ_{j=1}^k B_{k−j}(x)binom(h−1,j−1)/j, whose valuation is ≥−floor(log₂k), uniformly in h≠0. Thus k≥5 contributes 2^{k−floor(log₂k)}≥8 to the difference quotient, permitting termwise passage. For k≤4 coefficients of P_k=2^kB_k² have 2-adic denominators at worst 4, so for h∈32Z_2 finite differences agree with derivatives modulo8. Derivative integrality bound for k=3,4 puts them in 8Z_2; k=1,2 yield 4x+2x(x−1)(2x−1). Reducing at b≡1,2 mod4 gives exactly 4 mod8, and comparing increments 2h and h proves r+2 valuation. Independent Delannoy recurrence checked 60 valuations with b in both classes and 96 modular slopes; noninteger ordinary division for h with odd factors was properly treated by division in Z_2 (invert the odd factor mod8).

## originality

PASS

Best-of-knowledge originality assessment: the exact new claim was compared by implications with same-object primary results; known definitions/source results are credited, and no directly covering proved theorem was identified in the inspected material. This is not exhaustive priority certification. A uniform dyadic first-difference congruence for central Delannoy numbers. The proof uses uniform binomial derivative congruences to establish a genuinely new implication beyond the cited prior theorems, restricted to the first stratum.

## value

PASS

Resolves the full first nonzero valuation stratum of Lengyel’s explicitly published dyadic-difference conjecture with a universal threshold r≥5 and stronger interpolation congruence. The result measures cancellation between Delannoy values not determined by known one-term valuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
