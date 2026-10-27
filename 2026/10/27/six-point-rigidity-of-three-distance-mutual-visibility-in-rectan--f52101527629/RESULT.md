# Six-point rigidity of three-distance mutual visibility in rectangular grids

## Finding

For integers \(m,n\ge3\), let \(G_{m,n}=P_m\square P_n\) be the rectangular grid with vertex set \(\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\), adjacent at Manhattan distance one. A three-distance mutual-visibility set \(S\) requires, for each two distinct \(u,v\in S\), a shortest \(u,v\)-path of length at most three whose internal vertices avoid \(S\). Let \(\mu_3(G_{m,n})\) be the largest size of such a set.

**Theorem.** For all \(m,n\ge3\),
\[
\mu_3(G_{m,n})=\begin{cases}
5,&m=n=3,\\
6,&\max\{m,n\}\ge4.
\end{cases}
\]
If \(\max\{m,n\}\ge4\), every six-vertex maximizer is the translate of precisely one of the following two coordinate patterns:
\[
H=\{(0,1),(0,2),(1,0),(1,3),(2,1),(2,2)\},\qquad
V=\{(c,r):(r,c)\in H\}.
\]
The pattern \(H\) has bounding rectangle \(3\times4\), while \(V\) has bounding rectangle \(4\times3\). All translates fitting inside the grid are feasible, and distinct translates are distinct maximizers. Thus the number of maximum sets, with grid vertices distinguished, is
\[
\mathsf M_3(m,n)=(m-2)(n-3)+(m-3)(n-2)
\quad (m,n\ge3,\ \max\{m,n\}\ge4).
\]
In the exceptional \(3\times3\) grid there are exactly four maximum sets, each of cardinality five.

## Assumptions and scope

Paths are finite simple graphs; shortest paths are taken in the whole grid. Graph distance is Manhattan distance, and the existence of **one** unobstructed shortest path suffices for each selected pair. The path-length bound is simultaneous with the visibility condition: pairs farther than three are forbidden, not silently exempted. The theorem treats the two-dimensional Cartesian product of paths of orders at least three. A horizontal/vertical coordinate exchange is permitted, and vertex labels remain distinct when counting solutions.

## Proof

**1. Row bound and universal six-point bound.** Any three selected vertices in one row are impossible: the two extreme ones have a unique shortest horizontal path through the middle selected vertex. The same holds for columns. Moreover, every two selected vertices have Manhattan distance at most three, so the span of occupied row indices is at most three.

If the row span is at most two, at most three rows are occupied and each holds at most two selected vertices; hence \(|S|\le6\). If the span equals three, let its lowest and highest occupied rows be \(r\) and \(r+3\). Any selected vertices in these two rows must have the same column, since the vertical gap alone is three. Thus each extreme row contains exactly one selected vertex, and the two intervening rows contain at most two apiece. Again \(|S|\le1+2+2+1=6\).

**2. Rigidity when the occupied row span is three.** Equality in the last bound forces one vertex in each extreme row and two vertices in each intermediate row. Write the extremes as \((r,c)\) and \((r+3,c)\). Their unique vertical geodesic forces \((r+1,c)\) and \((r+2,c)\) to be unselected. Every vertex in either intermediate row must be within one column of \(c\): it is at vertical distance two from one of the extremes. Therefore each intermediate row must contain both \((\cdot,c-1)\) and \((\cdot,c+1)\). This is exactly a translate of \(V\).

**3. Rigidity when the occupied row span is at most two.** Six selected vertices require exactly three consecutive occupied rows with two vertices each. Their column span cannot be at most one, by the same two-per-column bound. Nor can it be exactly two: six points in a \(3\times3\) square would mean two points in every row and column, whose three omitted cells form a permutation matrix. But any diameter-three set must omit a corner from each of the two opposite-corner pairs. Two missing corners that hit these two pairs must share a row or column, impossible for a permutation matrix. Thus the column span is exactly three.

Call its extreme columns \(c\) and \(c+3\). Every selected vertex in either extreme column lies in the same row, since a row difference would make the Manhattan distance at least four. Consequently each extreme column contains exactly one selected vertex, and both lie in the same row. That row cannot be the upper or lower occupied row: a vertex two rows away could not have distance at most three from both column extremes (its column would have to lie simultaneously within one of both \(c\) and \(c+3\)). Thus the extreme-column vertices lie in the middle row. Both other rows must contain two vertices within one of the inner columns \(c+1,c+2\): comparing to both selected extremes at row distance one forces these two columns. Hence the set is exactly a translate of \(H\).

**4. Attainment and the exact number.** Both patterns are visible. It suffices to check \(H\), since transposition preserves shortest paths. Its row-reversal and column-reversal symmetries reduce the fifteen selected pairs to six representatives. The following list gives one shortest path for each representative; each internal coordinate is outside \(H\):

- \((0,1)\) to \((0,2)\): directly adjacent;
- \((0,1)\) to \((1,0)\): \((0,1),(1,1),(1,0)\);
- \((0,1)\) to \((1,3)\): \((0,1),(1,1),(1,2),(1,3)\);
- \((0,1)\) to \((2,1)\): \((0,1),(1,1),(2,1)\);
- \((0,1)\) to \((2,2)\): \((0,1),(1,1),(1,2),(2,2)\);
- \((1,0)\) to \((1,3)\): \((1,0),(1,1),(1,2),(1,3)\).

Every listed path has length at most three and equals Manhattan distance. Any translated copy sits in a geodesically convex subgrid, so remains valid in the larger grid. Steps 2–3 establish that there are no other six-element sets. There are \((m-2)(n-3)\) horizontal placements and \((m-3)(n-2)\) vertical placements; their bounding-rectangle dimensions differ, preventing duplicate counting.

**5. The \(3\times3\) boundary.** The argument in Step 3 proves six vertices impossible. Five vertices are feasible: take
\[
B=\{(0,0),(0,2),(1,0),(1,2),(2,1)\}.
\]
The original shortest-path condition can be checked directly for its ten pairs (also by the independent exhaustive verifier). In every five-set, at most two corners may be selected, since among any three corners there is a pair at Manhattan distance four. If the center is selected, at most two of the four edge midpoints can be selected (at most one from each opposite pair, whose unique geodesic would pass through the center); together with at most two corners, this gives at most five. Equality is impossible: the two selected corners must be adjacent, say the top corners. Their unique geodesic prohibits the top edge midpoint. The two selected midpoints would then have to be the bottom midpoint and exactly one of the left or right midpoints, because opposite midpoints cannot both be present. If the left midpoint is selected, every shortest path from the top-left corner to the bottom midpoint passes through either that left midpoint or the selected center; the right case is symmetric. Hence a center-containing set cannot attain five. If the center is not selected, five vertices require at least two corners; fewer than two corners would require all four midpoints, blocking the unique shortest path from the corner to its opposite-side midpoint. Thus precisely two corners are chosen, and they must be adjacent. Choosing the top two corners forces the bottom center to be selected and both middle-row endpoints to be selected; the center of that row cannot be one of the two since it would block a shortest path from a top corner to the bottom center. This yields \(B\). The same argument for any side gives exactly four possibilities, one for each side.

## Verification

The standalone script `check_grid_mu3.py` enumerates **every** subset satisfying the necessary diameter-three condition, by exhaustive recursive clique generation on the graph of Manhattan-distance-at-most-three pairs. It tests each candidate using the original definition, enumerating every shortest coordinate-step ordering and requiring an unobstructed path. It compares the exact sets of maximizers against the explicit translates of \(H\) and \(V\), rather than checking only numerical equality.

On thirteen independent grid instances (from \(1\times4\) to \(6\times8\)), the script examines 20,675 diameter-three cliques. All tested optima, all size-six optimizer families, and the four exceptional \(3\times3\) optima agree with the theorem; the record is in `check_grid_mu3.out`. Computation is corroborative: Steps 1–5 prove the statements for all \(m,n\ge3\).

Run with `python3 check_grid_mu3.py`; no third-party packages are required.

## Relationship to prior work

Cera López, García-Vázquez, Valenzuela-Tripodoro, and Yero introduced the distance-bounded mutual-visibility parameter in the arXiv preprint dated 2024-08-07, now published as *The k-Distance Mutual-Visibility Problem in Graphs*. Their open-problem section explicitly asks for the values on rectangular grids, whereas their exact results address paths, cycles, trees, path coronas, and strong-product families. This theorem settles the radius-three layer and classifies all optimizers within the two-dimensional path-product family, including a count of placements; it does not purport to settle general \(k\).

The known unrestricted mutual-visibility number \(\mu(P_m\square P_n)=2\min\{m,n\}\), discussed in the earlier grid and Cartesian-product literature, uses no distance cutoff. It does not imply the uniform six-point upper bound or its optimizer classification for larger grids. Korže and Vesel (2024) study unrestricted visibility on path-cycle and cycle-cycle products, not the present distance-three path-path statement. The 2025 *Mutual d-visibility in Graphs* uses a different convention, which exempts pairs at distance greater than \(d\) instead of forbidding them. The 2026 fault-tolerant variant requires multiple alternative shortest paths rather than a distance-three cutoff. These are distinct invariants.

## Limitations

This solves only the three-distance case on Cartesian products of two paths with both factors of order at least three; it does not settle larger distance thresholds, higher Cartesian dimensions, cylindrical grids, or other visibility variants. Search and source inspection found no equivalent earlier optimizer classification, but cannot exclude an unindexed independent result. The four-small-grid exceptional count is also checked exhaustively, while the infinite statement is established by a combinatorial proof.

## References

1. M. Cera López, P. García-Vázquez, J. C. Valenzuela-Tripodoro, I. G. Yero, *The k-Distance Mutual-Visibility Problem in Graphs*, arXiv:2408.03976 (first public version 2024-08-07); Bull. Malays. Math. Sci. Soc. 48, Article 25 (2025), DOI: 10.1007/s40840-024-01811-3. https://arxiv.org/abs/2408.03976
2. D. Korže and A. Vesel, *Mutual-Visibility Sets in Cartesian Products of Paths and Cycles*, Results Math. 79, 116 (2024), DOI: 10.1007/s00025-024-02139-x. https://link.springer.com/article/10.1007/s00025-024-02139-x
3. S. Cicerone, G. Di Stefano, S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, Appl. Math. Comput. 438 (2023), 127619, DOI: 10.1016/j.amc.2022.127619.
4. D. Kuziak, L. P. Montejano, J. A. Rodríguez-Velázquez, *Mutual d-visibility in Graphs*, Results Math. 80, 130 (2025), DOI: 10.1007/s00025-025-02450-1. https://link.springer.com/article/10.1007/s00025-025-02450-1
5. S. Cicerone, G. Di Stefano, S. Klavžar, G. Zhang, *Fault-Tolerant Mutual-Visibility: Complexity and Solutions for Grid-Like Networks*, Networks (2026), DOI: 10.1002/net.70074. https://onlinelibrary.wiley.com/doi/10.1002/net.70074
