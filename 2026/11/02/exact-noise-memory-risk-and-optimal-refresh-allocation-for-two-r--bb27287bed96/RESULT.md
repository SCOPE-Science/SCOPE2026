# Exact noise-memory risk and optimal refresh allocation for two-row cyclic Kaczmarz

## Finding

Consider exact full cyclic Kaczmarz sweeps for a consistent two-equation planar linear system, when each equation's noisy observation is independently retained or refreshed between sweeps. The exact limiting Euclidean mean-squared error and the unique optimum of a fixed expected observation-refresh budget can be evaluated without a distributional assumption beyond independent, centered, finite-variance observation innovations.

Write the unit row normals as \(a_1=(1,0)\), \(a_2=(c,s)\), with \(0<c<1\), \(s=\sqrt{1-c^2}>0\). Let \(\sigma_1^2,\sigma_2^2>0\) denote rowwise observation variances, and let \(0\le r_1,r_2\le1\) be the independent per-sweep probabilities of replacing each cached observation by a new draw. The exact limiting risk after complete row-1, row-2 sweeps is

\[
R(r_1,r_2)=\sigma_2^2+\frac{1}{1+c^2}\left[\sigma_1^2\frac{1+c^2(1-r_1)}{1-c^2(1-r_1)}+c^2\sigma_2^2\frac{1+c^2(1-r_2)}{1-c^2(1-r_2)}\right].
\]

Fix an expected new-measurement budget \(r_1+r_2=B\), where \(0<B<2\). Put \(u=c^2\), \(a=1-u\), \(L=\max\{0,B-1\}\), and \(U=\min\{1,B\}\). The unique risk-minimizing choice is

\[
r_1^*=\operatorname{clip}_{[L,U]}\!\left(\frac{(2a+uB)\sigma_1/(\sigma_1+c\sigma_2)-a}{u}\right),\qquad r_2^*=B-r_1^*.
\]

In the interior case (without clipping), the attained minimum is

\[
R_{\min}=\sigma_2^2-\frac{\sigma_1^2+u\sigma_2^2}{1+u}+\frac{2(\sigma_1+c\sigma_2)^2}{(1+u)(2a+uB)}.
\]

For equal variances \(\sigma_1^2=\sigma_2^2=\sigma^2\) and a common refresh rate \(r\), the exact simplification is

\[
R(r,r)=\frac{2\sigma^2}{1-(1-r)c^2}.
\]

In particular, a fixed positive common refresh rate prevents near-parallel divergence, whereas retaining both observations indefinitely gives \(R(0,0)=2\sigma^2/(1-c^2)\). At budget \(B=1\), refreshing only one of the two row observations produces divergent risk as \(c\uparrow1\), whereas refreshing each row with probability \(1/2\) gives a limiting risk of exactly \(4\sigma^2\). Thus a balanced refresh allocation has a qualitative robustness advantage for nearly parallel measurement normals.

## Assumptions and scope

The two rows are linearly independent and Euclidean-unit-normalized, with their signs chosen so that their mutual inner product \(c\) is strictly between zero and one. For any fixed consistent right-hand side \(b\), let \(x_\star\) be its unique solution. At sweep \(k\) the algorithm updates rows in the fixed order \(1,2\), using

\[
x\longleftarrow x+(b_i+\zeta_{i,k}-a_i^\top x)a_i,\qquad i=1,2.
\]

For each row \(i\), start with an independent centered cached error \(\zeta_{i,0}\) of variance \(\sigma_i^2\), having the same law as the subsequent fresh errors. For every subsequent sweep, independently for both rows, use \(\zeta_{i,k}=\zeta_{i,k-1}\) with probability \(1-r_i\), or replace it with an independent fresh centered draw of the same variance with probability \(r_i\). Innovations and refresh indicators are mutually independent across rows and times. The initial iterate is deterministic (or square-integrable and independent of the observation processes). Only complete-sweep iterates are assessed. The formula allows \(r_i=0\) and \(r_i=1\); no Gaussian assumption or ergodicity when \(r_i=0\) is required.

## Proof

**Orthogonal geometric reduction.** Define the orthogonal complement \(v=(-s,c)\) of \(a_2\). The error after sweep \(k\) has the exact representation

\[
e_k=x_k-x_\star=t_kv+\zeta_{2,k}a_2.
\]

Indeed the last row projection sets the row-2 inner product of the error to the current row-2 observation error. Taking the inner product with \(v\) before and after the two row projections gives the scalar recursion

\[
t_k=u t_{k-1}+cs\,\zeta_{2,k-1}-s\,\zeta_{1,k},\qquad u=c^2\in(0,1).
\]

The apparent one-sweep lag of the row-2 observation is essential: the row-2 projection leaves the component along \(v\) unchanged, and that component depends on the row-2 observation used in the preceding sweep.

**Observation autocovariances.** Independent replacement/retention implies each cached-error process is wide-sense stationary with

\[
\mathbb E[\zeta_{i,k}\zeta_{i,k-h}]=\sigma_i^2(1-r_i)^h\qquad(h\ge0).
\]

This follows by iterating conditional expectations: each retention carries the previous error forward, and each independent centered fresh draw contributes zero covariance. Across different rows the entire processes remain independent. The relation holds also at either endpoint \(r_i=0,1\).

**Infinite-sweep calculation.** Since \(0<u<1\), the influence of the initial iterate on \(t_k\) is \(u^kt_0\) and vanishes in mean square. Extending the stationary input history backwards, the unique square-integrable stationary solution is the geometrically summable linear filter

\[
t_\infty=cs\sum_{j\ge0}u^j\zeta_{2,-1-j}-s\sum_{j\ge0}u^j\zeta_{1,-j}.
\]

For any \(0\le\alpha\le1\) the necessary absolutely convergent double sum is

\[
\sum_{j,\ell\ge0}u^{j+\ell}\alpha^{|j-\ell|}=\frac{1+u\alpha}{(1-u^2)(1-u\alpha)}.
\]

To see this, split into diagonal terms, strictly upper terms and strictly lower terms, each a geometric series. Row independence removes mixed contributions, so with \(\alpha_i=1-r_i\),

\[
\operatorname{Var}(t_\infty)=\frac{s^2}{1-u^2}\left[\sigma_1^2\frac{1+u\alpha_1}{1-u\alpha_1}+u\sigma_2^2\frac{1+u\alpha_2}{1-u\alpha_2}\right].
\]

As \(s^2=1-u\), and because \(v\) and \(a_2\) are orthonormal, \(\|e_k\|^2=t_k^2+\zeta_{2,k}^2\); taking limits yields the stated \(R\). This proves existence, not merely a stationary candidate, and does not require tail or moment conditions beyond the second moment.

**Budget optimum.** The identity

\[
\frac{1+u(1-r)}{1-u(1-r)}=\frac{2}{1-u+ur}-1
\]

reduces the varying part of \(R\) to a positive multiple of

\[
\Phi(r_1,r_2)=\frac{\sigma_1^2}{a+ur_1}+\frac{u\sigma_2^2}{a+ur_2}.
\]

On the budget line \(r_1+r_2=B\), the feasible interval is \([L,U]\). Both denominators are strictly positive. The second derivative of \(\Phi(r_1,B-r_1)\) is strictly positive; its unconstrained derivative vanishes exactly when

\[
\frac{a+ur_1}{a+u(B-r_1)}=\frac{\sigma_1}{c\sigma_2}.
\]

Solving for \(r_1\) and projecting onto \([L,U]\) proves the clipped unique optimizer. In the interior, Cauchy--Schwarz on the two terms yields \(\Phi_{\min}=(\sigma_1+c\sigma_2)^2/[2a+uB]\), proving the displayed value. The equal-variance, common-rate expression follows by direct simplification; its near-parallel limits and the divergence of a one-sided budget allocation are immediate from the denominators.

## Verification

The included standalone standard-library Python script `verify.py` constructs the exact conditional polynomial transition for all monomials of degree at most two in the reduced state and both cached errors, by enumerating retention indicators and symmetric two-point centered innovations. It verifies that the closed-form stationary moments satisfy the independent polynomial-transition calculation at a Cartesian grid of rational parameters. Separately it checks the analytic clipped optimizer against a 65-point rational budget grid, and checks the equal-variance simplification. Running `python verify.py` reports `VERIFICATION_OK 8100 exact rational assertions`. All fractions and comparisons in these tests are exact. The tests support, but do not replace, the geometric and infinite-time proofs, and they do not establish generality by finite enumeration.

## Relationship to prior work

Coria, Haddock and Pacheco (2024, arXiv:2403.19874) study quantile randomized Kaczmarz in the presence of time-varying noise and corruption, with expected convergence bounds and horizons rather than exact cyclic two-row covariance under independently retained observations. Marshall and Mickelin (2022, arXiv:2202.12224) analyze noise and a scheduled learning rate for randomized Kaczmarz, but do not resolve this fixed-order, rowwise Bernoulli-cached observation budget. Schöpfer, Lorenz, Tondji and Winkler (2022, arXiv:2201.08620) treat extended sparse randomized Kaczmarz under inconsistent or impulsive-noise settings. General linear-filter covariance and convex allocation principles are established background; the contribution is their exact geometric combination in this specified cyclic row-measurement model, including the sharply defined allocation and near-parallel regime. The investigation does not establish historical priority over all specialized earlier work.

## Limitations

This is a two-row, planar, exact-projection, fixed-order result under independent rowwise stationary replacement noise with unchanged positive variance, not a result for arbitrary higher-dimensional or overdetermined systems. The budget is an expected number of fresh measurements per full sweep and does not incorporate latency, unequal measurement acquisition prices, or a global finite-horizon work optimum. The optimum minimizes asymptotic mean-squared solution error, not transient error or worst-case almost-sure performance. Dependence between row noise streams, biased observations, correlated replacement indicators, and adaptively chosen refresh probabilities are outside scope. Verification is mathematical and computational within the stated model; no independent audit was performed.

## References

1. N. Coria, J. Haddock and J. Pacheco, *On Quantile Randomized Kaczmarz for Linear Systems with Time-Varying Noise and Corruption*, first posted 2024-03-28, https://arxiv.org/abs/2403.19874 .
2. N. F. Marshall and P. Mickelin, *An optimal scheduled learning rate for a randomized Kaczmarz algorithm*, first posted 2022-02-24, https://arxiv.org/abs/2202.12224 .
3. F. Schöpfer, D. A. Lorenz, L. Tondji and M. Winkler, *Extended Randomized Kaczmarz Method for Sparse Least Squares and Impulsive Noise Problems*, first posted 2022-01-21, https://arxiv.org/abs/2201.08620 .
