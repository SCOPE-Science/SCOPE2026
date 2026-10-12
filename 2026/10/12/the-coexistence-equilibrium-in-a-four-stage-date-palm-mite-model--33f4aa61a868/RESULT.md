# The coexistence equilibrium in a four-stage date-palm-mite model is always locally stable above threshold
## Finding
Consider
\[
\dot E=\frac{\beta A}{1+(A+N+L)/K}-\alpha_1E,\qquad
\dot L=\gamma_EE-\alpha_2L,
\]
\[
\dot N=\gamma_LL-\alpha_3N,\qquad
\dot A=\gamma_NN-\alpha_4A,
\]
with
\[
\alpha_1=\gamma_E+\mu_E,\quad
\alpha_2=\gamma_L+\mu_L,\quad
\alpha_3=\gamma_N+\mu_N,\quad
\alpha_4=\mu_A,
\]
and all parameters positive. The source derives
\[
\mathcal R_0=
\frac{\beta\gamma_E\gamma_L\gamma_N}
{\alpha_1\alpha_2\alpha_3\alpha_4}
\]
and a unique positive equilibrium for \(\mathcal R_0>1\), but states local stability only if
\[
\Delta_3=\eta_1\eta_2\eta_3-\eta_3^2-\eta_1^2\eta_4>0.
\]

That condition is automatic. Hence \(P^*\) is locally asymptotically stable for every positive parameter vector with \(\mathcal R_0>1\). In particular, the positive equilibrium cannot undergo a Hopf loss of stability anywhere inside the coexistence region.

## Assumptions and scope
The result concerns the uncontrolled four-stage ODE printed in the motivating article. All transition, mortality, oviposition, and carrying-capacity parameters are strictly positive.

The source gives
\[
A^*=\frac{K(\mathcal R_0-1)}{1+C_L+C_N},
\quad
C_L=\frac{\alpha_3\alpha_4}{\gamma_L\gamma_N},
\quad
C_N=\frac{\alpha_4}{\gamma_N},
\]
and defines
\[
b=\frac{\beta A^*}{K\mathcal R_0^2}.
\]
These identities are used exactly below.

This is a local spectral result. It does not prove global convergence and does not remove the extra sufficient inequalities in the source's Li-Muldowney global theorem.

## Proof
Let \(e_j\) be the elementary symmetric polynomials in
\[
\alpha_1,\alpha_2,\alpha_3,\alpha_4.
\]
Then
\[
\prod_{j=1}^4(\lambda+\alpha_j)
=\lambda^4+e_1\lambda^3+e_2\lambda^2+e_3\lambda+e_4.
\]

The source's characteristic coefficients at \(P^*\) are
\[
\eta_1=e_1,\qquad
\eta_2=e_2+b\gamma_E,
\]
\[
\eta_3=e_3+b\gamma_E(\alpha_3+\alpha_4+\gamma_L),
\]
and
\[
\eta_4=b\gamma_E
\left[\gamma_L\gamma_N+\alpha_4(\alpha_3+\gamma_L)\right].
\]
Put
\[
B=b\gamma_E,\quad
c=\alpha_3+\alpha_4+\gamma_L,\quad
D=\gamma_L\gamma_N+\alpha_4(\alpha_3+\gamma_L).
\]
All are positive.

Since
\[
1+C_L+C_N=\frac{D}{\gamma_L\gamma_N}
\]
and
\[
\frac{\beta}{\mathcal R_0}
=\frac{e_4}{\gamma_E\gamma_L\gamma_N},
\]
the explicit equilibrium gives
\[
b=
\frac{e_4}{\gamma_E D}
\frac{\mathcal R_0-1}{\mathcal R_0}.
\]
Therefore, with
\[
t=\frac{\mathcal R_0-1}{\mathcal R_0}\in(0,1),
\]
we have
\[
\eta_1=e_1,\qquad
\eta_2=e_2+B,\qquad
\eta_3=e_3+Bc,\qquad
\eta_4=BD=t e_4.
\]

Expanding the Liénard-Chipart determinant,
\[
\begin{aligned}
\Delta_3
={}&e_1(e_2+B)(e_3+Bc)-(e_3+Bc)^2-e_1^2te_4\\
={}&(e_1e_2e_3-e_3^2-e_1^2e_4)
+e_1^2(1-t)e_4\\
&+B\left[c(e_1e_2-2e_3)+e_1e_3\right]
+B^2c(e_1-c).
\end{aligned}
\]

The first bracket is strictly positive because it is the third Hurwitz determinant of
\[
\prod_{j=1}^4(\lambda+\alpha_j),
\]
whose roots are the strictly negative numbers \(-\alpha_j\). The second term is positive because \(0<t<1\).

Also
\[
e_1e_2
=
3e_3+\sum_{i<j}\alpha_i\alpha_j(\alpha_i+\alpha_j)>3e_3,
\]
so
\[
c(e_1e_2-2e_3)+e_1e_3>ce_3+e_1e_3>0.
\]
Finally,
\[
e_1-c=\alpha_1+\alpha_2-\gamma_L=\alpha_1+\mu_L>0.
\]
Thus every displayed contribution is strictly positive and \(\Delta_3>0\) throughout \(\mathcal R_0>1\). With the source's already-established positivity of \(\eta_1,\eta_2,\eta_3,\eta_4\), the quartic Liénard-Chipart criterion proves local asymptotic stability.

## Verification
The bundled `verification/verify.py` reconstructs the coefficient reduction, checks
\[
BD=t e_4,
\]
and compares the direct and expanded formulas for \(\Delta_3\) on several deterministic positive parameter sets. It also checks every sign inequality used in the proof. The computation is supplementary; the theorem itself is analytic.

## Relationship to prior work
The motivating article derives the exact equilibrium and quartic coefficients, but its Theorem 9 leaves local stability conditional on \(\Delta_3>0\). Its numerical coexistence example evaluates that determinant only at one parameter vector.

Xing, Liu, and Guo (2019) study a different four-stage mosquito model in discrete time with stage-specific Beverton-Holt or Ricker survivorship. Its stability problem is a unit-disk problem for a discrete characteristic equation; under Ricker nonlinearities the paper also exhibits oscillatory and chaotic regimes. It does not imply the continuous-time determinant identity here.

Zhang and Zhao (2025) study a different two-state reaction-diffusion single-species model with Beverton-Holt birth. Their comparison and PDE arguments do not contain the four-stage date-palm-mite Jacobian or the identity above.

## Limitations
The theorem is local. The source's global coexistence theorem uses persistence and a Li-Muldowney compound-matrix criterion with additional sufficient inequalities, which are not removed here.

The result excludes a Hopf loss of stability of \(P^*\) in the printed model, but it does not by itself exclude other global invariant sets coexisting with a locally stable equilibrium.

Changing the recruitment law, adding delays, making transition rates state-dependent, or passing to discrete time can invalidate the determinant decomposition.

## References
1. S. F. Aljurbua, M. El-Shahed, “Cost-effective strategies for controlling date palm mite infestations: an optimal control approach,” AIMS Mathematics 11 (2026), 26359–26396. DOI: 10.3934/math.20261058.
2. Y. Xing, J. Liu, Z. Guo, “A discrete-time mathematical model of stage-structured mosquito populations,” Advances in Difference Equations 2019 (2019), 518. DOI: 10.1186/s13662-019-2449-x.
3. H. Zhang, J. Zhao, “Global stability of stage-structured single species model on \(\mathbb R^N\) with Beverton-Holt birth function,” Applied Mathematics in Science and Engineering 33 (2025). DOI: 10.1080/27690911.2025.2551358.
