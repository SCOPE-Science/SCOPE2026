# Sharp convexity threshold in the Klee inner-section counterexample family
## Finding
For every dimension
\[
n\ge3,
\]
consider the body of revolution \(K_\varepsilon\subset\mathbb R^n\) used in the Gardner--Ryabogin--Yaskin--Zvavitch construction for Klee's inner-section problem. Its radial function is
\[
\rho_\varepsilon(\phi)
=
\left(1+\varepsilon\cos^3\phi\right)^{-1/3},
\qquad
0\le\varepsilon<1.
\tag{1}
\]

The exact convexity range is
\[
\boxed{
K_\varepsilon\text{ is convex}
\quad\Longleftrightarrow\quad
0\le\varepsilon\le\frac{3\sqrt6}{8}
}.
\tag{2}
\]
Moreover,
\[
0\le\varepsilon<\frac{3\sqrt6}{8}
\]
gives strict convexity. At the sharp endpoint
\[
\varepsilon_*=\frac{3\sqrt6}{8}
\approx0.9185586535,
\]
the meridional curvature vanishes first at the unique polar cosine
\[
\cos\phi=-\sqrt{\frac23},
\tag{3}
\]
and for
\[
\varepsilon>\varepsilon_*
\]
the meridian is locally nonconvex near that latitude.

The original convexity lemma proves convexity for sufficiently small \(\varepsilon\) and notes the numerical sufficient value \(0.91\). Formula (2) gives the exact endpoint of that particular convexity question.

## Assumptions and scope
The polar angle \(\phi\in[0,\pi]\) is measured from the distinguished axis of revolution. The condition
\[
0\le\varepsilon<1
\]
ensures
\[
1+\varepsilon\cos^3\phi>0
\]
for every \(\phi\), so (1) is a positive smooth radial function.

For a body of revolution, convexity is equivalent to convexity of a planar meridian section containing the axis. Thus it is enough to study the polar curve
\[
r(\phi)=\left(1+\varepsilon\cos^3\phi\right)^{-1/3}.
\]

This result sharpens only the convexity sublemma for the radial family (1). The later analytic estimates in the full Klee counterexample construction impose additional smallness conditions on \(\varepsilon\); no claim is made that the complete construction remains valid for every parameter up to the endpoint (2).

## Proof
For a positive \(C^2\) polar curve \(r=r(\phi)\), the signed curvature has the sign of
\[
r^2+2(r')^2-r r''.
\tag{4}
\]
For (1), direct differentiation and simplification give
\[
r^2+2(r')^2-r r''
=
\frac{
1+2\varepsilon\cos\phi-\varepsilon\cos^3\phi
}{
\left(1+\varepsilon\cos^3\phi\right)^{8/3}
}.
\tag{5}
\]
The denominator is strictly positive throughout the stated parameter range. Therefore convexity of the meridian is controlled by
\[
F_\varepsilon(c)
=
1+\varepsilon(2c-c^3),
\qquad
-1\le c\le1.
\tag{6}
\]

Put
\[
g(c)=2c-c^3.
\]
Then
\[
g'(c)=2-3c^2.
\]
The only critical points in \([-1,1]\) are
\[
c=\pm\sqrt{\frac23}.
\]
The negative one is the unique global minimum:
\[
g\left(-\sqrt{\frac23}\right)
=
-\frac{4\sqrt6}{9}.
\tag{7}
\]
Indeed,
\[
g(-1)=-1,
\qquad
g(1)=1,
\]
while
\[
-\frac{4\sqrt6}{9}<-1.
\]

Combining (6) and (7),
\[
\min_{-1\le c\le1}F_\varepsilon(c)
=
1-\frac{4\sqrt6}{9}\varepsilon.
\tag{8}
\]
Hence
\[
F_\varepsilon(c)\ge0
\quad\text{for every }c\in[-1,1]
\]
if and only if
\[
\varepsilon
\le
\frac{9}{4\sqrt6}
=
\frac{3\sqrt6}{8}.
\tag{9}
\]

If
\[
0\le\varepsilon<\frac{3\sqrt6}{8},
\]
then the right-hand side of (8) is strictly positive, so the meridian has strictly positive curvature everywhere. This gives strict convexity.

At
\[
\varepsilon=\frac{3\sqrt6}{8},
\]
equation (8) vanishes only at
\[
c=-\sqrt{\frac23}.
\]
Convexity at the endpoint follows, for example, by taking any sequence
\[
\varepsilon_j\uparrow\frac{3\sqrt6}{8}.
\]
The radial functions converge uniformly, hence the corresponding compact bodies converge in Hausdorff distance. Each \(K_{\varepsilon_j}\) is convex, and a Hausdorff limit of convex compact sets is convex.

Finally, if
\[
\frac{3\sqrt6}{8}<\varepsilon<1,
\]
then substituting (3) into (6) makes \(F_\varepsilon\) negative. By (5), the meridional curvature is negative there, so the meridian and therefore the body of revolution are not convex. This proves (2).

## Verification
The bundled `verify.py` independently differentiates the radial function symbolically and verifies the exact factorization (5). It also verifies
\[
g'\left(\pm\sqrt{\frac23}\right)=0,
\]
the exact minimum value (7), and the vanishing of (8) at
\[
\varepsilon_*=\frac{3\sqrt6}{8}.
\]
As numerical stress checks, it confirms positive minimum curvature numerator at \(\varepsilon=0.91\) and negative minimum numerator at \(\varepsilon=0.92\).

These computations are regression checks. The quantified result follows from the exact one-variable minimization (6)--(9), not from numerical sampling.

## Relationship to prior work
Gardner, Ryabogin, Yaskin, and Zvavitch introduced the family (1) while giving a negative solution to Klee's inner-section problem. In their convexity lemma they reduce the question to a planar meridian, display the same curvature expression underlying (5), prove convexity for sufficiently small positive \(\varepsilon\), and explicitly note that numerically one may take
\[
\varepsilon_0=0.91.
\]
They do not identify the exact maximal convexity parameter.

The calculation above resolves that parameter exactly. It converts the source's curvature expression to the cubic minimization (6), whose unique worst latitude is (3), and shows that the sharp threshold is
\[
\frac{3\sqrt6}{8}
=
0.9185586535\ldots.
\]

Targeted searches using the radial formula, the Klee construction, the numerical value \(0.91\), and the exact radical did not locate a published statement of this sharp endpoint. A superficially similar exact constant occurs in a different cubic support-function convexity problem, but that problem concerns another family and does not imply the radial-body statement here.

## Limitations
This theorem concerns only convexity of the radial family (1). It does not enlarge the verified parameter range of every subsequent Fourier-analytic or section-function estimate used in the full counterexample construction.

The endpoint body is convex but not strictly convex in the meridional curvature sense because curvature vanishes at the latitude (3).

The proof does not classify perturbations obtained by replacing the cubic \(\cos^3\phi\) with a different odd profile.

Because the reduction is elementary once the published curvature formula is written down, an equivalent sharp endpoint may exist in unindexed notes or later discussions of the Klee construction. Targeted searches found no such statement, but that historical residual risk remains.

## References
1. R. J. Gardner, D. Ryabogin, V. Yaskin, and A. Zvavitch, *A problem of Klee on inner section functions of convex bodies*, arXiv:1101.3364v1, 18 January 2011; *Journal of Differential Geometry* 91 (2012), 261--279. DOI: 10.4310/jdg/1344430824.
