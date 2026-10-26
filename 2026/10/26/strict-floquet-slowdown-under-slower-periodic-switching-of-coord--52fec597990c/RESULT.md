# Strict Floquet slowdown under slower periodic switching of coordination games

## Finding

Fix two strict coordination environments with selection coefficients \(a_1,a_2>0\), thresholds \(0<h_1<h_2<1\), and a duty fraction \(0<p<1\). In a cycle of duration \(T>0\), environment 1 acts for \(pT\), followed by environment 2 for \((1-p)T\). For the two-strategy replicator equation

\[
\dot x=a_i x(1-x)(x-h_i),\qquad i=1,2,
\]

there is exactly one periodic solution with \(0<x(t)<1\). It is a repelling separatrix: trajectories strictly below it at a common cycle phase converge to \(0\), and those strictly above it converge to \(1\). Thus predetermined periodic switching does not create robust interior coexistence in this scalar strict-coordination family.

Let \(\ell(T)\) and \(u(T)\) be the minimum and maximum of its periodic orbit, and set

\[
\bar a=pa_1+(1-p)a_2,\qquad
h=\frac{pa_1h_1+(1-p)a_2h_2}{\bar a}.
\]

Along the periodic solution define the selection-weighted variance

\[
V(T)=\frac1{\bar a T}\int_0^T a(t)[x(t)-h]^2\,dt.
\]

The per-unit-time Floquet exponent \(\Lambda(T)=T^{-1}\log M(T)\) obeys the **exact identity**

\[
\boxed{\Lambda(T)=\bar a[h(1-h)-V(T)]>0.}
\]

More strongly, the variance has the **exact period derivative**

\[
\boxed{\frac{d}{dT}[T V(T)]=(h-\ell(T))(u(T)-h),}
\]

and consequently \(V'(T)>0\) and **\(\Lambda'(T)<0\) for every \(T>0\)**. The instability therefore becomes strictly weaker per unit time as the switching period increases, but never changes sign. The sharp limiting rates are

\[
\boxed{
\begin{aligned}
\lim_{T\downarrow0}\Lambda(T)&=\bar a h(1-h),\\
\lim_{T\to\infty}\Lambda(T)&=\bar a\{h(1-h)-(h-h_1)(h_2-h)\}>0.
\end{aligned}}
\]

The orbit endpoints are strictly nested as the period grows:

\[
h_1<\ell(T)<h<u(T)<h_2,\qquad
\ell'(T)<0<u'(T),
\]

with \(\ell(T),u(T)\to h\) as \(T\downarrow0\) and \(\ell(T)\to h_1\), \(u(T)\to h_2\) as \(T\to\infty\). In particular, define \(v=p a_1h(1-h)(h-h_1)>0\); then

\[
\ell(T)=h-\tfrac12vT+O(T^2),\quad
u(T)=h+\tfrac12vT+O(T^2),\quad
V(T)=\tfrac1{12}v^2T^2+O(T^3).
\]

The monotone Floquet slowdown and exact variance derivative, rather than the mere existence of an oscillating trajectory, are the principal quantitative conclusions.

## Assumptions and scope

The state is a frequency \(x\in[0,1]\), the elapsed time is continuous, and \(p,a_1,a_2,h_1,h_2\) remain fixed as the period \(T\) varies. Switching is precommitted by time, independent of \(x\). The environment order is: first \(a_1 x(1-x)(x-h_1)\) for \(pT\), then \(a_2x(1-x)(x-h_2)\) for \((1-p)T\), repeatedly. The scalar flow is unique and continuous through switching instants. The two environments each have two locally attracting pure states and one repelling interior threshold. The multiplier \(M(T)\) means the derivative of the time-\(T\) return map at the unique interior periodic point. All results hold for every real parameter set satisfying the displayed strict inequalities and every \(T>0\); asymptotic expressions concern the indicated limits only.

## Proof

**1. Unique repelling periodic solution and its basin boundary.** Write \(z=\log(x/(1-x))\), \(x=\sigma(z)=1/(1+e^{-z})\). In either environment, \(\dot z=a_i(\sigma(z)-h_i)\). Let \(Q_T\) be the time-\(T\) map on the real line. Differentiating the scalar variational equation gives

\[
Q_T'(z_0)=\exp\!\left(\int_0^T a(t)x(t)[1-x(t)]\,dt\right)>1.
\]

Therefore \(Q_T(z)-z\) is strictly increasing. Its limits at the two infinite endpoints are \(-T[pa_1h_1+(1-p)a_2h_2]<0\) and \(T[pa_1(1-h_1)+(1-p)a_2(1-h_2)]>0\), because trajectories issued from \(z\to\pm\infty\) remain uniformly near the corresponding pure state over a single finite cycle. There is exactly one fixed point \(z_T\), and its return derivative is greater than one. Iterations below and above \(z_T\) are respectively decreasing to \(-\infty\) and increasing to \(+\infty\), since there is no other fixed point. The continuous trajectories between cycles have bounded logit displacement, proving convergence to the corresponding pure state. In particular, the periodic orbit is globally separating rather than attracting.

**2. Extremes and the exact weighted measure.** On a nonconstant periodic orbit the first stage must move upward and the second downward. Otherwise an orbit starting at or below \(h_1\), or at or above \(h_2\), cannot complete a nonconstant cycle; nor can its upward phase cross \(h_2\) and return. Hence \(h_1<\ell(T)<u(T)<h_2\). Integrating \(\dot z\) over one period yields

\[
\frac1{\bar a T}\int_0^T a(t)x(t)\,dt=h,
\]

forcing \(\ell(T)<h<u(T)\). The upward and downward phases each traverse every \(x\) in \((\ell,u)\) once. Their selection-weighted residence density is exactly

\[
w(x)=\frac{h_2-h_1}{x(1-x)(x-h_1)(h_2-x)},\qquad \ell<x<u.
\]

Indeed \(a_1dt=dx/[x(1-x)(x-h_1)]\) on ascent, whereas \(a_2dt=dx/[x(1-x)(h_2-x)]\) on descent; adding these yields \(w(x)dx\). Consequently

\[
\int_\ell^u w(x)\,dx=\bar a T,\qquad
\int_\ell^u xw(x)\,dx=\bar a hT,\qquad
V(T)=\frac{\int_\ell^u(x-h)^2w(x)\,dx}{\bar a T}.
\]

**3. Differentiation, amplitude order and strict variance increase.** Smooth dependence of the time-\(T\) map on \(T\) and its strictly positive fixed-point crossing derivative \(Q_T'(z_T)-1\) ensure differentiability of \(\ell(T)\) and \(u(T)\) for every \(T>0\). Differentiating the first two residence integrals, and putting \(U=w(u)u'\) and \(L=-w(\ell)\ell'\), gives

\[
U+L=\bar a,\quad uU+\ell L=\bar a h,\quad
U=\bar a\frac{h-\ell}{u-\ell}>0,\quad
L=\bar a\frac{u-h}{u-\ell}>0.
\]

This proves \(u'>0>\ell'\). Differentiating the unnormalized second central moment now gives

\[
\frac d{dT}[\bar a TV]
=U(u-h)^2+L(\ell-h)^2
=\bar a(u-h)(h-\ell).
\]

For a probability law supported strictly inside \((\ell,u)\) with mean \(h\), the strict elementary inequality \((x-\ell)(u-x)>0\) implies

\[
V(T)<(h-\ell)(u-h).
\]

Thus \(T V'(T)=(h-\ell)(u-h)-V(T)>0\) for all \(T>0\). This argument does not assume symmetry of the environments, equal residence times or small forcing.

**4. Floquet exponent and limits.** By the logit variational formula in Step 1, \(\log M=\int_0^T a(t)x(t)(1-x(t))dt\). The exact weighted mean in Step 2 gives \(\int ax(1-x)=\bar a T[h(1-h)-V]\). The multiplier is strictly greater than one, proving the positive exponent; Step 3 proves it decreases strictly with \(T\).

For \(T\downarrow0\), bounded phase velocities imply \(u-\ell\to0\), and the weighted mean identity forces both endpoints to tend to \(h\). A first-order piecewise-constant-velocity expansion across the two stages gives a rising and falling linear segment of height \(vT+O(T^2)\), with equal leading selection-weighted occupation per unit \(x\) across the shared interval. Its central variance is therefore \(v^2T^2/12+O(T^3)\), establishing the small-period formulas.

For \(T\to\infty\), the exact residence integrals

\[
pT=\int_{\ell}^u\frac{dx}{a_1x(1-x)(x-h_1)},\quad
(1-p)T=\int_{\ell}^u\frac{dx}{a_2x(1-x)(h_2-x)}
\]

can diverge only if \(\ell\to h_1\) and \(u\to h_2\), respectively. The identity in Step 3 then implies \((TV)'\to(h-h_1)(h_2-h)\). Elementary Cesàro averaging yields \(V(T)\to(h-h_1)(h_2-h)\), proving the sharp positive limiting exponent. Its positivity also follows directly from the fact that the weighted average of \(x(1-x)\) is positive throughout the orbit.

## Verification

The included standalone `check_floquet.py` solves the original scalar differential equation on each half-cycle with independent accumulated integrals for the selection-weighted mean, selection-weighted variance, and original-coordinate variational derivative. It determines the unique periodic initial point by scalar root finding. Across four asymmetric and symmetric parameter sets and 31 total parameter/period instances, it checks exact-orbit return, threshold ordering, monotone endpoints, monotone variance and exponent, the Floquet/variance identity, the differential variance law (using an independent centered difference), and the predicted leading small-period coefficient. Run with `python check_floquet.py` after installing `scipy >= 1.10`; a compatible Python interpreter is required. These floating-point checks are finite consistency tests; the all-parameter mathematical assertions follow from the analytic proof above.

For example, with \(a_1=a_2=3\), \(h_1=1/3\), \(h_2=2/3\), and \(p=1/2\), the exponent strictly decreases from \(3/4\) to \(2/3\) as the switching period ranges from zero to infinity. At duration \(T=12\), numerical integration gives \(\ell\approx0.3381435771\), \(u\approx0.6618564229\), \(V\approx0.0153411471\), and \(\Lambda\approx0.7039765588\).

## Relationship to prior work

Shu and Fu (2022), *Eco-Evolutionary Dynamics of Bimatrix Games*, study the very same one-population switching replicator form, explicitly exhibit symmetric and asymmetric switching patterns that preserve a selected oscillating interior trajectory, and analyze associated trapping constructions. Those periodic constructions and the elementary observation that the pure states remain stable are treated as prior art. Their detailed one-dimensional discussion (Sections 3.1–3.3, equations (5)–(17)) does not provide the period-parametric **strict Floquet-exponent monotonicity**, the exact derivative \((TV)'=(h-\ell)(u-h)\), or the sharp variance-mediated limiting exponents established here. In the symmetric example their residence-time formula already relates excursion amplitude to switching period; amplitude monotonicity alone is therefore not an originality claim here.

Álvarez, Gasull and Giacomini (2006) develop uniqueness/hyperbolicity criteria for periodic Abel equations, including wider cubic scalar families. Their methods provide important prior context for uniqueness and hyperbolicity but do not state the two-stage selection-weighted residence measure or the exact period derivative and strict Floquet slowdown claimed here. Loginov (2021) studies endogenously evolving payoffs and a two-dimensional coordination feedback flow rather than a fixed, precommitted periodic switching schedule. No universal uniqueness beyond this scalar strict-coordination class is asserted.

## Limitations

The monotone slowdown holds when \(p,a_1,a_2,h_1,h_2\) are fixed while \(T\) varies; it does not apply if duty cycle or payoff coefficients change with \(T\). The comparison is the local exponential divergence rate **per unit physical time** along the exceptional interior periodic orbit, not the raw per-cycle multiplier: \(M(T)>1\) need not decrease with \(T\). The schedule is predetermined, not feedback/state-triggered; the result does not exclude robust coexistence under nonlinear feedback, additional state dimensions, mixing, demographic noise or stochastic dynamics. No claim is made about the original paper's multidimensional bimatrix network extension. Previously published general Abel-equation theory may imply uniqueness or hyperbolicity aspects, but the claimed mathematical gap concerns the explicit and strictly monotone period-dependence of the Floquet exponent in this particular evolutionary setting. Independent validation has not been performed.

## References

1. L. Shu and F. Fu (2022), *Eco-Evolutionary Dynamics of Bimatrix Games*, arXiv:2208.13306v1 (first publicly posted 2022-08-28); subsequently *Proceedings of the Royal Society A* 478, 20220567. https://arxiv.org/abs/2208.13306
2. M. J. Álvarez, A. Gasull and H. Giacomini (2006), *A new uniqueness criterion for the number of periodic orbits of Abel equations*, arXiv:math/0602468. https://arxiv.org/abs/math/0602468
3. G. Loginov (2021), *Cyclical behavior of evolutionary dynamics in coordination games with changing payoffs*, arXiv:2106.08224. https://arxiv.org/abs/2106.08224
