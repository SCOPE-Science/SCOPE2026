# Same-model review

## Correctness
PASS. Product-simplex functionals have additive scores \(p_i+q_j\). Once the largest entry is fixed, the second largest must lie in the same row or the same column; conversely every ordered pair of that form is realizable by separating row or column score gaps. The primary source's vertex criterion then gives exactly the two occupation-vector families in the theorem. Both families have squared norm \(1+\alpha^2+\beta^2\) and the same two block sums, so every vertex lies at squared distance
\[
1+\alpha^2+\beta^2-\frac1d-\frac1e
\]
from the row-column uniform point. A cyclic family of \(de\) genuine lineup vertices averages to that point, and the mean squared-distance identity proves minimum-enclosing optimality and uniqueness.

## Originality
PASS. The exact 2023 source was inspected at the lineup definition, occupation vectors, vertex criterion, and product-of-two-simplices additive-tableau section. It does not state a circumradius, minimum-enclosing sphere, or all-vertex cosphericity theorem. The earlier general lineup-polytope work was checked as broader coverage. Published-result and literature searches covered direct lineup terminology, occupation vectors, circumsphere/cosphericity, minimum-enclosing sphere, and Chebyshev-center formulations without locating a covering statement. Current and prior own ledgers contain no lineup-polytope finding.

## Value
PASS. Lineup polytopes were introduced for representability questions and products of simplices are the quantum-information setting singled out by the recent geometry paper. The theorem extracts a natural exact Euclidean invariant of every two-lineup product-of-two-simplices polytope, shows that all \(de(d+e-2)\) vertices are contacts, and provides a sparse \(de\)-vertex positive certificate. The result is uniform in both simplex dimensions and in the admissible weights.

## Closest literature and limitations
The primary literature develops normal fans, facets, realizable tableaux, and quantum marginal applications, not Euclidean enclosing spheres. The theorem is specific to lineup length two and the standard orthogonal product-simplex realization; longer lineups need not be cospherical by the same argument. A residual risk remains for an equivalent weighted-rook-configuration observation under different terminology.

Same-model review: passed. Independent audit: not yet performed.
