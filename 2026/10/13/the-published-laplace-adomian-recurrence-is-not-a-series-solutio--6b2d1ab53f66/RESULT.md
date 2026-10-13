# The published Laplace–Adomian recurrence is not a series solution of the stated COVID-19 model

## Finding

Consider the seven-compartment Caputo model with
\[
q=1-\epsilon_m e_m
\]
and initial data
\[
S(0)=K_1,\quad E(0)=K_2,\quad I_s(0)=K_3,\quad I_a(0)=K_4,
\]
\[
H(0)=K_5,\quad Q_h(0)=K_6,\quad R(0)=K_7.
\]

The internally consistent infection and transition equations printed in the source before its explicit iterates give
\[
{}^CD_t^\alpha S
=
\delta-q\beta SI_s-q\beta' SI_a-\lambda S,
\]
\[
{}^CD_t^\alpha E
=
q\beta SI_s+q\beta' SI_a-(\sigma+\lambda)E,
\]
\[
{}^CD_t^\alpha I_s
=
(1-a)\sigma E+\rho_a I_a-(\lambda_s+\lambda+\phi_s)I_s,
\]
and
\[
{}^CD_t^\alpha R
=
\rho_hQ_h+\tau_hH-\lambda R.
\]

Equation (5.9) is already inconsistent with these equations. The first symptomatic iterate uses
\[
-\phi_sK_4
\]
instead of
\[
-\phi_sK_3,
\]
and the first recovered iterate uses
\[
\rho_hK_5
\]
instead of
\[
\rho_hK_6.
\]

Equation (5.10), the recurrence the paper explicitly identifies as the source of its numerical graphs, contains further substitutions. In the susceptible and exposed recurrences it reverses the symptomatic and asymptomatic incidence pairings, using \(\beta SI_a\) and \(\beta' SI_s\). Its susceptible recurrence subtracts \(\lambda E\) rather than \(\lambda S\), and its symptomatic recurrence subtracts \(\phi_sI_a\) rather than \(\phi_sI_s\).

These are not notation-only changes. They alter the first Caputo-series coefficient for generic initial data, so the displayed recurrence is not a formal series solution of the stated model.

## Assumptions and scope

The claim is about the equations printed in the article. The intended infection pairing is fixed internally by the susceptible equation, the parameter table, the population-balance calculation, the fractional integral representation, and equations (5.6)–(5.8). In those places \(\beta\) acts on symptomatic infection and \(\beta'\) on asymptomatic infection.

The article contains an earlier typographical inconsistency in one display of the exposed equation. The finding does not rely on choosing that isolated display: it uses the source's internally repeated pairing that is also required for cancellation of infection transfers in the total-population balance.

The result does not assert that unavailable source code used the erroneous printed recurrence. It establishes that the published equations do not provide a reproducible derivation of the plotted approximations.

## Proof

For a Caputo equation
\[
{}^CD_t^\alpha y(t)=F(y(t)),
\qquad
0<\alpha\le1,
\]
the fractional integral form is
\[
y(t)
=
y(0)
+
\frac1{\Gamma(\alpha)}
\int_0^t
(t-\eta)^{\alpha-1}F(y(\eta))\,d\eta.
\]
Therefore the first decomposition iterate has coefficient
\[
F(y(0))
\]
multiplying
\[
\frac{t^\alpha}{\Gamma(\alpha+1)}.
\]

Applying that necessary condition to the source model gives
\[
A_S
=
\delta-q\beta K_1K_3-q\beta'K_1K_4-\lambda K_1,
\]
\[
A_E
=
q\beta K_1K_3+q\beta'K_1K_4-(\sigma+\lambda)K_2,
\]
\[
A_{I_s}
=
(1-a)\sigma K_2+\rho_aK_4-(\lambda_s+\lambda+\phi_s)K_3,
\]
and
\[
A_R
=
\rho_hK_6+\tau_hK_5-\lambda K_7.
\]

Equation (5.9) instead has
\[
A_{I_s}^{(5.9)}
=
(1-a)\sigma K_2+\rho_aK_4-(\lambda_s+\lambda)K_3-\phi_sK_4,
\]
so
\[
A_{I_s}^{(5.9)}-A_{I_s}
=
\phi_s(K_3-K_4).
\]
It also prints
\[
A_R^{(5.9)}
=
\rho_hK_5+\tau_hK_5-\lambda K_7,
\]
giving
\[
A_R^{(5.9)}-A_R
=
\rho_h(K_5-K_6).
\]

The first coefficient implied by equation (5.10) for the susceptible recurrence is
\[
A_S^{(5.10)}
=
\delta-q\beta K_1K_4-q\beta'K_1K_3-\lambda K_2.
\]
Therefore
\[
A_S^{(5.10)}-A_S
=
q(\beta-\beta')K_1(K_3-K_4)+\lambda(K_1-K_2).
\]
Its symptomatic recurrence again uses \(-\phi_sK_4\), so
\[
A_{I_s}^{(5.10)}-A_{I_s}
=
\phi_s(K_3-K_4).
\]

These differences vanish only on special algebraic subsets. They are not identities.

For
\[
q=\frac12,\quad
K_1=1,\ K_2=2,\ K_3=3,\ K_4=4,\ K_5=5,\ K_6=6,\ K_7=7,
\]
\[
\beta=2,\quad \beta'=1,\quad
\lambda=1,\quad \phi_s=1,\quad \rho_h=1,
\]
one obtains
\[
A_S^{(5.10)}-A_S=-\frac32,
\]
\[
A_{I_s}^{(5.10)}-A_{I_s}=-1,
\]
and
\[
A_R^{(5.9)}-A_R=-1.
\]
Thus the printed recurrence fails a necessary first-coefficient consistency condition.

## Verification

The bundled `verify.py` symbolically reconstructs the correct first coefficients from the source model and compares them with equations (5.9) and (5.10).

It verifies
\[
A_{I_s}^{(5.9)}-A_{I_s}
=
\phi_s(K_3-K_4),
\]
\[
A_R^{(5.9)}-A_R
=
\rho_h(K_5-K_6),
\]
and
\[
A_S^{(5.10)}-A_S
=
q(\beta-\beta')K_1(K_3-K_4)+\lambda(K_1-K_2).
\]
The exact positive witness returns
\[
-\frac32,\qquad -1,\qquad -1.
\]

No numerical integration or finite parameter search is used.

## Relationship to prior work

The motivating article adapts an earlier deterministic COVID-19 model with separate symptomatic and asymptomatic transmission, hospitalization, quarantine, face-mask effects, and recovery flows. The predecessor model provides the compartmental meaning of the two infection routes; the motivating article itself repeats the same route assignments in its parameter table and in the internally consistent part of its fractional derivation.

Laplace–Adomian decomposition for Caputo systems is standard. The present result does not claim a new decomposition method. It is a source-specific consistency result: the explicit iterates and the final recurrence printed in this article do not reproduce the vector field they are supposed to solve.

Targeted searches by DOI, exact title, equation number, decomposition terminology, symptomatic/asymptomatic substitutions, and correction or erratum terminology did not locate a published correction of equations (5.9)–(5.10).

## Limitations

The result establishes a defect in the published recurrence and therefore in the reproducibility of the reported numerical approximation from the printed derivation.

It does not reconstruct unavailable implementation code. If the authors' code silently used corrected equations, some plotted trajectories could differ from those generated by the printed recurrence.

The finding does not re-audit the article's existence or uniqueness arguments, and it does not claim that the underlying compartmental model is itself invalid.

## References

1. I. Ul Haq, N. Ali, H. Ahmad, T. A. Nofal, “On the fractional-order mathematical model of COVID-19 with the effects of multiple non-pharmaceutical interventions,” AIMS Mathematics 7 (2022), 16017–16036. DOI: 10.3934/math.2022877.
2. A. K. Srivastav, P. K. Tiwari, P. K. Srivastava, M. Ghosh, Y. Kang, “A mathematical model for the impacts of face mask, hospitalization and quarantine on the dynamics of COVID-19 in India: deterministic vs. stochastic,” Mathematical Biosciences and Engineering 18 (2021), 182–213. DOI: 10.3934/mbe.2021010.
