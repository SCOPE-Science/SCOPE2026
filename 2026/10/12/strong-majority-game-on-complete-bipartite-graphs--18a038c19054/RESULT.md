# Strong-majority game on complete bipartite graphs
## Finding
Let \(m,n\ge 2\) and \(k\ge 1\). In the strong majority coloring game on \(K_{m,n}\) with a palette of \(k\) colors, every legal play reaches a full coloring if and only if
\[
k\left\lfloor\frac m2\right\rfloor\ge m
\qquad\text{and}\qquad
k\left\lfloor\frac n2\right\rfloor\ge n.
\]
Thus Bob has no strategic leverage once the two capacity inequalities hold: no sequence of legal choices by either player can create a dead position before all vertices are colored. Consequently
\[
\operatorname{Maj}_g(K_{m,n})=
\begin{cases}
2,&m\text{ and }n\text{ are both even},\\
3,&\text{otherwise},
\end{cases}
\qquad m,n\ge2.
\]

## Assumptions and scope
Graphs are finite and simple. The strong majority condition requires that, for every vertex and every color, at most half of that vertex's neighborhood has that color. The game is played by alternating legal vertex-coloring moves, with Alice seeking a complete coloring and Bob seeking to prevent completion. The statement is restricted to \(m,n\ge2\), exactly the range in which \(K_{m,n}\) has minimum degree at least two and the strong majority parameter is defined in the initiating literature.

## Proof
Write the bipartition as \(A\cup B\), with \(|A|=m\) and \(|B|=n\). Every vertex of \(B\) has neighborhood exactly \(A\). Therefore a partial coloring satisfies the strong majority condition at all vertices of \(B\) exactly when, for every color, that color appears on at most \(\lfloor m/2\rfloor\) currently colored vertices of \(A\). Symmetrically, every color may appear on at most \(\lfloor n/2\rfloor\) vertices of \(B\).

Hence the two shores decouple into capacity systems. A move that colors a vertex of \(A\) with color \(c\) is legal exactly when the current number of \(c\)-colored vertices in \(A\) is below \(\lfloor m/2\rfloor\); the analogous statement holds for \(B\).

Fix a shore of size \(s\). If \(k\lfloor s/2\rfloor<s\), then no legal full coloring of that shore exists, because the total capacity of all \(k\) colors is too small. Conversely, suppose \(k\lfloor s/2\rfloor\ge s\). At any nonfull position fewer than \(s\) vertices of the shore are colored. If every color were already saturated, then at least \(k\lfloor s/2\rfloor\ge s\) vertices would be colored, a contradiction. Thus some color remains legal on every uncolored vertex of that shore. This argument is independent of whose turn it is and of all previous legal choices.

Applying this separately to \(A\) and \(B\) proves the if-and-only-if criterion and the stronger assertion that every legal play completes whenever the inequalities hold. For \(s\ge2\), the least \(k\) with \(k\lfloor s/2\rfloor\ge s\) is \(2\) when \(s\) is even and \(3\) when \(s\) is odd. Taking the maximum of the two shore thresholds gives the displayed formula for \(\operatorname{Maj}_g(K_{m,n})\).

## Verification
The accompanying checker enumerates all reachable color-count states on a shore for sizes \(2\) through \(12\) and palettes of size \(1\) through \(5\). It directly tests that a reachable nonfull dead state exists exactly when the capacity inequality fails. It also checks the resulting two-parameter formula for every \(2\le m,n\le100\). The replay result is:

`ALL CHECKS PASSED; shore_cases=55; reachable_state_checks=19450; pair_cases=9801; shore_range=2..12; palette_range=1..5; parameter_range=2<=m,n<=100`

These finite checks are stress tests only. The theorem for all parameters follows from the capacity proof above.

## Relationship to prior work
Chawda, Nanoti, Sankarnarayanan, and Srinivasan introduce the strong majority coloring game and define \(\operatorname{Maj}_g(G)\) in arXiv:2609.37796v1. Their paper determines the strong majority game chromatic number of cycles and proves complexity results, but the inspected full text contains no occurrence of “complete bipartite.” The same paper identifies Kalinowski, Kamyczura, Pilśniak, and Woźniak's arXiv:2605.23828v1 as the source of the underlying static strong majority coloring invariant. That earlier paper gives exact values for cycles and complete graphs and general upper bounds; its inspected full text likewise contains no complete-bipartite theorem.

The present result is not merely the static feasibility criterion: it proves that on every nonstar complete bipartite graph, static feasibility is equivalent to game feasibility for every palette size, because every legal play is automatically completable. Targeted database searches under the strong-majority-game, biclique, parity, and capacity formulations found no statement implying this all-palette game theorem.

## Limitations
The theorem concerns complete bipartite graphs with both shores of size at least two. It does not address general bipartite graphs, where the initiating paper records substantially more complicated game behavior and hardness phenomena. The originality comparison is bounded by the inspected 2026 primary full texts, targeted semantic database searches, and the earlier records checked for overlap; an older or differently indexed equivalent observation remains a residual literature risk.

## References
1. Y. Chawda, S. G. Nanoti, B. Sankarnarayanan, E. Srinivasan, *Structural and computational aspects of majority coloring games*, arXiv:2609.37796v1, first public 29 September 2026.
2. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1, first public 22 May 2026.
