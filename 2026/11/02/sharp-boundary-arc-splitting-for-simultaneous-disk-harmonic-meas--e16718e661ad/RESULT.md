# Sharp boundary-arc splitting for simultaneous disk harmonic measures

## Finding
For two equally distant points in the unit disk, the optimal measurable boundary observation set for the smaller of their two harmonic measures has a **complete, sharp one-arc/two-arc phase diagram**. The transition has an explicit algebraic separation threshold and a second explicit critical occupied fraction. In the split phase it strictly outperforms every connected observation arc; the best connected arc is known exactly.

Let \(0<r<1\), \(0\le a\le\pi/2\), and \(0<\rho<1\). Put \(z_\pm=re^{\pm ia}\), \(P_r(t)=(1-r^2)/(1+r^2-2r\cos t)\), and for measurable \(E\subset\mathbb T\) write
\[
\omega_\pm(E)=\frac1{2\pi}\int_{\{t:e^{it}\in E\}}P_r(t\mp a)\,dt,
\qquad |E|=2\pi\rho.
\]
The simultaneous observation value is
\[
V(r,a,\rho)=\sup_{|E|=2\pi\rho}\min\{\omega_+(E),\omega_-(E)\}.
\]
Write \(k=(r+r^{-1})/2>1\), \(c=\cos a\), and
\[
c_*(r)=\frac{\sqrt{k^2+8}-k}{2},\qquad a_*(r)=\arccos c_*(r).
\]
If \(a\le a_*(r)\), the unique optimal set, modulo boundary null sets, is the **single central arc** \(E_\rho=\{e^{it}:|t|\le\pi\rho\}\). If \(a>a_*(r)\), define
\[
\rho_c(r,a)=\frac1\pi\arccos(k\cos a+\cos^2a-1).
\]
Here \(0<\rho_c\le1\), with equality \(\rho_c=1\) precisely for \(a=\pi/2\). When \(0<\rho<\rho_c\), the unique optimal region (up to null sets) is a union of **two disjoint reflected arcs**
\[
E=\{e^{it}:t\in[\theta_-,\theta_+]\cup[-\theta_+,-\theta_-]\},
\quad 0<\theta_-<\theta_+<\pi,\quad\theta_+-\theta_-=\pi\rho,
\]
where \(\theta_\pm\) are uniquely specified by the equal-density condition \(H(\theta_-)=H(\theta_+)\), with \(H(t)=\tfrac12(P_r(t-a)+P_r(t+a))\), and by the requirement that the arcs contain the two maxima of \(H\). At \(\rho\ge\rho_c\), the optimizer is instead \(E_\rho\). The touching configuration at \(\rho=\rho_c\) is connected for its canonical closed representative; all uniqueness assertions concern sets modulo null sets.

Among **all connected arcs** of length \(2\pi\rho\), the sharp maximin value is always attained by \(E_\rho\), and, for \(0\le a<\pi/2\), by no other arc. At \(a=\pi/2\), the arc centered at the antipode gives the same connected value. The unrestricted value is strictly greater than the best connected value **if and only if** \(a>a_*(r)\) and \(\rho<\rho_c(r,a)\).

The small occupied-fraction efficiency gain in the split phase is explicit:
\[
\lim_{\rho\downarrow0}\frac{V(r,a,\rho)}{V_{\mathrm{arc}}(r,a,\rho)}=\frac{H(\theta_m)}{H(0)}>1,
\]
where \(\theta_m\in(0,\pi)\) is the unique positive maximizing angle. At separation onset, \(\rho_c\) follows a square-root law,
\[
\rho_c(r,a)\sim
\frac{\sqrt{2[k+2c_*(r)]\sin a_*(r)}}{\pi}
\sqrt{a-a_*(r)}\qquad(a\downarrow a_*(r),\ a>a_*(r)).
\]

## Assumptions and scope
The unit circle has arc-length measure \(dt\), not normalized measure; the prescribed normalized length is \(\rho=|E|/(2\pi)\). Each \(\omega_\pm\) is a probability measure because \(\int_{-\pi}^{\pi}P_r(t)\,dt=2\pi\). Sets may be arbitrary measurable subsets; no a priori component bound is imposed. Separation is at most half a revolution, \(2a\in[0,\pi]\), by relabeling the two source points and rotating the configuration. The angular coordinates are taken modulo \(2\pi\). At the degenerate case \(a=0\) the two harmonic measures coincide and the central-arc conclusion still holds.

For exact computation define the increasing continuous lift \(F_r:\mathbb R\to\mathbb R\) by \(F_r(0)=0\), \(F_r'=P_r\), and \(F_r(t+2\pi)=F_r(t)+2\pi\). On \((-\pi,\pi)\),
\[
F_r(t)=2\arctan\left(\frac{1+r}{1-r}\tan\frac t2\right).
\]
The best connected value is
\[
V_{\mathrm{arc}}(r,a,\rho)=\frac{F_r(\pi\rho-a)+F_r(\pi\rho+a)}{2\pi}.
\]
In the split phase the unrestricted value is
\[
V(r,a,\rho)=\frac{F_r(\theta_+-a)-F_r(\theta_--a)+F_r(\theta_++a)-F_r(\theta_-+a)}{2\pi}.
\]
These formulas remain valid at the endpoints by continuity when interpreted using the continuous lift.

## Proof
**1. A sharp symmetric reduction, with equality.** For every admissible set \(E\),
\[
\min\{\omega_+(E),\omega_-(E)\}\le \frac{\omega_+(E)+\omega_-(E)}2
=\frac1{2\pi}\int_E H(t)\,dt.
\]
The classical layer-cake/bathtub rearrangement principle says that the maximum of the right-hand side under fixed set length is obtained by a superlevel set of \(H\). Since \(H(-t)=H(t)\), each such set is reflection-invariant and hence has \(\omega_+(E)=\omega_-(E)\). Thus the upper bound is attained in the original maximin problem. The rational function below is nonconstant and real analytic on the circle; therefore each level set is finite and has arclength zero. This gives uniqueness modulo null sets of the superlevel-set maximizer, and hence of the maximin maximizer. Equality in the preceding bound by itself does not create additional optimizers, because any maximin optimizer must also maximize the strictly bathtublike average.

**2. Exact mode and topology classification.** Put \(u=\cos t\), \(c=\cos a\), \(s=\sin a\), and \(C=(1-r^2)/(2r)\). Directly combining the two Poisson fractions gives
\[
H(t)=H(u)=C\frac{k-cu}{Q(u)},\qquad Q(u)=u^2-2kcu+k^2-s^2>0\quad(-1\le u\le1).
\]
Differentiation yields
\[
\frac{dH}{du}=C\frac{q(u)}{Q(u)^2},
\qquad q(u)=cu^2-2ku+c(k^2+s^2).
\]
Because \(q'(u)=2cu-2k<0\) and \(q(-1)>0\), the density is either strictly increasing in \(u\) or has one maximum at an interior \(u_m\). At the center,
\[
q(1)=(k-c)(c^2+kc-2).
\]
Consequently the unimodal regime is exactly \(c\ge c_*(r)\), equivalently \(a\le a_*(r)\). In the other regime, \(u_m\in(-1,1)\) is the smaller root of \(q\), namely
\[
u_m=\frac{k-\sin a\sqrt{k^2-\cos^2a}}{\cos a}
\quad (0<\cos a<c_*),
\]
with \(u_m=0\) at \(a=\pi/2\). Therefore the even function \(H(t)\) has precisely two strict global maxima at \(t=\pm\theta_m\), \(\theta_m=\arccos u_m\).

The superlevel components first join at the central local minimum \(H(0)\). The exact algebraic factorization
\[
H(u)-H(1)=-\frac{C(k-c)(u-1)(u-u_0)}{Q(u)Q(1)},
\quad u_0=kc+c^2-1
\]
shows that the other contact point with that level is \(\theta_0=\arccos u_0\), so its occupied fraction is \(\theta_0/\pi=\rho_c\). When the selected threshold lies above \(H(0)\), it gives exactly two open separated arcs; below or at that threshold it gives a single central closed arc (the equality case joins at the central point). For \(a=\pi/2\), \(u_0=-1\), so the two regions stay separated for every \(\rho<1\). The equal-height endpoint equation and arc length together characterize the only possible two-arc superlevel set.

**3. Connected competitor and strict gap.** An arc of half-length \(\beta=\pi\rho\) centered at \(t\) has harmonic mass at a source of argument \(\phi\) equal to the function
\[
W_\beta(d)=\frac1{2\pi}\int_{d-\beta}^{d+\beta}P_r(v)\,dv,
\quad d=\operatorname{dist}_{\mathbb T}(t,\phi)\in[0,\pi].
\]
It is strictly decreasing in \(d\) because for \(0<d<\pi\)
\[
W_\beta'(d)=\frac{P_r(d+\beta)-P_r(d-\beta)}{2\pi}<0,
\]
as follows from \(\cos(d-\beta)>\cos(d+\beta)\). Maximizing the smaller of the two masses is therefore equivalent to minimizing the larger circular distance to the two source directions. A pair of directions separated by \(2a\le\pi\) has the unique short-geodesic midpoint \(t=0\), except for antipodal directions when the two midpoints \(0\) and \(\pi\) tie. This proves the connected-arc assertion. Since a maximin-optimal set is unique modulo null sets, a disconnected bathtub optimizer produces a strict gap against every connected arc, whereas in the connected phase equality holds.

**4. Limiting laws.** For small \(\rho\), the two short arcs shrink onto \(\pm\theta_m\), giving \(V=\rho H(\theta_m)+o(\rho)\); the best single arc shrinks onto \(0\), giving \(V_{\mathrm{arc}}=\rho H(0)+o(\rho)\). This proves the strict limiting gain. Finally the identity \(1-u_0=(k+2c_*)\sin a_*\,(a-a_*)+O_r((a-a_*)^2)\) and \(\arccos(1-x)\sim\sqrt{2x}\) give the displayed square-root onset law.

## Verification
The accompanying standalone Python checker `check_poisson_design.py` exercises the exact rational derivative, checks the level crossing and mode separation, integrates reflected-arc regions using the continuous Poisson primitive, compares analytic optima with a finite-grid superlevel rearrangement, and verifies balanced harmonic measures. It passed **953 deterministic assertions**. The proof above establishes global optimality and uniqueness analytically; grid experiments are corroborative only and are not an exhaustive proof. The symbolic factorization used in Step 2 was additionally checked independently with polynomial algebra.

## Relationship to prior work
Bo-Yong Long, *Boundary behavior of alpha-harmonic functions and their Riesz–Fejér inequalities* (first posted 2024-10-16), develops Poisson-type boundary integral theory and harmonic trace inequalities, but does not study two prescribed source points, fixed-length simultaneous harmonic-measure observation, or the geometry of its optimizers. McMillan, Hanson, Saunders and Gallun (2013) explicitly introduce **two-component wrapped Cauchy densities**, which are the same densities as circular Poisson kernels, and employ highest-density/excess-mass sets as descriptive tools. Thus neither the density model nor superlevel rearrangement is claimed as new; the new statement is the joint maximin solution with the explicit sharp separation threshold, occupied-fraction topology boundary, unique component geometry and connected-arc penalty. Siew, Kato and Shimizu (2008) analyze a generalized circular distribution family with unimodal and bimodal examples but a different density and objective. Betsakos (2003) studies two-point projection estimates for harmonic measure associated with compact interior obstacles; the accessible abstract does not establish this fixed-boundary-arclength maximin result. A full-text comparison with that last paper could not be completed. A separately established Gaussian two-source area-concentration result involves whole-space Gaussian densities, not boundary Poisson kernels; it does not imply the disk formulas or the connected-arc classification.

## Limitations
The theorem assumes equal radial distances and symmetric source directions; it does not cover unequal radii, more than two interior points, prescribed numbers of arcs exceeding two, or general simply connected domains. Uniqueness is always modulo zero arclength; at the joining value of \(\rho\), topological connectedness refers to the canonical closed superlevel representative. The result gives the exact analytic characterization of two-arc endpoints but does not claim an elementary closed expression for their individual angles. Historical priority remains subject to independent literature review, including one relevant source only accessible at abstract level. Independent mathematical validation has not been performed.

## References
1. Bo-Yong Long, *Boundary behavior of alpha-harmonic functions and their Riesz–Fejér inequalities*, arXiv:2410.12137v1 (2024-10-16), https://arxiv.org/abs/2410.12137.
2. G. P. McMillan, T. E. Hanson, G. Saunders, F. J. Gallun, *A Two-Component Circular Regression Model for Repeated Measures Auditory Localization Data*, Journal of the Royal Statistical Society, Series C 62 (2013), 515–534, https://doi.org/10.1111/rssc.12004.
3. H.-Y. Siew, S. Kato, K. Shimizu, *The Generalized t-Distribution on the Circle*, Japanese Journal of Applied Statistics 37 (2008), 1–16, https://www.jstage.jst.go.jp/article/jappstat/37/1/37_1_1/_pdf/-char/ja.
4. D. Betsakos, *Two-Point Projection Estimates for Harmonic Measure*, Bulletin of the London Mathematical Society 35 (2003), https://doi.org/10.1112/S0024609303002108.
