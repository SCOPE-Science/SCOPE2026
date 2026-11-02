# Joint crossing laws of orthographic tetrahedral, cubic and octahedral wireframes

## Finding
Let \(U=(u_1,u_2,u_3)\) be Haar-uniform on the unit sphere. Orthogonally project **all** vertices and edges (including occluded edges) of each of the following three regular solids onto \(U^\perp\):
\[
T=\operatorname{conv}\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\},\quad C=[-1,1]^3,\quad O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}.
\]
Count transverse intersections of projected edges whose original edges share no endpoint. Denote the counts by \(N_T,N_C,N_O\). Apart from a measure-zero set of directions, all counts are well-defined and obey the **same-direction joint identity**
\[
\boxed{N_C=2,\qquad N_O=6-4N_T,\qquad
N_T={\bf1}\!\left\{\max_i|u_i|>\sum_{j\ne i}|u_j|\right\}.}
\]
Consequently the entire joint distribution has two atoms,
\[
\mathbb P\big((N_T,N_C,N_O)=(1,2,2)\big)=p,
\qquad\mathbb P\big((N_T,N_C,N_O)=(0,2,6)\big)=1-p,
\]
where
\[
\boxed{p=\frac{12}{\pi}\arctan(3-2\sqrt2)\approx0.64904068781636.}
\]
Moreover, for every three-dimensional parallelepiped and every generic rank-two linear map into a plane, its projected full one-skeleton has **exactly two** transverse disjoint-edge intersections (affine rigidity, not merely a probabilistic statement).

## Assumptions and scope
The counting convention uses the full embedded polyhedral graph, without hidden-edge removal. A crossing must occur in the relative interiors of two segments with distinct endpoints; touchings, coincidences, and triple intersections are excluded by restricting to generic directions. The stated probabilistic conclusions concern the regular solids in the displayed common coordinate frame and an isotropic direction \(U\). The parallelepiped conclusion concerns arbitrary nonsingular affine images of the cube and any generic linear projection of rank two. There is no claim about perspective projections, random straight-line drawings of abstract graphs, or the number of outline vertices.

## Proof
**1. Tetrahedron.** Write the four displayed tetrahedral vertices as \(v_i\). They satisfy \(\sum_i v_i=0\), \(\sum_i v_iv_i^{\mathsf T}=4I\). For every unit \(U\), put \(\lambda_i=U\cdot v_i\). Then \(\sum_i\lambda_i=0\) and \(\sum_i\lambda_i\operatorname{proj}_{U^\perp}(v_i)=0\). These coefficients give the unique affine dependence of four generic planar projected vertices. The complete graph on the four projected vertices has exactly one proper crossing when this dependence has a \(2\)-positive/\(2\)-negative sign split (the opposite positive/negative pair segments meet); it has no crossings for a \(1\)-versus-\(3\) split (one projected vertex lies inside the other three). By symmetry it suffices to take \(u_i>0\). The four coefficients then are \(u_1+u_2+u_3\), \(u_1-u_2-u_3\), \(-u_1+u_2-u_3\), \(-u_1-u_2+u_3\). Exactly two are positive if and only if one coordinate dominates the other two together. Hence the asserted \(N_T\) formula.

**2. Octahedron.** The planar projected vertices form three opposite pairs \(\{\pm a,\pm b,\pm c\}\), and the edge set is the complete tripartite graph joining vertices from different opposite pairs. Away from degenerate directions, use a nonsingular planar coordinate change and edge-preserving sign reflections to put \(a=(1,0)\), \(b=(0,1)\), \(c=(s,t)\) with \(s,t>0\). The absolute dependency coefficients of \(a,b,c\) are proportional to \(|u_1|,|u_2|,|u_3|\), so the three cases \(s+t<1\), \(s>t+1\), \(t>s+1\) are exactly the dominant-coordinate chamber; the complementary triangle-inequality chamber is \(s+t>1\), \(s<t+1\), \(t<s+1\). An exact segment-orientation classification (see Verification and the standalone script) gives respectively \(2,2,2\) and \(6\) intersections. These are the four connected open sign chambers, and no determinant of any three distinct projected vertices changes sign within a chamber. Therefore \(N_O=2\) on the dominant chamber and \(N_O=6\) otherwise.

**3. Cube and parallelepipeds.** The cube's projected vertices can, after an invertible planar map and edge-preserving sign reflections, be represented as \((\epsilon_1-s\epsilon_3,\epsilon_2-t\epsilon_3)\), where \(s,t>0\) and \(\epsilon_i\in\{-1,1\}\); edges connect sign vectors differing in one entry. Each determinant defining a proper crossing is a constant multiple of one of \(1,s,t,1+s,1-s,1+t,1-t,s+t,s-t\). Hence the only relevant open-chamber boundaries in the positive quadrant are \(s=1\), \(t=1\), \(s=t\). The six chambers each have exactly two crossings, established by the included exhaustive exact-arithmetic edge-pair test. All generic projections of a parallelepiped reduce to this form, proving affine rigidity.

**4. Exact spherical probability.** The dominant-coordinate event splits into \(24\) congruent spherical triangles (six choices of signed dominant axis, and four sign choices of the two minor coordinates). A representative triangle has vertices \(e_1,(e_1+e_2)/\sqrt2,(e_1+e_3)/\sqrt2\). Its spherical area, from the standard three-unit-vector solid-angle identity, is
\[
\Omega=2\arctan\frac{|\det(a,b,c)|}{1+a\cdot b+b\cdot c+c\cdot a}=2\arctan(3-2\sqrt2).
\]
Division of \(24\Omega\) by the sphere area \(4\pi\) proves the claimed probability. Combining the first three parts proves the two-atom joint law.

## Verification
Execute `python3 verify_wireframe.py` with Python 3, using only the standard library. The exact-rational checker constructs every cube and octahedron edge and every unordered disjoint-edge pair. It symbolically factors all segment-orientation determinants in the two planar parameters: \(168\) cube and \(120\) octahedral nonzero determinants. Each polynomial is affine linear and vanishes only on the stated chamber boundaries; a rational exact witness in **every** chamber verifies counts \((2,2,2,2,2,2)\) for the cube and \((2,2,2,6)\) for the octahedron. Because crossing predicates depend only on determinant signs, the sign-invariance argument elevates these finite chamber tests to exhaustive parameter proofs. The tetrahedral case and the spherical areas are proved analytically above and do not depend on the checker. The code is a dependency-free, independently runnable source file embedded in this finding.

## Relationship to prior work
The subject is geometric drawing of fixed embedded polyhedral graphs under orthographic projection, rather than maximal rectilinear crossing numbers over **all** drawings. Alpert, Feder and Harborth (2008) study abstract regular graphs' maximal rectilinear crossing numbers and do not constrain drawings to a fixed three-dimensional embedded skeleton. Dujmović, Morin and Sheffer (2013) count crossings in geometric grid drawings, with different objects and asymptotic regimes. Alpert, Feder, Harborth and Klein (2009) treat maximum rectilinear crossing numbers of hypercube graphs; available abstract information does not establish this particular fixed-projection theorem. Related known octahedral shadow-vertex distributions determine how many silhouette vertices occur, but do not themselves specify crossing counts of the **entire wireframe** or the pointwise tetrahedron–octahedron coupling and affine cube rigidity. The novelty claim applies to their conjunction; it does not assert that any single shadow probability was previously unknown.

## Limitations
The conclusion excludes nongeneric projection directions; there, projected vertices or edges can coincide and proper-intersection counting may change by convention. The graph is a full wireframe with all back edges, not a visibility drawing. Historical-priority search is necessarily nonexhaustive; the full 2009 hypercube crossing-number article could not be retrieved and an equivalent older special case cannot be excluded. The result is proved for three polyhedral families, not all Platonic solids or arbitrary polyhedra. The numerical probability is subordinate to the exact formula.

## References
1. A. Alpert, S. Feder and H. Harborth, *The Maximum of the Maximum Rectilinear Crossing Numbers of d-regular Graphs of Order n*, arXiv:0812.1917, publicly posted 2008-12-10, https://arxiv.org/abs/0812.1917 .
2. V. Dujmović, P. Morin and A. Sheffer, *Crossings in Grid Drawings*, arXiv:1301.0303, publicly posted 2013-01-02, https://arxiv.org/abs/1301.0303 .
3. A. Alpert, S. Feder, H. Harborth and H. Klein, *The Maximum Rectilinear Crossing Number of the n Dimensional Cube Graph* (2009), accessible bibliographic abstract, https://academicworks.cuny.edu/kb_pubs/87/ .
