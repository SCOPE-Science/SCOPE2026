# Two-time bath-memory spectrum and a persistent Green–Kubo excess under probe-only resetting

## Finding
For a harmonically coupled Brownian tracer and an unreset bath coordinate, resetting only the tracer produces an **exact positive bi-exponential stationary time autocovariance**. At arbitrarily rapid resetting, the tracer's one-time variance agrees at leading order with that of an isolated resetting Brownian particle, but its time-integrated autocovariance retains the strictly larger factor \(1+\gamma/2\). For every fixed positive time lag, the rescaled autocovariance converges to a nonzero bath-memory exponential.

Specifically, define the stationary tracer autocovariance \(C_{\gamma,r}(t)=\operatorname{Cov}(X_t,X_0)\) for \(t\ge0\). With the parameters and definitions below,
\[
C_{\gamma,r}(t)=A_s e^{-k_st}+A_f e^{-k_ft},\qquad A_s>0,\ A_f>0,
\]
\[
\int_0^\infty C_{\gamma,r}(t)\,dt
=\frac{\gamma^2r+2\gamma^2+2\gamma r+4\gamma+2}{r^2(\gamma r+2\gamma+1)}.
\]
Its ratio to the isolated resetting Brownian Green–Kubo integral with the **same** stationary variance and reset rate is
\[
\mathcal R_{\gamma,r}=\frac{r}{a}\int_0^\infty C_{\gamma,r}(t)\,dt
=1+\frac{\gamma(\gamma r+2\gamma+2)}{2(\gamma r+\gamma+1)}.
\]
This strictly decreases with \(r>0\), ranges between \(1+\gamma\) and \(1+\gamma/2\), and satisfies
\[
\lim_{r\to\infty} r a=2,\qquad
\lim_{r\to\infty}r^2C_{\gamma,r}(t)=e^{-t/\gamma}\ \ (t>0),\qquad
\lim_{r\to\infty} r^2\int_0^\infty C_{\gamma,r}(t)\,dt=2+\gamma.
\]
Thus comparison with isolated Brownian resetting, whose integral equals \(2/r^2\), yields the nonvanishing multiplicative excess \(1+\gamma/2\).

## Assumptions and scope
Fix any bath friction ratio \(\gamma>0\) and independent Poisson reset rate \(r>0\). In dimensionless units, let independent standard Brownian motions \(W,B\) drive
\[
dX_t=(-X_t+Q_t)\,dt+\sqrt2\,dW_t,\qquad
dQ_t=\gamma^{-1}(X_t-Q_t)\,dt+\sqrt{2/\gamma}\,dB_t.
\]
At each event of an independent rate-\(r\) Poisson process, replace \(X_t\) by zero and leave \(Q_t\) unchanged. All results concern the unique stationary law and **instantaneous** probe-only resets. The mean coordinates vanish by symmetry. The probe's stationary second moment is denoted by \(a=\mathbb E[X_0^2]\), with cross moment \(b=\mathbb E[X_0Q_0]\). Define
\[
a=\frac{2(\gamma r+\gamma+1)}{r(\gamma r+2\gamma+1)},\qquad
b=\frac{\gamma r+2\gamma+2}{r(\gamma r+2\gamma+1)},
\]
\[
S=1+r+\gamma^{-1},\quad
\Delta=\sqrt{S^2-4r/\gamma},\quad
k_s=(S-\Delta)/2,\quad k_f=(S+\Delta)/2,
\]
\[
d=1+r-b/a,\qquad
A_s=a\frac{k_f-d}{k_f-k_s},\qquad A_f=a\frac{d-k_s}{k_f-k_s}.
\]
The superscripts \(s,f\) denote slow and fast temporal relaxation modes, not separately defined random components.

## Proof
**Stationarity and moments.** Couple two processes using identical Brownian increments and identical reset times. Their difference \((u,v)\) obeys the deterministic drift between resets; for \(V=u^2+\gamma v^2\), its generator satisfies
\[
\mathcal LV=-2(u-v)^2-r u^2.
\]
The right side is negative definite for \(r>0\), giving exponential mean-square contractivity under synchronized coupling. Together with bounded noise input this yields a unique stationary law with finite second moments; linear contractivity also supplies the necessary joint moments. The stationary equations for \(a=\mathbb E[X^2]\), \(b=\mathbb E[XQ]\), and \(c=\mathbb E[Q^2]\) are
\[
0=-(2+r)a+2b+2,\quad
0=\gamma^{-1}a-(1+\gamma^{-1}+r)b+c,\quad
0=2\gamma^{-1}(b-c+1).
\]
The unique solution is the quoted \(a,b\), with \(c=b+1\). These **one-time moments are known from the motivating paper** and are recalled to fix normalization.

**Two-time equation.** Conditional first moments propagate according to
\[
\frac{d}{dt}\binom{\mathbb E[X_t\mid X_0,Q_0]}{\mathbb E[Q_t\mid X_0,Q_0]}
=M\binom{\mathbb E[X_t\mid X_0,Q_0]}{\mathbb E[Q_t\mid X_0,Q_0]},\qquad
M=\begin{pmatrix}-1-r&1\\\gamma^{-1}&-\gamma^{-1}\end{pmatrix}.
\]
Resetting contributes \(-r\mathbb E[X_t\mid X_0,Q_0]\) but no instantaneous loss of bath memory. The eigenvalues of \(-M\) are the distinct positive roots \(k_s<k_f\) of \(k^2-Sk+r/\gamma=0\): the discriminant equals \((1+r-\gamma^{-1})^2+4/\gamma>0\). The initial conditions are \(C(0)=a\) and \(C'(0)=-(1+r)a+b=-ad\). Solving the two-mode initial-value problem produces exactly \(A_s,A_f\) above.

**Both spectral weights are strictly positive.** Substitution yields the identity
\[
d^2-Sd+r/\gamma
=-\frac{r(2\gamma^2r^2+7\gamma^2r+6\gamma^2+8\gamma r+12\gamma+6)}{4(\gamma r+\gamma+1)^2}<0.
\]
Because the left side factors as \((d-k_s)(d-k_f)\), it follows that \(k_s<d<k_f\), so both amplitudes are positive. In particular the covariance is completely monotone: \((-1)^n C^{(n)}(t)>0\) for all integers \(n\ge0\) and all \(t\ge0\).

**Integrated time correlation and observable fluctuations.** Since \(M\) is strictly stable, integration of the two-time equation gives
\[
\int_0^\infty C(t)\,dt=\left(-M^{-1}\binom ab\right)_1=\frac{a+\gamma b}{r}.
\]
Substituting the stationary moments gives the displayed rational Green–Kubo expression. For the integrated position \(Y_T=\int_0^T X_s\,ds\), stationarity implies
\[
\operatorname{Var}(Y_T)=2\int_0^T (T-t)C(t)\,dt,
\]
so dominated convergence gives \(\operatorname{Var}(Y_T)/(2T)\to\int_0^\infty C(t)\,dt\). The formula for \(\mathcal R\) follows immediately; differentiation gives
\[
\frac{\partial\mathcal R_{\gamma,r}}{\partial r}
=-\frac{\gamma^2(\gamma+1)}{2(\gamma r+\gamma+1)^2}<0.
\]
The strict range and limiting values follow by taking the endpoints \(r\downarrow0\) and \(r\to\infty\), without asserting a stationary law at \(r=0\).

**Strong-reset boundary layer.** At fixed \(\gamma>0\), elementary expansion of the explicit roots and weights yields
\[
k_f=r+O(1),\quad k_s=\gamma^{-1}+O(r^{-1}),\quad
A_f=2r^{-1}+O(r^{-2}),\quad A_s=r^{-2}+O(r^{-3}).
\]
The fast term vanishes under \(r^2\)-scaling at each **strictly positive** time lag, leaving \(e^{-t/\gamma}\). Its time integral does not vanish because the fast term has area \(2/r^2+o(r^{-2})\); the slow term has area \(\gamma/r^2+o(r^{-2})\). The same limit follows from the rational integrated-covariance formula. Note the fixed-positive-lag limit is nonuniform at \(t=0\), where \(r^2 C(0)\to\infty\).

## Verification
The accompanying `verify.py` checks the formulas against a separately assembled four-dimensional stationary moment generator, its linear two-time semigroup, and numerical time integration, for 80 parameter-lag choices. It also verifies spectral weight positivity on the tested grid and strong-reset expansions at six large-\(r\) parameter choices. `simulate.py` independently simulates the coupled stochastic dynamics with explicit probe-only Poisson resetting; four stationary lag covariances agree with the analytic law within the reported sampling tolerance. These are finite numerical checks, not replacements for the proof.

## Relationship to prior work
Santra and Das (2026) introduce this tracer/bath model and reset rule and derive its exact **one-time** second moments, steady distributions, and relaxation of moments from prescribed initial data. The present statement **does not claim these results as new**. It addresses different data: stationary *two-time* correlations, their positive spectral decomposition, the Green–Kubo integral of an accumulated tracer observable, and the nonuniform strong-reset time-lag asymptotic. The distinction matters because leading-order agreement of stationary variance with a Markovian comparator does not imply agreement of long-time integrated fluctuations. Related studies of resetting in non-Markovian environments, including Guéneau–Majumdar–Schehr (2023) and Ginot–Bechinger (2025/2026), investigate different protocols or observables. These exact formulas may be implicit in general linear jump-process generator techniques; no claim is made that the methodology is new.

## Limitations
The theorem holds for a **single linear bath coordinate**, independent thermal Brownian noises at their fluctuation-dissipation normalizations, zero reset location, and instantaneous Poisson probe-only resetting. It does not cover general colored baths, nonlinear interactions, heavy-tailed reset times, or finite-speed returns. The result is a direct finite-dimensional generator calculation and does not assert a new universal theory. Originality relative to all possible general Markov jump-process formulas is a residual literature risk. The two-time strong-reset limit holds for each fixed \(t>0\), and must not be extended to \(t=0\).

## References
1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1 (first public 2026-03-17); New Journal of Physics 28 (2026), 074601, DOI:10.1088/1367-2630/ae868c. Source of the coupled model, reset protocol, and one-time moment results.
2. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables* (2023), for a related but different resetting-noise protocol.
3. F. Ginot and C. Bechinger, *Experimental investigation of stochastic resetting in non-Markovian environment* (2025/2026), for experimental memory-preserving resetting context.
