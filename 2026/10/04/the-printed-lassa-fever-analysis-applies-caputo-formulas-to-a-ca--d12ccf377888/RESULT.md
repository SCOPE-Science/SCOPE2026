# The printed Lassa-fever analysis applies Caputo formulas to a Caputo-Fabrizio model

## Finding

The Lassa-fever paper declares that its nine-state system uses the Caputo-Fabrizio (CF) fractional derivative. Its existence analysis is consistent with that declaration: it writes the Losada-Nieto CF integral in the form
\[
y(t)-y(0)
=
A_\alpha f(t,y(t))
+
B_\alpha\int_0^t f(s,y(s))\,ds,
\]
where
\[
A_\alpha=
\frac{2(1-\alpha)}
{(2-\alpha)M(\alpha)}
\]
and
\[
B_\alpha=
\frac{2\alpha}
{(2-\alpha)M(\alpha)}.
\]

The boundedness and numerical sections then switch to formulas for the classical Caputo derivative.

The mismatch is already visible in the exact total-rodent equation
\[
{}^{CF}D_t^\alpha N_r
=
\Pi-\varphi N_r.
\]
The source treats this equation with a Mittag-Leffler transient,
\[
N_r(t)
=
\frac{\Pi}{\varphi}
+
\left(
N_{r0}-\frac{\Pi}{\varphi}
\right)
E_\alpha(-\varphi t^\alpha),
\]
equivalently to the power-law convolution displayed in its boundedness proof. This is the standard solution of the classical Caputo equation.

The paper's own CF integral gives a different relation:
\[
N_r(t)-N_{r0}
=
A_\alpha
\bigl(\Pi-\varphi N_r(t)\bigr)
+
B_\alpha
\int_0^t
\bigl(\Pi-\varphi N_r(s)\bigr)\,ds.
\]
For a continuous solution satisfying this relation at the initial time and
\[
0<\alpha<1,
\]
one necessarily has
\[
N_{r0}
=
\frac{\Pi}{\varphi}.
\]
If the Volterra equation is instead used for positive time with arbitrary \(N_{r0}\), then
\[
N_r(0+)
=
\frac{N_{r0}+A_\alpha\Pi}
{1+A_\alpha\varphi}
\]
and
\[
N_r(t)
=
\frac{\Pi}{\varphi}
+
\frac{N_{r0}-\Pi/\varphi}
{1+A_\alpha\varphi}
\exp\!\left(
-\frac{B_\alpha\varphi}
{1+A_\alpha\varphi}t
\right).
\]
The CF transient is therefore ordinary exponential after the compatibility adjustment, not Mittag-Leffler.

The same operator switch appears in the numerical section. Its Adams-Bashforth-Moulton formulas contain
\[
h^\alpha,
\]
Gamma-function denominators, and the power-law history weights of the Diethelm-Ford-Freed predictor-corrector. That cited method is derived for the classical Caputo operator and its power-law Volterra integral, not for the Losada-Nieto CF integral.

Thus, for
\[
0<\alpha<1,
\]
the printed fractional-order simulations solve a classical Caputo formulation of the compartmental vector field rather than the declared Caputo-Fabrizio formulation. The distinction vanishes at
\[
\alpha=1.
\]

## Assumptions and scope

The result concerns the fractional operator used in the mathematical analysis and printed numerical method.

The normalization function is assumed positive at the fractional order under consideration, so that
\[
A_\alpha>0,
\qquad
B_\alpha>0
\]
for
\[
0<\alpha<1.
\]
No particular numerical value of \(M(\alpha)\) is needed.

The result does not challenge the integer-order compartmental equations, disease-free equilibrium, or next-generation calculation. Those parts are evaluated at
\[
\alpha=1,
\]
where the fractional-operator distinction disappears.

The result also does not assert that every boundedness conclusion is false. It shows that the displayed Mittag-Leffler comparison is a classical Caputo calculation rather than a CF calculation.

No independent simulation code accompanies the source. The finding therefore concerns the printed scheme and the scientific interpretation supported by that scheme.

## Proof

The source's existence section applies the CF fractional integral and obtains
\[
y(t)-y(0)
=
A_\alpha f(t,y(t))
+
B_\alpha\int_0^t f(s,y(s))\,ds.
\]
This relation has a local term and an ordinary time integral.

Consider the total mastomys-rat equation, obtained exactly by adding the susceptible and infected rat equations:
\[
{}^{CF}D_t^\alpha N_r
=
\Pi-\varphi N_r.
\]
Applying the displayed CF integral gives
\[
N_r(t)-N_{r0}
=
A_\alpha(\Pi-\varphi N_r(t))
+
B_\alpha\int_0^t(\Pi-\varphi N_r(s))\,ds.
\]

At
\[
t=0,
\]
continuity implies
\[
0
=
A_\alpha(\Pi-\varphi N_{r0}).
\]
For a genuine fractional order,
\[
A_\alpha>0,
\]
so continuous initial data are compatible only if
\[
N_{r0}
=
\frac{\Pi}{\varphi}.
\]

For the positive-time Volterra interpretation, rearrange:
\[
(1+A_\alpha\varphi)N_r(t)
=
N_{r0}
+
A_\alpha\Pi
+
B_\alpha\Pi t
-
B_\alpha\varphi
\int_0^tN_r(s)\,ds.
\]
Differentiation for positive time yields
\[
(1+A_\alpha\varphi)N_r'
=
B_\alpha(\Pi-\varphi N_r).
\]
Hence
\[
N_r'
=
\frac{B_\alpha}
{1+A_\alpha\varphi}
(\Pi-\varphi N_r).
\]
The right limit supplied by the undifferentiated integral equation is
\[
N_r(0+)
=
\frac{N_{r0}+A_\alpha\Pi}
{1+A_\alpha\varphi},
\]
which gives the exponential formula in the finding.

By contrast, the classical Caputo equation
\[
{}^{C}D_t^\alpha N_r
=
\Pi-\varphi N_r
\]
has the continuous Mittag-Leffler solution
\[
N_r(t)
=
\frac{\Pi}{\varphi}
+
\left(
N_{r0}-\frac{\Pi}{\varphi}
\right)
E_\alpha(-\varphi t^\alpha).
\]
This is precisely the functional form used in the source's boundedness argument.

The numerical distinction is also exact. Diethelm, Ford, and Freed define their fractional operator by
\[
D_*^\alpha y
=
J^{m-\alpha}y^{(m)},
\]
explicitly identifying it as the Caputo derivative. Their predictor-corrector is derived from the equivalent power-law Volterra equation and therefore has power-law history quadrature weights.

The Lassa-fever numerical section reproduces that structure through its
\[
h^\alpha
\]
prefactor, Gamma-function denominators, and fractional Adams history weights. Those terms approximate the classical Caputo Volterra convolution. They do not discretize the source's earlier CF relation, whose memory contribution is an ordinary integral plus a local term.

Therefore the two fractional formulations agree at
\[
\alpha=1
\]
but are distinct for
\[
0<\alpha<1.
\]

## Verification

The bundled `verify.py` checks the scalar CF algebra independently.

For generic positive coefficients \(A\) and \(B\), it verifies that
\[
y(t)
=
\frac{\Pi}{\varphi}
+
\frac{y_0-\Pi/\varphi}
{1+A\varphi}
\exp\!\left(
-\frac{B\varphi}{1+A\varphi}t
\right)
\]
satisfies
\[
y(t)-y_0
=
A(\Pi-\varphi y(t))
+
B\int_0^t(\Pi-\varphi y(s))\,ds
\]
for positive time.

It also verifies the right-limit formula
\[
y(0+)
=
\frac{y_0+A\Pi}
{1+A\varphi}
\]
and the compatibility equivalence
\[
y(0+)=y_0
\quad\Longleftrightarrow\quad
y_0=\frac{\Pi}{\varphi}
\]
when
\[
A>0.
\]

A numerical illustration compares the CF exponential transient with the classical Caputo order-\(1/2\) Mittag-Leffler transient. This illustration is not used to prove the general operator mismatch.

## Relationship to prior work

Ndenda, Njagarah, and Shaw define the Lassa-fever system as Caputo-Fabrizio, use the Losada-Nieto CF integral in their existence analysis, use Mittag-Leffler formulas in their boundedness analysis, and then use a Diethelm-Ford-Freed Adams-Bashforth-Moulton predictor-corrector for the simulations.

Diethelm, Ford, and Freed explicitly formulate their predictor-corrector for the classical Caputo derivative
\[
D_*^\alpha y
=
J^{m-\alpha}y^{(m)}
\]
and derive it from the corresponding power-law Volterra equation. Their method is therefore not an operator-neutral Adams formula.

Losada and Nieto introduced the fractional integral associated with the Caputo-Fabrizio derivative. The motivating paper itself writes that integral explicitly, making the incompatibility with its later power-law quadrature visible without importing a different convention.

Later theoretical work on Caputo-Fabrizio-type operators emphasizes that nonsingular-kernel derivatives have a special initial-time compatibility issue and that their associated Volterra equations are structurally connected to ordinary differential equations. This is consistent with the scalar derivation above.

Searches using the exact motivating DOI and title, Caputo/Caputo-Fabrizio aliases, Adams-Bashforth-Moulton terminology, Mittag-Leffler terminology, and correction or erratum terms did not locate a published correction of this operator mismatch.

## Limitations

The result does not show that the source's integer-order epidemiological conclusions are wrong.

The boundedness inequalities might admit alternative CF proofs even though the displayed Mittag-Leffler calculation uses the wrong operator.

The numerical figures could still be meaningful for the classical Caputo version of the compartmental model. The finding is that they do not validate the declared Caputo-Fabrizio version for
\[
0<\alpha<1.
\]

The normalization \(M(\alpha)\) is kept symbolic; no disputed convention for its interior values is required.

## References

1. J. P. Ndenda, J. B. H. Njagarah, S. Shaw, “Influence of environmental viral load, interpersonal contact and infected rodents on Lassa fever transmission dynamics: Perspectives from fractional-order dynamic modelling,” AIMS Mathematics 7 (2022), 8975–9002. DOI: 10.3934/math.2022500. Published 8 March 2022.
2. K. Diethelm, N. J. Ford, A. D. Freed, “A Predictor-Corrector Approach for the Numerical Solution of Fractional Differential Equations,” Nonlinear Dynamics 29 (2002), 3–22. DOI: 10.1023/A:1016592219341.
3. J. Losada, J. J. Nieto, “Properties of a new fractional derivative without singular kernel,” Progress in Fractional Differentiation and Applications 1 (2015), 87–92. DOI: 10.12785/PFDA/010202.
4. M. Jornet, J. J. Nieto, “Properties of a New Generalized Caputo-Fabrizio Fractional Derivative,” Journal of Applied Analysis and Computation. DOI: 10.11948/20240079.
