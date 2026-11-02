# Exact leaf–Wiener covariance in uniform random recursive trees

## Finding
For every integer \(n\ge2\), the uniform random recursive tree on labels \(1,\ldots,n\) has leaf count \(L_n\) and Wiener index \(W_n\) satisfying
\[
\boxed{\operatorname{Cov}(L_n,W_n)=nH_n-\frac{n^2+5n-2}{4}},
\qquad H_n=\sum_{j=1}^n\frac1j.
\]
The covariance vanishes for \(n=2,3\) and is strictly negative for every \(n\ge4\). In particular it is \(-n^2/4+O(n\log n)\). The proof hinges on a simple exact identity for leaf distance centrality that also explains the negative sign.

## Assumptions and scope
A uniform random recursive tree is rooted at vertex \(1\). For each integer \(j=2,\ldots,n\), independently of previous choices, vertex \(j\) chooses a parent uniformly among \(1,\ldots,j-1\). There are \((n-1)!\) equiprobable parent lists. A leaf is a vertex of outdegree zero (the root is never a leaf when \(n\ge2\)). Graph distance \(d(u,v)\) counts edges on the unique path, and the Wiener index \(W\) sums distances over unordered vertex pairs, with no division by the number of pairs. The harmonic number \(H_n\) has the conventional normalization \(H_n=\sum_{j=1}^n 1/j\).

Write \(\mathcal L_m\) for the leaf set of the size-\(m\) tree, \(S_m(u)=\sum_{v=1}^m d(u,v)\) for its vertex distance sum, and \(A_m=\sum_{u\in\mathcal L_m}S_m(u)\) for its sum of leaf distance centralities. Define \(C_m=\operatorname{Cov}(L_m,W_m)\).

## Proof
**1. One-step identities.** Fix an arbitrary realized size-\(m\) tree with \(m\ge2\), and let \(P\) be the uniformly selected parent of the new vertex. Put \(J=\mathbf1_{\{P\in\mathcal L_m\}}\). Then
\[
L_{m+1}=L_m+1-J,\qquad W_{m+1}=W_m+m+S_m(P).
\]
Adding the new leaf also increases the distance sum of each old leaf \(u\) by \(d(u,P)+1\), while an old leaf selected as parent ceases to be a leaf. The exact identity is
\[
A_{m+1}=A_m+\sum_{u\in\mathcal L_m}(d(u,P)+1)+m+S_m(P)-J(S_m(P)+1).
\]
Since \(\sum_p S_m(p)=2W_m\), \(\sum_p\sum_{u\in\mathcal L_m}d(u,p)=A_m\), and \(\sum_{p\in\mathcal L_m}S_m(p)=A_m\), averaging uniformly over all \(m\) parent choices gives
\[
\begin{aligned}
\mathbb E[L_{m+1}\mid T_m]&=(1-1/m)L_m+1,\\
\mathbb E[W_{m+1}\mid T_m]&=(1+2/m)W_m+m,\\
\mathbb E[W_{m+1}-A_{m+1}\mid T_m]&=W_m-A_m-(1-1/m)L_m.
\end{aligned}
\]
The first equation and \(L_2=1\) imply \(\mathbb E L_m=m/2\) for all \(m\ge2\). With \(W_2=A_2=1\), the third equation therefore telescopes to the exact auxiliary mean identity
\[
\boxed{\mathbb E(W_m-A_m)=-\frac{(m-1)(m-2)}4}\qquad(m\ge2).
\]

**2. Covariance recurrence.** Conditional on \(T_m\), only \(P\) is random, so
\[
\operatorname{Cov}(L_{m+1},W_{m+1}\mid T_m)
=-\frac{A_m}m+\frac{2L_mW_m}{m^2}.
\]
The conditional-mean covariance is \((1-1/m)(1+2/m)C_m\). By the law of total covariance and \(\mathbb EL_m=m/2\),
\[
C_{m+1}=\frac{m+1}m C_m+\frac{\mathbb EW_m-\mathbb EA_m}m
=\frac{m+1}m C_m-\frac{(m-1)(m-2)}{4m},
\quad C_2=0.
\]
Iterating, for \(n\ge3\),
\[
\frac{C_n}n=-\frac14\sum_{k=3}^n\frac{(k-2)(k-3)}{k(k-1)}.
\]
The summand is \(1-6/k+2/(k-1)\), so the sum equals \(n+5-4H_n-2/n\). Therefore \(C_n=nH_n-(n^2+5n-2)/4\). Every summand is nonnegative, with strict positivity from \(k=4\) onward. This proves all equality and strict-sign cases, including the boundary values \(n=2,3\).

**3. Consequence for correlation.** The first-step leaf recursion also yields \(\operatorname{Var}(L_n)=n/12\) for \(n\ge3\): the law of total variance gives \(V_{m+1}=(1-2/m)V_m+1/4\) starting with \(V_2=0\). Neininger (2002, Theorem 1.2) established \(\operatorname{Var}(W_n)\sim (31-3\pi^2)n^4/18\). Combining that published marginal result with the new exact mixed covariance yields
\[
\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(L_n,W_n)
=-\frac{3\sqrt6}{2\sqrt{31-3\pi^2}}\approx-3.115115549.
\]

## Verification
`python verify_leaf_wiener.py` uses only the Python standard library. It enumerates all \(46,233\) recursive trees for \(2\le n\le9\), independently computes leaf counts, all-pairs shortest-path distances, and leaf distance sums, and checks the exact rational covariance, auxiliary identity, and Wiener mean at every size. It also checks \(5,912\) conditional one-vertex extensions across sizes \(2\le n\le7\), plus \(198\) exact rational moment-recursion steps up to size \(200\). All checks passed. Finite enumeration is corroboration; the proof above establishes the statement for all \(n\ge2\).

## Relationship to prior work
Neininger (2002) gave exact Wiener-index means and asymptotic variances and jointly analyzed Wiener index with **root path length**. Grübel and Michailow (arXiv:1406.7614v1, §3.3, Theorem 12) established strong limits for the Wiener index by subtree-size methods. These results do not state or imply the exact **leaf count–Wiener index** covariance: their joint statistic is path length, not leaf count. Published findings on recursive-tree root degree versus leaves and root attachment versus path length concern different pairs of observables. The present proof requires the additional leaf-centrality quantity \(A_m\), absent from those statements.

## Limitations
The theorem concerns ordinary uniform random recursive trees with independent uniform parent choices. It does not cover preferential-attachment, plane-oriented, or general weighted recursive tree models. No exact finite-size distribution of the pair \((L_n,W_n)\), conditional regression, or stochastic ordering is claimed. The claimed novelty is subject to the possibility of equivalent earlier mixed-moment formulas outside inspected sources. No independent audit has been performed.

## References
1. R. Neininger, *The Wiener Index of Random Trees*, Combinatorics, Probability and Computing **11** (2002), 587–597, DOI 10.1017/S0963548302005321; first publicly online 21 November 2002.
2. R. Grübel and I. Michailow, *Random Recursive Trees: A Boundary Theory Approach*, arXiv:1406.7614v1 (30 June 2014), especially §3.3, Theorem 12; primary 60C05.
3. H. Maehara, *The number of endpoints in a random recursive tree*, Ryukyu University Faculty of Education Bulletin (1984), 109–112; independent leaf-count background.
