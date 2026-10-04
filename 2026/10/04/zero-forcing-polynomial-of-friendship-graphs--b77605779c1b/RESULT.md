# Zero forcing polynomial of friendship graphs
## Finding
Let \(F_k\), with \(k\ge1\), be the friendship graph formed from \(k\) triangles sharing one common center. Its zero forcing polynomial is \[\mathcal Z(F_k;x)=x^k\big((1+x)(2+x)^k-2^k\big).\] More precisely, a vertex set \(S\subseteq V(F_k)\) is zero forcing exactly when either the center belongs to \(S\) and \(S\) meets every outer pair, or the center does not belong to \(S\), \(S\) meets every outer pair, and at least one outer pair is contained in \(S\). Consequently \(Z(F_k)=k+1\), the number of minimum zero forcing sets is \(2^{k-1}(k+2)\), and the total number of zero forcing sets is \(2\cdot3^k-2^k\).

## Assumptions and scope
All graphs are finite, simple, and undirected. For \(k\ge1\), let \(F_k\) be the friendship graph with common center \(c\) and outer pairs
\[
P_i=\{a_i,b_i\},\qquad 1\le i\le k,
\]
where \(c a_i b_i c\) is the \(i\)-th triangle.

A set of initially blue vertices is zero forcing if repeated use of the color-change rule—any blue vertex with exactly one white neighbor forces that neighbor blue—eventually colors every vertex blue. Write \(z(G;j)\) for the number of zero forcing sets of cardinality \(j\), and
\[
\mathcal Z(G;x)=\sum_j z(G;j)x^j.
\]

## Proof
Suppose first that \(c\in S\). If some outer pair \(P_i\) is disjoint from \(S\), then both vertices of that pair are white. They have the same blue neighbor \(c\), while \(c\) has at least those two white neighbors, so neither member of that pair can ever be the first forced vertex. Thus \(S\) is not zero forcing.

Conversely, if \(c\in S\) and every \(P_i\) meets \(S\), then each pair containing exactly one blue outer vertex is completed immediately: that blue outer vertex has its mate as its unique white neighbor because the center is already blue. Hence all vertices become blue. Therefore the zero forcing sets containing \(c\) are exactly those meeting every outer pair. Their contribution is
\[
x(2x+x^2)^k=x^{k+1}(2+x)^k.
\]

Now suppose \(c\notin S\). Again, if some outer pair is disjoint from \(S\), then after any possible future forcing of the center that pair still begins with two white vertices and cannot be entered by a force; thus such a set is not zero forcing. If every outer pair is represented by exactly one blue vertex, then initially each blue outer vertex has two white neighbors—its mate and the center—so no first force exists.

If instead every outer pair meets \(S\) and at least one pair \(P_i\) is fully blue, then either blue vertex in that full pair has the center as its unique white neighbor and forces \(c\). Once the center is blue, every singly represented outer pair completes as in the first case. Hence these conditions are sufficient and necessary.

The center-free zero forcing sets therefore contribute
\[
(2x+x^2)^k-(2x)^k=x^k\big((2+x)^k-2^k\big).
\]
Adding both cases gives
\[
\mathcal Z(F_k;x)=x^k\big((1+x)(2+x)^k-2^k\big).
\]

For \(1\le j\le k+1\), with out-of-range binomial coefficients interpreted as zero,
\[
z(F_k;k+j)=\binom{k}{j}2^{k-j}+\binom{k}{j-1}2^{k-j+1}.
\]
The least occupied exponent is \(k+1\), so \(Z(F_k)=k+1\). Its coefficient is
\[
2^k+k2^{k-1}=2^{k-1}(k+2).
\]
Finally, evaluating at \(x=1\) yields
\[
\mathcal Z(F_k;1)=2\cdot3^k-2^k.
\]

## Verification
The included checker constructs \(F_k\) directly for \(1\le k\le8\), tests every vertex subset using the standard zero forcing process, and independently compares the result with the structural classification above. It then checks every coefficient of the claimed polynomial, the minimum exponent, the number of minimum sets, and the total number of zero forcing sets.

## Relationship to prior work
The foundational paper on the zero forcing polynomial introduced \(\mathcal Z(G;x)\), established general coefficient properties, and derived exact polynomials for several graph families. Its first public version is dated 26 January 2018. Full-text searches of that source for friendship, windmill, Dutch windmill, and cactus terminology found no treatment of friendship graphs.

A later paper on zero forcing sets under graph operations proves broad inequalities and extremal comparisons, including results for several operations and graph families. Those results do not give the exact coefficient sequence above for friendship graphs.

Targeted semantic and exact-phrase searches for friendship graphs together with zero forcing polynomial, zero forcing sets, counting, and windmill terminology located general zero forcing polynomial work and unrelated polynomial invariants on windmill graphs, but no equivalent closed formula. The present result gives both a complete structural characterization of all zero forcing sets of \(F_k\) and the resulting exact polynomial.

## Limitations
The theorem is restricted to friendship graphs. It concerns the standard zero forcing process and its counting polynomial, not positive semidefinite, skew, signed, or other zero forcing variants. Exhaustive computation through \(k=8\) is corroborative only; the all-orders statement follows from the structural proof. Literature searches cannot exclude an unindexed or differently phrased exact formula.

## References
1. B. Brimkov, C. C. Fast, I. V. Hicks, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1, 26 January 2018; Discrete Applied Mathematics 258 (2019), 35–48, DOI 10.1016/j.dam.2018.11.033.
2. P. Menon, A. Singh, “Exploring the Influence of Graph Operations on Zero Forcing Sets,” arXiv:2405.01423v1, 2 May 2024; Discrete Mathematics 348 (2025), 114516, DOI 10.1016/j.disc.2025.114516.
