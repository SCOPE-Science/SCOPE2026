# Corrected endemic-equilibrium coordinates for an NPI-compliance mpox model
## Finding
For the mpox transmission model introduced by Alqahtani, Musa, and Inc, the endemic state printed as Eq. (7) is not a stationary point of the printed ODE when the compliance-transfer rate is positive. The first model equation is
\[
\dot S_n=(1-\rho)\pi-\lambda S_n-(\theta+\mu)S_n.
\]
Eq. (7) instead prints
\[
S_n^{\mathrm{pub}}=\frac{(1-\rho)\pi}{\lambda^*+\mu}.
\]
Substitution gives the exact residual
\[
(1-\rho)\pi-(\lambda^*+\theta+\mu)S_n^{\mathrm{pub}}
=-\frac{(1-\rho)\pi\theta}{\lambda^*+\mu},
\]
which is strictly negative for \(\pi>0\), \(\theta>0\), \(0\le\rho<1\), and \(\lambda^*>0\). Therefore the displayed endemic vector in Eq. (7) is not an equilibrium in that parameter regime.

Conditional on a positive scalar \(\lambda^*\), the corrected stationary coordinates are
\[
S_n^*=\frac{(1-\rho)\pi}{\lambda^*+\theta+\mu},\qquad
S_y^*=\frac{\pi(\rho\lambda^*+\theta+\rho\mu)}{(\varepsilon\lambda^*+\mu)(\lambda^*+\theta+\mu)},
\]
\[
E^*=\frac{\lambda^*\pi[\varepsilon\lambda^*+\varepsilon\theta+\mu(1-\rho+\varepsilon\rho)]}{A_1(\lambda^*+\theta+\mu)(\varepsilon\lambda^*+\mu)},
\]
where \(A_1=\sigma_n+\sigma_y+\mu\), and
\[
I_n^*=\frac{\sigma_nE^*}{A_2},\quad
I_y^*=\frac{\sigma_yE^*+\eta I_n^*}{A_3},\quad
J^*=\frac{\gamma_nI_n^*+\gamma_yI_y^*}{A_4},\quad
R^*=\frac{\tau_nI_n^*+\tau_yI_y^*+\tau_JJ^*}{\mu},
\]
with \(A_2=\eta+\gamma_n+\tau_n+\delta_n+\mu\), \(A_3=\gamma_y+\tau_y+\delta_y+\mu\), and \(A_4=\tau_J+\delta_J+\mu\).

## Assumptions and scope
All demographic and transition parameters in denominators are positive, \(0\le\rho<1\), and the claim concerns a putative endemic state with \(\lambda^*>0\). The corrected formulas above solve the seven stationary compartment equations after treating \(\lambda^*\) as a scalar parameter. They do not by themselves solve the nonlinear consistency equation
\[
\lambda^*=\frac{\beta(I_n^*+\alpha I_y^*)}{N^*},\qquad
N^*=S_n^*+S_y^*+E^*+I_n^*+I_y^*+J^*+R^*.
\]
Accordingly, existence, uniqueness, backward/forward bifurcation structure, and stability of a corrected endemic equilibrium are outside the claim.

## Proof
Setting the first stationary equation to zero immediately gives
\[
S_n^*=\frac{(1-\rho)\pi}{\lambda^*+\theta+\mu}.
\]
Setting the second to zero and substituting this expression gives the stated \(S_y^*\). The exposed-class equation is linear in \(E\), so substitution of \(S_n^*\) and \(S_y^*\) yields the displayed \(E^*\). The four downstream equations are triangular and give \(I_n^*,I_y^*,J^*,R^*\) successively. Direct symbolic substitution makes every one of the seven compartment residuals identically zero.

By contrast, substituting the source's printed \(S_n^{\mathrm{pub}}\) into the first stationary equation yields exactly
\[
-\frac{(1-\rho)\pi\theta}{\lambda^*+\mu},
\]
so no choice of the other six coordinates can repair the printed vector when \(\theta>0\) and \(\rho<1\).

## Verification
The companion `verify.py` reconstructs the stationary equations symbolically. It checks the nonzero residual of the printed first coordinate and verifies exact zero residuals for all seven corrected coordinates. Its output is stored in `verification_output.txt` and is `VERIFY_OK`.

A separate source-level consistency check was made against Appendix A of the same article: the Lyapunov calculation rewrites the first susceptible inflow using the stationarity relation \((1-\rho)\pi=(\lambda^*+\theta+\mu)S_n^*\), i.e. the relation implied by the ODE rather than by Eq. (7). This confirms that the missing \(\theta\) in the printed equilibrium is not a competing model convention.

## Relationship to prior work
The introducing article explicitly analyzes equilibria, local/global stability, and bifurcation for this model. The corrected statement is not implied by the paper because its displayed endemic coordinates omit \(\theta\) from the first denominator and propagate that choice into later coordinates. Targeted searches by DOI, exact title, endemic-equilibrium terminology, compliance-transfer terminology, and correction/erratum terminology located the original article and related mpox models but no published correction or equivalent formula. Searches of prior stored results likewise found no same-model correction.

The closest database results concern other epidemic systems, including a coupled-SEIR reproduction-number result and a threshold-controlled dengue switching result; neither contains this seven-compartment stationary solve or implies the residual above.

## Limitations
The result corrects the printed equilibrium coordinates only. It does not prove that the corrected scalar consistency equation has a positive solution, does not determine how many such solutions exist, and does not re-establish the article's local or global stability theorems or its bifurcation classification. Literature searches cannot exclude an unindexed correction or private communication. No claim is made about empirical calibration or intervention effectiveness.

## References
1. R. T. Alqahtani, S. S. Musa, and M. Inc, “Modeling the role of public health intervention measures in halting the transmission of monkeypox virus,” *AIMS Mathematics* 8(6) (2023), 14142–14166, DOI 10.3934/math.2023723. Model Eq. (1), endemic coordinates Eq. (7), and Appendix A were inspected. Published 17 April 2023.
