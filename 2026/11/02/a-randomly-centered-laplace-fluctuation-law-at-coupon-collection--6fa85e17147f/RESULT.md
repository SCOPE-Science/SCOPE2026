# A randomly centered Laplace fluctuation law at coupon collection

## Finding

For every integer \(n\ge2\), draw independent coupon labels uniformly from \(\{1,\ldots,n\}\). Let \(T_n\) be the number of draws until every label has appeared and let \(S_n\) be the number of labels appearing exactly once among those \(T_n\) draws. Define
\[
G_n=\frac{T_n}{n}-\log n,\qquad
W_n=\frac{S_n-n(\log n)e^{-T_n/n}}{\sqrt{\log n}}.
\]
Then
\[
(G_n,W_n)\ \xrightarrow{d}\ (G,\sqrt{E}\,Z),
\]
where \(E\sim\operatorname{Exp}(1)\), \(G=-\log E\) has the standard Gumbel law, and \(Z\sim N(0,1)\) is independent of \(E\). In particular, the fluctuation \(W_n\) converges to a **centered Laplace law of scale \(1/\sqrt2\)**, not a Gaussian law, with characteristic function
\[
\lim_{n\to\infty}\mathbb E e^{itW_n}=(1+t^2/2)^{-1}.
\]
More precisely, for every real \(u,t\),
\[
\lim_{n\to\infty}\mathbb E e^{iuG_n+itW_n}
=\frac{\Gamma(1-iu)}{(1+t^2/2)^{1-iu}}.
\]
These results describe the second-order fluctuation after observing the random completion time. The previously known first-order behavior \(S_n/\log n\Rightarrow E\) is not claimed as new.

## Assumptions and scope

There is exactly one draw per discrete step; coupon labels are independent and equiprobable; \(T_n\) includes the final draw obtaining the last missing label. All convergence statements concern \(n\to\infty\), with no conditioning on an atypical completion time. Both the random centering and \(\sqrt{\log n}\) scaling are essential to the stated limit. \(\Gamma\) denotes Euler's gamma function.

## Proof

**1. Poisson embedding.** For each label \(i\in\{1,\ldots,n\}\), let \(N_i(s)\) be independent rate-one Poisson processes. In the chronological superposition of these processes, the labels of successive arrivals are independent and uniform. Let \(X_i\) be the first arrival of process \(i\), and let \(M_n=\max_iX_i\). The labels observed up to \(M_n\) stop precisely upon their first complete collection. Consequently the number of superposed arrivals at \(M_n\) has law \(T_n\), and the number of processes with exactly one arrival at that time has law \(S_n\), jointly. The \(X_i\) are independent \(\operatorname{Exp}(1)\) variables, and for fixed real \(x\),
\[
\Pr\{M_n-\log n\le x\}=(1-e^{-x}/n)^n\longrightarrow e^{-e^{-x}}.
\]
Write \(H_n=M_n-\log n\); thus \(H_n\Rightarrow G\), with \(e^{-G}=E\sim\operatorname{Exp}(1)\).

**2. An exact conditional law.** Condition on \(M_n=y>0\) by regular conditional distributions. Almost surely there is one unique process whose first arrival is at \(y\); its count at that instant is one. By independence of first arrivals, all remaining counts at \(y\) are independent \(\operatorname{Poisson}(y)\) variables conditioned to be nonzero. Therefore
\[
S_n\mid\{M_n=y\}\overset d=
1+\operatorname{Bin}\!\left(n-1,p_y\right),\qquad
p_y=\frac{ye^{-y}}{1-e^{-y}}.
\]
For \(y=\log n+x\) and \(x\) in any fixed compact set,
\[
(n-1)p_y=(\log n)e^{-x}+O(1),\qquad
\frac{(n-1)p_y(1-p_y)}{\log n}=e^{-x}+o(1),
\]
where both errors are uniform on that compact set. Since \(p_y=O((\log n)/n)\), the binomial triangular-array central limit theorem yields, uniformly in compact \(x\),
\[
\mathcal L\left(
\frac{S_n-(\log n)e^{-x}}{\sqrt{\log n}}
\,\middle|\,M_n=\log n+x\right)
\Rightarrow N(0,e^{-x}).
\]
One can verify the uniform assertion directly from the conditional characteristic function \(e^{it(1-(\log n)e^{-x})/\sqrt{\log n}}(1+p_y(e^{it/\sqrt{\log n}}-1))^{n-1}\): its logarithm converges locally uniformly to \(-t^2e^{-x}/2\). Since \(H_n\) is tight, integration against the laws of \(H_n\) proves
\[
\left(H_n,\frac{S_n-(\log n)e^{-H_n}}{\sqrt{\log n}}\right)
\Rightarrow(G,\sqrt{e^{-G}}\,Z),
\]
with \(Z\) independent of \(G\).

**3. De-Poissonization of the random center.** Conditional on \(M_n=y\), let \(V_y\) be a rate-one Poisson count conditioned on being positive. Its mean and variance are
\[
\mu_y=\frac{y}{1-e^{-y}},\qquad
v_y=\frac{y}{1-e^{-y}}-\frac{y^2e^{-y}}{(1-e^{-y})^2}.
\]
Thus, in the same coupling,
\[
\mathbb E(T_n\mid M_n=y)=1+(n-1)\mu_y,\qquad
\operatorname{Var}(T_n\mid M_n=y)=(n-1)v_y.
\]
For \(y=\log n+x\) with bounded \(x\), the conditional mean of \(T_n/n-y\) is \(O((\log n)/n)\), and its conditional variance is \(O((\log n)/n)\), uniformly. Conditional Chebyshev inequality and tightness of \(H_n\) give
\[
\frac{T_n}{n}-M_n=O_{\Pr}(\sqrt{\log n/n}).
\]
The mean-value theorem on the event \(|H_n|\le K\) and \(|T_n/n-M_n|\le1\), followed by \(K\to\infty\), gives
\[
\frac{n(\log n)e^{-T_n/n}-(\log n)e^{-H_n}}{\sqrt{\log n}}
=O_{\Pr}(\log n/\sqrt n)=o_{\Pr}(1).
\]
Also \(G_n-H_n=o_{\Pr}(1)\). Slutsky's theorem transfers the preceding joint limit to \((G_n,W_n)\).

**4. Identify the law.** Given \(E\), the second limiting coordinate has characteristic function \(e^{-t^2E/2}\). Integrating against the unit exponential density yields \((1+t^2/2)^{-1}\), the characteristic function of a centered Laplace variable of scale \(1/\sqrt2\). Similarly,
\[
\mathbb E\big[e^{iuG+it\sqrt{E}Z}\big]
=\int_0^\infty z^{-iu}e^{-(1+t^2/2)z}\,dz
=\frac{\Gamma(1-iu)}{(1+t^2/2)^{1-iu}}.
\]
This completes the proof.

## Verification

Run `python3 checks/verify.py` with Python, SciPy and the standard library. It checks 724 exact-rational or numerical assertions, including exhaustive occupancy-state dynamic programming for \(2\le n\le7\) over the first twenty draw counts, agreement with the published associated-Stirling finite formula, comparison against the conditional Poisson-mixture representation, and truncated-Poisson moment identities. It also checks the numerical trend toward the displayed Laplace characteristic function at two test arguments, with a deliberately nonasymptotic tolerance. The analytic steps above, not finite arithmetic or numerical approximation, prove the infinite theorem.

## Relationship to prior work

Myers and Wilf (2003), §4, Eq. (46), derive the **full exact finite joint probability** for stopping time and number of singleton coupons; their Eq. (49) gives the marginal singleton distribution and they prove its expectation equals the harmonic number. This antecedent is stronger as finite enumeration and is not claimed as an additional result. Their inspected §4 does not state or analyze the random-time-centered second-order mixed-Gaussian/Laplace fluctuation or its joint Gumbel transform. The claimed contribution is this nontrivial asymptotic extraction, not a re-enumeration.

Doumas and Papanicolaou (2014), in the collector-siblings formulation, examine the residual singleton population. Mahmoud and Smythe (2012) prove joint laws for coupon counts over specified collection stages, rather than the present random completion stage and random centering. Later work by Ilienko (2026) and Long (2026) establishes the previously known exponential **first-order** singleton scale and related siblings laws; the latter comparison is limited to accessible abstract information. Related finite enumerators may in principle imply asymptotic specializations, and historical priority is not independently settled.

## Limitations

The theorem is asymptotic for equiprobable independent coupon draws; it does not claim rates of convergence, a finite-sample Laplace identity, arbitrary heterogeneous probabilities, or analogous limits for counts appearing exactly twice. The conditional normal limit must not be confused with an unconditional Gaussian limit. The exact finite joint distribution predates this analysis, and neither a formal proof assistant nor independent audit has validated historical priority.

## References

1. A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem* (2003), arXiv:math/0304229v1, §4, Eq. (46) and Eq. (49). https://arxiv.org/abs/math/0304229
2. A. Doumas and V. Papanicolaou, *The Siblings of the Coupon Collector* (2014), arXiv:1412.4346. https://arxiv.org/abs/1412.4346
3. H. M. Mahmoud and R. T. Smythe, *On the Joint Behavior of Types of Coupons in Generalized Coupon Collection*, Advances in Applied Probability 44 (2012), 429–451, doi:10.1239/aap/1339878719. https://doi.org/10.1239/aap/1339878719
4. A. Ilienko, *Limit theorems in the extended coupon collector's problem*, 2026. https://www.vmsta.org/journal/VMSTA/article/358/text
5. C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector* (2026), arXiv:2606.29635. https://arxiv.org/abs/2606.29635
