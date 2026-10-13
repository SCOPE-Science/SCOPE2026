# Exact endpoint reachability and weak-seed response in a reversible-confinement epidemic model

## Finding

In the reversible-confinement epidemic model introduced by Ricardo-Azanza and Hernandez-Vargas and analyzed in Almocera, González and Hernandez-Vargas, the **entire stable equilibrium segment is the closure of end states attainable from genuinely infected populations**, not merely an a priori set containing those endpoints. Every strict interior point of that segment is attainable *exactly*.

The model, for \(q,\eta,r>0\), is
\[
\begin{aligned}
\dot x&=-\eta r xz-qx+y,\\
\dot y&=qx-y,\\
\dot z&=\eta(rx-1)z.
\end{aligned}
\]
Here \(x\) is the unconfined susceptible fraction, \(y\) the confined susceptible fraction and \(z\) the infectious asymptomatic fraction. Write
\[
\mathcal X=\{(x,y,z)\in\mathbb R^3_{\ge0}:x+y+z\le1\},
\qquad
\mathcal B=\{(x,y,z)\in\mathcal X:z>0,\ x+y>0\},
\]
\[
\widehat x=\min\left\{\frac1r,\frac1{1+q}\right\},
\qquad
\mathcal A=\{(\xi,q\xi,0):0\le\xi\le\widehat x\}.
\]
Every trajectory from \(\mathcal B\) converges to some \((\xi,q\xi,0)\in\mathcal A\) with \(\xi>0\). Conversely **every** \(\xi\in(0,\widehat x)\) is the exact limit of at least one trajectory with initial condition in \(\mathcal B\). Consequently \(\mathcal A\) is the unique smallest **closed** attracting set relative to the seeded state sector \(\mathcal B\).

There is also a sharp final-size sensitivity formula. For \(0<u<\widehat x\) and \(0<\delta\le1-(1+q)u\), start at the balanced susceptible ratio
\[
(x(0),y(0),z(0))=(u,qu,\delta)
\]
and define \(F_\delta(u)=\lim_{t\to\infty}x(t)\). Then
\[
0<u-F_\delta(u)\le \frac{ru\delta}{(1+q)(1-ru)},
\]
and
\[
\boxed{\lim_{\delta\downarrow0}\frac{u-F_\delta(u)}{\delta}=\frac{ru}{(1+q)(1-ru)}.}
\]
Thus the linearized depletion coefficient can become large as the susceptible endpoint approaches the invasion threshold, although the fixed-\(u\) expansion must not be treated as uniform at that threshold.

## Assumptions and scope

All parameters \(q,\eta,r\) are strictly positive; no upper or lower restrictions on \(r\) relative to \(1+q\) are imposed. The feasible region is \(\mathcal X\). The attraction domain \(\mathcal B\) is intentionally restricted to positive initial infection and positive total susceptible population. A **closed** set \(K\subset\mathcal X\) *attracts \(\mathcal B\)* if
\[
\lim_{t\to\infty}\operatorname{dist}(\Phi_t(p),K)=0
\quad\text{for all }p\in\mathcal B.
\]
The theorem identifies the inclusion-minimal such closed set, without asserting Lyapunov attraction of every disease-free initial state in \(\mathcal X\).

The original paper uses \(q^*\), \(\eta^*\), and \(\mathcal R_0\); here these are denoted by \(q\), \(\eta\), and \(r\), respectively. The time is the source's nondimensionalized time.

## Proof

**1. Global convergence and limiting location.** The coordinate faces of \(\mathcal X\) point inward: \(\dot x=y\ge0\) at \(x=0\); \(\dot y=qx\ge0\) at \(y=0\); and \(\dot z=0\) at \(z=0\). Moreover
\[
(x+y+z)'=-\eta z\le0,
\]
so the simplex is forward invariant and solutions exist globally. Put \(s=x+y\). Then
\[
\dot s=-\eta r xz\le0,
\quad
(s+z)'=-\eta z.
\]
In particular \(s(t)\to s_\infty\ge0\), and \(z\) is integrable:
\[
\int_0^\infty z(t)\,dt=\frac{s(0)+z(0)-s_\infty}{\eta}\le\frac1\eta.
\]
The derivative \(z'=\eta(rx-1)z\) is bounded on the compact simplex, so a nonnegative integrable \(z\) with bounded derivative must tend to zero. The \(x\)-equation becomes
\[
\dot x+(1+q)x=s-\eta r xz,
\]
whose forcing tends to \(s_\infty\). Variation of constants gives \(x(t)\to s_\infty/(1+q)\), and therefore \(y(t)\to qs_\infty/(1+q)\).

For initial \(p\in\mathcal B\), note \(s(0)>0\) and
\[
\dot s=-\eta r xz\ge-\eta r sz.
\]
Gronwall and the integral bound imply
\[
s_\infty\ge s(0)\exp\!\left(-\eta r\int_0^\infty z(t)dt\right)\ge s(0)e^{-r}>0.
\]
Writing \(\xi=s_\infty/(1+q)\) yields \(\xi>0\). Since \(s_\infty\le s(0)\le1-z(0)<1\), we have \(\xi<1/(1+q)\). If \(\xi>1/r\), then eventually \(x(t)>1/r+\epsilon\) for some \(\epsilon>0\), and
\[
\dot z\ge \eta r\epsilon z
\]
would force exponential growth of \(z\), contradicting its integrability. Thus \(\xi\le1/r\) and \(\xi\le\widehat x\).

**2. Balanced infectious seed bound and derivative.** Fix \(u\in(0,\widehat x)\) and feasible \(\delta>0\). From \(s(t)\le s(0)=(1+q)u\) and the scalar comparison
\[
\dot x\le(1+q)(u-x),\qquad x(0)=u,
\]
it follows that \(0<x(t)\le u\). Hence
\[
0<z(t)\le\delta\exp[-\eta(1-ru)t].
\]
Integrating \(\dot s=-\eta r xz\) gives the exact integral identity
\[
F_\delta(u)=u-\frac{\eta r}{1+q}\int_0^\infty x(t)z(t)dt.
\]
Its integral is strictly positive, and the exponential estimate gives
\[
0<u-F_\delta(u)\le \frac{ru\delta}{(1+q)(1-ru)}.
\]
For each fixed time, continuous dependence on \(\delta\) gives \(x_\delta(t)\to u\) as \(\delta\to0\), since \((u,qu,0)\) is an equilibrium. The exact formula
\[
\frac{z_\delta(t)}{\delta}=\exp\!\left(\eta\int_0^t(rx_\delta(v)-1)dv\right)
\]
therefore tends to \(e^{-\eta(1-ru)t}\). Dominated convergence is valid because
\[
0\le \frac{x_\delta(t)z_\delta(t)}{\delta}\le u e^{-\eta(1-ru)t}
\]
for all \(t\ge0\). Dividing the integral identity by \(\delta\) and taking the limit proves
\[
\lim_{\delta\downarrow0}\frac{u-F_\delta(u)}{\delta}=
\frac{\eta r}{1+q}\int_0^\infty ue^{-\eta(1-ru)t}dt
=\frac{ru}{(1+q)(1-ru)}.
\]

**3. Exact endpoint reachability.** Fix any desired \(\xi\) with \(0<\xi<\widehat x\). Choose \(0<\ell<\xi<v<\widehat x\). For all sufficiently small \(\delta>0\), the initial conditions \((u,qu,\delta)\) are feasible for every \(u\in[\ell,v]\). The same exponential bound, with \(v\) in place of \(u\), dominates \(x_u(t)z_u(t)\) uniformly on the interval, so
\[
u\longmapsto F_\delta(u)
\]
is continuous by finite-time ODE continuous dependence and dominated convergence. The strict loss yields \(F_\delta(\ell)<\ell<\xi\). Choosing \(\delta\) additionally so that
\[
v-\frac{rv\delta}{(1+q)(1-rv)}>\xi
\]
gives \(F_\delta(v)>\xi\). The intermediate value theorem supplies \(u\in(\ell,v)\) such that \(F_\delta(u)=\xi\), producing a genuinely infected initial state that converges to the exact prescribed equilibrium.

**4. Minimality.** Step 1 proves \(\mathcal A\) attracts every trajectory from \(\mathcal B\). Step 3 proves that each equilibrium with \(0<\xi<\widehat x\) is a trajectory limit of some initial state in \(\mathcal B\). Any **closed** set attracting all of \(\mathcal B\) must contain each such limit, hence its closure \(\mathcal A\). Therefore \(\mathcal A\) is the unique smallest closed set attracting the infected sector.

## Verification

The standalone program `verify.py` checks the coefficient and comparison formulas with exact rational arithmetic where applicable and integrates the source's reduced differential equations for a worked parameter choice \(q=5/3\), \(\eta=100/33\), \(r=27/10\). It measures final susceptible depletion for two small infectious seeds and verifies the predicted first-order coefficient, nonnegativity and simplex invariance. It also numerically brackets a desired interior endpoint and constructs an approximate inverse initial condition. These finite numerical tests corroborate, but do not replace, the global analytic proof.

## Relationship to prior work

Almocera, González and Hernandez-Vargas prove that a trajectory starting with positive infection eventually enters their stable equilibrium segment (Theorem 4.9), derive a final-size relation involving a future-time confinement-tonicity integral, and give conditional subset attraction statements in Theorem 4.12. Their numerical Fig. 12 discussion explicitly conjectures that *all* stable endpoints are represented and that the stable segment is smallest attracting. The present theorem supplies exact reachability for every interior equilibrium, proves minimality **relative to positive infection**, and gives a quantitative infinitesimal-seed response not stated in the paper. Attraction over the **entire** feasible simplex is different because the disease-free equilibrium line includes unseeded stationary points.

The earlier model paper by Ricardo-Azanza and Hernandez-Vargas fits parameters and simulates lifting confinement rather than proving endpoint reachability. Sereno and coauthors establish a smallest attractive stable set for a classic controlled SIR system, which is important stronger conceptual prior art. Their two-dimensional SIR equations do not have the distinct reversible susceptible exchange \(\dot y=qx-y\), so their theorem does not directly supply this model's positive-\(q\) endpoint construction or susceptibility-loss coefficient. The limit \(q=0\) is a related special case and is not claimed as new.

## Limitations

The attracting-set conclusion is explicitly restricted to initial infection \(z(0)>0\) and positive susceptible total \(x(0)+y(0)>0\). It is not a global attraction statement over the entire simplex, especially when unseeded equilibria beyond the invasion threshold exist. Every strictly interior stable endpoint is exactly attained, while the endpoints of the closed stable segment are shown to be in the *closure* of attainable limits, not necessarily attained by infected initial conditions. The response expansion is a fixed-\(u\), vanishing-seed limit and cannot be used uniformly as \(ru\to1\). The limiting infected burden is not an assertion about control optimization when \(q\) is time varying. Unindexed or incompletely accessible mathematical literature may contain similar results.

## References

1. A. E. S. Almocera, A. H. González and E. A. Hernandez-Vargas, “Confinement tonicity on epidemic spreading,” *Journal of Mathematical Biology* **88** (2024), article 46. DOI: 10.1007/s00285-024-02064-1. Open full text: https://link.springer.com/article/10.1007/s00285-024-02064-1.
2. C. L. Ricardo-Azanza and E. A. Hernandez-Vargas, “Epidemiological Characteristics of COVID-19 in Mexico and the Potential Impact of Lifting Confinement Across Regions,” *Frontiers in Physics* **8** (2020), article 573322. DOI: 10.3389/fphy.2020.573322. Open full text: https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2020.573322/full.
3. J. Sereno, A. L. Anderson, A. Ferramosca, E. A. Hernandez-Vargas and A. H. González, “Minimizing the epidemic final size while containing the infected peak prevalence in SIR systems,” *Automatica* **144** (2022), 110496. DOI: 10.1016/j.automatica.2022.110496. Author preprint: arXiv:2111.05652.
