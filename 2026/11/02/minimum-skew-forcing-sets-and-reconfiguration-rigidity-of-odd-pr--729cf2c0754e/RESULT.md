# Minimum skew forcing sets and reconfiguration rigidity of odd prism graphs

## Finding

**Theorem.** For every odd integer \(n\ge5\), consider the prism \(Y_n=C_n\square K_2\). Its minimum skew zero forcing sets are precisely its unordered distance-two vertex pairs. There are exactly \(4n\) of them; the minimum skew forcing number is \(2\).

Write \(H_n\) for the distance-two graph of \(Y_n\): two distinct vertices are adjacent in \(H_n\) exactly when their shortest-path distance in \(Y_n\) is two. The token-exchange graph on minimum skew forcing sets is \(L(H_n)\), which is connected and \(6\)-regular on \(4n\) vertices, with \(12n\) edges. The token-sliding graph is
\[
\mathcal Z^{\mathrm{TS}}_-(Y_n)\cong
\begin{cases}
2C_5\sqcup10K_1,&n=5,\\
4nK_1,&n\ge7\text{ odd}.
\end{cases}
\]

In coordinates \((i,r)\in\mathbb Z_n\times\{0,1\}\), all minimum sets are the \(2n\) same-layer pairs \(\{(i,r),(i+2,r)\}\) and the \(2n\) cross-layer pairs \(\{(i,0),(i+1,1)\}\), \(\{(i,1),(i+1,0)\}\), with \(i\in\mathbb Z_n\). The cyclic indices in these expressions are understood modulo \(n\).

## Assumptions and scope

Graphs are finite, simple and undirected. Each vertex \((i,r)\) of \(Y_n\) has neighbors \((i-1,r)\), \((i+1,r)\), and \((i,1-r)\). Initially selected vertices are blue and the rest white. In *skew zero forcing*, a vertex of either color with exactly one white neighbor may force that neighbor blue; repeated legal moves must color the entire graph. The minimum set size is denoted \(Z_-(Y_n)\).

Both reconfiguration graphs have a vertex for each minimum skew forcing set. Token exchange joins two such sets when they differ in exactly one vertex. Token sliding imposes the additional requirement that the exchanged vertices be adjacent in the original prism. For two sets of size two, exchange adjacency means a common member; sliding means the two noncommon members are additionally adjacent in \(Y_n\).

## Proof

**1. Necessity and the minimum size.** Every prism vertex has degree three, so neither the empty set nor a one-vertex initial blue set admits a first force: every vertex has at most one blue neighbor. If two initially blue vertices permit a first force, some vertex must have exactly two blue neighbors. The two initial vertices therefore have a common neighbor, hence are at distance two (the prism is triangle-free for \(n\ge5\)). Consequently, any successful set of size two is a distance-two pair. Such pairs have exactly the listed forms. For odd \(n\ge5\), each layer contains \(n\) unordered index-difference-two pairs, and the cross-layer family contains \(2n\) pairs, giving \(4n\).

**2. Sufficiency: an explicit force sequence.** By cyclic shifts, layer interchange and reflection, it is enough to force from the same-layer seed \(S=\{(0,0),(2,0)\}\) and the cross-layer seed \(S'=\{(0,0),(1,1)\}\). From \(S\), the initially white vertex \((1,0)\) has the two blue rim neighbors \((0,0),(2,0)\), so it forces \((1,1)\). For each integer \(1\le j\le n-2\), in increasing order of \(j\), set \(r_j\equiv j\pmod 2\) and make the two moves
\[
 (j+1,r_j)\longrightarrow(j+2,r_j),\qquad
 (1-j,r_j)\longrightarrow(-j,r_j).
\]
All first coordinates are modulo \(n\). In either move, the source has its inward rim neighbor and its vertical neighbor already blue, while its outward rim neighbor is the displayed target. This holds at \(j=1\) using the three colored vertices \((0,0),(2,0),(1,1)\); for later \(j\), the vertical neighbor was colored at stage \(j-1\), and the inward rim neighbor at stage \(j-2\), with the \(j=2\) boundary supplied by an original seed. Thus each move is legal. The two target sequences cover \((3,r),(4,r),\ldots,(n-1,r)\) in opposite parities: for column \(i\in\{3,\ldots,n-1\}\), their stage indices \(i-2\) and \(n-i\) sum to the odd integer \(n-2\). They also color \((0,1)\) and \((2,1)\). Together with the initial three blue vertices, this leaves exactly \((1,0)\) white, which is then forced by \((0,0)\). Hence \(S\) succeeds.

Starting instead with \(S'\), the white vertex \((1,0)\) has its blue neighbors \((0,0)\) and \((1,1)\), so it forces \((2,0)\). The blue set now contains the already successful \(S\). Any skew forcing sequence remains legal after additional vertices have been colored, upon omitting moves whose targets are already blue. Therefore \(S'\) succeeds as well. Reflection and layer exchange handle all cross-layer pairs. This proves the complete classification and \(Z_-(Y_n)=2\).

**3. Token exchange.** Every minimum set is an edge of \(H_n\), and exchanging one of two vertices corresponds precisely to replacing one edge of \(H_n\) by an incident edge. Hence the exchange graph is \(L(H_n)\). The four distance-two neighbors of \((i,r)\) are \((i-2,r),(i+2,r),(i-1,1-r),(i+1,1-r)\), so \(H_n\) is \(4\)-regular with \(2n\) vertices and \(4n\) edges. Within either layer, the first two adjacency types form one length-\(n\) cycle because \(n\) is odd. Cross-layer edges connect the two cycles, so \(H_n\), hence its line graph, is connected. Each edge of a simple \(4\)-regular graph has six other incident edges, so \(L(H_n)\) is \(6\)-regular and has \(12n\) edges.

**4. Token sliding.** Fix the unchanged vertex \(v=(i,r)\). A slide between two minimum sets that contain \(v\) exists exactly when the other two vertices are adjacent in the original graph and both belong to \(N_2(v)\), the distance-two neighborhood of \(v\). This neighborhood consists of \((i\pm2,r)\) and \((i\pm1,1-r)\). The two opposite-layer members are nonadjacent for \(n\ge5\); no cross-layer member is adjacent to a same-layer member because their first coordinates differ. The two same-layer members are adjacent precisely when \(n=5\) (their column indices differ by four). Thus for odd \(n\ge7\) there are no token slides. When \(n=5\), every \(v\) supports exactly one slide, pairing its two same-layer distance-two partners. The same-layer minimum sets form a length-five cycle under these slides in each layer, while all ten cross-layer minimum sets are isolated. Hence the asserted decomposition holds.

## Verification

The accompanying `verify_skew_prism.py` generates all pairs of initial blue vertices of the actual prism, applies the original rule with blue **or white** sources, and independently compares the successful pairs against those at distance two. It builds token-exchange and token-sliding graphs directly from their move definitions, checking graph orders, degrees, edge counts and connected components exhaustively for odd \(n=5,7,9,11,13,15,17,19\). It also independently replays the displayed constructive force sequence for every odd \(n\) from five through 299, checking source-neighbor legality at every force. Both tests finish with `VERIFY_OK` and `CONSTRUCTIVE_CERTIFICATES_OK`. These finite tests are reproducibility checks; the argument above proves the claims for every odd \(n\ge5\).

## Relationship to prior work

Brešar and collaborators introduced Grundy-total-domination methods for graph products in 2017, providing foundational context for the study of propagation on product graphs. Chang's August 28, 2026 paper proves the **scalar** formula \(Z_-(P_2\square C_n)=2\) for odd \(n\), and its Lemma 5.4 gives one sufficient two-vertex seed. These scalar and seed facts are acknowledged, not claimed as novel. The present statement adds an all-seed classification, exact count, and both reconfiguration graph descriptions.

Bong, Flagg, Hunnell, Hutchens, Moruzzi, Schuerger and Small (2025) establish a general theory of skew forcing reconfiguration, including cycles, trees and other families. Their token-move definitions are used here; their inspected results do not give the odd-prism classification. The exact pair characterization and the change from connected exchange to frozen sliding is the evaluated contribution.

## Limitations

This theorem covers odd \(n\ge5\) only; it neither classifies even prisms nor asserts a new formula for the already-known scalar skew forcing number. Publication priority beyond the inspected sources is not independently certified. Reconfiguration is of *minimum* skew forcing sets, not of arbitrary forcing sets. The computational verification is exhaustive for the stated finite range, not for infinitely many parameters. No independent mathematical audit has been performed.

## References

- B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, T. Marc, B. Patkós, Z. Tuza and M. Vizer, *On Grundy total domination number in product graphs*, arXiv:1712.08780, first posted 2017-12-23. https://arxiv.org/abs/1712.08780
- F.-H. Chang, *Grundy Total Domination and Skew Zero Forcing in Cartesian Products of Paths and Cycles*, arXiv:2608.27804, first posted 2026-08-28, especially Theorem 1.2 and Lemma 5.4. https://arxiv.org/abs/2608.27804
- N. Bong, M. Flagg, M. Hunnell, J. Hutchens, R. Moruzzi, H. Schuerger and B. Small, *Reconfiguration of Minimum PSD Forcing Sets and Minimum Skew Forcing Sets*, arXiv:2501.03642, first posted 2025-01-07. https://arxiv.org/abs/2501.03642
