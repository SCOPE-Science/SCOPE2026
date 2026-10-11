# Same-model review

## Correctness

PASS. The source's 24 regular-octahedral facets each have volume \(\sqrt2/3\) and normals \((\pm e_i\pm e_j)/\sqrt2\). Cauchy's polytope projection formula yields the claimed exact brightness sum. The maximum is a sharp Cauchy--Schwarz estimate on \((3,2,1,0)\). The minimum uses a cone-generator decomposition: the linear functional divided by generator norm is strictly greater than \(3\) on the two middle generators, and equality in the remaining triangle inequality requires a single extremal generator. Counts of the signed permutations are \(192\) at the top and \(24\) at the bottom. The accompanying exact-rational checker independently verifies the facet normalization and discrete equality data; the infinite-direction classification rests on the analytic proof, not on a finite sample.

## Originality

PASS. An's recent 24-cell spherical-design paper analyzes duality and facet incidence, not directional shadow-volume extrema. Novaga--Song's recent isoperimetric work provides the full 24-cell facet geometry and root-normal moments but studies surface area and affine stability, not the full 3D hyperplane projection-volume profile. Comparisons with root-zonotope support functions, projection-body radii, other maximal-projection theorems, and published records revealed no covering statement. The ordinary Cauchy formula and root-facet structure are explicitly credited as prior ingredients; the sharp classification is the contribution.

Residual risk: an equivalent result may already be encoded in older \(D_4\) root-zonotope or Coxeter-orbit literature without explicit projection-volume terminology.

## Value

PASS. Projection brightness is a natural complete directional observable for convex bodies. The regular 24-cell is the newly established unique four-dimensional translative-tile isoperimetric minimizer, so its exact brightness anisotropy is a motivated geometric benchmark. The exact two endpoint configurations expose a nontrivial geometric coincidence: all 24 original vertices, and no other directions, minimize 3D shadow volume; there are exactly 192 maximizing directions. This is a complete sharp invariant rather than an arbitrary isolated computation.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The principal geometric sources are An, arXiv:2609.02439v1, Section 9.2, and Novaga--Song, arXiv:2610.01653v1, Lemma 2.3 and Lemma 8.1; the projection formula is classical. Other recent maximum-projection work treats cross-polytopes rather than exact 24-cell brightness. The result neither solves isoperimetry for new classes nor gives stability estimates or affine-generalized shadow extrema.
