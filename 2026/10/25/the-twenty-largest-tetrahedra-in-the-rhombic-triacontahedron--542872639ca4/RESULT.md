# The twenty largest tetrahedra in the rhombic triacontahedron

## Finding
Let \(\varphi=(1+\sqrt5)/2\), with \(\varphi^2=\varphi+1\), and let \(P\) be the convex hull of the following 32 points in Euclidean \(\mathbb R^3\): 12 cyclic permutations of \((0,\pm1,\pm\varphi)\), 12 cyclic permutations of \((0,\pm\varphi,\pm\varphi^{-1})\), and 8 points \((\pm1,\pm1,\pm1)\). All signs within each displayed type are independent. This is the standard coordinate realization of the rhombic triacontahedron.

The largest volume of any tetrahedron contained in \(P\) is
\[
  \max_{x_0,x_1,x_2,x_3\in P}
  \operatorname{Vol}_3(\operatorname{conv}\{x_0,x_1,x_2,x_3\})
  =\frac{5+2\sqrt5}{3}.
\]
There are **exactly 20 unordered maximizing tetrahedra, including arbitrary interior point choices**. They are all vertex-supported. A maximizing tetrahedron has exactly three vertices of the icosahedral 12-point orbit and one vertex of the dodecahedral 20-point orbit. More precisely, the 20 maximizers are obtained by taking each equilateral triple \(u,v,w\) of icosahedral vertices whose three mutual distances are \(2\varphi\), and adjoining the vertex \(-\varphi(u+v+w)\) of the dodecahedral orbit. All such apexes are distinct and no pair of distinct maximizing tetrahedra shares three vertices.

The containing polyhedron has volume \(20\) in these coordinates; hence the sharp relative tetrahedron volume is \((5+2\sqrt5)/60\). The ten well-known regular tetrahedra inscribed in its dodecahedral orbit each have volume \(8/3\), strictly below the optimum.

## Assumptions and scope
The body \(P\) is exactly the 32-vertex convex hull above; Euclidean, unnormalized volume is used. Tetrahedra may have arbitrary vertices anywhere in \(P\), not necessarily among its vertices; degenerate tetrahedra have zero volume. Equivalence is equality as **unordered geometric tetrahedra**, not modulo isometry. The classification makes no assertion about tetrahedra in other, noncongruent zonohedra.

## Proof
**Reduction to vertices.** For any four points \(x_0,x_1,x_2,x_3\in P\), the signed sixfold tetrahedron volume is an affine function of each point separately when the other three are fixed. Express each \(x_i\) as a convex combination of vertices of \(P\). Multiaffinity expands the signed determinant as a convex combination of determinants of ordered vertex quadruples. Consequently its absolute value is at most the greatest absolute vertex-quadruple determinant. Thus a global maximizer exists among vertex quadruples.

**An exact finite determinant lemma.** In the integral quadratic ring \(\mathbb Z[\varphi]\), represent \(a+b\varphi\) by \((a,b)\). Then multiplication is
\[
 (a,b)(c,d)=(ac+bd,\ ad+bc+bd).
\]
Its sign is exactly the sign of \((2a+b)+b\sqrt5\), decided by integer comparisons and, when signs oppose, by comparing \((2a+b)^2\) and \(5b^2\). Therefore there is no floating-point rounding or uncertain tie in ordering determinants. The standalone `triaconta_checker.py` enumerates all \(\binom{32}{4}=35{,}960\) distinct unordered four-vertex sets. For each set it computes a three-by-three determinant in \(\mathbb Z[\varphi]\) *twice*, once by minors and independently by Leibniz expansion. It compares their absolute values exactly, recording every maximizing set. Its exhaustive output is:

- Maximum absolute sixfold volume \(6+8\varphi\); precisely \(20\) maximizing four-subsets.
- Each such four-subset contains exactly three icosahedral and one dodecahedral vertex.
- Each icosahedral triple is equilateral with squared side length \(4\varphi^2\); there are precisely 20 such triples in the icosahedral orbit.
- For each triple \(u,v,w\), the fourth vertex equals \(-\varphi(u+v+w)\).
- No two maximizing four-subsets share three vertices.

The checker is complete rather than a truncated search: its loop is literally over all four-subsets, with a checked count asserted equal to \(35{,}960\). It also asserts every listed conclusion and checks the two independent determinant expansions at every iteration. As one direct equality witness, choose
\[
 u=(0,1,\varphi),\quad v=(0,1,-\varphi),\quad
 w=(1,-\varphi,0),\quad z=(-\varphi,-\varphi^{-1},0).
\]
Then \(z=-\varphi(u+v+w)\) and
\[
 |\det(v-u,w-u,z-u)|=6+8\varphi=10+4\sqrt5.
\]
Dividing by \(6\) gives the asserted maximum volume.

**No nonvertex equality cases.** Suppose any maximizing tetrahedron had a nonvertex corner. Express all four corners as convex combinations of polytope vertices, with at least two positive coefficients for the nonvertex corner. Orient the determinant positively. The signed determinant is then a convex combination of vertex-quadruple signed determinants, each bounded above by the certified maximum \(6+8\varphi\). Equality forces *every* combination with positive product weight to be a maximizing vertex quadruple of the same orientation. In particular, two different maximizing vertex quadruples would differ in exactly one corner and hence share three vertices. The exhaustive lemma proves no such pair exists. Thus all 20 maximizing tetrahedra are vertex-supported, and the stated classification is global.

**Volume ratio.** In this normalization each of the 30 golden-rhombus faces has perpendicular diagonals of lengths \(2\) and \(2/\varphi\), so face area is \(2/\varphi\). Each supporting face plane is at distance \(\varphi\) from the origin, by the same standard icosahedron/dodecahedron coordinate geometry. Splitting \(P\) into 30 pyramids with apex the origin yields
\[
 \operatorname{Vol}_3(P)=\frac13\cdot30\cdot\frac2\varphi\cdot\varphi=20.
\]
The classical ten regular tetrahedra on the dodecahedral vertices have exact sixfold volume \(16\), another directly checked determinant level, so volume \(16/6=8/3\). The maximizing volume is larger since \(6+8\varphi>16\).

## Verification
Run `python3 triaconta_checker.py` with an unmodified Python 3 standard library. It prints `CERTIFICATE_OK` only after verifying the exhaustive count, both determinant implementations for every candidate, the maximum \((6,8)\) as an exact pair of coefficients of \(1,\varphi\), all 20 maximizing vertex subsets, the equilateral-triangle/apex classification, and the three-vertex nonsharing property. All comparisons use exact integer arithmetic; no numerical approximations occur in the verifier. The published face-diagonal and volume formulas in the references provide an independent geometry check on the normalization.

## Relationship to prior work
The established geometry of the rhombic triacontahedron includes its exact 32-vertex icosahedral/dodecahedral construction, 30 golden-rhombus faces and volume; these facts are stated and developed by Raman and Krishnamoorthy (2001). MathWorld records the regular tetrahedron 10-compound inscribed in the 32 vertices, but does not identify it as volume-maximizing. The exact optimization, rigidity of all global equality cases and mixed-orbit classification above are distinct statements; in fact the known compound's regular tetrahedra are strictly smaller. Related published maximal-simplex calculations for the *regular icosahedron*, cube–octahedron interpolation and the four-dimensional 24-cell concern different containing polytopes, so their exact extrema do not determine this one.

## Limitations
This is a specific three-dimensional convex-polytope result, not a new universal bound for all zonohedra. Although the relevant sources and a semantic mathematical-results index were checked for implication or equivalence, an unindexed source containing the same special-case optimization remains a bibliographic risk. A finite exact enumeration is an exhaustive proof *only* for this explicitly finite vertex set; the separate multiaffine rigidity argument is essential to rule out nonvertex maximizers. The numeric face-volume normalization relies on standard geometric identities corroborated by the listed classical references.

## References
1. T. V. Raman and M. S. Krishnamoorthy, *Visual Techniques For Computing Polyhedral Volumes*, 2001-08-02, §§2.8 and 6: https://www.cs.cornell.edu/info/people/raman/publications/polyhedra/paper.html.
2. E. W. Weisstein, *Rhombic Triacontahedron*, MathWorld: https://mathworld.wolfram.com/RhombicTriacontahedron.html. In particular the 10-compound of tetrahedra and the 30 golden-rhombus faces.
3. *Rhombic triacontahedron*, standard 32-coordinate realization and face-diagonal/volume data: https://en.wikipedia.org/wiki/Rhombic_triacontahedron.
