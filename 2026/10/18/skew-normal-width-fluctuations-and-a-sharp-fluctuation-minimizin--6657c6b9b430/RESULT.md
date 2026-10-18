# Skew-normal width fluctuations and a sharp fluctuation-minimizing cant for isocanted cubes

## Finding

Fix \(\ell>0\). For integers \(d\ge2\) and \(0<a<\ell\), define the centered isocanted cube
\[
I_d(\ell,a)=\{x\in\mathbb R^d: |x_i|\le\ell/2,\ |x_i-x_j|\le\ell-a\ \text{for all }i,j\}.
\]
Let \(U_d\) be uniform on the Euclidean unit sphere and let \(W_{d,a}=h_{I_d}(U_d)+h_{I_d}(-U_d)\) be its random directional width. Set
\[
p=\ell-a,\quad q=a,\quad c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\quad
\mu=\sqrt{\frac2\pi},\quad \sigma^2=1-\frac3\pi,\quad \tau^2=1-\frac2\pi.
\]
The exact mean width is
\[
\mathbb EW_{d,a}=c_d(dp+\sqrt d\,q).
\]
Define \(g(r)=\frac2\pi(\sqrt{1-r^2}+r\arcsin r)\) for \(0\le r\le1\). The exact variance is
\[
\begin{aligned}
\operatorname{Var}(W_{d,a})={}&p^2\left(1+\frac{2(d-1)}\pi-d^2c_d^2\right)
+q^2(1-dc_d^2)\\
&+2pq\sqrt d\bigl(g(d^{-1/2})-dc_d^2\bigr).
\end{aligned}
\]
For fixed \(\ell\) and any cant sequence \(a_d\in(0,\ell)\) with \(a_d\to a\in[0,\ell]\),
\[
W_{d,a_d}-\mathbb EW_{d,a_d}\ \Longrightarrow\
(\ell-a)\sigma Z+a(|H|-\mu),
\]
where \(Z,H\) are independent standard normals. All fixed absolute moments converge. If \(0<a<\ell\), this is a centered, strictly right-skewed skew-normal law. With
\[
\omega=\sqrt{(\ell-a)^2\sigma^2+a^2},\qquad
\alpha=\frac{a}{(\ell-a)\sigma},
\]
its density is
\[
f(x)=\frac2\omega\,\phi\left(\frac{x+a\mu}{\omega}\right)
\Phi\left(\alpha\frac{x+a\mu}{\omega}\right),
\]
where \(\phi,\Phi\) are the standard normal density and distribution function. In particular,
\[
\lim_{d\to\infty}\operatorname{Var}(W_{d,a})
=(\ell-a)^2\sigma^2+a^2\tau^2,
\qquad
\lim_{d\to\infty}\mathbb E[(W_{d,a}-\mathbb EW_{d,a})^3]
=a^3\mu\left(\frac4\pi-1\right).
\]
The variance convergence is uniform for \(a\in[0,\ell]\), extending the width definition continuously to the cube endpoint and the degenerate-segment endpoint. Its limiting profile is **uniquely minimized** at the sharp interior cant
\[
\boxed{\frac{a_*}{\ell}=\frac{\pi-3}{2\pi-5}=0.110344666\ldots},
\]
with minimum \(\ell^2(\pi-3)(\pi-2)/(\pi(2\pi-5))\). Every sequence of exact finite-dimensional variance minimizers on the closed cant interval converges to \(a_*\); for all sufficiently large \(d\), such minimizers lie in the genuine isocanted range \((0,\ell)\).

## Assumptions and scope

All widths and norms are ordinary Euclidean ones in \(\mathbb R^d\). The angular direction \(U_d\) is Haar-uniform. The geometric polytope requires \(d\ge2\) and \(0<a<\ell\); the endpoint values of \(a\) are used only as limits of its zonotope formula. Dimension tends to infinity while \(\ell\) remains fixed. The finite formulas are exact in every indicated dimension, and the weak/moment limits concern centered, **unrescaled** widths. The primary geometric classification is MSC2020 52B12.

## Proof

**1. Zonotope identity and support function.** Put \(p=\ell-a\), \(q=a\). The constraints defining \(I_d\) are equivalent to the existence of \(t\in[-q/2,q/2]\) with \(|x_i-t|\le p/2\) for every \(i\): the intervals \([x_i-p/2,x_i+p/2]\) have common intersection by the pairwise-difference constraints, and this intersection meets \([-q/2,q/2]\) precisely because the coordinate bounds hold. Hence
\[
I_d(\ell,a)=\frac p2[-1,1]^d+\frac q2[-1,1](1,\ldots,1),
\quad
W_{d,a}=p\sum_{i=1}^d|U_{d,i}|+q\left|\sum_{i=1}^dU_{d,i}\right|.
\]
This Minkowski representation is established in earlier work and is used here as input, not claimed as new.

**2. Exact spherical moments.** Rotational invariance gives \(\mathbb E|\langle v,U_d\rangle|=c_d\) for each unit vector \(v\). For unit vectors \(v,w\) with inner product \(r\), Gaussian polar factorization gives
\[
\mathbb E\bigl[|\langle v,U_d\rangle|\,|\langle w,U_d\rangle|\bigr]
=\frac{g(|r|)}d.
\]
For completeness, if \(X,Y\) are standard normals with correlation \(r\), differentiation of their joint Gaussian integral gives \(\frac{d}{dr}\mathbb E|X||Y|=\frac2\pi\arcsin r\). The derivative identity follows by twice integrating by parts, and the sign-correlation integral is the angular measure of Gaussian quadrants. Since the value at \(r=0\) is \(2/\pi\), integration yields \(g(r)\) above. Let \(S=\sum_i|U_{d,i}|\) and \(B=|\sum_iU_{d,i}|\). The diagonal and off-diagonal terms give
\[
\begin{array}{lll}
\mathbb ES=dc_d,&\mathbb ES^2=1+2(d-1)/\pi,\\
\mathbb EB=\sqrt d\,c_d,&\mathbb EB^2=1,\\
&&\mathbb E(SB)=\sqrt d\,g(d^{-1/2}).
\end{array}
\]
Expanding the variance of \(pS+qB\) proves both exact formulas.

**3. Joint normal limit with the spherical denominator.** Write \(U_d=G/\|G\|_2\), where the coordinates of \(G\) are independent \(N(0,1)\). Define
\[
X_d=\frac{\sum_i(|G_i|-\mu)}{\sqrt d},\quad
Y_d=\frac{\sum_i(G_i^2-1)}{\sqrt d},\quad
H_d=\frac{\sum_iG_i}{\sqrt d}.
\]
The multivariate central limit theorem produces a centered Gaussian limit \((X,Y,H)\) with
\[
\operatorname{Var}X=1-2/\pi,\quad
\operatorname{Var}Y=2,\quad
\operatorname{Cov}(X,Y)=\mu,
\quad\operatorname{Cov}(H,X)=\operatorname{Cov}(H,Y)=0.
\]
The covariance \(\mu\) uses \(\mathbb E|G_1|^3=2\mu\); the zero covariances follow from oddness. Thus \(H\) is independent of \((X,Y)\). Taylor expansion of \((1+Y_d/\sqrt d)^{-1/2}\), on events tending to probability one, yields
\[
\sum_i|U_{d,i}|=\mu\sqrt d+X_d-\tfrac\mu2Y_d+o_{\mathbb P}(1),\qquad
\left|\sum_iU_{d,i}\right|=|H_d|+o_{\mathbb P}(1).
\]
The Gaussian variable \(X-\mu Y/2\) has variance
\[
(1-2/\pi)+\mu^2\cdot 2/4-\mu\cdot\mu=1-3/\pi=\sigma^2>0.
\]
The gamma-ratio expansion \(c_d=\mu d^{-1/2}(1+1/(4d)+O(d^{-2}))\) shows that subtracting the **exact** mean has the same limit as subtracting \(p\mu\sqrt d+q\mu\). Slutsky's theorem gives the announced limit, also for any convergent cant sequence.

**4. Moments, density, and sharp variance optimum.** The width function is \(\ell\sqrt d\)-Lipschitz on the unit sphere, since \(p+q=\ell\). Spherical concentration therefore bounds every fixed centered absolute moment uniformly in \(d\), establishing uniform integrability and moment convergence. In the limiting random variable, \(\sigma Z\) is independent of the folded-normal term \(|H|\); their convolution has the displayed skew-normal density, obtained by conditioning on \(|H|\). The folded normal has third centered moment \(\mu(4/\pi-1)>0\), whereas centered Gaussian terms have zero third cumulant. This proves the non-Gaussian distinction and cubic formula.

The exact variance is a quadratic polynomial in \(p,q\), whose three coefficients converge to \(\sigma^2,\tau^2,0\), respectively; hence convergence of this polynomial is uniform over the compact cant interval. Differentiating the limiting quadratic \((\ell-a)^2\sigma^2+a^2\tau^2\) gives the unique minimizer \(a_*=\ell\sigma^2/(\sigma^2+\tau^2)\), which simplifies to the value above. Uniform convergence and strict uniqueness force all exact finite-dimensional minimizers to converge to \(a_*\).

## Verification

The included standalone `checker.py` requires Python 3, NumPy and SciPy and can be run with `python checker.py`. It solves 300 independent facet-inequality linear programs in dimensions 2 through 6 and compares the optima to the support formula, performs reproducible spherical Monte Carlo comparisons against **both** finite exact moments, checks a high-dimensional skew-normal empirical distribution, and checks the unique limiting variance optimizer. All checks passed during preparation. Random finite checks are corroboration only; the infinite conclusions follow from the analytic argument.

## Relationship to prior work

The isocanted-cube family, its invariant cubical face structure, and its explicit zonotope generator decomposition are due to de la Puente and Clavería [R1, R2]. Their volume and polar-volume identities concern different invariants. A subsequent article [R3] computes lower face volumes and incidence numbers and explicitly asks for the mean width. The elementary mean-width identity here answers that question, but is **not** by itself the claimed substantial contribution. The new content assessed here is the exact finite second-moment formula, the full unscaled high-dimensional skew-normal fluctuation law, its nonzero limiting cubic asymmetry, and the unique sharp cant that minimizes limiting width variance at fixed \(\ell\). Classical Gaussian joint central limit and skew-normal convolution machinery are used explicitly rather than claimed as new.

## Limitations

The novelty assessment is bibliographic rather than a mathematical proof of uniqueness: an earlier equivalent statement under general zonotope or rank-one Gaussian perturbation terminology may exist. Finite simulations do not establish the asymptotic law; independent mathematical verification has not been performed. The variance-minimizer limit does not assert a closed formula for the minimizing cant in each finite dimension. Nothing is claimed here about unrelated intrinsic volumes or normalized volume constraints, and the limiting segment at \(a=\ell\) is not a full-dimensional isocanted cube.

## References

- [R1] M. J. de la Puente and P. L. Clavería, *Isocanted alcoved polytopes*, arXiv:2009.13858v1, first submitted 29 September 2020; *Applications of Mathematics* **65** (2020), 703–726, DOI:10.21136/AM.2020.0373-19.
- [R2] M. J. de la Puente and P. L. Clavería, *The volume of an isocanted cube is a determinant*, arXiv:2406.01565v1, 3 June 2024; equation (21) gives the explicit zonotope decomposition.
- [R3] M. J. de la Puente, *Isocanted cube: the lower Lebesgue volumes, incidence numbers and symmetries of this d-dimensional tile*, *Extracta Mathematicae* **40** (2025), 1–26, DOI:10.17398/2605-5686.40.1.1; §7, question 2, concerning mean width.
