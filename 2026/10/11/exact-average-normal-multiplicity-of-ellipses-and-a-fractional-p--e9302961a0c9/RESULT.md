# Exact average normal multiplicity of ellipses and a fractional phase transition

## Finding
For a Euclidean ellipse with semiaxes \(a\ge b>0\), let \(N_E(p)\) be the number of distinct boundary feet of perpendiculars from an interior point \(p\); equivalently, count boundary points whose Euclidean normal line contains \(p\). For an area-uniform point \(P\) in the ellipse, define \(M(r)=\mathbb E N_E(P)\), with aspect ratio \(r=a/b\). Then \(M\) depends only on \(r\), is strictly increasing on \([1,\infty)\), and satisfies \(M(1)=2\) and \(2<M(r)<4\) for finite \(r>1\).

For \(1\le r\le\sqrt 2\), its exact value is
\[
M(r)=2+\frac{3(r^2-1)^2}{4r^2}.
\]
For \(r>\sqrt2\), put
\[
\delta=r^2-1,\quad A=\frac\delta r,\quad B=\delta,\quad
v=\frac{2r^2-1}{r^4-1},\quad \phi=\arcsin\sqrt v,
\]
\[
x_*=A(1-v)^{3/2},\quad y_*=Bv^{3/2},\quad
F(t)=\frac t{16}-\frac{\sin(2t)}{64}-\frac{\sin(4t)}{64}+\frac{\sin(6t)}{192},
\]
\[
J(r)=\frac12\left(x_*y_*+r\arcsin\frac{x_*}{r}\right)+3ABF(\phi).
\]
Then the complete elementary formula is
\[
M(r)=2+\frac{8J(r)}{\pi r}.
\]
The transition at \(r=\sqrt2\) is genuinely nonanalytic: letting \(\varepsilon=r^2-2\downarrow0\),
\[
M(r)=2+\frac{3(r^2-1)^2}{4r^2}
-\frac8{5\pi}\left(\frac23\right)^{3/2}\varepsilon^{5/2}
+O(\varepsilon^{7/2}).
\]
Thus \(M\) is twice continuously differentiable there but not three times continuously differentiable. At high eccentricity,
\[
M(r)=4-\frac{352\sqrt2}{15\pi r^3}+o(r^{-3}).
\]

## Assumptions and scope
This is a population expectation with respect to planar Lebesgue area, not boundary arclength or a finite random sample. Normal feet are distinct boundary contact points, not oriented rays; normal-line multiplicity is counted almost everywhere. Points on the evolute, symmetry axes, or other discriminant sets have zero area and do not affect the mean. The body is a nondegenerate filled Euclidean ellipse; similarity permits normalization to semiaxes \((r,1)\). The circular case is interpreted separately, with two antipodal normal feet for almost every interior point. No statement is made for arbitrary smooth convex bodies.

## Proof
**1. Normal multiplicity and the evolute.** In coordinates \(E_r=\{(x,y):x^2/r^2+y^2\le1\}\), write \(\delta=r^2-1\). The evolute (normal-line envelope) is the astroid
\[
\mathcal C_r=\left\{(x,y):\left|\frac{x}{A}\right|^{2/3}+\left|\frac yB\right|^{2/3}=1\right\},
\qquad A=\frac\delta r,\quad B=\delta.
\]
For \(r>1\), a generic point inside the astroid has four normal feet and a generic point outside has two; this classical ellipse-normal classification also follows by counting real solutions of the normal-contact quartic, as explained below. Therefore, with \(\mathcal A_r\) denoting the closed region enclosed by the evolute,
\[
M(r)=2+\frac{2\operatorname{Area}(E_r\cap\mathcal A_r)}{\pi r}.
\tag{1}
\]
For reference, writing a boundary foot as \((r\cos\theta,\sin\theta)\), the tangent-perpendicularity equation for a point \((X,Y)\) is
\[
-rX\sin\theta+Y\cos\theta+\delta\sin\theta\cos\theta=0.
\]
Its substitution \(z=\tan(\theta/2)\) yields the polynomial
\[
-Yz^4-2(rX+\delta)z^3+2(\delta-rX)z+Y=0.
\]
Except on an algebraic discriminant set of area zero, its distinct real projective roots count the normal feet, giving the preceding 2-versus-4 classification and its astroid boundary.

**2. Entirely internal regime.** The four axial cusps are \((\pm A,0)\), \((0,\pm B)\). If \(r^2\le2\), all belong to \(E_r\), which is convex; the astroid lies inside their convex hull, hence inside \(E_r\). The full astroid area is \(3\pi AB/8\), obtained from the parametrization \((A\cos^3t,B\sin^3t)\). Equation (1) then gives the first branch.

**3. Partial overlap and exact integration.** For \(r^2>2\), each quadrant contains exactly one transverse crossing of the ellipse and the astroid. Set \(v=(y/B)^{2/3}\), so the astroid point is \((A(1-v)^{3/2},Bv^{3/2})\). The crossing equation is
\[
\delta^2\left[\frac{(1-v)^3}{r^4}+v^3\right]=1.
\tag{2}
\]
Its left side decreases and then increases on \([0,1]\), with its value at zero smaller than one and at one greater than one; thus the crossing is unique. Direct substitution gives the solution \(v=(2r^2-1)/(r^4-1)\). In the first quadrant, \(y_{E_r}(x)=\sqrt{1-x^2/r^2}\) for \(0\le x\le x_*\), while \(y_{\mathcal A_r}(x)=B[1-(x/A)^{2/3}]^{3/2}\) for \(x_*\le x\le A\). Hence the first-quadrant overlap area is
\[
J=\int_0^{x_*}\sqrt{1-x^2/r^2}\,dx+
\int_{x_*}^A B[1-(x/A)^{2/3}]^{3/2}\,dx.
\]
The first integral is \((x_*y_*+r\arcsin(x_*/r))/2\). In the second substitute \(x=A\cos^3t\); since \(F'(t)=\sin^4t\cos^2t\), it equals \(3ABF(\phi)\). Fourfold symmetry gives \(\operatorname{Area}(E_r\cap\mathcal A_r)=4J\), proving the second branch.

**4. Strict monotonicity.** In normalized disk coordinates \((u,y)=(x/r,y)\), the evolute has horizontal and vertical semiaxes \(1-r^{-2}\) and \(r^2-1\), both strictly increasing for \(r>1\). The overlap area with the unit disk therefore increases strictly, since each strict parameter increase adds an open positive-area set until the disk limit. This proves strict growth of \(M\), with limits 2 and 4.

**5. Sharp fractional onset.** Let \(\varepsilon=r^2-2\downarrow0\). The area of the full astroid exceeds the overlap by four congruent thin caps. In the first quadrant the excluded cap has horizontal extent
\[
x_*=\frac1{\sqrt2}\left(\frac{2\varepsilon}{3}\right)^{3/2}[1+O(\varepsilon)].
\]
Write \(x=x_*z\). Uniformly for \(0\le z\le1\), the astroid-minus-ellipse vertical height has leading term \(\varepsilon(1-z^{2/3})\), and an \(O(\varepsilon^2)\) remainder. Thus the excluded first-quadrant area is
\[
C_\varepsilon=\frac25\frac1{\sqrt2}\left(\frac23\right)^{3/2}\varepsilon^{5/2}+O(\varepsilon^{7/2}),
\]
because \(\int_0^1(1-z^{2/3})\,dz=2/5\). Subtracting \(8C_\varepsilon/(\pi r)\) from the analytic full-astroid branch yields the stated coefficient. All remaining terms are smooth functions of \(\varepsilon\) times half-integral powers beginning at \(7/2\), by the same change of variables; hence the function has two continuous derivatives at the threshold and an unbounded one-sided third derivative.

**6. Elongated regime.** In disk coordinates, set \(y=t/r\) near the rightmost disk point. The disk and astroid right boundaries satisfy uniformly for bounded \(t\),
\[
r^2(u_E-u_{\mathcal A})\longrightarrow 1+\frac32 t^{2/3}-\frac12t^2.
\]
The positive part has support \(0\le t\le2\sqrt2\), and the crossing endpoint converges to \(2\sqrt2\). The first-quadrant disk-minus-astroid area equals
\[
\frac1{r^3}\int_0^{2\sqrt2}\left(1+\frac32t^{2/3}-\frac12t^2\right)dt+o(r^{-3})
=\frac{44\sqrt2}{15r^3}+o(r^{-3}).
\]
Fourfold symmetry and equation (1), expressed in unit-disk coordinates, give \(4-M=(8/\pi)\) times this quarter-area and yield the stated constant.

## Verification
A companion Python script, `verify_normals.py`, evaluates the explicit formula and separately computes mean multiplicity via normal-map Jacobian quadrature, without integrating astroid overlap. It independently counts normal feet of thousands of generic area-uniform sampled points by finding real roots of the normal-contact quartic and tests both limiting constants. Running `python verify_normals.py` returned `VERIFY_OK 4439 independent finite checks; direct Jacobian quadrature and normal-polynomial roots agree`. The exact crossing identity (2) was also symbolically simplified to one. These finite tests are not a substitute for the proof, and floating-point root separation may fail near the measure-zero evolute, intentionally avoided in the sampled tests.

## Relationship to prior work
Santaló's average-normal question and the general normal multiplicity framework are reviewed by Domokos and Lángi (2014, arXiv:1406.0813v1). Hartmann and Jantzen (2010), the MathWorld ellipse-evolute reference, and Aliyev (2023, arXiv:2305.06065v1) describe the ellipse's 2-versus-4 normal classification and the geometry of its evolute, including the known axis-ratio crossing. Those facts are inputs, not claimed as new. The additional conclusion here is the complete area-averaged normal-count law for every ellipse, its strict monotonicity, the critical fractional-power singularity, and the sharp elongated limit. Older general papers by Hann (1993) and Hug (1995) could not be inspected fully, so equivalent earlier evaluations remain a genuine originality uncertainty.

## Limitations
The mean requires exact area sampling inside a nondegenerate ellipse. It is not a finite-sample estimator or a statement about the normal multiplicity of every individual point. Smoothness across the critical value is only claimed through order two. Numerical verification uses finite floating-point tests; older inaccessible primary literature prevents any claim of exhaustive historical novelty. No external independent audit has been performed.

## References
1. G. Domokos and Z. Lángi, *On the average number of normals through points of a convex body*, arXiv:1406.0813v1, publicly submitted 2014-06-03. https://arxiv.org/abs/1406.0813
2. Y. Aliyev, *Apollonius Problem and Caustics of an Ellipsoid*, arXiv:2305.06065v1. https://arxiv.org/abs/2305.06065
3. F. Hartmann and R. Jantzen, *Apollonius's Ellipse and Evolute Revisited*, Mathematical Association of America, *Convergence*, August 2010. https://old.maa.org/press/periodicals/convergence/apolloniuss-ellipse-and-evolute-revisited-the-alternative-approach-to-the-evolute
4. E. W. Weisstein, *Ellipse Evolute*, MathWorld. https://mathworld.wolfram.com/EllipseEvolute.html
5. K. Hann, *The average number of normals through a point in a convex body and a related Euler-type identity*, Geometriae Dedicata 48 (1993), 27–55.
6. D. Hug, *On the mean number of normals through a point in the interior of a convex body*, Geometriae Dedicata 55 (1995), 319–340.
