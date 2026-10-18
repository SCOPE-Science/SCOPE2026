# A sharp alignment threshold for minimax anisotropic Gaussian finite-difference probes

## Finding
Let \(d\ge2\), let \(H\subset\mathbb R^d\) have dimension \(1\le r<d\), write \(s=d-r\), and let \(P\) be the orthogonal projector onto \(H\). Fix an alignment interval \(0<a\le b<1\). A deterministic unit starting point is admissible when \(\|Px_0\|^2\in[a,b]\).

For the isotropic quadratic \(f(x)=\|x\|^2/2\), choose any positive-definite \(\Sigma\), any \(h>0\), and any \(\eta>0\). At each step draw a *fresh, independent* \(z_k\sim N(0,\Sigma)\) and update using the inverse-covariance-corrected central two-point estimator:
\[
\widehat g_\Sigma(x;z)=\Sigma^{-1}z\frac{f(x+hz)-f(x-hz)}{2h}=\Sigma^{-1}zz^{\mathsf T}x,\quad x_{k+1}=x_k-\eta\widehat g_\Sigma(x_k;z_k).
\]
This estimator is unbiased. Define \(c=1-2\eta+2\eta^2>0\) and \(L=1-2\eta+(d+2)\eta^2=c+d\eta^2\). For every integer \(k\ge0\), every deterministic \(x_0\), and every \(\Sigma\succ0\), the **exact** second moment is
\[
\mathbb E\|x_k\|^2=c^k\|x_0\|^2+\frac{L^k-c^k}{d}(x_0^{\mathsf T}\Sigma x_0)\operatorname{tr}(\Sigma^{-1}). \tag{1}
\]
For each \(k\ge1\), the global minimax choice over **all** positive-definite probe covariances and all admissible unit starting points can be taken \(\Sigma_*\propto t_*P+(I-P)\), with
\[
 t_* = \begin{cases}
 \sqrt{r(1-a)/(sa)},&a>r/d,\\
 \sqrt{r(1-b)/(sb)},&b<r/d,\\
 1,&a\le r/d\le b.
 \end{cases} \tag{2}
\]
The sharp worst-case expected squared norm is
\[
 c^k+\frac{L^k-c^k}{d}\Phi_*,\qquad
\Phi_* = \begin{cases}
 (\sqrt{ra}+\sqrt{s(1-a)})^2,&a>r/d,\\
 (\sqrt{rb}+\sqrt{s(1-b)})^2,&b<r/d,\\
 d,&a\le r/d\le b.
 \end{cases} \tag{3}
\]
The same \(t_*\) minimizes the risk at every positive finite horizon, regardless of \(\eta\) and \(h\). When the band lies strictly to one side of \(r/d\), anisotropy strictly improves the minimax finite-horizon risk relative to isotropic probes. When the band contains \(r/d\), isotropic probes are globally minimax.

However, **every** fixed positive-definite covariance has the *same* leading mean-square exponent \(L\): for nonzero \(x_0\), the coefficient of \(L^k\) in (1) is positive. Hence mean-square convergence holds exactly for \(0<\eta<2/(d+2)\), independently of the probe covariance. Shaping the probes changes a sharp finite-horizon prefactor but cannot improve the asymptotic exponent.

## Assumptions and scope
All spaces, random vectors, and matrices are real. Inverse covariance exists. Every Gaussian probe is independently redrawn; the difference uses two deterministic objective evaluations with the *same* probe and symmetric displacements. Computations use exact real arithmetic. The alignment interval is exogenous and fixed; the method is not assumed to infer it. Only initial unit vectors satisfying the band are adversarial; subsequent iterates need not remain aligned. The optimization is over constant, state-independent positive-definite \(\Sigma\) and a common constant stepsize \(\eta\). Multiplication of \(\Sigma\) by a positive scalar changes neither the law of the estimator nor the criterion.

## Proof
**Exact moment identity.** Since the quadratic is centered, its symmetric directional difference divided by \(2h\) equals \(z^{\mathsf T}x\). The second-moment matrix \(Q_k=\mathbb E[x_kx_k^{\mathsf T}]\) satisfies the Gaussian fourth-moment identity
\[
 \mathbb E[zz^{\mathsf T}Qzz^{\mathsf T}]=2\Sigma Q\Sigma+\operatorname{tr}(\Sigma Q)\Sigma.
\]
Consequently
\[
 Q_{k+1}=cQ_k+\eta^2\operatorname{tr}(\Sigma Q_k)\Sigma^{-1},\qquad
 \operatorname{tr}(\Sigma Q_{k+1})=L\operatorname{tr}(\Sigma Q_k).
\]
For \(Q_0=x_0x_0^{\mathsf T}\), solve the recursion directly:
\[
 Q_k=c^k Q_0+\frac{L^k-c^k}{d}(x_0^{\mathsf T}\Sigma x_0)\Sigma^{-1}.
\]
Taking the ordinary trace gives (1). As \(k\ge1\) and \(\eta>0\), the factor \(L^k-c^k\) is strictly positive.

**Reduction of the full positive-definite cone.** Normalize the inverse precision \(B=\Sigma^{-1}/\operatorname{tr}(\Sigma^{-1})\), so \(B\succ0\), \(\operatorname{tr}B=1\), and
\[
(x^{\mathsf T}\Sigma x)\operatorname{tr}(\Sigma^{-1})=x^{\mathsf T}B^{-1}x.
\]
Let \(\mathcal X=\{x:\|x\|=1,\ \|Px\|^2\in[a,b]\}\). The function \(F(B)=\sup_{x\in\mathcal X}x^{\mathsf T}B^{-1}x\) is convex, by operator convexity of matrix inversion (alternatively, the variational identity \(x^{\mathsf T}B^{-1}x=\sup_y(2x^{\mathsf T}y-y^{\mathsf T}By)\)). It is invariant under conjugation by the orthogonal group \(O(H)\times O(H^\perp)\), because \(\mathcal X\) is invariant. Averaging any \(B\) over this compact group preserves its trace and positive definiteness and, by convexity, cannot increase \(F\). The average is a positive scalar multiple of the identity on each subspace, so a global optimal covariance exists in the form \(tP+(I-P)\), \(t>0\). This argument covers *all* positive-definite covariances, including correlated matrices, not merely a preselected diagonal family.

**Scalar minimax and threshold.** For \(\Sigma=tP+(I-P)\) and \(\alpha=\|Px\|^2\), the factor to minimize is
\[
G(t)=\left(\frac rt+s\right)\max_{\alpha\in[a,b]}\bigl(\alpha t+1-\alpha\bigr).
\]
For \(t<1\) the maximizing alignment is \(a\); for \(t>1\) it is \(b\). At a fixed endpoint \(\alpha\), expand
\[
\left(\frac rt+s\right)(\alpha t+1-\alpha)
 =r\alpha+s(1-\alpha)+s\alpha t+\frac{r(1-\alpha)}t.
\]
The last two terms have a unique minimum at \(t=\sqrt{r(1-\alpha)/(s\alpha)}\), whose value yields \((\sqrt{r\alpha}+\sqrt{s(1-\alpha)})^2\). The minimizer lies below \(1\) exactly when \(\alpha>r/d\), and above \(1\) exactly when \(\alpha<r/d\). Therefore (2) and (3) exhaust the three alignment-band regimes, including boundary cases. For a band strictly on one side, \(\Phi_*<d\) follows from strict Cauchy–Schwarz. Otherwise every covariance has objective at least \(d\), attained by isotropic probes. The reduction and (1) prove simultaneous finite-horizon minimaxity.

**Asymptotic moment stability.** For nonzero \(x_0\) and \(\Sigma\succ0\), \((x_0^{\mathsf T}\Sigma x_0)\operatorname{tr}(\Sigma^{-1})/d>0\). Since \(0<c<L\), equation (1) has asymptotic growth factor \(L\). The strict inequality \(L<1\) holds exactly for \(0<\eta<2/(d+2)\). No alignment, covariance, or finite-horizon improvement alters this factor.

## Verification
A standalone Python program (`reproduce.py`) checks the closed-form minimizer against dense positive scalar-covariance grids for many dimensions and bands, verifies the convex-symmetrization Jensen bound on random positive-definite matrices, confirms the exact two-step covariance recursion, and compares one-step predictions to independently simulated Gaussian probes. Randomized comparisons are diagnostics, not proof of the global or infinite-horizon conclusions.

For example, take \(d=10\), \(r=2\), \([a,b]=[0.8,0.9]\). Then \(r/d=0.2\), \(t_*=1/4\), and \(\Phi_*=6.4\) rather than the isotropic \(10\); the coefficient of \(L^k-c^k\) improves by \(36\%\), although \(L\) does not change.

## Relationship to prior work
The directional-hint perspective was motivated by Ryabchenko, Qian, and Mou (2026), which proposes a control-variate approach to zeroth-order search; only its publicly accessible abstract and metadata were available for comparison. Ma and Huang (2025) optimize minimum-variance two-point estimators under an isotropic perturbation-moment constraint, including rank-deficient aligned designs. That isotropic constraint and their estimator do not imply the present inverse-covariance-corrected *all-SPD* covariance minimax with an uncertain alignment interval or exact finite-horizon evolution. Starnes and collaborators (2024) study anisotropic Gaussian smoothing of objectives and optimization procedures rather than this closed-form random-gradient moment/minimax law. Related published results on sparse Haar subspace descent concern different probe distributions and objectives. These distinctions are comparisons of examined statements, not a guarantee of global bibliographic novelty.

## Limitations
The result is for a centered isotropic quadratic and independent fresh Gaussian draws, without noisy function evaluations, finite precision, adaptive covariance estimation, or arbitrary smooth objectives. The criterion is worst-case Euclidean squared-norm *moment* at each fixed horizon, not the distributional tail, almost-sure convergence rate, computational cost, or objective decrease in general nonlinear problems. The result establishes existence of a block-isotropic global optimum and uniqueness of its covariance ratio among block-isotropic choices; it does **not** assert uniqueness over the entire SPD cone. Complete text of the recent directional-hint manuscript was unavailable, so possible coverage in unexamined material remains a bibliographic risk. Independent validation has not been performed.

## References
- D. Ryabchenko, Q. Qian, and L. Mou, *Adaptively Incorporating Directional Hints into Zeroth-Order Optimization*, first public September 8, 2026, arXiv:2609.08277. https://arxiv.org/abs/2609.08277
- Ma and Huang, *Revisiting Zeroth-Order Optimization: Minimum-Variance Two-Point Estimators and Directionally Aligned Perturbations*, arXiv:2510.19975. https://arxiv.org/abs/2510.19975
- Starnes et al., *Anisotropic Gaussian Smoothing for Gradient-based Optimization*, arXiv:2411.11747. https://arxiv.org/abs/2411.11747
- Published research: *Exact Haar moments remove sampling-dimension restrictions in sparse stochastic subspace descent*, September 18, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-exact-haar-moments-sparse-ssd--d9ecf263b248
