# A golden-ratio boundary for reversal and oscillation of reflection-reset Brownian autocovariance

## Finding
Consider a one-dimensional Brownian position with two modes, active and refractory. During the active mode the position evolves with variance rate \(2D\); independently, at rate \(r\) it is reflected and contracted by \(X\mapsto-uX\), then remains frozen in the refractory mode. At independent exponential rate \(b\), it resumes active Brownian motion from the frozen position. Assume \(D,r,b>0\) and \(0<u<1\). In its unique stationary regime set \(C(t)=\mathbb E[X_0X_t]\) for \(t\ge0\), \(\rho=b/r\), and \(\tau=rt\). Define
\[
 h=\frac{\rho(1+u)}{\rho+u^2},\qquad \delta=(1-\rho)^2-4\rho u,\qquad k=\frac{1+\rho}{2}.
\]
Then
\[
 C(0)=\frac{2D}{r}\frac{\rho+u^2}{(1+\rho)(1-u^2)},\qquad
 \frac{d^2}{d\tau^2}\frac{C(\tau/r)}{C(0)}+(1+\rho)\frac{d}{d\tau}\frac{C(\tau/r)}{C(0)}+\rho(1+u)\frac{C(\tau/r)}{C(0)}=0,
\]
with normalized initial slope \(-h\). Write
\[
 \rho_\pm=(\sqrt{1+u}\pm\sqrt u)^2,\qquad \rho_0=u(1-u),\qquad u_*=\frac{\sqrt5-1}{2}.
\]
There is an **exact, exhaustive classification of strictly positive-lag zeros**:

1. For every \(0<u<1\), if \(\rho_-<\rho<\rho_+\), then \(C\) has infinitely many simple positive zeros, spaced exactly \(\pi/(r\omega)\) with \(\omega=\sqrt{-\delta}/2\).
2. For \(0<u<u_*\) and \(\rho_0<\rho\le\rho_-\), it has exactly one positive zero.
3. In every other parameter case with \(0<u<1\), it has no positive zero and is strictly positive at every finite nonnegative lag.

In the single-zero region, as \(\rho\downarrow\rho_0\) at fixed \(u\in(0,u_*)\), the first zero in dimensionless time satisfies
\[
 r t_\mathrm{zero}=\frac{\log[1/(\rho-\rho_0)]}{1-u-u^2}+O(1).
\]
This includes the critical double-root and threshold cases; no zero is inferred from a numerical zero-finding procedure. In particular, reflection alone without refractory rests produces a positive single-exponential autocovariance, whereas reflection *with* rests can create oscillatory sign reversals despite the absence of deterministic oscillating dynamics.

## Assumptions and scope
The two-state process has state \((X_t,S_t)\), with \(S_t=A\) (active) or \(S_t=R\) (refractory). Its extended generator acts on mode-dependent smooth functions as
\[
 (Lf)_A(x)=D f_A''(x)+r[f_R(-ux)-f_A(x)],\qquad
 (Lf)_R(x)=b[f_A(x)-f_R(x)].
\]
There is no Brownian motion during rest, and the position does not change on restarting. The rates and Brownian increments are independent. All expectations are under the unique stationary probability law. The zeros count refers to \(t>0\), not to zero of the derivative or the negative-lag extension. The primary subject is the position two-time autocovariance, not a probability density or mean first-passage time.

## Proof
**Stationarity and second moments.** At successive active-to-rest transitions the post-contraction positions form an affine recursion whose multiplier has absolute value \(u<1\), with independent centered Gaussian increments accumulated during exponential active intervals. The standard contraction coupling yields a unique invariant distribution with finite second moment. The exponential active/rest clock alternates irreducibly, and its stationary active fraction is \(p_A=\rho/(1+\rho)\). Symmetry gives \(\mathbb E X_t=0\). Write \(M_A=\mathbb E[X_t^2\mathbf1_{\{S_t=A\}}]\) and \(M_R\) analogously. Stationary generator balances give
\[
 0=2Dp_A-rM_A+bM_R,\qquad 0=ru^2M_A-bM_R.
\]
Therefore
\[
 M_A=\frac{2Dp_A}{r(1-u^2)},\qquad M_R=\frac{u^2}{\rho}M_A,
\]
and their sum is the stated \(C(0)>0\).

**Two-time semigroup.** Brownian increments have zero conditional mean. Starting from position \(x\), the two conditional expectations are \(xv_A(\tau)\) and \(xv_R(\tau)\), where \(v_A(0)=v_R(0)=1\) and
\[
 \frac d{d\tau}\begin{pmatrix}v_A\\v_R\end{pmatrix}
 =\begin{pmatrix}-1&-u\\\rho&-\rho\end{pmatrix}
 \begin{pmatrix}v_A\\v_R\end{pmatrix}.
\]
Consequently \(C(\tau/r)=M_Av_A(\tau)+M_Rv_R(\tau)\). The matrix characteristic polynomial is \(z^2+(1+\rho)z+\rho(1+u)\). This gives the displayed second-order differential equation. Differentiating at zero gives \(C'(0)/(rC(0))=-M_A(1+u)/(M_A+M_R)=-h\). No closure approximation is used.

**Oscillatory regime.** If \(\delta<0\), put \(\omega=\sqrt{-\delta}/2\). The exact normalized covariance is
\[
 c(\tau)=e^{-k\tau}\left[\cos(\omega\tau)+\frac{k-h}{\omega}\sin(\omega\tau)\right].
\]
The bracket is a nonzero sinusoid because its cosine coefficient is one. Hence its positive zeros are simple, infinite in number, and separated by exactly \(\pi/\omega\). The inequality \(\delta<0\) is equivalent to \(\rho_-<\rho<\rho_+\).

**Real-spectrum regime.** For \(\delta>0\), write \(s_\mathrm{slow}=k-\sqrt\delta/2\) and \(s_\mathrm{fast}=k+\sqrt\delta/2\). Then
\[
 c(\tau)=A_\mathrm{slow}e^{-s_\mathrm{slow}\tau}+A_\mathrm{fast}e^{-s_\mathrm{fast}\tau},\quad
 A_\mathrm{slow}=\frac{s_\mathrm{fast}-h}{\sqrt\delta},\quad
 A_\mathrm{fast}=1-A_\mathrm{slow}.
\]
Since \(s_\mathrm{fast}>s_\mathrm{slow}\) and \(c(0)=1\), this sum crosses zero exactly once if and only if \(A_\mathrm{slow}<0\), equivalently \(h>s_\mathrm{fast}\). If \(A_\mathrm{slow}\ge0\), multiplying by \(e^{s_\mathrm{fast}\tau}\) shows strict positivity for all \(\tau\ge0\). At \(\delta=0\), the exact expression is \(c(\tau)=e^{-k\tau}[1+(k-h)\tau]\), with exactly one positive zero if and only if \(h>k\).

To classify \(h>s_\mathrm{fast}\), use the exact identity
\[
 (h-s_\mathrm{fast})(h-s_\mathrm{slow})
 =\frac{\rho u(1+u)^2[\rho-u(1-u)]}{(\rho+u^2)^2}.
\]
The discriminant is nonnegative precisely on \(0<\rho\le\rho_-\) or \(\rho\ge\rho_+\). At \(\rho=\rho_0=u(1-u)\), one spectral decay rate is \(h=1-u^2\), the other is \(u\). The former is the *fast* rate exactly when \(u^2+u<1\), equivalently \(u<u_*\). Below \(\rho_0\), \(h\) lies strictly between the real rates. Above \(\rho_0\) on the low-\(\rho\) real-spectrum branch, continuity and the displayed product show that \(h\) lies beyond the fast root if \(u<u_*\), but below the slow root if \(u>u_*\). On the high-\(\rho\) real-spectrum branch, \(h\) is below the slow root: it is so for large \(\rho\), and the product is strictly positive there, preventing root crossings. At \(u=u_*\), \(\rho_0=\rho_-=\sqrt5-2\), \(h=k\), and \(c=e^{-k\tau}>0\). This proves the complete classification including boundaries.

**Divergent first-zero lag.** Fix \(0<u<u_*\) and let \(\rho\downarrow\rho_0\) from above. The slow-mode coefficient is negative and vanishes linearly in \(\rho-\rho_0\), while the fast coefficient tends to one; this follows from the displayed product identity and the strictly positive limiting eigenvalue gap \(s_\mathrm{fast}-s_\mathrm{slow}=1-u-u^2\). Solving the two-exponential zero equation gives \(\tau_\mathrm{zero}=(s_\mathrm{fast}-s_\mathrm{slow})^{-1}\log(A_\mathrm{fast}/[-A_\mathrm{slow}])\), yielding the stated logarithmic asymptotic.

## Verification
The standalone Python program `checker.py` computes the stationary moment balances symbolically, verifies the characteristic polynomial and critical factorization, and checks the exact covariance against independent matrix-exponential semigroups over positive parameter grids, all three spectral regimes, and multiple dimensions of \(D\), \(r\) and lag. It also verifies examples in the single-crossing and noncrossing parameter strips. Run `python checker.py` with Python, NumPy, SciPy and SymPy. This verifies finite test cases only; the universal sign classification is proved algebraically above. For instance, \(u=1/5\), \(\rho=3/10\) gives the exact single reversal \(rt_\mathrm{zero}=2\log(112/27)\), whereas \(u=1/2\), \(\rho=1\) gives infinitely many damped sign reversals.

## Relationship to prior work
Biroli, Feld, Hartmann, Majumdar and Schehr (arXiv:2406.08387v1, June 12, 2024) analyze positive and negative rescaling resets without refractory rests, obtaining stationary distributions and mean first-passage properties. Olsen and Löwen (arXiv:2406.10039v1, June 14, 2024) study partial resets with refractory periods, explicitly restricting their resetting multiplier to the positive interval \((0,1)\), and derive one-time propagators, moments, and stationary kurtosis. García-Valladares, Gupta, Prados and Plata (arXiv:2310.19913v1, October 30, 2023) study complete resetting with refractory periods, its relaxation, and first-passage properties. The present joint negative-multiplier/exponential-rest process and the *stationary two-time sign-phase diagram* are not stated in these inspected sections. A general propagator may implicitly enable some aspects of the result via extension and differentiation; no priority exclusivity is asserted.

## Limitations
The analysis requires exponentially distributed active and refractory durations, constant Brownian diffusivity, and the specified reset-to-reflected-scaled-current-position rule. It does not describe non-Markovian rests, inertia, confined domains, thermodynamic work, or first-passage optimization. Oscillation is a correlation phenomenon, not deterministic particle motion. The analytic classification is internally checked but has not received an independent mathematical review, and a broader time-correlation formula not located in the literature could subsume it.

## References
1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (June 12, 2024), https://arxiv.org/abs/2406.08387.
2. K. S. Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1 (June 14, 2024), https://arxiv.org/abs/2406.10039.
3. G. García-Valladares, D. Gupta, A. Prados and C. A. Plata, *Stochastic resetting with refractory periods: pathway formulation and exact results*, arXiv:2310.19913v1 (October 30, 2023), https://arxiv.org/abs/2310.19913.
4. M. R. Evans and S. N. Majumdar, *Effects of refractory period on stochastic resetting*, arXiv:1809.01551 (September 5, 2018), https://arxiv.org/abs/1809.01551.
