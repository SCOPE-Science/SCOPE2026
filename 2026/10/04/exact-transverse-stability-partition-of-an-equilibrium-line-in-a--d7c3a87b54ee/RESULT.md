# Exact transverse-stability partition of an equilibrium line in an exponential hyperchaotic flow

## Finding

For the Li–Wu–Zhang four-dimensional flow \(\dot x_1=a(x_2-x_1)+x_4\), \(\dot x_2=bx_1+x_2-x_1x_3\), \(\dot x_3=-cx_3+e^{x_1x_2}\), \(\dot x_4=dx_2x_3\), assume \(a>0\), \(c>0\), and \(b=1/c\). Its equilibrium line \(E_\xi=(\xi,0,1/c,a\xi)\) has the exactly factored characteristic polynomial \(\chi_\xi(\lambda)=\lambda(\lambda+a)(\lambda^2+(c-1)\lambda+\xi^2-c)\). Consequently its three transverse eigenvalues all have negative real part exactly when \(c>1\) and \(\xi^2>c\); when \(\xi^2<c\) there is one positive and one negative eigenvalue from the quadratic factor, at \(\xi^2=c\) an additional zero eigenvalue appears, for \(c=1\) and \(\xi^2>1\) the transverse pair is purely imaginary, and for \(0<c<1\) with \(\xi^2>c\) that pair has positive real part. No individual point of the line can be locally asymptotically stable because every neighborhood contains distinct equilibria. Thus the stability condition stated as Equation (7) in the source is not valid: at its own line-equilibrium parameters \(a=2\), \(b=3/8\), \(c=8/3\), \(d=0.1\), the point \(E_0\) satisfies the stated inequality but has spectrum \(\{0,-2,1,-8/3\}\), while the two numerically reported limiting points \(\xi\approx1.6385\) and \(\xi\approx2.0070\) lie in the actual transversely attracting region \(|\xi|>\sqrt{8/3}\); the latter even violates the source's stated inequality.

## Assumptions and scope

Consider the smooth four-dimensional ODE
\[
\dot x_1=a(x_2-x_1)+x_4,\qquad
\dot x_2=bx_1+x_2-x_1x_3,
\]
\[
\dot x_3=-cx_3+e^{x_1x_2},\qquad
\dot x_4=dx_2x_3,
\]
with \(a>0\), \(c>0\), and the line-equilibrium parameter relation \(b=1/c\). The source treats \(d>0\); the linear spectrum along the equilibrium line below is independent of \(d\), so the algebraic classification itself does not need a sign assumption on \(d\). The result is local and spectral: it classifies normal attraction, saddle behavior, and neutral boundaries of the equilibrium line. It does not claim global convergence of arbitrary initial conditions or make any statement about the source's hyperchaotic regime away from \(b=1/c\).

## Proof

When \(b=1/c\), direct substitution shows that every
\[
E_\xi=(\xi,0,1/c,a\xi),\qquad \xi\in\mathbb R,
\]
is an equilibrium. The Jacobian at \(E_\xi\) is
\[
J_\xi=
\begin{pmatrix}
-a&a&0&1\\
0&1&-\xi&0\\
0&\xi&-c&0\\
0&d/c&0&0
\end{pmatrix}.
\]
Its characteristic polynomial factors exactly as
\[
\det(\lambda I-J_\xi)
=\lambda(\lambda+a)\bigl(\lambda^2+(c-1)\lambda+\xi^2-c\bigr).
\]
Thus one eigenvalue is the tangent zero eigenvalue of the equilibrium line and one transverse eigenvalue is \(-a<0\). The remaining two have sum \(1-c\) and product \(\xi^2-c\).

If \(\xi^2<c\), their product is negative, so one is positive and one is negative. If \(\xi^2=c\), one of them is zero, producing a second zero eigenvalue. If \(\xi^2>c\), their product is positive. For \(c>1\), their sum is negative, hence both have negative real part; for \(c=1\), their sum is zero and they are \(\pm i\sqrt{\xi^2-1}\); for \(0<c<1\), their sum is positive, so they have positive real part. Therefore all three nonzero eigenvalues have negative real part exactly for
\[
c>1,\qquad \xi^2>c.
\]
On any compact subsegment satisfying these strict inequalities, standard normal-hyperbolicity theory gives local exponential attraction transverse to the equilibrium line.

An individual \(E_\xi\) cannot be locally asymptotically stable in the full state space: every neighborhood of \(E_\xi\) contains another equilibrium \(E_\eta\) with \(\eta\ne\xi\), and that solution remains at \(E_\eta\) rather than converging to \(E_\xi\).

For the source's line-equilibrium example \(a=2\), \(b=3/8\), \(c=8/3\), \(d=0.1\), Equation (7) reduces to \(3-\xi^2>0\). At \(\xi=0\) this condition holds, yet the exact factorization becomes
\[
\chi_0(\lambda)=\lambda(\lambda+2)(\lambda-1)(\lambda+8/3),
\]
so the equilibrium has a positive eigenvalue. Conversely, the source reports convergence to \(\xi\approx1.6385\) and \(\xi\approx2.0070\). Both satisfy \(\xi^2>8/3\), exactly the criterion above, while \(2.0070^2>3\) makes the latter violate the source's Equation (7). The exact partition therefore matches both reported convergence examples and also exposes a direct counterexample to the published inequality.

## Verification

`artifacts/verify_line_equilibria.py` reconstructs the vector field and Jacobian symbolically, verifies the equilibrium line, factors the characteristic polynomial, checks the source-parameter counterexample \(\xi=0\), and checks the two rounded limiting coordinates quoted in the source. Its recorded output ends in `VERIFY_OK`.

The proof of the stability partition uses only the signs of the sum and product of the quadratic pair. The pointwise non-asymptotic-stability statement follows directly from the existence of the equilibrium continuum and does not depend on numerical simulation.

## Relationship to prior work

The primary article introduces this exponential four-dimensional flow, derives the same unfactored characteristic polynomial for the equilibrium line, states a Routh–Hurwitz condition in its Equation (7), and presents two trajectories converging to points on that line for \(a=2\), \(b=3/8\), \(c=8/3\), \(d=0.1\). The factorization above is not stated there. It yields the complete transverse spectral partition and shows that the published Equation (7) is not a valid stability criterion.

Targeted searches for the exact source title, the line-equilibrium parameter relation, the factored quadratic condition, normal attraction, and equivalent stability statements found the source article and later papers that cite it as a hyperchaotic-system example, but no inspected source supplied this factorization or correction. Semantic searches of published mathematical findings returned stability results for other dynamical systems, not this vector field.

## Limitations

The theorem is a local spectral and normal-hyperbolicity result on the special surface \(b=1/c\). It does not prove a global basin description, does not identify which point of the attracting part of the line is selected by a given initial condition, and does not alter the source's numerical hyperchaos claim for parameters with \(b\ne1/c\). The originality search cannot exclude unindexed literature or an equivalent result hidden by a non-obvious change of variables.

## References

Li, S.; Wu, Y.; Zhang, X. “Analysis and Synchronization of a New Hyperchaotic System with Exponential Term.” *Mathematics* 9 (2021), 3281. DOI: 10.3390/math9243281. Published 17 December 2021.

MSC2020 classification 37C75: stability theory for smooth dynamical systems.
