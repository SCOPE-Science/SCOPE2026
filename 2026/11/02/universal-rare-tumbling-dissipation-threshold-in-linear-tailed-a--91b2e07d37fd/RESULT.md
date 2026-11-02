# Universal rare-tumbling dissipation threshold in linear-tailed active traps

## Finding

Consider a thermally diffusing one-dimensional run-and-tumble particle whose orientation reverses at rate \(r>0\) and whose active speed is \(v>0\). If its potential is arbitrary in a compact region but has equal, exactly linear restoring tails of slope \(b>0\), its stationary entropy-production rate \(\mathcal E_r\), in the convention of symmetric internal flips and overdamped thermal dissipation, satisfies

\[
\boxed{\lim_{r\downarrow0}\mathcal E_r=\frac{(v^2-b^2)_+}{T},\qquad (y)_+=\max\{y,0\}.}
\]

This limit is independent of the potential's number of wells, their depths, their locations, and the thermal diffusivity \(T>0\) except for the explicit prefactor \(1/T\). The same threshold separates two mutually exclusive stationary localization behaviors: below threshold the joint stationary distribution converges to the equal mixture of the two *frozen-orientation tilted Gibbs states*, whereas at and above threshold the position distribution **escapes every fixed compact set** as \(r\downarrow0\).

In particular, this applies to the bistable piecewise-linear potential \(U(x)=b\lvert\lvert x\rvert-a\rvert\), \(a>0\), introduced in the motivating work. The limiting positive entropy production for \(v>b\) persists although switches become arbitrarily rare, because a frozen orientation can then carry the particle outward to distances diverging as \(r\downarrow0\).

## Assumptions and scope

Let \(T,b,v>0\), and let \(R>0\). The potential \(U:\mathbb R\to\mathbb R\) is locally absolutely continuous, with bounded force \(f=-U'\) that is piecewise continuous with finitely many jumps on compact intervals; for all \(x\ge R\), \(f(x)=-b\), and for all \(x\le-R\), \(f(x)=b\), almost everywhere. A continuous bounded force with these same tails is included. The dynamics are

\[
 dX_t=[f(X_t)+vS_t]dt+\sqrt{2T}\,dB_t,
 \qquad S_t\in\{-1,+1\},
\]

where \(B_t\) is standard Brownian motion, independent of \(S_t\), and each orientation reverses at rate \(r\). Let \(\mu_r\) be the unique stationary probability measure of \((X,S)\), and let \(p_{r,\pm}\) denote its two spatial densities. Entropy production is the nonnegative stationary total entropy-production rate of the Fokker–Planck process with equal forward/backward flip rates and with the orientation treated as an internal state. Mobility and Boltzmann's constant are set to one, so \(T\) also denotes translational diffusivity. This is the entropy convention in the cited motivating studies; different time-reversal conventions for self-propulsion require separate treatment.

The theorem holds pointwise for each fixed \(U,b,v,T\) as \(r\downarrow0\). No uniform statement as \(T\to0\), \(b\to v\), or as the interior potential varies is claimed.

## Proof

**1. Stationary measures and moment integrability.** For each \(r>0\), the generator acting on a test function \(g(x,s)\) is

\[
 \mathcal L_r g=T\partial_{xx}g+(f(x)+vs)\partial_xg
 +r\{g(x,-s)-g(x,s)\}.
\]

Outside \([-R,R]\), set \(V(x,s)=e^{\theta|x|}h_{s\operatorname{sgn}(x)}\), with the two positive entries of \(h\) chosen as a Perron eigenvector of the orientation-flip matrix with diagonal contributions \(\theta(-b+vs)+T\theta^2\). The largest eigenvalue is

\[
 \Lambda_r(\theta)=-b\theta+T\theta^2-r+\sqrt{r^2+v^2\theta^2}.
\]

For any fixed \(r>0\), \(\Lambda_r(\theta)<0\) for all sufficiently small \(\theta>0\), since \(\Lambda_r'(0)=-b\). Patching \(V\) to a positive smooth function inside a compact region gives a Foster–Lyapunov drift inequality. Uniform ellipticity, orientation irreducibility, and the drift inequality establish existence and uniqueness of \(\mu_r\), and \(\mathbb E_{\mu_r}e^{\theta|X|}<\infty\) for a possibly \(r\)-dependent \(\theta\). The stationary orientation marginal is exactly \((1/2,1/2)\).

**2. Entropy–force identity.** Write the stationary orientation currents as

\[
 J_\pm=(f\pm v)p_{r,\pm}-T\partial_xp_{r,\pm}.
\]

Normalization at infinity and conservation give \(J_++J_-=0\) pointwise. At stationarity, the total entropy production equals the thermal entropy flow, since the internal switch rates are symmetric. Using the current formula and integrating derivative terms at infinity gives the exact identity

\[
 \boxed{\mathcal E_r=\frac{v}{T}\left(v+\mathbb E_{\mu_r}[f(X)S]\right).}
\]

For completeness, the usual nonnegative expression \(\sum_s\int J_s^2/(Tp_s)+r\int(p_+-p_-)\log(p_+/p_-)\) equals the medium flow: integration by parts and the stationary continuity equations cancel the flip-dependent contribution. Hence the identity includes both thermal and internal contributions, without suppressing hidden dissipation.

**3. Subcritical active speed \(0<v<b\).** Outside \([-R,R]\), the state-independent test function \(e^{\theta|x|}\) satisfies \(\mathcal L_rV/V\le-\theta(b-v)+T\theta^2\) for every orientation and all \(r>0\). Choosing \(0<\theta<(b-v)/T\) gives a *uniform-in-\(r\)* exponential moment bound. Every weak accumulation point as \(r\downarrow0\) is therefore a full probability measure. The stationary weak equation for a compactly supported test function and the vanishing switch term show that each orientation's limiting component is invariant under the frozen diffusion with drift \(f(x)\pm v\). Its unique probability density is proportional to \(\exp[-(U(x)\mp vx)/T]\), which is integrable because \(v<b\). Since each component has mass \(1/2\), the entire family converges to

\[
 \mu_0(dx,ds)=\tfrac12\,Z_s^{-1}e^{-[U(x)-svx]/T}\,dx.
\]

Integrating the derivative of each tilted Gibbs density yields \(\mathbb E[f(X)\mid S=s]=-sv\). Thus \(\mathbb E_{\mu_r}[f(X)S]\to-v\), and Step 2 gives \(\mathcal E_r\to0\).

**4. At and above the threshold \(v\ge b\).** Fix any sequence \(r_n\downarrow0\). Bounded total mass implies vague subsequential compactness of each orientation's stationary spatial measure. In the stationary weak equation, its switching term is bounded by \(2r_n\|\varphi\|_\infty\) for any compactly supported smooth \(\varphi\), so any vague limit is a *finite invariant subprobability* for the corresponding frozen diffusion. This remains valid across finitely many force jumps, by the local one-dimensional stationary current equations and ellipticity. However, for \(s=+1\), the frozen drift on the right tail is \(v-b\ge0\); for \(s=-1\), the frozen drift on the left tail is \(-(v-b)\le0\). Neither frozen diffusion has a nonzero finite invariant measure: any such invariant density would have zero current and be proportional to \(\exp[-(U(x)-svx)/T]\), which is nonintegrable on the indicated tail. Hence every vague limit is zero, and

\[
 \boxed{\lim_{r\downarrow0}\mu_r\{|X|\le K\}=0\quad\text{for every fixed }K>0.}
\]

For a smooth even function \(g\) equal to \(|x|\) outside a small fixed interval, use \(\int\mathcal L_rg\,d\mu_r=0\), justified by the exponential moment from Step 1. Here \(g'=\operatorname{sgn}(x)\) on both tails, \(g''\) has compact support, and the force there equals \(-b\operatorname{sgn}(x)\). The compact-escape result gives

\[
 0=-b+v\lim_{r\downarrow0}\mathbb E_{\mu_r}[S\operatorname{sgn}(X)],
 \quad\text{so}\quad
 \lim_{r\downarrow0}\mathbb E_{\mu_r}[S\operatorname{sgn}(X)]=\frac bv.
\]

The difference between \(f(X)S\) and \(-bS\operatorname{sgn}(X)\) vanishes in expectation since it is bounded and supported in \([-R,R]\). Consequently \(\mathbb E[f(X)S]\to-b^2/v\), and Step 2 gives

\[
 \lim_{r\downarrow0}\mathcal E_r=\frac{v^2-b^2}{T}.
\]

At \(v=b\), the same proof gives zero and complete compact escape. Combining Steps 3 and 4 proves the theorem, including the sharp threshold and both stationary localization regimes.

## Verification

Run `python verification.py` (requires NumPy and SciPy). The script checks the two-decay-mode exact stationary solution for the single-cusp potential \(U(x)=b|x|\), evaluates both subcritical and supercritical small-switch limits, and independently solves discretized coupled steady-state generators for single-cusp, bistable, and asymmetric interior forces. It reports \(99\) deterministic assertions passed. For example, at \((b,T,v,r)=(1,0.7,1.5,0.00032)\) the exact single-cusp entropy production is \(1.78656660\), against the theorem's limit \(1.78571429\); at \(v=0.6\) the exact value at that flip rate is \(0.00032447\), against the limit zero. Reflected finite-volume boundaries and spatial discretization introduce finite-\(r\) errors; these computations are independent consistency checks, not the proof of the infinite-time or rare-switching limits.

## Relationship to prior work

Singh and Aghion (2026), arXiv:2610.08029, specify the bistable force, stationary Fokker–Planck equations, explicit density coefficients, and stationary entropy-flow formula (notably their Sections 2–3 and 7, equations (1)–(4) and (41)–(46)). Singh and Farago (2025), arXiv:2506.02645, give a two-mode density and exact entropy production for the single-cusp potential \(U(x)=b|x|\) (Sections 2 and 5, equations (8), (38)–(40)); the single-cusp specialization is therefore **not** claimed as an independent density formula or wholly new model. Frydel (2022), DOI:10.1103/PhysRevE.105.034113, discusses the frozen-orientation equilibrium limit and entropy suppression in confining examples, and Garcia-Millan and Pruessner (2021), arXiv:2012.02900, treat harmonic confinement. The present theorem adds a sharp universal rare-switching classification simultaneously for every bounded interior deformation of a trap with fixed linear tails, including nonconvex and asymmetric potentials: whether spatial mass remains tight or escapes, and whether entropy vanishes or retains a strictly positive limit, is completely determined by the tail slope and active speed. Existing exact one-well density formulas and general current identities are credited, not rebranded as novel.

## Limitations

The statement fixes the thermal diffusion \(T>0\), the potential and active speed before taking \(r\downarrow0\). It does not give a uniform rate of convergence near \(v=b\), a classification for different left/right tail slopes or non-Poisson tumbles, or a result for unbounded active forces. The stationary entropy convention treats the internal direction as an even state under time reversal; an alternative physical reversal protocol may alter the reported entropy production. Prior general entropy-current identities and single-cusp formulas are strong conceptual antecedents; publication-priority assessment for the universal arbitrary-interior threshold is not independently verified.

## References

1. R. K. Singh and E. Aghion, *Spatial density, first passage times, and entropy of run and tumble particles in a bistable potential* (2026), arXiv:2610.08029, https://arxiv.org/html/2610.08029v1 (public 2026-10-06).
2. R. K. Singh and O. Farago, *Steady state and relaxation dynamics of run and tumble particles in contact with a heat bath* (2025), arXiv:2506.02645, https://arxiv.org/html/2506.02645v1 (public 2025-06-03).
3. D. Frydel, *Intuitive view of entropy production of ideal run-and-tumble particles*, Phys. Rev. E 105, 034113 (2022), https://doi.org/10.1103/PhysRevE.105.034113.
4. M. Paoluzzi, A. Puglisi and L. Angelani, *Entropy Production of Run-and-Tumble Particles*, Entropy 26, 443 (2024), https://doi.org/10.3390/e26060443.
5. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, J. Stat. Mech. 2021, 063203, https://arxiv.org/abs/2012.02900.
