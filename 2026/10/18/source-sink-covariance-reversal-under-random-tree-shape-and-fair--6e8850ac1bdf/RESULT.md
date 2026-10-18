# Source–sink covariance reversal under random tree shape and fair orientation

## Finding

Let \(T_n\) be uniform among the \(n^{n-2}\) labeled trees on \(\{1,\ldots,n\}\), where \(n\ge2\). Conditional on \(T_n\), orient its \(n-1\) edges independently, each direction having probability \(1/2\). Count vertices with indegree zero by \(S_n\) and vertices with outdegree zero by \(K_n\). For
\[
a_n=\left(1-\frac1{2n}\right)^{n-2},\qquad
b_n=\left(1-\frac1n\right)^{n-2},
\]
the complete first and second moments satisfy
\[
\begin{aligned}
\mathbb E S_n=\mathbb E K_n&=\frac n2a_n,\\
\mathbb E[S_nK_n]&=\frac{n^2}{4}b_n,\\
\mathbb E[S_n^2]=\mathbb E[K_n^2]&=\frac n2a_n+\frac{n(n-2)}4b_n.
\end{aligned}
\]
In particular,
\[
\boxed{\operatorname{Cov}(S_n,K_n)=\frac{n^2}{4}\bigl(b_n-a_n^2\bigr)}.
\]
It is zero when \(n=2\) and **strictly negative for every integer \(n\ge3\)**. Moreover,
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(S_n,K_n)}n=-\frac1{16e},
\qquad
\lim_{n\to\infty}\operatorname{Corr}(S_n,K_n)=-\frac1{8\sqrt e-9}.
\]
The latter is a nonzero negative limit. By contrast, if the underlying tree is held fixed to be the path \(P_n\), then for all \(n\ge3\)
\[
\boxed{\operatorname{Cov}(S_n,K_n\mid T_n=P_n)=\frac{n-4}{16}},
\]
which is positive at all \(n\ge5\). Thus a positive fixed-path covariance can coexist with strictly negative covariance under random Cayley tree shape.

## Assumptions and scope

The probability model uses first a **uniform labeled tree**, and then **independent unbiased edge orientations**. Source and sink indicators refer to the final orientations, not to comparisons of shared random vertex labels. A vertex of positive degree cannot simultaneously be a source and a sink. All exact identities quantify over each integer \(n\ge2\); the fixed-path identity assumes \(n\ge3\). No distributional limit theorem is asserted, only moment and correlation limits.

## Proof

**1. Conditional local covariance.** Fix a labeled tree \(T\), write \(d_v\) for the degree of vertex \(v\), and put \(x_v=2^{-d_v}\). Independence of oriented edges gives \(\mathbb P(v\text{ source}\mid T)=\mathbb P(v\text{ sink}\mid T)=x_v\). If \(u\ne v\) are nonadjacent, their source/sink events involve disjoint edges and have joint probability \(x_ux_v\). If \(u,v\) are adjacent, the common edge's required orientation agrees for the event that \(u\) is a source and \(v\) is a sink, so their joint probability is \(2x_ux_v\). Two distinct source indicators have joint probability zero if adjacent and \(x_ux_v\) otherwise. Therefore, with edge sums over unordered edges,
\[
\begin{aligned}
\mathbb E[S_nK_n\mid T]
 &=\sum_{u\ne v}x_ux_v+2\sum_{\{u,v\}\in E(T)}x_ux_v,\\
\mathbb E[S_n(S_n-1)\mid T]
 &=\sum_{u\ne v}x_ux_v-2\sum_{\{u,v\}\in E(T)}x_ux_v,\\
\operatorname{Cov}(S_n,K_n\mid T)
 &=-\sum_vx_v^2+2\sum_{\{u,v\}\in E(T)}x_ux_v.
\end{aligned}
\]
All formulas are also valid for the two-vertex tree.

**2. Prüfer weights and edge incidence.** Under the uniform labeled-tree measure, the Prüfer word has length \(n-2\) and iid uniform letters. The degree is one plus the number of occurrences of that letter. Hence, for distinct \(u,v\),
\[
\mathbb E_T x_v=\frac12 a_n,
\qquad
\mathbb E_T[x_ux_v]=\frac14 b_n.
\]
For completeness, the weighted Cayley identity reads
\[
\sum_T\prod_{v=1}^n z_v^{d_v(T)-1}=\left(\sum_{v=1}^nz_v\right)^{n-2}
\]
for positive \(z_v\), directly from the Prüfer bijection. Under the resulting tilted tree measure, contracting the marked edge \(\{u,v\}\) and applying the same weighted identity gives its inclusion probability as
\[
\mathbb P_z(\{u,v\}\in E(T))=\frac{z_u+z_v}{\sum_j z_j}.
\]
Use \(z_u=z_v=1/2\) and all other weights one. The normalizing sum is \(n-1\), so
\[
\mathbb E_T[\mathbf1_{\{u,v\}\in E(T)}x_ux_v]
=\frac{b_n}{4(n-1)}.
\]
This equality holds also for \(n=2\), since the edge is then certain.

**3. Exact moments.** Take expectations of the identities in Step 1, use exchangeability of vertex pairs, and note that there are \(n(n-1)\) ordered pairs:
\[
\begin{aligned}
\mathbb E[S_nK_n]
 &=n(n-1)\frac{b_n}{4}
   +n(n-1)\frac{b_n}{4(n-1)}=\frac{n^2b_n}{4},\\
\mathbb E[S_n(S_n-1)]
 &=n(n-1)\frac{b_n}{4}
   -n(n-1)\frac{b_n}{4(n-1)}=\frac{n(n-2)b_n}{4}.
\end{aligned}
\]
Combined with the first moment, this proves all displayed second moments, using orientation reversal to exchange \(S_n\) and \(K_n\). For \(n>2\),
\[
\left(1-\frac1{2n}\right)^2
=1-\frac1n+\frac1{4n^2}>1-\frac1n,
\]
and raising these positive bases to \(n-2\) proves \(a_n^2>b_n\) and strict negativity. At \(n=2\), \(S_n=K_n=1\) deterministically.

**4. Shape reversal.** On \(P_n\) the two endpoints have \(x_v=1/2\), and the \(n-2\) internal vertices have \(x_v=1/4\). For \(n\ge3\), the last identity in Step 1 becomes
\[
-\left(\frac12+\frac{n-2}{16}\right)
+2\left(\frac14+\frac{n-3}{16}\right)
=\frac{n-4}{16}.
\]
The positive sign from \(n=5\) onward is therefore exact, not numerical.

**5. Correlation limit.** Elementary logarithmic expansions yield
\[
a_n=e^{-1/2}\left(1+\frac7{8n}+O(n^{-2})\right),
\qquad
b_n=e^{-1}\left(1+\frac3{2n}+O(n^{-2})\right).
\]
Thus
\[
\begin{aligned}
\operatorname{Cov}(S_n,K_n)/n&\longrightarrow-1/(16e),\\
\operatorname{Var}(S_n)/n&\longrightarrow(8\sqrt e-9)/(16e)>0.
\end{aligned}
\]
The same variance holds for \(K_n\); dividing proves the correlation limit. Positivity of the limiting denominator follows from \(\sqrt e>9/8\). For each finite \(n\ge3\), variance is positive because the oriented-path subevent produces different source counts with positive probability.

## Verification

The standalone Python 3 script `verify_oriented_trees.py` uses only the standard library. Run `python verify_oriented_trees.py` from the directory containing it. It enumerates every labeled Cayley tree and every fair orientation through \(n=7\), then compares exact rational moments with the formulas. This includes \(1{,}075{,}648\) oriented labeled trees at \(n=7\). It independently checks path covariances for \(2\le n\le11\), the weighted edge-inclusion formula for twelve weighted examples, and high-precision numerical convergence of the correlation. The program reported **70 passing checks**. These finite computations only cross-check the analytic proof, which establishes all unbounded statements.

## Relationship to prior work

Classical Prüfer enumeration supplies the degree and weighted-Cayley identities. Alm and Linusson's *A counter-intuitive correlation in a random tournament* (arXiv:0906.0240, first released 2009-06-01) considers correlations of specified **directed reachability events** in random orientations, including fixed trees; a reachability event for a pair of marked vertices is not the global source–sink count. Okoth and Wagner's *Locally Oriented Noncrossing Trees* (2015, DOI 10.37236/5164) enumerates sources and sinks of **noncrossing trees with label-induced deterministic orientations**, which differ in both tree law and orientation law. Narayanan's *Connections in randomly oriented graphs* (arXiv:1609.01003, first released 2016-09-05) proves correlation inequalities for **same-source path connectivity** on a fixed graph, not the present two global count statistics averaged over random tree shape.

A separate local-extremum model attaches iid continuous marks to vertices and directs edges by their shared endpoints' mark order; its orientations around a vertex are dependent, unlike the independent edge orientations here. Qualitative similarities in fixed-path covariance behavior do not imply the present exact Cayley-tree covariance, strict finite-size sign, or correlation constant.

## Limitations

No claim of independence between the source and sink counts is made; their covariance is in fact negative for \(n\ge3\). The random-tree model does not imply a negative conditional covariance for every tree shape: long paths give counterexamples. The proof concerns only independent, **unbiased** edge orientations and uniform labeled trees, not biased or edge-dependent orientations or other tree distributions. Exhaustive computations through seven vertices are supplementary evidence, not a proof for all sizes. The bibliographic comparison supports an originality assessment but cannot certify historical priority or rule out an earlier implicit formulation in a general orientation generating function.

## References

1. S. E. Alm and S. Linusson, *A counter-intuitive correlation in a random tournament*, arXiv:0906.0240 (first version 2009-06-01). https://arxiv.org/abs/0906.0240
2. I. O. Okoth and S. Wagner, *Locally Oriented Noncrossing Trees*, Electronic Journal of Combinatorics 22 (2015), P3.36; DOI:10.37236/5164. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v22i3p36
3. B. Narayanan, *Connections in randomly oriented graphs*, arXiv:1609.01003 (first version 2016-09-05). https://arxiv.org/abs/1609.01003
