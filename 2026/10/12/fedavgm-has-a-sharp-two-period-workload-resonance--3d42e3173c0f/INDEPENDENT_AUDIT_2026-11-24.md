# Independent mathematical audit

## correctness

PASS

The update with Δ_t=(1−q^{K_t})x_t gives x_{t+1}=(β+q^{K_t})x_t−βx_{t−1}. For fixed K the quadratic has determinant β and the values at ±1 are 1−q^K and 1+2β+q^K, both positive. For period two let A_i=β+q^{K_i}. The two-round trace is A_1A_2−2β and determinant β². For a real monic quadratic with nonnegative constant term <1, its roots lie strictly in the unit disk iff both values at ±1 are positive: nonreal roots have modulus the square root of the constant term, and any real root beyond either endpoint forces a nonpositive value there. At +1 the value (1+β)²−A_1A_2 is always positive. At −1 it is (1−β)²+A_1A_2, so equality gives multipliers −1 and −β², and strict negativity gives a multiplier below −1. For workloads 1 and 2 this value is the stated cubic; its derivative is everywhere positive for 0<β<1, and its values at −1 and 0 have opposite signs. β=0 and q≥0 in their respective domains give strict stability. For β=1/2 and q=−4/5, trace −671/500 and determinant 1/4 give exactly the stated eigenvalues, one below −1; the two fixed-workload quadratics have complex roots of modulus 1/√2. From zero momentum and x_0=1, P(1,1)ᵀ=(−353/250,−4/5)ᵀ, not proportional to (1,1)ᵀ, so the unstable component is nonzero. Without momentum the multiplier is −64/125. The frozen verify.py was inspected, not executed; the exact witness and initial-state check here replace reliance on finite simulations.

## originality

PASS

The distinct claim is the sharp instability and its attainability under an integer local-step alternation in unnormalized FedAvgM with a single contractive local map, not the algorithm, its fixed-workload reduction, or the general use of monodromy and the quadratic disk test. No inspected equivalent yields that exact alternating-workload statement. This is a bounded best-of-knowledge finding.

## value

PASS

The threshold shows that alternating the smallest unequal positive local workloads can defeat stability for every positive momentum, even with identical clients and stable fixed workloads. The overshoot requirement, exact rational witness reachable from zero momentum, and stable no-momentum control separate this mechanism from heterogeneity and from instability of a local gradient step. The value is the sharp model-specific failure regime, not a general advance in matrix-product stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
