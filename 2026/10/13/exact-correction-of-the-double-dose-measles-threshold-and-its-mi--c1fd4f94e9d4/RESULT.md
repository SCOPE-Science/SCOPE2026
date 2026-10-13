# Exact correction of the double-dose measles threshold and its missing-rate factor
## Finding
For the deterministic six-compartment measles system (2.1) of Din (2026), where \(N=S+E+I+V_1+V_2+R\), set \(k_1=\phi+\mu\), \(k_2=\gamma+\phi_1+\mu\), \(k_3=\omega_v+\kappa+\mu\), \(k_4=\omega+\mu\), \(D=\mu k_3+\psi_v(\kappa+\mu)\), and \(Q=k_3k_4+\psi_v(k_4+\kappa)\). The disease-free equilibrium has \(N^*=\Lambda/\mu\) and \(S^*=\Lambda k_3/D\), so the correct next-generation threshold is
\[\mathcal R_{\mathrm{tot}}=\frac{\beta\phi\,\mu k_3}{k_1k_2D}.\]
The 2026 paper instead prints \(\mathcal R_D^{(26)}=\beta\phi k_4/(k_1k_2Q)\). Under the paper's own rate definitions this quantity has units of time, so comparison with the dimensionless number \(1\) is not invariant under a change of time units. The cited 2024 predecessor prints the dimensionless expression \(\mathcal R_D^{(24)}=\beta\phi k_3k_4/(k_1k_2Q)\), but its displayed next-generation matrix normalizes by \(S^*+V_1^*+V_2^*\), omitting the nonzero recovered mass \(R^*\). Consequently
\[\mathcal R_D^{(24)}-\mathcal R_{\mathrm{tot}}=\frac{\beta\phi\,k_3\psi_v\kappa\omega}{k_1k_2DQ}\ge0,\]
strictly when \(\psi_v\kappa\omega>0\), while \(\mathcal R_D^{(26)}=\mathcal R_D^{(24)}/k_3\). The full disease-free Jacobian is locally asymptotically stable exactly when \(\mathcal R_{\mathrm{tot}}<1\), has a zero eigenvalue at equality, and is unstable when \(\mathcal R_{\mathrm{tot}}>1\). Thus the 2026 displayed threshold is not a valid reproduction number for the printed model, and even restoring its missing factor \(k_3\) leaves the recovered-mass normalization error inherited from the 2024 derivation.

## Assumptions and scope
Use equation (2.1) exactly as printed in Din (2026): standard incidence \(\beta SI/N\), six classes \(S,E,I,V_1,V_2,R\), and total population \(N=S+E+I+V_1+V_2+R\). Assume \(\Lambda,\mu,\beta,\phi>0\), \(\gamma,\phi_1,\psi_v,\omega_v,\kappa,\omega\ge0\), and \(k_2>0\). The strict recovered-mass comparison assumes \(\psi_v\kappa\omega>0\).

The result is a deterministic local-threshold statement. It does not independently re-prove the later stochastic extinction, persistence, global, ANN, or simulation claims.

## Proof
At a disease-free equilibrium, \(E^*=I^*=0\). The vaccination chain gives
\[
V_1^*=\frac{\psi_v}{k_3}S^*,\qquad
V_2^*=\frac{\kappa\psi_v}{k_3k_4}S^*,\qquad
R^*=\frac{\omega\kappa\psi_v}{\mu k_3k_4}S^*.
\]
The susceptible balance yields
\[
S^*=\frac{\Lambda k_3}{D},\qquad D=\mu k_3+\psi_v(\kappa+\mu).
\]
Summing all six ODEs gives \(\dot N=\Lambda-\mu N-\phi_1I\), hence \(N^*=\Lambda/\mu\). The infected linearization is
\[
\begin{pmatrix}\dot E\\\dot I\end{pmatrix}
=
\begin{pmatrix}-k_1&\beta S^*/N^*\\\phi&-k_2\end{pmatrix}
\begin{pmatrix}E\\I\end{pmatrix}.
\]
Therefore
\[
\mathcal R_{\mathrm{tot}}
=\frac{\beta\phi}{k_1k_2}\frac{S^*}{N^*}
=\frac{\beta\phi\,\mu k_3}{k_1k_2D}.
\]
The 2026 source prints
\[
\mathcal R_D^{(26)}=\frac{\beta\phi k_4}{k_1k_2Q},
\qquad Q=k_3k_4+\psi_v(k_4+\kappa).
\]
Every symbol in \(k_1,k_2,k_3,k_4,\beta,\phi,\psi_v,\kappa\) is a rate. Thus the numerator has rate-cubed units and the denominator rate-fourth units, so \(\mathcal R_D^{(26)}\) has units of time. If all rate numerals are multiplied by \(c>0\) under a change of time unit, then \(\mathcal R_D^{(26)}\) is divided by \(c\), whereas a reproduction number must be invariant.

The cited 2024 source instead has
\[
\mathcal R_D^{(24)}=\frac{\beta\phi k_3k_4}{k_1k_2Q}=k_3\mathcal R_D^{(26)}.
\]
Its displayed next-generation calculation uses the susceptible fraction
\[
\frac{S^*}{S^*+V_1^*+V_2^*}
=\frac{k_3k_4}{Q},
\]
not \(S^*/N^*\). Direct subtraction from the correct threshold gives
\[
\mathcal R_D^{(24)}-\mathcal R_{\mathrm{tot}}
=\frac{\beta\phi\,k_3\psi_v\kappa\omega}{k_1k_2DQ}.
\]
This is nonnegative and is positive exactly when the first-dose flow, second-dose flow, and transfer from \(V_2\) to \(R\) are all positive.

For local stability, the infection-free demographic block is Hurwitz: its \((S,V_1)\) subblock has negative trace and determinant \(D>0\), and its remaining eigenvalues are \(-k_4\) and \(-\mu\). The infected block has trace \(-(k_1+k_2)\) and determinant \(k_1k_2(1-\mathcal R_{\mathrm{tot}})\). This proves the stated sharp local threshold.

As an exact witness that even the restored 2024 expression can reverse classification, take \(\mu=\kappa=\omega_v=\psi_v=\phi=\gamma=\omega=1\), \(\phi_1=0\), and \(\beta=31/5\). Then \(\mathcal R_{\mathrm{tot}}=93/100<1\) but \(\mathcal R_D^{(24)}=31/30>1\).

## Verification
The bundled `verify.py` checks the equilibrium identities, the correct next-generation threshold, the exact relation \(\mathcal R_D^{(24)}=k_3\mathcal R_D^{(26)}\), the recovered-mass gap, time-unit scaling, and the rational stability-reversal witness using exact symbolic arithmetic. The local-stability conclusion is additionally justified by the block-triangular Jacobian argument above.

## Relationship to prior work
Din (2026) explicitly defines the six-class total population, prints equation (2.1) with standard incidence, and gives \(\mathcal R_D^{(26)}\) on p. 18719 while referring the detailed calculation to Farhan et al. (2024). Full-text inspection of Farhan et al. shows a numerator containing the additional factor \(k_3\), but its next-generation matrix uses \(S^*/(S^*+V_1^*+V_2^*)\), omitting \(R^*\) despite defining \(N\) as all six compartments. Hence the two papers expose a linked transcription-plus-normalization chain, but neither states the correction proved here.

Kuddus, Mohiuddin, and Rahman (2021) study double-dose measles vaccination with a recovered class, but their model uses a different constant-population, mass-action incidence law and a different threshold formula. It does not imply the present source-specific correction. Searches over source titles, formula aliases, dimensional-consistency phrasing, recovered-class normalization, and equivalent threshold statements found no covering result.

## Limitations
If incidence were intentionally normalized by a population excluding recovered individuals, the 2024 expression would describe a different model; that is not the model printed in either inspected source. The result establishes only the deterministic local disease-free threshold. Downstream stochastic and nonlinear global claims require separate rederivation and are not adjudicated here.

## References
1. A. Din, “Stochastic analysis and ANN-based approximation of measles transmission dynamics under Lévy noise,” *AIMS Mathematics* 11(6), 18715–18745 (2026), DOI 10.3934/math.2026761. See equation (2.1), Table 1, and the displayed \(\mathcal R_D\) on p. 18719.
2. M. Farhan, Z. Ling, S. Ullah, M. Alsubhi, M. Asiri, and M. B. Riaz, “A novel physics-informed neural network approach to assess the impact of double-dose vaccination on measles transmission,” *European Physical Journal Plus* 139, 1059 (2024), DOI 10.1140/epjp/s13360-024-05838-0. See the model, disease-free equilibrium, and next-generation calculation on pp. 3–5.
3. M. A. Kuddus, M. Mohiuddin, and A. Rahman, “Mathematical analysis of a measles transmission dynamics model in Bangladesh with double dose vaccination,” *Scientific Reports* 11, 16571 (2021), DOI 10.1038/s41598-021-95913-8.
