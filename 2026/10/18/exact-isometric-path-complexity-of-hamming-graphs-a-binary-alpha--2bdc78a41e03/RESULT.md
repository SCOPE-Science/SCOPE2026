# Exact isometric-path complexity of Hamming graphs: a binary-alphabet threshold

## Finding

Let \(d\geq1\) and \(q\geq2\) be integers. For the Hamming graph \(H(d,q)=K_q\square\cdots\square K_q\), with \(d\) Cartesian factors, the isometric-path complexity is exactly

\[
\operatorname{ipco}(H(d,q))=
\begin{cases}
\left\lceil (d+1)/2\right\rceil,&q=2,\\
d+1,&q\geq3.
\end{cases}
\]

In particular the binary hypercube \(Q_d=H(d,2)\) has complexity \(\lceil(d+1)/2\rceil\), whereas increasing the coordinate alphabet to three immediately gives the diameter-plus-one maximum. This yields a sharp change in the leading coefficient as the dimension grows.

## Assumptions and scope

All graphs are finite, simple, undirected and connected. Vertices of \(H(d,q)\) are words in \(\{0,1,\ldots,q-1\}^{d}\); two words are adjacent when they differ in exactly one coordinate. Their graph distance equals Hamming distance, and the graph has diameter \(d\). An *isometric path* is a shortest path between its endpoints. For a chosen vertex \(r\), let \(\kappa_r(P)\) be the minimum number of isometric paths having \(r\) as one endpoint whose vertex sets together contain \(V(P)\). Set

\[
\operatorname{ipco}(G)=\min_{r\in V(G)}\ \max_{P\text{ an isometric path of }G}\kappa_r(P).
\]

A path of length zero is allowed. No requirement is made that covering paths be disjoint, be subsets of the given path or have edges contained in it. The covering condition concerns vertices only. Every Hamming graph is vertex-transitive, so all choices of root yield the same maximum.

## Proof

**General upper bound.** A shortest path in \(H(d,q)\) changes each coordinate at most once, because any repeated change would make the path longer than the Hamming distance between its endpoints. It therefore has at most \(d+1\) vertices. For any root \(r\), each vertex of such a path lies on an \(r\)-rooted shortest path. Covering vertices individually proves \(\operatorname{ipco}(H(d,q))\leq d+1\).

**Alphabet size at least three: sharpness.** Fix any root \(r=(r_1,\ldots,r_d)\). Choose, for each coordinate \(i\), two *distinct* symbols \(a_i,b_i\), both different from \(r_i\); this is possible for \(q\geq3\). Starting at \((a_1,\ldots,a_d)\), successively replace coordinate \(i\) by \(b_i\), for \(i=1,\ldots,d\). Each coordinate changes exactly once, so the resulting \(d\)-edge path is isometric and contains \(d+1\) different vertices. Every one of its vertices is at distance \(d\) from \(r\). Along any \(r\)-rooted shortest path, distance from \(r\) increases by exactly one at each step. Thus such a covering path meets the distance-\(d\) sphere in at most one vertex. Covering the constructed \(d+1\) vertices needs at least \(d+1\) rooted paths. This works for **every** root, proving equality.

**Binary upper bound.** Suppose \(q=2\), and fix any root \(r\). Consider any isometric path \(P=(v_0,v_1,\ldots,v_\ell)\), where \(0\leq\ell\leq d\). Partition these \(\ell+1\) consecutive vertices into blocks of two, with one singleton if their count is odd. For a two-vertex block \((x,y)\), adjacent vertices of a binary cube lie in distance layers differing by exactly one: a flip changes the number of disagreements with \(r\) by \(\pm1\). Let \(z\) be the endpoint farther from \(r\) and \(w\) the nearer. Since \(d(r,z)=d(r,w)+1\), any shortest path from \(r\) to \(w\), followed by the edge \(wz\), is a shortest path from \(r\) to \(z\). This one rooted geodesic covers the whole block. A singleton is covered by any rooted shortest path through it. Hence

\[
\kappa_r(P)\leq\left\lceil\frac{\ell+1}{2}\right\rceil\leq\left\lceil\frac{d+1}{2}\right\rceil.
\]

**Binary lower bound.** Write \(d=2k\) or \(d=2k+1\). Relative to any fixed root \(r\), choose an initial word with exactly \(k\) disagreeing coordinates. There are \(k\) initially agreeing coordinates if \(d=2k\), and \(k+1\) if \(d=2k+1\). Traverse a path by alternately flipping an initially agreeing coordinate into disagreement and an initially disagreeing coordinate into agreement, always using a coordinate not previously flipped. If \(d\) is odd, perform one final agreeing-to-disagreeing flip. This uses each coordinate exactly once and therefore produces an isometric path of length \(d\). Its \(d+1\) vertices all lie in the union of Hamming spheres of radii \(k\) and \(k+1\) about \(r\). Any shortest path starting at \(r\) meets each distance sphere in at most one vertex and consequently covers at most two of the constructed vertices. Therefore covering this path requires at least \(\lceil(d+1)/2\rceil\) rooted paths. Together with the binary upper bound, equality follows.

The constructions and inequalities include the boundary \(d=1\): one path suffices in \(K_2\), whereas two paths are needed to cover an edge of \(K_q\) from a third root for \(q\geq3\).

## Verification

The accompanying standalone Python 3 script `verify.py` performs a separate finite combinatorial check. For each listed \((q,d)\), it constructs every shortest path by permuting the differing coordinates of ordered endpoint pairs, deduplicates the vertex sets of those paths, constructs every root-to-vertex shortest path for the all-zero root, and solves the exact finite set-cover problem on each candidate path using subset dynamic programming. It tests all binary dimensions \(1\leq d\leq5\), ternary dimensions \(1\leq d\leq3\) and quaternary dimensions \(1\leq d\leq2\), totaling 7,210 distinct geodesic vertex sets. Reproduction: run `python3 verify.py`; its final line must be `VERIFY_OK`, and the full reference output is `verification_output.txt`. Vertex-transitivity justifies considering one root per parameter pair. These finite checks are supplemental; the unrestricted statements are established by the preceding proof.

## Relationship to prior work

Chakraborty, Dailly, Das, Foucaud, Gahlawat and Ghosh (ISAAC 2022, DOI `10.4230/LIPIcs.ISAAC.2022.12`) introduced the isometric-path antichain-cover viewpoint while studying global isometric path cover and approximation ratios. The paper notes previously known *global* shortest-path-cover numbers of hypercubes and Cartesian products of complete graphs. Those global numbers are different from covering **each single shortest path by rooted shortest paths**, the invariant here.

Chakraborty, Chalopin, Foucaud and Vaxès (arXiv `2301.00278`, first posted 2022-12-31; MFCS 2023 DOI `10.4230/LIPIcs.MFCS.2023.32`; extended version 2025) define isometric-path complexity and show its equality to the earlier antichain parameter, provide algorithms, and prove bounds for graph classes including hyperbolic, Truemper-configuration-free and outerstring graphs. The inspected texts do not give the two exact Hamming-graph formulas above. The present proof instead exploits distance layers, a diametral geodesic contained in one Hamming sphere for the nonbinary case, and a two-layer zigzag in the binary case.

## Limitations

The result concerns uniform Hamming graphs \(H(d,q)\), not Cartesian products with different coordinate alphabet sizes, and it does not determine general rooted-cover complexities of arbitrary graphs. The finite computations do not certify infinite cases and are not a substitute for the proof. Full-text inspection of relevant primary sources and database searches did not reveal prior coverage of these formulas; a matching result under alternative terminology in unindexed or inaccessible work remains possible. No independent external audit has been performed.

## References

1. D. Chakraborty, A. Dailly, S. Das, F. Foucaud, H. Gahlawat, S. K. Ghosh, *Complexity and Algorithms for ISOMETRIC PATH COVER on Chordal Graphs and Beyond*, ISAAC 2022, DOI: `10.4230/LIPIcs.ISAAC.2022.12`. First public publisher date: 2022-12-14. Full text: `https://drops.dagstuhl.de/storage/00lipics/lipics-vol248-isaac2022/LIPIcs.ISAAC.2022.12/LIPIcs.ISAAC.2022.12.pdf`.
2. D. Chakraborty, J. Chalopin, F. Foucaud, Y. Vaxès, *Isometric Path Complexity of Graphs*, arXiv:2301.00278 (first posted 2022-12-31), MFCS 2023 DOI: `10.4230/LIPIcs.MFCS.2023.32`. Extended open-access article: `https://arxiv.org/html/2301.00278v5`.
