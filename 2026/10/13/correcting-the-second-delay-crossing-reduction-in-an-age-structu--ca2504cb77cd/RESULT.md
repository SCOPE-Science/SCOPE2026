# Correcting the second-delay crossing reduction in an age-structured predator-prey model
## Finding
For the source characteristic equation
\[
g(\zeta)=\zeta^2+A_1\zeta+B_1+(C_1+D_1\zeta)e^{-\zeta\tau_1}
 +(L_1+Q_1\zeta)e^{-\zeta\tau_2}+H_1e^{-\zeta(\tau_1+\tau_2)},
\]
the second-delay phase reduction printed in Li, Liu and Cai (2026) is algebraically inconsistent.

Set \(\zeta=i\omega\) and \(\theta=\omega\tau_2\). Equality of the relevant moduli gives
\[
K_2(\omega)=2U_2(\omega)\cos\theta-2V_2(\omega)\sin\theta,
\]
with
\[
K_2(\omega)=\omega^4+(A_1^2-2B_1-D_1^2+Q_1^2)\omega^2+B_1^2+L_1^2-C_1^2-H_1^2,
\]
\[
U_2(\omega)=(L_1-A_1Q_1)\omega^2+H_1C_1-B_1L_1,
\]
\[
V_2(\omega)=-Q_1\omega^3+(B_1Q_1-A_1L_1+D_1H_1)\omega.
\]
Hence
\[
\phi_2(\omega)=\arg\!\bigl(U_2(\omega)+iV_2(\omega)\bigr)
\]
and
\[
\tau_{2,n}^{\pm}(\omega)=
\frac{\pm\psi_2(\omega)-\phi_2(\omega)+2n\pi}{\omega},
\qquad
\cos\psi_2(\omega)=\frac{K_2(\omega)}{2\sqrt{U_2(\omega)^2+V_2(\omega)^2}}.
\]

The printed equation (3.11) reverses the \(D_1^2\) and \(Q_1^2\) signs in the quadratic coefficient, prints an incompatible \(V_2\), and then defines \(\phi_2=\arg(U_2+iU_2)\). At the source's own rounded coefficients and \(\omega=1.4\), the corrected cosine ratio is approximately \(0.8738119006\), whereas the printed construction gives approximately \(1.242308499\). The latter would reject a frequency that the paper itself reports inside \(\Omega=[1.015,1.838]\).

## Assumptions and scope
The coefficients are real and \(\omega>0\). The result corrects the analytic second-delay crossing reduction only. The numerical witness uses the coefficients rounded in the source; the symbolic identity is exact.

No claim is made that the paper's plotted crossing curves were generated from the erroneous displayed formulas. Undocumented numerical code could have used corrected expressions.

## Proof
Let
\[
a=B_1-\omega^2+iA_1\omega,\qquad b=L_1+iQ_1\omega,\qquad c=C_1+iD_1\omega.
\]
The relevant modulus equality is
\[
|a+be^{-i\theta}|^2=|c+H_1e^{-i\theta}|^2.
\]
Expanding gives
\[
|a|^2+|b|^2-|c|^2-H_1^2
+2\operatorname{Re}\!\left((a\overline b-cH_1)e^{i\theta}\right)=0.
\]
The constant term is exactly \(K_2\). Moreover,
\[
\operatorname{Re}(a\overline b-cH_1)=-U_2
\]
and
\[
\operatorname{Im}(a\overline b-cH_1)=-V_2.
\]
Therefore
\[
K_2-2U_2\cos\theta+2V_2\sin\theta=0.
\]
Writing \(R_2=\sqrt{U_2^2+V_2^2}\) and \(\phi_2=\arg(U_2+iV_2)\) gives
\[
U_2=R_2\cos\phi_2,\qquad V_2=R_2\sin\phi_2,
\]
so
\[
K_2=2R_2\cos(\phi_2+\theta),
\]
which yields the corrected crossing branches.

The printed phase \(\arg(U_2+iU_2)\) would force the sine component to equal \(U_2\), not \(V_2\), so it cannot represent the preceding identity unless \(V_2=U_2\) accidentally.

## Verification
The bundled `verification/verify.py` checks the exact complex-modulus identity at several angles for the source's numerical coefficients. It also reproduces the \(\omega=1.4\) witness: the corrected ratio lies strictly inside \([-1,1]\), while the printed ratio exceeds \(1\).

The proof is symbolic; the numerical check is supplementary.

## Relationship to prior work
Li, Liu and Cai derive the two-delay characteristic equation and use the crossing-curve method to describe stability switches. Their equations (3.11)--(3.13) are the exact location of the inconsistency corrected here.

Lin and Wang (2012), cited by the source, give the generic two-delay crossing construction. Their phase compression uses both trigonometric components through an amplitude of the form \(\sqrt{A_2^2+B_2^2}\) and a phase whose cosine and sine components are \(A_2\) and \(B_2\). That general method supports the corrected structure but does not identify this 2026 source's coefficient errors.

Targeted DOI, title, formula, crossing-curve, and erratum searches found no matching published correction.

## Limitations
The finding does not recompute the full two-delay stability region, crossing directions, Hopf criticality, or nonlinear periodic-orbit stability.

The inspected supplementary excerpt does not provide the code used for the crossing-curve figure, so the result does not assert that Figure 4 itself is wrong. It establishes that equations (3.11)--(3.13) do not justify the crossing construction exactly as printed.

## References
1. W. Li, D. Liu, Y. Cai, “Hopf bifurcation of predator-prey model with age structure,” AIMS Mathematics 11 (2026), 6989–7014. DOI: 10.3934/math.2026287.
2. X. Lin, H. Wang, “Stability analysis of delay differential equations with two discrete delays,” Canadian Applied Mathematics Quarterly 20 (2012), 519–533.
