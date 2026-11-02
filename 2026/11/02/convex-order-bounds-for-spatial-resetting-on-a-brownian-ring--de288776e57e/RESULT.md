# Convex-order bounds for spatial resetting on a Brownian ring

## Finding

**Theorem (simultaneously optimal reset-position laws).** Let a Brownian searcher with diffusivity \(D>0\) move on a circle of circumference \(L>0\) toward one absorbing target. Its initial geodesic distance to the target is \(d_0\in(0,L/2]\). At independent Poisson times of rate \(r>0\), it is transported instantaneously to a new location whose geodesic distance \(d\) is independently sampled from a fixed law \(\mu\); the target absorbs upon first contact. Fix \(0<a<b\le L/2\). Restrict reset-distance laws to \([a,b]\) and require the common *unreset search-cost budget*

\[
\mathbb E_\mu U=m,\qquad U=d(L-d),\quad a(L-a)<m<b(L-b).
\]

Define \(u_a=a(L-a)\), \(u_b=b(L-b)\), \(d_m=(L-\sqrt{L^2-4m})/2\), and \(\lambda=(u_b-m)/(u_b-u_a)\). Among every law satisfying these constraints, the deterministic law \(\delta_{d_m}\) **uniquely maximizes the mean target-hitting time** and **uniquely minimizes its Laplace transform at every positive argument**. The two-endpoint law \(\mu_{\rm ext}=\lambda\delta_a+(1-\lambda)\delta_b\) has the opposite two optimalities, uniquely, *for every reset rate* \(r>0\), without any retuning of its weights.

More generally, if two admissible laws induce cost variables ordered by convex order, \(U_1\le_{\rm cx} U_2\), then, for every \(r,s>0\), their target-hitting times satisfy

\[
\mathbb E e^{-s T_r^{(1)}}\le \mathbb E e^{-s T_r^{(2)}},
\qquad
\mathbb E T_r^{(1)}\ge\mathbb E T_r^{(2)}.
\]

Both inequalities are strict when the two cost distributions are different. The Laplace-transform ordering is not asserted to be a usual stochastic ordering of the hitting times or an ordering of all their quantiles.

The fixed-budget advantage has two further sharp limits. Let \(u_0=d_0(L-d_0)\). For each fixed admissible \(\mu\), as \(r\downarrow0\),

\[
\mathbb E T_r^{\delta_{d_m}}-\mathbb E T_r^{\mu}
=\frac{u_0\operatorname{Var}_{\mu}(U)}{48D^3}r^2+O(r^3).
\]

In particular, the endpoint spread gives the largest quadratic coefficient, because its variance equals \((u_b-m)(m-u_a)\). At high rates the ratio of the endpoint mean to the deterministic mean obeys

\[
\frac{\mathbb E T_r^{\mu_{\rm ext}}}{\mathbb E T_r^{\delta_{d_m}}}
\sim\frac{1}{\lambda}\exp\!\left[-(d_m-a)\sqrt{r/D}\right],\qquad r\to\infty.
\]

The fixed-cost bounds therefore persist across all resetting rates even though both mean times eventually diverge when \(a>0\).

## Assumptions and scope

Brownian motion is one-dimensional along the circle and has generator \(D\partial_x^2\) between resets. Reset times form a homogeneous Poisson process independent of the Brownian path and all sampled reset positions. Successive reset positions are independent and identically distributed. All target-hitting times are measured starting at the specified initial distance \(d_0\), not from the reset-position law. The reset law need not possess a density. Two points symmetric about the target have the same geodesic distance; uniqueness refers to the induced distribution of that distance, not to how probability is divided between those symmetric physical locations. The mean unreset hitting time from distance \(d\) is \(U/(2D)\), making the constraint a direct fixed mean free-search-cost budget. We require \(a>0\), so reset events never instantaneously put the particle on the target.

## Proof

**1. Killed-circle resolvent and free mean.** Cutting the circle at the target identifies the unreset problem with Brownian motion on \((0,L)\) killed at either endpoint. The unique solution to \(D\psi''=q\psi\), with \(\psi(0)=\psi(L)=1\), is

\[
\psi_q(d)=\mathbb E_d e^{-qT_0}
=\frac{\cosh[\sqrt{q/D}(L/2-d)]}{\cosh[\sqrt{q/D}L/2]},\quad 0\le d\le L/2,
\]

for every \(q>0\). The unique solution to \(Dv''=-1\) with zero boundary values yields \(\mathbb E_d T_0=d(L-d)/(2D)\).

**2. Exact resetting renewal identity.** Put \(\beta_\mu(q)=\int\psi_q(d)\,\mu(dd)\). Conditioning on the first reset or first absorption, then restarting from the reset law, gives for every \(r,s>0\)

\[
\mathcal L_\mu(s)=\mathbb E_{d_0} e^{-sT_r}
=\frac{s\psi_{s+r}(d_0)+r\beta_\mu(s+r)}{s+r\beta_\mu(s+r)}.
\]

Its derivative at \(s=0+\) yields

\[
M_\mu(r)=\mathbb E_{d_0}T_r
=\frac{1-\psi_r(d_0)}{r\beta_\mu(r)}.
\]

The expectation is finite for all \(r>0\), since \(\beta_\mu(r)>0\). For fixed \(r,s\), differentiation with respect to the scalar \(\beta=\beta_\mu(s+r)\) gives

\[
\frac{d}{d\beta}\frac{s\psi_{s+r}(d_0)+r\beta}{s+r\beta}
=\frac{rs[1-\psi_{s+r}(d_0)]}{(s+r\beta)^2}>0.
\]

Likewise, \(M_\mu(r)\) decreases strictly in \(\beta_\mu(r)\).

**3. Strict convexity in free-search cost.** The map \(d\mapsto u=d(L-d)\) is strictly increasing on \([0,L/2]\), with inverse \(d=(L-\sqrt{L^2-4u})/2\). Set \(k=\sqrt{q/D}\) and \(y=\sqrt{L^2/4-u}\). The unreset hitting transform as a function of cost is

\[
f_q(u)=\frac{\cosh(ky)}{\cosh(kL/2)}.
\]

For \(y>0\), direct differentiation gives

\[
f_q''(u)=\frac{k[ky\cosh(ky)-\sinh(ky)]}{4y^3\cosh(kL/2)}>0.
\]

Indeed \(z\cosh z-\sinh z\) is strictly positive for \(z>0\), because it vanishes at zero and its derivative is \(z\sinh z>0\). At the boundary \(y=0\), the continuous value is \(k^4/[12\cosh(kL/2)]>0\). Therefore \(\beta_\mu(q)=\mathbb E f_q(U)\) is monotone under convex order, and is strictly larger when two convex-ordered cost laws differ: the stop-loss representation of a smooth strictly convex function integrates the positive second derivative against \(\mathbb E(U-t)_+\), so a nonidentical convex-order pair yields a strictly positive integral. Step 2 transfers this order to the whole family of completed-hitting-time Laplace transforms, and reverses it for their means.

**4. Sharp laws and equality.** For a random variable \(U\in[u_a,u_b]\) with mean \(m\), Jensen's inequality and the secant/chord inequality give

\[
f_q(m)\le \mathbb E f_q(U)
\le \lambda f_q(u_a)+(1-\lambda)f_q(u_b),\qquad q>0.
\]

Strict convexity makes equality on the left possible only if \(U=m\) almost surely, and equality on the right possible only if \(U\) is supported on \(\{u_a,u_b\}\). The mean then fixes the endpoint weights uniquely. Since cost increases strictly with distance, these are exactly \(\delta_{d_m}\) and \(\mu_{\rm ext}\). The equality characterizations hold for each single \(q>0\), hence for every \(r,s>0\) simultaneously.

**5. Weak-reset cancellation and high-reset separation.** Uniformly over \(d\in[0,L/2]\), Taylor expansion of the killed-circle resolvent gives

\[
\psi_q(d)=1-\frac{qU}{2D}
+\frac{q^2U(L^2+U)}{24D^2}+O(q^3).
\]

At fixed \(\mathbb E U=m\), first-order terms in the two \(\beta\) functions cancel. Their quadratic difference is \(r^2\operatorname{Var}_\mu(U)/(24D^2)+O(r^3)\). Substitution into the exact mean formula, using \((1-\psi_r(d_0))/r=u_0/(2D)+O(r)\), produces the claimed \(u_0\operatorname{Var}(U)r^2/(48D^3)\) law. The endpoint maximum variance follows from \(\mathbb E[(U-u_a)(u_b-U)]\ge0\), whose expansion bounds the variance by \((u_b-m)(m-u_a)\), with equality only for endpoint support.

For \(r\to\infty\), because \(0<a<d_m<b\le L/2\), the killed transform obeys \(\psi_r(d)\sim\exp[-d\sqrt{r/D}]\) at each fixed \(d<L/2\); a harmless factor of two arises at \(d=L/2\), but its contribution is exponentially negligible compared with \(d=a\). Consequently \(\beta_{\rm ext}(r)\sim\lambda\psi_r(a)\), and \(\beta_{\delta_{d_m}}(r)=\psi_r(d_m)\). Their ratio in the exact mean identity establishes the final exponential-ratio asymptotic. This finishes the proof.

## Verification

The independent finite checker `verify.py` uses Python's standard library and runs with `python verify.py`; it reports `PASS 921 finite checks`. It tests the strict optimization inequalities for multiple parameter grids, uniform weak-reset cancellation, high-reset asymptotic ratios, and an independently discretized backward equation for the resetting hitting-time transform. Its finite computations supplement but do not establish the continuum theorem, which follows from the resolvent, renewal identity, and strict-convexity proof above.

## Relationship to prior work

Julián-Salgado and collaborators (2026, arXiv:2605.08414) introduced and analyzed Brownian resetting on a ring, including optimizing the rate with one or two preassigned reset sites and phase transitions. Méndez, Flaquer-Galmés, and Campos (2024, arXiv:2401.01125) studied random reset positions, their renewal transform, and an equivalent deterministic resetting point at fixed rate. Julián-Salgado, Dagdug, and Boyer (2025, arXiv:2507.14483) studied optimization for distributed resets on the half-line, with prescribed families and rate transitions. Evans and Majumdar (2011, arXiv:1107.4225) developed the foundational renewal approach to resetting and variable reset locations. The backward diffusion formula, renewal decomposition, Jensen's inequality, and convex order are standard and are not claimed as new. The assessed result is the simultaneous sharp pair of extremizers for *all* reset rates and *all* hitting-time Laplace parameters under the physically motivated fixed mean free-search-cost budget, plus the weak/strong resetting separation laws.

## Limitations

Laplace-transform ordering does not imply a pathwise coupling or ordinary stochastic dominance, and no universal ordering of all hitting-time quantiles is claimed. The equality rigidity is for the geodesic-distance law, not for angular location labels. The theorem assumes a single absorbing point, a homogeneous circle, independent Poisson event times, instantaneous complete resetting, i.i.d. reset positions, a strictly positive lower reset distance, and a fixed mean free-search-cost budget. It does not optimize over the resetting rate, reset-time distribution, moving target, or cost of relocating a particle. The result and priority assessment have not undergone independent external audit. General convex-order methods might provide a broader antecedent; the statement is confined to the specific physically motivated ring-reset model.

## References

1. P. Julián-Salgado and collaborators, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, first public preprint 2026-05-08, https://arxiv.org/abs/2605.08414.
2. I. Méndez, E. Flaquer-Galmés, and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, first public preprint 2024-01-02, https://arxiv.org/abs/2401.01125.
3. P. Julián-Salgado, L. Dagdug, and D. Boyer, *Abrupt transitions in the optimization of diffusion with distributed resetting*, first public preprint 2025-07-19, https://arxiv.org/abs/2507.14483.
4. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, 2011, https://arxiv.org/abs/1107.4225.
