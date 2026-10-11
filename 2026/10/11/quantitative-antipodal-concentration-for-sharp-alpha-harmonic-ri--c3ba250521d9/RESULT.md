# Quantitative antipodal concentration for sharp \(\alpha\)-harmonic Riesz–Fejér traces

## Finding

Fix an integer \(n\ge2\), a real parameter \(\alpha>\max\{-1,-(n-1)/2\}\), and a unit vector \(\eta\in\mathbb S^{n-1}\). The sharp \(L^2\) Riesz–Fejér trace inequality for the invariant Poisson extension has a quantitative deficit controlling the boundary \(L^2\) mass outside any fixed neighborhoods of the two antipodal endpoints. Specifically, for every \(0<\delta\le1\) and every complex- or real-valued \(f\in L^2(\mathbb S^{n-1},d\sigma)\),
\[
\mathcal C_{n,\alpha}\|f\|_2^2-\|T_{\alpha,\eta}f\|_{2,\mu}^2
\ge \kappa_{n,\alpha}(\delta)
\int_{E_\delta}|f(\xi)|^2\,d\sigma(\xi),
\]
where the positive constant \(\kappa_{n,\alpha}(\delta)\) is explicit below. Hence equality in the sharp norm inequality is impossible for any nonzero boundary datum; moreover every normalized extremizing sequence loses all its \(L^2\) mass away from the two antipodal caps. The sharp constant itself is due to Li, Luo, and Xu (2026); the assertion here is the quantitative *deficit and universal near-extremizer concentration*.

## Assumptions and scope

Surface measure \(d\sigma\) on \(\mathbb S^{n-1}\) has total mass one. Set \(d\mu(r)=(1-r^2)^{n-2}\,dr\) for \(-1<r<1\), and define
\[
c_{n,\alpha}=\frac{\Gamma((n+\alpha)/2)\Gamma(1+\alpha/2)}{\Gamma(n/2)\Gamma(1+\alpha)},\qquad
P_\alpha(r\eta,\xi)=c_{n,\alpha}\frac{(1-r^2)^{1+\alpha}}{|r\eta-\xi|^{n+\alpha}},
\qquad T_{\alpha,\eta}f(r)=\int_{\mathbb S^{n-1}}P_\alpha(r\eta,\xi)f(\xi)\,d\sigma(\xi).
\]
Put \(R_n=\omega_{n-2}/\omega_{n-1}\), where \(\omega_j\) denotes the surface area of \(\mathbb S^j\), and let
\[
b_0=B\left(\frac{n-1}{4},\frac{\alpha+1+(n-1)/2}{2}\right),\quad
\mathcal C_{n,\alpha}=2^{2\alpha+n-2}c_{n,\alpha}^2R_n b_0^2,\quad
\mathscr A=c_{n,\alpha}R_n2^{\alpha+(n-1)/2}b_0.
\]
Define the hypergeometric function
\[
F(t)={}_2F_1\left(-\frac{\alpha+(n-1)/2}{2},-\frac{\alpha+1}{2};\frac{n+1}{4};t\right),\qquad 0\le t\le1.
\]
For \(0<\delta\le1\), define the complement of the two Euclidean boundary caps
\[
E_\delta=\{\xi\in\mathbb S^{n-1}:|\xi-\eta|\ge\delta,\ |\xi+\eta|\ge\delta\}.
\]
The explicit quantitative constant, which is not claimed to be optimal, is
\[
\boxed{\kappa_{n,\alpha}(\delta)=
\frac{4\mathscr A\,c_{n,\alpha}}{3\,2^{n+\alpha}}
\left(1-\frac{F(1/4)}{F(1)}\right)
\left[\delta^2\left(1-\frac{\delta^2}{4}\right)\right]^{(n-1)/4}>0.}
\]
The stated range agrees with the sharp-constant range at exponent \(p=2\) of Li–Luo–Xu: for \(n=2\), it is \(\alpha>-1/2\); for \(n\ge3\), it is \(\alpha>-1\).

## Proof

**1. Exact positive comparison functions.** Put \(h(\xi)=(1-\langle\xi,\eta\rangle^2)^{-(n-1)/4}\) and \(g(r)=(1-r^2)^{-(n-1)/2}\). Both are positive and finite almost everywhere, and \(h\in L^1(d\sigma)\), though \(h\notin L^2(d\sigma)\). The angular beta/hypergeometric integration formula (Li–Luo–Xu, Section 3.1, with \(p=2\)) gives the *exact* equality
\[
(Th)(r)=\mathscr A\,g(r)\frac{F(r^2)}{F(1)}.
\]
The Gauss evaluation at one and duplication formula give \(\mathscr A=c_{n,\alpha}R_n2^{\alpha+(n-1)/2}b_0\). Both numerator hypergeometric parameters are strictly negative, the denominator parameter is positive, and the convergence excess is \(\alpha+1+(n-1)/2>0\). The hypergeometric monotonicity lemma (or Euler's integral and differentiation) shows \(F\) strictly increases on \([0,1]\); in particular \(0<F(1/4)<F(1)<\infty\). Thus the pointwise radial Schur gap is strictly positive:
\[
\mathscr A g(r)-(Th)(r)=\mathscr A g(r)\left(1-\frac{F(r^2)}{F(1)}\right)>0\quad(-1<r<1).
\]

**2. Dual Schur majorization.** The beta-integral bound in Li–Luo–Xu, Lemma 2.1 and Section 3.2 at \(p=2\), gives
\[
T^*g(\xi)\le\mathscr B h(\xi),\quad
\mathscr B=c_{n,\alpha}2^{\alpha+(n-1)/2-1}b_0,\quad
\mathscr A\mathscr B=\mathcal C_{n,\alpha}.
\]
Here \(T^*q(\xi)=\int_{-1}^{1}P_\alpha(r\eta,\xi)q(r)\,d\mu(r)\) denotes the positive-kernel formal adjoint. All inequalities hold for almost every nonpolar \(\xi\) and are justified for nonnegative data by Tonelli.

**3. An exact defect inequality.** Cauchy–Schwarz with measure \(P_\alpha(r\eta,\xi)h(\xi)\,d\sigma(\xi)\) yields
\[
|Tf(r)|^2\le(Th)(r)\int_{\mathbb S^{n-1}}P_\alpha(r\eta,\xi)\frac{|f(\xi)|^2}{h(\xi)}\,d\sigma(\xi).
\]
Integrating and using Tonelli gives
\[
\mathcal C_{n,\alpha}\|f\|_2^2-\|Tf\|_{2,\mu}^2
\ge\int_{\mathbb S^{n-1}}\frac{|f(\xi)|^2}{h(\xi)}\bigl(\mathcal C_{n,\alpha}h(\xi)-T^*Th(\xi)\bigr)\,d\sigma(\xi)
\ge \int_{\mathbb S^{n-1}}\frac{|f(\xi)|^2}{h(\xi)}T^*(\mathscr A g-Th)(\xi)\,d\sigma(\xi).
\]
This remains valid if the right-hand integrals are initially interpreted via nonnegative truncation; the norm bound controls finiteness in the stated \(L^2\) domain.

**4. Uniform interior positivity and the cap geometry.** For \(|r|\le1/2\), \(g(r)\ge1\), \(F(r^2)\le F(1/4)\), and
\[
P_\alpha(r\eta,\xi)\ge c_{n,\alpha}(3/4)^{1+\alpha}(2/3)^{n+\alpha},\qquad (1-r^2)^{n-2}\ge(3/4)^{n-2}.
\]
The interval \([-1/2,1/2]\) has length one; consequently for every nonpolar \(\xi\),
\[
T^*(\mathscr A g-Th)(\xi)\ge
\frac{4\mathscr A c_{n,\alpha}}{3\,2^{n+\alpha}}
\left(1-\frac{F(1/4)}{F(1)}\right).
\]
For \(\xi\in E_\delta\), the two inequalities \(|\xi\mp\eta|\ge\delta\) imply \(|\langle\xi,\eta\rangle|\le1-\delta^2/2\), and therefore
\[
\frac1{h(\xi)}=(1-\langle\xi,\eta\rangle^2)^{(n-1)/4}
\ge\left[\delta^2(1-\delta^2/4)\right]^{(n-1)/4}.
\]
Substitution in the defect inequality proves the claimed \(\kappa_{n,\alpha}(\delta)\).

**5. Nonattainment and necessary concentration.** The sets \(E_\delta\) increase to \(\mathbb S^{n-1}\setminus\{\eta,-\eta\}\) as \(\delta\downarrow0\). Since the two points have zero surface measure, every nonzero \(f\) has positive squared mass on some \(E_\delta\), forcing strict norm inequality. If \(\|f_j\|_2=1\) and \(\|Tf_j\|_{2,\mu}^2\to\mathcal C_{n,\alpha}\), then for each fixed \(\delta\),
\[
\int_{E_\delta}|f_j|^2\,d\sigma
\le\frac{\mathcal C_{n,\alpha}-\|Tf_j\|_{2,\mu}^2}{\kappa_{n,\alpha}(\delta)}\longrightarrow0.
\]
Such extremizing sequences do exist: Li–Luo–Xu construct them using endpoint-singular boundary powers (their Section 3.2). This is a *necessary* localization statement, not a sufficiency characterization of arbitrary concentrating sequences.

## Verification

The proof above verifies the strict hypergeometric gap, beta normalization, pointwise kernel lower bound and exact cap-geometry bound without assuming numerical experiments imply general truth. As a numerical consistency check only, arbitrary-precision calculations for \((n,\alpha)=(2,0),(2,0.75),(3,-0.5),(3,0),(5,2),(8,-0.9)\) confirmed the equality \(\mathscr A\mathscr B=\mathcal C_{n,\alpha}\), the independent Gauss/duplication formula for \(\mathscr A\), and positive \(\kappa_{n,\alpha}(1/2)\); the fully reproducible checker is included in `check_constants.py`. The analytic inequalities, not these finite checks, prove the theorem for all admissible parameters.

## Relationship to prior work

Li, Luo and Xu prove the sharp trace norm and exhibit one family attaining it asymptotically [1]. Their sharpness construction establishes the existence of an extremizing sequence, not the quantitative deficit or the universal necessity that *all* extremizing sequences concentrate at the two antipodal endpoints. The earlier theorem of Ahmed and Khalfallah [2] concerns the hyperbolic subfamily \(\alpha=n-2\); [1] already generalizes its sharp norm and supplies the explicit Schur identities used here. The result is a localization strengthening of the sharp bound, rather than another computation of the bound itself.

## Limitations

The displayed \(\kappa_{n,\alpha}(\delta)\) is an explicit strictly positive bound, not a claimed optimal stability constant. Concentration at the antipodal pair is necessary for near extremality; it is **not** asserted to be sufficient or to specify how the mass divides between the two poles. There is no result outside \(\alpha>\max\{-1,-(n-1)/2\}\), and no claim of an independent verification.

## References

[1] Q. Li, S. Luo, and Z. Xu, *Riesz–Fejér type Inequalities for \(\alpha\)-Harmonic Functions in the Unit Ball*, arXiv:2606.14457v1 (first posted 12 June 2026), Theorem 1.1, Lemma 2.1 and Section 3. https://arxiv.org/abs/2606.14457

[2] I. Ahmed and A. Khalfallah, *Riesz–Fejér inequalities for hyperbolic harmonic functions in the unit ball*, *Journal of Mathematical Analysis and Applications* 563 (2026), article 130826. https://doi.org/10.1016/j.jmaa.2026.130826
