# Seven combinatorial types of all central sections of the regular 24-cell

## Finding
Let \(P\subset\mathbb R^4\) be the regular root-system \(24\)-cell
\[
P=\operatorname{conv}\{\varepsilon e_i+\delta e_j:1\le i<j\le4,\ \varepsilon,\delta\in\{-1,1\}\}.
\]
For every nonzero normal \(u\), the central section \(Q(u)=P\cap u^\perp\) is a three-dimensional convex polytope. **Exactly seven combinatorial types occur**, distinguished by their face vectors and polygon-size multisets. Define simple roots
\[
\alpha_1=e_1-e_2,\quad \alpha_2=e_2-e_3,\quad
\alpha_3=e_3-e_4,\quad \alpha_4=e_3+e_4.
\]
Acting by a symmetry of \(P\), arrange \(u\cdot\alpha_i\ge0\) for all four indices. Define \(b=\mathbf 1_{u\cdot\alpha_2>0}\), and \(k=\#\{i\in\{1,3,4\}:u\cdot\alpha_i>0\}\). The seven possible pairs and their section face data are:

| \(b\) | \(k\) | Vertices | Edges | Faces | Triangles | Quadrilaterals | Pentagons | Hexagons |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 12 | 24 | 14 | 8 | 6 | 0 | 0 |
| 0 | 2 | 18 | 30 | 14 | 0 | 12 | 0 | 2 |
| 0 | 3 | 26 | 42 | 18 | 0 | 12 | 0 | 6 |
| 1 | 0 | 14 | 24 | 12 | 0 | 12 | 0 | 0 |
| 1 | 1 | 20 | 32 | 14 | 0 | 6 | 8 | 0 |
| 1 | 2 | 26 | 40 | 16 | 0 | 4 | 8 | 4 |
| 1 | 3 | 32 | 48 | 18 | 0 | 6 | 0 | 12 |

Any two sections assigned the same pair \((b,k)\) are combinatorially isomorphic, and no two rows are combinatorially isomorphic. The generic row \((1,3)\) was known previously; the classification here also covers **all singular directions**, including those whose planes contain vertices or triangular faces of \(P\).

## Assumptions and scope
The normal \(u\) ranges over all nonzero vectors in \(\mathbb R^4\). The metric and coordinate scale do not affect combinatorial type. A polygon size means the number of edges in a two-dimensional face of the three-dimensional section, not the polygon shape in Euclidean space. \(u\) and \(-u\) represent the same plane. The seven rows distinguish face lattices, not congruence classes or affine-equivalence classes.

## Proof
**1. Symmetry reduction.** The \(24\) vertices are precisely the roots of the \(D_4\) system. Its reflection group consists of signed coordinate permutations with an even number of sign changes and moves every nonzero normal into the closed chamber \(u_1\ge u_2\ge u_3\ge|u_4|\). Its four bounding inequalities are \(u\cdot\alpha_i\ge0\). There are \(2^4-1=15\) nonzero patterns of vanishing and strict inequalities. The outer automorphisms of the \(D_4\) diagram permute \(\alpha_1,\alpha_3,\alpha_4\) and fix \(\alpha_2\). They preserve the entire root set, hence \(P\), and merge the \(15\) patterns into the seven \((b,k)\) classes listed. Within one pattern the signs of \(u\cdot v\) are unchanged for every vertex \(v\) of \(P\), because each positive root is a nonnegative combination of simple roots. Consequently the face-incidence structure of the section is unchanged along a path in that relatively open chamber face. This establishes at most seven types.

**2. Exact section-incidence rule.** The \(24\) octahedral facets of \(P\) have supporting equations \(\pm x_i=1\) (eight choices) and \(\sum_{i=1}^4\varepsilon_i x_i=2\) (sixteen choices). Each has exactly six original vertices. Two original roots are joined by an edge precisely when their dot product is \(1\). This lists \(96\) edges and \(96\) triangular two-faces. For any specified \(u\), an intersection of the section with an original edge is a section vertex exactly when its two endpoint evaluations have opposite signs; an original root on the plane is also a section vertex. Thus
\[
 f_0(Q)=\#\{v\in\operatorname{vert}(P):u\cdot v=0\}
 +\#\{\{v,w\}\in\operatorname{edge}(P):(u\cdot v)(u\cdot w)<0\}.
\]
Every section facet is either the polygon where an octahedral facet has both positive and negative vertex evaluations, or an original triangular two-face lying wholly in the section plane. The first kind of polygon has as many vertices as there are zero-evaluated original facet vertices plus strict sign-crossing original edges of that facet. The second kind has three sides. These are exhaustive since a two-dimensional exposed face of the section comes from an exposed face of \(P\) of dimension at least two; if the parent is three-dimensional it straddles the plane, and if the parent has dimension two it must be contained in the plane. The number of section edges follows from Euler's formula \(f_1=f_0+f_2-2\). Alternatively, the polygon-side sum is \(2f_1\).

**3. Exhaustive integer count.** For any binary tuple \((a,b,c,d)\ne(0,0,0,0)\), take the integer normal
\[
 u=(2a+2b+c+d,\ 2b+c+d,\ c+d,\ d-c).
\]
It has \(u\cdot(\alpha_1,\alpha_2,\alpha_3,\alpha_4)=2(a,b,c,d)\), so these \(15\) normals represent every closed-chamber stratum. Apply the incidence rule to the explicit \(24\) roots, \(96\) edges, \(96\) triangular faces and \(24\) octahedral facets. The seven rows above result; all \(15\) cases are enumerated exactly by the attached standard-library verification program. The code checks that each of the six outer-node permutations really maps the full root set to itself and checks every row and the Euler incidences. It is a finite **exhaustive** enumeration of chamber strata, not a statistical sample or a claim that enumeration alone covers infinitely many normals: the chamber-symmetry and constant-sign arguments supply the infinite reduction.

**4. Distinctness.** The seven face vectors are all different, hence the corresponding face lattices are pairwise nonisomorphic. This establishes exactly seven types.

## Verification
Run `python3 verify_24cell_sections.py` with Python 3 and its standard library. The program reconstructs the vertices, edges, facets, triangular ridges, six root-preserving triality automorphisms, and all fifteen chamber-stratum signatures using integer arithmetic only, then prints `VERIFY_OK`. It also verifies the sum of all polygon side counts equals twice the section-edge count. No numerical tolerances, randomness, or externally downloaded data are used. The proof's symmetry reduction is mathematical; the program independently checks the finite incidence data.

## Relationship to prior work
Greg Egan's *Slice* (created 2002-03-11) explicitly gives six quadrilaterals and twelve hexagons for a **generic** \(24\)-cell slice; this is the last row, and is not claimed new. Classical descriptions of the \(24\)-cell also identify distinguished cuboctahedral and rhombic-dodecahedral central sections. Koca, Koca and Al-Barwani (arXiv:1106.3433, 2011-06-17) describe the \(D_4\) Weyl group and its \(S_3\) diagram symmetry. Cellini and Marietti (arXiv:1207.3429, 2012-07-14) investigate the face geometry and associated arrangements of root polytopes. The new object here is the **complete seven-class stratification including all nongeneric central section directions**, not a claim to discover the \(24\)-cell, its Weyl symmetry, or its generic slice. The inspected primary sources do not present this all-strata face-vector/face-size table. Broader earlier classifications and unindexed sources remain a historical-priority risk.

## Limitations
This result treats **central** three-dimensional hyperplane sections through the origin only; translated affine hyperplanes are excluded. Face-vector data do not specify exact metric shapes, areas or volumes. The finite checker establishes the table only after the separately explained chamber reduction. The originality assessment is best-knowledge only and not independently validated.

## References
1. Greg Egan, *Slice*, created Monday, 11 March 2002, https://www.gregegan.net/APPLETS/27/27.html .
2. Mehmet Koca, Nazife Ozdes Koca, Muataz Al-Barwani, *Snub 24-Cell Derived from the Coxeter-Weyl Group W(D4)*, arXiv:1106.3433, submitted 2011-06-17, https://arxiv.org/abs/1106.3433 .
3. Paola Cellini, Mario Marietti, *Root polytopes and abelian ideals*, arXiv:1207.3429, submitted 2012-07-14, https://arxiv.org/abs/1207.3429 .
