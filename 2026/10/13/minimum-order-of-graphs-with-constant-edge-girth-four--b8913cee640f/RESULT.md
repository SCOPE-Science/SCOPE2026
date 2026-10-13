# Minimum order of graphs with constant edge-girth four
## Finding
For a finite connected simple graph \(G\) and an edge \(e\), let the *edge-girth* of \(e\) be the length of the shortest simple cycle of \(G\) containing \(e\), or \(+\infty\) if there is no such cycle. Define \(\nu_4(m)\) as the smallest possible order of a connected simple graph having exactly \(m\) edges, each of edge-girth \(4\), and set \(\nu_4(m)=+\infty\) when no realization exists.

**Theorem.** For every positive integer \(m\),
\[
\nu_4(m)=\begin{cases}
+\infty,&m\in\{1,2,3,5\},\\
\lceil2\sqrt m\rceil,&m=4\text{ or }m\ge6.
\end{cases}
\]
For every admissible \(m\ge7\), an optimal realization is explicitly the balanced complete bipartite graph on \(\lceil2\sqrt m\rceil\) vertices with a suitably sized matching deleted.

Equivalently, when \(n\ge6\), **every** integer \(m\) in the interval
\[
\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1\le m\le\left\lfloor\frac{n^2}{4}\right\rfloor
\]
occurs in an \(n\)-vertex graph with constant edge-girth four, and none can be realized on fewer than \(n\) vertices. This is an exact minimum-order instance of the vertex-count realization problem for edge-girth sequences.

## Assumptions and scope
All graphs are finite, simple, undirected, and connected, with vertex count \(n\) and edge count \(m\). Edge-girth four means both (a) that \(G\) is triangle-free and (b) that every edge of \(G\) belongs to at least one simple four-cycle. A triangle would give its three edges edge-girth three, so the equivalence is immediate. The theorem concerns the constant sequence of four-edge-girth values only; it does not require planarity, regularity, or bipartiteness for arbitrary realizing graphs. It classifies **minimum vertex counts**, not all admissible vertex counts or isomorphism types.

## Proof
**Step 1 (existence exclusions and the small cases).** A cycle requires at least four edges, so \(m=1,2,3\) are impossible. Any two distinct simple four-cycles have at most two edges in common: if they shared three, those three edges would form a length-three path whose closing fourth edge is uniquely determined, forcing identical four-cycles. With five edges, choose one four-cycle; the fifth edge could belong only to a distinct four-cycle sharing at least three of its edges with the first, a contradiction. Thus \(m=5\) is impossible. For \(m=4\), the four-cycle attains order four. For \(m=6\), \(K_{2,3}\) has five vertices and six edges; every edge belongs to a four-cycle.

**Step 2 (universal lower bound).** Suppose a connected graph \(G\) has \(n\) vertices and every edge has edge-girth four. It contains no triangle, hence Mantel's theorem gives
\[
m\le\lfloor n^2/4\rfloor.
\]
Because \(m\) is an integer, this implies \(n\ge\lceil2\sqrt m\rceil\). No stronger lower bound is assumed.

**Step 3 (the construction parameters).** Fix \(m\ge7\). Define
\[
n=\lceil2\sqrt m\rceil,\quad a=\lfloor n/2\rfloor,\quad b=\lceil n/2\rceil,\quad d=ab-m.
\]
Here \(n\ge6\), \(a,b\ge3\), and \(n\) is the smallest integer with \(\lfloor n^2/4\rfloor\ge m\). Therefore
\[
\lfloor(n-1)^2/4\rfloor<m\le\lfloor n^2/4\rfloor=ab.
\]
If \(n=2a\), the preceding strict inequality gives \(m\ge a(a-1)+1\), so \(0\le d\le a-1\). If \(n=2a+1\), it gives \(m\ge a^2+1\), hence again \(0\le d\le a-1\). Choose \(d\) pairwise vertex-disjoint edges of \(K_{a,b}\), and delete precisely those edges; call the result \(H\). It has \(a+b=n\) vertices, \(ab-d=m\) edges, and is bipartite, hence triangle-free.

**Step 4 (all surviving edges belong to four-cycles).** Let \(uv\) be any remaining edge of \(H\), with \(u\) in the side of size \(a\) and \(v\) in the side of size \(b\). Put
\[
A'=N_H(v)\setminus\{u\},\qquad B'=N_H(u)\setminus\{v\}.
\]
Because deleted edges form a matching, \(|A'|\ge a-2\ge1\) and \(|B'|\ge b-2\ge1\). If some \(u'\in A'\) and \(v'\in B'\) are adjacent, the four vertices \(u,v,u',v'\) form the required cycle \(u-v-u'-v'-u\). Suppose, for a contradiction, that no edge joins \(A'\) and \(B'\). Then **all** edges in the complete bipartite product \(A'\times B'\) belong to the deleted matching. Since each vertex is incident to at most one deleted edge, nonemptiness implies \(|A'|=|B'|=1\). Their lower bounds force \(a=b=3\). In that case \(u\) and \(v\) each have a distinct missing incident edge (as \(uv\) survives), and the sole edge of \(A'\times B'\) is a third deleted edge. This contradicts \(d\le a-1=2\). Consequently every surviving edge lies on a four-cycle.

**Step 5 (connectivity).** Any two vertices in the side of size \(a\) share a neighbor: together they omit at most two of the \(b\ge3\) vertices on the other side. Symmetrically, any two vertices on the other side have a common neighbor because \(a\ge3\). Every vertex has at least two neighbors. Hence \(H\) is connected. Its edges have edge-girth exactly four by Steps 3–4, and its order equals the lower bound from Step 2.

This completes the proof for all positive integers \(m\).

## Verification
The accompanying standalone standard-library program `verify.py` reconstructs every claimed optimal witness for \(m=4\) and for all \(6\le m\le3000\), checking exact counts, connectivity, absence of triangles, and membership of **every edge** in a four-cycle. It independently enumerates all \(33{,}861\) nonempty labeled simple graphs on one through six vertices and finds minimum-order realizations only for \(m\in\{4,6,7,8,9\}\), at orders \(4,5,6,6,6\) respectively. Its recorded output is `VERIFY_OUTPUT.txt`. The universal proof is in Steps 1–5; these finite tests are reproducibility checks, not an extrapolation to all \(m\).

## Relationship to prior work
Marey, Hilaire, and Laclau introduce the edge-girth sequence and characterize which constant sequences are realizable (Theorem 6.1); for constant value four their criterion gives \(m=4\) or \(m\ge6\). Their Section 7 studies the **maximum diameter** of a realization, and Section 8 explicitly identifies determining **realizable numbers of vertices** as a natural further question. The theorem above solves its sharp *minimum-order* case for constant edge-girth four. The lower bound is Mantel's classical extremal theorem for triangle-free graphs, but Mantel alone does **not** imply that graphs attaining the requisite vertex count may have every edge in a four-cycle. The matching-deletion lemma in Step 4 supplies the missing upper-bound implication uniformly at each admissible size.

## Limitations
The finding does not determine which larger vertex counts are realizable, the number of realizing isomorphism types, diameter-extremal realizations, or the minimum order for edge-girth values other than four. It uses the classical Mantel bound without claiming that bound as new. Novelty comparisons are limited to consulted public primary literature, published searchable records, and prior research records; unindexed equivalent work cannot be excluded. No independent external audit has been performed.

## References
1. Lilian Marey, Paul Hilaire, and Charlotte Laclau, *On the Realizability of Edge-Girth Sequences*, arXiv:2607.25629, first public version 28 July 2026, especially Theorem 6.1 and Sections 7–8. Author-posted full text also available at https://www.researchgate.net/publication/410930988_On_the_Realizability_of_Edge-Girth_Sequences.
2. Willem Mantel, the classical triangle-free edge bound (1907): every \(n\)-vertex triangle-free graph has at most \(\lfloor n^2/4\rfloor\) edges. Standard summary: https://en.wikipedia.org/wiki/Tur%C3%A1n%27s_theorem#Mantel's_theorem.
