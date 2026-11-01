# Exact Haar polygon-count law for central sections of the regular truncated octahedron

## Finding
Let
\[
P=\bigl\{X\in\mathbb R^3:|X_i|\le2\ (i=1,2,3),\quad |X_1|+|X_2|+|X_3|\le3\bigr\}.
\]
This is a regular truncated octahedron with vertices the signed coordinate permutations of \((0,1,2)\). Choose an unoriented plane uniformly from the rotation-invariant probability measure on planes through the origin. For its polygonal section \(S\), let \(N\) denote the number of vertices (equivalently, sides). Then, almost surely,
\[
N\in\{6,8,10\}.
\]
Define the positive algebraic numbers
\[
\begin{aligned}
d_1&=9\sqrt{14}+7\sqrt{21}+13\sqrt6+33,\\
d_2&=\sqrt{105}+10+4\sqrt5+2\sqrt{21},\\
d_3&=\sqrt{126}+11+2\sqrt{21}+4\sqrt6.
\end{aligned}
\]
The **complete exact law** is
\[
\begin{aligned}
\Pr(N=8)&=\frac{24}{\pi}\left[\arctan\left(\frac2{d_1}\right)+\arctan\left(\frac1{d_2}\right)\right],\\
\Pr(N=10)&=\frac{24}{\pi}\arctan\left(\frac1{d_3}\right),\\
\Pr(N=6)&=1-\Pr(N=8)-\Pr(N=10).
\end{aligned}
\]
The respective probabilities are approximately \(0.4984506899177035\), \(0.3161088555801908\), and \(0.1854404545021058\). Every listed polygon type occurs on a nonempty open set of plane orientations. In particular, a generic central section never has four or twelve sides.

## Assumptions and scope
The object is **one fixed, solid convex regular truncated octahedron**; the cutting plane must pass through its center. The law is for Haar-uniform *orientation*, not a randomly translated plane, not a planar projection, and not a section of its infinite periodic extension. Choose a uniformly distributed unit normal \(u\in S^2\) to represent the unoriented plane \(u^\perp\); the sign of \(u\) is immaterial. The excluded directions are those for which the section passes through a vertex of \(P\), a measure-zero union of great circles. All statements about probabilities therefore include no ambiguity at chamber boundaries.

## Proof
**1. Facet-incidence formula.** The polytope has six square facets \(X_i=\pm2\) and eight hexagonal facets \(\pm X_1\pm X_2\pm X_3=3\). Their vertices are precisely the signed permutations of \((0,1,2)\). For any plane missing all vertices, each facet met in a nondegenerate segment contributes exactly one side of the section, and all sides arise this way.

By signed permutation symmetry we may sort the normal's absolute coordinates as \(x>y>z>0\). Square facets come in opposite pairs. The pair with fixed coordinate of absolute normal weight \(a\) is crossed exactly when twice \(a\) is smaller than the larger of the other two weights, since its four vertex height values are \(\pm2a\pm b\) and \(\pm2a\pm c\). Thus the number of crossed square facets is
\[
2\boldsymbol1_{\{x>2y\}}+2\boldsymbol1_{\{x>2z\}}.
\]

Each hexagonal facet with sign vector \(\sigma\) consists of the six signed permutations of \((0,1,2)\) with coordinate signs \(\sigma\). Its six heights are \(2\sigma_i u_i+\sigma_j u_j\) for distinct coordinate indices \(i,j\). Taking representatives \((+,+,+)\), \((+,+,-)\), \((+,-,+)\), \((+,-,-)\) for the four opposite-facet pairs, the first is never crossed, the second is crossed exactly when \(y<2z\), and the last two are always crossed. Hence the number of crossed hexagonal facets is \(4+2\boldsymbol1_{\{y<2z\}}\). Summing gives the complete directionwise formula
\[
\boxed{N(u)=4+2\bigl(\boldsymbol1_{\{x>2y\}}+\boldsymbol1_{\{x>2z\}}+\boldsymbol1_{\{y<2z\}}\bigr).}
\]
Because \(x>y>z>0\), the impossible combinations eliminate values four and twelve, leaving precisely six, eight and ten.

**2. The angular chambers.** The signed permutation group partitions the sphere, up to boundaries, into 48 congruent copies of \(\mathcal C=\{x\ge y\ge z\ge0\}\), each of solid angle \(\pi/12\). Denote rays in that chamber by
\[
U=(2,2,1),\quad V=(2,1,1),\quad T=(4,2,1),\quad W=(2,1,0),\quad C=(1,0,0).
\]
The ten-sided event is \(x>2y\) and \(y<2z\); within \(\mathcal C\) it is exactly the interior of the cone over the spherical triangle with rays \(V,T,C\). The eight-sided event is the disjoint union of (i) \(x>2z,\ x<2y,\ y<2z\), the spherical triangle with rays \(U,V,T\), and (ii) \(x>2y,\ y>2z\), the spherical triangle with rays \(T,W,C\). The remaining chamber area is the six-sided event.

**3. Evaluation.** For three nonzero rays \(a,b,c\) spanning a pointed spherical triangle, its solid angle is
\[
\Omega(a,b,c)=2\arctan\frac{|\det(a,b,c)|}{\|a\|\|b\|\|c\|+(a\cdot b)\|c\|+(a\cdot c)\|b\|+(b\cdot c)\|a\|}.
\]
All denominators here are positive. Direct dot products and determinants give
\[
\Omega(U,V,T)=2\arctan(2/d_1),\quad
\Omega(T,W,C)=2\arctan(1/d_2),\quad
\Omega(V,T,C)=2\arctan(1/d_3).
\]
Divide these sums by \(\pi/12\) to obtain the displayed probabilities. The three triangles have nonzero area and the complementary six-sided chamber does too, proving all three types occur on open orientation sets. This completes the proof.

## Verification
The standalone script `check_section_law.py` independently enumerates all 24 vertices, 14 facets and 36 edges. For **10,690 generic positive integer normals** with sorted coordinates at most 40, it compares (a) the number of intersected facets, (b) the number of edges crossed by the plane and (c) the analytic indicator formula using exact integer arithmetic. All three agree. It independently evaluates all spherical triangle areas, verifies their partition of one \(\pi/12\) chamber, and checks them against 80,000 Gaussian-normal directions. The resulting observed frequencies for \((6,8,10)\) are \((0.497,0.316575,0.186425)\). These finite checks are corroboration, **not** a substitute for the complete facet and solid-angle proof.

## Relationship to prior work
The regular truncated octahedron is classical (see Johnson's description of uniform regular-faced polyhedra). De Leo (2005/2006) analyzes plane foliations of a *periodic extension* of a truncated octahedron and the topology of open leaves, a different object and question from the single bounded central cross-section. Valiunas, Zappa and Thomas (2016) develop symmetry-preserving scans of Coxeter-orbit polytopes in prescribed directions rather than a Haar law of all central planes. De Loera, Lopez-Campos and Torres (2024) study feasible hyperplane-section vertex counts and algorithms for enumerating sections in broader settings; their abstract does not certify or imply the exact orientation probabilities here. Published exact Haar face-count laws for sections of other individual regular bodies, such as the icosahedron and four-cube, do not imply the values for this truncated octahedron. Generic spherical-cone integration methods are standard; the new object-specific chamber classification and its exact three-point law are the proposed contribution.

## Limitations
The classification is for **central**, not off-center, sections; it makes no claim about section areas, perimeters or shape distributions within each polygon type, nor about deformed truncated octahedra. The literature comparison supports a best-knowledge originality assessment, not certified historical priority. The full text of the 2024 broad section-enumeration paper was not inspected; its abstract concerns feasible numbers rather than orientation measures. No independent audit has been performed.

## References
1. Roberto De Leo, *Topology of plane sections of periodic polyhedra with an application to the Truncated Octahedron*, arXiv:math/0502219 (first public version February 10, 2005); *Experimental Mathematics* 15 (2006), 109–124. https://arxiv.org/abs/math/0502219
2. Motiejus Valiunas, Emilio Zappa and Briony Thomas, *Sections of Coxeter Orbihedra*, Bridges 2016, 469–472 (2016). https://eprints.whiterose.ac.uk/id/eprint/99122/
3. Jesús A. De Loera, Gyivan Lopez-Campos and Antonio J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (2024). https://arxiv.org/abs/2412.12419
4. Norman W. Johnson, *Convex polyhedra with regular faces*, *Canadian Journal of Mathematics* 18 (1966), 169–200. https://doi.org/10.4153/CJM-1966-021-8
