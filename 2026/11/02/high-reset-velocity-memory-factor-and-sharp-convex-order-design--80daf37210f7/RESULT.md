# High-reset velocity-memory factor and sharp convex-order design for an active Ornstein–Uhlenbeck searcher

## Finding
Fix \(D,D_v,\tau>0\), \(0<d<L<\infty\) and a compact velocity interval \([a,b]\) with \(a<b\). During each search attempt, \(X\in[0,L]\) is absorbed upon reaching zero, is normally reflected at \(L\), and evolves with active velocity \(V\):
\[
 dX_t=V_t\,dt+\sqrt{2D}\,dB_t-dK_t,\qquad
 dV_t=-\tau^{-1}V_t\,dt+\tau^{-1}\sqrt{2D_v}\,dW_t.
\]
Here \(B,W\) are independent standard Brownian motions and \(K\) is the minimal nondecreasing upper-wall regulator, supported on \(\{X_t=L\}\). Each independent attempt begins from \(X_0=d\) and an independent velocity drawn from a fixed law \(\nu\) on \([a,b]\). Independent Poisson resets of rate \(r>0\) terminate unsuccessful attempts and restart **both** position and velocity from this same law. Let \(M_r(\nu)\) be the mean total absorption time, and write \(c=d/(2D)\).

Then, uniformly over all probability laws \(\nu\) supported on \([a,b]\),
\[
 M_r(\nu)=\frac{e^{d\sqrt{r/D}}}{r\,C(\nu)}\bigl(1+O(r^{-1/4})\bigr),\qquad
 C(\nu)=\int_a^b e^{-cv}\,\nu(dv),\quad r\to\infty.
\]
The implied constant depends only on the fixed model parameters and \([a,b]\). In particular the **entire** leading active-velocity correction persists as \(r\to\infty\), but is independent of the persistence time and the OU velocity-noise strength. The base Brownian activation exponent \(d\sqrt{r/D}\) is unchanged.

Fix a reset-velocity mean \(m\in[a,b]\). Among all such \(\nu\), the asymptotically **largest** mean absorption time is attained by \(\delta_m\), and the asymptotically **smallest** by the endpoint mixture
\[
 \nu_* = \frac{b-m}{b-a}\delta_a+\frac{m-a}{b-a}\delta_b.
\]
More precisely, for \(C_*=(b-m)e^{-ca}/(b-a)+(m-a)e^{-cb}/(b-a)\),
\[
 \lim_{r\to\infty}r e^{-d\sqrt{r/D}}\inf_{\nu:\,\mathbb E_\nu V=m}M_r(\nu)=C_*^{-1},
\qquad
 \lim_{r\to\infty}r e^{-d\sqrt{r/D}}\sup_{\nu:\,\mathbb E_\nu V=m}M_r(\nu)=e^{cm}.
\]
If \(a<m<b\), the asymptotic constants have unique attaining distributions. If two laws of equal mean are ordered in convex order, the more variable law has the smaller or equal leading mean-time constant; equality requires the same value of \(C\), not necessarily identical laws. At fixed mean zero on \([-v_*,v_*]\), symmetric endpoint resetting improves the leading mean-time constant over deterministic zero-velocity resetting by the exact factor \(\cosh(cv_*)\). No finite-\(r\) ordering is asserted.

## Assumptions and scope
All limits keep \(D,D_v,\tau,d,L,a,b\) fixed while \(r\to\infty\). The reset velocity is independently redrawn at **every** attempt; keeping a continuously evolving velocity through a position-only reset is a different nonrenewal model. The upper-wall reflection is instantaneous in position, not a reversal of the active OU velocity. The theorem concerns the absorption mean rather than its full distribution. The compact-support requirement on the reset law is essential to the stated *uniform* bound. The velocity diffusion between resets is Gaussian and unbounded, despite the bounded reset draw.

## Proof
Let \(T\) denote absorption before resetting, started at \((d,v)\), and set \(q_r(v)=\mathbb E_{d,v}e^{-rT}\). Restart renewal gives exactly
\[
 M_r(\nu)=\frac{1-q_r(\nu)}{r q_r(\nu)},\qquad
 q_r(\nu)=\int q_r(v)\,\nu(dv).
\]
Indeed, the duration of each attempt is \(\min(T,E_r)\), of mean \((1-q_r(\nu))/r\), with independent success probability \(q_r(\nu)\).

We establish the uniform short-attempt estimate
\[
 q_r(v)=e^{-d\sqrt{r/D}}e^{-cv}\bigl(1+O(r^{-1/4})\bigr),\qquad v\in[a,b]. \tag{1}
\]
First remove active drift, retaining the reflected Brownian motion killed at zero. Its exact discounted hitting probability from \(x\in[0,L]\) is
\[
 h_r(x)=\frac{\cosh((L-x)\sqrt{r/D})}{\cosh(L\sqrt{r/D})},\qquad
 h_r(d)=e^{-d\sqrt{r/D}}\bigl(1+O(e^{-2(L-d)\sqrt{r/D}})\bigr). \tag{2}
\]
Under the killed-reference path measure \(Q\), tilt the path through its absorption time by \(dQ_r/dQ=e^{-rT}/h_r(d)\). This is a probability law. Its preabsorption generator is
\[
 D\partial_{xx}+2D\frac{h_r'(x)}{h_r(x)}\partial_x,
\]
with the original upper reflection. In particular the tilted position path stays in \([0,L]\). From \(\mathbb E_{Q_r}e^{-sT}=h_{r+s}(d)/h_r(d)\), differentiating twice, uniformly for fixed \(0<d<L\), gives
\[
 \mathbb E_{Q_r}T=\frac{d}{2\sqrt{Dr}}+O(e^{-\eta\sqrt r}),\quad
 \operatorname{Var}_{Q_r}(T)=\frac{d}{4\sqrt D\,r^{3/2}}+O(e^{-\eta\sqrt r}), \tag{3}
\]
for some \(\eta>0\). Consequently \(\mathbb E_{Q_r}\sqrt T=O(r^{-1/4})\). The probability of encountering the upper wall before absorption in the tilted reference process is exponentially small: by killing at both endpoints before its first upper hit,
\[
 Q_r(T_L<T_0)=\frac{\sinh(d\sqrt{r/D})}{\sinh(L\sqrt{r/D})}\frac{h_r(L)}{h_r(d)}
 =O(e^{-2(L-d)\sqrt{r/D}}). \tag{4}
\]

Keep the OU process \(V\), driven by a Brownian motion independent of the reference position. The conditional Girsanov density adding drift \(V\) to the spatial Brownian driver, stopped at absorption, is
\[
 Z_T=\exp\left(\frac1{\sqrt{2D}}\int_0^T V_s\,dB_s-\frac1{4D}\int_0^T V_s^2\,ds\right).
\]
The identity \(q_r(v)=h_r(d)\mathbb E_{Q_r,V}Z_T\) follows first at bounded stopping times; the extension to \(T\) follows by nonnegative localization and the discounted tail bound \(\mathbb E[e^{-rT};T>t]\le e^{-rt}\). Under \(Q_r\), replace the Brownian driver by the Doob-transformed driver and integrate \(\int V\,dX\) by parts. Because the position and velocity noises are independent, their quadratic covariation vanishes. Thus the **exact** identity is
\[
 Z_T=e^{-cv}\exp\left[-\frac1{2D}\int_0^T X_s\,dV_s+\frac1{2D}\int_0^T V_s\,dK_s-\frac1{4D}\int_0^T V_s^2\,ds\right]. \tag{5}
\]
Here \(K\) is the upper reflection regulator in the drift-free, transformed reference path; it vanishes unless the upper wall has been visited.

For completeness, the localization estimate needed in (5) is as follows. On paths with no upper-wall encounter and \(T\le r^{-1/3}\), insert \(dV=-V\,dt/\tau+\sqrt{2D_v}\,dW/\tau\). The remainder exponent in (5) is a time integral of \(XV\) and \(V^2\), plus a Gaussian Itô integral of the bounded integrand \(X/\tau\). Conditional on the positional path, the OU representation makes these terms Gaussian-linear and nonpositive-quadratic functionals of \(W\). Their exponential moments and their first absolute moments are controlled uniformly in \(v\in[a,b]\) by Gaussian completion of squares. Since \(0\le X\le L\) and \(\mathbb E_{Q_r}T^{1/2}=O(r^{-1/4})\), the conditional expectation of the exponential is \(1+O(r^{-1/4})\). To control exceptional trajectories, (3) and a Chernoff bound using \(h_{r-s}(d)/h_r(d)\) make \(T>r^{-1/3}\) exponentially negligible after discounting; (4) and the same Gaussian stopped-density estimate make paths encountering \(L\) exponentially negligible. All estimates are uniform on the compact set of starting velocities. Hence \(\mathbb E_{Q_r,V}Z_T=e^{-cv}(1+O(r^{-1/4}))\), which with (2) proves (1).

Integrating (1) against any supported \(\nu\), uniformly, gives \(q_r(\nu)=e^{-d\sqrt{r/D}}C(\nu)(1+O(r^{-1/4}))\). The renewal identity and \(q_r(\nu)\to0\) prove the first main assertion. Finally \(f(v)=e^{-cv}\) is strictly convex on \([a,b]\). Jensen's inequality gives \(C(\nu)\ge e^{-cm}\), with equality only at \(\delta_m\), and the strict chord inequality gives
\[
 C(\nu)\le \frac{b-m}{b-a}e^{-ca}+\frac{m-a}{b-a}e^{-cb},
\]
with equality only for the endpoint law. Uniformity of (1) allows the optimization and limit to commute. Convex-order monotonicity follows from the definition of convex order. This completes the proof.

## Verification
`verify.py` checks the drift-only solvable specialization, exact Brownian mixed-boundary resolvent identities, the renewal identity, and chord/Jensen inequalities across a deterministic grid. The accompanying `aoup_reference_mc.py` independently samples the discounted-reference diffusion and checks the exact Girsanov weight at selected rates. These checks are finite numerical corroboration, not substitutes for the estimates in the proof. Reproduce with `python verify.py`; the optional Monte Carlo example uses NumPy and runs with `python aoup_reference_mc.py`.

## Relationship to prior work
Georgiou, Bressloff and Bertrand (2026) formulate the finite-interval active OU resetting model, develop weak-activity perturbation theory for first passage, and demonstrate fixed-velocity resetting effects numerically. The present claim is restricted to the different, singular \(r\to\infty\) regime with independently *randomized* reset velocities and gives a sharp distributional design law without a weak-activity assumption. Baouche and Kurzthaler (2025) treat active Brownian rather than OU propulsion and use a weak-Péclet expansion for the first-passage problem. Shankari and Sahoo (2025) derive resetting stationary spreading statistics rather than an absorption-time velocity-law optimum. Classical exponential-restart renewal formulas and passive Brownian first-passage resolvents are inputs, not new findings.

## Limitations
The result does not establish finite-rate convex-order optimality, a uniform limit for unbounded reset laws, preservation of the formula for position-only resets without velocity renewal, or behavior at \(D=0\). No priority statement is made about all possible general small-time diffusion theorems. The \(O(r^{-1/4})\) bound is conservative and is not asserted to be optimal; no independent scientific audit has occurred.

## References
1. D. K. Georgiou, P. C. Bressloff, T. Bertrand, *Persistence, resetting, and first-passage times of an active Ornstein–Uhlenbeck particle* (2026), arXiv:2609.21124v1, https://arxiv.org/abs/2609.21124 . First public date 2026-09-17.
2. Y. Baouche, C. Kurzthaler, *Optimal first-passage times of active Brownian particles under stochastic resetting* (2025), arXiv:2504.02466v1, https://arxiv.org/html/2504.02466v1 .
3. U. Shankari, M. Sahoo, *Active Ornstein–Uhlenbeck particle under stochastic resetting* (2025), arXiv:2509.18515v1, https://arxiv.org/abs/2509.18515 .
4. M. R. Evans, S. N. Majumdar, *Diffusion with stochastic resetting* (2011), Phys. Rev. Lett. 106, 160601, https://doi.org/10.1103/PhysRevLett.106.160601 .
