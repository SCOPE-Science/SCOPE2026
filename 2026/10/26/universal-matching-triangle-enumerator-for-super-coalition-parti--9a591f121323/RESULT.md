# Universal matching–triangle enumerator for super-coalition partitions at deficiency two

## Finding
Let \(G\) be any finite simple graph on \(N\ge 7\) vertices, with no isolated vertices, whose super-domination number satisfies \(\gamma_{\mathrm{sp}}(G)\ge N-2\). A set \(D\subseteq V(G)\) is *super dominating* when, for each \(u\in V(G)\setminus D\), some \(w\in D\) has \(N_G(w)\cap(V(G)\setminus D)=\{u\}\). A *super-coalition partition* is an unordered partition of \(V(G)\) into nonempty blocks such that no block is super dominating but every block can be united with a different block to form a super dominating set.

Define the *admissible-pair graph* \(H=H(G)\) on \(V(G)\) by making \(uv\) an edge precisely when \(V(G)\setminus\{u,v\}\) is super dominating. Write \(e=|E(H)|\), \(m_2\) for the number of unordered pairs of vertex-disjoint edges of \(H\), and \(t\) for the number of triangles in \(H\). If \(c_k(G)\) counts super-coalition partitions having exactly \(k\) blocks, then the **complete partition enumerator** is

\[
\boxed{\sum_{k\ge 2}c_k(G)z^k
=\bigl(2^{N-1}-1-N-e\bigr)z^2
+\bigl(\binom N2+(N-3)e+m_2\bigr)z^3+t z^4.}
\]

Every super-coalition partition has at most four blocks, and \(c_3(G)>0\). Therefore its super-coalition number equals four if and only if \(H(G)\) contains a triangle, and equals three otherwise.

For the complete multipartite graph \(K_{a_1,\ldots,a_r}\) with \(r\ge2\), \(a_i\ge1\), and \(N=\sum_i a_i\ge7\), the hypotheses always hold. Its admissible-pair graph consists of a complete multipartite graph on the vertices belonging to parts of size at least two, together with isolated vertices from singleton parts. With \(Q=\sum_{a_i\ge2}a_i\), all coefficients are explicit:

\[
\begin{aligned}
e&=\sum_{i<j\,:\,a_i,a_j\ge2}a_ia_j,\\
m_2&=\binom e2-\sum_{i\,:\,a_i\ge2}a_i\binom{Q-a_i}{2},\\
t&=\sum_{i<j<k\,:\,a_i,a_j,a_k\ge2}a_i a_j a_k.
\end{aligned}
\]

Thus a complete multipartite graph of order at least seven has super-coalition number four **exactly when at least three of its parts have size at least two**; otherwise its number is three.

## Assumptions and scope
All graphs are finite, undirected, and simple; all partitions have unlabeled, nonempty blocks. The parameter \(\gamma_{\mathrm{sp}}(G)\) is the minimum super-dominating-set cardinality. The main theorem assumes \(N\ge7\), no isolated vertices, and \(\gamma_{\mathrm{sp}}(G)\ge N-2\); it does not assume connectivity or multipartiteness. The polynomial counts partitions, **not** pairs of coalition partners, assignments of partners, or graph-automorphism orbits. The auxiliary graph \(H(G)\) is determined by which two-vertex deletions leave super dominating sets, not by ordinary adjacency in \(G\).

## Proof
**Step 1: All possible super-dominating sets.** Since \(G\) has no isolated vertices, \(V(G)\setminus\{u\}\) is super dominating for every vertex \(u\): any neighbor of \(u\) witnesses its unique omission. By the hypothesis on \(\gamma_{\mathrm{sp}}\), no set omitting at least three vertices is super dominating. By definition of \(H\), the sets that omit exactly two vertices are super dominating precisely when their omitted pair is an edge of \(H\). The whole vertex set is super dominating vacuously. Consequently, a proper set is super dominating if and only if its complement is a singleton or an edge of \(H\).

**Step 2: At most four blocks.** For two disjoint blocks to form a coalition, their union must omit at most two vertices. In a partition with \(k\) blocks, their union omits at least \(k-2\) vertices. Therefore \(k\le4\). One-block partitions are disallowed because the sole block is super dominating.

**Step 3: Two blocks.** There are \(2^{N-1}-1\) unordered bipartitions into nonempty blocks. Since \(N\ge7\), both blocks cannot be super dominating: two super dominating sets would each contain at least \(N-2\) vertices, contradicting disjointness. Exactly \(N+e\) proper subsets are super dominating: \(N\) one-vertex complements and \(e\) admissible-pair complements. Their associated bipartitions are all distinct. Every remaining bipartition is a super-coalition partition because its two blocks unite to the whole vertex set. Hence \(c_2=2^{N-1}-1-N-e\).

**Step 4: Three blocks.** Suppose \(\{A,B,C\}\) is a super-coalition partition. At least two blocks have size at most two: if just one did, it could not form a coalition with either of the two larger blocks, because the third block would have more than two vertices. Choose the two small blocks as \(B,C\); then \(|A|\ge N-4\ge3\). Thus \(B\cup C\) is not super dominating, and the only possible partner for each of \(B,C\) is \(A\). It follows that \(B\) and \(C\) are each either singleton blocks or edges of \(H\), since their complements are the omissions of \(A\cup C\) and \(A\cup B\), respectively.

If \(|B|=|C|=1\), the big block \(A\) is not super dominating exactly when the two omitted singleton vertices form a nonedge of \(H\). There are \(\binom N2-e\) such partitions. If \(|B|=1\), \(|C|=2\), then \(C\) must be an edge of \(H\) and \(B\) an arbitrary vertex outside it: \((N-2)e\) partitions. If both sizes are two, they must be disjoint edges of \(H\), giving \(m_2\) unordered choices. Conversely, every partition in these three classes satisfies the required partner conditions and has no super dominating block: the big block omits at least two vertices and, in the two-singleton case, an inadmissible pair; the small blocks omit at least \(N-2\ge5\) vertices. Since \(N\ge7\), the big block has size at least three, so these cases are disjoint and exhaust all valid partitions. Thus \(c_3=(\binom N2-e)+(N-2)e+m_2=\binom N2+(N-3)e+m_2\). This is positive: if \(H\) is not complete then the first summand is positive, while if it is complete the last summand is positive.

**Step 5: Four blocks.** Every coalition-pair union must leave exactly two singleton blocks, and those two omitted vertices must form an edge of \(H\). A four-block partition with at most two singletons would leave every singleton without a coalition partner, hence is impossible. As \(N\ge7\), every viable four-block partition consequently has a unique large block \(A\) and three singleton blocks \(\{u\},\{v\},\{w\}\). Each singleton must partner \(A\). The three required complements are \(\{v,w\},\{u,w\},\{u,v\}\), which must all be edges of \(H\). Conversely, every triangle \(\{u,v,w\}\) in \(H\) gives exactly one such partition. Its large block omits three vertices and hence is not super dominating, nor are the singleton blocks. Therefore \(c_4=t\).

**Step 6: Complete multipartite application.** In \(G=K_{a_1,\ldots,a_r}\), consider an omitted set \(U\). If \(|U|\ge3\), no omitted vertex can have a selected witness adjacent to it and to no other member of \(U\): such a witness would require all other omitted vertices to lie in a single part, which cannot hold for every omitted vertex when \(|U|\ge3\). If \(|U|=2\), its vertices must be in different parts, and witnessing both requires a selected vertex remaining in each of those parts, so both part sizes must be at least two. Conversely, these conditions suffice, using the remaining selected vertices in the two parts as witnesses. Hence every complete multipartite graph has \(\gamma_{\mathrm{sp}}\ge N-2\), and \(H\) has exactly the claimed multipartite structure. An edge of \(H\) joins two vertices in different non-singleton parts. Counting such edges yields \(e\). A pair of distinct \(H\)-edges fails to be a matching exactly when the two share a unique vertex; summing \(\binom{\deg_H(v)}2\) gives the displayed \(m_2\). A triangle uses vertices from three distinct non-singleton parts, giving \(t\). The universal formula and the triangle criterion now apply.

## Verification
The included `verify.py` builds graph neighborhoods directly, checks super domination for every subset by its witness definition, and enumerates **all** unlabeled vertex partitions by restricted-growth recursion. It independently derives the admissible-pair graph from super-dominating status, counts its edges, two-matchings and triangles, and compares the exact partition counts to the formula. It checks every complete-multipartite integer-partition profile on seven, eight, and nine vertices (respectively 14, 21, and 29 profiles), five specified ten-vertex profiles, and 244 qualifying deterministic random graphs on seven or eight vertices. In each random instance it checks the hypotheses before invoking the comparison. All 313 applicable cases pass. The boundary control \(K_{3,3}\) has 16 two-block and 48 three-block super-coalition partitions, confirming that the seven-vertex restriction is substantive for the general formula. Run `python verify.py` in the directory containing this file and compare output to `verification.out`.

For a numerical example, \(K_{2,2,2,1}\) has \(N=7\), \(e=12\), \(m_2=30\), and \(t=8\). Its enumerator is \(44z^2+99z^3+8z^4\).

## Relationship to prior work
Alikhani and Ghanbari introduced super-coalition partitions and studied their number, general bounds, and selected graph classes in their 2026 preprint [1]. The present claim is the **complete enumerator** under the high super-domination hypothesis, and the universal reduction to a pair graph, two-edge matchings, and triangles. This is not just an upper bound on the number of parts. The paper's available abstract does not state this enumerator; the full text was not accessible for detailed comparison, so publication-priority uncertainty remains.

The foundational super-domination definition and parameter were treated by Klein, Rodríguez-Velázquez and Yi [2]. A published mathematical note [3] determines all super dominating sets in complete multipartite graphs, thereby already providing the admissible two-vertex deletion criterion for that special family. The multipartite corollary here **uses and independently rederives** that known criterion; its super-dominating-set characterization is not claimed to be new. The new general statement additionally counts full partitions for every graph satisfying the hypotheses, including nonmultipartite instances, and identifies the exact matching/triangle dependence. The accessible summary of [3] does not provide these partition counts. Relevant search limitations are recorded in `REVIEW.md` and `AUDIT.json`.

## Limitations
The theorem does not cover graphs with isolated vertices or graphs admitting super dominating sets omitting three or more vertices. It counts vertex partitions rather than partner assignments or automorphism classes. The threshold \(N\ge7\) is not cosmetic: at order six, partitions with three blocks of size two introduce terms absent from the universal stable formula (for example, \(K_{3,3}\) has \(c_3=48\), whereas naive substitution would give 60). Finite verification does not constitute an infinite proof. The primary 2026 preprint's full text was inaccessible through the available public retrieval routes; therefore a stronger or equivalent uninspected result remains possible. Independent mathematical audit has not been performed.

## References
1. S. Alikhani and N. Ghanbari, *Super Coalition Number in Graphs*, arXiv:2607.22686 (first publicly indexed 2026-07-15), https://arxiv.org/abs/2607.22686.
2. D. J. Klein, J. A. Rodríguez-Velázquez, and E. Yi, *On the super domination number of graphs* (2018 preprint; later journal publication), DOI:10.22049/CCO.2019.26587.1122.
3. *All super dominating sets of complete multipartite graphs*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-all-super-dominating-sets-of-complete-multipartite-graphs--315739371089.
