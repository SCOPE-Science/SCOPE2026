# Sharp Haar pentagon law for centroidal sections of right rectangular pyramids

## Finding
Fix any \(a,b,h>0\), and form the right rectangular pyramid
\[
K=\operatorname{conv}\left\{(\pm a/2,\pm b/2,0),(0,0,h)\right\}\subset\mathbb R^3.
\]
The parameters \(a,b\) denote *full* side lengths of its rectangular base. Its volume centroid is \(G=(0,0,h/4)\). Intersect \(K\) with a uniformly oriented **unoriented** plane through \(G\), and let \(N\) be the number of vertices of the resulting planar convex polygon. Then almost surely \(N\in\{4,5\}\), and, writing \(S=4a^2+4b^2+h^2\),
\[
\boxed{\Pr(N=5)=\frac4\pi\left(\arcsin\frac{2a}{\sqrt S}+\arcsin\frac{2b}{\sqrt S}+\arcsin\frac h{\sqrt S}\right)-2.}\tag{1}
\]
The remaining probability is \(\Pr(N=4)=1-\Pr(N=5)\), and \(\mathbb E[N]=4+\Pr(N=5)\). The pentagon probability has the **globally sharp** bound
\[
\boxed{0<\Pr(N=5)\le\frac{12}{\pi}\arcsin\frac1{\sqrt3}-2=0.350959312183644\ldots.}\tag{2}
\]
Equality in the upper bound holds **if and only if** \(a=b\) and \(h=2a\). The lower bound zero is the infimum over positive parameters and is never attained for a nondegenerate pyramid.

## Assumptions and scope
The section plane belongs to the Grassmannian \(G(2,3)\), with its rotation-invariant Haar probability measure. A plane is selected by its unit normal modulo antipodes. The polygon is the intersection of the three-dimensional solid with that plane. It is **not** the orthogonal projection, or shadow, of the solid. The plane contains the volume centroid, not the center of the rectangular base, and not an arbitrary section point. Geometrically degenerate section directions, where a base vertex or the apex lies in the plane, form a Haar-null set. The shape parameters are strictly positive; degenerations are considered only for the infimum statement. Similarity preserves all probabilities.

## Proof
**1. Classification of section vertices.** Translate \(G\) to the origin. The apex has position \(A=(0,0,3h/4)\), and the four base vertices are \(B_{\sigma,\tau}=(\sigma a/2,\tau b/2,-h/4)\), for \(\sigma,\tau\in\{\pm1\}\). Except on a null set, every section vertex is the transverse intersection with an edge whose endpoints have opposite signed heights under the plane normal. Orient the normal \(n=(n_x,n_y,n_z)\) with \(n_z>0\), making \(n\cdot A>0\).

For each pair of opposite base vertices, the two signed heights sum to \(-hn_z/2<0\). Thus at most two base vertices are on the positive side; if there are two, they are adjacent. When none is positive, four lateral edges cross the section, giving a quadrilateral. When exactly one is positive, three lateral edges and two base edges cross, giving a pentagon. When two adjacent ones are positive, two lateral and two base edges cross, again giving a quadrilateral. Consequently \(N=5\) exactly when **one base vertex** has positive signed height in the orientation with \(n_z>0\).

**2. A trivariate Gaussian orthant.** Consider the event where \(B_{+,+}\) is positive and its other three base vertices are negative. Multiplying signed heights by four, this is equivalent to the three conditions
\[
 n\cdot w_1>0,\quad n\cdot w_2>0,\quad n\cdot w_3>0,
\quad w_1=(2a,2b,-h),\quad w_2=(2a,-2b,h),\quad w_3=(-2a,2b,h).\tag{3}
\]
Indeed, \(w_1\) forces \(B_{+,+}\) positive, while \(w_2,w_3\) force \(B_{-,+}\) and \(B_{+,-}\) negative; the identity \(B_{-,-}=B_{-,+}+B_{+,-}-B_{+,+}\) forces the last base vertex negative. Moreover, \(w_2+w_3=(0,0,2h)\), so these inequalities imply \(n_z>0\) as required.

Replace a Haar-uniform normal by \(Z/\|Z\|\), where \(Z\) has three independent standard Gaussian coordinates. The vectors \(w_i\) have the common squared length \(S=4a^2+4b^2+h^2\). Their standardized Gaussian scalar products have pairwise correlations
\[
\rho_{12}=\frac{4a^2-4b^2-h^2}{S}=\frac{8a^2}{S}-1,\quad
\rho_{13}=\frac{8b^2}{S}-1,\quad
\rho_{23}=\frac{2h^2}{S}-1.\tag{4}
\]
For any centered bivariate standard normal pair with correlation \(\rho\), the sign correlation is \(\mathbb E[\operatorname{sgn}X\,\operatorname{sgn}Y]=(2/\pi)\arcsin\rho\). To see this without invoking a separate theorem, express the pair as two projections of an isotropic planar Gaussian onto unit vectors at angle \(\arccos\rho\). The fraction of directions with opposite signs is that angle divided by \(\pi\).

Expanding \(\prod_{i=1}^3(1+\operatorname{sgn}(Z\cdot w_i))/8\) and using symmetry to annihilate the odd-degree terms gives the exact positive-orthant probability
\[
 q=\frac18+\frac{\arcsin\rho_{12}+\arcsin\rho_{13}+\arcsin\rho_{23}}{4\pi}.\tag{5}
\]
There are four mutually disjoint one-positive-base events for \(n_z>0\). Their antipodal copies have the same measure, giving \(\Pr(N=5)=8q\). Substitution of (4) in (5), followed by the elementary identity \(\arcsin(2t-1)=2\arcsin\sqrt t-\pi/2\) for \(0<t<1\), establishes (1).

**3. Sharp global maximum and equality.** Put
\[
p_1=\frac{4a^2}{S},\qquad p_2=\frac{4b^2}{S},\qquad p_3=\frac{h^2}{S}.
\]
These three positive numbers sum to one; conversely, every strictly positive triple summing to one arises from some positive shape parameters. With \(f(t)=\arcsin\sqrt t\), (1) becomes \(\Pr(N=5)=(4/\pi)\sum_{i=1}^3 f(p_i)-2\).

Suppose \(x>y>0\) and \(x+y<1\). Since
\[
 x(1-x)-y(1-y)=(x-y)(1-x-y)>0,
\]
we have \(f'(x)<f'(y)\), using \(f'(t)=1/(2\sqrt{t(1-t)})\). Transferring an infinitesimal amount from the larger to the smaller coordinate therefore *strictly increases* their sum of \(f\)-values until equality. In any nonuniform three-coordinate probability vector this transfer is possible. Repeated balancing proves that the unique global maximizer occurs at \(p_1=p_2=p_3=1/3\). This is exactly the condition \(4a^2=4b^2=h^2\), equivalently \(a=b\) and \(h=2a\). Formula (2) follows. The orthant in (3) has positive Gaussian probability because its cone is full-dimensional, so \(\Pr(N=5)>0\). When one of the positive ratios \(p_i\) tends to one and the other two to zero, \(\sum_i f(p_i)\to\pi/2\), making \(\Pr(N=5)\to0\) without attaining zero in the stated domain.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It implements (1), an **independently derived spherical-triangle solid-angle expression**, and a crossed-edge count from sampled Gaussian normals, without treating sampled classifications as proof. It checks 840,000 random directions across seven positive parameter triples, the independent angle expression for 4,000 additional parameter triples, and the sharp-maximizer test. All checks passed; the maximum sampled absolute probability discrepancy was approximately 0.002629. Execute from the same directory with `python3 verify.py`. All quantifiers in (1)–(2) are established analytically above, not by these finite tests.

## Relationship to prior work
Feldman and Klain (2008) relate solid angles to the number of vertices in **orthogonal projections** of simplices, which is a different random experiment. Finch (2012) evaluates several planar shadow quantities, including a previously known \(0.3509593\ldots\) value. The published published-finding corpus result “Exact five-vertex shadow law and unique height optimum for right rectangular pyramids” likewise gives a full law for **shadows** of right rectangular pyramids; it neither states nor directly implies (1) for **central sections** of that same family. Central sections are dual to projections of the *polar body*, but the polar of a general right rectangular pyramid is a right pyramid with a rhombic—not rectangular—base, so the published rectangular-shadow family does not subsume the anisotropic section law. The square special case and its numerical coincidence with a known shadow probability are **not claimed as new**. Padrol and Pfeifle (2014) discuss possible polygon sections of quadrangular pyramids and other polytopes, without Haar orientation probabilities or the sharp rectangular aspect/height optimizer. Other inspected published records concern central sections of rectangular boxes and the regular icosahedron, not this theorem. The contribution assessed here is the complete all-positive-shape centroidal-section probability and its unique optimizer, subject to residual historical-priority uncertainty.

## Limitations
Only right rectangular pyramids, centered vertical apexes, planes through the **volume centroid**, and uniformly random orientations are covered. This does not establish probabilities for oblique pyramids, arbitrary section locations, uncentered planes, or orthogonal shadows. Finite simulations do not prove continuum claims, which are derived independently. General results about random sections or polar shadow combinatorics could conceivably imply this result after an unexamined specialization; the comparison was bounded to the identified materials and does not constitute independent priority certification.

## References
1. D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459v1 (2008-09-19), https://arxiv.org/abs/0809.3459 .
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (2012-03-12), https://arxiv.org/abs/1203.2464 .
3. A. Padrol and J. Pfeifle, *Polygons as sections of higher-dimensional polytopes*, arXiv:1404.2443v1 (2014-04-09), https://arxiv.org/abs/1404.2443 .
4. *Exact five-vertex shadow law and unique height optimum for right rectangular pyramids*, published research result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-five-vertex-shadow-law-and-unique-height-optimum-for-right--2273575e8a0a .
5. *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, published research result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4 .
