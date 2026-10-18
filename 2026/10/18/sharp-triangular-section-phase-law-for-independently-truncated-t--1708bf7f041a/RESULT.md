# Sharp triangular-section phase law for independently truncated tetrahedra

## Finding

Let \(T\subset\mathbb R^3\) be any nondegenerate tetrahedron with vertices \(v_0,v_1,v_2,v_3\) and centroid \(g=\tfrac14\sum_i v_i\). Independently truncate its four corners by fractions \(0<t_i<1/2\) of the outgoing edges. Write
\[
 p_{ij}=(1-t_i)v_i+t_i v_j\quad(i\ne j),\qquad
 P=\operatorname{conv}\{p_{ij}:i\ne j\},\qquad
 q_i=\frac{t_i}{1-t_i}.
\]
For a uniformly random (Haar) unoriented plane \(H_u=\{x:u\cdot(x-g)=0\}\) through the **original** centroid, let \(N(u)\) be the number of vertices of the generic section polygon \(P\cap H_u\). Then, independently of the metric shape of \(T\), a triangular section occurs with positive probability if and only if
\[
 \boxed{\sum_{i=0}^3q_i-\max_{0\le i\le3}q_i<1.}
\]
More precisely, put \(w_i=v_i-g\). For each \(i\), let \(J_i=\{0,1,2,3\}\setminus\{i\}\) and
\[
 m_{ij}=(1-t_j)w_j+t_jw_i\quad(j\in J_i),\qquad
 \Omega_i=\begin{cases}
 2\pi-\displaystyle\sum_{\{j,k\}\subset J_i}
 \arccos\!\left(\frac{m_{ij}\cdot m_{ik}}{\|m_{ij}\|\,\|m_{ik}\|}\right),
 &\displaystyle\sum_{j\in J_i}q_j<1,\\[4pt]
 0,&\displaystyle\sum_{j\in J_i}q_j\ge1.
 \end{cases}
\]
All vectors in the angular formula are nonzero in the active case. The **exact** law is
\[
 \boxed{\Pr\bigl(N(u)=3\bigr)=\frac{1}{2\pi}\sum_{i=0}^3\Omega_i.}
\]
Thus the existence criterion is affine invariant, while the probabilities depend on the Euclidean embedding.

For an equi-truncated regular tetrahedron, \(t_0=t_1=t_2=t_3=t\), the criterion is sharply \(0<t<1/4\), and
\[
 \boxed{\Pr(N=3)=\begin{cases}
 \dfrac{2}{\pi}\!\left[3\arccos\!\left(\dfrac{1-4t^2}{3-8t+8t^2}\right)-\pi\right],&0<t<1/4,\\[7pt]
 0,&1/4\le t<1/2.
 \end{cases}}
\]
At the critical depth the probability disappears **quadratically**:
\[
 \Pr_{\,t=1/4-\varepsilon}(N=3)=\frac{64\sqrt3}{3\pi}\,\varepsilon^2+O(\varepsilon^3)
 \qquad(\varepsilon\downarrow0).
\]
In particular the regular Archimedean truncated tetrahedron (\(t=1/3\)) admits no **generic** triangular plane section through its center, even though it has triangular faces.

## Assumptions and scope

The original tetrahedron is nondegenerate in Euclidean three-space. Each \(t_i\) lies strictly between zero and one half; hence the four parallel corner cuts are nonoverlapping and \(P\) has twelve distinct vertices and eighteen edges. In the unequal-depth case the distinguished plane center is \(g\), the centroid of \(T\), *not generally the centroid of* \(P\). The normal \(u\) is uniformly distributed on \(S^2\), modulo sign. The exceptional normal directions with a plane through one of the twelve vertices are a measure-zero union of great circles and are excluded from the polygon-count assertion; no claim about their combinatorially degenerate sections is made.

## Proof

**1. Exhaustive three-edge-cut lemma.** Label each truncated vertex by its ordered pair \((i,j)\) and partition the twelve vertices into four corner triples \(G_i=\{(i,j):j\ne i\}\). The graph edges comprise the three edges inside each \(G_i\) and one connector \((i,j)(j,i)\) for each unordered \(\{i,j\}\). Any generic transverse plane cutting a three-dimensional polytope meets exactly the graph edges whose endpoints lie in opposite open half-spaces; their number equals the number of section-polygon vertices.

A nontrivial sign cut in this 18-edge graph has exactly three crossing edges only if its positive vertex set is a singleton, the complement of a singleton, one complete corner triple \(G_i\), or its complement. To show this without computation, every partially selected triangle \(G_i\) contributes exactly two internal crossing edges. Two partially selected groups would already contribute four. If exactly one is partial, let \(r\in\{0,1,2,3\}\) of the other groups be fully selected. For \(r=1,2\), connectors among the three complete groups contribute two further crossings, so the total is at least four. For \(r=0\), the cut has \(2+k\) crossings, where \(k=1\) or \(2\) is the number selected in the partial triple; three crossings require \(k=1\), a singleton. For \(r=3\), the cut has \(2+(3-k)\) crossings and three crossings require \(k=2\), the complement of a singleton. If no group is partial, choosing \(r\) whole groups crosses \(r(4-r)\) connectors; three requires \(r=1\) or \(3\). This exhausts all possibilities.

**2. Elimination of singleton cuts by centering.** Fix one omitted vertex \(p_{ij}\) and choose the two other indices \(k,l\) so that \(\{i,j,k,l\}=\{0,1,2,3\}\). Because \(t_i+t_k<1\), the midpoint \((v_i+v_k)/2\) lies on the segment joining \(p_{ik}\) and \(p_{ki}\). Likewise \((v_j+v_l)/2\) lies on the segment joining \(p_{jl}\) and \(p_{lj}\). All four segment endpoints differ from \(p_{ij}\), and the mean of the two midpoints is \(g\). Therefore \(g\) belongs to the convex hull of the other eleven vertices. No plane through \(g\) can strictly separate the omitted vertex from all eleven others. Complement-singleton signs are excluded as well.

**3. An exact three-parameter simplex criterion at each corner.** Hence a generic triangular section is equivalent to one of the four complete triples \(G_i\) lying strictly on one side and the remaining nine vertices on the other. Translate the origin to \(g\), and put \(a_j=u\cdot w_j\). Since \(\sum_jw_j=0\), we have \(\sum_j a_j=0\). Also
\[
 \sum_{k\ne j}u\cdot(p_{jk}-g)=(3-4t_j)a_j,
\]
with \(3-4t_j>0\). When the triple \(G_i\) is positive and the others negative, this forces \(a_i>0\) and \(a_j<0\) for every \(j\ne i\). Set \(r_j=-a_j/a_i>0\), so \(\sum_{j\ne i}r_j=1\). The three connector vertices on the negative side obey
\[
 u\cdot(p_{ji}-g)<0\ \Longleftrightarrow\ r_j>\frac{t_j}{1-t_j}=q_j.
\]
All other negative vertices automatically have negative height. Because \(r_j<1\) and \(t_i<1/2\), the positive-corner vertex heights satisfy \(u\cdot(p_{ij}-g)=a_i[(1-t_i)-t_ir_j]>0\). Conversely, those strict inequalities on the three connector vertices force all the other required signs: indeed their weighted sum is
\[
 \sum_{j\ne i}\frac{p_{ji}-g}{1-t_j}=\left(\sum_{j\ne i}q_j-1\right)w_i.
\]
If \(\sum_{j\ne i}q_j<1\), the three inequalities imply \(a_i>0\), thence all the other signs. The possible ratios \((r_j)_{j\ne i}\) form the open unit 2-simplex, and every such ratio comes from some normal direction because the vertex-height map of a nondegenerate tetrahedron is an isomorphism onto \(\{(a_0,a_1,a_2,a_3):\sum a_i=0\}\). Thus corner \(i\) is active precisely when \(\sum_{j\ne i}q_j<1\). Existence for at least one corner is equivalent to the displayed minimum-three-odds criterion.

**4. Exact spherical integration.** At active corner \(i\), the three inequalities are \(u\cdot m_{ij}<0\) for \(j\ne i\). They define one nonempty pointed trihedral cone in normal space. Its spherical section is a geodesic spherical triangle with interior angles \(\pi-\arccos(m_{ij}\cdot m_{ik}/(\|m_{ij}\|\|m_{ik}\|))\) at the vertex shared by the two bounding great circles. By Girard's theorem its area is precisely \(\Omega_i\) above. A second antipodal triangle corresponds to the reverse sign of the same plane; cones for distinct \(i\) are disjoint. The total spherical probability is \(2\sum_i\Omega_i/(4\pi)=\sum_i\Omega_i/(2\pi)\). Inactive corners make no contribution.

**5. Regular equal-depth specialization.** Affine scale permits the regular vertex realization \((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\). For any distinct \(j,k\ne i\),
\[
 \|m_{ij}\|^2=3-8t+8t^2,\qquad m_{ij}\cdot m_{ik}=4t^2-1.
\]
Four identical corner areas give the stated one-variable expression. The condition \(3t/(1-t)<1\) is exactly \(t<1/4\). Writing \(t=1/4-\varepsilon\), one has
\[
 \frac{1-4t^2}{3-8t+8t^2}=\frac12-\frac{16}{3}\varepsilon^2+O(\varepsilon^3).
\]
Taylor expansion of \(\arccos\) at \(1/2\) produces the displayed coefficient \(64\sqrt3/(3\pi)\). This completes the proof.

## Verification

The accompanying standalone Python 3 file `tetra_truncation_verify.py` requires only the standard library. Run `python tetra_truncation_verify.py`. It independently enumerates all \(2^{12}-2\) nontrivial sign assignments of the 12-vertex graph, finding exactly 32 three-edge cuts (12 singletons, 12 complements, four corner triples, four complements). It checks 14,279 nondegenerate integer-normal examples with exact rational arithmetic for two tetrahedral affine shapes and six four-depth vectors. It also checks the solid-angle expression against 150,000 random orientations at each of five depth vectors and checks the equal-depth specialization. Reproduction yields `EXACT_GRAPH_CUTS_OK 32 EXACT_RATIONAL_NORMALS_OK 14279` and `SPHERICAL_SOLID_ANGLE_FORMULAS_OK`. The proof of the continuous probability statement is the analytic sign-cone and spherical-area argument, not the finite tests or Monte Carlo simulation.

## Relationship to prior work

Feldman and Klain (2008) relate solid angles of a tetrahedron to the probability of triangular **orthogonal shadows** of the untruncated tetrahedron. Their result motivates using normal cones, but orthogonal projection differs from slicing an independently truncated tetrahedron through the original centroid. The standard regular truncated tetrahedron and its 12-vertex graph are classical objects. Krčmár, Gendiar and Nishino (2015/2016) study a truncated-tetrahedral spin lattice, rather than these random-section probability laws. König (2020) studies noncentral **volume/perimeter extrema** of sections of untruncated simplices, cross-polytopes and cubes. The claimed contribution is the four-depth strict odds criterion, exact solid-angle law, and equal-depth quadratic extinction at the critical quarter-edge cut, not the classical graph, general Girard formula, or the untruncated tetrahedron's projection formula.

## Limitations

Only the triangular side-count atom of the **original-centroid-passing** random plane-section law is computed; higher polygon counts and random affine-offset plane sections are outside the claim. The parameter range excludes zero-depth, coincident cuts and past-midpoint overlaps, though the equal-depth formula admits its indicated zero-depth limit. Exceptional nongeneric directions are excluded, and the classical limit at zero depth does not imply historical novelty. An unindexed equivalent special case in older polyhedral section tables may remain undiscovered; definitive literature priority and independent mathematical validation have not been established.

## References

1. J. Feldman and D. Klain, *Angles as probabilities*, arXiv:0809.3459 (first public version, 2008-09-19), https://arxiv.org/abs/0809.3459 .
2. M. Krčmár, A. Gendiar and T. Nishino, *Phase diagram of truncated tetrahedral model*, arXiv:1512.09059 (2015/2016), https://arxiv.org/abs/1512.09059 .
3. H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743 (2020), https://arxiv.org/abs/2002.10743 .
