# A right circular cone disproves the dual-volume affine-section implication
## Finding
Let
\[
A=
\left\{
(x,y,z)\in\mathbb R^3:
0\le z\le1,\quad x^2+y^2\le z^2
\right\},
\]
and choose the two interior points
\[
p=\left(0,0,\frac{33}{50}\right),
\qquad
q=\left(0,0,\frac{23}{35}\right).
\]
For every affine plane \(H\) containing \(p\) and \(q\),
\[
\int_{S^2\cap(H-p)}
\rho_{(A\cap H)-p}(u)\,d\sigma(u)
<
\int_{S^2\cap(H-q)}
\rho_{(A\cap H)-q}(u)\,d\sigma(u).
\]
Nevertheless,
\[
\int_{S^2}\rho_{A-p}(u)\,d\sigma(u)
>
\int_{S^2}\rho_{A-q}(u)\,d\sigma(u).
\]

Therefore the implication asked in Problem 7, “Dual volumes and affine sections,” of the 2009 Banach Center Open Problem Session is false, already for a right circular cone truncated by a plane and already in dimension \(3\).

## Assumptions and scope
For a compact convex set \(C\) containing the origin, its radial function is
\[
\rho_C(u)=\sup\{\lambda\ge0:\lambda u\in C\}.
\]
The spherical measure \(d\sigma\) may be normalized or unnormalized: multiplying it by a positive constant does not affect any comparison below.

The points \(p\) and \(q\) lie on the symmetry axis of \(A\) and satisfy
\[
0<\frac{23}{35}<\frac{33}{50}<1.
\]
Every affine plane through both points contains the full \(z\)-axis, so every section \(A\cap H\) is the same isosceles triangle up to a rotation about that axis.

The argument treats the simple radial integral, corresponding to the identity function in the generalized dual-volume framework. It gives a counterexample to the stated implication, not a classification of all bodies or all powers of the radial function.

## Proof
For
\[
0<c<1
\]
put
\[
x_c=(0,0,c),
\qquad
q_c=1-c.
\]
Because \(A\) is rotationally symmetric, a ray from \(x_c\) is determined by its polar angle \(\theta\) from the positive \(z\)-axis. Let
\[
\theta_c=\arctan\!\left(\frac1{q_c}\right).
\]
The ray first meets the top disk when
\[
0\le\theta\le\theta_c
\]
and first meets the lateral cone when
\[
\theta_c\le\theta\le\pi.
\]
Hence
\[
\rho_c(\theta)=
\begin{cases}
\dfrac{q_c}{\cos\theta},
&0\le\theta\le\theta_c,\\[6pt]
\dfrac{c}{\sin\theta-\cos\theta},
&\theta_c\le\theta\le\pi.
\end{cases}
\]
At the transition the two expressions agree, so differentiating the corresponding integrals produces no boundary term.

For any plane through the \(z\)-axis, the section is an isosceles triangle and its radial integral at \(x_c\) is
\[
S(c)=2J(c),
\qquad
J(c)=\int_0^\pi\rho_c(\theta)\,d\theta.
\]
Differentiation gives
\[
J'(c)
=
-\int_0^{\theta_c}\sec\theta\,d\theta
+
\int_{\theta_c}^{\pi}
\frac{d\theta}{\sin\theta-\cos\theta}.
\]
At
\[
c=\frac{23}{35},
\qquad
q_c=\frac{12}{35},
\qquad
\sqrt{1+q_c^2}=\frac{37}{35},
\]
the two elementary antiderivatives simplify to
\[
J'\!\left(\frac{23}{35}\right)
=
-\log6+
\frac1{\sqrt2}
\log\!\left(
\frac{121+84\sqrt2}{23}
\right).
\]
The exact interval certificate in `verify.py` proves
\[
-0.134100
<
J'\!\left(\frac{23}{35}\right)
<
-0.134098,
\]
so this derivative is strictly negative.

The full three-dimensional radial integral is
\[
G(c)=2\pi K(c),
\qquad
K(c)=
\int_0^\pi
\rho_c(\theta)\sin\theta\,d\theta.
\]
Differentiation gives
\[
K'(c)
=
-\int_0^{\theta_c}\tan\theta\,d\theta
+
\int_{\theta_c}^{\pi}
\frac{\sin\theta}
{\sin\theta-\cos\theta}\,d\theta.
\]
Using
\[
\theta_c=\frac\pi2-\arctan q_c
\]
one obtains
\[
K'(c)
=
\frac\pi4+
\frac12\arctan q_c+
\frac14
\log\!\left(
\frac{q_c^4}
{c^2(1+q_c^2)}
\right).
\]
At
\[
c=\frac{33}{50},
\qquad
q_c=\frac{17}{50},
\qquad
1+q_c^2=\frac{2789}{2500},
\]
this becomes
\[
K'\!\left(\frac{33}{50}\right)
=
\frac\pi4+
\frac12\arctan\!\left(\frac{17}{50}\right)
+
\frac14
\log\!\left(
\frac{17^4}{33^2\cdot2789}
\right).
\]
The exact interval certificate proves
\[
0.050866
<
K'\!\left(\frac{33}{50}\right)
<
0.050869,
\]
so this derivative is strictly positive.

It remains to turn the two local derivative signs into the required two-point inequalities. Herburt, Moszyńska, and Peradzyński prove that, for every convex body in dimension at least \(2\), the functional
\[
x\longmapsto
\int_{S^{d-1}}
\rho_{C-x}(u)\,d\sigma(u)
\]
is strictly concave. Restricting a strictly concave differentiable function to a line remains strictly concave.

Apply this first to any two-dimensional axial section. The tangent-line inequality at
\[
c=\frac{23}{35}
\]
and the strict negativity of \(J'\) give
\[
J\!\left(\frac{33}{50}\right)
<
J\!\left(\frac{23}{35}\right).
\]
Since every plane through \(p\) and \(q\) is an axial plane, this proves every sectional inequality.

Apply strict concavity next to the three-dimensional body. The tangent-line inequality at
\[
c=\frac{33}{50}
\]
and the strict positivity of \(K'\) give
\[
K\!\left(\frac{23}{35}\right)
<
K\!\left(\frac{33}{50}\right).
\]
Multiplication by \(2\pi\) gives the reversed global inequality. This is exactly a counterexample to the proposed implication.

## Verification
The supplied `verify.py` uses rational interval arithmetic rather than floating-point sign tests. Square roots are enclosed by integer-square-root bounds; logarithms are certified by the convergent identity
\[
\log x=
2\operatorname{artanh}\!\left(\frac{x-1}{x+1}\right)
\]
after exact powers-of-two range reduction; arctangents are enclosed by their alternating Taylor series; and \(\pi\) is enclosed with Machin's formula.

The resulting rational intervals are strictly negative for the sectional derivative and strictly positive for the global derivative. The checker also verifies the rational identities
\[
1+\left(\frac{12}{35}\right)^2
=
\left(\frac{37}{35}\right)^2
\]
and
\[
1+\left(\frac{17}{50}\right)^2
=
\frac{2789}{2500}.
\]
It returns `VERIFY_OK`.

The strict-concavity step is analytic and comes from the cited primary theorem; finite computation is not being used to infer an infinite family of inequalities.

## Relationship to prior work
Herburt, Moszyńska, and Peradzyński developed radial centres as maximizers of generalized dual-volume functionals and proved, in particular, strict concavity of the relevant functional for every concave strictly increasing radial weight.

The 2009 Open Problem Session then asked whether comparison of the simple radial integral on every affine hyperplane through two points forces the same comparison for the whole convex body. The right circular cone above reverses the global comparison while preserving the sectional comparison on every admissible plane.

Later work on locations and uniqueness of radial or potential centres studies where such centres lie and when they are unique. The inspected statements do not give the affine-section implication or a counterexample to it.

Searches using “dual volumes and affine sections,” the problem wording, radial-centre aliases, cone specializations, and the exact rational witness heights did not locate a covering result.

## Limitations
The counterexample is three-dimensional and uses the first radial moment. It does not classify which convex bodies satisfy the implication.

No claim is made for higher radial powers or for section families not required to pass through both comparison points.

The proof exploits rotational symmetry so that all admissible planar sections coincide up to rotation. Historical indexing is incomplete, so an unindexed later resolution remains a residual originality risk.

## References
1. I. Herburt, M. Moszyńska, and Z. Peradzyński, *Remarks on Radial Centres of Convex Bodies*, Mathematical Physics, Analysis and Geometry 8 (2005), 157--172. DOI: 10.1007/s11040-005-2968-4.
2. *Open Problem Session*, Banach Center Publications 84 (2009), 217--222, Problem 7, “Dual volumes and affine sections.”
3. I. Herburt, *Location of radial centres of convex bodies*, Advances in Geometry 8 (2008), 309--313. DOI: 10.1515/ADVGEOM.2008.019.
