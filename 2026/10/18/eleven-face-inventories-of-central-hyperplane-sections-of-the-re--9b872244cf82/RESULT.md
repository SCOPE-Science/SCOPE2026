# Eleven face inventories of central hyperplane sections of the regular 600-cell

## Finding

Let \(\varphi=(1+\sqrt5)/2\), and let \(P\subset\mathbb R^4\) be the regular 600-cell of circumradius \(2\) whose vertex set consists of all \(120\) vectors
\[
\{(\pm2,0,0,0)\}_{\mathrm{perm}}
\;\cup\;\{(\pm1,\pm1,\pm1,\pm1)\}
\;\cup\;\{(0,\pm1,\pm\varphi,\pm\varphi^{-1})\}_{\mathrm{even\ perm}}.
\]
The signs in each family are independent. For every nonzero \(u\in\mathbb R^4\), the central section \(Q_u=P\cap u^\perp\) is a three-dimensional centrally symmetric polytope. Its face inventory, namely its counts of vertices, edges, triangular facets, and quadrilateral facets, is one of **exactly eleven** possibilities. All eleven occur. No section facet has more than four edges.

The following table gives all \(15\) nonempty relative-interior faces of a fundamental \(H_4\) Coxeter chamber, hence every possible inventory. Repeated rows correspond to distinct chamber strata having the same inventory. The four-digit mask is explained in the proof. Counts in the last two columns are the numbers of triangular and quadrilateral facets of the three-dimensional section.

| Mask | Vertices | Edges | Facets | Triangles | Quadrilaterals |
| --- | ---: | ---: | ---: | ---: | ---: |
| `0001` | 84 | 240 | 158 | 152 | 6 |
| `0010` | 104 | 282 | 180 | 156 | 24 |
| `0011` | 114 | 300 | 188 | 152 | 36 |
| `0100` | 92 | 250 | 160 | 140 | 20 |
| `0101` | 124 | 320 | 198 | 152 | 46 |
| `0110` | 124 | 322 | 200 | 156 | 44 |
| `0111` | 134 | 340 | 208 | 152 | 56 |
| `1000` | 42 | 120 | 80 | 80 | 0 |
| `1001` | 114 | 300 | 188 | 152 | 36 |
| `1010` | 124 | 322 | 200 | 156 | 44 |
| `1011` | 134 | 340 | 208 | 152 | 56 |
| `1100` | 102 | 270 | 170 | 140 | 30 |
| `1101` | 134 | 340 | 208 | 152 | 56 |
| `1110` | 134 | 342 | 210 | 156 | 54 |
| `1111` | 144 | 360 | 218 | 152 | 66 |

Consequently the **sharp minimum and maximum section-vertex counts** are \(42\) and \(144\), respectively. Every generic central section has precisely \((144,360,218)\) as its \((f_0,f_1,f_2)\)-vector, comprising \(152\) triangular and \(66\) quadrilateral facets. Here *generic* means that the section plane contains no original vertex.

## Assumptions and scope

All sections are through the origin and have a nonzero normal. The table includes normals on reflection mirrors and their intersections, rather than just generic normals. The polytope is the four-dimensional convex hull of the displayed vertices; the scale \(2\) is immaterial to combinatorial data. The statement classifies **face inventories**, not all combinatorial isomorphism types or metric volumes of sections. No claim is made about affine hyperplanes missing the origin.

## Proof

**1. Root system and fundamental chamber.** The \(120\) vertices form the root system of type \(H_4\). Take the following four roots, with row vectors listed in order:
\[
\alpha_1=(-2,0,0,0),\quad
\alpha_2=(\varphi,0,-1,1-\varphi),\quad
\alpha_3=(0,0,2,0),\quad
\alpha_4=(0,1-\varphi,-1,\varphi).
\]
Their Gram matrix is
\[
G=\begin{pmatrix}
4&-2\varphi&0&0\\
-2\varphi&4&-2&0\\
0&-2&4&-2\\
0&0&-2&4
\end{pmatrix}.
\]
Thus these are simple roots of a Coxeter system with diagram labels \(5,3,3\); the reflections in their orthogonal hyperplanes generate \(H_4\). Direct closure under the four reflections recovers all \(120\) displayed roots, and the standard fundamental-chamber theorem gives
\[
\mathcal C=\{u\in\mathbb R^4:\alpha_j\cdot u\ge0\ (1\le j\le4)\}
\]
as a closed fundamental chamber for the full root-hyperplane arrangement. Every nonzero normal is symmetry-equivalent to a point in \(\mathcal C\). The relative interiors of the nonzero faces of \(\mathcal C\) are precisely the \(15\) possibilities for the support of \((\alpha_1\cdot u,\ldots,\alpha_4\cdot u)\), each coordinate nonnegative. A non-simple positive root is a nonnegative linear combination of simple roots, so the sign pattern of all \(120\) vertex inner products is constant on each such relative interior.

For an entirely explicit representative, form the matrix \(A\) whose rows are the four simple roots. It has determinant \(8-4\varphi>0\). For every nonempty \(S\subseteq\{1,2,3,4\}\), take
\[
u_S=\operatorname{adj}(A)\sum_{j\in S}e_j.
\]
Then \(\alpha_i\cdot u_S=(8-4\varphi)\mathbf1_{\{i\in S\}}\). The mask is written in the order \((\mathbf1_{\{4\in S\}},\mathbf1_{\{3\in S\}},\mathbf1_{\{2\in S\}},\mathbf1_{\{1\in S\}})\). This proves that each row of the table has a realizable central section and that no further normal-sign patterns need consideration.

**2. Exact original face incidences.** Each vertex has squared norm \(4\). Two distinct vertices share a 600-cell edge exactly when their inner product equals \(2\varphi\), the nearest-neighbor inner product. Enumerating this equality over the displayed roots yields \(720\) edges. It gives \(1200\) three-vertex cliques and \(600\) four-vertex cliques. Each tetrahedral facet is a four-clique, and the 600-cell has exactly \(600\) tetrahedral facets [1–3]; therefore these are exactly all its facets. This is also checked directly by the included exact script.

**3. Reconstruction of the section.** Let \(\sigma_i=\operatorname{sign}(u\cdot v_i)\in\{-1,0,1\}\), where \(v_i\) ranges over the original vertices. Every vertex of the section is either an original vertex with \(\sigma_i=0\), or the interior crossing point of an original edge whose two endpoint signs have product \(-1\). These vertex sets are disjoint. Intersecting each tetrahedral facet with the plane produces either a polygonal facet of the section, a lower-dimensional face, or nothing. Its vertices are the zero-sign endpoints and the crossed-edge points in that tetrahedron. An intersected tetrahedron contributes a facet precisely when at least three distinct such vertices occur; the resulting polygon is triangular or quadrilateral. Polygonal intersections from different tetrahedra are identified by their sets of original-vertex or original-edge identifiers: this is essential when the plane contains an entire triangular ridge. The edges of the section are similarly obtained as intersections with the original \(1200\) triangular ridges. Each resulting section edge is incident with exactly two distinct section facets.

**4. Exhaustive exact finite computation.** The attached `EXACT_CHECK.py` builds the full vertex list over \(\mathbb Z[\varphi]\) and implements the above incidence rules with **exact** arithmetic. An element \(a+b\varphi\) is stored as the integer pair \((a,b)\), with multiplication using \(\varphi^2=\varphi+1\). Signs are decided exactly from the sign of \((2a+b)+b\sqrt5\) by integer comparisons of squares; no floating-point epsilon is used in the certificate. It constructs the matrix adjugate by integer-pair determinants, enumerates every nonempty support \(S\), and counts the distinct section vertices, edges, and facets. Its fifteen outputs are the fifteen rows of the displayed table. Each row independently satisfies both Euler's relation \(f_0-f_1+f_2=2\) and the facet-incidence identity \(3t+4q=2f_1\). The complete table contains eleven distinct tuples, proving the classification and its sharp bounds.

## Verification

Run `python3 EXACT_CHECK.py` from the directory containing that script. It requires only the Python standard library and prints all fifteen chamber representatives, including the numbers of old vertices on the plane and transversely crossed edges, followed by an exact success marker. It verifies root norms, original edge and clique counts, the \(H_4\) Gram matrix, matrix adjugate identities, every section-edge incidence multiplicity, both three-dimensional face-count identities, and the eleven-inventory count.

A separate optional implementation, `SPATIAL_CROSSCHECK.py`, constructs the exact-sign-derived section vertices numerically and independently checks each representative with a three-dimensional convex hull. Run `python3 SPATIAL_CROSSCHECK.py` with NumPy and SciPy installed. All fifteen hulls have the predicted number of extreme vertices, and their triangulated surfaces have the expected triangle counts. These floating-point experiments corroborate, but are not used in place of, the exact case enumeration and Coxeter-chamber reduction.

## Relationship to prior work

The vertex and face structure of the regular 600-cell, its binary-icosahedral \(H_4\) symmetry, and the existence of \(600\) tetrahedral facets are established classical material; they are not claimed as new [1–4]. Dutour Sikirić and Myrvold [1] classify **special cuts obtained by deleting independent vertex sets**; those are four-dimensional replacement polytopes, not three-dimensional central hyperplane sections. Bao and collaborators [2] determine matroid automorphism and flat data for \(H_4\), not the eleven-section face-inventory table. Denney and collaborators [3] investigate inscribed 24-cells and \(H_4\) structure without this central-section census. De Loera and collaborators [5] establish general hyperplane-section bounds and focus their explicit section sequences on cubes, rather than giving these 600-cell data. The finite chamber method here uses these known structures but computes an additional exact invariant specific to all central directions of the regular 600-cell.

## Limitations

Historical priority is not independently certified; older tabulations of special directions or parallel sections (including Coxeter's classical work) may contain subsets of the displayed inventories. The theorem does not classify face lattices beyond their inventories, nor does it cover noncentral hyperplanes, volumes, or random-orientation probabilities. Exact mathematical verification of the supplied enumerative proof is distinct from independent scholarly audit, which has not been performed.

## References

1. M. Dutour Sikirić and W. Myrvold, *The special cuts of the 600-cell* (arXiv:0708.3443, first version 25 August 2007), https://arxiv.org/abs/0708.3443.
2. C. Bao, C. Freidman-Gerlicz, G. Gordon, P. McGrath and J. Vega, *Matroid automorphisms of the root system H4* (arXiv:1005.5492, 2010), https://arxiv.org/abs/1005.5492.
3. T. Denney, D. Hooker, D. Johnson, T. Robinson, M. Butler and S. Claiborne, *The Geometry of H4 Polytopes* (arXiv:1912.06156, 2019), https://arxiv.org/abs/1912.06156.
4. M. Koca, M. Al-Ajmi and N. O. Koca, *Quaternionic Representation of Snub 24-Cell and its Dual Polytope Derived From E8 Root System* (arXiv:0906.2109, 2009), https://arxiv.org/abs/0906.2109.
5. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope* (arXiv:2412.12419, 2024), https://arxiv.org/abs/2412.12419.
