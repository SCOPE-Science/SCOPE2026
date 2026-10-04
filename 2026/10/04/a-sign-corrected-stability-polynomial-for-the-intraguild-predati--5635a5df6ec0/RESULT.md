# A sign-corrected stability polynomial for the intraguild-predation model
## Finding
For the dimensionless intraguild-predation model of Niu, Kang, Tao, and Wang, the characteristic polynomial written in Supplementary Eq. (S4) has all three non-leading signs reversed relative to the Jacobian entries defined immediately before it. With the paper's notation,
\[
\sigma_2=\operatorname{{tr}}J,\qquad
\sigma_1=-P_2(J),\qquad
\sigma_0=\det J,
\]
where \(P_2(J)\) is the sum of the three principal \(2\times2\) minors. Therefore
\[
\det(\lambda I-J)=\lambda^3-\sigma_2\lambda^2-\sigma_1\lambda-\sigma_0.
\]
The supplement instead writes all three signs as plus. The resulting stability test can reverse the classification of a biologically admissible coexistence equilibrium.

An exact witness is
\[
r=\frac83,\quad \alpha_1=\alpha_2=\alpha_3=\alpha_4=1,\quad
\omega_1=4,\quad \omega_2=\omega_3=1,\quad m_1=m_2=\frac56,
\]
with
\[
(R^*,C_1^*,C_2^*)=\left(\frac12,1,1\right).
\]
All parameters and state coordinates are positive. The three equilibrium residuals vanish exactly. The Jacobian is
\[
J=\begin{{pmatrix}}
-\frac89&-\frac13&-\frac13\\
\frac{16}{9}&\frac14&-\frac12\\
\frac49&\frac14&0
\end{{pmatrix}},
\]
and hence
\[
\det(\lambda I-J)=\lambda^3+\frac{23}{36}\lambda^2+\frac{139}{216}\lambda+\frac4{27}.
\]
The cubic Routh--Hurwitz inequalities hold because all three coefficients are positive and
\[
\frac{23}{36}\frac{139}{216}=\frac{3197}{7776}>\frac4{27}=\frac{1152}{7776}.
\]
Thus this coexistence equilibrium is locally asymptotically stable. By contrast, the supplement's definitions give
\[
(\sigma_2,\sigma_1,\sigma_0)=\left(-\frac{23}{36},-\frac{139}{216},-\frac4{27}\right),
\]
so its stated conditions requiring positive \(\sigma_0\) and \(\sigma_2\) reject this stable equilibrium.

## Assumptions and scope
The claim concerns the paper's dimensionless three-species ODE and the Jacobian convention \(J=[\partial g_i/\partial x_j]\) used in its supplement. It uses only positive model parameters and a positive coexistence equilibrium. No claim is made that the paper's numerically displayed homoclinic trajectory is absent; the correction is to the analytic characteristic-polynomial, Routh--Hurwitz, and downstream Cardano/Shilnikov criteria as written.

The earliest public version of the source is arXiv:2508.18038v1 from 2025-08-25. The current arXiv v2 contains the supplement used here, and the work was subsequently published as DOI 10.1088/1572-9494/ae4b18.

## Proof
For a general \(3\times3\) matrix \(J=[b_{{ij}}]\),
\[
\det(\lambda I-J)=\lambda^3-(\operatorname{{tr}}J)\lambda^2+P_2(J)\lambda-\det J,
\]
where
\[
P_2(J)=b_{{11}}b_{{22}}+b_{{11}}b_{{33}}+b_{{22}}b_{{33}}-b_{{12}}b_{{21}}-b_{{13}}b_{{31}}-b_{{23}}b_{{32}}.
\]
The source defines \(\sigma_2=\operatorname{{tr}}J\), its displayed \(\sigma_1\) is exactly \(-P_2(J)\), and its displayed \(\sigma_0\) is exactly \(\det J\). Substitution gives the corrected polynomial
\[
\lambda^3-\sigma_2\lambda^2-\sigma_1\lambda-\sigma_0.
\]
This is an identity, not a numerical inference.

For the witness parameters, the equilibrium equations reduce to
\[
\frac83\frac12\left(1-\frac12\right)-\frac{(1/2)\cdot1}{1+1/2}-\frac{(1/2)\cdot1}{1+1/2}=0,
\]
\[
4\frac{(1/2)\cdot1}{1+1/2}-\frac{1\cdot1}{1+1}-\frac56=0,
\]
and
\[
\frac{(1/2)\cdot1}{1+1/2}+\frac{1\cdot1}{1+1}-\frac56=0.
\]
Direct differentiation yields the displayed rational Jacobian. Its true characteristic polynomial follows from the determinant identity. The cubic Hurwitz criterion then proves local asymptotic stability exactly.

Writing the true polynomial as \(\lambda^3+a_1\lambda^2+a_2\lambda+a_3\), the source notation gives \(a_1=-\sigma_2\), \(a_2=-\sigma_1\), \(a_3=-\sigma_0\). Hence the correct source-notation Hurwitz conditions are
\[
\sigma_2<0,\qquad \sigma_1<0,\qquad \sigma_0<0,\qquad \sigma_1\sigma_2+\sigma_0>0.
\]
Because Supplementary Eqs. (S6)--(S10) are derived from the sign-reversed Eq. (S4), their \(p,q\), discriminant, and spectral inequality do not describe the eigenvalues of \(J\) without corresponding sign correction.

## Verification
The bundled `verifier.py` uses only `fractions.Fraction`. It verifies the equilibrium residuals, differentiates the model through the explicit Jacobian formulas, reproduces the source \(\sigma\)-definitions, reconstructs the true characteristic coefficients, and checks the exact Hurwitz inequalities. It also confirms that the source's stated supplement test rejects the witness while the corrected source-notation test accepts it.

The universal sign identity is proved symbolically above; the finite witness is used only to demonstrate that the sign error changes a stability conclusion inside the model's positive parameter/state region.

## Relationship to prior work
The source paper's main text states a cubic Routh--Hurwitz stability criterion for the coexistence equilibrium, while its supplement defines the Jacobian coefficients in Eqs. (S3)--(S5), asserts the sign-inconsistent polynomial in (S4), and builds its homoclinic spectral calculation on that polynomial. The same work is now published in *Communications in Theoretical Physics* under DOI 10.1088/1572-9494/ae4b18.

Targeted searches of published-finding corpus for the arXiv identifier, DOI, title, \(\sigma_0,\sigma_1,\sigma_2\), characteristic-polynomial signs, and the exact rational witness found no source-specific correction. The nearest returned results concern determinant-sign stability exchange in a different predator-dependent replicator model and a no-Hopf result for a serial AM2 model; neither implies this coefficient correction.

MSC2020 class 92D40 is the ecology class and matches the paper's intraguild-predation/ecological population-dynamics subject.

## Limitations
This result corrects the analytic local spectral framework as written. It does not establish or exclude a global homoclinic connection for any of the paper's numerical parameter sets, does not recompute its Lyapunov exponents, and does not assess the field-data fit. A future erratum or publisher-side supplement not present in the inspected arXiv v2 could supersede the correction.

## References
1. Y. Niu, J. Kang, W. Tao, X. Wang, *A homoclinic route to chaos in omnivore communities*, arXiv:2508.18038v2; published in *Communications in Theoretical Physics* 78 (2026), 065601, DOI 10.1088/1572-9494/ae4b18.
2. AMS Mathematical Reviews / zbMATH, MSC2020, class 92D40: Ecology.
