# The mean-square stability theorem analyzes a different stochastic predator–prey model
## Finding
Talapatra's stochastic dual-prey–predator model is introduced as
\[
dX=b(X)\,dt+\Sigma(X)\,dB,
\]
with
\[
\Sigma(x_1,x_2,y)=
\operatorname{diag}(\alpha_1x_1,\alpha_2x_2,\alpha_3y).
\]
Let
\[
E^*=(x_1^*,x_2^*,y^*)\in(0,\infty)^3
\]
be a positive equilibrium of the deterministic drift, so
\[
b(E^*)=0.
\]
Because the source assumes positive noise intensities,
\[
\Sigma(E^*)=
\operatorname{diag}(\alpha_1x_1^*,\alpha_2x_2^*,\alpha_3y^*)\ne0.
\]
Thus the constant process at \(E^*\) is not a solution of the stochastic model printed as Equation (2).

Section 3 changes the stochastic model before its mean-square analysis. Equation (13) uses the centered diffusion
\[
\operatorname{diag}\bigl(\alpha_1(x_1-x_1^*),\alpha_2(x_2-x_2^*),\alpha_3(y-y^*)\bigr),
\]
so after the change of variables
\[
\tilde u=X-E^*,
\]
Equation (15) has zero diffusion at \(\tilde u=0\). Theorem 3.2 then proves mean-square stability of that zero solution.

That homogeneous perturbation system is not the translation or linearization of Equation (2). Translating Equation (2) gives the affine diffusion
\[
\operatorname{diag}\bigl(\alpha_1(x_1^*+\tilde u_1),\alpha_2(x_2^*+\tilde u_2),\alpha_3(y^*+\tilde u_3)\bigr),
\]
which contains a nonzero constant stochastic forcing at \(\tilde u=0\). Consequently, the Section 3 mean-square theorem does not establish stability of the positive deterministic equilibrium for the stochastic system formulated in Section 2.

## Assumptions and scope
The statement concerns Equation (2) exactly as printed in the source, with
\[
\alpha_1>0,\qquad \alpha_2>0,\qquad \alpha_3>0,
\]
and a strictly positive deterministic equilibrium
\[
E^*=(x_1^*,x_2^*,y^*).
\]
No numerical parameter calibration is needed.

The finding distinguishes two stochastic models that share the same deterministic drift. It does not assert that equilibrium-centered noise is inappropriate. Such a choice is mathematically legitimate when stated as the model. It also does not re-audit the paper's positivity, persistence, or stationary-distribution theorems for Equation (2).

## Proof
Write the stochastic model of Equation (2) as
\[
dX=b(X)\,dt+\Sigma(X)\,dB,
\qquad
\Sigma(X)=\operatorname{diag}(\alpha_1X_1,\alpha_2X_2,\alpha_3X_3).
\]
At the positive deterministic equilibrium,
\[
b(E^*)=0,
\]
but
\[
\|\Sigma(E^*)\|_F^2
=(\alpha_1x_1^*)^2+(\alpha_2x_2^*)^2+(\alpha_3y^*)^2>0.
\]
An equilibrium solution of an Itô SDE must make both its drift and diffusion vanish. Therefore the constant process
\[
X(t)\equiv E^*
\]
is not a solution of Equation (2).

The same conclusion follows quantitatively from Itô's formula. Start Equation (2) at
\[
X(0)=E^*
\]
and set
\[
V(X)=\|X-E^*\|_2^2.
\]
Then
\[
dV=
2(X-E^*)^\top b(X)\,dt
+\|\Sigma(X)\|_F^2\,dt
+dM_t,
\]
where \(M_t\) is a local martingale. Taking expectations and using continuity of the coefficients at \(E^*\) gives
\[
\frac{d}{dt}\mathbb E V(X(t))\Big|_{t=0+}
=
\|\Sigma(E^*)\|_F^2>0.
\]
Hence
\[
\mathbb E\|X(t)-E^*\|_2^2
=
\|\Sigma(E^*)\|_F^2t+o(t).
\]
In particular, the deterministic equilibrium cannot be the mean-square-stable zero-displacement solution of the printed stochastic system.

Now translate Equation (2) by setting
\[
U=X-E^*.
\]
Its exact diffusion becomes
\[
\Sigma(E^*+U)
=
\operatorname{diag}\bigl(
\alpha_1(x_1^*+U_1),
\alpha_2(x_2^*+U_2),
\alpha_3(y^*+U_3)
\bigr).
\]
Thus the first-order stochastic equation near \(U=0\) necessarily retains the additive Brownian term
\[
\operatorname{diag}(\alpha_1x_1^*,\alpha_2x_2^*,\alpha_3y^*)\,dB.
\]

Equation (13) instead replaces the Section 2 diffusion by
\[
\operatorname{diag}(\alpha_1U_1,\alpha_2U_2,\alpha_3U_3),
\]
which vanishes at the origin. Equation (15) is the linearization of this newly centered system. The source's own Theorem 3.1 is explicitly a criterion for stability of the trivial solution of Equation (15), and Theorem 3.2 applies that criterion. Since the trivial solution does not correspond to a solution of the translated Equation (2), the implication cannot be transferred back to Equation (2).

The distinction is not confined to one typographical occurrence. In Section 6 the source rewrites Equation (2) for the stationary-distribution analysis and again uses
\[
\alpha_1x_1\,dB_1,
\qquad
\alpha_2x_2\,dB_2,
\qquad
\alpha_3y\,dB_3.
\]
Thus the paper itself treats the abundance-proportional and equilibrium-centered diffusions as different formulas in different parts of the analysis.

## Verification
The bundled script `verification/verify.py` uses exact rational arithmetic to replay the algebraic distinction between the two diffusion specifications. For representative strictly positive equilibrium coordinates and positive noise intensities, it verifies that the translated abundance-proportional diffusion has a nonzero constant term, while the centered diffusion vanishes at zero displacement. It also computes the positive Itô-generator coefficient
\[
\|\Sigma(E^*)\|_F^2.
\]

The numerical replay is not the proof of the universal statement. The proof is the exact translation of the diffusion matrix and the Itô identity above.

## Relationship to prior work
The motivating article prints the abundance-proportional noise in Equation (2), switches to equilibrium-centered noise in Equation (13), and then proves stability of the zero solution of Equation (15). Later, its stationary-distribution section explicitly returns to the abundance-proportional Equation (2). The source does not state that Section 3 has introduced a different stochastic model before using its result to discuss the positive equilibrium of the original system.

Equilibrium-centered noise is itself established modeling practice. For example, Shao and Kong explicitly introduce a separate stochastic predator–prey system whose random disturbances are proportional to deviations from a deterministic equilibrium before studying stochastic behavior around that equilibrium. That prior supports the mathematical distinction made here: centered noise can make the deterministic equilibrium an exact stochastic equilibrium, whereas abundance-proportional noise generally does not.

The present contribution is therefore not the general observation that different diffusion coefficients produce different SDEs. It is the source-specific implication that the mean-square theorem in the 2025 dual-prey–predator article is a theorem for its centered auxiliary model rather than for Equation (2).

## Limitations
The result does not quantify long-time fluctuations around \(E^*\) for Equation (2). A stochastic system with abundance-proportional noise may have a stationary distribution concentrated near the deterministic equilibrium when noise is small; that is a different question from mean-square stability of a constant equilibrium solution.

The result also does not invalidate the centered-noise model of Equation (13). If that is the intended model for the stability section, its analysis must be interpreted as applying to that explicitly modified SDE.

No claim is made here about the correctness of the paper's numerical calibration, harvesting conclusions, persistence thresholds, or stationary-distribution theorem beyond the precise model-identification issue proved above.

## References
1. C. Talapatra, “Stochastic Dynamics of Dual-Prey–Predator Interactions under Harvesting Pressure: Insights from the California Current Ecosystem,” Earthline Journal of Mathematical Sciences 15 (2025), 989–1020. DOI: 10.34198/ejms.15625.9891020.
2. Y. Shao, W. Kong, “A Predator–Prey Model with Beddington–DeAngelis Functional Response and Multiple Delays in Deterministic and Stochastic Environments,” Mathematics 10 (2022), 3378. DOI: 10.3390/math10183378.
