# Exact reactive-tail coefficient and universal survivor profile for passivating interval walls

## Finding
For a confined diffusing particle with radiation (partially reactive) endpoints whose reactivities decay as \(\kappa(t)=\kappa_*(1+t/t_0)^{-1-\alpha}\), \(\alpha>0\), the exact reaction-time tail amplitude is the never-reacted probability times total relative endpoint reactivity divided by interval length. In addition, the normalized spatial law conditional on survival has an explicit, universal first-order quadratic correction.

Let \(y=x/L\). The precise formulas, uniformly over \(x\in[0,L]\), are
\[
q_t(x)=\frac1L-\frac{\kappa(t)}D\left[a_0\left(\frac13-y+\frac{y^2}2\right)+a_L\left(-\frac16+\frac{y^2}2\right)\right]+o(\kappa(t)),
\]
\[
H(t)\sim\frac{S_\infty(a_0+a_L)}L\kappa(t),\qquad
S(t)-S_\infty\sim\frac{S_\infty(a_0+a_L)\kappa_*t_0^{1+\alpha}}{L\alpha}t^{-\alpha}.
\]
Consequently the previously unspecified reaction-tail amplitude within this interval model is \(A_\alpha=S_\infty(a_0+a_L)\kappa_*t_0^{1+\alpha}/L\). This is a sharp identity in terms of \(S_\infty\), not an asserted elementary formula for \(S_\infty\).

## Assumptions and scope
Fix \(L,D,\kappa_*,t_0>0\), \(\alpha>0\), and fixed \(a_0,a_L\ge0\) satisfying \(a_0+a_L>0\). Let \(u_0\in L^\infty(0,L)\) be nonnegative with \(\int_0^L u_0(x)\,dx=1\). Define \(\kappa(t)=\kappa_*(1+t/t_0)^{-p}\) with \(p=1+\alpha>1\). The nonnegative mild solution \(u\) satisfies
\[
\partial_tu=D\partial_x^2u,\quad
D\partial_xu(0,t)=a_0\kappa(t)u(0,t),\quad
-D\partial_xu(L,t)=a_L\kappa(t)u(L,t).
\]
The survival probability is \(S(t)=\int_0^L u(x,t)\,dx\), the first-reaction density is \(H(t)=-S'(t)\) for \(t>0\), the nonreaction probability is \(S_\infty=\lim_{t\to\infty}S(t)\), and \(q_t=u(\cdot,t)/S(t)\). All asymptotics refer to \(t\to\infty\) at fixed model parameters. A zero coefficient represents a reflecting endpoint; both nonzero coefficients allow distinct reactive walls.

## Proof
**1. Positivity and nonvanishing survival.** Robin positivity and the maximum principle give \(0\le u(x,t)\le \|u_0\|_\infty\); mass balance yields
\[
S'(t)=-\kappa(t)[a_0u(0,t)+a_Lu(L,t)]\le0.
\]
In the reflected-Brownian boundary-local-time representation, the survival weight is \(e^{-Z_t}\), with \(Z_t\) the nonnegative cumulative boundary hazard. Normalize local time so that its mean increments at endpoint \(j\) are \(\int_0^L u_0(z)K_t(z,j)\,dz\,dt\), where \(K\) is the reflecting heat kernel. Symmetry and spatial stochasticity of \(K\) then show
\[
\mathbb E Z_\infty\le\|u_0\|_\infty(a_0+a_L)\int_0^\infty\kappa(s)\,ds<\infty.
\]
Jensen's inequality gives \(S_\infty=\mathbb E e^{-Z_\infty}\ge e^{-\mathbb E Z_\infty}>0\). This argument accommodates nonuniform initial data and arbitrarily strong but finite initial reactivity.

**2. Reflection-kernel decomposition.** The Neumann kernel is
\[
K_t(x,z)=\frac1L+\frac2L\sum_{n=1}^\infty e^{-D(n\pi/L)^2t}\cos\frac{n\pi x}L\cos\frac{n\pi z}L.
\]
Write \(P_t\) for its semigroup and \(h_j(s)=a_j\kappa(s)u(j,s)\) for \(j\in\{0,L\}\). Boundary-flux variation of constants gives the exact mild representation
\[
u(x,t)=P_tu_0(x)-\sum_{j\in\{0,L\}}\int_0^t h_j(s)K_{t-s}(x,j)\,ds.
\]
Let \(w(x,t)=u(x,t)-S(t)/L\). After subtracting the mass identity,
\[
w(x,t)=P_t(u_0-1/L)(x)-\sum_j\int_0^t h_j(s)[K_{t-s}(x,j)-1/L]ds.
\]
The centered kernel envelope \(E(r)=\sup_{x,j}|K_r(x,j)-1/L|\) satisfies \(E(r)\le(2/L)\sum_{n\ge1}e^{-D(n\pi/L)^2r}\); hence \(E\in L^1(0,\infty)\), with an integrable \(O(r^{-1/2})\) singularity at zero and exponential decay at infinity. Since \(h_j\le a_j\kappa\|u_0\|_\infty\) lies in \(L^1\cap L^\infty\), convolution with \(E\) tends uniformly to zero. Thus \(w\to0\) uniformly and \(u(\cdot,t)\to S_\infty/L\) uniformly.

**3. Sharp leading centered profile.** Set \(r=t-s\). For \(0\le r\le t/2\), regular variation gives \(\kappa(t-r)/\kappa(t)\le2^p\). For every fixed \(r\),
\[
\frac{h_j(t-r)}{\kappa(t)}\longrightarrow\frac{a_jS_\infty}{L}.
\]
The bound \(E(r)\in L^1\) permits uniform dominated convergence in this recent-time part. For \(r\ge t/2\), the exponential bound on \(E(r)\) and integrability of \(h_j\) give a contribution \(O(e^{-ct/2})=o(\kappa(t))\). The free centered Neumann term is likewise exponentially negligible. It follows uniformly in space that
\[
\frac{w(x,t)}{\kappa(t)}\longrightarrow
-\frac{S_\infty}{L}\sum_{j\in\{0,L\}}a_jG_j(x),
\qquad
G_j(x)=\int_0^\infty[K_r(x,j)-1/L]dr.
\]
The classical cosine series \(\sum_{n\ge1}\cos(n\pi y)/n^2=\pi^2(1/6-y/2+y^2/4)\) for \(0\le y\le2\) gives
\[
G_0(x)=\frac LD\left(\frac13-y+\frac{y^2}2\right),\qquad
G_L(x)=\frac LD\left(-\frac16+\frac{y^2}2\right).
\]
Because \(S(t)\to S_\infty>0\), dividing the centered expansion by \(S(t)\) yields the stated conditional-density formula. The bracket has zero spatial average, preserving normalization.

**4. Tail coefficient.** Uniform boundary convergence gives
\[
\frac{H(t)}{\kappa(t)}=a_0u(0,t)+a_Lu(L,t)
\longrightarrow\frac{S_\infty(a_0+a_L)}L.
\]
The exact identity \(S(t)-S_\infty=\int_t^\infty H(s)\,ds\) and \(\int_t^\infty\kappa(s)\,ds\sim\kappa_*t_0^pt^{1-p}/(p-1)\) prove the survival-tail and first-reaction-density asymptotics. No adiabatic or small-initial-reactivity assumption is involved.

## Verification
The accompanying standalone `verify.py` performs conservative finite-volume integration with two independent, time-varying Robin boundary sinks; this method differs from the Neumann-kernel derivation. Nine time-point cases cover a reflecting wall, asymmetric two-wall reactivity, and equal reactive walls. At time \(t=240\) (simulation units), the maximum discrepancy of the rescaled conditioned profile is below \(0.00062\) across the three tested models, and all normalized flux ratios lie within \(0.00006\) of one. The numerical tests support but do not prove the asserted infinite-time limits. Run `python verify.py` using Python with NumPy and SciPy.

## Relationship to prior work
Grebenkov and Ye (arXiv:2610.23017v1), Sec. III.3, eq. (43), give the power \(t^{-1-\alpha}\) for \(\alpha>0\) while referring to an unknown prefactor \(A_\alpha\). Their Sec. III.4 identifies a strictly positive nonreaction probability. Those points are prior results. The present interval theorem identifies the exact coefficient \(A_\alpha\) **in terms of that probability** and determines the universal leading conditional spatial profile, including unequal endpoint reactivities, by a direct heat-kernel argument. It does not calculate \(S_\infty\) in elementary form. Earlier time-dependent absorption and Robin-heat formulations overlap at the model level, but the accessible material did not establish the stated combined coefficient-and-profile theorem; see the accompanying review for priority limitations.

## Limitations
The proof assumes a bounded, nonnegative initial density, a finite one-dimensional interval, pure Brownian diffusion with no bulk killing or drift, fixed nonnegative endpoint factors, and power-law integrable decay with \(\alpha>0\). The result is not uniform as \(\alpha\downarrow0\), does not cover nonintegrable or oscillatory wall laws without further argument, and does not give a closed-form value of \(S_\infty\). No claim is made for multidimensional geometries, exact finite-time profiles, or microscopic chemical mechanisms. Independent verification and final literature priority assessment have not been performed.

## References
- Grebenkov, D. S., and Ye, Y. (2026). Diffusion-controlled reactions with time-dependent surface reactivity. arXiv:2610.23017v1, first public 2026-10-16. https://arxiv.org/html/2610.23017v1
- Ré, M. A., and Budde, C. E. (2000). Diffusion-mediated reactions with a time-dependent absorption rate. Phys. Rev. E 61, 1110. https://doi.org/10.1103/PhysRevE.61.1110
- Colantoni, F. (2026). Time-dependent Robin heat equation via Markovian switching. arXiv:2604.27901. https://arxiv.org/abs/2604.27901
- Kay, T., and Giuggioli, L. (2023). Subdiffusion in the Presence of Reactive Boundaries: A Generalized Feynman--Kac Approach. J. Stat. Phys. 190, 92. https://doi.org/10.1007/s10955-023-03105-7
- Chen et al. (2010). Analytic Closed Solution for the Heat Conduction with Time Dependent Heat Convection Coefficient at One Boundary. https://doi.org/10.3970/cmes.2010.059.107
