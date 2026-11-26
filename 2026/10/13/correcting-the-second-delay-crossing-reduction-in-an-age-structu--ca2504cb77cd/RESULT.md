# Correcting the second-delay crossing reduction in an age-structured predator-prey model

## Finding
For the characteristic equation in Li, Liu and Cai (2026),
\[
g(\zeta)=\zeta^2+A_1\zeta+B_1+(C_1+D_1\zeta)e^{-\zeta\tau_1}
+(L_1+Q_1\zeta)e^{-\zeta\tau_2}+H_1e^{-\zeta(\tau_1+\tau_2)},
\]
the displayed second-delay reduction is inconsistent with the characteristic equation. For real coefficients, \(\omega>0\) and \(\theta=\omega\tau_2\), the exact equation for the projection of the imaginary-root locus onto \(\tau_2\) (allowing \(\tau_1\) to vary) is
\[
K_2=2U_2\cos\theta-2V_2\sin\theta,
\]
where
\[
\begin{aligned}
K_2&=\omega^4+(A_1^2-2B_1-D_1^2+Q_1^2)\omega^2+B_1^2+L_1^2-C_1^2-H_1^2,\\
U_2&=(L_1-A_1Q_1)\omega^2+H_1C_1-B_1L_1,\\
V_2&=-Q_1\omega^3+(B_1Q_1-A_1L_1+D_1H_1)\omega.
\end{aligned}
\]
Let \(R_2=\sqrt{U_2^2+V_2^2}\). When \(R_2>0\), there are admissible phases exactly when \(|K_2|\le 2R_2\). With \(\phi_2=\arg(U_2+iV_2)\) and \(\psi_2=\arccos(K_2/(2R_2))\), the candidates are
\[
\tau_{2,n}^{\pm}=\frac{\pm\psi_2-\phi_2+2n\pi}{\omega},\qquad n\in\mathbb Z,
\]
retaining the nonnegative values. When \(R_2=0\), no \(\tau_2\) is admissible if \(K_2\ne 0\); every nonnegative \(\tau_2\) is admissible if \(K_2=0\).

Equation (3.11) in the source reverses the signs of \(D_1^2\) and \(Q_1^2\) in the coefficient of \(\omega^2\). The accompanying formulas use \(V_{2,\mathrm{printed}}=Q_1\omega^3-(B_1Q_1+A_1L_1)\omega-D_1H_1\) (as in (3.12)) and \(\arg(U_2+iU_2)\) instead of the two-component phase. With the source's rounded coefficients at \(\omega=1.4\), the corrected ratio \(K_2/(2R_2)\) is approximately \(0.8738119006\), whereas using the printed \(K_2,V_2\) in its cosine admissibility test gives approximately \(1.242308499\). The printed test would reject a frequency in the source's own reported interval \(\Omega=[1.015,1.838]\).

## Assumptions and scope
The algebra is exact for real coefficients and \(\omega>0\). Both delays may vary over the nonnegative reals. The numerical example treats the source's decimals as given and makes no assertion about undocumented plotting code. Admissibility means that \(i\omega\) is a root for at least one \(\tau_1\) at the specified \(\tau_2\); it is not a transversality or Hopf conclusion.

## Proof
Put \(a=B_1-\omega^2+iA_1\omega\), \(b=L_1+iQ_1\omega\), \(c=C_1+iD_1\omega\), \(z=e^{-i\theta}\), and \(v=e^{-i\omega\tau_1}\). The root equation is \(a+bz+(c+H_1 z)v=0\). Since \(\omega>0\), varying \(\tau_1\) over the nonnegative reals allows every unit complex \(v\). If \(c+H_1z\ne0\), the necessary modulus equality \(|a+bz|=|c+H_1z|\) is sufficient: take \(v=-(a+bz)/(c+H_1z)\) and choose a nonnegative delay representative. If \(c+H_1z=0\), the equality forces \(a+bz=0\), and any \(\tau_1\) works. Unequal moduli cannot give a root.

The difference of the squared moduli is
\[
|a|^2+|b|^2-|c|^2-H_1^2+2\operatorname{Re}\big((a\overline b-cH_1)e^{i\theta}\big).
\]
Its constant term is \(K_2\) and \(a\overline b-cH_1=-U_2-iV_2\), yielding the stated projection equation. For \(R_2>0\) the right-hand side is \(2R_2\cos(\theta+\phi_2)\); the two branches follow and can coincide modulo \(2\pi\) at \(|K_2|=2R_2\). The printed phase cannot encode both components unless \(V_2=U_2\) with a defined phase. For \(R_2=0\) the right-hand side is identically zero, giving the two cases without taking a quotient or an argument of zero. For example, at \(\omega=1\) with \((A_1,B_1,C_1,D_1,L_1,Q_1,H_1)=(1,2,1,1,1,0,1)\), \(a=c=1+i\) and \(b=H_1=1\), so \(K_2=R_2=0\) and \(\tau_1=\pi\) gives a root for any \(\tau_2\).

## Verification
The bundled `verification/verify.py` evaluates the expanded identity against the direct complex-modulus expression at several angles for the numerical parameters and reproduces the contrasting admissibility tests. The inputs are \((A_1,B_1,C_1,D_1,L_1,Q_1,H_1)=(0.4006,-0.3195,0.3595,-0.9,2.1616,0.3624,-0.3262)\), as listed on p. 7007 of the source. One can also check the inequalities without square roots: for these decimals at \(\omega=7/5\), \(K_2,K_{2,\mathrm{printed}}>0\) and
\[
4(U_2^2+V_2^2)-K_2^2=\frac{71862999944771469}{3125000000000000}>0,\qquad
4(U_2^2+V_{2,\mathrm{printed}}^2)-K_{2,\mathrm{printed}}^2
=-\frac{17490708357457863591}{390625000000000000}<0.
\]
The all-coefficient statement follows from the algebra above, not from the numerical witness.

## Relationship to prior work and limitations
Lin and Wang (2012, p. 524, Eqs. (14)–(15)) give the generic two-delay crossing construction with both trigonometric components; it specializes to the regular-case formulas above. It is the model-specific coefficient correction and the separating test against the printed formulas in Li, Liu and Cai that are at issue here, not the generic amplitude–phase method. No full stability-region, crossing-direction, Hopf-criticality, or periodic-orbit computation is claimed; in particular this does not show that the paper's figure was produced with the erroneous expressions.

## References
1. W. Li, D. Liu, Y. Cai, “Hopf bifurcation of predator-prey model with age structure,” AIMS Mathematics 11 (2026), 6989–7014. DOI: 10.3934/math.2026287. [Publisher PDF](https://www.aimspress.com/aimspress-data/math/2026/3/PDF/math-11-03-287.pdf).
2. X. Lin, H. Wang, “Stability analysis of delay differential equations with two discrete delays,” Canadian Applied Mathematics Quarterly 20 (2012), 519–533. [Author-hosted PDF](https://www.math.ualberta.ca/~hwang/TwoDelayCAMQ.pdf).
