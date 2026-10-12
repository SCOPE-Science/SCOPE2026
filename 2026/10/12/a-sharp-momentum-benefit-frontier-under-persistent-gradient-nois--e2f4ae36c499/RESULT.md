# A sharp momentum-benefit frontier under persistent gradient noise

## Finding
For scalar stochastic heavy-ball optimization on a strictly convex quadratic with independent stationary first-order autoregressive (AR(1)) gradient noise of nonnegative persistence, there is an **exact and complete phase diagram** for whether adding positive momentum reduces the limiting squared error relative to plain stochastic gradient descent (SGD), at the same fixed stepsize. Let \(t=\eta a\in(0,2)\) be the normalized stepsize and \(r\in[0,1)\) the noise autocorrelation. Define
\[
\tau(r)=\begin{cases}
1,&r=0,\\
\displaystyle\frac{\sqrt{(1-r)^2+4r(1+r)}-(1-r)}{2r},&0<r<1.
\end{cases}
\]
When \(0<t\le\tau(r)\), **every** positive momentum \(0<\beta<1\) strictly *increases* stationary squared error. When \(\tau(r)<t<2\), there is a **unique** crossover \(\beta_c(t,r)\in(0,1)\) such that precisely \(0<\beta<\beta_c(t,r)\) strictly *decreases* stationary squared error; equality with plain SGD occurs at \(\beta=\beta_c(t,r)\), and every \(\beta_c(t,r)<\beta<1\) increases it. The threshold \(\tau\) increases strictly from \(1\) to the limiting value \(\sqrt2\) as temporal persistence increases from \(0\) to \(1\).

The explicit crossover solves \(Q_{t,r}(\beta_c)=0\) uniquely in \((0,1)\), where
\[
Q_{t,r}(\beta)=r[1+r(1-t)]\beta^2
 +[r^2(t-1)^2-rt-1]\beta
 +rt^2-rt-r+t-1.
\]
For \(r>0\), write \(A=r[1+r(1-t)]\), \(B=r^2(t-1)^2-rt-1\), and \(C=rt^2-rt-r+t-1\); then
\[
\beta_c(t,r)=\frac{-B-\sqrt{B^2-4AC}}{2A}.
\]
The uncorrelated boundary \(r=0\) reduces to \(\beta_c(t,0)=t-1\) when \(1<t<2\); its covariance formula is established prior work and is not the novelty claimed here.

## Assumptions and scope
Fix \(a>0\), \(\eta>0\) with \(0<t=\eta a<2\), and \(0\le\beta<1\). Consider the scalar quadratic \(f(x)=a x^2/2\) with optimizer at zero and iteration
\[
x_{k+1}=x_k-\eta(a x_k+\xi_k)+\beta(x_k-x_{k-1}),\qquad k\ge0.
\]
The additive gradient noise is independent of the iterates' initialization and obeys \(\xi_{k+1}=r\xi_k+\varepsilon_{k+1}\), where \(0\le r<1\), the innovations are independent, identically distributed with mean zero and finite variance \(\sigma^2>0\), and \(\xi_0\) has the stationary centered AR(1) law. Initial iterates \(x_{-1},x_0\) are arbitrary deterministic reals; no Gaussian distribution is assumed. All comparisons hold for every such initialization because the limiting variance is unique. Only the stationary limiting second moment is optimized, not transient error, convergence rate, or a joint choice of stepsize and momentum.

## Proof
**1. Stability and existence of the limiting covariance.** Put \(z_k=a x_k\), \(b=\beta\), and \(A_0=1-t+b\). Then
\[
z_{k+1}=A_0z_k-bz_{k-1}-t\xi_k.
\]
The homogeneous characteristic polynomial is \(\lambda^2-A_0\lambda+b\). The strict degree-two Schur conditions reduce to \(b<1\), \(t>0\), and \(t<2(1+b)\), all satisfied on the stated domain. The driving AR(1) root also has modulus below one. Thus the augmented three-state system has spectral radius below one, possesses a unique stationary second-moment matrix, and converges to it from every deterministic iterate initialization. Its centered stationary mean vanishes, so \(\lim_{k\to\infty}\mathbb E[x_k^2]\) equals the stationary variance.

**2. Exact moment identities.** Set \(H=\mathbb E[\xi_k^2]=\sigma^2/(1-r^2)\) and
\[
D_b=1-r+r t-br(1-r)>0,\qquad D_0=1-r+rt>0.
\]
Let \(W=\mathbb E[z_k\xi_k]\), \(V=\mathbb E[z_k^2]\), and \(J=\mathbb E[z_kz_{k-1}]\) denote stationary moments. Independence of each new innovation gives
\[
W=r(A_0W-brW-tH),\qquad W=-\frac{rtH}{D_b},
\]
where stationarity also yields \(\mathbb E[z_{k-1}\xi_k]=rW\). Multiplying the iteration by the previous iterate gives
\[
J=\frac{A_0V-tW}{1+b}.
\]
Squaring the iteration and inserting these identities gives
\[
\frac{t(1-b)[2(1+b)-t]}{1+b}V
=t^2H+2tW\left(-\frac{A_0}{1+b}+br\right).
\]
Consequently the exact limiting iterate variance \(\mathcal V_b=V/a^2\) is
\[
\mathcal V_b=\frac{t\sigma^2}{a^2(1-r^2)(1-b)[2(1+b)-t]}
\left[1+b+\frac{2r[A_0-br(1+b)]}{D_b}\right].
\tag{1}
\]
Every denominator in this expression is strictly positive on the stated domain. This formula specializes to the familiar uncorrelated-noise covariance at \(r=0\).

**3. Exact signed comparison.** Subtracting equation (1) at \(b=0\) from equation (1) at arbitrary \(b\) and factoring yields
\[
\mathcal V_b-\mathcal V_0
=-\frac{2bt\sigma^2 Q_{t,r}(b)}
{a^2(1-b)(1+r)(2-t)[2(1+b)-t]D_0D_b}.
\tag{2}
\]
The denominator is strictly positive for \(0\le b<1\), \(0<t<2\), and \(0\le r<1\), so for \(b>0\) variance improvement is equivalent **exactly** to \(Q_{t,r}(b)>0\).

**4. Classification of all momentum values.** Write \(Q_{t,r}(b)=A b^2+B b+C\), with the coefficients displayed under Finding. On the stated domain,
\[
A\ge0,\qquad B<0,\qquad
Q_{t,r}(1)=(1+r)(t-2)(1-r+rt)<0.
\]
Indeed \(1+r(1-t)>1-r>0\), and \(r^2(t-1)^2<1\) unless \(r=0\), where \(B=-1\). A convex polynomial lies below the chord joining its endpoint values. Hence when \(C=Q(0)\le0\), it is strictly negative at every \(0<b<1\). When \(C>0\), the opposite signs \(Q(0)>0\) and \(Q(1)<0\), together with convexity (or strict linear decrease when \(r=0\)), imply exactly one crossing inside \((0,1)\): a second crossing there would force \(Q(1)>0\). This proves all three stated strict comparison regimes and uniqueness of the crossover, including equality cases.

**5. Location and monotonicity of the phase frontier.** The constant coefficient has the form
\[
C=rt^2+(1-r)t-(1+r).
\]
For fixed \(r\in[0,1)\) it is strictly increasing in \(t\in(0,2)\), since its derivative is \(1+r(2t-1)>1-r>0\); hence it has one zero. At \(r=0\) that zero equals \(1\). For every \(0<r<1\), \(C(1,r)=-r<0\), whereas
\[
C(\sqrt2,r)=(\sqrt2-1)(1-r)>0.
\]
Thus \(1<\tau(r)<\sqrt2\). On this interval \(\partial C/\partial r=t^2-t-1<0\), so the implicit root increases strictly with \(r\). Taking \(r\uparrow1\) in the defining polynomial gives the limiting positive root \(\sqrt2\). These facts establish the complete claimed phase diagram.

**6. Exact reversal example.** Set \(a=\sigma^2=1\), \(t=6/5\), and \(b=1/10\). If \(r=0\), the difference (2) is \(-1/30\): momentum helps. For \(r=1/2\), the same difference equals \(+446/7095\): momentum hurts. Thus temporal correlation can reverse the variance benefit with fixed curvature, step and momentum, rather than merely rescale the noise level.

## Verification
The accompanying standalone Python 3 program `checker.py` solves the six unknown entries of the stationary three-by-three Lyapunov covariance equation by exact rational Gaussian elimination. It compares the resulting variance against equation (1), verifies the signed difference (2), and checks exact sign classification over 270 rational parameter triples spanning both regimes. It also verifies the two rational reversal examples independently. Execution produces `VERIFY_OK 270 exact covariance and difference cases, 2 contrasting rational witnesses`. These finite checks are **not** substitutes for the analytic proof, which covers the full continuous parameter domain and every allowed innovation distribution of finite variance.

## Relationship to prior work
Gadat, Panloup and Saadane's 2016 stochastic-heavy-ball study establishes the historical stochastic optimization context, but treats different noise assumptions and algorithmic regimes. Liu, Ziyin and Ueda (2020 preprint, 2021 final version) derive the exact finite-learning-rate stationary covariance for SGD with momentum and **temporally uncorrelated** gradient noise; the slice \(r=0\) of equation (1) is already covered by their result. Kühn and Rosenow (2023 preprint, subsequently revised) analyze stationary weight fluctuations under **epoch-induced, finite-range negative** gradient-noise correlations. Their general linear covariance representation in Appendix B can be specialized to other stationary noise processes, but their paper does not supply the positive-AR(1) all-momentum comparison, unique sign crossover, or strictly increasing dimensionless threshold above. Dang, Babanezhad and Vaswani (2024 preprint) study stochastic-heavy-ball convergence bounds and noise-adaptive parameter schedules, not this exact fixed-stepsize stationary comparison. The classical Lyapunov identity underlying our variance calculation is acknowledged as standard; novelty is confined to the sharp global momentum-benefit classification for persistent noise.

## Limitations
The claim is an exact result for a one-dimensional quadratic with state-independent additive autoregressive gradient noise and a fixed stepsize. It does not establish the behavior of multidimensional, nonlinear, nonstationary, state-dependent, or heavy-tailed infinite-variance noise models, nor that real minibatch sampling necessarily produces a positive-AR(1) law. Temporal correlation is restricted to \(0\le r<1\). It does not optimize convergence speed or time-varying momentum schedules. Existing general covariance formulas may permit derivation of specialized related comparisons, and an equivalent specialized comparison in older filtering/control or stochastic-optimization literature cannot be ruled out solely by the cited searches.

## References
1. S. Gadat, F. Panloup, S. Saadane, *Stochastic Heavy Ball*, arXiv:1609.04228, initial public submission 2016-09-14, https://arxiv.org/abs/1609.04228 .
2. K. Liu, L. Ziyin, M. Ueda, *Noise and Fluctuation of Finite Learning Rate Stochastic Gradient Descent*, arXiv:2012.03636, initial public submission 2020-12-07, https://arxiv.org/abs/2012.03636 .
3. M. Kühn, B. Rosenow, *Anti-Correlated Noise in Epoch-Based Stochastic Gradient Descent: Implications for Weight Variances in Flat Directions*, arXiv:2306.05300, initial public submission 2023-06-08, https://arxiv.org/abs/2306.05300 .
4. A. Dang, R. Babanezhad, S. Vaswani, *(Accelerated) Noise-adaptive Stochastic Heavy-Ball Momentum*, arXiv:2401.06738, initial public submission 2024-01-12, https://arxiv.org/abs/2401.06738 .
