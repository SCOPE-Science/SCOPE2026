# Sharp median-rank Wasserstein contraction for empirical quantile-clipped SGD

## Finding

For exact empirical-quantile clipping of one-dimensional quadratic component losses, there is a sharp **majority-rank criterion** for universal Wasserstein contraction. Let \(m\ge2\), \(1\le k\le m\), and \(a_1,\ldots,a_m\in\mathbb R\). Define
\[
\tau_k(x)=\operatorname{order}_k\bigl(|x-a_1|,\ldots,|x-a_m|\bigr),\qquad
g_i(x)=\max\bigl(-\tau_k(x),\min(x-a_i,\tau_k(x))\bigr).
\]
Let \(I_t\) be independent uniform choices from \(\{1,\ldots,m\}\), and let the exact-quantile update be
\[
X_{t+1}=X_t-\eta g_{I_t}(X_t),\qquad \eta>0.
\]
Writing \(s_{m,k}=(2k-m)/m\) and \(q_{m,k}(\eta)=1-2\eta s_{m,k}+\eta^2\), the mean clipped direction is \(1\)-Lipschitz and has lower secant slope \(s_{m,k}\). The transition kernel has the **sharp data-uniform** Lipschitz estimate
\[
 W_2(P(x,\cdot),P(y,\cdot))^2\le q_{m,k}(\eta)(x-y)^2.
\]
For every dataset, strictly above-median ranks \(k>m/2\) and steps \(0<\eta<2s_{m,k}\) imply one invariant probability measure of finite second moment and geometric \(W_2\) convergence from every initial measure of finite second moment. The same factor is attained on a two-location dataset. At or below the median rank, datasets with two absorbing states exist. Beyond the stated step interval, the sharp one-step Lipschitz factor is at least one, without asserting that every individual dataset diverges.

Importantly, this geometric \(W_2\) convergence does not imply convergence in total variation. Already ordinary Bernoulli SGD, which is the highest-rank member of the same family, has an invariant uniform law and finitely supported finite-time laws.

## Assumptions and scope

The component losses are \(f_i(x)=\tfrac12(x-a_i)^2\), all with unit curvature. Ties in the empirical order statistic are retained with multiplicity. The clipping threshold is recomputed *exactly* from the full fixed dataset at the current iterate, before one component is sampled with replacement. This is not a rolling quantile estimate, a minibatch quantile estimate, a noisy private update, or a high-dimensional gradient rule.

The quadratic Wasserstein distance \(W_2\) is defined on \(\mathcal P_2(\mathbb R)\), the probability measures with finite second moments. The standard total-variation distance between two laws is \(\sup_B|\mu(B)-\nu(B)|\). Constants are uniform over all locations and repetitions in the fixed finite dataset. No independence is assumed between successive iterates, only between freshly drawn sample indices.

For \(p\in(0,1]\), choosing the left empirical \(p\)-quantile corresponds to \(k=\lceil pm\rceil\). Thus the exact criterion is on **rank**, rather than a rounded verbal median convention. The theorem does not claim convergence of the iterates to the ordinary least-squares minimizer: clipping can alter the drift's zero.

## Proof

**Order-statistic geometry.** Every function \(d_i(x)=|x-a_i|\) is \(1\)-Lipschitz; consequently their \(k\)-th order statistic \(\tau_k\) is \(1\)-Lipschitz. Partition the real line at all data locations and all pair midpoints \((a_i+a_j)/2\). On each open interval of this finite partition, the order of all distances is fixed and \(\tau_k(x)=|x-a_j|\) for some fixed index \(j\). Every \(g_i\) is continuous and affine on each such interval, with slope \(1\) if \(|x-a_i|\le\tau_k(x)\) and slope either \(-1\) or \(1\) otherwise. Equal data locations contribute identical affine residuals, so ties cause no exception. Thus every \(g_i\) is globally \(1\)-Lipschitz.

**Sharp mean secant bound.** At least \(k\) of the \(m\) gradients are unclipped on any open partition interval. Their derivatives equal \(1\); derivatives of the remaining at most \(m-k\) functions are bounded below by \(-1\). Hence, wherever the mean \(h(x)=m^{-1}\sum_i g_i(x)\) is differentiable,
\[
 \frac{2k-m}{m}\le h'(x)\le1.
\]
It is continuous and piecewise affine, so integration over partition intervals gives, for every \(x<y\),
\[
 s_{m,k}(y-x)\le h(y)-h(x)\le y-x.
\]
If \(k>m/2\), the lower slope is positive, so the mean direction also has a unique zero. This zero need not equal the mean of the data.

**Mean-square coupling and invariant law.** Use the same index \(I\) to update two states \(x,y\). Writing \(\Delta_i=g_i(x)-g_i(y)\), the preceding two bounds imply
\[
\begin{aligned}
\mathbb E_I\left|(x-\eta g_I(x))-(y-\eta g_I(y))\right|^2
&=(x-y)^2-2\eta(x-y)(h(x)-h(y))
 +\frac{\eta^2}{m}\sum_i\Delta_i^2\\
&\le (1-2\eta s_{m,k}+\eta^2)(x-y)^2.
\end{aligned}
\]
For arbitrary input laws, apply this inequality to an optimal \(W_2\) coupling, independent of the common fresh index. It proves \(W_2(\mu P,\nu P)\le\sqrt{q_{m,k}(\eta)}W_2(\mu,\nu)\). Since each affine-piecewise map \(x\mapsto x-\eta g_i(x)\) has linear growth, the Markov operator sends \(\mathcal P_2(\mathbb R)\) into itself. For \(k>m/2\) and \(0<\eta<2s_{m,k}\), its contraction coefficient is strictly below one. Completeness of \((\mathcal P_2(\mathbb R),W_2)\) and the contraction fixed-point theorem yield the unique invariant law \(\pi\), with
\[
W_2(\mu P^t,\pi)\le q_{m,k}(\eta)^{t/2}W_2(\mu,\pi),\qquad t=0,1,2,\ldots.
\]
No density, irreducibility, or total-variation minorization hypothesis is used.

**Attainment and sharp parameter boundaries.** If \(k<m\), choose \(k\) copies of \(0\) and \(m-k\) copies of \(L>0\). At all \(0<x<L/2\), the empirical threshold is \(\tau_k(x)=x\). A sample from the first location gives \(g_i(x)=x\); one from the second gives \(g_i(x)=-x\). The transition from \(x\) is the two-point law of \((1-\eta)x\) with mass \(k/m\) and \((1+\eta)x\) with mass \((m-k)/m\). For \(0<x<y<L/2\), the monotone coupling of these two-point laws is optimal for \(W_2\) in one dimension. Its squared transport cost is exactly
\[
\left[\frac{k}{m}(1-\eta)^2+\frac{m-k}{m}(1+\eta)^2\right](y-x)^2
=q_{m,k}(\eta)(y-x)^2.
\]
For \(k=m\), use any dataset with all points equal; the transition is deterministic with exactly the same factor \((1-\eta)^2=q_{m,m}(\eta)\). Therefore the displayed data-uniform bound is optimal for every rank and stepsize. For \(k>m/2\) and \(\eta\ge2s_{m,k}\), this sharp factor is at least one, so no better uniform **strict one-step** \(W_2\) bound is possible.

If \(k\le m/2\), use the same two-location data with \(k\) zeros and \(m-k\) copies of \(L\). Because each location occurs at least \(k\) times, \(\tau_k(0)=\tau_k(L)=0\), so both \(0\) and \(L\) are absorbing under every positive stepsize. Hence their distinct Dirac masses are invariant; data-uniform uniqueness fails at and below the median rank.

**Failure of total-variation mixing above the threshold.** Take \(m=k=2\), \((a_1,a_2)=(0,1)\), \(\eta=1/2\). There is no clipping, and the update is \(X_{t+1}=(X_t+B_t)/2\) with independent fair \(B_t\in\{0,1\}\). Lebesgue-uniform measure on \([0,1]\) is invariant because \((U+B)/2\) is uniform if \(U\) is. The contraction argument proves it is unique. From any deterministic \(X_0\), the law at each finite time has at most \(2^t\) atoms; those atoms form a Lebesgue-null set to which the law assigns probability one. Therefore its total-variation distance from the invariant uniform law equals exactly \(1\) for every finite \(t\), despite \(W_2\) decay by \(2^{-t}\).

## Verification

The included standalone Python 3 program `verify_empirical_qc.py` uses only `fractions.Fraction` and `itertools`. It enumerates every multiset of sizes \(2\) through \(8\) from six integer data locations and every rank, verifies the predicted piecewise-affine slopes and interval-endpoint inequalities using exact rational arithmetic, checks sharp two-point \(W_2\) factors for many larger ranks, and checks the two absorbing states below the median. Reproduction command:

```bash
python3 verify_empirical_qc.py
```

Recorded successful output: `PASS: 282876 exact rational slope/endpoint tests; 272 attained contraction factors; 289 non-uniqueness examples.` The proof of the universal theorem is analytic; no finite test count is represented as exhaustive over arbitrary real data or infinite time.

## Relationship to prior work

Merad and Gaïffas introduced quantile-clipped SGD and proved invariant-law guarantees using diffuse-noise hypotheses for their Markov-chain analysis. Shulgin and Richtárik studied convergence and bias of quantile-clipped SGD through general descent bounds, while Koloskova, Hendrikx, and Stich studied fixed-radius clipped SGD and its unavoidable bias. Andrew and collaborators developed adaptive quantile clipping for private federated learning. The present result addresses a different exact finite-data phenomenon: a sharp median-*rank* threshold for global synchronous mean-square and Wasserstein contraction, together with examples distinguishing Wasserstein and total-variation convergence. The contraction mapping theorem and one-dimensional monotone optimal transport are standard ingredients, not claimed as newly discovered tools.

## Limitations

The guarantees apply to unit-curvature, one-dimensional quadratic components, fixed finite datasets, exact full-population empirical quantiles, fresh sampling with replacement, and the specified constant step intervals. They do not establish global contraction for heterogeneous curvature or vector-valued gradients, nor account for errors in estimated or rolling quantiles, differential-privacy noise, time-varying data, or adversarial corruption. Geometric Wasserstein convergence concerns the law of the stochastic iterate, not almost-sure convergence to the optimizer. For steps beyond the uniform contraction boundary, the result only rules out a universal strict one-step contraction, not stability of every individual dataset. Literature overlap remains subject to discovery of equivalent results not indexed by the checked sources.

## References

1. I. Merad and S. Gaïffas, *Robust Stochastic Optimization via Gradient Quantile Clipping*, arXiv:2309.17316, first posted 2023-09-29, https://arxiv.org/abs/2309.17316.
2. E. Shulgin and P. Richtárik, *On the Convergence of DP-SGD with Adaptive Clipping*, arXiv:2412.19916, first posted 2024-12-27, https://arxiv.org/abs/2412.19916.
3. A. Koloskova, H. Hendrikx and S. U. Stich, *Revisiting Gradient Clipping: Stochastic Bias and Tight Convergence Guarantees*, arXiv:2305.01588, first posted 2023-05-02, https://arxiv.org/abs/2305.01588.
4. G. Andrew, O. Thakkar, H. B. McMahan and S. Ramaswamy, *Differentially Private Learning with Adaptive Clipping*, arXiv:1905.03871, first posted 2019-05-09, https://arxiv.org/abs/1905.03871.
