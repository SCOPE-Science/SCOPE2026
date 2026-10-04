# Maximum-to-margin likelihood ratios characterize convex copula diagonals
## Finding
Let \(d\ge 2\). Let \((X_1,\ldots,X_d)\) have a common absolutely continuous distribution function \(F\) that is strictly increasing on an interval support \(I\), with density \(f>0\) almost everywhere on \(I\). Let \(C\) be the copula and
\[
\Delta(u)=C(u,\ldots,u),\qquad 0\le u\le 1,
\]
its diagonal. Put \(M=\max_{1\le i\le d}X_i\).

Every copula diagonal is \(d\)-Lipschitz, hence absolutely continuous. Writing \(q=\Delta'\) almost everywhere gives
\[
0\le q(u)\le d\quad\text{a.e.},\qquad \int_0^1q(u)\,du=1.
\]
The maximum has density \(g_M\) satisfying
\[
\frac{g_M(x)}{f(x)}=q(F(x))\quad\text{for a.e. }x\in I.
\]
Therefore the following are equivalent:

1. \(\Delta\) is convex;
2. for the uniform-margin realization, a coordinate is smaller than the maximum in likelihood-ratio order;
3. for every common margin satisfying the regularity above,
\[
X_1\le_{\mathrm{lr}}M.
\]

Thus diagonal convexity has an exact stochastic-order meaning: it is precisely monotonicity of the maximum-to-margin likelihood ratio.

There is also a margin-free information identity that does not require diagonal convexity. For any convex \(\phi:[0,d]\to\mathbb R\) with \(\phi(1)=0\), define
\[
D_\phi(P\|Q)=\int \phi\!\left(\frac{dP}{dQ}\right)dQ.
\]
Then
\[
D_\phi(\mathcal L(M)\|\mathcal L(X_1))
=\int_0^1\phi(q(u))\,du
\]
and
\[
0\le D_\phi(\mathcal L(M)\|\mathcal L(X_1))
\le \left(1-\frac1d\right)\phi(0)+\frac1d\phi(d).
\]
The upper bound is sharp. If \(\phi\) is strictly convex, equality at the lower endpoint forces \(q=1\) almost everywhere, hence \(\Delta(u)=u\). Equality at the upper endpoint forces \(q\in\{0,d\}\) almost everywhere; the mean-one constraint and monotonicity of the extremal representative give
\[
\Delta(u)=\max\{du-d+1,0\}.
\]
For Kullback–Leibler divergence, \(\phi(t)=t\log t\) with \(0\log0=0\), so
\[
0\le D_{\mathrm{KL}}(\mathcal L(M)\|\mathcal L(X_1))\le \log d.
\]
Under independence, \(q(u)=d u^{d-1}\), giving the exact intermediate value
\[
D_{\mathrm{KL}}(\mathcal L(M)\|\mathcal L(X_1))
=\log d-\frac{d-1}{d}.
\]

## Assumptions and scope
The likelihood-ratio statement is for a common absolutely continuous margin whose CDF is strictly increasing on an interval support and whose density is positive almost everywhere. These assumptions make the density ratio well defined on the common support and make the probability-integral transform invertible up to null sets. The copula itself need not be absolutely continuous. The diagonal is automatically absolutely continuous because every \(d\)-dimensional copula diagonal is \(d\)-Lipschitz.

The information identity and bound require only the same marginal regularity and the ordinary copula-diagonal constraints; diagonal convexity is not needed. The stated finite upper envelope assumes \(\phi\) is finite on \([0,d]\). The Kullback–Leibler specialization is in the direction \(D_{\mathrm{KL}}(\mathcal L(M)\|\mathcal L(X_1))\); the reverse divergence can be infinite for the lower Fréchet–Hoeffding extremal diagonal.

## Proof
By Sklar's representation,
\[
\Pr(M\le x)=C(F(x),\ldots,F(x))=\Delta(F(x)).
\]
A copula diagonal satisfies \(\Delta(1)=1\), \(\Delta(0)=0\), and
\[
0\le \Delta(v)-\Delta(u)\le d(v-u),\qquad 0\le u\le v\le1.
\]
Hence \(\Delta\) is absolutely continuous. Its almost-everywhere derivative \(q\) satisfies \(0\le q\le d\), and the fundamental theorem of calculus gives \(\int_0^1q=1\).

Because \(F\) is absolutely continuous and \(\Delta\) is Lipschitz, \(\Delta\circ F\) is absolutely continuous. At every point where the ordinary chain rule applies,
\[
g_M(x)=q(F(x))f(x).
\]
The exceptional set is null. If \(N\subset(0,1)\) is the null set where \(\Delta\) is not differentiable, the substitution formula gives \(\int_{F^{-1}(N)}f(x)\,dx=0\); because \(f>0\) almost everywhere, \(F^{-1}(N)\) is null. Since \(f>0\) almost everywhere,
\[
\frac{g_M(x)}{f(x)}=q(F(x))
\]
almost everywhere.

A real function on an interval is convex exactly when its derivative has a nondecreasing representative. Therefore, if \(\Delta\) is convex, \(q\) has a nondecreasing representative, and because \(F\) is increasing, \(q\circ F\) is nondecreasing. This is exactly \(X_1\le_{\mathrm{lr}}M\). Conversely, take the uniform-margin realization. Its coordinate density is one and the maximum density is \(q\). If the coordinate is smaller than the maximum in likelihood-ratio order, \(q\) has a nondecreasing representative, so \(\Delta(u)=\int_0^u q(v)\,dv\) is convex. This proves the equivalence.

For the information identity,
\[
D_\phi(\mathcal L(M)\|\mathcal L(X_1))
=\int_I \phi(q(F(x)))f(x)\,dx
=\int_0^1\phi(q(u))\,du.
\]
Jensen's inequality and \(\int_0^1q=1\) give the lower bound \(\int\phi(q)\ge\phi(1)=0\). For the upper bound, convexity of \(\phi\) on \([0,d]\) places its graph below the chord joining the endpoints:
\[
\phi(t)\le\left(1-\frac td\right)\phi(0)+\frac td\phi(d),\qquad 0\le t\le d.
\]
Integrating and using \(\int q=1\) yields the displayed upper envelope.

If \(\phi\) is strictly convex, equality in Jensen forces \(q=1\) almost everywhere and hence \(\Delta(u)=u\). Equality in the chord bound forces \(q\) to take only the endpoint values \(0\) and \(d\) almost everywhere, and the mean-one constraint makes the \(d\)-region have Lebesgue measure \(1/d\). In the diagonally convex class, \(q\) has a nondecreasing representative, so that region must be the upper interval and the unique extremal diagonal there is
\[
\Delta(u)=\max\{du-d+1,0\},
\]
which is known to be attainable. Thus the bounds are sharp. Substituting \(\phi(t)=t\log t\) gives the Kullback–Leibler upper bound \(\log d\). For independence, direct integration of \(q(u)=du^{d-1}\) gives \(\log d-(d-1)/d\).

## Verification
The proof was checked against the exact diagonal facts in Cattaneo, Masini, and Underwood: the maximum CDF depends on the copula only through \(\Delta\), every diagonal is \(d\)-Lipschitz, and their Definition 3 is precisely convexity of \(\Delta\). Their examples also confirm that \(\Delta(u)=u\), \(\Delta(u)=u^d\), and \(\Delta(u)=\max\{du-d+1,0\}\) are admissible diagonally convex cases.

Two boundary checks are exact. For the upper Fréchet–Hoeffding diagonal, \(q=1\) and the maximum has exactly the marginal law. For the lower Fréchet–Hoeffding diagonal, \(q=0\) below \(1-1/d\) and \(q=d\) above it, so the Kullback–Leibler divergence is exactly \(\log d\). Under independence, the direct integral yields \(\log d-(d-1)/d\), strictly between these endpoints for \(d>1\).

## Relationship to prior work
Cattaneo, Masini, and Underwood introduced diagonal convexity as a dependence restriction for sharp anti-concentration of maxima. Their paper states the maximum-CDF identity through the copula diagonal, gives the diagonal Lipschitz characterization, proves anti-concentration bounds under convexity, and verifies convexity for Gaussian and several Archimedean copulas. The inspected full text does not formulate diagonal convexity as a likelihood-ratio ordering, nor does it state the margin-free \(f\)-divergence identity or sharp information envelope.

Jaworski and Rychlik characterize which distributions can occur as single order statistics under absolutely continuous copulas. Their full text explicitly treats the greatest order statistic through the copula diagonal and gives derivative-size constraints implicit in the Lipschitz characterization. The inspected paper does not discuss likelihood-ratio order and does not derive the equivalence or information envelope above.

Belzunce, Gurler, and Ruiz study likelihood-ratio ordering of vectors of order statistics, including dependent observations. The accessible abstract is close enough to create a genuine comparison risk, but the accessible record describes comparisons among order-statistic vectors and conditional order statistics rather than a characterization of copula diagonal convexity by comparing a maximum with its own common marginal. Full text was not available through the inspected lawful sources, so this remains a residual originality risk rather than evidence of coverage.

Durante and Fernández-Sánchez study classes of copulas with prescribed diagonal sections and explicitly construct copulas with convex diagonals. The accessible article record is structurally relevant but does not state the maximum-to-margin likelihood-ratio equivalence; accessible full text was not available during this check.

## Limitations
The result does not classify the full copula: only its diagonal is identified by the maximum law. It does not claim that diagonal convexity implies stronger multivariate total-positivity properties of the joint law. The likelihood-ratio equivalence is not asserted for discontinuous margins or margins with flat portions without additional measure-theoretic formulation. The information upper bound is stated for generators finite on \([0,d]\), and uniqueness of the extremal diagonal uses strict convexity of the generator. An equivalent likelihood-ratio characterization could exist in older stochastic-order or reliability literature under different terminology; one especially relevant 2011 article could only be inspected at abstract level.

## References
1. M. D. Cattaneo, R. P. Masini, and W. G. Underwood, *Sharp Anti-Concentration Inequalities for Extremum Statistics via Copulas*, arXiv:2502.07699v1, first submitted 2025-02-11. https://arxiv.org/abs/2502.07699
2. P. Jaworski and T. Rychlik, *On distributions of order statistics for absolutely continuous copulas with applications to reliability*, Kybernetika 44 (2008), 757–776. DML-CZ 135889. https://dml.cz/handle/10338.dmlcz/135889
3. F. Belzunce, S. Gurler, and J. M. Ruiz, *Revisiting multivariate likelihood ratio ordering results for order statistics*, Probability in the Engineering and Informational Sciences 25 (2011), 355–368. https://doi.org/10.1017/S0269964811000052
4. F. Durante and J. Fernández-Sánchez, *On the classes of copulas and quasi-copulas with a given diagonal section*, International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 19 (2011), 1–10. https://doi.org/10.1142/S0218488511006848
