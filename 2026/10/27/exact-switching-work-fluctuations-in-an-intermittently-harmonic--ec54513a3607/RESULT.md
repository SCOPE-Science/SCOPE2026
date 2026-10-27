# Exact switching-work fluctuations in an intermittently harmonic Brownian trap

## Finding
For a stationary Brownian particle whose harmonic confinement switches between **off** and **on** at arbitrary positive, generally unequal Poisson rates, the accumulated mechanical work has an exact long-time variance and a Gaussian limit. Unlike the already-established mean rate, its variance rate is strictly sensitive to the overall switching speed.

Precisely, let \(D,k,a,b>0\), and let \(S_t\in\{0,1\}\) be an independent continuous-time Markov chain jumping from off \(0\) to on \(1\) at rate \(b\), and from on to off at rate \(a\). Define \(X_t\) and the switching work \(W_t\) under the assumptions below. Then, for a stationary initial state,
\[
\mathbb E W_t=\mu t,\qquad \mu=\frac{Dka}{a+b},
\]
\[
\lim_{t\to\infty}\frac{\operatorname{Var}(W_t)}{t}=V
=\frac{2D^2k^2a}{b}\left(\frac1k+\frac{2}{a+b}\right)
+\frac{2D^2k^2ab}{(a+b)^3}>0,
\]
\[
\frac{W_t-\mu t}{\sqrt t}\ \Longrightarrow\ \mathcal N(0,V).
\]
The mean power is prior work; the evaluated variance, Gaussian limit, and rate-dependence conclusion constitute the present finding.

At fixed off-state time fraction \(p=a/(a+b)\in(0,1)\) and switching intensity \(\lambda=a+b>0\),
\[
\mu=Dkp,\quad
V(\lambda)=\frac{2D^2kp}{1-p}
+\frac{2D^2k^2p}{\lambda}\left(\frac2{1-p}+1-p\right).
\]
Consequently, \(V(\lambda)\) decreases **strictly** with \(\lambda\), diverges as \(\lambda\downarrow0\), and tends to the strictly positive unattained floor \(2D^2kp/(1-p)\) as \(\lambda\uparrow\infty\), even though the mean power is unchanged. In the symmetric case \(a=b=\gamma\), the exact formulas simplify to
\[
\mu=\frac{Dk}{2},\qquad V=2D^2k+\frac{9D^2k^2}{4\gamma}.
\]

## Assumptions and scope
The model is the one-dimensional overdamped Itô diffusion
\[
 dX_t=-kS_tX_t\,dt+\sqrt{2D}\,dB_t,
\]
with a Brownian motion \(B\) independent of the Markov chain \(S\); state-dependent energy is \(U_s(x)=ksx^2/2\), and mobility is normalized to one. All parameters are positive, the chain switches at the specified constant rates without changing particle position, and the **joint** stationary law is used at time zero. In particular, the ``off'' position continues to diffuse freely until the next ``on'' event.

The mechanical work is the signed sum of **both** directions of stiffness jumps, with the continuous position sampled at each switch:
\[
W_t=\frac{k}{2}\sum_{0<u\le t:\,S_u\ne S_{u-}}(S_u-S_{u-})X_u^2.
\]
Switching on injects \(+kX_u^2/2\); switching off extracts \(-kX_u^2/2\). The variance and central limit refer to accumulated switching work over a deterministic observation duration \(t\), not to work per switch, heat, or a fixed count of switches. They do not include translational inertia or additional controller fluctuations.

Existence of the unique stationary joint law and all its polynomial moments follows by regeneration at successive off/on cycles. A full cycle has a strictly contracting on-phase factor \(e^{-kT_{\mathrm{on}}}\), while the Brownian increments across independent exponential off/on holding times possess moments of every finite order. The induced affine recursion is strictly contractive in logarithmic mean and has finite moments; the continuous-time process is positive recurrent and ergodic.

## Proof
**1. Stationary chain probabilities and position moments.** With \(q_0=b\), \(q_1=a\), the generator acting on functions of \((x,s)\) is
\[
(\mathcal Lf)_s=D\,\partial_{xx}f_s-ksx\,\partial_x f_s+q_s(f_{1-s}-f_s).
\]
The stationary state probabilities are \(p_0=a/(a+b)\) and \(p_1=b/(a+b)\). Write \(u_s=\mathbb E[X^2\mathbf1_{\{S=s\}}]\). The stationary generator identities for the two state-weighted quadratic observables give
\[
0=2Dp_0-bu_0+au_1,\qquad
0=2Dp_1-(2k+a)u_1+bu_0.
\]
On adding, \(u_1=D/k\), and hence
\[
u_0=\frac{Da}{b}\left(\frac1k+\frac2{a+b}\right).
\]
The predictable drift density of the jump-work process is \(j_0(x)=bkx^2/2\) in state zero and \(j_1(x)=-akx^2/2\) in state one. Thus
\[
\mathbb E W_t=t\mathbb Ej_S(X)=\frac{k}{2}(bu_0-au_1)t=\frac{Dka}{a+b}t.
\]
This mean-power identity is previously established by the entropy-production literature.

**2. A pointwise Poisson-equation coboundary.** Set \(c=Dk/(a+b)\) and
\[
g_0(x)=\frac{kx^2}{2}+c,\qquad g_1(x)=0.
\]
Directly,
\[
 j_0(x)+(\mathcal Lg)_0(x)=Dk-bc=\mu,
\qquad
 j_1(x)+(\mathcal Lg)_1(x)=ac=\mu.
\]
Therefore
\[
M_t=W_t+g_{S_t}(X_t)-g_{S_0}(X_0)-\mu t
\]
is a square-integrable martingale. Its continuous local-martingale part equals
\[
\int_0^t k\sqrt{2D}X_u\mathbf1_{\{S_u=0\}}\,dB_u.
\]
At a jump from zero to one the work and \(g\)-increment combine to \(-c\), while a jump from one to zero yields \(+c\). **The quadratic jump amplitudes cancel exactly**: the jumps of \(M\) have bounded deterministic magnitude \(c\).

**3. Exact bracket and asymptotic variance.** The predictable quadratic variation is
\[
\langle M\rangle_t=\int_0^t\left[2Dk^2X_u^2\mathbf1_{\{S_u=0\}}+c^2\bigl(b\mathbf1_{\{S_u=0\}}+a\mathbf1_{\{S_u=1\}}\bigr)\right]du.
\]
Its stationary expectation is \(tV\), where
\[
 V=2Dk^2u_0+c^2(bp_0+ap_1)
 =\frac{2D^2k^2a}{b}\left(\frac1k+\frac{2}{a+b}\right)
 +\frac{2D^2k^2ab}{(a+b)^3}.
\]
Martingale isometry gives \(\mathbb E M_t^2=tV\). Since the chain-diffusion has a stationary finite fourth position moment, the boundary term \(g_{S_t}(X_t)-g_{S_0}(X_0)\) has a uniformly bounded second moment. Its covariance with \(M_t\) is \(O(\sqrt t)\) by Cauchy–Schwarz. This establishes \(\operatorname{Var}(W_t)/t\to V\). No finite trajectory simulation is used to prove this limit.

**4. Gaussian limit.** Ergodicity and the explicit bracket give \(\langle M\rangle_t/t\to V\) almost surely. The martingale has constant-magnitude jumps \(\pm c\), satisfying its asymptotic jump-Lindeberg condition; its continuous local-martingale part has bracket already included above. The continuous-time martingale central limit theorem therefore gives \(M_t/\sqrt t\Rightarrow\mathcal N(0,V)\). The stationary finite-second-moment boundary is \(o_{\mathbb P}(\sqrt t)\), and Slutsky's theorem gives the claimed CLT for \(W_t\).

**5. Switching-rate monotonicity.** Substitute \(a=p\lambda\) and \(b=(1-p)\lambda\) into the exact closed form for \(V\). The term proportional to \(\lambda^{-1}\) has a strictly positive coefficient for every permitted parameter, proving strict monotonicity, the divergence, and the positive fast-switching limit. Substitute \(a=b=\gamma\) for the symmetric specialization.

## Verification
The standalone `verify_work.py` uses only the Python standard library. It first checks the exact stationary moment balances and coboundary identities with rational arithmetic. Independently of the martingale-bracket calculation, it integrates the closed twelve-dimensional forward ODE for the mixed moments \(\mathbb E[W_t^pX_t^{2m}\mathbf1_{\{S_t=s\}}]\), with indices \((p,m)=(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)\) and both states. The ODE includes work increments at both switch directions. In four disparate parameter regimes, the late-time slopes of the directly propagated work variance agree with the formula, and the propagated mean rates agree with \(\mu\). The command `python verify_work.py` prints `ALL_CHECKS_PASS` on success. These finite-time, floating-point results corroborate the proof but do not establish the limiting assertions by themselves.

## Relationship to prior work
Alston, Cocconi, and Bertrand (2022), particularly Section 4.2.1 and equation (40), study this intermittent harmonic potential with asymmetric rates and derive the stationary mean entropy-production / injected-work rate; the mean \(\mu\) above agrees after their parameter identification. Frydel (2024), especially Sections II and VI and equation (48), studies the symmetric on/off trap, obtains stationary position moments and the rate-independent mean dissipation. Neither inspected result supplies the **evaluated long-time variance of the signed cumulative switching work** or the bounded-jump coboundary yielding the CLT.

Work fluctuations for harmonically trapped particles with a fluctuating **trap center** are studied in earlier literature (for example Pal and Sabhapandit, 2013), but the mechanical observable and modulation mechanism differ. General theory of Markov-modulated Ornstein–Uhlenbeck processes and martingale additive functionals supplies reusable techniques; an unlocated theorem or published evaluated cumulant may subsume this explicit specialization. Priority beyond the inspected sources is not independently established.

## Limitations
Only a completely **off/on** trap with two independent exponential holding-time laws and positive finite parameters is addressed. The process begins in the joint stationary state; no nonstationary finite-time variance formula is asserted. The fluctuations of heat, work per completed switching cycle, partial/nonzero-off stiffness, non-Markovian switching, inertial dynamics, and optimal finite-duration control are not determined. The fast-switching variance floor is a sequential limit (first long observation time, then rapid switching), not a statement about a physically rescaled underdamped model. The novelty assessment is evidence-based and does not constitute an independent literature-priority certification.

## References
1. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213, first posted 2024-07-16, https://arxiv.org/abs/2407.12213 .
2. H. Alston, L. Cocconi, and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630, first posted 2022-02-05, https://arxiv.org/abs/2202.02630 .
3. General background: the martingale central limit theorem for locally square-integrable martingales with converging normalized predictable bracket and vanishing normalized jump size, as used in the proof above.
