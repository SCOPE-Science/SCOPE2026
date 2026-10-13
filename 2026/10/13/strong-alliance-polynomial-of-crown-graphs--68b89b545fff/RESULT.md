# Strong alliance polynomial of crown graphs
## Finding
For every integer \(n\ge4\), let \(\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\}\). For a nonempty set \(S\), put \(I=\{i:a_i\in S\}\), \(J=\{j:b_j\in S\}\), \(a=|I|\), \(b=|J|\), \(c=|I\cap J|\), and \(h=\lceil(n-1)/2\rceil\). Then \(S\) is a strong defensive alliance if and only if either \(c=0\) with \(a,b\ge h\), or \(c>0\) with \(a,b\ge h+1\). Consequently, if \(n=2m\ge4\) and \(Q_n(x)=\sum_{k=m+1}^{2m}\binom{2m}{k}x^k\), then \[a(\operatorname{Cr}_{2m};x)=Q_{2m}(x)^2+\binom{2m}{m}x^{2m}.\] If \(n=2m+1\ge5\) and \(Q_n(x)=\sum_{k=m+1}^{2m+1}\binom{2m+1}{k}x^k\), then \[a(\operatorname{Cr}_{2m+1};x)=Q_{2m+1}(x)^2+(m+1)\binom{2m+1}{m}x^{2m}+2\binom{2m+1}{m}x^{2m+1}.\] Hence the strong defensive alliance number is \(n\) for even \(n\) and \(n-1\) for odd \(n\ge5\); the numbers of minimum strong defensive alliances are respectively \(\binom{n}{n/2}\) and \(((n+1)/2)\binom{n}{(n-1)/2}\).

The formulas count every strong defensive alliance by cardinality, not merely minimum ones. They also expose a parity-sensitive effect of deleting a perfect matching from \(K_{n,n}\): for even \(n\), the minimum size stays \(n\) but only complementary half-side choices remain at minimum weight; for odd \(n\), the minimum size drops from \(n+1\) in \(K_{n,n}\) to \(n-1\) in the crown graph.

## Assumptions and scope
All graphs are finite and simple. The crown graph has bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with every cross edge present except \(a_i b_i\). A strong defensive alliance is a nonempty set \(S\) such that the induced subgraph \(G[S]\) is connected and, for every \(v\in S\),
\[
\delta_S(v)\ge \delta_{V\setminus S}(v).
\]
The strong alliance polynomial is \(a(G;x)=\sum_k a_k(G)x^k\), where \(a_k(G)\) is the number of strong defensive alliances of cardinality \(k\). The theorem is stated for \(n\ge4\). The boundary graph \(\operatorname{Cr}_3\cong C_6\) is excluded because some otherwise admissible four-vertex selections are disconnected; its polynomial is already covered by the known cycle formula.

## Proof
Every vertex of \(\operatorname{Cr}_n\) has degree \(n-1\). Thus the strong defensive inequality is equivalent to
\[
\delta_S(v)\ge h:=\left\lceil\frac{n-1}2\right\rceil.
\]
Let \(I,J,a,b,c\) be as in the finding. If \(a_i\in S\), then exactly the selected vertices of \(B\) are potential neighbors, except that \(b_i\) is not adjacent to \(a_i\). Hence
\[
\delta_S(a_i)=b-\mathbf 1_{i\in J}.
\]
Similarly, for \(b_j\in S\),
\[
\delta_S(b_j)=a-\mathbf 1_{j\in I}.
\]
If \(c=0\), no selected vertex loses its matched cross-neighbor inside \(S\), so the inequalities are exactly \(a,b\ge h\). If \(c>0\), at least one selected vertex on each side is paired with its deleted-matching mate inside \(S\), forcing and, conversely, being guaranteed by \(a,b\ge h+1\).

It remains to check connectivity. If \(c=0\), the induced graph is \(K_{a,b}\); in every feasible case with \(n\ge4\), \(a,b\ge2\), so it is connected. If \(c>0\), the induced graph is \(K_{a,b}\) with \(c\) independent matching edges deleted. Feasibility gives \(a,b\ge3\), so every pair of vertices is linked by a path of length at most three. Thus the displayed numerical criterion is necessary and sufficient.

For \(n=2m\), \(h=m\). Every choice with \(a,b\ge m+1\) is feasible, contributing \(Q_{2m}(x)^2\). Any remaining feasible set must have \(c=0\) and at least one side of size \(m\). Since disjoint index sets satisfy \(a+b\le2m\), this forces \(a=b=m\) and \(J=[2m]\setminus I\). There are \(\binom{2m}{m}\) such sets, producing the even formula.

For \(n=2m+1\), \(h=m\). Again all choices with \(a,b\ge m+1\) contribute \(Q_{2m+1}(x)^2\). The remaining feasible sets have \(c=0\) and at least one side of size \(m\). Disjointness leaves only the size pairs \((m,m)\), \((m,m+1)\), and \((m+1,m)\). The first type has \(\binom{2m+1}{m}(m+1)\) choices; each oriented second type has \(\binom{2m+1}{m}\) choices. This gives the odd formula. Reading the least exponent and its coefficient yields the minimum-size and minimum-count statements.

## Verification
The standalone script `artifacts/verify_strong_alliance_crown.py` reconstructs each crown graph, tests the definition directly (including connectivity), compares it with the \((a,b,c)\) classification, and compares the resulting cardinality counts with the closed parity formulas. Exhaustive replay for \(4\le n\le8\) checks every vertex subset. It separately confirms that \(n=3\) is a genuine connectivity boundary and agrees with the known cycle polynomial. The finite replay is corroborative only; the unrestricted theorem follows from the proof above. The executed package replay reported:

`VERIFY_OK n_range=4..8 subset_checks=87296 classification_checks=87296 coefficient_checks=65 minimum_checks=5 max_order=16 boundary_n3=C6`

## Relationship to prior work
Carballosa, Hernández-Gómez, Rosario, and Torres-Núñez introduced the strong alliance polynomial and computed it for several standard families, including complete bipartite graphs. Their complete-bipartite theorem gives
\[
a(K_{n,n};x)=\left(\sum_{k=\lceil n/2\rceil}^n\binom nk x^k\right)^2.
\]
The crown graph is obtained from \(K_{n,n}\) by deleting a perfect matching, and the deleted pairs make feasibility depend on the overlap \(I\cap J\); this index-sensitive condition is absent from the complete-bipartite formula. Their full text contains no crown-graph or perfect-matching specialization.

The later alliance-polynomial work on regular graphs concerns the distribution of exact defensive indices and supplies general regular-graph structure, but it does not determine this cardinality enumerator. Ibrahim's defensive alliance polynomial is a bivariate refinement from which the strong alliance polynomial can be extracted, so it is a plausible dominating source; its inspected full text lists many explicit graph families, including complete bipartite and book graphs, but not crown graphs, and full-text searches for “crown” and “perfect matching” returned no occurrences. These comparisons do not make failed searches a proof of novelty; they delimit the strongest located coverage and leave an explicit residual literature risk.

## Limitations
The theorem is for \(n\ge4\). It does not give the full bivariate defensive alliance polynomial or the exact-defensive-index alliance polynomial. The exhaustive checker reaches order sixteen and is not an infinite proof. Literature comparison was targeted across crown, complete-bipartite-minus-matching, strong defensive alliance, cohesive-set, and polynomial formulations; differently indexed older alliance literature remains a residual originality risk.

## References
1. W. Carballosa, J. C. Hernández-Gómez, O. Rosario, and Y. Torres-Núñez, “Computing the strong alliance polynomial of a graph,” arXiv:1507.08654v1, first posted 30 July 2015; later published in *Investigación Operacional* 37(2) (2016), 115–123.
2. W. Carballosa, J. M. Rodríguez, J. M. Sigarreta, and Y. Torres-Núñez, “Alliance polynomial of regular graphs,” arXiv:1506.06041, first posted 19 June 2015; later published in *Discrete Applied Mathematics* 225 (2017), 22–32.
3. H. Ibrahim, “Defensive alliance polynomial,” arXiv:1811.10089v1, first posted 25 November 2018.
