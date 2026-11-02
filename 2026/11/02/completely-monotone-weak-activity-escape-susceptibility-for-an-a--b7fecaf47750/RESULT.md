# Completely monotone weak-activity escape susceptibility for an absorbing active-Brownian disk

## Finding
For a planar active Brownian particle in a fully absorbing disk, the orientationally averaged mean exit time has an exact second-order small-propulsion coefficient at **every initial radius**. This coefficient is strictly completely monotone in rotational diffusivity: every successive derivative has the alternating sign. It interpolates between an exact persistent-orientation polynomial and a sharp fast-reorientation law.

More precisely, set \(s=|x_0|/R\in[0,1)\), \(p=vR/D\), and \(g=D_{\mathrm{rot}}R^2/D>0\). If the initial orientation is independent and uniform, then, as \(p\to0\) with \(g\) fixed,
\[
\frac{D}{R^2}\mathbb E_{x_0,\mathrm{unif}}\tau_R
=\frac{1-s^2}{4}-p^2 C_g(s)+O_g(p^4),
\]
where
\[
\boxed{C_g(s)=\frac{1}{4g}\left[\frac{1-s^2}{2}-\frac{I_0(\sqrt g)-I_0(s\sqrt g)}{\sqrt g\,I_1(\sqrt g)}\right].}
\]
Here \(I_0,I_1\) are modified Bessel functions. For every fixed \(0\le s<1\), every integer \(n\ge0\), and every \(g>0\),
\[
\boxed{(-1)^n\partial_g^n C_g(s)>0.}
\]
In particular, weak propulsion strictly decreases the mean exit time at each initial radius, and the magnitude of the decrease strictly declines as rotational diffusion increases. The sharp endpoint laws are
\[
\lim_{g\downarrow0}C_g(s)=\frac{(1-s^2)^2}{128},\qquad
\lim_{g\to\infty}gC_g(s)=\frac{1-s^2}{8}.
\]
The second limit is pointwise for fixed \(s<1\), not uniform near the absorbing rim.

## Assumptions and scope
Let \(B_t\) be standard planar Brownian motion and \(W_t\) an independent standard real Brownian motion. Before absorption at the circle \(|x|=R\), with \(R,D>0\), \(v\in\mathbb R\), and \(D_{\mathrm{rot}}>0\), the particle obeys
\[
 dX_t=v(\cos\Theta_t,\sin\Theta_t)\,dt+\sqrt{2D}\,dB_t,\qquad
 d\Theta_t=\sqrt{2D_{\mathrm{rot}}}\,dW_t\pmod{2\pi}.
\]
The exit time is \(\tau_R=\inf\{t\ge0:|X_t|\ge R\}\). The initial position satisfies \(|x_0|<R\), and the initial angle is independent and Haar-uniform on the circle. The circle is absorbing in every direction: there are no reflecting arcs, resetting events, or boundary-interaction torques. The expansion is for small signed propulsion \(p\) at fixed \(g>0\); negative signed propulsion is equivalent to shifting all angles by \(\pi\). The model has positive translational diffusivity, so the bounded-domain Dirichlet Poisson problem is well posed.

## Proof
**1. Backward equation and normalization.** Measure distances in units of \(R\), times in units of \(R^2/D\), and let \(T_p(z,\theta)\) be the corresponding mean exit time. On the unit disk it uniquely solves
\[
(\Delta_z+g\partial_\theta^2+p\,u_\theta\cdot\nabla_z)T_p=-1,
\qquad T_p|_{|z|=1}=0,
\]
with \(u_\theta=(\cos\theta,\sin\theta)\). Since the diffusive Dirichlet inverse is bounded and the first-order drift is relatively bounded, the Dirichlet solution is analytic for sufficiently small \(|p|\) at each fixed \(g>0\). Expand \(T_p=T_0+pT_1+p^2T_2+\cdots\); uniform orientation averages eliminate all odd powers by the symmetry \((p,\theta)\mapsto(-p,\theta+\pi)\).

**2. First angular harmonic.** Write \(\rho=|z|\) and \(\delta=\theta-\arg z\). The zeroth-order solution is \(T_0=(1-\rho^2)/4\). The first-order equation is \((\Delta+g\partial_\theta^2)T_1=\rho\cos\delta/2\). Therefore \(T_1=h_g(\rho)\cos\delta\), where the regular Dirichlet solution satisfies
\[
 h_g''+\rho^{-1}h_g'-\rho^{-2}h_g-gh_g=\rho/2,
 \qquad h_g(1)=0,
\]
and has the explicit form
\[
 h_g(\rho)=\frac{I_1(\sqrt g\,\rho)/I_1(\sqrt g)-\rho}{2g}.
\]
At the origin take the regular limit \(h_g(0)=0\). The formula follows from the order-one modified-Bessel differential equation and the elementary particular solution \(-\rho/(2g)\).

**3. Second-order orientation average.** Denote \(w_g(\rho)=\frac1{2\pi}\int_0^{2\pi}T_2(\rho,\theta)\,d\theta\). Since \(u_\theta\cdot\nabla(h_g(\rho)\cos\delta)=h_g'(\rho)\cos^2\delta+(h_g(\rho)/\rho)\sin^2\delta\), the angularly averaged second-order equation is
\[
 w_g''+\rho^{-1}w_g'=-\tfrac12(h_g'+h_g/\rho),
 \qquad w_g(1)=0.
\]
Radial regularity removes the integration constant and yields \(w_g'=-h_g/2\), hence \(w_g(s)=\frac12\int_s^1h_g(\rho)\,d\rho\). Setting \(C_g=-w_g\) and integrating \(I_1\) gives the boxed closed form in the finding. This computation is an exact coefficient identity, not a finite-order simulation of the full dynamics.

**4. Four-dimensional resolvent lift and strict complete monotonicity.** Put \(u_g=-h_g\) and \(u_g(\rho)=\rho f_g(\rho)\). The differential equation above becomes
\[
 -f_g''-\frac3\rho f_g'+gf_g=\frac12,
 \quad f_g(1)=0,\quad f_g'(0)=0.
\]
This is exactly the radial Dirichlet problem \((-\Delta_4+g)f_g=1/2\) on the **unit ball in four dimensions**, with the Laplacian normalized as the generator of \(\sqrt2\)-Brownian motion. Let \(\sigma_4\) be the first exit time of that Brownian motion from the four-ball, started at radius \(\rho\). The killed-diffusion resolvent gives
\[
 f_g(\rho)=\frac12\mathbb E_\rho\int_0^{\sigma_4}e^{-gt}\,dt,\qquad
 C_g(s)=\frac14\int_s^1\rho\,\mathbb E_\rho\int_0^{\sigma_4}e^{-gt}\,dt\,d\rho.
\]
The integrand is positive, and the exit time from the bounded four-ball has moments of every order. Differentiation under the integral for every integer \(n\ge0\) gives
\[
 (-1)^n\partial_g^nC_g(s)=\frac14\int_s^1\rho\,\mathbb E_\rho\int_0^{\sigma_4}t^n e^{-gt}\,dt\,d\rho>0
\]
for \(s<1\). This proves the entire hierarchy, including strict monotonic decrease and strict convexity. The dimension lift is exact; it is not a replacement of the active particle by a four-dimensional physical trajectory.

**5. Endpoint limits.** At \(g=0\), the four-dimensional Poisson equation has the explicit radial solution \(f_0(\rho)=(1-\rho^2)/16\). Integrating \(\frac12\rho f_0\) over \([s,1]\) gives \(C_0(s)=(1-s^2)^2/128\). For \(g\to\infty\), either the Bessel expression or the resolvent identity gives \(g f_g(\rho)\to1/2\) at every fixed \(0\le\rho<1\). Dominated convergence in the radial integral (or the Bessel asymptotics) yields \(gC_g(s)\to(1-s^2)/8\). At the absorbing rim \(s=1\), \(C_g(1)=0\) identically, and boundary-layer behavior prevents a uniform version of the large-\(g\) relative asymptotic.

## Verification
Run `python verify.py` with Python 3, SciPy, SymPy, NumPy, and mpmath. Its independent four-dimensional radial shooting solver checks 25 Bessel-coefficient values without invoking Bessel functions in the shooting computation. It verifies the zero-rotation polynomial in the differential equations, checks 60 alternating derivative signs by high-precision differentiation, and tests both asymptotic limits. The actual program was executed successfully. These finite checks support the exact argument but do not certify the infinite derivative statement; the killed-diffusion resolvent identity supplies the proof.

## Relationship to prior work
Di Trapani, Franosch, and Caraglio [1] formulate exactly this absorbing-disk active-Brownian model and solve the time-dependent propagator and survival probability using eigenfunction expansions. In their discussion they explicitly identify mean first-passage moments as further quantities their framework *could* calculate; the present exact radial coefficient, four-dimensional lift, and complete-monotonicity hierarchy are not asserted there. The general propagator certainly contains the information implicitly, a substantive prior-coverage risk: the new claim is the evaluated, quantitatively sharp, all-radius weak-activity comparison and its strict all-derivatives law, not the existence of a propagator.

Scacchi and Sharma [2] study first passage in one dimension using telegraph propulsion, resetting, and effective-diffusivity approximations, not the two-dimensional absorbing disk with continuous angular diffusion. Iyaniwura, Qiu, and Peng [3] analyze a later chiral model, with absorbing arcs and reflecting remainder in two dimensions, and obtain numerical mean exit times there; their analytic asymptotics concern one-dimensional high chirality. Those geometries and scalings do not give the present four-dimensional resolvent, exact \(p^2\)-coefficient, or alternating derivative hierarchy. Comparisons of mathematical research records and prior claims yielded no direct matching formula or dominating theorem, though the literature search is not a proof of publication priority.

## Limitations
This is a weak-activity expansion; it does not prove global monotonicity in arbitrary propulsion strength nor finite-propulsion ordering for every initial orientation. Complete monotonicity concerns the **leading quadratic activity susceptibility**, not the full mean exit time as a function of rotational diffusivity. The rapid-rotation limit is pointwise away from the absorbing edge. The result assumes independent translational and rotational Brownian noises and a completely absorbing circular boundary; reflecting arcs, torque-dependent direction, spatially varying propulsion, and interacting particles are not covered. An independent mathematical audit and definitive publication-priority determination have not been performed.

## References
[1] F. Di Trapani, T. Franosch and M. Caraglio, *Active Brownian Particles in a Circular Disk with an Absorbing Boundary*, arXiv:2306.12702v1, first public submission 2023-06-22; https://arxiv.org/html/2306.12702v1 (Phys. Rev. E 107, 064123, 2023).

[2] A. Scacchi and A. Sharma, *Mean first passage time of active Brownian particle in one dimension*, arXiv:1708.05591v2, https://arxiv.org/html/1708.05591v2 (Molecular Physics 116, 460–464, 2018).

[3] S. A. Iyaniwura, M. Qiu and Z. Peng, *Mean first passage time of chiral active Brownian particles*, arXiv:2605.23095v2, https://arxiv.org/html/2605.23095v2 (Soft Matter 22, 4489–4504, 2026).
