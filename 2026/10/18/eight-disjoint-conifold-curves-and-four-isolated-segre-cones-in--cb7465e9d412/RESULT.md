# Eight disjoint conifold curves and four isolated Segre cones in a matching-deleted permutohedral fourfold

## Finding
Let \(G=K_5\setminus\{\{1,2\},\{3,4\}\}\), where the fifth vertex is \(5\). This is the five-vertex wheel graph, with vertex \(5\) as hub and the remaining four vertices forming a cycle. Let \(Z_G=\sum_{\{i,j\}\in E(G)}[e_i,e_j]\subset\mathbb R^5\), lying in the affine hyperplane of coordinate sum \(8\) with difference lattice \(M=\{m\in\mathbb Z^5:\sum_i m_i=0\}\). Let \(X_G\) be the normal projective toric fourfold of its normal fan in the dual lattice \(N=\operatorname{Hom}(M,\mathbb Z)\cong\mathbb Z^5/\mathbb Z(1,1,1,1,1)\). For every algebraically closed field \(k\), the reduced singular locus is a disjoint union of eight projective lines and four isolated closed points:

\[
\operatorname{Sing}(X_G)_{\mathrm{red}}\cong
\left(\coprod_{i=1}^{8}\mathbb P^1_k\right)\amalg
\left(\coprod_{j=1}^{4}\operatorname{Spec}k\right).
\]

The transverse toric germ at the generic point of every singular line is the conifold \(uv-wz=0\), of Hilbert--Samuel multiplicity \(2\). At each isolated singular point the entire affine toric chart is isomorphic to the rank-one determinantal cone \(\{M\in\mathbb A^6:\operatorname{rank}M\le1\}\) for \(2\times3\) matrices, of Hilbert--Samuel multiplicity \(3\). There are exactly \(28\) singular torus orbits: \(8\) of dimension \(1\) and \(20\) fixed points. The full fan has \(78\) maximal cones, of which \(58\) are smooth. The singular support equals the non-\(\mathbb Q\)-factorial support.

## Assumptions and scope
The graph is the labeled five-vertex graph with exactly the two disjoint missing edges shown above, not an arbitrary two-edge deletion. The toric variety uses the **normal fan of the graphical zonotope**, not the normal fan of the graph-associahedron and not the face fan. A toric cone is smooth if its primitive rays extend to a basis of the saturated lattice in its linear span. Statements concern the reduced singular support; they do not specify nilpotent structure of a scheme-theoretic Jacobian singular subscheme.

## Proof
**1. Exact fan encoding.** The edge hyperplanes are \(x_i=x_j\), for \(\{i,j\}\in E(G)\), in \(N_\mathbb R\). For a potential \(a\in\mathbb R^5\), associate the signs \(\operatorname{sgn}(a_j-a_i)\) on the eight present edges, recording \(0\) on an equality edge. Every relatively open fan cone is determined by a realizable sign vector. Every such vector occurs among the \(5^5\) assignments \(a_i\in\{0,1,2,3,4\}\): replace the distinct potential levels, in increasing order, with consecutive integers. An independent enumeration by ordered set partitions gives the same set. There are exactly \(389\) sign vectors.

**2. Primitive rays and regularity.** For a sign vector \(s\), let \(E_0(s)\) be its zero edges and let \(c(s)\) be the number of components of \((V,E_0(s))\), isolated vertices included. Its cone has dimension \(c(s)-1\). For every nonempty proper \(S\subset V\), write \(\mathbf1_S\) for its class in \(N\). This is a generator of the cone exactly when it respects all prescribed inequalities and is constant on every zero edge. The extreme generators among these are precisely those for which both induced graphs \(G[S]\) and \(G[V\setminus S]\) are connected. Indeed, every order-preserving potential is a nonnegative sum of superlevel indicators modulo constants; at \(\mathbf1_S\), the active inequalities have precisely the edges internal to the two parts, so the smallest containing face is one-dimensional exactly when both induced graphs are connected. Each such generator is primitive. There are \(26\) allowed graph cuts. For any cone, its primitive rays are therefore obtained by testing these \(26\) cuts against its sign constraints.

To check lattice regularity, contract the zero-edge components and use their potential values modulo the last component as integral coordinates on the saturated span lattice. A simplicial cone is smooth exactly when the absolute determinant of its primitive-ray matrix is \(1\). These computations are finite exact integer operations.

**3. Exhaustive cone classification.** The resulting distribution, by cone dimension and number of primitive rays, is

| Cone dimension | 0 rays | 1 ray | 2 rays | 3 rays | 4 rays | 5 rays |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 26 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 116 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 160 | 8 | 0 |
| 4 | 0 | 0 | 0 | 0 | 58 | 20 |

Every simplicial cone in this table has primitive determinant \(1\). The \(28\) nonsmooth cones are exactly the \(8\) three-dimensional four-ray cones and the \(20\) four-dimensional five-ray cones. Among the latter, exactly \(16\) contain one of the eight nonsmooth three-cones as a face. The remaining four do not contain any nonsmooth proper face. Consequently the inclusion-minimal nonsmooth cones consist of exactly eight three-cones and four four-cones.

The eight three-cones each lie in exactly two maximal cones. No maximal cone contains two distinct ones; no isolated nonsmooth four-cone contains any of them. By toric orbit-cone closure and completeness, their orbit closures are eight pairwise disjoint complete normal toric curves, hence \(\mathbb P^1\), and the other four components are isolated fixed points. Each three-cone contributes its one-dimensional orbit; their sixteen maximal-cone endpoints are distinct. These give \(8+16+4=28\) singular torus orbits, including \(20\) singular fixed points.

**4. Integral local types.** For each of the eight minimal nonsmooth three-cones, its four primitive rays generate the saturated rank-three lattice and obey a primitive relation with coefficients \((1,1,-1,-1)\), up to reordering and overall sign; every three-column determinant has absolute value \(1\). Its affine transverse toric variety is \(\operatorname{Spec}k[u,v,w,z]/(uv-wz)\). The full-dimensional cones incident to a singular line have one additional free primitive ray, so their affine charts have this conifold times \(\mathbb A^1\) as model.

For each of the four isolated nonsmooth maximal cones, the five primitive rays generate \(N\), every four-column maximal minor has absolute value \(1\), and their primitive relation has two coefficients of one sign and three of the other, all of absolute value \(1\). The resulting toric quotient is \(\operatorname{Spec}k[z_{ij}:1\le i\le2,1\le j\le3]/I_2(z_{ij})\). Its projectivization is the Segre variety \(\mathbb P^1\times\mathbb P^2\subset\mathbb P^5\), of degree \(3\); its affine cone has multiplicity \(3\) at the origin. The analogous conifold multiplicity is \(2\). These semigroup identifications and multiplicities hold in all characteristics.

**5. Non-\(\mathbb Q\)-factorial support.** Every nonsmooth cone is nonsimplicial, and every simplicial cone is unimodular. The toric simplicial-cone criterion for \(\mathbb Q\)-factoriality therefore identifies the two supports.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. It enumerates realizable sign vectors both via scores and via ordered partitions, tests connected-cut primitive rays, computes integer determinants and primitive relations, identifies the minimal nonsmooth cones, verifies that every singular curve has two distinct maximal-cone endpoints, and tests all possible curve intersections. Its expected terminal marker is `VERIFY_OK`. The closed computation exhausts all potential-level order types for exactly five graph vertices; no numerical sampling or incomplete search is used.

## Relationship to prior work
Postnikov--Reiner--Williams give the graphical-zonotope, braid-fan, and Hasse-poset framework and the global simplicity criterion. Their Proposition 5.2 implies that this graph's zonotope is not simple, but does not give the exact singular components or affine local models obtained here. Padrol--Pilaud--Poullot give deformation-cone presentations for general graphical zonotopes; this is a different cone (the parameter space of Minkowski summands) from the individual normal cones whose local toric singularities are classified above. The graph is also the wheel \(W_5\); knowing its total and smooth torus-fixed-point counts (\(78\) and \(58\)) does not determine the full singular support or its distinct transverse analytic types. The two papers are not claimed to lack all related consequences, and the present theorem does not assert a new general toric smoothness criterion or claim the isolated smooth-point count as separately novel.

## Limitations
This is a complete classification for the specified five-vertex graph, not an all-parameter formula for complete graphs with arbitrary matchings removed. The calculation uses a fully disclosed, inspectable finite integer certificate together with standard toric orbit-cone and semigroup arguments; no independent mathematical audit has been performed. An unindexed equivalent worked example under graphic-arrangement or generalized-permutohedron terminology remains possible. No statement is made about a nonreduced singular subscheme or global resolution.

## References
1. A. Postnikov, V. Reiner, L. Williams, *Faces of Generalized Permutohedra*, arXiv:math/0609184 (first posted 2006-09-06), especially Sections 3 and 5, Proposition 5.2. https://arxiv.org/abs/math/0609184
2. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422 (2021), especially Sections 1 and 2. https://arxiv.org/abs/2111.12422
3. D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics 124, American Mathematical Society (2011), for toric smoothness, orbit closure, and affine semigroups.
