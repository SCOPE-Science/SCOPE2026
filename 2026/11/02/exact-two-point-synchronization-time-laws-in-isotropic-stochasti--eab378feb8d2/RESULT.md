# Exact two-point synchronization-time laws in isotropic stochastic Möbius circle flows

## Finding

An isotropic first-harmonic stochastic circle flow has a universal near-synchronization clock: shared angular forcing, common additive Brownian motion, and deterministic modulation of first-harmonic noise do not change its distribution once time is measured by accumulated first-harmonic intensity. For two initial phases with positive oriented separation \(x\in(0,2\pi)\), the first time \(S_\varepsilon\) (in this noise clock) that their lifted separation reaches \(\varepsilon\) or \(2\pi-\varepsilon\) obeys, for \(0<\varepsilon<\min\{x,2\pi-x\}\),

\[
\mathbb E S_\varepsilon=\log\frac{\sin(x/2)}{\sin(\varepsilon/2)},\qquad
\mathop{\mathrm{Var}}S_\varepsilon=2\log\frac{\sin(x/2)}{\sin(\varepsilon/2)}-\frac{(x-\varepsilon)(2\pi-\varepsilon-x)}4.
\]

The endpoint near \(2\pi\) is hit with probability \((x-\varepsilon)/(2\pi-2\varepsilon)\). In addition,
\[
\frac{S_\varepsilon}{\log(1/\varepsilon)}\longrightarrow 1\quad\text{almost surely},\qquad
\frac{S_\varepsilon-\mathbb E S_\varepsilon}{\sqrt{2\log(1/\varepsilon)}}\ \Longrightarrow\ \mathcal N(0,1)
\]
as \(\varepsilon\downarrow0\). These are statements about the first approach of either orientation to coinciding phases, not finite-time exact coalescence.

## Assumptions and scope

Let \(B^0,B^1,B^2\) be independent standard Brownian motions and \(a,d_0,d:[0,\infty)\to\mathbb R\) deterministic locally bounded functions. Assume \(a\) is continuous, \(d_0(t)\ge0\), \(d(t)>0\), the noise amplitudes \(\sqrt{d_0}\) and \(\sqrt d\) are continuously differentiable, and \(Q(t)=\int_0^t d(u)\,du\to\infty\). Consider the Stratonovich equation on the phase circle
\[
 d\varphi_t=a(t)\,dt+\sqrt{2d_0(t)}\circ dB^0_t
 +\sqrt{2d(t)}\cos(\varphi_t)\circ dB^1_t
 +\sqrt{2d(t)}\sin(\varphi_t)\circ dB^2_t.
\]
Take two solutions driven by the *same three noise realizations*, with lifts initially ordered by \(0<\varphi^2_0-\varphi^1_0=x<2\pi\). Let \(\Delta_t=\varphi^2_t-\varphi^1_t\in(0,2\pi)\). Define \(\tau_\varepsilon=\inf\{t\ge0:\Delta_t\notin(\varepsilon,2\pi-\varepsilon)\}\) and \(S_\varepsilon=Q(\tau_\varepsilon)\). All logarithms are natural. The equations are uniformly Lipschitz in phase on each finite time interval, hence produce an orientation-preserving stochastic flow; the lifted separation remains strictly between \(0\) and \(2\pi\) at every finite time. For constant \(d(t)=D>0\), physical time is exactly \(\tau_\varepsilon=S_\varepsilon/D\). For nonconstant \(d\), only noise-clock time has a universal law.

## Proof

**1. Exact autonomous gap diffusion.** Since \(d\cos\varphi\cdot(-\sin\varphi)+d\sin\varphi\cdot\cos\varphi=0\), the equal-intensity first-harmonic channels have zero net Stratonovich-to-Itô drift correction. The shared additive forcing and common angular drift cancel from the difference. The Itô gap is a continuous local martingale with quadratic variation
\[
 d[\Delta]_t=2d(t)\bigl[(\cos\varphi^2_t-\cos\varphi^1_t)^2+(\sin\varphi^2_t-\sin\varphi^1_t)^2\bigr]dt
 =8d(t)\sin^2(\Delta_t/2)\,dt.
\]
An adapted orthogonal projection of \((B^1,B^2)\) onto the unit difference vector is Brownian. The Dambis–Dubins–Schwarz time change \(s=Q(t)\), which is strictly increasing onto \([0,\infty)\), gives a diffusion \(X_s=\Delta_{Q^{-1}(s)}\) with
\[
 dX_s=\sqrt8\sin(X_s/2)\,dW_s,\qquad X_0=x,\qquad
 \mathcal L=4\sin^2(z/2)\frac{d^2}{dz^2}.
\]
Here \(\sin(X_s/2)>0\), so the Brownian normalization is unambiguous. Weak uniqueness of this scalar equation establishes universality in law of its entire stopped path and exit side.

**2. Almost-sure exit.** The bounded martingale \(X_s\) converges almost surely to \(X_\infty\in[0,2\pi]\). If the limit were in the interior with positive probability, the coefficient \(\sqrt8\sin(X_s/2)\) would eventually be bounded away from zero; the quadratic variation would then diverge, contradicting convergence of a bounded continuous martingale. Therefore \(X_\infty\in\{0,2\pi\}\) almost surely. As trajectories cannot reach either endpoint in finite time, every fixed \(\varepsilon\) is exited in finite time. Optional stopping of the bounded martingale at \(\sigma_\varepsilon=S_\varepsilon\) gives
\[
 \Pr(X_{\sigma_\varepsilon}=2\pi-\varepsilon)=\frac{x-\varepsilon}{2\pi-2\varepsilon}.
\]

**3. Mean and variance without solving a second-moment boundary-value equation.** Set \(g_\varepsilon(z)=\log[\sin(z/2)/\sin(\varepsilon/2)]\). Direct differentiation gives \(\mathcal Lg_\varepsilon=-1\), and Itô's formula, up to the exit, is
\[
 dg_\varepsilon(X_s)=-ds+\sqrt2\cos(X_s/2)\,dW_s.
\]
The function is bounded and nonnegative on the stopped compact interval and vanishes at either exit endpoint. Apply optional stopping at \(s\wedge\sigma_\varepsilon\), use boundedness, and let \(s\uparrow\infty\). This proves \(\mathbb E\sigma_\varepsilon=g_\varepsilon(x)<\infty\), and the square-integrable martingale representation
\[
 \sigma_\varepsilon-g_\varepsilon(x)=\sqrt2\int_0^{\sigma_\varepsilon}\cos(X_s/2)\,dW_s.
\]
By Itô isometry, \(\mathrm{Var}\,\sigma_\varepsilon=2\mathbb E\int_0^{\sigma_\varepsilon}\cos^2(X_s/2)\,ds\). Independently, optional stopping and Itô isometry for \(X_s-x\) give
\[
 8\mathbb E\int_0^{\sigma_\varepsilon}\sin^2(X_s/2)\,ds
 =\mathbb E(X_{\sigma_\varepsilon}-x)^2
 =(x-\varepsilon)(2\pi-\varepsilon-x).
\]
Subtract this contribution from \(2\mathbb E\sigma_\varepsilon\) to obtain the asserted exact variance, including its finite initial-separation correction.

**4. Almost-sure scale and central limit.** Put \(U_s=\log\tan(X_s/4)\). Itô's formula reduces the entire diffusion to
\[
 dU_s=\tanh(U_s)\,ds+\sqrt2\,dW_s.
\]
As \(X_s\to0\) or \(2\pi\), we have \(U_s\to-\infty\) or \(+\infty\) respectively. The martingale strong law \(W_s/s\to0\) and Cesàro averaging give \(U_s/s\to-1\) or \(+1\) almost surely. The exit of \(X\) from \((\varepsilon,2\pi-\varepsilon)\) is the first exit of \(U\) from \((-R_\varepsilon,R_\varepsilon)\), where \(R_\varepsilon=\log\cot(\varepsilon/4)=\log(1/\varepsilon)+O(1)\). Because the exited path ultimately has nonzero asymptotic speed, \(\sigma_\varepsilon/R_\varepsilon\to1\) almost surely.

For the centered martingale \(M_\varepsilon=\sigma_\varepsilon-\mathbb E\sigma_\varepsilon\), the stopped representation gives the bracket \(2\int_0^{\sigma_\varepsilon}\cos^2(X_s/2)\,ds\). The nonnegative integral \(\int_0^\infty\sin^2(X_s/2)\,ds\) is finite almost surely: the squared-increment identity for the bounded martingale gives its expected value \(x(2\pi-x)/8\). Hence, by the almost-sure exit scale,
\[
 \frac{[M]_{\sigma_\varepsilon}}{2\log(1/\varepsilon)}\to1\quad\text{almost surely}.
\]
The Dambis–Dubins–Schwarz representation and Brownian continuity under asymptotically deterministic clock changes imply the stated centered normal limit. This uses stochastic-process theorems plus the exact bracket control, not simulation.

## Verification

A standalone Python checker named `check.py` confirms the trigonometric difference identity, exact Poisson equation, martingale diffusion coefficients, and second-moment identities on a deterministic numerical grid. `check_output.txt` contains its actual output. The checker has no role in establishing almost-sure limits, universal quantifiers, or novelty; those are proved analytically above.

## Relationship to prior work

Alexandrov (2026), arXiv:2610.26354v1, introduces the noisy first-harmonic Möbius formulation and discusses matrix and phase Lyapunov exponents, phase locking, and phase slips. Its discussion identifies common-noise synchronization as a distinct question; it does not state these two-point finite-tolerance stopping-time formulas or their asymptotic fluctuations. Newman (2015/2017), arXiv:1502.07618, gives structural synchronization criteria for random circle homeomorphisms, rather than exact passage-time moments. Le Jan's account of isotropic Brownian stochastic flows contains the more general two-point diffusion covariance principle. That general principle explains part of the reduction here and is not claimed as new. The specific exact variance, first-exit orientation, accumulated-intensity universality, and stopping-time fluctuation law constitute the present quantitative result; an older specialized diffusion identity may potentially imply a subpart.

## Limitations

The drift must be common and *phase independent*. Equal sine/cosine channel intensities are essential to autonomy of the oriented gap. The intensity clock must diverge and be strictly increasing. No statement is made about distinct noise realizations, correlated sine/cosine channels, phase-dependent drifts, physical-time universality under varying intensity, higher harmonics, or exact finite-time synchronization. The formulas are internal mathematical results, not independent validation or a claim of exhaustive historical priority.

## References

1. A. Alexandrov, *Fate of Arnold tongues and canards in Möbius systems with noise*, arXiv:2610.26354v1 (first posted 19 October 2026), https://arxiv.org/html/2610.26354v1.
2. J. Newman, *Synchronisation in Invertible Random Dynamical Systems on the Circle*, arXiv:1502.07618 (first posted 26 February 2015; revised 2017), https://arxiv.org/abs/1502.07618.
3. Y. Le Jan, *New developments in stochastic dynamics*, International Congress of Mathematicians (2006), sections on stochastic flows and two-point motion; historical coverage risk identified.
