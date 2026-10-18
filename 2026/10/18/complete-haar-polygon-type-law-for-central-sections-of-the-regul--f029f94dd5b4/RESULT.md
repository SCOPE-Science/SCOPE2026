# Complete Haar polygon-type law for central sections of the regular truncated octahedron

## Finding
For the regular truncated octahedron
\[
K=[-2,2]^3\cap\left\{(x_1,x_2,x_3)\in\mathbb R^3:\sum_{j=1}^3|x_j|\le3\right\},
\]
choose \(U\) uniformly on the unit sphere \(S^2\), and let \(N\) be the number of vertices of the central planar section \(K\cap U^\perp\). Define
\[
\theta=\arccos\frac45,\qquad
D=11+3\sqrt{14}+4\sqrt6+2\sqrt{21},\qquad
q=\frac{24}{\pi}\arctan\frac1D.
\]
**Theorem (complete exact law).** With probability one, \(N\in\{6,8,10\}\). Its exact distribution is
\[
\boxed{\begin{aligned}
\Pr(N=6)&=4+q-\frac{18\theta}{\pi},\\
\Pr(N=8)&=\frac{18\theta}{\pi}-3-2q,\\
\Pr(N=10)&=q.
\end{aligned}}
\]
Equivalently, the probabilities are approximately \(0.498450689917704\), \(0.316108855580191\), and \(0.185440454502106\). In particular, the exact mean is
\[
\boxed{\mathbb E N=\frac{36}{\pi}\arccos\frac45
=7.373979529168805\ldots .}
\]
The decagonal-section event is exactly one open spherical triangle in each of the \(48\) signed-coordinate-permutation sectors. These probabilities are intrinsic under uniform scaling of the polytope.

## Assumptions and scope
The convex body \(K\) is the centered uniform Archimedean truncated octahedron: its \(24\) vertices are precisely the signed coordinate permutations of \((2,1,0)\), its \(36\) edges have length \(\sqrt2\), and its facets are six squares and eight regular hexagons. The sampling law is the rotation-invariant (Haar) probability on **planes through the origin**, induced by the uniform normal \(U\in S^2\). The two normals \(U\) and \(-U\) define the same plane. The finitely many great-circle conditions where the section passes through a vertex or has an otherwise exceptional face incidence have spherical measure zero. Polygon types are counted by edges or vertices, not by Euclidean regularity. Translated planes, affine images of the body, and non-Haar sampling are not included.

## Proof
**1. The facet-incidence formula.** Work away from the exceptional great circles. Sign changes and coordinate permutations allow the normal to be represented by positive coordinates \(x>y>z>0\). The section of a convex polytope by a transverse plane is a polygon whose edges arise bijectively from the facets the plane meets in their relative interiors. The six square facets of \(K\) are at coordinate levels \(\pm2\); the eight hexagonal facets lie in the planes \(\sigma_1x_1+\sigma_2x_2+\sigma_3x_3=3\), with \(\sigma_j\in\{-1,1\}\).

The two square facets perpendicular to the smallest coordinate axis are cut exactly if \(x>2z\): on each square face, the extreme plane-functional values are \(\pm2z\pm x\). Similarly, the square facets perpendicular to the middle axis are cut exactly if \(x>2y\), while neither square facet perpendicular to the largest axis is cut, because \(2x>y\). Thus the number of cut square facets is
\[
2\mathbf1_{x>2z}+2\mathbf1_{x>2y}.
\]
The hexagonal facets with all signs equal do not meet the central plane. Of the remaining three antipodal facet pairs, the two sign patterns having a negative sign on the largest or middle coordinate always intersect. The remaining antipodal pair, whose prototype has signs \((+,+,-)\), intersects exactly when \(y<2z\): over that hexagonal face, the minimal value of the plane functional occurs at its vertex \((0,1,-2)\), giving \(y-2z\), whereas the maximum is positive. Consequently the complete generic side-count formula is
\[
\boxed{N=4+2\mathbf1_{y<2z}+2\mathbf1_{x>2z}+2\mathbf1_{x>2y}.}\tag{1}
\]
Because \(x>y>z\), if \(y>2z\) then \(x>2z\). Applying this implication to (1) gives precisely \(N\in\{6,8,10\}\), and \(N=10\) holds exactly when
\[
\boxed{x>2y\quad\hbox{and}\quad y<2z.}\tag{2}
\]
Indeed both inequalities in (2) force \(x>2z\), so all four optional square facets meet along with all six optional hex facets.

**2. The exact decagonal probability.** The normal sphere splits into \(48\) congruent sectors determined by a choice of coordinate signs and a strict order of absolute coordinate values. One sector is
\[
\mathcal C=\{(x,y,z):x>y>z>0\}\cap S^2,
\qquad \operatorname{area}(\mathcal C)=\frac{4\pi}{48}=\frac\pi{12}.
\]
Inside this sector, (2) is the interior of the simplicial cone with extremal rays
\[
X=(1,0,0),\qquad R=(4,2,1),\qquad Q=(2,1,1).
\]
The ray \(R\) simultaneously satisfies \(x=2y\) and \(y=2z\); the ray \(Q\) satisfies \(x=2y\) and \(y=z\); and \(X\) is the common limit as \(y,z\to0\). These are exactly the three boundary intersections in the ordered cone, so no additional components exist.

For the spherical triangle subtended by noncoplanar rays \(a,b,c\), the classical solid-angle identity gives
\[
\Omega(a,b,c)=2\arctan\!\frac{|\det(a,b,c)|}{\|a\|\|b\|\|c\|+(a\cdot b)\|c\|+(b\cdot c)\|a\|+(c\cdot a)\|b\|},
\]
provided the denominator is positive. Here \(|\det(X,R,Q)|=1\), \(\|R\|=\sqrt{21}\), \(\|Q\|=\sqrt6\), and the pairwise products are \(4,11,2\). Therefore
\[
\Omega(X,R,Q)=2\arctan\frac1{11+3\sqrt{14}+4\sqrt6+2\sqrt{21}}.
\]
The triangle occupies the same fraction of every signed-permutation sector. Dividing by the sector area \(\pi/12\) yields \(\Pr(N=10)=24\arctan(1/D)/\pi=q\).

**3. The exact expectation by counting crossed edges.** The generic central section has one vertex for every original edge whose endpoints lie strictly on opposite sides of the section plane. For fixed nonzero vectors \(v,w\), the fraction of uniform sphere normals for which \((U\cdot v)(U\cdot w)<0\) is the angle between \(v,w\), divided by \(\pi\). This follows by measuring the corresponding symmetric spherical lune (equivalently, by restricting to the great-circle coordinates in their span). All \(36\) edges have endpoints on the sphere of radius \(\sqrt5\), have squared length \(2\), and hence have dot product \((5+5-2)/2=4\). Their common subtended angle is \(\theta=\arccos(4/5)\). Summing the \(36\) crossing indicators gives exactly
\[
\mathbb EN=\frac{36\theta}{\pi}.
\]

**4. Recover the remaining probabilities without unproved chamber integrations.** Write \(p_j=\Pr(N=j)\). Step 1 gives \(p_6+p_8+p_{10}=1\), while step 3 gives \(6p_6+8p_8+10p_{10}=36\theta/\pi\). Step 2 supplies \(p_{10}=q\). Solving these two independent linear equations gives \(p_6=4+q-18\theta/\pi\) and \(p_8=18\theta/\pi-3-2q\). No finite-grid approximation or unverified enumeration is used to deduce any probability. This completes the proof.

## Verification
Run `python3 verify.py` with Python 3 and its standard library only. It constructs all \(24\) signed-permutation vertices and all \(36\) edges with exact integer arithmetic, checks that each edge has squared length \(2\) and endpoint dot product \(4\), and tests equation (1) by direct crossed-edge counting at \(9,983\) generic integer-normal configurations. It checks an independent six-triangle triangulation of the ordered spherical sector, confirms that all solid-angle pieces add to \(\pi/12\), computes their independent probabilities, and compares each with the theorem. A separate seeded test samples \(200,000\) Gaussian normal vectors and independently counts edge crossings, observing empirical frequencies approximately \(0.498580\), \(0.315910\), and \(0.185510\) for the three polygon types. The script reports `VERIFY_OK` upon success. These finite computational checks corroborate the proof but do not substitute for the universal facet, spherical-cone, and expectation arguments.

## Relationship to prior work
Lonke's *On random sections of the cube* [1] analyzes the Haar expected face numbers of cube sections and provides established context for central-section incidence methods. Its full primary text concerns cubes and higher-dimensional cube sections, not the regular truncated octahedron's complete three-point polygon-type law. Agarwal and Escobedo [2] study assemblies and phase behaviour of several space-filling polyhedra including the regular truncated octahedron, motivating the body as a natural test geometry; that work does not calculate this central-section distribution. Paul [3] discusses simulated random cuts of truncated octahedra and distribution curves of sectional **areas**, so it is the most relevant object-level precedent; the accessible abstract does not establish an exact Haar central polygon-type law, but its unavailable full text leaves a genuine priority risk. The solid-angle identity [4] is classical and used as a computational ingredient, not claimed as a discovery. Other inspected research on blocking configurations and maximal inscribed tetrahedra for the same polytope concerns distinct invariants. In particular, optimization of tetrahedral determinants over the truncated octahedron does not determine the face-incidence probabilities of its randomly oriented planar sections. These comparisons do not establish absolute historical priority.

## Limitations
The statement is specific to one exact uniform three-dimensional truncated octahedron and to Haar-random **center-passing** planes. It neither covers arbitrary aspect ratios of a truncated octahedron nor translated random planes, random chord lengths, section areas, or higher-dimensional analogues. The mathematical probability identities are proved, but the classical solid-angle formula is invoked from [4], and the historical-priority check cannot exclude an unindexed prior table or a result within an inaccessible old stereology article [3]. Numerical experiments are corroborative and have no authority as proofs of measure identities. No independent mathematical audit or expert verification is asserted.

## References
1. Y. Lonke, *On random sections of the cube*, arXiv:math/9812123, initially submitted 21 December 1998; https://arxiv.org/html/math/9812123v1 .
2. U. Agarwal and F. A. Escobedo, *Mesophase behaviour of polyhedral particles*, *Nature Materials* 10 (2011), 230–235; published online 13 February 2011; DOI: 10.1038/nmat2959.
3. J. Lawrence Paul, *Distribution curves of sectional areas through some families of convex particles*, *Journal of Microscopy* 122 (1981), 165–172; DOI: 10.1111/j.1365-2818.1981.tb01255.x (full text not obtained).
4. A. van Oosterom and J. Strackee, *The solid angle of a plane triangle*, *IEEE Transactions on Biomedical Engineering* 30 (1983), 125–126; DOI: 10.1109/TBME.1983.325207.
