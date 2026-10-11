# Log-symmetric zero bifurcation in the equal-degree harmonic rational family

## Finding

Fix
\[
n\in\mathbb N
\]
and
\[
a,b\in\mathbb C\setminus\{0\}.
\]
Consider the harmonic rational function
\[
q(z)
=
z^n+\frac{a}{\overline z^{\,n}}+b.
\]
Set
\[
A
=
|b|^2-2\operatorname{Re}a
\]
and
\[
\Delta
=
A^2-4|a|^2.
\]

In the zero-existence region of the recent explicit-zero theorem, one has
\[
A\ge2|a|.
\]
Define
\[
\eta
=
\operatorname{arcosh}\!\left(
\frac{A}{2|a|}
\right).
\]
Equivalently,
\[
\eta
=
\operatorname{arsinh}\!\left(
\frac{\sqrt{\Delta}}{2|a|}
\right).
\]

Then the complete radial geometry of the zeros is
\[
|z|=\rho_-
\quad\text{or}\quad
|z|=\rho_+,
\]
where
\[
\rho_\pm
=
|a|^{1/(2n)}
\exp\!\left(
\pm\frac{\eta}{2n}
\right).
\]
On each noncoincident circle the \(n\) zeros form a regular \(n\)-gon.

The two radii obey the exact invariant
\[
\rho_+\rho_-
=
|a|^{1/n}.
\]
Thus their geometric mean is fixed:
\[
\sqrt{\rho_+\rho_-}
=
|a|^{1/(2n)}.
\]
Their logarithmic separation is
\[
\log\frac{\rho_+}{\rho_-}
=
\frac{\eta}{n}
=
\frac1n
\operatorname{arsinh}\!\left(
\frac{\sqrt{\Delta}}{2|a|}
\right).
\]

If
\[
\Delta>0,
\]
the two circles are distinct and the source theorem's
\[
2n
\]
zeros split into two regular \(n\)-gons.

If
\[
\Delta=0,
\]
then
\[
\rho_+=\rho_-
=
|a|^{1/(2n)},
\]
and the two polygons coalesce into the
\[
n
\]
double zeros from the source theorem.

For fixed nonzero \(a\), as
\[
\Delta\downarrow0,
\]
\[
\log\frac{\rho_+}{\rho_-}
=
\frac{\sqrt{\Delta}}{2n|a|}
+
O(\Delta^{3/2}),
\]
and
\[
\rho_+-\rho_-
=
\frac{|a|^{1/(2n)-1}}{2n}
\sqrt{\Delta}
+
O(\Delta^{3/2}).
\]

Hence the boundary of the coefficient region is not merely a counting threshold: it is an explicit square-root radial bifurcation, symmetric in logarithmic radius about the invariant circle
\[
|z|=|a|^{1/(2n)}.
\]

## Assumptions and scope

The source theorem treats the limiting equal-degree case
\[
k=n
\]
of the family
\[
z^n+\frac{a}{\overline z^{\,k}}+b.
\]
It proves that zeros exist exactly when
\[
(\operatorname{Im}a)^2
\le
-|b|^2\operatorname{Re}a
+
\frac{|b|^4}{4}.
\]
It then reduces the possible radii to the two positive roots of
\[
x^2
+
\left(
2\operatorname{Re}a-|b|^2
\right)x
+
|a|^2
=
0,
\qquad
x=|z|^{2n}.
\]

The coefficient condition is equivalent to
\[
\Delta\ge0
\]
together with positivity of the two roots. In the source's admissible region this is the same as
\[
A\ge2|a|.
\]

The theorem here reorganizes the source's quadratic roots into an exact logarithmic normal form. It does not alter the source's angular formulas and does not claim that the two regular \(n\)-gons have the same angular orientation when their radii differ.

The displayed square-root expansions are local statements with
\[
a\ne0
\]
fixed while the coefficient pair approaches the discriminant boundary.

## Proof

The source theorem shows that the squared radial variables
\[
x_\pm=\rho_\pm^{2n}
\]
are the two positive roots of
\[
x^2-Ax+|a|^2=0.
\]
Hence
\[
x_\pm
=
\frac{
A\pm\sqrt{\Delta}
}{2},
\]
with
\[
x_+x_-=|a|^2.
\]

Because
\[
A\ge2|a|,
\]
there is a unique
\[
\eta\ge0
\]
such that
\[
A=2|a|\cosh\eta.
\]
Then
\[
\sqrt{\Delta}
=
\sqrt{
A^2-4|a|^2
}
=
2|a|\sinh\eta.
\]
Therefore
\[
x_\pm
=
|a|
\left(
\cosh\eta\pm\sinh\eta
\right)
=
|a|e^{\pm\eta}.
\]
Taking positive
\[
2n
\]
th roots gives
\[
\rho_\pm
=
|a|^{1/(2n)}
e^{\pm\eta/(2n)}.
\]

The same identities give
\[
\sinh\eta
=
\frac{\sqrt{\Delta}}{2|a|},
\]
so
\[
\eta
=
\operatorname{arsinh}\!\left(
\frac{\sqrt{\Delta}}{2|a|}
\right).
\]
This proves the exact logarithmic-gap formula.

For either fixed radius \(\rho\), the source equation gives
\[
e^{in\varphi}
=
-
\frac{b}{
\rho^n+a\rho^{-n}
}.
\]
The right-hand side has modulus one precisely because \(\rho\) comes from the radial quadratic. Its
\[
n
\]
th roots are equally spaced by
\[
2\pi/n.
\]
Thus each radius supports a regular \(n\)-gon of zeros.

When
\[
\Delta>0,
\]
the radii are different, so these two \(n\)-gons are disjoint. When
\[
\Delta=0,
\]
one has
\[
\eta=0
\]
and the source theorem identifies the resulting
\[
n
\]
zeros as double.

For the boundary expansion, put
\[
s
=
\frac{\sqrt{\Delta}}{2|a|}.
\]
As
\[
s\downarrow0,
\]
\[
\operatorname{arsinh}s
=
s+O(s^3).
\]
Hence
\[
\log\frac{\rho_+}{\rho_-}
=
\frac1n\operatorname{arsinh}s
=
\frac{\sqrt{\Delta}}{2n|a|}
+
O(\Delta^{3/2}).
\]

Finally, with
\[
r_0=|a|^{1/(2n)},
\]
\[
\rho_+-\rho_-
=
2r_0
\sinh\!\left(
\frac{\eta}{2n}
\right).
\]
Using
\[
\sinh y=y+O(y^3)
\]
and the preceding expansion of \(\eta\) yields
\[
\rho_+-\rho_-
=
\frac{|a|^{1/(2n)-1}}{2n}
\sqrt{\Delta}
+
O(\Delta^{3/2}).
\]

## Verification

The proof was replayed directly from the source quadratic
\[
x^2-Ax+|a|^2=0.
\]
Viète's identity gives
\[
x_+x_-=|a|^2,
\]
which becomes the exact radius product
\[
\rho_+\rho_-=|a|^{1/n}.
\]

The hyperbolic parametrization was checked in both directions:
\[
A=2|a|\cosh\eta,
\qquad
\sqrt{\Delta}=2|a|\sinh\eta,
\]
so
\[
x_\pm=|a|e^{\pm\eta}.
\]

The angular conclusion uses the source's exact phase equation and only the elementary fact that the \(n\)th roots of a unimodular number form a regular \(n\)-gon.

The square-root coefficient was checked by expanding the exact
\[
\operatorname{arsinh}
\]
formula, not by fitting numerical data. Numerical substitutions in representative admissible coefficient pairs were used only as consistency checks.

## Relationship to prior work

Melman's 2026 paper proves the exact zero-existence parabola for the equal-degree case and gives the two quadratic radial roots explicitly. It records the trichotomy of no zeros, \(n\) double zeros, or \(2n\) distinct zeros.

The inspected article does not state the invariant radius product, the logarithmic-symmetry parametrization, the exact
\[
\operatorname{arsinh}
\]
radial gap, or the square-root coalescence law.

Brooks and Lee study zero counts for the related one-parameter harmonic rational family with poles. Their work supplies the counting context, but not this equal-degree two-ring normal form.

Melman's earlier zero-location paper develops inclusion sectors for analytic and harmonic trinomials. The 2026 paper itself identifies the equal-degree harmonic rational case as a separate limiting case and derives its explicit radial quadratic there.

Targeted searches for the equal-degree family, reciprocal or geometric-mean radius laws, logarithmic radial symmetry, discriminant splitting, and square-root zero bifurcation did not locate an implication-equivalent statement.

## Limitations

The result concerns only the equal-degree family
\[
k=n.
\]
For
\[
0<k<n,
\]
the radial equation is no longer quadratic in
\[
|z|^{2n},
\]
so the exact log-symmetric normal form does not follow.

The result classifies radii and their bifurcation. It does not provide a new zero-count theorem beyond the counts already proved in the source.

The angular orientations of the two regular \(n\)-gons can differ and remain governed by the source phase formula.

The local
\[
O(\Delta^{3/2})
\]
terms are stated for fixed
\[
a\ne0.
\]
No uniform expansion is claimed as
\[
a\to0.
\]

## References

1. A. Melman, *A Note on Zero Inclusion Sectors for a Family of Harmonic Rational Functions*, Computational Methods and Function Theory 26 (2026), 669--676, DOI: 10.1007/s40315-026-00606-w.
2. J. Brooks and A. Lee, *Zeros of a Family of Complex-Valued Harmonic Functions with Poles*, Computational Methods and Function Theory 26 (2026), 199--219, DOI: 10.1007/s40315-024-00572-1.
3. A. Melman, *Zero location for analytic and harmonic trinomials*, Journal of Mathematical Analysis and Applications 544 (2025), 129078, DOI: 10.1016/j.jmaa.2024.129078.
