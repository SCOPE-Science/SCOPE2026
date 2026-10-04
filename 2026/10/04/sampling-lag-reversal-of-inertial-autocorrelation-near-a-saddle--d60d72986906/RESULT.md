# Sampling-lag reversal of inertial autocorrelation near a saddle node
## Finding
Consider the stationary Ornstein--Uhlenbeck linearization of a damped second-order saddle-node model,
\[
dX_t=V_t\,dt,\qquad dV_t=(-\alpha X_t-\eta V_t)\,dt+\sigma\,dW_t,
\]
with \(\alpha>0\) and \(\eta>0\). Compare its normalized position autocorrelation \(R_2(\Delta)\) at lag \(\Delta>0\) with the variance-matched first-order comparator used by Ditlevsen and Ditlevsen. Their matching rescales the one-dimensional curvature and noise so that the first-order drift rate is \(\alpha/\eta\); hence
\[
R_1(\Delta)=e^{-\alpha\Delta/\eta}.
\]
Then the second-order autocorrelation does **not** dominate \(R_1\) uniformly in lag.

If \(0<\alpha<\eta^2/4\), there is a unique positive crossover \(\Delta_c\) such that
\[
R_2(\Delta)>R_1(\Delta)\quad(0<\Delta<\Delta_c),\qquad
R_2(\Delta_c)=R_1(\Delta_c),\qquad
R_2(\Delta)<R_1(\Delta)\quad(\Delta>\Delta_c).
\]
At \(\alpha=\eta^2/4\), the same trichotomy holds; with \(s_c=\eta\Delta_c\), the crossover is the unique positive root of
\[
e^{-s_c/4}(1+s_c/2)=1,
\]
so \(s_c\approx5.0257248345\).

If \(\alpha>\eta^2/4\), set \(\omega=\sqrt{4\alpha-\eta^2}/2\). The inertial position autocorrelation has infinitely many negative lag intervals although \(R_1(\Delta)>0\) for every finite lag. In particular,
\[
R_2\left(\frac{(2m+1)\pi}{\omega}\right)
=-\exp\left(-\frac{\eta(2m+1)\pi}{2\omega}\right)<0<R_1\left(\frac{(2m+1)\pi}{\omega}\right)
\]
for every integer \(m\ge0\).

Therefore the statement in arXiv:2609.01164v1 that the autocorrelation is "always larger" for the second-order than for the first-order model cannot hold uniformly in sampling lag. Inertia boosts the sufficiently short-lag autocorrelation, but at longer lags it can suppress the first-order comparator and, in the underdamped regime, reverse the sign of the statistic.

## Assumptions and scope
The claim concerns the stationary **linearized** model at a stable equilibrium, with fixed \(\alpha>0\), \(\eta>0\), white-noise forcing in velocity, and normalized position autocorrelation. It uses exactly the variance-matched first-order comparison adopted in the motivating source: the first-order drift rate is \(\alpha/\eta\). The result is a statement about theoretical autocorrelation as a function of sampling lag. It does not claim that finite-window sample autocorrelation has the same ordering, and it does not replace the nonlinear analysis near noise-induced escape.

## Proof
For \(0<\alpha<\eta^2/4\), let
\[
d=\sqrt{\eta^2-4\alpha},\qquad r_-=\frac{\eta-d}{2},\qquad r_+=\frac{\eta+d}{2}.
\]
Both \(r_-\) and \(r_+\) are positive, \(r_-r_+=\alpha\), and \(r_-+r_+=\eta\). The normalized position autocorrelation obtained from the matrix exponential is
\[
R_2(\Delta)=\frac{r_+e^{-r_-\Delta}-r_-e^{-r_+\Delta}}{r_+-r_-}.
\]
Put \(q=\alpha/\eta=r_-r_+/(r_-+r_+)\). The sign of \(R_2/R_1-1\) is the sign of
\[
F(\Delta)=r_+e^{-(r_--q)\Delta}-r_-e^{-(r_+-q)\Delta}-(r_+-r_-).
\]
Since
\[
r_--q=\frac{r_-^2}{\eta},\qquad r_+-q=\frac{r_+^2}{\eta},
\]
one obtains
\[
F'(\Delta)=\frac{r_-r_+}{\eta}
\left(r_+e^{-r_+^2\Delta/\eta}-r_-e^{-r_-^2\Delta/\eta}\right).
\]
The bracket vanishes exactly once, at
\[
\Delta_*=\frac{\log(r_+/r_-)}{r_+-r_-}.
\]
Thus \(F\) increases on \((0,\Delta_*)\) and decreases thereafter. Also \(F(0)=0\), \(F'(0)>0\), and \(F(\Delta)\to-(r_+-r_-)<0\) as \(\Delta\to\infty\). Therefore \(F\) has exactly one positive zero \(\Delta_c\), proving the overdamped trichotomy.

At critical damping \(\alpha=\eta^2/4\), the repeated-root limit gives
\[
R_2(\Delta)=e^{-\eta\Delta/2}\left(1+\frac{\eta\Delta}{2}\right),\qquad
R_1(\Delta)=e^{-\eta\Delta/4}.
\]
With \(s=\eta\Delta\), the logarithm of the ratio is
\[
H(s)=\log(1+s/2)-s/4.
\]
Here \(H(0)=0\) and \(H'(s)=1/(s+2)-1/4\), so \(H\) rises until \(s=2\), then decreases strictly to \(-\infty\). Hence it has exactly one positive zero. Numerical evaluation of this scalar equation gives \(s_c\approx5.0257248345\).

For \(\alpha>\eta^2/4\), define \(\omega=\sqrt{4\alpha-\eta^2}/2\). The matrix exponential gives
\[
R_2(\Delta)=e^{-\eta\Delta/2}
\left[\cos(\omega\Delta)+\frac{\eta}{2\omega}\sin(\omega\Delta)\right].
\]
At \(\Delta_m=(2m+1)\pi/\omega\), the sine term vanishes and the cosine equals \(-1\), proving the displayed strict reversal. More generally, if \(\phi=\arctan(\eta/(2\omega))\), the bracket is a positive multiple of \(\cos(\omega\Delta-\phi)\), so it is negative on the infinitely many intervals
\[
\frac{\phi+\pi/2+2m\pi}{\omega}<\Delta<
\frac{\phi+3\pi/2+2m\pi}{\omega},\qquad m=0,1,2,\ldots.
\]
Finally, \(R_2'(0)=0\) whereas \(R_1'(0)=-\alpha/\eta<0\), so the inertial correlation is indeed larger for all sufficiently small positive lags. The reversal is therefore a genuine sampling-lag effect rather than a mismatch at the origin.

## Verification
The derivation uses only the exact matrix-exponential autocorrelation of the stationary linearized system and elementary one-variable calculus. The overdamped comparison was reduced to a function whose derivative has exactly one zero; the critical case was reduced to a scalar log-ratio with one turning point; and the underdamped reversal is certified at exact odd half-period lags. No finite enumeration or simulation is used as proof.

The motivating source explicitly writes the underdamped and overdamped matrix exponentials, uses the variance-matched first-order scaling, and then states that the second-order autocorrelation is always larger. Those are the precise premises used here. Classical CAR(2) literature already treats stochastic damped-oscillator autocorrelation, so the formula itself is not claimed as new; the new point is the exact comparison and crossover classification against the source's first-order comparator.

## Relationship to prior work
Ditlevsen and Ditlevsen derive the same second-order linearization and its lagged autocorrelation, then state that the second-order autocorrelation is always larger than that of the first-order model. Their discussion also notes that damping may obscure autocorrelation-based warning signals, but it does not give a lag-domain correction to the universal comparison. The result above supplies that correction: in the overdamped regime the comparison changes sign exactly once, while in the underdamped regime the second-order autocorrelation has negative lobes.

Koen's study of stochastic damped oscillations treats the same second-order continuous-time autoregressive mechanism and its autocovariance/autocorrelation structure, including the importance of sampling in the time domain. That literature supplies background for oscillatory correlations but does not compare the source's variance-matched first- and second-order saddle-node models or state the crossover theorem proved here. The 2024 multidimensional early-warning literature addresses interference from additional noisy directions rather than this inertia-versus-sampling-lag comparison.

## Limitations
The result is local to the linearized stationary dynamics. It does not assert an ordering for nonlinear finite-amplitude trajectories, for sample autocorrelation estimators in short windows, or after noise-induced escape. In the underdamped regime the finding concerns fixed-lag autocorrelation, not an integrated correlation time. The originality assessment cannot exclude an equivalent comparison hidden in unindexed time-series literature, although the classical oscillator formulas themselves are explicitly treated as prior art rather than novelty.

## References
1. S. Ditlevsen and P. Ditlevsen, "Early Warning Signals Can Vanish or Amplify: Dimensionality in Complex Systems," arXiv:2609.01164v1, 2026.
2. C. Koen, "Estimation of the coherence time of stochastic oscillations from modest samples," Monthly Notices of the Royal Astronomical Society 419 (2012), 1197--1218, DOI: 10.1111/j.1365-2966.2011.19778.x.
3. L. Morr, P. Boers, and collaborators, "Internal Noise Interference to Warnings of Tipping Points in Generic Multidimensional Dynamical Systems," SIAM Journal on Applied Dynamical Systems, DOI: 10.1137/24M1669104.
