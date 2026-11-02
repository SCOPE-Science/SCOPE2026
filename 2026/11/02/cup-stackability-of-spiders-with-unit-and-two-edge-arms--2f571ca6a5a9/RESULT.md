# Cup stackability of spiders with unit and two-edge arms

## Finding
For integers \(a\ge1\) and \(b\ge2\), let \(T_{a,b}=S(1^a,2^b)\) be the tree formed from a center \(c\) by attaching \(a\) leaves directly to \(c\) and \(b\) paths of length two to \(c\). In the graph cup-stacking game, one cup initially occupies each vertex. A move transfers all \(k\) cups at an occupied vertex \(u\) to another occupied vertex \(v\) precisely when \(d(u,v)=k\). A graph is *stackable* when all cups can be moved onto every choice of target vertex.

**Theorem.** The mixed spider \(T_{a,b}\) is stackable if and only if \(a=1\). More precisely, when \(a\ge2\), no inner vertex of a length-two arm is a feasible stacking target. When \(a=1\), every target has an explicit sequence of exactly \(2b+1\) legal moves, given below. The separate case \(a=0\) was already covered by the known result for spiders with every arm of length at least two and is not claimed as new.

## Assumptions and scope
All graphs are finite, connected, simple and unweighted, and graph distances are ordinary shortest-path distances. The initially occupied target remains occupied throughout the constructions. Every move strictly reduces the number of occupied vertices. No moves into vacant vertices, zero-cup moves, or weighted/non-geodesic variants are used. The theorem concerns \(a\ge1,b\ge2\), not arbitrary arm-length multisets.

For \(a=1\), name the short leaf \(s\), and write the other arms as \(c-x_j-y_j\), for \(1\le j\le b\). The symbol \(u\to v\) denotes one complete legal cup-transfer move, not an edge of the tree. Concatenated moves are performed from left to right, and a phrase about a three- or four-cup stack refers to its current size immediately before a move.

## Proof
**Obstruction when \(a\ge2\).** Fix the intended target \(r=x_1\), the vertex adjacent to \(c\) on any length-two arm. Every short leaf \(s_i\) has distance two from \(r\); the target eccentricity is three, because the farthest vertices are the other long-arm ends. Consequently, if any stack ever reaches size four, the game cannot be won: stack sizes never decrease, whereas the final transfer into \(r\) must have size at most three.

No short leaf can ever hold three or more cups during a winning play. Indeed, if such a leaf holds three cups, its only possible outgoing transfers go distance three to an end \(y_j\) of a long arm, making a stack of at least four cups; if it holds four or more, it has no permissible outgoing transfer because its eccentricity is three. Since the target is not a short leaf, either situation is fatal.

Consider any short leaf \(s_i\). When it is emptied, if it still holds its original single cup, it must move to \(c\), its only neighbor. If its stack has grown before it is emptied, its *first* incoming transfer must have originated from \(c\) carrying one cup: an incoming stack of at least two would bring it to size at least three, which is impossible as just proved; and \(c\) is its only neighbor. Hence any short leaf is cleared either by moving its one cup into an occupied \(c\) or by receiving the initial single cup of \(c\). In the latter case, \(c\) becomes empty and cannot be occupied again (a destination must already be occupied), so no second short leaf can be cleared. In the former case, to clear two short leaves by sending both into \(c\) would give \(c\) at least three cups. Since \(c\) has eccentricity two and is not the target, such a stack cannot move, again impossible. Thus if \(a\ge2\), stacking onto \(x_1\) fails.

**Construction for \(a=1\).** All the following sources and destinations carry cups at the time of transfer. The tree distances used are \(d(c,y_j)=2\), \(d(s,x_j)=2\), \(d(s,y_j)=3\), and, for distinct indices \(i,j\), \(d(x_i,x_j)=2\), \(d(x_i,y_j)=3\), \(d(y_i,y_j)=4\).

*Target \(c\).* First move \(s\to c\). For each \(j\), execute \(x_j\to y_j\) (making two cups at \(y_j\)) followed by \(y_j\to c\), a distance-two transfer.

*Target \(s\).* First move \(c\to s\). For each \(j\), execute \(y_j\to x_j\) (making two cups there) followed by \(x_j\to s\), a distance-two transfer.

*Target \(x_1\).* Execute \(y_1\to x_1\), then \(c\to s\) and \(s\to x_1\). For each \(j=2,\ldots,b\), execute \(y_j\to x_j\), then move the resulting two-cup stack \(x_j\to x_1\).

*Target \(y_1\).* Begin with \(x_1\to y_1\). Four-cup stacks at ends \(y_j\) with \(j\ne1\), and three-cup stacks at \(x_j\) or \(s\), can be moved directly to \(y_1\). The following cases construct exactly these stacks.

If \(b=2\), execute \(x_2\to y_2\), \(s\to c\), \(c\to y_2\), \(y_2\to y_1\). The first and third moves into \(y_2\) create its four cups.

If \(b\ge4\) is even, execute \(c\to s\) and then \(s\to x_2\), leaving three cups at \(x_2\). Let \(p=x_2\). For \(j=3,5,\ldots,b-1\), perform the following four moves in order:

\[
 p\to y_j,\quad y_j\to y_1,\quad y_{j+1}\to x_{j+1},\quad x_{j+1}\to x_j,
\]

then replace \(p\) with \(x_j\). At the start of each iteration, \(p\) has three cups and is at distance three from \(y_j\); the first move makes four at \(y_j\). The last two moves make exactly three at \(x_j\). After the last iteration, execute \(p\to y_2\) and \(y_2\to y_1\); the first of these creates four cups at \(y_2\).

If \(b\ge3\) is odd, execute \(c\to x_2\), \(y_2\to x_2\), and \(x_2\to y_1\); the last transfer has size three. Next execute \(y_3\to x_3\), \(x_3\to s\); now \(s\) has three cups. Set \(p=s\). For \(j=4,6,\ldots,b-1\), perform

\[
 p\to y_j,\quad y_j\to y_1,\quad y_{j+1}\to x_{j+1},\quad x_{j+1}\to x_j,
\]

then set \(p=x_j\). As in the even case, the first two moves transfer a newly formed four-cup stack into the target, and the latter two leave a three-cup stack at the next \(p\). Finally execute \(p\to y_1\), a distance-three transfer. When \(b=3\) the loop is empty and this last move is simply \(s\to y_1\).

Each construction eliminates all occupied vertices except the chosen target. Every transfer has source size equal to the tree distance to its destination, and the target is never emptied. Since the tree has \(2b+2\) vertices, every successful sequence has exactly \(2b+1\) moves. Every vertex is one of the four target types by arm symmetry, completing the proof.

## Verification
Run `python3 verify_cup_spiders.py` in the same directory. The independent rule-level checker computes graph distances by breadth-first search, reconstructs each of the four explicit target strategies without relying on the theorem's distance table, and tests every move against the original game rule for all \(2\le b\le120\). It also exhaustively searches the finite state graph for non-stackability of nine sample parameter pairs with \(a\ge2\), \(2\le b\le4\). The checker reports `VERIFY_OK`. The unbounded cases are established by the proof, not inferred from the finite computations.

## Relationship to prior work
Fay, Hurlbert and Tennant, *Cup Stacking in Graphs*, arXiv:2310.06192 (first public version October 9, 2023), introduced the game, proved the stacking-partition lemma, and explicitly left spiders with both unit arms and longer arms unresolved apart from the subcase of exactly one longer arm. They credit Veselovac for prior starfish and dandelion results, including stackability when all arms have length at least two. This theorem settles the previously omitted two-length subfamily having at least two longer arms and at least one unit arm.

Gregor, Merino, Mütze and Verciani, *Graphs that admit a Hamilton path are cup-stackable*, arXiv:2401.06189 (2024), give a general sufficient Hamilton-path condition and results on other bipartite graphs. These mixed spiders have at least three leaves, so they do not have a Hamilton path, and those results do not directly provide this classification. Their obstruction for two pendant leaves with a common neighbor in diameter-three graphs resembles the local obstruction here; the complete classification additionally needs the explicit positive all-target constructions in diameter-four trees.

## Limitations
No claim is made about mixed spiders with long arms of arbitrary unequal lengths or about which other targets remain stackable when \(a\ge2\). The detailed case \(a=0\) is older literature, not a new assertion. Earlier equivalent unpublished, unindexed, or inaccessible work cannot be ruled out. Finite replay does not independently certify the infinite proof or publication priority.

## References
1. P. Fay, G. Hurlbert, M. Tennant, *Cup Stacking in Graphs*, arXiv:2310.06192, version 1 publicly posted 2023-10-09; version 2 (2024) examined. https://arxiv.org/abs/2310.06192
2. P. Gregor, A. Merino, T. Mütze, F. Verciani, *Graphs that admit a Hamilton path are cup-stackable*, arXiv:2401.06189, first publicly posted 2024-01-11; version 3 (2024) examined. https://arxiv.org/abs/2401.06189
3. I. Veselovac, prior frog-jumping work on trees, as cited and described in references 1 and 2; original thesis not inspected here.
