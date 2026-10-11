# Exact Winternitz measure of the Reuleaux triangle
## Finding
Let \(R\) be a Euclidean Reuleaux triangle with uniform area measure. For a point \(O\in R\), let
\[
d_R(O)=
\inf_{H\ni O}\frac{\operatorname{area}(R\cap H)}{\operatorname{area}(R)},
\]
where the infimum is over closed halfplanes \(H\) containing \(O\). The maximum value
\[
\delta_R=\sup_{O\in R}d_R(O)
\]
is the halfspace-depth form of the Winternitz measure.

The unique maximizing point is the dihedral center \(O_0\). In width-one normalization, define
\[
A_0=\frac{\pi-\sqrt3}{2}
\]
and
\[
s_0=
\arccos\!\left(\frac1{2\sqrt3}\right)
-\frac{\pi}{6}
-\frac{\sqrt{11}+\sqrt3}{12}.
\]
Then
\[
\delta_R
=
\frac{s_0}{A_0}
=
0.473390433801114\ldots.
\]
Equivalently, if the Winternitz asymmetry is written as the larger-to-smaller area ratio over all lines through a point and then minimized over the point, its exact value is
\[
w_R^*
=
\frac{A_0-s_0}{s_0}
=
1.112421224844882\ldots.
\]

At the center, the minimum-area halfplanes are exactly those bounded by one of the three center-lines parallel to a side of the generating equilateral triangle, with either orientation chosen so that the smaller side is taken.

## Assumptions and scope
Scale the Reuleaux triangle to width \(1\). Use the generating equilateral triangle
\[
A=\left(0,\frac1{\sqrt3}\right),\quad
B=\left(-\frac12,-\frac1{2\sqrt3}\right),\quad
C=\left(\frac12,-\frac1{2\sqrt3}\right),
\]
so
\[
R=\overline B_1(A)\cap\overline B_1(B)\cap\overline B_1(C).
\]
Its center is the origin and its area is
\[
A_0=\frac{\pi-\sqrt3}{2}.
\]

The Winternitz problem uses arbitrary lines through a variable point and minimizes the worst area imbalance. It is not the Groemer--Wallen asymmetry for bodies of constant width, which restricts the cutting lines to lines containing metric diameters.

## Proof
A standard structural theorem for the center of area says that the maximizer of halfspace depth for a planar convex body is unique. Every symmetry of \(R\) must therefore fix that point. Since the three reflection axes of the Reuleaux triangle meet only at the origin, the unique Winternitz center is
\[
O_0=(0,0).
\]

It remains to minimize the area of a halfplane bounded by a line through \(O_0\).

Let \(\rho(\phi)\) be the radial function of \(R\) at polar angle \(\phi\). If the directed boundary line has angle \(\theta\), write
\[
F(\theta)=
\frac12\int_{\theta}^{\theta+\pi}\rho(\phi)^2\,d\phi
\]
for the area on its left. Threefold rotational symmetry gives
\[
\rho\!\left(\phi+\frac{2\pi}{3}\right)=\rho(\phi),
\]
and differentiation yields
\[
F'(\theta)
=
\frac12\left(
\rho\!\left(\theta+\pi\right)^2-\rho(\theta)^2
\right)
=
\frac12\left(
\rho\!\left(\theta+\frac{\pi}{3}\right)^2-\rho(\theta)^2
\right).
\]

By the dihedral symmetries, every unoriented line through the center is equivalent to one with
\[
0\le\theta\le\frac{\pi}{6}.
\]
For all rays with
\[
0\le\phi\le\frac{\pi}{2},
\]
the active circular boundary is the unit circle centered at \(B\). Put
\[
R_c=\frac1{\sqrt3},\qquad
c(\phi)=R_c\cos\!\left(\phi-\frac{7\pi}{6}\right).
\]
Solving the ray-circle equation gives
\[
\rho(\phi)=g(c(\phi)),
\qquad
g(t)=t+\sqrt{\frac23+t^2}.
\]
The function \(g\) is strictly increasing. For \(0\le\theta\le\pi/6\), both \(\theta\) and \(\theta+\pi/3\) lie in \([0,\pi/2]\), and
\[
c\!\left(\theta+\frac{\pi}{3}\right)-c(\theta)
=
\frac{\sin\theta}{\sqrt3}\ge0,
\]
with strict inequality for \(\theta>0\). Hence
\[
F'(\theta)\ge0
\]
on the fundamental interval, strictly away from \(0\). Therefore the smallest center-halfplane area occurs exactly at \(\theta=0\), and, by rotation through multiples of \(2\pi/3\), at the three lines parallel to the sides of the generating equilateral triangle.

It remains to evaluate \(F(0)\). The upper boundary on the right half-plane is
\[
y=
-\frac1{2\sqrt3}
+
\sqrt{1-\left(x+\frac12\right)^2}.
\]
Its intersection with \(y=0\) has
\[
x_0=\frac{\sqrt{33}}6-\frac12.
\]
Thus the smaller center-halfplane area is
\[
s_0
=
2\int_0^{x_0}
\left[
-\frac1{2\sqrt3}
+
\sqrt{1-\left(x+\frac12\right)^2}
\right]dx.
\]
Using
\[
\int\sqrt{1-t^2}\,dt
=
\frac12\left(t\sqrt{1-t^2}+\arcsin t\right)
\]
and
\[
\arcsin\!\left(\frac{\sqrt{33}}6\right)
=
\arccos\!\left(\frac1{2\sqrt3}\right)
\]
gives
\[
s_0=
\arccos\!\left(\frac1{2\sqrt3}\right)
-\frac{\pi}{6}
-\frac{\sqrt{11}+\sqrt3}{12}.
\]
Dividing by \(A_0\) proves the depth formula. The larger-to-smaller Winternitz ratio is
\[
\frac{A_0-s_0}{s_0}.
\]

## Verification
The supplied `verify.py` reconstructs the Reuleaux triangle as the intersection of three unit disks. It computes the radial function directly from the ray-circle equations, numerically integrates the halfplane-area function, verifies the exact closed form for \(s_0\), checks the monotonicity of \(F\) on the fundamental angular interval, and confirms the displayed depth and ratio.

The finite angular checks in the script are consistency tests only. The continuum minimization is proved by the sign formula for \(F'(\theta)\).

## Relationship to prior work
The Winternitz measure is a classical measure of symmetry and is equivalent, for uniform area measure, to maximum halfspace depth. General treatments establish existence and uniqueness of the center of area and place the invariant among the standard measures of symmetry.

Rousseeuw and Ruts derived explicit halfspace-depth functions for several uniform planar distributions, including every regular polygon. Their paper does not treat the Reuleaux triangle.

Groemer and Wallen introduced a different asymmetry measure specifically for planar bodies of constant width. Their cutting line must contain a metric diameter, and for the Reuleaux triangle their extremal ratio is
\[
\frac{4\pi-3\sqrt3}{2\pi-3\sqrt3},
\]
which is about \(6.78\). That statement neither implies nor is implied by the Winternitz center-line calculation above.

Exact-name, halfspace-depth, Tukey-depth, area-split, radical-form, and decimal-value searches did not locate the formula
\[
\delta_R=0.473390433801114\ldots
\]
or its equivalent Winternitz ratio in the inspected literature.

## Limitations
The theorem computes the invariant only for the Reuleaux triangle. It does not assert that the Reuleaux triangle is extremal for Winternitz measure among all bodies of constant width, nor does it give the corresponding formula for higher regular Reuleaux odd-gons.

Historical literature on symmetry measures is extensive, so a residual risk remains that the same short computation occurs in an unindexed note, exercise, or source using only the older “center of area” terminology.

## References
1. G. Tóth, *Measures of Symmetry for Convex Sets and Stability*, Springer, 2015. DOI: 10.1007/978-3-319-23733-6.
2. P. J. Rousseeuw and I. Ruts, *The depth function of a population distribution*, Metrika 49 (1999), 213--244. DOI: 10.1007/PL00020903.
3. H. Groemer and L. J. Wallen, *A measure of asymmetry for domains of constant width*, Beiträge zur Algebra und Geometrie 42 (2001), 517--521.
