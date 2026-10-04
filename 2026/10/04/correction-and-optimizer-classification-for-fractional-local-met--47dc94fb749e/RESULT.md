# Correction and optimizer classification for fractional local metric dimension of complete multipartite graphs
## Finding
Let \(G=K_{a_1,\ldots,a_k}\) be a connected complete multipartite graph with \(k\ge2\). Its fractional local metric dimension is \[\operatorname{ldim}_f(G)=\begin{cases}1,&k=2,\\k/2,&k\ge3.\end{cases}\] For a local resolving function \(f:V(G)\to[0,1]\), let \(s_i=\sum_{v\in V_i}f(v)\). Then feasibility is equivalent to \(s_i+s_j\ge1\) for every pair of distinct parts. If \(k\ge3\), optimality is equivalent to \(s_i=1/2\) for every part; if \(k=2\), it is equivalent to \(s_1+s_2=1\). This corrects the published claim \(\operatorname{ldim}_f(K_{a_1,\ldots,a_k})=k-1\) for \(k>2\).

## Assumptions and scope
All graphs are finite, simple, and connected. Let \(G=K_{a_1,\ldots,a_k}\) have partite sets \(V_1,\ldots,V_k\), where \(a_i=|V_i|\ge1\) and \(k\ge2\). For an edge \(xy\), its local resolving neighborhood is
\[
L(xy)=\{z\in V(G):d(z,x)\ne d(z,y)\}.
\]
A local resolving function is a map \(f:V(G)\to[0,1]\) satisfying \(\sum_{z\in L(xy)}f(z)\ge1\) for every edge \(xy\). The minimum possible weight \(\sum_v f(v)\) is \(\operatorname{ldim}_f(G)\).

## Proof
Take an edge \(xy\) with \(x\in V_i\) and \(y\in V_j\), \(i\ne j\). Every vertex of \(V_i\cup V_j\) has different distances to \(x\) and \(y\), while every vertex in a third part has distance \(1\) from both. Hence
\[
L(xy)=V_i\cup V_j.
\]
With \(s_i=\sum_{v\in V_i}f(v)\), the vertex-level linear program is exactly
\[
s_i+s_j\ge1\qquad(i\ne j),
\]
with objective \(\sum_i s_i\).

For \(k=2\) there is one constraint, so the optimum is \(1\), attained exactly when \(s_1+s_2=1\). For \(k\ge3\), summing all \(\binom{k}{2}\) constraints gives
\[
(k-1)\sum_i s_i\ge\binom{k}{2},
\]
so \(\sum_i s_i\ge k/2\). Equality is attained by assigning total weight \(1/2\) to each part. If the total is \(k/2\), then every pair inequality must be tight; with at least three parts, the equations \(s_i+s_j=1\) force \(s_i=1/2\) for all \(i\). Thus the optimum face is completely characterized.

The published value \(k-1\) is therefore false for every \(k>2\). The smallest witness is \(K_3\): assigning weight \(1/2\) to each vertex is feasible with total weight \(3/2\), not \(2\). The same published article also contains a true-twin theorem that yields \(\operatorname{ldim}_f(K_3)=3/2\), so its complete-partite lemma is internally inconsistent.

## Verification
The included checker rebuilds every connected complete multipartite isomorphism type of orders \(2\) through \(10\), computes all-pairs distances, constructs every local resolving neighborhood directly from the definition, and solves the original vertex-variable linear program. Every optimum matches \(1\) for two parts and \(k/2\) for at least three parts. The explicit \(K_3\) witness is checked separately.

## Relationship to prior work
The foundational paper first appeared publicly on 5 October 2018 and was published in Contributions to Discrete Mathematics in 2024. Its current published Lemma 2.11 states that a complete \(k\)-partite graph with \(k>2\) has fractional local metric dimension \(k-1\). On the same pages it correctly records \(L(xy)=V_i\cup V_j\), which reduces the problem to the pair-cover linear program solved above.

The same published article proves a general theorem giving fractional local metric dimension \(|V(G)|/2\) when every vertex has a true twin; applied to \(K_3\), that theorem gives \(3/2\), contradicting the complete-partite lemma. Exact-phrase, lemma-number, correction/erratum, and semantic searches located no later repair or stronger complete-multipartite result giving the corrected value and optimizer face.

## Limitations
This correction concerns fractional local metric dimension, not ordinary local metric dimension or ordinary fractional metric dimension. Within each part, optimal vertex weights are not unique; only their totals are fixed. Finite LP checks through order ten are corroborative only. Search coverage cannot exclude an unindexed or differently phrased correction.

## References
1. H. Benish, M. Murtaza, I. Javaid, “The Fractional Local Metric Dimension of Graphs,” arXiv:1810.02882v1, 5 October 2018.
2. I. Javaid, H. Benish, M. Murtaza, “The Fractional Local Metric Dimension of Graphs,” Contributions to Discrete Mathematics 19(3) (2024), 163–177, DOI 10.55016/ojs/cdm.v19i3.62807.
3. S. Aisyah, M. I. Utoyo, L. Susilowati, “Fractional Local Metric Dimension of Comb Product Graphs,” Baghdad Science Journal 17(4) (2020), DOI 10.21123/bsj.2020.17.4.1288.
