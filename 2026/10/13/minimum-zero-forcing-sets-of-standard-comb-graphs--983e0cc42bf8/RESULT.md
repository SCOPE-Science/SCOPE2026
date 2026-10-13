# Minimum zero forcing sets of standard comb graphs
## Finding
Let \(C_n=P_n\circ K_1\) be the standard comb on \(2n\) vertices, with spine \(v_1,\ldots,v_n\) and pendant leaf \(u_i\) adjacent only to \(v_i\). For \(n\ge 2\), its zero forcing number is \(Z(C_n)=\lceil n/2\rceil\), and all minimum zero forcing sets admit the following exact classification.

If \(n=2m\), a minimum set contains only leaves and contains exactly one member of each pair
\[
\{u_1,u_2\},\{u_3,u_4\},\ldots,\{u_{2m-1},u_{2m}\}.
\]
Hence there are exactly \(2^m\) minimum zero forcing sets.

If \(n=2m+1\) with \(m\ge 1\), choose \(t\in\{0,\ldots,m\}\) and put \(q=2t+1\). Pair the indices on the two sides of \(q\) consecutively:
\[
\{1,2\},\ldots,\{2t-1,2t\},\qquad
\{2t+2,2t+3\},\ldots,\{2m,2m+1\}.
\]
A minimum zero forcing set is obtained by choosing one leaf from every displayed pair and then choosing either \(u_q\) or \(v_q\); every minimum zero forcing set arises in this way. The choices with \(v_q\) are all distinct and number \((m+1)2^m\). The distinct all-leaf choices number \((m+2)2^{m-1}\). Therefore
\[
\#\{S:|S|=Z(C_{2m+1}),\ S\text{ zero forcing}\}=(3m+4)2^{m-1}.
\]
The scalar equality for \(Z(C_n)\) is a consequence of the classical tree path-cover theorem and is not the novelty claim; the contribution here is the complete minimum-set classification and its parity-sensitive exact count.

## Assumptions and scope
Graphs are finite, simple, and undirected, and zero forcing uses the standard color-change rule: a blue vertex with exactly one white neighbor forces that neighbor blue. The name “standard comb” is fixed here to mean the corona \(P_n\circ K_1\), not the broader class of maximum-degree-three trees whose degree-three vertices lie on one path. The result concerns minimum zero forcing sets only, not all zero forcing sets and not the \(q\)-analogue, positive-semidefinite, skew, or directed variants.

## Proof
A forcing process decomposes into vertex-disjoint forcing chains. Each chain is a path, each initial blue vertex is one endpoint of exactly one chain, and the chains cover all vertices. Thus a zero forcing set of size \(k\) induces a path cover by \(k\) paths. Conversely, for a tree, the classical path-cover theorem states that selecting one endpoint from every path of a minimum path cover gives a zero forcing set.

The comb \(C_n\) has \(n\) pendant leaves. A path contains at most two leaves, so every path cover has at least \(\lceil n/2\rceil\) paths. Consecutively pairing leaves along the spine, with one remaining leaf-spine edge when \(n\) is odd, gives a path cover with exactly \(\lceil n/2\rceil\) paths. Hence \(Z(C_n)=\lceil n/2\rceil\).

Suppose first that \(n=2m\). In a minimum forcing-chain cover there are \(m\) paths and \(2m\) leaves, so every chain contains exactly two leaves. Hence every initial endpoint is a leaf. If one chain joined \(u_i\) to \(u_j\) with \(j\ge i+2\), then the unique path between them contains \(v_{i+1}\), while the pendant leaf \(u_{i+1}\) cannot belong to that chain. Since its only neighbor is already used by the chain, \(u_{i+1}\) would have to be a one-leaf singleton path, contradicting the fact that every chain has two leaves. Therefore every two-leaf chain joins adjacent leaf indices. The only perfect pairing of the ordered indices by adjacent pairs is \(\{1,2\},\{3,4\},\ldots,\{2m-1,2m\}\). One endpoint of each chain is initially blue, giving exactly one selected leaf from each pair and exactly \(2^m\) possibilities.

Now let \(n=2m+1\). A minimum forcing-chain cover has \(m+1\) chains and \(2m+1\) leaves, so exactly one chain contains one leaf and every other chain contains two leaves.

If the minimum zero forcing set contains a spine vertex, then that spine vertex is the initial endpoint of the unique one-leaf chain. Any nonadjacent two-leaf chain would force an internal pendant leaf to be a second one-leaf chain, which is impossible. Thus all two-leaf chains join adjacent indices. The uncovered spine index is consequently odd, say \(q=2t+1\), the one-leaf chain is \(u_qv_q\), and the remaining indices are paired consecutively on both sides of \(q\). The initial spine endpoint must be \(v_q\), while each two-leaf chain contributes either of its two leaf endpoints. This gives \((m+1)2^m\) distinct sets.

If all initial vertices are leaves, the same leaf deficit shows that either all two-leaf chains are adjacent and the one-leaf chain is \(u_qv_q\) for an odd \(q\), or there is exactly one two-leaf chain joining \(u_i\) to \(u_{i+2}\); then \(u_{i+1}\) is the unique one-leaf singleton chain and every other two-leaf chain is adjacent. In the latter case the chosen endpoints are represented by the adjacent-pair construction with unmatched index \(q=i\) when \(u_i\) is chosen from the long chain, and with \(q=i+2\) when \(u_{i+2}\) is chosen. Hence the union of the displayed families is complete even though different odd \(q\) can represent the same all-leaf set.

It remains to count those distinct all-leaf sets. Let \(A_m\) denote their number on \(C_{2m+1}\). Encode such a set by a binary word \(x_1\cdots x_{2m+1}\), where \(x_i=1\) means \(u_i\) is selected. The prefix \(00\) is impossible. Prefixes \(10\) and \(01\) are each in bijection, after deleting their first two entries, with the valid all-leaf words for \(C_{2m-1}\). For prefix \(11\), the unmatched index must be \(q=1\), so \(x_3=0\) and exactly one leaf is chosen from each pair \(\{u_4,u_5\},\ldots,\{u_{2m},u_{2m+1}\}\); this gives \(2^{m-1}\) words. Therefore
\[
A_m=2A_{m-1}+2^{m-1},\qquad A_1=3,
\]
so \(A_m=(m+2)2^{m-1}\). Adding the spine-containing sets proves the stated odd-order count.

## Verification
The accompanying checker constructs \(C_n\), implements the standard zero forcing closure, enumerates every subset of size below \(\lceil n/2\rceil\) and every subset of size exactly \(\lceil n/2\rceil\) for \(2\le n\le 11\), and compares the brute-force minimum sets with the classification above. It also checks the closed counts. The replay result is:

`VERIFY_OK n_range=2..11 subset_checks=148899 classification_checks=573 count_checks=10 max_order=22`

The computation is a finite stress test, not the proof for arbitrary \(n\); the proof is the forcing-chain and path-cover argument above.

## Relationship to prior work
The foundational zero forcing paper introduced the standard rule and proves for every tree that zero forcing equals the minimum path-cover number. Its Proposition 4.2 explicitly constructs a zero forcing set by choosing one endpoint of each path in a minimum path cover. That theorem supplies the scalar framework used here, but it does not classify or count all distinct endpoint selections arising from overlapping minimum path covers of the standard comb.

Butler, Erickson, Fallat, Hall, Kroschel, Lin, Shader, Warnberg, and Yang study a \(q\)-analogue of zero forcing and define the broader comb class. Their comb result concerns the \(Z_1\)-game and pairs of initial vertices, not ordinary minimum zero forcing sets of \(P_n\circ K_1\). Becker, Cameron, Hanely, Ong, and Previte study minimal forts and use a comb graph in that different fort/maximal-failed-set context; their paper does not state this minimum-basis census.

## Limitations
The result is only for the standard comb \(P_n\circ K_1\). It does not enumerate nonminimum zero forcing sets or extend the formula to arbitrary generalized combs. The originality comparison found no exact prior minimum-basis census, but literature search cannot logically prove nonexistence of an obscure or unindexed equivalent result. The scalar zero forcing number is deliberately excluded from the novelty claim.

## References
1. AIM Minimum Rank – Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI 10.1016/j.laa.2007.10.009. Available online 26 November 2007.
2. S. Butler, C. Erickson, S. M. Fallat, H. T. Hall, B. Kroschel, J. C.-H. Lin, B. L. Shader, N. Warnberg, and B. Yang, “Properties of a \(q\)-analogue of zero forcing,” arXiv:1809.07640; *Graphs and Combinatorics* 36 (2020), 1401–1419.
3. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, “On the Number of Minimal Forts of a Graph,” arXiv:2404.05963; *Graphs and Combinatorics* 41 (2025), Article 25.
