# Sharp vaccination extinction threshold and exact infection decay exponent in a fomite SVEIR system

## Finding

**Theorem (sharp global Holling-II vaccination threshold and infection exponent).** For the six-compartment model and parameter assumptions below, the disease-free equilibrium is globally asymptotically stable on the nonnegative state cone **if and only if** the control reproduction number satisfies \(\mathcal R_c\le 1\). For every initial state with \(E(0)+I(0)+C(0)>0\), if \(\mathcal R_c\le1\) then, more precisely,
\[
\lim_{t\to\infty}\frac{1}{t}\log\big(E(t)+I(t)+C(t)\big)=s(B_0),
\]
where \(s(B_0)\) is the spectral abscissa of the explicit irreducible Metzler matrix below: it is negative for \(\mathcal R_c<1\), and zero at \(\mathcal R_c=1\). The equality case is globally attracting but not exponentially attracting along initially infected or contaminated trajectories. At \(\mathcal R_c>1\), the disease-free state has a positive unstable eigenvalue, so cannot be globally asymptotically stable.

The theorem retains imperfect vaccination and the environmental infection pathway. In contrast to the earlier sufficient threshold \(\mathcal J_c\le1\), the exact sharp extinction boundary depends on vaccination parameters. For an exact parameter family displayed below, \(\mathcal J_c=3/2>1\) while \(\mathcal R_c=15/31<1\); at a second member \(\mathcal J_c=31/10>1\) while \(\mathcal R_c=1\). Both disease-free states are therefore globally asymptotically stable outside the range certified by that earlier criterion.

## Assumptions and scope

The state is \((S,E,I,V,R,C)\in[0,\infty)^6\): susceptible, exposed, infectious, vaccinated awaiting protection, recovered/immune hosts, and environmental pathogen. For \(n=1\), put \(g(C)=C/(\kappa+C)\). The system is
\[
\begin{aligned}
\dot S&=\Lambda-(\sigma+\mu)S+(1-p)\eta V-\beta_1 SI-\alpha_1 Sg(C),\\
\dot E&=(\beta_1 S+\beta_2 V)I+(\alpha_1S+\alpha_2V)g(C)-(\xi+\mu)E,\\
\dot I&=\xi E-(\gamma+d+\mu)I,\\
\dot V&=\sigma S-(\eta+\mu)V-\beta_2VI-\alpha_2 Vg(C),\\
\dot R&=\gamma I-\mu R+p\eta V,\\
\dot C&=\varphi I-\omega C.
\end{aligned}
\]
Assume \(\Lambda,\mu,\sigma,\eta,\xi,\kappa,\omega,\varphi,\alpha_1,\beta_1>0\), \(0<p<1\), \(\gamma,d\ge0\), \(0\le\alpha_2\le\alpha_1\), and \(0\le\beta_2\le\beta_1\). The positive-parameter regime of the motivating article is contained in these assumptions. All assertions concern finite nonnegative initial data; no truncation to a particular invariant box is needed.

Define \(D=\mu(\mu+\eta)+\sigma(\mu+p\eta)\) and
\[
S_0=\frac{\Lambda(\mu+\eta)}{D},\qquad V_0=\frac{\Lambda\sigma}{D},\qquad R_0^{\mathrm{df}}=\frac{p\eta V_0}{\mu}.
\]
Here \(R_0^{\mathrm{df}}\) is the **recovered-compartment disease-free level**, not a reproduction number. The disease-free equilibrium is \(X_0=(S_0,0,0,V_0,R_0^{\mathrm{df}},0)\). Write
\[
A=\xi+\mu,\quad H=\gamma+d+\mu,\quad b_0=\beta_1S_0+\beta_2V_0,\quad a_0=\alpha_1S_0+\alpha_2V_0,
\]
\[
B_0=\begin{pmatrix}-A&b_0&a_0/\kappa\\ \xi&-H&0\\0&\varphi&-\omega\end{pmatrix},\qquad
\mathcal R_c=\frac{\xi}{AH}\left(b_0+\frac{\varphi a_0}{\kappa\omega}\right).
\]
The matrix is irreducible Metzler since \(S_0,\alpha_1,\beta_1,\xi,\varphi>0\).

## Proof

**1. Global positive solutions and the infection-free envelope.** Every boundary derivative points inward or along the nonnegative cone. With \(N=S+E+I+V+R\), direct summation gives \(\dot N=\Lambda-\mu N-dI\le\Lambda-\mu N\); thus every host state is bounded, and \(\dot C=\varphi I-\omega C\) bounds environmental pathogen. Smoothness on the cone gives global solutions with bounded first derivatives.

Set \(x=(S,V)^T\), and let \(x_0=(S_0,V_0)^T\). Then
\[
\dot x=H_u x+(\Lambda,0)^T-q(t),\quad
H_u=\begin{pmatrix}-(\sigma+\mu)&(1-p)\eta\\ \sigma&-(\eta+\mu)\end{pmatrix},
\]
\[
q(t)=\begin{pmatrix}\beta_1SI+\alpha_1Sg(C)\\ \beta_2VI+\alpha_2Vg(C)\end{pmatrix}\ge0.
\]
The trace of \(H_u\) is negative and its determinant is \(D>0\), so it is Hurwitz. Since it is Metzler, \(e^{H_ut}\) is entrywise nonnegative. Let \(\bar x\) solve the infection-free linear system with \(\bar x(0)=x(0)\). Variation of constants yields the exact comparison
\[
\bar x(t)-x(t)=\int_0^t e^{H_u(t-s)}q(s)\,ds\ge0,\qquad
\bar x(t)-x_0=e^{H_ut}(x(0)-x_0).
\]
Consequently, for some \(r>0\) and \(K<\infty\) determined by the initial state,
\[
 S(t)\le S_0+Ke^{-rt},\qquad V(t)\le V_0+Ke^{-rt}\quad(t\ge0).
\tag{1}
\]
This time-decaying **componentwise** envelope is the key distinction from replacing both host compartments by the fixed total-population maximum.

**2. Infection linearization and the sign criterion.** For \(z=(E,I,C)^T\), its exact equation is \(\dot z=B(t)z\), where
\[
B(t)=\begin{pmatrix}-A&\beta_1S(t)+\beta_2V(t)&(\alpha_1S(t)+\alpha_2V(t))/(\kappa+C(t))\\ \xi&-H&0\\0&\varphi&-\omega\end{pmatrix}.
\]
At the disease-free state this becomes \(B_0\). The characteristic determinant at zero satisfies
\[
\det(-B_0)=AH\omega-\xi\big(\omega b_0+\varphi a_0/\kappa\big)=AH\omega(1-\mathcal R_c).
\]
Because \(B_0\) is irreducible Metzler with a positive transmission cycle, the Perron–Frobenius comparison criterion gives \(s(B_0)<0\), \(=0\), or \(>0\) according as \(\mathcal R_c<1\), \(=1\), or \(>1\). An elementary alternative is to note that the nonnegative next-generation operator has radius \(\mathcal R_c\), while \(B_0\) is an irreducible infected-block \(F-V\) decomposition with stable positive \(V\). The zero root is simple at equality. The uninfected block \(H_u\) and recovered eigenvalue \(-\mu\) are stable, so \(\mathcal R_c>1\) makes the full equilibrium unstable.

**3. Strictly subcritical convergence.** Since \(g(C)\le C/\kappa\) and (1) holds, for every \(\varepsilon>0\), after sufficiently long time \(B(t)\le B_+(\varepsilon)\) entrywise for a constant irreducible Metzler matrix formed from \(B_0\) by increasing its two positive first-row off-diagonal entries by \(\varepsilon\). If \(\mathcal R_c<1\), choose \(\varepsilon\) so that \(s(B_+(\varepsilon))<0\). Positivity of the linear comparison system gives \(0\le z(t)\le e^{B_+(\varepsilon)(t-T)}z(T)\), hence \(E,I,C\to0\) exponentially. Now \(q(t)\to0\), and stable convolution in the \(x\)-equation gives \(x(t)\to x_0\); the recovered equation then yields \(R(t)\to R_0^{\mathrm{df}}\). Standard local linear stability or the same small-data comparison gives Lyapunov stability.

**4. Equality case.** Assume \(\mathcal R_c=1\). By irreducibility there exists \(w=(w_E,w_I,w_C)^T>0\) with \(w^TB_0=0\). Put \(W=w^Tz\), \(a(t)=\alpha_1S(t)+\alpha_2V(t)\), and \(b(t)=\beta_1S(t)+\beta_2V(t)\). Direct subtraction of \(w^TB_0z=0\) gives the **exact** identity
\[
\dot W=w_E\left[(b(t)-b_0)I+\frac{a(t)-a_0}{\kappa}C-
\frac{a(t)C^2}{\kappa(\kappa+C)}\right].
\tag{2}
\]
Using (1) and equivalence of \(W\) with \(E+I+C\),
\[
\dot W\le K_1e^{-rt}W-\frac{w_Ea(t)C^2}{\kappa(\kappa+C)}.
\tag{3}
\]
Gronwall bounds \(W\) uniformly. The already-established host bounds imply a finite upper bound \(M_I\) for \(I\), so
\(\dot S\ge\Lambda-(\sigma+\mu+\beta_1M_I+\alpha_1)S\).
Hence \(\liminf_{t\to\infty}S(t)>0\), and therefore \(a(t)\ge a_*>0\) for all sufficiently large \(t\). Integrating (3) and using \(W\ge0\) yields
\[
\int_T^\infty\frac{C(t)^2}{\kappa+C(t)}\,dt<\infty.
\]
The nonnegative \(C\) has bounded derivative; therefore \(C(t)\to0\) by uniform continuity. Moreover \(C'=\varphi I-\omega C\) is uniformly continuous because \(I'\) and \(C'\) are bounded. Since \(C\) converges, its uniformly continuous derivative converges to zero (Barbalat's lemma), giving \(I(t)\to0\). The stable \(E\)-equation has forcing \(b(t)I+a(t)g(C)\to0\), so \(E\to0\); the stable \(x\)- and recovered equations then give convergence to \(X_0\).

For Lyapunov stability at this nonhyperbolic boundary, choose initial displacement at most \(\delta\) from \(X_0\). The homogeneous envelope error is then bounded by \(K\delta e^{-rt}\) uniformly on a common bounded neighborhood. Equation (3) implies \(W(t)\le W(0)\exp(K\delta/r)\) for all \(t\ge0\). On that neighborhood \(\|q(t)\|\le K_2W(t)\). Stable convolution of the \(x\) and \(R\) equations therefore bounds the total displacement for every \(t\ge0\) by \(K_3(\delta+W(0))\). This proves Lyapunov stability as well as global attraction at equality.

**5. Exact asymptotic logarithmic decay rate.** For either \(\mathcal R_c<1\) or \(\mathcal R_c=1\), the previous steps show \(S\to S_0\), \(V\to V_0\), and \(C\to0\), hence \(B(t)\to B_0\). A trajectory with \(E(0)+I(0)+C(0)>0\) has \(z(T)>0\) componentwise for every sufficiently large \(T>0\) because \(\xi,\varphi,\beta_1S(t),\alpha_1S(t)>0\) for \(t>0\). Given sufficiently small \(\varepsilon>0\), bound the two first-row off-diagonal entries for all \(t\ge T\) between those of constant irreducible Metzler matrices \(B_-(\varepsilon)\le B(t)\le B_+(\varepsilon)\), whose entries converge to those of \(B_0\) as \(\varepsilon\downarrow0\). Cooperative-system comparison gives
\[
e^{B_-(\varepsilon)(t-T)}z(T)\le z(t)\le e^{B_+(\varepsilon)(t-T)}z(T).
\]
For strictly positive initial vectors, Perron–Frobenius asymptotics give logarithmic growth rates \(s(B_-(\varepsilon))\) and \(s(B_+(\varepsilon))\) to the bounding systems. Letting \(\varepsilon\downarrow0\) by eigenvalue continuity proves
\[
\lim_{t\to\infty}t^{-1}\log\|z(t)\|_1=s(B_0).
\]
At \(\mathcal R_c=1\), this rate is exactly zero although \(z(t)\to0\), so no uniform strictly exponential trajectory decay holds there. Together with the supercritical instability, this proves the theorem.

## Verification

Use the accompanying standalone standard-library code `verify.py`: run `python3 verify.py` from the package directory. It checks rational disease-free values, exact reproduction thresholds, the characteristic polynomial, an exact positive left-null eigenvector for the critical infected matrix, and positivity/convergence in illustrative fourth-order Runge–Kutta trajectories. Its expected output is `VERIFY_OK: exact rational matrices, critical kernel, and non-proof trajectories`. **The numerical trajectories do not establish the global theorem**; Steps 1–5 are its mathematical proof.

For the exact witness take \(\Lambda=\mu=\eta=\xi=\kappa=\omega=\varphi=1\), \(\sigma=9\), \(p=1/2\), \(\gamma=d=1/2\), \(\beta_1=\alpha_1=3m\), and \(\beta_2=\alpha_2=m\). Then \(S_0=4/31\), \(V_0=18/31\), \(\mathcal R_c=15m/31\), and \(\mathcal J_c=3m/2\). For \(m=1\), \(\mathcal R_c=15/31<1<\mathcal J_c=3/2\), with
\[
\det(\lambda I-B_0)=\lambda^3+5\lambda^2+\frac{218}{31}\lambda+\frac{64}{31}.
\]
For \(m=31/15\), \(\mathcal R_c=1<\mathcal J_c=31/10\) and
\[
B_0=\begin{pmatrix}-2&2&2\\1&-2&0\\0&1&-1\end{pmatrix},\quad
\det(\lambda I-B_0)=\lambda(\lambda+2)(\lambda+3),\quad (1,2,2)B_0=0.
\]
Both exact rational tests respect the original paper's strictly positive parameter conditions.

## Relationship to prior work

Penitente–Foryś–Gürbüz (arXiv:2603.28285v1, Sections 3.1–3.2, Theorem 1, Remark 1 and Corollary 1) establish the control reproduction number, local stability for \(\mathcal R_c<1\), a sufficient global criterion \(\mathcal J_c\le1\), and the **sharp nonvaccinated** special case \(\mathcal R_0\le1\). Their proof takes a time-independent maximal infection bound across the whole invariant host region. The present theorem sharpens the **vaccinated** case, including \(\mathcal R_c=1\), by exploiting the exponentially converging infection-free upper envelope of both susceptible populations; it also determines the exact asymptotic logarithmic infection exponent, not given in their results. The explicit witnesses demonstrate a real difference in parameter coverage, rather than a rewriting of the same sufficient condition.

The original Gökçe–Gürbüz–Rendall model (arXiv:2307.12707v1 and its open 2024 publication) develops local stability and bifurcation for both Holling-II and higher-order saturation. General positive-system and Perron–Frobenius comparison methods are established antecedents. In particular, Kamgang–Sallet (2005), Theorem 2.1 and Corollary 2.2, obtain a sharp global reproduction-number threshold when a single time-independent upper bound on the infected matrix equals its value at the disease-free state. That hypothesis fails globally here: states with \(S>S_0\) yield infection coefficients above their disease-free values. The present proof instead uses the **transient time-dependent** infection-free envelope and a critical saturation-dissipation identity. Novelty is claimed for this concrete sharp vaccinated fomite-model theorem and its exact logarithmic exponent, not for general Metzler theory.

## Limitations

This theorem addresses autonomous, deterministic, Holling-II incidence \(n=1\) with no waning of recovered immunity. It does not extend to Holling-III \(n\ge2\), for which backward bifurcation can occur. The equality-case logarithmic rate zero is not a claim of a precise algebraic prefactor. No observation model, parameter estimation, stochastic process, numerical convergence order, or epidemiological data fitting is established. The comparison with accessible published work does not rule out unindexed or unpublished equivalents; independent scientific validation has not been performed.

## References

1. E. Penitente, U. Foryś and B. Gürbüz, *Global stability and uniform persistence in an epidemic model with saturating fomite-mediated transmission*, arXiv:2603.28285v1 (30 March 2026), https://arxiv.org/html/2603.28285v1; later published in *Ricerche di Matematica*, DOI 10.1007/s11587-026-01159-9 (2026).
2. A. Gökçe, B. Gürbüz and A. D. Rendall, *Dynamics of a mathematical model of virus spreading incorporating the effect of a vaccine*, arXiv:2307.12707v1 (2023); open 2024 published version, https://openscience.ub.uni-mainz.de/server/api/core/bitstreams/f1c57520-9683-4d6a-bfc7-5469950e85fe/content.
3. J. C. Kamgang and G. Sallet, *Global asymptotic stability for the disease-free equilibrium for epidemiological models*, *C. R. Math. Acad. Sci. Paris* **341** (2005), 433–438, DOI 10.1016/j.crma.2005.07.015, https://www.numdam.org/item/10.1016/j.crma.2005.07.015.pdf, especially Theorem 2.1 and Corollary 2.2.
