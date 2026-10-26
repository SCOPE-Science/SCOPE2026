# Cospectral two-token graphs with different maximum-independent-set counts

## Finding

Let \(R=K_4\square K_4\) be the rook graph, and let \(S\) be the Shrikhande graph. Their two-token graphs are known to be cospectral. The new exact maximum-independent-set classification is:

\[
\alpha(F_2(R))=\alpha(F_2(S))=32,\qquad
\#\mathcal B(F_2(R))=144,\quad \#\mathcal B(F_2(S))=54,
\]

where \(\mathcal B(H)\) denotes the family of all maximum independent vertex sets of \(H\). In each case a member can be viewed as the edge set of a spanning four-regular graph on the sixteen base vertices. Precisely two auxiliary-graph isomorphism types occur:

| Auxiliary graph | Rook graph | Shrikhande graph |
| --- | ---: | ---: |
| \(2K_{4,4}\) | 72 | 30 |
| \(C_8[\overline{K_2}]\) | 72 | 24 |

Under the full base-graph automorphism group, the rook solutions form four orbits of sizes \(18,18,36,72\), and the Shrikhande solutions form six orbits of sizes \(3,3,6,6,12,24\). The corresponding orbit-type refinements are: rook \(2K_{4,4}\): \(18,18,36\), rook blowup: \(72\); Shrikhande \(2K_{4,4}\): \(3,3,6,6,12\), Shrikhande blowup: \(24\).

## Assumptions and scope

All graphs are finite simple undirected graphs. For each \(G\), the vertices of \(F_2(G)\) are the unordered two-element subsets of \(V(G)\); two such subsets are adjacent when their symmetric difference is an edge of \(G\). The base graphs have vertex set \(\mathbb Z_4^2\): in \(R\), adjacency means agreement in exactly one coordinate; in \(S\), adjacency means the difference belongs to \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\), interpreted modulo four. Both have parameters \((16,6,2,2)\). These definitions fix labels, so counts are of actual subsets of the 120-state vertex set, not counts modulo symmetry. The stated automorphism orbits use automorphisms of the sixteen-vertex base graph acting on pairs.

## Proof

**Local capacity.** Given an independent family \(I\subseteq V(F_2(G))\), let \(H_I\) be the auxiliary graph with \(V(H_I)=V(G)\) and \(E(H_I)=I\). For each base vertex \(v\), its neighbors \(N_{H_I}(v)\) must be pairwise nonadjacent in \(G\): otherwise \(\{u,v\}\) and \(\{w,v\}\) would be adjacent token states. Conversely this neighborhood condition for every \(v\) is exactly the token-independence condition. Direct examination of all four- and five-subsets establishes \(\alpha(G)=4\) for both base graphs; the verifier counts 24 four-cocliques in \(R\) and 16 in \(S\), and checks no independent five-subset. Thus

\[
2|I|=\sum_{v\in V(G)}\deg_{H_I}(v)\le 16\cdot 4=64.
\]

Equality holds if and only if each vertex has precisely four neighbors in \(H_I\), forming a maximum coclique of \(G\).

**Exhaustive finite classification.** Enumerate every four-coclique of each base graph. For each \(v\), choose a four-coclique \(C_v\) that omits \(v\). The choices give an auxiliary simple undirected graph if and only if the reciprocity constraints \(u\in C_v\iff v\in C_u\) hold for all distinct \(u,v\). A recursive exhaustive constraint solver chooses the unassigned vertex with the smallest candidate domain and propagates every reciprocity constraint. It finds exactly 144 (rook) and 54 (Shrikhande) distinct complete systems. The verifier reconstructs the independent subset of \(F_2(G)\) associated with every system, checks size 32, and tests all its internal adjacencies. This provides both the attained lower bound and exact completeness of the count.

**Two auxiliary types.** For every enumerated auxiliary graph, the code checks connectivity and the multiplicities of identical open neighborhoods. In the disconnected case, there are two eight-vertex components and four neighborhood-equivalence classes each of size four. Since an open neighborhood has size four, this forces each component to be \(K_{4,4}\). In the connected case, there are eight classes of size two. Each class consists of nonadjacent twins; the quotient by these classes is connected, simple and 2-regular, hence is \(C_8\). Thus the graph is \(C_8[\overline{K_2}]\). The respective type counts are \(72,72\) and \(30,24\).

**Symmetry completeness.** Every base automorphism carries a feasible neighborhood system to another. For \(R\), permuting the four rows and four columns and interchanging coordinates gives all \(2(4!)^2=1152\) automorphisms, since rows and columns are exactly the maximal four-cliques. For \(S\), the explicit group of 16 translations and 12 invertible linear maps preserving the six-step difference set gives 192 automorphisms. This is the full group: the local graph at any vertex is a six-cycle, and the nine vertices at distance two have nine distinct pairs of neighbors in that six-cycle. Thus a vertex stabilizer acts faithfully on the six-cycle and embeds into its dihedral group of order twelve. Applying these groups to every solution yields, without overlaps, the orbit partitions stated above.

## Verification

Run `python3 verify.py` with Python 3.10 or later; only the standard library is required. It constructs base edges from the displayed definitions, enumerates all four- and five-subsets, builds the 120-state token graph and its 672 edges, exhausts the reciprocal-coclique search, verifies each candidate independent set, constructs the full base automorphism groups, and partitions every solution into orbits. It outputs `VERIFY_OK` after all asserted totals match. Exactly 2173 recursive nodes are visited for the rook system and 782 for the Shrikhande system; these are search-tree sizes, not substitutes for the completeness argument.

## Relationship to prior work

Audenaert, Godsil, Royle and Rudolph establish that the symmetric squares of strongly regular graphs with the same parameters are cospectral; the present pair falls under that theorem, so cospectrality is **not claimed as new**. Their graph construction equals the two-token graph. The 2016 work of de Alba, Carballosa, Leaños and Rivera develops exact independence results for token graphs of certain other graph families and general bounds, not the specific extremal-set counts of these two nonbipartite parameter mates. The related published comparison of the base graphs' independence-complex homotopy types pertains to different complexes and does not imply this two-token-graph census. The contribution here is the precise leading independent-set coefficient and natural structural classification for these already-cospectral symmetric squares.

## Limitations

This is an exhaustive finite result for two specified sixteen-vertex base graphs, not an infinite-family theorem or a claim about all strongly regular graphs. The classification is proved by a self-contained enumerative certificate; its completeness relies on the finite search being faithfully executed as specified. Earlier unindexed computations might have reported the same numbers. The 2019 article *On the 2-token graph of a graph* could only be compared through available indexed theorem passages, and the closest published base independence-complex record was not available in full; those are residual literature-access limitations.

## References

1. K. Audenaert, C. Godsil, G. Royle and T. Rudolph, *Symmetric Squares of Graphs* (arXiv:math/0507251, first public 12 July 2005). https://arxiv.org/html/math/0507251v1
2. H. de Alba, W. Carballosa, J. Leaños and L. M. Rivera, *Independence and matching numbers of some token graphs* (arXiv:1606.06370, first public 21 June 2016). https://arxiv.org/abs/1606.06370
3. *On the 2-token graph of a graph*, DOI:10.1016/j.akcej.2019.05.002. Comparison limited to indexed accessible passages.
4. Published mathematical record, *Independence complexes of the Shrikhande and 4×4 rook graph have different sphere-wedge homotopy types*, identifier 2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187 (available summary only).
5. Standard Shrikhande graph entry, https://jaanos.github.io/tables/graphs/Shrikhande.html.
