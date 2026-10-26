# Universal midpoint maximum of the optimal restart rate across a permeable interface

## Finding

A one-dimensional semipermeable interface produces a parameter-independent *geometric maximum* of the optimal Poisson restart rate, although the mean search time itself decreases with interface position. For every finite positive permeability and any fixed target-reset separation, the optimal restart rate is largest precisely when the interface is halfway between the absorbing target and reset point. The model allows resets across the membrane; it is not the interface-screened restart model.

Fix \(D>0\), \(L>0\), \(\kappa>0\), and \(b\in(0,L)\). Write \(\tau_r\) for the target-hitting time under global Poisson resets to \(L\) at rate \(r>0\). Put
\[
z=L\sqrt{r/D},\qquad B=b/L,\qquad \eta=D/(2\kappa L),\qquad \alpha=1-2B.
\]
Then, exactly for every \(z>0\), \(0<B<1\), and \(\eta>0\),
\[
F(z,B,\eta):=\frac{D}{L^2}\mathbb E\tau_r
=\frac{e^z-1}{z^2}+\eta\frac{e^z+e^{\alpha z}}{z}.
\]
For fixed \(B,\eta\), this function has a unique global minimizer \(z_*(B,\eta)>0\). The physical optimum is \(r_*=Dz_*^2/L^2\). Its interface-position derivative is
\[
\frac{\partial z_*}{\partial B}
=\frac{2\eta(1-2B)e^{(1-2B)z_*}}{\partial_{zz}F(z_*,B,\eta)}.
\]
Thus \(z_*\) and \(r_*\) increase strictly for \(0<B<1/2\), decrease strictly for \(1/2<B<1\), and have their unique maximum at \(B=1/2\). Neither the location of that maximum nor the sign pattern depends on \(D\), \(L\), or \(\kappa\). In contrast,
\[
\frac{\partial F}{\partial B}(z,B,\eta)=-2\eta e^{(1-2B)z}<0
\]
for every fixed \(z>0\). The optimized mean \(F(z_*(B,\eta),B,\eta)\) also decreases strictly in \(B\).

## Assumptions and scope

The particle starts at \(L\) on the half-line \([0,\infty)\), undergoes Brownian diffusion with infinitesimal generator \(D\partial_{xx}\), and is absorbed on first reaching zero. At \(b\in(0,L)\), it crosses a two-sided membrane of permeability \(\kappa\) according to the standard flux-continuity/leather interface law. At every event of an independent homogeneous rate-\(r\) Poisson clock, **regardless of the current side of the interface**, its position is instantaneously reset to \(L\). The membrane need not be traversed during the externally imposed reset displacement. Resetting stops at absorption. The underlying non-reset process is the standard snapping-out/permeable-interface Brownian motion. All parameters are strictly positive and finite; the interface is strictly between target and reset point. No claims are made for a reset clock suppressed on one side, a perfectly impermeable interface, moving interfaces, or spatially dependent diffusivities.

## Proof

**1. Transform of the no-reset hitting time.** Let \(H\) be the absorption time without resetting. For \(s>0\), put \(k=\sqrt{s/D}\) and \(u(x)=\mathbb E_x e^{-sH}\). On both sides of the membrane, \(u''=k^2u\). The absorbing condition is \(u(0)=1\), and \(u\) is bounded as \(x\to\infty\). The backward membrane conditions are
\[
Du'(b^-)=Du'(b^+)=\kappa[u(b^+)-u(b^-)].
\]
Write \(u(x)=\cosh(kx)+a\sinh(kx)\) for \(x<b\), and \(u(x)=c e^{-k(x-b)}\) for \(x>b\). Flux continuity gives \(a=-(c+\sinh(kb))/\cosh(kb)\); the membrane condition then yields
\[
c=\frac1{\sinh(kb)+(1+Dk/\kappa)\cosh(kb)}.
\]
Consequently,
\[
\phi(s)=\mathbb E_L e^{-sH}=u(L)
=\frac{e^{-Lk}}{1+(Dk/(2\kappa))(1+e^{-2bk})}.
\]
This reproduces the no-reset first-passage transform of Kay and Giuggioli, Eq. (11), in the specified geometry. The transform is also derived here directly from the two-region backward problem; no inference about reset dynamics is imported from that paper.

**2. Global Poisson renewal.** Every reset starts a fresh independent copy of the full no-reset first-passage experiment at \(L\). Let \(E_r\sim\operatorname{Exp}(r)\) be independent of \(H\). A trial succeeds with probability \(\Pr(H<E_r)=\phi(r)>0\), has mean length \(\mathbb E\min(H,E_r)=(1-\phi(r))/r\), and otherwise restarts. Thus
\[
\mathbb E\tau_r=\frac{1-\phi(r)}{r\phi(r)}.
\]
Substitute the transform and the dimensionless quantities. Since \(z^2=rL^2/D\), straightforward algebra gives
\[
F(z,B,\eta)=\frac{e^z-1}{z^2}+\eta\frac{e^z+e^{(1-2B)z}}z.
\]
This renewal argument **would be invalid for interface-screened resets**: there, an excursion inside the membrane is not terminated by the resetting clock, so attempts are not globally restarted at every Poisson event.

**3. Strict convexity and existence.** Decompose \(F=F_0+\eta F_1\) with
\[
F_0(z)=\frac{e^z-1}{z^2}=\frac1z+\int_0^1(1-t)e^{tz}\,dt,
\qquad F_1(z,B)=\frac{e^z+e^{\alpha z}}z.
\]
Direct differentiation gives
\[
F_0''(z)=\frac2{z^3}+\int_0^1(1-t)t^2e^{tz}\,dt>0
\]
and
\[
\partial_{zz}F_1(z,B)=\frac{e^z[(z-1)^2+1]
+e^{\alpha z}[(\alpha z-1)^2+1]}{z^3}>0.
\]
All terms are strictly positive for every \(z>0\), \(-1<\alpha<1\), and \(\eta>0\), so \(F\) is strictly convex in \(z\). As \(z\downarrow0\), \(F\sim(1+2\eta)/z\to\infty\). As \(z\to\infty\), \(F\sim\eta e^z/z\to\infty\). Hence a unique interior global minimizer \(z_*\) exists, characterized by \(F_z(z_*,B,\eta)=0\), and \(F_{zz}(z_*,B,\eta)>0\).

**4. Universal midpoint law.** Differentiating \(F\) with respect to \(B\) gives
\[
F_B(z,B,\eta)=-2\eta e^{\alpha z},\qquad
F_{zB}(z,B,\eta)=-2\eta\alpha e^{\alpha z}.
\]
The implicit-function theorem applies globally to the unique minimizing root, giving
\[
\partial_B z_*=-\frac{F_{zB}(z_*,B,\eta)}{F_{zz}(z_*,B,\eta)}
=\frac{2\eta\alpha e^{\alpha z_*}}{F_{zz}(z_*,B,\eta)}.
\]
Its sign is exactly that of \(\alpha=1-2B\). The positive transformation \(r_*=Dz_*^2/L^2\) preserves the sign. Therefore the unique maximizing interface position is \(b=L/2\), for every finite positive permeability. At each fixed restart rate, \(F_B<0\) strictly. Along the optimal branch the envelope identity \(\frac{d}{dB}F(z_*(B),B,\eta)=F_B(z_*,B,\eta)<0\) proves that the optimized mean also decreases strictly. This completes the theorem.

## Verification

The accompanying `check.py` independently solves the two-interval backward problem for the no-reset Laplace transform and compares it with the closed expression, verifies the standard renewal transformation, tests first and second derivatives by centered differences, and checks convexity and the interface-position monotonicity of the unique minimizer across deterministic parameter sweeps. The script uses only the Python standard library. It is illustrative numerical corroboration; the uncountable-parameter theorem is proved above by exact identities, strict positivity, and the implicit-function theorem.

At \(D=L=1\) and \(\eta=1\), the computed optimal rates are approximately \(1.4356033207\), \(1.8331776095\), and \(1.7138642600\) for \(B=0.1\), \(0.5\), and \(0.9\), respectively, while the optimized dimensionless mean times decrease from approximately \(6.5543619785\) to \(5.1659255412\) to \(4.6737341462\).

## Relationship to prior work

Kay and Giuggioli (2022) derive the no-reset interface first-passage transform and investigate barrier-position dependence, including their Eq. (11) used as an independent consistency check. The transform is not claimed as new. The geometric optimization here combines it with global Poisson restarting to prove a sign-changing derivative of the minimizing restart rate and a parameter-independent midpoint maximizer.

Bressloff (2022/2023), *Diffusion with stochastic resetting screened by a semipermeable interface*, studies a different spatially restricted protocol: events in the target-side compartment do **not** reset the searcher. Its one-dimensional discussion describes an optimal rate shifting to the right as the barrier is moved toward the reset position, rather than the midpoint maximum proved here for global resets. Bressloff (2022/2023), *A probabilistic model of diffusion through a semi-permeable barrier*, also studies membrane-side-preserving resets, chiefly stationary densities and relaxation; its own discussion explicitly forbids resetting across the membrane. Neither paper's equations imply the present global-restart law by simply identifying parameters; the renewal mechanism differs. Existence of optimal Poisson resetting and the standard renewal formula are classical and not independently claimed.

## Limitations

The theorem assumes a single fixed, symmetric, permeability-controlled interface, unbiased homogeneous diffusion, global instantaneous Poisson reset to a single point, and complete absorption at the origin. It gives no first-passage variance, no finite-time distribution with resets, and no claim for spatially screened resets. The strict position effect disappears in the limit of infinite permeability \(\kappa\to\infty\); the strict theorem assumes finite \(\kappa\). No exhaustive survey of all equivalent general Markov restart theorems is asserted; independent priority assessment remains outstanding.

## References

1. T. Kay and L. Giuggioli, “Diffusion through permeable interfaces: Fundamental equations and their application to first-passage and local time statistics,” *Physical Review Research* **4**, L032039 (first published 7 September 2022). DOI: `10.1103/PhysRevResearch.4.L032039`. Primary OA text: https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.4.L032039 (Eq. 11).
2. P. C. Bressloff, “Diffusion with stochastic resetting screened by a semipermeable interface,” *Journal of Physics A: Mathematical and Theoretical* **56**, 105001 (2023); publicly posted 22 November 2022. arXiv: `2211.12468`; DOI: `10.1088/1751-8121/acba63`; https://arxiv.org/abs/2211.12468 (Secs. 2–5).
3. P. C. Bressloff, “A probabilistic model of diffusion through a semi-permeable barrier,” *Proceedings of the Royal Society A* (2023); publicly posted 19 September 2022. arXiv: `2209.09176`; https://arxiv.org/html/2209.09176v1 (Secs. 2–5, especially Sec. 3).
4. M. R. Evans and S. N. Majumdar, “Diffusion with stochastic resetting,” *Physical Review Letters* **106**, 160601 (2011). DOI: `10.1103/PhysRevLett.106.160601` (general restart background).
