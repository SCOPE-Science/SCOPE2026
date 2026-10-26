# Isolated-forest zero forcing and exchange connectivity of triangular graphs

## Finding
Let \(n\ge3\) be an integer and let \(T_n=J(n,2)=L(K_n)\). Identify each vertex of \(T_n\) with a distinct unordered pair from \([n]\); two such vertices are adjacent precisely when their pairs intersect. For an initially blue set \(B\subseteq V(T_n)\), let \(H_B=([n],E(K_n)\setminus B)\) be the graph formed by the *white* pairs, retaining all \(n\) labeled base vertices.

**Theorem.** The blue set \(B\) is a zero forcing set of \(T_n\) if and only if \(H_B\) is an acyclic graph containing at least one isolated vertex. In particular,
\[
Z(T_n)=\binom n2-n+2,\qquad m_n=n(n-1)^{n-3},
\]
where \(m_n\) is the number of *all* minimum zero forcing sets. They are exactly the complements of a labeled tree on \(n-1\) vertices together with one isolated vertex.

If \(\mathcal Z(T_n;x)=\sum_{B\text{ zero forcing}}x^{|B|}\), the **complete polynomial** is
\[
\mathcal Z(T_n;x)=x^{\binom n2}\,n!\,[z^n](e^z-1)\exp\left(\sum_{k=2}^n\frac{k^{k-2}}{k!}\,x^{-(k-1)}z^k\right).
\]
This formal coefficient expression always simplifies to an ordinary polynomial with nonnegative integer coefficients. For instance,
\[
\mathcal Z(T_5;x)=80x^7+45x^8+10x^9+x^{10}.
\]

Define \(\mathcal R_n\) with one vertex for each minimum zero forcing set of \(T_n\), and an edge when the blue sets differ by deleting one blue vertex and adding one formerly white vertex. Then \(\mathcal R_n\) is connected. The minimum sets are uniquely labeled by pairs \((r,T)\), with \(r\in[n]\) isolated in the white graph and \(T\) a spanning tree on \([n]\setminus\{r\}\). When \(r=s\), adjacency is exactly ordinary single-edge tree exchange. For \(r\ne s\), adjacency between \((r,T)\) and \((s,T')\) holds exactly when
\[
T=U\cup\{sa\},\qquad T'=U\cup\{rb\},
\]
for a spanning tree \(U\) on \([n]\setminus\{r,s\}\) and any \(a,b\) in that set. In particular, the **number of edges between different isolated-vertex classes** is
\[
\binom n2(n-2)^{n-2}.
\]

## Assumptions and scope
All graphs are finite, simple and undirected. An ordinary zero forcing process starts from a chosen blue vertex set; a blue vertex with exactly one white neighbor changes that neighbor to blue, and forces may be performed sequentially in any legal order. A zero forcing set eventually colors all vertices blue. A forest may include isolated vertices. The parameter \(n\) ranges over **every integer at least three**, with the convention that the unique labeled tree on one vertex has count one (needed in the cross-class formula when \(n=3\)). The theorem concerns *ordinary* zero forcing and minimum-set token jumping, not positive semidefinite zero forcing or a claimed diameter of \(\mathcal R_n\).

## Proof
**Local forcing rule.** At an intermediate stage let \(H\) be the graph of currently white edges in \(K_n\). A blue vertex \(uv\) of \(T_n\) corresponds to an edge not in \(H\). Its white neighbors are exactly the white edges incident with \(u\) or \(v\). Since \(uv\notin E(H)\), these two sets are disjoint. Hence the number of its white neighbors is \(d_H(u)+d_H(v)\). It forces exactly one white edge if and only if one endpoint of \(uv\) is isolated in \(H\) and the other has white degree one. Such a force deletes a *leaf edge* of the white graph.

**Necessity.** If the initial white graph has no isolated base vertex, the local rule prohibits any first force. If it has a cycle, consider the first attempted force of an edge on that cycle. Until that moment all cycle edges remain white, so each endpoint of that edge has white degree at least two. The local rule makes the force impossible. Therefore a successful starting set must have an isolated base vertex and no cycle.

**Sufficiency.** Suppose \(H\) is a forest with an isolated vertex \(z\). If \(H\) has an edge, choose a leaf \(u\), whose unique white edge is \(uv\). Since \(z\) is isolated, \(uz\) is blue and has exactly one white neighbor, namely \(uv\). The resulting white graph remains a forest with \(z\) isolated. Repeating deletes all white edges. This proves the equivalence for every initial set.

**Extremal count.** A forest on \(n\) vertices with at least one isolated vertex has at most \(n-2\) edges. Equality forces exactly two connected components: one isolated vertex and one tree on the other \(n-1\) vertices. Cayley's formula supplies \((n-1)^{n-3}\) trees on each fixed set of \(n-1\) labels, with \(n\) choices for the omitted label. Since blue vertices are the complementary \(\binom n2\) pairs, the stated minimum size and count follow. The scalar minimum was previously known; the argument here supplies the equality-family characterization.

**Polynomial.** A labeled forest is an unordered assembly of labeled tree components. A nonsingleton tree of order \(k\ge2\) has \(k^{k-2}\) choices and \(k-1\) edges. If \(t\) marks white edges and \(z\) marks base vertices, the exponential generating function of forests having at least one singleton component is
\[
(e^z-1)\exp\left(\sum_{k=2}^{\infty}\frac{k^{k-2}}{k!}\,t^{k-1}z^k\right).
\]
Indeed the singleton components contribute the first factor, while the nonsingleton tree components contribute the second. Extract the coefficient of \(z^n\), multiply by \(n!\), and substitute \(t=x^{-1}\) with global factor \(x^{\binom n2}\). Terms of order exceeding \(n\) can be truncated, giving the stated polynomial.

**All exchange adjacencies.** Replacing one blue pair by one white pair corresponds exactly to deleting one white edge and adding another, keeping the number \(n-2\) fixed. For equal isolated labels \(r\), this is the standard spanning-tree exchange on the remaining \(n-1\) labels. Suppose instead that the isolated label changes from \(r\) to \(s\). The old tree must have precisely one edge incident with \(s\), because a single edge deletion makes \(s\) isolated; similarly the new tree must have precisely one edge incident with \(r\). Removing these two distinct leaf edges leaves the same spanning tree \(U\) on \([n]\setminus\{r,s\}\). Conversely any such \(U\) and attachment vertices \(a,b\) produce two valid white trees differing in exactly one edge. Thus the cross-class adjacency criterion is necessary and sufficient.

**Connectivity.** Within a fixed isolated class, the spanning-tree exchange graph of a complete graph is connected: given two trees, remove an edge outside the target tree and insert an appropriate target-tree edge reconnecting its two components, strictly increasing their common edges. For different isolated labels \(r,s\), choose any \(t\in[n]\setminus\{r,s\}\). Via within-class exchanges, change the current tree into the star centered at \(t\) on \([n]\setminus\{r\}\). Replace its edge \(ts\) by \(tr\), reaching the star centered at \(t\) on \([n]\setminus\{s\}\). Thus any isolated class communicates with any other, and \(\mathcal R_n\) is connected.

**Cross-class edge count.** Choose an unordered pair \(\{r,s\}\) of isolated labels. The common tree \(U\) on the other \(n-2\) labels has \((n-2)^{n-4}\) possibilities when \(n\ge4\) by Cayley, and one possibility at \(n=3\). Each of \(s\) and \(r\) has \(n-2\) independently chosen attachment vertices. Every cross-class exchange is uniquely determined by these data, yielding \(\binom n2(n-2)^{n-2}\) edges; the same formula gives three edges when \(n=3\).

## Verification
The standalone file `verify.cpp` performs exhaustive independent checks for all \(2^{\binom n2}\) initial blue/white configurations at each \(3\le n\le7\). One implementation uses the graph-theoretic forest-and-isolate criterion; a second constructs the line graph and performs simultaneous legal forcing rounds. For \(n\le6\), a third implementation performs chronological single forces in a different order. The computations also compare coefficients with an independently implemented labeled-forest recurrence. For \(n\le6\), they enumerate all minimum configurations, check connectivity of the full optimum exchange graph, and verify the formula for cross-isolate exchange edges. To replay, use a standard C++17 compiler: `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. The expected final line is `ALL_VERIFY_OK`.

The checked minimum-set counts for \(n=3,4,5,6,7\) are \(3,12,80,750,9072\); the checked cross-isolate edge counts for \(n=3,4,5,6\) are \(3,24,270,3840\). These are **finite regression checks**, not the proof of the all-parameter statements, which is provided above.

## Relationship to prior work
The scalar value \(Z(L(K_n))=\binom n2-n+2\) is established prior work. Earlier line-graph theorems for graphs with Hamiltonian paths imply it, and later Johnson-graph literature independently records the same scalar; neither scalar result is claimed new. Fallat, Meagher, Soltani and Yang specifically discuss \(J(n,2)\) and compute its *positive* zero forcing number, which is a related but different forcing rule. General papers introducing zero forcing polynomials and token-jumping reconfiguration supply the terminology; their inspected statements are not this complete ordinary-forcing characterization, forest enumeration, and exchange description. The contributions asserted here are the exact criterion for **every** initial set and the consequent complete polynomial, count/classification of all minimizers, and connected exchange structure with an exact cross-class edge count.

## Limitations
This theorem treats only the triangular graphs \(J(n,2)\), not general Johnson graphs, other line graphs, or positive semidefinite zero forcing. It does not determine the full diameter or complete distance distribution of \(\mathcal R_n\). The novelty comparison uses accessible indexed literature and is not a proof that no earlier unindexed statement or thesis gives an equivalent forest criterion. The integer checks stop at \(n=7\) for full forcing and \(n=6\) for reconfiguration; the all-parameter proof is symbolic.

## References
1. S. Fallat, K. Meagher, A. Soltani and B. Yang, *Compressed Cliques Graphs, Clique Coverings and Positive Zero Forcing*, arXiv:1508.07357v1 (public 2015-08-28), especially Section 8 and Lemma 8.3.
2. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra Appl. (2008), DOI: 10.1016/j.laa.2007.10.009.
3. S. Fallat and A. Soltani, *Line graphs: their maximum nullities and zero forcing numbers*, Czechoslovak Math. J. 66 (2016), 743–755, DML-CZ identifier 145869, especially Theorem 3.4 and the cited earlier result.
4. A. Abiad, R. Simoens and S. Zeijlemaker, *On the diameter and zero forcing number of some graph classes in the Johnson, Grassmann and Hamming association scheme*, arXiv:2302.07757, especially Corollary 9.
5. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020).
6. K. Boyer and collaborators, *The zero forcing polynomial of a graph*, arXiv:1801.08910 (2018); Discrete Appl. Math. (2019), DOI: 10.1016/j.dam.2018.11.033.
