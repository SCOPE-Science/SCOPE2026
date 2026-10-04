# An exact error-estimator resonance in the classical Fehlberg RK4(5) pair
## Finding
Consider Fehlberg's six-stage RK4(5) Formula 2 and apply it in exact arithmetic to the scalar linear test equation
\[
y'(t)=\lambda y(t).
\]
Write \(z=h\lambda\). The fourth- and fifth-order members have stability polynomials
\[
R_4(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}+\frac{z^5}{104},
\]
and
\[
R_5(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}+\frac{z^5}{120}+\frac{z^6}{2080}.
\]
Therefore the embedded error signal is exactly
\[
E(z)=R_5(z)-R_4(z)=\frac{z^5(3z-8)}{6240}.
\]

Besides the order-forced zero at \(z=0\), this error signal has the unique finite nonzero zero
\[
z_*=\frac83.
\]
At this resonance the two numerical answers coincide,
\[
R_4(z_*)=R_5(z_*)=\frac{1613}{117},
\]
but the exact multiplier is \(e^{8/3}\). Hence the local estimator is exactly zero while the propagated value underestimates the exact one by the relative amount
\[
1-\frac{1613}{117}e^{-8/3}
=0.0420785741677019\ldots.
\]

The blindness is not confined to one exactly tuned point. If
\[
L_5(z)=e^z-R_5(z)
\]
denotes the true one-step defect of the fifth-order member, then \(L_5(z_*)>0\) and
\[
E'(z_*)=\frac{1024}{15795}\ne0.
\]
Consequently
\[
\frac{|L_5(z)|}{|E(z)|}
\sim
\frac{15795\left(e^{8/3}-1613/117\right)}{1024\,|z-8/3|}
\qquad(z\to8/3),
\]
so the true-error-to-estimator ratio is unbounded in every punctured neighborhood of the resonance.

If the same step is imposed repeatedly, for example by an external maximum-step constraint with \(h\lambda=8/3\), then the error signal remains exactly zero on every nonzero step while
\[
y_n=\left(\frac{1613}{117}\right)^n y_0,
\qquad
y(t_n)=e^{8n/3}y_0.
\]
For \(y_0\ne0\), the relative global error is
\[
1-\left(\frac{1613}{117}e^{-8/3}\right)^n,
\]
which increases to \(1\). Numerically it is about \(0.88345\) after \(50\) resonant steps and \(0.98642\) after \(100\).

A structural reason this calculation is especially simple is that any explicit six-stage embedded pair of orders five and four has, on the scalar linear test equation, an error signal of the form
\[
z^5(A+Bz).
\]
Thus such a pair has at most one isolated nonzero scalar-linear error-estimator resonance unless the difference polynomial degenerates.

## Assumptions and scope
The theorem concerns the exact Fehlberg coefficients in Formula 2 of NASA TR R-315 and exact arithmetic. The local error signal is the difference between the fifth- and fourth-order embedded outputs. The repeated-step statement assumes that the same step size is actually imposed; a free adaptive controller may react to a zero estimate by enlarging the next step and therefore need not remain at the resonance.

The resonance lies on the positive real axis, so it concerns a growing scalar mode. There is no nonzero negative-real root of \(E\). The result does not claim that a production ODE solver without a maximum-step restriction will repeatedly hit \(z_*\), nor that floating-point evaluation will return an exactly zero difference.

## Proof
For an explicit Runge--Kutta method applied to \(y'=\lambda y\), write each stage derivative as \(\lambda y_n\) times a polynomial in \(z=h\lambda\). Substituting Fehlberg's Table III coefficients stage by stage and then applying the two output-weight vectors gives
\[
R_4(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}+\frac{z^5}{104},
\]
and
\[
R_5(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}+\frac{z^5}{120}+\frac{z^6}{2080}.
\]
Their difference factors as
\[
R_5(z)-R_4(z)
=
-\frac{z^5}{780}+\frac{z^6}{2080}
=
\frac{z^5(3z-8)}{6240}.
\]
This proves the unique nonzero zero \(z_*=8/3\).

Direct rational substitution yields
\[
R_4(8/3)=R_5(8/3)=\frac{1613}{117}.
\]
The true defect is nonzero and positive. Indeed,
\[
e^{8/3}>
\sum_{j=0}^{6}\frac{(8/3)^j}{j!}
=
\frac{462973}{32805},
\]
and
\[
\frac{462973}{32805}-\frac{1613}{117}
=
\frac{139264}{426465}>0.
\]
Thus a zero embedded difference does not represent a zero true local error.

Differentiating the factored error signal at its simple nonzero root gives
\[
E'(8/3)=\frac{1024}{15795}.
\]
Continuity of \(L_5\), the strict inequality \(L_5(8/3)>0\), and the first-order expansion of \(E\) at a simple root give the displayed reciprocal-distance divergence.

For repeated fixed resonant steps, linearity makes both embedded outputs multiply the current value by \(1613/117\), while the exact flow multiplies by \(e^{8/3}\). Since
\[
0<\frac{1613}{117}e^{-8/3}<1,
\]
iteration gives the exact relative-global-error formula and its limit.

Finally, an explicit six-stage Runge--Kutta method has a scalar stability polynomial of degree at most six. Fifth order fixes its coefficients through degree five to those of \(e^z\), while fourth order fixes coefficients through degree four. Subtracting the two therefore leaves only degree-five and degree-six terms, proving the structural form \(z^5(A+Bz)\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic to reconstruct all six scalar stages from Fehlberg's Table III coefficients. It independently recovers both stability polynomials, factors their difference, checks the resonance \(z_*=8/3\), checks the common multiplier \(1613/117\), verifies the positive rational lower bound on the true defect obtained from the sixth Taylor partial sum, and verifies the exact derivative \(E'(z_*)=1024/15795\).

It additionally evaluates the repeated-step relative-error formula numerically at \(n=1,50,100\). These decimal evaluations are illustrative only; the algebraic identities and asymptotic conclusions are proved analytically.

## Relationship to prior work
Fehlberg's 1969 report introduces the exact RK4(5) Formula 2 coefficients used here and explicitly proposes the difference of the fourth- and fifth-order outputs as an approximation to the leading truncation error for stepsize control. Those coefficients and the embedded-error principle are prior work.

Higham and Hall later analyze embedded order \(4,5\) pairs when stability restricts the stepsize. Their analysis explicitly introduces the main stability polynomial and the embedded error polynomial on the scalar linear model, studies equilibrium behavior of stepsize controllers, and includes the commonly used six-stage Fehlberg pair in its comparisons. The inspected paper does not state the positive-real root \(z=8/3\), the common multiplier \(1613/117\), the reciprocal-distance reliability blow-up, or the repeated fixed-step blind trajectory proved here.

Higham's later work on regular Runge--Kutta pairs studies avoidance of spurious fixed points under variable stepsize local error control. Only the abstract was accessible in the lawful routes checked; a full-text institutional retrieval encountered a human-verification barrier. Its stated object is regularity with respect to spurious fixed points, whereas the resonant Fehlberg multiplier here is \(1613/117\ne1\). An equivalent calculation elsewhere in that unavailable full text cannot be excluded and is the main residual originality risk.

Modern controller analysis also writes the scalar model as
\[
u^{n+1}=R(z)u^n,\qquad e^{n+1}=E(z)u^n
\]
with \(E\) the difference of the two stability polynomials. That framework makes roots of \(E\) mathematically natural, but the inspected modern source does not report this Fehlberg-specific resonance.

Targeted semantic searches of the checked research database for the exact Fehlberg factor, the value \(8/3\), scalar-linear estimator cancellation, and persistent zero estimates returned no implication-equivalent record. A failed search is not a novelty proof; it is recorded only as one component of the comparison.

## Limitations
The exact cancellation is an exact-arithmetic phenomenon. Roundoff perturbs it, although the reciprocal-distance divergence shows that near-resonant underestimation remains arbitrarily severe in principle.

The repeated-step global-error statement requires a fixed or externally capped step that remains resonant. It does not describe an unconstrained controller after a zero estimate. The resonance is on the positive real axis and therefore does not provide an analogous exact blind spot for strictly decaying scalar modes.

The general \(z^5(A+Bz)\) observation is an elementary consequence of stage count and order and is not presented as a separate novelty claim. The scientific contribution assessed here is the exact classical-Fehlberg resonance together with its nonzero true defect, near-resonant reliability blow-up, and persistent fixed-step error law.

## References
1. E. Fehlberg, *Low-Order Classical Runge-Kutta Formulas with Stepsize Control and Their Application to Some Heat Transfer Problems*, NASA Technical Report R-315, July 1969, NASA NTRS document 19690021375.
2. D. J. Higham and G. Hall, *Embedded Runge-Kutta formulae with stable equilibrium states*, Journal of Computational and Applied Mathematics 29 (1990), 25--33, DOI: 10.1016/0377-0427(90)90192-3.
3. D. J. Higham, *Regular Runge-Kutta pairs*, Applied Numerical Mathematics 25 (1997), 229--241, DOI: 10.1016/S0168-9274(97)00062-7.
4. H. Ranocha, L. Dalcin, M. Parsani, and D. I. Ketcheson, *Optimized Runge-Kutta Methods with Automatic Step Size Control for Compressible Computational Fluid Dynamics*, Communications on Applied Mathematics and Computation (2022), DOI: 10.1007/s42967-021-00159-w.
