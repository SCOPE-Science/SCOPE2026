# Klein-bottle links in the eleven-point Paley tournament flag complex

## Finding

Let \(R=\{1,3,4,5,9\}\subset\mathbb F_{11}^\times\), and orient \(u\to v\) if \(v-u\in R\). Let \(K\) be the simplicial complex whose faces are the transitive subtournaments of this tournament. Then \(K\) is a normal three-dimensional pseudomanifold. Its nonmanifold locus consists of its eleven vertices, with a Klein-bottle link at each vertex.

## Proof

A subtournament is transitive exactly when it admits successive deletion of a source (a vertex with an arc to every other remaining vertex) down to the empty set. In one direction, delete the first vertex of the transitive order. In the other direction, the deletion order gives a transitive order. The accompanying finite checker applies this test to every subset of sizes one to five. It finds face numbers \((11,55,110,55)\), with no transitive five-vertex set and thus no larger face. Every triangle belongs to exactly two tetrahedra, and the tetrahedron adjacency graph, joining tetrahedra sharing a triangle, is connected. There are no maximal edges or isolated vertices: each edge lies in a triangle, and the one-skeleton is complete. Hence \(K\) is a pure connected pseudomanifold.

Write \(a=10\) for a vertex label. The complete list of link triangles at zero, obtained by removing zero from the tetrahedra containing it, is

```
134 139 145 157 178 189 235 23a 257 267
268 28a 34a 359 459 469 46a 67a 689 78a
```

The checker verifies that this list spans the whole link, has ten vertices and thirty edges, and has connected triangle adjacency. Every link edge lies in two triangles, and the link of every vertex of this surface complex is a single six-cycle. Thus it is a connected closed triangulated surface, with Euler characteristic \(10-30+20=0\).

To test orientability, start with each triangle in numeric vertex order. If the common edge of two adjacent triangles omits positions \(i,j\) in their respective orders (positions start at zero), their relative orientation signs must multiply to \((-1)^{i+j+1}\). On the closed dual walk

```
268 — 267 — 257 — 157 — 178 — 189 — 689 — 268
```

the required products are \(-1,-1,-1,+1,+1,-1,-1\), which multiply to \(-1\). Coherent triangle orientations would make the product \(+1\). The surface is therefore nonorientable and, by the classification of closed surfaces, is the Klein bottle. Translation carries this link to every other vertex link in \(K\).

Every edge link is the link of a vertex inside one of these triangulated surfaces and hence is a circle. Together with the triangle incidence, this shows that the links of all faces of codimension at least two are connected, as required for normality. Points in the relative interior of an edge, triangle, or tetrahedron have manifold neighborhoods (their transverse links are respectively a circle, a pair of points, or empty). A Klein-bottle link has \(\widetilde H_1(-;\mathbb Q)\cong\mathbb Q\), giving nonzero local homology at the linked vertex in degree two. Thus none of the eleven vertices is a manifold point.

## Reproducibility

Run `python3 paley11_checker.py`. It uses only the Python standard library and exhausts this finite complex, including exact incidence and the named orientation obstruction. It prints `PALEY11_KLEIN_BOTTLE_LINKS_OK` if all checks succeed.

## Relationship to prior work and scope

The complex here is the directed flag complex, not an out-neighborhood, directed Hom, or graph Rips complex. Counts of its transitive triangles and tetrahedra follow from McCarthy–Springfield [2]. Govc [1] already determined its nonequivariant homotopy type, and the affine second-homology character and rational quotient Betti numbers are explicitly stated in [3], which goes further by computing integral quotient homology. Those global invariants are not asserted as contributions here. The assertion is the local surface type and precise singular set of this natural complex. No priority over previously catalogued abstract Klein-bottle triangulations is claimed; nor is there a claim for other tournament sizes.

1. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, Proposition 3.4, [arXiv:2006.05333](https://arxiv.org/abs/2006.05333).
2. D. McCarthy and M. Springfield, *Transitive subtournaments of k-th power Paley digraphs and improved lower bounds for Ramsey numbers*, Corollaries 2.3 and 2.7, [arXiv:2311.02135](https://arxiv.org/abs/2311.02135).
3. *A Moore-space affine quotient of the Paley-11 directed flag complex*, “The two subgroup quotients” and “Independent structural checks,” [Resultary record bae7258c42e0](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-moore-space-affine-quotient-of-the-paley-11-directed-flag-comp--bae7258c42e0/RESULT.md).
