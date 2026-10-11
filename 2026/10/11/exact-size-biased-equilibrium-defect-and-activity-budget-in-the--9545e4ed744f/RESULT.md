# Exact size-biased equilibrium defect and activity budget in the Mackey–Glass equation

## Finding
Consider the Mackey–Glass delay equation
\[
\dot x(t)=\beta\frac{x(t-\tau)}{1+x(t-\tau)^n}-\gamma x(t),
\]
with \(\beta,\gamma,\tau,n>0\). Let a time-translation-invariant probability law be supported on a compact family of bounded complete strictly positive solutions. Define \(X=x(0)\), \(B=x(-\tau)\), and \(f(u)=u/(1+u^n)\).

Then the delayed production obeys the exact conditional calibration
\[
\mathbb E[f(B)\mid X]=\frac{\gamma}{\beta}X.
\]
Consequently a strictly positive compact stationary state is possible only if \(\beta>\gamma\). Writing
\[
x_* = \left(\frac{\beta}{\gamma}-1\right)^{1/n},
\]
the positive equilibrium scale, every such stationary state satisfies
\[
\frac{\mathbb E[X^{n+1}]}{\mathbb E[X]}-x_*^n
=
\frac{\mathbb E\!\left[\dfrac{X(X^n-x_*^n)^2}{1+X^n}\right]}{\mathbb E[X]}
\ge 0.
\]
The defect is zero exactly for the equilibrium trajectory \(x(t)\equiv x_*\).

There is also an exact activity budget
\[
\beta^2\operatorname{Var}(f(X))-\gamma^2\operatorname{Var}(X)
=
\mathbb E[\dot x(0)^2]
\ge0,
\]
and the nonlinear lag covariance is fixed by
\[
\operatorname{Cov}(X,f(B))
=
\frac{\gamma}{\beta}\operatorname{Var}(X).
\]
For every non-equilibrium stationary state, the activity budget is strict.

## Assumptions and scope
The probability law is defined on complete strictly positive solutions and is invariant under time translation. Compact support is used to justify differentiation under the expectation and to keep all displayed moments finite. No ergodicity assumption is required. The exponent \(n\) may be any positive real number because the solutions are strictly positive.

The statement concerns invariant statistics of the deterministic delay equation. It does not assert existence or uniqueness of a chaotic invariant measure for any particular parameter set.

## Proof
Time-translation invariance makes \(t\mapsto\mathbb E[G(x(t))]\) constant for every \(C^1\) function \(G\) on the compact current-state range. Differentiating at \(t=0\) gives
\[
0=\mathbb E[G'(X)\dot x(0)].
\]
Every continuous function on the compact range is the derivative of some \(C^1\) function there, so
\[
\mathbb E[\dot x(0)\mid X]=0.
\]
Using the differential equation yields
\[
\mathbb E[f(B)\mid X]=\frac{\gamma}{\beta}X.
\]
Taking expectations and using stationarity of the one-time marginal gives
\[
\beta\mathbb E[f(X)]=\gamma\mathbb E[X].
\]
Since \(X>0\), let \(m=\mathbb E[X]>0\) and introduce the size-biased law \(dQ=X\,dP/m\). Setting \(q=\gamma/\beta\), the preceding balance becomes
\[
\mathbb E_Q\left[\frac{1}{1+X^n}\right]=q.
\]
The left side is strictly between \(0\) and \(1\), hence \(0<q<1\), so \(\beta>\gamma\). Put \(a=(1-q)/q=x_*^n\) and \(Y=X^n\). Then
\[
\mathbb E_Q\left[\frac{Y-a}{1+Y}\right]=0.
\]
The pointwise identity
\[
Y-a=\frac{(Y-a)^2}{1+Y}+(1+a)\frac{Y-a}{1+Y}
\]
therefore gives
\[
\mathbb E_Q[Y]-a=\mathbb E_Q\left[\frac{(Y-a)^2}{1+Y}\right].
\]
Rewriting this equality in the original probability law produces the displayed size-biased defect formula. Its right side vanishes only when \(X^n=x_*^n\) almost surely, hence \(X=x_*\) almost surely. Time-translation invariance and continuity then force the complete trajectory to be constant, so the law is the equilibrium atom.

For the activity law, the conditional calibration gives
\[
\operatorname{Cov}(X,f(B))=\frac{\gamma}{\beta}\operatorname{Var}(X).
\]
Stationarity gives \(f(B)\) and \(f(X)\) the same marginal distribution. Expanding the square of \(\dot x(0)=\beta f(B)-\gamma X\), and using the preceding covariance and the mean balance, yields
\[
\mathbb E[\dot x(0)^2]
=
\beta^2\operatorname{Var}(f(X))-\gamma^2\operatorname{Var}(X).
\]
If the left side is zero, then \(\dot x(0)=0\) almost surely. Translation invariance makes the derivative vanish at every time almost surely, and continuity then makes the sampled complete solution constant. Thus equality again forces the positive equilibrium.

## Verification
The proof uses only the shift-invariance identity, the Mackey–Glass equation, and exact algebra. The companion script `checker.py` verifies the pointwise rational defect decomposition and the algebra reducing the variance expansion to the stated activity budget. Its recorded output is `CHECKER_OUTPUT.txt` and begins with `ALGEBRA_OK`.

For the commonly used normalization \(\beta=2\) and \(\gamma=1\), one has \(x_*=1\), so the defect becomes
\[
\frac{\mathbb E[X^{n+1}]}{\mathbb E[X]}-1
=
\frac{\mathbb E\!\left[\dfrac{X(X^n-1)^2}{1+X^n}\right]}{\mathbb E[X]}.
\]
This is an exact invariant-statistics check and not a numerical approximation.

## Relationship to prior work
Mackey and Glass introduced the physiological delay model in 1977. Later work developed stability, global-attractor bounds, periodic-orbit theory, bifurcation structure, and chaotic-attractor computations. A 2009 global-attractor paper treats the unimodal-feedback framework and lists primary classification \(34K20\); a 2022 same-equation bifurcation study lists primary classifications \(34K18\) and \(34K60\) and gives detailed numerical continuation and attractor-dimension analysis.

The inspected same-equation sources focus on stability, attractor geometry, periodic solutions, bifurcations, and chaos. Targeted searches for stationary moments, invariant-measure identities, conditional expectations, and the displayed rational defect did not locate the theorem above. The closest previously catalogued result concerns Nicholson's blowflies equation with exponential recruitment; that statement does not imply the rational Mackey–Glass defect because its feedback law is different. The conditional-calibration step is a general stationarity mechanism, while the exact squared defect is specific to the reciprocal Mackey–Glass feedback.

## Limitations
The result is conditional on the existence of a compact time-translation-invariant law supported on strictly positive complete solutions. It does not prove existence, ergodicity, uniqueness, mixing, or chaos for any parameter values. The literature on the Mackey–Glass equation is extensive, so the source comparison reduces but cannot eliminate the possibility of an unlocated equivalent identity. The result is primarily an exact invariant-statistics constraint and diagnostic, not a new bifurcation theorem.

## References
M. C. Mackey and L. Glass, “Oscillation and chaos in physiological control systems,” *Science* 197 (1977), 287–289. DOI: 10.1126/science.267326. Publication date: 1977-07-15.

E. Liz and G. Röst, “On the global attractor of delay differential equations with unimodal feedback,” *Discrete and Continuous Dynamical Systems* 24 (2009), 1215–1224. DOI: 10.3934/dcds.2009.24.1215.

H.-O. Walther, “The impact on mathematics of the paper ‘Oscillation and Chaos in Physiological Control Systems’ by Mackey and Glass in Science, 1977,” arXiv:2001.09010.

V. Duruisseaux and A. R. Humphries, “Bistability, bifurcations and chaos in the Mackey-Glass equation,” *Journal of Computational Dynamics* 9 (2022), 421–450. DOI: 10.3934/jcd.2022009.
