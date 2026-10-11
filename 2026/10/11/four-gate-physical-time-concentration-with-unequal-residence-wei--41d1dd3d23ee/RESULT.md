# Four-gate physical-time concentration with unequal residence weights in a cubic star-node oscillator

## Finding
For the explicitly defined contracting cubic oscillator below, every positive angular drift \(\varepsilon\) yields one globally attracting limit cycle with exact original-time period
\[
T_\varepsilon=\frac{2\pi\kappa}{\lambda\sqrt{\varepsilon(\varepsilon+\omega)}}.
\]
The period does not depend on the radial anisotropy parameter \(\eta\). Nevertheless, a uniform original-time sample of the orbital angle converges, as \(\varepsilon\downarrow0\), to a four-point law on the coordinate axes with weights
\[
w_0=w_2=\frac{\kappa+\eta}{4\kappa},\qquad w_1=w_3=\frac{\kappa-\eta}{4\kappa}.
\]
Conditional on approaching any of the four axes, the angular distance divided by \(\sqrt{\varepsilon/(4\omega)}\) has a standard Cauchy limit. Thus the exact total period conceals a tunable imbalance among four bottlenecks.

## Assumptions and scope
Fix real parameters \(\lambda>0\), \(\omega>0\), \(\eta\in\mathbb R\), \(\kappa>|\eta|+\omega/2\), and \(\varepsilon>0\). On \(\mathbb R^2\) consider
\[
\begin{aligned}
\dot x={}&\lambda x-[\kappa(x^2+y^2)+\eta(x^2-y^2)]x-2\omega x^2y-\varepsilon(x^2+y^2)y,\\
\dot y={}&\lambda y-[\kappa(x^2+y^2)+\eta(x^2-y^2)]y+2\omega xy^2+\varepsilon(x^2+y^2)x.
\end{aligned}
\]
A nonzero trajectory has polar coordinates \(x=r\cos\theta\), \(y=r\sin\theta\). The angle is taken modulo \(2\pi\). \(T_\varepsilon\) denotes the minimal period in the equation's original physical time. Sampling at uniform time means choosing \(t\) according to normalized Lebesgue measure on \([0,T_\varepsilon)\) along the cycle.

Let \(\theta_j=j\pi/2\) for \(j=0,1,2,3\), and define \(J_\varepsilon\) to be the index of the nearest \(\theta_j\) in circular angular distance; ties (a null event) can be resolved arbitrarily. Put
\[
V_\varepsilon=2\sqrt{\omega/\varepsilon}\,\operatorname{Arg}(e^{i(\Theta_\varepsilon-\theta_{J_\varepsilon})}),
\]
with principal argument in \([-\pi,\pi)\). All limits hold with the other four parameters fixed.

## Proof
**1. Exact polar reduction and the periodic orbit.** Write \(u=r^2\). Direct polynomial differentiation gives
\[
\dot r=r(\lambda-F(\theta)r^2),\quad \dot\theta=u\,g_\varepsilon(\theta),\quad F(\theta)=\kappa+\eta\cos(2\theta)+\tfrac\omega2\sin(4\theta),\quad g_\varepsilon(\theta)=\varepsilon+\omega\sin^2(2\theta).
\]
Set \(m=\kappa-|\eta|-\omega/2>0\) and \(M=\kappa+|\eta|+\omega/2\). Then \(m\le F\le M\) and \(g_\varepsilon>0\). In increasing angular time the radial-square equation is linear:
\[
\frac{du}{d\theta}=\frac{2}{g_\varepsilon(\theta)}(\lambda-F(\theta)u).
\]
Its full-revolution return map has the form \(u\mapsto Au+B\), where \(A=\exp(-2\int_0^{2\pi}F/g_\varepsilon\,d\theta)\in(0,1)\) and \(B>0\). Its unique positive fixed point defines a positive smooth periodic function \(u_\varepsilon(\theta)\); the corresponding closed curve is the unique nonconstant periodic orbit. The scalar comparison principle places \(\lambda/M\le u_\varepsilon\le\lambda/m\). Since every other positive radial-square solution converges geometrically in angular revolutions to this fixed point, all nonzero trajectories approach the limit cycle. Global forward existence follows from the radial trapping bound and bounded angular speed on bounded radial sets.

**2. Original-time period, including its anisotropy cancellation.** Along the periodic orbit, \(d(\log r)/dt=\lambda-F(\theta)u\). Its period average is zero, so, using \(dt=d\theta/[u\,g_\varepsilon(\theta)]\),
\[
\lambda T_\varepsilon=\int_0^{2\pi}\frac{F(\theta)}{g_\varepsilon(\theta)}\,d\theta.
\]
The \(\eta\cos2\theta\) term integrates to zero by shifting \(\theta\mapsto\theta+\pi/2\), and the \(\sin4\theta\) term integrates to zero by reflection. The standard trigonometric integral gives
\[
\int_0^{2\pi}\frac{d\theta}{\varepsilon+\omega\sin^2(2\theta)}=\frac{2\pi}{\sqrt{\varepsilon(\varepsilon+\omega)}}.
\]
Hence the stated exact period. In particular, \(\sqrt\varepsilon T_\varepsilon\to 2\pi\kappa/(\lambda\sqrt\omega)\).

**3. Radial equilibration in each bottleneck.** Let \(\theta_j=j\pi/2\). For every fixed \(R>0\) we show uniformly on \(|v|\le R\) that
\[
u_\varepsilon\left(\theta_j+v\sqrt{\varepsilon/(4\omega)}\right)\longrightarrow \frac{\lambda}{F_j},\qquad F_j=F(\theta_j)=\kappa+(-1)^j\eta.
\]
The linear angular equation is the positive-coefficient relaxation equation \(u'=a_\varepsilon(\theta)(\lambda/F(\theta)-u)\), with \(a_\varepsilon=2F/g_\varepsilon\). Fix a small \(h>0\). On \([\theta_j-h,\theta_j+h]\), \(F\) differs from \(F_j\) by at most a modulus of continuity \(\xi(h)\to0\). Compare its solutions to the equations with the two constant targets \(\lambda/(F_j\pm\xi(h))\), using the common nonnegative damping \(a_\varepsilon\). The initial differences are bounded uniformly by \(\lambda/m\) and \(\lambda/M\). For any fixed bounded \(v\), the damping accumulated from \(\theta_j-h\) to \(\theta_j+v\sqrt{\varepsilon/(4\omega)}\) diverges as \(\varepsilon\downarrow0\), since \(g_\varepsilon\le\varepsilon+4\omega(\theta-\theta_j)^2\) locally. The initial differences therefore disappear. Letting \(h\downarrow0\) gives the displayed convergence uniformly on compact sets of \(v\).

**4. Local Cauchy law and four unequal masses.** The normalized original-time orbital angle has density
\[
p_\varepsilon(\theta)=\frac{1}{T_\varepsilon u_\varepsilon(\theta)g_\varepsilon(\theta)}.
\]
For \(\theta=\theta_j+v\sqrt{\varepsilon/(4\omega)}\) with bounded \(v\),
\[
\frac{g_\varepsilon(\theta)}\varepsilon\to1+v^2,\qquad
u_\varepsilon(\theta)\to\lambda/F_j,
\]
uniformly on compact sets. Combining with the exact period, the probability measure in this rescaled neighborhood converges locally to
\[
\frac{F_j}{4\pi\kappa}\frac{dv}{1+v^2}.
\]
To upgrade this local statement to convergence of probability laws, note that \(u_\varepsilon\ge\lambda/M\) and, near any of the four zeros of \(\sin2\theta\), \(g_\varepsilon\ge\varepsilon+c\operatorname{dist}(\theta,\{\theta_k\})^2\), with fixed \(c>0\). By \(T_\varepsilon\asymp\varepsilon^{-1/2}\), the normalized time mass outside all windows of width \(R\sqrt\varepsilon\) is bounded by \(C/R+O(\sqrt\varepsilon)\) for suitable constants. This proves tightness of the scaled variables and convergence of the entire joint law:
\[
\mathbb P(J_\varepsilon=j,V_\varepsilon\in dv)\Longrightarrow
w_j\frac{dv}{\pi(1+v^2)},\qquad
w_j=\frac{F_j}{4\kappa}.
\]
The four \(w_j\) sum to one because \(\sum_jF_j=4\kappa\); each factor is positive because \(\kappa>|\eta|\). Integrating over \(v\) yields weak convergence of the unscaled orbital-angle law to \(\sum_jw_j\delta_{\theta_j}\), and the factorization establishes asymptotic independence of the gate index and standard Cauchy coordinate. The result is a limit of invariant time-sampling measures of periodic orbits, not a claim about a random dynamical forcing.

## Verification
The included `verify.py` replays the polynomial angular reduction by direct numerical evaluation, integrates the attracting radial-square equation in angular time, compares the reconstructed physical period with the exact formula, and evaluates the four gate weights and central Cauchy mass at two positive drift parameters. It prints `CHECK_OK`. Its finite grids are numerical checks only; the limiting measure is proved by the comparison and tightness arguments above.

## Relationship to prior work
Alarcón, Castro, and Labouriau classify the global flow of contracting homogeneous polynomial star-node systems, prove existence of the attracting invariant circle, and distinguish periodic circles from policycles according to zeros of the angular field. The present system lies within that established class, and its existence/phase-portrait conclusions are credited. Earlier Darboux-integrability and homogeneous return-map methods provide background for period quadratures and transverse multipliers; neither existence nor those generic methods is claimed as a new result. The result addressed here is the exact anisotropy-independent time total together with a **parameter-dependent four-gate weak limit and a resolved Cauchy boundary layer** in original physical time. General saddle-node slowdown is also known; the explicit four-way weights for this polynomial family and their coexistence with an anisotropy-independent total period are the specialized conclusions.

## Limitations
The theorem is restricted to the stated contracting parameter region and \(\varepsilon>0\), with the other parameters fixed. It does not address arbitrary perturbations of the vector field or uniqueness of publication priority. The \(\varepsilon=0\) limiting phase portrait contains equilibria on the invariant circle and is not itself a periodic orbit. General saddle-node-normal-form arguments may cover aspects of the local Cauchy shape; the claimed mathematical object is the combined explicit four-gate law with its unequal weights and exact physical-time period. Earlier literature not available in complete readable form remains a priority risk.

## References
1. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, arXiv:2307.16020v1 (first public 2023-07-29); *Research in the Mathematical Sciences* 11, 21 (2024), DOI 10.1007/s40687-024-00427-0.
2. A. Bendjeddou, J. Llibre, T. Salhi, *Dynamics of the polynomial differential systems with homogeneous nonlinearities and a star node*, *Journal of Differential Equations* 254 (2013), 3530–3537, DOI 10.1016/j.jde.2013.01.032.
3. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Global planar dynamics with star nodes: beyond Hilbert's sixteenth problem*, arXiv:2106.07516 (2021 preprint).
