# Gaussian-curvature histograms classify convex planar-core tubes up to curvature rearrangement

## Finding
For any smooth strictly convex closed planar curve \(\gamma\), and any \(0<r<\operatorname{reach}(\gamma)\), the **distribution of Gaussian curvature under normalized surface area** on the radius-\(r\) tube determines exactly (i) the tube radius \(r\), (ii) the normalized arclength distribution of the positive curvature \(\kappa\) of \(\gamma\), and hence (iii) the length of \(\gamma\) and the area and enclosed volume of its tube. Conversely these two items determine the entire Gaussian-curvature distribution. The curve itself is not determined: infinitely many pairwise noncongruent strictly convex curves yield identical distributions for one common sufficiently small radius.

More explicitly, let \(K_-<0<K_+\) be the endpoints of the essential support of the Gaussian-curvature law \(\mu\). Then
\[
r^2=\frac12\left(\frac1{K_+}+\frac1{K_-}\right),\qquad \kappa_{\max}=\frac{rK_+}{1-r^2K_+}.
\]
For every integer \(j\ge1\), the normalized arclength curvature moments are recovered by
\[
\frac1L\int_0^L\kappa(s)^{2j}\,ds
=\frac{4^j r^{2j}}{\binom{2j}{j}}\int_{\mathbb R}\frac{k^{2j}}{(1-r^2k)^{2j-1}}\,d\mu(k).
\]
These moments determine the positive-curvature distribution uniquely. Writing the recovered measure as \(\nu\), the curve length is \(L=2\pi/(\int x\,d\nu(x))\). The tube surface area and volume are respectively \(2\pi rL\) and \(\pi r^2L\).

## Assumptions and scope
Let \(\gamma:[0,L]\to\mathbb R^2\) be a simple positively oriented strictly convex \(C^3\) closed curve parametrized once by arclength, with everywhere positive continuous curvature \(\kappa(s)\). The radius \(r\) is strictly less than the reach of \(\gamma\), so its Euclidean tube boundary \(\Sigma=\{p:\operatorname{dist}(p,\gamma)=r\}\subset\mathbb R^3\) is smooth and embedded. A point on \(\Sigma\) is drawn from normalized two-dimensional surface area, and \(\mu\) is the law of its Gaussian curvature. Equality of laws means equality of Borel probability measures on \(\mathbb R\), without recorded point location or orientation. No assumption that \(\gamma\) is a circle is made.

## Proof
Let \(T\) be the positively oriented unit tangent, \(n\) the inward planar normal, and \(e_3\) the perpendicular unit vector. The tube parametrization is
\[
X(s,\theta)=\gamma(s)+r(\cos\theta\,n(s)+\sin\theta\,e_3),\quad 0\le\theta<2\pi.
\]
Since \(n'=-\kappa T\), its area element and Gaussian curvature are exactly
\[
dA=r(1-r\kappa(s)\cos\theta)\,ds\,d\theta,\qquad K(s,\theta)=-\frac{\kappa(s)\cos\theta}{r(1-r\kappa(s)\cos\theta)}.
\]
The reach assumption ensures \(1-r\kappa\cos\theta>0\). Integrating \(dA\) gives \(S=2\pi rL\). The tubular volume is \(V=\pi r^2L\) by normal-disk integration.

Put \(u=\kappa(s)\cos\theta\). The map \(u\mapsto K=-u/[r(1-ru)]\) has derivative \(-1/[r(1-ru)^2]<0\), and \(|u|\le\kappa_{\max}\), with both extremes attained. Therefore
\[
K_+=\frac{\kappa_{\max}}{r(1+r\kappa_{\max})},\quad
K_-=-\frac{\kappa_{\max}}{r(1-r\kappa_{\max})},
\]
which proves the endpoint recovery formula (including the formula for \(\kappa_{\max}\)). Solving for \(u\) gives \(u=-rK/(1-r^2K)\) and \(1-r^2K=(1-ru)^{-1}\). Consequently, for every continuous function \(F\),
\[
\int (1-r^2k)F\!\left(-\frac{rk}{1-r^2k}\right)d\mu(k)
=\frac{1}{2\pi L}\int_0^L\int_0^{2\pi}F(\kappa(s)\cos\theta)\,d\theta\,ds.
\]
Take \(F(u)=u^{2j}\) and use \((2\pi)^{-1}\int_0^{2\pi}\cos^{2j}\theta\,d\theta=\binom{2j}{j}/4^j\) to obtain the stated moment formula. Since \(\kappa\) is positive and bounded, the sequence of even moments uniquely determines the law \(\nu\) of \(\kappa\) under normalized arclength: they are all moments of the compactly supported variable \(\kappa^2\). Conversely, \(r\) and \(\nu\) determine the right-hand side of the above test-function identity, hence the law of \(u\); reversing its known positive area weight and the monotone fractional transformation uniquely determines \(\mu\). The turning-angle theorem gives \(\int\kappa\,ds=2\pi\) and thus the stated length formula.

To show sharp nonidentifiability, fix \(R>0\), \(0<\varepsilon<1\), and for every integer \(m\ge2\) define a strictly convex curve by its support function
\[
h_m(\phi)=R+\frac{R\varepsilon}{1-m^2}\cos(m\phi).
\]
Its radius of curvature is \(\rho_m=h_m+h_m''=R(1+\varepsilon\cos(m\phi))>0\), so \(ds=\rho_m\,d\phi\) and \(\kappa=1/\rho_m\). These support functions define smooth closed convex curves, with the first Fourier harmonics absent. For every bounded continuous \(f\),
\[
\frac1L\int f(\kappa)\,ds=\frac1{2\pi}\int_0^{2\pi}(1+\varepsilon\cos(m\phi))f\!\left(\frac1{R(1+\varepsilon\cos(m\phi))}\right)d\phi.
\]
This is independent of \(m\) by periodic substitution, while every curve has \(L=2\pi R\). The different rotational symmetry orders \(m\) show these curves are pairwise noncongruent. Take one common positive radius below the reach of any chosen finite subfamily (for instance \(m=2,3\)); all their tubes have exactly the same Gaussian-curvature probability law. This proves the inverse classification and its sharp failure of core-shape rigidity.

## Verification
The self-contained program `verify.py` runs deterministic periodic quadratures for distinct harmonic cores, tests the endpoint radius identity, checks the fractional transformation, recovers three even curvature moments, and compares four Gaussian-curvature moments between noncongruent cores. It reports `ALL_CHECKS_PASSED`. These finite numerical checks are supplementary; the proof above is exact for all admissible curves and every moment order.

## Relationship to prior work
Saad et al. (2024, Section 3, equation (3.6)) state the classical local Gaussian-curvature formula for a general tubular surface and analyze focal/Weingarten properties. Tunçer, Yoon and Karacan (2011, Section 3) also treat local tubular curvatures and Weingarten classifications. Both supply forward geometric context; neither inspected full text gives an area-sampled curvature-law inverse theorem or the explicit noncongruent harmonic-core equivalence family. The present claim does **not** regard the local curvature formula or tubular volume formula as new. Its subject is the exact measure-level inverse classification and its geometric nonuniqueness. Earlier equivalent probability-transform or curvature-histogram work under different terminology remains possible.

## Limitations
The results require an embedded constant-radius tube about a strictly convex planar core of everywhere positive curvature. Negative or vanishing signed core curvature, open cores, variable radius, spatial nonplanar cores, noisy observations, and finite-sample recovery are not covered. The moment inverse is mathematical identifiability, not a stability guarantee. The historical novelty assessment is provisional and independent expert validation is outstanding.

## References
1. M. Khalifa Saad, N. Yüksel, N. Oğraş, F. Alghamdi and A. A. Abdel-Salam, "Geometry of tubular surfaces and their focal surfaces in Euclidean 3-space," *AIMS Mathematics* 9 (2024), 12479–12493, doi:10.3934/math.2024610 (first published 2024-04-01, primary MSC 53A05).
2. Y. Tunçer, D. W. Yoon and M. K. Karacan, "Weingarten and Linear Weingarten Type Tubular Surfaces in \(E^3\)," *Mathematical Problems in Engineering* (2011), 191849, doi:10.1155/2011/191849 (first published 2011-06-23).
