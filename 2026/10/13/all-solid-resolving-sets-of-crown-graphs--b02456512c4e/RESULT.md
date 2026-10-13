# All solid-resolving sets of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted matched pairs \(P_i=\{a_i,b_i\}\). A set \(S\) is solid-resolving exactly when its complement \(T=V\setminus S\) satisfies
\[
T\subseteq A,\qquad T\subseteq B,\qquad\text{or}\qquad T\subseteq P_i\text{ for some }i.
\]
Consequently
\[
\beta^s(\operatorname{Cr}_n)=n,
\]
and the only solid-metric bases are \(A\) and \(B\).

Define
\[
F_s(G;z)=\sum_{S\text{ solid-resolving}}z^{|S|}.
\]
Then
\[
F_s(\operatorname{Cr}_n;z)=2z^n(1+z)^n-z^{2n}+nz^{2n-2}.
\]

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. The crown graph is connected for \(n\ge3\). We use the published characterization that \(S\) is solid-resolving exactly when, for every ordered pair of distinct vertices \(x,y\), some \(s\in S\) satisfies
\[
d(s,x)<d(s,y).
\]
In \(\operatorname{Cr}_n\), distinct same-side vertices are at distance \(2\), unmatched opposite-side vertices are at distance \(1\), and matched opposite-side vertices are at distance \(3\).

## Proof
Fix distinct indices \(i,j\). For the ordered pair \((a_i,a_j)\), the vertices strictly closer to \(a_i\) than to \(a_j\) are exactly
\[
\{a_i,b_j\}.
\]
Indeed, their distance pairs are \((0,2)\) and \((1,3)\), respectively; \(a_j,b_i\) favor the reverse order, and every vertex in any third matched pair has equal distance to \(a_i,a_j\). Hence any solid-resolving set satisfies
\[
S\cap\{a_i,b_j\}\ne\varnothing\qquad(i\ne j).
\tag{1}
\]
Thus its complement cannot contain an \(A\)-vertex and a \(B\)-vertex with different indices. If the complement meets only one side, it lies in \(A\) or \(B\); if it meets both sides, all omitted vertices have one common index and the complement lies in one \(P_i\). This proves necessity.

For sufficiency, suppose first that \(T\subseteq A\), so all of \(B\) is selected. A selected first vertex distinguishes itself. For first vertex \(a_i\): against \(a_j\), use \(b_j\), giving \(1<3\); against \(b_i\), use any \(b_j\) with \(j\ne i\), giving \(1<2\); against \(b_j\) with \(j\ne i\), choose \(b_k\) with \(k\notin\{i,j\}\), giving \(1<2\). Such \(k\) exists because \(n\ge3\). Thus \(S\) is solid-resolving. The case \(T\subseteq B\) is symmetric.

If \(T\subseteq P_i\), only the case \(T=P_i\) is new. Every selected first vertex again distinguishes itself. For omitted \(a_i\): against \(b_i\), use \(b_j\), giving \(1<2\); against \(a_j\), use \(b_j\), giving \(1<3\); against \(b_j\), use \(b_k\) for a third index, giving \(1<2\). The omitted \(b_i\) case is symmetric. Hence every listed complement type is valid.

The largest valid complements have size \(n\), and the only such complements are \(A\) and \(B\). Thus \(\beta^s(\operatorname{Cr}_n)=n\) and the only bases are the two sides.

For the enumerator, complements contained in \(A\) contribute \(z^n(1+z)^n\), and those contained in \(B\) contribute the same. The empty complement is counted twice, so subtract \(z^{2n}\). The only additional mixed complements are the \(n\) full pairs \(P_i\), each contributing \(z^{2n-2}\). This gives the formula.

## Verification
The included checker constructs each crown graph, computes all-pairs distances, and applies the ordered-pair solid-resolving criterion directly. For every \(3\le n\le9\), it tests every vertex subset, compares it with the complement classification, checks every enumerator coefficient, and verifies the exact basis family.

## Relationship to prior work
The foundational solid-metric paper proves the ordered-pair characterization used above and develops forced vertices, bounds, trees, cycles, products, and complexity results. Its searchable full text contains no occurrence of “crown,” “bipartite,” or “matching.”

A public 2020 preprint generalizes the notion to \(\ell\)-solid resolution, restates the \(\ell=1\) criterion, and studies general bounds, rook graphs, Cartesian products, and flower snarks. Its searchable text contains no crown or complete-bipartite specialization. Its journal form lists Mathematics Subject Classification \(05C12\) and \(05C69\).

Known crown results for edge metric, strong resolving, domination, and other distance variants do not imply the solid condition, which is directional for every ordered pair. The exact witness set \(\{a_i,b_j\}\) in (1) is the new structural obstruction.

## Limitations
The theorem concerns ordinary solid resolution, equivalently the \(1\)-solid case; it does not address \(\ell\)-solid dimension for \(\ell\ge2\). The disconnected graph \(\operatorname{Cr}_2\) is excluded. The foundational article has month-level public evidence from February 2019, but no exact public day was verified in the inspected sources; the metadata therefore uses the earliest inspected primary source with an exact date, 4 March 2020. The finite computation is corroborative only.

## References
1. A. Hakanen, V. Junnila, T. Laihonen, “The solid-metric dimension,” Theoretical Computer Science 806 (2020), 156–170, DOI 10.1016/j.tcs.2019.02.013.
2. A. Hakanen, V. Junnila, T. Laihonen, M. L. Puertas, “On the Metric Dimensions for Sets of Vertices,” arXiv:2003.02048v1, 4 March 2020; Discussiones Mathematicae Graph Theory 43(1) (2023), 245–275, DOI 10.7151/dmgt.2367.
