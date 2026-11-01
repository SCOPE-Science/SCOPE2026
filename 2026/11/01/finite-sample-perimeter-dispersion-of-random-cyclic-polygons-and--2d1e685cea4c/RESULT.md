# Finite-sample perimeter dispersion of random cyclic polygons and two higher-order corrections

## Finding
Let \(n\ge3\) be an integer, and sample \(n\) points independently and uniformly by arclength from the unit circle. Write \(L_n\) for the perimeter of their convex hull. For \(k\ge0\) and real \(a>0\), define
\[
J_k(a)=\int_0^1(1-t)^k e^{iat}\,dt=\frac{k!}{(ia)^{k+1}}\left(e^{ia}-\sum_{j=0}^k\frac{(ia)^j}{j!}\right).
\]
Define the real numbers
\[
\begin{aligned}
u_n&=(n-1)\operatorname{Im}J_{n-2}(\pi),\\
v_n&=(n-1)\operatorname{Re}J_{n-2}(2\pi),\\
r_n&=(n-1)(n-2)\operatorname{Re}\left(J_{n-3}(\pi)-J_{n-2}(\pi)\right),\\
s_n&=\frac{(n-1)(n-2)}{\pi}\operatorname{Im}J_{n-3}(\pi).
\end{aligned}
\]
Then the exact finite-size expectation and variance are
\[
\boxed{\mathbb E L_n=2n u_n},\qquad
\boxed{\operatorname{Var}(L_n)=2n(1-v_n)+2n(n-1)(s_n-r_n)-4n^2u_n^2}.
\]
In particular,
\[
\operatorname{Var}(L_3)=6-\frac{48}{\pi^2},\qquad
\operatorname{Var}(L_4)=8-\frac{444}{\pi^2}+\frac{4608}{\pi^4}-\frac{9216}{\pi^6}.
\]
The dispersion has the following three-term large-sample expansion, including two corrections beyond the classical leading order:
\[
\boxed{\operatorname{Var}(L_n)=\frac{40\pi^6}{n^5}-\frac{672\pi^6}{n^6}
+\frac{6728\pi^6-320\pi^8}{n^7}+O(n^{-8})}.
\]
The term \(40\pi^6 n^{-5}\) is a known asymptotic variance scale; the finite-size formula and its subsequent coefficients are the contributions considered here.

## Assumptions and scope
All points are independent with normalized uniform arclength law on a circle of radius one. Ordering their arguments cyclically and rooting at one sampled point, the normalized successive gaps \(X_1,\ldots,X_n\) form a \(\operatorname{Dirichlet}(1,\ldots,1)\) vector, with all entries positive and sum one almost surely. The root choice does not affect the perimeter. The chord corresponding to a gap \(x\) has length \(2\sin(\pi x)\), even when \(x>1/2\). Thus \(L_n=2\sum_{j=1}^n\sin(\pi X_j)\). These are ordinary Euclidean polygon perimeters, not sums of shorter central arc lengths. The formulas cover every integer \(n\ge3\), with no asymptotic qualification for the exact expression.

## Proof
**Gap reduction and the first moment.** Fix one sampled point by rotational invariance, and sort the remaining \(n-1\) independent uniform angles. Their \(n\) gaps, including the closing gap, have the constant Dirichlet density \((n-1)!\) on the simplex. Every single gap has density \((n-1)(1-x)^{n-2}\) on \((0,1)\). Consequently \(\mathbb E\sin(\pi X_1)=u_n\) and \(\mathbb E\cos(2\pi X_1)=v_n\), giving the stated mean and the identity \(\mathbb E\sin^2(\pi X_1)=(1-v_n)/2\).

**The two-gap second moment.** For two distinct gaps, the pair has joint density \((n-1)(n-2)(1-x-y)^{n-3}\) on \(x,y>0\), \(x+y<1\). Write \(z=x+y\); conditional on \(z\), the first gap is uniform on \((0,z)\). Hence
\[
\begin{aligned}
\mathbb E\cos\big(\pi(X_1-X_2)\big)
&=(n-1)(n-2)\int_0^1(1-z)^{n-3}\frac{\sin(\pi z)}\pi\,dz=s_n,\\
\mathbb E\cos\big(\pi(X_1+X_2)\big)
&=(n-1)(n-2)\int_0^1z(1-z)^{n-3}\cos(\pi z)\,dz=r_n.
\end{aligned}
\]
The product-to-sum identity gives \(\mathbb E[\sin(\pi X_1)\sin(\pi X_2)]=(s_n-r_n)/2\). Squaring \(L_n\), counting \(n\) diagonal and \(n(n-1)\) ordered off-diagonal contributions, and subtracting the squared mean proves the finite-size variance. Integrating by parts gives the displayed finite expression for \(J_k(a)\), so the answer consists of elementary finite sums. Substitution at \(n=3,4\) yields the exact special values.

**Two finite-size corrections.** Set \(T_j=\sum_{i=1}^n X_i^j\). Taylor's alternating bound on \([0,\pi]\) gives
\[
L_n=2\pi-\frac{\pi^3}{3}T_3+\frac{\pi^5}{60}T_5+R_n,
\qquad |R_n|\le\frac{\pi^7}{2520}T_7.
\]
For nonnegative integer exponents, Dirichlet moments are
\[
\mathbb E\prod_{i=1}^nX_i^{m_i}
=\frac{\prod_i m_i!}{n(n+1)\cdots(n+\sum_i m_i-1)}.
\]
Directly summing the diagonal and off-diagonal products gives the exact identities
\[
\operatorname{Var}(T_3)=
\frac{72(n-1)(5n+11)}{(n+1)^2(n+2)^2(n+3)(n+4)(n+5)},
\]
\[
\operatorname{Cov}(T_3,T_5)=
\frac{14400(n-1)(2n+5)}{(n+1)^2(n+2)^2(n+3)(n+4)(n+5)(n+6)(n+7)}.
\]
Their expansions are respectively
\[
\operatorname{Var}(T_3)=360n^{-5}-6048n^{-6}+60552n^{-7}+O(n^{-8}),
\quad\operatorname{Cov}(T_3,T_5)=28800n^{-7}+O(n^{-8}).
\]
Moreover \(\operatorname{Var}(T_5)=O(n^{-9})\) and \(\mathbb E[T_7^2]=O(n^{-12})\), by the same factorial moment formula. Cauchy--Schwarz bounds the covariance of \(R_n\) with \(T_3\) by \(O(n^{-17/2})\), and its other variance and covariance contributions are smaller. Thus, through terms of order \(n^{-7}\),
\[
\operatorname{Var}(L_n)=\frac{\pi^6}{9}\operatorname{Var}(T_3)
-\frac{\pi^8}{90}\operatorname{Cov}(T_3,T_5)+O(n^{-8}),
\]
which gives all three asserted coefficients. This proof controls remainders as \(n\to\infty\), rather than inferring them from a finite experiment.

## Verification
The accompanying standalone script `check_random_cyclic_perimeter.py` evaluates the closed finite sums against independent one- and two-gap beta-density quadratures for each integer \(3\le n\le10\). It also verifies exact rational Dirichlet identities at several integer indices, the explicit triangle and quadrilateral variances, and independent iid-uniform-angle simulations. These computations corroborate, but are not premises of, the analytic proof.

## Relationship to prior work
Nikitin and Polevaya (2020) study the mean perimeter in exactly this random-polygon model. Bélisle (2011) gives large-sample convergence and normal approximation. Wang and Xu (2018), and Wang, Li, and Xu (2023), place the same polygon in the Dirichlet-spacing framework and study asymptotic fluctuations and related extrapolation estimators. In particular, the first coefficient \(40\pi^6\) for the full perimeter follows from previously known first-order asymptotics. A standard Dirichlet monomial-moment identity also underlies the present derivation and is not claimed new. The present scope is the compact exact finite-integer perimeter variance and the two explicitly evaluated next-order coefficients, which are not stated in the inspected accessible full text of Wang, Li, and Xu (2023). Priorities involving inaccessible full texts remain provisional.

## Limitations
This result uses exactly iid uniform arclength samples on a circle; it does not cover nonuniform angular distributions, interior-uniform points, arbitrary convex curves, circumscribed polygons, or joint area-perimeter covariance. The leading \(n^{-5}\) variance scale and central-limit theorem are prior literature. The formulas determine variance, not the full perimeter distribution. Historical priority is provisional given limited access to some earlier full texts.

## References
1. Ya. Yu. Nikitin and T. A. Polevaya, *On the average perimeter of the inscribed random polygon*, Vestnik of Saint Petersburg University, Mathematics, Mechanics, Astronomy **7** (2020), 77--84. https://doi.org/10.21638/11701/spbu01.2020.108 . Author full text: https://www.researchgate.net/publication/340563585_On_the_average_perimeter_of_the_inscribed_random_polygon .
2. S. Wang, Z. Li, and W.-Q. Xu, *Nonlinear random extrapolation estimates of pi under Dirichlet distributions*, J. Numer. Anal. Approx. Theory **52** (2023), 273--294, https://doi.org/10.33993/jnaat522-1360 . Full-text HTML: https://ictp.acad.ro/jnaat/journal/article/view/1360/1463 .
3. C. Bélisle, *On the polygon generated by n random points on a circle*, Statist. Probab. Lett. **81** (2011), 236--242, https://doi.org/10.1016/j.spl.2010.11.012 .
4. S. Wang and W.-Q. Xu, *Random cyclic polygons from Dirichlet distributions and approximations of pi*, Statist. Probab. Lett. **140** (2018), 84--90, https://doi.org/10.1016/j.spl.2018.05.007 .
