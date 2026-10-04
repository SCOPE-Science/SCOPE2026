# Exact algebraic coordinates of the \(30^\circ\)-\(60^\circ\)-\(90^\circ\) thermodynamic center
## Finding
For the triangle \(T=\operatorname{conv}\{(0,0),(1,0),(0,\sqrt3)\}\), let its thermodynamic center be the unique maximum of the first Dirichlet Laplacian eigenfunction. Define \(c_*\) as the unique zero in \((93/100,47/50)\) of
\[
Q(c)=100c^6-120c^4+30c^2-1,
\]
and define
\[
d_*=-20c_*^5+24c_*^3-5c_*.
\]
Then the thermodynamic center is exactly
\[
(x_*,y_*)=\left(rac{3}{\pi}rccos c_*,rac{\sqrt3}{\pi}rccos d_*ight).
\]
Numerically,
\[
x_*=0.3558473606263811208579681\ldots,\qquad
y_*=0.4255359610370576630888604\ldots.
\]
The second algebraic cosine also obeys
\[
500d_*^6-600d_*^4+186d_*^2-5=0.
\]

## Assumptions and scope
The domain is the open \(30^\circ\)-\(60^\circ\)-\(90^\circ\) triangle with vertices \((0,0)\), \((1,0)\), and \((0,\sqrt3)\). The thermodynamic center is used in Finch's sense: the unique maximizer of the positive first eigenfunction for the Dirichlet Laplacian. No claim is made about an exact formula for arbitrary triangles or about other proposed triangle centers.

Set
\[
X=rac{\pi x}{3},\qquad Y=rac{\pi y}{\sqrt3}.
\]
The triangle becomes \(X>0\), \(Y>0\), and \(3X+Y<\pi\).

## Proof
Finch records the first eigenfunction in the form
\[
u=\sin X\sin(3Y)+\sin(4X)\sin(2Y)+\sin(5X)\sin Y.
\]
The three summands all have eigenvalue \(28\pi^2/9\). Elementary product-to-sum identities give the factorization
\[
u=4\sin X\sin Y\,(\cos X+\cos Y)(\cos 3X+\cos Y),
\]
or equivalently
\[
u=16\sin X\sin Y
\cosrac{X+Y}{2}\cosrac{X-Y}{2}
\cosrac{3X+Y}{2}\cosrac{3X-Y}{2}.
\]
Every displayed factor is positive in the open triangle and the product vanishes on its boundary. Hence this is the positive first eigenfunction up to scaling.

Moreover, \(\log u\) is strictly concave on the triangle. Indeed, \(\log\sin X+\log\sin Y\) has negative-definite Hessian, while each \(\log\cos\) term above is concave because its affine argument lies in \((-\pi/2,\pi/2)\). Thus \(u\) has at most one interior critical point, and since \(u>0\) inside and \(u=0\) on the boundary, that critical point is the unique global maximum.

Write \(c=\cos X\), \(d=\cos Y\), and \(c_3=4c^3-3c\). Dividing the two logarithmic-gradient equations by the positive sines gives
\[
rac{d}{1-d^2}=rac{1}{c+d}+rac{1}{c_3+d},
\]
\[
rac{c}{1-c^2}=rac{1}{c+d}+rac{3(4c^2-1)}{c_3+d}.
\]
After clearing positive denominators these equations are
\[
E_Y=4c^4d+8c^3d^2-4c^3-3c^2d-4cd^2+2c+3d^3-2d=0,
\]
\[
E_X=20c^5+16c^4d-25c^3-16c^2d+cd^2+6c+2d=0.
\]
Now put \(d=-20c^5+24c^3-5c\). Direct exact expansion gives
\[
E_Y=-4c(c-1)^2(c+1)^2(60c^4-32c^2+3)Q(c),
\]
and
\[
E_X=4c(c-1)^2(c+1)^2Q(c).
\]
Therefore the chosen zero \(c_*\) of \(Q\), together with \(d_*\), solves both critical equations.

The interval \((93/100,47/50)\) contains exactly one zero of \(Q\): the endpoint values have opposite signs and \(Q'(c)=60c(10c^4-8c^2+1)>0\) throughout this interval. On the same interval, \(0<d_*<1\), and
\[
d_*+4c_*^3-3c_*=-4c_*(c_*-1)(c_*+1)(5c_*^2-2)>0.
\]
Thus the corresponding \((X,Y)\) lies strictly inside \(X>0\), \(Y>0\), \(3X+Y<\pi\), all denominators used above are positive, and the point is a genuine interior critical point. Strict concavity makes it the unique global maximum.

Finally, substitution of \(d=-20c^5+24c^3-5c\) shows that \(500d^6-600d^4+186d^2-5\) is divisible by \(Q(c)\), proving the stated polynomial equation for \(d_*\).

## Verification
The accompanying `verify.py` uses only the Python standard library. It checks the two exact polynomial identities above with rational/integer polynomial arithmetic, verifies by a Sturm sequence that \(Q\) has exactly one root in \((93/100,47/50)\), bisects that root numerically, reconstructs \(d_*\), and confirms the quoted coordinates. The numerical stage is diagnostic; the uniqueness and critical-point arguments are analytic.

## Relationship to prior work
Finch introduced the thermodynamic center in this triangle-center context and printed the same first eigenfunction together with only numerical coordinates for the \(30^\circ\)-\(60^\circ\)-\(90^\circ\) case. The present result upgrades that numerical location to an exact algebraic-cosine characterization.

Damle and Peterson develop complete trigonometric eigenstructures for the \(30^\circ\)-\(60^\circ\)-\(90^\circ\) triangle, providing the spectral background for such formulas, but the inspected paper does not study the hot-spot maximizer. Brasco, Magnanini, and Salani study uniqueness and geometric localization of hot spots for convex conductors; their result supplies general context rather than these exact coordinates.

## Limitations
The claim is specific to this normalized \(30^\circ\)-\(60^\circ\)-\(90^\circ\) triangle. It does not classify thermodynamic centers for arbitrary triangles and does not claim that algebraic-cosine coordinates persist outside triangles with explicit trigonometric eigenfunctions. Literature searches cannot exclude an unindexed or differently phrased earlier derivation of the same exact coordinates.

## References
1. S. R. Finch, *In Limbo: Three Triangle Centers*, arXiv:1406.0836v1, 2014.
2. A. Damle and G. C. Peterson, *Understanding the Eigenstructure of Various Triangles*, SIAM Undergraduate Research Online 3 (2010), 187–208.
3. L. Brasco, R. Magnanini, and P. Salani, *The location of the hot spot in a grounded convex conductor*, Indiana Univ. Math. J. 60 (2011), 633–659; arXiv:1012.4742.
