# An affine-invariant exact convex-hull area law for equal-area ellipses

## Finding
Let \(A,B\) be real symmetric positive-definite \(2\times2\) matrices with \(\det A=\det B=s^2>0\). Define the centered solid ellipses
\[
E_A=\{x\in\mathbb R^2:x^{\mathsf T}A^{-1}x\le1\},\qquad
E_B=\{x\in\mathbb R^2:x^{\mathsf T}B^{-1}x\le1\},
\]
and their intrinsic spectral mismatch
\[
D=\sqrt{\operatorname{tr}(A^{-1}B)-2}\ge0.
\]
Then the area of their convex hull is exactly
\[
\boxed{\operatorname{area}(\operatorname{conv}(E_A\cup E_B))
=s\left[\pi+2D-2\arctan\!\left(\frac D2\right)\right].}
\]
This expression is symmetric in \(A,B\), affine-invariant after division by \(s\), and strictly increasing in \(D\). If \(A\ne B\), the hull has four smooth elliptic boundary arcs joined by four straight common-tangent segments; at \(A=B\), it is a single ellipse.

The normalized excess \(G(D)=2D-2\arctan(D/2)\) is strictly convex for \(D>0\), and its sharp global linear bounds are
\[
\boxed{sD<\operatorname{area}(\operatorname{conv}(E_A\cup E_B))-\pi s<2sD\quad(A\ne B).}
\]
The coefficients \(1\) and \(2\) cannot be improved uniformly: the lower ratio tends to \(1\) as \(D\downarrow0\), and the upper ratio tends to \(2\) as \(D\to\infty\). In fact,
\[
G(D)=D+\frac{D^3}{12}+O(D^5)\quad(D\to0),\qquad
G'(D)=1+\frac{D^2}{4+D^2}\in[1,2).
\]

## Assumptions and scope
Both ellipses are filled, nondegenerate, centered at the same point (taken as the origin), and have the same positive area \(\pi s\). The shape matrices \(A,B\) encode the squared semiaxes and orientation, not the inverse quadratic-form coefficients. Any invertible common affine change of variables is allowed; no equality of eccentricities or principal-axis alignment is assumed. The statement concerns planar Euclidean area, not volume in higher dimensions, and does not assert the formula for unequal-area or displaced ellipses.

## Proof
**Affine reduction.** Since \(A\) is positive definite, the linear change \(y=A^{-1/2}x\) sends \(E_A\) to the unit disk and sends \(E_B\) to the ellipse with shape matrix \(C=A^{-1/2}BA^{-1/2}\). Area is multiplied by \(\det(A^{-1/2})=1/s\). By the equal-determinant hypothesis, \(\det C=1\); hence its two eigenvalues are \(\lambda^2\) and \(\lambda^{-2}\), with \(\lambda\ge1\). An orthogonal coordinate change therefore reduces the pair to
\[
E_0=\{(x,y):x^2+y^2\le1\},\qquad
E_1=\{(x,y):x^2/\lambda^2+\lambda^2y^2\le1\}.
\]
The trace relation is \(D^2=\operatorname{tr}C-2=(\lambda-\lambda^{-1})^2\), so \(D=\lambda-\lambda^{-1}\). This also shows \(D=0\) exactly when \(A=B\), and \(\operatorname{tr}(A^{-1}B)=\operatorname{tr}(B^{-1}A)\): the reciprocal eigenvalue pair has the same sum.

**Active supporting arcs.** The support functions at unit normal \(u_\phi=(\cos\phi,\sin\phi)\) are
\[
h_0(\phi)=1,\qquad
h_1(\phi)=\sqrt{\lambda^2\cos^2\phi+\lambda^{-2}\sin^2\phi}.
\]
For \(\lambda>1\), equality holds exactly at \(\phi=\pm\beta\pmod\pi\), where \(\beta=\arctan\lambda\in(\pi/4,\pi/2)\). On one period \(( -\beta,\pi-\beta)\), the hull support \(h=\max(h_0,h_1)\) equals \(h_1\) on \([-\beta,\beta]\) and \(1\) on \([\beta,\pi-\beta]\). Each switch has different support points because the two strictly convex ellipses are distinct and tangent to the same supporting line, giving exactly four straight facets over a full turn and four elliptic arcs.

**Exact area integration.** For any planar convex body with Lipschitz support function \(h\), the support-function area identity reads
\[
\operatorname{area}(K)=\frac12\int_0^{2\pi}(h^2-h'^2)\,d\phi.
\]
It applies to the maximum of the two smooth supports, using its almost-everywhere derivative; it can also be obtained by approximation from smooth supports. Central symmetry of the reduced hull makes the two half-period integrals equal. Direct differentiation and simplification give
\[
h_1^2-(h_1')^2=(\lambda^2-\lambda^{-2})\cos2\phi+\frac1{h_1^2}.
\]
Consequently
\[
\operatorname{area}(\operatorname{conv}(E_0\cup E_1))
=\int_{-\beta}^{\beta}\left[(\lambda^2-\lambda^{-2})\cos2\phi+\frac1{\lambda^2\cos^2\phi+\lambda^{-2}\sin^2\phi}\right]d\phi+(\pi-2\beta).
\]
The cosine term integrates to \((\lambda^2-\lambda^{-2})\sin2\beta=2(\lambda-\lambda^{-1})\). For the other term, substituting \(t=\tan\phi\) yields
\[
\int_{-\beta}^{\beta}\frac{d\phi}{\lambda^2\cos^2\phi+\lambda^{-2}\sin^2\phi}
=2\arctan(\lambda^{-2}\tan\beta)=2\arctan(\lambda^{-1}).
\]
Since \(\pi-2\beta=2\arctan(\lambda^{-1})\), the area becomes
\[
2(\lambda-\lambda^{-1})+4\arctan(\lambda^{-1}).
\]
For \(D=\lambda-\lambda^{-1}\ge0\), the elementary double-angle identity on the indicated branches gives \(4\arctan(\lambda^{-1})=\pi-2\arctan(D/2)\). Multiplying by the inverse affine Jacobian factor \(s\) proves the formula; \(\lambda=1\) follows directly or by continuity.

**Strict monotonicity, convexity, and sharpness.** Differentiating \(G\) gives
\[
G'(D)=2-\frac1{1+D^2/4}=1+\frac{D^2}{4+D^2},\qquad
G''(D)=\frac{8D}{(4+D^2)^2}>0\quad(D>0).
\]
For every \(D>0\), \(0<\arctan(D/2)<D/2\) implies \(D<G(D)<2D\). The Taylor expansion of arctangent gives \(G(D)/D\to1\) as \(D\downarrow0\); the boundedness of arctangent gives \(G(D)/D\to2\) as \(D\to\infty\). Both limits are realized as limits of actual admissible pairs, for example the unit disk and ellipses with semiaxes \(\lambda,\lambda^{-1}\), varying \(\lambda\downarrow1\) or \(\lambda\to\infty\). This establishes optimality of both constants.

## Verification
The standalone program `verify_elliptic_hull.py` constructs seven pairs of equal-area ellipses, including misaligned and sheared pairs; it independently approximates their convex hulls by dense polygonal samples and compares areas with the matrix-trace formula. It also checks the strict bounds at five mismatch scales. The numerical tests are corroborative; the proof of the continuum statement is the support-function calculation above, not finite sampling.

## Relationship to prior work
The convex-hull volume questions of Horváth and Lángi (2013) concern congruent copies under translations and reflections, with general extremal inequalities. The 2015 survey by Horváth reviews convex hulls of two bodies and the corresponding volume function, particularly translation and simplex questions. The present assertion instead gives an explicit full **equal-area centered ellipse-pair** area function governed by a single affine-invariant spectral mismatch, including noncongruent ellipses. A later geometric discussion of equal-area centered ellipses proves existence of a larger ellipse inside their hull but does not provide the hull's exact area or sharp spectral constants. These prior statements do not mathematically imply the boxed area identity without new geometry and integration.

## Limitations
The assertion does not address nonconcentric or unequal-area pairs, nor does it classify a maximum-area inscribed ellipse inside the hull. The value of the formula can be obtained by elementary support calculus once the affine reduction is identified; the claim of interest is the complete invariant classification and its sharp global constants. Literature searching is not a proof of first discovery: related historical formulas in unindexed sources or alternative conventions for shape matrices remain a priority risk. No independent external audit is claimed.

## References
1. Á. G. Horváth and Z. Lángi, *On the volume of the convex hull of two convex bodies*, arXiv:1302.6164, first posted 2013-02-25; openly accessible author manuscript: https://math.bme.hu/~ghorvath/convhullvolume6.pdf.
2. Á. G. Horváth, *Volume of convex hull of two bodies and related problems*, arXiv:1509.08859, first posted 2015-09-29; https://arxiv.org/abs/1509.08859.
3. *Prove that convex hull of two non-coinciding ellipses of equal area and with coinciding centers contains ellipse of larger area*, Mathematics Stack Exchange question 5015315 and answer, 2024-12-24/25; https://math.stackexchange.com/questions/5015315/.
