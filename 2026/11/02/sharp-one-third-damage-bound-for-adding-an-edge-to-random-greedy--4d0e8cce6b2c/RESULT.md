# Sharp one-third damage bound for adding an edge to random greedy matching

## Finding

**Theorem.** Let \(G=(V,E)\) be any finite simple undirected graph, and let \(u,v\in V\) be two distinct nonadjacent vertices. Process all the edges in uniformly random order, accepting an edge exactly when neither endpoint is already matched, and write \(\mu(G)\) for the expected number of accepted edges. Then

\[
-\frac13\le \mu(G+uv)-\mu(G)\le 1.
\]

Both constants are best possible over all finite simple graphs. Moreover, if either \(u\) or \(v\) is isolated in \(G\), then

\[
\mu(G+uv)\ge\mu(G).
\]

Hence adding one allowed match can decrease the expected output of the random-edge greedy algorithm, but by **at most one third of an edge**, independently of graph size. This is a statement about the expected cardinality of the maximal matching selected by this particular randomized procedure, not the maximum matching number.

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted. The random greedy procedure examines each existing edge once in a uniformly random permutation; equivalently, it repeatedly chooses uniformly among the edges remaining in the subgraph induced by unmatched vertices. \(G+uv\) inserts exactly one previously absent edge, retaining the same vertex set. The expectation \(\mu\) is over the edge order, with no additional random graph sampling. The bounds hold for every vertex count including isolated vertices, with the empty-edge graph admitted.

## Proof

**1. Vertex-deletion lemma.** Fix any total order \(\prec\) on the edges of a finite graph \(K\). Let \(j(K;\prec)\) be the number of edges accepted by the greedy procedure and give \(K-w\) the relative order inherited from \(\prec\). For each vertex \(w\),

\[
0\le j(K;\prec)-j(K-w;\prec)\le1.
\]

We prove this by induction on the number of edges. For an edgeless graph it is immediate. Let \(f=ab\) be the first edge. If \(w\notin\{a,b\}\), both procedures take \(f\), and the difference is exactly the difference for \(K-\{a,b\}\) versus its deletion of \(w\), with the inherited order. Apply the induction hypothesis. If \(w=a\), the original process takes \(f=ab\), so its total equals \(1+j(K-\{w,b\};\prec)\). Applying the induction hypothesis to vertex \(b\) in \(K-w\) gives

\[
j(K-\{w,b\};\prec)\le j(K-w;\prec)\le1+j(K-\{w,b\};\prec),
\]

which proves the desired difference. The case \(w=b\) is symmetric. This proof also covers cases where removing endpoints leaves no edges.

A uniformly random edge order restricts to a uniformly random order on every subgraph. Consequently,

\[
0\le\mu(K)-\mu(K-w)\le1,
\qquad
0\le\mu(K)-\mu(K-\{u,v\})\le2.
\tag{1}
\]

If one of \(u,v\) is isolated, the second upper bound improves to \(1\), because deleting an isolated vertex leaves the greedy matching unchanged.

**2. Exact edge-addition recursion.** Put \(m=|E(G)|\), \(e=uv\notin E(G)\), and define

\[
\Delta(G,e)=\mu(G+e)-\mu(G).
\]

If \(m=0\), then \(\Delta(G,e)=1\). For \(m\ge1\), conditioning on the first selected edge gives the exact identity

\[
(m+1)\Delta(G,e)
=1+\mu(G-\{u,v\})-\mu(G)
+\sum_{\substack{f\in E(G)\\ f\cap\{u,v\}=\varnothing}}
\Delta(G-V(f),e),
\tag{2}
\]

where \(V(f)\) is the pair of endpoints of \(f\). To check (2), use \(\mu(K)=1+|E(K)|^{-1}\sum_{f\in E(K)}\mu(K-V(f))\) for every nonempty \(K\), and subtract the first-edge expansions for \(G+e\) and \(G\). For a first edge \(f\) incident with \(u\) or \(v\), the newly inserted \(e\) disappears on removing the endpoints, so its contribution cancels. For an edge disjoint from both, the residual contribution is \(\Delta(G-V(f),e)\). The special first edge \(e\) contributes \(1+\mu(G-\{u,v\})\).

**3. Simultaneous induction.** Induct on \(m\) to prove the claimed upper and lower bounds, plus the nonnegative bound if one endpoint of \(e\) is isolated. All graphs on fewer edges satisfy the induction hypothesis, regardless of vertex count. Let \(q\) be the number of edges of \(G\) disjoint from \(\{u,v\}\), and let \(k=m-q=\deg_G(u)+\deg_G(v)\), since \(uv\notin E(G)\).

For the upper bound, (1) gives \(1+\mu(G-\{u,v\})-\mu(G)\le1\), while the \(q\) summands in (2) are at most \(1\). Thus

\[
(m+1)\Delta(G,e)\le1+q\le m+1.
\]

If \(k\le1\), at least one of \(u,v\) is isolated. By the improved deletion bound, the first three terms of (2) together satisfy \(1+\mu(G-\{u,v\})-\mu(G)\ge0\). The isolated endpoint remains isolated in every graph \(G-V(f)\) occurring in (2); therefore every summand is nonnegative by the stronger induction hypothesis. Hence \(\Delta(G,e)\ge0\).

If \(k\ge2\), (1) gives \(1+\mu(G-\{u,v\})-\mu(G)\ge-1\). Every summand is at least \(-1/3\) by induction, and therefore

\[
(m+1)\Delta(G,e)\ge-1-\frac q3
\ge-\frac{m+1}{3},
\]

because \(m=q+k\) and \(k\ge2\). This proves all assertions simultaneously.

**4. Sharp examples.** If \(G\) is edgeless and \(u,v\) are distinct, inserting \(uv\) increases the greedy matching size from \(0\) to \(1\) deterministically, attaining the upper constant. For the lower constant, take \(G\) with edges \(\{a,b\}\) and \(\{c,d\}\), and insert \(e=\{b,c\}\). The original greedy matching has size \(2\) surely. The augmented graph is the four-vertex path with three edges. If its middle edge is first (probability \(1/3\)), exactly one edge is accepted; otherwise two edges are accepted. Its expected size is \(5/3\), so \(\Delta(G,e)=-1/3\). Both examples are finite and exact.

## Verification

A standalone standard-library Python checker, `verify_greedy_matching.py`, evaluates \(\mu\) using exact rational first-edge recursions on all labeled simple graphs with at most six vertices, tests every single missing-edge addition, and tests the vertex-deletion inequalities. It separately computes direct edge-permutation averages and common-order vertex-deletion outcomes on graphs with at most four vertices. A replay from the standalone source passed **945204 exact assertions**. The analytic induction above, rather than finite enumeration, proves the universal theorem.

## Relationship to prior work

Random-edge greedy matching is a standard procedure: Miller and Pritikin (1997) study expected sizes and worst-case approximation ratios, and Arnosti (first publicly available November 2, 2021) studies RANDOM-EDGE on random bipartite graphs and compares distinct greedy policies. The present assertion concerns a different axis: an **adversarial single-edge insertion into an arbitrary fixed graph** and its sharp change in expected matching size. In the checked material, no stronger published theorem was found to imply the exact interval or the isolated-endpoint refinement. This is a qualified novelty assessment, not a claim of exhaustive priority. The complete 1997 Miller–Pritikin article could not be examined, and may contain a closely related comparison.

## Limitations

The result concerns unweighted cardinality, uniformly random edge order, and one inserted edge. It does not address weighted random-greedy matching, vertex-arrival algorithms, batches of edge insertions, pathwise domination, or whether any particular matching obtained after insertion contains the earlier one. Finite checks do not certify the induction for infinitely many graph orders; the proof does. Historical priority has not been independently audited, particularly against inaccessible older full text.

## References

- N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, *Stochastic Systems* 12 (2022), 133–150, first published online 2021-11-02. https://doi.org/10.1287/stsy.2021.0082
- Z. Miller and D. Pritikin, *On randomized greedy matchings*, *Random Structures & Algorithms* 10 (1997), 353–383. https://doi.org/10.1002/(SICI)1098-2418(199705)10:3%3C353::AID-RSA5%3E3.0.CO;2-V
- M. Dyer and A. Frieze, *Randomized greedy matching*, early random-greedy approximation analysis, 1991 (bibliographic context in Arnosti 2021 and Miller–Pritikin 1997).
