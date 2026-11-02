# Edge-open-packing polynomial and all maximum configurations of rectangular rook graphs

## Finding
For integers \(m,n\ge2\), write \(R_{m,n}=K_m\square K_n\), with vertex set \([m]\times[n]\). Two squares are adjacent when they share a row or a column. An **edge-open-packing** is a subset \(B\subseteq E(R_{m,n})\) such that any two distinct edges in \(B\) have no *third* edge joining one endpoint of the first to one endpoint of the second. The first or second edge itself is not counted as a third edge. Let \(E_{m,n}(z)=\sum_{B}z^{|B|}\), summing over all edge-open-packings, including the empty set.

The complete edge-open-packing polynomial is
\[
E_{m,n}(z)=\sum_{\substack{a,b,c\ge0\\2a+b+2c\le m\\2a+2b+c\le n}}
\frac{m!n!}{2^{b+c}a!b!c!(m-2a-b-2c)!(n-2a-2b-c)!}\,z^{2a+b+c}.
\]
The maximum size is
\[
\rho_e^o(R_{m,n})=\min\{m,n\}-\mathbf1_{\{m=n\text{ is odd}\}}.
\]
Every maximum packing has the unique component decomposition described in the proof. Its exact labeled count is as follows. When \(m<n\), put \(b=m-2a\) and sum over nonnegative integers \(a\) for which \(b\ge0\) and \(m+b\le n\):
\[
N_{m,n}=\sum_{\substack{a\ge0,\ b=m-2a\ge0\\m+b\le n}}\frac{m!n!}{2^b a!b!(n-m-b)!}.
\]
For \(n<m\), interchange the arguments. When \(m=n=2k\),
\[
N_{2k,2k}=\frac{((2k)!)^2}{k!}.
\]
When \(m=n=2k+1\),
\[
N_{2k+1,2k+1}=((2k+1)!)^2\left(\frac1{k!}+\frac1{4(k-1)!}\right).
\]
These counts classify all labeled maxima; no additional configuration types occur.

## Assumptions and scope
All graphs are finite, undirected, and simple. The orders \(m,n\) are integers at least two. Horizontal means an edge joining two distinct columns in one fixed row, and vertical means an edge joining two distinct rows in one fixed column. A two-edge **corner** is a path on three squares contained in a \(2\times2\) sub-board, meeting at the square at its bend. For two such corners, or a corner and a single edge, *disjoint supports* means that both their row-index sets and their column-index sets are disjoint. All factorials have nonnegative integer arguments, and \(0!=1\).

## Proof
**1. Shape lemma.** Let \(B\) be an edge-open-packing in the rook graph and let \(S\) consist of all endpoints of its edges. For two edges of \(B\), a third edge between their endpoints is forbidden. Thus the graph induced by \(S\) is a disjoint union of stars whose edges are precisely \(B\). Conversely, the edges of any induced disjoint union of stars constitute an edge-open-packing: any putative third joining edge would either connect separate components or connect two leaves in one star. (A center-to-leaf edge is already one of the two selected edges, not a third.)

At a rook-graph vertex, all neighbors in its row form a clique and all neighbors in its column form a clique. An induced star therefore has at most one leaf in the row direction and at most one in the column direction. Accordingly its nontrivial components are exactly: a two-edge corner with two rows and two columns; a horizontal single edge with one row and two columns; or a vertical single edge with two rows and one column. Distinct components cannot share a row index or a column index, because otherwise one endpoint from each component would be adjacent. Conversely any collection of these components with disjoint row and column supports gives an induced union of stars. This proves a bijection between edge-open-packings and these three-component collections.

**2. Counting all sizes.** Let \(a,b,c\) be the numbers of corners, horizontal edges, and vertical edges. Their edge count is \(t=2a+b+c\), their row-index use is \(R=2a+b+2c=t+c\), and their column-index use is \(C=2a+2b+c=t+b\). The constraints are \(R\le m\), \(C\le n\).

Partitioning the selected labeled rows into \(a\) unordered pairs for corners, \(b\) singletons for horizontal edges, and \(c\) unordered pairs for vertical edges (and unused rows) can be done in
\[
\frac{m!}{2^{a+c}a!b!c!(m-R)!}
\]
ways. Independently, partitioning the columns into \(a\) unordered pairs for corners, \(b\) unordered pairs for horizontal edges, and \(c\) singletons for vertical edges takes
\[
\frac{n!}{2^{a+b}a!b!c!(n-C)!}
\]
ways. Match like-type row and column groups in \(a!b!c!\) ways and choose one of four corner centers per matched \(2\times2\) rectangle (\(4^a\) ways). Their product simplifies exactly to the coefficient in the displayed polynomial. Each packing has one such decomposition, so no overcount or omission is possible.

**3. Maximum size.** Since \(R=t+c\le m\) and \(C=t+b\le n\), always \(t\le\min(m,n)\). If \(m=n\) is odd and \(t=m\), the inequalities force \(b=c=0\); then \(t=2a\) is even, contradiction. Hence \(t\le m-1\) on an odd square. For the converse suppose \(m<n\). We may choose \(a=\lfloor m/2\rfloor\), \(b=m-2a\in\{0,1\}\), and \(c=0\). This uses exactly \(m\) rows and \(m+b\le n\) columns, so attains \(t=m\). Interchanging axes treats \(n<m\). For even squares take \(a=m/2\), \(b=c=0\), attaining \(t=m\). For odd squares take \(a=(m-1)/2\), \(b=c=0\), attaining \(t=m-1\). This gives the formula in every case.

**4. Complete equality cases and counts.** If \(m<n\), equality \(t=m\) forces \(c=0\), whence \(b=m-2a\ge0\) and \(C=m+b\le n\). Thus every maximum consists exactly of \(a\) pairwise-support-disjoint corners and \(b\) horizontal single edges, with the indicated constraints. Summing the polynomial coefficients over these allowed \(a\) gives \(N_{m,n}\). For even squares equality forces \(b=c=0\), hence \(a=m/2\) and the first square count. For odd squares, let \(m=2k+1\) and \(t=2k\). The row/column constraints imply \(b,c\le1\). Since \(b+c\) is even, either \((b,c)=(0,0)\), with \(a=k\), or \((b,c)=(1,1)\), with \(a=k-1\). Applying the polynomial coefficient to both cases yields the two terms in the odd-square count. No other maximizers exist by the shape lemma.

## Verification
A standalone C++17 program, `check_rook.cpp`, constructs the rook graph from the adjacency definition. For every pair of candidate selected edges it tests the original forbidden-third-edge predicate directly, without using the component-counting argument. Independent exhaustive enumeration checks every cardinality coefficient, the exact maximum, its number of realizations, and the absence of larger packings, for \((m,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5)\). It finishes with `VERIFY_OK`. Compile using `g++ -O3 -std=c++17 check_rook.cpp -o check_rook`, then execute `./check_rook`.

The computation verifies a finite range only. The unrestricted theorem is proved by the bijection, resource inequalities, and exact labeled enumeration above.

## Relationship to prior work
Edge-open-packings and their standard induced-disjoint-stars interpretation are defined and studied in Brešar–Samadi (2024), which supplies complexity and general bounds; its graph-product successor by Brešar–Dravec–Hedžet–Samadi (2024) gives a Cartesian-product **lower bound**, not a rook-graph enumeration. The complete polynomial and the parity-sensitive extremizer classification here are stronger, differently quantified assertions than those published general product inequalities. Neither inspected primary full text states or implies this exact two-parameter polynomial or the labeled equality cases. Targeted literature and record searches did not reveal a preexisting equivalent formula; search incompleteness remains an originality risk.

## Limitations
The result applies to the Cartesian product of exactly two complete graphs of orders at least two, not to arbitrary Hamming graphs or other graph products. The coefficient polynomial counts labeled vertex-coordinate configurations. Exhaustive code checks only the eleven finite board sizes listed above and do not certify the infinite theorem independently. An unindexed equivalent result or a source not inspected in full could affect publication priority.

## References
1. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1, first posted 2024-03-01, https://arxiv.org/abs/2403.00750 .
2. B. Brešar, T. Dravec, J. Hedžet, and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020v1, first posted 2024-06-06, https://arxiv.org/abs/2406.04020 .
3. *Edge open packing sets in graphs*, RAIRO—Operations Research 56 (2022), 3765–3776 (original foundational source cited in References 1–2; its complete text was not inspected in this study).
