# Universal hidden-phase and Gaussian age laws for extreme Gamma-reset diffusion with finite-speed returns

## Finding
Fix positive parameters \(s,r,D,v\) and observe the unique stationary position \(X\) of the reset–return Brownian process defined below. An unusually positive position \(X>x\) selects diffusive trajectories with a duration proportional to \(x\), with normal duration fluctuations of order \(\sqrt{x}\), although the stationary position itself has an exponentially small tail. In the limit, the hidden phase, centered duration, and position overshoot become independent. The phase is asymptotically diffusive with probability
\[
 p_{\mathrm{diff}}=\frac{v}{v+\sqrt{Dr}},
\]
independent of the Gamma shape. The completed or elapsed diffusion time \(S\), depending on phase, satisfies
\[
 \frac{S-t_x}{h_x}\Longrightarrow N(0,1),\qquad
 t_x=\frac{x}{2\sqrt{Dr}},\quad h_x=\sqrt{\frac{t_x}{2r}}.
\]
The excess stationary position \(X-x\), conditioned on \(X>x\), tends independently to \(\operatorname{Exp}(\sqrt{r/D})\). During diffusion, the as-yet-unelapsed time to the next reset alarm converges independently to \(\operatorname{Exp}(r)\). During return, the distance already traversed from the diffusion endpoint to the observed position tends independently to \(\operatorname{Exp}(\sqrt{r/D})\); its time cost is that distance divided by \(v\). Here \(\operatorname{Exp}(\lambda)\) means the exponential law of rate \(\lambda\).

The full leading positive-tail coefficient is
\[
 \mathbb P(X>x)\sim \frac{k^{s-1}}{2^s\Gamma(s)\,m}
 \left(\frac1r+\frac1{vk}\right)x^{s-1}e^{-kx},\quad k=\sqrt{\frac rD},
\]
where
\[
 m=\frac sr+\frac{2\sqrt{D/r}}{v}\frac{\Gamma(s+1/2)}{\sqrt\pi\,\Gamma(s)}.
\]
The tail coefficient and its decomposition follow from the stationary densities in Radice (2022); the conditional *joint time/phase/overshoot limit*, not that marginal tail, is the finding assessed here.

## Assumptions and scope
Start each regenerative cycle at position zero. First run standard Brownian motion with generator \(D\partial_{yy}\), from zero up to an independent time \(T\) having Gamma density
\[
 \psi(t)=\frac{r^s}{\Gamma(s)}t^{s-1}e^{-rt},\qquad t>0.
\]
At that time let \(Z\) be the Brownian endpoint. Return deterministically along the line segment from \(Z\) to zero at constant speed \(v\), taking time \(|Z|/v\); immediately start a new independent cycle. All parameters are fixed and strictly positive, and all diffusion runs, clocks, and cycles are independent. Each cycle has finite positive mean \(m\) displayed above, so its equilibrium occupation law is well-defined. At observation time, \(B=\mathrm{diff}\) or \(B=\mathrm{return}\) records the current phase; \(S\) equals elapsed diffusive time if \(B=\mathrm{diff}\) and completed diffusion duration if \(B=\mathrm{return}\). Let \(U=X-x\) on \(X>x\). If \(B=\mathrm{diff}\), let \(R\) denote the remaining waiting time until the resetting alarm. If \(B=\mathrm{return}\), let \(J\) denote the distance traversed since the return began. The auxiliary variables \(R,J\) are defined only in their indicated phase. There is no instantaneous teleportation, no observation at a renewal epoch, and no claim about a first-passage time.

## Proof
Write the Brownian heat kernel as
\[
 p_t(y)=(4\pi Dt)^{-1/2}\exp(-y^2/(4Dt)),\quad t>0.
\]
By the renewal-reward theorem, stationary occupation is expected position-time per cycle divided by \(m\). Fix \(y>0\). The exact *augmented* occupation densities, without the common factor \(m^{-1}\), are
\[
 \begin{aligned}
 d\nu_{\mathrm{diff}}(t,y,\delta)&=p_t(y)\,\psi(t+\delta)\,dt\,dy\,d\delta,\\
 d\nu_{\mathrm{return}}(t,y,j)&=v^{-1}\psi(t)\,p_t(y+j)\,dt\,dy\,dj.
 \end{aligned}
\]
In the first line \(t\) is elapsed diffusion and \(\delta\ge0\) is remaining alarm time. In the second \(t\) is completed diffusion duration and \(j\ge0\) is return distance already traversed. The return formula follows because a return with positive endpoint \(Z=y+j\) occupies each positive \(y\in(0,Z)\) for time \(dy/v\). Integrating \(\delta\) gives the familiar diffusive occupation density \(\int_0^\infty\overline F(t)p_t(y)dt\); integrating \(j\) gives the return density \(v^{-1}\int_0^\infty\psi(t)\Pr(B_t>y)dt\). Negative endpoints cannot contribute at positive \(y\).

Let \(k=\sqrt{r/D}\), \(t_x=x/(2\sqrt{Dr})\), \(h_x=\sqrt{t_x/(2r)}\), and set \(t=t_x+h_x z\), \(y=x+u\), with fixed \(z\in\mathbb R\), \(u\ge0\). The unique minimum of the exponent
\[
 \Phi_x(t)=rt+\frac{x^2}{4Dt}
\]
is at \(t_x\) with \(\Phi_x(t_x)=kx\) and \(\Phi_x''(t_x)h_x^2=1\). Taylor's formula, uniformly on compact sets of \((z,u,j,\delta)\), yields
\[
 rt+\frac{(x+u+j)^2}{4Dt}
 =kx+\frac{z^2}{2}+k(u+j)+o(1).
\]
Since \(\psi(t+\delta)/\psi(t)\to e^{-r\delta}\) uniformly for bounded \(\delta\), both rescaled occupation measures share the Gaussian factor \(e^{-z^2/2}\) and the positional factor \(e^{-ku}\). In the diffusive phase the additional factor is \(e^{-r\delta}\); in return it is \(v^{-1}e^{-kj}\). The common polynomial factor is \(t_x^{s-3/2}\) and cancels in every conditional ratio. This demonstrates the independence assertion and determines the normal, overshoot, residual-alarm, and return-progress laws after normalization.

For completeness the local approximation extends from compact sets to the full domains. For every fixed \(\epsilon>0\), away from \(|t/t_x-1|<\epsilon\), strict convexity of \(rt+x^2/(4Dt)\) at its unique positive minimizer yields an exponential penalty proportional to \(x\). On the central domain the quadratic Taylor lower bound controls \(z\), while the Gaussian kernel supplies an exponential bound in \(u+j\), and the Gamma survival supplies one in \(\delta\). Splitting the integral into these regions and then increasing compact cutoffs establishes tightness and dominated convergence. This argument applies to every \(s>0\): powers of \(t\) do not change the exponential saddle, and endpoint regions are exponentially negligible. Thus the weak convergence is joint, including the conditional auxiliary variables.

Integrating the limiting \((u,\delta)\) factors shows that the relative asymptotic diffusion and return masses are respectively \(1/(kr)\) and \(1/(vk^2)\). Therefore
\[
 \Pr(B=\mathrm{diff}\mid X>x)\to
 \frac{1/(kr)}{1/(kr)+1/(vk^2)}=\frac{vk}{r+vk}=\frac{v}{v+\sqrt{Dr}}.
\]
The fact that the Gamma shape disappears reflects cancellation of the common saddle prefactor, not a claim that the full stationary density is Gamma-shape independent.

For the tail coefficient, mixing the Brownian endpoint density over the Gamma clock gives
\[
 f(y)=\int_0^\infty\psi(t)p_t(y)dt
 \sim \frac{k^s}{2^s\Gamma(s)}y^{s-1}e^{-ky}
 \quad(y\to+\infty),
\]
by the same Laplace saddle (equivalently, the standard Bessel-\(K\) representation). Since \(\overline F(t)/\psi(t)\to1/r\), the diffusive stationary density has asymptotic \(f(y)/(rm)\); the return density is \(m^{-1}v^{-1}\int_y^\infty f(z)dz\sim f(y)/(vkm)\). Integrating in \(y>x\) gives the displayed exact leading tail coefficient. Finally, \(m=\mathbb ET+\mathbb E|B_T|/v\), and \(\mathbb E|B_T|=(2\sqrt D/\sqrt\pi)\mathbb E\sqrt T\) yields the stated expression.

## Verification
The standalone `CHECKER.py` uses SciPy quadrature of two independently specified phase-age occupation kernels and compares their positive-position phase mixture and conditional duration moments with the derived asymptotics across Gamma shapes below, at, and above one and two independent physical-parameter choices. It also tests the exact Poisson-clock special case. It reports 90 deterministic assertions. This numerical check is corroborative: the proof of the joint limit is the saddle-point argument above, not finite-threshold quadrature.

## Relationship to prior work
Radice (2022, arXiv:2201.01829) explicitly derives the model, both stationary phase occupation densities, and large-position marginal stationary asymptotics. Those published statements imply the marginal tail and the limiting phase weight and are **not** claimed as independent novelty. The distinct result here is the *conditional joint law of the latent diffusion duration, stationary overshoot, and phase-specific remaining or elapsed time*. Earlier works by Bodrova and Sokolov (2019), Masó-Puigdellosas–Campos–Méndez (2019), and Zhou–Xu–Deng (2021) derive stationary densities, renewal structure, mean-square displacement, or passage-time properties of finite-speed reset-return systems, rather than this joint extreme-position conditioning. These comparisons do not exclude all possible general conditioning theorems.

## Limitations
This is a one-dimensional Brownian model with independent Gamma reset duration and deterministic constant-speed return, in its stationary regenerative state. All limits hold as a fixed positive threshold tends to infinity, for fixed physical parameters; they are not uniform in Gamma shape or return speed, and no explicit finite-threshold error bars are established. The nonlinear joint limit requires the specific Gaussian propagator and Gamma exponential tail; no claim is made for arbitrary resetting clocks or return trajectories. Priority relative to general large-deviation conditioning theorems remains a scholarly risk.

## References
- Mattia Radice, *Diffusion processes with Gamma-distributed resetting and non-instantaneous returns*, arXiv:2201.01829v1 (first public January 5, 2022), sections 2–4 and Appendices A–B; DOI 10.1088/1751-8121/ac654f.
- Anna S. Bodrova and Igor M. Sokolov, *Resetting processes with non-instantaneous return*, arXiv:1907.12326v1 (2019), sections II–VII.
- Axel Masó-Puigdellosas, Daniel Campos, and Vicenç Méndez, *Transport properties of random walks under stochastic non-instantaneous resetting*, arXiv:1910.09927v1 (2019).
- Tian Zhou, Pengbo Xu, and Weihua Deng, *Gaussian Process and Lévy Walk under Stochastic Non-instantaneous Resetting and Stochastic Rest*, arXiv:2105.12571v1 (2021).
