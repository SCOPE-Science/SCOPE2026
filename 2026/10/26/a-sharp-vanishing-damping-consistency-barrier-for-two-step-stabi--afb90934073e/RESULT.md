# A sharp vanishing-damping consistency barrier for two-step stabilized Chebyshev integration

## Finding

Consider the damped, second-order, **two-stage** member of the two-step stabilized Runge–Kutta–Chebyshev construction of Moisa and Faleichik [1], on its real branch tending to the undamped stability polynomial as the damping \(\varepsilon\downarrow0\). Write \(\eta=1-\varepsilon\), \(e=\eta^2\), and, for sufficiently small \(\varepsilon>0\), define
\[
q=\frac{\sqrt{e^2+18e-3}-e}{3},\quad
w=\frac{1-q}{2},\quad
c_0=\frac{q+e}{1-e},\quad
c_1=\frac{q+2e+1}{2(1-e)}.
\]

For the nonautonomous, entire-polynomial test equation \(y'(t)=t^2\), with \(y(t)=t^3/3\) and **exact first two starting values**, this published two-stage realization takes precisely the form
\[
Y_{n+1}=(1+q)Y_n-qY_{n-1}
+h w\bigl[(t_n+c_0h)^2+(t_n+c_1h)^2\bigr].
\]
Its one-step local defect (numerical value minus exact value, with exact previous values) is \(h^3E_\varepsilon\), where
\[
E_\varepsilon=\frac{q-1}{3}
+\frac{1-q}{2}(c_0^2+c_1^2)
=\frac1\varepsilon-\frac{11}{8}+O(\varepsilon).
\]
In particular \(c_0=\varepsilon^{-1}-1+O(\varepsilon)\) and \(c_1=\varepsilon^{-1}-3/4+O(\varepsilon)\): the internal evaluations move far beyond the nominal current step as damping vanishes.

Fix a final time \(T>0\), take \(h=T/N\), \(N\to\infty\), and allow \(\varepsilon=\varepsilon(h)\downarrow0\). With \(Y_0=y(0)\) and \(Y_1=y(h)\), let \(\mathcal E_N=Y_N-y(T)\). Then the **sharp necessary-and-sufficient consistency condition** on this smooth problem is
\[
\boxed{\mathcal E_N\longrightarrow0\quad\Longleftrightarrow\quad
\varepsilon(h)/h\longrightarrow\infty.}
\]
More precisely:

* If \(\varepsilon/h\to\infty\), then \(\mathcal E_N\sim T h^2/\varepsilon^2\to0\).
* If \(\varepsilon/h\to\kappa\in(0,\infty)\), then
\[
\mathcal E_N\longrightarrow\frac{\kappa T-1+e^{-\kappa T}}{\kappa^3}>0.
\]
* If \(\varepsilon/h\to0\), then \(\mathcal E_N\sim T^2 h/(2\varepsilon)\to+\infty\).

Thus each fixed-damping formula remains a valid second-order method, yet a natural simultaneous ``small damping/small mesh'' choice \(\varepsilon\asymp h\) causes a nonzero global error on a cubic exact solution. The conclusion concerns the **particular two-stage construction** in [1] and this smooth nonautonomous test, not all Chebyshev integrators or fixed positive damping.

## Assumptions and scope

The step is constant within each computation; \(h=T/N\) for integer \(N\ge2\). The method is the recurrence (21), with the coefficients (24) and the order-two damping equations (9)–(10), of [1], specialized to two stages. Its branch is selected by \(\alpha,\omega,\beta\to1\) as \(\eta\uparrow1\), with \(\alpha,\beta,\omega>0\), and exists for all \(\eta\) sufficiently close to one. This is an exact-arithmetic calculation. The ODE is \(y'=t^2\), \(y(0)=0\); both starting values are exact and no solver startup error is used. All error statements are at the fixed final time \(T>0\), along sequences \(N\to\infty\) and \(0<\varepsilon_N\to0\). The first cited preprint has primary listed MSC code 65L04 and was submitted 2023-03-28.

## Proof

**1. Recover the actual two-stage coefficients.** The source writes the damping-polynomial pair as
\[
R^1(\mu)=\alpha[1+T_2(\omega+\beta\mu/4)],\qquad
R^0(\mu)=-eT_2(\omega+\beta\mu/4),
\]
where \(T_2(z)=2z^2-1\), with the second-order and preconsistency conditions. Put \(q=eT_2(\omega)\). The zero-input recurrence has coefficients \(1+q,-q\). For the source's actual stage realization, set
\[
\delta=\alpha-e,\quad
b=\delta T_2(\omega),\quad
\widetilde a=\alpha/\delta,\quad
\widetilde m_1=\beta/(4\omega),\quad
m_2=2\omega^2/T_2(\omega),\quad
\widetilde m_2=\beta\omega/[2T_2(\omega)].
\]
(The stage symbol \(\widetilde a\) is distinct from the output coefficient \(\alpha\).) Direct elimination of the stages when \(f(t,y)=g(t)\) gives
\[
Y_{n+1}=(1+q)Y_n-qY_{n-1}
+h\frac{\delta\beta\omega}{2}
\bigl[g(t_n+c_0h)+g(t_n+c_1h)\bigr],
\]
with \(c_0=\widetilde a-1\), \(c_1=c_0+\widetilde m_1\). In particular this uses the **published realization**, not an arbitrary other method having the same stability polynomials.

Preconsistency and exactness on \(y'=1\) yield \(\delta\beta\omega=1-q\). Exactness on \(y'=t\) then yields
\[
(1-q)(c_0+c_1)=1+q.
\]
The identity \(\alpha+(\alpha-e)T_2(\omega)=1\) gives
\[
\alpha=\frac{1+q}{1+q/e},\quad
\delta=\frac{1-e}{1+q/e},\quad
c_0=\frac{q+e}{1-e},\quad
c_1=c_0+\frac{1-q}{2(1-e)}.
\]
Substitution in the order-two condition reduces to the **exact scalar quadratic**
\[
3q^2+2eq+1-6e=0.
\]
The branch \(q\to1\) as \(e\uparrow1\) is precisely the positive-radical formula in the Finding. Its associated \(\omega^2=(1+q/e)/2\) and \(\beta=2\omega(1-q)/(1-e)\) are positive and tend to one, which proves it is the required local branch. Conversely, substituting these expressions satisfies both source order-two conditions, so no independent alternative discretization is being substituted.

**2. A one-step defect with a diverging constant.** Expanding \((t_n+c_jh)^2\), and using the two exact moment identities \(q+2w=1\) and \(2w(c_0+c_1)=1+q\), cancels all terms involving \(t_n\) against the exact cubic solution. The remaining defect is exactly \(h^3E_\varepsilon\) with the displayed expression. Expansion of the explicit radical at \(\varepsilon=0\) yields
\[
q=1-\varepsilon-\frac38\varepsilon^2+O(\varepsilon^3),\quad
c_0=\varepsilon^{-1}-1+O(\varepsilon),\quad
c_1=\varepsilon^{-1}-\frac34+O(\varepsilon),
\]
\[
E_\varepsilon=\varepsilon^{-1}-\frac{11}{8}+O(\varepsilon).
\]
Thus \(E_\varepsilon>0\) for sufficiently small \(\varepsilon\). In particular, the usual local-error \(O(h^3)\) bound is not uniform in the damping parameter.

**3. Exact accumulated error.** Set \(d=h^3E_\varepsilon\), \(e_n=Y_n-y(t_n)\), with \(e_0=e_1=0\). Subtracting exact values gives
\[
e_{n+1}=(1+q)e_n-qe_{n-1}+d.
\]
The first differences satisfy \(e_{n+1}-e_n=q(e_n-e_{n-1})+d\). Solving and summing yields the **finite-horizon identity**
\[
\mathcal E_N=\frac{h^3E_\varepsilon}{1-q}
\left[(N-1)-\frac{q(1-q^{N-1})}{1-q}\right].
\]
For small damping, \(1-q=\varepsilon+O(\varepsilon^2)\) and \(E_\varepsilon=\varepsilon^{-1}+O(1)\). If \(N\varepsilon\to\infty\), then \(q^N\to0\); substitution gives the first regime. If \(N\varepsilon\to\kappa T\in(0,\infty)\), then \(q^N\to e^{-\kappa T}\), giving the stated nonzero critical limit. If \(N\varepsilon\to0\), use \(1-q^j\sim j(1-q)\) uniformly for \(j\le N\) in the sum-of-differences form to obtain \(\mathcal E_N\sim h^3E_\varepsilon N(N-1)/2\), the third regime.

For the if-and-only-if assertion with arbitrary positive sequences, suppose \(\mathcal E_N\to0\) but \(\varepsilon/h\not\to\infty\). A subsequence has \(\varepsilon/h\le C\); passing to a further subsequence gives a finite nonnegative limit. A positive limit produces a strictly positive critical error, and zero produces divergence. This contradiction establishes necessity; the first regime supplies sufficiency.

## Verification

The standalone `verify.py` checks the rational polynomial-identity reduction and quadrature moment identities at exact rational points, independently computes the two-stage recurrence from the original source coefficients, compares the reduced forcing law with direct stages, checks the exact finite-horizon error against iteration, and tests the three asymptotic regimes. Execute `python3 verify.py` with only the Python standard library. The proof above, not the finite checks, establishes the general asymptotic and necessity assertions.

## Relationship to prior work

Moisa and Faleichik [1] construct the two-step stabilized family and publish the stage formulas, damping equations and a large first stage abscissa; **those constructions are prior work**. Their convergence experiments use fixed damping. The contribution here is the closed-form two-stage damping branch and an exact three-regime **mesh-dependent damping** error theorem on a nonautonomous forcing problem; this theorem is not asserted in [1]. Internal-stage robustness is a recognized concern for stabilized methods, including [2], which studies a different many-stage, one-step method and does not imply the forcing-error threshold here. A later, closely relevant two-step family [3] remains a residual originality risk because full text was not accessible; its abstract and bibliographic record do not decide whether it treats this precise simultaneous limit. Another prior finding on the **undamped** two-stage method concerns positivity for scalar autonomous decay rather than variable-damping consistency; its statement does not imply the present theorem. No global claim of uniqueness or independent publication priority is made.

## Limitations

This is a statement about the 2023 two-stage realization and its specified local damping branch; it does not describe a different 2024 family or a software implementation by the same authors. The counterexample is a smooth nonautonomous equation; no assertion is made that fixed damping leads to loss of convergence, or that the usual autonomous scalar stability interval is invalid. Floating-point rounding and higher stage counts are outside the theorem. The inaccessible full text in [3] means publication priority should receive independent checking.

## References

[1] A. Moisa and B. Faleichik, *Second order stabilized two-step Runge-Kutta methods*, arXiv:2303.16267v1, submitted 2023-03-28, especially equations (9)–(10), (21)–(25), sections 2–6 and Appendix A. https://arxiv.org/html/2303.16267v1

[2] D. Doehring, G. J. Gassner, and M. Torrilhon, *Many-Stage Optimal Stabilized Runge–Kutta Methods for Hyperbolic Partial Differential Equations*, Journal of Scientific Computing 99 (2024), article 28, especially discussion of internal stability. https://doi.org/10.1007/s10915-024-02478-5

[3] A. Moisa, *A family of two-step second order Runge–Kutta–Chebyshev methods*, Journal of Computational and Applied Mathematics 446 (2024), 115868. https://doi.org/10.1016/j.cam.2024.115868
