# Inverse-linear Coulomb law for sharp Turán minima

## Finding

Fix
\[
L\ge0,
\qquad
\eta>0,
\qquad
\nu=L+\frac12.
\]
Let
\[
\Psi_{L,\eta}
\]
be the regular-Coulomb Riccati Turán profile introduced in the recent oscillatory-special-function theorem. On the \(n\)-th positive nodal interval, let
\[
a_{L,\eta,n}
\]
be its unique minimizer and put
\[
b_{L,\eta,n}
=
\Psi_{L,\eta}(a_{L,\eta,n}).
\]
The source proves
\[
0<b_{L,\eta,1}<b_{L,\eta,2}<\cdots<1
\]
and
\[
b_{L,\eta,n}\longrightarrow1.
\]

The convergence has the sharp local expansion
\[
1-b_{L,\eta,n}
=
\frac{2\eta}{a_{L,\eta,n}}
+
\frac{\nu^2}{a_{L,\eta,n}^2}
+
O_{L,\eta}
\left(
a_{L,\eta,n}^{-3}
\right).
\]
In particular,
\[
a_{L,\eta,n}
\left(
1-b_{L,\eta,n}
\right)
\longrightarrow
2\eta.
\]

Using the standard large-zero phase law for regular Coulomb waves,
\[
a_{L,\eta,n}
=
\pi n+\eta\log n+O_{L,\eta}(1),
\]
one obtains
\[
1-b_{L,\eta,n}
=
\frac{2\eta}{\pi n}
-
\frac{2\eta^2}{\pi^2}
\frac{\log n}{n^2}
+
O_{L,\eta}(n^{-2}).
\]
Equivalently,
\[
\lim_{n\to\infty}
n
\left(
1-b_{L,\eta,n}
\right)
=
\frac{2\eta}{\pi},
\]
and
\[
\lim_{n\to\infty}
\frac{n^2}{\log n}
\left(
1-b_{L,\eta,n}
-
\frac{2\eta}{\pi n}
\right)
=
-\frac{2\eta^2}{\pi^2}.
\]

Thus every fixed positive Coulomb parameter changes the convergence scale of the sharp nodal minima from inverse-square in the zero-charge Bessel case to inverse-linear. The first local correction after the Coulomb term is exactly the Bessel-order contribution
\[
\nu^2/a_{L,\eta,n}^2.
\]

For
\[
L>0,
\]
the sharp Turán constants in the source are
\[
L(L+1)b_{L,\eta,n},
\]
so their deficit from the limiting constant satisfies
\[
L(L+1)
\left(
1-b_{L,\eta,n}
\right)
\sim
\frac{
2\eta L(L+1)
}{
\pi n
}.
\]

## Assumptions and scope

The quantities
\[
\Psi_{L,\eta},
\qquad
a_{L,\eta,n},
\qquad
b_{L,\eta,n}
\]
are exactly those in Theorem 4.3 of arXiv:2609.39008v1.

The parameter range is
\[
L\ge0,
\qquad
\eta>0.
\]
The source writes
\[
\nu=L+\frac12
\]
after reducing the regular Coulomb equation to Bessel form.

The result concerns the successive minima of the source's Riccati-normalized Coulomb Turán functional. It does not assert a convergence rate for every other Coulomb Turánian in the earlier literature.

The index asymptotic uses fixed
\[
L,\eta
\]
as
\[
n\to\infty.
\]
No uniformity as
\[
\eta\downarrow0
\]
is claimed. Indeed, the change from inverse-linear to inverse-square behavior is itself nonuniform at
\[
\eta=0.
\]

## Proof

At a critical point
\[
a=a_{L,\eta,n},
\]
write
\[
y=y_{L,\eta}(a).
\]
The source proves the two exact identities
\[
b_{L,\eta,n}
=
\frac{
1-\eta/a
}{
1+y
}
\]
and
\[
H(a,y)=0,
\]
where
\[
H(a,y)
=
ya^2
-
\eta(2y+1)a
+
(1+y)(y^2-\nu^2).
\]

Set
\[
\varepsilon=\frac1a
\]
and
\[
y=\varepsilon Y.
\]
After multiplying
\[
H(a,y)=0
\]
by
\[
\varepsilon,
\]
the equation becomes
\[
G(\varepsilon,Y)=0,
\]
with
\[
G(\varepsilon,Y)
=
Y-\eta
-
2\eta\varepsilon Y
+
\varepsilon
(1+\varepsilon Y)
(\varepsilon^2Y^2-\nu^2).
\]

At
\[
(\varepsilon,Y)=(0,\eta),
\]
\[
G(0,\eta)=0
\]
and
\[
\partial_YG(0,\eta)=1.
\]
The implicit-function theorem therefore gives a unique analytic solution branch near
\[
\varepsilon=0.
\]
Expanding the equation to first order in
\[
\varepsilon
\]
gives
\[
Y
=
\eta
+
(2\eta^2+\nu^2)\varepsilon
+
O_{L,\eta}(\varepsilon^2).
\]
Therefore
\[
y
=
\frac{\eta}{a}
+
\frac{2\eta^2+\nu^2}{a^2}
+
O_{L,\eta}(a^{-3}).
\]

Now use
\[
b
=
\frac{1-\eta/a}{1+y}.
\]
Since
\[
y=O(a^{-1}),
\]
the reciprocal expansion gives
\[
\frac1{1+y}
=
1-y+y^2+O(a^{-3}).
\]
Substitution yields
\[
b
=
1
-
\frac{2\eta}{a}
-
\frac{\nu^2}{a^2}
+
O_{L,\eta}(a^{-3}),
\]
hence
\[
1-b
=
\frac{2\eta}{a}
+
\frac{\nu^2}{a^2}
+
O_{L,\eta}(a^{-3}).
\]

It remains to convert minimizing radius to nodal index. The regular Coulomb phase is
\[
\theta_L(\eta,\rho)
=
\rho
-
\eta\log(2\rho)
-
\frac{L\pi}{2}
+
\sigma_L(\eta).
\]
The McMahon-type expansion of the positive zeros states that the \(n\)-th zero is obtained from
\[
\rho_0-\eta\log\rho_0
=
n\pi+O_{L,\eta}(1)
\]
with an inverse-power correction. Consequently
\[
x_{L,\eta,n}
=
\pi n
+
\eta\log n
+
O_{L,\eta}(1).
\]
Because
\[
x_{L,\eta,n}
<
a_{L,\eta,n}
<
x_{L,\eta,n+1},
\]
the same estimate holds for the minimizer:
\[
a_{L,\eta,n}
=
\pi n
+
\eta\log n
+
O_{L,\eta}(1).
\]

Finally,
\[
\frac1{a_{L,\eta,n}}
=
\frac1{\pi n}
-
\frac{\eta\log n}{\pi^2n^2}
+
O_{L,\eta}(n^{-2}),
\]
while
\[
\frac1{a_{L,\eta,n}^2}
=
\frac1{\pi^2n^2}
+
O_{L,\eta}
\left(
\frac{\log n}{n^3}
\right).
\]
Insertion into the local expansion proves
\[
1-b_{L,\eta,n}
=
\frac{2\eta}{\pi n}
-
\frac{2\eta^2}{\pi^2}
\frac{\log n}{n^2}
+
O_{L,\eta}(n^{-2}),
\]
and both stated limits follow.

## Verification

The fresh primary paper was inspected at the Coulomb differential equation, Riccati transform, Theorem 4.3, and the complete proof of the successive-minimum result.

In particular, the source proves only
\[
b_{L,\eta,n}\uparrow1
\]
and obtains this limit by showing
\[
y(a)\to0.
\]
Its exact algebraic critical-point equation
\[
H(a,y)=0
\]
and exact formula for
\[
b
\]
were independently expanded above.

The independent zero-asymptotic source was inspected at its Coulomb phase function and its McMahon expansion. It gives
\[
\rho-\eta\log\rho
=
n\pi+O_{L,\eta}(1)
\]
for the positive zeros, with inverse-power corrections, which is sufficient for the index conversion.

The earlier full primary paper on regular Coulomb Turán inequalities was also inspected. It studies order-shifted Turánians, Mittag--Leffler expansions, zero interlacing, and related inequalities, but not the new 2026 successive-minimum sequence.

No numerical computation is needed for the proof. Direct numerical solutions of the algebraic critical-point equation were used only to sanity-check the expansion.

## Relationship to prior work

The recent theorem introduces the successive Coulomb minimum sequence and proves its strict increase and qualitative convergence to
\[
1.
\]
The present result supplies the missing convergence law.

The same recent paper shows that at
\[
\eta=0
\]
the Coulomb functional reduces exactly to the normalized Bessel Turán quotient. In the zero-charge case the deficit is of inverse-square size. For every fixed
\[
\eta>0,
\]
the long-range Coulomb term creates the larger inverse-linear contribution
\[
2\eta/a.
\]
Thus the two regimes are separated by a genuine singular perturbation at zero charge.

The 2024 McMahon expansion determines the large-zero geometry needed to convert radius to nodal index but contains no Turán-minimum sequence. The 2015 Coulomb Turán paper contains no implication for the 2026 Riccati minimum rate.

Targeted searches for the source identifier, Coulomb successive minima, inverse-linear convergence, and the equivalent radius law did not locate an implication-equivalent statement.

## Limitations

The theorem is a fixed-parameter asymptotic. It is not uniform in a joint limit where
\[
\eta
\]
tends to zero with
\[
n.
\]
Such a joint limit would contain a crossover between the inverse-linear and inverse-square regimes.

The result does not address the source's open question about monotonicity of
\[
b_{L,\eta,n}
\]
as a function of
\[
L.
\]

The displayed logarithmic second term in nodal index uses the standard Coulomb zero phase. The unknown bounded phase shift is absorbed into the
\[
O_{L,\eta}(n^{-2})
\]
term.

## References

1. I. Aktaş and Á. Baricz, *Turán type inequalities for oscillatory special functions*, arXiv:2609.39008v1, 2026.
2. A. Gil, J. Segura, and N. M. Temme, *McMahon-Type Asymptotic Expansions of the Zeros of the Coulomb Wave Functions*, SIGMA 20 (2024), 075; arXiv:2402.14537v2.
3. Á. Baricz, *Turán type inequalities for regular Coulomb wave functions*, Journal of Mathematical Analysis and Applications 430 (2015), 166--180; arXiv:1504.06448.
