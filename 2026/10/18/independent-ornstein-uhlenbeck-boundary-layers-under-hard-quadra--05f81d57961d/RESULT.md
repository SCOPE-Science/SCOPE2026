# Independent Ornstein–Uhlenbeck boundary layers under hard quadratic Brownian confinement

## Finding
Let \(B\) be standard one-dimensional Brownian motion. Fix \(x,\mu\in\mathbb R\), \(\theta>0\), \(S>0\), and, for \(T>2S\), define \(W_t=x+\mu t+B_t\) and the hard occupation-budget event
\[
 A_T=\left\{\int_0^T W_t^2\,dt\le\theta T\right\}.
\]
As \(T\to\infty\), conditionally on \(A_T\), the ordered pair of paths \(((W_t)_{0\le t\le S},(W_{T-r})_{0\le r\le S})\) converges weakly in \(C([0,S])\times C([0,S])\) to independent processes \(X\) and \(Y\) satisfying
\[
 dX_t=dB_t^{(1)}-\omega X_t\,dt,\quad X_0=x,\qquad
 dY_r=dB_r^{(2)}-\omega Y_r\,dr,\quad
 Y_0\sim N(2\theta\mu,2\theta),\quad \omega=\frac1{2\theta}.
\]
The two Brownian drivers are independent and independent of \(Y_0\); \(X_0\) is deterministic. In particular, the backward terminal window is not stationary at its free endpoint:
\[
 \mathbb EY_r=2\theta\mu e^{-\omega r},\qquad
 \operatorname{Cov}(Y_r,Y_s)=\theta\bigl(e^{-\omega|r-s|}+e^{-\omega(r+s)}\bigr).
\]
Its endpoint variance is \(2\theta\), twice the bulk stationary Ornstein–Uhlenbeck variance \(\theta\). The initial-window covariance has the *minus* reflection term \(\theta(e^{-\omega|s-t|}-e^{-\omega(s+t)})\), and all cross-boundary covariances vanish in the limit.

## Assumptions and scope
The drift \(\mu\), start \(x\), budget parameter \(\theta\), and observation length \(S\) are fixed as \(T\to\infty\). The conditioning event has positive probability for finite \(T\). Reversed time is \(r=T-t\); this is not a reversal of the unconditioned Brownian law. The convergence is joint weak convergence of continuous-path measures, not merely one-time marginals or a statement about the process on time intervals of length proportional to \(T\).

## Proof
**1. Exact Gaussian transform.** Work first under driftless Brownian motion with starting value \(x\), and write \(Z_T=\int_0^T W_t^2\,dt\). The Cameron–Martin formula cancels the constant factor and reduces the desired conditional law to driftless paths weighted by \(e^{\mu W_T}\): for every bounded measurable path functional \(F\),
\[
 \mathbb E_x^\mu[F\mid A_T]
 =\frac{\mathbb E_x^0[F e^{\mu W_T}\mathbf1_{\{Z_T\le\theta T\}}]}{\mathbb E_x^0[e^{\mu W_T}\mathbf1_{\{Z_T\le\theta T\}}]}.
\]
For complex \(u\) with \(\Re u>0\), choose the square root \(w=\sqrt{2u}\) with \(\Re w>0\). Completing the Gaussian square (or solving the harmonic-oscillator Feynman–Kac equation) gives
\[
 L_T(u):=\mathbb E_x^0e^{-uZ_T}
 =\frac{\exp[-wx^2\tanh(wT)/2]}{\sqrt{\cosh(wT)}}.
\]
Under this unnormalized quadratic tilt, every finite vector of \(W\)-coordinates has a Gaussian generating function with mean
\[
 m_{T,u}(t)=x\frac{\cosh(w(T-t))}{\cosh(wT)}
\]
and covariance kernel
\[
 C_{T,u}(s,t)=\frac{\sinh(w\min(s,t))\cosh(w(T-\max(s,t)))}{w\cosh(wT)}.
\]
These formulas continue analytically from real \(u>0\) to the right half-plane. Indeed, \(m\) solves the homogeneous equation \((-\partial_t^2+2u)m=0\) with \(m(0)=x\), \(m'(T)=0\), while \(C\) is the Green kernel with \(C(0,t)=0\), \(\partial_s C(T,t)=0\), and derivative jump \(-1\). Consequently, if \(t_j\in[0,T]\) and \(z_j\in\mathbb C\),
\[
 \mathbb E_x^0\exp[-uZ_T+\sum_j z_jW_{t_j}]
 =L_T(u)\exp\!\left(\sum_j z_jm_{T,u}(t_j)+\frac12\sum_{i,j}z_i z_jC_{T,u}(t_i,t_j)\right). \tag{1}
\]

**2. Two boundary limits.** Let \(t,s,r,v\in[0,S]\) stay fixed and let \(T\to\infty\), locally uniformly in \(\Re u>0\). Elementary hyperbolic expansions yield
\[
\begin{aligned}
 m_{T,u}(t)&\to xe^{-wt},&m_{T,u}(T-r)&\to0,\\
 C_{T,u}(s,t)&\to C^-_w(s,t):=\frac{e^{-w|s-t|}-e^{-w(s+t)}}{2w},\\
 C_{T,u}(T-r,T-v)&\to C^+_w(r,v):=\frac{e^{-w|r-v|}+e^{-w(r+v)}}{2w},\\
 C_{T,u}(t,T-r)&\to0.&&
\end{aligned}\tag{2}
\]
The plus sign in the terminal reflection term comes from the free (Neumann) right boundary; the minus sign at the initial boundary comes from the fixed (Dirichlet) start. In particular, \(C^+_w(0,0)=1/w\), not the stationary covariance \(1/(2w)\).

**3. Exact hard-budget inversion and saddle localization.** Put \(u_*=1/(8\theta^2)\), \(w_*=1/(2\theta)\), and take any finite list of observation times from the two windows. Incorporate the real coefficient \(\mu\) of \(W_T\) and arbitrary imaginary Fourier coefficients of observed coordinates into the Gaussian factor \(H_T(u)\) on the right-hand side of (1). Bromwich inversion, applied to the absolutely continuous weighted distribution function of \(Z_T\), writes the desired weighted expectation as
\[
 I_T(H_T)=\frac{1}{2\pi}\int_{\mathbb R}
 \frac{e^{(u_*+iv)\theta T}L_T(u_*+iv)H_T(u_*+iv)}{u_*+iv}\,dv. \tag{3}
\]
The conditional finite-dimensional characteristic function equals \(I_T(H_T)/I_T(H_T^{\rm den})\), where \(H_T^{\rm den}\) contains only the real terminal coefficient \(\mu\). This identity is for a *hard inequality*, not just the exponentially tilted ensemble.

Here are the contour estimates needed to use (3). Along \(u=u_*+iv\), \(\Re w\ge w_*\) and, for sufficiently large \(T\), the hyperbolic formulas imply \(|L_T(u)|\le C e^{-T\Re w/2}\). For coefficients at finitely many locations in the two fixed windows, \(|H_T(u)|\le C\) uniformly in real \(v\); this follows from the bounds on \(m_{T,u}\), \(C_{T,u}\), and \(|w|^{-1}\le w_*^{-1}\). Moreover, \(\Re w-w_*>0\) except at \(v=0\), has quadratic growth there, and grows like \(\sqrt{|v|}\) in the tails. Thus the contour contribution outside every shrinking saddle neighborhood is negligible compared with the integral at \(v=0\). More explicitly, for
\[
 f(u)=\theta u-\tfrac12\sqrt{2u},\qquad
 f'(u_*)=0,\qquad f''(u_*)=4\theta^3,
\]
putting \(v=y/\sqrt T\) shows that the normalized local integrand has the Gaussian weight \(e^{-2\theta^3y^2}\). Formula (2) shows \(H_T(u_*+iy/\sqrt T)\to H_\infty(u_*)\) uniformly on compact \(y\)-sets. The leading denominator is nonzero and positive, with terminal factor \(\exp(\mu^2/(2w_*))\). Consequently
\[
 \lim_{T\to\infty}\frac{I_T(H_T)}{I_T(H_T^{\rm den})}
 =\frac{H_\infty(u_*)}{H_\infty^{\rm den}(u_*)}. \tag{4}
\]
The ratio on the right is exactly the characteristic function of two independent Gaussian boundary vectors with means and covariances as in (2), except that exponential tilting by \(e^{\mu W_T}\) shifts the terminal mean by \(\mu C^+_{w_*}(r,0)=\mu e^{-w_*r}/w_*=2\theta\mu e^{-r/(2\theta)}\). It does not alter either covariance or the cross-boundary independence.

**4. Tightness and continuous-path convergence.** The established initial-window conditioned-path theorem of Aurzada–Dutta–Wiegand (Theorem 1, fixed drift case) supplies tightness of \((W_t)_{0\le t\le S}\). We give the separate terminal-window estimate, because terminal tightness does not follow from an initial-window theorem. In the complex Gaussian transform (1), for \(0\le r,s\le S\) and \(T\ge2S+1\), the covariance of \(\Delta=W_{T-r}-W_{T-s}\) obeys \(|\operatorname{Cov}_u(\Delta,\Delta)|\le C|r-s|\), uniformly on the contour \(\Re u=u_*\). Indeed, substituting the displayed hyperbolic kernel and using \(|1-e^{-w h}|\le |w|h\) whenever \(\Re w\ge0\) bounds the differences; the exponentially small reflected corrections have the same Lipschitz bound. Likewise \(|m_{T,u}(T-r)-m_{T,u}(T-s)+\mu\operatorname{Cov}_u(\Delta,W_T)|\le C|r-s|\), since both the terminal mean and terminal covariance with \(W_T\) are uniformly Lipschitz in backward time. The Gaussian fourth-moment identity therefore bounds the corresponding transformed fourth increment moment by \(C|r-s|^2|L_T(u)H_T^{\rm den}(u)|\). Integrating along (3), using the preceding contour absolute estimates and its positive saddle denominator, yields, for all sufficiently large \(T\),
\[
 \mathbb E_x^\mu[|W_{T-r}-W_{T-s}|^4\mid A_T]\le C_S|r-s|^2. \tag{5}
\]
The endpoint laws are tight by (4). Kolmogorov's criterion gives tightness of the reversed terminal window in \(C([0,S])\). Together with tightness of the initial window and the finite-dimensional convergence (4), this proves joint weak path convergence. The two limiting Gaussian processes have the asserted Ornstein–Uhlenbeck dynamics because the covariance \(C^-\) is that of the OU process started at \(x\), while \(C^+\) is that of an OU process with independent starting variance \(1/w_*=2\theta\).

## Verification
The included standalone standard-library program `verification.py` checks the exact complex-Gaussian kernels against a separate discrete Brownian tridiagonal resolvent, tests their boundary ODE conditions and derivative jump, confirms both boundary covariance limits and asymptotic cross-boundary decoupling, checks saddle curvature, and verifies the terminal exponential-tilt shift. It passes 569 deterministic assertions. These finite numerical checks do not prove the hard-budget inversion, localization, or tightness; those steps are analytical above.

## Relationship to prior work
Aurzada–Dutta–Wiegand, arXiv:2610.12354v1 (2026), prove exact hard-budget small-deviation probabilities and convergence on *fixed initial* intervals to an OU diffusion independent of the original drift. Their discussion notes heuristically that drift can remain influential close to the terminal time, but does not give a joint two-boundary path law. Our initial-window limit and the basic Laplace transform are established inputs, not new claims. Their scalar small-deviation asymptotic also implies the **one-time** terminal Gaussian law by a Cameron–Martin ratio, so the terminal scalar marginal alone is **not** asserted as new. The additional statement is the complete reversed-terminal window process, its Neumann reflection covariance and the asymptotic independence of *both* windows under **hard** conditioning.

Schmidt, arXiv:2608.19744 (2026), proves broad fixed-*initial*-window microcanonical/canonical equivalence and sharp probability asymptotics for confining potentials. Its stated theorems do not include the joint reversed-terminal window with its Gaussian reflecting boundary. Chetrite–Touchette, arXiv:1405.5157 (2014), establish general logarithmic path-measure equivalence and driven-process constructions for additive rare events; those results alone do not imply the exact fixed-width terminal law or its reflection covariance. These comparisons do not claim uniqueness among all published mathematics.

## Limitations
The theorem is for fixed \(x,\mu,\theta,S\), one-dimensional Brownian motion, and a quadratic integral constraint. It does not assert the same limit with growing drift or windows, total-variation convergence on the double path space, a rate of convergence, or independence at finite \(T\). Independence arises only in the joint limit. The explicit Gaussian transform makes the result special to this model. Independent literature and proof auditing remain to be performed.

## References
1. F. Aurzada, Y. Dutta, M. Wiegand, *Brownian motion with drift conditioned to have restricted L²-norm*, arXiv:2610.12354v1, 8 October 2026, https://arxiv.org/html/2610.12354v1.
2. T. Schmidt, *Conditioned Brownian motion and local equivalence of path ensembles*, arXiv:2608.19744v1, 20 August 2026, https://arxiv.org/abs/2608.19744.
3. R. Chetrite, H. Touchette, *Nonequilibrium Markov processes conditioned on large deviations*, arXiv:1405.5157, 2014, https://arxiv.org/abs/1405.5157.
