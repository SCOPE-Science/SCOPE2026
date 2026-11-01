# Exact directional-width distribution and sharp critical laws of the regular icosahedron
## Finding
Let \(I\subset\mathbb R^3\) be a regular icosahedron of circumradius \(1\), centered at the origin. If \(U\) is uniform on \(S^2\), write \(W=h_I(U)+h_I(-U)\) for its directional width. Define
\[
c=1/\sqrt5,\quad r=\arccos\sqrt{(1+c)/2},\quad \rho=\arccos\sqrt{(1+2c)/3},\quad w_0=2\cos r,\quad w_-=2\cos\rho.
\]
For \(r\le\theta\le\rho\) put
\[
S(\theta)=2\left[\arccos\left(\frac{\sin r}{\sin\theta}\right)-\cos\theta\,\arccos\left(\frac{\tan r}{\tan\theta}\right)\right].
\]
Then the **entire** cumulative distribution \(F(w)=\Pr(W\le w)\) is
\[
F(w)=\begin{cases}
0,&w\le w_-,\\
3w-5+\dfrac{15}{\pi}S(\arccos(w/2)),&w_-<w<w_0,\\
3w-5,&w_0\le w\le2,\\
1,&w\ge2.
\end{cases}
\]
The numerical thresholds are \(w_-\approx1.589308944584\) and \(w_0\approx1.701301616704\). The upper branch is exactly linear; at the unique interior formula transition it has the sharp one-sided correction
\[
F(w)-(3w-5)\sim\frac{10}{\pi\sin r\sqrt{\cos r}}(w_0-w)^{3/2}\qquad(w\uparrow w_0).
\]
At the lower endpoint,
\[
F(w)\sim\frac{15\sqrt3}{4\pi\sin^2\rho}(w-w_-)^2\qquad(w\downarrow w_-).
\]
These are claims about a fixed three-dimensional Euclidean icosahedron and invariant random *directions*, not random line chords.
## Assumptions and scope
For \(\varphi=(1+\sqrt5)/2\), the vertex set is the twelve permutations of the coordinate patterns \((0,\pm1,\pm\varphi)\), \((\pm1,\pm\varphi,0)\), and \((\pm\varphi,0,\pm1)\), divided by \(\sqrt{1+\varphi^2}\). Opposite vertices are paired, and adjacent vertex dot products equal \(c=1/\sqrt5\). Uniform directions mean normalized surface-area measure \(d\sigma/(4\pi)\) on \(S^2\). The circumradius-one edge length is \(\sqrt{2-2/\sqrt5}\); unit-edge distributions follow by rescaling widths by its reciprocal.
## Proof
**Normal-cell geometry.** Since \(I=-I\), \(W(u)=2\max_{v\in V(I)}u\cdot v\). With every vertex on \(S^2\), this is \(2\cos d_{S^2}(u,V(I))\). Its nearest-vertex spherical Voronoi decomposition has twelve congruent regular spherical pentagons \(C\), each centered at a vertex and of area \(4\pi/12=\pi/3\). There are five adjacent vertices at spherical distance \(\alpha=\arccos c\), and each Voronoi bounding great circle is equidistant from the center and one adjacent vertex. Its radial distance is \(r=\alpha/2\). The Voronoi vertices are spherical circumcenters of triangular icosahedron faces, at distance \(\rho\): the normalized sum of three mutually \(c\)-correlated unit face vertices has dot product \(\sqrt{(1+2c)/3}\) with each. Thus \(r\) and \(\rho\) are exactly the minimum and maximum radial distances to the pentagonal boundary.

**Full spherical distribution.** Let \(A(\theta)\) be the area of \(C\cap B_{S^2}(v,\theta)\), where \(v\) is its center. Since the twelve cells tile the sphere up to measure-zero boundaries, \(F(2\cos\theta)=1-3A(\theta)/\pi\). For \(\theta\le r\), the full cap fits, so \(A(\theta)=2\pi(1-\cos\theta)\), yielding \(F(w)=3w-5\). For \(\theta\ge\rho\), the whole cell fits and \(F=0\). For \(r<\theta<\rho\), the cap crosses five sides. Any point violating two side halfspaces has polar radius at least \(\arctan(\tan r/\cos(\pi/5))=\rho\) (the nearest pair consists of adjacent sides with azimuthal separation \(2\pi/5\)); nonadjacent pairs require an even larger radius. Consequently the five outside-side pieces do not overlap in the open range, and \(A(\theta)=2\pi(1-\cos\theta)-5S(\theta)\).

To evaluate a piece \(S\), take azimuth zero toward the midpoint of a Voronoi side. At polar angle \(t>r\), the offending azimuth interval has length \(2\arccos(\tan r/\tan t)\). Therefore
\[
S(\theta)=2\int_r^\theta \sin t\,\arccos\left(\frac{\tan r}{\tan t}\right)dt.
\]
Integrating by parts (or differentiating the stated arccosine formula, with its zero boundary at \(t=r\)) gives exactly the displayed \(S\). Substitution yields the complete CDF, including all endpoint and transition values.

**Critical exponents.** As \(\theta\downarrow r\), the integrand above is \(2\sqrt{2\tan r}\,(\theta-r)^{1/2}+O((\theta-r)^{3/2})\); hence \(S(\theta)=(4/3)\sqrt{2\tan r}(\theta-r)^{3/2}+O((\theta-r)^{5/2})\). Since \(w_0-w\sim2\sin r(\theta-r)\), the stated coefficient and exponent follow. At \(\theta=\rho\), five Voronoi corners attain the maximal radius. Three cells meet at each such vertex, so the spherical pentagon has interior angle \(2\pi/3\). Along either incident edge the radial distance falls at first order with slope \(1/2\) per unit tangent distance. The area in one corner with radial deficit at most \(\delta\) is \(\sqrt3\delta^2+o(\delta^2)\), by the tangent parallelogram Jacobian \(\sin(2\pi/3)\) and the triangle \(s+t\le2\delta\). Summing five corners per cell and twelve cells gives \(F(2\cos(\rho-\delta))=15\sqrt3\delta^2/\pi+o(\delta^2)\); conversion via \(w-w_-\sim2\sin\rho\,\delta\) proves the lower-endpoint coefficient.
## Verification
The standalone `verify.py` constructs all twelve circumradius-one vertices, checks adjacent dot products, samples the *actual width* \(2\max_vU\cdot v\) with one million deterministic low-discrepancy sphere directions, and checks eight CDF thresholds, support limits, transition continuity, and the critical \(3/2\) coefficient. Deterministic quadrature of \(F\) reproduces the previously known mean and second moment of the unit-edge icosahedron. These numerical checks are independent diagnostics, not infinite proofs; the spherical-area calculation above supplies the exact argument.
## Relationship to prior work
Finch (2011, first public arXiv version) introduced systematic regular-polyhedron width moments, concentrating on the tetrahedron and cube; his full paper does not evaluate the icosahedral CDF. Kabluchko, Litvak and Zaporozhets (2015) provided general mean-width and moment frameworks, not this complete elementary distribution. A published Platonic-solid calculation gives the exact **second moment** for the icosahedron but expressly leaves its full width distribution open; that second moment is recovered here as a consistency check. An exact octahedral-width result uses related spherical-cap ideas, but its six-axis configuration and threshold law do not imply the icosahedral twelve-vertex formula. A 2026 general polyhedral-width theory supplies an all-polytope coarea representation and explicitly identifies other specialized densities; its available abstract does not identify an evaluated icosahedral law. This general method is credited rather than claimed as new.
## Limitations
The result is specific to regular icosahedra in Euclidean three-space, modulo similarity. The spherical Voronoi and cap-segment mechanisms are standard and are not presented as discoveries. Full-text priority inspection of the 2026 general polyhedral-width treatise was unavailable; independently indexed older stereological sources under Feret or caliper width remain a historical-priority risk. No claim of independent verification or publication priority is made.
## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, 4 October 2011, https://arxiv.org/abs/1110.0671 .
2. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479v1, 26 November 2015, https://arxiv.org/abs/1511.08479 .
3. *Mean-square widths of all five Platonic solids*, published-finding corpus public record `a3835a8d344f`, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-mean-square-widths-of-all-five-platonic-solids--a3835a8d344f .
4. *Exact width distribution of the unit-edge regular octahedron*, published-finding corpus public record `953206d3d8c4`, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-width-distribution-of-the-unit-edge-regular-octahedron--953206d3d8c4 .
5. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1, 10 August 2026, https://arxiv.org/abs/2609.26202 .
