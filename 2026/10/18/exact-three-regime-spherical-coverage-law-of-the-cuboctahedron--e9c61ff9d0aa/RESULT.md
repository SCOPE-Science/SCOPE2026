# Exact three-regime spherical coverage law of the cuboctahedron

## Finding
Let \(V\subset S^2\) be the twelve vertex directions of a regular cuboctahedron,
\[
V=\frac1{\sqrt2}\{(\pm1,\pm1,0),(\pm1,0,\pm1),(0,\pm1,\pm1)\},
\]
with independent choices of signs. Let \(U\) be uniform in spherical area measure on \(S^2\), and define the nearest-site geodesic radius
\[
R=\min_{v\in V}\arccos(U\cdot v),\qquad F(t)=\Pr(R\le t).
\]
The complete distribution has exactly two internal positive thresholds,
\[
a=\frac\pi6,\qquad b=\arccos\sqrt{\frac23},\qquad c=\frac\pi4.
\]
For \(a<t\le c\), set
\[
\beta(t)=\arccos\!\left(\frac{\cot t}{\sqrt3}\right),\quad
\gamma(t)=\arccos\!\left(\frac{\tfrac12-\cos^2t}{\sin^2t}\right),\quad
\eta=\arccos\frac13.
\]
Define two nonnegative spherical-overlap areas on \([0,c]\):
\[
L(t)=\begin{cases}0,&0\le t\le a,\\2\pi-2\gamma(t)-4\beta(t)\cos t,&a<t\le c,\end{cases}
\]
\[
T(t)=\begin{cases}0,&0\le t\le b,\\2\pi-3\gamma(t)-3(2\beta(t)-\eta)\cos t,&b<t\le c.\end{cases}
\]
Then the *entire* probability law is
\[
\boxed{F(t)=6(1-\cos t)-\frac6\pi L(t)+\frac2\pi T(t)\quad(0\le t\le c),}
\]
with \(F(t)=0\) for \(t<0\), and \(F(t)=1\) for \(t\ge c\).

The transition at \(b\) is genuinely quadratic:
\[
\boxed{T(b+\varepsilon)=3\sqrt3\,\varepsilon^2+O(\varepsilon^3)\quad(\varepsilon\downarrow0).}
\]
The final uncovered fraction has the explicit two-term endpoint expansion
\[
\boxed{1-F(c-\varepsilon)=\frac6\pi\varepsilon^2+\frac2\pi\varepsilon^3+O(\varepsilon^4)\quad(\varepsilon\downarrow0).}
\]
In particular the exact spherical covering radius of this twelve-point arrangement is \(\pi/4\), and the three area-law regimes are disjoint caps, caps with pair overlaps, and caps with both pair and triple overlaps.

## Assumptions and scope
All distances are short great-circle distances on the unit sphere; \(U\) has Haar-uniform spherical area law. The twelve sites are fixed, not independently randomized, and their orientation is immaterial. Caps are closed, so distinctions on cap boundaries do not affect the probabilities. The expressions for \(\beta\) and \(\gamma\) are only used when \(t>a\), where their inverse-cosine arguments lie in \([-1,1]\). The \(O(\cdot)\) estimates concern the stated one-sided real limits, with absolute implied constants for this fixed configuration. No optimization over all possible twelve-site configurations is claimed.

## Proof
**1. Pair and triple incidence.** For distinct \(v,w\in V\), direct multiplication of the signed-permutation coordinates gives \(v\cdot w\in\{\tfrac12,0,-\tfrac12,-1\}\). Exactly 24 unordered pairs have inner product \(\tfrac12\), so their angular separation is \(\alpha=\pi/3\). All other pair separations are at least \(\pi/2\). The resulting adjacency graph is the cuboctahedral graph. It has exactly eight three-vertex cliques (the triangular faces) and no four-vertex clique. These counts also follow by fixing one vertex: four adjacent vertices form the link of an alternating triangle-square vertex; each of the 24 edges belongs to one of the eight triangles, and a clique of size four would require a triangular link.

For \(0\le t<c\), one has \(2t<\pi/2\). Intersecting caps must therefore have adjacent centers. Consequently all nonempty pair intersections are among the 24 edges; all possible triple intersections are among the eight triangular faces; no four caps can intersect. At \(t=c\), nonadjacent caps can only touch in a set of spherical area zero. Thus inclusion-exclusion for the union of all twelve radius-\(t\) caps terminates at triples throughout \([0,c]\), as an area identity.

For a face triangle with unit centers \(v_1,v_2,v_3\), their pairwise scalar products are \(1/2\) and \(\|v_1+v_2+v_3\|=\sqrt6\). If a point is in all three radius-\(t\) caps, then
\[
3\cos t\le U\cdot(v_1+v_2+v_3)\le\sqrt6.
\]
This requires \(t\ge b\). Equality occurs at the face-normal direction \((v_1+v_2+v_3)/\sqrt6\), while for \(t>b\) the intersection has positive spherical area. A neighboring pair of caps first meets when \(t=a=\alpha/2\).

**2. Exact pair and triple overlap areas.** Fix two adjacent cap centers at angular separation \(\alpha\). For \(t>a\), their radius-\(t\) boundary circles intersect in two points. Spherical cosine laws in the isosceles triangle with sides \(t,t,\alpha\) give its apex angle
\[
\gamma(t)=\arccos\frac{\cos\alpha-\cos^2t}{\sin^2t},
\]
and the half-angle subtended at a cap center,
\[
\beta(t)=\arccos\left(\tan\frac\alpha2\cot t\right).
\]
Each of the two lens-boundary arcs has central angle \(2\beta\). The exterior turning angle at each corner is \(\gamma\), while the total geodesic-curvature integral of the two arcs is \(4\beta\cos t\). Spherical Gauss--Bonnet therefore gives
\[
L=2\pi-2\gamma-4\beta\cos t.
\]

For three cap centers at the vertices of an equilateral spherical triangle with side \(\alpha\), the angle at a triangle vertex is \(\eta=\arccos(1/3)\) by the spherical cosine rule. For \(b<t\le c\), the boundary of the common intersection consists of three circular arcs, each subtending \(2\beta-\eta\) at its cap center. The three corner exterior angles are \(\gamma\). Another application of Gauss--Bonnet gives
\[
T=2\pi-3\gamma-3(2\beta-\eta)\cos t.
\]
At \(t=b\), \(2\beta(b)=\eta\) and \(\gamma(b)=2\pi/3\), so the latter expression tends to zero. Both formulas agree with the zero-overlap cases at their respective thresholds.

**3. Coverage and exact support.** Each individual cap has spherical area \(2\pi(1-\cos t)\). The adjacency and triple counts from Step 1, together with inclusion-exclusion, yield the union area
\[
12\,[2\pi(1-\cos t)]-24L(t)+8T(t).
\]
Dividing by total spherical area \(4\pi\) gives the displayed CDF.

To prove sharp coverage at \(c\), consider the spherical Voronoi cell of \(v=(1,1,0)/\sqrt2\). Comparison of \(U\cdot v\) with all eleven other site products shows that, writing \(U=(x,y,z)\), this cell is exactly
\[
\{(x,y,z)\in S^2:x\ge|z|,\ y\ge|z|\}.
\]
Within the cell, \(x,y\ge0\) and \(z^2\le\min(x^2,y^2)\le xy\); hence \((x+y)^2\ge x^2+y^2+z^2=1\). Thus \(U\cdot v=(x+y)/\sqrt2\ge1/\sqrt2\), meaning the nearest-site angle is at most \(c\). Equality occurs only at the two axial directions \((1,0,0)\) and \((0,1,0)\) in this cell. By symmetry all six coordinate axes realize \(R=c\). Therefore the covering radius is exactly \(c\), and the CDF equals one thereafter. No atom occurs at the endpoints because all individual exact-distance level sets have spherical area zero.

**4. First triple-overlap asymptotic.** At any one triangular face center \(p=(v_1+v_2+v_3)/\sqrt6\), each of the three site angles equals \(b\), and the three site directions projected onto the tangent plane have magnitude \(\sin b\) and pairwise angles \(120^\circ\). In geodesic normal coordinates \(x\) at \(p\), the three inequalities for radius \(b+\varepsilon\) are, uniformly for \(x=O(\varepsilon)\),
\[
\frac{v_i-(p\cdot v_i)p}{\sin b}\cdot x\ge-\varepsilon+O(\varepsilon^2),\qquad i=1,2,3.
\]
After setting \(x=\varepsilon y\), their limiting intersection is the equilateral Euclidean triangle of inradius one and area \(3\sqrt3\). Smooth Taylor expansion of the three arcs and of the spherical area Jacobian supplies the error \(O(\varepsilon^3)\). Hence the triple-overlap area is \(3\sqrt3\varepsilon^2+O(\varepsilon^3)\). Multiplication by the eight triples and division by \(4\pi\) shows that the correction to pairwise inclusion-exclusion begins with \(6\sqrt3\varepsilon^2/\pi\).

**5. Final uncovered-area asymptotic.** At radius \(c\), the six axial directions are the only points with nearest-site distance \(c\), by Step 3 and symmetry. For small \(\varepsilon>0\), the uncovered region therefore lies in six disjoint small neighborhoods. Near \(p=(1,0,0)\), the only constraints that can be active come from the four sites \((1,\pm1,0)/\sqrt2\) and \((1,0,\pm1)/\sqrt2\); every other site is strictly farther away there. Use spherical normal coordinates \(x=(x_1,x_2)\) at \(p\), with \(\rho=\|x\|\). A point remains outside all four radius-\((c-\varepsilon)\) caps precisely when
\[
\cos\rho+\frac{\sin\rho}{\rho}|x_j|<\cos\varepsilon+\sin\varepsilon,
\qquad j=1,2.
\]
Putting \(x=\varepsilon y\) and Taylor-expanding on the bounded region gives
\[
|y_j|<1+\frac\varepsilon2(\|y\|^2-1)+O(\varepsilon^2),\qquad j=1,2.
\]
The limiting hole is the square \([-1,1]^2\), of area four. On each side the first outward normal displacement is \(\tfrac\varepsilon2y_{\mathrm{tangent}}^2\). Integrating it along the four sides adds \(4\varepsilon/3\) to the rescaled area. Since the spherical normal-coordinate area Jacobian is \(1+O(\varepsilon^2)\), one hole has spherical area
\[
4\varepsilon^2+\frac43\varepsilon^3+O(\varepsilon^4).
\]
There are six congruent holes. Dividing their total area by \(4\pi\) proves the displayed two-term survival expansion.

## Verification
The standalone `check_cuboctahedral_cap_law.py` verifies all exact adjacency and triangle-clique counts directly from integer site coordinates and independently compares spherical-lens Gauss--Bonnet formulas with one-dimensional quadrature. It also compares the full CDF with a reproducible scrambled Sobol spherical sample of \(262144\) directions over ten radii, and checks both singular coefficients with 80-decimal-place arithmetic. Its successful output begins `CUBOCTAHEDRAL_SPHERICAL_CDF_OK`. The proof above is analytic; the finite checks do not establish global combinatorial or asymptotic identities by themselves.

The exact CDF values at the phase points are \(F(a)=6-3\sqrt3\), \(F(b)\approx0.94012099502993\), and \(F(c)=1\). The face normal is at angular distance \(b\) from its three closest sites. The six axial farthest-point directions have angular distance \(c\). These independently identifiable geometric landmarks provide boundary and normalization checks.

## Relationship to prior work
Fowler, Tarnai and Gáspár (2002) study maximum spherical-cap coverage among moving arrangements of antipodal pairs. At six pairs they use the optimized icosahedral configuration, not the fixed twelve cuboctahedral site directions. Their overlap-based coverage framework motivates the question, but their investigated optimizers and coverage plots do not give the stated cuboctahedral three-regime distribution or its endpoint coefficients.

Fowler, Tarnai and Kabai (2005), Sections 2--3, explicitly identify the twelve cuboctahedral vertex directions as a rigid packing of four equilateral-circle triplets with packing radius \(\pi/6\). Their result is about the largest **nonoverlapping** caps under the triplet constraint; it neither computes the coverage curve after that radius nor the triple-overlap or covering-endpoint laws. In particular, the packing threshold \(a\) and the site configuration are prior work, not newly claimed.

Kimberling (2011), Sections 7--9, sets up nearest-site spherical Voronoi regions and calculates mean nearest-vertex distances for the five Platonic solids. The present solid is Archimedean, has a nonregular four-sided spherical Voronoi cell, and the present claim is the complete CDF with two overlap transitions and local asymptotics, not a Platonic mean. Koay (2012) discusses computational antipodal spherical centroidal Voronoi tessellations; it does not evaluate this fixed twelve-site law.

A published 2026 note on third-order unions of caps centered on regular-simplex vertices also uses inclusion-exclusion at the onset of triple overlap. It concerns a different center Gram matrix (equally negative off-diagonal correlations in higher dimension) and does not determine the cuboctahedron's 24/8 incidence, Gauss--Bonnet lens and triangular areas, or six-square endpoint tails. The general technique of inclusion-exclusion and spherical Gauss--Bonnet is not claimed as novel.

## Limitations
This is a fixed-site probability law, not a proof of covering or packing optimality among twelve points. The cuboctahedral covering radius \(45^\circ\) exceeds the classical optimal twelve-point icosahedral value. No claim is made about all Archimedean solids, about nonuniform direction laws, or about first moments unless obtained by integrating this CDF. Historic sources not indexed or not accessible in full could potentially contain equivalent special cases; historical priority is not certified. Independent mathematical examination has not been performed.

## References
1. P. W. Fowler, T. Tarnai, Z. Gáspár, “From circle packing to covering on a sphere with antipodal constraints,” Proc. R. Soc. A 458 (2002), 2275–2287. DOI: 10.1098/rspa.2002.0990. Public online date: 24 July 2002.
2. C. Kimberling, “Mean distances on a sphere,” Elem. Math. 66 (2011), 63–73. DOI: 10.4171/EM/172, especially Sections 7–9.
3. P. W. Fowler, T. Tarnai, S. Kabai, “Packing regular triplets of circles on a sphere,” Proc. R. Soc. A 461 (2005), 2355–2367. DOI: 10.1098/rspa.2005.1464, especially Section 3(b).
4. S. Y. Koay, “Pseudometrically Constrained Centroidal Voronoi Tessellations,” arXiv:1211.7141 (2012).
5. “Exact third-order union formula at the first multiple-overlap threshold for simplex-centred spherical caps,” public research note (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-third-order-union-formula-at-the-first-multiple-overlap-th--e4ea7f0caeb7/RESULT.md.
