# Super domination of three-row grids and rigidity at even width

## Finding

For every integer \(n\geq1\), the super domination number of the Cartesian grid \(G_n=P_3\square P_n\) is
\[
\gamma_{\mathrm{sp}}(G_n)=
\begin{cases}
2,&n=1,\\
5,&n=3,\\
3n/2,&n\geq2\text{ even},\\
3(n+1)/2,&n\geq5\text{ odd}.
\end{cases}
\]
Moreover, for every even integer \(n\geq2\), there are **exactly two** minimum super dominating sets: the union of all three vertices in alternating columns, with either choice of column parity.

## Assumptions and scope

The path \(P_k\) has vertices \(1,\ldots,k\) and edges joining consecutive integers (including the one-vertex path). The Cartesian product \(G_n=P_3\square P_n\) has vertices \((r,j)\), \(1\leq r\leq3\), \(1\leq j\leq n\), with edges between vertices that differ by one in exactly one coordinate. The open neighborhood of \(v\) is \(N(v)\). A set \(D\subseteq V(G_n)\) is *super dominating* when each \(u\notin D\) has a witness \(v\in D\) satisfying \(N(v)\cap(V(G_n)\setminus D)=\{u\}\). The minimum cardinality of such a set is \(\gamma_{\mathrm{sp}}(G_n)\). There are no asymptotic assumptions and no restrictions on the parity beyond the cases in the formula.

## Proof

**1. An exact five-column local rule.** Represent the *omitted* vertices \(V(G_n)\setminus D\) in column \(j\) by a three-bit mask \(a_j\in\{0,\ldots,7\}\). Add virtual zero masks outside the grid; virtual vertices must never be used as witnesses. The witness property for an omitted vertex in column \(j\) can be decided using only \(a_{j-2},a_{j-1},a_j,a_{j+1},a_{j+2}\): its witness is in column \(j\) or an adjacent column, and all neighbors of that witness lie at distance at most two columns from \(j\). For the first and last columns, forbid witness candidates outside the actual grid. The Boolean predicate `local_ok` in `verify.py` implements precisely these four candidate-witness directions and counts all omitted neighbors of each candidate. Thus all local predicates hold if and only if \(D\) is super dominating.

**2. Exact max-plus transfer.** Let \(V_t(s)\), indexed by four consecutive three-bit masks \(s\), be the largest number of omitted vertices in the first \(t\) real columns among all mask sequences with last four masks \(s\) whose local tests for columns through \(t-2\) have passed. Prefixes use virtual zero masks on the left, and the test at the first real column excludes imaginary left witnesses. Impossible states have value \(-\infty\). Upon appending a new mask, shift the four-mask state, add its number of one-bits, and check the newly completed five-mask local window. Take the maximum over predecessors with equal new state. This is a fixed max-plus linear transfer \(T\) once at least three real columns have been processed. In particular, a constant shift of all finite entries commutes with \(T\).

**3. A finite induction certificate, not a numerical extrapolation.** The self-contained `verify.py` generates the complete exact state vectors through width \(12\), with all integers represented exactly, and checks the identities
\[
V_{11}=V_9+3,\qquad V_{12}=V_{10}+3,
\]
where equality includes *identical supports of states*, each of size \(1543\). These are the entire reachable state vectors, not just their maximum entries. Max-plus homogeneity and identical transitions then give
\[
V_{t+2}=V_t+3\qquad\text{for every integer }t\geq9
\]
by induction, separately in the two parities. Append two virtual zero columns to test the last two actual columns, forbidding a rightward witness beyond the boundary in the last test. Both terminal transfers are independent of \(t\) for \(t\geq9\) and preserve constant shifts. Therefore if \(M_n\) is the largest possible number of omitted vertices, then \(M_{n+2}=M_n+3\) for all \(n\geq9\). Since \(\gamma_{\mathrm{sp}}(G_n)=3n-M_n\), the same increment of three holds for the super domination number. The checker also verifies the **exact** finite base values at every integer width from \(1\) through \(12\):
\[
(2,3,5,6,9,9,12,12,15,15,18,18).
\]
These base values and the proved two-step recurrence imply the claimed piecewise formula for *all* positive integers \(n\). Every assertion used to propagate the infinite family is a deterministic finite identity with its complete computation included in `verify.py`.

**4. All minimum sets for even widths.** For any super dominating set \(D\) on an even-order graph, the injection assigning one selected witness to each omitted vertex gives \(|D|\geq |V|/2\). Equality forces each selected vertex to have exactly one neighbor outside \(D\), and each omitted vertex to have exactly one neighbor in \(D\): the edges of the cut \((D,V\setminus D)\) form a perfect matching. In a four-cycle, two crossing cut edges cannot meet and the number of crossing edges is even. Thus if any edge of a grid unit square crosses the cut, its opposite edge must also cross it. A horizontal crossing therefore propagates across all three rows at the same column boundary; a vertical crossing similarly propagates across all columns at the same row boundary. Horizontal and vertical crossings cannot coexist, because their propagated lines intersect at a vertex and would violate the perfect-matching condition. A purely vertical crossing perfect matching is impossible across the three rows (an odd path of rows). Consequently all crossing edges are horizontal, and they uniquely match consecutive columns in pairs, with boundaries \((1,2),(3,4),\ldots,(n-1,n)\). Each entire column is then monochromatic in the cut bipartition and consecutive columns alternate sides. Exactly two assignments of selected versus omitted columns result, and both satisfy the super domination condition (each selected vertex is the unique omitted neighbor's witness). Hence there are exactly two minimum sets for every even \(n\geq2\).

## Verification

Run `python3 verify.py` with a standard Python interpreter (no packages, input files, or internet required). It exhaustively constructs the exact transfer-state vectors, asserts support and entry-wise equality of the two critical identities, closes all twelve base cases, and independently tests every candidate vertex subset against the **original graph-neighborhood definition** for widths \(1\) through \(6\) (at most \(18\) vertices). The local and direct algorithms use different implementations. The base vectors, finite certificate, and brute-force cross-check were executed successfully. The induction proves the infinite statement; direct enumeration is an auxiliary consistency check only.

## Relationship to prior work

Klein, Rodríguez-Velázquez and Yi (2017, first public version 2 May 2017) proved the exact half-order super domination number for products with even path factors and lower/upper bounds for odd path factors, in particular Theorem 24 of arXiv:1705.00928v2. Our even-width **numerical** formula follows directly from that theorem and is **not claimed as new**. The new numerical assertion is exactness of their odd-path upper bound at three rows and odd widths \(n\geq5\), together with the exceptional square width \(3\). The complete **two-minimum-set rigidity** at even widths is additional structural information beyond a numerical minimum. Ghanbari, Jäger and Lehtilä (2022 preprint) studied super domination products and enumeration for other graph classes but did not state a three-row Cartesian-grid solution. Bujtás, Ghanbari and Klavžar (2023 preprint) address complexity and structural techniques, not this exact grid family. Integer \(\{2\}\)-domination of three-row grids is a distinct invariant and not equivalent to super domination.

## Limitations

The conclusion concerns Cartesian grids with exactly three rows, not arbitrary rectangles, toroidal grids, or other types of domination. The exact recurrence depends on the supplied finite-state certificate, for which the algorithm and every required state identity are supplied; it is not a short certificate that can be checked without performing the finite enumeration. Counts of minimum sets at odd widths are not determined by this result. The finite brute-force tests alone would not establish the infinite theorem, and no general theorem for larger fixed heights is claimed.

## References

1. D. J. Klein, J. A. Rodríguez-Velázquez and E. Yi, *On the super domination number of graphs*, first public arXiv submission 2 May 2017, arXiv:1705.00928v2, Section 4 and Theorem 24. https://arxiv.org/html/1705.00928v2
2. N. Ghanbari, G. Jäger and T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795v3, Sections 3–6. https://arxiv.org/html/2209.01795v3
3. Cs. Bujtás, N. Ghanbari and S. Klavžar, *Computational complexity aspects of super domination*, arXiv:2302.08862v1. https://arxiv.org/html/2302.08862v1
