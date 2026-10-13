# Sharp inverted-concavity threshold and compound-Poisson majorization boundary for log-Pareto laws

## Finding

**Theorem (sharp boundary and its failure witness).** Consider the log-Pareto family of probability distributions supported on \([0,\infty)\), with parameter \(\alpha>0\) and distribution function
\[
F_\alpha(x)=1-\bigl(1+\log(1+x)\bigr)^{-\alpha},\qquad x\ge 0.
\]
Define \(y_*>1\) as the unique solution of
\[
y_*-2-y_*^{-1}=2\log y_*,
\]
and put \(\alpha_*=(y_*+y_*^{-1})/2=2.906557937512901\ldots\). Then the reciprocal survival function \(u\mapsto 1-F_\alpha(1/u)\) is concave on \((0,\infty)\) **if and only if** \(0<\alpha\le\alpha_*\). Equivalently, \(x\mapsto x^2f_\alpha(x)\) is nondecreasing on \((0,\infty)\) exactly for this parameter range, where \(f_\alpha\) denotes the density.

Consequently, by the compound-Poisson characterization of Chen, Hu, Shneer and Zou [1, Theorem 3], for every \(\lambda>0\), every \(n\ge2\), and independent \(X_i\sim\mathrm{CP}(\lambda,F_\alpha)\), every pair of nonnegative vectors \(w,v\in[0,\infty)^n\) satisfying \(w\prec v\) obeys
\[
\sum_{i=1}^n w_iX_i\ge_{\mathrm{st}}\sum_{i=1}^n v_iX_i
\]
**if and only if** \(0<\alpha\le\alpha_*\) when the universal quantifiers over intensity, dimension and weights are included. The two weight vectors necessarily have the same total weight, but need not be normalized; positive scaling preserves the comparison.

For \(\alpha>\alpha_*\), the derivative of \(x^2f_\alpha(x)\) changes sign exactly twice, from positive to negative and back to positive. If \(x_-<x_+\) denote the two transition points, then as \(\delta=\alpha-\alpha_*\downarrow0\),
\[
x_\pm= (y_*-1)\pm y_*\sqrt{2\delta}+O(\delta).
\]
For every \(\alpha>\alpha_*\) there are two strictly positive unequal weight vectors and a strictly positive intensity such that the displayed stochastic dominance fails. An explicit such witness is given below for \(\alpha=4\).

## Assumptions and scope

The log-Pareto severity has continuous density
\[
f_\alpha(x)=\frac{\alpha}{(1+x)(1+\log(1+x))^{\alpha+1}},\qquad x>0.
\]
It has essential infimum zero and infinite mean for every \(\alpha>0\). Here \(\mathrm{CP}(\lambda,F)\) denotes the distribution of a sum of an independent Poisson number of independent nonnegative severities, with Poisson mean \(\lambda\). The usual stochastic order is \(A\ge_{\mathrm{st}}B\) if \(\mathbb P(A>t)\ge\mathbb P(B>t)\) for every real \(t\); equivalently, \(\mathbb P(A\le t)\le\mathbb P(B\le t)\). The majorization relation \(w\prec v\) means \(w\) is more balanced than \(v\), their coordinate sums agree, and decreasing-order partial sums of \(w\) do not exceed those of \(v\).

The theorem concerns the sharp *inverted-concavity* boundary and the corresponding **universal-in-intensity compound-Poisson** weight-majorization principle. It does not assert that the majorization order for the un-compounded log-Pareto distribution fails whenever \(\alpha>\alpha_*\); nor does it assert failure for every fixed positive Poisson intensity in that range.

## Proof

**1. Exact one-variable sign reduction.** Define \(h_\alpha(x)=x^2f_\alpha(x)\). Direct differentiation gives
\[
h_\alpha'(x)=\frac{\alpha x}{(x+1)^2(1+\log(1+x))^{\alpha+2}}\bigl[(x+2)\log(1+x)+2-\alpha x\bigr].
\]
For \(x>0\), set
\[
B(x)=\frac{(x+2)\log(1+x)+2}{x}.
\]
Every factor outside the final bracket is strictly positive. Hence \(\operatorname{sgn}h_\alpha'(x)=\operatorname{sgn}(B(x)-\alpha)\), and the problem reduces to finding the global minimum of \(B\).

**2. Unique global minimum and exact threshold.** Differentiation gives
\[
B'(x)=\frac{q(x)}{x^2},\quad
q(x)=x-1-\frac1{1+x}-2\log(1+x),\quad
q'(x)=\frac{x^2}{(1+x)^2}>0.
\]
Also \(q(0+)=-2\), \(q(x)\to\infty\) as \(x\to\infty\), and \(B(x)\to\infty\) at both endpoints \(x\downarrow0\) and \(x\to\infty\). Therefore \(q\) has precisely one zero \(x_*>0\), \(B\) decreases strictly on \((0,x_*)\) and increases strictly on \((x_*,\infty)\), and \(B(x_*)\) is its unique global minimum. With \(y_*=1+x_*\), the equation \(q(x_*)=0\) is equivalent to \(y_*-2-y_*^{-1}=2\log y_*\). Substitution in \(B(x_*)\) yields the exact identity
\[
\alpha_*=B(x_*)=\frac{y_*+y_*^{-1}}2.
\]
Thus \(h_\alpha'\ge0\) everywhere precisely for \(\alpha\le\alpha_*\). At equality, the derivative is zero at only one isolated point, so \(h_\alpha\) is still strictly increasing. By the exact inverted-concavity criterion [1, Proposition 2], \(F_\alpha\) belongs to that class exactly in this range. The distribution is continuous with essential infimum zero, so the *universal-in-\(\lambda\)* stochastic-majorization equivalence follows by [1, Theorem 3]. Those two general results are prior work; the sharp log-Pareto optimization is the present contribution.

**3. Curvature geometry at the boundary.** If \(\alpha>\alpha_*\), the level set \(B(x)=\alpha\) has exactly two distinct positive roots \(x_-<x_*<x_+\), by the strictly decreasing/increasing branches and endpoint divergence of \(B\). The sign of \(h_\alpha'\) is positive before \(x_-\), negative between the roots, and positive after \(x_+\). At \(x_*\),
\[
B''(x_*)=q'(x_*)/x_*^2=1/y_*^2>0.
\]
Taylor expansion at the nondegenerate minimum gives \(B(x)=\alpha_*+(x-x_*)^2/(2y_*^2)+O((x-x_*)^3)\), and inversion on the two monotonic branches gives the stated square-root root splitting. This is an ordinary asymptotic statement as \(\delta\downarrow0\), not an exact finite-\(\delta\) equality.

**4. Direct low-intensity reversal, without using necessity as a black box.** For any \(\alpha>\alpha_*\), choose \(x_0\in(x_-,x_+)\), set \(z=x_0/2>0\), and write \(G(u)=F_\alpha(z/u)\) for \(u>0\). The chain rule yields the exact identity \(G''(u)=h_\alpha'(z/u)/u^2\). Therefore \(G''(1/2)=4h_\alpha'(x_0)<0\). For some sufficiently small \(0<\varepsilon<1/2\), strict concavity near \(1/2\) gives
\[
\Delta=F_\alpha(2z)-\frac12\left[F_\alpha\left(\frac z{1/2+\varepsilon}\right)+F_\alpha\left(\frac z{1/2-\varepsilon}\right)\right]>0.
\]
Take two independent compound-Poisson variables \(X_1,X_2\) of common intensity \(\lambda\) and severity \(F_\alpha\), and form \(S_{\mathrm{bal}}=(X_1+X_2)/2\), \(S_{\mathrm{unbal}}=(1/2+\varepsilon)X_1+(1/2-\varepsilon)X_2\). The balanced vector is majorized by the unbalanced vector. Under the standard superposition representation, the number \(N\) of total severity jumps is Poisson with mean \(2\lambda\). The two sums agree in distribution at \(N=0\). Conditional on \(N=1\), the difference between their CDFs at \(z\) equals \(\Delta\), since the sole jump originates from either component with probability one half. At \(N\ge2\), the difference of conditional CDFs is bounded below by \(-1\). Thus
\[
\mathbb P(S_{\mathrm{bal}}\le z)-\mathbb P(S_{\mathrm{unbal}}\le z)
\ge e^{-2\lambda}\left[2\lambda\Delta-(e^{2\lambda}-1-2\lambda)\right].
\]
Since \(0<\Delta<1\), whenever \(0<\lambda<\Delta/(2e)\), we have \(2\lambda<1\), and Taylor's remainder gives \(e^{2\lambda}-1-2\lambda\le 2e\lambda^2<2\lambda\Delta\). The displayed CDF difference is then positive, which contradicts the proposed usual stochastic order. The failure is therefore constructive and occurs already with two strictly positive weights at all sufficiently low intensities.

**5. Fixed numerical witness.** At \(\alpha=4\), \(z=1\) and \(\varepsilon=1/4\), the exact single-jump CDF difference is
\[
\Delta_4=\frac12\left[(1+\log(7/3))^{-4}+(1+\log5)^{-4}\right]-(1+\log3)^{-4}
=0.002165083438733\ldots>0.
\]
Consequently \(S_{\mathrm{bal}}=(X_1+X_2)/2\) has a **strictly larger** CDF at \(z=1\) than \(S_{\mathrm{unbal}}=3X_1/4+X_2/4\) for every \(0<\lambda<\Delta_4/(2e)=0.000398244842765\ldots\). This reverses the stochastic-majorization conclusion for those parameters.

## Verification

The standalone Python 3 checker `check_logpareto.py` reconstructs the elementary scalar expressions, brackets the unique zero of \(q\), verifies the numerical threshold via its independent exact formula, checks analytical derivative signs at selected points, evaluates the explicit positive \(\Delta_4\), and locates the two curvature transitions for three small positive parameter perturbations. Invoke `python3 check_logpareto.py`; the script uses only the standard library and prints a final `PASS` if its assertions hold. All existence, uniqueness, shape, and stochastic-order conclusions for continuous parameter ranges are established analytically in the proof rather than by finite tests.

## Relationship to prior work

Chen, Hu, Shneer and Zou [1, Appendix A, Example 6] give the exact derivative of \(x^2f_\alpha(x)\) and prove the **sufficient** log-Pareto membership range \(0<\alpha\le2\), using a sufficient monotonicity check on an auxiliary function. They do not optimize that derivative for its sharp global threshold, classify the post-threshold turning points, or provide the explicit intensity-dependent two-weight counterexample here. Their Proposition 2 and Theorem 3 are the indispensable established general equivalences, so no general new stochastic-order equivalence is claimed. The sharp parameter range \(2<\alpha\le2.9065579375\ldots\) newly satisfies their same condition, and the geometric failure mechanism is complete above it.

Chen and Shneer [2] discuss log-Pareto in the distinct setting of a single-aggregate comparison; it does not supply the exact universal majorization classification above. Inverted-subadditive distributions studied by Arab, Lando and Oliveira [3] also concern the weaker single-aggregate stochastic comparison, not the universal compound-Poisson majorization equivalence. A substantive possibility remains that an unindexed source has independently minimized the same auxiliary function, and this result is not an independent validation of the cited general theorems.

## Limitations

The sharp boundary is for the precise log-Pareto parameterization stated here, and the compound-Poisson quantification is over **all** positive intensities. Above the threshold the constructive failure holds at sufficiently small positive intensities; it is not asserted at every intensity. The counterexample does not establish failure of the un-compounded weighted-sum ordering. The numerical root and curvature coefficients are analytic consequences, while their decimal approximations are not exact certificates. No claim is made about dependence between severities or about statistical parameter fitting.

## References

[1] Y. Chen, T. Hu, V. Shneer, Z. Zou, *Stochastic dominance for linear combinations of infinite-mean risks*, arXiv:2505.01739 (first posted 3 May 2025), Journal of Applied Probability (online 30 September 2026), DOI: 10.1017/jpr.2026.10138. Open-access full article: https://www.cambridge.org/core/journals/journal-of-applied-probability/article/stochastic-dominance-for-linear-combinations-of-infinitemean-risks/93318CB01EFDDE5A18671FEB6DC303A8 .

[2] Y. Chen, S. Shneer, *Risk aggregation and stochastic dominance for a class of heavy-tailed distributions*, arXiv:2408.15033; ASTIN Bulletin (2025), DOI: 10.1017/asb.2025.10053.

[3] I. Arab, T. Lando, P. Oliveira, *Convex combinations of random variables stochastically dominate the parent for a new class of heavy-tailed distributions*, arXiv:2411.14926; DOI: 10.1214/25-ECP714.
