# All edge-length arrangements of scalene-faced convex octahedra

## Finding
Let \(T\) be a nondegenerate **scalene** Euclidean triangle with distinct side lengths \(a,b,c\). Consider three-dimensional convex polyhedra combinatorially equivalent to the octahedron, with all eight facets congruent to \(T\), allowing reflected copies. Two *edge-length arrangements* are equivalent if a combinatorial automorphism maps the edges of every numerical length to those of the same numerical length.

**Theorem.** There are exactly four possible combinatorial edge-length arrangements, before geometric feasibility: one *coordinate* type and three *twisted* types, distinguished by which of \(a,b,c\) labels the cyclic four-edge equator. The coordinate type is geometrically realizable if and only if \(T\) is acute. The twisted type with equatorial edge length \(s\) is geometrically realizable if and only if the angle opposite \(s\) in \(T\) is acute. Each feasible arrangement determines exactly one Euclidean congruence class of convex octahedra.

Hence **four** congruence classes occur for acute scalene triangles, and **two** for right or obtuse scalene triangles. Each geometric shape realizes exactly its indicated edge-length arrangement. Non-octahedral eight-face combinatorial types are outside the theorem.

## Assumptions and scope
A convex octahedron means a full-dimensional convex three-polytope whose vertex–edge–facet incidence graph is the standard six-vertex octahedron. Its eight facets must be genuine nondegenerate triangles, not merely a triangulation of larger polygonal facets. Congruence of facets allows reflections. Scalene means all three side lengths are different. The angle opposite a side \(s\) is acute precisely when \(s^2\) is strictly less than the sum of squares of the other two side lengths.

The four arrangements are classified only up to length-preserving combinatorial automorphisms; an individual polyhedron may be embedded in either handed orientation in space, but this does not change its ordinary Euclidean congruence class.

## Proof
**1. Four and only four combinatorial arrangements.** The dual of the octahedron's edge graph is the cube. Each triangular facet uses one edge of each of the three distinct lengths. Therefore, assigning edge lengths on the octahedron is equivalent to a proper three-edge-coloring of the cube: each of its eight vertices is incident with precisely one edge of each color. Each color class is a perfect matching of the cube. The cube has exactly nine perfect matchings. An exhaustive case split, or the finite exact enumeration in `check_octahedron_classification.py`, shows that the 12 cube edges have exactly **four** partitions into three perfect matchings (ignoring a permutation of the three color names): one partition consists of the three coordinate-direction matchings; each of the other three contains precisely one coordinate-direction matching and two non-coordinate matchings. For a fixed set of numerical colors, the latter three arrangements are distinguished by *which numerical color* forms the straight matching; automorphisms preserve straightness. The straight cube matching corresponds in the dual octahedron to a four-cycle whose four edges have a common length. This proves the combinatorial classification, including exhaustiveness.

A direct finite verification iterates all \(\binom{12}{4}=495\) candidate four-edge subsets of the cube, retains the nine that cover all eight cube vertices exactly once, and enumerates all disjoint triples with union the full twelve-edge set. It finds exactly four, and their numbers of coordinate-direction matchings are \(3,1,1,1\). This is an exhaustive finite assertion, independently of floating-point experiments.

**2. Coordinate arrangement.** Label the octahedron's opposite vertex pairs \(\{\pm u\},\{\pm v\},\{\pm w\}\), with independent vectors \(u,v,w\in\mathbb R^3\). Every convex polyhedron with the octahedron graph and a selected center of inversion has this form in the coordinate coloring: opposite pairs carry no edges, and each of the four edges between two opposite pairs has the same prescribed length. The equalities
\[
|u-v|^2=|u+v|^2,\quad |u-w|^2=|u+w|^2,\quad |v-w|^2=|v+w|^2
\]
force \(u\cdot v=u\cdot w=v\cdot w=0\). Conversely orthogonal axes produce all eight congruent triangles, with side lengths \(\sqrt{|u|^2+|v|^2}\), \(\sqrt{|u|^2+|w|^2}\), and \(\sqrt{|v|^2+|w|^2}\). For any prescribed assignment of \(a,b,c\), the three positive squared axis lengths are one-half of the respective differences \(a^2+b^2-c^2\), \(a^2+c^2-b^2\), and \(b^2+c^2-a^2\). All are positive exactly when \(T\) is acute. They determine the shape uniquely up to rigid motion.

For completeness, central symmetry need not be an *a priori* hypothesis: the coordinate edge-length pattern itself forces it. Regard the six vertices as three opposite graph pairs \(\{U_+,U_-\},\{V_+,V_-\},\{W_+,W_-\}\). Equal distances from both points of the first pair to both of the second pair imply that the pair midpoints have mutually perpendicular difference vectors, and the three distinct pair-midpoints coincide. One can see this by writing each pair as midpoint plus half-difference; the four equal cross-distances force the difference vectors orthogonal and their midpoint displacement orthogonal to both difference vectors. Applying this to all three pairs and using linear independence gives a common midpoint. Thus the displayed centered representation is forced.

**3. Twisted arrangement and necessary angle condition.** Suppose the unique straight cube matching has numerical color \(s\), so its primal edges make a four-cycle \(ABCD\) of length \(s\), and the remaining two vertices are apices \(U,V\). Write the other face side lengths as \(p,q\). After exchanging apex labels and cyclically relabeling the equator, the lengths are
\[
|UA|=|UC|=|VB|=|VD|=p,\qquad
|UB|=|UD|=|VA|=|VC|=q,
\]
and \(|AB|=|BC|=|CD|=|DA|=s\).

Place \(U=(0,0,h)\), \(V=(0,0,-h)\) with \(h>0\). The distance equations put \(A,C\) on a circle at height \(t\) and \(B,D\) on a circle at height \(-t\); the two circles have the **same** radius \(r>0\). Equality of the four cyclic edge lengths forces the horizontal projections of \(A,C\) and of \(B,D\) to be antipodal pairs, with these two pairs perpendicular. Indeed equality of \(|AB|,|BC|\) makes each of the two projected points \(B,D\) perpendicular to the difference between the projections of \(A,C\), and equality of \(|AB|,|AD|\) similarly gives the converse; distinctness of all four vertices yields antipodal pairs. After a rotation,
\[
A=(r,0,t),\ B=(0,r,-t),\ C=(-r,0,t),\ D=(0,-r,-t).
\]
Since \(UAB\) and the other seven listed triangles are *supporting facets*, the opposite vertices must lie strictly inside their inward halfspaces. The cross product \((A-U)\times(B-U)=(r(h-t),r(h+t),r^2)\), and tests against \(C,D\), yield \(h-t>0\) and \(h+t>0\). (The other apex is likewise strictly inward.) Thus \(d=h-t>0\) and \(q_0=h+t>0\), and
\[
p^2=r^2+d^2,\qquad q^2=r^2+q_0^2,\qquad s^2=2r^2+(q_0-d)^2.
\]
Subtracting gives \(p^2+q^2-s^2=2d q_0>0\). The angle opposite the prescribed equatorial side \(s\) must therefore be acute.

**4. Sufficient construction and uniqueness.** Conversely assume \(p^2+q^2>s^2\) and the strict triangle inequalities. Put \(M=(p^2+q^2-s^2)/2\), so \(0<M<pq\). There is a unique \(X\in(0,\min\{p^2,q^2\})\) such that \((p^2-X)(q^2-X)=M^2\), because the left side is strictly decreasing on this interval, starts at \(p^2q^2>M^2\), and ends at zero. Set
\[
r=\sqrt X,\quad d=\sqrt{p^2-X},\quad q_0=\sqrt{q^2-X},\quad h=(d+q_0)/2,\quad t=(q_0-d)/2.
\]
Take the six coordinates displayed above. The eight specified triangles have side lengths \(s,p,q\), and their support inequalities are strict because \(r,d,q_0>0\) (the normals of the eight triangles follow from the normal of \(UAB\) by the point symmetries). Consequently the convex hull has precisely those eight genuine triangular facets. The construction and the uniqueness of \(X\) show that any realization in that incidence class is congruent to this one.

**5. Counting feasible classes.** Every nondegenerate Euclidean triangle has at least two acute angles. If scalene and acute it has three, so all three twisted arrangements and the coordinate arrangement occur: four types. If scalene and right or obtuse, precisely two angles are acute; the corresponding two twisted arrangements occur, but the third twisted arrangement and the coordinate arrangement do not: two types. This completes the classification.

## Verification
The standalone Python file `check_octahedron_classification.py` enumerates all cube perfect matchings exactly and checks the four partitions, including their coordinate-match distribution. It also checks an exact rational Gram-identity consistency certificate and sample acute/nonacute class counts. The infinite geometric realization and nonrealization statements follow from the explicit supporting-hyperplane and circle arguments above, **not** from the finite enumeration or numerical sample tests alone.

## Relationship to prior work
Georgiou [1] proves existence of an eight-face convex octahedron with any prescribed triangle, exhibits one realization, and classifies the *minimum number of faces* among arbitrary convex polyhedra. Its Section 2 treats an alternating four-cycle construction, while its Lemma 5 classifies equifacial tetrahedra by acuteness. Neither its eight-face existence assertion nor its tetrahedral characterization compares the distinct edge-length incidence arrangements of the octahedral graph or states the four-versus-two classification and uniqueness in each class established here. The coordinate realization is related to the classical disphenoid construction but the classification of all octahedral edge-color patterns requires the cube-matching analysis; the twisted realizations include the source construction for different choices of equatorial edge length.

## Limitations
The theorem applies only when the prescribed face triangle is scalene and the polyhedron is combinatorially octahedral. It does not classify eight-triangle polyhedra with a stacked or other non-octahedral graph, isosceles triangles where equal lengths merge color classes, orientation-preserving face matching, or the possible number of noncongruent realizations outside these incidence patterns. The primary paper's eight-face construction is prior art; its universality is not claimed as new. Literature searches do not prove absolute historical priority, and independent audit has not been performed.

## References
[1] George M. Georgiou, *Congruent Triangular Faces, Reflections Allowed: Universal Realization and the Minimum Face Count in Problem B22*, arXiv:2608.01109v1 (first public 2026-08-02), especially Sections 2–4 and Lemma 5. https://arxiv.org/pdf/2608.01109

[2] J. Leech, *Some properties of the isosceles tetrahedron*, Mathematical Gazette 34 (1950), 269–271, as cited in [1].
