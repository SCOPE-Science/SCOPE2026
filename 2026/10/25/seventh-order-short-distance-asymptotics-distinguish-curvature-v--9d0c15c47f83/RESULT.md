# Seventh-order short-distance asymptotics distinguish curvature variation in convex ovals

## Finding
Let \(X,Y\) be two independent uniformly distributed points in a smooth strictly convex planar body. The cumulative distribution of their Euclidean separation has a seventh-order coefficient governed by a *difference* of curvature energies:
\[
\Pr(|X-Y|\le r)=\frac{\pi r^2}{A}-\frac{2P r^3}{3A^2}
+\frac{r^5}{60A^2}\int_{\partial K}\kappa^2\,ds
+\frac{r^7}{A^2}\left[\frac1{2240}\int_{\partial K}\kappa^4\,ds-\frac1{2520}\int_{\partial K}(\kappa_s)^2\,ds\right]+o(r^7).
\]
There are no terms of degrees four or six. Here \(A\) and \(P\) are the body's area and perimeter, \(s\) is arclength, \(\kappa>0\) denotes curvature, and \(\kappa_s=d\kappa/ds\). Unlike the positive fifth-order curvature energy, the seventh-order coefficient can have either sign.

For a particularly transparent sign-changing family, let the radius of curvature in outward-normal-angle coordinates be
\[
\rho_m(\theta)=1+\tfrac12\cos(m\theta),\qquad m=2,3,4,\ldots.
\]
Every member exists as a real-analytic strictly convex oval with support function
\[
h_m(\theta)=1-\frac{\cos(m\theta)}{2(m^2-1)},\qquad h_m+h_m''=\rho_m>0.
\]
All have perimeter \(2\pi\) and the same normal-angle distribution of curvature radius. Nevertheless the seventh-order coefficient is positive at \(m=2\), zero for no integer \(m\ge2\), and negative for all \(m\ge3\). This isolates the curvature-gradient energy as a genuinely geometric feature of the distance law.

## Assumptions and scope
\(K\subset\mathbb R^2\) is a compact convex body with nonempty interior and \(C^6\) boundary with strictly positive curvature everywhere. All limits are as \(r\downarrow0\), keeping \(K\) fixed. Translation, orientation and scale are unrestricted. The independent points \(X,Y\) are distributed according to planar area normalized by \(A\). The statement is an asymptotic expansion, not an equality for finite positive \(r\).

## Proof
**1. Covariogram representation.** For a unit vector \(u\), let \(g(tu)=\operatorname{Area}(K\cap(K+tu))\). Write \(w_u\) for the length of the orthogonal projection of \(K\) onto \(u^\perp\). Fubini over lines parallel to \(u\) gives
\[
g(tu)=\int_{u^\perp}(\ell_u(y)-t)_+\,dy,
\]
where \(\ell_u(y)\) is the chord length. Therefore the distance CDF satisfies the exact identity
\[
\Pr(|X-Y|\le r)=\frac1{A^2}\int_0^r t\int_0^{2\pi}g(tu_\phi)\,d\phi\,dt.
\]

**2. Uniform local tangent expansion.** Fix one of the two boundary points where \(u\) is tangent. Choose signed tangent coordinate \(z\) and inward normal coordinate \(v\) with the boundary locally \(v=f(z)\), \(f(0)=f'(0)=0\). Denote arclength curvature derivatives at the point by \(\kappa_s\) and \(\kappa_{ss}\). Frenet graph calculus gives
\[
f''(0)=\kappa,\quad f'''(0)=\kappa_s,\quad f''''(0)=\kappa_{ss}+3\kappa^3.
\]
For sufficiently small \(t>0\), define \(c(t)\) by \(f(c(t)+t/2)=f(c(t)-t/2)\). Taylor expansion and positive curvature give
\[
c(t)=-\frac{\kappa_s}{24\kappa}t^2+O(t^4).
\]
The departure from the linear projection-width law at this tangent point is the exact local fiber correction \(\int_{c(t)-t/2}^{c(t)+t/2}f(z)\,dz\). Substituting the fourth-order graph Taylor polynomial gives
\[
\frac{\kappa}{24}t^3+
\left(\frac{\kappa_{ss}+3\kappa^3}{1920}-\frac{\kappa_s^2}{1152\kappa}\right)t^5+o(t^5).
\]
Compactness, uniform positive curvature and \(C^6\) regularity ensure the error is uniform in \(u\). The two tangency points contribute additively, yielding the directional covariogram through order five:
\[
g(tu)=A-tw_u+\sum_{x:\,u\text{ tangent at }x}\left[\frac{\kappa(x)}{24}t^3+
\left(\frac{\kappa_{ss}(x)+3\kappa(x)^3}{1920}-\frac{\kappa_s(x)^2}{1152\kappa(x)}\right)t^5\right]+o(t^5).
\]

**3. Angular integration and cancellation.** Cauchy's projection formula gives \(\int_0^{2\pi}w_{u_\phi}\,d\phi=2P\). Each tangent point is represented twice as \(u\) ranges around the circle, and the normal angle satisfies \(d\theta=\kappa\,ds\). Consequently
\[
\int_0^{2\pi}g(tu_\phi)\,d\phi=2\pi A-2Pt+
\frac{t^3}{12}\int_{\partial K}\kappa^2\,ds+
 t^5\int_{\partial K}\left(\frac{\kappa\kappa_{ss}}{960}+\frac{\kappa^4}{320}-\frac{\kappa_s^2}{576}\right)ds+o(t^5).
\]
Since the boundary is closed, \(\int\kappa\kappa_{ss}\,ds=-\int\kappa_s^2\,ds\); the fifth-order angular coefficient simplifies to \(\int(\kappa^4/320-\kappa_s^2/360)ds\). Integrating against \(t\,dt/A^2\) proves the CDF expansion and all numerical normalizations.

**4. Exact sign-change witnesses.** In outward-normal-angle coordinates, \(ds=\rho\,d\theta\), \(\kappa=1/\rho\), and \(\kappa_s=-\rho'/\rho^3\). For \(\rho_m=1+a\cos(m\theta)\), \(0<a<1\), exact trigonometric integration yields
\[
\int\kappa^4\,ds=\frac{\pi(2+a^2)}{(1-a^2)^{5/2}},\qquad
\int(\kappa_s)^2\,ds=\frac{\pi a^2m^2(4+a^2)}{4(1-a^2)^{7/2}}.
\]
Therefore the sign of the seventh coefficient is the sign of
\[
\frac{(2+a^2)(1-a^2)}{2240}-\frac{a^2m^2(4+a^2)}{10080}.
\]
At \(a=1/2\) this is positive for \(m=2\) and negative for all integers \(m\ge3\), since the sign changes when \(m^2>243/34\). The ovals are closed because the first Fourier harmonic of their curvature radii vanishes. Their perimeters are all \(2\pi\).

## Verification
The reproducibility program `check_seventh_order.py` independently computes the covariogram of an affine disk, verifies that its exact angular fifth-order coefficient agrees with the derived combination of ellipse curvature energies for four distinct aspect ratios, expands the exact unit-disk interpoint-distance CDF through degree seven, and compares the curvature-radius family integrals to closed forms, including both signs. It executed successfully and printed `ALL_SEVENTH_ORDER_COVARIOGRAM_CHECKS_OK`. The Python checks are finite algebraic/numerical corroboration; the proof above establishes the asymptotics for the stated infinite class.

## Relationship to prior work
Gečiauskas (1966, 1968) gave general Crofton and integral-geometric representations for oval interpoint-distance distributions; his inspected formulas and examples do not explicitly evaluate the order-seven coefficient in boundary curvature energies. Rataj's 2004 Theorem 3 computes the directional *third* derivative of covariograms for smooth convex bodies and, in dimension two, identifies the sum of two tangent-point curvatures. It already implies the fifth-order CDF coefficient after angular integration; that coefficient is **not asserted to be new**. The new content is the fifth directional covariogram coefficient, the integrated seventh-order distance coefficient with the curvature-gradient correction, and explicit analytic ovals where its sign flips. The 1992 paper of Meyer, Reisner and Schmuckenschläger studies translate intersections and low-order smoothness, rather than this seventh-order local distance invariant. Bianchi's 2014 survey addresses covariograms and inverse determination; it does not state this curvature-gradient coefficient in the inspected sections. Nearby polygonal short-distance results do not imply the smooth-boundary seventh-order expansion. These are literature comparisons, not a proof of global historical priority.

## Limitations
The expansion requires uniformly positive curvature and sufficient boundary smoothness; corners, curvature-zero points and families with nonuniform smoothness may change the exponents. The sign example does not classify all bodies by the sign of this coefficient. The full text of the closely related Bianchi–Segala–Volčič 2002 covariogram-rigidity article was not accessible during comparison, and the older Gates chord-distribution article was inspected only at its abstract; historical priority remains a risk. Independent mathematical validation has not been performed.

## References
1. M. Meyer, S. Reisner and M. Schmuckenschläger, *The Volume of the Intersection of a Convex Body with its Translates*, first public preprint 1992-04-14, arXiv:math/9204212, https://arxiv.org/abs/math/9204212.
2. J. Rataj, *On Set Covariance and Three-Point Test Sets*, Czechoslovak Mathematical Journal 54 (2004), 205–214, Theorem 3, https://dml.cz/dmlcz/127877.
3. G. Bianchi, *The Covariogram Problem*, 2014 survey, https://people.dimai.unifi.it/bianchi/lavori/covariogram_survey14.pdf.
4. G. Bianchi, F. Segala, A. Volčič, *The Solution of the Covariogram Problem for Plane \(C^2_+\) Convex Bodies*, Journal of Differential Geometry 60 (2002), 177–198, DOI:10.4310/jdg/1090351101 (full-text access limited).
5. J. Gates, *Some Properties of Chord Length Distributions*, Journal of Applied Probability 24 (1987), 863–874 (abstract inspected; full-text access limited).
6. E. Gečiauskas, *Distribution Function of a Distance Between Two Random Points in an Oval*, Lithuanian Mathematical Journal 6 (1966), 245–248, https://doi.org/10.15388/LMJ.1966.19722.
7. E. Gečiauskas, *The Method of Integral Geometry for Finding the Distribution Functions of Chord Length of an Oval and of Distance in an Oval*, Lithuanian Mathematical Journal 8 (1968), 237–241, https://doi.org/10.15388/LMJ.1968.20212.
8. *Sharp uniform angular stability for the short-pair-distance coefficient of convex polygons*, publicly indexed result record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b (different polygonal model).
