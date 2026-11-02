# Scientific assessment

## Correctness — PASS

The graph has precisely \(N=d2^d\) vertices and degree \(2(d-1)\). The cut identity and discrete convexity give an exact upper bound. The parity-defined initial half-set has no selected lateral edge; balanced occupancy in each word clique is maintained under deleting a vertex from the most populated clique. This supplies equality for every sector, not merely observed small dimensions. The piecewise-affine sector energies yield all positive field thresholds and all coexisting magnetizations. Exact C++ enumeration at \(d=3\) was performed twice, independently; a separate graph/witness checker verifies \(d=3\) through \(d=8\), including the polyhedral realization. The counts reported for \(d=3\) match both exhaustive recurrences.

## Originality — PASS (examined evidence; historical priority provisional)

The 2005 Schmidt–Richter–Schnack and 2007 Rousochatzakis–Läuchli–Mila articles were materially inspected in their accessible arXiv article text, including model definitions, explored clusters, field discussions, and the 2007 Ising-point appendix. They treat the cuboctahedron or icosidodecahedron, rather than the 24-site rhombicuboctahedron or the described dimension-scalable graph family. Retrieved public summaries about rhombicuboctahedral independence and Rips complexes concern topology rather than its Ising all-sector cut function. Different Ising models on triangle-expanded cubic graphs, biregular-bipartite line graphs and circular prisms have different adjacency structures and their formulas do not directly give the new result. The convex occupancy method is standard and not claimed. An unknown more general graph theorem may still subsume the claimed special family.

## Mathematical value — PASS

The family grows exponentially in dimension and contains a canonical frustrated Archimedean polyhedron at dimension three. A single sharp clique-occupancy certificate yields all sector minima and every field transition, replacing exponential magnetic-state enumeration. Odd and even dimensions have different low-field magnetization structure; in the 24-site physical benchmark both transition fields and all critical coexistence multiplicities are exact. The result is a motivated soluble frustrated-spin benchmark and a structural theorem, rather than a table-only computation.

## Limits and closest literature

The result is classical, uniform-coupling, finite-graph and zero-temperature; higher-dimensional degeneracies are not enumerated. The two primary papers discuss different polyhedra and mostly quantum Heisenberg effects, so the comparison does not guarantee exhaustive priority. The primary-text scientific comparisons are recorded in `AUDIT.json`; reproducible computations are in `verify.py` and `census_independent.cpp`.

Self-review: passed. Independent audit: not yet performed.
