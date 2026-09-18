# Exact elliptic quasi-eigenvectors and sharp strip leakage for the double Hilbert transform

## Result

Let
\[
\mathbf H=\mathcal H_2\mathcal H_1
\]
be the double Hilbert transform on \(L^2(\mathbb R^2)\). Its Fourier multiplier is
\[
\phi(\xi_1,\xi_2)=
\begin{cases}
-1,&\xi_1\xi_2>0,\\
+1,&\xi_1\xi_2<0.
\end{cases}
\]

There are two complementary conclusions.

### 1. Exact defect formula for every ellipse

Let \(D=\{z\in\mathbb R^2:|z|<1\}\), let \(A\in GL_2(\mathbb R)\), and let
\[
E=x_0+A D
\]
be an arbitrary nondegenerate ellipse. Write \(r_1,r_2\) for the two row vectors of \(A^{-T}\), and let
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

In particular, introduce the diagonal coordinates
\[
u=\frac{x-y}{\sqrt2},\qquad v=\frac{x+y}{\sqrt2},
\]
and for \(0<\varepsilon\le 1\) let
\[
E_\varepsilon^+
=
\left\{(x,y):
\frac{u^2}{\varepsilon^2}+v^2<1
\right\}.
\]
This is a bounded \(C^\infty\), strictly convex ellipse elongated along the \(+1\) invariant diagonal \(x=y\). Its defect is exactly
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
Define likewise
\[
E_\varepsilon^-=
\left\{(x,y):
u^2+\frac{v^2}{\varepsilon^2}<1
\right\},
\]
which is elongated along the \(-1\) invariant anti-diagonal \(x=-y\). Then
\[
\boxed{
\frac{\|(\mathbf H+I)\chi_{E_\varepsilon^-}\|_2}
{\|\chi_{E_\varepsilon^-}\|_2}
=
\sqrt{\frac8\pi\arctan\varepsilon}.
}
\]

Thus bounded smooth strictly convex indicator quasi-eigenvectors exist with a log-free \(O(\sqrt\varepsilon)\) defect.

### 2. The logarithm in the truncated-strip example is sharp for that family

Abakumov, Domelevo, Petermichl and Poltoratski use
\[
V_\varepsilon
=
\{(x_1,x_2): |x_1-x_2|<\varepsilon,\ |x_2|<1\}
\]
and prove the upper estimate
\[
\frac{\|(\mathbf H-I)\chi_{V_\varepsilon}\|_2}
{\|\chi_{V_\varepsilon}\|_2}
\lesssim
\sqrt{\varepsilon|\log\varepsilon|}.
\]
For this same family one in fact has the sharp asymptotic
\[
\boxed{
\frac{\|(\mathbf H-I)\chi_{V_\varepsilon}\|_2^2}
{\|\chi_{V_\varepsilon}\|_2^2}
=
\frac4{\pi^2}\,
\varepsilon\log\frac1\varepsilon
+O(\varepsilon)
}
\]
and hence
\[
\boxed{
\frac{\|(\mathbf H-I)\chi_{V_\varepsilon}\|_2}
{\|\chi_{V_\varepsilon}\|_2}
=
\frac2\pi
\sqrt{\varepsilon\log\frac1\varepsilon}
\left(
1+O\!\left(\frac1{\log(1/\varepsilon)}\right)
\right).
}
\]

Consequently the logarithmic factor is genuinely present in the particular hard truncated-strip construction, but it is not intrinsic to bounded indicator quasi-eigenvectors of the double Hilbert transform.

## Proof

### Ellipses

The Fourier transform of an affine disk indicator is
\[
\widehat{\chi_E}(\xi)
=
e^{-i x_0\cdot\xi}\,
|\det A|\,
\widehat{\chi_D}(A^T\xi).
\]
The factor \(|\widehat{\chi_D}(\zeta)|^2\) is radial. With
\[
\zeta=A^T\xi,\qquad
\xi=A^{-T}\zeta,
\]
the first and second coordinates of \(\xi\) are
\[
\xi_1=r_1\cdot\zeta,\qquad
\xi_2=r_2\cdot\zeta.
\]
Therefore the fraction of the Fourier \(L^2\)-mass of \(\chi_E\) lying in the first and third quadrants is exactly the angular fraction
\[
\frac{
|\{\omega\in S^1:(r_1\cdot\omega)(r_2\cdot\omega)>0\}|
}{2\pi}.
\]
If the angle between \(r_1\) and \(r_2\) is \(\alpha\), the two sign-disagreement wedges have total angular measure \(2\alpha\). Hence the same-sign fraction is
\[
1-\frac{\alpha}{\pi},
\]
and the opposite-sign fraction is \(\alpha/\pi\).

Since \(\mathbf H-I\) has multiplier \(-2\) on the same-sign quadrants and \(0\) on the opposite-sign quadrants, Plancherel gives
\[
\frac{\|(\mathbf H-I)\chi_E\|_2^2}{\|\chi_E\|_2^2}
=
4\left(1-\frac{\alpha}{\pi}\right).
\]
The formula for \(\mathbf H+I\) is identical with the two quadrant classes interchanged.

For \(E_\varepsilon^+\), a convenient affine map from the disk is
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
Substitution yields
\[
4\left(1-\frac{\alpha_\varepsilon}{\pi}\right)
=
\frac8\pi\arctan\varepsilon.
\]
Reflection across a coordinate axis swaps the same-sign and opposite-sign quadrants and gives the \(-1\) statement.

Equivalently, the mechanism can be seen directly after anisotropic scaling: in the rotated frequency coordinates
\[
\eta_u=\frac{\xi_1-\xi_2}{\sqrt2},
\qquad
\eta_v=\frac{\xi_1+\xi_2}{\sqrt2},
\]
the bad region for eigenvalue \(+1\) is
\[
|\eta_v|>|\eta_u|.
\]
Putting
\[
\zeta_u=\varepsilon\eta_u,\qquad
\zeta_v=\eta_v
\]
turns this into
\[
|\zeta_u|<\varepsilon|\zeta_v|.
\]
Because the rescaled disk Fourier energy is radial, this is exactly two cones of total angle \(4\arctan\varepsilon\).

### Sharp asymptotic for the truncated strip

The source computation gives the Fourier mass of one bad quadrant as
\[
I_\varepsilon
=
\frac4{\pi^2}
\int_0^\infty
\frac{\sin^2(\varepsilon t)}{t^2}
A(t)\,dt,
\qquad
A(t)=
\int_t^\infty
\frac{\sin^2 p}{p^2}\,dp.
\]
Using
\[
\sin^2p=\frac{1-\cos 2p}{2}
\]
and one integration by parts in the oscillatory term,
\[
A(t)=\frac1{2t}+O(t^{-2})
\qquad (t\ge1).
\]
Split the \(t\)-integral into
\[
(0,1),\qquad (1,\varepsilon^{-1}),\qquad
(\varepsilon^{-1},\infty).
\]
The first and third pieces are \(O(\varepsilon^2)\). On the middle interval,
\[
\frac{\sin^2(\varepsilon t)}{t^2}
=
\varepsilon^2+O(\varepsilon^4t^2),
\]
so
\[
\int_1^{1/\varepsilon}
\frac{\sin^2(\varepsilon t)}{t^2}A(t)\,dt
=
\frac{\varepsilon^2}{2}
\log\frac1\varepsilon
+O(\varepsilon^2).
\]
Therefore
\[
I_\varepsilon
=
\frac2{\pi^2}\varepsilon^2\log\frac1\varepsilon
+O(\varepsilon^2).
\]
The two bad quadrants have equal mass and are orthogonal Fourier pieces, while
\[
\mathbf H-I=-2(P_{++}+P_{--}).
\]
Thus
\[
\|(\mathbf H-I)\chi_{V_\varepsilon}\|_2^2
=
8I_\varepsilon
=
\frac{16}{\pi^2}
\varepsilon^2\log\frac1\varepsilon
+O(\varepsilon^2).
\]
Finally
\[
\|\chi_{V_\varepsilon}\|_2^2
=
|V_\varepsilon|
=
4\varepsilon,
\]
which gives the asserted normalized asymptotic.

## Relation to prior work

Abakumov, Domelevo, Petermichl and Poltoratski, in arXiv:2609.15155v1, prove that bounded open-set indicators can be approximate \(+1\) eigenvectors of the double Hilbert transform. Their continuous example is the truncated diagonal strip above, for which they prove the upper bound
\[
\lesssim \sqrt{\varepsilon|\log\varepsilon|},
\]
and they explicitly contrast this with a related dyadic construction having no logarithmic factor.

The present result adds two points not stated there:

1. the logarithmic loss is sharp for their specific truncated-strip family, with an explicit leading constant;
2. the logarithm is not a continuous double-Hilbert obstruction: diagonal ellipses give bounded \(C^\infty\), strictly convex indicator quasi-eigenvectors with an exact log-free defect.

The all-ellipse identity also gives a closed-form description of both \(\pm1\) defects for every affine disk.

## Limitations

No optimality is claimed among all bounded sets, all convex sets, or all sets with a prescribed eccentricity. In particular, the exponent \(1/2\) is not asserted to be a universal lower bound under any geometric normalization. The result is an \(L^2\) statement for the standard product double Hilbert transform on \(\mathbb R^2\); it does not provide a corresponding sharp bound for iterated commutators. The sharp strip asymptotic concerns exactly the truncated family \(V_\varepsilon\) above and does not assert that every polygonal or nonsmooth truncation must carry a logarithm.

## References

1. E. Abakumov, K. Domelevo, S. Petermichl, A. Poltoratski, *Invariant sets of the double Hilbert transform*, arXiv:2609.15155v1 (2026), https://arxiv.org/abs/2609.15155.
2. C. Fefferman, *Estimates for a double Hilbert transform*, Studia Mathematica 44 (1972), 1–15.
