# Boundary curvature is the first nonuniversal coefficient in holomorphic energy asymptotics

## Finding

Let \(f\) be a nonzero holomorphic function on a neighborhood of \(\overline{\mathbb D}\). Suppose its zeros in \(\mathbb D\) are \(p_j\), with multiplicities \(k_j\), and its zeros on \(\partial\mathbb D\) are \(q_\nu\), with multiplicities \(\ell_\nu\).

For a boundary zero \(q\) of multiplicity \(\ell\), factor
\[
f(z)=(z-q)^\ell g(z),
\qquad
g(q)\ne0.
\]
Define
\[
\kappa_f(q)
=
|g(q)|^{-1/\ell}
\left(
1+\frac{2}{\ell}\operatorname{Re}\frac{qg'(q)}{g(q)}
\right).
\]
Equivalently,
\[
\kappa_f(q)
=
\left|\frac{f^{(\ell)}(q)}{\ell!}\right|^{-1/\ell}
\left(
1+
\frac{2}{\ell(\ell+1)}
\operatorname{Re}\frac{qf^{(\ell+1)}(q)}{f^{(\ell)}(q)}
\right).
\]

Then, for any sufficiently small zero-isolating neighborhood \(U_q\),
\[
\int_{\{|f|=\epsilon\}\cap U_q}|f'(z)|\,ds
=
\pi\ell\,\epsilon
-
\ell\kappa_f(q)\epsilon^{1+1/\ell}
+
O\!\left(\epsilon^{1+2/\ell}\right),
\]
and
\[
\int_{\{|f|<\epsilon\}\cap U_q}|f'(z)|^2\,dA
=
\frac{\pi\ell}{2}\epsilon^2
-
\frac{\ell^2\kappa_f(q)}{2\ell+1}\epsilon^{2+1/\ell}
+
O\!\left(\epsilon^{2+2/\ell}\right).
\]

Interior zeros contribute exactly
\[
2\pi k_j\epsilon
\]
to the level-set integral and
\[
\pi k_j\epsilon^2
\]
to the sublevel-set energy, once \(\epsilon\) is sufficiently small. Therefore the global expansion is the sum of these exact interior terms and the displayed boundary expansions.

For a simple boundary zero,
\[
\kappa_f(q)
=
\frac{1}{|f'(q)|}
\left(
1+\operatorname{Re}\frac{qf''(q)}{f'(q)}
\right).
\]
Thus the first correction to the universal half-multiplicity coefficient is exactly a signed curvature invariant of the normalized boundary germ.

## Assumptions and scope

The disk is
\[
\mathbb D=\{z\in\mathbb C:|z|<1\}.
\]
The function \(f\) is assumed holomorphic on an open neighborhood of the closed disk and is not identically zero. Hence it has finitely many zeros in \(\overline{\mathbb D}\).

For a boundary zero \(q\), choose a small simply connected neighborhood in which
\[
g(z)=\frac{f(z)}{(z-q)^\ell}
\]
does not vanish. Any local holomorphic branch
\[
h(z)=g(z)^{1/\ell}
\]
defines
\[
\psi(z)=(z-q)h(z),
\qquad
f(z)=\psi(z)^\ell.
\]
Shrinking the neighborhood if necessary, \(\psi\) is biholomorphic. Replacing \(h\) by another branch rotates \(\psi\) by an \(\ell\)-th root of unity, so the signed curvature used below is branch-independent.

The signed curvature convention is positive when the image of the disk lies locally on the curvature side of the tangent. With that convention, the identity normalization at a boundary point of the unit disk has curvature \(1\).

The result refines the boundary part of the leading asymptotic theorem of Chen, Shao, Wu, and Xia. It does not assert a higher-order expansion at singular boundaries other than the analytic boundary germs produced here, and it does not address several-complex-variable analogues.

## Proof

Fix a boundary zero \(q\) of multiplicity \(\ell\). Let
\[
h=g^{1/\ell}
\]
and
\[
\psi(z)=(z-q)h(z).
\]
Write
\[
w=\psi(z)
\]
and let
\[
\Omega=\psi(\mathbb D\cap U_q).
\]
Then
\[
f(z)=w^\ell.
\]

The curve
\[
\psi(\partial\mathbb D)
\]
is real analytic. Parameterize \(\partial\mathbb D\) counterclockwise. At \(q\), its unit tangent is
\[
T=iq.
\]
For a conformal map, the signed curvature of the image boundary is
\[
\kappa
=
\frac{
1+\operatorname{Im}\!\left((\psi''(q)/\psi'(q))T\right)
}{
|\psi'(q)|
}
=
\frac{
1+\operatorname{Re}\!\left(q\psi''(q)/\psi'(q)\right)
}{
|\psi'(q)|
}.
\]
Since
\[
\psi'(q)=h(q),
\qquad
\psi''(q)=2h'(q),
\qquad
\frac{h'(q)}{h(q)}
=
\frac1\ell\frac{g'(q)}{g(q)},
\]
this gives
\[
\kappa=\kappa_f(q).
\]

Rotate the \(w\)-plane so that the boundary tangent at the origin is horizontal. Locally,
\[
\partial\Omega:
\quad
y=\frac{\kappa}{2}x^2+O(x^3),
\]
with the sign chosen so that \(\Omega\) lies on the inward side. Intersecting this graph with the circle
\[
|w|=\rho
\]
shows that the two boundary intersection angles are shifted from the two endpoints of a semicircle by
\[
\frac{\kappa\rho}{2}+O(\rho^2).
\]
Consequently the angular measure of
\[
\Omega\cap\{|w|=\rho\}
\]
is
\[
|\Theta(\rho)|
=
\pi-\kappa\rho+O(\rho^2).
\]
Its circular length is therefore
\[
\pi\rho-\kappa\rho^2+O(\rho^3).
\]

Put
\[
\rho=\epsilon^{1/\ell}.
\]
Because
\[
f'(z)
=
\ell w^{\ell-1}\psi'(z)
\]
and
\[
ds_z
=
\frac{ds_w}{|\psi'(z)|},
\]
the Jacobian factors cancel on the level curve:
\[
|f'(z)|\,ds_z
=
\ell\rho^{\ell-1}ds_w.
\]
Hence
\[
\begin{aligned}
\int_{\{|f|=\epsilon\}\cap U_q}|f'(z)|\,ds
&=
\ell\rho^{\ell-1}
\left(
\pi\rho-\kappa\rho^2+O(\rho^3)
\right)\\
&=
\pi\ell\,\epsilon
-
\ell\kappa\,\epsilon^{1+1/\ell}
+
O\!\left(\epsilon^{1+2/\ell}\right).
\end{aligned}
\]

For the area integral,
\[
dA_z
=
|\psi'(z)|^{-2}dA_w,
\]
so again the conformal Jacobian cancels:
\[
|f'(z)|^2\,dA_z
=
\ell^2|w|^{2\ell-2}dA_w.
\]
Using polar coordinates in \(\Omega\),
\[
\begin{aligned}
\int_{\{|f|<\epsilon\}\cap U_q}|f'(z)|^2\,dA
&=
\ell^2
\int_0^\rho
t^{2\ell-1}
\left(
\pi-\kappa t+O(t^2)
\right)\,dt\\
&=
\frac{\pi\ell}{2}\rho^{2\ell}
-
\frac{\ell^2\kappa}{2\ell+1}\rho^{2\ell+1}
+
O(\rho^{2\ell+2})\\
&=
\frac{\pi\ell}{2}\epsilon^2
-
\frac{\ell^2\kappa}{2\ell+1}\epsilon^{2+1/\ell}
+
O\!\left(\epsilon^{2+2/\ell}\right).
\end{aligned}
\]

At an interior zero \(p\) of multiplicity \(k\), the same coordinate reduction maps a full small disk to a full disk. The angular measure is exactly
\[
2\pi,
\]
so the corresponding two contributions are exactly
\[
2\pi k\epsilon
\quad\text{and}\quad
\pi k\epsilon^2.
\]

Finally, choose mutually disjoint zero neighborhoods. On the compact complement, \(|f|\) has a positive lower bound. Thus for all sufficiently small \(\epsilon\), the level and sublevel sets lie entirely inside those neighborhoods, and summing the local formulas gives the global expansion.

## Verification

The curvature formula was checked directly from the counterclockwise unit-circle tangent
\[
T=iq
\]
and the standard conformal-image curvature transformation. For the normalization
\[
\psi(z)=z-q,
\]
it gives
\[
\kappa=1,
\]
as required for the translated unit circle.

The model
\[
f(z)=z-1
\]
provides an exact sign check. On
\[
|z-1|=\epsilon,
\]
the portion inside the unit disk has angular measure
\[
\pi-\epsilon+O(\epsilon^3).
\]
Hence
\[
\int_{\{|f|=\epsilon\}\cap\mathbb D}|f'|\,ds
=
\pi\epsilon-\epsilon^2+O(\epsilon^4),
\]
and direct radial integration gives
\[
\int_{\{|f|<\epsilon\}\cap\mathbb D}|f'|^2\,dA
=
\frac{\pi}{2}\epsilon^2-\frac13\epsilon^3+O(\epsilon^5).
\]
These agree with the theorem at
\[
\ell=1,
\qquad
\kappa_f(1)=1.
\]

No numerical experiment is used to establish the continuum assertion. The proof requires only the local holomorphic factorization, the exact conformal Jacobian cancellation, and a second-order Taylor expansion of an analytic boundary germ.

## Relationship to prior work

Chen, Shao, Wu, and Xia prove the leading one-dimensional asymptotics
\[
\int_{\{|f|=\epsilon\}\cap\mathbb D}|f'|\,ds
=
2\pi
\left(
\sum_j k_j+\frac12\sum_\nu\ell_\nu
\right)
\epsilon
+
o(\epsilon)
\]
and
\[
\int_{\{|f|<\epsilon\}\cap\mathbb D}|f'|^2\,dA
=
\pi
\left(
\sum_j k_j+\frac12\sum_\nu\ell_\nu
\right)
\epsilon^2
+
o(\epsilon^2).
\]
Their boundary proof uses the fact that, in a local holomorphic coordinate, the image of the disk occupies asymptotically a half-plane. The present result continues precisely that local calculation by one geometric order and identifies the coefficient.

Classical work on curvature of level curves of harmonic functions studies curvature bounds and geometric behavior of level sets themselves. That does not imply the weighted level-set and sublevel-energy coefficients above. The coefficient
\[
1+\operatorname{Re}\frac{qf''(q)}{f'(q)}
\]
at a simple zero is familiar from conformal-image curvature formulas, but its role as the first correction to these energy asymptotics is a separate statement.

## Limitations

The expansion is local to analytic boundary germs arising from a holomorphic coordinate near a zero of a function defined beyond the unit circle. The stated remainder is not claimed to be optimal.

The result determines the first geometry-sensitive coefficient but does not compute all higher coefficients. Those would depend on higher boundary jets.

No several-variable analogue is claimed. In higher complex dimension, the zero set and boundary intersection geometry are qualitatively different.

Targeted searches did not locate an implication-equivalent published expansion, but older conformal-geometry literature may contain related local tube or arc-length expansions under different terminology.

## References

1. H. Chen, G. Shao, J. Wu, and W. Xia, *Energy asymptotics of holomorphic functions with application to Calderón-Zygmund theory in \(\mathbb C\)*, arXiv:2609.02601v1, first public version 2 September 2026.
2. L. De Carli and S. M. Hudson, *Geometric remarks on the level curves of harmonic functions*, Bulletin of the London Mathematical Society 42 (2010), 83--95, DOI: 10.1112/blms/bdp099.
3. M. Ortel and W. Schneider, *Curvature of Level Curves of Harmonic Functions*, Canadian Mathematical Bulletin 26 (1983), 399--405, DOI: 10.4153/CMB-1983-066-4.
