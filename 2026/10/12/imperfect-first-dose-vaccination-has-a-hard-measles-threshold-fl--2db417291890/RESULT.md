# Imperfect first-dose vaccination has a hard measles threshold floor

## Finding

The measles model uses two first-dose controls: a newborn vaccination proportion \(u_1\) and an adult first-dose rate \(u_2\). In Section 3.6 the source sets the second-dose and treatment rates to zero to study first-dose vaccination alone.

For that exact scenario, define
\[
K=\frac{\eta A\beta}{\mu(\mu+\gamma)(\mu+\eta)}.
\]
The reproduction number simplifies to
\[
\mathcal R_F(u_1,u_2)
=
K\left[
\epsilon+
(1-\epsilon)\frac{\mu(1-u_1)}{u_2+\mu}
\right].
\]
Therefore
\[
\inf_{0\le u_1<1,\;u_2\ge0}\mathcal R_F(u_1,u_2)
=K\epsilon.
\]
A finite admissible first-dose strategy reaches \(\mathcal R_F<1\) if and only if
\[
K\epsilon<1.
\]

At the source's fitted parameters,
\[
K\approx20.0314888219,
\qquad
\epsilon=0.07,
\]
so
\[
K\epsilon\approx1.4022042175>1.
\]
Thus neither arbitrarily high adult first-dose vaccination nor any admissible newborn first-dose proportion can push the first-dose-only reproduction number below one.

When \(u_2=0\), the formal threshold is
\[
u_{1,c}=
\frac{1-K^{-1}}{1-\epsilon}
\approx1.0215898907.
\]
The source reports this as \(u_1^*=1.02\) and states that choosing a larger \(u_1\) would eradicate measles. But its own parameter table defines
\[
0\le u_1<1.
\]
The reported threshold is therefore outside the model's admissible domain.

## Assumptions and scope

The result uses the source's dimensional reproduction number and the same special case as Section 3.6:
\[
u_3=u_4=0.
\]
Here \(u_1\in[0,1)\), \(u_2\ge0\), and \(\epsilon\) is residual susceptibility after first-dose vaccination, so the vaccine efficacy is \(1-\epsilon\).

All demographic and disease rates appearing in \(K\) are positive. The sharp existence classification assumes \(0\le\epsilon<1\); the source uses \(\epsilon=0.07\).

The finding concerns the unit reproduction-number threshold for first-dose-only intervention. It does not assert that all intervention combinations fail: second-dose vaccination or medical treatment changes the denominator of the source's full reproduction number.

## Proof

The source's dimensional reproduction number is
\[
\widetilde{\mathcal R}_0
=
\frac{\eta A\beta\left(\epsilon(u_1\mu+u_2)+(u_3+\mu)(1-u_1)\right)}
{(u_3+\mu)(u_2+\mu)(\mu+\gamma)(\mu+\eta+u_4)}.
\]
Set
\[
u_3=u_4=0.
\]
Then
\[
\widetilde{\mathcal R}_0
=
\frac{\eta A\beta}{\mu(\mu+\gamma)(\mu+\eta)}
\frac{\epsilon(u_1\mu+u_2)+\mu(1-u_1)}{u_2+\mu}.
\]
The numerator in the final fraction has the identity
\[
\epsilon(u_1\mu+u_2)+\mu(1-u_1)
=
\epsilon(u_2+\mu)+(1-\epsilon)\mu(1-u_1).
\]
Hence
\[
\mathcal R_F(u_1,u_2)
=
K\left[
\epsilon+
(1-\epsilon)\frac{\mu(1-u_1)}{u_2+\mu}
\right].
\]

For \(0\le\epsilon<1\), \(0\le u_1<1\), and finite \(u_2\ge0\), the second term in brackets is strictly positive. Consequently
\[
\mathcal R_F(u_1,u_2)>K\epsilon.
\]
The lower bound is sharp as an infimum: it is approached either by taking \(u_1\uparrow1\) or by taking \(u_2\to\infty\). Therefore
\[
\inf\mathcal R_F=K\epsilon.
\]

If \(K\epsilon\ge1\), every finite admissible pair has \(\mathcal R_F>1\), so crossing is impossible. If \(K\epsilon<1\), continuity and the sharp infimum imply that sufficiently large \(u_2\), or sufficiently high admissible \(u_1\), gives \(\mathcal R_F<1\). This proves the if-and-only-if statement.

For \(u_2=0\),
\[
\mathcal R_F(u_1,0)
=K\left[1-(1-\epsilon)u_1\right].
\]
Solving \(\mathcal R_F=1\) gives
\[
u_{1,c}=\frac{1-K^{-1}}{1-\epsilon}.
\]
With the source values this is approximately \(1.0215898907\), outside \([0,1)\).

## Verification

The bundled `verify.py` reconstructs the first-dose-only reduction with exact rational arithmetic from the source's printed decimal parameters.

It verifies
\[
K\approx20.0314888219,
\qquad
K\epsilon\approx1.4022042175,
\]
and
\[
u_{1,c}\approx1.0215898907.
\]
It also checks the algebraic factorization of the reproduction number and proves symbolically that its derivatives satisfy
\[
\frac{\partial\mathcal R_F}{\partial u_1}<0,
\qquad
\frac{\partial\mathcal R_F}{\partial u_2}<0
\]
for \(u_1<1\) and \(0\le\epsilon<1\). The lower bound is analytic, not inferred from a parameter grid.

## Relationship to prior work

The motivating article explicitly defines \(u_1\) as a newborn first-dose vaccination proportion in \([0,1)\). In its first-dose sensitivity subsection it sets \(u_2=u_3=u_4=0\), obtains the approximate equation
\[
-18.63u_1^*+20.03=1,
\]
reports \(u_1^*=1.02\), and states that larger values would make the reproduction number subunit. It then displays a contour of the first-dose variables \(u_1\) and \(u_2\).

The sharp result above strengthens the domain observation: with the source parameters, even the joint class of newborn and adult first-dose vaccination has the irreducible floor \(K\epsilon\approx1.4022\). Thus adult first-dose vaccination cannot rescue the first-dose-only scenario.

Fakhruddin and coauthors analyze a different Jakarta measles model with one vaccination-coverage parameter and a fixed successful-vaccination probability. Their reproduction number has a different susceptible-removal structure and does not imply the two-control floor derived here.

Searches by the motivating DOI, exact title, the reported value \(1.02\), first-dose-only terminology, imperfect-vaccine floor terminology, and equivalent reproduction-number formulations did not locate a published correction or the sharp source-specific classification above.

## Limitations

The result is about the source's deterministic reproduction number and its first-dose-only sensitivity experiment.

It does not evaluate economic cost, transient incidence reduction, or the optimal-control strategies that combine vaccination with treatment.

A reproduction number above one in this special intervention slice does not imply that second-dose vaccination or medical treatment cannot make the full model subcritical.

## References

1. S. A. Rahmayani, D. Aldila, B. D. Handari, “Cost-effectiveness analysis on measles transmission with vaccination and treatment intervention,” AIMS Mathematics 6 (2021), 12491–12527. DOI: 10.3934/math.2021721.
2. M. Fakhruddin, D. Suandi, Sumiati, H. Fahlena, N. Nuraini, E. Soewono, “Investigation of a measles transmission with vaccination: a case study in Jakarta, Indonesia,” Mathematical Biosciences and Engineering 17 (2020), 2998–3018. DOI: 10.3934/mbe.2020170.
