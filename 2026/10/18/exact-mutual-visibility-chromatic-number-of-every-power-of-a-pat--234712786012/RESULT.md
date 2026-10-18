# Exact mutual-visibility chromatic number of every power of a path

## Finding

For every pair of integers \(n,k\geq1\), let \(P_n^k\) be the simple graph on \(\{0,1,\ldots,n-1\}\), with two distinct vertices adjacent exactly when their integer difference in absolute value is at most \(k\). Its mutual-visibility chromatic number is

\[
\chi_{\mu}(P_n^k)=
\begin{cases}
1,&1\le n\le k+1,\\
\max\{2,\lceil n/(2k)\rceil\},& n\ge k+2.
\end{cases}
\]

Equivalently, it is \(1\) through \(n=k+1\), it is \(2\) for \(k+2\le n\le4k\), and it is \(\lceil n/(2k)\rceil\) for \(n\ge4k+1\). A constructive coloring attains each value. In particular, for any fixed \(k\), this visibility parameter grows without bound even though the ordinary chromatic number of \(P_n^k\) is \(k+1\) once \(n\ge k+1\).

## Assumptions and scope

A vertex set \(S\) in a graph is *mutually visible* when, for any two distinct vertices of \(S\), some shortest path between them has all internal vertices outside \(S\). A mutual-visibility coloring is a partition of the vertex set into such sets; \(\chi_\mu\) is its minimum number of nonempty classes. The theorem concerns undirected simple powers of finite paths with \(n,k\) positive integers. All distances in \(P_n^k\) obey

\[
d(u,v)=\left\lceil\frac{|u-v|}{k}\right\rceil.
\]

Indeed, each move changes the label by at most \(k\), and moving monotonically by steps of size at most \(k\) attains this lower bound.

## Proof

**Lower bound.** Partition the vertices into their \(k\) congruence classes modulo \(k\). For any three vertices \(a<b<c\) in the same class, write \(c-a=sk\). A shortest path from \(a\) to \(c\) has exactly \(s\) edges, each increasing the label by exactly \(k\): otherwise it could not achieve a total increase of \(sk\). In particular, this unique geodesic passes through \(b\). Therefore a mutually visible set contains at most two vertices from each congruence class and has size at most \(2k\). Every coloring consequently uses at least \(\lceil n/(2k)\rceil\) colors. If \(n>k+1\), the graph is noncomplete, and no single color can contain all vertices: two nonadjacent vertices require an internal vertex on any shortest path. Hence at least two colors are necessary. If \(n\le k+1\), the graph is complete and one color suffices.

**Short noncomplete powers.** If \(k+2\le n\le2k\), the first \(k\) labels form a clique and the remaining \(n-k\) labels form a second clique (each length is at most \(k\)). These two mutually visible classes attain the lower bound.

**Two-block lemma.** Fix integers \(k\ge1\), \(t\ge2\) and a multiple \(a\) of \(k\). In \(P_{2kt}^k\), consider two length-\(k\) blocks

\[
S=[a,a+k-1]\ \cup\ [a+tk,a+tk+k-1]
\]

with both blocks contained in the vertex range. Then \(S\) is mutually visible. Pairs within a block are adjacent. For a cross-block pair let \(u=a+\alpha\), \(v=a+tk+\beta\), where \(0\le\alpha,\beta\le k-1\). The distance is

\[
d(u,v)=t+\mathbf1_{\{\beta>\alpha\}}.
\]

The gap between the blocks is the interval from \(a+k\) to \(a+tk-1\). If \(t\ge3\), put \(p=u+k\) and \(q=v-k\); both are in the gap and \(p\le q\). Join \(u\) to \(p\), travel monotonically from \(p\) to \(q\) in \(\lceil(q-p)/k\rceil\) steps, then join \(q\) to \(v\). Its length is

\[
2+\left\lceil\frac{(t-2)k+\beta-\alpha}{k}\right\rceil
=t+\mathbf1_{\{\beta>\alpha\}},
\]

so it is a geodesic whose internal vertices avoid \(S\). If \(t=2\) and \(\beta\ge\alpha\), the same construction works, allowing \(p=q\) when \(\alpha=\beta\). If \(t=2\) and \(\beta<\alpha\), take the two-edge path through \(w=a+k+\beta\); both increments \(w-u=k+\beta-\alpha\) and \(v-w=k\) lie between \(1\) and \(k\), and the internal vertex is in the gap. This path is shortest because \(k<v-u<2k\). The lemma follows in all cases.

**Coloring long powers.** If \(n>2k\), put \(t=\lceil n/(2k)\rceil\ge2\) and \(N=2kt\). For \(i=0,\ldots,t-1\), define

\[
S_i=[ik,(i+1)k-1]\ \cup\ [(t+i)k,(t+i+1)k-1].
\]

These \(t\) mutually visible classes partition \(P_N^k\) by the two-block lemma. Intersect each class with the prefix \(\{0,\ldots,n-1\}\). Each geodesic used in the lemma is monotonically increasing and hence stays between its endpoints, so it remains a shortest path in \(P_n^k\). The restricted classes are therefore mutually visible, and the nonempty ones partition the desired vertex set using at most \(t\) colors. The lower bound forces exactly \(t\) colors. Combined with the previous cases this proves the formula. \(\square\)

## Verification

The standalone script `verify.py` constructs graph adjacencies and checks geodesic preservation by separate breadth-first searches in the full graph and the graph with same-color internal vertices forbidden. It checks the explicit construction for all \(1\le k\le8\) and \(1\le n\le65\). A separate exhaustive exact-cover calculation over BFS-verified mutually visible subsets confirms the optimum for all \(1\le k\le4\) and \(1\le n\le10\). The recorded output is included in `verification_output.txt`; finite checks support but do not replace the proof.

## Relationship to prior work

Klavžar, Kuziak, Valenzuela Tripodoro and Yero introduced mutual-visibility coloring, its basic lower bound, and exact values on trees, including paths [1]. Their path result recovers the \(k=1\) instance, which is not claimed as new. The new statement provides an all-\(k\) exact classification for powers of paths, which cease to be trees for \(k\ge2\). The same paper gives broad bounds and a description of some two-color families but no path-power formula. Brešar, Peterin, Samadi and Yero [2] consider a *different* independent variant and strong/Cartesian products, including products of two paths, and do not supply the present path-power statement. Babu, Di Stefano and Lakshmanan [3] treat complexity and glued trees rather than path powers. The geometric graph-power object is not to be confused with Cartesian or strong *products* of paths.

## Limitations

No statement is made for powers of cycles, arbitrary unit-interval graphs, or independent/dual/outer/total variants of visibility coloring. The comparison with accessible literature does not establish absolute publication priority; an independently unindexed equivalent characterization remains possible. No independent external validation of this proof has been performed.

## References

[1] S. Klavžar, D. Kuziak, J. C. Valenzuela Tripodoro, I. G. Yero, *Coloring the vertices of a graph with mutual-visibility property*, arXiv:2408.03132v1 (2024), https://arxiv.org/html/2408.03132v1 .

[2] B. Brešar, I. Peterin, B. Samadi, I. G. Yero, *Independent mutual-visibility coloring and related concepts*, arXiv:2505.04144v1 (2025), https://arxiv.org/pdf/2505.04144 .

[3] S. Babu, G. Di Stefano, A. Lakshmanan S., *Mutual-visibility coloring of graphs*, arXiv:2512.12251v1 (2025), https://arxiv.org/html/2512.12251v1 .
