# Unique switching optimum and sharp memory-duration boundary in the colored-noise Ising–Kuramoto response

## Finding

Consider the Ornstein–Uhlenbeck (OU) first-harmonic linear-response threshold of the dynamic Ising–Kuramoto model. Its finite-switching optimum is **unique whenever present**, and it disappears at a sharp, unique correlation-time boundary. This resolves the existence, uniqueness and parameter classification of the finite-rate optimum for the specific susceptibility given below; it is not a theorem about fully nonlinear synchrony.

For \(D,\tau,\mu,\beta_s>0\) and \(\gamma\ge0\), define
\[
G_\tau(t)=\exp\!\left[-D\left(t-\tau(1-e^{-t/\tau})\right)\right],\quad
\chi_\gamma(\tau)=\frac12\int_0^\infty e^{-\gamma t}G_\tau(t)\,dt,\quad
K_c(\gamma,\tau)=\frac1{(\mu+\beta_s\gamma)\chi_\gamma(\tau)}.
\]
Write \(c=\mu/\beta_s\) and
\[
M_k(\gamma,\tau)=\int_0^\infty t^k e^{-\gamma t}G_\tau(t)\,dt,\qquad
c_*(\tau)=\frac{M_0(0,\tau)}{M_1(0,\tau)}.
\]
The following statements hold for every indicated parameter, with no restriction to a numerical parameter sample.

1. **Complete optimum classification.** If \(c\ge c_*(\tau)\), \(K_c(\gamma,\tau)\) has its unique global minimum at \(\gamma=0\) and is strictly increasing for \(\gamma>0\). If \(0<c<c_*(\tau)\), it has a unique strict global minimum \(\gamma_*(\tau)>0\), is strictly decreasing before that minimum and strictly increasing thereafter.

2. **Sharp memory-duration boundary.** The function \(c_*:(0,\infty)\to(0,D)\) is continuous and strictly decreasing, with
\[
\lim_{\tau\downarrow0}c_*(\tau)=D,\qquad
c_*(\tau)\sim \sqrt{\frac{\pi D}{2\tau}}\quad(\tau\to\infty).
\]
For each \(0<c<D\), there is exactly one \(\tau_c>0\) satisfying \(c_*(\tau_c)=c\); a strictly positive optimum exists exactly when \(0<\tau<\tau_c\). For \(c\ge D\) no positive-rate optimum exists at any \(\tau>0\).

3. **Singular short-memory optimizer.** For each fixed \(0<c<D\), with \(\kappa=c/D\),
\[
\lim_{\tau\downarrow0}\tau\gamma_*(\tau)
=\frac{\sqrt{1-\kappa}}{1-\sqrt{1-\kappa}}.
\]
In particular, the optimum diverges like \(\tau^{-1}\) even though at exactly zero memory the response is Markovian.

## Assumptions and scope

The quantities \(D>0\), \(\tau>0\), \(\mu>0\), \(\beta_s>0\) and \(\gamma\in[0,\infty)\) are real. The OU correlation \(G_\tau\) and linear-response threshold are **definitions of the object optimized**. All integrals and their first derivatives converge since \(G_\tau(t)\le e^{D\tau}e^{-Dt}\). All statements concern the nonmagnetic incoherent state's linear first-harmonic response in this specific model; they do not assert a phase diagram for nonlinear stationary solutions, finite-system bistability, nor a physical minimum under independently imposed bounds on \(\gamma\).

## Proof

**Step 1: Derivative and one-crossing structure.** Put
\[
h_\tau(t)=-\partial_t\log G_\tau(t)=D(1-e^{-t/\tau}),
\qquad F(\gamma)=(\mu+\beta_s\gamma)\chi_\gamma(\tau)
=\frac{\beta_s}{2}(\gamma+c)M_0(\gamma,\tau).
\]
The function \(h_\tau\) is strictly increasing from zero to \(D\). Integration by parts, with \(t e^{-\gamma t}G_\tau(t)\) vanishing at both ends, gives
\[
M_0(\gamma,\tau)-\gamma M_1(\gamma,\tau)
=\int_0^\infty t h_\tau(t)e^{-\gamma t}G_\tau(t)\,dt.
\]
Hence
\[
F'(\gamma)=\frac{\beta_s}{2}\left[M_0-(\gamma+c)M_1\right]
=\frac{\beta_s}{2}\int_0^\infty t(h_\tau(t)-c)e^{-\gamma t}G_\tau(t)\,dt.
\tag{1}
\]
If \(c\ge D\), the integrand in (1) is strictly negative for \(t>0\). Since \(K_c=1/F>0\), its minimum is uniquely at zero.

For \(0<c<D\), set \(t_0=-\tau\log(1-c/D)\). Define the strictly positive contributions
\[
P_\gamma=\int_0^{t_0}t(c-h_\tau(t))e^{-\gamma t}G_\tau(t)\,dt,
\qquad N_\gamma=\int_{t_0}^\infty t(h_\tau(t)-c)e^{-\gamma t}G_\tau(t)\,dt.
\]
The sign of \(F'\) is that of \(N_\gamma-P_\gamma\). Their ratio \(R=N/P\) is strictly decreasing, because
\[
\frac{d}{d\gamma}\log R(\gamma)
=-\frac{\int_{t_0}^\infty t^2(h_\tau-c)e^{-\gamma t}G_\tau\,dt}{N_\gamma}
+\frac{\int_0^{t_0}t^2(c-h_\tau)e^{-\gamma t}G_\tau\,dt}{P_\gamma}<0.
\]
Indeed, the first weighted mean time exceeds \(t_0\) and the second lies below \(t_0\). Further, \(R(\gamma)\to0\) as \(\gamma\to\infty\): the positive sector is separated from zero by \(t_0\), whereas the negative sector has positive mass arbitrarily near zero. Finally,
\[
F'(0)=\frac{\beta_s}{2}\bigl(M_0(0,\tau)-cM_1(0,\tau)\bigr).
\]
Thus \(R(0)>1\) exactly when \(c<c_*(\tau)\); in that case it crosses one exactly once, from above, giving the unique strict global maximum of \(F\) and unique strict global minimum of \(K_c\). If \(R(0)\le1\), \(F'<0\) for all \(\gamma>0\). This covers the equality boundary, with no other local/global extrema.

**Step 2: Strict memory monotonicity and endpoints.** For \(\tau_2>\tau_1>0\),
\[
\frac{d}{dt}\log\frac{G_{\tau_2}(t)}{G_{\tau_1}(t)}
=h_{\tau_1}(t)-h_{\tau_2}(t)>0\qquad(t>0).
\]
Thus the probability density proportional to \(G_{\tau_2}\) is a strictly increasing likelihood-ratio tilt of the one proportional to \(G_{\tau_1}\). Its mean time \(M_1(0,\tau)/M_0(0,\tau)\) is strictly greater. Therefore \(c_*(\tau)\) decreases strictly; dominated convergence on every compact positive-\(\tau\) interval gives continuity. As \(\tau\downarrow0\), \(G_\tau(t)\to e^{-Dt}\), and dominated convergence gives \(M_0\to D^{-1}\) and \(M_1\to D^{-2}\), hence \(c_*\to D\).

For the large-memory endpoint substitute \(t=\sqrt\tau u\). The exponent becomes
\(D\tau[u/\sqrt\tau-1+e^{-u/\sqrt\tau}]\to Du^2/2\).
The bound \(s-1+e^{-s}\ge s^2/[2(1+s)]\) for \(s\ge0\) supplies an integrable dominator \(u^k e^{-Du^2/[2(1+u)]}\) when \(\tau\ge1\). Therefore
\[
M_0(0,\tau)\sim\sqrt\tau\int_0^\infty e^{-Du^2/2}\,du
=\sqrt{\frac{\pi\tau}{2D}},\quad
M_1(0,\tau)\sim\tau\int_0^\infty u e^{-Du^2/2}\,du=\frac\tau D.
\]
The stated asymptotic and unique crossing \(\tau_c\) follow from strict monotonicity and the intermediate-value theorem.

**Step 3: Singular small-\(\tau\) scaling.** Fix \(c/D=\kappa\in(0,1)\), set \(t=\tau u\), \(\gamma=b/\tau\), and \(a=D\tau\). Up to a positive factor, the derivative in (1) is
\[
J_a(b)=\int_0^\infty u(1-e^{-u}-\kappa)
\exp\!\big[-bu-a(u-1+e^{-u})\big]\,du.
\]
For each \(b>0\), uniformly on compact positive intervals of \(b\), dominated convergence gives
\[
J_a(b)\longrightarrow \frac{1-\kappa}{b^2}-\frac1{(b+1)^2}.
\]
The limiting expression has a unique positive zero
\(b_0=\sqrt{1-\kappa}/(1-\sqrt{1-\kappa})\), is positive below \(b_0\) and negative above. By Step 1, for all sufficiently small \(\tau\) the derivative has exactly one positive zero; fixing any two test points on opposite sides of \(b_0\) traps \(\tau\gamma_*(\tau)\) between them. Letting the test points converge to \(b_0\) establishes the claimed limit.

## Verification

The self-contained supplementary program `verification/check_response.py` requires SciPy; run `python verification/check_response.py`. It separately computes \(M_0\), \(M_1\), evaluates equation (1) by a second quadrature, brackets stationary points and checks sign changes for a grid of positive \(D\), \(\tau\) and \(c\). The included program passes 908 assertions with SciPy in a standard Python environment.

For \(D=1\) and \(\mu/\beta_s=1/2\), the computed sharp memory boundary is \(\tau_c\approx4.2214624401713\). There is a positive optimizer at \(\tau=3\), about \(\gamma_*=0.2273477\), but not at \(\tau=5\). The singular short-memory constant in this example is \(\sqrt2+1\approx2.41421356237\). Finite quadrature confirms sample instances only; the preceding analytic arguments prove the universal claims.

## Relationship to prior work

Hayashi [1] derives exactly the OU first-harmonic susceptibility and its competition between linear growth in switching response and decreasing memory susceptibility. The source provides a sufficient condition for an interior optimum and numerical finite-rate examples. The contribution here is the **necessary-and-sufficient global optimizer classification**, strict uniqueness for all positive parameters, the **unique memory-duration boundary** at which the finite-rate optimum vanishes, and the singular short-memory scale. These statements are not attributed to the original source. Related prior analyses of Kuramoto oscillators with colored frequency noise [2] do not contain the spin-switching prefactor; the switched temporal networks in [3] concern distinct coupling architecture and optimization. Standard single-crossing/Laplace-transform variation principles provide general background but do not by themselves supply this model's explicit memory boundary.

## Limitations

No claim is made about nonlinear global stability, finite-size switching stochasticity, abrupt order-disorder transitions, non-OU correlation kernels or uniqueness of a minimizer under additional cost terms. The \(\tau\downarrow0\) optimizer diverges, so the limit does not commute with fixing a bounded switching rate. The existence of a finite positive optimum refers only to the linear-response formula in the assumptions. Priority assessment remains best-knowledge and has not received independent literature-wide confirmation.

## References

[1] R. Hayashi, *Memory-induced optimal switching in a dynamic Ising–Kuramoto model*, arXiv:2609.35838v1 (first public 2026-09-24), https://arxiv.org/abs/2609.35838.

[2] R. Tönjes, *Synchronization Transition in the Kuramoto Model with Colored Noise*, arXiv:1003.1549 (2010), https://arxiv.org/abs/1003.1549.

[3] Y. Zhang and S. H. Strogatz, *Designing temporal networks that synchronize under resource constraints*, arXiv:2101.02721 (2021), https://arxiv.org/abs/2101.02721.

[4] L. Chen, C. Qiu, and X. Huang, *Synchronization with on-off coupling: Role of time scales in network dynamics*, Physical Review E 79, 045101 (2009), https://doi.org/10.1103/PhysRevE.79.045101.
