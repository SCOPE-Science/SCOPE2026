# Scientific review: exact random central sections of the truncated tetrahedron

## Correctness — PASS

The claim concerns Haar-uniform **unoriented central planes** of the explicitly specified twelve-vertex truncated tetrahedron. The analytic proof reconstructs the eighteen-edge graph from four triangular and four hexagonal facets, counts only edges with opposite endpoint signs, and uses the full tetrahedral symmetry group to restrict normals to a fundamental chamber of area \(\pi/12\). Four of the twelve vertex-zero hyperplanes cut that chamber into six rational polygons, each with a verified constant section side count. The standard exact spherical triangle formula gives the three probabilities. The independently derived mean \(18\arccos(7/11)/\pi\) agrees to numerical precision. `verify.py` was run from the present package: exact integer and rational assertions passed, spherical areas normalized, and a separately sampled finite test was consistent. The proof, not numerical sampling, covers the infinite continuum of orientations. Generic-position restrictions are measure zero.

## Originality — PASS, with priority uncertainty

The March 26, 2026 source by Brandenburg, De Loera, Luo, and Meroni gives general slice formulas and a detailed study of cube-like polyhedral norm balls. Birkemeyer, Brose, Brandenburg, and Prün (September 14, 2026) study combinatorial reconstruction from section data, including the vertex-count function of central sections. Brandenburg, De Loera, and Meroni (2023 preprint) establish the polyhedral slicing chamber framework. These results supply prior ingredients and general methods, but the inspected relevant full texts do **not** present evaluated four-/five-/six-sided uniform-orientation probabilities for the regular truncated tetrahedron. Published exact random central-section laws for regular icosahedra, cubes, and rectangular boxes involve different solids, and the accessible summaries do not imply this distribution. Own accessible mathematical claim records were compared, including a regular **truncated octahedron** result; the latter is not the truncated tetrahedron and has a different distribution. Database coverage cannot prove uniqueness, and a historical stereological calculation might duplicate the result.

## Mathematical value — PASS

A complete exact polygon-type law for a natural, asymmetric Archimedean polyhedron is a geometric invariant not determined by its face vector or its symmetry group alone. The computation resolves an explicitly motivated missing benchmark: nonzero probabilities for four, five, and six section sides, with pentagons accounting for over half of all orientations. The six rational spherical cells also provide a compact reproducible model of the general section-chamber decomposition. The independently evaluated mean supplies a structural consistency check. This is a natural finite classification; no broad conjecture or downstream theorem is claimed.

## Limits and risk

Only central sections of the fixed regular truncated tetrahedron are covered. The method does not calculate conditional areas, off-center sections, or analogous laws for other solids. Numerical checks do not prove exhaustiveness; the explicit rational-cell proof does. An older equivalent result could occur under different stereological terminology, so historical priority is provisional. No independent expert audit has been performed.

Self-review: passed. Independent audit: not yet performed.
