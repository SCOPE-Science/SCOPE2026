# Same-model mathematical review: central regular-icosahedron sections

## Correctness — PASS

The unit-normal sphere is partitioned by six antipodal vertex-axis great circles. For all 64 six-sign patterns, the exact arithmetic verifier tests all 30 oriented great-circle intersections. Exactly 32 chambers survive: 20 triangles with 12 sign-changing icosahedron edges and 12 pentagons with 10 sign-changing edges. No triple intersections occur, so the list exhausts generic orientations. By uniform spherical separation an icosahedron edge crosses the central plane with probability \(\theta/\pi\), where \(\theta=\arccos(1/\sqrt5)\), hence the mean is \(30\theta/\pi\). The two-point support yields \(\mathbb P(N=12)=15\theta/\pi-5\). Girard's spherical polygon formula supplies an independent area derivation. No finite simulation is used as proof of the continuum assertion.

## Originality — PASS, with residual risk

The most relevant primary full texts inspected are De Loera–Lopez-Campos–Torres (arXiv:2412.12419, possible polytope section counts and icosahedral gaps), Jeon (arXiv:2603.00017, a distinguished equatorial decagon), and Kabluchko–Seidel (arXiv:2006.09492, expected face numbers of other regular polytope families). None contains the complete Haar 10/12 section-type law in the sections examined. Frederick's 2023 note **does** already describe the six-great-circle 20-triangle/12-pentagon tessellation, and MathPages has already given the numerical area fractions of its triangular and pentagonal chambers. Both those facts are prior art, not new. The claim's differentiating content is the exhaustive exact incidence of chamber types with 10- and 12-vertex central sections, giving the stated law; the probabilities follow easily from earlier area fractions **once that incidence is known**. Equivalent stereological formulations could be unindexed and cannot be excluded by search alone.

## Value — PASS

The 2024 polytope-section problem identifies the regular icosahedron as a structurally distinctive test case. This result is an exact, nontrivial rotation-invariant section invariant: an almost-sure complete type classification with exact nondegenerate probabilities and expectation. Its correspondence between a spherical geodesic tessellation and the section edge-crossing statistic gives a reusable finite-dimensional benchmark. It is not asserted to cover noncentral cuts or arbitrary icosahedra.

## Reproducibility and limits

The included `verify_icosahedron.py` requires only Python's standard library and uses exact arithmetic in \(\mathbb Z[\sqrt5]\) for all chamber, edge and angle signs. It checks all candidate sign patterns and all pair-circle intersections. The continuous Haar calculation and Girard identity are proved separately. Full source comparisons reduce, but do not eliminate, historical overlap risk.

Same-model review: passed. Independent audit: not yet performed.
