# An optimized all-Hill-order extinction barrier for vaccinated fomite epidemics

## Finding
Consider the six-compartment epidemic model in [1], with a Hill environmental infection response of integer order \(n\ge 2\). Define the disease-free susceptible and vaccinated values \(S_0,V_0\) and the optimal global linear-response constant \(L_n\) below. Put
\[
\mathcal T_n=\frac{\xi}{(\xi+\mu)(\gamma+d+\mu)}\left[\beta_1S_0+\beta_2V_0+\frac{\varphi L_n}{\omega}(\alpha_1S_0+\alpha_2V_0)\right].
\]
**Theorem.** For every integer \(n\ge2\), every admissible positive parameter vector and every finite nonnegative initial state, \(\mathcal T_n\le1\) implies convergence of all six compartments to the unique disease-free equilibrium. Each trajectory converges exponentially after a sufficiently large time (the prefactor and entry time may depend on the initial condition). The constant
\[
L_n=\frac{(n-1)^{(n-1)/n}}{n\kappa}
\]
is the smallest possible constant satisfying \(g_n(C)\le L_nC\) for **every** \(C\ge0\), with equality at the strictly positive concentration \(C=\kappa(n-1)^{1/n}\). The stated threshold is a sufficient global-eradication condition, not a claimed necessary one. In particular, the equality case \(\mathcal T_n=1\) is included, although its comparison matrix has a neutral eigenvalue.

## Assumptions and scope
The state variables \(S,V,E,I,R,C\) are nonnegative and satisfy, for \(t\ge0\),
\[
\begin{aligned}
\dot S&=\Lambda-(\sigma+\mu)S+(1-p)\eta V-\beta_1SI-\alpha_1Sg_n(C),\\
\dot V&=\sigma S-(\eta+\mu)V-\beta_2VI-\alpha_2Vg_n(C),\\
\dot E&=(\beta_1S+\beta_2V)I+(\alpha_1S+\alpha_2V)g_n(C)-(\xi+\mu)E,\\
\dot I&=\xi E-(\gamma+d+\mu)I,\\
\dot C&=\varphi I-\omega C,\\
\dot R&=\gamma I+p\eta V-\mu R,\\
 g_n(C)&=\frac{C^n}{C^n+\kappa^n}.
\end{aligned}
\]
Assume \(\Lambda,\sigma,\mu,\eta,\beta_1,\beta_2,\alpha_1,\alpha_2,\xi,\gamma,d,\varphi,\omega,\kappa>0\), \(0<p<1\), and integer \(n\ge2\). The biological inequalities \(\beta_2\le\beta_1\), \(\alpha_2\le\alpha_1\) in [1] may be imposed; the proof needs only positivity. Let
\[
D=\mu(\sigma+\eta+\mu)+p\eta\sigma,\qquad
S_0=\frac{\Lambda(\eta+\mu)}D,\quad V_0=\frac{\Lambda\sigma}D,\quad R_0=\frac{p\eta V_0}{\mu}.
\]
The disease-free equilibrium is \((S_0,V_0,0,0,R_0,0)\) in the displayed coordinate order. The paper's local direct-transmission control reproduction number for \(n\ge2\) is
\[
\mathcal R_c=\frac{\xi(\beta_1S_0+\beta_2V_0)}{(\xi+\mu)(\gamma+d+\mu)}.
\]
The theorem concerns this deterministic homogeneous ODE, not stochastic or spatial models. No uniform global decay prefactor across unbounded initial data is asserted.

## Proof
**1. Positive global trajectories and an exponentially accurate susceptible/vaccinated ceiling.** The vector field is locally Lipschitz on the nonnegative cone and points inward at each coordinate face. With \(N=S+V+E+I+R\), the exact balance equation is \(\dot N=\Lambda-\mu N-dI\le\Lambda-\mu N\); thus \(N\) is bounded. The environmental equation then bounds \(C\), giving global existence. Put \(w=(S,V)^\mathsf T\), \(b_0=(\Lambda,0)^\mathsf T\), and
\[
A=\begin{pmatrix}-(\sigma+\mu)&(1-p)\eta\\\sigma&-(\eta+\mu)\end{pmatrix}.
\]
It is Metzler, with negative trace and positive determinant \(D\), hence Hurwitz. The nonlinear equations have \(\dot w=Aw+b_0-h\), where \(h=(S(\beta_1I+\alpha_1g_n(C)),V(\beta_2I+\alpha_2g_n(C)))^\mathsf T\ge0\). By cooperative comparison,
\[
w(t)\le w_0+e^{At}(w(0)-w_0),\qquad w_0=(S_0,V_0)^\mathsf T.
\]
Therefore there exist finite trajectory-dependent \(K,\rho>0\) such that \(S(t)\le S_0+Ke^{-\rho t}\) and \(V(t)\le V_0+Ke^{-\rho t}\) for all \(t\ge0\).

**2. Exact global Hill envelope.** For \(C>0\), the ratio \(g_n(C)/C=C^{n-1}/(C^n+\kappa^n)\). Its derivative has the sign of \((n-1)\kappa^n-C^n\), so its unique global maximum is attained at \(C_*=\kappa(n-1)^{1/n}\), with value \(L_n\) stated above. At \(C=0\), \(g_n(0)=0\). Thus \(g_n(C)\le L_nC\) for every nonnegative concentration, and the constant cannot be decreased.

**3. Strict comparison regime.** Write \(a=\xi+\mu\), \(b=\gamma+d+\mu\), \(q_0=\beta_1S_0+\beta_2V_0\), and \(r_0=\alpha_1S_0+\alpha_2V_0\). For \(u=(E,I,C)^\mathsf T\), the bounds in steps 1--2 give, for all sufficiently large \(t\),
\[
\dot u\le B_\epsilon u,\quad
B_\epsilon=\begin{pmatrix}-a&q_0+(\beta_1+\beta_2)\epsilon&L_n[r_0+(\alpha_1+\alpha_2)\epsilon]\\
\xi&-b&0\\0&\varphi&-\omega\end{pmatrix}.
\]
Here and below vector inequalities are coordinatewise. Let \(B_0\) denote this matrix at \(\epsilon=0\). When \(\mathcal T_n<1\), choose a sufficiently small \(\delta\in(0,1)\) and set \(v=(b(1-\delta)/\xi,1,\varphi(1+\delta)/\omega)^\mathsf T>0\). Direct substitution yields \((B_0v)_2=-b\delta<0\), \((B_0v)_3=-\varphi\delta<0\) and
\[
(B_0v)_1=-\frac{ab}{\xi}(1-\mathcal T_n)+\delta\left(\frac{ab}{\xi}+\frac{L_nr_0\varphi}{\omega}\right)<0.
\]
A Metzler matrix with a strictly positive vector mapped strictly below zero is Hurwitz (diagonal similarity followed by the maximum norm gives a negative logarithmic norm). By continuity, \(B_\epsilon\) is Hurwitz for small \(\epsilon>0\). The positive matrix semigroup comparison implies exponential decay of \(u\). Variation of constants in the stable \(w\)-subsystem then gives \(w(t)\to w_0\) exponentially, and the linear \(R\)-equation gives \(R(t)\to R_0\) exponentially.

**4. The neutral-envelope boundary.** Now suppose \(\mathcal T_n=1\); here \(q_0+(\varphi/\omega)L_nr_0=ab/\xi\). The comparison matrix \(B_0\) has the strictly positive left nullvector
\[
\ell=\left(1,\frac a\xi,\frac{L_nr_0}{\omega}\right)^\mathsf T,
\qquad \ell^\mathsf T B_0=0.
\]
Set \(Z=E+(a/\xi)I+(L_nr_0/\omega)C\), \(q(t)=\beta_1S(t)+\beta_2V(t)\), \(r(t)=\alpha_1S(t)+\alpha_2V(t)\). Differentiation using the **exact nonlinear system** (not its linearization) yields
\[
\dot Z=(q(t)-q_0)I+L_n(r(t)-r_0)C-r(t)[L_nC-g_n(C)].\tag{*}
\]
The first two coefficients are bounded above by \(Ke^{-\rho t}\), and \(L_nC-g_n(C)\ge0\). Consequently \(\dot Z\le K'e^{-\rho t}Z\). Gronwall bounds \(Z(t)\), and the nonnegative function \(Z(t)+\int_t^\infty K'e^{-\rho s}Z(s)\,ds\) is nonincreasing. Thus \(Z(t)\) has a finite limit \(Z_\infty\ge0\).

The full trajectory is bounded, so its omega-limit set is nonempty, compact and positively invariant. Step 1 ensures that every point in this set has \(S\le S_0\) and \(V\le V_0\). Also \(Z\equiv Z_\infty\) along every forward orbit contained in the set. On that set, equation (*) becomes the sum of three nonpositive terms:
\[
\dot Z=-[\beta_1(S_0-S)+\beta_2(V_0-V)]I
-L_n[\alpha_1(S_0-S)+\alpha_2(V_0-V)]C-r(t)[L_nC-g_n(C)].
\]
If \(I>0\) or \(C>0\), equality \(\dot Z=0\) forces \(S=S_0\) and \(V=V_0\). But at such a point \(\dot S=-S_0[\beta_1I+\alpha_1g_n(C)]<0\), contradicting equality throughout the forward orbit. If \(Z_\infty>0\) yet initially \(I=C=0\) at a point of the omega-limit set, then \(E>0\) and \(\dot I=\xi E>0\), producing \(I>0\) immediately and the same contradiction. Thus \(Z_\infty=0\) and \(E,I,C\to0\). The stable \(w\) and \(R\) equations give convergence to the disease-free equilibrium.

At the boundary \(\mathcal T_n=1\), positivity of the environmental coupling implies \(\mathcal R_c<1\). Because \(n\ge2\), \(g_n'(0)=0\), so the infected disease-free Jacobian is triangularly coupled to the strictly stable direct-transmission \((E,I)\) block and the stable environmental \(C\) equation. The \((S,V)\) and \(R\) Jacobian blocks are also Hurwitz. Therefore the disease-free equilibrium is a hyperbolic sink; convergence established above implies eventual exponential convergence for every solution. This completes the proof for \(\mathcal T_n\le1\).

**5. Explicit interior and equality witnesses.** Take \(n=2\), \(\Lambda=\mu=\xi=\gamma=d=\eta=\varphi=\omega=\kappa=1\), \(\sigma=10\), \(p=1/2\), \(\beta_1=5\), \(\beta_2=\alpha_2=1/10\). Then \(D=17\), \(S_0=2/17\), \(V_0=10/17\), \(L_2=1/2\), and \(\mathcal R_c=11/102<1\). With \(\alpha_1=10\), the global threshold is \(\mathcal T_2=43/204<1\). Yet the cruder total-population/Hill-envelope bound
\[
\mathcal U_2:=\frac{\Lambda\xi}{\mu ab}\left[\beta_1+\frac{\varphi L_2}{\omega}\alpha_1\right]=\frac53>1
\]
does not certify extinction. With the same parameters except \(\alpha_1=181/2\), the threshold is **exactly** \(\mathcal T_2=1\), while \(\mathcal R_c=11/102<1\). Thus the boundary proof treats a nonempty, genuinely neutral-envelope case.

## Verification
The standalone implementation `verify.py` included with this report checks the parameter substitutions using exact rational arithmetic, the two critical comparison-vector identities, the n=2 optimal-envelope inequality as an exact square, and finite numeric checks of the Hill ratio for orders 2 through 10. Invoke `python verify.py` from the containing directory; the expected last line is `VERIFY_OK`. The analytic proof in steps 1--4, not the finite sampling, establishes the theorem for **all** integer orders and all admissible parameters.

## Relationship to prior work
Penitente, Foryś and Gürbüz [1] prove a sufficient global extinction condition for the **Holling-II case \(n=1\)** (Theorem 1) and persistence when \(\mathcal R_c>1\). Their concluding remarks explicitly identify the incomplete global-extinction picture for **\(n\ge2\)**. Earlier Gökçe, Gürbüz and Rendall [2] establish backward bifurcation and multiplicity of endemic equilibria for some \(n=2\) parameters, demonstrating why the local \(\mathcal R_c<1\) threshold alone cannot guarantee global elimination. The present theorem makes no contradictory claim: it establishes an explicit, nonempty sufficient extinction region for each \(n\ge2\), calculated using the disease-free vaccinated composition rather than a worst-case total-population ceiling, including the limiting neutral comparison boundary.

The cooperative comparison and Metzler-matrix ingredients are standard and not presented as new. The claimed contribution is their exact all-Hill-order, vaccination-weighted quantitative synthesis with the sharp Hill majorant and the critical-boundary argument for this model. The published \(n=1\) theorem does not imply the statement for \(n\ge2\), since the Hill derivative at zero and the comparison envelope differ.

## Limitations
The condition \(\mathcal T_n\le1\) is sufficient, not necessary; it is not asserted to be the sharp **nonlinear epidemic extinction threshold**. Optimality is claimed only for the scalar uniform inequality \(g_n(C)\le L_n C\). The theorem supplies no conclusion when \(\mathcal T_n>1\). The derived convergence is specific to the deterministic ODE with strictly positive parameters; stochastic extinction, temporal forcing, space, behavior adaptation, and optimal intervention policies are outside scope. The eventual exponential rate is not given as a uniform numerical constant over all admissible parameter vectors. The result has not received independent mathematical audit. An unindexed general monotone-system theorem might subsume parts of the proof method.

## References
[1] E. Penitente, U. Foryś and B. Gürbüz, *Global stability and uniform persistence in an epidemic model with saturating fomite-mediated transmission*, arXiv:2603.28285v1 (first public 2026-03-30); *Ricerche di Matematica* (2026), DOI: 10.1007/s11587-026-01159-9. Model equation (2), Theorem 1, Remark 1, Sect. 5 and Appendix examined.

[2] A. Gökçe, B. Gürbüz and A. D. Rendall, *Dynamics of a mathematical model of virus spreading incorporating the effect of a vaccine*, arXiv:2307.12707v1 (2023), Theorem 3.1 and Sect. 4.

[3] J. C. Kamgang and G. Sallet, *Computation of threshold conditions for epidemiological models and global stability of the disease-free equilibrium (DFE)*, Mathematical Biosciences 213(1), 1–12 (2008); general comparison framework, not an independent model-specific Hill-order claim.
