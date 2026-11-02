# Sharp inclusion-minimal fort sizes in rectangular rook graphs

## Finding

For integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\) be the rook graph on the cells of an \(m\)-by-\(n\) board. A **fort** is a nonempty vertex set \(F\) such that each vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is **inclusion-minimal** when it contains no strictly smaller nonempty fort. Write \(\rho(G)\) for the largest cardinality of an inclusion-minimal fort of \(G\), equivalently the rank (largest hyperedge cardinality) of its minimal-fort hypergraph.

Then, for all \(m,n\ge2\),
\[
\boxed{\rho(R_{m,n})=m+n-2+\mathbf{1}_{\{|m-n|=1\}}.}
\]

In particular square boards have rank \(2n-2\), while boards with dimensions differing by exactly one have rank \(m+n-1\). Both terms of the formula are attained by explicit minimal forts.

## Assumptions and scope

Graphs are finite simple undirected graphs. The Cartesian product convention is that distinct board cells are adjacent if and only if they share a row or column. All occurrences of “minimal” mean minimal under inclusion among **all nonempty forts**; deleting one vertex without breaking the fort property is not a sufficient test for minimality. The theorem concerns maximal *size of a minimal fort*, not the minimum fort size, number of minimal forts, or maximum number of pairwise disjoint forts.

Identify an \(m\)-by-\(n\) collection \(F\) of cells with an edge subset of \(K_{m,n}\). The incidence graph \(B_F\) has the \(m\) row-vertices and \(n\) column-vertices, including isolates, and edge \(ij\) for each selected cell \((i,j)\). Degrees \(d_i\) and \(e_j\) refer to this incidence graph.

## Proof

**Incidence criterion.** For a cell \((i,j)\notin F\), its number of neighbors in \(F\) equals \(d_i+e_j\). Therefore \(F\) is a fort precisely when (i) any empty row coexists with no column of degree one and (ii) any empty column coexists with no row of degree one. Equivalently there is no unselected cell incident to exactly one selected cell. This criterion includes all empty-row/empty-column boundary cases.

**Upper bound, cyclic case.** Suppose \(F\) is inclusion-minimal and \(B_F\) contains a cycle \(C\). Because \(B_F\) is bipartite, \(C\) is even, and its edge set by itself is a fort: each row- or column-vertex has degree zero or two in that selected edge set; hence any unselected cell has zero, two, or four selected rook neighbors. Minimality forces \(F\) to equal this cycle edge set. If \(m\ne n\), the cycle uses at most \(\min(m,n)\) row-vertices and the same number of column-vertices, whence \(|F|\le2\min(m,n)\). If \(m=n\) and the cycle visits all \(n\) rows and columns, its alternating perfect matching is a strictly smaller fort: with one selected cell in each row and each column, every unselected cell has exactly two selected neighbors. Thus such a spanning cycle is not minimal, and every cyclic minimal fort on a square board has \(|F|\le2n-2\).

**Upper bound, acyclic case.** Suppose \(B_F\) is a forest. If it has at least two components, including any isolated row or column, then \(|F|\le(m+n)-2\). If it has one component, it is a tree spanning the full \(m+n\) incidence vertices. Because both bipartition classes have at least two vertices, this spanning tree is not a star and has an edge whose endpoints both have degree at least two (take the middle edge along a leaf-to-leaf path of length at least three). Delete such an edge. All row and column vertices still have positive degree. The remaining nonempty cell set is therefore a fort by the incidence criterion, contradicting minimality. Thus every acyclic minimal fort also has cardinality at most \(m+n-2\).

Combining the cases gives
\[
|F|\le
\begin{cases}
\max(m+n-2,2n-2),&m=n,\\
\max(m+n-2,2\min(m,n)),&m\ne n,
\end{cases}
=m+n-2+\mathbf1_{\{|m-n|=1\}}.
\]

**Lower bound, cross construction.** Fix a row \(r\) and column \(c\). Let \(F_\times\) comprise all \(n-1\) cells in row \(r\) except \((r,c)\), together with all \(m-1\) cells in column \(c\) except \((r,c)\). The two arms have disjoint supports in the incidence graph; each row and each column has positive degree, so \(F_\times\) is a fort of size \(m+n-2\).

To prove inclusion-minimality, take a nonempty proper subset \(T\subsetneq F_\times\). If \(T\) uses both arms, at least one arm is incomplete; omitting a cell in the horizontal arm creates an empty column while any selected cell of the vertical arm leaves a row of degree one, violating the incidence criterion. Omitting a cell in the vertical arm gives the transposed violation. If \(T\) uses only the horizontal arm, then some row is empty and some selected column has degree one, again violating the criterion; the vertical-only case is symmetric. Hence no proper nonempty subset is a fort, proving \(\rho(R_{m,n})\ge m+n-2\).

**Consecutive-side improvement.** Suppose \(n=m+1\); the transposed argument covers \(m=n+1\). Choose any simple cycle \(C\) of length \(2m\) in \(K_{m,n}\), using all \(m\) rows and exactly \(m\) columns; such a cycle exists even when \(m=2\). Its edge set is a fort, and has \(2m=m+n-1\) elements. Every proper nonempty edge subset \(T\) of \(C\) has at least one empty column (the unused column of \(K_{m,n}\)). If \(T\) were a fort, the incidence criterion would force every nonempty row of \(T\) to have degree at least two; because each row in \(C\) has degree two, this forces either both of its cycle edges to be included or neither. As the cycle is connected, retaining any edge then forces all cycle edges, contradicting propriety. Therefore \(C\) is inclusion-minimal and attains \(m+n-1\). Together with the upper bound, this finishes the proof. \(\square\)

## Verification

Run `python3 verify.py` using Python 3.8 or newer. This implementation builds the original rook-graph adjacency independently from the incidence proof, checks the fort condition for **every** subset of ten labeled boards, and uses a proper-subset dynamic program (not a one-element-deletion test) to identify inclusion-minimal forts. The boards are \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)\). Across these ten boards the procedure checks 1,414,992 subset masks including the empty mask and compares the exact largest inclusion-minimal fort cardinality with the theorem. The exhaustive finite check passed. The universal conclusion comes from the proof above; the code verifies finite examples only.

## Relationship to prior work

The literature of fort hypergraphs links forts to failed zero-forcing configurations, fractional zero forcing, and Cartesian graph products. The work of Cameron, Hogben, Kenter, Mojallal and Schuerger studies forts and the maximum number of pairwise disjoint forts under products; that “fort number” is not the rank of the hypergraph of inclusion-minimal forts. Becker, Cameron, Hanely, Ong and Previte investigate the **number** of inclusion-minimal forts in various graph families and the complement correspondence with maximal failed zero-forcing sets; their inspected family results do not give the largest inclusion-minimal fort in every rectangular rook graph. The present result specifies this different extremal cardinality uniformly for all rectangles, including the consecutive-dimension exception. This literature comparison is not a claim of exhaustive publication priority.

## Limitations

The theorem does not enumerate all minimal forts, compute the fractional cover number, or determine the upper zero forcing number. Its novelty has not been independently established against every possible alternative formulation or unindexed publication. The code covers only the listed finite parameters; no general inference rests on exhaustive computations.

## References

1. A. Cameron, L. Hogben, F. Kenter, D. Mojallal, and H. Schuerger, “Forts, (fractional) zero forcing, and Cartesian products of graphs,” arXiv:2310.17904 (first public version 27 October 2023), https://arxiv.org/abs/2310.17904.
2. C. Becker, A. Cameron, J. Hanely, D. Ong, and R. Previte, “On the number of minimal forts of a graph,” arXiv:2404.05963 (first public version 9 April 2024), https://arxiv.org/abs/2404.05963.
