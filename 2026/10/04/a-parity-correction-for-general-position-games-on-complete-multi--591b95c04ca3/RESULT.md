# A parity correction for general-position games on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_k}\) with \(k\ge2\) and every \(n_i\ge2\). The published conclusion that player A wins the general-position achievement game if and only if player B wins the general-position avoidance game is false. In fact, B wins both games exactly when either \(k\) is odd and all \(n_i\) are even, or \(k\) is even and all \(n_i\) are odd; otherwise the two games have opposite winners, and A never wins both. The smallest counterexamples have order six and are exactly \(K_{3,3}\) and \(K_{2,2,2}\).

The correction concerns the joint conclusion drawn from two correct parity classifications. It does not alter either classification individually.

## Assumptions and scope
All graphs are finite, simple, and connected. Let \(G=K_{n_1,\ldots,n_k}\), where \(k\ge2\) and \(n_i\ge2\) for every \(i\). In the general-position achievement game, the player making the last legal move wins. In the avoidance game, the player making the last legal move loses. A move is legal when the set of all vertices selected so far remains in general position.

## Proof
A legal position in a complete multipartite graph has one of two relevant forms after the first move.

Suppose A first selects a vertex in a part \(X\) of size \(n_X\). If B selects a second vertex in the same part, then no vertex outside \(X\) is thereafter playable: any outside vertex lies on a length-two geodesic between the two selected vertices of \(X\). Every remaining vertex of \(X\) is playable, so the game has exactly \(n_X\) moves.

If B instead selects a vertex in a different part, then no part can subsequently contribute a second selected vertex. Indeed, a second vertex from an already represented part together with a selected vertex from another part would create a selected internal vertex on a length-two geodesic. Conversely, one vertex from each new part remains playable. Hence this branch has exactly \(k\) moves.

Therefore A wins the achievement game precisely when A can start in a part for which both terminal lengths available to B are odd. This is equivalent to
\[
k\text{ is odd and at least one }n_i\text{ is odd}.
\]
Likewise, in the avoidance game A wins precisely when A can start in a part for which both terminal lengths available to B are even. This is equivalent to
\[
k\text{ is even and at least one }n_i\text{ is even}.
\]

These are exactly the two published parity criteria. Combining them gives the joint outcome table. If \(k\) is odd and some \(n_i\) is odd, then A wins achievement and B wins avoidance. If \(k\) is odd and all \(n_i\) are even, then B wins both. If \(k\) is even and some \(n_i\) is even, then B wins achievement and A wins avoidance. If \(k\) is even and all \(n_i\) are odd, then B wins both. Thus the claimed equivalence between “A wins achievement” and “B wins avoidance” fails in the two parity-homogeneous cases.

For the smallest counterexamples, the hypothesis \(n_i\ge2\) forces order at least four. At order four the only type is \(K_{2,2}\), and at order five the only type is \(K_{2,3}\); in both, the winners are opposite. At order six, the multipartite types are \(K_{2,4}\), \(K_{3,3}\), and \(K_{2,2,2}\). The latter two are exactly the parity-homogeneous cases, so they are exactly the smallest counterexamples.

## Verification
The included `verify.py` independently constructs the graph metric, tests the general-position condition for every candidate move, and solves both finite games by recursive minimax. It exhaustively confirms the parity formulas for every complete multipartite isomorphism type with all parts of size at least two and order at most ten, and separately confirms that B wins both games on \(K_{3,3}\) and \(K_{2,2,2}\). The computation is corroborative; the all-orders result is proved above.

## Relationship to prior work
Klavžar, Neethu, and Ullas Chandran proved the achievement criterion for complete multipartite graphs in Proposition 2.3 of the 2021 preprint / 2022 paper. Ullas Chandran, Klavžar, Neethu, and Sampaio proved the avoidance criterion in Proposition 2.5 of the 2022 preprint / 2024 paper. Immediately after Proposition 2.5, the latter source states that A wins the achievement game if and only if B wins the avoidance game. The two propositions themselves imply the corrected four-case table above, not that equivalence.

Targeted searches for the parity correction, the two smallest counterexamples, and a later correction did not locate an equivalent statement. A later survey restates the two parity propositions separately.

## Limitations
The finding corrects the joint conclusion only for the complete multipartite family under the stated \(n_i\ge2\) hypothesis. It does not challenge the two source propositions, and it does not classify relationships between the achievement and avoidance games on arbitrary graphs. Exhaustive verification is finite and does not replace the symbolic proof. Literature searches cannot exclude differently phrased or non-indexed prior corrections.

## References
1. S. Klavžar, P. K. Neethu, U. Chandran S. V., “The general position achievement game played on graphs,” arXiv:2111.07425; Discrete Applied Mathematics 317 (2022), 109–116, DOI 10.1016/j.dam.2022.04.019.
2. U. Chandran S. V., S. Klavžar, P. K. Neethu, R. Sampaio, “The general position avoidance game and hardness of general position games,” arXiv:2205.03526; Theoretical Computer Science (2024), 114370, DOI 10.1016/j.tcs.2023.114370.
