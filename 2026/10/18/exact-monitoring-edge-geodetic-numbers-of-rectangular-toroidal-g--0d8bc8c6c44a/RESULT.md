# Exact monitoring edge-geodetic numbers of rectangular toroidal grids

## Finding

For every pair of integers \(m,n\ge5\), the Cartesian product of cycles has monitoring edge-geodetic number
\[
\operatorname{meg}(C_m\square C_n)=3\max\{m,n\}.
\]
The result includes all unequal side lengths, for which the published equal-side construction does not directly apply. It is attained by an explicit \(3\)-point-per-column placement, with only two small adjustments to a uniform balanced-floor construction.

## Assumptions and scope

All graphs are finite, simple, undirected and connected. Write \(C_k\) for the cycle on vertex set \(\mathbb Z/k\mathbb Z\), with adjacent residues differing by \(1\). The Cartesian product \(C_m\square C_n\) has vertex set \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\), with edges differing by one cycle edge in exactly one coordinate.

For an edge \(e\), a pair of vertices \(u,v\) *monitors* \(e\) if deletion of \(e\) strictly increases the distance between \(u\) and \(v\), or equivalently if \(e\) lies on **every** shortest \(u\)-\(v\) path. A monitoring edge-geodetic set (MEG-set) \(S\) monitors every edge with at least one pair in \(S\); \(\operatorname{meg}(G)\) is its minimum cardinality. The theorem is claimed only for \(m,n\ge5\).

## Proof

**Step 1 (fiber reduction and lower bound).** If two endpoints of a shortest path in a Cartesian product differ in both coordinates, the coordinate moves can be made first in either order, producing two edge-disjoint shortest paths. Thus such a pair cannot monitor any one edge. When the endpoints share a coordinate, their shortest paths lie in the corresponding one-dimensional fiber. Consequently a vertex set is an MEG-set of \(C_m\square C_n\) if and only if its intersection with each \(C_m\) column and each \(C_n\) row is an MEG-set of the respective cycle. This is also the fiber characterization proved in Haslegrave's Theorem 1 [1]. Since \(\operatorname{meg}(C_k)=3\) for \(k\ge5\) [2], every one of the \(n\) columns contains at least three probes, giving \(\operatorname{meg}(C_m\square C_n)\ge3n\). Interchanging coordinates gives the lower bound \(3\max\{m,n\}\).

**Step 2 (exact cycle test).** For a selected set \(A\subseteq\mathbb Z/k\mathbb Z\) with at least two distinct vertices, arrange its elements around the cycle. Let \(h_1,\ldots,h_r\) be the positive cyclic differences between consecutive selected vertices, with sum \(k\). Then
\[
 A\text{ is an MEG-set of }C_k\quad\Longleftrightarrow\quad 2h_i<k\ \text{for every }i.
\]
Indeed, each gap of length less than half the cycle is the unique shortest path between its consecutive selected endpoints; these paths monitor all cycle edges. Conversely, an edge strictly inside a gap of length at least half the cycle could only lie on a selected-endpoint geodesic by traversing the entire gap. The complementary route is shorter if the gap is longer than half the cycle, or is an equally short route avoiding the edge if the gap equals half. Thus no selected pair monitors that edge. In particular, three points with all cyclic gaps less than half are enough.

**Step 3 (balanced-floor placement).** By coordinate symmetry assume \(5\le m\le n\). Put
\[
 T=\{0,\lfloor m/3\rfloor,\lfloor2m/3\rfloor\}\subseteq\mathbb Z/m\mathbb Z,
 \qquad g=\lceil m/3\rceil.
\]
All three cyclic gaps of \(T\) are at most \(g<m/2\). At every column \(j\in\{0,\ldots,n-1\}\), choose the triple
\[
 S_j=\bigl\{(t-\lfloor mj/n\rfloor)\bmod m:t\in T\bigr\}.
\]
The resulting probe set \(S=\bigcup_{j=0}^{n-1}(S_j\times\{j\})\) has exactly \(3n\) vertices and each column is an MEG-set.

It remains to check the rows. The function \(f(j)=\lfloor mj/n\rfloor\) takes every integer \(v\in\{0,\ldots,m-1\}\) on one nonempty consecutive block of columns, since \(n\ge m\). The block starts at
\[
 J_v=\lceil vn/m\rceil,\qquad J_{v+m}=J_v+n.
\]
For a fixed row \(i\), the selected blocks are exactly those for which \(f(j)\equiv t-i\pmod m\) for one of the three \(t\in T\). Their cyclic residue gaps are at most \(g\). For two successive selected residue blocks \(v\) and \(v+h\), with \(1\le h\le g\), the longest gap of selected column indices starts at the last column \(J_{v+1}-1\) of the first block and ends at the first column \(J_{v+h}\) of the second. Its length is
\[
 J_{v+h}-J_{v+1}+1
 \le1+\left\lceil\frac{(h-1)n}{m}\right\rceil
 \le B(m,n):=1+\left\lceil\frac{(g-1)n}{m}\right\rceil.
\]
Gaps within a block are one. Because \(g-1<m/3\), we have \(B(m,n)<2+n/3\). For all \(n\ge12\), this is strictly below \(n/2\), and Step 2 proves the row condition. For the finite range \(5\le m\le n\le11\), directly substituting the seven possible \(m\)-values into the displayed explicit ceiling expression shows \(2B(m,n)\ge n\) only for \((m,n)=(5,6)\) and \((7,8)\). All other pairs satisfy Step 2.

**Step 4 (the two exceptional dimensions).** For \((m,n)=(5,6)\), take the three rows \(\{1,3,4\}\) in each even column and \(\{0,2,4\}\) in each odd column. Every column has circular gaps \(1,2,2\); each row is either present in all columns or in the three columns of one parity, so the largest row gap is \(2<6/2\). Thus the set of size \(18\) is an MEG-set.

For \((m,n)=(7,8)\), the triples of selected row indices in columns \(0\) through \(7\) are
\[
(0,2,4),\ (2,4,6),\ (1,3,5),\ (0,2,5),\ (1,4,6),\ (0,3,5),\ (2,4,6),\ (1,3,5).
\]
Their maximum circular column gap is \(3<7/2\). The selected column positions in rows \(0\) through \(6\), respectively, are
\[
\begin{gathered}
(0,3,5),\ (2,4,7),\ (0,1,3,6),\ (2,5,7),\\
(0,1,4,6),\ (2,3,5,7),\ (1,4,6).
\end{gathered}
\]
All of these have maximum circular gap \(3<8/2\). Hence this set of size \(24\) is an MEG-set. The upper bound \(3n\) is proved in every case, and Step 1 completes the theorem. \(\square\)

## Verification

The accompanying standard-library `verify.py` implements both the balanced-floor construction and the two small certificates. It exhausts all \(8160\) subsets of cycles of orders \(5\) through \(12\) to compare the cyclic-gap criterion with shortest-arc edge monitoring, checks the finite arithmetic exception list, verifies the complete row/column certificates for \(5016\) pairs with \(5\le m\le70\) and \(m\le n<\min(3m+1,211)\), and independently removes each edge and recomputes probe-pair distances in eight representative toroidal grids, including the two exceptions. Execute `python3 verify.py` from a directory containing this file and `verify.py`. The general assertion relies on the proof above, not on finite enumeration.

## Relationship to prior work

Haslegrave [1, Theorem 1] gives the Cartesian-product fiber condition and lower bound. His Theorem 4 establishes equality for **square** tori \(C_m\square C_m\) by a diagonal construction; that proof does not directly supply the unequal-side placements. The present theorem supplies an exact formula for every rectangle, with a balanced-floor construction and two nonuniform boundary certificates. Dev, Dey, Foucaud, Narayanan, and Ramasubramony Sulochana [2] establish the cycle parameter and path-grid cases. Xu et al. [3] consider other product operations (their accessible abstract names join, corona, cluster, lexicographic, and direct products). Tan et al. [4] consider ladder, butterfly, circulant and Beneš networks, a nearby graph-network context; their full text was not accessible for comparison.

## Limitations

This is a theorem only about the **Cartesian** product of two simple cycles of order at least five. No claim is made for smaller cycles, strong products, general twisted tori, uniqueness of optimal sets, or the number of optimal sets. The published square case is acknowledged, not claimed as new. The scientific comparison used accessible full text for [1] and [2], but some relevant publisher full texts [3] and [4] were inaccessible; hence a risk remains that a previously unstated transformation or result in that literature subsumes part of this theorem. The finite program is a reproducibility check, not independent validation or a substitute for the proof.

## References

[1] John Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955, first posted 17 October 2022, Theorems 1 and 4. https://arxiv.org/abs/2210.08955

[2] Subhadeep R. Dev, Sanjana Dey, Florent Foucaud, Krishna Narayanan, and Lekshmi Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774, 2022 preprint; see the cycle and path-grid sections. https://arxiv.org/abs/2210.03774

[3] Xin Xu, Chenxu Yang, Gemaji Bao, Ayun Zhang, and Xuan Shao, *Monitoring-edge-geodetic sets in product networks*, International Journal of Parallel, Emergent and Distributed Systems 39 (2024), 264–277. DOI:10.1080/17445760.2024.2301929

[4] Ao Tan, Wen Li, Xiumin Wang, and Xin Li, *Monitoring edge-geodetic numbers of convex polytopes and four networks*, International Journal of Parallel, Emergent and Distributed Systems 38 (2023), 301–312. DOI:10.1080/17445760.2023.2220143
