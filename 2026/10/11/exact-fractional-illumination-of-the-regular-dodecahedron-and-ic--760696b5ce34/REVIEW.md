# Review

## Correctness
**PASS.** The fractional lower bound is an exact double count over vertex constraints, and the matching upper bound is a finite symmetry average, giving \(i^*(P)=f_0(P)/\alpha(P)\) for every vertex-transitive polytope. Polar duality converts \(\alpha(P)\) into the largest number of dual facets contained in an open central halfspace. Exact antipodal-transversal enumeration gives \(\alpha(D)=5\) and \(\alpha(I)=3\). For the ordinary dodecahedral value, four directions would force four disjoint maximal five-sets; exhaustive enumeration rules this out, while five explicit dual halfspaces cover all twenty facets. The standalone checker performs these finite steps over \(\mathbb Q(\sqrt5)\), not by numerical sampling.

## Originality
**PASS, with a close-prior-geometry residual risk.** Naszódi's defining paper introduces fractional illumination and proves general bounds but does not evaluate either dual Platonic solid. Kiss--de Wet's full paper materially analyzes the same dodecahedral and icosahedral incidence geometry for a different norm-weighted illumination parameter; it contains no occurrence of fractional illumination. Its icosahedral discussion already implies the ordinary value \(4\), which is explicitly excluded from the novelty claim. Its dodecahedral proof supplies nearby structural facts but does not state the ordinary value \(5\), the fractional values \(4\), or the gap \(5/4\). Candidate-specific searches found no implication-equivalent statement.

## Value
**PASS.** The dodecahedron and icosahedron are the canonical centrally symmetric Platonic solids beyond the cube and octahedron. Exact fractional values on this pair provide basic three-dimensional benchmarks for the invariant introduced by Naszódi. The dodecahedron additionally exhibits a clean nonintegral relaxation gap \(5/4\), and the symmetry formula isolates the general reason fractional illumination becomes exactly computable on vertex-transitive polytopes once the one-direction incidence maximum is known.

Same-model review: passed. Independent audit: not yet performed.
