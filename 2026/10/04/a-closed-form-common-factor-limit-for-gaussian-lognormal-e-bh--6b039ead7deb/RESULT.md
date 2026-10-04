# A closed-form common-factor limit for Gaussian lognormal e-BH
## Finding
Under the complete null, fix \(0<\alpha<1\), \(\delta>0\), and \(0<\rho<1\). Let
\[
X_i=\sqrt{\rho}\,W+\sqrt{1-\rho}\,Z_i,
\]
where \(W,Z_1,Z_2,\ldots\) are independent standard normal variables, and define the likelihood-ratio e-values
\[
E_i=\exp(\delta X_i-\delta^2/2).
\]
Each \(E_i\) has null expectation one. Apply the base e-BH procedure at level \(\alpha\) to \(E_1,\ldots,E_K\).

Write \(\bar\Phi(x)=1-\Phi(x)\), \(\phi\) for the standard normal density, and
\[
h(x)={\phi(x)\over\bar\Phi(x)},\qquad s=\delta\sqrt{1-\rho}.
\]
There is a unique \(x_*\in\mathbb R\) with \(h(x_*)=s\). Define
\[
t_*=\bar\Phi(x_*),\qquad
w_*={\log(1/(\alpha t_*))+\delta^2/2-sx_*\over\delta\sqrt{\rho}}.
\]
Then
\[
\lim_{K\to\infty}\operatorname{FDR}_K=\bar\Phi(w_*).
\]
At the onset of rejection, the limiting rejection fraction is \(t_*\). In particular, \(t_*\) depends on \(\delta\) and \(\rho\) but not on \(\alpha\); changing \(\alpha\) shifts the common-factor boundary \(w_*\) without changing the tangency fraction.

For \(\alpha=0.05\), \(\delta=3\), and \(\rho=1/2\),
\[
t_*=0.0433882935111,\qquad w_*=3.29993272728449,
\]
and
\[
\lim_{K\to\infty}\operatorname{FDR}_K=0.000483540037138.
\]
Thus a rare common-factor excursion can trigger a macroscopic block of false rejections even though the limiting global-null FDR is far below the nominal level.

## Assumptions and scope
The claim concerns the complete null and the one-factor equicorrelated Gaussian model with fixed \(\rho\in(0,1)\), fixed \(\delta>0\), and fixed \(\alpha\in(0,1)\) as \(K\to\infty\). It concerns the unboosted base e-BH procedure. It does not claim the same formula for negative correlations, non-Gaussian factors, two-sided Gaussian p-values, mixtures of likelihood-ratio e-values, or finite \(K\).

The e-value construction is the Gaussian likelihood-ratio example used by Wang and Ramdas. The asymptotic question is motivated by their explicit discussion of Gaussian dependence as a direction for further study. The comparison paper by Dey treats the standard BH procedure for one-sided Gaussian p-values, not likelihood-ratio e-values.

## Proof
Let \(E_{[1]}\ge\cdots\ge E_{[K]}\) denote the decreasing order statistics. Under the complete null, base e-BH rejects at least one hypothesis exactly when, for some \(k\in\{1,\ldots,K\}\),
\[
E_{[k]}\ge {K\over \alpha k}.
\]
Put \(t=k/K\). Conditional on \(W=w\), the \(E_i\) are iid lognormal and
\[
q_w(t):=\Pr\!\left(E_i\ge {1\over\alpha t}\mid W=w\right)
=\bar\Phi\!\left({\log(1/(\alpha t))-\delta\sqrt\rho\,w+\delta^2/2\over s}\right).
\]
Hence the large-\(K\) step-up boundary is determined by whether there exists \(t\in(0,1]\) with \(q_w(t)\ge t\).

For fixed \(w\), \(q_w(t)/t\to0\) as \(t\downarrow0\), because a lognormal upper tail is smaller than every positive power of its threshold. On any interval \([\varepsilon,1]\), conditional Glivenko--Cantelli convergence makes the empirical tail uniformly converge to \(q_w\). For \(t<\varepsilon\), choose \(\varepsilon\) so that \(q_w(t)/t\) is uniformly small; binomial Chernoff bounds, first for finitely many small \(k\) and then geometrically for the remaining \(k\), rule out a residual extreme-order-statistic rejection when \(\sup_t q_w(t)/t<1\). Conversely, if \(q_w(t_0)>t_0\) for some fixed \(t_0\), the conditional law of large numbers gives rejection with probability tending to one. Therefore, except at a boundary value of \(w\),
\[
\Pr(R_K>0\mid W=w)\longrightarrow
\mathbf 1\left\{\sup_{0<t\le1}{q_w(t)\over t}>1\right\}.
\]

Writing \(x=\Phi^{-1}(1-t)\), so that \(t=\bar\Phi(x)\), the equality \(q_w(t)=t\) is equivalent to
\[
w=g(x):={\log(1/(\alpha\bar\Phi(x)))+\delta^2/2-sx\over\delta\sqrt\rho}.
\]
Thus the first common-factor value at which the limiting step-up curve touches the diagonal is \(w_*=\inf_x g(x)\). Its derivative has the sign of
\[
h(x)-s,
\]
where \(h(x)=\phi(x)/\bar\Phi(x)\). The Gaussian hazard is strictly increasing: differentiating gives \(h'(x)=h(x)(h(x)-x)>0\), using the standard Mills inequality \(h(x)>x\) for \(x>0\), while the inequality is immediate for \(x\le0\). Also \(h(x)\) increases from zero to infinity. Hence there is a unique \(x_*\) satisfying \(h(x_*)=s\), and it is the unique minimizer of \(g\). This proves the displayed formulas for \(t_*\) and \(w_*\). The fact that \(t_*\) is independent of \(\alpha\) follows because \(\alpha\) enters \(g\) only through the additive constant \(\log(1/\alpha)\).

Under the complete null, every rejection is false, so \(\operatorname{FDR}_K=\Pr(R_K>0)\). Since \(W\) has a continuous standard normal law, \(\Pr(W=w_*)=0\). Dominated convergence over \(W\) therefore yields
\[
\lim_{K\to\infty}\operatorname{FDR}_K
=\Pr(W>w_*)=\bar\Phi(w_*).
\]

## Verification
The standalone script `verifier.py` evaluates the Gaussian hazard equation by bisection, checks that the derivative changes sign at the unique root, independently grids the scalar boundary functional to confirm its minimum, verifies the tangency equation \(q_{w_*}(t_*)=t_*\), and checks that the conditional tail-to-step ratio is below one just below \(w_*\) and above one just above it. For \(\alpha=0.05\), \(\delta=3\), and \(\rho=1/2\), it returns `VERIFY_OK` and reproduces all displayed numerical constants.

The asymptotic proof itself is analytic; the script checks the nontrivial scalar calculus and numerical benchmark rather than substituting simulation for proof.

## Relationship to prior work
Wang and Ramdas introduce base e-BH, prove FDR control under arbitrary dependence, and explicitly use Gaussian likelihood-ratio e-values \(\exp(\delta X-\delta^2/2)\). Their paper computes marginal boosting formulas for these lognormal e-values and closes by identifying multivariate Gaussian dependence as a direction for further study. It does not give the equicorrelated large-\(K\) global-null formula above.

Dey derives a positive large-\(K\) global-null FDR limit for the ordinary BH procedure applied to one-sided Gaussian p-values under equicorrelation. That result uses the same common-factor representation, but its boundary is based on \(\Phi^{-1}(1-\alpha t)\). Here the e-BH likelihood-ratio boundary is logarithmic in \(t\), namely \(\log(1/(\alpha t))/\delta+\delta/2\), and its first-contact fraction has the closed Mills-hazard characterization \(h(x_*)=\delta\sqrt{1-\rho}\). No matching likelihood-ratio e-BH formula was found in the inspected sources or targeted database searches.

## Limitations
The result is asymptotic in the number of hypotheses and does not provide a finite-\(K\) error bound. The proof uses positive fixed equicorrelation and the exact Gaussian likelihood-ratio e-values. A general theorem for arbitrary factor-model step-up boundaries, if present in literature not located by the targeted searches, could subsume this calculation; this is the main residual originality risk. No independent audit has been performed.

## References
1. R. Wang and A. Ramdas, “False discovery rate control with e-values,” arXiv:2009.02824, first posted 2020-09-06; Journal of the Royal Statistical Society Series B 84 (2022), 822–852.
2. M. Dey, “On Asymptotic Behaviors of Stepwise Multiple Testing Procedures,” arXiv:2212.08372, first posted 2022-12-16; revised journal version, Statistical Papers 65 (2024), 5691–5717.
