# A sharp kurtosis-design transition for distributed resetting of a trapped run-and-tumble particle

## Finding
Consider a one-dimensional run-and-tumble particle with harmonic restoring drift, fair spin reinitialization, and independently sampled random reset positions. For any fixed strictly positive confinement, self-propulsion, tumbling, and Poisson reset rates, minimize the **stationary positional kurtosis** over **all centered probability reset laws with finite fourth moment**, with no support or second-moment restriction.

Set \(q=r/\kappa>0\), \(g=2\gamma/\kappa>0\), and
\[
q_c(g)=\frac{1-g+\sqrt{g^2+2g+13}}{2}>1.
\]
Write \(K(\mu)=\mathbb E[X^4]/(\mathbb E[X^2])^2\) for the unique stationary position law. The sharp global **minimum/infimum** and all its attainment cases are:

- If \(0<q<q_c(g)\), the minimum is attained by **exactly one** centered reset law,
\[
\mu_\star=\tfrac12\delta_{-R_\star}+\tfrac12\delta_{R_\star},\qquad
R_\star=\frac{v}{\kappa}\sqrt{\frac{3}{3-(q-1)(q+g)}}.
\]
Its kurtosis is
\[
K_{\min}=\frac{(q+2)^2}{q(q+4)}-
\frac{4[3-(q-1)(q+g)]^2}{q(q+4)(q+g+3)^2}.
\]
- If \(q\ge q_c(g)\), the sharp infimum is
\[
K_{\inf}=\frac{(q+2)^2}{q(q+4)},
\]
which **no** centered reset law with finite fourth moment attains. It is approached by equiprobable resets to \(\pm R\) as \(R\to\infty\).

As \(q\uparrow q_c(g)\) from below, the uniquely optimal radius diverges at the sharp rate
\[
\frac{\kappa R_\star}{v}\sim
\sqrt{\frac{3}{(2q_c(g)+g-1)[q_c(g)-q]}}.
\]
In particular, the transition is from a finite, uniquely optimizing symmetric binary reset law to a nonattained infinite-radius limit. The full attainable kurtosis sets are \([K_{\min},\infty)\) below the threshold and \((K_{\inf},\infty)\) at or above it.

## Assumptions and scope
Let \(\kappa,v,\gamma,r\) be finite strictly positive constants. Between resets,
\[
\frac{dX_t}{dt}=-\kappa X_t+v S_t,
\]
where \(S_t\in\{-1,+1\}\) changes sign at independent exponential epochs of rate \(\gamma\). Independently, a Poisson clock of rate \(r\) resets the pair \((X_t,S_t)\) to \((R,S')\), where \(R\sim\mu\) is an independent new draw from an arbitrary Borel probability law on the real line with \(\mathbb E[R]=0\), \(\mathbb E[R^4]<\infty\), and \(S'\) is a **fair independent sign**. Successive reset draws and all clocks are independent. No thermal translational diffusion is present. The reset-location law need not be symmetric before optimization; centeredness is its sole mean constraint.

Since \(r>0\), the process has a unique regenerative stationary state. Its stationary position has finite fourth moment: if \(A\) is the last-reset age, then \(|X|\le e^{-\kappa A}|R|+v/\kappa\). The stationary positional mean is zero because the reset location is centered and the initial sign is fair. Thus its raw normalized fourth moment equals its conventional central kurtosis. The stationary variance is strictly positive, even for point resetting at zero, because \(v>0\).

## Proof
**1. Exact second and fourth moments.** Let \(L=v/\kappa\), \(x=\mathbb E[R^2]/L^2\), \(y=\mathbb E[R^4]/L^4\), \(V=\mathbb E[X^2]/L^2\), and \(F=\mathbb E[X^4]/L^4\). The Markov generator acting on polynomials is
\[
\mathcal L f(x,s)=(-\kappa x+vs)\partial_x f(x,s)
+\gamma[f(x,-s)-f(x,s)]
+r\{\mathbb E_{R,S'}f(R,S')-f(x,s)\}.
\]
Its stationary equations for \(XS\) and \(X^3S\) give, respectively,
\[
\mathbb E[XS]=\frac{v}{\kappa+2\gamma+r},\qquad
\mathbb E[X^3S]=\frac{3v\,\mathbb E[X^2]}{3\kappa+2\gamma+r}.
\]
Using \(X^2\) and \(X^4\) in the same generator yields the dimensionless, **exact** identities
\[
V=\frac{2/(q+g+1)+qx}{q+2},\qquad
F=\frac{12V/(q+g+3)+qy}{q+4}.
\]
These equations can alternatively be recovered by specializing the published arbitrary-reset moment hierarchy [1, Sec. IV, Eqs. (36)--(42)]. The underlying moment recurrence is therefore **prior work**; the minimization below is the present claim.

**2. Optimize over every reset law, not only symmetric laws.** Jensen's inequality gives \(y\ge x^2\). At each \(x>0\), equality is possible exactly when \(|R|\) is constant almost surely, and centeredness then forces equal masses on the two endpoints. At \(x=0\), equality forces \(R=0\). Since \(F\) is strictly increasing in \(y\) and \(V\) depends only on \(x\), **every** global optimizer must lie in this unique binary family.

Introduce the positive base variance and dimensionless rational coefficients
\[
V_0=\frac{2}{(q+2)(q+g+1)},\qquad
A=\frac{(q+2)^2}{q(q+4)},\qquad
B=\frac{8[(q-1)(q+g)-3]}{q(q+4)(q+g+1)(q+g+3)}.
\]
As \(x\) runs through \([0,\infty)\), the stationary variance runs through \([V_0,\infty)\). Substituting \(y=x^2\) and eliminating \(x\) gives **without approximation**
\[
K_{\mathrm{binary}}(V)=A+\frac{B}{V}+\frac{AV_0^2}{V^2},\qquad V\ge V_0.
\]
Its derivative is \(-B/V^2-2AV_0^2/V^3\).

**3. Sharp threshold, attainment, and limiting law.** The sign of \(B\) is the sign of \((q-1)(q+g)-3\). For fixed \(g>0\), this expression crosses zero exactly once at \(q=q_c(g)>1\). If \(B<0\), the derivative changes sign precisely once, at \(V_\star=-2AV_0^2/B>V_0\); it is negative below and positive above. Solving \(V_\star=V_0+qx/(q+2)\) gives
\[
x_\star=\frac{3}{3-(q-1)(q+g)}>0.
\]
Hence the reset radius and uniquely attained minimum in the Finding follow by substitution. If \(B\ge0\), the derivative is strictly negative at every finite \(V\ge V_0\), so \(K>A\) there and \(K\downarrow A\) as \(V\to\infty\). Binary reset laws with \(x\to\infty\) realize this sharp unattained limit.

The full range follows because every \(x>0\) admits centered three-atom reset laws
\[
\mu_p=(1-p)\delta_0+\frac p2\left(\delta_{-L\sqrt{x/p}}+\delta_{L\sqrt{x/p}}\right),\qquad 0<p\le1,
\]
whose second moment is fixed at \(L^2x\) and fourth moment is \(L^4x^2/p\). Their stationary kurtosis ranges continuously from its binary value to infinity. Continuity and the preceding monotonicity then give the claimed attainable intervals.

Finally \(3-(q-1)(q+g)=(2q_c+g-1)(q_c-q)+O((q_c-q)^2)\), which proves the displayed critical square-root divergence. All steps hold for any finite positive parameters and every centered finite-fourth-moment reset law; no finite parameter grid is used to prove a universal statement.

## Verification
Run the included standalone Python 3 checker by executing `python3 verify.py`. It uses only the Python standard library and re-evaluates the generator identities, the all-law moment constraint, the critical algebra, comparisons with nearby and distant binary choices, the nonattainment limiting behavior, and an independent regenerative Monte Carlo simulation. In the packaged check it passed 2,932 numerical assertions. The Monte Carlo comparisons are finite-sample diagnostics with tolerances; strict optimality, nonattainment, and sharp critical scaling are established analytically above, not inferred from numerical tests.

## Relationship to prior work
Olsen [1] derived the harmonic run-and-tumble model with resetting to arbitrary position distributions and arbitrary-order stationary moment recursions, including the formulas that yield the present second and fourth moments. We neither claim that model nor its moment closure as new. The additional result here is the **exact minimization of stationary positional kurtosis over all centered reset measures**, which singles out symmetric two-atom laws, identifies the sharp finite-radius versus unattained-radius threshold, and quantifies its singular approach. Direct examination of [1, Sec. IV and conclusion] found forward moments, variance, and examples with Gaussian reset laws, but not this global all-measure optimization or its threshold.

Garcia-Millan and Pruessner [2] treat run-and-tumble motion with harmonic confinement using field theory; they do not formulate this particular distributed-reset kurtosis design problem. Evans and Majumdar [3] address free run-and-tumble motion with resetting to a fixed location, rather than harmonic trapping and optimization over reset distributions. These distinctions are comparisons of hypotheses and implications, not priority certificates. General optimization of ratios of moments and unpublished equivalent specializations remain possible; independent scholarly validation is not claimed.

## Limitations
The result is confined to a one-dimensional harmonic trap, strictly positive rates, independent fair spin reinitialization at each common reset, a centered reset-location law, no translational Brownian noise, and reset distributions with finite fourth moment. Fixing the reset variance, restricting admissible supports, allowing correlated reset position and spin, or changing the flip/reset protocol produces a different optimization problem. Kurtosis quantifies distribution shape but by itself does not determine any single extreme-tail probability. The infinite-radius optimum above threshold is an unattained infimum, not a physically realizable finite-distance solution. The proof does not establish novelty against inaccessible or unknown literature, and no independent audit has been performed.

## References
[1] Kristian Stølevik Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840v1 (first posted 2023-10-07), especially Sec. IV, Eqs. (36)--(42). https://arxiv.org/html/2310.04840v1

[2] Rosalba Garcia-Millan and Gunnar Pruessner, *Run-and-tumble motion: field theory and entropy production*, arXiv:2012.02900v1 (first posted 2020-12-04). https://arxiv.org/abs/2012.02900

[3] Martin R. Evans and Satya N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, Journal of Physics A 51, 475003 (2018), DOI: 10.1088/1751-8121/aae74e.
