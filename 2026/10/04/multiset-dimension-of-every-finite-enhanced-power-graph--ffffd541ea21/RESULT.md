# Multiset dimension of every finite enhanced power graph
## Finding
For every finite group \(G\), let \(\mathcal P_e(G)\) denote the enhanced power graph: its vertices are the elements of \(G\), and two distinct vertices are adjacent exactly when they lie in a common cyclic subgroup. Under the convention of Simanjuntak--Siagian--Vetrík for multiset dimension,
\[
\operatorname{md}(\mathcal P_e(G))=
\begin{cases}
1,& |G|\le 2,\\
\infty,& |G|\ge 3.
\end{cases}
\]
Thus the multiset-dimension problem posed for arbitrary finite enhanced power graphs has a complete answer.

## Assumptions and scope
The graph is the full enhanced power graph, including the identity vertex. Multiset dimension is the invariant defined by Simanjuntak, Siagian and Vetrík: a set \(W\) is multiset-resolving when the multiset of distances from each vertex to \(W\) distinguishes every pair of vertices; if no such set exists, the dimension is \(\infty\). Their convention gives multiset dimension \(1\) to paths.

The statement is for finite groups only. It does not concern the deleted or proper enhanced power graph obtained after removing the identity or other dominating vertices.

## Proof
Let \(e\) be the identity of \(G\). For every \(x\in G\setminus\{e\}\), the subgroup \(\langle e,x\rangle=\langle x\rangle\) is cyclic. Hence \(e\) is adjacent to every other vertex of \(\mathcal P_e(G)\). Therefore
\[
\operatorname{diam}(\mathcal P_e(G))\le 2.
\]

Assume first that \(|G|\ge4\). The identity has degree \(|G|-1\ge3\), whereas every vertex of a path has degree at most \(2\). Thus \(\mathcal P_e(G)\) is not a path. If \(|G|=3\), then \(G\cong C_3\), so every pair of elements lies in the cyclic group \(G\) itself and \(\mathcal P_e(G)=K_3\), again not a path. Simanjuntak--Siagian--Vetrík prove that every non-path graph of diameter at most \(2\) has infinite multiset dimension. It follows that
\[
|G|\ge3\quad\Longrightarrow\quad \operatorname{md}(\mathcal P_e(G))=\infty.
\]

For \(|G|=1\) or \(2\), the group is cyclic and \(\mathcal P_e(G)\) is respectively \(P_1\) or \(P_2\). The same source proves that a graph has multiset dimension \(1\) exactly when it is a path. Hence \(\operatorname{md}(\mathcal P_e(G))=1\) in these two cases.

## Verification
The proof uses two ingredients whose hypotheses match exactly: the identity is a universal vertex of the full enhanced power graph, and Theorem 3.1 of Simanjuntak--Siagian--Vetrík applies to any non-path graph of diameter at most \(2\). The only possible path cases are checked separately.

The accompanying `verify.py` independently builds several finite examples from their multiplication laws, constructs the enhanced power graph, computes all-pairs graph distances, and exhaustively tests every nonempty landmark set for the multiset-resolving property. It returns multiset dimension \(1\) for \(C_1\) and \(C_2\), and no multiset-resolving set for \(C_3\), \(C_4\), \(C_2\times C_2\), and \(S_3\).

## Relationship to prior work
Simanjuntak, Siagian and Vetrík introduced multiset dimension and proved the diameter-two obstruction: a non-path graph of diameter at most \(2\) has infinite multiset dimension. Ma, Kelarev, Lin and Wang later surveyed enhanced power graphs and explicitly posed as Problem 14 the determination of the multiset dimension of \(\mathcal P_e(G)\) for every finite group. Their survey cites the multiset-dimension literature but does not state the above consequence.

The present observation combines the universal identity vertex of an enhanced power graph with the diameter-two obstruction, and then resolves the small orders separately. Targeted searches for the exact invariant together with “enhanced power graph” found the 2022 open problem and later work on other enhanced-power-graph invariants, but no source stating this classification.

## Limitations
This is a short structural consequence rather than a new technique for multiset dimension. Its value is that it gives a complete classification for a specifically posed open problem. The conclusion depends essentially on retaining the identity vertex; proper or deleted enhanced power graphs need not have diameter at most \(2\), so the argument does not classify their multiset dimension.

Literature searches cannot prove absolute absence from all unindexed sources. The originality conclusion is therefore limited to the inspected primary sources, targeted web searches, and the searched mathematical-results database.

## References
1. R. Simanjuntak, P. Siagian and T. Vetrík, “The multiset dimension of graphs,” arXiv:1711.00225v1, 1 November 2017; revised 2019. In particular, Theorem 3.1 states that a non-path graph of diameter at most \(2\) has infinite multiset dimension. https://arxiv.org/abs/1711.00225
2. X. Ma, A. Kelarev, Y. Lin and K. Wang, “A survey on enhanced power graphs of finite groups,” *Electronic Journal of Graph Theory and Applications* 10 (2022), 89–111, DOI: 10.5614/ejgta.2022.10.1.6. Problem 14 asks for the multiset dimension of the enhanced power graph of every finite group.
3. G. Aalipour, S. Akbari, P. J. Cameron, R. Nikandish and F. Shaveisi, “On the structure of the power graph and the enhanced power graph of a group,” *Electronic Journal of Combinatorics* 24(3) (2017), P3.16, DOI: 10.37236/6497.
