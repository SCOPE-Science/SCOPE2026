# Covariance twins and fourth-cumulant identification in a randomly switched harmonic trap

## Finding

A stationary Brownian particle whose harmonic trap switches off and on at symmetric Poisson rate \(q>0\) has a **two-to-one inverse map** from its complete position autocovariance to the physical rates. With trapping relaxation rate \(k>0\) and Brownian diffusivity \(D>0\), the exact involution
\[
(q,k,D)\longmapsto (k/2,2q,D)
\]
leaves \(C(t)=\mathbb E[X_0X_t]\) unchanged for **every** \(t\geq0\). The map fixes a parameter triple only when \(k=2q\); otherwise it gives the only distinct parameter triple with the same complete autocovariance. Equivalently, it leaves the full stationary position power spectrum unchanged.

The stationary fourth cumulant separates every nontrivial covariance twin:
\[
\kappa_4=\operatorname{cum}_4(X_0)
=D^2\left(\frac{9}{q^2}+\frac6{qk}\right),\qquad
\kappa_4(q,k,D)-\kappa_4(k/2,2q,D)
=9D^2\left(\frac1{q^2}-\frac4{k^2}\right).
\]
Consequently, the complete autocovariance together with this one stationary fourth cumulant **identifies all three model parameters uniquely**. The fourth-moment identity itself follows from previously published stationary-moment formulas; the new statement is the exact covariance ambiguity, its complete inverse-fiber classification, and its resolution by a higher-order statistic.

## Assumptions and scope

Let \(S_t\in\{0,1\}\) be an autonomous stationary continuous-time Markov chain that changes state at rate \(q>0\) in either direction. Independently, let \(W_t\) be standard Brownian motion. Define the stationary solution of
\[
 dX_t=-kS_tX_t\,dt+\sqrt{2D}\,dW_t,
 \qquad q,k,D>0.
\]
The state \(S=0\) is untrapped diffusion; \(S=1\) is an Ornstein--Uhlenbeck trap of relaxation rate \(k\). The observable is position alone, not the hidden switching state. The position is centered, its stationary moments of every fixed even order are finite, and its covariance is an even function of lag. All stated right derivatives refer to \(t\downarrow0\) from positive lag.

Set \(L=k+2q\) and \(P=kq\). Then
\[
 C(0)=D\left(\frac2k+\frac1q\right)=\frac{DL}{P},\qquad
 C'(0+)=-D,
\]
\[
 C''(t)+LC'(t)+PC(t)=0\qquad(t>0).
\]
The two positive relaxation exponents are
\[
 \lambda_{\pm}=\frac{L\pm\sqrt{L^2-4P}}2
 =\frac{k+2q\pm\sqrt{k^2+4q^2}}2.
\]
In particular,
\[
 C(t)=\frac{D}{P(\lambda_+-\lambda_-)}
 \left[\lambda_+^2e^{-\lambda_-t}-\lambda_-^2e^{-\lambda_+t}\right].
\]
The corresponding two-sided stationary spectral density, defined as \(S_X(\omega)=\int_{-\infty}^{\infty} e^{-i\omega t}C(t)\,dt\), is
\[
 S_X(\omega)=\frac{2D(\omega^2+L^2-P)}{(P-\omega^2)^2+L^2\omega^2}.
\]

## Proof

**1. Stationarity and moments.** The stationary causal representation is
\[
 X_t=\sqrt{2D}\int_{-\infty}^t
 \exp\!\left(-k\int_u^t S_a\,da\right)dW_u.
\]
Its existence and uniqueness follow because the two-state Feynman--Kac generator with a positive killing rate in state \(1\) has strictly negative spectral bound. Repeating the generator argument below yields finite moments of every fixed order.

Write \(m_{j,s}=\mathbb E[X_0^j\mathbf1_{\{S_0=s\}}]\) for the unnormalized stationary moments. In particular, \(m_{0,0}=m_{0,1}=1/2\). Stationary generator equations at order two give
\[
 0=-q m_{2,0}+q m_{2,1}+D,\quad
 0=q m_{2,0}-(q+2k)m_{2,1}+D.
\]
Hence
\[
 m_{2,1}=D/k,\qquad m_{2,0}=D/k+D/q,
\]
which proves the variance formula.

**2. All-lag covariance.** Let
\[
 Q=\begin{pmatrix}-q&q\\q&-q\end{pmatrix},\qquad
 K=\begin{pmatrix}0&0\\0&k\end{pmatrix}.
\]
Future Brownian increments have zero conditional mean, so the conditional propagation of the initial position is governed by \(Q-K\). With \(m=(m_{2,0},m_{2,1})^\top\),
\[
 C(t)=m^\top e^{(Q-K)t}\begin{pmatrix}1\\1\end{pmatrix}.
\]
The characteristic polynomial of \(Q-K\) is \(z^2+Lz+P\). Cayley--Hamilton gives the displayed second-order ODE. The first derivative is \(C'(0+)=-k m_{2,1}=-D\), which completes the unique initial-value solution and the explicit two-exponential representation. The discriminant \(k^2+4q^2\) is positive and both exponential coefficients are nonzero, so no spectral pole is spurious. Fourier transforming gives the spectral density formula.

**3. Complete inverse classification.** The entire covariance depends only on \((D,L,P)\). These three quantities are uniquely recoverable from that covariance, since the ODE and stationarity imply
\[
 C''(0+)=0,\quad C'''(0+)=DP,\quad C^{(4)}(0+)=-DPL.
\]
Thus
\[
 D=-C'(0+),\quad P=C'''(0+)/D,\quad
 L=-C^{(4)}(0+)/C'''(0+).
\]
Now \(k\) and \(2q\) are precisely the two positive roots of \(z^2-Lz+2P=0\). Hence the unordered pair \(\{k,2q\}\) is identifiable, and its two possible assignments give exactly the original triple and its involutive twin. They coincide exactly when \(k=2q\). No other positive parameter triple yields the same covariance.

**4. Fourth-cumulant separation and reconstruction.** At moment order four the stationary generator gives
\[
 4k m_{4,1}=12D(m_{2,0}+m_{2,1}),\qquad
 q(m_{4,0}-m_{4,1})=12D m_{2,0}.
\]
Solving yields
\[
 \mathbb E[X_0^4]=D^2\left(\frac{12}{k^2}+\frac{18}{qk}+\frac{12}{q^2}\right),
\]
and subtracting three times the squared variance gives the stated fourth cumulant. Its twin difference vanishes only on the self-dual line \(k=2q\), proving separation elsewhere. Indeed, with the quantities \(D,P\) recovered from the covariance, the positive-parameter inverse is explicitly
\[
 q=\frac{3D}{\sqrt{\kappa_4-6D^2/P}},\qquad k=P/q.
\]
The radicand is positive for every admitted parameter triple. This proves exact identification by covariance plus fourth cumulant.

## Verification

The accompanying `verify_dual.py` independently constructs the two-state stationary moment generators and propagates the covariance with a matrix exponential. Symbolic equalities verify both moments, four right derivatives, and the involution's fourth-cumulant separation. Across 50 seeded positive parameter triples, five lag choices per triple, it also checks analytic covariance, matrix exponential, twin equality, spectral-parameter inversion, and cumulant reconstruction. The script executed successfully with 1,300 counted numerical comparisons and the symbolic checks. For illustration, \((q,k,D)=(1,1,1)\) and \((1/2,2,1)\) both have \(C(0)=3\) and exactly the same \(C(t)\), but their fourth cumulants are respectively \(15\) and \(42\). The proof, not the finite numerical tests, establishes the continuum statement.

## Relationship to prior work

Santra, Das and Nath (2021), arXiv:2104.00609, introduced and analyzed this intermittently trapped Brownian model, including transient positional variance, stationary variance and selected stationary distributions. Frydel (2024), arXiv:2407.12213, obtained the stationary even-moment recurrence and evaluated the second and fourth moments; those marginal formulas are **prior knowledge**, not a claimed new contribution. Huang et al., arXiv:1412.7952, gave covariance matrix-exponential methods for the broader class of Markov-modulated Ornstein--Uhlenbeck processes. Their forward framework covers the present dynamical generator, but does not state an inverse-fiber classification or this involutive pair of indistinguishable trapping protocols. Frydel (2026), arXiv:2607.05173, generalizes fluctuating traps to semi-Markovian switching; its analysis of stationary spatial moments does not state the present covariance-inversion duality. The assessed new theorem is the exact **two-to-one inverse covariance map** and its rigorous higher-moment resolution, not the existence of a forward covariance or stationary-moment formula.

## Limitations

This theorem assumes symmetric exponential switching, an exactly untrapped off state, additive independent Brownian noise, and an ideal stationary position covariance at all nonnegative lags. It does not assert that finite noisy time series allow stable recovery of high right derivatives or of a fourth cumulant. It does not imply equality of full joint two-time distributions, nonlinear response, higher moments, or hidden-state trajectories for a covariance-twin pair. General asymmetric switching and semi-Markov waiting-time laws are not covered. General Markov-modulated covariance machinery is substantial prior knowledge; the novelty assessment concerns the newly evaluated inverse ambiguity rather than the already available forward expressions.

## References

1. I. Santra, S. Das, S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609, first posted 2021-04-01; https://arxiv.org/abs/2104.00609 .
2. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213, first posted 2024-07-16; https://arxiv.org/abs/2407.12213 .
3. G. Huang, H. Jansen, M. Mandjes, P. Spreij and K. De Turck, *Markov-modulated Ornstein-Uhlenbeck processes*, arXiv:1412.7952, preprint 2014; https://arxiv.org/abs/1412.7952 .
4. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173, first posted 2026-07-06; https://arxiv.org/abs/2607.05173 .
