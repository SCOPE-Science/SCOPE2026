# Overlap-sensitive concentration for nonuniform prediction horizons

## Finding

Let \((\mathcal F_t)_{t\in\mathbb Z}\) be a filtration and let \(Y_1,\ldots,Y_N\) be adapted random variables with \(|Y_n|\le 1\) almost surely. Fix deterministic integer horizons \(K_n\ge 1\), and define
\[
Z_n=Y_n-\mathbb E(Y_n\mid\mathcal F_{n-K_n}),\qquad
I_n=\{n-K_n+1,\ldots,n\}.
\]
Let
\[
\Delta=\max_{t\in\mathbb Z}\#\{n\in\{1,\ldots,N\}:t\in I_n\}
\]
be the maximum overlap of the backward information windows. Then, for every \(x\ge0\),
\[
\Pr\!\left(\left|\sum_{n=1}^N Z_n\right|\ge x\right)
\le 2\exp\!\left(-\frac{x^2}{8\Delta N}\right).
\]
Equivalently, for every \(\epsilon\in(0,1)\),
\[
\Pr\!\left(\left|\sum_{n=1}^N Z_n\right|
\ge\sqrt{8\Delta N\log(2/\epsilon)}\right)\le\epsilon.
\]
For a triangular array of deterministic horizons, if \(\Delta_N=o(N)\), then
\[
\frac1N\sum_{n=1}^N
\left(Y_{n,N}-\mathbb E(Y_{n,N}\mid\mathcal F_{n-K_{n,N}})\right)
\xrightarrow{\Pr}0.
\]
Thus the sufficient complexity parameter is maximum simultaneous overlap, not the largest individual horizon.

## Assumptions and scope

The filtration is increasing and indexed by all integers, as in the fixed-horizon theorem motivating this result. Each \(Y_n\) is \(\mathcal F_n\)-measurable and bounded by \(1\) in absolute value. Every \(K_n\) is a deterministic, prespecified positive integer; data-dependent or random horizons are not covered. No independence between the \(Y_n\) is assumed.

The intervals \(I_n\) contain exactly the indices between the conditioning time \(n-K_n\) and the observation time \(n\). The overlap number \(\Delta\) is an integer between \(1\) and \(N\).

## Proof

The intervals \(I_n\) form an interval graph whose clique number is \(\Delta\). Greedy interval coloring partitions them into at most \(\Delta\) classes, with pairwise disjoint intervals within each class. Let the nonempty classes be indexed by \(c\), let \(r_c\) be the number of terms in class \(c\), and put \(S_c=\sum_{n\in c}Z_n\). Then \(\sum_c r_c=N\).

Fix one class and list its indices as \(n_1<\cdots<n_{r_c}\). Disjointness gives \(n_{j-1}\le n_j-K_{n_j}\) for each \(j\ge2\). Hence every earlier term in this class is measurable with respect to \(\mathcal F_{n_j-K_{n_j}}\). By iterated conditioning,
\[
\mathbb E(Z_{n_j}\mid\mathcal F_{n_{j-1}})=0.
\]
Also \(|Z_{n_j}|\le2\). Conditional Hoeffding's lemma therefore yields
\[
\mathbb E(e^{\lambda Z_{n_j}}\mid\mathcal F_{n_{j-1}})
\le e^{2\lambda^2}\qquad(\lambda\in\mathbb R).
\]
Iterating this inequality, including the first term by its unconditional version, gives
\[
\mathbb E e^{\lambda S_c}\le e^{2\lambda^2r_c}.
\]

Write \(R=(\sum_c\sqrt{r_c})^2\) and choose
\[
p_c=\frac{\sum_d\sqrt{r_d}}{\sqrt{r_c}}.
\]
Then \(p_c\ge1\), \(\sum_c1/p_c=1\), and \(\sum_c p_cr_c=R\). Generalized Hölder's inequality and the classwise moment bounds imply
\[
\begin{aligned}
\mathbb E e^{\lambda\sum_cS_c}
&\le\prod_c\left(\mathbb E e^{p_c\lambda S_c}\right)^{1/p_c}\\
&\le\exp\!\left(2\lambda^2\sum_cp_cr_c\right)
=\exp(2\lambda^2R).
\end{aligned}
\]
Chernoff's bound, optimized at \(\lambda=x/(4R)\), gives
\[
\Pr\!\left(\left|\sum_cS_c\right|\ge x\right)
\le2e^{-x^2/(8R)}.
\]
Finally, Cauchy–Schwarz gives \(R\le(\#\{c\})\sum_cr_c\le\Delta N\), proving the stated inequality.

For a concrete boundary case, take \(K_n=1\) for \(n<N\) and \(K_N=N\). The maximum horizon is \(N\), but the windows overlap at most twice, so \(\Delta=2\). The bound is still of order \(\sqrt N\) at fixed confidence. More generally, substituting \(x=\delta N\) shows that the normalized sum converges to zero in probability whenever \(\Delta_N/N\to0\).

## Verification

The proof establishes the bound for every finite \(N\), every deterministic horizon pattern, and every increasing two-sided filtration satisfying the stated assumptions. The constant follows from the conditional range \([-2,2]\), interval coloring, generalized Hölder, and Chernoff optimization. No finite enumeration or numerical experiment is used as evidence for the universal statement.

## Relationship to prior work

Vovk's fixed-horizon result treats a single common horizon \(K\) and proves a bound of order \(\sqrt{K(N+K)\log(1/\epsilon)}\). Its proof groups observations by residue classes modulo \(K\). The present result replaces that fixed partition by a coloring of the actual backward information windows and uses their maximum overlap \(\Delta\). When every \(K_n=K\le N\), \(\Delta=K\); when horizons vary, the overlap parameter can be much smaller than \(\max_n K_n\). The fixed-horizon theorem does not directly yield this dependence for arbitrary deterministic \(K_n\).

## Limitations

The overlap bound is sufficient; no matching lower bound is claimed for every horizon pattern. Random or data-adaptive horizons, unbounded variables, strong laws, central limit theorems, and optimal constants beyond the stated inequality remain outside the result. A bounded literature search cannot prove absolute novelty, and an equivalent statement in unindexed general martingale concentration literature remains possible.

## References

1. V. Vovk, “A law of large numbers for predicting several steps ahead,” first posted 24 August 2025, arXiv:2508.17507; published in *Statistics and Probability Letters* 236 (2026), article 110785, DOI: 10.1016/j.spl.2026.110785. Preprint: https://arxiv.org/abs/2508.17507.
