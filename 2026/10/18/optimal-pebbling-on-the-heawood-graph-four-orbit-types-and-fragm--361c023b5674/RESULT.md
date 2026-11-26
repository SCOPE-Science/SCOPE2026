# Fano incidence characterizes the optimal Heawood pebbling distributions

## Finding

For ordinary pebbling on the Heawood graph, the optimal distributions have the following four geometric types, each a single orbit under the full graph automorphism group:

| Nonzero piles | Incidence condition | Orbit size |
|---|---|---:|
| \(3,3\) | A point and an incident line | 21 |
| \(4,2\) | A point and an incident line, with the four-pebble vertex distinguished | 42 |
| \(4,2\) | A point and a nonincident line, with the four-pebble vertex distinguished | 56 |
| \(4,1,1\) | The three points of a line, or the three lines through a point, with the four-pebble vertex distinguished | 42 |

The incidence conditions are necessary and sufficient, not just orbit representatives found among the solutions. In particular, knowing only that a distribution has pile sizes \(4,1,1\) does not decide solvability; the three occupied vertices must form a marked Fano triple.

## Assumptions and input

The Heawood graph is the point–line incidence graph of the Fano plane. A move consumes two pebbles at one vertex and creates one at an adjacent vertex. Solvability requires a legal sequence reaching each target separately from the original distribution. Distinct points lie on one common line, distinct lines meet in one point, and each vertex has degree three. The distance within one bipartition class between distinct vertices is two, and the distance between a nonincident point and line is three.

We use the exact finite results of [*A sharp two-pebble slack threshold for solvable pebbling transfers on the Heawood graph*](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-sharp-two-pebble-slack-threshold-for-solvable-pebbling-transfe--99c7c303db16/RESULT.md): no weight below six is solvable, and at weight six the only solvable pile-size multisets are \((3,3),(4,2),(4,1,1)\). Those results, the total number of distributions, and the slide and jump census are not contributions here. The proof below determines the incidence geometry within each multiset without using a census of the labelled placements or any transfer calculation.

## Proof

For a target \(L\), let \(W_L(D)=\sum_v D(v)2^{-d(v,L)}\). A move cannot increase \(W_L\), because the recipient is at distance at least \(d(v,L)-1\) from the target when the donor is \(v\). Therefore \(W_L<1\) excludes reachability. When \(W_L=1\), reaching \(L\) requires every move to decrease the moving pebble's distance by one, and the final distribution at first reach must consist solely of one pebble at \(L\).

**Two piles on the same side.** For either multiset \((3,3)\) or \((4,2)\), if both vertices are points, choose a line through neither: the union of their pencils contains only five of the seven lines. The potential at that line is \(6/8<1\). Duality handles two lines.

**Opposite sides.** Suppose there are three pebbles at each of a nonincident point \(p\) and line \(M\). The only possible moves are one from each initial pile. Indeed neither can send to the other, each leaves only one pebble when used, and their destinations are on opposite sides so the moved pebbles cannot combine. A point different from \(p\) and off \(M\) remains unreachable. If \(p\) and \(M\) are incident, use two at \(M\) to bring \(p\) to four pebbles and then reach any point along a path of length at most two; symmetrically any line is reachable by first sending a pebble from \(p\) to \(M\).

Now put four pebbles at a point \(p\) and two at a line \(M\), whether incident or not. Four at \(p\) reach all points and incident lines directly along paths of length at most two. For a line \(L\ne M\) not incident with \(p\), take \(x=M\cap L\). One pebble from \(M\) and one from \(p\) along a two-edge path meet at \(x\). Sending from \(M\) first also works if the path from \(p\) to \(x\) uses \(M\). Use the resulting pair at \(x\) to reach \(L\). Duality handles four on a line and two at a point.

**Three piles.** By duality take four pebbles at a point \(p\). If one singleton is at a point \(q\) and the other is at a line \(M\), there is a line \(L\ne M\) through neither \(p\) nor \(q\). At this target \(W_L=5/8+1/4<1\). If both singletons are lines \(M,N\), choose \(L\ne M,N\) not incident with \(p\). Here \(W_L=4/8+2/4=1\). In a successful sequence all moves must be toward the target by the potential argument, and no vertex at distance two can retain a pebble. The only initially occupied vertex of distance three is \(p\), and only vertices at distance three can supply distance-two vertices. Exactly one of the at most two deliveries from \(p\) is needed at each of \(M,N\), since each starts with an odd count and must empty in pairs. If either is not incident with \(p\) this is impossible. Otherwise, the pebbles from \(M,N\) go to \(M\cap L,N\cap L\) respectively. These points are distinct since \(M\cap N=p\notin L\), so the two pebbles cannot combine to reach \(L\).

It remains to put both singletons on points. If the three occupied points are not collinear, the three pencils of lines through them have union of size \(3\cdot3-3=6\), leaving a target line at distance three from all three piles. The potential there is \(6/8<1\). If the three points are on the same line \(M\), four at \(p\) already suffice for every point and every line through \(p\). A line \(L\) not through \(p\) meets \(M\) at one of the singleton points. Deliver a pebble from \(p\) to that point via \(M\) and use the resulting pair to reach \(L\). This also proves the dual case of three concurrent lines.

**Orbits.** Identify points with the nonzero vectors in \(\mathbb F_2^3\) and lines with the two-dimensional subspaces. Invertible linear maps act transitively on incident point–line pairs, by taking a basis whose first vector is the specified point and whose first two vectors span the specified line. They act transitively on nonincident pairs by taking a basis of the line and adjoining the specified point as a complement. The map taking a point to its orthogonal line and a line to its orthogonal point is a graph duality, so the orientations of marked flags and nonflags, and the two sides of the marked-triple type, do not split into separate full orbits. For the triple type, specifying the line and marked point is exactly specifying a flag; the dual identifies the concurrent version. The pile sizes and incidence distinguish the four types. There are 21 flags and 28 nonflags of a point and a line, giving respectively \(21,2\cdot21,2\cdot28,2\cdot21\) placements as listed.

## Verification and limitations

The geometric necessity and sufficiency arguments are exact. For the finite input on allowable pile sizes, one can enumerate all fourteen-part weak compositions of weights zero through six and compute reachable targets in increasing total weight: the target mask of a distribution is its occupied-vertex mask union the masks of every legal successor, all of one less weight. The original supporting state and optimum lists give respectively 38,760 masks and 161 optima. The proof is for this fixed incidence graph and does not apply to simultaneous covering, rubbling, pegging or a different starting mass; nor does it claim chronological priority for the geometric classification.
