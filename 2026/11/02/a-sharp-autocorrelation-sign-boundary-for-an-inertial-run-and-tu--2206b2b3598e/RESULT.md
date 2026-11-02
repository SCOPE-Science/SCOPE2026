# A sharp autocorrelation sign boundary for an inertial run-and-tumble oscillator

## Finding

Consider the stationary athermal inertial run-and-tumble particle in a harmonic trap,
\[
\dot X_t=V_t,\qquad
\dot V_t=-2\beta V_t-\omega_0^2X_t+a\sigma_t,
\]
where \(\beta,\omega_0>0\), \(a\ne0\), and the symmetric stationary telegraph signal \(\sigma_t\in\{-1,+1\}\) flips at rate \(q/2>0\). Thus \(\mathbb E[\sigma_t\sigma_0]=e^{-q|t|}\). Define the stationary position autocovariance \(C_q(t)=\mathbb E[X_tX_0]\) for \(t\ge0\).

**Theorem (complete sign dichotomy and sharp onset).** The stationary position autocovariance is strictly positive for every finite lag whenever either \(\beta\ge\omega_0\), or \(0<\beta<\omega_0\) and \(q\le\beta\). When \(0<\beta<\omega_0\) and \(q>\beta\), it has infinitely many alternating strictly positive and strictly negative lag intervals and infinitely many zeros. Thus
\[
\boxed{\exists t>0:\ C_q(t)<0\quad\Longleftrightarrow\quad
0<\beta<\omega_0\ \text{ and }\ q>\beta.}
\]
For each fixed \(0<\beta<\omega_0\), define \(T_-(q)=\inf\{t>0:C_q(t)<0\}\), which is finite for \(q>\beta\). Its first-negative-lag onset has the sharp limit
\[
\boxed{\lim_{q\downarrow\beta}(q-\beta)T_-(q)
=\log\!\left(\frac{2}{\sqrt{1+3\beta^2/\omega_0^2}}\right)>0.}
\]
Equivalently, for mass \(m\), friction \(\gamma\), trap stiffness \(\mu\), and average time between tumbles \(\tau_a\), negative stationary position correlations occur precisely when \(\gamma^2<4m\mu\) and \(\tau_a<4m/\gamma\). The switching threshold is independent of trap stiffness within the underdamped region.

## Assumptions and scope

The process is defined as the unique causal stationary solution of the stable linear equations above, with symmetric, two-state, stationary Markov propulsion. In the physical form \(m\ddot X_t=-\gamma\dot X_t-\mu X_t+a_0\sigma_t\), the correspondence is \(2\beta=\gamma/m\), \(\omega_0^2=\mu/m\), \(a=a_0/m\), and \(q=2/\tau_a\). All positive real parameter values stated in the theorem are included, as are critically damped systems. The force amplitude can have either sign and is nonzero. There is no additive thermal white noise, multiplicative force, or nonlinear confinement. The exact covariance formulas and their sign classification also hold for any stationary zero-mean finite-variance input with the same strictly positive exponential covariance, after multiplying by that input's variance; non-Gaussianity of the telegraph law is not used at second order.

## Proof

**1. Stationarity and covariance normalization.** Let \(h\) be the causal Green function of \(\partial_t^2+2\beta\partial_t+\omega_0^2\), normalized by \(h(0)=0\), \(h'(0)=1\). Since both deterministic oscillator roots have negative real part, \(h\) is absolutely integrable and
\[
X_t=a\int_0^\infty h(s)\sigma_{t-s}\,ds
\]
exists as a stationary square-integrable solution. Its mean is zero. Put \(M_q=\omega_0^2+2\beta q+q^2\). From the stationary generator applied to \(X\sigma\), \(V\sigma\), \(XV\), and \(V^2\), respectively,
\[
\mathbb E[V\sigma]=q\mathbb E[X\sigma],\quad
\mathbb E[X\sigma]=a/M_q,\quad
\mathbb E[XV]=0,\quad
\mathbb E[V^2]=a^2q/(2\beta M_q).
\]
The stationary \(XV\) balance then gives
\[
C_q(0)=\mathbb E[X^2]=
\frac{a^2(2\beta+q)}{2\beta\omega_0^2 M_q},\qquad C_q'(0)=0.
\]
For positive lag, stationarity and the Markov property of the telegraph process imply \(\mathbb E[\sigma_tX_0]=(a/M_q)e^{-qt}\). Hence
\[
C_q''(t)+2\beta C_q'(t)+\omega_0^2C_q(t)
=\frac{a^2}{M_q}e^{-qt}.
\]
This initial-value problem uniquely determines the covariance. For arbitrary stationary forcing having the specified exponential covariance, the same identity follows instead from its transfer-function spectrum.

**2. Underdamped closed form.** For \(0<\beta<\omega_0\), write \(\Omega=\sqrt{\omega_0^2-\beta^2}\) and \(H_q=(q-\beta)^2+\Omega^2=\omega_0^2+q^2-2\beta q\). Solving the initial-value problem gives
\[
C_q(t)=K_q\left[e^{-qt}+e^{-\beta t}
\big(A_q\cos(\Omega t)+B_q\sin(\Omega t)\big)\right],
\qquad K_q=\frac{a^2}{M_qH_q}>0,
\]
where the dimensionless coefficients are
\[
A_q=\frac{q(\omega_0^2+q^2-4\beta^2)}{2\beta\omega_0^2},\qquad
B_q=\frac{q(3\omega_0^2+q^2-4\beta^2)}{2\omega_0^2\Omega}.
\]
These coefficients cannot vanish simultaneously: their zero numerators differ by \(2\omega_0^2>0\).

**3. Positive regime at and below the switching threshold.** At \(q=\beta\), the trigonometric amplitude satisfies
\[
R_\beta:=\sqrt{A_\beta^2+B_\beta^2}
=\frac12\sqrt{1+3\beta^2/\omega_0^2}<1.
\]
Consequently \(C_\beta(t)\ge K_\beta e^{-\beta t}(1-R_\beta)>0\) for every finite \(t\ge0\). To treat all \(0<q<\beta\) without an invalid oscillatory-envelope comparison, use the positive covariance-kernel decomposition: for \(0<q<r\),
\[
e^{-q|t|}=\frac qr e^{-r|t|}
+\frac{r^2-q^2}{2r}\int_{\mathbb R}
e^{-q|s|}e^{-r|t-s|}\,ds.
\]
This follows by Fourier transformation, using \(\widehat{e^{-q|\cdot|}}(\xi)=2q/(q^2+\xi^2)\). Convolution by the linear oscillator's impulse response and its reflection transfers the same identity to the output covariance:
\[
C_q(t)=\frac qr C_r(t)
+\frac{r^2-q^2}{2r}\int_{\mathbb R}e^{-q|s|}C_r(t-s)\,ds.
\]
The coefficients and kernel are positive. Setting \(r=\beta\), and using the evenness and strict positivity of \(C_\beta\), proves \(C_q(t)>0\) for every finite lag when \(q<\beta\).

**4. Overdamped and critically damped systems.** If \(\beta>\omega_0\), then with \(d=\sqrt{\beta^2-\omega_0^2}\), the impulse response is \(h(t)=e^{-\beta t}\sinh(dt)/d>0\) for \(t>0\). At \(\beta=\omega_0\), it is \(h(t)=t e^{-\beta t}>0\). Thus in either case,
\[
C_q(t)=a^2\int_0^\infty\int_0^\infty
h(u)h(v)e^{-q|t-u+v|}\,du\,dv>0
\]
for all \(t\ge0\), all \(q>0\). This completes the positive half of the dichotomy, including the double-root boundary.

**5. Infinite negative-lag bands above threshold.** For \(q>\beta\) in the underdamped regime, multiplying the closed form by \(e^{\beta t}/K_q\) yields
\[
\frac{e^{\beta t}}{K_q}C_q(t)
=e^{-(q-\beta)t}+A_q\cos(\Omega t)+B_q\sin(\Omega t).
\]
The first term tends to zero, while the last two have a nonzero periodic amplitude. Therefore an infinite sequence of positive maxima and negative minima survives at large lags, with infinitely many intervening zeros. No finite numerical enumeration is used to establish this.

**6. Sharp delay to the first negative lag.** Set \(R_q=\sqrt{A_q^2+B_q^2}\). Continuity and \(R_\beta<1\) imply \(0<R_q<1\) for all \(q>\beta\) sufficiently close to \(\beta\). Dividing the covariance by \(K_qe^{-qt}\), its sign becomes that of \(1+R_qe^{(q-\beta)t}\cos(\Omega t-\phi_q)\), with a suitable real phase \(\phi_q\). Consequently, for \(L_q=\log(1/R_q)/(q-\beta)\), the covariance remains positive on \([0,L_q)\), while the first phase point with cosine equal to \(-1\) after \(L_q\) occurs within an additional \(2\pi/\Omega\) and makes the covariance negative (at equality, take the immediately following minimum). Thus
\[
L_q\le T_-(q)\le L_q+2\pi/\Omega,
\]
and multiplying by \(q-\beta\), then taking \(q\downarrow\beta\), proves the stated limit.

## Verification

The exact sign witness \(\beta=1/2\), \(\omega_0=1\), \(q=1\), \(a=1\) yields
\[
C_1(t)=\frac13\left[e^{-t}+e^{-t/2}
\left(\cos\frac{\sqrt3t}{2}+\sqrt3\sin\frac{\sqrt3t}{2}\right)\right].
\]
At \(t=2\pi/\sqrt3\),
\[
C_1(2\pi/\sqrt3)=\frac13\big(e^{-2\pi/\sqrt3}-e^{-\pi/\sqrt3}\big)<0.
\]
The included `checker.py`, using only the Python standard library, compares the formula with an independently integrated three-variable moment system, checks the critical amplitude, samples positive and negative regimes, and checks near-threshold scaling. Run `python3 checker.py` in the same directory; it reports 2015 passed finite diagnostics. Those finite tests are supplementary, not proofs of the global sign classification or asymptotic limit.

## Relationship to prior work

Dutta, Kundu, Sabhapandit and Basu (arXiv:2406.06120, first released 2024-06-10) provide the exact inertial telegraph-driven model, its Green function, equal-time stationary moments and nonstationary equal-time correlations. They classify position and velocity marginal shapes, not the sign of stationary unequal-time position covariance. Their Green function makes a forward covariance calculation possible but does not by itself establish the strict all-lag positivity below the threshold or the first-negative-lag delay law. Garcia-Millan and Pruessner (arXiv:2012.02900, Appendix F) compute two-time correlations for an **overdamped** run-and-tumble particle with thermal noise, not the inertial positive-versus-oscillatory dichotomy here. General colored-noise filtering and spectral-pole methods provide additional conceptual precursors, whose broader coverage and publication priority require independent review. The statement is not a claim of originality for the linear impulse response, the telegraph autocorrelation, or routine transfer-function algebra.

## Limitations

The theorem classifies stationary *second-order position correlations*, not sample-path oscillations, velocity correlations, probability distributions, spectral-peak locations, or thermodynamic entropy production. The critical onset concerns the *first finite negative lag*, which diverges as the threshold is approached from above; a finite measurement horizon can fail to detect the eventual negative lobes. Additive thermal noise, finite observation windows, state-dependent tumbling and nonlinear traps are not covered. The closed-form spectral transfer relation is classical and could make some of the derived threshold implicit in wider literature; priority is not independently certified.

## References

1. D. Dutta, A. Kundu, S. Sabhapandit and U. Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120v1 (2024-06-10), https://arxiv.org/abs/2406.06120 ; accessible HTML version https://arxiv.org/html/2406.06120v2 (model, Sec. II; moments, Sec. III; Green function, App. A; equal-time calculations, App. B).
2. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion: field theory and entropy production*, arXiv:2012.02900 (2020), https://arxiv.org/abs/2012.02900 (overdamped dynamics and Appendix F two-time correlation).
3. F. Marchesoni, E. Menichella-Saetta, M. Pochini and S. Santucci, *Analog simulation of underdamped stochastic systems driven by colored noise: Spectral densities*, Physical Review A 37, 3058 (1988), https://doi.org/10.1103/PhysRevA.37.3058 (related colored-noise spectral setting, not a source for the claimed sharp sign threshold).
