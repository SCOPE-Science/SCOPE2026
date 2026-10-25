# Independent mathematical audit

## correctness

PASS

Condition on multinomial side-counts K. For each occupied side with k samples, expected omitted endpoint fractions are 1/(k+1). Complement to hull decomposes into disjoint vertex gaps if all three occupied; in two-side occupancy, direct shoelace yields 1-1/(k_i+1)-1/(k_j+1). This leads to one exact occupancy identity with indicators K_k>0. Using 1/(k+1)=int_0^1 t^k dt and multinomial PGF derives 1-B_m/[m(m-1)pqr], m=N+2. Triple forward-difference of t^m gives 1-N int_[0,1]^3(pu+qv+rw)^(N-1), no approximation. Strict convexity for N>=3 and averaging unequal weights proves this moment integral strictly Schur-convex; hence area strictly Schur-concave. Triangle normalized side vectors are majorized by (1/2,1/2,0), and in turn majorize (1/3,1/3,1/3), proving extrema and rigidity. Independent exact rational multinomial occupancy vs cubic moment integral checks matched in 42 cases at N=1..14 across three p,q,r triples; finite checks corroborate exact all-N proof.

## originality

PASS

Best-of-knowledge: targeted published finding search and primary-source theorem comparison did not identify a prior result implying the entire final claim; known components are explicitly credited, not counted as novel. Exact all-N area expectation for perimeter-uniform boundary sampling in any triangle, with strict Schur shape ordering and sharp equilateral/degenerate endpoints. Unindexed-equivalent risk retained.

## value

PASS

Fixed-N perimeter-boundary random inscribed hulls of nonregular triangles are a natural finite-sample problem. Exact normalized area and complete triangle-shape optimization, including an unattained sharp degeneracy, add a nontrivial, interpretable finite-sample geometric extremal law beyond known asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
