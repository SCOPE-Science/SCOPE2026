# Sharp asymptotic curvature-use ceiling in Wang--Peypouquet adaptive acceleration
## Finding

Consider the scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad \lambda>0,
\]
and the adaptive accelerated gradient method of Wang--Peypouquet. Assume that, from some index onward, consecutive iterates are distinct. On every such tail step the source local smoothness estimator is exact:
\[
L_{k+1}=\lambda.
\]

Let
\[
r_k=\lambda s_k.
\]
The published step-size rule then becomes exactly
\[
r_{k+1}=\min\{A_kr_k,B_kr_k,C_k\},
\]
where
\[
A_k=\frac{t_{k+1}-m}{t_{k+1}-1},
\qquad
B_k=\frac{2(t_{k+1}-1)}{(1+\beta)\gamma t_{k+1}},
\]
and
\[
C_k=
\frac{1-\omega}
{2/B_k+1/[\beta\gamma(1-\eta)A_k]}.
\]

For every source-admissible parameter choice,
\[
r_k\longrightarrow
C_\infty:=
\frac{1-\omega}
{(1+\beta)\gamma+1/[\beta\gamma(1-\eta)]}.
\]

Write
\[
q=\frac{2(t_0-1)+m}{2t_0+m}.
\]
The source parameter constraint is
\[
\frac{(1+\beta)\gamma}{2}\le q.
\]
At fixed \((m,t_0)\), the exact supremum of the limiting normalized step over all admissible \(\beta,\gamma,\eta,\omega\) is
\[
\sup C_\infty=
\begin{cases}
\dfrac{2q}{1+4q^2},&q\le\dfrac12,\\[2mm]
\dfrac12,&q\ge\dfrac12.
\end{cases}
\]
The supremum is not attained. In particular, every fixed admissible parameter choice satisfies
\[
C_\infty<\frac12.
\]

For the source-convenient initialization
\[
t_0=1,
\]
one has
\[
q=\frac{m}{2+m}<\frac13.
\]
Consequently
\[
C_\infty<\frac6{13}
\]
uniformly over all
\[
m\in(0,1).
\]

Thus, even when the local curvature estimate is exact, the source safeguards asymptotically use strictly less than half of the reciprocal-curvature scale; with \(t_0=1\), they use strictly less than \(6/(13\lambda)\).

## Assumptions and scope

The claim concerns the published scalar step-size mechanism on a positive quadratic. The nondegeneracy assumption is that consecutive iterates are distinct from some index onward. If two consecutive iterates coincide, the source explicitly sets the corresponding local estimate to zero and removes the curvature cap for that update, so such exceptional repeat steps are outside the exact tail recursion analyzed here.

No assumption is made that the gradient substep alone determines the rate of the full accelerated method. The inertial update can still produce acceleration. The result isolates how much of an exactly identified local curvature scale can survive the paper's three simultaneous Lyapunov safeguards.

The constants are suprema over source-admissible parameters. They are not attained because the parameterization always has
\[
\beta\gamma<(1+\beta)\gamma.
\]

## Proof

For the scalar quadratic, if
\[
x_{k+1}\ne x_k,
\]
then the source estimator equals
\[
L_{k+1}
=
\frac{\frac12\lambda^2(x_{k+1}-x_k)^2}
{\lambda x_{k+1}(x_{k+1}-x_k)-\frac\lambda2(x_{k+1}^2-x_k^2)}
=\lambda.
\]
Hence, multiplying the source update for \(s_{k+1}\) by \(\lambda\),
\[
r_{k+1}=\min\{A_kr_k,B_kr_k,C_k\}.
\]

The inertial parameters obey
\[
t_{k+1}=\frac{m+\sqrt{m^2+4t_k^2}}{2}.
\]
Since
\[
\sqrt{m^2+4t_k^2}\le2t_k+m,
\]
we have
\[
t_{k+1}\le t_k+m,
\]
so \(t_k=O(k)\). Also
\[
A_k=1+\frac{1-m}{t_{k+1}-1}>1.
\]
Because \(t_{k+1}=O(k)\), the series of increments of \(A_k\) dominates a harmonic tail. Therefore
\[
\prod_{j=N}^k A_j\longrightarrow\infty
\]
for every fixed \(N\).

The source admissibility condition implies \(B_k>1\) for every \(k\), and \(B_k\) increases to
\[
B_\infty=\frac{2}{(1+\beta)\gamma}>1.
\]
Thus, with
\[
g_k=\min\{A_k,B_k\},
\]
one has \(g_k>1\) and
\[
\prod_{j=N}^kg_j\longrightarrow\infty.
\]
Moreover,
\[
A_k\to1,
\qquad
B_k\to\frac{2}{(1+\beta)\gamma},
\]
so
\[
C_k\to
C_\infty=
\frac{1-\omega}
{(1+\beta)\gamma+1/[\beta\gamma(1-\eta)]}.
\]
The recurrence is now
\[
r_{k+1}=\min\{g_kr_k,C_k\}.
\]
Its limsup is at most \(C_\infty\). For any \(\varepsilon>0\), eventually
\[
C_k\ge C_\infty-\varepsilon.
\]
If at such an index
\[
r_k<C_\infty-2\varepsilon,
\]
then repeated multiplication by \(g_k>1\), whose tail product diverges, must eventually raise the iterate to at least \(C_\infty-2\varepsilon\); after that, the lower cap bound prevents it from falling below that level. Hence
\[
\liminf r_k\ge C_\infty-2\varepsilon.
\]
Letting \(\varepsilon\downarrow0\) proves
\[
r_k\to C_\infty.
\]

It remains to optimize the limit. Since positive \(\eta\) or \(\omega\) can only reduce \(C_\infty\), its supremum is approached with
\[
\eta=\omega=0.
\]
Set
\[
x=\beta\gamma,
\qquad
y=(1+\beta)\gamma.
\]
Then
\[
0<x<y\le2q,
\]
and
\[
C_\infty=\frac1{y+1/x}.
\]
Conversely, every pair
\[
0<x<y\le2q
\]
comes from admissible positive \(\beta,\gamma\) by taking
\[
\gamma=y-x,
\qquad
\beta=\frac{x}{y-x}.
\]
Thus the sharp envelope is the reciprocal of
\[
\inf_{0<x<y\le2q}(y+1/x).
\]
For fixed \(x\), the infimum is approached as \(y\downarrow x\), reducing the problem to minimizing
\[
x+\frac1x
\]
over
\[
0<x<2q.
\]
If \(q\le1/2\), this expression decreases throughout the admissible interval and its infimum is
\[
2q+\frac1{2q}.
\]
If \(q\ge1/2\), the infimum is \(2\), approached at \(x=1\). This proves the displayed piecewise formula and the strict bound
\[
C_\infty<\frac12.
\]

Finally, if \(t_0=1\), then
\[
q=\frac{m}{2+m}.
\]
For \(m\in(0,1)\), this lies below \(1/3\), and the function
\[
\frac{2q}{1+4q^2}
\]
is increasing on \((0,1/2)\). Letting \(m\uparrow1\) gives the sharp uniform supremum
\[
\frac{2/3}{1+4/9}=\frac6{13}.
\]

## Verification

The standalone script `artifacts/verify_curvature_ceiling.py` replays the exact \((t_k,A_k,B_k,C_k,r_k)\) recursion for several admissible parameter choices and checks convergence to the closed-form \(C_\infty\). It also performs a deterministic grid search over admissible transformed parameters \((x,y)\) and verifies approach to the analytic envelope.

The convergence and optimization claims are proved symbolically above. The finite computations are supporting checks only.

## Relationship to prior work

Wang and Peypouquet introduce the three-way safeguarded step-size update, prove a positive lower bound for its step sizes, and emphasize that \(A_k>1\) and \(B_k>1\) allow step growth. They also discuss a tradeoff between the inertial parameter \(m\), growth of \((t_k)\), and possible growth of \((s_k)\). The paper does not state the scalar-quadratic limit \(C_\infty\) or optimize that limit over its admissible parameter set.

Malitsky and Mishchenko's adaptive gradient method is an important predecessor using local curvature estimates, but it has a different two-way update and no inertial \((A_k,B_k,C_k)\) safeguard. Suh and Ma's AdaNAG is the accelerated predecessor explicitly identified by the primary source; its parameter-free update is also different. Neither inspected source implies the exact ceiling derived here.

The source itself notes that an earlier adaptive-gradient rule uses a cap proportional to \(1/(2L_k)\). The present result is not a restatement of that cap: it derives the exact asymptotic cap of the new three-way accelerated rule and shows how the source admissibility condition and the commonly convenient choice \(t_0=1\) further restrict the achievable normalized limit.

Targeted published-result searches using the primary title, scalar-quadratic specialization, local-curvature aliases, asymptotic step-size language, and the \(A_k,B_k,C_k\) safeguard did not locate an equivalent statement.

## Limitations

The exact limit assumes that the scalar quadratic trajectory has no consecutive-repeat events after some finite index. Such events make the source set \(L_{k+1}=0\) and temporarily remove the curvature cap.

The theorem concerns the adaptive step size, not the overall accelerated rate. It does not assert that a smaller gradient substep makes the full inertial method slower.

The scalar quadratic has constant curvature, so the result does not classify how the step sequence behaves under genuinely varying local smoothness.

## References

1. Z. Wang, J. Peypouquet, *Adaptive Accelerated Gradient Method for Smooth Convex Optimization*, arXiv:2512.20478v1, first public 23 December 2025; later published in *Journal of Optimization Theory and Applications* 210, article 52, 2026, DOI: 10.1007/s10957-026-03086-z.
2. Y. Malitsky, K. Mishchenko, *Adaptive Gradient Descent without Descent*, ICML 2020, arXiv:1910.09529.
3. J. J. Suh, S. Ma, *An Adaptive and Parameter-Free Nesterov's Accelerated Gradient Method for Convex Optimization*, arXiv:2505.11670v1, first public 16 May 2025.
