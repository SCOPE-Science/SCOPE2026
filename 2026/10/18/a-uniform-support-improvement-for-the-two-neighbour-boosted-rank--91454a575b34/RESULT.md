# A uniform support improvement for the two-neighbour boosted rank correlation

## Finding

For an integer \(n\ge 2\), let \((r_1,\ldots,r_n)\) be any permutation of \((1,\ldots,n)\). In the two-right-neighbour statistic of Lin and Han, set \(j_m(i)=i+m\) if \(i+m\le n\), and \(j_m(i)=i\) otherwise, for \(m=1,2\). Put

\[
\xi_{n,2}=-2+\frac{6}{(n+1)(2n+3/2)}\sum_{i=1}^{n}\sum_{m=1}^{2}\min\{r_i,r_{j_m(i)}\}.
\]

Define the explicit integer

\[
L_n=\sum_{k=1}^{n}\max\left\{0,\left\lceil\frac{3k-n}{2}\right\rceil,\left\lceil\frac{5k-2n}{2}\right\rceil,4k-2n\right\}.
\]

**Claim.** For every \(n\ge2\) and every such rank permutation,

\[
\boxed{\xi_{n,2}\ge -2+\frac{6L_n}{(n+1)(2n+3/2)}}.
\]

Moreover, the finite lower bound has the asymptotic limit

\[
\boxed{-2+\frac{6L_n}{(n+1)(2n+3/2)}\longrightarrow-\frac38}.
\]

Consequently \(\liminf_{n\to\infty}\min_{r\in\mathfrak S_n}\xi_{n,2}\ge-3/8\). This **does not** establish that \(-3/8\) is the attainable limiting minimum. It improves the previously published \(-1/2+O(1/n)\) lower range bound for the fixed choice \(M=2\), by an asymptotic gap of \(1/8\).

## Assumptions and scope

There are no ties in either coordinate of the ranked sample. The ranks in increasing predictor order form an arbitrary permutation, and the two right neighbours use the convention \(j_m(i)=i\) when a corresponding neighbour is absent. The normalization is exactly Lin and Han's normalization for \(M=2\), not that of the original single-neighbour Chatterjee coefficient or a symmetrized version. This is a deterministic support bound, valid for every rank configuration; no distributional assumptions, independence hypothesis, or asymptotic sampling regime are imposed.

## Proof

**1. Threshold decomposition.** Let \(S_\ell=\{i:r_i\ge\ell\}\) for \(1\le\ell\le n\). Write \(x_i={\bf1}\{i\in S\}\) for any subset \(S\subseteq\{1,\ldots,n\}\), and define

\[
\Phi_n(S)=\sum_{i=1}^{n-1}x_ix_{i+1}+\sum_{i=1}^{n-2}x_ix_{i+2}+x_{n-1}+2x_n.
\]

The elementary identity \(\min\{u,v\}=\sum_{\ell=1}^n{\bf1}\{u\ge\ell,v\ge\ell\}\), for integers \(1\le u,v\le n\), gives the exact relation

\[
\sum_{i=1}^n\sum_{m=1}^2\min\{r_i,r_{j_m(i)}\}=\sum_{\ell=1}^n\Phi_n(S_\ell).
\]

The last two terms of \(\Phi_n\) are essential: they represent the self-neighbour cases \((n-1,2)\), \((n,1)\), and \((n,2)\). Since the ranks are a permutation, the cardinalities \(|S_\ell|\) run through \(1,\ldots,n\).

**2. Three supporting inequalities.** We prove for every binary word \((x_1,\ldots,x_n)\) with \(k=\sum_i x_i\) that

\[
\Phi_n(S)\ge0,\qquad \Phi_n(S)\ge\frac{3k-n}{2},\qquad
\Phi_n(S)\ge\frac{5k-2n}{2},\qquad\Phi_n(S)\ge4k-2n.
\]

For the last three inequalities extend the word to the left by \(x_{-1}=x_0=0\). Choose one of the pairs

\[
(s,t)\in\left\{(3/2,1/2),(5/2,1),(4,2)\right\}.
\]

For a two-bit state \((a,b)\), use the following potential \(h(a,b)\):

| \((s,t)\) | \(h(0,0)\) | \(h(0,1)\) | \(h(1,0)\) | \(h(1,1)\) |
| --- | ---: | ---: | ---: | ---: |
| \((3/2,1/2)\) | \(0\) | \(-1\) | \(-1/2\) | \(-1\) |
| \((5/2,1)\) | \(0\) | \(-3/2\) | \(-1\) | \(-2\) |
| \((4,2)\) | \(0\) | \(-2\) | \(-1\) | \(-3\) |

For every one of the eight triples \((a,b,c)\in\{0,1\}^3\), direct substitution shows

\[
\Delta_{s,t}(a,b,c):=c(a+b)-sc+t+h(a,b)-h(b,c)\ge0.
\]

In addition, for every terminal state \((a,b)\in\{0,1\}^2\),

\[
a+2b+h(a,b)\ge0.
\]

Both finite checks are exact rational inequalities; the accompanying verification program enumerates all cases. Summing the transition inequalities and telescoping the potentials yields

\[
\begin{aligned}
\Phi_n(S)-sk+tn
&=\sum_{i=1}^n\Delta_{s,t}(x_{i-2},x_{i-1},x_i)
  +h(x_{n-1},x_n)+x_{n-1}+2x_n\\
&\ge0.
\end{aligned}
\]

Here \(\sum_i x_i(x_{i-2}+x_{i-1})\) is exactly the number of occupied edges of the square of the path, and \(h(0,0)=0\). The terminal boundary term is what removes all constant-size endpoint losses from these inequalities.

**3. Integer strengthening and rank statistic.** The quantity \(\Phi_n(S)\) is an integer. From the four inequalities, if \(|S|=k\), then

\[
\Phi_n(S)\ge H_n(k):=\max\left\{0,\left\lceil\frac{3k-n}{2}\right\rceil,\left\lceil\frac{5k-2n}{2}\right\rceil,4k-2n\right\}.
\]

The threshold identity and the permutation property give \(\sum_{\ell=1}^n\Phi_n(S_\ell)\ge\sum_{k=1}^nH_n(k)=L_n\), proving the finite bound after substitution into the definition of \(\xi_{n,2}\).

**4. Asymptotic constant.** Put

\[
f(z)=\max\left\{0,\frac{3z-1}{2},\frac{5z-2}{2},4z-2\right\},\quad 0\le z\le1.
\]

The function is continuous and piecewise affine with breaks at \(1/3,1/2,2/3\). It is \(0\) on the first interval, and then equals the three respective positive affine pieces. Direct integration gives

\[
\int_0^1 f(z)\,dz=\frac{13}{24}.
\]

Since \(H_n(k)=nf(k/n)+O(1)\) uniformly in \(k\), the Riemann-sum limit is \(L_n/n^2\to13/24\). Therefore

\[
-2+\frac{6L_n}{(n+1)(2n+3/2)}\to-2+\frac{6(13/24)}2=-\frac38.
\]

## Verification

The included `verify.py` uses only the Python standard library. Running `python verify.py` checks all 24 transition slacks and all 12 boundary inequalities exactly as fractions, all \(409112\) distinct-rank permutations across \(2\le n\le9\), and \(131053\) subset states in exact dynamic programs across \(2\le n\le16\). It also checks the exact integral \(13/24\) and reports representative finite lower bounds. These computations are cross-checks; the universal assertion follows from the symbolic potential proof. The finite lower bound is not asserted to be optimal, and the dynamic programs are not asserted to prove any infinite statement.

## Relationship to prior work

Lin and Han (arXiv:2108.06828, initially public August 15, 2021; subsequently *Biometrika* 110, 283–299, 2023) introduced this two-right-neighbour normalization as part of their general \(M\)-neighbour rank correlation and supplied the lower-range guarantee \(-1/2+O(M/n)\). The present claim concerns the deterministic rank support for their precise choice \(M=2\) and gives an explicit all-sample-size strengthening with asymptotic lower endpoint at least \(-3/8\). It neither repeats their null central limit theorem nor alters their statistical consistency theorem.

Dalitz, Arning and Goebbels (2024) discuss finite-sample bounds and rescaling for the **one-neighbour** Chatterjee coefficient, including its upper endpoint. Those assertions do not imply the inequality for the modified two-neighbour statistic, whose boundary self-terms are part of the present proof. Xia, Cao, Du and Chen (2024) introduce a separately weighted rank statistic; its inverse-distance weighting is different from Lin and Han's unweighted two-neighbour definition.

## Limitations

The inequality is a valid universal lower bound, **not** a proof of the exact minimum over permutations, even asymptotically. Nested optimal sets at different thresholds can be incompatible, so pointwise sharpness of the underlying binary-word inequalities would not itself establish sharpness for ranked samples. The finding treats \(M=2\) only, and makes no claim for arbitrary \(M\), tied ranks, modified denominators, or sampling laws. Possible equivalent derivations in the maximal-linear-arrangement and rank-statistics literature remain a historical-priority risk.

## References

1. Z. Lin and F. Han, *On boosting the power of Chatterjee's rank correlation*, arXiv:2108.06828 (first submitted 2021-08-15), *Biometrika* **110** (2023), 283–299. DOI: 10.1093/biomet/asac048. Original preprint: https://arxiv.org/pdf/2108.06828.
2. S. Chatterjee, *A new coefficient of correlation*, *Journal of the American Statistical Association* **116** (2021), 2009–2022.
3. C. Dalitz, J. Arning and S. Goebbels, *A simple bias reduction for Chatterjee's correlation*, *Journal of Statistical Theory and Practice* **18** (2024), article 51. DOI: 10.1007/s42519-024-00399-y.
4. L. Xia, R. Cao, J. Du and X. Chen, *The improved correlation coefficient of Chatterjee*, *Journal of Nonparametric Statistics* **37** (2025), 265–281; first publicly available 2024. DOI: 10.1080/10485252.2024.2373242.
