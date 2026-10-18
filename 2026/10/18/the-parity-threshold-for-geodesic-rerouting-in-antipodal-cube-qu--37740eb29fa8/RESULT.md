# The parity threshold for geodesic rerouting in antipodal cube quotients

## Finding
For each integer \(n\ge3\), let \(F_n\) be the simple graph obtained by identifying antipodal binary strings in the cube \(Q_n\), with edges inherited from one-coordinate changes. For distinct vertices \(a,b\), define \(\mathcal R(F_n;a,b)\) to have all shortest \(a\)-to-\(b\) vertex paths as its vertices; two paths are adjacent exactly when they differ at one internal vertex. Put \(r=d_{F_n}(a,b)\). Let \(\mathcal P_r\) denote the adjacent-transposition Cayley graph of the symmetric group \(S_r\), with \(\mathcal P_1=K_1\). Then the complete classification, for every pair \(a\ne b\), is
\[
\mathcal R(F_n;a,b)\cong
\begin{cases}
K_4,& n=4,\ r=2,\\
\mathcal P_r\sqcup\mathcal P_r,& n\ge6\text{ even},\ r=n/2,\\
\mathcal P_r,&\text{otherwise}.
\end{cases}
\]
The cases are exhaustive: \(1\le r\le\lfloor n/2\rfloor\). In particular, shortest-path rerouting is connected for all endpoint pairs when \(n\) is odd or \(n=4\), and disconnected precisely for diametric endpoint pairs when \(n\ge6\) is even. The smallest disconnected case has \(n=6\) and two six-cycles, each with no isolated geodesic.

For even \(n\ge6\), the number of unordered distinct endpoint pairs for which rerouting is disconnected is exactly
\[
2^{n-3}\binom{n}{n/2}.
\]
Their fraction among all unordered distinct pairs of quotient vertices is
\[
\frac{\binom{n}{n/2}}{2(2^{n-1}-1)}\sim\sqrt{\frac{2}{\pi n}}\quad(n\to\infty\text{ through even values}).
\]
Each connected \(\mathcal P_r\) component has \(r!\) vertices, degree \(r-1\), \(r!(r-1)/2\) edges, and equal radius and diameter \(\binom r2\). The exceptional \(K_4\) has radius and diameter one.

## Assumptions and scope
Work with simple undirected graphs and shortest paths as sequences of distinct vertices, with their two endpoints fixed. The antipodal-quotient convention used here has \(2^{n-1}\) vertices and degree \(n\); it must not be confused with the convention that calls the \(2^n\)-vertex cube with an added antipodal perfect matching the folded hypercube. Write \(V(F_n)=\mathbb F_2^n/\langle\mathbf1\rangle\), where \(\mathbf1\) is the all-ones vector, and let \(s_i=[e_i]\) denote the \(n\) coordinate generators. This exactly describes the quotient for \(n\ge3\). In the graph \(\mathcal P_r\), neighboring permutations differ by interchanging adjacent entries. The quantified claim concerns all integers \(n\ge3\) and all pairs of distinct vertices, without restrictions on the underlying shortest paths.

## Proof
**1. Geodesic words.** A walk from \(a\) to \(b\) gives a word in the generators \(s_1,\ldots,s_n\). The kernel of the map from coordinate subsets to \(\mathbb F_2^n/\langle\mathbf1\rangle\) consists of the empty subset and the full coordinate set. Hence if one binary representative of the endpoint displacement has support \(S\), every word for that displacement has odd-occurrence support either \(S\) or \([n]\setminus S\). Its length is at least the size of that support. Consequently,
\[
r=\min\{|S|,n-|S|\}.
\]
Every word of minimum length \(r\) uses \(r\) *different* generators, once each, with the support of size \(r\). When \(r<n/2\), exactly one of \(S,S^c\) has that size, so there are \(r!\) geodesics. When \(n=2r\), both do, so there are \(2r!\) geodesics. These generator words give simple vertex paths because a shorter nonempty proper segment cannot sum to zero in the quotient.

**2. Allowed reroutings for \(n\ge5\).** Suppose two shortest paths differ at exactly one internal vertex, at level \(i\). Their unchanged vertices at levels \(i-1\) and \(i+1\) are joined by alternative two-step walks. If the unordered generator pairs used by these two walks are \(A\) and \(B\), equality of endpoint displacements says their indicator vectors differ by either zero or \(\mathbf1\). But \(|A\mathbin{\triangle}B|\le4<n\), so for \(n\ge5\) they must be the same unordered pair. The intermediate vertex changes precisely when their two distinct generators are exchanged. Thus **each legal rerouting is exactly one adjacent transposition in the generator word**, and conversely each adjacent transposition is legal. It never changes the underlying generator support. For \(r<n/2\), the result is \(\mathcal P_r\). For even \(n=2r\ge6\) at diameter, the two complementary supports therefore give two disconnected copies of \(\mathcal P_r\), with no edges between them.

**3. Exceptional small quotient.** The graph \(F_3\) is complete on four vertices, so all geodesics have one edge and the claimed graph is \(K_1\). The quotient \(F_4\) is the complete bipartite graph \(K_{4,4}\): complementing four bits preserves parity, and each quotient vertex is adjacent to all four vertices of the opposite parity class. Between two distinct vertices of the same class there are four shortest two-edge paths, one through each opposite-class vertex. Every two differ at their sole internal vertex, giving \(K_4\). Pairs of opposite parity are adjacent and have the one-state graph \(K_1\).

**4. Metrics and endpoint count.** The graph \(\mathcal P_r\) is connected because adjacent transpositions sort any permutation. The shortest number of adjacent transpositions taking one permutation to another is their relative inversion count: each swap changes that count by one and bubble sort attains the bound. Its maximal value is \(\binom r2\), attained by reversed order. Vertex transitivity gives equal radius and diameter. For even \(n=2r\), every vertex of \(F_n\) has exactly \(\binom nr/2\) vertices at diameter, because size-\(r\) supports occur in complementary pairs. Since \(|V(F_n)|=2^{n-1}\), divide their incidence count by two for unordered endpoint pairs, obtaining \(2^{n-3}\binom nr\). Dividing by \(\binom{2^{n-1}}2\) and applying the central-binomial Stirling estimate gives the fraction and asymptotic above. The \(n=4\) case is excluded from this disconnected-pair count.

## Verification
The accompanying standalone Python program `verify_folded_geodesics.py` constructs the quotient graph directly from bitmasks; finds distances by breadth-first search; generates every shortest vertex path from the zero class to every other target; constructs the rerouting graph by comparing *vertex sequences*, not generator words; and checks the theorem's component sizes, edge counts and degrees for all targets at every distance for \(3\le n\le10\). It independently measures radii and diameters in one representative rerouting graph of each endpoint distance. The exact output `verify_folded_geodesics.out` ends with `VERIFY_OK`. This finite check is supplementary evidence; the preceding argument proves the infinite family.

## Relationship to prior work
Bonsma [1] formalizes rerouting shortest paths by changing one vertex and studies the complexity and connectivity of that operation. Asplund et al. [2, Proposition 27] prove that the shortest-path graph between antipodes of the *ordinary* cube is an adjacent-transposition Cayley graph. The present theorem classifies **all endpoint pairs of the antipodal quotient**, which is a different base graph. The quotient can create or separate geodesic families: it produces the exceptional \(K_4\) for \(n=4\), but two disconnected permutahedron components for diametric pairs in every even dimension at least six. These conclusions do not follow by simply identifying the vertices of the ordinary cube's path graph. Fang [3] considers folded-hypercube path embedding and panconnectivity, rather than this vertex-by-vertex rerouting relation; only its bibliographic abstract was accessible for comparison.

## Limitations
The result concerns shortest paths, not arbitrary walks, non-shortest paths, or edge-change rerouting. It uses the antipodal quotient convention, not the added-antipodal-edge convention. No claim is made about algorithmic complexity for general base graphs. The exact source comparison is limited by the unavailability of Fang [3]'s complete text under the access available for this review; some unindexed equivalent folded-cube geodesic classification could exist. No independent external mathematical audit has been performed.

## References
[1] P. Bonsma, *The Complexity of Rerouting Shortest Paths*, arXiv:1009.3217 (first public version 2010-09-16; subsequent full version 2012), https://arxiv.org/abs/1009.3217.

[2] J. Asplund, K. Edoh, R. Haas, Y. Hristova, B. Novick, B. Werner, *Reconfiguration graphs of shortest paths*, arXiv:1705.09385 (2017), especially Proposition 27, https://arxiv.org/abs/1705.09385.

[3] J.-F. Fang, *The bipanconnectivity and -panconnectivity of the folded hypercube*, Theoretical Computer Science **385** (2007), 286–300, https://doi.org/10.1016/j.tcs.2007.07.005. Only the abstract and bibliographic record were accessible.
