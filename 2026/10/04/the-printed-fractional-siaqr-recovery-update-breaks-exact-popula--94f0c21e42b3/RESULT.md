# The printed fractional SIAQR recovery update breaks exact population conservation

## Finding

Consider the Caputo SIAQR model
\[
{}^C D_t^\gamma S=g_1,\qquad
{}^C D_t^\gamma I=g_2,\qquad
{}^C D_t^\gamma A=g_3,\qquad
{}^C D_t^\gamma Q=g_4,\qquad
{}^C D_t^\gamma R=g_5,
\]
with
\[
N=S+I+A+Q+R.
\]
Adding the five printed right-hand sides gives the exact identity
\[
g_1+g_2+g_3+g_4+g_5=0.
\]
Hence the continuous fractional model satisfies
\[
{}^C D_t^\gamma N=0
\]
and therefore conserves
\[
N(t)=N(0).
\]

The numerical recurrences printed in equations (5.18)--(5.22) do not preserve the componentwise structure needed for the same cancellation. In the recovery recurrence, the first history sum uses the recovery component \(R\), but the second and third history corrections use the quarantine component \(Q\) as the argument of \(g_5\).

This is not an inert notation change. At fractional order
\[
\gamma=\frac12,
\]
take
\[
N=1,\qquad
\delta=\omega=\frac12,
\]
with arbitrary positive remaining rates and
\[
S(0)=0,\qquad
R(0)=1,\qquad
I(0)=A(0)=Q(0)=0.
\]
Then the exact model stays on
\[
I=A=Q=0,\qquad S=1-R,
\]
and
\[
{}^C D_t^{1/2}R=-R.
\]
Thus
\[
R(t)=E_{1/2}(-t^{1/2})
=e^t\operatorname{erfc}(\sqrt t).
\]

On the unit mesh,
\[
R_0=1,\qquad
R_1=e\operatorname{erfc}(1),\qquad
R_2=e^2\operatorname{erfc}(\sqrt2).
\]
At the first recurrence level containing all three history terms, namely \(m=2\), the total-population error caused solely by the printed \(Q\)-arguments is
\[
\Delta N_3
=
\frac{4}{\Gamma(5/2)}(R_1-R_0)
+
\frac{17}{2\Gamma(7/2)}(R_2-2R_1+R_0).
\]
Numerically,
\[
\Delta N_3
\approx
-0.492078936843789.
\]
Therefore the published update maps this exact admissible history to
\[
N_3\approx0.507921063156211
\]
instead of the exact value
\[
N_3=1.
\]

The componentwise repair is to replace the \(Q\)-arguments inside the second and third \(g_5\) history differences of equation (5.22) by the corresponding \(R\)-arguments.

## Assumptions and scope

All rates are nonnegative, the fixed total population satisfies
\[
N(0)>0,
\]
and the fractional order satisfies
\[
0<\gamma<1.
\]

The explicit witness uses
\[
\gamma=\frac12,
\qquad
\delta=\omega=\frac12,
\]
so it lies strictly inside the fractional regime rather than relying on an integer-order endpoint.

The result concerns the recurrence printed in the article. The numerical implementation used to create the figures is not available, so the finding does not claim that unpublished code necessarily contains the same \(Q\)-for-\(R\) substitution.

The finding also does not assess the accuracy of the underlying Atangana-Seda formula itself. It isolates a component-selection error in the source's specialization of that formula to the recovered compartment.

## Proof

Summing the five model equations cancels every infection transfer, quarantine transfer, recovery transfer, and immunity-loss transfer. Birth and natural-death terms also cancel because the birth input is
\[
\delta N
\]
and the five natural-death terms sum to
\[
-\delta N.
\]
Thus
\[
\sum_{j=1}^5g_j=0.
\]
By linearity of the Caputo derivative,
\[
{}^C D_t^\gamma N=0,
\]
whose Volterra representation gives
\[
N(t)=N(0).
\]

Now specialize to
\[
I=A=Q=0,\qquad
N=1,\qquad
\delta=\omega=\frac12,\qquad
S=1-R.
\]
The recovery equation becomes
\[
{}^C D_t^{1/2}R=-R.
\]
The susceptible equation reduces to
\[
{}^C D_t^{1/2}S=R.
\]
Hence their exact right-hand sides satisfy
\[
g_1=R,\qquad g_5=-R.
\]

For
\[
{}^C D_t^{1/2}R=-R,\qquad R(0)=1,
\]
the exact solution is
\[
R(t)=E_{1/2}(-t^{1/2})
=e^t\operatorname{erfc}(\sqrt t).
\]

At \(m=2\) and unit step size, the coefficient multiplying the first difference in the source's three-level history formula is
\[
C_2
=
\frac{3+2\gamma}{\Gamma(\gamma+2)}
=
\frac{4}{\Gamma(5/2)}.
\]
The coefficient multiplying the second difference is
\[
C_3
=
\frac{2\gamma^2+9\gamma+12}{2\Gamma(\gamma+3)}
=
\frac{17}{2\Gamma(7/2)}.
\]

If the recovery equation used \(R\) in all three history terms, the susceptible and recovery contributions would cancel at every history level because
\[
g_1(t_j)+g_5(t_j)=0.
\]
The printed equation instead evaluates the recovery correction terms at the identically zero quarantine history. Those two recovery corrections are therefore zero, leaving the uncancelled susceptible corrections
\[
C_2(R_1-R_0)
+
C_3(R_2-2R_1+R_0).
\]
Substituting the exact \(R_j\) values gives the stated nonzero defect.

Replacing the erroneous \(Q\)-arguments by \(R\)-arguments restores the componentwise cancellation.

## Verification

The bundled `verify.py` uses 80-digit arithmetic.

It evaluates
\[
R_1=e\operatorname{erfc}(1)
\]
and
\[
R_2=e^2\operatorname{erfc}(\sqrt2),
\]
constructs the exact \(m=2\), \(\gamma=1/2\) coefficients from the printed recurrence, and reproduces
\[
\Delta N_3
\approx
-0.49207893684378897699.
\]

It separately checks that the source-model right-hand sides in the chosen invariant submodel satisfy
\[
g_1+g_5=0
\]
at each supplied history value.

The computation is a finite replay of the explicit witness. General population conservation and the reason for its failure in the printed recurrence are algebraic identities proved above.

## Relationship to prior work

Althubiti, Sharma, Goswami, and Dubey define the fractional SIAQR model and print the five component recurrences. Equations (5.18)--(5.21) use each component's own field consistently, while equation (5.22) changes from \(R\) in its first recovery history term to \(Q\) in the subsequent recovery differences.

Rihan and Alsakaji analyze a stochastic delay SIAQR model and prove global positivity for that different formulation. Their model confirms that SIAQR state-space structure is established prior context, but it does not contain the fractional recurrence studied here.

Later descriptions of Newton-polynomial fractional schemes formulate the quadrature for a scalar equation
\[
D_t^\alpha y=f(t,y)
\]
using the same component function \(f\) throughout its history interpolation. This is consistent with the componentwise repair and does not supply or justify the \(Q\)-for-\(R\) substitution in the motivating article.

Searches by exact DOI and title, by “recovered numerical scheme,” by the \(g_5/Q/R\) aliases, and by correction/erratum terminology did not locate a published correction of equation (5.22).

## Limitations

The result does not establish that the article's plotted trajectories violate population conservation, because the code used to generate them is unavailable and may have used the intended \(R\)-arguments.

The witness isolates the printed component-selection defect; it does not certify the convergence order, stability region, or positivity preservation of the underlying Newton-polynomial method.

The correction restores the algebraic cancellation required by the continuous conservation law. It does not by itself prove every other property of the fully discrete method.

## References

1. S. Althubiti, S. Sharma, P. Goswami, R. S. Dubey, “Fractional SIAQR model with time dependent infection rate,” Arab Journal of Basic and Applied Sciences 30 (2023), 307--316. DOI: 10.1080/25765299.2023.2209981. Published online 16 May 2023.
2. F. A. Rihan, H. J. Alsakaji, “Dynamics of a stochastic delay differential model for COVID-19 infection with asymptomatic infected and interacting people: Case study in the UAE,” Results in Physics 28 (2021), 104658. DOI: 10.1016/j.rinp.2021.104658.
3. J.-L. Wang, Y.-L. Wang, X.-Y. Li, “An efficient numerical simulation of chaos dynamical behaviors for fractional-order Rössler chaotic systems with Caputo fractional derivative,” Journal of Low Frequency Noise, Vibration and Active Control. DOI: 10.1177/14613484231224611.
