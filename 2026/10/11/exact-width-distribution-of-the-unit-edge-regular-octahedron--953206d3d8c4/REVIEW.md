# Review

## Correctness
**PASS.** The width reduces exactly to
\[
W=\sqrt2\max_i|U_i|.
\]
For threshold \(m\ge1/\sqrt2\), the six excluded coordinate caps have disjoint interiors, giving the linear branch. For \(1/\sqrt3\le m\le1/\sqrt2\), triple overlaps have zero area and exactly twelve congruent pairwise overlaps remain. The pair overlap is a spherical lens whose area follows from two cap sectors minus two spherical triangles; the spherical cosine rule gives its two required angles. Endpoint identities and branch matching are exact. The packaged verifier independently checks normalization, endpoints, direct spherical-area quadrature, and the lens integral.

## Originality
**PASS, with an explicit implicit-characterization risk.** The closest older source gives every integer moment of the regular-crosspolytope projection length through a Gaussian-maximum formula, but does not print or derive a finite \(n=3\) CDF. Because compact support makes the moment sequence determining, that source characterizes the law implicitly; the new contribution is the nontrivial closed evaluation of that law. Finch's full paper treats only the tetrahedron and cube. A recent full-length general polytope-density paper proves a universal co-area formula and explicitly evaluates the tetrahedron, truncated octahedron, and rhombic dodecahedron; full-text search finds no crosspolytope occurrence. Exact-object, caliper/Feret, maximum-coordinate, and formula searches found no prior closed octahedral width law.

## Value
**PASS.** The regular octahedron is a canonical Platonic solid and the three-dimensional regular crosspolytope. Its full width law is a natural object in the exact random-projection program represented by the cited literature, and it contains substantially more information than a mean or second moment. The formula isolates the geometric transition where pairwise spherical-cap overlaps disappear, giving a reusable benchmark for both polyhedral width-density methods and probabilistic maximum-coordinate calculations.

Same-model review: passed. Independent audit: not yet performed.
