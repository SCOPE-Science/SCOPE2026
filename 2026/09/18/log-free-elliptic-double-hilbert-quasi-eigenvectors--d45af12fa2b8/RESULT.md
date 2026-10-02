# Exact elliptic quasi-eigenvectors for the double Hilbert transform

## Result

Let
\[
\mathbf H=\mathcal H_2\mathcal H_1
\]
be the double Hilbert transform on \(L^2(\mathbb R^2)\), with multiplier
\[
\phi(\xi_1,\xi_2)=
\begin{cases}
-1,&\xi_1\xi_2>0,\\
+1,&\xi_1\xi_2<0.
\end{cases}
\]

Let \(D=\{z\in\mathbb R^2:|z|<1\}\), let \(A\in GL_2(\mathbb R)\), and let
\[
E=x_0+AD
\]
be a nondegenerate ellipse. Write \(r_1,r_2\) for the row vectors of \(A^{-T}\), and let
\[
\alpha=\angle(r_1,r_2)\in(0,\pi).
\]
Then
\[
\boxed{
\frac{\|(\mathbf H-I)\chi_E\|_2^2}{\|\chi_E\|_2^2}
=
4\left(1-\frac{\alpha}{\pi}\right)
}
\]
and
\[
\boxed{
\frac{\|(\mathbf H+I)\chi_E\|_2^2}{\|\chi_E\|_2^2}
=
\frac{4\alpha}{\pi}.
}
\]

In diagonal coordinates
\[
u=\frac{x-y}{\sqrt2},
\qquad
v=\frac{x+y}{\sqrt2},
\]
define, for \(0<\varepsilon\le1\),
\[
E_\varepsilon^+
=
\left\{(x,y):
\frac{u^2}{\varepsilon^2}+v^2<1
\right\}.
\]
Then
\[
\boxed{
\frac{\|(\mathbf H-I)\chi_{E_\varepsilon^+}\|_2}
{\|\chi_{E_\varepsilon^+}\|_2}
=
\sqrt{\frac8\pi\arctan\varepsilon}
=
\sqrt{\frac8\pi}\,\varepsilon^{1/2}(1+O(\varepsilon^2)).
}
\]
The reflected anti-diagonal ellipse gives the corresponding \(-1\) formula.

Thus bounded \(C^\infty\), strictly convex indicator quasi-eigenvectors exist with an exact log-free square-root defect.

## Proof

The Fourier transform of an affine disk indicator is
\[
\widehat{\chi_E}(\xi)
=
e^{-ix_0\cdot\xi}
|\det A|
\widehat{\chi_D}(A^T\xi).
\]
The density \(|\widehat{\chi_D}(\zeta)|^2\) is radial. With
\[
\zeta=A^T\xi,
\qquad
\xi=A^{-T}\zeta,
\]
we have
\[
\xi_1=r_1\cdot\zeta,
\qquad
\xi_2=r_2\cdot\zeta.
\]
Therefore the fraction of Fourier \(L^2\)-mass in the opposite-sign quadrants is exactly the angular fraction of unit vectors for which
\[
(r_1\cdot\omega)(r_2\cdot\omega)<0.
\]
If the angle between \(r_1\) and \(r_2\) is \(\alpha\), the two sign-disagreement wedges have total angular measure \(2\alpha\). Hence the opposite-sign mass fraction is \(\alpha/\pi\), and the same-sign fraction is \(1-\alpha/\pi\).

The multiplier of \(\mathbf H-I\) is \(-2\) on the same-sign quadrants and \(0\) on the opposite-sign quadrants. Plancherel therefore gives
\[
\frac{\|(\mathbf H-I)\chi_E\|_2^2}{\|\chi_E\|_2^2}
=
4\left(1-\frac{\alpha}{\pi}\right).
\]
The formula for \(\mathbf H+I\) follows by interchanging the two quadrant classes.

For \(E_\varepsilon^+\), one affine map from the disk is
\[
A_\varepsilon
=
\frac1{\sqrt2}
\begin{pmatrix}
\varepsilon&1\\
-\varepsilon&1
\end{pmatrix}.
\]
The angle \(\alpha_\varepsilon\) between the rows of \(A_\varepsilon^{-T}\) satisfies
\[
\cos\alpha_\varepsilon
=
\frac{\varepsilon^2-1}{\varepsilon^2+1},
\]
so
\[
\alpha_\varepsilon
=
\pi-2\arctan\varepsilon.
\]
Substitution gives
\[
4\left(1-\frac{\alpha_\varepsilon}{\pi}\right)
=
\frac8\pi\arctan\varepsilon.
\]

## Originality boundary

A separate published result already gives the sharp asymptotic for the truncated diagonal strip introduced by Abakumov, Domelevo, Petermichl and Poltoratski. That strip result is therefore not part of the claim here.

The surviving theorem is the all-ellipse angular defect identity and its smooth strictly convex diagonal-ellipse corollary. In the accessible primary abstract of arXiv:2609.15155, the authors construct approximate invariant open sets and exact invariant bent strips, but no ellipse formula is stated. Full source text was not available in this audit, so originality is asserted only to the best of current knowledge.

## Limitations

No optimality is claimed among all bounded sets, all convex sets, or all ellipses with prescribed eccentricity. The exponent \(1/2\) is not asserted to be a universal lower bound under a geometric normalization. The statement is an \(L^2\) result for the standard product double Hilbert transform on \(\mathbb R^2\).

## References

1. E. Abakumov, K. Domelevo, S. Petermichl, A. Poltoratski, *Invariant sets of the double Hilbert transform*, arXiv:2609.15155 (2026).
