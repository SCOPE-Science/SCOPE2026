# Independent mathematical audit

## correctness

PASS

The truncating hyperplane deletes the one corner without creating vertices; the retained coordinate facets and new product facet exhaust the facets. Outside the new facet the proper fixed-coordinate subsets are saturated, while the ten vertex cones have six rays in rank five. Inside the product facet the full facet, its facets and its square faces have independent saturated normals; the triangular faces have four rays, any three a basis of their rank-three saturation, with primitive 2-versus-2 relation. In such a basis the dual semigroup consists of (a,b,c) with a,b,c nonnegative and c at most a+b; its four generators give the determinant of a 2-by-2 matrix. Every edge or vertex of the product lies in one of the triangles; its normal cone contains a nonsimplicial face, so it too is nonsimplicial. Orbit closures are unions over subfaces, so the six unimodular triangles give standard projective planes with nine distinct cross-family incidences. The ten remaining charts are the equal-total row/column margin semigroup: every nonnegative integral margin pair is a sum of unit row-unit column pairs. This is the rank-one 3-by-3 cone, smooth off its vertex and of Segre degree six. The tensor product with the orbit torus at each triangle leaves transverse multiplicity two. Thus exactly the nonsimplicial cones are singular and the orbit profile is (19,18,6). Independent replay: python3 /workspace/branches/check_1.py enumerates the coordinate patterns with and without the cut active and independently verifies ranks, saturation, maximal singular faces and intersection counts.

## originality

PASS

Credit the previously published identical matroid and face vector, and the general Resultary calculation of its maximal-cone rays, fixed-point singularity and class groups. The supported distinct contribution is the full reduced singular stratification with component incidence and transverse rings and multiplicities; it is not a claim that the fixed points or the face vector are new.

## value

PASS

This is a natural test of how removing one basis changes the projective toric singularities of a uniform matroid. The decomposition tells a reader exactly which directions acquire nonisolated singularities, how those components meet, where the isolated Segre model persists, and whether non-factoriality is a reliable detector in this case. Such explicit strata can be used as a benchmark for other splits and are not just the known face vector or an undifferentiated list of singular fixed points. The finding is a focused example, not a general classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
