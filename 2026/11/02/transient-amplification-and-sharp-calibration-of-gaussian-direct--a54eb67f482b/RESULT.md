# Transient amplification and sharp calibration of Gaussian direction-hint descent

## Finding

For a centered two-point Gaussian control-variate descent method on an isotropic quadratic, a partially accurate projected-gradient hint has an exact two-component mean-square evolution. Its optimal **asymptotic** convergence can improve strictly over unguided Gaussian probing while its sharp **one-step** worst-case error never improves. A nearly full-dimensional hint yields a dimension-free asymptotic factor only when its relative calibration error is on the scale \(d^{-1/2}\) or smaller.

The following statements form one theorem, including the finite-time boundary that distinguishes asymptotic improvement from transient amplification.

## Assumptions and scope

Fix integers \(d\ge2\) and \(1\le k<d\). Set \(r=d-k\). Let \(P=P^\mathsf T=P^2\) have rank \(k\), and write \(Q=I_d-P\). Let \(a>0\), \(\tau>0\), \(s>0\), and \(\beta\in\mathbb R\). The objective is \(f(x)=\frac a2\|x\|^2\), with minimizer at the origin. Independently for each integer \(t\ge0\), draw \(u_t\sim N(0,I_d)\), and set

\[
 m_t=\beta aPx_t,\qquad
 \widehat g_t=m_t+\left[\frac{f(x_t+\tau u_t)-f(x_t-\tau u_t)}{2\tau}-m_t^\mathsf Tu_t\right]u_t,\qquad
 x_{t+1}=x_t-\frac{s}{a}\widehat g_t.
\]

Here \(P\) and \(\beta\) remain fixed over time, and \(x_0\) is deterministic, though the same formulas hold for a square-integrable independent initial condition. The reference can represent an inexpensive approximate projected gradient; on this quadratic it could also be computed from centered coordinate probes in a basis of \(\operatorname{ran}P\). No assumption of a globally bounded gradient is made. The central difference (unlike the one-sided estimator in the motivating article) is exact on quadratics for every positive radius \(\tau\).

Put \(\delta=1-\beta\), \(V_t=\mathbb E\|Px_t\|^2\), and \(W_t=\mathbb E\|Qx_t\|^2\).

## Proof

**1. Exact conditional moments.** Since the centered difference equals \(a\langle x_t,u_t\rangle\), write \(v=(I-\beta P)x_t=\delta Px_t+Qx_t\). The dimensionless estimator is

\[
 a^{-1}\widehat g_t=x_t+(u_tu_t^\mathsf T-I_d)v.
\]

For a standard real Gaussian vector \(u\), Isserlis' identity gives

\[
 \mathbb E[(u^\mathsf Tv)^2uu^\mathsf T]=\|v\|^2I_d+2vv^\mathsf T,\quad
 \mathbb E[(uu^\mathsf T-I_d)v]=0,\quad
 \operatorname{Cov}((uu^\mathsf T-I_d)v)=\|v\|^2I_d+vv^\mathsf T.
\]

Project the update onto the two mutually orthogonal blocks and take squared norms. Their cross terms vanish conditionally. With \(c=(1-s)^2\), the result is **exact**, for every integer \(t\ge0\):

\[
 \binom{V_{t+1}}{W_{t+1}}=M_s\binom{V_t}{W_t},\qquad
 M_s=cI_2+s^2B,\quad
 B=\begin{pmatrix}(k+1)\delta^2&k\\r\delta^2&r+1\end{pmatrix}.
\]

No stochastic approximation, smoothing-radius limit, or independence assumption between \(Px_t\) and \(Qx_t\) has been used.

**2. Perron eigenvalue and optimal step.** The trace and determinant of \(B\) are \(T=(k+1)\delta^2+r+1\) and \(D=(d+1)\delta^2\). The discriminant is

\[
 T^2-4D=\big((k+1)\delta^2-(r+1)\big)^2+4kr\delta^2\ge0.
\]

The Perron eigenvalue and the resulting sharp worst-initial-state asymptotic mean-square factor are

\[
 \lambda_+=\frac{T+\sqrt{T^2-4D}}2,\qquad
 \rho_s=(1-s)^2+s^2\lambda_+.
\]

Indeed \(M_s\) is nonnegative. For \(\delta\ne0\), it is irreducible and the Perron mode is reached by any nonzero positive initial block energy. For \(\delta=0\), its eigenvalues are \(c\) and \(c+s^2(r+1)\), the latter attained for any initial error with \(W_0>0\). Thus

\[
 \lim_{t\to\infty}\left(\sup_{x_0\ne0}\frac{\mathbb E\|x_t\|^2}{\|x_0\|^2}\right)^{1/t}=\rho_s.
\]

The quadratic in \(s\) has a unique minimum at \(s_*=1/(1+\lambda_+)\), with \(\rho_*=\lambda_+/(1+\lambda_+)\); all initial conditions converge in mean square exactly for \(0<s<2/(1+\lambda_+)\).

**3. Calibration phase and the one-step contrast.** At \(\delta^2=1\), every row of \(B\) sums to \(d+1\), so \(\lambda_+=d+1\). For \(\delta^2>0\), the Perron root is strictly increasing in \(\delta^2\) by the comparison theorem for irreducible nonnegative matrices (both first-column entries grow strictly). Continuity gives the same ordering at \(\delta=0\). Hence the optimally tuned asymptotic rate is strictly better than unguided \(\beta=0\) precisely when \(|1-\beta|<1\), equivalently \(0<\beta<2\). Equality occurs at \(\beta=0,2\); outside the interval the rate worsens.

On the other hand, summing the projected variances in Step 1 **before iteration** gives

\[
 \mathbb E[\|x_1\|^2\mid x_0]
 =\big(c+s^2(d+1)\delta^2\big)\|Px_0\|^2
 +\big(c+s^2(d+1)\big)\|Qx_0\|^2.
\]

Therefore the sharp one-step worst-case factor over all nonzero initial errors is

\[
 C_1(s)=c+s^2(d+1)\max\{1,\delta^2\}.
\]

For every \(0\le\beta\le2\) and each common \(s\), this is **identical** to the unguided worst-case first step. In particular, asymptotic acceleration does not imply a better uniform one-step guarantee.

**4. Exact finite-time transient for a perfect hint.** At \(\beta=1\), set \(b=c+s^2(r+1)\). The upper-triangular matrix gives for every integer \(t\ge0\)

\[
 W_t=b^tW_0,\qquad
 V_t=c^tV_0+\frac{k}{r+1}(b^t-c^t)W_0.
\]

For each \(t\ge1\), the exact worst-initial-state energy factor is

\[
 C_t=b^t+\frac{k}{r+1}(b^t-c^t),
\]

attained by initial errors in \(\operatorname{ran}Q\). The optimal step is \(s_*=1/(r+2)\), so \(b=(r+1)/(r+2)<1\), but \(C_1=(1-s_*)^2+s_*^2(d+1)\). For example, if \(r=1\) and \(s_*=1/3\), then \(C_1=(d+5)/9\), which exceeds one for \(d\ge5\), even though the sharp asymptotic factor is \(2/3\). This isolates a rank-dependent transient-amplification mechanism.

**5. Critical calibration window.** For fixed \(r\) as \(d\to\infty\), the Perron root satisfies \(\lambda_+\ge\max\{r+1,(k+1)\delta^2\}\) and \(\lambda_+\le T=r+1+(k+1)\delta^2\). Consequently \(\sup_d\lambda_+<\infty\) exactly when \(\sup_d d\delta_d^2<\infty\) (over \(d>r\)). Since \(\rho_*=\lambda_+/(1+\lambda_+)\), this is equivalent to a uniform contraction factor strictly below one. Under \(\delta_d=c_0/\sqrt d\) for fixed real \(c_0\), the trace approaches \(r+1+c_0^2\) and determinant approaches \(c_0^2\), hence

\[
 \lambda_+\longrightarrow
 \frac{r+1+c_0^2+\sqrt{(r+1+c_0^2)^2-4c_0^2}}2.
\]

This completes the theorem.

## Verification

Run `python3 verify.py` in the same directory as this document. The self-contained standard-library verifier performs 210 exact-rational independent update-moment replays using a five-atom distribution matching Gaussian moments through order four; 13,688 spectral/parameter comparisons; and 16 critical-window checks. The resulting output is `VERIFY_OK 13914`. The exact-rational replay checks the stochastic update itself, while the proof above supplies the infinite-dimensional-parameter and all-time conclusions.

## Relationship to prior work

Ryabchenko, Qian and Mou introduce the reference-vector control-variate estimator and directional-hint framework and prove adaptive upper bounds for nonconvex optimization. Their published algorithm uses a forward one-sided finite difference; their theorems also assume globally bounded gradients. The theorem here concerns a **distinct centered-probe quadratic specialization**, derives an exact block second-moment matrix and global constant-step mean-square rate, and identifies the sharp calibration window and transient failure of one-step improvement. It does not claim novelty for the control-variate estimator, Gaussian fourth moments, or Perron–Frobenius theory.

Cheng, Wu and Zhu study prior-guided randomized derivative-free search through a biased, different estimator; Maheswaranathan and collaborators likewise analyze covariance-guided evolutionary strategies. General Gaussian derivative-free and stochastic subspace-descent estimates do not by themselves give the exact two-block calibrated control-variate transient and long-run phase diagram recorded here. Prior coverage cannot be excluded categorically, especially in classical mean-square stochastic adaptive-filtering literature.

## Limitations

This is an exact-arithmetic, isotropic quadratic result with a fixed orthogonal hint projector, fixed calibration multiplier, one independent isotropic Gaussian probe per update and centered function differences. It is not a guarantee for noisy function queries, nonquadratic objectives, changing hint spaces, finite-precision implementations, or the adaptive algorithm of the motivating article. It measures expected squared error, not pathwise convergence or total function-query complexity. The worst-initial-state asymptotic rate and the finite-time constants are different performance criteria. The reference vector must be available or computed, at a possibly nontrivial cost. No independent mathematical audit has yet been performed.

## References

1. A. Ryabchenko, J. Qian, W. Mou, *Adaptively Incorporating Directional Hints into Zeroth-Order Optimization*, arXiv:2609.08277v1 (8 September 2026), https://arxiv.org/html/2609.08277v1.
2. S. Cheng, G. Wu, J. Zhu, *On the Convergence of Prior-Guided Zeroth-Order Optimization Algorithms*, NeurIPS 34 (2021), https://arxiv.org/abs/2107.10110.
3. N. Maheswaranathan et al., *Guided Evolutionary Strategies: Augmenting Random Search with Surrogate Gradients*, ICML/PMLR 97 (2019), https://proceedings.mlr.press/v97/maheswaranathan19a.html.
4. H. Ye, *High-Probability Last-Iterate Guarantees for Two-Point Gaussian Zeroth-Order Stochastic Gradient Descent*, arXiv:2606.20446 (2026), https://arxiv.org/abs/2606.20446.
