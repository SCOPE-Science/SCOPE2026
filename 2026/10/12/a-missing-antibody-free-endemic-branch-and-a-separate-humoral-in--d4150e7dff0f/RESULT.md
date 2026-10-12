# A missing antibody-free endemic branch and a separate humoral-invasion threshold in an HPV model
## Finding
Consider the within-host system
\[
\dot S=\lambda-d_SS-\frac{\beta SV}{1+\sigma V},\qquad
\dot I=\frac{\beta SV}{1+\sigma V}-d_II-pEI,
\]
\[
\dot V=kI-d_VV-qAV,\qquad
\dot C=\gamma I+(\xi-d_C)C,
\]
\[
\dot E=s+\frac{cIE}{h_1+E}-d_EE,\qquad
\dot A=\frac{\omega VA}{h_2+A}-d_AA.
\]
All kinetic parameters are positive and \(d_C>\xi\). The source analyzes a disease-free equilibrium and a positive-antibody endemic equilibrium, but the printed equations have an invariant face \(A=0\) carrying an additional endemic branch.

Set
\[
E_b=\frac{s}{d_E},\qquad D(E)=d_I+pE,\qquad
I(E)=\frac{(d_EE-s)(h_1+E)}{cE}\quad(E>E_b).
\]
Define
\[
\beta_c=\frac{d_Sd_V(d_I+ps/d_E)}{k\lambda}.
\]
There is a unique antibody-free endemic equilibrium exactly when \(\beta>\beta_c\). Its coordinates are
\[
I^*=I(E^*),\qquad V^*=\frac{kI^*}{d_V},\qquad
S^*=\frac{D(E^*)(d_V+\sigma kI^*)}{\beta k},\qquad
C^*=\frac{\gamma I^*}{d_C-\xi},
\]
where \(E^*>E_b\) is the unique root of
\[
\lambda=D(E)\left[\frac{d_Sd_V}{\beta k}+
\left(1+\frac{d_S\sigma}{\beta}\right)I(E)\right].
\]
Moreover, \(E^*\), \(I^*\), and \(V^*\) increase strictly with \(\beta\).

The exact transverse antibody eigenvalue is
\[
r_A=\frac{\omega V^*}{h_2}-d_A.
\]
Let
\[
I_A=\frac{d_Ad_Vh_2}{\omega k},
\]
and let \(E_A>E_b\) be the unique solution of \(I(E_A)=I_A\). With \(D_A=d_I+pE_A\), a finite antibody-invasion threshold exists exactly when \(\lambda>D_AI_A\), and then it is
\[
\beta_A=
\frac{D_A d_S(d_V+\sigma kI_A)}
{k(\lambda-D_AI_A)}>\beta_c.
\]
For \(\beta_c<\beta<\beta_A\), the antibody direction decays locally; for \(\beta>\beta_A\), a small antibody population grows locally. If \(\lambda\le D_AI_A\), the antibody-free branch has no finite antibody-invasion crossing.

This separates viral invasion from humoral invasion. The source's disease-free next-generation number is
\[
R_0^2=\frac{\beta k\lambda}
{d_Sd_V(d_I+ps/d_E)}=\frac{\beta}{\beta_c},
\]
so neither \(q\) nor \(\omega\) belongs in that first threshold. The later sensitivity formula in the source that inserts \(d_V+q\omega\) into the denominator is therefore not the disease-free next-generation threshold of the printed equations.

## Assumptions and scope
The result concerns the autonomous uncontrolled system printed in the source, on the nonnegative state space. Parameters are positive and \(d_C>\xi\). The additional equilibrium has \(A=0\), \(I>0\), and all other listed coordinates positive. The result is source-specific: it does not claim a new general theory of humoral-immune invasion thresholds.

The source imposes strictly positive initial data early in its model presentation, but later states a positively invariant box that includes boundary points and formulates a global-stability theorem for initial conditions in that box. The invariant-face observation applies to the nonnegative mathematical state space and shows that the theorem cannot literally send \(A(0)=0\) to an equilibrium with \(A^*>0\). This finding does not assess the theorem restricted to strictly positive antibody initial data.

## Proof
The antibody equation factors:
\[
\dot A=A\left(\frac{\omega V}{h_2+A}-d_A\right),
\]
so \(A=0\) is invariant.

At an antibody-free equilibrium with \(I>0\), the virus equation gives
\[
V=\frac{kI}{d_V}.
\]
The CTL equation gives
\[
cIE=(d_EE-s)(h_1+E),
\]
hence \(E>E_b=s/d_E\) and
\[
I=I(E)=\frac{(d_EE-s)(h_1+E)}{cE}.
\]
Its derivative is
\[
I'(E)=\frac{1}{c}\left(d_E+\frac{sh_1}{E^2}\right)>0,
\]
so \(I(E)\) maps \((E_b,\infty)\) strictly increasingly from \(0\) to \(\infty\).

Dividing the infected-cell equilibrium equation by \(I>0\) and substituting \(V=kI/d_V\) yields
\[
\frac{\beta kS}{d_V+\sigma kI}=d_I+pE=D(E),
\]
so
\[
S=\frac{D(E)(d_V+\sigma kI(E))}{\beta k}.
\]
The susceptible equilibrium equation is
\[
\lambda=d_SS+(d_I+pE)I.
\]
Substitution gives
\[
\lambda=F_\beta(E)
=D(E)\left[\frac{d_Sd_V}{\beta k}+
\left(1+\frac{d_S\sigma}{\beta}\right)I(E)\right].
\]
For \(E>E_b\), both \(D(E)\) and the bracketed factor are positive and strictly increasing, so \(F_\beta\) is strictly increasing. At the left endpoint,
\[
F_\beta(E_b)=
\frac{d_Sd_V(d_I+ps/d_E)}{\beta k}
=\lambda\frac{\beta_c}{\beta},
\]
and \(F_\beta(E)\to\infty\) as \(E\to\infty\). Therefore \(F_\beta(E)=\lambda\) has exactly one root in \(E>E_b\) if and only if \(\beta>\beta_c\). This proves existence and uniqueness of the antibody-free endemic equilibrium.

For fixed \(E>E_b\),
\[
\frac{\partial F_\beta(E)}{\partial\beta}
=-\frac{D(E)d_S(d_V+\sigma kI(E))}{\beta^2k}<0.
\]
Since \(F_\beta\) is strictly increasing in \(E\), its unique root \(E^*(\beta)\) is strictly increasing in \(\beta\). Consequently \(I^*(\beta)\) and \(V^*(\beta)\) are strictly increasing as well.

At \(A=0\), differentiating the antibody equation with respect to \(A\) gives the transverse eigenvalue
\[
r_A=\frac{\omega V^*}{h_2}-d_A.
\]
Thus the sign changes exactly when \(I^*=I_A=d_Ad_Vh_2/(\omega k)\). Because \(I(E)\) is a bijection from \((E_b,\infty)\) to \((0,\infty)\), there is a unique \(E_A>E_b\) with \(I(E_A)=I_A\). Equivalently \(E_A\) is the positive root larger than \(E_b\) of
\[
d_EE^2+(d_Eh_1-s-cI_A)E-sh_1=0.
\]
At a crossing, the equilibrium identity becomes
\[
\lambda=D_A\left[I_A+
\frac{d_S(d_V+\sigma kI_A)}{\beta k}\right].
\]
A positive finite solution exists exactly when \(\lambda>D_AI_A\), and solving for \(\beta\) gives the displayed \(\beta_A\). Since the antibody-free branch is born with \(I^*=0\) at \(\beta_c\) and reaches \(I_A>0\) only later, every finite crossing satisfies \(\beta_A>\beta_c\).

If \(\lambda\le D_AI_A\), the right side at \(E_A\) remains at least \(\lambda\) even in the limit \(\beta\to\infty\), so the strictly increasing root \(E^*(\beta)\) never reaches \(E_A\) at finite \(\beta\). Hence there is no finite antibody-invasion crossing.

Finally,
\[
\dot C=0\quad\Longrightarrow\quad
C^*=\frac{\gamma I^*}{d_C-\xi}>0,
\]
so the branch is a genuine equilibrium branch of the full six-dimensional system.

## Verification
The bundled script `verification/verify.py` independently reconstructs the scalar equilibrium reduction, checks the residuals of all six equilibrium equations, verifies the strict ordering \(\beta_c<\beta_A\) in a representative positive-parameter instance, and checks the predicted sign change of the antibody eigenvalue on both sides of \(\beta_A\). It uses only the Python standard library and prints `VERIFY_OK` on success.

The analytic proof, not the numerical check, establishes the theorem for all positive parameters satisfying the stated hypotheses.

## Relationship to prior work
The motivating 2026 HPV paper explicitly includes a saturated antibody equation, states that the model has two equilibria, computes the disease-free next-generation threshold, and later uses a different sensitivity expression containing \(d_V+q\omega\). Its printed equilibrium census omits the invariant antibody-free endemic branch derived here.

Jiang and Wang (2014) studied a different HIV/HBV model with both CTL and antibody responses and explicitly introduced separate viral, CTL, antibody, and competitive immune-invasion reproduction numbers. Their full equilibrium classification confirms that secondary immune-invasion thresholds are a standard structural possibility in virus models. However, their equations differ materially from the HPV system here: the HPV model has a basal CTL source, saturated infection, a cancer compartment, and a different CTL response law. Their formulas do not imply the scalar function \(F_\beta\), the source-specific uniqueness result, or the exact \(\beta_A\) above without a new derivation.

The 2025 HPV/Langerhans-cell model treats humoral clearance implicitly through a virion-clearance parameter rather than an explicit antibody state, so it does not contain this invariant antibody-free face or the corresponding antibody-invasion threshold.

## Limitations
No statement is made about the five non-antibody eigenvalues of the antibody-free endemic equilibrium, so “antibody-decaying” and “antibody-growing” refer only to the transverse antibody direction. No transcritical-bifurcation claim is made at \(\beta_A\). The positive-antibody endemic branch is not re-solved or globally classified here. The result also does not establish global convergence for strictly positive antibody initial data.

Generic immune-invasion thresholds are known in earlier virus models; the originality claimed here is the exact source-specific missing branch, its unique scalar parameterization, and the sharp humoral-invasion boundary for this 2026 HPV system.

## References
1. F. Al Basir, K. Aldawsari, K. B. Blyuss, “A model for HPV-related cervical cancer dynamics with saturated terms: an optimal control problem using chemotherapy, immunotherapy, and antibody drugs,” AIMS Mathematics 11 (2026), 21293–21322. DOI: 10.3934/math.2026864.
2. C. Jiang, W. Wang, “Complete classification of global dynamics of a virus model with immune responses,” Discrete and Continuous Dynamical Systems - B 19 (2014), 1087–1103. DOI: 10.3934/dcdsb.2014.19.1087.
3. F. Al Basir, K. B. Blyuss, A. A. Raezah, B. Rahman, H. J. Alsakaji, “Mathematical modelling of the role of Langerhans cells in the dynamics of HPV infection,” Scientific Reports 15 (2025), 17505. DOI: 10.1038/s41598-025-02608-5.
