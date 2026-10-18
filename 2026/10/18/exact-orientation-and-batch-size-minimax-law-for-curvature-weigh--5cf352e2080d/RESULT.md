# Exact orientation and batch-size minimax law for curvature-weighted Rademacher probes

## Finding
Consider the three-point, curvature-weighted simultaneous-perturbation update on a centered positive-definite quadratic in two real dimensions. With the full curvature exponent, its optimal **worst-start one-step expected objective error**, jointly over the orientation of the quadratic and the positive step size, is exactly \(1/(n+1)\) times the initial error for any batch of \(n\geq1\) independent Rademacher probes. For unequal fixed eigenvalues, the unique optimal orientation puts the Hessian eigenvectors on the two Rademacher diagonals (a \(45^\circ\) rotation), and the unique optimal step is \(2n/(n+1)\). At this orientation, the resulting factor holds at every iteration and therefore gives the exact finite-horizon mean-square law.

More precisely, let \(\kappa>1\), \(n\in\{1,2,\ldots\}\), \(0\leq\theta\leq\pi/4\), and
\[
H_\theta=R_\theta\operatorname{diag}(\kappa,1)R_\theta^{\mathsf T},\qquad R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}.
\]
For a deterministic \(e\ne0\), take independent probes \(z_1,\ldots,z_n\), each uniform on \(\{-1,1\}^2\), and set
\[
e^+=e-\frac{\eta}{n}\sum_{j=1}^{n}\frac{z_j^{\mathsf T}H_\theta e}{z_j^{\mathsf T}H_\theta z_j}\,z_j,\qquad\eta>0.
\]
Write \(\|e\|_H^2=e^{\mathsf T}He\), and let \(\mathcal R_{n,\theta}(\eta)\) be the supremum of \(\mathbb E\|e^+\|_{H_\theta}^2/\|e\|_{H_\theta}^2\) over nonzero deterministic \(e\). Define
\[
\delta_\theta=\frac{(\kappa-1)\cos(2\theta)}{\sqrt{(\kappa+1)^2-(\kappa-1)^2\sin^2(2\theta)}},\qquad
\lambda_\pm=\frac{1\pm\delta_\theta}{2},
\]
and
\[
F_{n,\eta}(t)=1-2\eta t+\eta^2\left(\frac{t}{n}+\left(1-\frac1n\right)t^2\right).
\]
Then the exact all-angle result is
\[
\boxed{\mathcal R_{n,\theta}(\eta)=\max\{F_{n,\eta}(\lambda_-),F_{n,\eta}(\lambda_+)\}.}
\]
Furthermore,
\[
\boxed{\min_{0\leq\theta\leq\pi/4,\,\eta>0}\mathcal R_{n,\theta}(\eta)=\frac1{n+1},\quad
\theta_*=\frac\pi4,\quad\eta_*=\frac{2n}{n+1}.}
\]
The displayed minimizer is unique for every \(\kappa>1\) and positive integer \(n\). With independent new batches at every step and fixed optimal parameters,
\[
\boxed{\mathbb E\|e_k\|_{H_{\pi/4}}^2=(n+1)^{-k}\|e_0\|_{H_{\pi/4}}^2\quad(k=0,1,2,\ldots).}
\]
In contrast, for axis-aligned Hessians \((\theta=0)\), \(\lim_{\kappa\to\infty}\min_{\eta>0}\mathcal R_{n,0}(\eta)=1\), whereas the optimally rotated factor remains \(1/(n+1)\). This quantifies a sharp orientation effect not captured by the Hessian condition number alone.

## Assumptions and scope
The loss is exactly \(L(e)=\tfrac12e^{\mathsf T}H_\theta e\); there is no observation noise or numerical rounding. All probes are independent within and across batches. The three-point curvature estimate is \(c(z)=[L(e+\epsilon z)-2L(e)+L(e-\epsilon z)]/\epsilon^2=z^{\mathsf T}H_\theta z\) for any \(\epsilon>0\). Its value is at least \(2\), since \(H_\theta\succeq I\) and \(\|z\|^2=2\). Consequently, the scalar weight of the cited three-point method with curvature exponent \(\alpha=1\) and regularization floor \(\lambda_{\rm reg}=1\) is exactly \(w(z)=1/c(z)\), without saturation. Writing the update in the conventional learning-rate form yields the displayed \(\eta\); the source's tied learning-rate/perturbation-radius convention is recovered by setting \(\epsilon=\eta\). All formulas are exact for this quadratic at every positive perturbation radius.

The risk is **expected objective energy** (equivalently, squared Hessian norm) in the worst deterministic initial direction. It is not the Euclidean squared norm, not a high-probability bound, and not a general nonlinear guarantee. Orientation is varied while eigenvalues \(\{1,\kappa\}\) are held fixed; the optimizer need not be able to rotate an arbitrary real-world objective.

## Proof
First, the four possible sign probes reduce projectively to two equiprobable directions \(u_+=(1,1)^{\mathsf T}/\sqrt2\) and \(u_-=(1,-1)^{\mathsf T}/\sqrt2\). Define
\[
G_\pm=\frac{u_\pm u_\pm^{\mathsf T}H_\theta}{u_\pm^{\mathsf T}H_\theta u_\pm},\qquad M=\frac{G_++G_-}{2}.
\]
Each \(G_\pm\) is a rank-one projector in the \(H_\theta\) inner product: \(G_\pm^2=G_\pm\) and \(G_\pm^{\mathsf T}H_\theta=H_\theta G_\pm\). This is verified directly by multiplying the rank-one expression and using its positive scalar denominator.

In the orthonormal basis \((u_+,u_-)\), write \(H_\theta=\begin{pmatrix}a&b\\b&d\end{pmatrix}\). The identities \(a+d=\kappa+1\), \(ad-b^2=\kappa\), \(a-d=(\kappa-1)\sin2\theta\), and \(b=(\kappa-1)\cos2\theta/2\) hold, with a harmless sign change in \(b\) for the opposite rotation convention. Therefore
\[
M=\frac12\begin{pmatrix}1&b/a\\b/d&1\end{pmatrix},\qquad
\operatorname{spec}(M)=\left\{\frac{1\pm b/\sqrt{ad}}2\right\}.
\]
Since \(4ad=(\kappa+1)^2-(\kappa-1)^2\sin^2(2\theta)\), these eigenvalues equal the stated \(\lambda_\pm\). The matrix \(M\) is self-adjoint in the \(H_\theta\) inner product, so its eigenvectors form an orthogonal basis for that metric.

Next, put \(\overline G=n^{-1}\sum_{j=1}^n G_j\) for independent equally likely copies of \(G_+\) and \(G_-\). Independence and idempotence give the **exact matrix identities**
\[
\mathbb E\overline G=M,\qquad
\mathbb E\overline G^2=\left(1-\frac1n\right)M^2+\frac1nM.
\]
The product \(I-\eta\overline G\) is self-adjoint in the Hessian metric. Expanding its squared metric norm and taking conditional expectation yields
\[
\mathbb E\|e^+\|_{H_\theta}^2
=e^{\mathsf T}H_\theta\left[I-2\eta M+\eta^2\left(\left(1-\frac1n\right)M^2+\frac1nM\right)\right]e.
\]
Diagonalizing \(M\) in the Hessian metric proves the formula for \(\mathcal R_{n,\theta}(\eta)\), with no asymptotic approximations or unverified enumeration.

For global optimality, since \(\lambda_-+\lambda_+=1\), the mean of the two directional risk factors satisfies
\[
\frac{F_{n,\eta}(\lambda_-)+F_{n,\eta}(\lambda_+)}2
=F_{n,\eta}(1/2)+\frac{\eta^2}{4}\left(1-\frac1n\right)\delta_\theta^2
\geq F_{n,\eta}(1/2).
\]
The maximum is at least this mean. Direct completion of the square gives
\[
F_{n,\eta}(1/2)=1-\eta+\frac{n+1}{4n}\eta^2
=\frac1{n+1}+\frac{n+1}{4n}\left(\eta-\frac{2n}{n+1}\right)^2.
\]
Thus no angle or step beats \(1/(n+1)\). At \(\theta=\pi/4\), \(b=\delta_\theta=0\) and \(M=I/2\), so equality holds at the stated step. For \(n>1\), strictness of the averaged inequality forces \(\delta_\theta=0\) at every positive optimal step, hence \(\theta=\pi/4\). For \(n=1\), the sole optimal step is \(\eta=1\), and \(F_{1,1}(t)=1-t\); the larger of its two values exceeds \(1/2\) unless \(\delta_\theta=0\). This proves uniqueness also for one probe.

For independent subsequent batches at the optimal orientation, the just-proved conditional expectation is \(\mathbb E(\|e_{k+1}\|_{H_{\pi/4}}^2\mid e_k)=(n+1)^{-1}\|e_k\|_{H_{\pi/4}}^2\). Iterated conditioning gives the exact claimed \(k\)-step identity.

Finally, at \(\theta=0\), \(\lambda_-=1/(\kappa+1)\) and \(\lambda_+=\kappa/(\kappa+1)\). The candidate \(\eta=1\) has both risk factors at most one, so the optimal factor does not exceed one. Any step with a worst-case factor at most one obeys \(\eta\leq2/[\lambda_+(1-1/n)+1/n]\), which is uniformly bounded for \(\kappa\geq1\). For these bounded steps, \(F_{n,\eta}(\lambda_-)\geq1-2\eta/(\kappa+1)\to1\) uniformly. The infimum therefore tends to one, proving the sharp orientation contrast.

## Verification
The standalone `REPRODUCE.py` script independently assembles the quadratic Hessian, evaluates the three-point finite-difference quantities (rather than substituting the analytical estimator), enumerates all binomial outcomes for batches up to size eight, and compares their exact conditional energy matrices against the polynomial moment identity. It additionally checks the projector identities, the closed eigenvalue formula, risk eigenvalues, the optimal-angle equality and strict nonoptimal-angle tests. Execution with Python and NumPy completed 5,719 numerical identity/inequality checks without failures. These are finite corroborations; arbitrary dimensions, batch sizes, and horizons are proved above analytically under the stated two-dimensional model.

Reproduce with `python REPRODUCE.py` after installing NumPy. No dataset, third-party paper, network, or auxiliary file is required.

## Relationship to prior work
Chaubard, Kochenderfer, and Ré introduced curvature-weighted probe-space 1.5-SPSA, including the power-one weight as an allowed parameter choice and a rotated stiff-quadratic test. Their Appendix A.2 explicitly notes that Rademacher probes require rotation to expose variable directional curvature; that qualitative observation is credited here. Their Sections 4–5 and the relevant appendix do not state the present all-angle Hessian-metric risk spectrum, the exact finite-batch minimax, uniqueness of the optimizing orientation and step, or the exact all-horizon law at that optimum.

Classical simultaneous perturbation stochastic approximation and randomized one-dimensional line-search/gradient-subspace methods supply the broader framework for random-direction optimization. The best-aligned special case here is a familiar randomized orthogonal-direction projection; its projector algebra is standard and is not claimed as independently new. The assessed contribution is the full **orientation-dependent, curvature-weighted finite-batch** characterization and its sharp joint optimization, including the axis-aligned asymptotic obstruction. General rates for independent random subspaces do not by themselves identify this two-direction orientation phase law.

## Limitations
The theorem covers a noise-free, centered, two-dimensional quadratic, full curvature weighting \(\alpha=1\), regularization floor one, independent Rademacher probes, and exact arithmetic. The reported mean-square rate measures Hessian energy, not Euclidean error or almost-sure rate. The practical study cited below prefers a smaller curvature exponent, so the theorem is a structural benchmark for a permitted endpoint rather than a performance prediction for its selected exponent. It does not assert that optimizing an objective's orientation is feasible, nor extend to arbitrary perturbation distributions, indefinite Hessians, noisy function values, nonlinear losses, or learning outcomes. Other unindexed work may contain equivalent specializations.

## References
1. F. Chaubard, M. J. Kochenderfer, and C. Ré, *Probe-Space Preconditioning for Fast and Stable Zero-Order Training*, arXiv:2609.38095v1, first public 2026-09-29, Sections 3–5 and Appendix A.2, https://arxiv.org/html/2609.38095.
2. D. Kozak, S. Becker, A. Doostan, and L. Tenorio, *A stochastic subspace approach to gradient-free optimization in high dimensions*, arXiv:2003.02684, https://arxiv.org/abs/2003.02684.
3. S. U. Stich, C. L. Müller, and B. Gärtner, *Optimization of Convex Functions with Random Pursuit*, SIAM Journal on Optimization 23 (2013), 1284–1309, https://doi.org/10.1137/110853613.
4. J. C. Spall, *Simultaneous Perturbation Stochastic Approximation*, in *Introduction to Stochastic Search and Optimization* (2003), https://doi.org/10.1002/0471722138.ch7.
