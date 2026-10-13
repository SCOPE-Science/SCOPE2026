# Distance-fall spectra of crown graphs
## Finding
For an integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph, where the deleted perfect matching is \(M_n=\{a_i b_i:1\le i\le n\}\). For \(d\ge 1\), let \(\operatorname{Fall}_d(G)\) be the set of numbers of colors occurring in distance-\(d\) fall colorings of \(G\). Then
\[
\operatorname{Fall}_1(\operatorname{Cr}_n)=\{2,n\},\qquad
\operatorname{Fall}_2(\operatorname{Cr}_n)=\{2,3,\ldots,n\},
\]
and, for every \(d\ge 3\),
\[
\operatorname{Fall}_d(\operatorname{Cr}_n)=\{2,3,\ldots,2n\}.
\]
The structural core is sharper: a proper coloring of \(\operatorname{Cr}_n\) is distance-\(2\) fall if and only if every color class has at least two vertices.

## Assumptions and scope
A distance-\(d\) fall coloring is a proper vertex coloring in which every vertex lies within graph distance at most \(d\) of at least one vertex of every color. The result concerns finite simple crown graphs with \(n\ge3\). This lower bound on \(n\) ensures that \(\operatorname{Cr}_n\) is connected and has diameter \(3\). The statement classifies the complete set of feasible color counts; it does not count labeled colorings or color-class partitions.

## Proof
Write the two shores as \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with exactly the pairs \(a_i b_i\) missing. For \(n\ge3\), the only pairs at distance \(3\) are \(a_i,b_i\). Distinct vertices in one shore are at distance \(2\), and nonmatched cross-shore pairs are adjacent.

Every independent set in \(\operatorname{Cr}_n\) is either contained in one shore or is exactly one deleted matched pair \(\{a_i,b_i\}\). Consider a nonempty independent set \(C\). If \(|C|=1\), say \(C=\{a_i\}\), then \(b_i\) is at distance \(3\) from \(C\), so \(C\) is not distance-\(2\) dominating. Conversely, if \(|C|\ge2\), then \(C\) is distance-\(2\) dominating. This is immediate for a deleted matched pair. If \(C\subseteq A\) (or symmetrically \(C\subseteq B\)), vertices of its own shore are within distance at most \(2\), while every vertex on the opposite shore is adjacent to all but at most one member of \(C\); because \(|C|\ge2\), at least one adjacent member remains. Therefore an independent color class is distance-\(2\) dominating exactly when it has size at least two. Since a distance-\(2\) fall coloring is precisely a partition into independent distance-\(2\) dominating sets, the stated structural characterization follows.

Thus any distance-\(2\) fall coloring has at most \(n\) colors. The bipartition gives two colors. For each \(q\) with \(2\le q\le n\), use \(q-2\) deleted matched pairs as color classes and use the two residual shore sets as the final two classes. Each residual shore has size \(n-q+2\ge2\), so all classes satisfy the characterization. Hence \(\operatorname{Fall}_2(\operatorname{Cr}_n)=\{2,\ldots,n\}\).

For \(d\ge3\), the diameter is \(3\), so every proper coloring is distance-\(d\) fall. The proper-coloring spectrum is every integer from \(2\) through \(2n\): split \(A\) into \(r\) nonempty classes and \(B\) into \(q-r\) nonempty classes using disjoint palettes, choosing \(r\) so that \(1\le r\le n\) and \(1\le q-r\le n\). Hence \(\operatorname{Fall}_d(\operatorname{Cr}_n)=\{2,\ldots,2n\}\).

For completeness, the ordinary fall case \(d=1\) has only two possible partitions. An independent dominating set is either a whole shore or one deleted matched pair. Consequently a fall partition is either \(\{A,B\}\) or the partition into all \(n\) deleted matched pairs, giving \(\operatorname{Fall}_1(\operatorname{Cr}_n)=\{2,n\}\).

## Verification
The proof is uniform in \(n\). The accompanying checker independently constructs crown-graph distances, exhaustively verifies for \(3\le n\le8\) that a nonempty independent set is distance-\(2\) dominating exactly when it has cardinality at least two, and enumerates every unlabeled vertex partition for \(n=3,4,5\). For those orders it filters partitions by properness and the distance-fall condition at radii \(1,2,3\), reproducing exactly the three spectra above. The finite computation corroborates but is not used as an infinite proof.

## Relationship to prior work
Goddard and Mafunda introduced distance-\(k\) fall colorings and proved that every connected \(3\)-colorable graph of order at least \(3\) has a distance-\(2\) fall \(3\)-coloring. They also note that diameter-\(2\) graphs make distance-\(2\) fall automatic for proper colorings. Crown graphs are bipartite but have diameter \(3\), so neither statement determines their distance-\(2\) spectrum. Their full text contains no occurrence of “crown” or “perfect matching.” The classical radius-\(1\) endpoint \(\{2,n\}\) is part of the older fall-coloring picture; the new content here is the exact radius-\(2\) structural characterization and spectrum, together with the resulting complete radius transition.

## Limitations
The theorem concerns only crown graphs and feasible color counts. It does not enumerate the number of distance-fall colorings, classify spectra for arbitrary matching-deleted bicliques, or address algorithmic complexity. The radius-\(1\) branch is included for a complete transition picture and is not claimed as new. The principal originality risk is terminological: an equivalent radius-\(2\) crown calculation could exist under independent distance domination or an unindexed fall-coloring formulation.

## References
1. W. Goddard and S. Mafunda, “A Note on Distance-Fall Colorings,” arXiv:2508.21232v1, 2025.
2. J. E. Dunbar, S. M. Hedetniemi, S. T. Hedetniemi, D. P. Jacobs, J. Knisely, R. C. Laskar, and D. F. Rall, “Fall Colorings of Graphs,” Journal of Combinatorial Mathematics and Combinatorial Computing 33 (2000), 257–273.
