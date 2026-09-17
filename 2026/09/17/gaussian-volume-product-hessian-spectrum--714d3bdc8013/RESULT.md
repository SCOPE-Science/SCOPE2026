# Exact second-variation spectrum of the uncentered Gaussian volume product at the ball

Let
\[
G_\sigma^n(K)=\gamma_\sigma^n(K)\,\gamma_\sigma^n(K^\circ),
\]
where \(\gamma_\sigma^n\) is the centered Gaussian probability measure on \(\mathbb R^n\) with covariance \(\sigma^2I_n\), and \(K^\circ\) is the polar body with respect to the origin.

Artstein-Avidan, Fradelizi and Wyczesany recently proved that the Euclidean unit ball \(B=B_2^n\) is always a critical point, and that translated balls destabilize it when
\[
\sigma^2>\frac{2}{n+1}.
\]
The calculation below gives the full Hessian of \(G_\sigma^n\) at \(B\) for arbitrary smooth support-function perturbations and diagonalizes it in spherical harmonics.

## Theorem

Let \(n\ge 2\), \(\sigma>0\), and \(\varphi\in C^2(S^{n-1})\). For sufficiently small \(t\), let \(K_t\) be the strictly convex body with support function
\[
h_t(u)=1+t\varphi(u).
\]
Write
\[
M=\gamma_\sigma^n(B),\qquad
a=(2\pi\sigma^2)^{-n/2}e^{-1/(2\sigma^2)},
\]
and let \(d\omega\) denote the usual surface measure on \(S^{n-1}\). Then
\[
\left.\frac{d}{dt}G_\sigma^n(K_t)\right|_{t=0}=0,
\]
and
\[
\boxed{
\left.\frac{d^2}{dt^2}G_\sigma^n(K_t)\right|_{t=0}
=
Ma\left[
-\int_{S^{n-1}}|\nabla_S\varphi|^2\,d\omega
+\left(2n-\frac{2}{\sigma^2}\right)
\int_{S^{n-1}}\varphi^2\,d\omega
\right]
-2a^2\left(\int_{S^{n-1}}\varphi\,d\omega\right)^2 .
}
\]

Consequently, after decomposing \(\varphi\) into spherical harmonics:

1. The constant mode is strictly negative for every \(\sigma>0\).
2. On degree \(\ell\ge1\), the Hessian eigenvalue, up to the positive \(L^2\)-normalization factor, is
   \[
   \lambda_\ell
   =
   Ma\left(
   2n-\frac{2}{\sigma^2}-\ell(\ell+n-2)
   \right).
   \]
3. Every degree \(\ell\ge2\) mode is strictly negative for every \(\sigma>0\); in particular
   \[
   \lambda_2=-\frac{2Ma}{\sigma^2}<0.
   \]
4. The only mode whose sign can change is degree \(1\), corresponding exactly to infinitesimal translations:
   \[
   \lambda_1=Ma\left(n+1-\frac{2}{\sigma^2}\right).
   \]

Thus:

- if \(\sigma^2<2/(n+1)\), the second variation is strictly negative in every nonzero \(C^2\) support direction;
- if \(\sigma^2=2/(n+1)\), its kernel is exactly the \(n\)-dimensional space of degree-one spherical harmonics and every other mode is strictly negative;
- if \(\sigma^2>2/(n+1)\), the positive eigenspace is exactly the \(n\)-dimensional degree-one space, while all other modes remain strictly negative.

In particular, the translated-ball perturbations used to detect failure above \(2/(n+1)\) exhaust the entire linear instability of the ball. For \(n\ge3\), throughout the still-open global range
\[
\frac1n<\sigma^2<\frac{2}{n+1},
\]
the ball has strictly negative second variation in every smooth support direction.

## Proof

For small \(t\),
\[
\nabla_S^2 h_t+h_tI
=
I+t(\nabla_S^2\varphi+\varphi I)
\]
is positive definite, so \(h_t\) is the support function of a smooth strictly convex body. Put
\[
A=\nabla_S^2\varphi+\varphi I.
\]
The boundary point with outer normal \(u\) is
\[
x_t(u)=h_t(u)u+\nabla_Sh_t(u).
\]

### Gaussian measure of \(K_t\)

The Gaussian surface-area density in support coordinates is
\[
a\,
\exp\!\left(-\frac{|x_t|^2-1}{2\sigma^2}\right)
\det(I+tA)\,d\omega.
\]
Since the normal velocity of the support perturbation is \(\varphi\),
\[
\left.\frac d{dt}\gamma_\sigma^n(K_t)\right|_{0}
=a\int\varphi\,d\omega.
\]
At \(t=0\),
\[
\left.\frac d{dt}\log
\exp\!\left(-\frac{|x_t|^2-1}{2\sigma^2}\right)\right|_0
=-\frac{\varphi}{\sigma^2},
\]
because \(x_0=u\) and
\(\dot x_0=\varphi u+\nabla_S\varphi\), while
\[
\left.\frac d{dt}\det(I+tA)\right|_0
=\operatorname{tr}A
=\Delta_S\varphi+(n-1)\varphi.
\]
Therefore
\[
\left.\frac{d^2}{dt^2}\gamma_\sigma^n(K_t)\right|_0
=a\int\varphi\left(
\Delta_S\varphi+(n-1)\varphi-\frac{\varphi}{\sigma^2}
\right)d\omega,
\]
hence, by integration by parts,
\[
\left.\frac{d^2}{dt^2}\gamma_\sigma^n(K_t)\right|_0
=a\left[
-\int|\nabla_S\varphi|^2\,d\omega
+\left(n-1-\frac1{\sigma^2}\right)\int\varphi^2\,d\omega
\right].
\]

### Gaussian measure of the polar

Because \(h_t\) is the actual support function,
\[
\rho_{K_t^\circ}(u)=\frac1{h_t(u)}=\frac1{1+t\varphi(u)}.
\]
Define
\[
F(r)=(2\pi\sigma^2)^{-n/2}
\int_0^r e^{-s^2/(2\sigma^2)}s^{n-1}\,ds.
\]
Then
\[
F'(1)=a,\qquad
F''(1)=a\left(n-1-\frac1{\sigma^2}\right),
\]
and
\[
\gamma_\sigma^n(K_t^\circ)
=
\int_{S^{n-1}}
F\!\left(\frac1{1+t\varphi}\right)d\omega.
\]
Since
\[
\left.\frac d{dt}(1+t\varphi)^{-1}\right|_0=-\varphi,
\qquad
\left.\frac {d^2}{dt^2}(1+t\varphi)^{-1}\right|_0=2\varphi^2,
\]
we get
\[
\left.\frac d{dt}\gamma_\sigma^n(K_t^\circ)\right|_0
=-a\int\varphi\,d\omega,
\]
and
\[
\left.\frac {d^2}{dt^2}\gamma_\sigma^n(K_t^\circ)\right|_0
=
a\left(n+1-\frac1{\sigma^2}\right)\int\varphi^2\,d\omega.
\]

### The product Hessian

At \(t=0\), both factors equal \(M\). The two first variations cancel in the first derivative of the product, while the cross term in the second derivative is
\[
2\left(a\int\varphi\right)\left(-a\int\varphi\right)
=-2a^2\left(\int\varphi\right)^2.
\]
Combining the preceding formulas gives the boxed identity.

### Harmonic diagonalization

For a spherical harmonic \(Y_\ell\) of degree \(\ell\ge1\),
\[
\int Y_\ell\,d\omega=0,\qquad
-\Delta_SY_\ell=\ell(\ell+n-2)Y_\ell.
\]
The asserted eigenvalue formula follows immediately.

For \(\ell\ge2\),
\[
\ell(\ell+n-2)\ge 2n,
\]
so
\[
\lambda_\ell\le -\frac{2Ma}{\sigma^2}<0.
\]
For \(\ell=1\) one obtains
\[
\lambda_1=Ma\left(n+1-\frac2{\sigma^2}\right).
\]

It remains to check the constant mode. If \(|S^{n-1}|=\Omega\), its coefficient per unit \(L^2\)-mass is
\[
\lambda_0
=
Ma\left(2n-\frac2{\sigma^2}\right)-2a^2\Omega.
\]
Write
\[
I=\int_0^1e^{-r^2/(2\sigma^2)}r^{n-1}\,dr,
\qquad
J=\int_0^1e^{-r^2/(2\sigma^2)}r^{n+1}\,dr.
\]
Since \(M=(2\pi\sigma^2)^{-n/2}\Omega I\),
\[
\frac{a\Omega}{M}=\frac{e^{-1/(2\sigma^2)}}{I}.
\]
Integrating
\[
\frac d{dr}\left(r^n e^{-r^2/(2\sigma^2)}\right)
=
e^{-r^2/(2\sigma^2)}r^{n-1}
\left(n-\frac{r^2}{\sigma^2}\right)
\]
from \(0\) to \(1\) yields
\[
e^{-1/(2\sigma^2)}=nI-\frac{J}{\sigma^2}.
\]
As \(0<J<I\),
\[
\frac{a\Omega}{M}
=
n-\frac{J}{\sigma^2I}
>
n-\frac1{\sigma^2}.
\]
This is exactly \(\lambda_0<0\). The spectral conclusions follow.

## Relation to the recent result

Artstein-Avidan, Fradelizi and Wyczesany derive the Euler--Lagrange equation for maximizers and, in Proposition 5.1, perturb \(B_2^n\) only by translations \(h_\varepsilon(u)=1+\varepsilon\langle u,e\rangle\). Their quadratic coefficient is the \(\ell=1\) case above and proves non-optimality for \(\sigma^2>2/(n+1)\).

The theorem here computes the complete support-function Hessian. It shows that the same threshold is a genuine spectral transition: no shape mode of degree at least \(2\), and no radial mode, can destabilize the ball at second order for any \(\sigma\).

## Limitations

This is a local second-variation statement. It does not settle whether the ball is a global maximizer in dimensions \(n\ge3\) for
\[
1/n<\sigma^2\le 2/(n+1),
\]
nor does it decide the nonlinear behavior of the degree-one kernel exactly at \(\sigma^2=2/(n+1)\). Strict negativity of the Hessian in each fixed nonzero smooth direction is not asserted here as a uniform \(C^2\)-neighborhood stability theorem.

Originality is asserted only to the best of our knowledge. The motivating preprint is extremely recent, so unindexed concurrent work remains a residual risk.

## References

1. S. Artstein-Avidan, M. Fradelizi, K. Wyczesany, *Uncentered Blaschke--Santaló inequalities for the Gaussian measure*, arXiv:2609.18472v1 (2026).
2. D. Cordero-Erausquin, *Santaló's inequality on \(\mathbb C^n\) by complex interpolation*, C. R. Math. Acad. Sci. Paris 334 (2002), 767--772, DOI: 10.1016/S1631-073X(02)02328-2.
