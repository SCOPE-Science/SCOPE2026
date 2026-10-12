# Exact maximal correlation under Bernoulli thinning of a uniform subset
## Finding
Let integers \(1\le m<n\) be fixed. Let \(T\) be uniform over the \(m\)-subsets of \([n]\). Conditional on \(T\), retain each element independently with probability \(p\in[0,1]\), and call the retained subset \(S\). Put \(K=|S|\). Then the Hirschfeld--Gebelein--Renyi maximal correlation is
\[
R(S,T)^2=\frac{n-m}{m}\,\mathbb E\!\left[\frac{K}{n-K}\right]
=\frac{n-m}{m}\sum_{k=0}^{m}\binom{m}{k}p^k(1-p)^{m-k}\frac{k}{n-k}.
\]
It obeys the sharp elementary bounds
\[
\frac{p(n-m)}{n-mp}\le R(S,T)^2\le p.
\]
For fixed \(p\), if \(m/n\to\alpha\in(0,1)\), then
\[
R(S,T)^2\longrightarrow \frac{p(1-\alpha)}{1-\alpha p}.
\]

There is also an exact marked-subvector consequence. Let \(X_1,\ldots,X_n\) be independent nondegenerate random variables taking values in a general measurable space, independent of \((S,T)\), and let \(\partial\) be an erasure symbol outside that space. Define \(Y_i=X_i\) for \(i\in S\) and \(Y_i=\partial\) otherwise, and define \(Z_i=X_i\) for \(i\in T\) and \(Z_i=\partial\) otherwise. Then
\[
R(Y,Z)=\sqrt p.
\]
Thus Bernoulli thinning has a finite-population correction at the subset-label level, but after independent nondegenerate marks are exposed the exact maximal correlation depends only on the retention probability.

## Assumptions and scope
Maximal correlation is the operator norm of conditional expectation on mean-zero square-integrable functions. The subset formula assumes \(1\le m<n\); the endpoint cases \(p=0\) and \(p=1\) are included. The marked-subvector statement assumes only independence and nondegeneracy of the marks and does not require identical mark distributions.

The source theorem used below treats a fixed retained size: conditional on \(K=k\), the pair \((S,T)\) is exactly a uniform \(k\)-subset nested inside a uniform \(m\)-subset. The present statement concerns the random-size Bernoulli mixture and identifies its exact norm rather than merely averaging pairwise correlations.

## Proof
Let \(f(T)\) be any mean-zero, variance-one square-integrable function. Since \(K\) is measurable from \(S\) and is independent of \(T\), conditioning on \(K=k\) leaves the law of \(T\) uniform on the \(m\)-subsets. Conditional on \(K=k\), the source fixed-size theorem gives
\[
R_k^2=\frac{k(n-m)}{m(n-k)}.
\]
Therefore
\[
\mathbb E\!\left[\mathbb E[f(T)\mid S]^2\right]
=\sum_{k=0}^{m}\Pr(K=k)\,
\mathbb E\!\left[\mathbb E[f(T)\mid S,K=k]^2\mid K=k\right]
\le \sum_{k=0}^{m}\Pr(K=k)R_k^2.
\]
This proves the desired upper bound on the squared operator norm.

The same function attains every conditional bound simultaneously. Let \(I=\mathbf 1_{\{1\in T\}}\), centered and normalized. Given \(K=k\) and \(S\),
\[
\mathbb E[I\mid S,K=k]
=
\begin{cases}
1,&1\in S,\\
\dfrac{m-k}{n-k},&1\notin S.
\end{cases}
\]
Since \(\Pr(1\in S\mid K=k)=k/n\), direct variance calculation gives
\[
\frac{\operatorname{Var}(\mathbb E[I\mid S,K=k])}{\operatorname{Var}(I)}
=\frac{k(n-m)}{m(n-k)}=R_k^2.
\]
After normalization of \(I\), averaging over \(K\) therefore attains the preceding upper bound. This proves the exact formula.

For the bounds, the function \(h(x)=x/(n-x)\) is strictly convex on \([0,m]\). Jensen's inequality yields
\[
\mathbb E h(K)\ge h(mp)=\frac{mp}{n-mp},
\]
which gives the lower bound. Also \(h(k)\le k/(n-m)\) for \(0\le k\le m\), so
\[
\mathbb E h(K)\le \frac{mp}{n-m},
\]
which gives the upper bound. If \(0<p<1\), the Jensen bound is strict; if also \(m\ge2\), the upper bound is strict. For \(m/n\to\alpha\in(0,1)\), the bounded random variables \(K/(n-K)\) converge in probability to \(\alpha p/(1-\alpha p)\), which yields the stated limit.

For the marked subvectors, the source's two-subvector theorem states that
\[
R(Y,Z)=\max\left\{R(S,T),\max_j r_j\right\},
\]
where \(r_j\) is the best constant in its coordinate-incidence bilinear inequality. Here \(S\subseteq T\) and, conditional on \(T\), coordinate \(j\) is retained with probability \(p\). For arbitrary coefficient families \((a_s)\) and \((b_t)\), Cauchy--Schwarz gives
\[
\left|\mathbb E[a_S b_T\mathbf 1_{\{j\in S\}}]\right|
\le
\sqrt{\mathbb E[a_S^2\mathbf 1_{\{j\in S\}}]}
\sqrt{p\,\mathbb E[b_T^2\mathbf 1_{\{j\in T\}}]}.
\]
Hence \(r_j\le\sqrt p\). Constant coefficients attain equality because \(\Pr(j\in S)=p\Pr(j\in T)\), so \(r_j=\sqrt p\). The subset bound already proved gives \(R(S,T)\le\sqrt p\), and therefore \(R(Y,Z)=\sqrt p\).

## Verification
The proof is analytic and uses no finite enumeration as a substitute for an infinite argument. The critical fixed-size norm was checked against the full text of the source theorem, and the equality function is exhibited explicitly. As a nonessential numerical stress test, direct singular-value calculations for the finite joint tables at \((n,m,p)=(4,2,0.3)\), \((5,3,0.7)\), \((6,1,0.4)\), and \((6,4,0.2)\) matched the displayed formula to numerical precision; the proof does not depend on those computations.

Boundary checks are consistent: at \(p=0\), \(S\) is deterministic and both maximal correlations are zero; at \(p=1\), \(S=T\), the subset correlation is one because \(T\) is nondegenerate, and the marked vectors coincide.

## Relationship to prior work
Chang and Chen's current paper gives an exact formula for two fixed-size nested random subsets and an exact reduction for two randomly selected marked subvectors. It explicitly notes that dependent subset pairs are generally difficult and gives the fixed-size nested case as a partial answer. The Bernoulli-thinning result above changes the retained size from deterministic to binomial and proves that the operator norm of the mixture is an exact weighted square average of the fixed-size norms, with one first-order subset statistic attaining every component simultaneously.

Csáki and Fischer's 1963 paper gives the classical eigenvalue calculation for multivariate hypergeometric laws. That result underlies the fixed-size theory but does not state the random-size Bernoulli mixture formula above. Searches under maximal-correlation, random-subset, thinning, Johnson-scheme, Boolean-slice, inclusion-matrix, and erasure-channel terminology did not locate a published statement of the Bernoulli-mixture formula or the marked-subvector identity \(R(Y,Z)=\sqrt p\).

## Limitations
No claim is made for arbitrary dependent thinning, unequal retention probabilities, sampling designs in which \(K\) depends on \(T\), or dependent marks. The exact mixture argument relies on the fact that \(K\) is observed from \(S\), is independent of \(T\), and the same centered coordinate indicator is extremal for every fixed retained size. The main residual originality risk is an equivalent spectral statement in older association-scheme or inclusion-matrix literature expressed without maximal-correlation language.

## References
1. Y. Chang and Q. Chen, *On the maximal correlation of some stochastic processes*, arXiv:2411.17109; Annals of Applied Probability 36 (2026), DOI:10.1214/25-AAP2293. Earliest public version: 2024-11-26.
2. P. Csáki and J. Fischer, *On the General Notion of Maximal Correlation*, A Magyar Tudományos Akadémia Matematikai Kutató Intézetének Közleményei 8 (1963), 27--51; repository record real.mtak.hu:201421.
