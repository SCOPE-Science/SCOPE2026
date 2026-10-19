# Sharp vaccinated-fomite extinction threshold and its universal critical decay law

## Finding
For the Holling type II vaccinated–fomite epidemic system of Penitente, Foryś and Gürbüz, the actual control reproduction number \(\mathcal R_c\), not the larger sufficient bound \(\mathcal J_c\), is the **sharp global disease-elimination threshold**. The disease-free equilibrium (DFE) is globally asymptotically stable for \(\mathcal R_c\le1\) and unstable for \(\mathcal R_c>1\). At equality, every trajectory starting with nonzero exposed, infectious, or environmental pathogen concentration has exactly the same leading inverse-time decay profile. This result encompasses arbitrary nonnegative initial conditions and strictly positive vaccination; it does not claim that every noncritical trajectory decays algebraically.

Set \(a=\xi+\mu\), \(b=\gamma+d+\mu\), \(h=\varphi/(\kappa\omega)\), and \(H=\alpha_1 S_0+\alpha_2V_0\). Let
\[
A=\begin{pmatrix}-(\sigma+\mu)&(1-p)\eta\\ \sigma&-(\eta+\mu)\end{pmatrix},\quad
q=\begin{pmatrix}\beta_1+\alpha_1h\\\beta_2+\alpha_2h\end{pmatrix},\quad
T=A^{-1}\begin{pmatrix}S_0q_1\\V_0q_2\end{pmatrix}.
\]
The entries of \(T\) are strictly negative. Define the strictly positive constant
\[
K=\frac{-q^\top T+Hh^2}{(a+b)/\xi+H\varphi/(\kappa\omega^2)}.
\]
If \(\mathcal R_c=1\) and \(E(0)+I(0)+C(0)>0\), then
\[
\lim_{t\to\infty}t I(t)=K^{-1},\qquad
\lim_{t\to\infty}t\begin{pmatrix}E(t)\\I(t)\\C(t)\end{pmatrix}
=\frac1K\begin{pmatrix}b/\xi\\1\\\varphi/\omega\end{pmatrix},\qquad
\lim_{t\to\infty}t\left[\begin{pmatrix}S(t)\\V(t)\end{pmatrix}-\begin{pmatrix}S_0\\V_0\end{pmatrix}\right]=\frac{T}{K}.
\]
The limit is independent of the magnitudes of the initial nonzero infection, though the finite-time approach is not.

## Assumptions and scope
In the biologically meaningful nonnegative cone, take \(\Lambda,\mu,\sigma,\eta,\xi,\gamma,d,\beta_1,\beta_2,\alpha_1,\alpha_2,\kappa,\varphi,\omega>0\), \(0<p<1\), \(\beta_2\le\beta_1\), \(\alpha_2\le\alpha_1\), with the Holling type II response \(g(C)=C/(\kappa+C)\). The five-dimensional subsystem (the recovered class is linearly slaved) is
\[
\begin{aligned}
\dot S&=\Lambda-(\sigma+\mu)S+(1-p)\eta V-S[\beta_1I+\alpha_1g(C)],\\
\dot V&=\sigma S-(\eta+\mu)V-V[\beta_2I+\alpha_2g(C)],\\
\dot E&=I(\beta_1S+\beta_2V)+g(C)(\alpha_1S+\alpha_2V)-aE,\\
\dot I&=\xi E-bI,\qquad \dot C=\varphi I-\omega C.
\end{aligned}
\]
All finite initial data are nonnegative. The disease-free equilibrium has \((E,I,C)=(0,0,0)\) and
\[
S_0=\frac{\Lambda(\eta+\mu)}{D},\qquad V_0=\frac{\Lambda\sigma}{D},\qquad
D=\mu(\eta+\mu)+\sigma(\mu+p\eta).
\]
Its next-generation threshold is
\[
\mathcal R_c=\frac{\xi}{ab}\left[\beta_1S_0+\beta_2V_0+h(\alpha_1S_0+\alpha_2V_0)\right].
\]
For the full recovered class, \(\dot R=\gamma I-\mu R+p\eta V\); thus \(R\) tends to the corresponding immune DFE coordinate, but the displayed inverse-time law concerns the five-dimensional active subsystem. The claim excludes Holling type III responses, nonpositive rate parameters, external pathogen importation, and time-varying controls.

## Proof
**1. Invariance and uniform bounds.** Summing the four host equations for \(P=S+V+E+I\) gives \(\dot P=\Lambda-\mu P-dI-p\eta V\le\Lambda-\mu P\). Therefore all host coordinates are nonnegative, globally bounded, and the environmental equation bounds \(C\) for every finite initial condition. Moreover \(\dot S\ge\Lambda-(\sigma+\mu+\beta_1I+\alpha_1)S\); hence \(S\) eventually has a positive uniform lower bound along any given trajectory. The system remains in the nonnegative cone by its quasi-positive vector field.

**2. Demographic comparison.** Put \(u=(S,V)^\top\), \(u_0=(S_0,V_0)^\top\). Then \(u'=A(u-u_0)-f(u,I,C)\), where \(f=(S[\beta_1I+\alpha_1g(C)],V[\beta_2I+\alpha_2g(C)])^\top\ge0\). Matrix \(A\) is irreducible Metzler with negative trace and positive determinant \(D\); it is Hurwitz and \(e^{At}\ge0\). Variation of constants shows
\[
u(t)-u_0\le e^{At}(u(0)-u_0)^+
\]
componentwise, where the positive part is componentwise. The right side is exponentially small. This is an **eventual asymptotic upper comparison**, not the false assertion \(u(t)\le u_0\) at every time.

**3. Strictly subcritical global extinction.** Write \(y=(E,I,C)^\top\). Since \(g(C)\le C/\kappa\),
\[
y'\le B(u(t))y,\quad B(u)=\begin{pmatrix}
-a&\beta_1S+\beta_2V&(\alpha_1S+\alpha_2V)/\kappa\\
\xi&-b&0\\0&\varphi&-\omega
\end{pmatrix}.
\]
At \(u_0\), the Metzler matrix \(B_0=B(u_0)\) has negative spectral abscissa exactly when \(\mathcal R_c<1\) (the standard irreducible three-stage threshold, equivalently the source's local calculation). For sufficiently large time, \(B(u(t))\le B_0+\varepsilon M\) with a fixed nonnegative matrix \(M\) and sufficiently small \(\varepsilon>0\); this comparison matrix is still Hurwitz. Positivity of its semigroup gives \(y(t)\to0\) exponentially. The exponentially stable demographic equation then yields \(u(t)\to u_0\).

**4. Critical global extinction.** Assume \(\mathcal R_c=1\). The irreducible matrix \(B_0\) has one simple eigenvalue zero and its other eigenvalues in the open left half-plane. Its right and left nullvectors can be chosen as
\[
r=(b/\xi,1,\varphi/\omega)^\top,\qquad
\ell=(1,a/\xi,H/(\kappa\omega))^\top,
\]
with \(P_c=\ell^\top r=(a+b)/\xi+H\varphi/(\kappa\omega^2)>0\). The positive infected mass \(Z=\ell^\top y\) obeys the **exact identity**
\[
\begin{aligned}
Z'={}&\bigl[\beta_1(S-S_0)+\beta_2(V-V_0)\bigr]I
+\frac{\alpha_1(S-S_0)+\alpha_2(V-V_0)}{\kappa}C\\
&-\frac{(\alpha_1S+\alpha_2V)C^2}{\kappa(\kappa+C)}.
\end{aligned}
\]
Step 2 bounds the two possibly positive linear deviations by \(M_0e^{-ct}\), whereas Step 1 implies \(\alpha_1S+\alpha_2V\ge k_0>0\) eventually. Since \(I+C\le M_1Z\), there are constants \(c,M_2,k_1>0\) (depending on the solution) such that for all large \(t\),
\[
Z'\le M_2e^{-ct}Z-k_1\frac{C^2}{\kappa+C}.
\]
Multiplication by the integrating factor for \(M_2e^{-ct}\) shows that \(Z\) is bounded and \(\int_{t_0}^\infty C(t)^2/(\kappa+C(t))\,dt<\infty\). Boundedness of \(C'\) gives \(C(t)\to0\) (uniform continuity and the nonnegative integrand). Bounded \(C''=\varphi I'-\omega C'\) gives \(C'(t)\to0\), hence \(I(t)\to0\) by \(C'=\varphi I-\omega C\). Bounded \(I''=\xi E'-bI'\) likewise implies \(I'(t)\to0\), hence \(E(t)\to0\). Variation of constants then yields \(u(t)\to u_0\). In addition, the same positive-mass bound and demographic variation of constants prove Lyapunov stability for sufficiently small initial disturbances, so the DFE is globally asymptotically stable at equality, not merely globally attractive.

**5. Exact critical coefficient.** The linearization at the DFE has exactly one center eigenvalue, with tangent vector \((T,r)\) in the \((u,y)\) splitting. Indeed, the demographic center equation is \(AT=\operatorname{diag}(S_0,V_0)q\), so \(T\) is strictly negative because \(-A^{-1}\) is entrywise positive. For the analytic center manifold, parameterize by \(i=I\); then
\[
u=u_0+Ti+O(i^2),\quad y=ri+O(i^2),\quad Z=P_ci+O(i^2).
\]
Substitute into the exact mass identity: the quadratic term is \((q^\top T-Hh^2)i^2\), and therefore
\[
\dot i=-Ki^2+O(i^3),\quad K=\frac{-q^\top T+Hh^2}{P_c}>0.
\]
The strict sign comes from the positive parameters and \(T<0\). The neighboring stable spectrum has strictly negative real parts, so the local center-manifold stable-foliation/tracking theorem reduces every sufficiently late orbit converging to the DFE to a center orbit up to an exponentially small remainder. A nonzero-infection nonnegative orbit cannot lie on the exceptional exponentially converging strong-stable leaf: on such an orbit the exact \(Z'\) identity and \(I,C\le MZ\) imply \(Z'\ge-M'e^{-ct}Z\), whose integrated lower bound contradicts \(Z(t)\to0\) for \(Z(t_0)>0\). Its center coordinate is therefore positive and solves \(\dot i=-Ki^2+O(i^3)\), yielding \(ti(t)\to 1/K\). Tracking and the linear center tangent then give all five coordinate limits in the Finding. On the invariant infection-free face \(E=I=C=0\), the only motion is the exponentially convergent demographic subsystem; thus the nonzero-infection qualification is essential.

**6. Necessity.** If \(\mathcal R_c>1\), the irreducible infected Jacobian has a strictly positive eigenvalue. Therefore the DFE is unstable and cannot be globally asymptotically stable; the motivating study additionally proves uniform persistence. This completes the if-and-only-if threshold assertion.

## Verification
For the exactly rational parameter choice
\[
\Lambda=7/2,\quad p=1/2,\quad \beta_1=3/2,\quad \beta_2=1/2,\quad \alpha_1=1,\quad \alpha_2=1/2,
\]
with every other positive rate in the model equal to \(1\), one computes \((S_0,V_0)=(2,1)\), \(\mathcal R_c=1\), \(\mathcal J_c=35/24>1\), \(T=(-3,-2)\), \(K=8/5\). Hence the rigorous prediction is
\[
\lim_{t\to\infty}t(E,I,C)=(15/8,5/8,5/8),\quad
\lim_{t\to\infty}t(S-2,V-1)=(-15/8,-10/8).
\]
The included `verify.py` uses only the Python standard library and exact fractions to reconstruct the matrices, eigenvector identities, thresholds, center coefficient, and predictions. It also checks the second-order infected-mass coefficient by an independent formal Taylor calculation for this witness. Numerical integration from distinct initial conditions (which is not a proof) approaches the predicted \(tI\to 5/8\) and stage ratios.

## Relationship to prior work
Penitente–Foryś–Gürbüz (2026) derive \(\mathcal R_c\), prove local DFE stability for \(\mathcal R_c<1\), global DFE stability under the **stronger** condition \(\mathcal J_c\le1\), and persistence when \(\mathcal R_c>1\). Their Theorem 1 and Remark 1 explicitly distinguish these thresholds and give sharp global extinction only in the unvaccinated limit. Their vaccinated case does not contain the sharp \(\mathcal R_c\le1\) global theorem or the universal critical coefficient \(K\). Gökçe–Gürbüz–Rendall (2024) analyze the same parent model's local transcritical bifurcation and forward direction for Holling type II. Their local coefficient is compatible with quadratic decay near the DFE, but does not imply the **all-initial-data global** conclusion above. Kamgang–Sallet's general sufficient-condition approach is invoked in the 2026 source, but its specific upper comparison uses \(\mathcal J_c\), not the sharp vaccinated \(\mathcal R_c\) threshold. General critical-extinction results for structurally different epidemic systems do not imply these fomite-specific five-coordinate amplitudes. Novelty is assessed relative to the identified accessible literature, not asserted as a proof that nothing comparable can exist.

## Limitations
The theorem is for the smooth Holling type II dose response with strictly positive constant rates. The critical asymptotic excludes initial states on the exactly infection-free invariant face and supplies no finite-time error bound or parameter-uniform approximation near \(\mathcal R_c=1\). It does not address Holling type III backward bifurcation, seasonal forcing, stochastic fluctuations, spatial mixing, or arbitrary incidence functions. The center-manifold/stable-foliation reduction is a classical finite-dimensional theorem; independent formal validation of the entire result is not claimed. Literature comparisons cannot rule out all unpublished or unindexed equivalent results.

## References
1. E. Penitente, U. Foryś and B. Gürbüz, “Global stability and uniform persistence in an epidemic model with saturating fomite-mediated transmission,” *Ricerche di Matematica* (2026), DOI: 10.1007/s11587-026-01159-9; first posted 2026-03-30, arXiv:2603.28285. Theorem 1, Remark 1 and equations (2)–(5).
2. A. Gökçe, B. Gürbüz and A. D. Rendall, “Dynamics of a mathematical model of virus spreading incorporating the effect of a vaccine,” *Nonlinear Analysis: Real World Applications* 78 (2024), article 104097, DOI: 10.1016/j.nonrwa.2024.104097; arXiv:2307.12707.
3. J. C. Kamgang and G. Sallet, “Computation of threshold conditions for epidemiological models and global stability of the disease-free equilibrium,” *Mathematical Biosciences* 213 (2008), 1–12; cited and applied in Reference 1.
