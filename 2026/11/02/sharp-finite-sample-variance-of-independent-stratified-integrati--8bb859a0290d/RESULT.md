# Sharp finite-sample variance of independent stratified integration for bounded monotone Lipschitz functions

## Finding

Consider one independent uniform evaluation per equal-width stratum of the unit interval. For the natural class of nondecreasing functions taking values in \([0,1]\) with Lipschitz constant at most \(L>0\), the exact worst-case mean-squared integration error is a finite maximum of elementary rational expressions. Unlike the unrestricted monotone class, its extremizers are continuous, centered ramps. For fixed \(L>4/3\) and increasing sample size, a worst-case function concentrates all variation into approximately \(4n/(3L)\) strata, with a slope-\(L\) ramp occupying approximately three-quarters of each active stratum.

Specifically, for \(n\ge1\), independent \(U_i\sim\mathrm{Uniform}(0,1)\), and
\[
Q_n(f)=\frac1n\sum_{i=1}^n f\left(\frac{i-1+U_i}{n}\right),\qquad I(f)=\int_0^1f(x)\,dx,
\]
let
\[
\mathcal F_L=\{f:[0,1]\to[0,1]:f\text{ nondecreasing and }|f(x)-f(y)|\le L|x-y|\},\quad
s=\frac{n\min\{1,L\}}{L}.
\]
Then, with the endpoints interpreted as inclusive integers,
\[
\boxed{\sup_{f\in\mathcal F_L}\mathbb E\bigl(Q_n(f)-I(f)\bigr)^2
=\frac{L^2}{n^4}\max_{\lceil s\rceil\le k\le n}\left(\frac{s^2}{4k}-\frac{s^3}{6k^2}\right).}\tag{1}
\]
Every term in the maximum is attained by an explicit admissible function with exactly \(k\) active strata and a centered linear ramp of slope \(L\) in each, with all other strata constant. In particular, a maximizing \(k\) can be found by comparing the feasible integers nearest \(4s/3\), together with the endpoints when necessary; there is no continuous optimization or unknown constant.

The exact low-Lipschitz branches are
\[
\sup_{f\in\mathcal F_L}\operatorname{Var}(Q_n(f))=
\begin{cases}
\displaystyle\frac{L^2}{12n^3},&0<L\le1,\\[3pt]
\displaystyle\frac{1/4-1/(6L)}{n^3},&1\le L\le4/3.
\end{cases}\tag{2}
\]
For every fixed \(L>4/3\),
\[
\lim_{n\to\infty}n^3\sup_{f\in\mathcal F_L}\operatorname{Var}(Q_n(f))=\frac{3L}{32}.\tag{3}
\]
For \(L\ge n\), a single active stratum is optimal (possibly tied at \(L=n\)), and (1) simplifies to
\[
\frac1{4n^2}-\frac1{6Ln};\tag{4}
\]
its \(L\to\infty\) limit recovers the unrestricted bounded-monotone step-function variance \(1/(4n^2)\).

## Assumptions and scope

The sample points are independent across strata, exactly uniform within each of the \(n\) intervals, and independent of the integrand. The estimator is unbiased. The Lipschitz constant is a global upper bound, not a required attained derivative. No differentiability beyond Lipschitz continuity is assumed. A function in \(\mathcal F_L\) may have flat regions and may have total variation strictly less than one. The supremum concerns the squared-error expectation for this specific estimator, not minimax error over all randomized algorithms or optimal allocation of sampling points.

## Proof

**1. A sharp local fixed-increment inequality.** Fix an interval of length \(H\), and a nondecreasing \(L\)-Lipschitz function whose endpoint increase is \(\Delta\), with \(0<\Delta\le LH\). Let \(U\) be uniform on that interval and normalize \(Y=(f(U)-f(\text{left}))/\Delta\in[0,1]\). Since \(f\) is absolutely continuous and has derivative between zero and \(L\) almost everywhere, the pushforward distribution of \(Y\) dominates \(t\) times the uniform distribution on \([0,1]\), where \(t=\Delta/(LH)\). To see this, every interval of values of length \(v\) has preimage of length at least \(\Delta v/L\); monotone approximation extends this lower measure bound to Borel subsets. Thus the law of \(Y\) is a mixture \(t\,\mathrm{Uniform}(0,1)+(1-t)\nu\), for a probability measure \(\nu\) on \([0,1]\).

For \(\mu=\mathbb EY\), \(y^2\le y\) on \([0,1]\) gives
\[
\mathbb EY^2\le\mathbb EY-t\int_0^1(y-y^2)\,dy=\mu-\frac t6.
\]
Consequently
\[
\operatorname{Var}(f(U))\le\Delta^2\left(\mu(1-\mu)-\frac t6\right)
\le\Delta^2\left(\frac14-\frac{\Delta}{6LH}\right).\tag{5}
\]
The centered ramp of slope \(L\), with width \(\Delta/L\) and equal-length plateaux on its two sides, realizes equality. Its output distribution consists of mass \((1-t)/2\) at each endpoint and uniform mass \(t\) between. If \(\Delta=0\), the local variance is zero, consistently with (5).

**2. Reduction to a finite separable maximization.** Let \(\Delta_i\) be the increase across stratum \(i\) and set \(t_i=n\Delta_i/L\in[0,1]\). Monotonicity and range boundedness give \(\sum_i\Delta_i\le\min\{1,L\}\). Independence of the \(U_i\) and (5) yield
\[
\operatorname{Var}(Q_n(f))\le\frac{L^2}{n^4}\sum_{i=1}^n h(t_i),\qquad
h(t)=\frac{t^2(3-2t)}{12}.\tag{6}
\]
Conversely, every tuple \(t_i\in[0,1]\) satisfying the total-increase constraint is attainable simultaneously at equality, by placing a centered ramp of slope \(L\) in every stratum with \(t_i>0\) and concatenating the constant portions. Since \(h'(t)=t(1-t)/2\) is strictly positive for \(0<t<1\), the maximizing tuple saturates \(\sum_i t_i=s\) unless \(s=n\), in which case all coordinates already equal one.

**3. Pairwise exchange and exact classification of the maximum.** For \(x,y\in[0,1]\), writing \(u=x+y\), direct expansion gives
\[
h(x)+h(y)=h(u)+\frac{u-1}{2}xy.\tag{7}
\]
At fixed \(u<1\), maximizing the right side forces \(xy=0\), so two small positive coordinates can be merged. At fixed \(u>1\), maximizing forces \(x=y=u/2\), so any unequal pair with sum exceeding one can be improved. At \(u=1\), redistributing a pair does not affect the objective.

Choose a global maximizing vector and order its positive entries. If unequal entries \(a<b\) occur, the previous two rules require \(a+b=1\). Every other positive entry \(z\) then satisfies \(a+z\ge1\), hence \(z\ge b\); also \(b+z>1\) unless \(z=a\), so the equalization rule forces \(z=b\). If there are at least three positive entries, replacing the pair \((a,b)\) by \((0,1)\) leaves (7) unchanged, after which the unequal pair \((1,b)\) has sum greater than one and can be improved, a contradiction. With exactly two unequal positive entries, \(a+b=1\), and replacing them by \((0,1)\) gives the same maximum. Therefore some global maximizer has \(k\) equal positive coordinates \(s/k\) and \(n-k\) zeros. Feasibility requires \(\lceil s\rceil\le k\le n\). Substituting into (6) proves (1), with exact attainment.

**4. Maximizing the integer budget and limits.** The objective before the common scaling is
\[
q_s(k)=\frac{s^2}{4k}-\frac{s^3}{6k^2},\qquad
q_s'(k)=\frac{s^2}{k^3}\left(\frac s3-\frac k4\right).
\]
It increases until \(k=4s/3\) and decreases thereafter, proving the finite integer-selection assertion. If \(L\le1\), then \(s=n\) and only \(k=n\) is feasible, yielding the first branch of (2). If \(1\le L\le4/3\), then \(4s/3\ge n\), so \(k=n\) and the second branch follows. If \(L>4/3\) is fixed, \(k=4n/(3L)+O(1)\), whence (3) by substitution. If \(L\ge n\), then \(s\le1\) and \(q_s(1)-q_s(2)=s^2(1-s)/8\ge0\); unimodality gives \(k=1\) as an optimum and (4) follows. This completes the proof.

## Verification

Run `python verify_lipschitz_stratified.py` with a standard Python 3 interpreter. The script uses only the standard library and checks the pairwise polynomial identity with exact fractions, local ramp variance by exact integration, all elementary optimizer branches over a parameter grid, and finite exhaustive families of monotone piecewise-linear functions. These are diagnostic finite checks, not substitutes for the proof of the universal assertions. The theorem's endpoints \(L=1\), \(L=4/3\), \(L=n\), and \(n=1\) are addressed by the symbolic formulas, including ties in the integer maximization.

## Relationship to prior work

Basak, Bect and Vazquez [1, Section 4, Theorem 4.1] prove the sharp \(1/(4n^2)\) variance for equal-width independent stratification over all bounded nondecreasing functions, with a discontinuous midpoint step extremizer. Equation (1) instead solves the Lipschitz-constrained optimization for every finite \(n\) and \(L\), giving continuous extremizers and the nontrivial budget \(k\). Their unrestricted theorem does not determine the quantitative cost of a finite slope bound. Their proof's fixed-increment bound is a starting comparison; (5), (7), and the integer allocation are not stated there.

Pettersson and Krumscheid [2] analyze adaptive stratification for nonsmooth parameter dependence and sample allocation, rather than the sharp variance of a fixed equal-width design over this bounded monotone Lipschitz class. Kunsch [3] studies confidence error bounds and rates in Sobolev classes and designs involving stratified control variates, not this exact monotonicity-and-range-constrained variance envelope. Earlier maximal-variance theory for Lipschitz functions [4] is relevant to the local inequality but is not known here to imply the multi-stratum integer maximization. Adaptive Lipschitz integration [5] optimizes a different algorithmic problem.

## Limitations

The sharp constant is estimator-specific and one-dimensional. It uses independent within-stratum sampling, fixed equal widths and exactly one evaluation per cell. It is not a general optimality theorem among all quadrature methods. Global range \([0,1]\) and monotonicity are essential to the total-variation budget; without either, (1) need not hold. The proof is analytic and the verifier covers only finite diagnostic cases. A specialized prior result phrased as an extremal Lipschitz variance problem might overlap a component; independent historical review remains necessary before publication-priority claims.

## References

[1] S. Basak, J. Bect, E. Vazquez, *Integration of bounded monotone functions: Revisiting the nonsequential case, with a focus on unbiased Monte Carlo (randomized) methods*, arXiv:2203.00423, first public March 1, 2022, Section 4, Theorem 4.1. https://arxiv.org/abs/2203.00423

[2] P. Pettersson, S. Krumscheid, *Adaptive stratified sampling for non-smooth problems*, arXiv:2107.01355, first public July 3, 2021. https://arxiv.org/abs/2107.01355

[3] R. J. Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals*, arXiv:2309.09059, first public September 16, 2023. https://arxiv.org/html/2309.09059v2

[4] S. G. Bobkov, C. Houdré, *Variance of Lipschitz functions and an isoperimetric problem for a class of product measures*, Bernoulli 2 (1996), 249–255. https://doi.org/10.3150/bj/1178291721

[5] I. Baran, E. D. Demaine, D. A. Katz, *Optimally Adaptive Integration of Univariate Lipschitz Functions*, LATIN 2006, 142–153. https://erikdemaine.org/papers/Integration_LATIN2006/
