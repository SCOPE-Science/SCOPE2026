# A generation-time-weighted slow selection law at a virulence fitness tie

## Finding
At a tie between the transmission potentials of two phenotypes in a heterogeneous-immunity epidemic, an arbitrarily small transmission advantage produces a non-logistic, generation-time-weighted replacement law on the long time scale \(t\asymp\varepsilon^{-1}\). The time-shifted strain frequency tends uniformly on every bounded slow-time interval to the solution
\[
\frac{du}{d\tau}=\frac{(\delta_1-\delta_2)u(1-u)}{T_1(1-u)+T_2u},\quad u(0)=u_0\in(0,1),\quad\tau=\varepsilon t,
\]
where the two positive constants \(T_i=\sum_{j=1}^2 a_jk_{ji}/d_{ji}^2\) are generation-time moments. Its unique solution obeys the exact implicit law
\[
T_1\log\frac{u(\tau)}{u_0}-T_2\log\frac{1-u(\tau)}{1-u_0}=(\delta_1-\delta_2)\tau.
\]
The result holds even when the tied phenotypes have different stage-specific transmission coefficients and removal rates. For \(T_1\ne T_2\) the selection speed changes with frequency; equal fitness alone does not imply identical epidemiological clocks. We prove this limit for each fixed finite \(\tau\)-window, not uniformly through eventual fixation as \(\tau\to\infty\).

## Assumptions and scope
Fix \(0<p<1\), \(a_1=1-p\), \(a_2=p\), demographic rates \(b,m,r>0\), and two sets of positive transmission coefficients \(k_{ji}>0\) and stage-removal rates \(d_{1i}=m+r\), \(d_{2i}=m+m_{d,i}>0\) with \(m_{d,i}>0\), for \(i,j\in\{1,2\}\). Assume both strains have the same transmission potential
\[
K=\sum_{j=1}^{2}\frac{a_j k_{ji}}{d_{ji}}>\frac{m}{b}.
\]
Define \(H=bK-m>0\) and \(T_i=\sum_j a_j k_{ji}/d_{ji}^2>0\). Let \(\delta_1,\delta_2\in\mathbb R\) be fixed. For sufficiently small \(\varepsilon>0\), perturb **only** transmission by \(k_{ji}^{\varepsilon}=k_{ji}(1+\varepsilon\delta_i/K)>0\). The physical equations, with \(F_i^\varepsilon=\sum_jk_{ji}^\varepsilon I_{ji}\), are
\[
\dot S=b-mS-S(F_1^\varepsilon+F_2^\varepsilon),\qquad
\dot I_{ji}=a_j S F_i^\varepsilon-d_{ji}I_{ji}.
\]
Choose \(u_0\in(0,1)\) and initialize at the **unperturbed** endemic equilibrium
\[
S(0)=1/K,\quad I_{j1}(0)=\frac{a_jHu_0}{K d_{j1}},\quad I_{j2}(0)=\frac{a_jH(1-u_0)}{K d_{j2}}.
\]
For every fixed \(L>0\), as \(\varepsilon\downarrow0\), the physical fraction
\[
q_\varepsilon(\tau)=\frac{F_1^\varepsilon(\tau/\varepsilon)}{F_1^\varepsilon(\tau/\varepsilon)+F_2^\varepsilon(\tau/\varepsilon)}
\]
converges uniformly for \(0\le\tau\le L\) to the solution \(u(\tau)\) stated above. All quantities are deterministic; there are no mutations, coinfections or fluctuating populations in the claim.

## Proof
**1. Neutral equilibrium manifold.** At \(\varepsilon=0\), for every \(h_1,h_2>0\) with \(h_1+h_2=H\), the state
\[
E(h):\quad S_*=1/K,\qquad I_{ji,*}=\frac{a_jh_i}{K d_{ji}},\qquad F_{i,*}=h_i
\]
is an equilibrium. This follows by direct substitution and \(\sum_j a_j k_{ji}/d_{ji}=K\). In particular \(S_* H=b-mS_*\).

**2. Normal attraction at every interior point.** Fix \(E(h)\). Put \(w_{ji}=k_{ji}/(K d_{ji})\), \(\pi_{ji}=a_j k_{ji}/(K d_{ji})\), so \(\pi_{1i}+\pi_{2i}=1\). With \(\Phi(z,z_*)=z-z_*-z_*\log(z/z_*)\), consider the strictly positive definite relative entropy
\[
\mathcal L_h=\Phi(S,S_*)+\sum_{i,j}w_{ji}\Phi(I_{ji},I_{ji,*}).
\]
Writing \(r_{ji}=I_{ji}/I_{ji,*}\), differentiation gives exactly
\[
\dot{\mathcal L}_h=\frac{S-S_*}{S}(b-mS)+\sum_i\left(S_*h_i-SF_i\sum_j\frac{\pi_{ji}}{r_{ji}}\right).
\]
Because \(F_i=h_i\sum_j\pi_{ji}r_{ji}\), weighted Cauchy--Schwarz yields \(F_i\sum_j\pi_{ji}/r_{ji}\ge h_i\), with equality precisely when \(r_{1i}=r_{2i}\). Thus
\[
\dot{\mathcal L}_h\le-\frac{(m+H)(S-S_*)^2}{S}.
\]
The quadratic part of \(\mathcal L_h\) at \(E(h)\) defines a positive definite inner product for the linearization, whose dissipation vanishes only when \(\delta S=0\) and \(\delta I_{1i}/I_{1i,*}=\delta I_{2i}/I_{2i,*}=c_i\) for each strain. On such a vector, the linearized infected equations vanish and the remaining equation is \(\delta\dot S=-S_*\sum_i h_i c_i\). A linear orbit remaining in the zero-dissipation subspace therefore has \(\sum_i h_i c_i=0\), precisely the one-dimensional tangent to \(E(h)\); it is stationary. Consequently all other eigenvalues of the Jacobian have strictly negative real parts: a nondecaying imaginary eigenmode would remain in that dissipation kernel, and a Jordan block at zero is excluded by the positive definite nonincreasing quadratic energy. The family is a normally attracting one-dimensional manifold on any closed subsegment with \(0<h_1<H\), with a uniform transverse spectral gap there.

**3. Perturbation and exact tangential drift.** On any such compact subsegment, the standard finite-dimensional normally hyperbolic invariant-manifold theorem gives a nearby invariant slow curve, transverse exponential tracking, and a \(C^1\) reduced vector field \(\dot h_i=\varepsilon G_i(h)+O(\varepsilon^2)\), for \(h_1+h_2=H\). The initial state \(E(Hu_0,H(1-u_0))\) is an \(O(\varepsilon)\) distance from this slow curve; all fast adjustments remain \(O(\varepsilon)\). To calculate \(G_i\) without solving a linear system, define the exact reproductive-value observable
\[
U_i=\sum_j\frac{k_{ji}}{d_{ji}} I_{ji}.
\]
For the perturbed equations, differentiation and the definition of \(K\) give the exact identity
\[
\dot U_i=\left(KS-1+\varepsilon\delta_i S\right)\,F_i^0,\qquad F_i^0=\sum_j k_{ji} I_{ji}.
\]
Along the slow curve, \(S=1/K+\varepsilon\sigma(h)+O(\varepsilon^2)\), \(F_i^0=h_i+O(\varepsilon)\) and \(U_i=T_i h_i/K+O(\varepsilon)\). Comparing terms of order \(\varepsilon\) gives
\[
\frac{T_i}{K}G_i=h_i\left(K\sigma+\frac{\delta_i}{K}\right),\qquad G_1+G_2=0.
\]
Solving these two equations yields
\[
G_1=\frac{h_1h_2(\delta_1-\delta_2)}{h_1T_2+h_2T_1},\qquad G_2=-G_1.
\]
Set \(u=h_1/H\) and \(\tau=\varepsilon t\). Then the reduced equation is exactly the claimed formula up to an error \(O(\varepsilon)\), uniform as long as \(u\) stays in a fixed compact subinterval of \((0,1)\). The limiting solution remains interior for every bounded \(\tau\)-interval. Standard Gronwall dependence plus fast tracking proves the claimed uniform convergence of \(q_\varepsilon\). Separation of variables integrates to the stated weighted-logarithm law; its left-hand side is strictly increasing from negative to positive infinity as \(u\) increases from zero to one, hence determines a unique trajectory.

**4. An exact unequal-generation-time example.** Let \(p=1/2\), \(b=3\), \(m=r=1\). Set \((d_{11},d_{21})=(2,2)\), \((k_{11},k_{21})=(2,2)\), and \((d_{12},d_{22})=(2,3)\), \((k_{12},k_{22})=(1,9/2)\). Both potentials equal \(K=1\), and \(H=2\), yet \(T_1=1/2\) and \(T_2=3/8\). With \(u_0=1/2\), \(\delta_1=0\), \(\delta_2=1\), the limiting law reads
\[
\frac12\log(2u)-\frac38\log(2(1-u))=-\tau.
\]
At \(\tau=1\), its unique root is approximately \(u=0.1047406326\). Its instantaneous selection speed differs between rare and common frequencies because the denominator is \((1-u)/2+3u/8\). Each strain has distinct stages even at exact equal fitness.

## Verification
The standalone `verify.py` recomputes all source-model identities for the explicit rational example using `fractions.Fraction`; checks the neutral Jacobian's one zero eigenvalue and negative nonzero eigenvalue real parts at three interior equilibria; solves the complete five-dimensional equations for four positive perturbations; and verifies convergence of the scaled frequencies toward the exact weighted-logarithm limit as the perturbation decreases. The spectral samples and numerical integrations support but do not establish the infinite-family theorem; the entropy and normal-hyperbolicity arguments above establish it analytically.

## Relationship to prior work
Barril and Vegué (2026), DOI `10.1007/s11538-026-01673-9`, introduced the heterogeneous-immunity multi-strain equations and established exclusion for a **strict** maximum of transmission potential. Their Appendix Proposition 3 does not analyze the \(\varepsilon^{-1}\)-time dynamics near a fitness tie. Girel and Richard (2026), arXiv `2603.29464`, proved broad global coexistence and exclusion results, including tied fitness, for infection-age models; that prior theorem supplies context but does not give this perturbative drift coefficient or weighted-logarithm selection curve. Gjini and Madec (2016/2017) and Madec and Gjini (2020) developed slow-fast replicator reductions for co-colonizing SIS systems; their unperturbed strains share clearance and the perturbation concerns co-colonization interactions, rather than persistently unequal stage-removal profiles at equal transmission potential. Accordingly the general idea of slow selection and coexistence is not claimed as new; only the explicit law proved here in the specified model is claimed.

## Limitations
The law is an asymptotic singular-perturbation limit on each fixed bounded slow-time window, not an error bound uniform all the way to fixation; it does not predict the final balance at an exact tie for arbitrary nonequilibrium starting states. The selection perturbation scales each strain's two transmission coefficients together; varying mortality or recovery simultaneously can produce a different drift. Fitness ties, deterministic population sizes, and perfect mutual exclusion of infections are structural assumptions. Numerical tests do not replace the normal-hyperbolicity proof. A structurally equivalent model could contain the formula without being identified in the inspected literature; independent audit has not been performed.

## References
1. C. Barril and M. Vegué, *Virulence Evolution in Host Populations with Heterogeneous Immune Responses: The Weakening of the Uncommon Weak*, Bulletin of Mathematical Biology 88 (2026), article 109. DOI: 10.1007/s11538-026-01673-9. First published 2026-06-09.
2. S. Girel and Q. Richard, *On the Global Asymptotic Stability of an Infection-Age-Structured Competitive Model*, arXiv:2603.29464 (2026-03-31); Mathematical Methods in the Applied Sciences (2026), DOI: 10.1002/mma.70967.
3. S. Madec and E. Gjini, *Predicting N-Strain Coexistence from Co-colonization Interactions: Epidemiology Meets Ecology and the Replicator Equation*, Bulletin of Mathematical Biology 82 (2020), article 142, DOI: 10.1007/s11538-020-00816-w.
4. E. Gjini and S. Madec, *A slow-fast dynamic decomposition links neutral and non-neutral coexistence in interacting multi-strain pathogens*, Theoretical Ecology 10 (2017), 129–141, DOI: 10.1007/s12080-016-0320-1.
