# Exact locating-domination coalition numbers of complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_t}\) be a finite connected complete multipartite graph, with \(t\ge2\), positive part sizes, and \(N=\sum_i n_i\ge3\). Put \(r=\#\{i:n_i=2\}\) and \(s=\#\{i:n_i=1\}\). The locating-domination coalition number satisfies

\[
C_L(G)=\begin{cases}
4,&\max_i n_i\le2,\ s\le2,\text{ and }[r\ge2\text{ or }(r=1,s=2)],\\
3,&\text{otherwise}.
\end{cases}
\]

In particular, \(C_L(G)\le4\) without any bound on the number or sizes of parts. The equality class contains arbitrarily large graphs \(K_{2,\ldots,2}\), and outside the exceptional small-part configurations the sharp value is three. The only complete bipartite graph of order at least three attaining four is \(K_{2,2}\). This is a classification of the exact maximum number of blocks, not merely an existence theorem.

## Assumptions and scope

All graphs are finite, simple and undirected. A locating-dominating (LD) set \(D\subseteq V(G)\) dominates every vertex outside \(D\), and the signatures \(N_G(v)\cap D\) for vertices outside \(D\) are pairwise distinct. An LD-coalition is a pair of disjoint non-LD sets whose union is LD. An LDC-partition is a partition of the vertex set into nonempty non-LD blocks, each with some different block forming an LD-coalition. \(C_L(G)\) is the greatest number of blocks in such a partition. The graph \(K_2\) has no LDC-partition and is excluded by \(N\ge3\).

For a complete multipartite graph, denote its original partite sets by \(V_1,\ldots,V_t\). Every LD-set omits at most one vertex of each \(V_i\), and at most one vertex belonging to a singleton part. Conversely, these two omission conditions together with domination characterize LD-sets. Indeed, two omitted vertices in one part have identical signatures, as do two omitted singleton parts. If neither pair exists, equal signatures for two omitted vertices in different parts would force both respective parts to contribute no vertex of the LD-set, contradicting the singleton-omission condition.

## Proof

**Lower bound three.** If some original part has at least two vertices \(u,v\), take blocks \(V(G)\setminus\{u,v\},\{u\},\{v\}\). The first block is not LD since it fails to distinguish the false twins \(u,v\); neither singleton dominates the other vertex of their part. Either union of the first block with one singleton is the complement of a single vertex and is LD, because the graph is connected. If every original part is a singleton, the graph is complete; the same partition works, because two omitted vertices have identical signatures, while a singleton cannot distinguish the other vertices. Thus \(C_L(G)\ge3\).

**A coalition-graph lemma.** Associate with any LDC-partition a simple graph whose vertices are its blocks and whose edges represent LD-coalitions. Every block has a neighbour. If a graph on at least four vertices has minimum degree at least one and no two disjoint edges, it must be a star: three edges with pairwise intersection are either incident at a common vertex or form a triangle, and the triangle cannot accommodate another nonisolated vertex without a disjoint edge.

**No block has three coalition partners in such a star.** Suppose a block \(A\) has three disjoint partner blocks \(B_1,B_2,B_3\), so each \(A\cup B_j\) is LD. Let \(q_i=|V_i\setminus A|\). Each \(B_j\) must contain at least \(q_i-1\) members of \(V_i\), and the three partners are disjoint. Therefore \(3(q_i-1)\le q_i\), forcing \(q_i\le1\). Let \(q_s\) be the number of omitted vertices belonging to singleton parts. Applying the same argument to the singleton-omission condition gives \(q_s\le1\). If \(A\) fails to dominate a vertex, all of \(A\) is contained in that vertex's original part. The two omission bounds then force all other parts to consist of at most one omitted singleton part and at most one omitted vertex of the occupied part; thus \(|V(G)\setminus A|\le2\), contradicting three distinct nonempty partner blocks. Consequently \(A\) is dominating and, by the omission criterion, locating: it is LD, contradicting the definition of the partition. Hence every LDC-partition with at least four blocks has two disjoint coalition edges.

**Two disjoint edges impose part-size rigidity.** Let \(A\cup B\) and \(C\cup D\) be disjoint LD unions. For any original part of size \(m\), each LD union includes at least \(m-1\) of its vertices. Disjointness gives \(2(m-1)\le m\), hence \(m\le2\). Let \(s\) be the number of singleton original parts. Each union includes at least \(s-1\) singleton vertices, so \(2(s-1)\le s\), hence \(s\le2\).

**Five blocks are impossible.** Suppose there is a fifth block \(E\) outside \(A,B,C,D\). Every original two-vertex part already contributes exactly one vertex to each of the two disjoint LD unions, so \(E\) contains only singleton-part vertices. Both LD unions omit \(E\), and can each omit at most one singleton vertex; thus \(E=\{z\}\). There can be no other original singleton vertices anywhere, since a singleton vertex in either coalition pair would be omitted along with \(z\) by the opposite pair. All other blocks outside the four are therefore impossible. Since \(E\) has a coalition partner \(F\), the LD set \(E\cup F\) contains at least one vertex from every two-vertex original part. As at least four nonempty blocks other than \(E\) exist, there are at least two such original parts. It follows that \(F\) by itself dominates and distinguishes every omitted vertex: it meets every two-vertex part, omits at most one vertex from each, and omits only the singleton vertex \(z\). Thus \(F\) is LD, a contradiction. We conclude \(C_L(G)\le4\).

**Characterization of four.** If an LDC-partition has four blocks, its coalition graph has two disjoint edges by the star argument. The rigidity argument forces every original part to have size at most two and \(s\le2\). Because the graph has at least four vertices, these conditions imply either \(r\ge2\) or \((r,s)=(1,2)\).

Conversely, when \(r\ge2\) and \(s\le2\), choose a two-vertex original part \(\{u,v\}\) and use singleton blocks \(\{u\},\{v\}\). Split each of the other two-vertex parts, placing one vertex into a block \(A\) and its mate into \(B\). Distribute the at most two original singleton-part vertices so that \(A\) and \(B\) each receive at most one. The four blocks are \(A,B,\{u\},\{v\}\). The large blocks omit both \(u,v\) and are not LD; the singletons fail to dominate the other vertex of their original part. Each union of \(A\) or \(B\) with either \(\{u\}\) or \(\{v\}\) leaves at most one vertex omitted from each original part and at most one omitted singleton part. It also meets at least two original parts, so is LD. Hence the four blocks form an LDC-partition.

For \((r,s)=(1,2)\), the graph is \(K_{2,1,1}\). Its four singleton vertex blocks form an LDC-partition: either vertex of the two-vertex part forms an LD-coalition with either singleton-part vertex. This completes the classification. \(\square\)

## Verification

The standalone program `verify_ldc_multipartite.py` independently constructs the actual graph adjacency masks, checks domination and distinct open-neighbourhood signatures for every vertex subset, and exhaustively enumerates all vertex-set partitions by restricted-growth strings. The comparison covers all 86 complete-multipartite isomorphism profiles on three through nine vertices, including complete graphs, stars, and mixed part-size patterns. The recorded output is `verification_output.txt`: `VERIFY_OK` and the complete counts by order. These finite checks corroborate the unrestricted proof; they are not its basis.

## Relationship to prior work

Chellali, Dobrynin, Foucaud, Golmohammadi and Valenzuela-Tripodoro (2026) introduced the parameter \(C_L\), proved a general upper bound \(C_L(G)\le |V(G)|-\gamma_L(G)+2\), and determined it for paths, cycles, and certain near-order extremizers. Their complete small-order classification already includes \(K_{2,2}\) and \(K_{2,1,1}\). Those two finite cases are not claimed as new. The theorem above concerns the entire infinite multipartite class and its sharp size-independent bound. For example, the previously published general upper bound allows \(r+2\) blocks on \(K_{2,\ldots,2}\) with \(r\) parts, whereas the present result gives exactly four for every \(r\ge2\). Counting and domination variants based on different forms of locating sets do not by themselves compare coalition partitions.

## Limitations

No claim is made about graphs that are not complete multipartite, or about the number of different optimal partitions. The small cases mentioned above were covered previously. The proof is a self-contained mathematical argument supported by finite checks, but no independent audit has been performed. A differently indexed equivalent theorem could affect publication priority.

## References

1. M. Chellali, A. A. Dobrynin, F. Foucaud, H. Golmohammadi, and J. C. Valenzuela-Tripodoro, *Locating-dominating coalitions in graphs*, arXiv:2602.18760, first submitted 2026-02-21. https://arxiv.org/html/2602.18760v2
2. T. W. Haynes et al., *Introduction to coalitions in graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 653–659, for the earlier ordinary-coalition notion; see the bibliography of reference 1.
