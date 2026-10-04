# Oriented-tree general position as a Greene–Kleitman two-family
## Finding
For every finite oriented tree \(\vec T\), if \(P_{\vec T}\) is the reachability poset and \(a_2(P_{\vec T})\) is the maximum size of a subset containing no chain of three elements, then \(\operatorname{gp}(\vec T)=a_2(P_{\vec T})=\min_{\Pi}\sum_{C\in\Pi}\min\{2,|C|\}\), where \(\Pi\) ranges over all partitions of \(P_{\vec T}\) into chains.

Thus the directed general-position problem for an arbitrary orientation of a tree is exactly the maximum two-family problem in its reachability poset. The final equality is the Greene–Kleitman min–max theorem at \(k=2\).

## Assumptions and scope
An oriented tree \(\vec T\) is an orientation of a finite simple undirected tree. A directed geodesic is a shortest directed path between its ordered endpoints. A vertex set is in general position when no directed geodesic contains three of its vertices. Define the reachability order \(u\leq v\) when \(u=v\) or there is a directed path from \(u\) to \(v\). Because an oriented tree is acyclic, this is a partial order \(P_{\vec T}\).

A two-family in a finite poset is a subset containing no chain of three elements. Equivalently, by the standard dual form of Dilworth/Mirsky theory, it is a union of at most two antichains. The quantity \(a_2(P)\) denotes the largest cardinality of such a subset.

## Proof
Let \(S\subseteq V(\vec T)\). We first prove that \(S\) is in directed general position if and only if \(S\) contains no three-element chain in \(P_{\vec T}\).

Suppose \(x<y<z\) are three vertices of \(S\). There is a directed path from \(x\) to \(y\) and a directed path from \(y\) to \(z\). Their concatenation is the unique underlying \(x\)-to-\(z\) tree path, oriented consistently from \(x\) to \(z\). A tree has no alternative \(x\)-to-\(z\) path, so this directed path is necessarily a geodesic. It contains \(x,y,z\), and hence \(S\) is not in general position.

Conversely, suppose \(S\) is not in general position. Some directed geodesic contains three distinct vertices of \(S\). Reading those three vertices in their order along the directed path gives \(x<y<z\) in the reachability order. Therefore \(S\) contains a three-element chain.

Hence the general-position sets of \(\vec T\) are exactly the two-families of \(P_{\vec T}\), so
\[
\operatorname{{gp}}(\vec T)=a_2(P_{{\vec T}}).
\]

Greene and Kleitman's theorem states that, for a finite poset \(P\), the maximum cardinality of a union of \(k\) antichains equals
\[
\min_{{\Pi}}\sum_{{C\in\Pi}}\min\{{k,|C|\}},
\]
where \(\Pi\) ranges over all chain partitions of \(P\). Applying the theorem with \(k=2\) completes the proof.

## Verification
The accompanying deterministic verifier independently computes the three quantities in the displayed claim for every labeled oriented tree on at most six vertices. It enumerates all Prüfer-coded labeled trees and every orientation; for each case it (i) tests general-position subsets directly from directed tree geodesics, (ii) tests two-families from the reachability relation, and (iii) enumerates all set partitions and minimizes the Greene–Kleitman chain-partition objective. The replay covers \(43{,}615\) oriented labeled trees and requires equality of all three values in every case.

This finite replay is a stress test only. The theorem itself is proved for every finite oriented tree by the argument above and the classical Greene–Kleitman theorem.

## Relationship to prior work
Chandran S. V. et al. introduced and studied the general-position number of digraphs in arXiv:2604.15909 (first posted 17 April 2026). Their tree section gives a leaf lower bound and an exact formula for out-arborescences, while their Problem 5.2 asks for a formula for the general-position number of an arbitrary oriented tree. Full-text inspection of that preprint found no use of antichains, reachability posets, chain partitions, or the Greene–Kleitman theorem.

Greene and Kleitman's 1976 theorem supplies the poset min–max equality once the directed-geodesic condition on an oriented tree is identified with exclusion of a three-element reachability chain. Cameron's 1986 acyclic-digraph extension gives a related dipath-partition min–max theorem; applied to a transitive closure it recovers the same order-theoretic machinery, but it likewise does not identify oriented-tree general-position sets with two-families. These results are therefore supporting machinery rather than prior statements of the target directed-general-position formula.

## Limitations
The formula is a structural min–max characterization in terms of the reachability poset; it is not a closed expression in elementary statistics such as the number of leaves or the in/out-degree sequence. The proof relies on the tree property: in a general acyclic digraph, comparability of three selected vertices does not by itself force the corresponding directed path to be geodesic because shortcuts may exist. The literature search cannot exclude an unindexed or very recent independent observation of the same reachability-poset reduction.

## References
1. U. Chandran S. V., G. Di Stefano, G. Erskine, H. S, E. J. Thomas, J. Tuite, *The general position number of digraphs*, arXiv:2604.15909, first posted 17 April 2026.
2. C. Greene, D. J. Kleitman, *The Structure of Sperner k-families*, Journal of Combinatorial Theory, Series A 20 (1976), 41–68, DOI 10.1016/0097-3165(76)90077-7.
3. K. Cameron, *On k-Optimum Dipath Partitions and Partial k-Colourings of Acyclic Digraphs*, European Journal of Combinatorics 7 (1986), 115–118, DOI 10.1016/S0195-6698(86)80036-1.
