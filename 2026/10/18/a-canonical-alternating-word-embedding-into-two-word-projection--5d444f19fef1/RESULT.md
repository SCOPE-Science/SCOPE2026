# A canonical alternating-word embedding into two-word projection representations

## Finding

Let \(k\ge 1\) be an integer and let \(u\) be a \(k\)-uniform word over a nonempty finite alphabet \(A\). Write \(p(u)\) for the permutation of \(A\) in order of first appearance in \(u\), and put \(v=p(u)^k\). For distinct letters \(a,b\in A\), let \(\pi_{a,b}\) delete all letters except \(a,b\). Then

\[
\pi_{a,b}(u)=\pi_{a,b}(v)\quad\Longleftrightarrow\quad
\pi_{a,b}(u)\text{ is alternating.}
\]

Consequently the classical graph represented by \(u\) (edge if and only if two letters alternate) equals the two-word projection graph \(G(u,p(u)^k)\) (edge if and only if the two projections agree). If \(\mathcal C_k\) denotes the class of graphs admitting a classical \(k\)-uniform word representation and \(\mathcal G_k\) the class admitting two \(k\)-uniform words under projection equality, this gives an explicit, length-preserving embedding \(\mathcal C_k\subseteq\mathcal G_k\) for every \(k\ge1\). The algorithm constructs the second word from the first in linear time in their common length.

In particular, \(\mathcal C_2\) is exactly the class of circle graphs, hence *every finite circle graph is in* \(\mathcal G_2\). Define \(\mu_\pi(H)\) to be the smallest positive integer \(k\) for which the graph \(H\) has a two-word \(k\)-uniform projection-equality representation. The classification of \(\mathcal G_1\) in [1] gives the sharp formula for every nonempty circle graph \(H\):

\[
\mu_\pi(H)=\begin{cases}1,&H\text{ is a permutation graph},\\2,&H\text{ is not a permutation graph}.\end{cases}
\]

More generally, for a classically word-representable graph \(H\), \(\mu_\pi(H)\le\operatorname{rep}(H)\), where \(\operatorname{rep}(H)\) is the minimum classical uniform representation multiplicity.

## Assumptions and scope

All graphs are finite, simple and undirected. Each word uses exactly the stated alphabet \(A\), and a \(k\)-uniform word contains each letter exactly \(k\) times. For each pair of distinct letters, the projection \(\pi_{a,b}\) preserves the order of the surviving letters. A projected word is *alternating* when no adjacent letters are identical. The empty-alphabet case is not needed. The circle-graph statement uses the standard characterization of circle graphs by classical \(2\)-uniform words [2,3]. The first-public-date attribution is to the introduction of the two-word projection model [1], not to the older classical word characterization.

## Proof

**Canonical projection lemma.** Fix distinct \(a,b\in A\). Suppose first that the earliest occurrence of \(a\) in \(u\) precedes that of \(b\). By the definition of \(p(u)\), their projection from the single permutation \(p(u)\) is \(ab\). It follows that

\[
\pi_{a,b}(p(u)^k)=(ab)^k.
\]

The projection \(\pi_{a,b}(u)\) has exactly \(k\) occurrences of each of \(a,b\), and its first symbol is \(a\). There is exactly one alternating word of length \(2k\) with those counts and first symbol \(a\), namely \((ab)^k\). Equality of projections therefore holds precisely when \(\pi_{a,b}(u)\) alternates. If \(b\) occurs first, interchange the roles to obtain \((ba)^k\). Both directions and all pairs follow. The lemma includes \(k=1\), when all projected pairs alternate and \(p(u)=u\).

**Graph embedding.** For every unordered pair \(\{a,b\}\), the classical edge criterion is alternation in \(\pi_{a,b}(u)\). The two-word criterion is equality between this projection and \(\pi_{a,b}(p(u)^k)\). The lemma makes the criteria identical on every pair. The two words both have length \(k|A|\), so the construction does not increase uniform multiplicity or word length. A single scan of \(u\) records first appearances; repeating the resulting permutation \(k\) times then takes \(O(k|A|)\) time and output space.

**Circle graphs and minimum multiplicity.** Every circle graph has a classical \(2\)-uniform representing word [2,3], so the construction gives two \(2\)-uniform representing words. Conversely, the previously established theorem [1, Theorem 3.2] identifies exactly \(\mathcal G_1\) with permutation graphs. Thus a circle graph requires multiplicity \(1\) if it is a permutation graph, and otherwise requires multiplicity \(2\) (the upper bound just proved and the exclusion from \(\mathcal G_1\) match). This also proves the inequality for classical representation number.

**A strictness example.** On vertices \(0,1,2,3,4\), the word `0140342312` alternates exactly on the five cyclic edges \(01,12,23,34,40\); its first-appearance permutation is `01432`, and the second word `0143201432` has matching two-letter projections exactly on those five edges. This constructs an explicit \(\mathcal G_2\) encoding of \(C_5\). The cycle \(C_5\) is not a permutation graph: every permutation graph admits a transitive orientation, whereas a triangle-free graph admits a transitive orientation only if each vertex is exclusively a source or a sink (otherwise two consecutive directed edges would require a triangle); an odd cycle admits no such assignment. Therefore \(\mu_\pi(C_5)=2\). This example confirms the minimum \(2\) occurs, but membership of individual cycles in \(\mathcal G_2\) was already established in [1, Theorem 3.7]; novelty is not claimed for the example alone.

## Verification

Run `python3 verify.py` and compare its standard output with `verify_output.txt`. The checker exhaustively verifies the canonical-pair lemma on all \(4348\) distinct \(k\)-uniform words in the parameter combinations \((|A|,k)=(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2)\). It separately checks \(2000\) seeded four-letter, three-occurrence words, and searches for and verifies the explicit \(C_5\) example. All recorded checks passed. These finite checks are complementary to, and not substitutes for, the pairwise proof for every \(k\).

## Relationship to prior work

Adamson, Dietz, Fleischmann, Huch and Sacher [1] introduce the two-word projection-equality model, show that the multiplicity-one class equals the permutation graphs, and establish multiplicity-two membership for cycles and \(12\)-representable graphs. Their Theorem 4.1 treats joins and implies some additional examples such as wheels. Those results do not formulate the uniform canonical embedding from arbitrary classical alternating words nor the resulting full circle-graph inclusion. The latter is strictly broader than an individual cycle construction; the proof here uses the first-occurrence permutation instead of the edge-deletion constructions of [1].

Classical circle-graph/\(2\)-uniform equivalence is established independently in [2,3]; it is not claimed as new. The contribution is a translation into the different two-word projection model, together with its sharp one-versus-two multiplicity statement for the entire circle-graph class. Literature and research-record searches did not identify a directly covering result, but absence from searched sources does not certify historical priority.

## Limitations

The theorem gives a constructive upper bound for classical graph representations and an exact minimum specifically for circle graphs. It does **not** characterize all of \(\mathcal G_2\), determine \(\mu_\pi\) for every word-representable graph, or give a converse from arbitrary two-word projection representations to classical words. A two-word pair outside the canonical subclass may represent a graph with smaller multiplicity. The originality assessment is limited by indexing and equivalent terminology; independent validation has not been performed.

## References

[1] D. Adamson, A. Dietz, P. Fleischmann, A. Huch, S. C. Sacher, *2-word-π-representable Graphs*, arXiv:2605.27183v1 (first public version 2026-05-26), https://arxiv.org/html/2605.27183v1 . Consulted Definition 1, Theorems 3.2, 3.7, 3.8, 4.1 and the conclusion.

[2] P. Fleischmann, L. Haschke, J. Löck, D. Nowotka, *Word-representable graphs from a word's perspective*, Acta Informatica (2024), doi:10.1007/s00236-024-00462-y, https://link.springer.com/article/10.1007/s00236-024-00462-y . Its discussion of classical \(2\)-representability identifies circle graphs.

[3] S. Kitaev, *On graphs with representation number 3*, Journal of Automata, Languages and Combinatorics 18 (2013), arXiv:1403.1616, https://arxiv.org/abs/1403.1616 . Describes classical representation number and circle-graph equivalence.
