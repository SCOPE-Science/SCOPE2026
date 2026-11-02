# Exact reset-origin and endpoint singularity phases of nonlinear telegraph-driven velocities

## Finding
Consider the one-dimensional active velocity process with a symmetric telegraph force, a confining nonlinear drag, and Poisson velocity resets that leave the telegraph orientation unchanged. Its stationary velocity density has two independently tunable singularity thresholds. The first is an **exact universal one-sided derivative at the resetting velocity**, whereas the second is an **endpoint power law**. Their combination yields a sharp coexistence criterion for central and boundary peaks in a shear-thinning medium.

Let the force magnitude be \(\Sigma>0\), the sign-flip rate be \(\lambda>0\), and the velocity-reset rate be \(r>0\). Suppose the drag \(g\) is odd, strictly increasing and \(C^2\) on a neighborhood of the accessible velocity interval, with \(g(0)=0\), \(g'(0)=k_0>0\). Assume that \(g(v_*)=\Sigma\) at a finite \(v_*>0\), and \(k_*=g'(v_*)>0\). In the unique stationary distribution, write \(p(v)\) for the total velocity density. Then
\[
\boxed{p'(0+)=-p'(0-)=\frac{r(k_0-2\lambda-r)}{2\Sigma^2}.}
\]
Consequently, \(v=0\) is a **strict local cusp maximum** if \(2\lambda+r>k_0\), and a **strict local cusp minimum** if \(2\lambda+r<k_0\). At equality, the one-sided first derivatives vanish; no higher-order classification is asserted. The origin value \(p(0)\) need not be known to determine the cusp slopes.

At each support endpoint, for some \(C_+>0\) (with the same coefficient at the left endpoint by symmetry),
\[
\boxed{p(v)\sim C_+(v_*-v)^{(r+\lambda)/k_*-1}\quad(v\uparrow v_*).}
\]
Thus the endpoint density diverges if \(r+\lambda<k_*\), tends to \(C_+\) if \(r+\lambda=k_*\), and vanishes if \(r+\lambda>k_*\). More precisely, write the stationary orientation densities \(p_+\) and \(p_-\), and their positive outward/inward probability-current magnitudes
\[
U(v)=(\Sigma-g(v))p_+(v),\qquad W(v)=(\Sigma+g(v))p_-(v),\quad 0<v<v_*.
\]
Then \(U,W>0\) and the ratio at the endpoint obeys the drag-independent law
\[
\boxed{\lim_{v\uparrow v_*}\frac{W(v)}{U(v)}=\frac{\lambda}{r+\lambda}.}
\]

Two particularly relevant drag laws, both used in the source literature, are \(g(v)=\tan v\) (shear thickening) and \(g(v)=\tanh v\) (shear thinning, \(0<\Sigma<1\)). In either case \(k_0=1\). Their endpoint slopes are respectively \(k_*=1+\Sigma^2\) and \(k_*=1-\Sigma^2\). Therefore the strict central-cusp maximum and the divergent endpoint peaks coexist precisely in the parameter region
\[
\boxed{2\lambda+r>1,\qquad \lambda+r<1+\Sigma^2}\quad\text{for \(g=\tan\)},
\]
respectively
\[
\boxed{2\lambda+r>1,\qquad \lambda+r<1-\Sigma^2}\quad\text{for \(g=\tanh\)}.
\]
Each such coexistence forces at least one interior minimum on each side of the origin. For some positive rates \(\lambda,r\), this coexistence **exists for every \(\Sigma>0\)** in the tangent model, but in the hyperbolic-tangent model it is possible **if and only if**
\[
\boxed{0<\Sigma<\frac{1}{\sqrt2}.}
\]
This amplitude threshold is for coexistence of a central *local cusp maximum* and *divergent endpoints*, not a classification of every interior extremum.

There is also a zero-reset-rate morphology discontinuity: for \(g=\tan\) or \(g=\tanh\), if \(1/2<\lambda<1\), the \(r=0\) stationary density has a smooth, strict local minimum at zero, but the density for **every** \(r>0\) has a strict local cusp maximum at zero. Indeed the unreset law satisfies
\[
\frac{p_0''(0)}{p_0(0)}=\frac{2(1-\lambda)}{\Sigma^2}>0,
\]
whereas the displayed reset-origin derivative is negative for all \(r>0\). This is a local statement: no discontinuity in global measures or probability mass is asserted.

## Assumptions and scope
Write \(S_t\in\{+1,-1\}\) for a stationary symmetric two-state continuous-time Markov chain, with independent transitions from each state to the opposite at rate \(\lambda\). Between the events of an independent rate-\(r\) Poisson process, the velocity satisfies
\[
\dot V_t=\Sigma S_t-g(V_t).
\]
At each Poisson event, set \(V_t=0\) without changing \(S_t\). We assume \(\lambda,r,\Sigma>0\), the stated properties of \(g\), and initial velocity in \([-v_*,v_*]\). The vector fields \(\pm\Sigma-g(v)\) preserve this interval. For the named drags, \(g=\tan\) is considered only on its regular interval enclosing \([-v_*,v_*]\), and \(g=\tanh\) requires \(0<\Sigma<1\). The boundary derivative \(k_*\) is finite and positive. The statements concern the unique stationary *velocity* distribution; the spatial coordinate obtained by integrating velocity is not reset.

## Proof
**Existence, uniqueness, and interior regularity.** Start with a stationary two-sided telegraph chain and a stationary independent two-sided Poisson reset process. At a reference time the most recent reset occurred a finite time ago almost surely. Set the velocity to zero at that reset and solve the deterministic, sign-switched ODE forward; this gives a stationary process. To couple two initial laws, first couple the irreducible two-state orientation chains in finite time, then use the same Poisson clock; the velocities coalesce exactly at the first subsequent reset. Hence the stationary velocity-orientation law is unique. Each orientation has marginal probability \(1/2\). The reachable support is \([-v_*,v_*]\). Since the deterministic velocities at zero have opposite nonzero signs, and the coefficients are regular inside the interval, the stationary orientation densities \(p_\pm\) have finite traces and are \(C^1\) on either open side of zero. They are positive inside the accessible support. There is no stationary atom at zero, since trajectories leave the reset point immediately and Poisson events have zero occupation time.

**Transport and the origin.** The stationary forward equations, in distributions, are
\[
0=-\frac{d}{dv}[(\Sigma-g)p_+]-(r+\lambda)p_++\lambda p_-+\frac r2\delta_0,
\]
\[
0=-\frac{d}{dv}[(-\Sigma-g)p_-]-(r+\lambda)p_-+\lambda p_++\frac r2\delta_0.
\]
Define \(p=p_++p_-\), \(d=p_+-p_-\), \(J=\Sigma d-gp\), and \(H=\Sigma p-gd\). Addition and subtraction give
\[
J'=-rp+r\delta_0,\qquad H'=-(r+2\lambda)d.
\]
By confinement and the absence of an external boundary source, the outgoing total flux at \(v_*\) is zero. Reflection symmetry of the unique stationary law gives \(\int_0^{v_*}p(v)\,dv=1/2\). Integrating the first identity from \(0+\) to \(v_*\) therefore yields \(J(0+)=r/2\), so \(d(0+)=r/(2\Sigma)\). Integrating across the delta yields the opposite left trace; their sums show that \(p\) is continuous at zero. Evaluating the second identity on the positive side gives
\[
\Sigma p'(0+)-g'(0)d(0+)=-(r+2\lambda)d(0+),
\]
which proves the origin derivative. Reflection gives the left derivative. Strict local extremum types follow from the sign of the first one-sided derivative.

**Endpoint power and current ratio.** On \((0,v_*)\) put \(f=\Sigma-g>0\), \(b=\Sigma+g>0\), \(a=r+\lambda\), \(U=fp_+\), and \(W=bp_-\). The forward equations become the first-order system
\[
U'=-\frac{a}{f}U+\frac\lambda bW,\qquad
W'=\frac abW-\frac\lambda fU.
\]
The total outward current \(J=U-W\) satisfies \(J'=-rp\), with \(J(v_*)=0\), hence
\[
0<W(v)<U(v)\quad(0<v<v_*).
\]
This inequality and \(b\ge\Sigma\) are crucial: let \(A(v)=\int_0^v a/f(s)\,ds\) and \(Y(v)=e^{A(v)}U(v)\). Then
\[
0\le Y'(v)=\frac\lambda b e^{A(v)}W(v)\le\frac\lambda\Sigma Y(v).
\]
Gronwall's inequality on the bounded interval proves that \(Y\) has a finite strictly positive limit \(Y_*\) at the endpoint. Since
\[
f(v)=k_*(v_*-v)+O((v_*-v)^2),
\]
the difference between \(A(v)\) and \(-a\log(v_*-v)/k_*\) converges to a finite constant. Thus \(U(v)\sim C(v_*-v)^{a/k_*}\) with \(C>0\).

The inward-flow boundary condition is \(W(v_*)=0\). Solving the second equation backward gives
\[
W(v)=\int_v^{v_*}\frac{\lambda U(s)}{f(s)}
\exp\left(-\int_v^s\frac a{b(z)}\,dz\right)ds.
\]
The preceding asymptotic and dominated convergence yield \(W(v)/U(v)\to\lambda/a\). Since \(p_+=U/f\) has order \((v_*-v)^{a/k_*-1}\) while \(p_-=W/b\) has order \((v_*-v)^{a/k_*}\), the claimed density power, the positive coefficient, and all endpoint classifications follow. No endpoint atom exists: deterministic trajectories approach the attracting endpoint asymptotically, and flips and resets have positive rates.

**Coexistence and the small-reset morphology.** In the tangent model \(v_*=\arctan\Sigma\) and \(k_*=1+\Sigma^2\); in the hyperbolic-tangent model \(v_*=\operatorname{arctanh}\Sigma\) and \(k_*=1-\Sigma^2\). Substitution into the two *independent* strict inequalities gives the phase regions. For the hyperbolic-tangent case, those inequalities require \(\Sigma^2<\lambda<1-\Sigma^2\), hence \(\Sigma^2<1/2\). Conversely, if \(\Sigma^2<1/2\), choose \(1/2<\lambda<1-\Sigma^2\) and then \(0<r<1-\Sigma^2-\lambda\). For the tangent case choose \(1/2<\lambda<1+\Sigma^2\) and sufficiently small \(r>0\). In either region the density decreases immediately to the right of zero but diverges at the right endpoint, so an intervening minimum exists; reflection supplies the left minimum.

For \(r=0\), the current vanishes identically and the standard stationary relation is
\[
\frac{d}{dv}[(\Sigma^2-g(v)^2)p_0(v)]=-2\lambda g(v)p_0(v).
\]
Differentiating at zero and using the oddness of \(g\) gives \(p_0'(0)=0\) and
\[
\frac{p_0''(0)}{p_0(0)}=\frac{2k_0(k_0-\lambda)}{\Sigma^2}.
\]
For both named drag laws \(k_0=1\), so \(1/2<\lambda<1\) yields an unreset strict minimum, whereas the reset-origin formula yields a strict maximum for every \(r>0\). This completes the proof.

## Verification
The accompanying `verify.py` integrates the two stationary current equations from an endpoint power-law boundary seed inward, normalizes by \(J(0+)=r/2\), and compares the resulting origin derivative, endpoint logarithmic slope, and inward-to-outward flux ratio with their analytical formulas for seven parameter choices. All 21 numerical comparisons passed. To reproduce: install the dependencies in `requirements.txt`, then run `python verify.py`. These finite ODE calculations test normalization, signs, and constants but do not establish the limiting statements; those are proved above.

## Relationship to prior work
Howlader, Mondal, and Das (2026), arXiv:2606.00560, define precisely this nonlinear-drag velocity-reset model, numerically observe reset-induced origin cusps and changing edge shapes for tangent and hyperbolic-tangent drag, and analyze transport and first-passage behavior. Their printed stationary equations underpin the present calculation. The added results are the **explicit source-normalized cusp derivative**, the **reset-shifted endpoint exponent with a positive coefficient and flux ratio**, their **sharp coexistence boundary**, and the **singular zero-reset local-morphology reversal**.

Dhar, Kundu, Majumdar, Sabhapandit, and Schehr (2018/2019), arXiv:1811.03808, derive stationary telegraph-confinement densities and edge shape transitions *without velocity resetting*. Howlader, Mondal, and Das (2025), DOI:10.1103/sy7f-7mn4, supply tangent-drag stationary phase regimes in the *reset-free* setting. Olsen and Löwen (2024), arXiv:2401.12685, analyze velocity-reset transport and diffusivities for inertial systems; their general transport observables are distinct from the present source-induced stationary cusp and endpoint coexistence criteria. General first-order Markov transport principles are not claimed as new.

## Limitations
The theorem concerns an idealized one-dimensional, athermal, symmetric two-orientation model, an independent Poisson reset clock, fixed reset velocity zero, preserved orientation at resets, smooth monotone odd drag, and finite simple attracting velocity endpoints. No claim is made for position resetting, randomly sampled reset velocities, asymmetric tumbling, nonlinear multistable drags, non-Poisson clocks, velocity diffusion, exact interior mode counts, dynamics of approach to stationarity, or exact first-passage times. At equality in the center cusp threshold the vanishing first derivative alone does not determine higher-order morphology. All originality assessments are conditional on the inspected sources and are not independent publication-priority certification.

## References
1. S. Howlader, S. Mondal, and P. Das, *Velocity Resetting of Inertial Run-and-Tumble Particles in Non-Newtonian Media: Velocity Distribution, Diffusion and First-Passage Time*, arXiv:2606.00560 (first submitted 2026-05-30), https://arxiv.org/abs/2606.00560.
2. A. Dhar, A. Kundu, S. N. Majumdar, S. Sabhapandit, and G. Schehr, *Run-and-tumble particle in one-dimensional confining potential: Steady state, relaxation and first passage properties*, arXiv:1811.03808 (2018), https://arxiv.org/abs/1811.03808.
3. S. Howlader, S. Mondal, and P. Das, *Velocity distribution and diffusion of an athermal inertial run-and-tumble particle in a shear-thickening medium*, Physical Review E 112, 025403 (2025), DOI:10.1103/sy7f-7mn4.
4. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (2024), https://arxiv.org/abs/2401.12685.
