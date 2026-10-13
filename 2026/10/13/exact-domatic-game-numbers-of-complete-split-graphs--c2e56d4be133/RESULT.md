# Exact domatic-game numbers of complete split graphs
## Finding
For integers \(u\ge1\) and \(m\ge2\), define
\[
S_{u,m}=K_u\vee\overline{K_m}=K_{1,\ldots,1,m}.
\]
Thus \(S_{u,m}\) has a clique \(U\) of \(u\) universal vertices and an independent set \(I\) of \(m\) vertices. Then
\[
\operatorname{dom}_g(S_{u,m})=
\begin{cases}
(u+1)/2,&u\text{ odd},\\
u/2,&u\text{ even and }m\text{ even},\\
u/2+1,&u\text{ even and }m\text{ odd},
\end{cases}
\]
and
\[
\operatorname{dom}'_g(S_{u,m})=
\begin{cases}
(u+1)/2,&u\text{ odd},\\
u/2+1,&u\text{ even and }m\text{ even},\\
u/2,&u\text{ even and }m\text{ odd}.
\end{cases}
\]
For odd \(u\), the two starting conventions therefore agree. For even \(u\), they differ by one and the larger value switches between the two games when the parity of \(m\) switches.

## Assumptions and scope
The graph is finite and simple. The A-game is the version in which Alice moves first; the B-game is the version in which Bob moves first. A completed coloring is winning for Alice exactly when every color class is a dominating set. The restriction \(m\ge2\) makes the graph noncomplete; the boundary \(m=1\) is the complete graph and is already covered by the initiating paper. The case \(u=1\) is a star and the formulas give value \(1\) in both games.

## Proof
A color class \(D\) dominates \(S_{u,m}\) exactly when either \(D\cap U\ne\varnothing\), or \(D=I\). Indeed, any vertex of \(U\) is universal. If \(D\subseteq I\) and \(D\ne I\), then a vertex of \(I\setminus D\) has no neighbor in \(D\), because \(I\) is independent. Consequently, a completed coloring is winning exactly when every color appears in \(U\), except that one color may be absent from \(U\) if all of \(I\) receives that color.

Write \(u=2q+1\) or \(u=2q\). Alice's lower-bound strategies use a fresh color whenever she colors a vertex of \(U\).

If \(u=2q+1\), then in the A-game Alice simply chooses a vertex of \(U\) whenever one is available. Since she moves first, she obtains at least \(q+1\) of the \(U\)-moves, so she can represent \(q+1\) colors in \(U\). In the B-game, if Alice receives \(q+1\) or more \(U\)-moves the same argument applies; if she receives only \(q\), then Bob has made at least one \(U\)-move, and Alice can choose on each of her \(q\) such moves a color not yet represented there. Bob's first represented color together with her \(q\) fresh colors again yields \(q+1\) represented colors. Hence both game numbers are at least \(q+1\).

Now let \(u=2q\). In the A-game with even \(m\), Alice can again take \(U\) whenever possible and guarantees at least \(q\) \(U\)-moves, so \(q\) colors can be represented. If \(m\) is odd, Alice first colors one vertex of \(I\). Thereafter, whenever possible, she answers Bob in the same zone, \(U\) or \(I\). After her opening, both remaining zone sizes are even, so the remaining moves occur in Bob--Alice pairs within zones. In \(U\), Bob is first in each of the \(q\) pairs; after his first \(U\)-move Alice can add a new color on every reply, producing \(q+1\) represented colors. Thus the A-game lower bounds are \(q\) for even \(m\) and \(q+1\) for odd \(m\).

For the B-game with \(u=2q\), if \(m\) is odd Alice can choose a vertex of \(U\) whenever possible and guarantees \(q\) \(U\)-moves. If \(m\) is even, she answers Bob in the same zone whenever possible. Both zone sizes are even, so every \(U\)-move belongs to a Bob--Alice pair; Bob's first color in \(U\) together with one fresh color from each of Alice's \(q\) replies yields \(q+1\) represented colors. This proves all lower bounds.

For the matching upper bounds, Bob uses the reverse pairing idea. Whenever he answers Alice in \(U\), he uses a color already represented there, so his reply introduces no new \(U\)-color. When needed, he also makes \(I\) nonmonochromatic, or places in \(I\) a color already represented in \(U\); either condition prevents the exceptional possibility that a color absent from \(U\) dominates by occupying all of \(I\).

If \(u=2q+1\) in the A-game with palette size \(q+2\), Bob pairs Alice's \(U\)-moves whenever possible. If Alice begins in \(I\) with color \(a\), Bob immediately puts color \(a\) in \(U\); if she begins in \(U\), Bob uses the same color there and later puts it in \(I\). In either case at most \(q+1\) colors appear in \(U\), and \(I\) contains a color that is represented in \(U\), so a missing color cannot equal all of \(I\). Bob wins. In the B-game, Bob opens in \(U\) with color \(a\), pairs Alice's later \(U\)-moves without introducing new colors, and places \(a\) in \(I\) on his first opportunity. Again at most \(q+1\) colors appear in \(U\), so palette size \(q+2\) is impossible.

Let \(u=2q\). In the A-game with even \(m\), Bob replies in the same zone as Alice. Both zone sizes are even, so Alice has exactly \(q\) opportunities to introduce colors in \(U\); Bob copies existing colors there. On the first \(I\)-pair, Bob uses a color different from Alice's, making \(I\) nonmonochromatic. Hence \(q+1\) colors cannot all dominate. If \(m\) is odd, the same reply strategy gives at most \(q+1\) represented colors in \(U\) even when the unique parity break forces one Bob initiation there, while the first available \(I\)-pair is made bichromatic; thus palette size \(q+2\) is impossible.

For the B-game with odd \(m\), Bob opens in \(I\). The remaining \(I\)-size is even; he then pairs Alice's moves within zones, copies existing colors on \(U\), and makes the first remaining \(I\)-pair bichromatic. Therefore at most \(q\) colors appear in \(U\), so \(q+1\) colors cannot all dominate. Finally, if \(m\) is even, Bob opens in \(U\) with color \(a\), pairs Alice's later \(U\)-moves without adding new colors, and ensures that color \(a\) also occurs in \(I\). At most \(q+1\) colors appear in \(U\), so palette size \(q+2\) is impossible. These upper bounds match the lower bounds.

## Verification
The proof is analytic for all \(u\ge1\) and \(m\ge2\). A standalone minimax program independently constructs the graph, checks the terminal-color characterization, and solves both starting conventions at the claimed threshold and one color above it for every tested profile with \(u\le4\), \(m\le5\), and total order at most \(8\). It reports `ALL CHECKS PASSED; game_profiles=30; terminal_colorings=299; max_order=8`. These finite computations are corroborative and are not used to discharge the infinite quantifiers.

## Relationship to prior work
Hartnell and Rall introduced the domatic number game, proved general degree bounds, and determined exact values for complete graphs and complete bipartite graphs. Their paper lists primary MSC \(05C57\) and was first public on 2025-08-14. The present family is neither complete nor bipartite when \(u\ge2\), except for the star boundary \(u=1\). English and Swan later developed general lower bounds and comparisons between starting conventions, but their full text contains no split-graph, complete-multipartite, or universal-vertex family theorem. A later paper on deletion and palette size proves palette downward closure and edge-deletion monotonicity, but its inspected text likewise contains no exact complete-split classification.

A prior exact result for the one-dimensional subfamily \(K_{1,1,m}\) is a strict special case of the theorem above. The new result determines every \(K_u\vee\overline{K_m}\) with arbitrary \(u\), revealing that the earlier parity reversal is the even-\(u\) slice of a complete two-parameter law rather than an isolated phenomenon.

## Limitations
The theorem is restricted to complete split graphs with exactly one non-singleton partite class. It does not classify arbitrary complete multipartite graphs with two or more non-singleton parts. The originality search cannot exclude an equivalent result hidden under substantially different terminology or in unindexed material.

## References
1. B. L. Hartnell and D. F. Rall, *The domatic number game played on graphs*, arXiv:2508.10754v1; later Ars Combinatoria 165 (2025), 31--43.
2. S. English and L. Swan, *On the Domatic Game*, arXiv:2603.13522v1.
3. *Deletion and palette size in the domatic number game*, DOI:10.61091/ars168-07, published online 2026-08-11.
