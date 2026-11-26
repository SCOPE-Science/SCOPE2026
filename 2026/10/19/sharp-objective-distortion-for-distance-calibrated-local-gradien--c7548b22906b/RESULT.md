# Sharp one-step objective amplification under a distance-calibrated gradient step

## Finding

Let \(Q\in\mathbb R^{d\times d}\) be symmetric positive definite, \(d\ge2\), and write \(\kappa=\lambda_{\max}(Q)/\lambda_{\min}(Q)\). For \(f(x)=x^{\mathsf T}Qx/2\) and \(x\ne0\), consider the distance-calibrated local linear-minimization step
\[
T(x)=x-\theta\|x\|_2\frac{Qx}{\|Qx\|_2},\qquad \theta=\frac{2\sqrt\kappa}{1+\kappa}.
\]
The supremum of \(f(T(x))/f(x)\) over all such \(d,Q,x\) is **5**, and it is not attained at any finite condition number. Moreover, for any fixed \(1<\gamma<2\), let \(d=\lceil\kappa^\gamma\rceil\), \(Q=\operatorname{diag}(\kappa,1,\ldots,1)\), and let \(x\) be uniform on the real Euclidean unit sphere in dimension \(d\). Then
\[
\frac{f(T(x))}{f(x)}\longrightarrow 5 \quad\text{in probability as }\kappa\to\infty.
\]
In this family a random initialization therefore typically approaches the global worst-case objective amplification even though every step decreases Euclidean distance to the minimizer.

## Assumptions and scope

The minimizer is zero. All objectives are full-space quadratics and the local linear oracle is solved exactly over the Euclidean ball of radius \(\theta\|x\|_2\) centered at \(x\). The condition number in the step is the actual condition number of \(Q\). The objective quotient is well defined for every nonzero \(x\). The probability statement uses the uniform-sphere law in each dimension and makes no claim of almost-sure convergence or about repeated iterates.

## Proof

Scaling \(Q\) to have smallest eigenvalue 1 and scaling \(x\) to have norm 1 do not change the objective quotient. In an orthonormal eigenbasis put \(p_i=x_i^2\) and \(m_j=\sum_i p_i\lambda_i^j\), where \(1\le\lambda_i\le\kappa\) and \(\sum_i p_i=1\). Direct expansion gives
\[
\frac{f(T(x))}{f(x)}=1-\frac{2\theta\sqrt{m_2}}{m_1}
+\frac{\theta^2m_3}{m_1m_2}.
\tag{1}
\]
As \(m_1\ge1\) and \(m_3\le\kappa m_2\), the ratio is bounded by \(1+\theta^2\kappa=1+4\kappa^2/(1+\kappa)^2<5\) at finite \(\kappa\).

For the spiked diagonal family in the finding, put \(p=x_1^2\). By the normalized-Gaussian representation of a uniform sphere vector, \(p\) has law \(U/(U+V_d)\), with independent \(U\sim\chi_1^2\) and \(V_d\sim\chi_{d-1}^2\). The law of large numbers gives \(dp\Rightarrow U\). The sequence \(dp\) is tight and its limit has no atom at zero. Since \(\kappa/d\to0\) and \(\kappa^2/d\to\infty\), it follows that \(\kappa p\to0\) and \(\kappa^2p\to\infty\) in probability. For the latter inference, for any fixed \(A>0\) and \(\delta>0\), eventually \(\Pr(\kappa^2 p\le A)\le\Pr(dp\le\delta)\); the limiting upper bound tends to zero as \(\delta\downarrow0\).

Now \(m_j=1-p+\kappa^j p\). Consequently \(m_1\to1\), \(m_2\to\infty\), and
\[
\frac{m_3}{\kappa m_2}=1-\frac{(1-1/\kappa)(1-p)}{m_2}\longrightarrow1,
\qquad
\theta^2m_2\le\frac4\kappa+4\kappa p\longrightarrow0
\]
in probability. In (1) the negative term tends to zero, and the last term tends to 4 because \(\theta^2\kappa\to4\). This proves the probability statement, hence also sharpness: for every positive tolerance, the ratio exceeds 5 minus that tolerance with positive probability for sufficiently large finite \(\kappa\).

## Verification

The proof uses exact expansion and elementary spectral inequalities, then the normalized-Gaussian law and convergence in probability. As an exact small-instance check, with \(Q=\operatorname{diag}(1,8)\) and \(x=(6,1)^{\mathsf T}\), the ratio is \((125654/2025-40\sqrt{74}/9)/22\), approximately \(1.08267\). This illustrates increase at finite \(\kappa\); it does not establish the sharp bound or the probability limit.

## Relationship to prior work

Theorem 3.5 of Richtárik, Gruntkowska and Li [1] gives squared-distance contraction by \(1-\theta^2\) at the same calibration. One-step amplification of the objective is a different question because the objective weights directions by their eigenvalues. The core-LARS descent frontier [2] already gives the exact sign of the one-step change uniformly over spectra in a prescribed interval for the proportional step with a free trust coefficient. Substituting \(\theta\) in that prior frontier recovers the descent cutoff for this calibration. That cutoff is not a contribution here. The result concerns the sharp magnitude of amplification and the probability of approaching it for the spiked sphere family; neither is given by the descent frontier.

## Limitations

The factor five is a supremum across condition numbers, not a finite-condition-number maximizer or a sharp amplification factor at each fixed condition number. The typicality assertion is for the specified varying-dimensional spectrum and does not concern arbitrary spectra, constrained or nonlinear optimization, finite-sample rates, or multistep objective growth.

## References

1. P. Richtárik, K. Gruntkowska, and H. Li, *Local LMO: Constrained Gradient Optimization via a Local Linear Minimization Oracle*, arXiv:2605.08850v1, §3.3, Theorem 3.5. https://arxiv.org/html/2605.08850v1
2. *Sharp condition-number frontier for objective descent in core LARS*, Resultary record 70b4a7c981f6. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-condition-number-frontier-for-objective-descent-in-core-la--70b4a7c981f6
