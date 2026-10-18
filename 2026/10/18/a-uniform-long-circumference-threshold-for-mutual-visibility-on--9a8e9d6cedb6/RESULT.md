# A uniform long-circumference threshold for mutual visibility on cylindrical grids

## Finding
For integers \(s\ge 3\) and \(t\ge 6s\), the Cartesian cylindrical grid \(P_s\square C_t\) has mutual-visibility number
\[
\mu(P_s\square C_t)=3s.
\]
More precisely, write \(h=\lfloor t/3\rfloor\). Label the path vertices \(0,\ldots,s-1\) and the cycle vertices \(0,\ldots,t-1\), with second coordinates read modulo \(t\). Then the \(3s\)-vertex set
\[
M=\{(a,kh+a):0\le a<s,\ k\in\{0,1,2\}\}
\]
is a maximum mutual-visibility set. The theorem establishes the sharp rowwise upper bound uniformly for arbitrarily large path height when the cycle circumference is at least six times the height.

## Assumptions and scope
All graphs are finite, simple and undirected. The Cartesian product has vertices \((a,c)\), with an edge if exactly one coordinate moves along an edge of its factor. A set \(M\) is *mutually visible* when each pair of its vertices can be connected by a shortest path whose internal vertices avoid \(M\). The maximum cardinality of such a set is denoted \(\mu\). The parameter range is precisely \(s\ge3\) and \(t\ge6s\); no formula is claimed here for smaller circumferences. This is ordinary mutual visibility, not connected, total or fault-tolerant mutual visibility.

## Proof
**Upper bound.** The cycle layer at any fixed path coordinate is convex: a shortest path between two vertices in that layer never changes the first coordinate. A mutual-visibility set on any cycle has at most three vertices. Indeed, if four distinct selected cycle vertices appear in cyclic order \(a,b,c,d\), each of the two \(a\)-to-\(c\) arcs contains another selected vertex (respectively \(b\) and \(d\)); hence even an unrestricted cycle path between \(a\) and \(c\) cannot avoid the other selected vertices. Therefore each of the \(s\) cycle layers contains at most three selected vertices, proving \(\mu(P_s\square C_t)\le3s\).

**Separated windows.** Put \(h=\lfloor t/3\rfloor\) and \(r=t-3h\in\{0,1,2\}\). Since \(t\ge6s\), \(h\ge2s\). The chosen vertices occupy three disjoint column blocks
\[
B_k=\{kh,kh+1,\ldots,kh+s-1\},\qquad k=0,1,2.
\]
Each block contains exactly one selected vertex in every path row; every occupied column contains exactly one selected vertex. Between consecutive blocks in the forward cyclic direction there is at least one entirely unoccupied column. The third-to-first gap may include the final \(r\) columns of the cycle.

**Same-block endpoints.** Let \(u=(a,kh+a)\) and \(v=(b,kh+b)\), with \(a\ne b\). First move vertically at column \(kh+a\) from row \(a\) to row \(b\), and then horizontally inside \(B_k\) to column \(kh+b\). No internal vertex is selected: the vertical column contains only \(u\), and the horizontal segment meets the selected vertex of row \(b\) in this block only at \(v\). Its length is \(2|a-b|\), equal to
\[
d((a,c),(b,d))=|a-b|+\min\{|c-d|,t-|c-d|\}
\]
for these endpoints (as \(|a-b|<t/2\)). Thus this is a clear geodesic.

**Different-block endpoints.** Every unordered pair of different blocks consists of consecutive blocks in one of the forward cyclic orientations \(0\to1\), \(1\to2\), or \(2\to0\). Orient the endpoints accordingly as \(u=(a,kh+a)\) and \(v=(b,\ell h+b)\), where \(\ell=k+1\) modulo \(3\). The forward cyclic distance \(D\) from the column of \(u\) to that of \(v\), through their separating empty gap, equals \(h+b-a\) for \(k=0,1\) and \(h+r+b-a\) for \(k=2\). This is a *shortest* cycle arc. Indeed, in the first two cases
\[
t-2D=h+r+2(a-b)\ge h+r-2(s-1)>0,
\]
and in the last case
\[
t-2D=h-r+2(a-b)\ge h-r-2(s-1)\ge0.
\]
Both inequalities use \(h\ge2s\) and \(0\le r\le2\). Choose an unoccupied column \(g\) strictly between these blocks along that forward arc, for example \(g=kh+s\) (which is a valid cycle column even when \(k=2\)). Traverse the forward arc from \(u\) to \(g\) while staying in row \(a\), move vertically at \(g\) to row \(b\), then continue along the same forward arc to \(v\) in row \(b\). Before the vertical move, the route meets only the starting block and the empty gap, and row \(a\) has only \(u\) selected in that block. The vertical segment is entirely unoccupied. After it, the route meets only the gap and destination block, and row \(b\) has only \(v\) selected there. Hence the geodesic has no selected interior vertex. Its length \(D+|a-b|\) is exactly the Cartesian-product distance. Every selected pair is therefore mutually visible.

There are \(3s\) distinct selected vertices, proving \(\mu(P_s\square C_t)\ge3s\). Combined with the upper bound this establishes the theorem. \(\square\)

## Verification
Run `python3 verify.py` with Python 3 and the standard library. The supplied program constructs \(M\), explicitly constructs the three-stage geodesic for each selected pair, tests path length, adjacency and absence of other selected vertices, and independently computes the distance after deleting all other selected vertices using breadth-first search. The script completed successfully on \(89\) parameter pairs: all \(3\le s\le10\) with \(6s\le t\le6s+9\), and \(s\in\{12,16,20\}\) with \(t\in\{6s,6s+1,6s+2\}\). This checks \(26{,}904\) unordered endpoint pairs. These finite checks corroborate, but do not replace, the proof for arbitrary parameters.

## Relationship to prior work
Korže and Vesel [1, Proposition 2.1] proved the upper bound \(\mu(P_s\square C_t)\le\min\{3s,2t\}\); their Theorem 2.4 proves equality with \(2t\) for \(s+1\ge t\ge6\), which is a different aspect-ratio regime. Their Conjecture 2.6 predicts equality with the upper bound whenever \(t\ge12\), and their finite tables extend through only a limited range of circumferences. The present theorem supplies an explicit proof of that prediction throughout the unbounded parameter wedge \(s\ge3\), \(t\ge6s\), rather than relying on finite construction tables. It does not settle the remainder of the conjecture.

Cicerone, Di Stefano and Klavžar [2, Theorem 3.2] gave general Cartesian-product bounds; they supply no matching long-cycle construction of size \(3s\). A later paper by Cicerone, Di Stefano, Klavžar and Zhang [3, Section 6.2] explicitly treats the ordinary \(k=0\) cylinder case as an earlier conjecture and solves a *different* fault-tolerant variant for \(k\ge1\), so its formulas do not imply this result.

## Limitations
The threshold \(t\ge6s\) is sufficient, not asserted to be necessary or sharp. The complete conjectured region \(t\ge12\) remains unresolved by this theorem. Finite reproducibility checks are not proofs outside tested instances, and unindexed equivalent work cannot be excluded.

## References
[1] D. Korže and A. Vesel, “Mutual-visibility sets in Cartesian products of paths and cycles,” arXiv:2309.15201, first version 2023-09-26; *Results in Mathematics* 79, article 116 (2024), DOI 10.1007/s00025-024-02139-x. https://arxiv.org/abs/2309.15201 ; https://doi.org/10.1007/s00025-024-02139-x

[2] S. Cicerone, G. Di Stefano and S. Klavžar, “On the mutual visibility in Cartesian products and triangle-free graphs,” arXiv:2112.13024, initial version 2021-12-24; *Applied Mathematics and Computation* 438, 127619 (2023). https://arxiv.org/abs/2112.13024

[3] S. Cicerone, G. Di Stefano, S. Klavžar and G. Zhang, “Fault-tolerant mutual-visibility: Complexity and solutions for grid-like networks,” *Networks*, first published 2026-09-26, DOI 10.1002/net.70074. https://doi.org/10.1002/net.70074
