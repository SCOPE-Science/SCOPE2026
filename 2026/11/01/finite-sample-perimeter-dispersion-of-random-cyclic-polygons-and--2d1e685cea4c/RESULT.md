# Exact finite-sample perimeter variance of uniform random cyclic polygons

## Finding

Take \(n\ge3\) independent points with normalized uniform arclength law on the unit circle, and let \(L_n\) be the Euclidean perimeter of their convex hull. For \(k\ge0\) and \(a>0\), put
\[
J_k(a)=\frac{k!}{(ia)^{k+1}}\left(e^{ia}-\sum_{j=0}^k\frac{(ia)^j}{j!}\right).
\]
Define
\[
\begin{aligned}
u_n&=(n-1)\operatorname{Im}J_{n-2}(\pi),&
v_n&=(n-1)\operatorname{Re}J_{n-2}(2\pi),\\
r_n&=(n-1)(n-2)\operatorname{Re}\big(J_{n-3}(\pi)-J_{n-2}(\pi)\big),&
s_n&=\frac{(n-1)(n-2)}{\pi}\operatorname{Im}J_{n-3}(\pi).
\end{aligned}
\]
Then \(\mathbb E L_n=2nu_n\) and the exact finite-sample variance is
\[
\operatorname{Var}(L_n)=2n(1-v_n)+2n(n-1)(s_n-r_n)-4n^2u_n^2.
\]
The contribution is the evaluated finite-sample expression for arbitrary \(n\), including the nonpolynomial two-gap mixed moment. The mean, the already documented fixed-four variance, and the asymptotic coefficients obtainable from earlier mixed power-sum calculations are not claimed as new.

## Assumptions and scope

Root the cyclic order at a labelled sampled point, not at a fixed angular cutoff. After rotation this puts one point at zero and leaves \(n-1\) iid uniform arguments. The successive gaps \(X_1,\ldots,X_n\), in units of one revolution, have the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. An oriented gap \(x\) contributes the ordinary Euclidean chord \(2\sin(\pi x)\), including when \(x>1/2\). Distinct samples and a nondegenerate polygon occur almost surely. The formula concerns the full perimeter, not the semiperimeter, and does not assume an asymptotic regime.

## Proof

The affine map from the ordered \(n-1\) uniform arguments to the first \(n-1\) gaps has determinant one, giving the constant simplex density \((n-1)!\). The one-gap density is \((n-1)(1-x)^{n-2}\) on \((0,1)\). Taylor's integral remainder for the exponential, or integration by parts, gives \(J_k(a)=\int_0^1(1-t)^ke^{iat}\,dt\). Hence \(\mathbb E\sin(\pi X_1)=u_n\) and \(\mathbb E\sin^2(\pi X_1)=(1-v_n)/2\).

Two distinct gaps have joint density \((n-1)(n-2)(1-x-y)^{n-3}\) on \(x,y>0\), \(x+y<1\). On each slice \(x+y=z\), the product-to-sum identity gives the integrated mixed term
\[
\int_0^z \sin(\pi x)\sin(\pi(z-x))\,dx
=\frac12\left(\frac{\sin(\pi z)}{\pi}-z\cos(\pi z)\right).
\]
Integrating this against \((n-1)(n-2)(1-z)^{n-3}\,dz\) gives \((s_n-r_n)/2\); here \(z(1-z)^{n-3}=(1-z)^{n-3}-(1-z)^{n-2}\). Squaring \(L_n=2\sum_{i=1}^n\sin(\pi X_i)\) gives \(n\) diagonal terms and \(n(n-1)\) ordered cross terms. Subtracting the squared mean proves the expression. In particular, it evaluates to \(6-48/\pi^2\) for \(n=3\) and \(8-444/\pi^2+4608/\pi^4-9216/\pi^6\) for \(n=4\). These are checks of the general formula, not separate priority claims.

## Relationship to prior results

Nikitin and Polevaya study the mean for this model [1]. The Dirichlet-gap framework and central-limit behavior are prior [2, 5, 6]. The exact four-vertex variance is given in [3], whose joint laws and integrations are specifically for four gaps. Work on area–perimeter regression [4, steps 1–2] gives both the perimeter Taylor expansion and the exact mixed covariances of the monomial spacing sums. It already yields the asymptotic coefficients through \(n^{-7}\): with \(T_j=\sum_i X_i^j\), the expansion of \(\operatorname{Var}(T_3)\) has coefficients \(360,-6048,60552\) at orders \(n^{-5},n^{-6},n^{-7}\), and \(\operatorname{Cov}(T_3,T_5)=28800n^{-7}+O(n^{-8})\). Multiplying by \(\pi^6/9\) and \(-\pi^8/90\), respectively, yields \(40\pi^6n^{-5}-672\pi^6n^{-6}+(6728\pi^6-320\pi^8)n^{-7}+O(n^{-8})\). The Taylor and moment bounds in [4] suffice here: the seventh-power remainder is \(O_{L^2}(n^{-6})\) and the centered cubic term is \(O_{L^2}(n^{-5/2})\). Neither an asymptotic variance law nor a list of monomial covariances gives the evaluated finite sine moment above without an additional integration or resummation.

## Verification and limitations

The companion `check_random_cyclic_perimeter.py` retains the finite-integral comparisons, triangle and quadrilateral checks, factorial-moment diagnostics and angle simulations. The simplex integration, not the numerical examples, proves the variance identity for all integers \(n\ge3\). The expression gives the exact variance of a natural circle-length estimator at finite sample size. It does not give the full perimeter distribution, apply off the circle, or by itself guarantee numerical conditioning of the finite sums at large \(n\). Earlier full texts [5, 6] were not available for a complete exact-moment comparison; historical priority remains provisional.

## References

1. Ya. Yu. Nikitin and T. A. Polevaya, *On the average perimeter of the inscribed random polygon*, DOI:10.21638/11701/spbu01.2020.108.
2. S. Wang, Z. Li, and W.-Q. Xu, *Nonlinear Random Extrapolation Estimates of \(\pi\) Under Dirichlet Distributions*, DOI:10.33993/jnaat522-1360.
3. *Exact perimeter–area second moments of a random cyclic quadrilateral*, Resultary record `1c13b772d78d`, 2026/10/12.
4. *Sharp area–perimeter regression and fourth-order decorrelation for random cyclic polygons*, Resultary record `c0156d4b4464`, 2026/10/25.
5. C. Bélisle, *On the polygon generated by n random points on a circle*, DOI:10.1016/j.spl.2010.11.012.
6. S. Wang and W.-Q. Xu, *Random cyclic polygons from Dirichlet distributions and approximations of pi*, DOI:10.1016/j.spl.2018.05.007.
