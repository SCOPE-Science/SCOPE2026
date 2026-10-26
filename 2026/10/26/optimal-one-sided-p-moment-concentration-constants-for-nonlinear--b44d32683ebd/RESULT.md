# Optimal one-sided \(p\)-moment concentration constants for nonlinear product functions

## Finding
Let \(1<p\leq2\). Define
\[
F(u)=u-1+e^{-u},\qquad
C_p=\sup_{u>0}\frac{F(u)}{u^p},\qquad
c_p=\frac{p-1}{p}(pC_p)^{-1/(p-1)}.
\]
For any positive integer \(n\), independent random inputs \(X_1,\ldots,X_n\), and real measurable function \(f(X_1,\ldots,X_n)\) that is integrable and bounded above, define the coordinate deficits \(D_i\) and moment budget \(V\) below. If \(0<V<\infty\), then for every \(t>0\),
\[
\Pr\{f(X)-\mathbb Ef(X)\geq t\}\leq
\exp\left[-c_p\left(\frac{t^p}{V}\right)^{1/(p-1)}\right].\tag{1}
\]
**The numerical coefficient \(c_p\) is best possible uniformly over all sample sizes, product distributions, and functions in this class.** Even independent two-point inputs with the additive function \(f=-\sum_iX_i\) rule out every larger coefficient. If \(V=0\), the function is almost surely constant.

For \(1<p<2\), \(C_p\) has a unique positive maximizer \(u_p\), characterized by
\[
\frac{u_p(1-e^{-u_p})}{u_p-1+e^{-u_p}}=p.
\]
For \(p=2\), \(C_2=c_2=1/2\) and the supremum defining \(C_2\) occurs in the limit \(u\downarrow0\). The previously available exponent coefficient \((p-1)/p\) is strictly smaller for all \(1<p<2\). For example, \(c_{3/2}=0.9179352766\ldots\), rather than \(1/3\). Moreover, \(c_p\to1\) as \(p\downarrow1\), so the improvement factor diverges as \(p\downarrow1\).

## Assumptions and scope
Each input takes values in an arbitrary measurable space. Conditional on all other coordinates, let
\[
s_i(x_{-i})=\operatorname*{ess\,sup}_{z\sim X_i}
 f(x_1,\ldots,x_{i-1},z,x_{i+1},\ldots,x_n),
\quad D_i(x)=s_i(x_{-i})-f(x)\geq0.
\]
With \(\mathbb E^{(i)}\) denoting integration over input \(i\) while other inputs are fixed, set
\[
V=\operatorname*{ess\,sup}_{x\sim\mathcal L(X)}
\sum_{i=1}^n\mathbb E^{(i)}[D_i(X)^p](x).
\]
Assume \(f(X)\) is integrable and essentially bounded above and \(V<\infty\). The statement is uniform in \(n\), the distributions, and all measurable nonlinear functions satisfying these assumptions. There is no independence assumption between the deficits, only independence of input coordinates. Finite \(p\)-moment of the deficits allows infinite variance of \(f\) for \(p<2\).

## Proof
**1. Optimal scalar coefficient.** Write \(F(u)=u-1+e^{-u}\), which is positive for \(u>0\). Its logarithmic elasticity is
\[
k(u)=\frac{uF'(u)}{F(u)}=\frac{u(1-e^{-u})}{u-1+e^{-u}}.
\]
Direct differentiation yields
\[
k'(u)=\frac{e^{-u}\big(u^2+2-2\cosh u\big)}{F(u)^2}<0
\quad(u>0),
\]
since \(2\cosh u>2+u^2\). The limits are \(k(0+)=2\) and \(k(\infty)=1\). Hence, when \(1<p<2\), the function \(F(u)/u^p\) increases and then decreases, with its unique maximum at the displayed solution \(k(u_p)=p\). At \(p=2\), \(F(u)\leq u^2/2\) with equality only in the limit \(u\downarrow0\). Therefore
\[
e^{-u}\leq 1-u+C_pu^p\quad(u\geq0)
\tag{2}
\]
with the smallest possible coefficient \(C_p\).

**2. Conditional exponential moments.** Fix \(i\) and all other coordinates. Because \(f=s_i-D_i\), equation (2), the logarithmic inequality \(\log z\leq z-1\), and conditional integration give, for \(\beta>0\),
\[
\log\mathbb E^{(i)}e^{\beta f}-\beta\mathbb E^{(i)}f
=\log\mathbb E^{(i)}e^{-\beta D_i}+\beta\mathbb E^{(i)}D_i
\leq C_p\beta^p\mathbb E^{(i)}D_i^p.
\tag{3}
\]

**3. Global bound.** The reverse-KL tensorization proposition proved by Eshima, Esposito and Paudice (2026, Proposition 3.4 and Appendix A.2) states, for independent inputs and any bounded-above integrable \(h\),
\[
\log\mathbb E e^{h}-\mathbb Eh
\leq\operatorname*{ess\,sup}\sum_i
\big(\log\mathbb E^{(i)} e^h-\mathbb E^{(i)}h\big).
\tag{4}
\]
For completeness, its proof uses the tilted density \(\rho=e^h/\mathbb Ee^h\), conditional densities \(g_S=\mathbb E[\rho\mid X_S]\), and a uniform random ordering of the coordinates. Conditional Donsker--Varadhan inequalities bound telescoping increments of \(\rho\); joint convexity of KL bounds their entropy costs by the telescoping total \(D_{\mathrm{KL}}(\rho P\Vert P)\), which cancels, leaving exactly (4). Thus it is applicable to \(h=\beta(f-b)\) for an essential upper bound \(b\), and (3) gives
\[
\log\mathbb E e^{\beta(f-\mathbb Ef)}\leq C_pV\beta^p.
\tag{5}
\]
Minimizing \(-\beta t+C_pV\beta^p\) at \(\beta=(t/(pC_pV))^{1/(p-1)}\) proves (1). When \(V=0\), equation (5) for all \(\beta\) forces \(f\) constant almost surely.

**4. Sharpness of the tail coefficient.** Let \(X_i\) be independent, with \(\Pr(X_i=1)=\varepsilon\) and \(\Pr(X_i=0)=1-\varepsilon\), and put \(f=-\sum_{i=1}^nX_i\). Then \(D_i=X_i\) and \(V=n\varepsilon\). For any \(0<\kappa<1\), take \(t=n\varepsilon(1-\kappa)\). The event in (1) becomes \(\{\operatorname{Bin}(n,\varepsilon)\leq\kappa n\varepsilon\}\). For each fixed \(\varepsilon\), the binomial large-deviation theorem gives the exact exponential rate
\[
\lim_{n\to\infty}-\frac1n\log\Pr\{\operatorname{Bin}(n,\varepsilon)\leq\kappa n\varepsilon\}
=d(\kappa\varepsilon\Vert\varepsilon),
\]
where \(d(a\Vert b)=a\log(a/b)+(1-a)\log((1-a)/(1-b))\). As \(\varepsilon\downarrow0\),
\[
\varepsilon^{-1}d(\kappa\varepsilon\Vert\varepsilon)
\longrightarrow 1-\kappa+\kappa\log\kappa.
\]
Consequently, no valid universal exponent coefficient can exceed
\[
R_p(\kappa)=\frac{1-\kappa+\kappa\log\kappa}{(1-\kappa)^{p/(p-1)}}.
\tag{6}
\]
For \(1<p<2\), choose \(\kappa=e^{-u_p}\). The maximizing equation \(u_pF'(u_p)=pF(u_p)\), together with \(F'(u_p)=1-\kappa\), shows
\[
R_p(e^{-u_p})=\frac{(p-1)F(u_p)}{F'(u_p)^{p/(p-1)}}
=\frac{p-1}{p}(pC_p)^{-1/(p-1)}=c_p.
\]
Thus every larger exponent fails on an additive Bernoulli example. At \(p=2\), (6) tends to \(1/2\) as \(\kappa\uparrow1\), proving optimality of \(c_2=1/2\). The order of limits is first \(n\to\infty\), next \(\varepsilon\downarrow0\), and for \(p=2\) finally \(\kappa\uparrow1\); no finite enumeration replaces this argument.

**5. Small-moment endpoint.** The same rare-Bernoulli expression proves \(\lim_{p\downarrow1}c_p=1\). Indeed \(c_p\leq\lim_{\kappa\downarrow0}R_p(\kappa)=1\). For each fixed \(\delta\in(0,1)\), when \(\kappa\leq\delta\), its numerator is uniformly at least \(1-\delta+\delta\log\delta\), while the denominator is at most one. For \(\kappa\geq\delta\), use \(1-\kappa+\kappa\log\kappa\geq(1-\kappa)^2/2\), so \(R_p(\kappa)\geq\frac12(1-\delta)^{2-p/(p-1)}\to\infty\) as \(p\downarrow1\). Letting \(\delta\downarrow0\) proves the limit.

## Verification
The attached standalone Python program checks the exact coefficient equations numerically at six orders, the coincidence of the binomial rare-event rate and derived sharp exponent for interior orders, and 3,600 randomly generated nonlinear product functions against (5). The calculus, large-deviation, and tensorization arguments above are the mathematical proof; finite computations are consistency checks, not exhaustive verification. The source appendix's conditional-density, random-permutation, convexity, and entropy-telescoping steps of the nonstandard tensorization lemma were inspected separately.

## Relationship to prior work
Eshima, Esposito and Paudice (2026), Theorem 3.1, prove (1) with \(c_p\) replaced by \((p-1)/p\), using their reverse-KL tensorization and the nonoptimal scalar estimate \(F(u)\leq u^p/p\). That work establishes the functional setup and global tensorization; the present finding supplies the exact best universal constant and its matching rare-event obstruction. For \(1<p<2\) the exponent improvement is strict, and as \(p\downarrow1\) its multiplicative advantage is unbounded. Aminian (2026) gives the earlier additive heavy-tailed concentration estimate with the same unoptimized coefficient. Work on optimal left-tail bounds with prescribed first and second moments (Pinelis, 2016), and on heavy-tail large deviations assuming finite variance (Bakhshizadeh, Maleki and de la Peña, 2020/2023), imposes different moment information and does not state the uniform nonlinear product-function constant here. The scalar optimization is elementary; sharpness of the *universal nonlinear tail coefficient* is the distinguishing global claim.

## Limitations
The normalization uses the uncentered, one-sided coordinate deficit budget \(V\); it is not a theorem about variance proxies, two-sided tails, or a best pointwise tail envelope for fixed \(n,t,V\). No assertion of equality for any fixed finite sample is made. The proof relies on the previously established reverse-KL tensorization lemma. Literature overlap cannot be ruled out absolutely, particularly an equivalent constant hidden in older one-sided large-deviation analyses. An earlier additive paper was located but its full text could not be inspected in this review. Independent validation of this result has not been performed.

## References
1. H. Eshima, A. R. Esposito and A. Paudice, *A One-Sided McDiarmid-Type Inequality for Heavy Tails via Reverse KL Tensorization*, arXiv:2610.21103v1 (first public 15 October 2026), especially Theorem 3.1, Proposition 3.4, and Appendix A.2. https://arxiv.org/html/2610.21103v1
2. G. Aminian, *Generalization Bounds Under Heavy-Tailed Losses*, Proceedings of Machine Learning Research 300, 5005–5013 (2026). https://proceedings.mlr.press/v300/aminian26a.html
3. I. Pinelis, *Optimal binomial, Poisson, and normal left-tail domination for sums of nonnegative random variables*, Electronic Journal of Probability 21 (2016), arXiv:1503.06482. https://arxiv.org/abs/1503.06482
4. M. Bakhshizadeh, A. Maleki and V. H. de la Peña, *Sharp Concentration Results for Heavy-Tailed Distributions*, arXiv:2003.13819, Information and Inference 12 (2023), 1655–1685. https://arxiv.org/html/2003.13819
