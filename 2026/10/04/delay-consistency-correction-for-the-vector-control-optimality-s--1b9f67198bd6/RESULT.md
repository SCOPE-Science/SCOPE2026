# Delay consistency correction for the vector-control optimality system
## Finding
Hu and Nie's controlled vector-borne disease model contains the delayed vector-incidence term
\[
F_5(t)=(1-u_2(t))\beta_{hv}e^{-\mu_v\tau}I_h(t-\tau)S_v(t-\tau).
\]
For a positive delay \(\tau\), the first variation printed in their Eq. (26) and the delayed contributions propagated into the adjoint and control formulas are not the first variation of this term. The exact variation is
\[
\delta F_5(t)=\beta_{hv}e^{-\mu_v\tau}\left[(1-u_2(t))\left(\widetilde I_h(t-\tau)S_v(t-\tau)+I_h(t-\tau)\widetilde S_v(t-\tau)\right)-\rho_2(t)I_h(t-\tau)S_v(t-\tau)\right].
\]
Thus the vector-control gradient and the advanced adjoint terms must retain both the vector-survival factor and the correct delayed/advanced time arguments. Theorem 9 as printed therefore does not characterize first-order optimality for the stated delayed control system when \(\tau>0\) in general.

## Assumptions and scope
The claim concerns exactly the control system displayed as Eq. (23) in the 2026 article, on a finite horizon \([0,T]\), with \(\tau>0\), and with perturbations \(u_2^\varepsilon=u_2+\varepsilon\rho_2\), \(I_h^\varepsilon=I_h+\varepsilon\widetilde I_h+o(\varepsilon)\), and \(S_v^\varepsilon=S_v+\varepsilon\widetilde S_v+o(\varepsilon)\). The coefficients \(\beta_{hv}>0\) and \(\mu_v>0\) are those of the source model. No smoothness beyond that needed for the displayed Gâteaux calculation is used.

The result is a correction to the delay-dependent first-order system. It does not challenge the paper's uncontrolled reproduction number or steady-state stability results, and it does not prove or disprove existence or uniqueness of an optimizer after the optimality system is corrected.

## Proof
Define
\[
F_5^\varepsilon(t)=(1-u_2(t)-\varepsilon\rho_2(t))\beta_{hv}e^{-\mu_v\tau}\bigl(I_h(t-\tau)+\varepsilon\widetilde I_h(t-\tau)\bigr)\bigl(S_v(t-\tau)+\varepsilon\widetilde S_v(t-\tau)\bigr).
\]
Expanding and taking the coefficient of \(\varepsilon\) gives
\[
\left.\frac{d}{d\varepsilon}F_5^\varepsilon(t)\right|_{\varepsilon=0}
=\beta_{hv}e^{-\mu_v\tau}\left[(1-u_2(t))\left(\widetilde I_h(t-\tau)S_v(t-\tau)+I_h(t-\tau)\widetilde S_v(t-\tau)\right)-\rho_2(t)I_h(t-\tau)S_v(t-\tau)\right].
\]
This identity is algebraic. In contrast, the source's fifth variation equation drops \(e^{-\mu_v\tau}\), repeats the \(\widetilde I_h\) contribution where an \(\widetilde S_v\) contribution is required, and places the \(\rho_2\) contribution at current rather than delayed state values.

The control derivative is already enough to correct the \(u_2\) stationarity term. With the source's Lagrange-multiplier sign convention, the contribution from the fifth state equation to the coefficient of \(\rho_2(t)\) is
\[
+\lambda_5(t)\beta_{hv}e^{-\mu_v\tau}I_h(t-\tau)S_v(t-\tau).
\]
Solving the stationarity equation for the unconstrained control therefore places
\[
-\lambda_5(t)\beta_{hv}e^{-\mu_v\tau}I_h(t-\tau)S_v(t-\tau)
\]
in the numerator of the source's \(\widetilde u_2(t)\), replacing its current-state term without the survival factor.

The state-dependent delayed terms give the adjoint correction by a change of variables. For example,
\[
\int_0^T \lambda_5(s)(1-u_2(s))\beta_{hv}e^{-\mu_v\tau}S_v(s-\tau)\widetilde I_h(s-\tau)\,ds
\]
becomes, with \(t=s-\tau\),
\[
\int_0^{T-\tau}\lambda_5(t+\tau)(1-u_2(t+\tau))\beta_{hv}e^{-\mu_v\tau}S_v(t)\widetilde I_h(t)\,dt.
\]
Hence the advanced \(I_h\)-adjoint coefficient is
\[
\chi_{[0,T-\tau]}(t)\lambda_5(t+\tau)(1-u_2(t+\tau))\beta_{hv}e^{-\mu_v\tau}S_v(t).
\]
The same calculation with \(\widetilde S_v\) gives the corresponding coefficient with \(I_h(t)\). These expressions differ structurally from the printed advanced terms, which use \(u_2(t)\), backward-shifted state factors, and no survival factor. Therefore the printed adjoint/control system cannot be the first-order optimality system of Eq. (23) for a general positive delay.

## Verification
The primary article's full-text control section was checked at Eqs. (23), (26), (32), and (35). Eq. (23) contains the factor \(e^{-\mu_v\tau}I_h(t-\tau)S_v(t-\tau)\); the subsequent first-variation equation omits the factor and misplaces the delayed arguments. The packaged `verifier.py` expands the perturbed delayed incidence in a formal polynomial ring over exact rational coefficients and checks the coefficient of \(\varepsilon\) against the displayed corrected formula. The universal claim follows from the symbolic expansion and the change of variables above, not from numerical sampling.

## Relationship to prior work
The motivating source was published on 27 January 2026 and lists Mathematics Subject Classification 92B05 and 92D30. Its control section explicitly presents the hybrid ODE/PDE/DDE optimality derivation as a central contribution. Exact-title, DOI, delay-adjoint, and vector-control-gradient searches located no correction or erratum of the stated formulas.

A closely related delayed biological-control paper by Liao, Gao, Yan, and Zhou (2021), DOI 10.3934/mbe.2021209, applies Pontryagin's principle to a different delayed Huanglongbing model. It confirms that delayed biological optimal-control systems are an established object of study but does not contain the Hu-Nie state equations or imply the source-specific correction above. The 2023 multi-class-age vector-borne predecessor by Liang, Wang, Hu, and Nie, DOI 10.1142/S0218339023500109, uses a different class-age structure and does not cover the discrete vector incubation term corrected here.

## Limitations
Only the delay-generated pieces of the Gâteaux linearization, adjoint equations, and \(u_2\) stationarity formula are claimed here. Other printed terms were not rederived exhaustively. The result does not establish the corrected optimizer, uniqueness of a corrected fixed point, or the quantitative difference between corrected and published numerical intervention trajectories. A differently titled earlier public version of the 2026 article was not found in the checked searches; 27 January 2026 is the earliest verified public date used here.

## References
1. L. Hu and L. Nie, “Global dynamics and optimal control of a vector-borne disease model with class-age structured incubation and discrete incubation, and multiple transmission pathways,” *Advances in Continuous and Discrete Models* 2026, article 20 (2026). DOI 10.1186/s13662-026-04062-7.
2. Z. Liao, S. Gao, S. Yan, and G. Zhou, “Transmission dynamics and optimal control of a Huanglongbing model with time delay,” *Mathematical Biosciences and Engineering* 18 (2021), 4162–4192. DOI 10.3934/mbe.2021209.
3. S. Liang, S. Wang, L. Hu, and L. Nie, “Global dynamics and optimal control for a vector-borne epidemic model with multi-class-age structure and horizontal transmission,” *Journal of Biological Systems* 31 (2023), 375–416. DOI 10.1142/S0218339023500109.
