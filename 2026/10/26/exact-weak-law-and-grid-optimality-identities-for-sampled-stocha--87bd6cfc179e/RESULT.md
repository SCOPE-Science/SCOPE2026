# Exact weak-law and grid-optimality identities for sampled stochastic volatility

## Finding

For \(T>0\), let \(0=t_0<\cdots<t_N=T\) be a partition with widths \(h_i=t_{i+1}-t_i>0\). Let \(A_i\) be independent identically distributed real random variables, independent of a Brownian motion \(W\), and put \(Z=A^2\), \(q=\mathbb E Z<\infty\). On interval \([t_i,t_{i+1})\), define the sampled process by \(dX_t^\pi=A_i\,dW_t\), and define the aggregated process by \(d\widetilde X_t=\sqrt q\,dW_t\); both start at zero.

Writing \(\ell(s)=\mathbb E[e^{-sZ}]\), the terminal characteristic functions satisfy

\[
\mathbb E[e^{iuX_T^\pi}]=\prod_{i=0}^{N-1}\ell\!\left(\frac{u^2h_i}{2}\right),\qquad
\mathbb E[e^{iu\widetilde X_T}]=e^{-u^2qT/2}.
\]

For every \(u\ne0\), the sampled characteristic function is strictly larger than the aggregated one if and only if \(Z\) is nonconstant. The entire process laws coincide if and only if \(A^2\) is almost surely constant; this can happen even when the two processes, coupled to the same Brownian path, have nonzero strong error. For fixed \(N\) and \(T\), the uniform partition uniquely minimizes the characteristic-function excess at every nonzero frequency whenever \(Z\) is nonconstant.

If \(\mathbb E[A^4]<\infty\), the exact fourth-moment excess is

\[
\mathbb E[(X_T^\pi)^4]-\mathbb E[\widetilde X_T^4]
=3\operatorname{Var}(A^2)\sum_{i=0}^{N-1}h_i^2.
\]

It is uniquely minimized by the uniform partition, where it equals \(3T^2\operatorname{Var}(A^2)/N\) when \(\operatorname{Var}(A^2)>0\). For each integer \(k\ge1\) with \(\mathbb E|A|^{2k}<\infty\), every terminal even moment of order \(2k\) is also minimized by the uniform partition.

There is also an explicit leading weak-bias coefficient. Assume \(q>0\), \(\mathbb E Z^3<\infty\), and \(f\in C_b^6(\mathbb R)\), meaning that \(f\) and its derivatives through order six are bounded and continuous. Then

\[
\mathbb E[f(X_T^\pi)]-\mathbb E[f(\widetilde X_T)]
=\frac{\operatorname{Var}(Z)}8\left(\sum_{i=0}^{N-1}h_i^2\right)
\mathbb E[f^{(4)}(\widetilde X_T)]+R_\pi,
\]

with the explicit remainder bound

\[
|R_\pi|\le\frac{\|f^{(6)}\|_\infty}{48}
\mathbb E\left|\sum_{i=0}^{N-1}h_i(Z_i-q)\right|^3.
\]

For a uniform partition and a finite third absolute moment of \(Z-q\), the remainder is \(O(N^{-3/2})\). Thus the first weak-error coefficient is known exactly in this model, rather than only bounded by a generic order estimate.

## Assumptions and scope

The theorem concerns a one-dimensional, state-independent, zero-drift controlled-volatility model with scalar volatility \(\sigma(a)=a\). The action is drawn independently at each grid point, remains fixed on the next interval, and is independent of the environmental Brownian motion. The aggregated comparison uses the diffusion coefficient \(\sqrt{\mathbb E[A^2]}\). No assertion is made for state-dependent policies, controlled drift, jumps, vector-valued systems, or general value functions.

The exact characteristic-function formula needs only \(\mathbb E[A^2]<\infty\). The fourth-moment identity needs \(\mathbb E[A^4]<\infty\). The smooth-payoff expansion additionally needs \(\mathbb E[Z^3]<\infty\) and the stated bounded derivatives. The uniform-grid conclusion is limited to the characteristic-function excess and even moments; it is not a stochastic-order claim for every payoff.

## Proof

### Conditional Gaussian representation

Set \(Z_i=A_i^2\) and \(V_\pi=\sum_i h_iZ_i\). Conditional on the actions, the increments \(A_i(W_{t_{i+1}}-W_{t_i})\) are independent centered Gaussians with variances \(h_iZ_i\). Hence \(X_T^\pi\mid(A_0,\ldots,A_{N-1})\) is centered Gaussian with variance \(V_\pi\), and

\[
\mathbb E[e^{iuX_T^\pi}]=\mathbb E[e^{-u^2V_\pi/2}]
=\prod_i\mathbb E[e^{-u^2h_iZ/2}].
\]

The aggregated terminal state is Gaussian with variance \(qT\), giving the second displayed characteristic function. Since \(z\mapsto e^{-sz}\) is strictly convex for \(s>0\), Jensen's inequality gives \(\ell(s)\ge e^{-sq}\), with equality for \(s>0\) exactly when \(Z\) is almost surely constant. Multiplying the interval inequalities proves the strict characteristic-function comparison.

Conditional on the action sequence, the whole sampled path is Gaussian with covariance \(\int_0^{s\wedge t}Z_{\delta(r)}\,dr\). If \(Z\) is constant, this covariance is deterministically \(q\min(s,t)\), so the process law equals that of \(\sqrt q W\). Conversely, if \(Z\) is nonconstant, the strict terminal characteristic-function comparison at any nonzero frequency prevents equality of process laws.

### Uniform-grid optimality

For \(s>0\), the function \(g(s)=\log\ell(s)\) is strictly convex when \(Z\) is nonconstant: its second derivative is the variance of \(Z\) under the exponentially tilted probability law proportional to \(e^{-sZ}\,d\mathbb P\), and that variance is positive. For \(c=u^2/2>0\), Jensen's inequality therefore gives

\[
\sum_{i=0}^{N-1}g(ch_i)\ge N g(cT/N),
\]

with equality only when all widths are equal. Exponentiating proves that the uniform partition uniquely minimizes the characteristic function at every nonzero frequency. The aggregated characteristic function is independent of the partition, so the same ordering holds for the excess.

### Moment identities and even-moment minimization

The conditional Gaussian fourth moment is \(3V_\pi^2\). Independence of the \(Z_i\) yields

\[
\mathbb E[V_\pi^2]=q^2T^2+\operatorname{Var}(Z)\sum_i h_i^2,
\]

which proves the exact fourth-moment identity. Cauchy--Schwarz gives \(\sum_i h_i^2\ge T^2/N\), with equality only on the uniform grid.

More generally, for every integer \(k\ge1\) with finite \(k\)-th moment of \(Z\),

\[
\mathbb E[(X_T^\pi)^{2k}]=(2k-1)!!\,\mathbb E\left[\left(\sum_i h_iZ_i\right)^k\right].
\]

The right-hand side is a symmetric convex function of the width vector: it is an expectation of the convex function \(x\mapsto x^k\) applied to a nonnegative linear form, and the \(Z_i\) are identically distributed. Symmetric convex functions are Schur-convex. The equal-width vector is majorized by every positive width vector with the same sum, so it minimizes every such even moment.

### Weak-bias expansion

Let \(G\sim N(0,1)\) and define \(H(v)=\mathbb E[f(\sqrt vG)]\) for \(v\ge0\). The heat-semigroup derivative identities give \(H''(v)=\frac14\mathbb E[f^{(4)}(\sqrt vG)]\) and \(\|H'''\|_\infty\le\|f^{(6)}\|_\infty/8\). Since \(\mathbb E V_\pi=qT\) and \(\operatorname{Var}(V_\pi)=\operatorname{Var}(Z)\sum_i h_i^2\), Taylor's theorem around \(qT\), followed by expectation, gives the stated leading term; the linear term vanishes. The third-order Taylor remainder is at most \(\|f^{(6)}\|_\infty\mathbb E|V_\pi-qT|^3/48\). For a uniform partition, \(V_\pi-qT=(T/N)\sum_i(Z_i-q)\); the standard third-moment bound for sums of independent centered variables gives the stated \(O(N^{-3/2})\) remainder.

### Gaussian-policy benchmark

For \(A\sim N(0,1)\), \(\ell(s)=(1+2s)^{-1/2}\), so a uniform grid has characteristic function \((1+u^2T/N)^{-N/2}\), compared with \(e^{-u^2T/2}\) for the aggregated process. Moreover,

\[
\mathbb E[(X_T^\pi)^{2k}]=(2k-1)!!\,T^k\prod_{j=0}^{k-1}\left(1+\frac{2j}{N}\right),
\]

and the fourth-moment excess is exactly \(6T^2/N\). This supplies a closed-form benchmark for the standard-Gaussian controlled-volatility illustration used in the sampled-policy literature.

## Verification

The included `verify.py` checks the characteristic-function inequality and uniform-grid ordering at several frequencies, the exact fourth-moment identity, the finite-distribution even-moment ordering for orders two through ten, the constant-magnitude equality case, and the Gaussian specialization. These checks are deterministic consistency tests; the general claims are proved above, not inferred from numerical sampling.

## Relationship to prior work

Jia, Ouyang, and Zhang establish weak convergence rates for discretely sampled stochastic policies and explicitly exhibit failure of strong convergence when volatility is controlled. Their numerical illustration uses a standard Gaussian policy and estimates a fourth-moment difference by Monte Carlo. The present result is narrower in its model assumptions but gives an exact terminal law, an exact grid-optimality statement, and a leading weak-bias coefficient for smooth terminal tests in the state-independent controlled-volatility case.

Bender and Nguyen Tran Thuan develop a general grid-sampling limit SDE for randomized policies with controlled diffusion and jumps. That work supplies a broader limiting framework, not the finite-grid characteristic-function identity or the explicit partition-dependent fourth-moment excess proved here. Szpruch, Treetanthiploet, and Zhang analyze Gaussian-policy execution in linear-quadratic reinforcement learning with deterministic uncontrolled diffusion; their discussion identifies controlled diffusion as a separate case.

The classical conditional-Gaussian and majorization viewpoints are equivalent formulations of parts of the proof and are not claimed as new abstract principles. The specific value here is the exact quantitative specialization to sampled controlled volatility, including the weak-law equality criterion and the error coefficient for the test functions used in the motivating numerical example.

## Limitations

This is not a convergence theorem for general controlled diffusions. It does not imply a pathwise error rate when volatility is randomized, does not rank arbitrary terminal payoffs, and does not address feedback-dependent actions, nonzero drift, jumps, or finite-precision effects. The literature comparison was bounded to the sources listed below and semantic searches; it cannot establish global priority or rule out an equivalent result in uninspected literature.

## References

1. Y. Jia, D. Ouyang, and Y. Zhang, *Accuracy of Discretely Sampled Stochastic Policies in Continuous-time Reinforcement Learning*, arXiv:2503.09981v1, first submitted 2025-03-13; see §§4.1.1, 4.3 (Example 4.7), and 4.4.
2. C. Bender and N. Tran Thuan, *A random measure approach to reinforcement learning in continuous time*, arXiv:2409.17200v1, first submitted 2024-09-25; see §§2.1–2.4 and Example 2.13.
3. L. Szpruch, T. Treetanthiploet, and Y. Zhang, *Optimal scheduling of entropy regulariser for continuous-time linear-quadratic reinforcement learning*, arXiv:2208.04466v3; first submitted 2022-08-08; see §§2.1, 2.3, and 2.5.
