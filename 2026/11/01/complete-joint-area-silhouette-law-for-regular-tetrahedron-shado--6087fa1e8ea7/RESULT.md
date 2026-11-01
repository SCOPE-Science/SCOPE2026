# Complete joint area–silhouette law for regular-tetrahedron shadows
## Finding
Let \(T\subset\mathbb R^3\) be the regular tetrahedron with vertices
\[
(1,1,1),\quad(1,-1,-1),\quad(-1,1,-1),\quad(-1,-1,1),
\]
whose side length is \(2\sqrt2\). Let \(U\) be uniform on \(S^2\), and let \(A\) denote the Euclidean area of the orthogonal projection of \(T\) onto \(U^\perp\). Let \(N\in\{3,4\}\) denote the number of vertices of that projected polygon (generic directions only). This theorem determines the *complete joint law* of \((A,N)\), not merely the already-known marginal law of \(A\) or its first two conditional moments.

Set
\[
b_0=2\sqrt2,\qquad b_*=4\sqrt{\frac23},\qquad b_3=2\sqrt3,\qquad b_4=4.
\]
The finite nonnegative densities \(f_3,f_4\), defined by \(\Pr(A\in dt,N=j)=f_j(t)\,dt\), are exactly
\[
\boxed{f_3(t)=\begin{cases}
\displaystyle \frac2{\sqrt3}\left[1-\frac3\pi\arccos\!\left(\frac{t}{2\sqrt2\sqrt{12-t^2}}\right)\right],&b_0<t<b_*,\\[2mm]
\displaystyle\frac2{\sqrt3},&b_*\le t<b_3,\\
0,&\text{otherwise},
\end{cases}}
\]
\[
\boxed{f_4(t)=\begin{cases}
\displaystyle \frac34-\frac3\pi\arccos\!\left(\frac{t}{\sqrt2\sqrt{16-t^2}}\right),&b_0<t<b_*,\\[2mm]
\displaystyle\frac34,&b_*\le t<b_4,\\
0,&\text{otherwise}.
\end{cases}}
\]
Values at individual breakpoints do not affect these probability measures. In particular, **both joint densities are exactly constant on an overlapping interval of positive length**, giving the sharp constant posterior
\[
\boxed{\Pr(N=3\mid A=t)=\frac8{8+3\sqrt3}\quad\text{for almost every }b_*<t<b_3.}
\]
For \(b_3<t<b_4\), this posterior is zero. The three-vertex density has a downward jump at \(b_3\), whereas the four-vertex density continues uninterrupted. The joint law supplies a fully explicit area-only Bayesian silhouette classifier.

The masses and first area-weighted masses are
\[
\Pr(N=3)=\frac{2}{\pi}\left(\frac\pi2-3\arcsin\frac13\right),\qquad
\Pr(N=4)=1-\Pr(N=3),
\]
\[
\int t f_3(t)\,dt=\frac2{\sqrt3},\qquad
\int t f_4(t)\,dt=\frac4{\sqrt3}.
\]
The latter identities agree with earlier conditional-moment results; they are checks, not the new contribution.

## Assumptions and scope
The random plane is an orthogonal two-dimensional subspace chosen using Haar probability measure; choosing \(U\) uniformly on the sphere gives this law because \(U\) and \(-U\) define the same plane. The tetrahedron is regular, full-dimensional, and has the stated Euclidean normalization. The measure-zero orientations at which projected vertices coincide or become collinear are excluded from the combinatorial label. The formulas are joint **densities**, not conditional densities; the latter are obtained by dividing by the respective total silhouette probabilities. For a tetrahedron uniformly scaled by \(\lambda>0\), all area breakpoints scale by \(\lambda^2\) and each area density transforms by the reciprocal Jacobian \(\lambda^{-2}\).

## Proof
**1. A pointwise geometric dichotomy.** Cauchy's projection formula, using the four face normals of this tetrahedron, gives
\[
A(u)=|u_1+u_2+u_3|+|u_1-u_2-u_3|+|-u_1+u_2-u_3|+|-u_1-u_2+u_3|.
\]
Write \(a=\max_i|u_i|\) and \(s=\sum_i|u_i|\). Sorting the absolute coordinates and checking the two possible signs of \(a-(s-a)\) yields the *pointwise identity*
\[
\boxed{A(u)=\max\{2s,4a\}.}
\]
A projected tetrahedron has a triangular silhouette precisely when one vertex projects into the triangle of the other three. The normal then lies in the tangent cone at that vertex or its negative. In the first octant this is equivalent to \(2a<s\); its complement \(2a>s\) gives a quadrilateral. The boundary has spherical measure zero. These equivalences can also be checked by the signs of the four oriented face-normal dot products in the displayed Cauchy sum.

**2. Triangular silhouettes.** In the first octant, the region \(2a<s\) is the spherical equilateral triangle
\[
\mathcal T=\{u\in S^2:u_i\ge0,\quad u_i<u_j+u_k\text{ for all distinct }i,j,k\}.
\]
Its vertices are \((0,1,1)/\sqrt2\), \((1,0,1)/\sqrt2\), \((1,1,0)/\sqrt2\), and its spherical center is \(e=(1,1,1)/\sqrt3\). Its inradius is \(\delta=\arcsin(1/3)\), and its circumradius is \(\rho_*=\arccos\sqrt{2/3}\). With polar angle \(\rho\in[0,\rho_*]\) about \(e\), the area is \(A=2\sqrt3\cos\rho\).

For \(0<\rho\le\delta\), a full azimuthal circle lies in \(\mathcal T\), so the permitted azimuth measure is \(L_3(\rho)=2\pi\). For \(\delta<\rho<\rho_*\), the three disjoint excluded azimuth arcs have half-width \(\arccos(\tan\delta\cot\rho)\). Consequently,
\[
L_3(\rho)=2\pi-6\arccos\!\left(\frac{\cot\rho}{2\sqrt2}\right).
\]
The factor for all eight sign octants in Haar probability is \(8/(4\pi)\). The spherical area element \(\sin\rho\,d\rho\,d\varphi\) and \(|dt/d\rho|=2\sqrt3\sin\rho\) therefore give the joint density
\[
f_3(t)=\frac{L_3(\rho)}{\pi\sqrt3},\qquad t=2\sqrt3\cos\rho.
\]
Substitution of \(\cot\rho=t/\sqrt{12-t^2}\) establishes precisely the two nonzero branches of \(f_3\), including their break at \(t=2\sqrt3\cos\delta=4\sqrt{2/3}\). It also proves that the triangular support is \((2\sqrt2,2\sqrt3)\).

**3. Quadrilateral silhouettes.** The first octant consists of \(\mathcal T\) together with three disjoint (up to boundaries) regions such as
\[
\mathcal Q_x=\{u\in S^2:u_i\ge0,\quad u_1>u_2+u_3\}.
\]
Use polar angle \(\theta\) about the positive first coordinate axis and azimuth \(\varphi\in[0,\pi/2]\), so \(u_1=\cos\theta\), \(u_2=\sin\theta\cos\varphi\), \(u_3=\sin\theta\sin\varphi\). The cone condition becomes
\[
\cot\theta>\cos\varphi+\sin\varphi.
\]
The cone is empty for \(\theta\ge\pi/4\). For \(\theta\le\arctan(1/\sqrt2)\), its entire first-quadrant azimuth interval is allowed, giving \(L_4(\theta)=\pi/2\). For larger \(\theta<\pi/4\), the allowed azimuthal measure is
\[
L_4(\theta)=\frac\pi2-2\arccos\!\left(\frac{\cot\theta}{\sqrt2}\right).
\]
Here \(A=4\cos\theta\). There are three such cones in each of eight octants; multiplying their spherical measure by \(24/(4\pi)\) and changing variables using \(|dt/d\theta|=4\sin\theta\) yields
\[
f_4(t)=\frac{3}{2\pi}L_4(\theta),\qquad t=4\cos\theta.
\]
Substituting \(\cot\theta=t/\sqrt{16-t^2}\) proves the two nonzero branches of \(f_4\), including the same transition \(b_*\). The quadrilateral area support is \((2\sqrt2,4)\). The two cone families partition the sphere up to null boundaries, so no mass is omitted.

**4. Posterior plateau and normalization.** On \(b_*<t<b_3\), both computed densities are constants, \(2/\sqrt3\) and \(3/4\), so Bayes' formula gives \(8/(8+3\sqrt3)\). Above \(b_3\), the triangular density vanishes. Each of the four spherical vertex cones has area \(\Omega=\pi/2-3\arcsin(1/3)\). Counting both signs gives \(\Pr(N=3)=2\Omega/\pi\), while the complement has probability \(1-2\Omega/\pi\). The area-weighted integrals are \(2/\sqrt3\) and \(4/\sqrt3\), respectively, as can be found either by the preceding one-dimensional densities or by integrating the linear area formulas over the cones. This completes a normalized joint probability law on all generic viewing directions.

## Verification
The standalone `verify.py` independently reconstructs projected convex hulls for 2,500 Haar directions using two-dimensional hull geometry and confirms **both** the predicted vertex count and the area identity, to floating-point tolerance. It integrates the derived densities piecewise to check their total masses, first moments, and second moments against independent published formulas. It checks the intermediate constant posterior and the known 2001 unconditional-density plateaus after converting from the present edge-length normalization to unit edge length. Finally, 450,000 additional random spherical directions check the silhouette probabilities, conditional area means and constant posterior in the overlap band. Executing `python verify.py` with `numpy` and `scipy` installed prints `ALL_TETRAHEDRAL_JOINT_AREA_SILHOUETTE_CHECKS_PASSED`.

The numerical experiment is finite and cannot establish the joint density for all area values; that conclusion is proved by the exact spherical-geometry and change-of-variables calculations above.

## Relationship to prior work
Vickers and Brown (2001) already derived the **unconditional** density \(f_3+f_4\) of projected area of a unit-edge regular tetrahedron; its three scalar branches, including the constant middle and upper branches, are known. Their Appendix B describes viewing-sphere contours and briefly discusses cap intersections, but does not give the *separate* densities indexed by triangle-versus-quadrilateral silhouette or their Bayes posterior. The unconditional density cannot by itself recover the joint density; the cone partition is an additional calculation. This full marginal is explicitly prior work, not a newly discovered probability law.

Finch (2012) independently records unconditional area moments and triangle/quadrilateral probabilities for tetrahedral shadows. The published *Area-weighted silhouette probabilities of arbitrary tetrahedra* (2026) already gives first and second **conditional area moments**, for all tetrahedra, which this result specializes but does not extend at those moment orders. A finite collection of conditional moments does not imply a complete conditional density; the present novelty is the regular-tetrahedron **all-threshold joint law** and its positive-length constant-posterior interval.

Feldman and Klain (2008) derive silhouette probabilities from solid angles, explaining the known normalization. Black and Criado (2024) study expected combinatorial complexity of random two-dimensional shadows of fixed polytopes, not simultaneous metric-area and discrete-silhouette distributions. None of those inspected source statements implies the two separate densities or the nontrivial posterior plateau without an additional, type-resolved spherical calculation.

## Limitations
The theorem is specialized to orthogonal planar shadows of an exactly regular Euclidean tetrahedron under Haar-uniform orientations. It does not give a corresponding joint density for arbitrary asymmetric tetrahedra or nonuniform orientations, nor does it classify other geometric observables such as perimeter. A precise constant posterior holds only inside the stated open area interval, not over all areas. Older viewing-sphere calculations may implicitly contain a route to these formulas, so historical originality is provisional. No independent mathematical audit has been performed.

## References
1. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1 (11 June 2024), introduction and Theorem 1.1, original full text at https://arxiv.org/html/2406.06936v1.
2. G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, Proc. R. Soc. Lond. A 457 (2001), 283–306, DOI 10.1098/rspa.2000.0667, especially section 3(c)(ii), figure 8, and Appendix B. Full-text copy: https://citeseerx.ist.psu.edu/document?doi=f14600ad2bde247cc61c2b0b88946e263860590d&repid=rep1&type=pdf.
3. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (12 March 2012), section 2.1 and section 5, https://arxiv.org/html/1203.2464v1.
4. D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459v1 (19 September 2008), Theorem 1, https://arxiv.org/abs/0809.3459.
5. *Area-weighted silhouette probabilities of arbitrary tetrahedra* (2026), publicly available result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-area-weighted-silhouette-probabilities-of-arbitrary-tetrahedra--ddfd7f3eeb66.
