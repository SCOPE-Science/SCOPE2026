# A spurious incidence sink makes the printed Milstein measles scheme drift-inconsistent

## Finding
Din's stochastic double-dose measles model has six state variables \(S,E,I,V_1,V_2,R\) and total population \(N=S+E+I+V_1+V_2+R\). In the stated SDE (2.2), the infected drift is
\[
b_I(S,E,I)=\phi E-(\mu+\gamma+\phi_1)I.
\]
Section 6.1 later prints a Milstein update with infected drift
\[
b_I^{\mathrm{M}}(S,E,I)=\phi E-(\mu+\gamma+\phi_1)I-\frac{\beta SI}{N}.
\]
Therefore the printed Milstein scheme has the exact drift defect
\[
b_I^{\mathrm{M}}-b_I=-\frac{\beta SI}{N},
\]
which is nonzero for every biologically interior state with \(S>0\), \(I>0\), and \(\beta>0\).

This is not a higher-order Milstein correction. It is an \(O(\Delta t)\) change in the one-step deterministic increment. Thus the printed scheme is a discretization of a different drift field. Removing this one extra incidence term from the infected update restores the stated model's drift.

## Assumptions and scope
The claim concerns the equations printed in model (2.2) and the Milstein scheme printed in Section 6.1 of Din (2026), DOI 10.3934/math.2026761. It assumes \(N>0\) and uses only the paper's compartment definitions and drift formulas. For the strict mismatch statement, assume \(\beta>0\), \(S>0\), and \(I>0\).

No claim is made about unpublished code. If the simulations were generated from code different from the printed Milstein formula, the effect on those particular figures would have to be assessed from that code. The mathematical statement here is exactly about the published formula and its relation to the published SDE.

## Proof
Write the target deterministic drift from model (2.2) as
\[
\begin{aligned}
b_S&=\Lambda-\frac{\beta SI}{N}-(\psi_v+\mu)S+\omega_vV_1,\\
b_E&=\frac{\beta SI}{N}-(\mu+\phi)E,\\
b_I&=\phi E-(\mu+\gamma+\phi_1)I,\\
b_{V_1}&=\psi_vS-(\mu+\omega_v+\kappa)V_1,\\
b_{V_2}&=\kappa V_1-(\mu+\omega)V_2,\\
b_R&=\gamma I+\omega V_2-\mu R.
\end{aligned}
\]
The incidence transfer \(\beta SI/N\) appears negatively in \(b_S\) and positively in \(b_E\); it does not appear in \(b_I\). The Section 6.1 Milstein formula instead inserts a second negative copy in the infected drift. Hence its deterministic one-step increment satisfies
\[
I_{n+1}-I_n=\left(b_I-\frac{\beta S_nI_n}{N_n}\right)\Delta t+\text{stochastic Milstein terms}.
\]
The Brownian Milstein correction has conditional mean zero because \(\mathbb E[(\Delta W)^2-\Delta t]=0\). More decisively, set all Gaussian and jump amplitudes to zero. Then the displayed scheme becomes ordinary forward Euler for the modified infected ODE
\[
\dot I=\phi E-(\mu+\gamma+\phi_1)I-\frac{\beta SI}{N},
\]
so decreasing \(\Delta t\) cannot recover the target infected equation at a state with \(\beta SI/N>0\).

Summing the six target drifts cancels every internal transfer:
\[
b_S+b_E+b_I+b_{V_1}+b_{V_2}+b_R=\Lambda-\mu N-\phi_1 I.
\]
Summing the drift part of the printed Milstein scheme leaves the additional term
\[
-\frac{\beta SI}{N},
\]
so its deterministic population increment is
\[
N_{n+1}-N_n=\left(\Lambda-\mu N_n-\phi_1 I_n-\frac{\beta S_nI_n}{N_n}\right)\Delta t
\]
before stochastic increments. The incidence event has therefore been converted into an artificial total-population sink as well as the intended \(S\)-to-\(E\) transfer.

The minimal correction is to delete only the extra \(-\beta S_nI_n/N_n\) from the infected Milstein drift. All target transfer cancellations then return exactly.

## Verification
The bundled verifier `verifier.py` symbolically reconstructs the six target drifts and the six printed Milstein drifts, verifies that their infected-component difference is exactly \(-\beta SI/N\), verifies the two population-balance identities, and evaluates an exact rational witness. With the paper's persistence value \(\beta=0.05=1/20\) and the admissible state \(S=I=1\), \(E=V_1=V_2=R=0\), so \(N=2\), the extra drift is
\[
-\frac{1}{40}.
\]
The verifier prints `VERIFY_OK` only after all symbolic identities and the witness pass.

The paper later gives a forward-Euler update for ANN data generation in which the infected drift is printed as \(\phi E-(\mu+\gamma+\phi_1)I\), with no extra incidence sink. This independent formula within the same article agrees with model (2.2) and localizes the discrepancy to the Section 6.1 Milstein update.

## Relationship to prior work
The 2026 article states that its deterministic model is based on the 2024 double-dose-vaccination study of Farhan et al. The present finding is not a new epidemic model and does not alter that deterministic transfer structure; it identifies a mismatch introduced when the 2026 paper writes its Milstein discretization.

A 2023 AIMS Mathematics paper by Khan and Din also studies measles under Lévy noise, but it uses a different compartmental model and does not supply the exact six-compartment double-dose Milstein formula at issue here. Searches for the 2026 DOI, title, the extra infected incidence term, drift consistency, population balance, correction, and erratum found no published correction or equivalent statement. The closest indexed epidemic results concerned other threshold questions and neither contain nor imply this source-specific discretization identity.

The article itself is the decisive comparison: model (2.2), its generator calculation, and its later ANN Euler update all use the infected drift without an incidence loss, while Section 6.1 alone prints the extra term.

## Limitations
The conclusion is about the printed equations, not inaccessible author code. It does not re-run Figures 1--2, estimate the quantitative bias accumulated over their full trajectories, or claim that every qualitative extinction/persistence conclusion changes. It proves the narrower structural fact that the published Milstein formula is drift-inconsistent with the published SDE whenever \(\beta SI/N>0\), and it identifies the exact correction.

No exhaustive search can establish absolute novelty. The literature and database checks reported in the accompanying review found no equivalent published correction; a later erratum, private correspondence, or nonindexed discussion could still exist.

## References
1. A. Din, “Stochastic analysis and ANN-based approximation of measles transmission dynamics under Lévy noise,” *AIMS Mathematics* 11(6), 18715--18745 (2026), DOI 10.3934/math.2026761. Published 25 June 2026. Primary MSC 92D30.
2. M. Farhan, Z. Ling, S. Ullah, M. Alsubhi, M. Asiri, M. B. Riaz, “A novel physics-informed neural network approach to assess the impact of double-dose vaccination on measles transmission,” *European Physical Journal Plus* 139, 1059 (2024), DOI 10.1140/epjp/s13360-024-05838-0.
3. A. Khan, A. Din, “Stochastic analysis for measles transmission with Lévy noise: a case study,” *AIMS Mathematics* 8(8), 18696--18716 (2023), DOI 10.3934/math.2023952.
