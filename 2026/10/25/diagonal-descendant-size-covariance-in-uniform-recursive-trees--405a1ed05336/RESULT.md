# Diagonal descendant-size covariance in uniform recursive trees

## Finding

Let \(T_n\) be the uniform recursive tree on the chronological labels \(1,\dots,n\): each vertex \(t\ge2\) attaches independently to a uniformly selected vertex in \(\{1,\ldots,t-1\}\). Let \(S_i(n)\) be the size of the complete descendant subtree rooted at birth label \(i\), counting \(i\) itself. For every integer \(n\ge1\), the covariance matrix of \((S_1(n),\ldots,S_n(n))\) is *exactly diagonal*, despite the subtrees being nested or disjoint according to the random genealogy. Specifically,

\[
\mathbb E S_i(n)=\frac ni,\qquad
\operatorname{Cov}(S_i(n),S_j(n))=
\begin{cases}
\displaystyle\frac{n(n-i)(i-1)}{i^2(i+1)},&i=j,\\
0,&i\ne j.
\end{cases}
\]

Consequently, every real weighted descendant-size score \(W_n=\sum_{i=1}^n a_iS_i(n)\) has the **exact variance decomposition**
\[
\operatorname{Var}(W_n)=\sum_{i=2}^{n-1}a_i^2\frac{n(n-i)(i-1)}{i^2(i+1)}.
\]
In particular, for \(n\ge3\) the covariance matrix has rank \(n-2\), with zero modes at the deterministic root and latest-born vertex.

The total internal path length \(P_n\), the sum of the root distances of all vertices, satisfies \(P_n=\sum_{i=2}^n S_i(n)\). Therefore
\[
\mathbb E P_n=n(H_n-1),\qquad
\operatorname{Var}(P_n)=2n^2-nH_n-n^2H_n^{(2)},
\]
where \(H_n=\sum_{j=1}^n1/j\) and \(H_n^{(2)}=\sum_{j=1}^n1/j^2\). More precisely, \(\operatorname{Cov}(P_n,S_i(n))=\operatorname{Var}(S_i(n))\) for every \(i\ge2\), so the fluctuation of each birth-indexed subtree accounts for one orthogonal contribution to global path-length variance.

For every fixed \(k\ge2\), the asymptotic fraction of the path-length variance remaining after the optimal linear predictor using descendant sizes at labels \(2,\ldots,k\) equals
\[
\frac{\displaystyle\sum_{i=k+1}^{\infty}\frac{i-1}{i^2(i+1)}}{2-\pi^2/6}.
\]
This fraction is positive for every finite \(k\), bounded above by \(1/[k(2-\pi^2/6)]\), and decreases to zero as \(k\to\infty\). Thus the growing path-length fluctuations are asymptotically localized in the earliest birth-indexed descendant sizes.

## Assumptions and scope

The parent choices at distinct times are independent and uniform among all existing vertices. Subtree size counts all descendants, including the specified root of the subtree. Labels are *birth times*, not degree rankings or depths. All exact equations hold for finite integers \(n\ge1\); the rank statement assumes \(n\ge3\), and the variance-localization limit first sends \(n\to\infty\) at fixed \(k\), then \(k\to\infty\). No independence of distinct subtree-size variables is claimed.

## Proof

**One-point moments.** At time \(t\ge i\), conditionally on the tree, a newly arriving vertex joins the descendant subtree at \(i\) with probability \(S_i(t)/t\). For \(i\ge2\), the process starts with one descendant and \(i-1\) non-descendants at time \(i\), hence is the classical two-colour Pólya urn. In particular \(S_i(n)-1\) has the beta-binomial law with draw count \(n-i\) and parameters \(1,i-1\). Its mean and variance, including the zero-draw boundary, are
\[
\mathbb E S_i(n)=\frac ni,\qquad
\operatorname{Var}(S_i(n))=\frac{n(n-i)(i-1)}{i^2(i+1)}.
\]
For \(i=1\), \(S_1(n)=n\) deterministically, consistent with these formulas.

**Cross moment.** Fix \(1\le i<j\le n\). Let \(A\) indicate that vertex \(j\) is a descendant of \(i\) when it arrives. At time \(j-1\), \(\mathbb E S_i(j-1)=(j-1)/i\); thus \(\mathbb P(A=1)=1/i\). Once vertex \(j\) arrives, conditional on any history through time \(j\), the future expected growth of its subtree satisfies
\[
\mathbb E[S_j(t)\mid\mathcal F_j]=t/j\quad(t\ge j).
\]
Consequently \(\mathbb E[A S_j(t)]=t/(ij)\).

Write \(U_t=\mathbb E[S_i(t)S_j(t)]\) for \(t\ge j\). Let \(B_i,B_j\) indicate that vertex \(t+1\) joins the respective descendant subtrees. Conditional on the whole tree at time \(t\),
\[
\mathbb E B_i=S_i(t)/t,\qquad \mathbb E B_j=S_j(t)/t,
\qquad \mathbb E(B_iB_j)=A S_j(t)/t.
\]
The last equality holds since the subtrees are nested exactly when \(A=1\), otherwise disjoint. Expanding the product after one addition and averaging yields
\[
U_{t+1}=\left(1+\frac2t\right)U_t+\frac1{ij}.
\]
At time \(j\), \(S_j(j)=1\) and \(U_j=\mathbb E S_i(j)=j/i\). The unique solution is \(U_t=t^2/(ij)\) by direct induction, since \((1+2/t)t^2+1=(t+1)^2\). Therefore
\[
\mathbb E[S_i(n)S_j(n)]=\frac{n^2}{ij}=\mathbb E S_i(n)\,\mathbb E S_j(n),
\]
proving every off-diagonal covariance vanishes, including boundary labels.

**Path length and concentration.** Each non-root vertex \(i\) contributes one edge to the tree, and that edge lies on the root path of precisely \(S_i(n)\) vertices; summing edge contributions proves \(P_n=\sum_{i=2}^n S_i(n)\). Pairwise orthogonality gives its exact variance as a sum. A partial fraction identity,
\[
\frac{n(n-i)(i-1)}{i^2(i+1)}=
-\frac{n^2}{i^2}-\frac{2n(n+1)}{i+1}+\frac{n(2n+1)}{i},
\]
then telescopes to \(2n^2-nH_n-n^2H_n^{(2)}\). For each fixed \(i\), dividing its variance by \(n^2\) gives the limit \((i-1)/(i^2(i+1))\). Since the full variance divided by \(n^2\) tends to \(2-\pi^2/6>0\), finite sums and complements establish the displayed limiting residual fraction. Finally \((i-1)/(i^2(i+1))<i^{-2}\), and the tail of \(\sum_{i>k} i^{-2}\) is at most \(1/k\). The optimality of the linear predictor follows from diagonal covariance and zero-mean centering.

## Verification

The standalone file `verify.py` independently enumerates all \((n-1)!\) parent assignments for each \(1\le n\le9\), computes each descendant-size vector from the parent array, and compares all empirical means and covariance entries to the exact formulas using integer sums and rational arithmetic. It also checks the harmonic path-length variance and a finite dependent-joint-law example. It reports `VERIFY_OK 219 exact equality assertions; dependent example validated`. The infinite-family theorem is established by the conditional-moment proof above, not by the finite enumeration.

## Relationship to prior work

Janson's 2017 work (published in 2018) identifies uniform recursive trees with a split-tree model, with primary MSC 60C05, and analyzes subtree split laws and an ancestor-based global statistic. Acan, Frieze and Pittel (2019) provide the one-vertex beta limit for descendant sizes in uniform attachment trees. Lodewijks (2022) studies joint degree, depth, label and distance distributions in recursive trees. Benkner and Wagner (2021) study the number of distinct fringe-subtree shapes. The one-point urn distribution and known scalar path-length moments are **not** asserted to be new here. The added statement is the complete finite-sample diagonal covariance of descendant subtree sizes indexed by birth label, and the resulting sharp per-label variance attribution for path length. An earlier implicit deduction from generalized urn or split-tree formulas remains possible; priority is not independently established.

## Limitations

The theorem is specific to *uniform attachment with increasing birth labels*. It does not assert diagonal covariance for arbitrary preferential attachment weights, randomly relabeled trees, or counts of subtrees grouped by shape or degree. Zero covariance does not imply independence; indeed the subtree sizes at labels two and three are dependent for \(n=4\). The variance localization is about the optimal linear predictor of total path length, not an independent additive construction of its distribution. Historical novelty is subject to the stated residual literature risk; no external audit has been performed.

## References

- Svante Janson, *Random recursive trees and preferential attachment trees are random split trees*, arXiv:1706.05487 (first posted 2017-06-17), *Combinatorics, Probability and Computing* 28 (2019), 81–99. https://arxiv.org/abs/1706.05487
- Huseyin Acan, Alan Frieze, Boris Pittel, *Giant descendant trees, matchings and independent sets in the age-biased attachment graphs*, arXiv:1908.02407 (first posted 2019-08-07), *Journal of Applied Probability*. https://arxiv.org/abs/1908.02407
- Bas Lodewijks, *On joint properties of vertices with a given degree or label in the random recursive tree*, arXiv:2204.09032 (first posted 2022-04-19). https://arxiv.org/abs/2204.09032
- Louisa Seelbach Benkner and Stephan Wagner, *Distinct Fringe Subtrees in Random Trees*, arXiv:2105.04231 (first posted 2021-05-10). https://arxiv.org/abs/2105.04231
