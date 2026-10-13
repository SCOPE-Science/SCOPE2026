# Exact proper \(3\)-domination of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), \(n_i\ge1\), and \(N=\sum_i n_i\). A proper \(3\)-dominating set is a vertex set that \(3\)-dominates every vertex outside it and for which at least one outside vertex has exactly three neighbors in the set. Write \(\gamma_{\overline{3}}(G)=\infty\) when no such set exists.

Let \(P\) denote the condition that \(N\ge4\) and some nonempty proper subcollection of the partite classes has total order \(3\). Then
\[
\gamma_{\overline{3}}(G)=
\begin{cases}
3,&P,\\
4,&\neg P\text{ and }\bigl(r\ge4\text{ or }(r=3\text{ and some }n_i=2)\bigr),\\
5,&\neg P,\ r=3,\ \text{no }n_i=2,\ \text{and at most one }n_i=1,\\
6,&\neg P,\ r=2,\ \min_i n_i\ge4,\\
\infty,&\text{otherwise.}
\end{cases}
\]
Thus the finite proper \(3\)-domination numbers of connected complete multipartite graphs are exactly \(3,4,5,6\).

## Assumptions and scope
The graph is finite, simple, connected, and complete multipartite, with at least two nonempty partite classes \(V_1,\ldots,V_r\). The convention \(\gamma_{\overline{3}}(G)=\infty\) is used only to state the nonexistence cases uniformly; the initiating definition treats the parameter only when a proper \(3\)-dominating set exists.

For a vertex set \(D\), put \(d_i=|D\cap V_i|\) and \(s=|D|\). A vertex outside \(D\) in \(V_i\) has exactly \(s-d_i\) neighbors in \(D\). Consequently,
\[
D\text{ is proper \(3\)-dominating}\iff
\begin{cases}
D\ne V(G),\\
s-d_i\ge3&\text{for every }i\text{ with }d_i<n_i,\\
s-d_j=3&\text{for at least one }j\text{ with }d_j<n_j.
\end{cases}
\]
This occupancy criterion is also a complete characterization of all proper \(3\)-dominating sets in the class.

## Proof
Choose an incomplete witness part \(V_j\) with \(s-d_j=3\). Exactly three selected vertices therefore lie outside \(V_j\). If \(s\ge7\), then \(d_j\ge4\). Keep the same three selected vertices outside \(V_j\), keep any three selected vertices in \(V_j\), and delete the other selected vertices of \(V_j\). The resulting set has size \(6\); the witness part still has exactly three selected neighbors outside it, while every other incomplete part contains at most three selected vertices and hence sees at least \(3\) of the six selected vertices. Thus every existence instance has a witness of size at most \(6\).

It remains to classify sizes \(3,4,5,6\).

For \(s=3\), a witness part has occupancy \(0\). Every incomplete part must also have occupancy \(0\), because \(3-d_i\ge3\). Hence every selected part is full, and the selected full parts have total order \(3\). Conversely, the union of any nonempty proper subcollection of parts of total order \(3\) is proper \(3\)-dominating. This is exactly condition \(P\).

Assume \(P\) fails. For \(s=4\), the witness occupancy is \(1\), and the other three selected vertices lie outside the witness. Every other incomplete part has occupancy at most \(1\). Hence either the three outside vertices occupy three distinct parts, requiring at least four parts in total, or two of them fill a part of order \(2\) and the third lies in another part. A full part of order \(3\) would give \(P\), and a full order-\(2\) part together with a full singleton would also give \(P\). Therefore size \(4\) occurs exactly when \(r\ge4\), or when \(r=3\) and some part has order \(2\). The converse constructions use one vertex in the witness part and either one vertex in each of three other parts, or all two vertices of an order-\(2\) part plus one vertex in the third part.

Now suppose neither size \(3\) nor size \(4\) is possible. For \(s=5\), the witness occupancy is \(2\), so its part has order at least \(3\), and the remaining three selected vertices must lie in at least two other parts: placing all three in one other part would force that part to be a full order-\(3\) part and hence give \(P\). Since \(r\ge4\) would already give size \(4\), only \(r=3\) remains. Failure of the size-\(4\) case removes parts of order \(2\), and failure of \(P\) removes parts of order \(3\). A size-\(5\) witness therefore exists precisely when the two parts outside some non-singleton witness contain at least three vertices, which in this residual regime is equivalent to having at most one singleton part. A construction selects two vertices in a part of order at least \(4\) and distributes the other three selected vertices over the other two parts with at most two selected vertices in either incomplete part.

Finally suppose sizes \(3,4,5\) all fail. For \(s=6\), the witness occupancy is \(3\), so its part has order at least \(4\), and exactly three selected vertices lie outside it. For two parts, this is possible exactly when both parts have order at least \(4\): an opposite part of order \(3\) would have triggered \(P\), while an opposite part of order at most \(2\) cannot supply three vertices. For three parts, the only residual obstruction after failure of size \(5\) is two singleton parts together with one larger part, and the two singleton parts supply only two outside vertices. Four or more parts were already covered by size \(4\). Hence the only new finite case is \(r=2\) with both part sizes at least \(4\), where selecting three vertices from each shore gives a proper \(3\)-dominating set. All remaining profiles admit no proper \(3\)-dominating set.

## Verification
The accompanying `verify.py` performs two independent finite checks. First, it enumerates every part-occupancy vector for every nondecreasing multipartite profile of total order at most \(20\), computes the proper \(3\)-domination number directly from the defining inequalities, and compares it with the displayed classification. Second, for every profile of total order at most \(9\), it constructs the labeled graph and exhausts all vertex subsets directly from adjacency. It also checks the complete-bipartite specializations stated in the initiating article across a wider finite range. These computations corroborate the proof but are not used to infer the unbounded theorem.

## Relationship to prior work
Chen and Cai introduced proper \(3\)-dominating sets and proved exact complete-bipartite values in the regimes \(K_{3,n}\) and \(K_{m,n}\) with \(m,n\ge4\). Their complete-bipartite argument is recovered by the two-part branch above. The classification here additionally resolves the small-shore bipartite cases and every complete multipartite graph with at least three parts. Full-text inspection of the initiating article found no complete-multipartite theorem or terminology.

The ordinary \(p\)-domination and total \(k\)-domination literature does not imply this classification: those invariants impose lower bounds on the number of selected neighbors, whereas proper \(3\)-domination additionally requires an outside witness with exactly three selected neighbors. That equality condition is the step that forces the three-vertex outside-witness reduction used above.

## Limitations
The result is confined to complete multipartite graphs and the proper \(3\)-domination parameter. It does not classify proper \(p\)-domination for arbitrary \(p\), nor does it address algorithmic complexity on general graphs. The literature search cannot exclude an older poorly indexed equivalent statement under substantially different terminology, although direct searches under the defining phrase, the proper-\(p\) aliases, secondary-domination language, and the complete-multipartite specialization found no such statement.

## References
1. D. Chen and S. Cai, “Proper 3-Dominating Sets in Graphs,” *Mathematics* 13 (2025), 1960. DOI: 10.3390/math13121960. Published 13 June 2025. MSC: 05C09; 05C69.
2. P. Bednarz and M. Pirga, “On Proper 2-Dominating Sets in Graphs,” *Symmetry* 16 (2024), 296. DOI: 10.3390/sym16030296.
3. A. P. Kazemi, “On the Total k-domination Number of Graphs,” *Discussiones Mathematicae Graph Theory* 32 (2012), 419–426. DOI: 10.7151/dmgt.1616.
