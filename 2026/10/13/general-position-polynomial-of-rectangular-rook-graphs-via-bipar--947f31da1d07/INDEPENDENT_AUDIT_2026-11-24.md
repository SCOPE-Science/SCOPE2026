# Independent mathematical audit

## correctness

PASS

The rook graph is the line graph of K_{m,n}. Its distance-two geodesic triples correspond exactly to three selected edges forming a simple three-edge path in that bipartite board graph. A component with an edge joining two degree-at-least-two vertices contains such a path, and absent such an edge each nontrivial component is a star. The edge-set bijection retains isolated row and column labels. The bicolored component series counts the two isolated types, a single-edge component once, and the two center orientations for at least two leaves, giving u exp(zv)+v exp(zu)−zuv; the labeled set formula gives its exponential. An empty side gives polynomial 1, and a side of size 1 gives a complete graph and polynomial (1+z) raised to the size of the other side, both consistent with the series. For m,n≥2 the edge maximum comes from exactly two spanning components. If m,n≥3 neither can be isolated (the other would contain at least two vertices in each part) and the two centers must be on opposite sides, giving mn forests. For 2×n with n>2 a degree-two column forces all other columns isolated, giving just two edges, so at the maximum there is exactly one edge in each column, with independent row choices. The 2×2 maximum consists of all six pairs. An independently written exhaustive metric check matched exact EGF extraction for 2×2, 2×3, 3×3, 3×4 and 4×4 (70,224 subsets), including both displayed examples and top coefficients 6,8,9,12,16. This finite replay supports, but does not replace, the proof. The frozen checker was inspected, not executed.

## originality

PASS

The scalar degree and diameter-two cluster criterion are known and not credited. The distinct supported contribution is the full labeled two-parameter weight enumeration with its explicit top-count cases. Earlier inspected primary results on general-position polynomials, extremal size and complete bipartite forests do not supply this weighted subclass enumeration. Several distinct indexed records demonstrably contain the very same formula or enumerand, and the overlap is real; the available records bearing those statements are later than the assigned record and do not establish a distinct earlier source for its finding. This is a bounded comparison, not an absolute first-priority claim.

## value

PASS

The general-position polynomial is a previously motivated enumerative invariant; complete-graph products are a natural family where the extremal number was already known. The formula determines every coefficient for both labeled board parameters, and distinguishes how many maximum vertex sets realize the common extremal size, including the exceptional two-row and square cases. It is reusable both for GP profiles and edge-weighted complete-bipartite star forests, rather than a table reprint or a tiny isolated coefficient. Neither the known degree nor the finite replay is credited as the substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
