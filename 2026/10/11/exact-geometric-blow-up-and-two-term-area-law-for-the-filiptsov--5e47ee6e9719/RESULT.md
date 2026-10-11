# Exact geometric blow-up and two-term area law for the Filiptsov algebraic limit cycle

## Finding
For the classical Filiptsov quadratic system with \(0<a<3/13\), the Euclidean area \(A(a)\) enclosed by its known algebraic limit cycle obeys the sharp two-term law
\[
 A(a)=\frac{81}{560a^4}-\frac{81}{280a^3}+O(a^{-2})\quad(a\downarrow0).
\]
The entire cycle admits an explicit affine blow-up: after \((x,y)\mapsto(a^2x,a^2y)\), it converges in Hausdorff distance to the singular closed loop
\[
 (X(z),Y(z))=\left(\frac23z^2(3-2z),\frac23z^3(3-2z)\right),\qquad0\le z\le\frac32.
\]
Thus the positive-coordinate extrema satisfy \(a^2\max x\to2/3\) and \(a^2\max y\to729/1024\). These are geometric quantities in the original affine coordinates, not changes of orbital time.

## Assumptions and scope
Take \(0<a<3/13\) and \(s=1+a\). The vector field is
\[
\begin{aligned}
\dot x&=6sx+2y-6(2+a)x^2+12xy,\\
\dot y&=15sy+3asx^2-2(9+5a)xy+16y^2.
\end{aligned}
\]
Its invariant quartic is \(f_a(x,y)=3s(ax^2+y)^2+2y^2(2y-3sx)\). Previous work proves that the positive-quadrant oval \(\Gamma_a\subset\{f_a=0\}\) is the system's unique limit cycle for this parameter range and that it escapes to infinity as \(a\downarrow0\). We use those established orbit-identification facts and claim only the quantitative geometric assertions above. Area means ordinary unoriented Euclidean planar area enclosed by the oval. All limits are along positive real \(a\to0\).

## Proof
**Exact radial graph.** Put \(X=a^2x\), \(Y=a^2y\), and \(z=y/x=Y/X\) in the positive quadrant. For \(X>0\), multiplying \(f_a(X/a^2,zX/a^2)=0\) by \(a^6/X^2\) yields
\[
 3sX^2-2zh_a(z)X+3sa^2z^2=0,\qquad h_a(z)=3sz-2z^2-3sa.
\]
Set \(d_a=3sa\) and
\[
 z_\pm=\frac{3s\pm\sqrt{3s(3-13a)}}4.
\]
Since \(h_a(z)-d_a=2(z-z_-)(z_+-z)\), the positive roots exist precisely for \(z_-\le z\le z_+\); explicitly,
\[
 X_\pm(z)=\frac{z}{3s}\left[h_a(z)\pm\sqrt{h_a(z)^2-d_a^2}\right],
 \quad Y_\pm(z)=zX_\pm(z).
\]
Indeed, on the stated interval \(h_a\ge d_a>0\), and elsewhere there is no pair of positive roots. The two branches meet at both turning slopes, giving precisely the previously identified positive-quadrant oval. Their product is \(X_+(z)X_-(z)=a^2z^2\), so \(0<X_-(z)\le az\).

**Area.** The coordinate map \((X,z)\mapsto(X,Y=zX)\) has Jacobian \(X\). Its domain between the branches is \(\{z_-\le z\le z_+,\ X_-(z)\le X\le X_+(z)\}\). Therefore
\[
\begin{aligned}
a^4A(a)&=\frac12\int_{z_-}^{z_+}(X_+^2-X_-^2)\,dz\\
 &=\frac{2}{9s^2}\int_{z_-}^{z_+}
 z^2h_a(z)\sqrt{h_a(z)^2-d_a^2}\,dz.
\end{aligned}
\]
This holds for every \(0<a<3/13\), not merely asymptotically.

**Two-term expansion with controlled remainder.** Since \(h_a\ge d_a\) on the integration interval,
\[
0\le h_a^2-h_a\sqrt{h_a^2-d_a^2}
=\frac{h_ad_a^2}{h_a+\sqrt{h_a^2-d_a^2}}\le d_a^2.
\]
The interval length and \(z\) are uniformly bounded, so replacing the square-root factor in the exact integral by \(h_a\) incurs error \(O(a^2)\). The endpoints satisfy \(z_-=O(a)\) and \(z_+=3/2+O(a)\). In an \(O(a)\) neighborhood of either endpoint of \([0,3/2]\), \(h_a=O(a)\), so replacing the variable interval in the resulting polynomial integral by \([0,3/2]\) incurs only \(O(a^3)\). Hence
\[
 a^4A(a)=\frac{2}{9s^2}\int_0^{3/2}z^2(3sz-2z^2-3sa)^2\,dz+O(a^2).
\]
Direct rational polynomial integration gives
\[
\frac{2}{9s^2}\int_0^{3/2}z^2(3sz-2z^2-3sa)^2\,dz
 =\frac{9(140a^4-35a^3-49a^2+9)}{560(1+a)^2}
 =\frac{81}{560}-\frac{81}{280}a+O(a^2),
\]
proving the claimed expansion. These error bounds are uniform for \(a\) in a sufficiently small fixed positive interval.

**Limit loop and coordinate extrema.** Since \(z_-\to0\), \(z_+\to3/2\), and \(h_a(z)\to z(3-2z)\), the outer graph converges uniformly (after continuous endpoint parametrization) to \(X_0(z)=2z^2(3-2z)/3\). The inner graph obeys \(0<X_-\le az\), so collapses uniformly to the origin. This proves Hausdorff convergence of the two-branch cycle to the displayed closed loop. The limiting parametrization is injective on \((0,3/2)\), with the two endpoints coinciding only at the origin, hence is a Jordan loop. Elementary differentiation shows \(X_0\) has unique maximum \(2/3\) at \(z=1\), while \(zX_0\) has unique maximum \(729/1024\) at \(z=9/8\). Uniform graph convergence and the collapsing inner branch imply convergence of the coordinate maxima.

## Verification
The accompanying standalone `verify_filiptsov_area.py` uses exact rational polynomial operations to check the leading area coefficient and its linear correction, and numerical quadrature of the *exact* area expression at several positive values of \(a\) to check the predicted convergence. It does not replace the infinite-parameter algebraic inequalities, which are proved above. The invariant curve and vector field coefficients were independently cross-checked against the 2022 primary text. The conclusion is a theorem about the explicit quartic oval; no claim is made about period, stability changes, or uniqueness beyond the cited earlier results.

## Relationship to prior work
Filiptsov originally exhibited this degree-four algebraic limit cycle. Llibre, Oliveira and Zhao (2021, Theorem 2(b)) explicitly describe its escape to a heteroclinic cycle involving infinity as \(a\downarrow0\); that qualitative singular degeneration is **already known**. Gasull and Giacomini (2022 preprint, Theorem 1.2 and Case 3) give the invariant quartic and another uniqueness treatment. Neither examined result supplies the two-term Euclidean area divergence or a sharp affine-rescaled limiting loop with coordinate-extremum constants. The current theorem refines, rather than replaces, the known qualitative bifurcation picture. The geometry is sensitive to affine normalization: it is not a claim of affine-invariant shape or dynamical conjugacy.

## Limitations
The analysis concerns the named explicit positive-quadrant algebraic oval and the endpoint \(a\downarrow0\); it gives no classification of other polynomial families. The proof is mathematical rather than an independent external certification. Historical priority cannot be conclusively excluded because the complete original 1973 Filiptsov article and every later source under alternative terminology were not fully accessible. The limit loop has a singular endpoint at the origin and is not asserted to be a regular periodic orbit of the \(a=0\) system.

## References
1. A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803v1, 27 October 2022, Theorem 1.2 and Case 3.
2. J. Llibre, R. Oliveira and Y. Zhao, *On the birth and death of algebraic limit cycles in quadratic differential systems*, 2021, Theorem 2(b), freely available at https://ddd.uab.cat/pub/artpub/2021/240882/LliOliZha2019.pdf.
3. V. F. Filiptsov, *Algebraic limit cycles*, Differential Equations **9** (1973), 983–986 (original historical reference; full text not inspected).
