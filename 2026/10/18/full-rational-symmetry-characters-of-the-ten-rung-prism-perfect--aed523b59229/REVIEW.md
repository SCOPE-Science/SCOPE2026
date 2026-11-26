# Independent mathematical audit

## correctness

PASS

Recomputed the facets by choosing the set of rungs: a nonempty choice leaves paths, each with a unique matching if of even order, and the empty choice gives four rim matchings. This gives 125 facets and 60,852 faces including the empty face. Excluding the two staggered rim facets gives the 59,050-face K, exhaustively identical to the complex obtained by expanding each rim column into its two interchangeable rim edges. Projection from K to the 20-vertex column/rung complex is equivariant and a homotopy equivalence: the top-layer section and its composite with projection are contiguous to the identity on their respective complexes. Exact rational boundaries on the 6,726-face quotient give only reduced H4 of rank two. The two exceptional facet intersections with K are disjoint copies of the independence complex of C10, whose exact boundaries give only reduced H2 of rank one. The relative chain groups split by exceptional facet and the pair sequence gives H3(P) from relative H3 and H4(P) from K. Computed the H4 trace on the column/rung quotient and the relative H3 trace from the intersections (zero for exchanging facets), using signed fixed faces. All 40 pairs agree with the proposed character sums, hence yield the claimed rational modules. Replay: python3 /workspace/independent/recompute_complexes.py 4. The frozen proof's 'ten-simplices' have ten vertices and dimension nine; the relative argument uses their contractibility and is unaffected.

## originality

PASS

The nonequivariant Betti numbers are prior. The separately resolved degree-three and degree-four characters are not supplied by the strongest inspected prior results; the bounded comparisons did not establish equivalent prior coverage of this pair of modules.

## value

PASS

Ten rungs is the first two-degree case in the cited ladder classification. In this case a single Euler trace cannot separate H3 from H4, and dimensions are equal although the actions are distinct. The character calculation determines, for example, the absence of global invariants in H3 and one global invariant in H4, with layer swap and reflection distinguishing the degrees. This is a motivated finite benchmark for equivariant work on the natural ladder family, not a recomputation of the known Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
