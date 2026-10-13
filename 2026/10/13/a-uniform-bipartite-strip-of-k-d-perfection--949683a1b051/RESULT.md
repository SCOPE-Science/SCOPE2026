# A uniform bipartite strip of \(k,d\)-perfection
## Finding
Let \(G\) be a finite bipartite graph and let \(k,d\) be integers satisfying
\[
2\le k\le d+1\quad\text{and}\quad d\le 2k-3.
\]
Equivalently, \(k-1\le d\le 2k-3\). Then \(G\) is \(k,d\)-perfect: for every induced subgraph \(H\),
\[
\chi_d^k(H)=\left\lceil\frac{\omega_d^k(H)}{k-1}\right\rceil.
\]
In particular, every finite bipartite graph is both \(3,2\)-perfect and \(3,3\)-perfect. The case \((k,d)=(2,1)\) recovers classical perfection of bipartite graphs.

## Assumptions and scope
A set is \(k,d\)-independent when every shortest path of length at most \(d\) contains fewer than \(k\) vertices of the set. The number \(\chi_d^k(H)\) is the least number of \(k,d\)-independent color classes covering \(V(H)\). A set is a \(k,d\)-clique when each of its \(k\)-subsets is contained in a shortest path of length at most \(d\); its maximum size is \(\omega_d^k(H)\). The empty graph is immediate under the standard zero convention, so the proof below treats nonempty induced subgraphs.

## Proof
Fix a nonempty induced subgraph \(H\) of \(G\). It is bipartite; write its bipartition as \(A\cup B\). A shortest path of length \(\ell\le d\) alternates between \(A\) and \(B\), and hence contains at most
\[
\left\lceil\frac{\ell+1}{2}\right\rceil\le
\left\lceil\frac{d+1}{2}\right\rceil\le k-1
\]
vertices from either side. Therefore the two bipartition classes form a \(k,d\)-proper coloring, so \(\chi_d^k(H)\le2\).

Consider the \(k\)-uniform geodesic hypergraph whose hyperedges are the \(k\)-sets contained in shortest paths of length at most \(d\). If it has no hyperedge, then every vertex set is \(k,d\)-independent, so \(\chi_d^k(H)=1\). In that case no set of size at least \(k\) is a \(k,d\)-clique, while every set of size below \(k\) is vacuously one. Thus \(\omega_d^k(H)=\min\{|V(H)|,k-1\}\), and the displayed perfection equality is \(1=1\).

Suppose instead that the geodesic hypergraph has a hyperedge. Then one color cannot be \(k,d\)-proper, so \(\chi_d^k(H)=2\); the hyperedge itself is a \(k,d\)-clique, hence \(\omega_d^k(H)\ge k\). On the other hand, any set of \(2k-1\) vertices contains at least \(k\) vertices in one of \(A,B\). No shortest path of length at most \(d\) contains \(k\) vertices from one bipartition class, by the first paragraph. Consequently no \((2k-1)\)-set is a \(k,d\)-clique, so
\[
k\le \omega_d^k(H)\le2k-2.
\]
It follows that
\[
\left\lceil\frac{\omega_d^k(H)}{k-1}\right\rceil=2=\chi_d^k(H).
\]
Since the argument applies to every induced subgraph, \(G\) is \(k,d\)-perfect.

## Verification
A standalone checker reconstructs the defining geodesic hypergraph directly for every labeled bipartite graph with fixed side sizes between one and three, for every nonempty induced subgraph, and for \(2\le k\le5\) with \(k-1\le d\le2k-3\). It independently checks the exact \(k,d\)-clique number and the one-versus-two-color dichotomy. The exhaustive stress test covers 682 labeled bipartite graphs, 36,766 nonempty induced-subgraph instances, and 367,660 parameter checks. A separate arithmetic check verifies the two proof inequalities for \(2\le k\le100\). These finite checks are not used as a proof of the infinite statement.

## Relationship to prior work
Cody and Detore introduced these \(k,d\)-invariants and the corresponding notion of \(k,d\)-perfection. They prove that every finite tree is \(3,2\)-perfect and that every cycle is \(3,2\)-perfect, then explicitly ask which graphs are \(3,2\)-perfect. The theorem above contains all finite trees and all even cycles at \((3,2)\), while extending simultaneously to every bipartite graph and to the entire strip \(k-1\le d\le2k-3\). Their full text contains no occurrence of the term “bipartite.”

The earlier general-position-coloring literature treats the special regime \(k=3\) with the distance cutoff equal to the graph diameter. That work determines the corresponding coloring invariant for several graph classes, but does not provide the hereditary clique-equality statement proved here for arbitrary bipartite graphs across a two-parameter strip.

## Limitations
No claim is made for \(d\ge2k-2\), where a shortest path can contain \(k\) vertices from one bipartition class and the two key counting steps above no longer apply. The literature comparison is necessarily limited by discoverability: a differently phrased or uncatalogued result could exist. The finite checker tests only small labeled graphs and is a stress test, not a substitute for the analytic proof.

## References
1. Brent Cody and Rose Detore, “Metric general position extensions of classical graph invariants and perfection,” arXiv:2601.04351, first public 2026-01-07.
2. Ullas Chandran S. V., Gabriele Di Stefano, Haritha S., Elias John Thomas, and James Tuite, “Colouring a graph with position sets,” arXiv:2408.13494, first public 2024-08-24.
