# Harmonic equilibrium bias and a one-gradient covariance obstruction for randomized ULMC

## Result

Consider the one-dimensional underdamped Langevin dynamics
\[
 dX_t=V_t\,dt,\qquad
 dV_t=-\gamma V_t\,dt-\alpha\kappa X_t\,dt+\sqrt{2\gamma\alpha}\,dW_t,
\]
with \(\gamma,\alpha,\kappa>0\). Its Gibbs equilibrium has centered covariance
\[
\Sigma_\star=\begin{pmatrix}\kappa^{-1}&0\\0&\alpha\end{pmatrix}.
\]

The randomized exponential schemes RMM, ALUM and the new LC-REI of Lyu--Wang--Yang can be placed in the following predictor family. Let \(\tau\in[0,1]\), let
\[
\psi(u)=e^{-\gamma u},\qquad \phi(u)=\frac{1-e^{-\gamma u}}{\gamma u},
\]
and write the intermediate position as
\[
X_{k+\tau}=X_k+\tau h\phi(\tau h)V_k
-\delta\,\alpha\gamma^{-1}\tau h\bigl(1-\phi(\tau h)\bigr)\kappa X_k
+\beta\sqrt{2\gamma\alpha}\,\Delta W^{\phi,1}_{k+\tau}.
\]
The source methods correspond to
\[
(\delta,\beta)=(1,1)\quad\text{(RMM)},\qquad
(0,1)\quad\text{(ALUM)},\qquad
(0,0)\quad\text{(LC-REI)},
\]
with the same full-step corrector as in the source paper. The continuous parameters \(\delta,\beta\) are used only to expose the cancellation mechanism.

For sufficiently small \(h\), the harmonic random affine chain is mean-square stable and has a unique stationary second-moment matrix \(\Sigma_h^{\delta,\beta}\). For the source choice \(\tau\sim U[0,1]\), direct expansion of its discrete Lyapunov equation gives
\[
\begin{aligned}
(\Sigma_h)_{XX}
&=\kappa^{-1}+\frac{\alpha}{6}(1+\delta-2\beta)h^2\\
&\quad+\frac{\alpha\{\alpha\kappa(4-3\delta)+\gamma^2(2\beta-\delta-1)\}}{24\gamma}h^3+O(h^4),\\
(\Sigma_h)_{XV}
&=\frac{\alpha^2\kappa(\delta-2)}{24}h^3+O(h^4),\\
(\Sigma_h)_{VV}
&=\alpha+\frac{\alpha^2\kappa}{3}(1-\beta)h^2\\
&\quad+\frac{\alpha^2\kappa\{\alpha\kappa(4-3\delta)+\gamma^2(2\beta-1)\}}{24\gamma}h^3+O(h^4).
\end{aligned}
\]

Hence the three principal methods have sharply different equilibrium moment biases:

| method | \(h^2\) coefficient of \(\operatorname{Var}X\) | \(h^2\) coefficient of \(\operatorname{Var}V\) | first displayed \(X,V\) covariance term |
|---|---:|---:|---:|
| LC-REI | \(+\alpha/6\) | \(+\alpha^2\kappa/3\) | \(-\alpha^2\kappa h^3/12\) |
| ALUM | \(-\alpha/6\) | \(0\) | \(-\alpha^2\kappa h^3/12\) |
| RMM | \(0\) | \(0\) | \(-\alpha^2\kappa h^3/24\) |

Thus LC-REI and ALUM have equal-magnitude but opposite leading configurational variance biases on a harmonic target, while only RMM cancels both variance defects at order \(h^2\). In particular, the source paper's empirical ordering of long-time *pathwise* RMSE does not determine equilibrium sampling bias: its reported LC-REI advantage over ALUM is compatible with the opposite-sign equilibrium variance defects above.

## A one-gradient no-go theorem

The obstruction persists beyond uniform randomization. Keep the one-gradient predictor, i.e. set \(\delta=0\), but allow an arbitrary law of \(\tau\in[0,1]\) and an arbitrary multiplier \(\beta\) on the intermediate Brownian term. Put
\[
m_1=\mathbb E\tau,\qquad m_2=\mathbb E\tau^2.
\]
Then
\[
\Sigma_h=\Sigma_\star+h\Sigma_1+h^2\Sigma_2+O(h^3),
\]
where
\[
(\Sigma_1)_{XX}=(\Sigma_1)_{VV}=0,\qquad
(\Sigma_1)_{XV}=\alpha\left(\frac12-m_1\right),
\]
and
\[
\begin{aligned}
(\Sigma_2)_{XX}
&=\alpha\left[m_1^2-m_1+(1-\beta)m_2+\frac1{12}\right],\\
(\Sigma_2)_{XV}
&=\frac{\alpha\gamma}{12}(6m_1-6m_2-1),\\
(\Sigma_2)_{VV}
&=\alpha^2\kappa\left[m_1^2+\frac1{12}-\beta m_2\right].
\end{aligned}
\]

Consequently, **no member of this one-gradient predictor family can match the full harmonic Gibbs covariance through order \(h^2\)**. Indeed, \((\Sigma_1)_{XV}=0\) forces \(m_1=1/2\), and then \((\Sigma_2)_{XV}=0\) forces \(m_2=1/3\). Under those two necessary conditions,
\[
(\Sigma_2)_{XX}=\frac{\alpha}{6}(1-2\beta),\qquad
(\Sigma_2)_{VV}=\frac{\alpha^2\kappa}{3}(1-\beta).
\]
The first vanishes only for \(\beta=1/2\), while the second vanishes only for \(\beta=1\). Thus changing only the random intermediate-time law and the predictor-noise amplitude cannot reproduce RMM's second-moment cancellation without restoring the extra deterministic predictor force evaluation.

For the uniform-time source family, the same statement is even simpler: the two order-\(h^2\) variance coefficients vanish simultaneously only at \((\delta,\beta)=(1,1)\), i.e. RMM.

## What uniform randomization buys LC-REI

For LC-REI itself (\(\delta=\beta=0\)), imposing only \(\mathbb E\tau=1/2\) gives
\[
\begin{aligned}
\operatorname{Var}_h(X)
&=\kappa^{-1}+\alpha\left(\operatorname{Var}(\tau)+\frac1{12}\right)h^2+O(h^3),\\
\operatorname{Cov}_h(X,V)
&=\alpha\gamma\left(\frac1{24}-\frac12\operatorname{Var}(\tau)\right)h^2+O(h^3),\\
\operatorname{Var}_h(V)
&=\alpha+\frac{\alpha^2\kappa}{3}h^2+O(h^3).
\end{aligned}
\]
Thus the configurational variance inflation is unavoidable for every centered random-time law and is minimized by deterministic \(\tau=1/2\), where its coefficient is \(\alpha/12\). Uniform randomization has \(\operatorname{Var}(\tau)=1/12\), doubling that minimum coefficient to \(\alpha/6\), but exactly cancels the order-\(h^2\) cross-covariance. More generally that cancellation fixes only the second moment \(m_2=1/3\); it does not uniquely characterize the uniform law.

The variance defect also yields a metric lower bound. Let \(\nu_h^X\) denote the stationary position marginal. Since the stationary mean is zero, every coupling with the target \(N(0,\kappa^{-1})\) obeys
\[
W_2\!\left(\nu_h^X,N(0,\kappa^{-1})\right)
\ge
\left|\sqrt{\operatorname{Var}_h(X)}-\kappa^{-1/2}\right|.
\]
For uniform LC-REI,
\[
W_2\!\left(\nu_h^X,N(0,\kappa^{-1})\right)
\ge \frac{\alpha\sqrt\kappa}{12}h^2+O(h^3).
\]
This is an invariant-measure error floor on the harmonic test problem, not an upper bound on general-target error.

## Verification

The symbolic artifact `artifacts/derive_series.py` expands the exact random affine recurrence and solves the stationary discrete Lyapunov equations coefficient-by-coefficient. It reproduces both the uniform \((\delta,\beta)\) family and the arbitrary-time one-gradient formulas above. The independent numerical artifact `artifacts/verify_stationary_covariance.py` evaluates the exact conditional Gaussian covariances by Gauss--Legendre quadrature and solves the stationary second-moment system at finite \(h\). For \(\gamma=3,\alpha=\kappa=1\), the scaled LC-REI variance defects converge numerically to \(1/6\) and \(1/3\), ALUM to \(-1/6\) and \(0\), and RMM to \(0\) and \(0\), while the LC-REI cross covariance divided by \(h^3\) approaches \(-1/12\).

## Relation to prior work and originality boundary

Lyu--Wang--Yang introduce LC-REI and explicitly compare it with RMM and ALUM. Their paper states that RMM uses two gradients and three Gaussians per step, ALUM one gradient and three Gaussians, and LC-REI one gradient and two Gaussians; it also reports smaller long-time pathwise position RMSE for LC-REI than ALUM on a linear underdamped OU experiment. Their analysis gives non-asymptotic Wasserstein convergence rates, but the inspected source does not state the stationary harmonic covariance expansions, the random-time moment formulas, or the one-gradient covariance obstruction above.

Stationary bias analysis for randomized midpoint Langevin schemes is not new in general. He--Balasubramanian--Erdogdu study ergodicity and stationary bias of randomized midpoint sampling, and a substantial numerical-analysis literature develops invariant-measure order conditions and harmonic-oscillator diagnostics for Langevin integrators. The present originality claim is therefore narrow: **to the best of our knowledge, it is the explicit equilibrium-moment classification for the newly proposed LC-REI / ALUM / RMM predictor family, together with the arbitrary-time one-gradient impossibility result and the resulting LC-REI harmonic Wasserstein lower bound.** Because LC-REI appeared only in arXiv:2609.20713, contemporaneous or not-yet-indexed follow-up analysis remains a residual originality risk.

## Limitations

The result is a one-dimensional harmonic-target theorem and a local small-\(h\) expansion of stationary second moments. It is not a proof of the full invariant distribution, which is generally non-Gaussian because the random intermediate time makes the linear update multiplicative-random. It does not rank the methods by transient strong error, general-target Wasserstein error, mixing time, or wall-clock efficiency. The continuous \(\beta\) interpolation is an analytic device; only \(\beta=0\) and \(\beta=1\) correspond to the source's listed schemes. The stability statement is asymptotic in sufficiently small \(h\); no maximal finite-step stability interval is claimed.

## References

1. W. Lyu, X. Wang, B. Yang, *A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New*, arXiv:2609.20713 (2026). https://arxiv.org/abs/2609.20713
2. Z. Hu, F. Huang, H. Huang, *Optimal Underdamped Langevin MCMC Method*, NeurIPS 34 (2021), 19363--19374. https://proceedings.neurips.cc/paper/2021/hash/a18aa23ee676d7f5ffb34cf16df3e08c-Abstract.html
3. Y. He, K. Balasubramanian, M. A. Erdogdu, *On the Ergodicity, Bias and Asymptotic Normality of Randomized Midpoint Sampling Method*, NeurIPS 33 (2020). https://arxiv.org/abs/2011.03176
4. N. Bou-Rabee, H. Owhadi, *Long-Run Accuracy of Variational Integrators in the Stochastic Context*, SIAM J. Numer. Anal. 48 (2010), 278--297. https://doi.org/10.1137/090758842
5. B. Leimkuhler, M. Sachs, *Efficient Numerical Algorithms for the Generalized Langevin Equation*, SIAM J. Sci. Comput. 44 (2022), A364--A388. https://doi.org/10.1137/20M138497X
