# An explicit graph family with minimal-fort growth base exceeding the windmill bound

## Finding
For every integer \(k\ge1\), construct a connected graph \(G_k\) from \(k\) copies of the six-vertex graph \(H=(K_1\sqcup K_2)\vee(K_1\sqcup K_2)\) by identifying the isolated vertices in the first three-vertex parts into a single root. The number of inclusion-minimal zero-forcing forts satisfies
\[
\mathcal F(G_k)=8^k+6k,\qquad |V(G_k)|=5k+1.
\]
More precisely, exactly \(8^k\) minimal forts contain the common root, and exactly \(6k\) avoid it. Therefore
\[
\lim_{k\to\infty}\mathcal F(G_k)^{1/|V(G_k)|}
=8^{1/5}=1.515716\ldots>3^{1/3}=1.442249\ldots.
\]
This establishes a connected infinite family whose per-vertex exponential growth exceeds the previously exhibited windmill value.

## Assumptions and scope
Graphs are finite, simple, undirected. A **fort** is a nonempty vertex set \(F\) for which no vertex outside \(F\) has exactly one neighbor in \(F\). A fort is **minimal** when none of its proper subsets is a fort. The graph join is denoted \(\vee\) and disjoint union by \(\sqcup\). The graph \(H\) has vertices \(0,1,2,3,4,5\), root \(0\), and its eleven edges are
\[
01,03,05,12,14,15,23,24,25,34,45,
\]
where \(ij\) represents the undirected edge with endpoints \(i\) and \(j\). Equivalently, the only missing edges of \(K_6\) are \(02,04,13,35\). Distinct copies of \(H\) share only vertex \(0\).

## Proof
**Finite-gadget lemma.** The inclusion-minimal forts of \(H\) containing the root are exactly the eight triples
\[
\{012,013,023,014,034,025,035,045\}.
\]
The inclusion-minimal forts avoiding the root are exactly
\[
\{24,15,123,134,235,345\}.
\]
Here each digit string denotes its vertex set, not an integer. Both assertions can be checked rigorously by testing all \(64\) vertex subsets against the fort definition, then comparing inclusion. The accompanying standalone script performs this exhaustive check.

We also need a local observation. For any \(S\subseteq\{1,2,3,4,5\}\), say \(S\) is *peripherally admissible* if no peripheral vertex outside \(S\) has exactly one neighbor in \(S\). Put \(t(S)=|S\cap\{1,3,5\}|\), the number of neighbors of the root selected in \(S\). Direct examination of all \(32\) possibilities gives exactly \(17\) peripherally admissible sets, partitioned as follows:

* \(t=0\): \(\varnothing,24\).
* \(t=1\): \(124,234,245\).
* \(t=2\): \(123,134,1234,15,235,1245,345,2345\).
* \(t=3\): \(135,1235,1345,12345\).

In particular, every admissible set with \(t=1\) contains the rootless fort \(24\), and every nonempty admissible set with \(t=0\) or \(t\ge2\) contains one of the six rootless minimal forts listed above. Also, the two peripheral vertices accompanying each of the eight root-containing triples contain **no** nonempty peripherally admissible subset; this is an immediate check against the displayed list.

**Forts avoiding the common root.** Let \(F\) be such a minimal fort of \(G_k\), and write \(S_i\) for the intersection of \(F\) with peripheral vertices of petal \(i\). Each \(S_i\) is peripherally admissible. If one nonempty \(S_i\) has \(t=1\), it contains the proper-or-equal rootless fort \(24\) in that petal, so minimality forces \(F\) to equal this fort. If one nonempty \(S_i\) has \(t=0\) or \(t\ge2\), then \(S_i\) itself satisfies the common root's fort condition and contains a rootless minimal fort in that petal. Thus again minimality forces \(F\) to equal a rootless minimal fort in one petal. Conversely, each of the six local rootless minimal forts is a minimal fort globally. Hence there are precisely \(6k\) such forts.

**Forts containing the common root.** For a fort \(F\) containing the common root, its intersection with each petal is a root-containing fort of \(H\): only the root is shared between petals, and peripheral constraints do not involve other petals. If \(F\) is minimal, each restriction must be inclusion-minimal among root-containing forts of \(H\), because any reduction maintaining the root would remain a global fort. Therefore every such \(F\) is the union of one of the eight root-containing triples on each petal.

Conversely, any such union is a fort since all peripheral constraints hold and the root is selected. To prove it is minimal, a proper subfort maintaining the root is excluded by the local minimality of each triple. A subfort omitting the root would consist of peripherally admissible subsets of the selected two peripheral vertices in each petal, yet no selected pair contains a nonempty peripherally admissible set, as established above. Therefore no proper subfort exists. The independent eight choices across \(k\) petals yield exactly \(8^k\) minimal forts containing the root.

Summing proves the formula and taking \((5k+1)\)-st roots proves the exponential-growth statement.

## Verification
Run `python3 verify.py` with Python 3.10 or newer. The standalone checker exhaustively identifies the six rootless and eight rooted minimal forts of \(H\), verifies the \(17\)-set local admissibility table and its implications, and enumerates all minimal forts directly for \(k=1,2,3\), obtaining \(14,76,530\), respectively. The finite checks validate the gadget lemma and corroborate the general argument. The passage to all \(k\) follows from the proof, not from finite testing.

## Relationship to prior work
Becker, Cameron, Hanely, Ong and Previte [1] construct windmill graphs with \(3^k+3k\) minimal forts on \(3k+1\) vertices and formulate a faster-growth conjecture. Dat and Kenter [2], in research first public on 2026-05-08, solve the tree case and explicitly discuss the possibility of general-graph growth exceeding \(3^{1/3}\). Our construction gives the strict inequality \(8^{1/5}>3^{1/3}\) for a connected graph family, using a six-vertex non-multipartite petal. Abiad and Ghasemi Nezhad [3] study fort abundance and tree enumeration but their accessible abstract does not assert this gadget count or the precise improved base. No equivalence to a previously published count was established by the checked sources or mathematical-record queries.

## Limitations
The sequence \(G_k\) has orders only \(5k+1\). The result establishes a strictly larger *per-vertex exponential base along this subsequence*, but does **not** establish that there exists an all-orders family for which the literal consecutive-order ratios converge to a value in \((3^{1/3},2)\). Only the number of minimal forts is counted; no maximality over all graphs of an order is claimed. Independent mathematical validation has not been performed. Unindexed or inaccessible equivalent constructions remain a publication-priority risk; the full text of [3] was not retrieved.

## References
[1] P. Becker, T. R. Cameron, D. Hanely, B. Ong and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963 (first posted 2024-04-09), https://arxiv.org/abs/2404.05963.

[2] N. H. Dat and F. H. J. Kenter, *On the Number of Zero Forcing Minimal Forts on Trees*, arXiv:2605.07298 (first posted 2026-05-08), https://arxiv.org/abs/2605.07298.

[3] A. Abiad and S. Ghasemi Nezhad, *Fort Abundance in Zero Forcing*, arXiv:2609.11754 (first posted 2026-09-10), https://arxiv.org/abs/2609.11754.
