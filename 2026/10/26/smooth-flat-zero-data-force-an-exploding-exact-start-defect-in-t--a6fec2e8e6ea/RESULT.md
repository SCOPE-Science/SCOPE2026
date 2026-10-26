# Smooth flat-zero data force an exploding exact-start defect in two-stage Gaussian RBF Runge–Kutta integration

## Finding

For the uncapped two-stage Gaussian radial-basis-function Runge–Kutta method with its exact derivative-based shape parameter, one fixed smooth, globally state-Lipschitz scalar initial-value problem defeats even *local consistency along every sufficiently fine uniform grid*. At a grid node immediately to the right of an irrational flat zero of the exact solution, the numerical output produced from the **exact** datum exceeds the next exact value by a quantity tending to positive infinity. No grid node coincides with the zero, so the method's shape quotient is finite on every tested mesh.

Specifically, let \(\tau=\sqrt2/4\), define \(g(\tau)=0\) and \(g(t)=\exp[-1/(t-\tau)^2]\) for \(t\ne\tau\), and set
\[
 f(t,v)=v+g'(t)-g(t),\qquad u(0)=g(0),\quad 0\le t\le1.
\]
The unique exact solution is \(u(t)=g(t)\). Let \(\Phi_h(t,v)\) be the original two-stage method defined below. For **every** integer \(N\ge4\), with \(h=1/N\), \(n=\lceil N\tau\rceil\), and \(t=n/N\), its exact-data defect satisfies
\[
 \Phi_h(t,g(t))-g(t+h)
 \ge \frac{3h}{4}\exp\left(\frac1{2h^4}\right)-K,
\]
where \(K<\infty\) is a constant independent of \(N\). In particular the defect diverges to \(+\infty\) as \(N\to\infty\).

## Assumptions and scope

The method from Gu, Chen and Jung [1, equations (12) and (15)] is, in scalar form,
\[
 \begin{aligned}
 k_1&=f(t,v),\\
 w&=v\exp\!\left(-\epsilon^2\frac{4h^2}{9}\right)+\frac{2h}{3}k_1,\\
 k_2&=f\left(t+\frac{2h}{3},w\right),\\
 \Phi_h(t,v)&=v+h\left(\frac14 k_1+\frac34k_2\right),\\
 \epsilon^2&=-\frac{f_t(t,v)+f_v(t,v)f(t,v)}{2v}.
 \end{aligned}
\]
Here no shape clipping, limiting, substitution, or special zero handling is applied. The formula is evaluated in exact real arithmetic using \(\epsilon^2\), which is allowed to be negative (the original method allows an imaginary \(\epsilon\)). The stage is well-defined whenever \(v\ne0\). The claim is about **a single exact-data step at a mesh-dependent node**, not the recursively produced global numerical solution.

The ODE has \(f\in C^\infty([0,1]\times\mathbb R)\), \(\partial_vf=1\), global state Lipschitz constant one, and bounded smooth exact solution. The flat function is strictly positive at every rational mesh node because \(\tau\) is irrational.

## Proof

**1. Smoothness and exact trajectory.** The standard flat-function extension satisfies \(g\in C^\infty[0,1]\), with all derivatives vanishing at \(\tau\). The function \(f(t,v)=v+g'(t)-g(t)\) is globally Lipschitz in \(v\) with constant one. Substitution gives \(f(t,g(t))=g'(t)\), so uniqueness of the scalar IVP yields \(u=g\).

**2. The exact shape exponent.** Fix any integer \(N\ge4\). With \(h=1/N\), choose \(n=\lceil N\tau\rceil\) and \(t=n/N\). Irrationality of \(\tau\) gives \(0<\delta:=t-\tau<h\); furthermore \(t+h\le1\). In particular \(g(t)>0\), and the shape quotient exists. At \(v=g(t)\), the derivative identity \(f_t+f_vf=g''\) implies
\[
 \epsilon^2=-\frac{g''(t)}{2g(t)},\qquad
 \frac{g''(t)}{g(t)}=\frac4{\delta^6}-\frac6{\delta^4}.
\]
Thus the exponent applied to the first-stage datum is
\[
 E:=-\epsilon^2\frac{4h^2}{9}
 =\frac{2h^2}{9}\left(\frac4{\delta^6}-\frac6{\delta^4}\right),
\]
which is positive for \(h\le1/4\).

**3. An all-mesh, quantitative lower bound.** Rearrangement gives the exact identity
\[
 E-\frac1{\delta^2}=\frac{h^2}{\delta^6}
 \left(\frac89-\frac43\delta^2-\frac{\delta^4}{h^2}\right).
\]
Because \(0<\delta<h\le1/4\), the factor in parentheses is at least
\[
 \frac89-\frac43h^2-h^2\ge \frac{107}{144}>\frac12.
\]
Consequently
\[
 g(t)e^E=\exp(E-\delta^{-2})
 \ge\exp\!\left(\frac{h^2}{2\delta^6}\right)
 \ge\exp\!\left(\frac1{2h^4}\right).
\]
The key lower bound is uniform in the irrational grid offset \(\delta/h\); it therefore holds along *every* uniform mesh refinement, not merely a Diophantine subsequence.

**4. The exact full step.** The first stage is \(k_1=g'(t)\). Put \(s=t+2h/3\). Since \(f(s,w)=w+g'(s)-g(s)\), direct substitution yields
\[
 \begin{aligned}
 \Phi_h(t,g(t))&=B_N+C_N,\\
 B_N&=\frac{3h}{4}\exp(E-\delta^{-2}),\\
 C_N&=g(t)+h\left[\frac14 g'(t)
 +\frac34\left(\frac{2h}{3}g'(t)+g'(s)-g(s)\right)\right].
 \end{aligned}
\]
Both \(g\) and \(g'\) are bounded on \([0,1]\), so \(|C_N|\) is bounded independently of \(N\), as is \(g(t+h)\). The lower bound in Step 3 gives
\[
 \Phi_h(t,g(t))-g(t+h)
 \ge \frac{3h}{4}\exp\!\left(\frac1{2h^4}\right)-K
 \longrightarrow+\infty.
\]
This proves the claim with explicit quantifiers and no numerical approximation.

## Verification

The standalone `verify.py` reproduces \(g''/g=4/\delta^6-6/\delta^4\) with symbolic differentiation, verifies the analytic lower bound and the exact step decomposition in high-precision and log-domain arithmetic on eleven uniform meshes, and checks direct method outputs on four small meshes. It returned `VERIFY_OK 91 exact symbolic identities and mesh/log-domain diagnostics`. These finite tests are only consistency checks; the proof of the all-mesh assertion is Steps 1–4.

Run with Python and installed `sympy` and `mpmath`: `python verify.py`. No other input files are needed.

## Relationship to prior work

Gu, Chen and Jung [1] introduced the two-stage RBF Runge–Kutta method and the shape choice \(\epsilon^2=-u''/(2u)\); these are **not new**. Their two-stage convergence theorem [1, Section 4.1] explicitly assumes bounded \(\epsilon^2\). The example above violates that hypothesis, so it does **not** refute the theorem. Instead it proves that mere smoothness of the underlying problem and Lipschitz continuity in the state do not suffice for even local consistency under the uncapped formula.

Gu and Jung [2] already identify that adaptive Gaussian RBF shape formulas may become singular because of their denominator and refer to a remedy; Gu and Jung [3] develop related adaptive MQ-RBF methods. The present observation is **not** the known possibility of division by zero. It establishes an unbounded, positive, quantifiable exact-data defect for one smooth IVP on every fine uniform grid **without any division by zero at the chosen mesh nodes**. It is not a claim about the behavior of the previously proposed remedies, clipping policies, or alternative RBF schemes.

## Limitations

This example uses a solution flat at a single irrational interior time, an uncapped derivative-based shape prescription, and exact arithmetic. It does not claim that actual recursively propagated approximations diverge, nor that other RBF Runge–Kutta stages, revised methods, or shape-regularized schemes fail. The lower bound concerns one mesh-selected exact-data step for every \(N\ge4\). No publication-level claim of first discovery is made beyond the literature comparisons recorded separately.

## References

[1] J. Gu, X. Chen, J.-H. Jung, *Explicit radial basis function Runge-Kutta methods*, arXiv:2403.08253v1, first submitted 13 March 2024, Sections 3.1 and 4.1. https://arxiv.org/abs/2403.08253

[2] J. Gu and J.-H. Jung, *Adaptive Gaussian radial basis function methods for initial value problems: Construction and comparison with adaptive multiquadric radial basis function methods*, Journal of Computational and Applied Mathematics 381 (2021), 113036. https://doi.org/10.1016/j.cam.2020.113036

[3] J. Gu and J.-H. Jung, *Adaptive Radial Basis Function Methods for Initial Value Problems*, Journal of Scientific Computing 82 (2020), article 47. https://doi.org/10.1007/s10915-020-01140-0
