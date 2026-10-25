# Exact Convexity Phase Diagram for Curvature-Weighted Ellipse Offsets

## Finding
Let \(c(t)=(\alpha\cos t,\beta\sin t)\), where \(\alpha\ge\beta>0\), and let \(\kappa(t)\) and \(n(t)\) denote its Euclidean curvature and outward unit normal. Consider
\[
C_k(t)=c(t)+\frac{k}{\kappa(t)}n(t),\qquad k\ge0.
\]
Put \(x=(\alpha/\beta)^2\) and \(x_*=17+12\sqrt2=(3+2\sqrt2)^2\). For \(x>3/2\), let
\[
k_0=\frac{x}{2x-3}.
\]
For \(x\ge x_*\), let
\[
k_\pm=\frac{3x^2-22x+3\pm3(x-1)\sqrt{x^2-34x+1}}{12x^2-8x+12}.
\]
The complete convexity range is
\[
\begin{cases}
[0,\infty),&1\le x\le 3/2,\\
[0,k_0],&3/2<x<x_*,\\
[0,k_-]\cup[k_+,k_0],&x\ge x_*.
\end{cases}
\]
At \(x=x_*\), the roots coincide at \(k_-=k_+=1/5\), so the last union is simply \([0,k_0]\). For \(x>x_*\), the interval \((k_-,k_+)\) is genuinely nonconvex; convexity returns on \([k_+,k_0]\) and is lost again for \(k>k_0\). Boundary values remain convex, although the curvature vanishes at isolated parameters.

## Assumptions and scope
The result concerns only a plane ellipse and the family whose signed normal displacement is proportional to its radius of curvature. The parameter \(k\) is nonnegative and the axes are ordered so that \(\alpha\ge\beta\). No assertion is made for arbitrary convex curves, other distance laws, or convex surfaces in three-dimensional space.

Set
\[
q(t)=\alpha^2\sin^2t+\beta^2\cos^2t.
\]
Then \(\kappa(t)=\alpha\beta/q(t)^{3/2}\) and \(n(t)=(\beta\cos t,\alpha\sin t)/\sqrt{q(t)}\), so
\[
C_k(t)=\left(\left(\alpha+\frac{kq(t)}{\alpha}\right)\cos t,\left(\beta+\frac{kq(t)}{\beta}\right)\sin t\right).
\]

## Proof
Put \(u=\sin^2t\) and \(x=\alpha^2/\beta^2\). Direct differentiation gives
\[
\det(C_k'(t),C_k''(t))=\frac{\beta^2}{\sqrt{x}}Q_x(k,u),
\]
where
\[
\begin{aligned}
Q_x(k,u)={}&(k+1)(x+k(3-2x))\\
&+3k(x-1)(2kx-x+3)u\\
&+3k(2-k)(x-1)^2u^2.
\end{aligned}
\]
The determinant has the sign of the signed curvature. The curve is regular and simple for every \(k\ge0\): writing its coordinates as \((F(t)\cos t,G(t)\sin t)\), with \(F,G>0\), gives
\[
C_{k,1}C_{k,2}'-C_{k,2}C_{k,1}'=FG+\frac{2k(\alpha^2-\beta^2)^2}{\alpha\beta}\sin^2t\cos^2t>0.
\]
Thus its polar angle increases once around the origin, and convexity is equivalent to \(Q_x(k,u)\ge0\) for every \(u\in[0,1]\).

The endpoint values are
\[
Q_x(k,0)=(k+1)(x+k(3-2x)),\qquad Q_x(k,1)=x(k+1)(3kx-2k+1)>0.
\]
If \(x\le3/2\), both endpoints are positive for all \(k\ge0\). For \(k\le2\), the coefficients of \(u\) and \(u^2\) are nonnegative; for \(k>2\), the quadratic is concave in \(u\), so its minimum on \([0,1]\) is at an endpoint. Hence all such curves are convex.

For \(x>3/2\), the first endpoint is nonnegative exactly when \(k\le k_0=x/(2x-3)\); if \(k>k_0\), it is negative and the curve is nonconvex. It remains to test for an interior negative value before \(k_0\). For \(x\le3\), the coefficient of \(u\) is nonnegative for all \(k\), so the endpoint test suffices. For \(x>3\), put \(k_1=(x-3)/(2x)<1/2\). When \(k\ge k_1\), the coefficient of \(u\) is nonnegative; the same endpoint argument applies, including the concave case \(k>2\). When \(0<k<k_1\), the quadratic is strictly convex in \(u\) and its vertex lies in \((0,1)\). Its discriminant in \(u\) is
\[
\Delta_u=3k(2k-1)(x-1)^2R_x(k),
\]
where
\[
R_x(k)=(6x^2-4x+6)k^2+(-3x^2+22x-3)k+8x.
\]
The discriminant of \(R_x\) as a quadratic in \(k\) is
\[
9(x-1)^2(x^2-34x+1).
\]
For \(x>3\), this is nonnegative exactly when \(x\ge x_*=17+12\sqrt2\). If \(3<x<x_*\), then \(R_x(k)>0\) for all real \(k\), so no interior nonconvex interval occurs. At \(x=x_*\), it has the double root \(k=1/5\), giving zero curvature but no negative minimum. If \(x>x_*\), its roots are \(k_-\) and \(k_+\). They lie in \((0,k_1)\): the vertex \(v=(3x^2-22x+3)/(12x^2-8x+12)\) is positive and
\[
k_1-v=\frac{3(x-1)(x^2+x+6)}{4x(3x^2-2x+3)}>0.
\]
Moreover, \(R_x(0)>0\), \(R_x(k_1)=27(x-1)^2(x+1)/(2x^2)>0\), and the minimum of \(R_x\) is negative. Thus both roots lie below \(k_1\). Also
\[
k_0-k_1=\frac{9(x-1)}{2x(2x-3)}>0,
\]
so \(k_+<k_1<k_0\). Since \(2k-1<0\) on \((0,k_1)\), \(\Delta_u>0\) precisely between the roots, making the interior minimum negative precisely for \(k_-<k<k_+\). At the roots the minimum is zero; outside that interval it is nonnegative. This proves the classification.

## Verification
The determinant identity and discriminant factorization are exact algebraic identities. The proof reduces global convexity to the sign of a quadratic on \([0,1]\); no finite sampling is used as proof. As a consistency illustration, when \(\alpha/\beta=10\), the thresholds are approximately \(k_-=0.0308088\), \(k_+=0.4356375\), and \(k_0=0.5076142\), showing the additional nonconvex window and subsequent convexity recovery.

## Relationship to prior work
Veerman's 2023 paper introduces this same family for ellipse cross-sections of cylinders whose projections preserve geodesics. Its Section 6 notes that the curves cease to be convex for sufficiently large \(k\), but gives no exact axis-ratio threshold and does not describe the additional nonconvex interval and convexity recovery for highly eccentric ellipses. Hinterleitner's work on geodesic mappings of surfaces of revolution studies a different metric-deformation framework, not this curvature-weighted normal-offset family or its convexity range. The present result is the exact sign/convexity classification for this family, not a solution of the general surface-projection problem.

## Limitations
The result is confined to ellipses and the stated curvature-weighted displacement. It does not classify arbitrary convex curves or settle whether an arbitrary smooth convex surface in \(\mathbb R^3\) admits a geodesic-preserving projection from an exterior surface. The literature comparison is targeted rather than an exhaustive proof that no equivalent statement exists elsewhere.

## References
1. J. J. P. Veerman, “Geodesics on Regular Constant Distance Surfaces,” arXiv:2309.05808v1 (first public version 2023-09-11), especially Section 6. https://arxiv.org/abs/2309.05808 ; https://doi.org/10.1007/s00022-023-00690-6
2. I. Hinterleitner, “On Global Geodesic Mappings of \(n\)-Dimensional Surfaces of Revolution,” arXiv:1103.6128v1 (2011). https://arxiv.org/abs/1103.6128
