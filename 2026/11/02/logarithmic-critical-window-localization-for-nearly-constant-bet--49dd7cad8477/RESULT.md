# Logarithmic critical-window localization for nearly constant Beta samples

## Finding
Fix an integer \(n\ge2\), put \(d=n-1\) and \(c=d/n\), and fix \(\lambda,\mu\in\mathbb R\). For each \(0<\varepsilon<1\), set \(L=\log(1/\varepsilon)\) and take independent \(X_1,\ldots,X_n\) with common \(\operatorname{Beta}(\alpha_\varepsilon,\beta_\varepsilon)\) distribution, where
\[
\alpha_\varepsilon=c+\frac{\lambda}{L},\qquad
\beta_\varepsilon=c+\frac{\mu}{L}.
\]
These shape parameters are positive for all sufficiently small \(\varepsilon\). Write \(T_\varepsilon=n^{-1}\sum_iX_i\), \(Q_\varepsilon=\sum_i(X_i-T_\varepsilon)^2\), \(E_\varepsilon=\{Q_\varepsilon\le\varepsilon\}\), and let
\[
V_d=\frac{\pi^{d/2}}{\Gamma(1+d/2)},\qquad
\Phi_n(z)=\int_0^1 e^{-nzu/2}\,du.
\]
Then the **critical-window probability** satisfies
\[
\boxed{\Pr(E_\varepsilon)\sim
\frac{\sqrt n\,V_d}{2B(c,c)^n}\,
\varepsilon^{d/2}\log(1/\varepsilon)
\bigl[\Phi_n(\lambda)+\Phi_n(\mu)\bigr].}
\]

The corresponding **conditional localization law** specifies where such a nearly constant sample concentrates. Set \(S_\varepsilon=0\) if \(T_\varepsilon\le1/2\) and \(S_\varepsilon=1\) otherwise. Let \(D_\varepsilon=T_\varepsilon\) when \(S_\varepsilon=0\) and \(D_\varepsilon=1-T_\varepsilon\) otherwise, and define
\[
U_\varepsilon=\frac{-2\log D_\varepsilon}{L},\qquad
W_\varepsilon=\frac{(X_1-T_\varepsilon,\ldots,X_n-T_\varepsilon)}{\sqrt\varepsilon}.
\]
Let \(H=\{v\in\mathbb R^n:\sum_i v_i=0\}\), equipped with its induced Euclidean volume, and \(\mathcal B_H=\{v\in H:\|v\|\le1\}\). Conditional on \(E_\varepsilon\), the triple \((S_\varepsilon,U_\varepsilon,W_\varepsilon)\) converges weakly to \((S,U,W)\), with
\[
\Pr(S=0)=\frac{\Phi_n(\lambda)}{\Phi_n(\lambda)+\Phi_n(\mu)},\qquad
\Pr(S=1)=\frac{\Phi_n(\mu)}{\Phi_n(\lambda)+\Phi_n(\mu)},
\]
\[
\Pr(U\in du\mid S=0)=\frac{e^{-n\lambda u/2}}{\Phi_n(\lambda)}\,\mathbf1_{(0,1)}(u)du,\quad
\Pr(U\in du\mid S=1)=\frac{e^{-n\mu u/2}}{\Phi_n(\mu)}\,\mathbf1_{(0,1)}(u)du.
\]
The variable \(W\) is independent of \((S,U)\) and uniformly distributed over \(\mathcal B_H\). In the doubly critical case \(\lambda=\mu=0\), the selected endpoint is fair and the logarithmic location is uniform on \((0,1)\). For unequal drifts, the two endpoints compete by the exact smooth weights \(\Phi_n\).

## Assumptions and scope
The sample size \(n\) and drift parameters \(\lambda,\mu\) are fixed as \(\varepsilon\downarrow0\). The centering statistic \(Q_\varepsilon\) is the **sum of squared deviations**, not the unbiased variance: \(Q_\varepsilon=(n-1)S^2_\varepsilon\). The weak convergence is on \(\{0,1\}\times[0,\infty)\times H\), with the Euclidean topology on \(H\). The conditional laws are well-defined for sufficiently small \(\varepsilon\) because \(\Pr(E_\varepsilon)>0\). The Beta normalization is \(B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)\), and \(\Phi_n(0)=1\).

## Proof
Let \(x=(x_1,\ldots,x_n)\), \(t=n^{-1}\sum_ix_i\), and \(w=x-t\mathbf1\in H\). Orthogonality of the diagonal direction \(\mathbf1/\sqrt n\) to \(H\) gives the Euclidean change-of-variables formula
\[
dx_1\cdots dx_n=\sqrt n\,dt\,d\operatorname{vol}_H(w),\qquad
\sum_i(x_i-t)^2=\|w\|^2.
\]
Set \(w=\sqrt\varepsilon v\), with \(v\in\mathcal B_H\). The joint probability measure on \((t,v)\) inside \(E_\varepsilon\) has density (on the constraints \(0<t+\sqrt\varepsilon v_i<1\))
\[
\sqrt n\,\varepsilon^{d/2}B(\alpha_\varepsilon,\beta_\varepsilon)^{-n}
\prod_{i=1}^n(t+\sqrt\varepsilon v_i)^{\alpha_\varepsilon-1}
(1-t-\sqrt\varepsilon v_i)^{\beta_\varepsilon-1}
\,dt\,d\operatorname{vol}_H(v).
\]
The parameter pair converges to \((c,c)\), so the Beta normalizer converges to \(B(c,c)\). Because \(n(c-1)=-1\), the diagonal density at the lower endpoint is exactly of the form
\[
t^{n(\alpha_\varepsilon-1)}=t^{-1+n\lambda/L}.
\]
Fix \(0<\eta<1/2\) and restrict first to \(\varepsilon^{(1-\eta)/2}\le t\le\varepsilon^{\eta/2}\). Here \(t\to0\) and \(\sqrt\varepsilon/t\to0\) uniformly. Therefore the integrand, divided by its diagonal approximation, converges uniformly to one as \(\varepsilon\downarrow0\), for every \(v\in\mathcal B_H\). The substitution \(t=\varepsilon^{u/2}\) gives
\[
t^{-1+n\lambda/L}|dt|=\frac{L}{2}e^{-n\lambda u/2}\,du.
\]
For a bounded continuous test function \(g\) of \((u,v)\), the contribution from this range, divided by \(\varepsilon^{d/2}L\), tends to
\[
\frac{\sqrt n}{2B(c,c)^n}
\int_\eta^{1-\eta}\int_{\mathcal B_H}
 g(u,v)e^{-n\lambda u/2}\,d\operatorname{vol}_H(v)\,du.
\]
Exactly the same argument near the upper endpoint, with \(1-t=\varepsilon^{u/2}\) and \(\mu\) instead of \(\lambda\), gives the second contribution.

For completeness, the discarded boundary layers are negligible in the correct order as \(\eta\downarrow0\). Fix a small constant \(a\in(0,1/4)\). For \(2\sqrt\varepsilon\le t\le a\), all admissible coordinates \(t+\sqrt\varepsilon v_i\) are comparable to \(t\) and all \(1-t-\sqrt\varepsilon v_i\) are uniformly bounded away from zero. Hence the integrand is bounded by a constant multiple of \(\varepsilon^{d/2}t^{-1+n\lambda/L}\); the same bound holds symmetrically near \(t=1\). In logarithmic coordinates, any strip of \(u\)-width \(\eta\) therefore contributes at most \(C\eta\varepsilon^{d/2}L\), apart from the fixed-distance strip which is only \(O(\varepsilon^{d/2})\). The corner \(t\le2\sqrt\varepsilon\) implies every \(x_i\le3\sqrt\varepsilon\); direct integration of the Beta density over this cube gives the upper bound
\[
O\bigl(\varepsilon^{n\alpha_\varepsilon/2}\bigr)
=O\bigl(\varepsilon^{d/2}\bigr),
\]
since \(n\alpha_\varepsilon/2=d/2+n\lambda/(2L)\). The upper corner is analogous with \(\beta_\varepsilon\). The region of \(t\) separated from both endpoints contributes \(O(\varepsilon^{d/2})\). The constants can be chosen uniformly for sufficiently small \(\varepsilon\), as both shapes remain in a compact subset of \((0,\infty)\).

Thus the rescaled probability measure converges, against bounded continuous tests, to the sum of the two endpoint integrals over the **full** interval \(0<u<1\). Evaluating the \(v\)-integral gives \(V_d\), proving the probability asymptotic. Dividing the endpoint-specific limits by their sum gives the claimed conditional distribution of \((S,U,W)\), including independence and uniformity of \(W\). Contributions with \(U\notin[0,1]\) vanish after this normalization. This also proves the required weak convergence and completes the argument.

## Verification
The included standalone program `verify.py` verifies the geometric Jacobian and Beta normalization, the exponential-tilt integral and endpoint probabilities, and a direct one-dimensional calculation in the two-observation arcsine case. At \(n=2\), \(\lambda=\mu=0\), the Beta density is \(1/[\pi\sqrt{x(1-x)}]\), so the event probability is independently calculable from its exact arcsine CDF by one numerical integral. Its asymptotic matches the displayed constant, with ratios approaching one as the threshold shrinks. These are finite numerical checks, not proofs of asymptotic convergence. The proof above supplies the uniform error bounds in the critical window.

For an algebraic normalization check against the established three-observation theorem, put \(n=3\) and \(\lambda=\mu=0\), so \(Q=2S^2\). The formula yields \(\Pr(S^2\le y)\sim 2\sqrt3\pi B(2/3,2/3)^{-3}y\log(1/y)\), exactly matching the tied-critical-endpoint coefficient of the fixed-shape result cited below. The new theorem additionally permits **shape drift of order inverse logarithm**, and specifies the **conditional joint location/transverse limit**, neither of which follows from that fixed-parameter leading term without uniform-in-shape analysis.

## Relationship to prior work
Benhamou (2018) gives general moment and dependence properties of sample variance and the sample mean, highlighting their nontrivial joint behavior outside the normal parent. Papadatos (2022) studies inference in the two-parameter Beta family. Neither paper provides the vanishing-variance rare-event conditional law above.

Royen (2008), particularly Theorem 3, proves a one-sided pure-power fixed-parameter lower-tail phase transition for sample variance, including a logarithm at its critical exponent. Thus neither the existence of the critical exponent nor the fixed-parameter logarithmic mechanism is attributed here to the present result. The previously published “Exact lower-tail phase diagram for the three-sample Beta variance” extends fixed-parameter, three-observation asymptotics to two Beta endpoints and supplies their coefficients. Those fixed-shape results are stronger on their own parameter domain but do not imply a parameter-uniform crossover or conditional weak law merely by substituting a moving exponent into pointwise limits.

The result here is restricted to the **simultaneous two-parameter logarithmic critical window**, its explicit endpoint competition, and the entire conditional joint limit including transverse residuals. It claims no priority for sample-variance normalization, Beta densities, the orthogonal diagonal transformation, or the fixed-parameter phase transition.

## Limitations
The asymptotic is first-order, with no error rate, and requires fixed \(n\), fixed \(\lambda,\mu\) and independent identically distributed Beta observations. It does not cover general bounded densities without endpoint regularity, shape drifts faster than the inverse-logarithm scale, the joint limit \(n\to\infty\), or arbitrary dependence among observations. The unit-ball law applies to the critical window and the normalization \(Q\le\varepsilon\); it is not asserted for a generic small-variance event away from criticality. The historical priority check remains provisional, especially for potentially equivalent uniform asymptotics hidden within exact transforms.

## References
1. E. Benhamou, “A few properties of sample variance,” arXiv:1809.03774v1, first publicly posted 2018-09-11, https://arxiv.org/abs/1809.03774.
2. N. D. Papadatos, “On point estimators for Gamma and Beta distributions,” arXiv:2205.10799v1, first publicly posted 2022-05-22, https://arxiv.org/abs/2205.10799.
3. T. Royen, “The exact distribution of the sample variance from bounded continuous random variables,” arXiv:0810.1572, first publicly posted 2008-10-09, https://arxiv.org/abs/0810.1572, especially Theorem 3.
4. “Exact lower-tail phase diagram for the three-sample Beta variance,” published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-lower-tail-phase-diagram-for-the-three-sample-beta-varianc--f275509045a1.
