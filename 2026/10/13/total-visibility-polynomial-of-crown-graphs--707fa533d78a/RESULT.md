# Total visibility polynomial of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M,\qquad n\ge3,
\]
with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where \(M=\{a_i b_i:1\le i\le n\}\) is the deleted perfect matching.

A set \(X\subseteq V(\operatorname{Cr}_n)\) is total mutual-visible if and only if
\[
|A\setminus X|\ge3,\qquad |B\setminus X|\ge3.
\tag{1}
\]

Therefore
\[
\mathcal V_{\mathrm t}(\operatorname{Cr}_n;z)
=
\left(\sum_{k=0}^{n-3}\binom nk z^k\right)^2.
\tag{2}
\]
Hence
\[
\mu_{\mathrm t}(\operatorname{Cr}_n)=2n-6.
\]
Every inclusion-maximal total mutual-visibility set contains exactly \(n-3\) vertices from each part, and there are
\[
\binom n3^2
\]
such sets.

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. Vertices \(u,v\) are \(X\)-visible when some shortest \(u,v\)-path has no internal vertex in \(X\). A set \(X\) is total mutual-visible when every pair of graph vertices is \(X\)-visible. The polynomial counts all such sets by size, including the empty set.

## Proof
Put \(Y_A=A\setminus X\) and \(Y_B=B\setminus X\).

If \(i\ne j\), then \(a_i\) and \(a_j\) are at distance \(2\), and their common neighbors are exactly
\[
B\setminus\{b_i,b_j\}.
\]
Thus every pair of \(A\)-vertices is \(X\)-visible exactly when
\[
Y_B\setminus\{b_i,b_j\}\ne\varnothing
\]
for all distinct \(i,j\). This is equivalent to \(|Y_B|\ge3\). By symmetry, every pair of \(B\)-vertices is \(X\)-visible exactly when \(|Y_A|\ge3\).

Unmatched cross-part pairs are adjacent, so they are always \(X\)-visible. The remaining pairs are \(a_i,b_i\), whose distance is \(3\). Their shortest paths are
\[
a_i-b_j-a_k-b_i
\]
with \(j\ne i\), \(k\ne i\), and \(j\ne k\). If \(|Y_A|,|Y_B|\ge3\), choose \(b_j\in Y_B\setminus\{b_i\}\); then choose \(a_k\in Y_A\) with \(k\ne i,j\). The resulting geodesic has both internal vertices outside \(X\). Hence (1) is sufficient, and the same-side argument already showed it is necessary.

The choices on the two bipartition classes are independent, giving (2). Maximality forces exactly three omitted vertices in each part, proving the remaining statements.

## Verification
The included checker constructs every \(\operatorname{Cr}_n\) for \(3\le n\le8\), enumerates all shortest paths for every vertex pair, and directly tests every vertex subset. It independently compares the direct result with (1), every polynomial coefficient in (2), the degree, and the number and size of maximal sets.

## Relationship to prior work
Total mutual-visibility was introduced in 2022. The introducing paper develops the notion for strong products and, in the inspected searchable full text, contains no crown or bipartite treatment.

Visibility polynomials were introduced later. The foundational polynomial paper computes
\[
\mathcal V_{\mathrm t}(K_{n,n};z)=\bigl((1+z)^n-z^n\bigr)^2,
\]
so for complete bipartite graphs one omitted vertex in each part suffices. In a crown graph, deleting the perfect matching changes same-side common-neighbor sets and creates matched distance-\(3\) pairs; the exact threshold becomes three omitted vertices in each part.

Targeted searches under crown graph, \(K_{n,n}\) minus a perfect matching, and complete bipartite graph minus a perfect matching did not locate the crown formula.

## Limitations
The theorem concerns total mutual-visibility only, not ordinary, outer, dual, connected, or distance-limited mutual visibility. At \(n=3\), the empty set is the only feasible set in the polynomial convention, so the total mutual-visibility number is \(0\). The exhaustive computation is corroborative only; the arbitrary-\(n\) result follows from the proof. A differently phrased or non-indexed crown treatment may exist.

## References
1. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, “Mutual-visibility in strong products of graphs via total mutual-visibility,” arXiv:2210.07835v1, 14 October 2022.
2. C. Bujtás, S. Klavžar, J. Tian, “Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets,” arXiv:2412.03066v1, 4 December 2024; Aequationes Mathematicae 99 (2025), 1883–1901, DOI 10.1007/s00010-025-01197-y.
