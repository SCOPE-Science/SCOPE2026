# Exact inradius law for random planar projections of the regular octahedron

## Finding
Let \(O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\subset\mathbb R^3\) be the unit regular octahedron, and let \(E\) be an unoriented two-plane drawn from Haar probability measure on \(\operatorname{Gr}(2,3)\). Write \(\rho(E)\) for the Euclidean inradius of the orthogonal projection \(P_E O\), measured within \(E\). For \(0\le s\le1\), define
\[
G(s)=\mathbb P\!\left\{\rho(E)\ge\frac1{\sqrt{2+s^2}}\right\}.
\]
The following elementary *exact* distribution formula holds:
\[
\boxed{G(s)=\frac{24}{\pi}\left[\arctan\frac{s^2}{D_1(s)}+\arctan\frac{s^2}{D_2(s)}\right]},
\]
where
\[
\begin{aligned}
D_1(s)&=(1+\sqrt{1+s^2})\sqrt{4+2s^2}+2+s^2+2\sqrt{1+s^2},\\
D_2(s)&=\sqrt{3(3-2s+s^2)(3+2s+s^2)}\\
&\quad +(3-s)\sqrt{3+2s+s^2}+(3+s)\sqrt{3-2s+s^2}+3\sqrt3.
\end{aligned}
\]
In particular \(\rho(E)\in[1/\sqrt3,1/\sqrt2]\) almost surely, the distribution has no atoms, \(G(0)=0\), and \(G(1)=1\). This gives the usual cumulative distribution of \(\rho\): for \(1/\sqrt3\le t\le1/\sqrt2\),
\[
\mathbb P\{\rho(E)\le t\}=1-G\!\left(\sqrt{t^{-2}-2}\right).
\]
Below or above this support interval the cumulative distribution is \(0\) or \(1\), respectively. Boundary inequalities can be interchanged because the directions of equality have spherical measure zero.

## Assumptions and scope
The ambient metric and orthogonal projection are Euclidean. The six vertices of \(O\) are exactly the unit coordinate vectors and their negatives; no rotation, scaling, or change of reference measure is implicit. Haar measure on planes means the distribution induced by the normal plane \(E=u^\perp\) with \(u\) uniform on \(S^2\), where \(u\) and \(-u\) represent the same plane. The inradius is the radius of the largest translated disk in the projected polygon, not its minimum width or its area-equivalent radius. Central symmetry implies that a largest inscribed disk can be centered at the origin.

## Proof
**1. Polar reduction.** The polar of \(O\) is the cube \(C=[-1,1]^3\). For every plane \(E\), polarity inside \(E\) gives \((P_E O)^\circ=C\cap E\). If a disk \(B_E(z,r)\) lies inside the origin-symmetric polygon \(P_E O\), symmetry also gives \(B_E(-z,r)\); averaging shows \(B_E(0,r)\subset P_E O\). Consequently
\[
\rho(E)^{-1}=R(E),\qquad R(E)=\max\{\|x\|_2:x\in C\cap E\}.
\]

**2. Exact cube-section circumradius.** Write the absolute values of the three components of a nonzero normal \(u\) in decreasing order \(a\ge b\ge c\ge0\), with \(a>0\). Coordinate sign changes and permutations leave \(R\) unchanged. Every vertex of the polygon \(C\cap u^\perp\) has at least two coordinates in \(\{-1,1\}\). If \(a\ge b+c\), the only feasible choice of free coordinate at a section vertex away from boundary degeneracies is the coordinate associated with \(a\); the largest possible remaining absolute coordinate is \((b+c)/a\). Hence \(R^2=2+((b+c)/a)^2\).

If \(a\le b+c\), a feasible section vertex with free coordinate \(a\) has remaining magnitude at most \((b-c)/a\); with free coordinate \(b\), the largest is \((a-c)/b\); with free coordinate \(c\), the largest is \((a-b)/c\). The comparisons
\[
\begin{aligned}
 a(a-c)-b(b-c)&=(a-b)(a+b-c)\ge0,\\
 c(a-c)-b(a-b)&=(b-c)(b+c-a)\ge0
\end{aligned}
\]
show that \((a-c)/b\) is largest in the second regime. Zero coordinates and transition normals follow by continuity, and the result is therefore
\[
R(u)^2=2+\begin{cases}
\bigl((b+c)/a\bigr)^2,&a\ge b+c,\\
\bigl((a-c)/b\bigr)^2,&a\le b+c.
\end{cases}
\]
Both formulas agree when \(a=b+c\). Each displayed ratio lies in \([0,1]\), proving the support interval. The normalization of \(u\) does not enter this ratio.

**3. Two exact cones for the distribution.** For \(0\le s\le1\), the condition \(R^2\le2+s^2\) in the positive sorted chamber \(a\ge b\ge c\ge0\) is the union, up to shared measure-zero boundaries, of the following simplicial cones:
\[
\begin{aligned}
C_1(s)&=\{(a,b,c):a\ge b\ge c\ge0,\ b+c\le sa\},\\
C_2(s)&=\{(a,b,c):a\ge b\ge c\ge0,\ a-c\le sb\}.
\end{aligned}
\]
Indeed the first inequality automatically implies \(a\ge b+c\), and the second implies \(a\le b+c\) because \(s\le1\). Their spanning rays, in their \((a,b,c)\) coordinates, are respectively
\[
\begin{aligned}
U_1(s)&=((1,0,0),(1,s,0),(2,s,s)),\\
U_2(s)&=((1,1,1-s),(1,1,1),(1+s,1,1)).
\end{aligned}
\]
The first description follows by normalizing \(a=1\) and triangulating \(0\le c\le b\), \(b+c\le s\); the second follows by normalizing \(b=1\) and triangulating \(1\le a\le1+s\), \(a-s\le c\le1\). These identities also hold at the degenerate endpoints by continuity.

**4. Spherical solid angles.** The sphere is partitioned, modulo great-circle boundaries, into \(48\) congruent coordinate sign-and-order chambers. For rays \(v,w,z\in\mathbb R^3\) spanning a pointed simplicial cone whose dot-product denominator below is positive, its solid angle in steradians is the standard spherical triangle identity
\[
\Omega(v,w,z)=2\arctan\!\left(
\frac{|\det(v,w,z)|}{\|v\|\|w\|\|z\|+(v\cdot w)\|z\|+(w\cdot z)\|v\|+(z\cdot v)\|w\|}
\right).
\]
For both triples \(U_i(s)\), the absolute determinant is exactly \(s^2\). Evaluating the norms and dot products gives their respective denominators \(D_1(s)\) and \(D_2(s)\) displayed above; both are strictly positive for \(0\le s\le1\). Each chamber has probability factor \(1/(4\pi)\) times solid angle. Thus
\[
G(s)=\frac{48}{4\pi}(\Omega(U_1(s))+\Omega(U_2(s)))
=\frac{24}{\pi}\left[\arctan\frac{s^2}{D_1(s)}+\arctan\frac{s^2}{D_2(s)}\right].
\]
This is exactly the asserted law. At \(s=1\), the two cones partition the full sorted chamber, giving \(G(1)=1\); at \(s=0\), both have zero spherical area, giving \(G(0)=0\). The same construction shows absence of atoms because each strict level-set boundary lies on finitely many smooth conic curves, which have spherical area zero. \(\square\)

## Verification
Run `python3 verify.py` from the accompanying directory. The self-contained standard-library script checks \(1329\) integer-parameter central cube sections with exact rational arithmetic; independently constructs and analyzes \(500\) planar convex hull projections; checks the two cone determinants, the endpoints, monotonicity and selected explicit probability values; and compares the analytic distribution with \(80000\) seeded Haar-normal samples. It prints `VERIFY_OK` if all checks succeed. Only the analytic proof establishes the continuum statement, and simulation is not used as a novelty or completeness argument.

## Relationship to prior work
Abas, *Width Laws and Spectral Geometry* (2026), develops exact distributions and reconstruction from random *widths* of boxes and zonotopes and proves a great-circle incidence formula for zonotopal width densities. Its primary class is 52A22. The present invariant is instead the inradius of a *randomly projected polar body*; it is the inverse of a nonlinear maximal norm on cube sections, not a scalar width, and does not follow from the cited linear width-law theorem. Böröczky and Henk (1997) study face numbers of projected regular crosspolytopes and, for the three-dimensional octahedron, give the exact probability that its planar projection has six vertices. A face-count law does not determine the inradius distribution. The 2026 preprint of Guédon, Litvak, Tatarko and Vritsiou treats upper and lower probabilistic bounds for diameters of random sections, including applications to \(p\)-ellipsoids; no assertion that its full text lacks an exact special-case formula is made because the full text could not be accessed. The present elementary law resolves the finite-dimensional, fully normalized distribution for this one particular regular polytope, without asserting a general random-section theorem.

## Limitations
The formula applies specifically to Haar-uniform orthogonal planar projections of the three-dimensional regular octahedron at the stated unit normalization. It is not a formula for arbitrary centrally symmetric bodies, other ambient dimensions, or non-Haar projection distributions. A highly relevant 2026 random-section-diameter manuscript could be checked at the abstract level but not inspected in full; a presently unrecognized equivalent special case or unpublished calculation remains a residual originality risk. The spherical solid-angle identity is classical; the combination with the two cube-section regimes is the result here.

## References
1. O. Abas, *Width Laws and Spectral Geometry*, arXiv:2608.06348v1, posted 6 August 2026, https://arxiv.org/abs/2608.06348; lawful full text at https://www.researchgate.net/publication/411823813_Width_Laws_and_Spectral_Geometry.
2. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, Preprint SC-97-21, 1997, author manuscript at https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf.
3. O. Guédon, A. E. Litvak, K. Tatarko, and B.-H. Vritsiou, *On Random Diameters of Convex Bodies*, arXiv:2609.24131v1, posted 21 September 2026, https://arxiv.org/abs/2609.24131 (abstract inspected; full manuscript inaccessible during comparison).
4. A. van Oosterom and J. Strackee, *The Solid Angle of a Plane Triangle*, IEEE Trans. Biomed. Eng. 30 (1983), 125–126, DOI:10.1109/TBME.1983.325207 (classical solid-angle identity).
