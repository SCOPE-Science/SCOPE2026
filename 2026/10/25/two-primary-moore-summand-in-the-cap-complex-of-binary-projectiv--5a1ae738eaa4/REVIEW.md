# Scientific review: binary projective cap complex

## Correctness — PASS

All 35 projective lines follow by XOR on the 15 nonzero four-bit vectors. Exact enumeration of all 32,767 candidate nonempty subsets gives 3,048 faces. The deterministic 1,484-pair matching leaves one critical vertex, one three-cell and 78 four-cells. The complete 13,770-incidence directed graph is acyclic by an exhaustive topological ordering; this is a proof of the matching condition rather than a partial search. The signed gradient-path recurrence gives 15 coefficients \(-2\), 44 zeros, and 19 coefficients \(+2\), so the attaching-degree ideal is exactly \(2\mathbb Z\). The reduced CW model is a Moore space and 77 four-spheres. Direct mod-two and mod-three simplicial boundary ranks provide separate checks, with no reliance on an experimental extrapolation.

## Originality — PASS (with residual risk)

The closest primary source on the *same underlying cap objects* is Grynkiewicz–Lev, arXiv:0811.1322, whose theorems concern large complete caps and minimal saturating sets. Its material inspected includes the introduction, definitions, main results, examples and full-document checks for topology/homology; these do not supply an attaching-degree or homotopy classification. Superdock, arXiv:2110.12314, builds different projective-plane complexes with prescribed facets and free abelian fundamental groups, not the cap-subset complex of \(\operatorname{PG}(3,2)\). Other indexed finite-geometric cap classifications concern different incidence systems. No retrieved prior statement implies the degree-two Moore summand or the 77 four-spheres. Failure to find a match is not a proof of global priority; an unindexed equivalent remains possible.

## Value — PASS

The 15-point, 35-line projective three-space is a canonical finite-geometric test object. Its cap complex is nonpure, with 168 five-point and 15 eight-point maximal caps, so straightforward manifold or matroid-shellability arguments do not describe it. The detected \(\mathbb Z/2\)-torsion is invisible to rational Betti numbers and forces a non-sphere-wedge homotopy type. The complete degree-two Moore attachment gives a natural integral topological invariant relevant to comparisons of cap complexes across different finite geometries. The claim is a substantive complete classification for a canonical object, not a numeric slice chosen after computation.

## Sources and limitations

Primary cap literature: Grynkiewicz–Lev, arXiv:0811.1322, especially introduction and geometric/additive definitions and classification theorems. Different topological construction: Superdock, arXiv:2110.12314, introduction, finite projective-plane definitions and Corollary 6.6. Topological reduction: Forman, Advances in Mathematics 134 (1998), 90–145. Residual risk: unindexed or unavailable equivalent homotopy calculation; independently checking the finite certificate remains advisable.

Self-review: passed. Independent audit: not yet performed.
