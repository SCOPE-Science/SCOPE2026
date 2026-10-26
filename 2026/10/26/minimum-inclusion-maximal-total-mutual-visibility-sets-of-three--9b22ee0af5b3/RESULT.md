# Minimum inclusion-maximal total mutual-visibility sets of three-factor Hamming graphs

## Finding
For every \(a,b,c\ge2\), let \(G=K_a\square K_b\square K_c\) and \(m=\min\{a,b,c\}\). The lower total mutual-visibility number of \(G\), meaning the smallest size of an inclusion-maximal total mutual-visibility set, equals \(m\). More strongly, all sets of that size are classified below and their complete multiplicity is
\[
N(a,b,c)=\sum_{i:q_i=m}\sum_{r=1}^{\lfloor m/2\rfloor} S_{\ge2}(m,r)(q_j)_{\downarrow r}(q_k)_{\downarrow r}+\mathbf1_{\{a=b=c=m\}}(m!)^2,
\]
where \(\{i,j,k\}=\{1,2,3\}\), \((q_1,q_2,q_3)=(a,b,c)\), \((q)_{\downarrow r}=q(q-1)\cdots(q-r+1)\), and \(S_{\ge2}(m,r)\) counts partitions of a labeled \(m\)-set into \(r\) unlabeled blocks each of size at least two.

## Assumptions and scope
All graphs are finite, simple, undirected. A set \(X\subseteq V(G)\) is a total mutual-visibility set when for every pair of vertices \(u,v\) of \(G\) there is a shortest \(u\)-to-\(v\) path whose internal vertices avoid \(X\). Inclusion-maximal means no strict superset is total mutual-visible. For products of three nontrivial cliques, the established Hamming-graph criterion is that \(X\) is total mutual-visible precisely when no two distinct members have Hamming distance two. Consequently, an inclusion-maximal set is exactly an independent dominating set in the graph whose edges join pairs at Hamming distance two. No product with more than three factors is claimed.

## Proof
**The lower bound.** Suppose \(|X|<m\). In every coordinate, some symbol is absent from all vertices of \(X\). The triple of three absent symbols differs in all three coordinates from every member of \(X\), so it can be added without introducing a forbidden distance-two pair. Thus \(X\) is not inclusion-maximal.

**A sharp example.** Fix two coordinates and take the full coordinate line in the remaining coordinate having \(m\) possible symbols. Its members are mutually at Hamming distance one. For an omitted triple, if both fixed coordinates differ, its first coordinate can be matched by a line vertex to make distance two; if exactly one fixed coordinate differs, choose a line vertex with a different varying coordinate (possible as \(m\ge2\)). These observations also prove maximality. The minimum is therefore \(m\).

**Exhaustion of minimum sets.** Fix an inclusion-maximal set \(X\) of size \(m\). If every coordinate projection omitted a symbol, the triple of omitted symbols could be added. Therefore some projection is surjective. Since \(|X|=m\), that axis has exactly \(m\) symbols, and each selected triple has a different coordinate there. Index selected triples by their value on that axis. Any two selected triples already differ on that axis. Their Hamming distance cannot equal two, so their two other coordinates are either simultaneously equal or simultaneously different. Consequently the equality partitions of the indexed vertices in the two remaining coordinate projections coincide. Let this common partition have \(r\) blocks. Distinct blocks receive distinct symbols in each of the two coordinates.

If the partition has a singleton block at index \(t\) and there is a symbol unused by one of the other coordinate projections, replace that coordinate of the selected triple at index \(t\) with the unused symbol. The new vertex differs in one coordinate from its indexed selected triple and in all three coordinates from every other selected triple; thus it could be added, contrary to maximality. Hence a singleton forces both other projections to use every available symbol: \(q_j=q_k=r\). Since \(r\le m\le q_j,q_k\), equality throughout gives \(r=m=q_j=q_k\), so all partition blocks are singletons and all three coordinates have size \(m\). This is exactly the exceptional full-transversal family.

Otherwise each block has size at least two. Conversely, given any such common partition and two injections of the blocks into the other coordinate alphabets, the resulting \(m\) triples have pairwise distance either one (same block) or three (different blocks), so form a total mutual-visibility set. To prove maximality, take an omitted triple and index the unique selected triple with its first coordinate. If both other coordinates differ from this selected triple, their distance is two. If exactly one differs, use a distinct index in the same block: there the first coordinate and precisely one other coordinate differ. If neither differs, the vertex is already selected. This exhausts all cases.

Finally, in the exceptional all-singleton case, all three coordinate projections are bijections. For any omitted vertex, index the selected triple matching its first coordinate. If both other coordinates differ, the distance is two; if exactly one differs, index the selected triple matching the mismatched coordinate and obtain distance two. Hence every such transversal is maximal.

**Counting without duplicates.** For each axis with \(m\) symbols, choose a partition into \(r\) nonsingleton blocks and independently injectively label these blocks with the other two coordinate alphabets. This produces \(S_{\ge2}(m,r)(q_j)_{\downarrow r}(q_k)_{\downarrow r}\) sets. Such sets have exactly one surjective coordinate projection, because \(r\le m/2<m\le q_j,q_k\); thus axis choices never double count. Exceptional full transversals require \(a=b=c=m\), are bijective on all three axes, do not overlap the first family, and number \((m!)^2\), after indexing by their first coordinate. The stated formula follows.

## Verification
The standalone `verify.py` enumerates all \(m\)-vertex subsets on six small products, checks the distance-two condition and its maximality directly, and compares the exact counts to the finite partition formula. It also checks the total mutual-visibility interpretation independently against the original shortest-path definition on the eight-vertex binary cube. Recorded checks, parameters, counts, and limits are in `verification_output.txt`. Finite checks supplement, not replace, the universal proof above.

## Relationship to prior work
Brešar and Yero introduced the lower (total) mutual-visibility parameters and determined the two-factor complete-graph Cartesian-product lower parameter. Bujtás, Klavžar and Tian gave the decisive no-distance-two criterion in Hamming graphs and treated the maximum total mutual-visibility parameter. These ingredients are prior results, not discoveries of this note. The present contribution is the classification and exact multiplicity of all **minimum inclusion-maximal** total mutual-visibility sets for arbitrary three-factor Hamming graphs, including the nonsingleton-block versus square-transversal dichotomy. Published lower results for a binary factor are subsumed by the minimum-value statement here, but do not give this full multiplicity classification.

## Limitations
No novelty guarantee against unindexed equivalent literature is asserted. The classification is limited to three factors with each factor size at least two and counts only minimum-size inclusion-maximal sets, not all maximal sets. All statements are self-reviewed but not independently audited. The computer checks are finite, whereas the proof is for all stated orders.

## References
1. B. Brešar and I. G. Yero, *Lower (total) mutual-visibility in graphs*, arXiv:2307.02951, first public 6 July 2023; original parameter and two-factor results.
2. C. Bujtás, S. Klavžar and Y. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168, first public 11 July 2023; Hamming distance-two characterization, Theorem 6.
