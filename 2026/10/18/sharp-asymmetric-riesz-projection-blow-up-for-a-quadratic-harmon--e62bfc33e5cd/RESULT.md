# Sharp asymmetric Riesz-projection blow-up for a quadratic harmonic-Bergman Toeplitz outlier

## Finding

Let \(\mathcal H_h^2\) be the complex harmonic Bergman space of the unit disk with normalized area measure, let \(P_h\) be its orthogonal projection, and let \(T_b=P_h M_{z^2+bz}|_{\mathcal H_h^2}\), where \(b\in\mathbb C\). For \(7/4<|b|<7/3\), the point \(\lambda_b=-12b^2/49\) is the unique isolated spectral point of \(T_b\), and it is a simple eigenvalue. Let \(\Pi_b\) be its Riesz spectral projection. With \(r=|b|\) and \(q=49/(16r^2)\), its operator norm is **exactly**

\[
\|\Pi_b\|=\frac17\left[\frac1{(1-9r^2/49)^2}+\frac{-\log(1-q)-q}{q}\right].
\]

The two collision limits have different orders and explicit leading constants:

\[
\lim_{r\downarrow7/4}\frac{\|\Pi_b\|}{\log\bigl(1/(r-7/4)\bigr)}=\frac17,
\qquad
\lim_{r\uparrow7/3}(7/3-r)^2\|\Pi_b\|=\frac7{36}.
\]

The expressions depend only on \(|b|\), although the eigenvalue rotates with \(b^2\). Outside the displayed open parameter interval there is no isolated spectral point outside the essential spectral curve \(\{z^2+bz:|z|=1\}\). The new quantitative assertion is the exact projection norm and its two distinct boundary laws, not the previously known possibility of a disconnected spectrum.

## Assumptions and scope

The measure is \(dA=\pi^{-1}\,dx\,dy\) on \(\mathbb D\). The orthonormal basis is \(e_k(z)=\sqrt{k+1}\,z^k\) for integers \(k\ge0\), and \(e_k(z)=\sqrt{1-k}\,\bar z^{-k}\) for integers \(k<0\). Let \(U=P_hM_z|_{\mathcal H_h^2}\), whose matrix is the bilateral weighted shift \(Ue_k=w_ke_{k+1}\) with

\[
w_k=\begin{cases}\sqrt{(k+1)/(k+2)},&k\ge0,\\
\sqrt{(-k)/(1-k)},&k\le-1.\end{cases}
\]

The spectral projection is the contour integral \(\Pi_b=(2\pi i)^{-1}\int_\Gamma(\zeta I-T_b)^{-1}\,d\zeta\), where \(\Gamma\) is a sufficiently small positively oriented contour around \(\lambda_b\). The result does not define an isolated-eigenvalue projection at either endpoint \(|b|=7/4\) or \(|b|=7/3\).

## Proof

**1. Exact rank-one reduction.** Direct orthogonal projection of normalized monomials gives \(T_{z^2}=U^2+(1/6)e_1\otimes e_{-1}\), with the convention \((x\otimes y)f=\langle f,y\rangle x\). The two operators agree on every basis vector except \(e_{-1}\), where their coefficients toward \(e_1\) are respectively \(2/3\) and \(1/2\). Consequently

\[
T_b=p_b(U)+\frac16 e_1\otimes e_{-1},\qquad p_b(z)=z^2+bz.
\]

The weights are positive and tend to one at both ends of \(\mathbb Z\). The operator \(U\) is a compact perturbation of the bilateral unitary shift, while \(\|U^n\|\le1\) and \(\|U^{-n}\|\le n+1\) for positive integers \(n\) (the products of successive reciprocal weights telescope on either side of the origin). Hence \(\sigma(U)=\{z:|z|=1\}\). The polynomial spectral-mapping theorem gives \(\sigma(p_b(U))=p_b(\partial\mathbb D)\), which is also the essential spectrum of \(T_b\).

**2. Isolated eigenvalue and its simplicity.** For \(\lambda\notin p_b(\partial\mathbb D)\), set \(R_\lambda=(p_b(U)-\lambda I)^{-1}\) and \(m(\lambda)=\langle R_\lambda e_1,e_{-1}\rangle\). Rank-one inversion shows that \(\lambda\) is an eigenvalue exactly when \(1+m(\lambda)/6=0\). Let \(\alpha,\beta\) be the roots of \(p_b(z)=\lambda\). The resolvent expansions

\[
(U-aI)^{-1}=\sum_{n\ge0}a^nU^{-n-1}\quad(|a|<1),
\qquad
(U-aI)^{-1}=-\sum_{n\ge0}a^{-n-1}U^n\quad(|a|>1)
\]

converge in operator norm. Since \(\langle U^{-2}e_1,e_{-1}\rangle=2\) and all other powers contribute zero to the same matrix entry, they give \(\langle(U-aI)^{-1}e_1,e_{-1}\rangle=2a\) for \(|a|<1\), and zero for \(|a|>1\). For distinct roots, partial fractions imply that \(m(\lambda)=0\) if both roots are exterior, \(m(\lambda)=2\) if both are interior, and \(m(\lambda)=2\alpha/(\alpha-\beta)\) when \(|\alpha|<1<|\beta|\). The same two constant cases hold for a repeated root by differentiating the scalar resolvent, so a repeated root cannot produce an isolated eigenvalue.

In the mixed-root case the equation \(m(\lambda)=-6\) forces \(\beta=4\alpha/3\), hence \(\alpha=-3b/7\), \(\beta=-4b/7\), and \(\lambda=-12b^2/49\). The strict mixed-root condition is precisely \(7/4<|b|<7/3\). Differentiating the roots with respect to \(\lambda\) gives \(\alpha'=1/(\alpha-\beta)\), \(\beta'=-1/(\alpha-\beta)\), and

\[
m'(\lambda_b)=\frac{2b}{(\alpha-\beta)^3}=\frac{686}{b^2}\ne0.
\]

Thus the resolvent has a simple pole, the eigenvalue has algebraic multiplicity one, and the rank-one perturbation introduces no other spectral points off the essential curve.

**3. Exact Riesz-projection norm.** Put \(R=R_{\lambda_b}\), \(v=Re_1\), and \(u=R^*e_{-1}\). The rank-one resolvent formula and the nonzero derivative above give

\[
\Pi_b=\frac{v\otimes u}{m'(\lambda_b)},\qquad
\|\Pi_b\|=\frac{\|v\|\,\|u\|}{|m'(\lambda_b)|}.
\]

Let \(d=\alpha-\beta=b/7\). Expanding the two resolvents yields the exact coefficients

\[
\langle v,e_{-n}\rangle=\frac{\sqrt{2(n+1)}\,\alpha^n}{d}\quad(n\ge0),
\qquad
\langle v,e_{n+1}\rangle=\frac{\sqrt{2/(n+2)}\,\beta^{-n-1}}{d}\quad(n\ge0).
\]

The corresponding row coefficients for \(u\) give the same squared norm as for \(v\). Writing \(q=|\beta|^{-2}\in(0,1)\), the elementary series \(\sum_{n\ge0}(n+1)t^n=(1-t)^{-2}\) and \(\sum_{n\ge0}q^{n+1}/(n+2)=(-\log(1-q)-q)/q\) yield

\[
\|v\|^2=\|u\|^2=\frac2{|d|^2}\left[\frac1{(1-|\alpha|^2)^2}+\frac{-\log(1-q)-q}{q}\right].
\]

Substituting \(|d|^2=r^2/49\) and \(|m'(\lambda_b)|=686/r^2\) establishes the displayed exact formula. Near \(r=7/4\), \(1-q\sim(8/7)(r-7/4)\), while the first summand remains finite; hence the logarithmic coefficient is \(1/7\). Near \(r=7/3\), \(1-9r^2/49\sim(6/7)(7/3-r)\), while the logarithmic summand remains finite; hence the quadratic coefficient is \(7/36\).

## Verification

The independent symbolic checks in the proof are the rank-one coefficient \(2/3-1/2=1/6\), the two resolvent matrix entries, the derivative \(686/b^2\), and the exact evaluation of two convergent norm series. The included `checker.py` uses only the Python 3 standard library. Run `python3 checker.py` to compare the exact spectral-projection norm against truncations of right and left resolvent eigenvectors, their pairing, and the eigenvector residual in four representative real and complex parameter choices. A finite-section test is only supplementary evidence; the proof establishes the infinite-dimensional identities.

## Relationship to prior work

Wang and Zhao (2021) established that a quadratic analytic-symbol Toeplitz operator on harmonic Bergman space can have disconnected spectrum and proved Weyl's theorem for low-degree polynomial symbols. Huang, Wang and Zhao (2026, arXiv:2610.09638v1) established the general finite-outlier structure for analytic polynomial symbols and a root-based criterion. Those spectral-set statements motivate the present quantitative question. Knowing that an outlying eigenvalue exists, or even knowing its location, does not determine the norm of its nonorthogonal Riesz projection: similarity transformations preserve eigenvalues but can change projection norms. The contribution here is the full closed formula for the projection condition number and its *different logarithmic and quadratic collision scales*.

## Limitations

The theorem concerns the unweighted harmonic Bergman Hilbert space and the one-complex-parameter quadratic symbol \(p_b(z)=z^2+bz\). It does not give projection norms for arbitrary polynomial symbols, endpoint embedded eigenvectors, or global pseudospectral bounds. The complete text of the earlier Wang–Zhao 2021 quadratic example was unavailable during comparison; it could affect priority, even though the accessible abstract describes spectral disconnectedness rather than spectral-projection conditioning. The new result has not undergone independent mathematical review.

## References

1. M. Huang, J. Wang and X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638v1, first released 2026-10-07. https://arxiv.org/html/2610.09638v1
2. C. Wang and X. Zhao, *Weyl's theorem for Toeplitz operators with polynomial symbols on the harmonic Bergman space*, J. Math. Anal. Appl. 495 (2021), 124770. DOI:10.1016/j.jmaa.2020.124770.
3. K. Guo and D. Zheng, *Toeplitz algebra and Hankel algebra on the harmonic Bergman space*, J. Math. Anal. Appl. 276 (2002), 213–230. DOI:10.1016/S0022-247X(02)00429-8.
