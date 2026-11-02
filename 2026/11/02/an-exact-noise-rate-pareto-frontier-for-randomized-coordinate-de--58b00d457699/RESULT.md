# An exact noise–rate Pareto frontier for randomized coordinate descent

## Finding

For a diagonal strongly convex quadratic with persistent unbiased additive noise in the selected coordinate-gradient oracle, the globally least stationary objective error attainable by *jointly choosing all independent coordinate-sampling probabilities and all coordinate-specific constant steps* at a prescribed sharp mean-square convergence rate has a unique, one-scalar solution. A notable structural feature is that the optimal sampling probabilities approach square-root noise-curvature weights at slow rates, but their *excess above the mandatory selection probabilities* approaches squared noise-curvature weights near the fastest possible rate.

Let the dimension satisfy \(d\ge 2\), let \(\lambda_i,\sigma_i^2>0\), and put \(w_i=\sigma_i^2/(2\lambda_i)\). For a prescribed contraction deficit \(\tau\in(0,1/d)\), define \(u_i(k)\in(0,1)\) by

\[
 u_i(k)=\frac{2}{2+k/w_i+\sqrt{(k/w_i)(k/w_i+4)}},\qquad k>0.
\]

There is a unique \(k=k_\tau>0\) satisfying

\[
 \sum_{i=1}^d\frac{\tau}{1-u_i(k)^2}=1.
\]

The unique optimal probability and step-size vectors are

\[
 p_i^*=\frac{\tau}{1-u_i(k_\tau)^2},\qquad
 \eta_i^*=\frac{1-u_i(k_\tau)}{\lambda_i}.
\]

The optimal stationary loss is

\[
 \mathcal F_*(\tau)=\sum_{i=1}^d w_i\frac{1-u_i(k_\tau)}{1+u_i(k_\tau)}.
\]

At the fastest feasible rate \(\tau=1/d\), the unique optimum is \(p_i^*=1/d\), \(\eta_i^*=1/\lambda_i\), and \(\mathcal F_*(1/d)=\sum_i w_i\). No design can satisfy the prescribed factor if \(\tau>1/d\).

The opposite endpoints obey the two distinct sampling laws

\[
 \lim_{\tau\downarrow0}p_i^*=\frac{\sqrt{w_i}}{\sum_j\sqrt{w_j}},\qquad
 \mathcal F_*(\tau)=\frac{\tau}{4}\left(\sum_i\sqrt{w_i}\right)^2+o(\tau).
\]

For \(\delta=1-d\tau\downarrow0\),

\[
 p_i^*=\tau+\delta\frac{w_i^2}{\sum_jw_j^2}+o(\delta),\qquad
 \mathcal F_*(\tau)=\sum_iw_i-2\sqrt{\frac{\delta}{\tau}}\sqrt{\sum_iw_i^2}+O(\delta).
\]

## Assumptions and scope

Consider \(f(x)=\frac12\sum_{i=1}^d\lambda_i x_i^2\) on \(\mathbb R^d\), with fixed \(d\ge2\) and \(\lambda_i>0\). At each integer time choose \(I_n\) independently, with \(\Pr(I_n=i)=p_i>0\) and \(\sum_i p_i=1\). Given \(I_n=i\), evaluate \(\lambda_i X_{n,i}+\xi_{n,i}\), where the centered noise has variance \(\sigma_i^2\in(0,\infty)\), is independent of the iterate and past and of the coordinate draw, and the collection of sampling rounds is independent. Update only the selected coordinate, using \(\eta_i>0\). No Gaussian assumption on the noise is needed.

Write \(s_i=\lambda_i\eta_i\in(0,2)\). The second-moment transient factor is defined as the smallest \(r\ge0\) such that, for *every* finite-second-moment initial distribution,

\[
 \left|\mathbb E f(X_n)-\mathcal F(p,s)\right|
 \le r^n\sum_i\frac{\lambda_i}{2}\left|\mathbb E X_{0,i}^2-v_i^*\right|,
\]

where \(v_i^*\) denotes the stationary coordinate second moment and \(\mathcal F(p,s)\) is stationary expected objective. The sharp factor is \(r(p,s)=\max_i[1-p_is_i(2-s_i)]\): it is attained by an initial second-moment perturbation supported on a maximizing coordinate. A demanded rate means \(r(p,s)\le1-\tau\) with \(\tau>0\). This definition concerns second moments, not a sample-path geometric rate.

## Proof

**1. Exact stationary moments and sharp rate.** With \(v_{n,i}=\mathbb E X_{n,i}^2\), conditional expectation, centering, and independence give

\[
 v_{n+1,i}=\bigl[1-p_is_i(2-s_i)\bigr]v_{n,i}
 +\frac{p_is_i^2\sigma_i^2}{\lambda_i^2}.
\]

Every scalar coefficient lies strictly between zero and one. Therefore

\[
 v_i^*=\frac{s_i\sigma_i^2}{\lambda_i^2(2-s_i)},\quad
 \mathcal F(p,s)=\sum_i w_i\frac{s_i}{2-s_i},\quad
 r(p,s)=\max_i[1-p_is_i(2-s_i)].
\]

For completeness, couple two copies by using the same coordinate selection and noise each round. Their squared Euclidean separation contracts in expectation by at most \(r(p,s)\), and the transition preserves finite second moments. Hence the transition is a strict Wasserstein-two contraction and has a unique finite-second-moment invariant distribution. The scalar recursion proves the advertised sharp second-moment transient coefficient and its attainability. The stationary loss depends on the sampling probabilities only through the rate constraints, not directly.

**2. Feasibility and individual step optimization.** Since \(0<s_i(2-s_i)\le1\), the constraints \(p_is_i(2-s_i)\ge\tau\) require \(p_i\ge\tau\), and consequently \(d\tau\le1\). Conversely, for \(0<\tau\le1/d\), a uniform probability vector with unit normalized steps is feasible. Since \(s/(2-s)\) strictly increases on \((0,2)\), the smallest admissible normalized step for given \(p_i\ge\tau\) is

\[
 s_i=1-\sqrt{1-\tau/p_i}.
\]

Every optimal rate constraint is therefore tight. Substitution gives the reduced constrained problem

\[
 \min_{p_i\ge\tau,\ \sum_i p_i=1}
 \Phi_\tau(p)=\sum_iw_i
 \frac{1-\sqrt{1-\tau/p_i}}{1+\sqrt{1-\tau/p_i}}.
\]

**3. Strict convexity, uniqueness, and scalar root.** For \(p>\tau\), put \(u=\sqrt{1-\tau/p}\). Direct differentiation gives

\[
 \frac{d}{dp}\left[w_i\frac{1-u}{1+u}\right]
 =-\frac{w_i\tau}{p^2u(1+u)^2}.
\]

The positive denominator strictly increases with \(p\), so each summand is strictly convex. The derivative tends to minus infinity as \(p\downarrow\tau\). If \(\tau<1/d\), a minimizer cannot have \(p_i=\tau\): shifting a small mass to that coordinate yields a leading gain of order the square root of the mass, while any donor coordinate loses only a linear amount. Thus the unique minimizer lies in the interior. Its Lagrange multiplier \(\mu>0\) obeys

\[
 \frac{w_i\tau}{p_i^2u_i(1+u_i)^2}=\mu.
\]

The identity \(p_i=\tau/(1-u_i^2)\) turns this into

\[
 w_i\frac{(1-u_i)^2}{u_i}=k,\qquad k=\mu\tau.
\]

Solving the quadratic for the root \(u_i\in(0,1)\) gives the stated \(u_i(k)\). As \(k\) increases from zero to infinity, each \(u_i(k)\) decreases strictly from one to zero. Consequently \(\sum_i\tau/(1-u_i(k)^2)\) decreases strictly from infinity to \(d\tau<1\), producing exactly one positive root. Strict convexity proves global, not merely local, optimality. At \(\tau=1/d\), the constraints force \(p_i=\tau\) and \(s_i=1\), so the endpoint is also unique.

**4. Slow-rate asymptotics.** As \(\tau\downarrow0\), a feasible design with fixed strictly positive probabilities has loss \(O(\tau)\); hence the minimum does also. Since \(s_i\ge\tau/(2p_i)\), the minimum cannot have any \(p_i\) tending to zero: its corresponding contribution would make \(\mathcal F_*(\tau)/\tau\) unbounded. Uniformly on probabilities bounded away from zero,

\[
 \frac{1-\sqrt{1-\tau/p_i}}{1+\sqrt{1-\tau/p_i}}
 =\frac{\tau}{4p_i}+O(\tau^2).
\]

Cauchy–Schwarz gives \(\sum_iw_i/p_i\ge(\sum_i\sqrt{w_i})^2\), with equality only when \(p_i\propto\sqrt{w_i}\). Compactness and uniqueness yield both the probability limit and the loss expansion.

**5. Fast-rate boundary layer.** Write \(\delta=1-d\tau\) and \(p_i=\tau+\delta a_i\), with \(a_i\ge0\), \(\sum_i a_i=1\). Then

\[
 u_i=\sqrt{\frac{\delta a_i}{\tau+\delta a_i}}
 =\sqrt{\frac\delta\tau}\sqrt{a_i}+O(\delta^{3/2}),
\]

uniformly for \(a_i\in[0,1]\) as \(\delta\downarrow0\). Expanding the objective gives

\[
 \Phi_\tau(p)=\sum_iw_i
 -2\sqrt{\frac\delta\tau}\sum_iw_i\sqrt{a_i}+O(\delta)
\]

uniformly on the simplex. By Cauchy–Schwarz, \(\sum_iw_i\sqrt{a_i}\le\sqrt{\sum_iw_i^2}\), with a unique maximizer \(a_i=w_i^2/\sum_jw_j^2\). Uniform convergence of the rescaled objective and uniqueness imply \(a_i\to w_i^2/\sum_jw_j^2\). This proves the squared-weight excess law and the sharp square-root drop of the optimal loss.

## Verification

The self-contained Python file `verify.py` runs without dependencies beyond the standard library. Execute `python verify.py`. It checks 9,499 exact-rational and numerical assertions, including the moment fixed-point identity, the unique scalar design's feasibility and equal marginal derivatives, thousands of competing feasible probability vectors, both boundary asymptotics, and a two-coordinate example. Numerical tests are finite cross-checks; the preceding calculus and contraction arguments prove the universal result.

For \(d=2\), \(\lambda_1=\lambda_2=1\), \(\sigma_1=1\), \(\sigma_2=3\), and \(\tau=0.1\), the optimum has \(p_1\approx0.277779\), \(p_2\approx0.722221\) with \(\mathcal F_*\approx0.223143\). Uniform selection, optimally matched individual steps for the same factor, gives \(\mathcal F\approx0.278640\), a roughly 20% higher stationary objective loss.

## Relationship to prior work

Ding et al. introduced and analyzed noisy random coordinate descent under a local Polyak–Łojasiewicz condition and emphasized its single-partial-derivative cost (arXiv:2311.00088, posted October 31, 2023). Their uniform-coordinate formulation and convergence/stability bounds do not state the joint stationary-loss minimax design derived here. Qu and Richtárik developed arbitrary coordinate sampling and complexity theory (arXiv:1412.8060), but the accessible abstract does not specify an exact additive-noise stationary Pareto frontier. Richtárik and Takáč analyzed optimal nonuniform probabilities and coordinate steps for the NSync method (DOI:10.1007/s11590-015-0916-1), with a deterministic-iteration-complexity objective rather than a persistent-noise stationary-error objective. Rodomanov and Kropotov analyzed volume sampling and deterministic convergence rates (DOI:10.1137/19M125532X); their abstract does not claim our noise-weighted optimum. These are substantive precedents, not novelty proofs; the possibility of prior equivalent statements in broader noise-aware design literature remains.

## Limitations

The loss/rate design is exact for independent single-coordinate updates of *diagonal* positive-definite quadratics with nonzero finite coordinate-noise variances and independent sampling rounds. It does not cover correlated or state-dependent oracle noise, nonseparable Hessians, state-adaptive coordinate distributions, variable steps, wall-clock costs varying by coordinate, or tail-probability objectives. The comparator rate is an exact second-moment transient rate; it is not a claim about pathwise convergence or the best finite-horizon expected loss. Publication priority remains subject to broader literature and independent expert evaluation.

## References

1. Z. Ding, T. Ko, J. Yao, L. Lin, and X. Li, *Random coordinate descent: a simple alternative for optimizing parameterized quantum circuits*, arXiv:2311.00088 (first posted October 31, 2023), https://arxiv.org/abs/2311.00088 .
2. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling I: Algorithms and Complexity*, arXiv:1412.8060 (2015), https://arxiv.org/abs/1412.8060 .
3. P. Richtárik and M. Takáč, *On optimal probabilities in stochastic coordinate descent methods*, Optimization Letters 10 (2016), first published online July 2, 2015, https://doi.org/10.1007/s11590-015-0916-1 .
4. A. Rodomanov and D. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, SIAM Journal on Optimization 30 (2020), 1878–1904, https://doi.org/10.1137/19M125532X .
