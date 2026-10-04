# The printed fractional prostate-cancer scheme numerically slaves PSA to androgen

## Finding

The six-state prostate-cancer model distinguishes serum androgen from serum prostate-specific antigen (PSA). In the source notation, their right-hand sides are
\[
H_5
=
\gamma_1(a_0-A)-\gamma_1a_0u(t)
\]
and
\[
H_6
=
\sigma_0(X_1+X_2)
+\sigma_1X_1\frac{Q_1^m}{Q_1^m+\varpi_1^m}
+\sigma_2X_2\frac{Q_2^m}{Q_2^m+\varpi_2^m}
-\delta_3P.
\]

The final numerical recurrences printed in equation (33), however, use \(H_5\) for both variables. The androgen update has the form
\[
A_{n+1}=A_0+\mathcal N_n[H_5],
\]
and the printed PSA update has the same form
\[
P_{n+1}=P_0+\mathcal N_n[H_5],
\]
where \(\mathcal N_n\) denotes the identical local-plus-history operator displayed in the paper.

Subtracting the two recurrences gives the exact invariant
\[
P_{n+1}-A_{n+1}=P_0-A_0
\]
at every step. Hence, as written,
\[
P_n-A_n=P_0-A_0
\]
throughout the numerical trajectory.

This invariant is absent from the stated biological model. For the source's integer-order case \(\alpha=1\), choose
\[
X_1=X_2=0,\qquad
A=a_0=10,\qquad
P=1,\qquad
u=0,
\]
with positive cell quotas. Table 1 gives
\[
\gamma_1=0.08,\qquad
\delta_3=0.08.
\]
Therefore
\[
H_5=0
\]
but
\[
H_6=-0.08.
\]
The differential model consequently satisfies
\[
\frac{d}{dt}(P-A)=-0.08
\]
at this state, contradicting the discrete invariant imposed by the printed update.

The componentwise correction is direct: the PSA recurrence must use \(H_6\), not \(H_5\), in its local term and every history term.

## Assumptions and scope

The claim concerns the mathematical scheme printed in Section 5 of the cited article and the six-component model printed earlier in the same article.

The state used for the exact consistency witness is admissible under the source's nonnegative-population formulation. The cell quotas are taken positive so that no division by zero is introduced elsewhere in the model.

The proof does not assume a particular fractional history weight. The discrete invariant follows solely because the published androgen and PSA recurrences have identical increment expressions.

The article does not provide the simulation source code. Therefore this finding does not assert that the implementation used to draw the figures necessarily duplicated \(H_5\). The implementation may have contained the componentwise \(H_6\) correction even though the published recurrence does not.

## Proof

Let
\[
\mathcal N_n[G]
\]
denote the complete increment functional in equation (33): its local Atangana-Baleanu term plus the displayed weighted two-step history sum, evaluated with a component right-hand side \(G\).

The printed androgen recurrence is
\[
A_{n+1}=A_0+\mathcal N_n[H_5].
\]
Immediately below it, the printed PSA recurrence is
\[
P_{n+1}=P_0+\mathcal N_n[H_5].
\]
The right-hand sides differ only in their initial constants. Subtraction therefore gives
\[
P_{n+1}-A_{n+1}=P_0-A_0.
\]
No approximation is used in this deduction.

By contrast, the model equations define a distinct PSA field \(H_6\). At
\[
X_1=X_2=0,\qquad A=a_0,\qquad P=1,\qquad u=0,
\]
the androgen field vanishes:
\[
H_5
=
\gamma_1(a_0-a_0)-\gamma_1a_0\cdot0
=
0.
\]
All PSA production terms vanish because both cancer-cell populations are zero, while PSA clearance remains:
\[
H_6=-\delta_3P=-0.08.
\]
For the integer-order case \(\alpha=1\), which the paper explicitly includes among its simulations, the model therefore has
\[
\frac{d}{dt}(P-A)=H_6-H_5=-0.08.
\]
A numerical rule that enforces \(P-A\) exactly constant cannot consistently discretize this vector field at that state.

Replacing \(H_5\) by \(H_6\) in the PSA recurrence restores the required componentwise structure.

## Verification

The bundled `verify.py` uses exact rational arithmetic for the Table 1 witness
\[
\gamma_1=\delta_3=\frac{2}{25},\qquad
a_0=A=10,\qquad
P=1,\qquad
u=0,\qquad
X_1=X_2=0.
\]
It verifies
\[
H_5=0,\qquad
H_6=-\frac{2}{25}.
\]

The script also feeds several arbitrary rational increment values into two recurrences with identical increments and checks that their difference is invariant step by step. This second check is only a replay of the algebraic identity; the general proof is the subtraction argument above.

## Relationship to prior work

Alzahrani and Khan define the six-state Atangana-Baleanu prostate-cancer model and the numerical recurrence at issue. Their article states that the numerical results in Figures 1--7 are obtained using the scheme presented in Section 5.

Toufik and Atangana are the cited source for the underlying Atangana-Baleanu numerical construction. A 2022 author correction to that method paper repairs a finite-sum identity in its error analysis and explicitly states that the correction does not affect the formulation of the numerical scheme. That correction does not address the later prostate-cancer paper's substitution of the androgen component \(H_5\) into the PSA update.

Portz, Kuang, and Nagy provide the earlier clinically validated prostate-cancer model on which the biological state variables are based. Their work reinforces that androgen and PSA are distinct observables; it does not contain the later fractional recurrence.

Searches by the exact article DOI and title, by the aliases “PSA recurrence,” “\(H_5\)/\(H_6\),” and “androgen numerical scheme,” and by correction/erratum terminology did not locate a published correction of this component substitution.

## Limitations

The result establishes a defect in the printed numerical scheme, not necessarily in unpublished simulation code. The plotted PSA curves may have been produced with a corrected implementation.

No claim is made here about the accuracy of the other five recurrences or about the general convergence theory of the cited Atangana-Baleanu method.

The witness at \(\alpha=1\) is sufficient to disprove componentwise consistency of the printed six-state scheme because the source itself includes that integer-order endpoint. The finding does not require a separate convergence analysis for \(0<\alpha<1\).

## References

1. E. O. Alzahrani and M. A. Khan, “Androgen driven evolutionary population dynamics in prostate cancer growth,” Discrete and Continuous Dynamical Systems - S 14 (2021), 3419--3440. DOI: 10.3934/dcdss.2020426. Early access: 18 September 2020.
2. M. Toufik and A. Atangana, “New numerical approximation of fractional derivative with non-local and non-singular kernel: Application to chaotic models,” The European Physical Journal Plus 132 (2017), Article 444. DOI: 10.1140/epjp/i2017-11717-0.
3. M. Toufik and A. Atangana, “Correction to: New numerical approximation of fractional derivative with non-local and non-singular kernel: application to chaotic models,” The European Physical Journal Plus 137 (2022), Article 191. DOI: 10.1140/epjp/s13360-022-02380-9.
4. T. Portz, Y. Kuang, and J. D. Nagy, “A clinical data validated mathematical model of prostate cancer growth under intermittent androgen suppression therapy,” AIP Advances 2 (2012), 011002. DOI: 10.1063/1.3697848.
