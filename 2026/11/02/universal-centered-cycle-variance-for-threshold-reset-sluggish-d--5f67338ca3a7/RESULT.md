# Universal centered-cycle variance for threshold-reset sluggish diffusion

## Finding
Fix \(\alpha\geq0\), \(L>0\), and \(0<\rho<1\). Consider the one-dimensional natural-scale diffusion with generator \(\mathcal Lf(x)=|x|^{-\alpha}f''(x)\) inside \((-L,L)\), instantaneously restarted at \(x_0=\rho L\) upon hitting either endpoint. Let
\[
F_T=\frac1T\int_0^T \mathbf{1}_{\{X_t>0\}}\,dt,
\qquad
\theta_{\alpha}(\rho)=1-\frac{1-\rho}{2(1-\rho^{\alpha+2})}.
\]
For every fixed admissible triple \((\alpha,L,\rho)\), the following central limit theorem holds as \(T\to\infty\):
\[
\sqrt T\bigl(F_T-\theta_{\alpha}(\rho)\bigr)
\ \Longrightarrow\ N\bigl(0,\mathcal V_{\alpha,L}(\rho)\bigr),
\]
where the **exact positive variance coefficient** is
\[
\boxed{\displaystyle
\mathcal V_{\alpha,L}(\rho)=
\frac{3(\alpha+1)L^{\alpha+2}(1-\rho^2)}
{4(\alpha+2)(\alpha+3)(2\alpha+3)(1-\rho^{\alpha+2})}.}
\]
The exact centered second moment of a single stopped excursion is also universal in its restart-point dependence. If \(\tau\) is its first exit time and \(A=\int_0^\tau(\mathbf{1}_{\{X_t>0\}}-\theta_{\alpha}(\rho))\,dt\), then
\[
\boxed{\displaystyle
\mathbb EA^2=
\frac{3L^{2\alpha+4}(1-\rho^2)}
{4(\alpha+2)^2(\alpha+3)(2\alpha+3)}.}
\]
In particular, for ordinary Brownian diffusion (\(\alpha=0\)), the Gaussian fluctuation coefficient is exactly \(L^2/24\), independent of the positive restart position. For every \(\alpha>0\), it decreases **strictly** as \(\rho\) increases. Its sharp one-sided endpoint limits are
\[
\lim_{\rho\downarrow0}\mathcal V_{\alpha,L}(\rho)=
\frac{3(\alpha+1)L^{\alpha+2}}{4(\alpha+2)(\alpha+3)(2\alpha+3)},
\]
\[
\lim_{\rho\uparrow1}\mathcal V_{\alpha,L}(\rho)=
\frac{3(\alpha+1)L^{\alpha+2}}{2(\alpha+2)^2(\alpha+3)(2\alpha+3)}.
\]
These are limits from inside the open parameter interval; they do not assert that an instantaneous-restart process is defined at \(\rho=1\).

## Assumptions and scope
The diffusion is specified unambiguously as a time change of Brownian motion with generator \(d^2/dx^2\): stop a Brownian path \(B_s\), started at \(x_0\), upon exiting \((-L,L)\), and use the strictly increasing physical clock \(t(s)=\int_0^s|B_u|^\alpha\,du\). The inverse-clock path is the diffusion with the displayed generator. Construct each new excursion independently after its exit. This definition also covers the singular coefficient at the origin for \(\alpha>0\); no sticky holding at zero is imposed. At \(\alpha=0\), it is Brownian motion of variance \(2t\). The observable assigns no time at the origin almost surely.

Every statement concerns the continuum threshold-reset model, not a finite-spacing lattice approximation. The restart ratio stays strictly between zero and one, with \(\alpha\) and \(L\) fixed as \(T\) grows. The result holds when started at a restart time; starting in the stationary regenerative regime yields the same central limit law.

## Proof
Let \(q=\alpha+1\), first set \(L=1\), and put \(s=\rho\). The stopped Brownian Green function for \(-d^2/dx^2\) is
\[
G(s,y)=\tfrac12
\begin{cases}
(1-s)(1+y),&-1<y\leq s,\\
(1+s)(1-y),&s\leq y<1.
\end{cases}
\]
The diffusion's expected physical occupation density before exit is \(G(s,y)|y|^{q-1}\). Consequently
\[
m:=\mathbb E_s\tau=\frac{1-s^{q+1}}{q(q+1)},
\qquad
\mathbb E_s\int_0^\tau\mathbf{1}_{\{X_t<0\}}\,dt
=\frac{1-s}{2q(q+1)}.
\]
Thus, defining
\[
\eta=1-\theta=\frac{1-s}{2(1-s^{q+1})},
\qquad D=q(q+1),
\]
we have \(\mathbb E_s A=0\).

Let \(g(x)=\mathbf{1}_{\{x>0\}}-\theta\). Its Dirichlet Poisson potential \(u(x)=\mathbb E_x\int_0^\tau g(X_t)\,dt\) solves \(u''(x)=-|x|^{q-1}g(x)\), \(u(-1)=u(1)=0\), with \(u,u'\) continuous at zero. Direct integration gives
\[
u(x)=\frac1{2D}
\begin{cases}
2\eta-1+x+2(1-\eta)|x|^{q+1},&-1\leq x\leq0,\\
2\eta-1+x-2\eta x^{q+1},&0\leq x\leq1.
\end{cases}
\]
The relation \(2\eta(1-s^{q+1})=1-s\) implies \(u(s)=0\). Therefore Itô's formula up to exit, including its continuous-derivative version across zero, yields
\[
A=\int_0^\tau \sqrt{2}|X_t|^{-(q-1)/2}u'(X_t)\,dW_t.
\]
Its second moment is the following nonnegative Dirichlet-energy integral:
\[
\mathbb E_sA^2=2\int_{-1}^1G(s,y)[u'(y)]^2\,dy.
\]
To make the elementary evaluation explicit, write \(b=1/[2q(q+1)]\). The derivatives of \(u\) are
\[
u'(-t)=b-\frac{1-\eta}{q}t^q,
\qquad u'(t)=b-\frac\eta q t^q
\quad(0\leq t\leq1).
\]
Substitution in the preceding integral splits it into three power integrals:
\[
\begin{aligned}
\mathbb E_sA^2={}&(1-s)\int_0^1(1-t)\left(b-\frac{1-\eta}{q}t^q\right)^2dt\\
&+(1-s)\int_0^s(1+t)\left(b-\frac\eta q t^q\right)^2dt\\
&+(1+s)\int_s^1(1-t)\left(b-\frac\eta q t^q\right)^2dt.
\end{aligned}
\]
Expand the squares, integrate monomials using \(\int_a^bt^zdt=(b^{z+1}-a^{z+1})/(z+1)\), and use \(2\eta(1-s^{q+1})=1-s\). The expression reduces **exactly**, for every real \(q\geq1\), to
\[
\mathbb E_sA^2=\frac{3(1-s^2)}{4(q+1)^2(q+2)(2q+1)}.
\]
The integrands are bounded and square-integrable in the Green representation. To justify optional stopping and the second-moment calculation, observe from the Brownian clock construction that the physical exit time is at most \(L^\alpha\) times the Brownian exit time, which has moments of all orders. Localization then removes the stopped-martingale cutoff.

Independent cycles give i.i.d. pairs of duration and positive occupation reward. The classical regenerative renewal-reward central limit theorem, applied to their centered reward \(A\), yields a Gaussian variance \(\mathbb EA^2/\mathbb E\tau\). Dividing the two displayed identities proves the formula for \(L=1\). The Brownian spatial scaling \(x\mapsto Lx\) changes each physical excursion time by \(L^{q+1}=L^{\alpha+2}\), so it multiplies the limiting variance coefficient by the same factor and the cycle second moment by its square.

Finally, the restart-point dependence of the variance is proportional to \(h(s)=(1-s^2)/(1-s^{\alpha+2})\). For \(\alpha=0\), this ratio is identically one. For \(\alpha>0\), its reciprocal is
\[
\frac{1-s^{\alpha+2}}{1-s^2}
=\frac{\alpha+2}{2}\,
\frac{\int_s^1t^{\alpha}t\,dt}{\int_s^1t\,dt}.
\]
The rightmost conditional average of the strictly increasing function \(t^{\alpha}\), under measure proportional to \(t\,dt\) on \([s,1]\), is strictly increasing in \(s\). Thus \(h\) strictly decreases, and the endpoint limits follow by direct substitution and l'Hôpital's rule.

## Verification
The accompanying `verification.py` performs a formal symbolic simplification of the general real-exponent Green-energy identity with SymPy. It also evaluates the signed Poisson-potential representation in exact rational arithmetic for 108 finite parameter examples, and checks 24 noninteger-exponent cases by numerical quadrature. `verification_output.txt` records the actual checker output. These tests corroborate intermediate algebra but do not replace the continuum proof, regenerative limit argument, or literature comparison.

## Relationship to prior work
Frimpong, Bresque, and Roldán (2026) establish the threshold-restarted sluggish diffusion, its Green occupation measure and mean restart-cycle duration, and the deterministic limiting positive occupation fraction \(\theta\). In §6.1.2 they state concentration on its deterministic limit with square-root order fluctuations, but do not evaluate the Gaussian variance coefficient. Their explicit Gaussian variance in §6.1.1 concerns the **different protocol** of externally timed Poisson resetting, not boundary-triggered resetting.

Méndez, Flaquer-Galmés, and Pal (2024) compute occupation-time statistics for continuous-time random walks with independent Poissonian position resetting. In the inspected manuscript §VI, the resetting events occur at a fixed Poisson rate rather than upon first exit of a bounded interval. General renewal-reward CLTs supply the abstract ratio of cycle moments, but not the evaluated power-law coefficient or the exact Brownian-invariance/strict-monotonicity distinction. These related frameworks motivate the calculation; the claimed mathematical addition is the explicit stopped-cycle second moment and complete continuum fluctuation coefficient.

## Limitations
The result assumes symmetric thresholds, instantaneous restart at one fixed positive point, natural-scale diffusion, and \(\alpha\geq0\). It neither covers higher-dimensional sluggish diffusion nor arbitrary reset points or random restart rules. The small- and large-\(\rho\) values are **one-sided coefficient limits**, not simultaneous-time asymptotics or a definition at the boundary. Finite checking cannot independently establish historical priority; a broader, differently phrased additive-functional result might contain the evaluated coefficient.

## References
1. T. D. Frimpong, L. Bresque, and É. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1 (first posted 2026-10-15), especially §§2.1 and 6.1.2. https://arxiv.org/html/2610.21962
2. V. Méndez, R. Flaquer-Galmés, and A. Pal, *Occupation time statistics for non-Markovian random walks*, arXiv:2412.05247v1 (first posted 2024-12-06), especially §VI. https://arxiv.org/pdf/2412.05247
3. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009 (2018). https://arxiv.org/abs/1812.03009
