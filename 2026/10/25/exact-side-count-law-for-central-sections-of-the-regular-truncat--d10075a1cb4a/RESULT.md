# Exact side-count law for central sections of the regular truncated tetrahedron

## Finding

Let \(K\subset\mathbb R^3\) be the Archimedean regular truncated tetrahedron with vertices
\[
V=\bigl\{(3s_1,s_2,s_3),(s_1,3s_2,s_3),(s_1,s_2,3s_3):
 s_i\in\{-1,1\},\ s_1s_2s_3=1\bigr\}.
\]
For a uniformly distributed \(U\in S^2\), let \(N(U)\) be the number of sides of the planar convex polygon \(K\cap U^\perp\). Define
\[
\alpha=\arccos(1/11),\quad\beta=\arccos(5/11),\quad
\gamma=\arccos(7/11),\quad\delta=\arccos(9/11).
\]
For almost every orientation, \(N\in\{4,5,6\}\), and its **complete** probability law is
\[
\begin{aligned}
\Pr(N=4)&=\frac{24(2\alpha+\beta-\gamma-\pi)+6(2\pi-4\gamma-4\delta)}{4\pi}
             =0.215936085312640\ldots,\\
\Pr(N=5)&=\frac{48(\gamma+\delta-\alpha)+24(2\pi-2\alpha-2\beta-\gamma)}{4\pi}
             =0.520247465238935\ldots,\\
\Pr(N=6)&=\frac{8(3\beta-\pi)+24(2\alpha+\gamma-\delta-\pi)}{4\pi}
             =0.263816449448423\ldots.
\end{aligned}
\]
Consequently pentagons form a strict majority among central sections of this non-centrally-symmetric solid. An independent angular identity gives
\[
\mathbb E N=\frac{18}{\pi}\arccos(7/11)=5.047880364135783\ldots.
\]

## Assumptions and scope

The plane passes through the origin, which is the geometric center of \(K\); its **unoriented** normal has the rotation-invariant probability distribution, equivalently a uniformly random oriented unit normal \(U\). The side count is the number of genuine polygon vertices, not the number of faces of \(K\) meeting the plane with multiplicity. The exceptional orientations passing through a vertex or containing an edge have spherical measure zero. All assertions concern this single three-dimensional regular truncated tetrahedron, scaled as above; scaling does not change the side-count law.

## Proof

**1. Exact polyhedron and edge incidence.** Write \(T=\{s\in\{-1,1\}^3:s_1s_2s_3=1\}\). The polyhedron has the eight facet inequalities
\[
-3\le s\cdot x\le5\qquad(s\in T).
\]
Intersecting triples of their boundary planes and retaining points satisfying all inequalities yields exactly the twelve displayed vertices: each vertex lies on one triangular facet at level \(5\) and two hexagonal facets at level \(-3\). Two vertices are adjacent precisely when their squared distance is \(8\). There are eighteen such unordered pairs, each edge has length \(2\sqrt2\), and every vertex has degree three. The finite integer checks for the vertex and edge lists are in `verify_truncated_tetrahedron.py`. This also constructs the ordinary one-third truncation of a tetrahedron and shows the origin is interior.

For a generic \(u\), the section plane cuts a polyhedron edge at an interior point exactly when its endpoint scalar products with \(u\) have opposite signs. Hence
\[
N(u)=\sum_{\{i,j\}\in E}
  \boldsymbol1_{\{(u\cdot v_i)(u\cdot v_j)<0\}},
\]
where \(E\) is the set of those eighteen edges. This reduces the entire law to signs of twelve linear forms.

**2. A complete finite spherical partition.** The twelve great circles \(v_i\cdot u=0\) are distinct and no three pass through the same point: direct integer determinants of every three distinct \(v_i\) are nonzero. Thus their arrangement on \(S^2\) has exactly \(12(12-1)+2=134\) open chambers (the usual Euler count for great circles in general position). Inside each chamber all twelve signs, hence \(N\), are constant.

Here is the exhaustive finite procedure, with all decisions made using integers. For each of the \(2^{12}=4096\) sign masks, orient each normal \(v_i\) to point into its proposed chamber. Form all candidate extreme rays \(\pm\operatorname{primitive}(v_i\times v_j)\), for \(i<j\), retaining only the rays satisfying the twelve weak oriented inequalities. A genuine full-dimensional chamber is a pointed polyhedral cone; its extreme rays arise from two tight inequalities, and the sum of all its extreme rays is strictly inside every nonredundant halfspace. Conversely a strictly interior such sum verifies positive spherical area. This criterion yields exactly 134 genuine sign masks, also matching the independent Euler count.

For each such chamber, sort its primitive integer rays cyclically about their integer sum by exact integer planar orientation comparisons. Consecutive corner rays share exactly one great-circle wall. Denote the inward wall normals in cyclic order by \(w_1,\ldots,w_m\), each equal to one of \(\pm v_i\) and hence of squared length \(11\). The chamber is a geodesically convex spherical \(m\)-gon. Its interior corner angle is \(\pi-\arccos((w_{j-1}\cdot w_j)/11)\); Girard's spherical excess formula therefore gives **exactly**
\[
\operatorname{area}(C)=2\pi-\sum_{j=1}^{m}
 \arccos\!\left(\frac{w_{j-1}\cdot w_j}{11}\right).
\]
The table records every chamber, grouped by its section side count, chamber vertex count, integer scalar-product signature and multiplicity. Entries such as \((-5:1,-1:2,7:1)\) say that the cyclic inward-wall scalar products contain \(-5\) once, \(-1\) twice and \(7\) once. The table's arithmetic can be reconstructed independently from the supplied finite enumerator.

| Section sides | Number of chambers | Chamber corners | Inward-wall products and multiplicities | Individual spherical area |
| --- | ---: | ---: | --- | --- |
| \(4\) | \(24\) | \(4\) | \((-5:1,-1:2,7:1)\) | \(2\alpha+\beta-\gamma-\pi\) |
| \(4\) | \(6\) | \(8\) | \((7:4,9:4)\) | \(2\pi-4\gamma-4\delta\) |
| \(5\) | \(48\) | \(3\) | \((-9:1,-7:1,1:1)\) | \(\gamma+\delta-\alpha\) |
| \(5\) | \(24\) | \(5\) | \((1:2,5:2,7:1)\) | \(2\pi-2\alpha-2\beta-\gamma\) |
| \(6\) | \(8\) | \(3\) | \((-5:3)\) | \(3\beta-\pi\) |
| \(6\) | \(24\) | \(4\) | \((-7:1,-1:2,9:1)\) | \(2\alpha+\gamma-\delta-\pi\) |

The six multiplicities total 134 and the corresponding solid angles total \(4\pi\). Dividing the area of every side-count union by \(4\pi\) gives the three stated probabilities. In particular, the values of the four inverse cosines lie respectively in \((1.4797,1.4798)\), \((1.0989,1.0990)\), \((0.8810,0.8811)\), and \((0.6125,0.6126)\); these monotone-trigonometric bounds with \(3.14159<\pi<3.14160\) imply \(\Pr(N=5)>0.5194>1/2\).

**3. Independent mean identity.** Every edge pair has vertex norms \(\sqrt{11}\) and scalar product \(7\), so its endpoint directions form angle \(\arccos(7/11)\). A uniformly random oriented plane strictly separates either fixed pair with probability equal to their angular separation divided by \(\pi\). Summing over eighteen edges gives the displayed expectation without using the chamber enumeration. This agrees with the expectation computed from the complete law.

## Verification

Run `python3 verify_truncated_tetrahedron.py` with the Python standard library. The program first reconstructs all vertices as feasible intersections of triples of the eight explicit planes using rational arithmetic. It exhaustively computes all \(220\) triple determinants, \(132\) signed pairwise-intersection rays and \(4096\) potential sign masks; cyclic ordering and chamber classification use integer arithmetic. The resulting six integer signatures exactly match the displayed table. Numerical inverse-cosine evaluations are used only *after* exact signatures have been obtained, to display the probabilities and compare the independent expectation. Separate checks intersect the central section plane directly with pairs of the eight facet planes for 600 directions (not through the edge-crossing formula), and sample 80,000 Gaussian sphere directions. These finite tests corroborate, but do not replace, the geometric reduction and exhaustive finite argument.

## Relationship to prior work

Lonke's *On random sections of the cube* (first public arXiv version, 21 December 1998) develops vertex-expectation formulas for random central sections of cubes, not the side-count distribution of the non-centrally-symmetric truncated tetrahedron. The open-access study by Schein, Yeh, Coolsaet and Gayed (2016) treats the geometry and face decorations of this same Archimedean solid but does not state a central-section probability law. The MathWorld entry records its standard face, metric and projection descriptions, not these probabilities. Generic spherical-hyperplane arrangements and Girard's area formula are classical tools used in the proof, not claimed as new. Known formulas for other regular solids' random sections do not imply the present three-atom law for this different polyhedron.

## Limitations

No assertion is made about randomly translated (noncentral) sections, section area or perimeter, arbitrary affine deformations, other truncated tetrahedra or historical priority beyond the searched and inspected sources. This is a finite exact computation supported by a transparent exhaustive certificate; the independent geometric checks are finite samples and are not infinite proofs. No independent mathematical validation has been performed.

## References

1. Y. Lonke, *On random sections of the cube*, arXiv:math/9812123 (first public version 21 December 1998), https://arxiv.org/abs/math/9812123 .
2. S. Schein, A. J. Yeh, K. Coolsaet, J. M. Gayed, *Decoration of the Truncated Tetrahedron—An Archimedean Polyhedron—To Produce a New Class of Convex Equilateral Polyhedra with Tetrahedral Symmetry*, Symmetry **8** (2016), article 82, doi:10.3390/sym8080082; openly accessible at https://biblio.ugent.be/publication/8509418/file/8547887.pdf .
3. E. W. Weisstein, *Truncated Tetrahedron*, MathWorld, https://mathworld.wolfram.com/TruncatedTetrahedron.html (geometry and known invariants).
