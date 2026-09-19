# The full support-function Hessian of the uncentered Gaussian Santaló product

## Statement

Let
\[
d\gamma^n_\sigma(x)=c_{n,\sigma}e^{-|x|^2/(2\sigma^2)}\,dx,
\qquad
G^n_\sigma(K)=\gamma^n_\sigma(K)\,\gamma^n_\sigma(K^\circ),
\]
where \(K\subset\mathbb R^n\) is a convex body containing the origin in its interior and \(K^\circ\) is its polar. Fix \(n\ge2\) and let \(B=B_2^n\).

Put
\[
q=\sigma^{-2},\qquad
m=\gamma^n_\sigma(B),\qquad
a=c_{n,\sigma}e^{-q/2},\qquad
R=\frac{a\,|\mathbb S^{n-1}|}{m},
\]
and let \(d\nu=d\omega/|\mathbb S^{n-1}|\) be normalized spherical measure. For \(f\in C^2(\mathbb S^{n-1})\), let \(K_t\) have support function
\[
h_t=1+t f
\]
for sufficiently small \(|t|\), so that \(K_t\) remains strictly convex.

Then the unit ball is critical for every such support-function variation and its exact logarithmic Hessian is
\[
\boxed{
\left.\frac{d^2}{dt^2}\right|_{t=0}\log G^n_\sigma(K_t)
=
R\!\left[-\int |\nabla_S f|^2\,d\nu
+2(n-q)\int f^2\,d\nu\right]
-2R^2\!\left(\int f\,d\nu\right)^2 .
}
\tag{1}
\]

If
\[
f=\sum_{\ell\ge0} f_\ell,
\qquad
-\Delta_{\mathbb S^{n-1}}f_\ell=\lambda_\ell f_\ell,
\qquad
\lambda_\ell=\ell(\ell+n-2),
\]
is its spherical-harmonic decomposition, then (1) diagonalizes as
\[
\boxed{
Q_\sigma(f)
=
2R(n-q-R)\|f_0\|_2^2
+
R\sum_{\ell\ge1}
\bigl(2(n-q)-\lambda_\ell\bigr)\|f_\ell\|_2^2 .
}
\tag{2}
\]
Here all \(L^2\)-norms are with respect to \(\nu\).

Consequently:

1. If
\[
\boxed{\sigma^2<\frac{2}{n+1}},
\]
then \(Q_\sigma(f)<0\) for every nonzero \(f\). Thus the ball is strictly stable to second order in every support-function direction.

2. If
\[
\boxed{\sigma^2=\frac{2}{n+1}},
\]
then the Hessian kernel is exactly the degree-one harmonic space
\[
\mathcal H_1=\{u\mapsto\langle u,e\rangle:e\in\mathbb R^n\},
\]
which is precisely the space of infinitesimal translations. Every degree \(\ell\neq1\) is strictly stable.

3. If
\[
\boxed{\sigma^2>\frac{2}{n+1}},
\]
then the only positive Hessian directions are the \(n\)-dimensional translation space \(\mathcal H_1\). The constant mode and every harmonic degree \(\ell\ge2\) remain strictly negative for every finite \(\sigma\).

Hence the threshold \(2/(n+1)\) found from translated balls is not merely a convenient destabilizing test: it is the exact loss-of-second-order-stability threshold, and translations are the unique modes responsible for the loss.

At the critical variance, translations are quadratic null directions but still decrease the product at fourth order. More precisely, for \(e\in\mathbb S^{n-1}\), \(K_t=B+t e\), and \(q=(n+1)/2\),
\[
\boxed{
\frac{G^n_\sigma(B+t e)}{m^2}
=
1-C_n t^4+O(t^6),
\qquad C_n>0,
}
\tag{3}
\]
where
\[
C_n=
\frac{R(n+1)}{32n^2(n+2)}
\left(2R(n+1)(n+2)+n(17-n^2)\right).
\tag{4}
\]
In particular, the translated-ball perturbation does not break maximality at the endpoint itself.

## Context

Artstein-Avidan, Fradelizi and Wyczesany recently introduced the uncentered Gaussian volume-product problem in this form. They prove that the Euclidean ball is the unique global maximizer when \(n\ge3\) and \(\sigma^2\le1/n\), that it is not a maximizer when \(\sigma^2>2/(n+1)\), and that in dimension two the exact global threshold is \(\sigma^2=2/3\). Their instability proof above \(2/(n+1)\) uses the single translated-ball family \(B+te\). For \(n\ge3\), the global range
\[
\frac1n<\sigma^2\le\frac{2}{n+1}
\]
remains open in their work.

The formulas above show that throughout the open part of this global gap,
\[
\frac1n<\sigma^2<\frac{2}{n+1},
\]
the ball is nevertheless strictly stable in every fixed smooth infinitesimal support direction. Thus any failure of global optimality inside that interval cannot be detected by a quadratic perturbation of the ball. It would have to be genuinely nonlinear, nonlocal, or arise through a mechanism invisible to the Hessian.

There is also a useful classical-limit interpretation. For \(\ell=2\), the eigenvalue in (2) equals \(-2Rq\), so it tends to zero as \(\sigma\to\infty\); the constant eigenvalue also tends to zero. These are exactly the infinitesimal homothety and ellipsoidal degeneracies expected from linear invariance of the classical Lebesgue volume product. Finite Gaussian variance removes those affine degeneracies, while the degree-one translation mode changes sign at the finite threshold above.

## Proof of the Hessian formula

Write
\[
A(t)=\gamma^n_\sigma(K_t),\qquad
B(t)=\gamma^n_\sigma(K_t^\circ).
\]
For a smooth support function \(h\), the inverse Gauss parametrization of \(\partial K\) is
\[
x(u)=h(u)u+\nabla_S h(u),
\]
and the ordinary surface-area density is
\[
\det(\nabla_S^2h+hI)\,d\omega.
\]
The Gaussian first-variation formula therefore gives, at the unit ball,
\[
A'(0)=a\int f\,d\omega.
\tag{5}
\]
For \(h_t=1+tf\), differentiation of the Gaussian surface-area density yields
\[
\left.\frac{d}{dt}\right|_0
\left[e^{-q|x_t|^2/2}\det(\nabla_S^2h_t+h_tI)\right]
=e^{-q/2}\bigl(\Delta_S f+(n-1-q)f\bigr).
\]
Hence
\[
A''(0)
=a\int f\bigl(\Delta_S f+(n-1-q)f\bigr)\,d\omega
=a\left[-\int|\nabla_S f|^2\,d\omega+(n-1-q)\int f^2\,d\omega\right].
\tag{6}
\]

For the polar body,
\[
\rho_{K_t^\circ}(u)=\frac1{h_t(u)}.
\]
Define
\[
F(r)=c_{n,\sigma}\int_0^r e^{-qs^2/2}s^{n-1}\,ds.
\]
Then
\[
B(t)=\int_{\mathbb S^{n-1}}F\!\left(\frac1{1+tf(u)}\right)d\omega(u),
\]
with
\[
F'(1)=a,
\qquad
F''(1)=a(n-1-q).
\]
Since
\[
(1+tf)^{-1}=1-tf+t^2f^2+O(t^3),
\]
we obtain
\[
B'(0)=-a\int f\,d\omega,
\tag{7}
\]
and
\[
B''(0)=a(n+1-q)\int f^2\,d\omega.
\tag{8}
\]
Equations (5) and (7) cancel, so the ball is critical. Since \(A(0)=B(0)=m\),
\[
\frac{d^2}{dt^2}\Big|_0\log(A(t)B(t))
=
\frac{A''(0)+B''(0)}m
-2\left(\frac{a\int f\,d\omega}{m}\right)^2.
\]
Substituting (6) and (8) and normalizing spherical measure gives (1).

To diagonalize, use
\[
\int|\nabla_S f_\ell|^2\,d\nu=\lambda_\ell\|f_\ell\|_2^2
\]
and orthogonality. Only the constant mode contributes to the squared mean, yielding (2).

It remains to determine the sign of the constant mode. Let
\[
I_0=\int_0^1 e^{-qr^2/2}r^{n-1}\,dr,
\qquad
I_2=\int_0^1 e^{-qr^2/2}r^{n+1}\,dr.
\]
Then \(m=c_{n,\sigma}|\mathbb S^{n-1}|I_0\), and integration of
\[
\frac{d}{dr}\left(r^ne^{-qr^2/2}\right)
\]
from \(0\) to \(1\) gives
\[
e^{-q/2}=nI_0-qI_2.
\]
Therefore
\[
R=n-q\frac{I_2}{I_0}>n-q,
\tag{9}
\]
because \(I_2<I_0\). Thus the constant coefficient \(2R(n-q-R)\) is always negative.

For \(\ell=1\), \(\lambda_1=n-1\), so the eigenvalue is
\[
R(n+1-2q),
\]
which changes sign exactly at \(q=(n+1)/2\), i.e. \(\sigma^2=2/(n+1)\). For \(\ell\ge2\), \(\lambda_\ell\ge\lambda_2=2n\), and hence
\[
R(2(n-q)-\lambda_\ell)\le-2Rq<0.
\]
This proves the full sign classification.

## Fourth order on the critical translation branch

Set \(q=(n+1)/2\), \(Y(u)=\langle u,e\rangle\), and \(K_t=B+te\). The relevant spherical moments are
\[
\int Y^2\,d\nu=\frac1n,
\qquad
\int Y^4\,d\nu=\frac{3}{n(n+2)}.
\]
Expanding the shifted Gaussian integral for \(A(t)\), and expanding
\(F((1+tY)^{-1})\) for the polar factor, gives
\[
\frac{A(t)}m
=1-\frac{R(n+1)}{4n}t^2
+\frac{R(n+1)^2(n+3)}{64n(n+2)}t^4+O(t^6),
\]
and
\[
\frac{B(t)}m
=1+\frac{R(n+1)}{4n}t^2
+\frac{R(n+1)(n^2-4n-37)}{64n(n+2)}t^4+O(t^6).
\]
Multiplication yields (3)-(4). At the critical value, (9) gives
\[
R>\frac{n-1}{2}.
\]
Hence the bracket in (4) is bounded below by
\[
(n-1)(n+1)(n+2)+n(17-n^2)=2n^2+16n-2>0,
\]
so \(C_n>0\).

## What is and is not resolved

The result determines the complete quadratic variational spectrum of the ball and the first nonzero term on the critical translation branch. It does **not** settle the global maximization problem in dimensions \(n\ge3\) for \(1/n<\sigma^2\le2/(n+1)\). It also does not claim a full fourth-order normal form at the endpoint: only the actual translation branch is expanded to order four. Finally, strict negativity of the Hessian is a second-variation statement for fixed smooth support directions; no topology-uniform quantitative neighborhood theorem is claimed here.

## References

1. S. Artstein-Avidan, M. Fradelizi, K. Wyczesany, *Uncentered Blaschke-Santaló inequalities for the Gaussian measure*, arXiv:2609.18472 (2026). https://arxiv.org/abs/2609.18472
2. D. Cordero-Erausquin, *Santaló's inequality on C^n by complex interpolation*, C. R. Math. Acad. Sci. Paris 334 (2002), 767-772. https://www.numdam.org/item/10.1016/S1631-073X%2802%2902328-2/
3. A. Colesanti, A. Kolesnikov, G. Livshyts, L. Rotem, *On weighted Blaschke-Santaló and strong Brascamp-Lieb inequalities*, arXiv:2409.11503 (2024). https://arxiv.org/abs/2409.11503
