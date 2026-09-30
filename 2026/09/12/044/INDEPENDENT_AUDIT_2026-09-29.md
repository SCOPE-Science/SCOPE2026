# Independent audit — 2026-09-29

Record: `2026/09/12/044`  
Audited tree: `28f0ea459fab80693abd5d8183a30e77c3148787`  
Disposition: **passed**

## Correctness

The named case reduces to a direct combinatorial decomposition. The standard multiwedge minimal-nonface rule sends the octahedron's three antipodal-pair nonfaces under J=(3,2,1,1,1,1) to two 2-vertex nonfaces and one 5-vertex nonface, up to relabeling. Hence K is the join of a square boundary with the boundary of a 4-simplex, so Z_K=(S^3×S^3)×S^9. The f-vector (9,34,70,85,60,20), 8-dimensional exterior cohomology and formality follow. Independently counting ordered triples of the seven positive-degree exterior-basis monomials with both adjacent products zero gives exactly 205, matching the record.

## Originality

The J-construction, Hochster description and moment-angle join/product rule are standard. The focused search did not surface this exact named simplification, but its proof is elementary once the disjoint minimal nonfaces are recognized.

## Scientific value

The product-of-spheres identification decisively resolves the named case and makes the Massey-vanishing conclusion transparent.

## Limitations

- The conclusion is rational formality; no integral classification is claimed.
- The diffeomorphism identification uses standard moment-angle facts rather than a new general theorem.
- homology_lib.py, wedge_correct.py, tor_true.py and massey_true.py referenced by the record are absent from the audited repository tree; the named case was verified directly.
- Literature non-detection is not proof of novelty or priority.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/12/044
- https://doi.org/10.1134/S008154381903009X
- https://arxiv.org/abs/1911.07083
- https://doc.sagemath.org/html/en/reference/topology/sage/topology/moment_angle_complex.html
