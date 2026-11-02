# Independent mathematical audit

## correctness

PASS

PASS: The folded cube is a quotient Cayley graph F2^(n+1)/<all-ones> with generating set the n+1 coordinate cosets; translations and all generator permutations prove edge transitivity, including formerly distinguished antipodal edges. Even Walsh character subsets index Laplacian eigenvalues 2|S|, so an edge source-sink solution is expressible as finite character sum. Reciprocal integral yields U_j=∫_(1/2)^1[z^(n−j)(1−z)^j−z^j(1−z)^(n−j)]dz, strictly decreasing in j and antisymmetric U_(n−j)=−U_j. Thus all cube-edge drops sum exactly n/2, antipodal drops sum B_(2k−1)=B_(2k)=1−4^(−k)binom(2k,k) by binomial-majority integration by parts. These are full cut-column absolute sums. Effective resistance diagonal is (2^n−1)/[(n+1)2^(n−1)]=2(1−2^(−n))/(n+1) by rank(Q)=2^n−1 and edge transitivity; |I−Q| column sum equals |Q| column sum +1−2q. Independently built full graph incidence/Laplacian and pseudoinverse for n=3,4,5,6, checking all edge columns and both closed forms, plus read exact rational package checker. The proof establishes every integer n≥5; tests are finite corroboration.

## originality

PASS

PASS: A graph automorphism description helps prove folded-edge transitivity but cannot itself specify Euclidean current-column norms. No equivalent known formula found in inspected articles. Abstract formula Q=D^T L^+ D alone does not automatically dominate the closed central-binomial folded formula; it merely gives a starting calculation. Not a known-table recomputation; the proof derives a symbolic n-formula from an all-n Laplacian spectral sum. The statement is a new concrete specialization to a different natural Cayley graph, not a corollary of the exact ordinary-cube projection formula.

## value

PASS

PASS: This solves the exact natural endpoint projection norms of a canonical graph family obtained by adding the antipodal matching, not a recomputation for the original cube. Edge-transitivity and a binomial-majority law produce a new central-binomial correction with odd/even pairing and precise excess over ordinary-cube norm, useful for graph cycle-space and transportation-cost projection estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
