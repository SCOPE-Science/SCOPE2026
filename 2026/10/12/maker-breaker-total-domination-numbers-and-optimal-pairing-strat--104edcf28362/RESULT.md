# Maker–Breaker total domination numbers and optimal pairing strategies of crown graphs
## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph for \(n\ge3\), with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the deleted perfect-matching edge. Then
\[
\gamma_t(\operatorname{Cr}_n)=4.
\]
For \(n=3\),
\[
\gamma_{\mathrm{MBT}}(\operatorname{Cr}_3)=\gamma^{\prime}_{\mathrm{MBT}}(\operatorname{Cr}_3)=\infty.
\]
For every \(n\ge4\),
\[
\gamma_{\mathrm{MBT}}(\operatorname{Cr}_n)=\gamma^{\prime}_{\mathrm{MBT}}(\operatorname{Cr}_n)=4.
\]
Moreover, every minimum pairing total dominating set consists of four disjoint vertex-pairs, exactly two contained in \(A\) and exactly two contained in \(B\). Conversely every such choice is a pairing total dominating set. Hence the number of minimum four-pair systems is
\[
\left(3\binom{n}{4}\right)^2.
\]

## Assumptions and scope
A total dominating set is a vertex set \(D\) such that every vertex, including every vertex of \(D\), has a neighbor in \(D\). In the Maker–Breaker total domination game, Dominator and Staller alternately claim unclaimed vertices; Dominator wins when his claimed vertices contain a total dominating set. The D-game has Dominator first, while the S-game has Staller first. The parameters \(\gamma_{\mathrm{MBT}}\) and \(\gamma^{\prime}_{\mathrm{MBT}}\) are the minimum numbers of Dominator moves needed to force a win in those games, with value \(\infty\) when no winning strategy exists. A pairing total dominating set is a family of pairwise vertex-disjoint pairs such that every transversal choosing one vertex from each pair is a total dominating set.

## Proof
First characterize minimum total dominating sets. To dominate every vertex of \(B\), the set \(D\cap A\) must contain at least two vertices: a singleton \(\{a_i\}\) misses \(b_i\). Symmetrically \(|D\cap B|\ge2\). Thus \(|D|\ge4\). Conversely, any two distinct vertices of \(A\) together with any two distinct vertices of \(B\) totally dominate the crown, because each vertex has at most one nonneighbor on the opposite shore. Therefore \(\gamma_t(\operatorname{Cr}_n)=4\), and the minimum total dominating sets are exactly the \(2+2\) shore selections.

When \(n=3\), the graph has six vertices. In either starting convention Dominator can claim at most three vertices before the board is exhausted. Since a total dominating set needs four vertices, Dominator cannot win, and both Maker–Breaker total domination numbers are infinite.

Now let \(n\ge4\). Choose four distinct vertices of \(A\) and partition them into two pairs; independently choose four distinct vertices of \(B\) and partition them into two pairs. Every transversal of these four pairs contains exactly two vertices from each shore, hence is a total dominating set. This gives a four-pair pairing total dominating set. Dominator follows the standard pairing response: after Staller takes a vertex of an as-yet-unrepresented pair, Dominator takes its mate; otherwise Dominator takes any vertex from a fresh pair. After four Dominator moves he has one vertex from each pair, in either the D-game or the S-game. Thus both game numbers are at most four. The general lower bound \(\gamma_t(G)\le\gamma_{\mathrm{MBT}}(G)\le\gamma^{\prime}_{\mathrm{MBT}}(G)\), together with \(\gamma_t(\operatorname{Cr}_n)=4\), forces equality.

It remains to classify minimum pairing systems. Let four disjoint pairs have the property that every transversal is total dominating. Every transversal has four vertices and therefore, by the characterization above, exactly two vertices in each shore. If one of the four pairs were a cross-pair with one endpoint in each shore, changing only the choice in that pair would change the number of selected \(A\)-vertices by one, contradicting the requirement that every transversal have exactly two. Hence all pairs lie within shores. If \(x\) pairs lie in \(A\), every transversal has exactly \(x\) vertices in \(A\), so \(x=2\), and the other two pairs lie in \(B\). Conversely this form works by the earlier transversal argument. The number of two-edge matchings on an \(n\)-element shore is \(3\binom{n}{4}\), so independence of the two shores gives the stated square.

## Verification
The accompanying checker reconstructs crown adjacency from the definition. It exhaustively verifies \(\gamma_t=4\) and the count of minimum total dominating sets through \(n=7\), solves both finite games by minimax for \(n=3,4,5\), and enumerates every four-pair system for \(n=4,5,6\), confirming both the classification and the closed count. These finite checks corroborate the proof; the theorem for arbitrary \(n\) rests on the analytic arguments above.

## Relationship to prior work
Divakaran, James, Klavžar, and Nair introduced the quantitative Maker–Breaker total domination numbers in 2025 and defined pairing total dominating sets. They proved the general inequalities used above and explicitly used a pairing total dominating set to obtain a sharp Staller-start value. Their inspected preprint contains no occurrence of “crown”; its mention of complete bipartite graphs concerns earlier ordinary Maker–Breaker domination work rather than an exact total-domination result for crowns.

Gledel, Henning, Iršič, and Klavžar introduced the underlying Maker–Breaker total domination game in 2019. Their work treats basic game properties, grids, cacti, cubic examples, and complexity on bipartite graphs. The inspected full text contains no occurrence of “crown”, “complete bipartite”, or “perfect matching”. The present result instead gives both quantitative game numbers on the entire crown family and classifies and counts all minimum pairing certificates.

## Limitations
The theorem is restricted to crown graphs and does not classify Maker–Breaker total domination numbers for arbitrary matching-deleted complete bipartite graphs \(K_{r,s}-M_t\). The literature comparison cannot exclude a poorly indexed older equivalent statement phrased under an alias such as the bipartite complement of a one-factor. The computational checks are finite corroboration only and are not used as an infinite proof.

## References
1. A. Divakaran, T. James, S. Klavžar, and L. S. Nair, “Maker-Breaker total domination number,” arXiv:2507.17341v1, first public 2025-07-23.
2. V. Gledel, M. A. Henning, V. Iršič, and S. Klavžar, “Maker-Breaker total domination game,” arXiv:1902.00204v1, first public 2019-02-01.
