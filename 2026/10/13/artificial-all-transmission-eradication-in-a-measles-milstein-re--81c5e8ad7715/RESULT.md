# Artificial all-transmission eradication in a measles Milstein recurrence

## Finding

Consider the six-class measles system of Din (2026), with susceptible, exposed, infectious, first-dose vaccinated, second-dose vaccinated, and recovered variables \((S,E,I,V_1,V_2,R)\). Let all recruitment, transmission, and transition rates appearing below be strictly positive. For any such rates, the zero-noise specialization of the *printed* Section 6.1 Milstein recurrence has the exact cancellation
\[
(E_{n+1}+I_{n+1})-(E_n+I_n)=-h\bigl(\mu E_n+(\mu+\gamma+\phi_1)I_n\bigr).
\]
For every sufficiently small positive step \(h\), the full six-dimensional recurrence preserves the nonnegative cone and its total exposed-plus-infectious mass obeys
\[
0\le E_n+I_n\le(1-\mu h)^n(E_0+I_0),\qquad n=0,1,2,\ldots.
\]
**Consequently, the printed noise-free numerical recurrence forces infection eradication for every positive transmission rate \(\beta\), even where the source's intended deterministic model has an unstable disease-free equilibrium and a strictly positive endemic equilibrium.** Its infected update is not first-order consistent with the corresponding drift of the source's equation (2.2).

This conclusion concerns the numerical recurrence exactly as printed, not the correctly formulated stochastic differential equation or any implementation not independently inspected.

## Assumptions and scope

Write \(N=S+E+I+V_1+V_2+R\), \(\mathcal J=\beta SI/N\), and suppose \(\Lambda,\beta,\psi_v,\mu,\omega_v,\phi,\gamma,\phi_1,\kappa,\omega>0\). Initially all six states are nonnegative and \(N>0\). Define
\[
a=\mu+\phi,\quad d=\mu+\gamma+\phi_1,\quad A=\mu+\kappa+\omega_v,\quad B=\mu+\omega.
\]
The intended deterministic drift (equation (2.1), also the drift of stochastic equation (2.2)) is
\[
\begin{aligned}
S'&=\Lambda+\omega_v V_1-\mathcal J-(\psi_v+\mu)S,\\
E'&=\mathcal J-aE,\\
I'&=\phi E-dI,\\
V_1'&=\psi_vS-AV_1,\\
V_2'&=\kappa V_1-BV_2,\\
R'&=\gamma I+\omega V_2-\mu R.
\end{aligned}
\]
In contrast, the *printed* Section 6.1 formula adds \(-h\mathcal J_n\) to the infectious-coordinate step, in addition to the susceptible incidence loss. Set all six Gaussian and jump coefficients to zero, obtaining the paper's explicit first-order skeleton with the same remaining five drifts but with
\[
E_{n+1}=E_n+h(\mathcal J_n-aE_n),\qquad
I_{n+1}=I_n+h(\phi E_n-dI_n-\mathcal J_n).
\]
No assertion is made about the numerical recurrence when random increments are nonzero. The zero-noise restriction is used to test drift consistency and threshold preservation.

## Proof

**1. Global positivity at small steps.** Put
\[
M=\max\{\beta+\psi_v+\mu,\ a,\ d+\beta,\ A,\ B,\mu\}.
\]
For \(0<h\le1/M\) and nonnegative inputs, \(0\le I/N,S/N\le1\). The susceptible step satisfies
\[
S_{n+1}\ge[1-h(\beta+\psi_v+\mu)]S_n+h\Lambda+h\omega_v V_{1,n}\ge h\Lambda>0.
\]
The exposed and infectious updates obey
\[
E_{n+1}\ge(1-ha)E_n,\qquad I_{n+1}\ge[1-h(d+\beta)]I_n+h\phi E_n.
\]
The vaccinated and recovered coordinates satisfy the analogous inward-pointing Euler bounds with losses \(A,B,\mu\) and nonnegative inflows. Induction gives a nonnegative six-vector with \(N_n>0\) at every step, so each rational incidence expression is well-defined.

**2. Cancellation and sharp artificial extinction.** Addition of the two printed infection updates cancels \(+\mathcal J_n\) against \(-\mathcal J_n\) and cancels \(-\phi E_n\) against \(+\phi E_n\). Therefore
\[
H_{n+1}=H_n-h(\mu E_n+dI_n)\le(1-\mu h)H_n,
\qquad H_n=E_n+I_n.
\]
With \(0<h\le1/M\), the factor is in \([0,1)\) and all \(H_n\) are nonnegative. Iteration proves the claimed uniform geometric extinction. In the continuous modified vector field underlying the printed deterministic recurrence, the exact relation \(H'=-\mu E-dI\le-\mu H\) gives exponential extinction as well.

**3. Invasion thresholds differ for every positive rate choice.** Both deterministic vector fields have the same disease-free equilibrium, with
\[
S^*=\frac{\Lambda A}{\mu A+\psi_v(\mu+\kappa)},\qquad N^*=\frac{\Lambda}{\mu},\qquad q=\frac{S^*}{N^*}=\frac{\mu A}{\mu A+\psi_v(\mu+\kappa)}.
\]
The true infected linearization in variables \((E,I)\) and the modified printed one are respectively
\[
J_{\mathrm{true}}=\begin{pmatrix}-a&\beta q\\\phi&-d\end{pmatrix},\quad
J_{\mathrm{print}}=\begin{pmatrix}-a&\beta q\\\phi&-d-\beta q\end{pmatrix}.
\]
The true determinant is \(ad-\phi\beta q\), which is negative whenever \(\phi\beta q>ad\), giving a positive eigenvalue. However
\[
\operatorname{tr}J_{\mathrm{print}}=-(a+d+\beta q)<0,\qquad
\det J_{\mathrm{print}}=ad+(a-\phi)\beta q=ad+\mu\beta q>0.
\]
Thus the printed infected block is Hurwitz for **every** \(\beta>0\). The remaining four disease-free Jacobian eigenvalues arise from a stable susceptible/first-vaccine block and the two negative diagonal rates \(-B,-\mu\). In particular, the full printed disease-free fixed point is linearly attracting for sufficiently small Euler step sizes irrespective of transmission strength.

**4. Exact six-compartment contradiction.** Choose
\[
\Lambda=5,\quad\beta=20,\quad
\mu=\psi_v=\kappa=\omega_v=\omega=\phi=\gamma=\phi_1=1.
\]
The disease-free state in the order \((S,E,I,V_1,V_2,R)\) is
\[
\left(3,0,0,1,\frac12,\frac12\right),\qquad q=\frac35.
\]
The true infected block is \(\bigl(\begin{smallmatrix}-2&12\\1&-3\end{smallmatrix}\bigr)\), with eigenvalues \(1,-6\), so the disease-free state is unstable in the intended model. Indeed, the strictly positive state
\[
\boxed{\left(\frac{15}{11},\frac{15}{11},\frac5{11},\frac5{11},\frac5{22},\frac{15}{22}\right)}
\]
is an *exact endemic equilibrium* of all six intended equations, with \(N=50/11\) and \(\mathcal J=30/11\). The printed infectious drift evaluated there is \(-30/11\), so it is not a fixed point of the printed scheme. For the printed infected block, the trace is \(-17\) and determinant \(18\), hence it is Hurwitz. Taking \(h=1/40\) satisfies the explicit nonnegativity bound and forces \(E_n+I_n\le(39/40)^n(E_0+I_0)\) for **every** nonnegative initial state. At that same step size, the true Euler linearization has a multiplier \(41/40>1\).

**5. Consistency obstruction.** At every strictly positive state, the one-step drift of the printed infectious coordinate differs from that of equation (2.2) by \(-\mathcal J\), independently of step size. The local deterministic consistency defect is
\[
\frac{I_{n+1}-I_n}{h}-(\phi E_n-dI_n)=-\frac{\beta S_n I_n}{N_n},
\]
which does not tend to zero as \(h\downarrow0\). Deleting the extra \(-h\mathcal J_n\) from the printed infectious update removes this particular drift inconsistency and restores the correct deterministic total-infection balance, although it does not by itself establish convergence or positivity for the full Lévy scheme.

## Verification

Run the standalone standard-library program `verify.py`. It checks the exact rational equilibrium, exact right-hand sides, the disease-free fractions and two infected-block characteristic polynomials, the printed infection-mass cancellation, and the small-step cone-preservation bound. Expected last line: `VERIFY_OK`. The general all-parameter statement is proved symbolically in Steps 1–3, not inferred from finitely many computed examples.

## Relationship to prior work

Din (2026), equations (2.1) and (2.2), supplies the intended six-compartment drift; its Section 6.1 supplies the printed stochastic Milstein recurrence. The two formulas must be compared **coordinate by coordinate**: the extra infectious-coordinate infection loss is absent in the continuous system. Farhan and collaborators (2024) analyze the related deterministic double-vaccination measles system using a physics-informed neural network rather than this 2026 Lévy recurrence. The earlier measles Lévy study of Khan and Din (2023) addresses a stochastic vaccination system, but the accessible abstract does not settle the particular 2026 printed formula. The standard SEIR next-generation threshold is background; what is established here is an exact, all-parameter *extinction identity for this specific published numerical recurrence*, including a mismatch with an exact endemic state of its source ODE. Earlier analyses of the deterministic threshold alone do not imply this separate numerical conclusion.

## Limitations

The result is about the *printed formulas*, not confirmed software implementations or the random-increment scheme. The all-parameter extinction theorem holds on the zero-noise submodel under a concrete step-size bound; it does not prove stochastic almost-sure extinction. The corrected term is a local consistency repair only, not a certified high-order Lévy integrator. Some earlier literature could remain unindexed, and full-text access to the earlier Khan–Din study was incomplete. The particular endemic equilibrium is a mathematical counterexample, not a clinical forecast. No independent validation has been performed.

## References

1. A. Din, *Stochastic analysis and ANN-based approximation of measles transmission dynamics under Lévy noise*, AIMS Mathematics 11 (2026), 18715–18745, doi:10.3934/math.2026761; in particular equations (2.1), (2.2), and Section 6.1. https://www.aimspress.com/article/doi/10.3934/math.2026761
2. M. Farhan, Z. Ling, S. Ullah, M. Alsubhi, M. Asiri, and M. B. Riaz, *A novel physics-informed neural network approach to assess the impact of double-dose vaccination on measles transmission*, European Physical Journal Plus 139 (2024), 1059, doi:10.1140/epjp/s13360-024-05838-0.
3. A. Khan and A. Din, *Stochastic analysis for measles transmission with Lévy noise: a case study*, AIMS Mathematics 8 (2023), 18696–18716, doi:10.3934/math.2023952.
