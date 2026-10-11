# Universal radial coverage by concentric regular-polygon unions

## Finding
Let \(n\ge3\) and \(m\ge2\) be integers, \(R>0\), and let \(U\) be the union of \(m\) rotated copies of one regular Euclidean \(n\)-gon, all with the same center and circumradius \(R\). Set \(\alpha=\pi/n\) and \(r=R\cos\alpha\). Define \(C_U(t)\) as the angular measure (in radians) of directions \(u\in S^1\) with \(tu\in U\), where \(r<t<R\).

Write the rotations as cyclically ordered phases modulo \(2\alpha\), and let their \(m\) cyclic gaps be \(g_1,\ldots,g_m\ge0\), with \(\sum_j g_j=2\alpha\). Coincident phases are permitted, with zero gaps. Then for every \(r<t<R\),
\[
 C_U(t)=n\sum_{j=1}^{m}\min\left\{g_j,\;2\left(\alpha-\arccos\frac rt\right)\right\}.
\]
In particular,
\[
 C_U(t)\le\min\left\{2\pi,\;2mn\left(\alpha-\arccos\frac rt\right)\right\}.
\]
Every level \(t\) attains this bound when the rotation phases are equally spaced modulo \(2\alpha\). **The equally spaced configuration is the only arrangement, up to a common rotation and permutation of copies, which maximizes all levels simultaneously.** For every measurable radial density \(w:[0,R]\to[0,\infty)\) that is integrable with area element and positive almost everywhere on \((r,R)\), it uniquely maximizes \(\int_U w(|x|)\,dx\) in the same sense.

The exact area for arbitrary phases is
\[
 \operatorname{area}(U)=nr^2\sum_{j=1}^{m}\left[\tan\alpha-\tan\left(\alpha-\frac{g_j}{2}\right)\right].
\]
Consequently the maximum, minimum, and unique maximizing family are
\[
 A_{\max}=nmr^2\left[\tan\alpha-\tan\left(\alpha-\frac\alpha m\right)\right],\qquad
 A_{\min}=nr^2\tan\alpha.
\]
The minimum holds precisely when all rotations coincide modulo \(2\alpha\). The optimal asymptotic disk-area deficit is
\[
 \pi R^2-A_{\max}=\frac{\pi^2R^2}{n}\tan\left(\frac\pi n\right)\frac1m+O_n\left(\frac{R^2}{m^2}\right)
 \quad(m\to\infty).
\]
The largest origin-centered disk contained in the union has radius \(r/\cos(\alpha-g_{\max}/2)\), where \(g_{\max}=\max_jg_j\). Its sharp maximum is \(r/\cos(\alpha-\alpha/m)\), again only for equally spaced rotations.

## Assumptions and scope
All input polygons are congruent, regular, closed, Euclidean and share exactly the same center; only their rotations vary. The original polygons need not be in general position. The union is generally nonconvex. Angular coverage uses arc-length measure on the unit circle, not normalized probability, and counts a direction once even if several input polygons cover it. The results are valid for every integer \(n\ge3\), every integer \(m\ge2\), and every real \(R>0\), including repeated rotation phases and endpoint gap patterns. At \(t\le r\) the entire circle is covered; at \(t>R\) none is. At \(t=R\), only finitely many vertex directions are covered, hence their angular measure is zero.

## Proof
**1. Radial reduction.** Let the vertices of one copy occur at arguments \(\theta+2k\alpha\). Its side outward normals have arguments \(\theta+(2k+1)\alpha\) and all supporting lines have distance \(r\) from the common center. If \(\delta\in[0,\alpha]\) is the angular distance from a direction to the nearest vertex, then its radial boundary distance is exactly
\[
 \rho(\delta)=\frac{r}{\cos(\alpha-\delta)}.
\]
For the union, the radial boundary is the pointwise maximum of the individual radial boundaries. Since \(\rho(\delta)\) decreases strictly on \([0,\alpha]\), the union radial boundary is given by the angular distance to the nearest vertex of *any* copy.

**2. Exact coverage at each radius.** At \(r<t<R\), a radial direction belongs to the union at radius \(t\) exactly when it is within angular distance \(\eta(t)=\alpha-\arccos(r/t)\in(0,\alpha)\) of some input vertex. The union of input vertex angles consists of \(n\) periodic copies of the phase configuration on a fundamental circle of length \(2\alpha\). Within each cyclic gap \(g_j\), the angular amount covered by the two adjacent vertex neighborhoods is \(\min(g_j,2\eta(t))\). Summing over gaps and periods proves the identity for \(C_U(t)\). This argument is valid for coincident phases as well.

**3. Universal optimality and rigidity.** For every \(c\ge0\),
\[
 \sum_{j=1}^{m}\min(g_j,c)\le\min\left(\sum_jg_j,mc\right)=\min(2\alpha,mc).
\]
All equal gaps \(g_j=2\alpha/m\) attain equality for every \(c\). Conversely, if the gaps are not all equal, choose \(c=2\alpha/m\). Some gap exceeds \(c\), and therefore the sum of truncated gaps is strictly less than \(2\alpha\). The strict deficit persists for an open interval of \(c\) by continuity. Since \(2\eta(t)\) ranges continuously through \((0,2\alpha)\), every unequal-gap arrangement has strictly smaller \(C_U(t)\) on a nonempty open interval of radii. Integrating \(tC_U(t)w(t)\) over \((r,R)\), and adding the common inner-disk contribution, proves universal weighted-area optimality and uniqueness for the stated densities.

**4. Exact area, extrema, and inradius.** In one angular gap of length \(g\), the nearest-vertex distance increases from zero to \(g/2\) and decreases back to zero. Integrating the radial square over the gap gives
\[
 \frac12\int_{\mathrm{gap}}\rho_U(\phi)^2\,d\phi
 =r^2\int_0^{g/2}\frac{du}{\cos^2(\alpha-u)}
 =r^2\left[\tan\alpha-\tan(\alpha-g/2)\right].
\]
There are \(n\) copies of the cyclic gaps, yielding the area formula. The upper extremum and equality statement follow from Step 3 with \(w=1\). The union contains each input polygon, so its area is at least that of one polygon, with equality only when all polygons coincide, because every distinct rotated copy has a distinct circumcircle vertex outside the other copy's boundary and consequently contributes positive area. The greatest directional distance to the nearest vertex occurs at the midpoint of a largest phase gap, giving the inradius formula. Every set of gaps of sum \(2\alpha\) has \(g_{\max}\ge2\alpha/m\), with equality only for equal gaps.

**5. Sharp disk deficit.** Taylor expansion at \(\alpha\) gives, for \(\varepsilon=\alpha/m\to0\),
\[
 \tan\alpha-\tan(\alpha-\varepsilon)
 =\varepsilon\sec^2\alpha-\varepsilon^2\sec^2\alpha\tan\alpha+O_\alpha(\varepsilon^3).
\]
Substituting \(r=R\cos\alpha\) and \(n\alpha=\pi\) yields the stated first-order deficit, with the remainder uniform for each fixed \(n\) and \(R\).

## Verification
Run `python verify.py` with Python 3.9+ and Shapely 2.x. It constructs literal polygon unions independently of the angular-gap derivation, comparing their area and perimeter with the formula for 240 arrangements including coincident and equally spaced phases. It independently evaluates coverage by direct polygon halfplane membership at sampled angles for fifteen radius/configuration tests, and checks the asymptotic coefficient numerically for four polygon orders. The run used for this report returned `VERIFY_OK`, with maximum polygon-union area discrepancy \(1.78\times10^{-15}\), perimeter discrepancy \(7.11\times10^{-15}\), and angular sampling discrepancy \(0.00139\) radians at 12,000 sampled directions. Numerical diagnostics do not prove the all-parameter theorem; Steps 1--5 are analytic proofs.

## Relationship to prior work
Kiss and Vidnyánszky (2014, arXiv:1402.5452, §§1--4) study unions of congruent regular polygons and define equally spaced, common-center “basic” arrangements. Their Lemma 2.5 proves the perimeter-to-area ratio for the basic arrangement; its argument explains the constant-ratio phenomenon for concentric polygon unions. That pre-existing ratio and the basic construction are not claimed to be new. This result instead gives the *sharp angular-coverage profile at every radius*, the universal inequality for all radial densities, the exact max/min area range and full equality classification for every order and number of rotations. Gyenes (2011) proves perimeter-to-area results for unions of congruent sets, including centered squares, but the accessible summary does not state radial coverage dominance or an exact rotational area optimizer. O'Rourke's 2015 question and answer on intersections of rotated regular polygons concern facet counts of intersections rather than radial angular coverage of unions.

## Limitations
No translations, changes of scale, different input polygon orders, or higher-dimensional unions are covered. The claim of a new contribution is relative to the materially examined literature and mathematical-record searches, not a proof that every historical paper has been indexed. Gyenes's full article was not materially inspected, so an unindexed or inaccessible sharp coverage statement remains a residual historical risk. No independent audit has been performed. The equality uniqueness for arbitrary radial weights assumes positivity almost everywhere on the open annulus; it does not hold for densities supported entirely inside the common incircle.

## References
1. Viktor Kiss and Zoltán Vidnyánszky, “Unions of regular polygons with large perimeter-to-area ratio”, arXiv:1402.5452v1 (first public 2014-02-21), *Discrete & Computational Geometry* 53 (2015), 878--889. https://arxiv.org/abs/1402.5452 ; HTML full text: https://arxiv.org/html/1402.5452v2
2. Zoltán Gyenes, “The Ratio of the Perimeter and the Area of Unions of Copies of a Fixed Set”, *Discrete & Computational Geometry* 45 (2011), 400--409, doi:10.1007/s00454-010-9321-9.
3. Joseph O'Rourke and Gjergji Zaimi, “Intersection of rotating regular polygons”, MathOverflow question/answer, 2015-10-17. https://mathoverflow.net/questions/221120/intersection-of-rotating-regular-polygons
