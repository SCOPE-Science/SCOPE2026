# Exact residual-budget-optimal sampling sizes for symmetric three-row Kaczmarz–Motzkin

## Finding
For a symmetric three-row consistent system in the plane, the asymptotically optimal sampling Kaczmarz–Motzkin (SKM) sample size **per charged residual evaluation** switches twice as the row geometry changes. Define \(x=\cos^2\theta\), \(y=(2x-1)^2\), and the two algebraic roots \(x_-\approx0.114204276900733\), \(x_+\approx0.332327385175607\) specified below. The optimal size is three when \(0<x<x_-\) or \(x_+<x<1\), and two when \(x_-<x<x_+\). At the endpoints two and three tie. There is one further tie: at \(x=1/4\), sampling one and two tie (but three loses). Sampling one is never uniquely optimal.

## Assumptions and scope
Consider the consistent homogeneous real system with unit row normals
\[
a_0=(1,0),\qquad a_+=(\cos\theta,\sin\theta),\qquad a_-=(\cos\theta,-\sin\theta),\qquad0<\theta<\pi/2.
\]
For each fixed \(\beta\in\{1,2,3\}\), at each iteration independently sample a uniformly chosen \(\beta\)-subset of the three distinct rows, compute each sampled absolute residual \(|a_i^\mathsf Te|\), pick the largest (uniform ties), and apply \(e\leftarrow e-a_i(a_i^\mathsf Te)\). The initial error is nonzero and not parallel to any row; exceptional aligned starts may terminate immediately and thus have a different asymptotic factor. Let \(x=\cos^2\theta\in(0,1)\), \(y=(2x-1)^2\). The nominal work budget counts \(\beta\) evaluated row residuals per iteration, and does not count the final projection, row caching, communication, or hardware effects.

Let \(\lambda_\beta\) be the root-exponential rate of expected squared Euclidean error after \(k\) iterations, and let \(q_\beta=\lambda_\beta^{1/\beta}\) be the rate per charged residual evaluation. Then
\[
\lambda_1=\frac{2+y+\sqrt{y^2+8x^2}}6,\qquad
\lambda_2=\begin{cases}
\dfrac{y+\sqrt{y^2+24x^2}}6,&0<x\le1/4,\\[2pt]
\dfrac{y+\sqrt{y^2+3x^2}}3,&1/4\le x<1,
\end{cases}
\qquad\lambda_3=\min\{x,y\}.
\]
Define
\[
P_5(x)=64x^5-128x^4+192x^3-40x^2+11x-1,
\]
\[
P_9(x)=8192x^9-32768x^8+53632x^7-45056x^6+18401x^5-607x^4-2887x^3+1313x^2-253x+19.
\]
There is exactly one root \(x_-\in(1/12,1/8)\) of \(P_5\), and exactly one root \(x_+\in(1/4,1/3)\) of \(P_9\). The optimal choices are: \(\beta=3\) on \((0,x_-)\cup(x_+,1)\), \(\beta=2\) on \((x_-,x_+)\), and both sizes \(\{2,3\}\) at \(x_-,x_+\). At \(x=1/4\), the additional minimizing choice \(\beta=1\) ties with two. At \(x=1/2\), full sampling has \(\lambda_3=0\) and reaches the solution in finitely many steps. Exact equalities are in the described arithmetic model.

## Proof
**Reduction to a three-state weighted Markov recurrence.** After one nonterminating projection the error lies on one of the lines perpendicular to the three row normals. The squared-norm multiplier upon moving from the perpendicular line of row \(i\) to that of row \(j\) is the squared cosine of the angle between rows. Thus it equals \(x\) between row \(0\) and either signed row, \(y\) between signed rows, and one for a repeated row. The squared *selection residual*, by contrast, is one minus that squared cosine. Consequently, on a signed-row line the greedy selection prefers row \(0\) over the other signed row precisely when \(x<y\), equivalently \(x<1/4\). Define the weighted transition matrices, indexed \(0,+,-\):
\[
M_1=\frac13\begin{pmatrix}1&x&x\\x&1&y\\x&y&1\end{pmatrix},\quad
M_2=\begin{pmatrix}0&x/2&x/2\\\alpha x&0&(1-\alpha)y\\\alpha x&(1-\alpha)y&0\end{pmatrix},
\]
where \(\alpha=2/3\) when \(x<1/4\), \(\alpha=1/3\) when \(x>1/4\), and \(\alpha=1/2\) at the tie. Full sampling uses
\[
M_3=\begin{cases}
\begin{pmatrix}0&x/2&x/2\\x&0&0\\x&0&0\end{pmatrix},&x<1/4,\\[6pt]
\begin{pmatrix}0&x/2&x/2\\0&0&y\\0&y&0\end{pmatrix},&x>1/4.
\end{cases}
\]
At \(x=1/4\) all off-diagonal squared cosines agree, and the full-sampling matrix's spectral radius is still \(x=y=1/4\). If \(v_i\) is the probability-weighted squared norm of the post-first-step error on line \(i\), exact conditional expectation gives, for all integers \(k\ge1\),
\[
\mathbb E\|e_k\|_2^2=vM_\beta^{k-1}\mathbf1.
\]
With the nonaligned initial condition, the weighted recurrence accesses the Perron class and hence has root-exponential factor equal to \(\rho(M_\beta)\). The zero-spectral-radius case is finite termination. Direct characteristic factorization, using the symmetry between \(+\) and \(-\), yields the three stated expressions for \(\lambda_\beta\).

**Two algebraic crossover roots.** On \(0<x<1/4\), the positive \(t=\lambda_2\) solves \(3t^2-yt-2x^2=0\); comparing \(q_2\) and \(q_3\) is comparing \(t^3\) and \(x^2\). The exact resultant is
\[
\operatorname{Res}_t(3t^2-yt-2x^2,\ t^3-x^2)=-x^2(x-1)P_5(x).
\]
On \(1/4<x<1\), the positive \(t=\lambda_2\) solves \(3t^2-2yt-x^2=0\); the corresponding resultant is
\[
\operatorname{Res}_t(3t^2-2yt-x^2,\ t^3-y^2)=-(x-1)P_9(x).
\]
The other quadratic root in each case is negative, so it cannot satisfy the strictly positive cubic right-hand side. Exact rational Sturm variations at \(0,1/12,1/8,1/4\) for \(P_5\) are \(3,3,2,2\); variations at \(1/4,1/3,1\) for \(P_9\) are \(5,4,4\). These certify precisely one crossover in each stated interval and no further crossover in the respective range. Evaluate the inequalities at \(x=1/16,1/5,3/10,1/2\) to fix the branch orientations: full sampling wins outside the roots and two-row sampling wins between them.

**Exclusion of uniquely optimal singleton sampling.** From the expression for \(\lambda_1\), the inequality \(\lambda_1\ge1/2\) is equivalent to \(8x^2+2y-1=(4x-1)^2\ge0\), with equality only at \(x=1/4\). Within the two-row-winning interval the quadratic equation for \(\lambda_2\) evaluated at \(t=1/4\) yields \(\lambda_2\le1/4\), strictly except at \(x=1/4\): the relevant factors are \(-(4x-1)(12x-1)/16\) to the left, and \(-(4x-1)(12x-5)/16\) to the right. Therefore \(q_2\le1/2\le q_1\) there. For \(0<x\le x_-<1/8\), \(q_3=x^{1/3}<1/2\le q_1\). For \(x_+\le x\le1/3\), \(y\le1/9<1/8\), so again \(q_3<1/2\le q_1\). For \(1/3\le x<1\), the positive symmetric vector yields the Rayleigh quotient lower bound
\[
\lambda_1\ge R(x)=\frac{3+4x+2y}{9},\qquad
R(x)^3-y=\frac{4(x-1)^2}{729}\bigl(128x^4+64x^3+336x^2+352x-151\bigr)\ge0.
\]
The final quartic is strictly increasing for nonnegative \(x\) and positive already at \(x=1/3\); hence \(q_1\ge q_3\). This completes the global choice classification.

## Verification
Run `python verify.py` with the standalone `requirements.txt` dependencies installed. The verifier checks both polynomial resultants, exact Sturm counts and variations, weighted-transition characteristic factors, rational inequalities, 15 direct exact-rational finite-time expectations independently enumerating sampled subsets and tie rules, and five diagnostic phase points. These are checks of exact identities and finite recurrences; the preceding Perron argument and Sturm proof, rather than a finite experiment, establish the all-iteration and all-parameter claims.

## Relationship to prior work
Haddock and Ma's 2019 preprint [1] analyzes SKM's partially greedy sampling and computational sample-size choices, supplying general convergence guarantees and motivating the tradeoff between per-step progress and sampled residual costs. De Loera, Haddock, and Needell [2] introduced the SKM framework and explored sample-size performance. Their inspected results do not state this exact three-row geometry-dependent optimal-cost phase diagram. The result also differs from one-step residual amplification and deterministic full-greedy projection bounds because it concerns an infinite-horizon squared-solution-error exponent normalized by explicitly charged sampled residual counts.

## Limitations
The construction has only three unit rows and two unknowns, with independent uniform sampling without replacement, greedy absolute residuals, exact arithmetic, and a consistent system. It is not a worst-case guarantee for general SKM matrices or a universal optimal sample size. Residual evaluations are the charged cost; projection overhead, caching, parallelism, and hardware can change practical best choices. The root-asymptotic statement excludes starts parallel to a row, which can terminate in one step for full greed. Near \(x=1/2\), full sampling exhibits structural finite-step termination; finite precision is not modeled.

## References
[1] J. Haddock and A. Ma, “Greed Works: An Improved Analysis of Sampling Kaczmarz–Motzkin,” arXiv:1912.03544, initially public December 7, 2019; SIAM Journal on Mathematics of Data Science 3 (2021), 342–368. https://arxiv.org/abs/1912.03544

[2] J. A. De Loera, J. Haddock, and D. Needell, “A Sampling Kaczmarz–Motzkin Algorithm for Linear Feasibility,” arXiv:1605.01418 (2016). https://arxiv.org/abs/1605.01418
