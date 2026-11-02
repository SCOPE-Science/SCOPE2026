# A sharp covariance-rank frontier for finite-step Landweber iteration

## Finding
For every integer \(K\ge2\), there is a unique \(t_K\in(0,1)\) solving
\[
2Kt_K(1-t_K)^{K-1}=1-(1-t_K)^K.
\]
In the finite-dimensional Gaussian Landweber model defined below, a truncation to the leading eigenvectors of the normal operator is simultaneously a best rank-restricted truncation of the propagated noise covariance for **every** admissible normal operator whose scaled spectrum lies in \((0,t_K]\). This is the largest possible *uniform* spectral ceiling with that guarantee. Specifically, for every \(s\in(t_K,2)\), a stable two-dimensional example with scaled operator norm below \(s\) violates the leading-normal-eigenvector ranking.

The first thresholds and the large-iteration law are
\[
t_2=\frac23,\qquad t_3=\frac{9-\sqrt{21}}{10},\qquad
Kt_K\longrightarrow c_*=1.2564312086261696\ldots,
\quad e^{c_*}=1+2c_*.
\]

The discrepancy does not require step sizes close to the stability boundary: at \(K=2\), the scaled spectrum \(\{1,2/3\}\) produces respective covariance eigenweights \(1,32/27\), reversing the normal-operator order under a nonovershooting step.

For **every even** \(K\ge2\), the difference between leading-normal-operator truncation and covariance-optimal truncation can be unboundedly large in relative approximation error while the Landweber iteration remains convergent. In the explicit two-dimensional family below, their rank-one error ratio grows as \(\epsilon^{-2}\), and the exact ratio of the variances of standard Rademacher estimators for their respective residual covariance diagonals grows as \(\epsilon^{-4}\). This is an exact parameter-selection and residual-sampling-cost boundary, not a failure theorem for any complete uncertainty-quantification algorithm that also accounts for residuals.

## Assumptions and scope
Let \(A\in\mathbb R^{m\times d}\) have full column rank, \(B=A^\top A\) be positive definite, and suppose the data are \(y=Ax^\dagger+\xi\) with \(\xi\sim N(0,\sigma^2I_m)\), \(\sigma>0\). Start at zero and perform exactly \(K\ge2\) ordinary, unpreconditioned Landweber iterations
\[
x^{(j+1)}=x^{(j)}+\omega A^\top(y-Ax^{(j)}),\quad
x^{(0)}=0,\quad 0<\omega\lambda_{\max}(B)<2.
\]
Define the propagated covariance \(\Gamma_K=\operatorname{Cov}(x^{(K)})\), where the fixed deterministic \(x^\dagger\) is not random. An exact rank-\(r\) *normal-eigenvector truncation* is the restriction of \(\Gamma_K\) to the span of eigenvectors of the \(r\) largest eigenvalues of \(B\). A *covariance-optimal rank-\(r\) truncation* is a best rank-\(r\) positive-semidefinite approximation to \(\Gamma_K\) in either spectral or Frobenius norm. These are ideal deterministic truncations, distinct from approximation errors of a randomized eigensolver.

The probe comparison uses independent Rademacher vectors \(z\in\{-1,1\}^2\), the unbiased diagonal estimator \(\widehat{\operatorname{diag}}(R)=N^{-1}\sum_{a=1}^N z^{(a)}\odot(Rz^{(a)})\), and a positive-semidefinite rank-one residual covariance \(R\). Only its coordinatewise probe variance is compared.

## Proof
**Covariance spectrum.** Write \(T=I-\omega B\). The random part of the \(K\)-th iterate is \(\omega\sum_{j=0}^{K-1}T^jA^\top\xi\). Since \(B\) and \(T\) commute,
\[
\begin{aligned}
\Gamma_K
&=\sigma^2\omega^2B\left[\sum_{j=0}^{K-1}(I-\omega B)^j\right]^2\\
&=\sigma^2B^{-1}[I-(I-\omega B)^K]^2
=\sigma^2\omega f_K(\omega B),
\\
f_K(t)&=\frac{[1-(1-t)^K]^2}{t},\qquad 0<t<2.
\end{aligned}
\]
In particular, the covariance and normal operator have identical eigenvectors but may rank them differently.

**Unique interior threshold.** On \(0<t<1\), put \(g=1-(1-t)^K>0\). Then
\[
f_K'(t)=\frac{g}{t^2}\left[2Kt(1-t)^{K-1}-g\right].\]
Set \(u=1-t\); the bracket becomes
\[
H_K(u)=2Ku^{K-1}-(2K-1)u^K-1,
\quad H_K'(u)=Ku^{K-2}[2(K-1)-(2K-1)u].
\]
Here \(H_K(0)=-1\), \(H_K(1)=0\), and \(H_K\) first strictly increases to its sole interior maximum at \(u=2(K-1)/(2K-1)\), then strictly decreases to zero. Hence the maximum is positive and there is exactly one zero strictly between zero and one, giving \(t_K\in(0,1)\). The derivative \(f_K'\) is positive before \(t_K\) and negative throughout \((t_K,1)\).

It follows that if \(\omega\lambda_{\max}(B)\le t_K\), normal eigenvalue ranking and covariance eigenvalue ranking coincide. The Eckart--Young--Mirsky principle applied to the positive-semidefinite covariance then shows leading-normal-eigenvector truncation is best for every rank \(r\). Conversely, fix any \(s>t_K\) below the stability ceiling \(2\); choose \(t_K<a<b<\min\{s,1\}\) and \(B=\operatorname{diag}(b,a)\), \(\omega=1\). Then \(f_K(a)>f_K(b)\), so its largest-normal-eigenvector rank-one truncation is strictly suboptimal. This proves sharpness as a **uniform** ceiling, without asserting reversal for every fixed normal spectrum above the ceiling.

For \(K=2\), \(f_2(t)=t(2-t)^2\), with unique interior maximum at \(2/3\). For \(K=3\), \(f_3(t)=t(3-3t+t^2)^2\); its derivative changes sign at \((9-\sqrt{21})/10\). For the large-\(K\) limit, evaluate the defining derivative bracket at \(t=c/K\). It converges, for every fixed \(c>0\), to
\[
(1+2c)e^{-c}-1.
\]
This expression is positive at \(c=1\), negative at \(c=2\), and has exactly one positive zero \(c_*=1.2564312086261696\ldots\). The uniqueness of \(t_K\) traps \(Kt_K\) between any two constants straddling \(c_*\), proving the limit.

**Unbounded mismatch even with stable steps.** Fix even \(K\ge2\), let \(Q=2^{-1/2}\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}\), and define
\[
B_\epsilon=Q\operatorname{diag}(2-\epsilon,t_K)Q^\top,
\quad A_\epsilon=B_\epsilon^{1/2},\quad\omega=\sigma=1.
\]
For every sufficiently small \(\epsilon>0\), \(B_\epsilon\) is positive definite and \(\|B_\epsilon\|_2=2-\epsilon<2\), so the iteration is strictly stable. Its covariance eigenvalues on the high and low normal modes are, respectively,
\[
a_\epsilon=f_K(2-\epsilon)
=\frac{[1-(1-\epsilon)^K]^2}{2-\epsilon}
\sim\frac{K^2}{2}\epsilon^2,
\qquad b_K=f_K(t_K)>0.
\]
For sufficiently small \(\epsilon\), \(a_\epsilon<b_K\). The rank-one truncation keeping the high eigenmode of \(B_\epsilon\) has residual covariance \(b_Kv_Lv_L^\top\), whereas the covariance-optimal rank-one truncation has residual \(a_\epsilon v_Hv_H^\top\), with \(v_H=(1,1)^\top/\sqrt2\) and \(v_L=(1,-1)^\top/\sqrt2\). Both spectral-norm and Frobenius-norm error ratios are therefore
\[
R_K(\epsilon)=\frac{b_K}{a_\epsilon}
\sim\frac{2f_K(t_K)}{K^2\epsilon^2}\longrightarrow\infty.
\]
For \(K=2\), this ratio is exactly
\[
R_2(\epsilon)=\frac{32}{27(2-\epsilon)\epsilon^2}.
\]

**Exact diagonal probe variance.** For either residual rank-one covariance \(R=\gamma vv^\top\), where \(v=(1,\pm1)^\top/\sqrt2\), the first-coordinate single-probe diagonal estimator is \(\gamma(1\pm z_1z_2)/2\). Its expectation is \(\gamma/2\), and its variance is exactly \(\gamma^2/4\). For \(N\) independent probes, this becomes \(\gamma^2/(4N)\). The ratio of the two rank-one residual-probe variances is exactly
\[
\frac{b_K^2/(4N)}{a_\epsilon^2/(4N)}
=R_K(\epsilon)^2
\sim\frac{4f_K(t_K)^2}{K^4\epsilon^4}.
\]
This is a comparison at the same probe count and for the same numerical covariance diagonal; it does not claim the entire underlying inverse-problem confidence procedure has that error ratio.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It checks the first two thresholds, the derivative sign and root separation on thousands of parameter pairs, three large-iteration scales, literal finite-step matrix covariance against the spectral functional calculus, exact-rational two-step ratios, and complete enumeration of the four two-dimensional Rademacher outcomes. These computations corroborate the formulas; the derivative, asymptotic, sharpness, and variance arguments above, not a finite grid, establish the universal claims.

Run with `python3 verify.py`.

## Relationship to prior work
Abhishek and Holman (arXiv:2610.00882v1, first public 2026-10-01) derive propagated uncertainty for ordinary Landweber iteration and motivate approximating a normal operator with randomized singular-value decomposition, including residual correction and sampling uncertainty. That covariance formula and the use of normal-operator spectral truncation are prior work, not claimed as new. The present claim concerns the **sharp uniform ordering threshold** for the covariance versus the normal operator and the explicit, unbounded rank/probe-efficiency separation when that order reverses. The motivating method may remain statistically valid if its residual correction is sufficiently accurate.

Celisse and Wahl (JMLR 22, 2021) state the ordinary Landweber spectral filter and study discrepancy stopping and risk bounds under a step convention excluding the nearly \(2\)-scaled regime, but do not give this rank-order or Hutchinson diagonal-probe classification. Ito and Jin (arXiv:1909.01947) study low-rank randomized SVD in regularized inverse reconstruction; their work is relevant to approximation but not known to supply the present joint rank-and-probe threshold. The familiar Eckart--Young rank-selection principle, spectral filter identity, and Rademacher diagonal-estimation identity are used as standard ingredients. Absence from examined sources is not a claim of exhaustive historical priority.

## Limitations
The operator is finite-dimensional and full-column-rank, and the noise is white Gaussian. This is an *ideal eigen-subspace* comparison, not a bound for approximate randomized eigenvectors or for joint bias-plus-variance statistical coverage. The unbounded error and probe-cost ratios use even iteration counts and steps approaching the upper stability limit; the sharp uniform safe-ranking threshold is valid for all integers \(K\ge2\). Results are for fixed-step, unpreconditioned Landweber and a standard independent Rademacher diagonal estimator; they do not cover adaptive or variance-reduced probe allocations, nonwhite noise, nonlinear inverse maps, arbitrary priors, or full confidence-interval validity. Some older specialized literature could contain an equivalent ordering result; no independent audit has been performed.

## References
1. A. Abhishek and S. Holman, *Uncertainty Quantification for Landweber Iteration with Randomized Normal-Operator Approximation*, arXiv:2610.00882v1, first public 2026-10-01, https://arxiv.org/abs/2610.00882.
2. A. Celisse and M. Wahl, *Analyzing the discrepancy principle for kernelized spectral filter learning algorithms*, Journal of Machine Learning Research 22(76), 2021, https://jmlr.org/papers/volume22/20-358/20-358.pdf.
3. K. Ito and B. Jin, *Regularized Linear Inversion with Randomized Singular Value Decomposition*, arXiv:1909.01947, https://arxiv.org/abs/1909.01947.
