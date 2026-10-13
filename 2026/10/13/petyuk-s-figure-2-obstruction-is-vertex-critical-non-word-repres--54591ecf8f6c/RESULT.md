# Petyuk's Figure-2 obstruction is vertex-critical non-word-representable
## Finding
Let \(S\) be the \(17\)-vertex induced subgraph of the simplified de Bruijn graph \(S(3,3)\) displayed in Petyuk's Figure 2, with vertex set
\[
\{102,210,021,121,212,221,022,202,220,222,122,112,211,111,011,110,101\}.
\]
The published paper proves that \(S\) is non-word-representable. The new statement is that \(S\) is vertex-critical for non-word-representability: for every vertex \(v\in V(S)\), the graph \(S-v\) is word-representable. Consequently every proper induced subgraph of \(S\) is word-representable.

Thus the published obstruction cannot be shortened by deleting vertices from its own vertex set. Any smaller non-word-representable induced subgraph of the ambient graph \(S(3,3)\), if one exists, must use at least one vertex outside this Figure-2 obstruction.
## Assumptions and scope
The simplified de Bruijn graph \(S(3,3)\) has ternary words of length \(3\) as vertices. Distinct vertices \(x_1x_2x_3\) and \(y_1y_2y_3\) are adjacent exactly when \(x_2x_3=y_1y_2\) or \(y_2y_3=x_1x_2\).

A graph is word-representable exactly when it admits a semi-transitive orientation. For a fixed total order of the vertices, orient each edge from the earlier vertex to the later one. Such an orientation is semi-transitive exactly when it is shortcut-free.

The finding establishes minimality only among induced subgraphs of the displayed graph \(S\). It does not settle Petyuk's stronger open problem asking whether \(S\) has minimum order among all non-word-representable induced subgraphs of the full \(27\)-vertex graph \(S(3,3)\).
## Proof
Petyuk's Theorem 5 proves non-word-representability of the displayed graph \(S\) by a complete semi-transitive-orientation contradiction.

For the new direction, for each of the \(17\) choices of a deleted vertex \(v\), the accompanying certificate supplies an explicit total order on the remaining \(16\) vertices. Orient every edge of \(S-v\) forward in that order. The verifier exhaustively enumerates every directed path in this acyclic orientation. Whenever a directed path has at least three edges and its endpoints are adjacent, it checks that every pair of vertices on the path is adjacent. This is exactly the condition excluding shortcuts. Therefore each supplied orientation is semi-transitive, and each \(S-v\) is word-representable.

Now let \(H\) be any proper induced subgraph of \(S\). Choose a vertex \(v\in V(S)\setminus V(H)\). Then \(H\) is an induced subgraph of \(S-v\). Word-representability is hereditary under induced subgraphs, so \(H\) is word-representable. Hence \(S\) is induced-subgraph-minimal, equivalently vertex-critical, among non-word-representable graphs.
## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs all edges of the \(17\)-vertex graph directly from the simplified de Bruijn overlap rule. For each deleted vertex it checks that the listed order contains exactly the other \(16\) vertices, orients every edge forward, enumerates all directed paths, and rejects any shortcut. All \(17\) orientations pass.

No search timeout or failed solver call is used as evidence. The non-word-representability of the undeleted graph is the published premise; the new computational evidence consists only of explicit positive semi-transitive-orientation witnesses for all vertex deletions.
## Relationship to prior work
Petyuk introduced simplified de Bruijn graphs, proved \(S(3,k)\) non-word-representable for every \(k\ge3\), and used the present \(17\)-vertex graph \(S\subset S(3,3)\) as the obstruction for \(k=3\). The paper then asks whether this graph is minimum by number of vertices among non-word-representable induced subgraphs of \(S(3,3)\).

The later embedding paper of Huang, Kitaev, and Pyatkin continues the study of induced subgraphs of simplified de Bruijn graphs and develops positive word-representability results for structured induced subgraphs. It restates the broader simplified-de-Bruijn conjecture but does not give a deletion-minimality analysis of Petyuk's Figure-2 obstruction.

The present result is a strict partial answer to the stated minimal-obstruction problem: it proves that no proper induced subgraph contained inside the Figure-2 vertex set can be a counterexample. It does not exclude a smaller obstruction on a different vertex set of \(S(3,3)\).
## Limitations
The result does not determine the minimum order of a non-word-representable induced subgraph of the ambient \(S(3,3)\). In particular, it does not exclude an obstruction on fewer than \(17\) vertices using vertices outside the displayed set.

The supplied orders certify word-representability but do not optimize representation number or the length of a representing word.

An unindexed computation may already have tested the \(17\) vertex deletions, although the inspected primary and follow-up papers and targeted searches do not report this vertex-criticality statement.
## References
1. A. V. Petyuk, “On word-representability of simplified de Bruijn graphs,” arXiv:2210.14762v1, first public version 2022-10-20.
2. S. Huang, S. Kitaev, and A. Pyatkin, “An embedding technique in the study of word-representability of graphs,” arXiv:2312.10377v1; Discrete Applied Mathematics 346 (2024), 170–182, DOI 10.1016/j.dam.2023.12.017.
3. M. M. Halldórsson, S. Kitaev, and A. Pyatkin, “Semi-transitive orientations and word-representable graphs,” Discrete Applied Mathematics 201 (2016), 164–171, DOI 10.1016/j.dam.2015.07.033.
