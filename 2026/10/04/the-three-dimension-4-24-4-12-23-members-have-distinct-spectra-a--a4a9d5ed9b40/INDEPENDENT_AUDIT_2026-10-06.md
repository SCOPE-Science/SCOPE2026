# Independent mathematical audit

## correctness

PASS

The field model \(\mathbb F_{23}[u]/(u^2-5)\) is valid because 5 is nonsquare modulo 23. Independently of the package verifier, this audit checked that \(\beta=4+7u\) has order 24, reconstructed all eleven quadratic minimal polynomials, and multiplied the appropriate factors to recover all three displayed degree-20 generators. A fresh exhaustive enumeration of all \(23^4=279841\) messages for each generator reproduced every coefficient of all three weight enumerators. Independently projectivizing the 24 generator-matrix columns gave 8 points of multiplicity 3 with maximum line count 6, 12 points of multiplicity 2 with maximum line count 4, and 24 distinct points with maximum line count 2. The standard projective-system formula for generalized weights then gives exactly the three stated hierarchies. Distinct weight enumerators already force monomial inequivalence.

## originality

PASS

The defining 2026 source's accessible article page and Table 1 identify exactly these three choices as \([24,4,12]_{23}\) codes but do not expose weight enumerators or generalized Hamming weights. Full article text could not be obtained through the available open route, and the authorized institutional retrieval returned an operational error; that is retained as a material residual risk rather than treated as failure. The broad Yang--Xiong--Ding arbitrary-zero weight-distribution theorem was read in full and uses a different equal-degree/arithmetic-progression zero setup; it does not directly specialize to the present mixed linear/quadratic parity-check factors. Exact coefficient and support-hierarchy searches found no independent prior statement.

## value

PASS

Weight distributions and generalized Hamming weights are standard, intrinsic coding-theoretic invariants. Here they separate three natural codes that the defining source leaves indistinguishable at the basic \([n,k,d]\) level, and the support hierarchies quantify subcode support geometry relevant to higher-order erasure and wiretap behavior. This is a motivated exact finite classification rather than an arbitrary statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
