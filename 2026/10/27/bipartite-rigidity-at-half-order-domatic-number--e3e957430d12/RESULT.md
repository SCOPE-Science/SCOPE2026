# Bipartite rigidity at half-order domatic number

## Finding
Let \(m\ge 3\) be an integer. A connected finite simple bipartite graph \(G\) on \(2m\) vertices satisfies \(\operatorname{dom}(G)=m\) if and only if
\[
G\cong K_{m,m}-M_t\qquad\text{for some }0\le t\le m,
\]
where \(M_t\) is a matching with \(t\) edges. Every graph on this list has domination number \(\gamma(G)=2\). It has exactly \((m-t)!\) unordered domatic partitions with \(m\) classes. Among these graphs, **exactly** the crown graph \(K_{m,m}-M_m\) is domatically edge-critical, meaning deletion of every edge strictly decreases the domatic number (necessarily from \(m\) to \(m-1\)).

In particular, the classification describes all connected bipartite domatically perfect graphs with domination number \(2\) and order at least \(6\), where *domatically perfect* means \(\operatorname{dom}(G)=|V(G)|/\gamma(G)\).

## Assumptions and scope
All graphs are finite, undirected, loopless, and simple. A set \(D\subseteq V(G)\) is *dominating* when each vertex is in \(D\) or adjacent to a vertex in \(D\). A domatic partition is an **unordered** partition of all vertices into nonempty dominating sets; its maximum possible number of classes is \(\operatorname{dom}(G)\). Edge-critical means \(\operatorname{dom}(G-e)<\operatorname{dom}(G)\) for every \(e\in E(G)\). The number \(m\) is an integer with \(m\ge3\). The missing edges \(M_t\) have pairwise disjoint endpoints, with \(t\) ranging from \(0\) to \(m\) inclusive. No assertion is made for \(m=2\), where same-bipartition dominating pairs create additional optimal partitions.

## Proof
**1. No singleton class.** If a connected bipartite graph \(G\) of order \(2m\ge6\) has a dominating singleton, the chosen vertex is universal. Bipartiteness forces \(G\) to be the star \(K_{1,2m-1}\). Its domatic number is \(2\): one class can be the center and the other all leaves, while the closed neighbourhood of a leaf has size \(2\), preventing any larger partition. Since \(m\ge3\), a graph with domatic number \(m\) has no dominating singleton.

**2. Forced pairs and balanced sides.** If \(\operatorname{dom}(G)=m\), an \(m\)-class domatic partition has \(2m\) vertices and no singleton class. Hence every class consists of two vertices. Write a bipartition \(V(G)=A\sqcup B\). A two-vertex dominating set wholly contained in \(A\) must equal \(A\), since vertices of \(A\) have no neighbours in \(A\). Thus \(|A|=2\). Every other class then lies entirely in \(B\), but with \(|B|=2m-2\ge4\), no two-vertex subset of \(B\) can dominate the other vertices of \(B\). This is impossible; the same argument excludes a class wholly in \(B\). Consequently the classes can be written \(\{a_i,b_i\}\), for \(1\le i\le m\), where \(a_i\in A\), \(b_i\in B\). Therefore \(|A|=|B|=m\).

For each \(i\), the class \(\{a_i,b_i\}\) dominates every \(b_j\) with \(j\ne i\) only if \(a_i b_j\) is an edge; it dominates every \(a_j\) with \(j\ne i\) only if \(a_j b_i\) is an edge. Thus every off-diagonal cross-edge exists. The only edges that can be absent are the diagonal \(a_i b_i\), which form a matching. This gives necessity.

**3. Converse and minimum domination.** Conversely, in \(K_{m,m}-M_t\), pair each vertex with its same-index partner in a labelling in which the deleted matching lies on the diagonal. Every class \(\{a_i,b_i\}\) dominates the graph because all off-diagonal cross-edges exist. Hence \(\operatorname{dom}(G)\ge m\). No vertex dominates the graph alone, as it cannot dominate the other \(m-1\) vertices on its own bipartition side. Therefore \(\gamma(G)\ge2\), while one of the displayed pairs shows \(\gamma(G)\le2\). The universal inequality \(\operatorname{dom}(G)\le |V(G)|/\gamma(G)\) gives \(\operatorname{dom}(G)=m\). For \(m\ge3\) every such graph is connected, since any two vertices in one side have a common neighbour and every vertex has neighbours on the other side.

**4. Exact number of optimum partitions.** In any optimum partition every class is a cross-pair. If \(a_i b_i\) is a deleted edge, then \(a_i\) must be paired with \(b_i\): were it paired with another \(b_j\), the unselected \(b_i\) would not be dominated. Equivalently, its missing-neighbour obstruction forces the original deleted pair. The \(t\) deleted edges therefore force \(t\) specific classes. All remaining \(m-t\) vertices on each side have complete cross-adjacency and may be paired by an arbitrary bijection; each resulting pair dominates. Hence the number of unordered optimum partitions is exactly \((m-t)!\).

**5. Criticality.** If \(t<m\), choose a diagonal edge not in \(M_t\). Deleting it gives \(K_{m,m}-M_{t+1}\), which still has domatic number \(m\); thus the graph is not domatically edge-critical. If \(t=m\), deleting any edge \(a_i b_j\) with \(i\ne j\) leaves both \(a_i b_i\) and \(a_i b_j\) absent. The set of missing cross-edges is therefore not a matching. By the necessary direction of the classification (the graph remains connected, or directly by the forced-pair argument), its domatic number cannot be \(m\). Deleting a single edge from an \(m\)-domatic graph reduces its domatic number by at most one: merge the two colour classes of the endpoints of that edge; all the remaining classes retain their domination property, and the merged class still dominates. Thus the new domatic number is exactly \(m-1\).

## Verification
The accompanying standalone Python program `verify_domatic.py` independently encodes closed-neighbourhood domination with bit masks, enumerates all \(800\) labelled bipartite-side graphs of order \(6\) and all \(102{,}528\) of order \(8\) (one orientation of each bipartition size), and checks the classification against the existence of a partition into dominating pairs. The numbers of graphs satisfying the property were \(34\) and \(209\), respectively, matching the numbers of deleted matchings in \(K_{3,3}\) and \(K_{4,4}\). The program also exhausts all perfect pairings for every \(m=3,4,5\) and \(0\le t\le m\), reproducing the exact \((m-t)!\) counts. The infinite-parameter proof above, not these finite computations, establishes the theorem.

Run from a folder containing the script using `python3 verify_domatic.py` (Python standard library only). Its output terminates with `All exhaustive tests passed.` on success.

## Relationship to prior work
Matsumoto's *Domatically perfect graphs* (2020), Section 5, Problem 5.2, asks for a characterization of graphs whose domination number is \(2\) and which are domatically perfect. The paper explicitly notes \(K_{n,n}\) and the single-edge-deleted \(K_{n,n}\) as examples; the present theorem characterizes **all** connected bipartite examples of order at least \(6\), including arbitrary matching deletions, and counts their optimum partitions. Matsumoto's theorem for complete multipartite graphs does not by itself cover graphs with deleted cross-edges. Spakowski's *The Complexity of Domatic Criticality* (2026) studies the edge-deletion recognition problem and does not supply this bipartite characterization. Earlier general domatic-criticality structure results may independently imply some special-case consequences, but no equivalent full statement was found in the checked sources.

## Limitations
The classification requires bipartiteness and \(m\ge3\); it is not a characterization of all graphs with domination number \(2\), or of all domatically critical graphs. It does not claim a faster algorithm for the general recognition problem. A finite search is not a substitute for the displayed general proof. Historical priority requires independent literature review beyond the inspected sources, particularly older structural work on domatically critical graphs.

## References
1. Naoki Matsumoto, *Domatically perfect graphs*, AKCE International Journal of Graphs and Combinatorics **17** (2020), 242–251, DOI: 10.1016/j.akcej.2019.06.008 (Section 5, Problem 5.2).
2. Holger Spakowski, *The Complexity of Domatic Criticality*, arXiv:2607.18878, first posted 2026-07-21, https://arxiv.org/abs/2607.18878.
3. B. Zelinka, *Domatically critical graphs* (1980), cited in Spakowski, for earlier structural background; not relied on for the proof.
