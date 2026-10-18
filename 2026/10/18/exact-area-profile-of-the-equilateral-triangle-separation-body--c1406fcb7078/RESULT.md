# Exact area profile of the equilateral-triangle separation body

## Finding

Let \(T\) be the equilateral triangle of side length \(2\) with vertices
\[
A=(0,2/\sqrt3),\qquad B=(-1,-1/\sqrt3),\qquad C=(1,-1/\sqrt3).
\]
Its isotropic separation body, in the normalized mean-width convention, is
\[
T[\delta]=\{x\in\mathbb R^2:W(\operatorname{conv}(T\cup\{x\}))-W(T)\le\delta\},\qquad\delta\ge0,
\]
where planar mean width is perimeter divided by \(\pi\). Put \(q=\pi\delta\) and define
\[
\begin{aligned}
u&=\frac{q(q+4)}{2(q+3)},&a_f&=1+\frac q2,&b_f&=\sqrt{a_f^2-1},\\
a_v&=2+\frac q2,&b_v&=\sqrt{a_v^2-1},&
\varphi&=\arcsin\!\left(\frac{\sqrt3\,u}{2b_f}\right),\\
\psi&=\arcsin\!\left(\frac{u}{2a_v}\right).
\end{aligned}
\]
The expression for \(\varphi\) is used for \(q>0\), with its continuous value \(0\) at \(q=0\). For every \(\delta\ge0\), the **exact area** is
\[
\boxed{\operatorname{Area}(T[\delta])
=\sqrt3+\frac32\left[a_fb_f(\pi-2\varphi)+2a_vb_v\psi\right].}
\]
For every \(\delta>0\), the boundary consists of exactly six nondegenerate ellipse arcs, alternating between three side arcs and three vertex arcs. For small parameters,
\[
\operatorname{Area}(T[\delta])
=\sqrt3+\frac{3\pi^{3/2}}2\delta^{1/2}
+\frac{15\pi^{5/2}}{16}\delta^{3/2}
-\frac{2\sqrt3\,\pi^2}{9}\delta^2
+O(\delta^{5/2}).
\]
In particular the linear term vanishes. Similarity and scaling give the area for **every** equilateral triangle: for side length \(L>0\), multiply the displayed side-\(2\) area by \((L/2)^2\) after replacing \(\delta\) by \(2\delta/L\).

## Assumptions and scope

The body uses the *isotropic* translation-invariant hyperplane measure with normalized uniform spherical directional law. Schneider's planar identity reads
\[
m(K,x)=\frac{\operatorname{Per}(\operatorname{conv}(K\cup\{x\}))-\operatorname{Per}(K)}\pi.
\]
Thus the condition in the theorem is precisely \(\operatorname{Per}(\operatorname{conv}(T\cup\{x\}))-6\le q\). The area is ordinary two-dimensional Lebesgue area. All parameter ranges are \(q\ge0\), \(\delta\ge0\); no stochastic expectations, arbitrary triangles, or anisotropic measures are claimed.

## Proof

**1. Exterior chamber decomposition.** The three complete edge-supporting lines divide the plane into the interior and six exterior chambers. In the chamber adjacent to side \(BC\), the only visible side is \(BC\); writing \(z\) for the external point, its convex hull has perimeter increment
\[
|z-B|+|z-C|-2.
\]
In the chamber beyond vertex \(A\), the visible polygonal path is \(B\!\to A\!\to C\), of length \(4\). Its increment is
\[
|z-B|+|z-C|-4.
\]
Hence the boundary in the side chamber is an ellipse with foci \(B,C\), center \(M=(0,-1/\sqrt3)\), horizontal semiaxis \(a_f\), and vertical semiaxis \(b_f\). The boundary in the vertex chamber beyond \(A\) is a concentric ellipse with horizontal semiaxis \(a_v\) and vertical semiaxis \(b_v\). Rotation by \(2\pi/3\) gives the other four arcs.

**2. Exact arc-transition parameter.** On the extension of \(AB\) beyond \(B\), parameterize a point at distance \(t\ge0\) from \(B\) by
\[
z=B+\frac t2(B-A)=(-1-t/2,-1/\sqrt3-\sqrt3 t/2).
\]
Since \(|z-C|=\sqrt{t^2+2t+4}\), the separation boundary equation is
\[
t+\sqrt{t^2+2t+4}-2=q.
\]
The left side increases strictly from zero; solving and checking the nonnegative square-root branch gives the unique solution \(t=u=q(q+4)/(2(q+3))\). It follows that the two endpoints of the \(BC\)-side arc are
\[
(-1-u/2,-1/\sqrt3-\sqrt3u/2),\quad(1+u/2,-1/\sqrt3-\sqrt3u/2).
\]
The two endpoints of the upper vertex arc beyond \(A\) are
\[
(-u/2,2/\sqrt3+\sqrt3u/2),\quad(u/2,2/\sqrt3+\sqrt3u/2).
\]
The endpoint equations also establish the stated inverse-sine arguments lie in the interval \([0,1]\). For \(q>0\), each of the six arcs has positive length.

**3. Ellipse Green integrals.** Set \(h=1/\sqrt3\). Parametrize either ellipse by \(x=a\cos\theta,\ y=-h+b\sin\theta\) (center \(M\) fixed). The exact differential is
\[
x\,dy-y\,dx=(ab-ah\sin\theta)\,d\theta.
\]
Following the counterclockwise boundary orientation, the lower side arc runs from \(\theta=\pi+\varphi\) to \(\theta=2\pi-\varphi\). Its Green integral is
\[
I_f=a_fb_f(\pi-2\varphi)+2h+hu.
\]
The upper vertex arc runs from \(\theta=\pi/2-\psi\) to \(\theta=\pi/2+\psi\). Its Green integral is
\[
I_v=2a_vb_v\psi-hu.
\]
The exact terms proportional to \(u\) cancel, so Green's theorem and threefold symmetry give
\[
\operatorname{Area}(T[\delta])=\frac12\cdot3(I_f+I_v)
=\sqrt3+\frac32\left[a_fb_f(\pi-2\varphi)+2a_vb_v\psi\right].
\]
For \(q=0\) the limit is the original triangle of area \(\sqrt3\), establishing the endpoint as well.

**4. Small-parameter expansion.** Writing \(q=s^2\) and expanding the explicit rational, square-root, and inverse-sine expressions at \(s=0^+\) yields
\[
\operatorname{Area}(T[q/\pi])=\sqrt3+\frac{3\pi}{2}s+\frac{15\pi}{16}s^3-\frac{2\sqrt3}{9}s^4+O(s^5).
\]
The stated expansion follows on substituting \(s=\sqrt{\pi\delta}\). The lack of an order-\(s^2\) term follows from exact cancellation of face and corner contributions, not merely a numerical fit.

## Verification

The included standalone `verify.py` uses only the Python standard library. It reconstructs \(\operatorname{conv}(T\cup\{z\})\) by an independent monotone-chain convex hull, checks the perimeter level at the six-chamber transition for six positive parameters, and finds radial boundaries by bisection in \(720\) directions. Direct polar-area quadrature then agrees with the exact formula with observed errors below \(3\times10^{-6}\) for \(q=0.01,0.1,0.5,1,3,10\). The checker prints `VERIFY_OK equilateral triangle separation-body all-parameter area` after passing. These computations test the formula; the universal statement follows from the geometric proof, not from finite sampling.

## Relationship to prior work

Schneider introduced separation bodies and proved the planar perimeter normalization and the general observation that a polygon's isotropic separation-body boundary consists of ellipse arcs in the chambers of its edge-line arrangement. This **does not supply** the six-arc joining parameter or the all-parameter area formula above. Böröczky and Schneider previously introduced the same mean-width sublevel construction in random circumscribed-polytope approximation, without a triangular exact profile.

A separately published exact **square** separation-body profile uses eight different ellipse arcs and a different full area formula; it neither gives the triangular profile nor dominates it by affine equivalence, because the objects are different and mean width is not affinely invariant. Exact floating-body profiles for triangles concern an *interior cap-volume sublevel construction*, not the exterior perimeter-increment level set defined here. Thus the present profile is a complementary canonical noncentrally symmetric example rather than a special case of those formulas.

The all-parameter triangle area is pertinent to explicit area-excess benchmarks in the Poisson hyperplane cell setting of Schneider's volume-comparison theorem. This result does **not** itself compute the random cell's expectation.

## Limitations

The closed form is proved only for equilateral Euclidean triangles and the isotropic measure. It is not an area formula for arbitrary triangles, general polygons, volume-based illumination bodies, or anisotropic separation bodies. The asymptotic expansion is for the small positive parameter and does not by itself imply any exact Poisson-cell expected area. Targeted bibliographic and research-record searches did not uncover the same triangle formula, but an unindexed equivalent calculation in historical stochastic-geometry literature remains a residual originality risk. Independent validation is not claimed.

## References

R. Schneider, *Separation bodies: a conceptual dual to floating bodies*, arXiv:1910.12670 (first submitted 2019-10-28), Monatshefte für Mathematik 193 (2020), 611–622, DOI: 10.1007/s00605-020-01443-2.

K. J. Böröczky and R. Schneider, *The mean width of circumscribed random polytopes*, arXiv:0901.3343 (first submitted 2009-01-21), Canadian Mathematical Bulletin 53 (2010), 614–628.

*Exact area profile of the square separation body*, public mathematical research record dated 2026-10-04; exact comparison: the square formula has eight ellipse arcs rather than the six of an equilateral triangle.
