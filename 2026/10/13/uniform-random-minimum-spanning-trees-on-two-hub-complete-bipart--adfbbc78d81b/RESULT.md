# Uniform random minimum spanning trees on two-hub complete bipartite graphs

## Finding

**Theorem (exact equality of random-tree laws).** Fix an integer \(n\geq 2\). Give the \(2n\) edges of the complete bipartite graph \(K_{2,n}\) independent weights drawn from any one atomless probability law on \(\mathbb R\). Let \(T_n\) denote their almost surely unique minimum-weight spanning tree. Then, for **every** spanning tree \(t\) of \(K_{2,n}\),
\[
\Pr(T_n=t)=\frac{1}{n\,2^{n-1}}.
\]
In particular, the entire law of \(T_n\) equals the uniform spanning-tree law, not merely its edge-inclusion marginals.

For each edge \(e\), let \(I_e=\mathbf 1_{\{e\in T_n\}}\). If \(e\ne f\) are distinct edges, then
\[
\Pr(I_e=1)=\frac{n+1}{2n},\qquad
\Pr(I_e=I_f=1)=
\begin{cases}
1/n,&\text{if }e,f\text{ meet the same degree-two-side vertex},\\
(n+2)/(4n),&\text{otherwise}.
\end{cases}
\]
Consequently,
\[
\operatorname{Cov}(I_e,I_f)=
\begin{cases}
-(n-1)^2/(4n^2),&\text{same degree-two-side vertex},\\
-1/(4n^2),&\text{different degree-two-side vertices},
\end{cases}
\]
with strict negative covariance in both cases for every \(n\ge2\).

## Assumptions and scope

The graph has two distinguished hubs \(a,b\) and \(n\) further vertices \(v_1,\ldots,v_n\). Its edges are exactly \(av_i\) and \(bv_i\), for \(1\le i\le n\). These further vertices have degree two **in the underlying graph**, not necessarily in the sampled tree. Denote the weights of \(av_i\) and \(bv_i\) by \(X_i\) and \(Y_i\), respectively. All \(2n\) weights are independent and identically distributed; no density, bounded support, positive support, or moment condition is imposed. Atomlessness rules out weight ties almost surely. The statement is about the spanning-tree **distribution**, not its random total weight.

## Proof

**1. Exhaustive description of all spanning trees.** Every spanning tree on \(n+2\) vertices has exactly \(n+1\) edges. Each of the \(n\) vertices \(v_i\) has degree at least one in such a tree, and degree at most two because it has only two available incident edges. Counting the \(n+1\) edges by their endpoint on the \(v_i\) side shows that exactly one of the \(v_i\), say \(v_j\), has both incident edges in the tree; every other \(v_i\) has exactly one. Conversely, any choice of \(j\in\{1,\ldots,n\}\), together with one of the two incident edges at each \(v_i\) for \(i\ne j\), produces a connected, acyclic graph with \(n+1\) edges, hence a spanning tree. There are therefore exactly \(n\,2^{n-1}\) spanning trees. Their indexing by \(j\) and \(n-1\) binary orientation choices is one-to-one.

**2. Exact deterministic minimization.** Put \(U_i=\min(X_i,Y_i)\) and \(Z_i=\max(X_i,Y_i)\). Among spanning trees whose unique double-edge vertex is \(v_j\), the smallest attainable total edge weight is
\[
\sum_{i\ne j}U_i+X_j+Y_j
=\sum_{i=1}^{n}U_i+Z_j.
\]
The equality is an identity for every real edge-weight assignment. For fixed \(j\), the minimizing edge at each other vertex is precisely the cheaper of its two incident edges. Thus the unique optimizing doubled vertex is
\[
J=\operatorname*{arg\,min}_{1\le i\le n} Z_i.
\]
The resulting tree uses both edges at \(v_J\) and, independently of that formula, the cheaper edge at every \(v_i\) with \(i\ne J\). Because all weights are atomless and independent, the minima within columns and the minimum among \(Z_i\) are unique almost surely.

**3. Probabilistic factorization.** For each \(i\), let \(B_i=0\) when \(X_i<Y_i\), and \(B_i=1\) when \(Y_i<X_i\). Exchangeability of the identically distributed ordered pair \((X_i,Y_i)\) implies, for every Borel set \(H\subseteq\mathbb R\),
\[
\Pr(B_i=0,\ Z_i\in H)=\Pr(B_i=1,\ Z_i\in H)
=\tfrac12\Pr(Z_i\in H).
\]
Hence \(B_i\) is a fair coin independent of \(Z_i\). Independence across columns implies that the entire vector \((B_1,\ldots,B_n)\) comprises independent fair coins and is independent of the entire vector \((Z_1,\ldots,Z_n)\). The random variables \(Z_i\) are also independent, identically distributed, and atomless, so their unique minimizer \(J\) is uniform on \(\{1,\ldots,n\}\) and independent of all coins.

Fix a spanning tree indexed by \(j\) and by specified binary choices \(b_i\) for every \(i\ne j\). The preceding characterization gives exactly
\[
\Pr(T_n=t)
=\Pr\bigl(J=j,\ B_i=b_i\ \text{for all }i\ne j\bigr)
=\frac1n\left(\frac12\right)^{n-1}.
\]
This is independent of \(t\), completing the proof of the uniform law.

**4. Exact two-edge correlations.** An edge at \(v_i\) is always present when \(J=i\), and otherwise is present exactly when the fair coin \(B_i\) chooses it. Thus
\[
\Pr(I_e=1)=\frac1n+\frac{n-1}{2n}=\frac{n+1}{2n}.
\]
If \(e,f\) belong to the same vertex \(v_i\), both are in the tree precisely when \(J=i\), of probability \(1/n\). For distinct vertices \(v_i\) and \(v_k\), condition on whether \(J\) is \(i\), \(k\), or neither. The joint edge-inclusion probability is
\[
\frac{2}{n}\cdot\frac12+\frac{n-2}{n}\cdot\frac14
=\frac{n+2}{4n}.
\]
Subtracting the square of the marginal probability in the two cases gives the stated covariances. For \(n\ge2\), both are strictly negative.

## Verification

The standalone Python 3 standard-library program `checker.py` exhausts **all** \((2n)!\) distinct weight orders for each \(n=2,3,4\); these are respectively \(24\), \(720\), and \(40320\) orders. It checks that the numbers of spanning trees are respectively \(4,12,32\), with equal order-counts \(6,60,1260\), and independently checks every one-edge and two-edge inclusion formula by exact rational arithmetic. There is no floating-point comparison.

For a boundary check that the conclusion is not an automatic property of complete bipartite graphs, the same program exhausts all \(9!\) edge orders of \(K_{3,3}\): its \(81\) spanning trees have three distinct multiplicities, \(4200\), \(4680\), and \(4800\). Thus the random minimum-spanning-tree law is **not** uniform there. This boundary check is finite and is not used to justify the infinite-family theorem.

Reproduce with `python3 checker.py` from a directory containing the standalone file. The general result for every integer \(n\ge2\) follows entirely from the deterministic structural argument and the independence/symmetry calculation above; the finite enumeration is a cross-check, not an extrapolation.

## Relationship to prior work

Tang and Zhang's 2026 study of pairwise negative correlation for random minimum spanning trees focuses on complete graphs and, in a remark, sufficiently large balanced complete bipartite graphs. Its stated negative-correlation results concern pairs of edge indicators, not equality of whole minimum-spanning-tree and uniform-spanning-tree measures. Gupta's 2026 study proves a universal multiplicative edge-correlation inequality for random minimum spanning trees and strict pairwise negative correlation for complete graphs \(K_n\). Its inspected manuscript does not discuss the law of \(K_{2,n}\). Neither conclusion implies the exact law proved here.

The standard uniform-spanning-tree model is equally likely to select every spanning tree, and its pairwise negative correlation is classical. Such negative correlation cannot by itself identify the law of a random minimum spanning tree; the new equality rests instead on the two-hub spanning-tree decomposition. Unlike a cactus graph, the graphs \(K_{2,n}\) for \(n\ge3\) contain cycles sharing edges, so independent deletion of one maximal edge per disjoint cycle cannot directly explain the result.

Targeted searches for equivalent formulations involving randomized Kruskal bases, subdivisions of parallel edges, generalized theta graphs, complete bipartite trees, and distributional equality did not identify a covering published theorem. This is an evidence-based comparison, **not** a proof of absolute priority.

## Limitations

The theorem requires identically distributed and independent atomless edge weights. It does not assert uniformity under heterogeneous laws, dependent weights, other graph families, or random optimization objectives other than minimum total spanning-tree weight. It gives no classification of all graphs where the random minimum spanning tree and the uniform spanning tree share a law. The exact nonuniform \(K_{3,3}\) case underscores that the two-hub geometry is essential. Source-indexing gaps or differently expressed earlier general theorems remain a genuine priority risk.

## References

1. P. Tang and Z. Zhang, *From second moments to pairwise negative correlation: applications to minimal and uniform spanning trees*, arXiv:2605.01444 (first publicly submitted 2026-05-02); see the complete manuscript, Theorem 1.1 and Remarks 1.2 and 2.4. https://arxiv.org/abs/2605.01444
2. A. Gupta, *Pairwise edge correlations in random minimum spanning trees: a universal bound and complete-graph negative correlation*, arXiv:2608.06816 (first public arXiv submission 2026-08-07; an earlier 2026-08-03 archived version is disclosed by the author's repository). The complete manuscript source used for comparison is `paper/main.tex` at https://github.com/agupta/random-mst-correlations ; primary MSC2020 60C05. https://arxiv.org/abs/2608.06816
3. N. Albin, J. Clemens, D. Hoare, P. Poggi-Corradini, B. Sit and S. Tymochko, *Fairest edge usage and minimum expected overlap for random spanning trees*, Discrete Mathematics 344 (2021), article 112282. Its uniform-spanning-tree definitions and effective-resistance results concern a different optimization of spanning-tree laws. https://doi.org/10.1016/j.disc.2020.112282
