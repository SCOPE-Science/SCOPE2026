# Independent mathematical audit

## correctness

PASS

The frozen formulas are mathematically correct. In the replacement the claim is narrowed to the labelled packing multiplicities. Diameter is two, so the maximal paths are exactly the clique edges and the three-vertex paths with two independent endpoints and a clique center; single vertices extend, and every cross edge extends because s≥2. A type (t,u) uses 2t independent vertices and t+2u clique vertices. Choosing t centers, assigning unordered pairs from the independent set to these distinct centers, and choosing a size-u matching on unused clique vertices gives exactly A_{r,s}(t,u) with no extra t! divisor. This counts each packing once and includes the empty one. At fixed t the greatest size is floor((r+t)/2), so the leading coefficient only receives contributions from t=h and, for odd r+h, t=h−1, with u fixed in each case. In the saturated case h=r the coefficient reduces to the stated factorial ratio. The formal exponential generating function counts singleton unused vertices and the two types of path blocks. The retained comparison facts are correct: a maximal safe complement is I or one independent vertex with one clique vertex, including at r=1 and at the coincident degrees when s=2; comparison with the packing maximum gives the stated gap. The replacement marks those facts, feasible types, and optimum size as known specializations.

## originality

PASS

The frozen novelty claim fails in material part: the packing number and existence-side maximum-type classification follow from 483fcd9cfba1, and the inclusion-minimal transversal census and minimum cases follow from e5c4e05a4d10. Combining those results gives the gap and equality boundary. A complete replacement at /workspace/repairs/4/RESULT.md credits those implications and claims only the surviving labelled packing polynomial and multiplicities, including the exact number of maximizers. Those counts are not supplied by the inspected capacity or transversal classifications, and the closest counting theorem excludes singleton parts and hence the maximal clique-edge blocks. The pass applies to the narrowed replacement, not the frozen originality claims.

## value

PASS

The retained result counts solutions of the natural geodesic packing problem by size and path type on the standard split family, rather than rederiving the known feasible sizes. Multiplicities measure how many optima are available: at fixed r throughout s≥2r the optimal size is constant while the number of maximizing packings varies with s. The exact coefficients also describe how the two possible types share the optimum in the odd-parity regime. This is a useful exact invariant in its own right; previously implied transversal and maximum-size results are not credited as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
