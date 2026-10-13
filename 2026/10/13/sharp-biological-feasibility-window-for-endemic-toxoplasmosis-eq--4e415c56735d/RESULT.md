# Sharp biological-feasibility window for endemic toxoplasmosis equilibria

## Finding
For the unforced normalized cat–oocyst–mouse equations (2) of Ouyadri, El Koufi and Belhdid, the usual reproduction-number condition alone need not imply a physically meaningful endemic equilibrium. The sharp classification depends on the competition between recovered-cat inflow and congenital cat recruitment. With \(a=\alpha-\mu(t_1+t_2)\), when \(a\geq0\) the cat-population simplex is forward invariant and a biologically admissible endemic equilibrium exists precisely when \(\mathcal R_0>1\). When \(a<0\), the simplex is not forward invariant, and admissible endemic equilibria exist **only in a bounded transmission window**, even though \(\mathcal R_0\) grows strictly with transmission. This is a statement about the printed reduced equations (2), considered as a stand-alone dynamical system, rather than a derivation from the earlier unreduced system (1).

More precisely, put
\[
 d=\alpha-\mu t_1,\quad H=\alpha+\mu(1-t_1-t_2)=\mu+a,\quad
 \beta_c=\frac{d\mu_0(\mu+\gamma)}{\mu k},\quad
 \mathcal R_0=\frac{\beta}{\beta_c}.
\]
If \(a<0\), put \(q=\mu(t_1+t_2)-\alpha=-a>0\) and
\[
 \beta_{\max}=\frac{d\mu_0(\gamma+q)}{kq}>\beta_c.
\]
Then for \(a<0\), the unique endemic equilibrium is physically admissible (including a possibly zero vaccinated/recovered-cat fraction) if and only if \(\beta_c<\beta\leq\beta_{\max}\); its vaccinated/recovered fraction is strictly positive if and only if \(\beta_c<\beta<\beta_{\max}\). For \(\beta>\beta_{\max}\) there is no physically admissible endemic equilibrium, despite \(\mathcal R_0>1\).

## Assumptions and scope
The state is \((S,I,O,M)\), with \(S\) the susceptible-cat fraction, \(I\) the infected-cat fraction, \(O\) the environmental oocyst load, and \(M\) the susceptible-mouse fraction. The recovered/vaccinated-cat fraction is **defined** by \(V=1-S-I\), not introduced as an independent equation. The unforced normalized equations are
\[
\begin{aligned}
\dot S&=\mu-(\mu+\gamma)S-\beta SO-\mu(1-t_2)I,\\
\dot I&=\beta SO-(\alpha-\mu t_1)I,\\
\dot O&=kI-\mu_0 O,\\
\dot M&=-\beta_m MO.
\end{aligned}
\]
All \(\mu,\gamma,\alpha,\beta,k,\mu_0,\beta_m\) are strictly positive; \(0\leq t_1,t_2\), \(t_1+t_2\leq1\); and \(d=\alpha-\mu t_1>0\). Consequently \(H=\alpha+\mu(1-t_1-t_2)>0\). A *physically admissible* state satisfies \(S,I,V\geq0\), \(O\geq0\), and \(0\leq M\leq1\). An *endemic equilibrium* requires \(S,I,O>0\) and permits \(M=0\): infection necessarily eliminates susceptible mice at any positive equilibrium of the fourth equation. We distinguish an endemic equilibrium with \(V=0\) from one with all three cat fractions positive. All conclusions are algebraic equilibrium existence/uniqueness or forward-invariance claims, not global-attraction or optimal-control theorems.

## Proof
**1. The physical cat simplex.** Direct addition of the first two equations gives
\[
\dot S+\dot I=\mu(1-S-I)-\gamma S-aI,
\qquad \dot V=-\mu V+\gamma S+aI.
\]
For \(a\geq0\), the vector field points inward or tangent on \(V=0\). It also points inward or tangent on \(S=0\), where \(\dot S=\mu[1-(1-t_2)I]\geq0\) for \(0\leq I\leq1\); on \(I=0\), where \(\dot I=\beta SO\geq0\); and on \(O=0\), where \(\dot O=kI\geq0\). Finally \(\dot M=-\beta_m MO\) keeps \(0\leq M\leq1\). Local uniqueness and the inward-vector-field criterion imply forward invariance of the full physical state region when \(a\geq0\); the bounded cat fractions imply \(O(t)\) is bounded by comparison with \(\dot O\leq k-\mu_0 O\), so solutions exist globally. Conversely, when \(a<0\), at \(S=0\), \(I=1\), \(V=0\) we have \(\dot V=a<0\), regardless of \(O\) and \(\beta\). Therefore the simplex is not positively invariant. By continuity, sufficiently nearby strictly interior states also leave the physical simplex.

**2. All endemic equilibria.** Fix \(\beta>0\), and suppose \(I,O>0\). The third stationary equation forces \(O=kI/\mu_0>0\). The fourth forces \(M=0\). Cancelling \(I>0\) in the second gives \(\beta k S/\mu_0=d\), hence necessarily
\[
 S_*=\frac{d\mu_0}{\beta k}.
\]
Substituting \(\beta S_*O_*=dI_*\) in the first equation yields \(\mu-(\mu+\gamma)S_*-HI_*=0\), so
\[
 I_*=\frac{\mu-(\mu+\gamma)S_*}{H},\quad
 O_*=\frac{kI_*}{\mu_0},\quad M_*=0,
 \quad V_*=1-S_*-I_*=\frac{a+(\gamma-a)S_*}{H}.
\]
These formulas also suffice: direct substitution satisfies all four equilibrium equations. Their uniqueness follows because each step above is forced. Since \(H>0\), the infection quantity is positive exactly when \(S_*<\mu/(\mu+\gamma)\), or equivalently \(\beta>\beta_c\). This is precisely \(\mathcal R_0>1\). If \(a\geq0\), then \(V_*>0\) automatically for \(\beta>\beta_c\): the numerator is \(a(1-S_*)+\gamma S_*>0\) because \(0<S_*<\mu/(\mu+\gamma)<1\). If \(a=-q<0\), the numerator becomes \(-q+(\gamma+q)S_*\), so \(V_*\geq0\) exactly when \(S_*\geq q/(\gamma+q)\), equivalently \(\beta\leq\beta_{\max}\). At equality \(V_*=0\); inequality gives \(V_*>0\). Because \(0<q<\mu\), the threshold ordering is strict:
\[
\frac{\beta_{\max}}{\beta_c}
=\frac{\mu(\gamma+q)}{q(\mu+\gamma)}
=1+\frac{\gamma(\mu-q)}{q(\mu+\gamma)}>1.
\]
For \(\beta>\beta_{\max}\), the only algebraic endemic solution has \(V_*<0\), so the original physical simplex contains no endemic equilibrium. This proves the complete classification.

## Verification
A standalone exact-rational check is provided in `verify.py` (Python standard library only). It evaluates the four stationary residuals directly and compares \(V_*\), \(\mathcal R_0\), and the threshold ordering for three rational cases. In particular choose \(\mu=\gamma=k=\mu_0=\beta_m=1\), \(\alpha=1/2\), \(t_1=1/4\), \(t_2=1/2\). Then \(a=-1/4\), \(\beta_c=1/2\), and \(\beta_{\max}=5/4\). At \(\beta=1\), the equilibrium \((S,I,O,M,V)=(1/4,2/3,2/3,0,1/12)\) is physical. At \(\beta=5/4\) it is \((1/5,4/5,4/5,0,0)\), on the physical boundary. At \(\beta=2\), the unique algebraic endemic equilibrium is \((1/8,1,1,0,-1/8)\), although \(\mathcal R_0=4\). These exact examples illustrate the sharp boundary; the inequalities for all parameters are proved above, not inferred from a finite computation.

## Relationship to prior work
Ouyadri, El Koufi and Belhdid (2026) introduce the reduced equations as their equation (2), state that a biological region with \(S+I\leq1\) is invariant (Theorem 2), and present \(\mathcal R_0>1\) together with \(\alpha>\mu t_1\) as sufficient for a biologically feasible endemic equilibrium (Section 3.4). The present result isolates an additional, necessary cat-simplex condition and completely classifies its transmission-dependent consequences. Their printed endemic infection formula also differs algebraically from the forced expression above; no statement about numerical figures is needed. The paper's own numerical parameter choices lie in the \(a\geq0\) regime and are not counterexamples to this theorem. Earlier cat-vaccination/oocyst models (Arenas, González-Parra and Villanueva Micó, 2010) analyze a different model, while Khan et al. (2024) study a harmonic-incidence human–cat system; neither provides this particular two-threshold feasibility classification.

## Limitations
This theorem applies **only** to the written four-variable reduced system (2), as its own mathematical system. The earlier unnormalized system (1) has different total-cat bookkeeping; a physical interpretation of the reduction as an exact rescaling of (1) is not asserted. We assume the specified nonnegative congenital transmission fractions sum to at most one and the positive effective infected removal rate. The result classifies equilibria and forward invariance but proves no basin of attraction or stability for general parameters, no efficacy of vaccination controls, and no empirical epidemiological calibration. Existing or unindexed variants/corrections could affect novelty. The first-public-date field uses the earliest discovered explicitly day-stamped public author upload (March 7, 2026); the publisher's 2026 issue and URL do not provide a separately verified earlier day.

## References
1. M. Ouyadri, A. El Koufi, S. Belhdid, “Mathematical Modeling and Optimal Control Strategies for Toxoplasmosis with Multiple Hosts,” *Mathematical Modeling and Computing* **13** (2026), 60–76. DOI: `10.23939/mmc2026.01.060`. Public publisher text: https://science.lpnu.ua/sites/default/files/journal-paper/2026/feb/41647/2026131060076.pdf .
2. A. J. Arenas, G. González-Parra, R.-J. Villanueva Micó, “Modeling toxoplasmosis spread in cat populations under vaccination,” *Theoretical Population Biology* **77** (2010), 227–237. DOI: `10.1016/j.tpb.2010.03.005` (abstract inspected; full text not obtained).
3. U. Khan et al., “Optimal control strategies for toxoplasmosis disease transmission dynamics via harmonic mean-type incident rate,” *Scientific Reports* **14** (2024), 12616. DOI: `10.1038/s41598-024-63263-w` (public HTML/model description inspected).
