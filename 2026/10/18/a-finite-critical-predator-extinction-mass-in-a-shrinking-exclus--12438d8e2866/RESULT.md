# A finite critical predator-extinction mass in a shrinking exclusion-zone habitat

## Finding
Consider the two-species reaction–diffusion system in which prey occupy the entire interval \(\Omega=(0,L)\), predators occupy only \(A=(0,a)\), and both species satisfy no-flux conditions on their respective boundaries. At the critical conversion–mortality equality \(\gamma=\alpha\), all sufficiently small nonzero predator introductions near the prey carrying-capacity state become extinct. The extinction is algebraic rather than exponential, with an **exact geometry-dependent amplitude**.

Write \(\lambda=r(1-\theta)\), \(\kappa=\sqrt{\lambda/d_u}\), and
\[
 s_a=\frac{1}{\lambda}\left(1-\frac{\sinh(\kappa(L-a))\sinh(\kappa a)}{\kappa a\sinh(\kappa L)}\right)>0.
\]
Then, with \(z(t)=a^{-1}\int_0^a v(t,x)\,dx\),
\[
 \lim_{t\to\infty}tz(t)=\frac{1}{\alpha\beta s_a},\qquad
 \lim_{t\to\infty}\left\|tv(t,\cdot)-\frac{1}{\alpha\beta s_a}\right\|_{C([0,a])}=0.
\]
The prey deficit has the uniform asymptotic profile
\[
 \lim_{t\to\infty}\left\|t(1-u(t,\cdot))-\frac{\psi_a}{\alpha s_a}\right\|_{C([0,L])}=0,
\qquad \psi_a=(-d_u\partial_{xx}+\lambda)_{N}^{-1}{\bf1}_{(0,a)}.
\]
Crucially, the leading predator amplitude is independent of positive predator diffusion \(d_v\), although it depends on prey diffusion \(d_u\). Taking the long-time limit **before** shrinking the predator habitat gives
\[
 \boxed{\lim_{a\downarrow0}\lim_{t\to\infty}t\int_0^a v(t,x)\,dx
 =\frac{\sqrt{\lambda d_u}\,\tanh(L\sqrt{\lambda/d_u})}{\alpha\beta}>0.}
\]
This statement concerns transient, vanishing predator populations at the threshold; it does not assert positive coexistence equilibria at criticality.

## Assumptions and scope
Fix \(L>0\), \(0<a<L\), \(d_u,d_v,r,\alpha,\beta>0\), and \(0<\theta<\tfrac12\). The prey growth function is the strong-Allee cubic \(f(u)=r u(u-\theta)(1-u)\). The system is
\[
\begin{aligned}
 u_t&=d_u u_{xx}+f(u)-\beta {\bf1}_{(0,a)}uv,&&0<x<L,\\
 v_t&=d_v v_{xx}+\alpha(u-1)v,&&0<x<a,\\
 u_x(t,0)&=u_x(t,L)=0,\\
 v_x(t,0)&=v_x(t,a)=0.
\end{aligned}
\]
Here the usual predator mortality and conversion parameters satisfy \(\gamma=\alpha\); thus the predator equation is the critical specialization of \(v_t=d_v v_{xx}+(\alpha u-\gamma)v\). Take compatible, nonnegative, sufficiently regular initial data with \(1-\varepsilon\le u_0\le1\) on \([0,L]\), \(0\le v_0\le\varepsilon\) on \([0,a]\), and \(v_0\not\equiv0\). For each fixed admissible parameter set there is \(\varepsilon_0>0\) such that all claims hold whenever \(0<\varepsilon<\varepsilon_0\). Piecewise-smooth prey forcing at \(x=a\) is understood in the standard mild/parabolic sense, with uniform spatial limits; the initial profiles may be \(C^{2+\sigma}\) with Neumann compatibility.

The limits are valid for each fixed positive \(a\) and \(d_v\). No uniform-in-\(a\) or uniform-in-\(d_v\) time-to-asymptotics estimate is asserted.

## Proof
**Step 1: invariant region and uniformly small prey deficit.** Set \(w=1-u\). Comparison at \(u=0,1\) gives \(0\le u\le1\); the predator equation is scalar linear with nonnegative initial data, hence \(0\le v(t,\cdot)\le\|v_0\|_\infty\). Also
\[
 w_t=d_u w_{xx}-f(1-w)+\beta {\bf1}_{(0,a)}(1-w)v.
\]
Since \(f(1-w)=\lambda w+O(w^2)\), choose \(0<\delta<1-\theta\) such that \(f(1-w)\ge(\lambda/2)w\) on \([0,\delta]\). Decrease \(\delta\) if necessary so that \(\alpha\delta<\tfrac14\min\{\lambda,d_v\pi^2/a^2\}\). For sufficiently small \(\varepsilon\), scalar comparison yields
\[
0\le w(t,x)\le\varepsilon e^{-\lambda t/2}+\frac{2\beta\varepsilon}{\lambda}<\delta.
\]
This bootstrap is closed for all times; boundedness and parabolic continuation give a global nonnegative solution.

**Step 2: predator and prey converge to their boundary equilibrium.** Define \(z(t)=a^{-1}\int_Av(t,x)\,dx\). Positivity of the Neumann heat kernel gives \(z(t)>0\) for \(t>0\), and
\[
 z'(t)=-\frac{\alpha}{a}\int_A w(t,x)v(t,x)\,dx,\qquad
 -\alpha\delta z(t)\le z'(t)\le0.
\]
For every \(t\ge1\), the strictly positive upper and lower bounds on the Neumann heat kernel over a unit time step, together with \(0\le\alpha w\le\alpha\delta\), yield constants \(0<c<C<\infty\) such that
\[
 c z(t)\le v(t,x)\le C z(t)\quad\text{for all }x\in[0,a].
\]
Indeed, the one-step bounds are initially in terms of \(z(t-1)\), and the differential inequality for \(z\) compares \(z(t-1)\) to \(z(t)\). If \(z(t)\) tended to a strictly positive value, the lower predator bound would produce a time-uniform positive prey deficit on \(A\): compare the \(w\)-equation from below with the stable forced heat equation \(q_t=d_u q_{xx}-M q+c_0{\bf1}_{A}\), using bounded derivatives of \(f\), \(1-w\ge1-\delta\), and a positive forcing constant. This would force \(z'(t)\le-c_1<0\), a contradiction. Therefore \(z(t)\to0\), hence \(v(t,\cdot)\to0\) uniformly. The stable \(w\)-comparison from Step 1, with \(\|v(t)\|_\infty\to0\), then gives \(w(t,\cdot)\to0\) uniformly.

**Step 3: the predator's neutral spatial mode dominates.** Since \(w(t)\to0\),
\[
\frac{d}{dt}\log z(t)=-\alpha\frac{\int_Awv}{\int_Av}\longrightarrow0.
\]
Thus \(z(t-h)/z(t)\to1\) for every fixed \(h\ge0\). For any \(s\le t\) there is also the uniform bound \(z(s)/z(t)\le e^{\alpha\delta(t-s)}\). Write \(v=z+\eta\), with \(\int_A\eta=0\). Then
\[
 \eta_t=d_v\eta_{xx}-\alpha\left(wv-\frac1a\int_Awv\right).
\]
The Neumann heat semigroup restricted to zero-mean functions decays exponentially, at its spectral gap \(\mu=d_v\pi^2/a^2\). Because \(\|wv\|_\infty=o(z)\), variation of constants and \(\alpha\delta<\mu/4\) show
\[
\|\eta(t)\|_\infty=o(z(t)).
\]
To justify the convolution ratio, split at a fixed large time, use \(z(s)/z(t)\le e^{\alpha\delta(t-s)}\) for domination by the integrable kernel \(e^{-(\mu-\alpha\delta)(t-s)}\), then use the vanishing factor \(\|w(s)\|_\infty\). The initial transient divided by \(z(t)\) vanishes exponentially. Consequently \(v(t,\cdot)/z(t)\to1\) uniformly.

**Step 4: the spatial prey-response kernel.** Let \(B=d_u\partial_{xx}-\lambda\), with Neumann boundaries. The prey equation is
\[
 w_t=Bw+\beta{\bf1}_A v+R(t,x),\qquad
 |R|\le C(w^2+wv)
\]
while \(w\le\delta\). The stable comparison bound and \(\|v(t)\|\le C z(t)\) imply \(\|w(t)\|\le C' z(t)\) for large \(t\): apply the \(e^{-\lambda t/2}\) kernel and the estimate \(z(s)/z(t)\le e^{\alpha\delta(t-s)}\). Hence \(\|R(t)\|=o(z(t))\). Variation of constants, \(v/z\to1\), and \(z(t-h)/z(t)\to1\) now yield
\[
\frac{w(t,\cdot)}{z(t)}\longrightarrow\beta\int_0^\infty e^{hB}{\bf1}_A\,dh
=\beta\psi_a
\]
uniformly on \([0,L]\). The operator integral is the strictly positive Neumann inverse \((-B)^{-1}\).

**Step 5: exact slow amplitude.** Steps 3–4 and the identity for \(z'\) imply
\[
-\frac{z'(t)}{z(t)^2}
=\frac{\alpha}{a}\int_A\frac{w(t,x)}{z(t)}\frac{v(t,x)}{z(t)}\,dx
\longrightarrow\alpha\beta s_a>0.
\]
Integrate \((1/z)'\) and divide by time: \(1/(t z(t))\to\alpha\beta s_a\). Substitution into Steps 3–4 gives both uniform profile limits.

**Step 6: solve the geometry.** Put \(\kappa=\sqrt{\lambda/d_u}\). The unique continuous, continuously differentiable, Neumann solution of \(-d_u\psi_a''+\lambda\psi_a={\bf1}_A\) is
\[
\psi_a(x)=\begin{cases}
\displaystyle\frac{1}{\lambda}\left[1-\frac{\sinh(\kappa(L-a))}{\sinh(\kappa L)}\cosh(\kappa x)\right],&0\le x\le a,\\[4pt]
\displaystyle\frac{\sinh(\kappa a)}{\lambda\sinh(\kappa L)}\cosh(\kappa(L-x)),&a\le x\le L.
\end{cases}
\]
Both derivatives vanish at their outer endpoints, and the values and fluxes agree at \(a\). Integration over \((0,a)\) gives the stated expression for \(s_a\). Positivity follows either from the positive Neumann resolvent or directly from the formula. Taylor expansion gives \(s_a/a\to(\kappa/\lambda)\coth(\kappa L)\); therefore \(a/(\alpha\beta s_a)\to\lambda\tanh(\kappa L)/(\alpha\beta\kappa)\), as asserted.

## Verification
The complete proof is analytic. The self-contained standard-library script `verify.py` independently solves the Neumann resolvent on uniform finite-volume meshes, checks reconstructed linear equations to numerical tolerance, compares the solution with the closed-form profile and integrated coefficient for five parameter tuples and two meshes, and checks the thin-zone limit for three parameter tuples. Its 16 test instances pass. A separate symbolic check confirms continuity of the profile and derivative at the interface, the integrated formula, and the limiting coefficient. These finite calculations corroborate algebra; they do not certify the infinite-dimensional asymptotics, which follow from the semigroup argument above.

## Relationship to prior work
Berestycki, Fagan, and Safsten (arXiv:2602.21414, first public version 2026-02-24) introduce precisely this exclusion-zone reaction–diffusion model and investigate coexistence equilibria and thin-zone limits when predators can persist. Their Proposition 1.1 establishes predator extinction for the strictly subcritical condition \(\alpha<\gamma\); their equilibrium theorems focus on \(\alpha>\gamma\). The present claim instead treats the critical boundary \(\alpha=\gamma\), gives a non-exponential universal long-time relaxation amplitude, and then takes a different **iterated** thin-zone limit. It neither reproduces nor asserts a positive critical equilibrium.

Earlier protection-zone studies by Du and Shi (2006), Cui–Shi–Wu (2014), and Min–Wang (2018) analyze population dynamics, stability, persistence, and stationary spatial patterns. The 2014 model has saturating Holling-II predation, and the 2018 model uses ratio-dependent predation; neither is the present bilinear critical system. General reaction–diffusion semigroup spectral gaps and elliptic Neumann resolvents are standard mathematical ingredients, not claimed as new.

## Limitations
The conclusion assumes small initial perturbations of the high-prey predator-free state, one contiguous boundary-attached predator zone, constant positive diffusion rates, exact conversion–mortality equality, and a cubic strong-Allee prey response. It does not claim a global basin of attraction for large predator introductions (which may overexploit the prey), uniformity of convergence as \(a\to0\), exponential predator decay, persistence at the critical threshold, or a statement about field data. The limit \(a\to0\) is taken **after** \(t\to\infty\); interchanging the limits is not justified. Relevant unindexed literature and adaptations of general infinite-dimensional center-manifold theorems remain originality risks. No independent scientific validation has been performed.

## References
1. H. Berestycki, W. F. Fagan, A. Safsten, *The Influence of Exclusion Zones on the Coexistence of Predator and Prey with an Allee Effect*, arXiv:2602.21414 (initial preprint 2026-02-24), https://arxiv.org/abs/2602.21414.
2. Y. Du, J. Shi, *A diffusive predator-prey model with a protection zone*, Journal of Differential Equations 229 (2006), 63–91, doi:10.1016/j.jde.2006.01.013.
3. R. Cui, J. Shi, B. Wu, *Strong Allee effect in a diffusive predator-prey system with a protection zone*, Journal of Differential Equations 256 (2014), 108–129, doi:10.1016/j.jde.2013.08.015.
4. N. Min, M. Wang, *Dynamics of a diffusive prey-predator system with strong Allee effect growth rate and a protection zone for the prey*, Discrete and Continuous Dynamical Systems B 23 (2018), 1721–1737, doi:10.3934/dcdsb.2018073.
