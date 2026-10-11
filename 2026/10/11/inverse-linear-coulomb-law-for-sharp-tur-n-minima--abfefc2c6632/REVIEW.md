# Review of Inverse-linear Coulomb law for sharp Turán minima

## Correctness

PASS. The 2026 source gives, at each minimum, the exact identities
\[
b
=
\frac{1-\eta/a}{1+y}
\]
and
\[
ya^2-\eta(2y+1)a+(1+y)(y^2-\nu^2)=0.
\]
After
\[
\varepsilon=1/a,
\qquad
y=\varepsilon Y,
\]
the second equation has a regular implicit-function point at
\[
(\varepsilon,Y)=(0,\eta).
\]
Coefficient extraction gives
\[
y
=
\frac{\eta}{a}
+
\frac{2\eta^2+\nu^2}{a^2}
+
O(a^{-3}),
\]
and the exact formula for
\[
b
\]
then gives
\[
1-b
=
\frac{2\eta}{a}
+
\frac{\nu^2}{a^2}
+
O(a^{-3}).
\]

The independently inspected McMahon expansion gives the required positive-zero law
\[
x_n=\pi n+\eta\log n+O(1).
\]
The minimizer lies between consecutive zeros, so it has the same two leading scales. Substitution proves both index limits.

## Originality

PASS. The fresh paper proves only monotone convergence of the regular-Coulomb minima and does not state a rate. Its Bessel and general-cylinder sections do not imply the Coulomb rate because the Coulomb equation contains the long-range
\[
2\eta/\rho
\]
term.

A previously known zero asymptotic supplies only the nodal geometry and has no Turán-minimum sequence. The earlier Coulomb Turán literature studies different order-shifted expressions. Searches under source-specific and implication-equivalent formulations did not locate the inverse-linear minimum law or its logarithmic index correction.

A nearby same-source Bessel/cylinder asymptotic has inverse-square scale. It is not covering: the accepted claim is restricted to fixed
\[
\eta>0
\]
and identifies the new leading term created by Coulomb charge.

## Value

PASS. The 2026 theorem makes the Coulomb sequence a new sharp-constant object but leaves its approach to the limiting sharp constant qualitative. The accepted result determines that approach and reveals a structural phase change: any fixed positive Coulomb charge slows inverse-square Bessel convergence to inverse-linear convergence.

The coefficient
\[
2\eta/\pi
\]
quantifies the sharp-constant deficit in nodal index, while the next logarithmic term records the Coulomb phase distortion of the zero lattice. These are natural asymptotic invariants of the new sharp inequalities rather than arbitrary numerical refinements.

Same-model review: passed. Independent audit: not yet performed.
