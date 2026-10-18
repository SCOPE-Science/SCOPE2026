# Joint central-section law and a rigid icosahedral refinement of dodecahedral normal chambers

## Finding

Let \(\varphi=(1+\sqrt5)/2\). In one coordinate system, take the centered regular dodecahedron
\[
D=\operatorname{conv}\{(\pm1,\pm1,\pm1),\ (0,\pm\varphi^{-1},\pm\varphi),\ (\pm\varphi^{-1},\pm\varphi,0),\ (\pm\varphi,0,\pm\varphi^{-1})\},
\]
and its regular icosahedral dual
\[
I=\operatorname{conv}\{(0,\pm\varphi,\pm1),\ (\pm\varphi,\pm1,0),\ (\pm1,0,\pm\varphi)\}.
\]
The signs in each displayed coordinate family vary independently. Let \(U\) be uniform on the unit sphere, and let \(N_D(U)\) and \(N_I(U)\) be the numbers of vertices of \(D\cap U^\perp\) and \(I\cap U^\perp\), respectively. Put
\[
\alpha=\arccos(\sqrt5/3),\qquad \beta=\arccos(1/3),\qquad \theta=\arccos(1/\sqrt5).
\]
The **complete joint probability law** is
\[
\begin{array}{c|cc}
 &N_I=10&N_I=12\\\hline
N_D=6&\displaystyle\frac{15(\pi-\alpha-\beta-\theta)}\pi&\displaystyle\frac{5(3\theta-\pi)}\pi\\[3pt]
N_D=8&\displaystyle\frac{15(2\beta+\alpha-\pi)}\pi&0\\[3pt]
N_D=10&\displaystyle\frac{3(2\pi-5\beta)}\pi&0.
\end{array}
\]
The four nonzero entries are approximately \(0.352163076315839\), \(0.286245735243501\), \(0.238989468899770\), and \(0.122601719540890\) in row-major order. In particular, **every generic central dodecahedral octagon or decagon is paired with an icosahedral decagon**; an icosahedral dodecagon forces a dodecahedral hexagon.

A stronger combinatorial assertion explains the coupling. The ten great circles orthogonal to the antipodal vertex axes of \(D\) partition the sphere into \(20\) hexagonal, \(60\) triangular and \(12\) pentagonal chambers. The six great circles orthogonal to the antipodal vertex axes of \(I\) refine **each** dodecahedral hexagonal chamber into four spherical triangles, one of icosahedral section type \(12\) and three of icosahedral section type \(10\); they leave every dodecahedral triangular and pentagonal chamber uncut. The common refinement has exactly \(152\) chambers and creates no additional intersection vertices. Its four joint-section classes contain \(60,20,60,12\) chambers, respectively, in the row-major order above with the zero classes omitted.

## Assumptions and scope

A central section uses a plane through the common origin. The normal \(U\) has spherical area measure normalized by \(4\pi\). A normal is *generic* when it is not perpendicular to any vertex of either solid. The exceptional finite union of great circles has probability zero. The coupling concerns the **same** normal for both solids: independent normal choices do not obey the displayed joint law. The conclusion is invariant under common rigid motions and independent positive rescaling of either polyhedron, but not under arbitrary relative rotation or arbitrary deformation.

## Proof

**1. From plane sections to great-circle chambers.** For a generic normal \(u\), an edge \([v,w]\) of a convex three-polytope contributes exactly one vertex to its central section if and only if \(\langle u,v\rangle\langle u,w\rangle<0\). Thus the section vertex count is the number of edges cut by the vertex-sign bipartition. Every vertex set above comes in antipodal pairs: there are ten such pairs for \(D\), six for \(I\). Their orthogonal great circles partition the normal sphere into open chambers on each of which both section counts are constant.

**2. Exhaustive common-refinement certificate.** All vertex coordinates and every cross product belong to the quadratic integer ring \(\mathbb Z[\varphi]\), where \(\varphi^2=\varphi+1\). The attached self-contained `verify.py` implements exact signs in that ring. It constructs the \(30\) edges of each solid from exact squared edge lengths \(8-4\varphi\) and \(4\), respectively; then forms the projective intersection directions of every pair of great-circle normals and merges pairs only when their exact cross product vanishes. For the ten-circle arrangement, the counts \((V,E,F)\) of spherical arrangement vertices, edges and chambers are \((90,180,92)\). For the six-circle arrangement they are \((30,60,32)\). For their common sixteen-circle refinement, they are \((90,240,152)\). In each case, \(F=E-V+2\) follows from Euler's formula for the sphere. In particular, the extra six great circles introduce no new arrangement vertices.

For every arrangement vertex \(x\), the program constructs candidate open sign chambers using the infinitesimal perturbations \(x+\varepsilon y\), where \(y\) lies between consecutive tangent rays of the incident great circles. Each candidate's signs are evaluated **exactly**: nonvanishing products use \(\operatorname{sgn}\langle x,v\rangle\), and products vanishing at \(x\) use \(\operatorname{sgn}\langle y,v\rangle\). Thus every recorded sign mask labels a genuine open chamber for all sufficiently small positive \(\varepsilon\). Distinct sign masks label disjoint convex spherical chambers. The resulting counts are precisely \(92,32,152\), independently agreeing with Euler's counts, which proves that the enumeration is exhaustive rather than sampled. The only use of approximate angles is to propose tangent-ray sectors; exact feasibility and the independent Euler bound certify completeness.

The complete exact edge-crossing count over the \(152\) feasible joint masks is

| Dodecahedral section | Icosahedral section | Common chambers |
| ---: | ---: | ---: |
| 6 | 10 | 60 |
| 6 | 12 | 20 |
| 8 | 10 | 60 |
| 10 | 10 | 12 |

No other pair is feasible on an open chamber. On the ten-circle arrangement alone the exact classes are \((N_D,\text{chamber sides},\text{multiplicity})=(6,6,20),(8,3,60),(10,5,12)\), while the six-circle arrangement has \((N_I,\text{chamber sides},\text{multiplicity})=(12,3,20),(10,5,12)\). Because the common refinement has no new arrangement vertices and the \(60\) dodecahedral triangular and \(12\) pentagonal chambers remain single common chambers, precisely the \(20\) hexagonal chambers split into four triangles each. Their subdivision has one \(N_I=12\) triangle and three \(N_I=10\) triangles. The exact component counts, not a random sample, prove both this refinement assertion and the stated impossible pairings.

**3. Exact areas.** The small-circle arrangement computations in the same coordinate system give the following exterior turning-angle multisets, which may also be recovered by crossing the bounding planes at their exact cross products. Set \(\alpha=\arccos(\sqrt5/3)\) and \(\beta=\arccos(1/3)\). A dodecahedral six-section chamber is a spherical hexagon with three exterior turns \(\alpha\) and three \(\beta\). An eight-section chamber is a spherical triangle with two exterior turns \(\pi-\beta\) and one \(\pi-\alpha\). A ten-section chamber is a spherical pentagon with five exterior turns \(\beta\). The icosahedral twelve-section chamber is a spherical triangle with three exterior turns \(\pi-\theta\), where \(\theta=\arccos(1/\sqrt5)\). For a convex spherical polygon, Gauss–Bonnet gives its area as \(2\pi\) minus the sum of exterior turns. Hence the four relevant single-chamber areas are
\[
\Omega_{D,6}=2\pi-3(\alpha+\beta),\quad
\Omega_{D,8}=2\beta+\alpha-\pi,\quad
\Omega_{D,10}=2\pi-5\beta,\quad
\Omega_{I,12}=3\theta-\pi.
\]
Each class is a symmetry orbit with the multiplicities from Step 2. Consequently, the dodecahedral marginals are \(20\Omega_{D,6}/(4\pi)\), \(60\Omega_{D,8}/(4\pi)\), and \(12\Omega_{D,10}/(4\pi)\); the icosahedral twelve-section marginal is \(20\Omega_{I,12}/(4\pi)\). The refinement proves that its entire mass is paired with \(N_D=6\). Subtracting this mass from the dodecahedral six-section marginal and retaining the other two dodecahedral marginals produces the claimed joint matrix. This also proves that its entries sum to one.

## Verification

Run `python3 verify.py` using Python 3 with no third-party packages. The first output line must read `EXACT_DUAL_CHAMBER_ENUMERATION_OK`. The checker reconstructs both vertex sets and all \(60\) polyhedral edges, uses exact integer-pair arithmetic for \(\mathbb Z[\varphi]\), computes all projective great-circle intersections and Euler counts, and classifies the section side counts for every open chamber of the common refinement. It separately rebuilds the two marginal chamber counts, certifies every dodecahedral and icosahedral chamber’s exterior-turn cosine multiset by exact arithmetic, and evaluates the resulting four probability formulas. The analytic spherical-angle identities and the original coordinate definitions are explicitly given in the proof, so the attached code is a reproducible finite certificate for the sole combinatorial step, not a substitute for Gauss–Bonnet or a finite experiment extrapolated to arbitrary directions.

## Relationship to prior work

The classical ten-circle dodecahedral arrangement is explicitly recorded by *MathPages, N Points On Sphere all in One Hemisphere*: it has \(60\) triangles, \(20\) hexagons and \(12\) pentagons, with numerical area fractions. Neither the individual region counts nor those numerical fractions are claimed new here. The published *Exact Haar polygon-type law for central icosahedron sections* (published-finding corpus, 11 October 2026) already gives the standalone icosahedral two-point section law and its six-circle chamber classification. The older 31-great-circle icosahedral geometry, including its ten- and six-circle subfamilies, is also publicly described; such diagrams are relevant possible antecedents for the refinement incidence. Padrol–Pfeifle (2014) study polygonal sections and intersection complexity in a different optimization setting. De Loera–Lopez-Campos–Torres (2024) examine possible section vertex counts and their gaps, including the icosahedron, rather than a coupled random-direction law for dual Platonic bodies.

**The candidate contribution is specifically the joint incidence/refinement theorem and the resulting paired distribution.** Neither marginal by itself determines its coupling; the forbidden pairs and the exact partition of each hexagonal chamber require the additional common-refinement argument. Historical geometric diagrams might implicitly encode this incidence, and a definitive priority assertion is not made.

## Limitations

The result does not cover noncentral or independently oriented section planes, arbitrary icosahedral deformations, or the measure-zero directions that pass through vertices. The known one-body great-circle regions and the icosahedral marginal must not be mistaken for new results. Published spherical tessellations may contain equivalent drawings of the common sixteen-circle arrangement without naming the joint section-count implication; comprehensive historical-priority verification remains open. This is a proof and self-review, not independent mathematical certification.

## References

1. A. Padrol and J. Pfeifle, *Polygons as sections of higher-dimensional polytopes*, arXiv:1404.2443, first posted 9 April 2014, https://arxiv.org/abs/1404.2443.
2. *N Points On Sphere all in One Hemisphere*, MathPages, especially the ten-circle dodecahedral passage and area-fraction table, https://www.mathpages.com/home/kmath327/kmath327.htm (initial publication date not verified).
3. *Exact Haar polygon-type law for central icosahedron sections*, published-finding corpus, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
4. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419, first posted 17 December 2024, https://arxiv.org/abs/2412.12419.
5. *31 great circles of the spherical icosahedron*, background on the classical ten-, six-, and fifteen-circle subfamilies, https://en.wikipedia.org/wiki/31_great_circles_of_the_spherical_icosahedron.
