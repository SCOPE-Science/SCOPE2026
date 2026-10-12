# Complete maximum total-coalition partitions of crown graphs

## Finding

For every integer \(n\ge5\), let \(H_n=K_{n,n}-M\) be the crown graph, with two labeled independent sets \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_j\) is an edge precisely when \(i\ne j\). Let a *total-coalition partition* mean a partition \(\mathcal P\) into nonempty blocks, none of which is a total dominating set, such that every block has some other block whose union with it is a total dominating set.

**Extremizer classification.** All maximum total-coalition partitions, and no others, comprise two triple blocks \(U,V\) with
\[
(|U\cap A|,|U\cap B|)=(2,1),\qquad (|V\cap A|,|V\cap B|)=(1,2),
\]
and singleton blocks for every remaining vertex. In particular, the total-coalition number is \(TC(H_n)=2n-4\) (a previously implied scalar value), and the **new complete extremizer count** is
\[
N_n=\binom n2\,n(n-2)\binom{n-1}{2}.
\]
For each such partition the total-coalition graph is uniquely, up to graph isomorphism, the double star whose two adjacent central vertices each have \(n-3\) pendant neighbors.

## Assumptions and scope

All graphs are finite, simple, and have open-neighborhood total domination; every vertex, including a selected one, must have a neighbor in the chosen set. The parameter is ordinary *total coalition*, not ordinary (closed-neighborhood) coalition, double coalition, or total restrained coalition. The perfect matching \(M\) deletes the \(n\) edges \(a_i b_i\) from \(K_{n,n}\). Unordered partitions are counted on the fixed labeled vertex set. The assertion concerns precisely \(n\ge5\); smaller orders can have different equality cases. No claim is made about arbitrary bipartite graphs or minimum partitions.

For a block \(X\), write \(a(X)=|X\cap A|\), \(b(X)=|X\cap B|\), and \(c(X)=|X|-1\), its partition deficit. For any partition \(\mathcal P\), its total deficit is
\[
s=\sum_{X\in\mathcal P}c(X)=2n-|\mathcal P|.
\]

## Proof

**Step 1 (total domination as two occupancy inequalities).** For every \(n\ge3\), a vertex set \(D\) totally dominates \(H_n\) if and only if \(a(D)\ge2\) and \(b(D)\ge2\). Indeed, if \(D\) has no vertices in \(A\), no vertex in \(B\) has a neighbor in \(D\); if \(D\) contains exactly one \(a_i\), then \(b_i\) has no neighbor in \(D\). The opposite side is symmetric. Conversely two distinct chosen vertices in either side ensure that every vertex of the other side is adjacent to at least one of them, regardless of the deleted matching. Consequently, a block is not total dominating exactly when at least one of its two occupancies is at most one, and two blocks form a total coalition precisely when their sums satisfy both occupancy inequalities.

**Step 2 (singleton-forcing deficit lemma).** Suppose a total-coalition partition \(\mathcal P\) has deficit \(s\le4\). A block of size \(m\ge2\) contains at most \(2(m-1)\) vertices, so the total number of vertices in nonsingleton blocks is at most \(2s\le8\). Since \(2n\ge10\), at least one singleton block exists. We prove that there must be a singleton in *each* side.

Assume, for contradiction, that there is no singleton from \(A\); at least one singleton \(\{b_j\}\) then exists. Its coalition partner \(W\) must have \(a(W)\ge2\) and \(b(W)\ge1\); since \(W\) itself is not total dominating, \(b(W)=1\). Hence \(c(W)\ge2\).

If every block containing an \(A\)-vertex were mixed (met both sides), then for each such block \(X\), \(c(X)=a(X)+b(X)-1\ge a(X)\), giving \(n\le\sum_X c(X)=s\le4\), a contradiction. Thus an \(A\)-only nonsingleton block \(Q\) exists. Since \(Q\) is not a singleton, \(a(Q)\ge2\); to form a coalition it needs a partner \(R\) having \(b(R)\ge2\). The three blocks \(Q,R,W\) are distinct because \(b(Q)=0\), \(b(W)=1\), and \(b(R)\ge2\). Their deficits are at least \(1,1,2\), respectively. Since the total deficit is at most four, equality must hold throughout: \(Q\) has two \(A\)-vertices, \(R\) has two \(B\)-vertices, \(W\) has two \(A\)-vertices and one \(B\)-vertex, and every remaining block is a singleton. That leaves at most four \(A\)-vertices in nonsingleton blocks, contradicting the absence of \(A\)-singletons for \(n\ge5\). Therefore an \(A\)-singleton exists. Exchanging the two sides yields a \(B\)-singleton.

**Step 3 (all equality cases).** Let \(\{a_i\}\) be an \(A\)-singleton. Its coalition partner \(V\) must have \(a(V)\ge1\) and \(b(V)\ge2\). Since \(V\) is not total dominating, necessarily \(a(V)=1\), and \(c(V)\ge2\). Likewise a \(B\)-singleton needs a partner \(U\) of occupancy \(a(U)\ge2\) and \(b(U)=1\), hence \(c(U)\ge2\). These partners are distinct. Consequently \(s\ge c(U)+c(V)\ge4\), proving that no partition can have more than \(2n-4\) blocks. If \(s=4\), then \(c(U)=c(V)=2\) and all other blocks are singletons, yielding precisely \((a(U),b(U))=(2,1)\) and \((a(V),b(V))=(1,2)\).

Conversely, choose any disjoint triple blocks of these two profiles and leave all other vertices as singletons. No block is total dominating. Their union is total dominating, each remaining \(A\)-singleton forms a coalition with \(V\), and each remaining \(B\)-singleton forms a coalition with \(U\). Hence every partition of the stated form is valid and maximum.

**Step 4 (exact count and coalition graph).** Choose the two \(A\)-vertices and one \(B\)-vertex of \(U\) in \(\binom n2\,n\) ways, then the \(A\)-vertex and two \(B\)-vertices of \(V\) in \((n-2)\binom{n-1}{2}\) ways. Since the profiles distinguish \(U\) and \(V\), there is no extra symmetry divisor. The remaining singleton blocks are forced, proving the displayed count. The only partnerships are the edge \(UV\), the \(n-3\) edges from \(U\) to the singleton blocks from \(B\), and the \(n-3\) edges from \(V\) to the singleton blocks from \(A\). Thus the coalition graph is the claimed double star.

## Verification

A reproducible Python 3 standard-library checker is supplied in `verify_total_coalition_crowns.py`, with its direct output in `verify_total_coalition_crowns_output.txt`. It independently compares the side-occupancy total-domination criterion to actual graph adjacency for all \(21,824\) subsets of \(H_n\), \(3\le n\le7\). It enumerates all \(115,975\) unordered partitions of \(V(H_5)\), recovers maximum size six with exactly \(900\) maximum partitions, and separately exhausts the cardinality-\(2n-4\) slice at \(n=5,6,7\), testing \(22,827\), \(159,027\), and \(752,752\) partitions. The surviving cases number \(900\), \(3,600\), and \(11,025\), all have the theorem's shape and total-coalition graph degree profile. Finite checks corroborate but do not establish the general theorem; Steps 1–4 provide the proof.

## Relationship to prior work

Alikhani, Bakhshesh and Golmohammadi introduced ordinary total-coalition partitions in their arXiv preprint first public on 21 November 2022 [1]. Barát and Blázsik [2] studied general upper bounds and optimal total-coalition graphs, but their sharp-bound equality hypotheses do not apply to these crown graphs.

**Crucial non-novelty distinction.** For \(n\ge3\), the total-dominating subsets of \(H_n\) are *exactly* the total \(2\)-dominating subsets of \(K_{n,n}\), so the *entire total-coalition feasibility predicate* agrees with the total \(2\)-coalition predicate of that complete bipartite graph. Golmohammadi, Alikhani and Bakhshesh [3, Proposition 3.3] had already established the scalar value \(2n-4\) for the complete-bipartite double-total-coalition parameter, and Brešar, Henning and Samadi [5, Theorem 5.3] independently treat general total \(k\)-coalition numbers and recover the same scalar. Their proof gives an extremal construction of two mixed triple blocks. These sources were examined for statement-level implication: neither states or counts **all** extremal partitions, nor determines their coalition graph for this family. The contribution here is precisely that complete, rigid structural and numerical classification, not the scalar value or example construction. Brešar, Klavžar and Samadi [4] introduce additional total \(k\)-coalition bounds without this classification.

## Limitations

The theorem concerns fixed labeled crown graphs with \(n\ge5\), not all graphs and not all bipartite graphs. It has not undergone an independent mathematical audit. The highly relevant 2024 preprint and 2025 complete-bipartite total \(k\)-coalition paper already cover the scalar and provide the same extremal construction; only the uniqueness, exact number, and coalition-graph classification are presented as new. Other nonindexed literature could in principle contain equivalent statements. Small-order enumeration is not a substitute for the symbolic argument.

## References

1. S. Alikhani, D. Bakhshesh and H. Golmohammadi, *Introduction to total coalitions in graphs*, arXiv:2211.11590, first public 2022-11-21, https://arxiv.org/html/2211.11590v2.
2. J. Barát and Z. L. Blázsik, *General sharp upper bounds on the total coalition number*, arXiv:2301.09979, first public 2023-01-24, https://arxiv.org/html/2301.09979v3.
3. H. Golmohammadi, S. Alikhani and D. Bakhshesh, *Double total coalitions in graphs*, public preprint 2024-12-24, especially Proposition 3.3, https://www.researchgate.net/publication/387352932_Double_total_coalitions_in_graphs.
4. B. Brešar, S. Klavžar and B. Samadi, *Total \(k\)-coalition: bounds, exact values and an application to double coalition*, arXiv:2502.07310, first public 2025-02-11, https://arxiv.org/html/2502.07310v3.
5. B. Brešar, M. A. Henning and B. Samadi, *On \(k\)-coalition in graphs: bounds and exact values*, arXiv:2507.18306, first public 2025-07-24, especially Theorem 5.3 and its proof, https://arxiv.org/html/2507.18306v1.
