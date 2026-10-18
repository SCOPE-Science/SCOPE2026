# Sharp theta-method positivity and rate-majorization on directed cycles

## Finding
Fix an integer \(n\ge3\), positive rates \(r_1,\ldots,r_n\), and \(0\le\theta\le1\). Let \(Q\) be the row-convention generator of a one-way cycle: its only nonzero entries in row \(i\) are \(Q_{ii}=-r_i\) and \(Q_{i,i+1}=r_i\), indices taken modulo \(n\). For a timestep \(h\ge0\) let
\[
M_\theta(h)=(I-\theta hQ)^{-1}(I+(1-\theta)hQ).
\]
Define the **positivity horizon** \(H_\theta(r)\) by requiring that \(M_\theta(h)\) be entrywise nonnegative exactly for \(0\le h\le H_\theta(r)\), with the usual convention for \(H_\theta(r)=\infty\).

**Exact criterion and one-interval law.** For \(0<\theta<1\), set
\[
s=\theta h,\qquad t_i(s)=\frac{sr_i}{1+sr_i},\qquad P(s)=\prod_{j=1}^{n}t_j(s),\qquad r_{\max}=\max_jr_j.
\]
For all \(h>0\),
\[
\boxed{\ M_\theta(h)\ge0\quad\Longleftrightarrow\quad
\max_i t_i(s)\le\theta+(1-\theta)P(s).\ }
\]
The positivity set is always a single initial interval, despite the fact that this directed Markov generator is not reversible for \(n\ge3\). With
\[
\pi_{\min}=\frac{1}{r_{\max}\sum_{j=1}^{n}r_j^{-1}},
\]
its horizon is infinite precisely when \(\theta\ge1-\pi_{\min}\). For \(0<\theta<1-\pi_{\min}\), there is exactly one positive solution \(s_*\) of
\[
\frac{s_*r_{\max}}{1+s_*r_{\max}}=
\theta+(1-\theta)\prod_{j=1}^{n}\frac{s_*r_j}{1+s_*r_j},
\]
and \(H_\theta(r)=s_*/\theta\). At \(\theta=0\), the exact horizon is \(H_0(r)=1/r_{\max}\); at \(\theta=1\), it is \(H_1(r)=\infty\). Boundary equality is included whenever the horizon is finite.

**Strict majorization and rate-budget transition.** Fix \(0<\theta<1\). For positive rate vectors \(r,u\) of the same length and the same sum, suppose \(r\) **majorizes** \(u\): after sorting coordinates in descending order, each of the first \(k<n\) partial sums of \(r\) is at least that of \(u\). Then
\[
H_\theta(r)\le H_\theta(u).
\]
The inequality is strict if the vectors are not permutations and \(H_\theta(u)<\infty\). Thus redistributing rate budget away from balance cannot enlarge the positive-step range; except in the unbounded-horizon regime, every nontrivial imbalance strictly shrinks it. The horizon depends only on the multiset of rates, not their cyclic order.

For fixed total exit-rate budget \(B>0\), let \(\rho=B/n\). The uniform vector \(r_i=\rho\) uniquely maximizes \(H_\theta\) among all positive rate vectors exactly for
\[
\boxed{\ 0\le\theta\le\frac{n-1}{n}.\ }
\]
At the critical value \(\theta=(n-1)/n\), its horizon is already infinite while every nonuniform vector still has a finite horizon. For \((n-1)/n<\theta\le1\), infinitely many nonuniform positive vectors also attain the infinite maximum. When \(0<\theta<(n-1)/n\), the finite uniform optimum is given by the unique \(t\in(0,1)\) solving
\[
t=\theta+(1-\theta)t^n,
\qquad
H_\theta^{\max}=\frac{t}{\theta\rho(1-t)}.
\]
At \(\theta=0\), the uniform maximum is \(1/\rho\). As an exact comparison for \(n=3\), \(\theta=1/2\), and \(B=6\), the balanced rates \((2,2,2)\) permit
\[
H_{1/2}(2,2,2)=\frac{1+\sqrt5}{2},
\]
whereas the more unequal rates \((4,1,1)\) permit only
\[
H_{1/2}(4,1,1)=\frac{2(2\sqrt2-1)}7.
\]

## Assumptions and scope
The generator has precisely one positive off-diagonal rate in each row, directed along a single cycle. Every rate is strictly positive, so the finite-state Markov chain is irreducible. We analyze entrywise nonnegativity of the **end-step matrix**, equivalent to preservation of every nonnegative row vector, not positivity of internal Runge–Kutta stages, strong-stability-preserving coefficients, or numerical stability in other senses. The timestep \(h\) is nonnegative and \(\theta\) lies in the full closed interval \([0,1]\). The strict majorization assertion requires fixed sum and \(0<\theta<1\); its finite-horizon hypothesis is essential. The equal-rate optimization claims are global over the open positive rate simplex with fixed total \(B\), and do not concern allowing zero rates or disconnecting the cycle.

## Proof
**1. Exact resolvent on a heterogeneous directed cycle.** Fix \(s>0\). Write \(S\) for the cyclic permutation matrix that sends each vertex to its successor, and set
\[
D_s=\operatorname{diag}(1+sr_i),\qquad T_s=\operatorname{diag}(t_i(s))S.
\]
Then \(I-sQ=D_s(I-T_s)\). Since \(T_s^n=P(s)I\) and \(0<P(s)<1\),
\[
R_s:=(I-sQ)^{-1}
=\frac{I+T_s+\cdots+T_s^{n-1}}{1-P(s)}D_s^{-1}.
\]
Every entry of \(R_s\) is strictly positive, and \(R_s\mathbf1=\mathbf1\). The only diagonal contribution to the finite cyclic geometric sum is the identity term, giving
\[
\boxed{\ (R_s)_{ii}=\frac{1-t_i(s)}{1-P(s)}.\ }
\]
For \(0<\theta<1\), the algebraic theta-method identity is
\[
M_\theta(h)=\frac1\theta R_{\theta h}-\frac{1-\theta}{\theta}I.
\]
All off-diagonal entries are positive. A diagonal entry is nonnegative exactly when \((R_s)_{ii}\ge1-\theta\), or equivalently \(t_i(s)\le\theta+(1-\theta)P(s)\). It is enough to check a vertex of largest rate, since \(t_i(s)\) is increasing in \(r_i\). This proves the stated criterion, including cyclic-order invariance.

**2. A strict return monotonicity law at the fastest vertex.** Let \(i_*\) be any index attaining \(r_{\max}\); write \(t_*=t_{i_*}\), \(a_j=1-t_j\), and \(P=P(s)\). For every \(s>0\), logarithmic differentiation gives
\[
\frac{d\log (R_s)_{i_*i_*}}{d\log s}
=-t_*+\frac{P\sum_j a_j}{1-P}.
\]
But \(t_j\le t_*\), all \(a_j,t_j\) are positive, and the positive cross-terms in a product of at least two factors give
\[
\frac{1-P}{P}
=\prod_{j=1}^{n}\left(1+\frac{a_j}{t_j}\right)-1
>\sum_j\frac{a_j}{t_j}
\ge\frac{\sum_ja_j}{t_*}.
\]
Consequently the displayed logarithmic derivative is strictly negative. This monotonicity is proved directly: it does not assume reversibility or falsely assert that all resolvent diagonals decrease.

The return diagonal is \(1\) at \(s=0\). As \(s\to\infty\),
\[
1-t_i(s)\sim\frac1{sr_i},\qquad
1-P(s)\sim\frac1s\sum_j\frac1{r_j},
\]
so the fastest-state return probability tends to \(\pi_{\min}\). It decreases strictly from \(1\) to \(\pi_{\min}\). Positivity therefore holds for all finite steps exactly when \(1-\theta\le\pi_{\min}\); otherwise there is one finite crossing and no later recovery. At the crossing the most restrictive diagonal is zero. The endpoint cases follow separately: \(M_0(h)=I+hQ\) is nonnegative if and only if \(h\le1/r_{\max}\), while \(M_1(h)=(I-hQ)^{-1}\ge0\) at every nonnegative step.

**3. Strict rate majorization.** Let \(r\) majorize \(u\), with fixed sum, and suppose they are not permutations. For fixed \(s>0\) the function
\[
f_s(x)=\log\left(\frac{sx}{1+sx}\right),\qquad
f_s''(x)=-\frac{1+2sx}{x^2(1+sx)^2}<0
\]
is strictly concave for \(x>0\). Strict Karamata gives
\[
P_r(s)=\exp\!\left(\sum_j f_s(r_j)\right)
<\exp\!\left(\sum_j f_s(u_j)\right)=P_u(s).
\]
Also \(\max r_j\ge\max u_j\), so \(\max t_j(r,s)\ge\max t_j(u,s)\). Hence the positivity criterion at any finite positive step is strictly harder for \(r\). If \(H_\theta(u)<\infty\), at the positive crossing for \(u\) the inequality for \(r\) is strictly violated; since its admissible set is an initial interval, \(H_\theta(r)<H_\theta(u)\). If the latter horizon is infinite, only the weak inequality is meaningful. This proves all the majorization claims.

**4. Exact budget optimizer and uniqueness transition.** At fixed \(B\), every positive rate vector majorizes the uniform vector \((\rho,\ldots,\rho)\), with strict majorization unless it is uniform. The uniform stationary distribution has \(\pi_{\min}=1/n\), so its horizon is infinite exactly when \(\theta\ge(n-1)/n\). Every nonuniform vector has
\[
r_{\max}\sum_jr_j^{-1}>n,
\qquad\text{hence}\qquad
\pi_{\min}<1/n.
\]
Therefore at the critical \(\theta\), every nonuniform vector has a finite horizon and loses to uniformity. Below the critical \(\theta\), strict majorization makes the uniform vector the unique maximum; at \(\theta=0\), use \(r_{\max}\ge\rho\), with equality only for uniform rates. Above the critical value and below \(1\), sufficiently small nonuniform perturbations retain \(\pi_{\min}>1-\theta\) by continuity and hence share an infinite horizon. At \(\theta=1\), all positive vectors do. Finally, uniform rates make all \(t_i\) equal; the crossing equation reduces to \(t=\theta+(1-\theta)t^n\), which has exactly one root in \((0,1)\) when \(0<\theta<(n-1)/n\), by strict convexity of the right-hand side minus \(t\) and the endpoint signs. Solving \(t=s\rho/(1+s\rho)\) gives the stated horizon. This completes the proof.

## Verification
The self-contained Python 3 standard-library program `verify.py` performs exact rational matrix inversion. It constructs cyclic generators of sizes \(2\) through \(7\), three rate patterns per size, seven theta values, and eight timesteps. It checks every update's exact row sums, its off-diagonal signs, the explicit resolvent diagonal, and the claimed equivalent entrywise positivity test. It additionally checks fifty-five strict rational comparisons for uneven versus uniform rate vectors at fixed total budget, and two direct matrix checks around an explicit finite horizon. The program reports `VERIFY_OK exact_checks= 1065`.

These tests are finite consistency checks. The proof for all \(n\ge3\), all positive real rates, every \(\theta\in[0,1]\), and all \(h\ge0\) is analytical, via the resolvent product, strict derivative inequality, and strict majorization inequality. No floating-point threshold estimates or sampled graphs are used as evidence of the universal claim.

## Relationship to prior work
Horváth's 1998 and 2005 papers establish fundamental positivity-threshold frameworks for Runge–Kutta methods and classes of positive ODEs. These method-class conditions do not imply the exact heterogeneous directed-cycle horizon or the strict rate-budget majorization law. Fallat and Tsatsomeros (2002) develop Cayley-transform identities for matrix positivity classes: resolvent algebra as such is prior work, not a claimed innovation.

Hadjimichael, Ketcheson, and Lóczi (2021) analyze theta-method positivity for *periodic centered and higher-order spatial discretizations of advection*. Their primary full text explicitly studies spatial semidiscretizations that are not positivity preserving. The present setting is a **positive one-sided cyclic Markov generator**, allowing arbitrary vertex-dependent rates; the centered-difference results do not imply the cyclic return product, the nonreversible one-interval theorem, or majorization optimization.

The publicly accessible research finding *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026) already establishes the general resolvent-diagonal criterion for \(\theta=1/2\), along with monotonic threshold laws under reversibility. That foundational implication is acknowledged. The present theorem derives a strictly decreasing **fastest-state** diagonal for a genuinely nonreversible heterogeneous directed cycle, treats the full theta range, and proves new rate-majorization and optimizer uniqueness conclusions; it is not a restatement of the general Cayley criterion.

## Limitations
The theorem requires exactly one clockwise edge out of each vertex. It does not assert interval positivity or majorization for arbitrary nonreversible generators or networks with extra chords, reverse edges, or zero rates. For \(\theta\) above the budget transition, strict optimizer uniqueness is false and is not claimed. The result concerns end-step entrywise positivity, not nonlinear invariant sets, internal stage positivity, or a global method-class SSP radius. The resolvent identity and Karamata's inequality are established mathematical tools; the novelty claim concerns their specific directed-cycle combination and resulting exact optimization classification. Equivalent unindexed or differently formulated cyclic Markov-chain results remain possible and require external scholarly verification.

## References
1. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics 28 (1998), 309–326. DOI: 10.1016/S0168-9274(98)00050-6.
2. Z. Horváth, *On the Positivity Step Size Threshold of Runge–Kutta Methods*, Applied Numerical Mathematics 53 (2005), 341–356; first available online 27 October 2004. DOI: 10.1016/j.apnum.2004.08.026.
3. S. M. Fallat and M. J. Tsatsomeros, *On the Cayley Transform of Positivity Classes of Matrices*, Electronic Journal of Linear Algebra 9 (2002), 190–196. DOI: 10.13001/1081-3810.1086.
4. Y. Hadjimichael, D. I. Ketcheson, and L. Lóczi, *Positivity Preservation of Implicit Discretizations of the Advection Equation*, arXiv:2105.07403, first posted 16 May 2021.
5. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, publicly available research finding (2026), identifier `d475df91cd2a`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
