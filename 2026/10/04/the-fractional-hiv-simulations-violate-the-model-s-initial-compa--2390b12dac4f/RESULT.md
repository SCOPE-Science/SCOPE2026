# The fractional HIV simulations violate the model’s initial compatibility and history identity

## Finding

The paper studies the autonomous Caputo–Fabrizio HIV-1 system
\[
{}^{CF}D_t^\gamma x=s_0-\mu x-\beta xz,
\]
\[
{}^{CF}D_t^\gamma y=\beta xz-\varepsilon y,
\]
\[
{}^{CF}D_t^\gamma z=cy-\zeta z,
\qquad 0<\gamma\le1.
\]
For \(0<\gamma<1\), its Definition 2.1 is the standard Caputo–Fabrizio derivative
\[
{}^{CF}D_t^\gamma u(t)
=
\frac{M(\gamma)}{1-\gamma}
\int_0^t
u'(s)e^{-\gamma(t-s)/(1-\gamma)}\,ds.
\]

This definition forces an initial compatibility condition that the paper's fractional simulations violate. If \(X\) is absolutely continuous and
\[
{}^{CF}D_t^\gamma X(t)=F(X(t)),
\]
then
\[
{}^{CF}D_t^\gamma X(t)\to0
\qquad (t\downarrow0),
\]
while continuity of \(F\) and \(X\) gives
\[
F(X(t))\to F(X(0)).
\]
Thus every such solution must satisfy
\[
F(X(0))=0.
\]

For Figures 1–3 the paper uses
\[
X(0)=(100,0,1)
\]
and the parameter values
\[
s_0=0.272,
\quad
\mu=0.00136,
\quad
\beta=0.00027,
\quad
\varepsilon=0.33,
\quad
c=50,
\quad
\zeta=2.
\]
The exact residual is
\[
F(X(0))
=
(0.109,0.027,-2),
\]
so the compatibility condition fails in all three coordinates. Consequently there is no absolutely continuous solution of the stated fractional initial-value problem with these data for the plotted orders
\[
\gamma=0.85,
\quad
0.9,
\quad
0.95.
\]
The \(\gamma=1\) curve is an ordinary differential-equation calculation and is not subject to this particular obstruction.

The paper's own derivation then changes the integral equation in two mutually inconsistent ways. Definition 2.2 gives
\[
{}^{CF}I_t^\gamma g(t)
=
\frac{1-\gamma}{M(\gamma)}g(t)
+
\frac{\gamma}{M(\gamma)}\int_0^t g(s)\,ds.
\]
But equation (3.4) uses, componentwise, an algebraic term proportional to
\[
g(t)-g(0),
\]
which is absent from Definition 2.2. This subtraction makes arbitrary initial data look compatible by construction, but it no longer follows from the displayed Caputo–Fabrizio integral.

Section 4 changes the equation again. Its equation (4.3) contains an exponentially weighted memory term of the form
\[
Q(t)=\int_0^t \Xi(s)e^{-k(t-s)}\,ds,
\qquad
k=\frac{\gamma}{1-\gamma},
\]
although Definition 2.2 contains an unweighted ordinary integral. Moreover, subtracting the equations at consecutive time levels requires the exact identity
\[
Q(t+h)-Q(t)
=
(e^{-kh}-1)Q(t)
+
\int_t^{t+h}
e^{-k(t+h-s)}\Xi(s)\,ds.
\]
The step leading to equation (4.6) replaces this with an unweighted integral over only the newest interval, thereby dropping the entire history term.

For the constant test input
\[
\Xi(s)\equiv1,
\]
one has
\[
Q(t)=\frac{1-e^{-kt}}{k}
\]
and hence
\[
Q(t+h)-Q(t)
=
\frac{e^{-kt}(1-e^{-kh})}{k},
\]
whereas the replacement in the paper is simply \(h\). These expressions are generically unequal. Expanding the exact identity gives
\[
(e^{-kh}-1)Q(t)
=
-khQ(t)+O(h^2),
\]
so the missing history contribution is generally first order in the step size.

The fractional simulations are therefore not established as numerical solutions of the displayed initial-value problem. This affects the fractional trajectories in Figures 1–3 directly, and it prevents the later plots produced by the same recurrence from serving, by themselves, as evidence for oscillation or chaos of the stated Caputo–Fabrizio system.

## Assumptions and scope

The compatibility statement assumes an absolutely continuous state trajectory, exactly the regularity needed for the Caputo–Fabrizio derivative written in Definition 2.1, and a continuous autonomous vector field \(F\), which the polynomial HIV vector field has.

The numerical-history objection concerns equations (4.3)–(4.6) exactly as printed. It does not assert that every three-step Adams–Bashforth formula appearing elsewhere in the fractional-calculus literature is invalid. It establishes that the recurrence in this paper is not derived from its own displayed history equation by the algebra written there.

The result does not rule out oscillations or chaos in a different, explicitly modified model with a compatible initial formulation. It also does not challenge the ordinary differential-equation case \(\gamma=1\).

## Proof

Let
\[
({}^{CF}D_t^\gamma u)(t)
=
\frac{M(\gamma)}{1-\gamma}
\int_0^t
u'(s)e^{-k(t-s)}\,ds,
\qquad
k=\frac{\gamma}{1-\gamma}.
\]
For an absolutely continuous \(u\), the derivative \(u'\) is integrable. Since the exponential factor is bounded by one,
\[
\left|{}^{CF}D_t^\gamma u(t)\right|
\le
\frac{M(\gamma)}{1-\gamma}
\int_0^t |u'(s)|\,ds.
\]
Absolute continuity implies that the right-hand side tends to zero as \(t\downarrow0\). Applying this componentwise to \(X\) gives
\[
{}^{CF}D_t^\gamma X(t)\to0.
\]
If the differential equation holds for positive \(t\), continuity gives
\[
0
=
\lim_{t\downarrow0}{}^{CF}D_t^\gamma X(t)
=
\lim_{t\downarrow0}F(X(t))
=
F(X(0)).
\]

For the source initial condition and parameters,
\[
F_1
=
0.272-(0.00136)(100)-(0.00027)(100)(1)
=
0.109,
\]
\[
F_2
=
(0.00027)(100)(1)-(0.33)(0)
=
0.027,
\]
and
\[
F_3
=
(50)(0)-(2)(1)
=
-2.
\]
Therefore
\[
F(X(0))\ne0,
\]
proving nonexistence of an absolutely continuous solution for these fractional initial data.

For the numerical-history step, define
\[
Q(t)=\int_0^t \Xi(s)e^{-k(t-s)}\,ds.
\]
Splitting the integral at \(t\) gives
\[
\begin{aligned}
Q(t+h)
&=
\int_0^t \Xi(s)e^{-k(t+h-s)}\,ds
+
\int_t^{t+h}\Xi(s)e^{-k(t+h-s)}\,ds\\
&=
e^{-kh}Q(t)
+
\int_t^{t+h}\Xi(s)e^{-k(t+h-s)}\,ds.
\end{aligned}
\]
Subtracting \(Q(t)\) yields the exact identity
\[
Q(t+h)-Q(t)
=
(e^{-kh}-1)Q(t)
+
\int_t^{t+h}\Xi(s)e^{-k(t+h-s)}\,ds.
\]
No algebraic simplification turns this expression into the unweighted newest-interval integral used in the paper. The constant-input example \(\Xi\equiv1\) gives a direct counterexample to that replacement.

## Verification

The bundled `verify.py` evaluates the source initial residual with exact rational arithmetic and checks
\[
F(X(0))=
\left(
\frac{109}{1000},
\frac{27}{1000},
-2
\right).
\]

It also checks the weighted-history identity numerically for a constant input. For
\[
\gamma=0.9,
\quad
k=9,
\quad
t=0.5,
\quad
h=0.01,
\]
the exact memory increment is approximately
\[
1.06265\times10^{-4},
\]
whereas the unweighted newest-interval replacement equals
\[
0.01.
\]
The discrepancy is not used as a numerical proof; it merely replays the exact analytic identity above.

## Relationship to prior work

Ahmad et al. (2021), DOI 10.3934/math.2022265, provide the HIV model, the Caputo–Fabrizio definitions, the existence construction, the three-step recurrence, and the simulations examined here.

Diethelm, Garrappa, Giusti, and Stynes (2020), DOI 10.1515/fca-2020-0032, explain the general zero-initial-value restriction for nonsingular-kernel derivatives and note that an autonomous initial-value problem can be compatible only when the vector field vanishes at the prescribed initial state. That general issue is established prior art and is not claimed as new here. The source-specific content is the exact residual for the published HIV data and the additional internal mismatch among Definition 2.2, equation (3.4), equation (4.3), and the history subtraction leading to equation (4.6).

Shankar and Bora (2023), DOI 10.1016/j.fraope.2023.100043, likewise discuss compatibility and stability questions for Caputo–Fabrizio evolution equations. Their results reinforce the need to distinguish a mathematically compatible Caputo–Fabrizio problem from a formally written autonomous equation, but they do not inspect this HIV paper's numerical derivation.

## Limitations

The general initial-compatibility phenomenon is not new; the new claim is its exact consequence for this published model and the separate history-identity failure in the source's numerical derivation.

The paper may have intended a modified regularized formulation different from the equations it prints. Such a model would have to be stated and analyzed separately.

The finding does not prove that no alternative fractional HIV model can oscillate or behave chaotically. It establishes only that the displayed simulations are not certified as solutions of the displayed Caputo–Fabrizio initial-value problem.

## References

1. S. Ahmad, A. Ullah, M. Partohaghighi, S. Saifullah, A. Akgül, F. Jarad, “Oscillatory and complex behaviour of Caputo-Fabrizio fractional order HIV-1 infection model,” AIMS Mathematics 7 (2022), 4778–4792. DOI: 10.3934/math.2022265.
2. K. Diethelm, R. Garrappa, A. Giusti, M. Stynes, “Why fractional derivatives with nonsingular kernels should not be used,” Fractional Calculus and Applied Analysis 23 (2020), 610–634. DOI: 10.1515/fca-2020-0032.
3. M. Shankar, S. N. Bora, “Stabilization and asymptotic stability of the Caputo–Fabrizio fractional-order linear and semilinear evolution equations,” Fractional Operators and Applications 1 (2023), 100043. DOI: 10.1016/j.fraope.2023.100043.
