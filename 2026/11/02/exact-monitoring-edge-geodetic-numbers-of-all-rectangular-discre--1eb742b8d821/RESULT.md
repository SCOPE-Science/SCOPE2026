# Exact monitoring edge-geodetic numbers of all rectangular discrete tori

## Finding

For every pair of integers \(m,n\ge 3\), let \(T_{m,n}=C_m\square C_n\) be the Cartesian product of the simple cycles. Let \(\operatorname{meg}(G)\) be the minimum size of a vertex set \(S\) such that for each edge \(e\) of \(G\), at least one pair of vertices in \(S\) has \(e\) on **every** shortest path joining the pair. Then

\[
\operatorname{meg}(T_{m,n})=
\begin{cases}
mn,&\min\{m,n\}\le4,\\
3\max\{m,n\},&m,n\ge5.
\end{cases}
\]

The new assertion is the sharp, all-aspect-ratio rectangular case \(m,n\ge5\), including unequal factors. The square case and the general product lower bound were already established by Haslegrave; the small-factor case follows from his product characterization together with the known cycle values. An explicit optimal selection is provided below for every pair of dimensions.

## Assumptions and scope

Graphs are finite, simple, undirected, unweighted, and connected. The cycle \(C_k\) has vertex set \(\mathbb Z/k\mathbb Z\), with consecutive residues adjacent, and \(k\ge3\). Distances are ordinary edge-count distances. In the construction take \(5\le m\le n\), which involves no loss of generality because the Cartesian product is commutative up to isomorphism. Each coordinate is interpreted modulo its corresponding cycle length.

A finite cyclic set of at least two selected vertices has a *circular gap* \(g\) when consecutive selected vertices along the positive cyclic order are separated by \(g\) edges. If all such gaps are strictly less than half the cycle length, then the selected set monitors the cycle: each gap is the **unique** shortest path between its two endpoints, and these paths cover every cycle edge. In particular, for every \(k\ge5\), the three residues

\[
R_k=\left\{0,\left\lfloor\frac{k}{3}\right\rfloor,\left\lfloor\frac{2k}{3}\right\rfloor\right\}
\]

form a monitoring edge-geodetic set, since their gaps are at most \(\lceil k/3\rceil<k/2\). No two selected vertices can monitor all the edges of a cycle (they monitor at most one shortest arc), hence \(\operatorname{meg}(C_k)=3\) for \(k\ge5\). The shorter cycles \(C_3\) and \(C_4\) both require all of their vertices.

## Proof

**1. Cartesian fibers and the lower bound.** Haslegrave's Cartesian-product monitoring lemma states that \(S\subseteq V(G\square H)\) monitors every edge if and only if each of its \(G\)-fibers is a monitoring edge-geodetic set of \(G\) and each of its \(H\)-fibers is such a set of \(H\). For completeness: a shortest path between vertices differing in both coordinates can traverse the first coordinate before the second or vice versa, yielding two edge-disjoint shortest paths. Such a pair cannot force an individual edge. If the endpoints agree in one coordinate, all their shortest paths lie in the corresponding coordinate fiber. This proves the fiber criterion.

For \(5\le m\le n\), each of the \(n\) fibers isomorphic to \(C_m\) consequently requires at least three selected vertices. Therefore \(\operatorname{meg}(T_{m,n})\ge3n\). If a factor is \(C_3\) or \(C_4\), every fiber parallel to that factor must contain all vertices, so every vertex of the product is selected and \(\operatorname{meg}(T_{m,n})=mn\).

**2. Balanced construction.** Assume \(5\le m\le n\), except for the two pairs \((m,n)=(5,6),(7,8)\). Set

\[
R=\left\{0,\left\lfloor m/3\right\rfloor,\left\lfloor2m/3\right\rfloor\right\},\qquad
f(j)=\left\lfloor\frac{mj}{n}\right\rfloor\quad(0\le j<n).
\]

In column \(j\), select precisely those vertices whose first coordinate lies in \(R+f(j)\pmod m\). Every column consists of a rotation of \(R\), hence is a monitoring edge-geodetic triple in \(C_m\). There are exactly \(3n\) selected vertices.

We verify every row \(i\) is a monitoring edge-geodetic set of \(C_n\). Its selected columns are exactly those \(j\) with \(f(j)\) in the three-residue set \(i-R\pmod m\). The map \(f\) is a nondecreasing surjection onto \(0,1,\ldots,m-1\); the columns realizing residue \(r\) are the consecutive integers

\[
\left\lceil\frac{rn}{m}\right\rceil\le j
\le\left\lceil\frac{(r+1)n}{m}\right\rceil-1.
\]

The consecutive circular gaps among the three selected residues in \(\mathbb Z/m\mathbb Z\) are at most \(g=\lceil m/3\rceil\). If two successive selected residues are separated by \(h\) residual steps (so \(1\le h\le g\)), the difference between the last selected column in the first residual block and the first selected column in the next is at most

\[
\left\lceil\frac{(h-1)n}{m}\right\rceil+1.
\]

This holds also across the cyclic wrap, using \(\lceil x+n\rceil=\lceil x\rceil+n\). Consequently every row's largest circular gap is at most

\[
U(m,n)=\left\lceil\frac{\lfloor(m-1)/3\rfloor n}{m}\right\rceil+1.
\]

For \(n\ge13\), the bound satisfies

\[
U(m,n)\le\left\lceil n/3\right\rceil+1<n/2.
\]

For the remaining \(5\le m\le n\le12\), direct substitution in the explicit integer expression for \(U(m,n)\) shows that \(2U(m,n)<n\) except for \((5,6)\) and \((7,8)\). There are 36 parameter pairs in this finite elementary arithmetic check; `verify.py` reproduces all of them using integer-only arithmetic. Hence the balanced construction monitors every row and every column for all nonexceptional parameters.

**3. Two small exceptional constructions.** Write each column as the three selected first-coordinate residues, in increasing column order. For \((m,n)=(5,6)\), take

\[
\{0,2,4\},\ \{1,3,4\},\ \{0,2,4\},\ \{0,1,3\},\ \{1,2,4\},\ \{0,1,3\}.
\]

Every column has largest circular gap two; every row has largest circular gap two. In both directions these gaps are less than half the cycle length.

For \((m,n)=(7,8)\), take

\[
\begin{gathered}
\{0,2,5\},\ \{2,4,6\},\ \{1,3,5\},\ \{0,1,4\},\\
\{2,3,6\},\ \{1,2,5\},\ \{0,1,4\},\ \{1,3,6\}.
\end{gathered}
\]

Every column has largest circular gap at most three, and every row has largest circular gap at most three; these are strictly less than half of seven and eight, respectively. Thus the fiber criterion applies also in both exceptional cases.

The constructed set has exactly three vertices per column, meeting the lower bound \(3n\). This proves the formula for \(m,n\ge5\). Combining with the small-factor argument proves the stated classification for every \(m,n\ge3\).

## Verification

The standalone Python 3 program `verify.py` recomputes the exact small-parameter arithmetic exception list, checks every cyclic fiber in 7,491 parameter pairs with \(5\le m\le70\) and \(m\le n\le150\), and separately builds the full graph and tests edge deletion using breadth-first searches for 14 products with \(5\le m\le8\), \(m\le n\le9\). The independent graph-level test covers 1,318 edges. An additional 16 direct graph tests show that deleting one selected vertex destroys monitoring whenever a cycle factor has order three or four. Its expected result is:

`VERIFY_OK: 36 arithmetic small pairs; 7491 cycle-slice parameter pairs; 14 independent adjacency/BFS graph cases; 1318 edge-deletion checks; 16 forced-small-factor graph cases`

These finite tests are reproducibility checks, **not** a substitute for the universal gap bound and the two explicit exceptional arrays.

## Relationship to prior work

Dev, Dey, Foucaud, Narayanan, and Ramasubramony Sulochana introduced monitoring edge-geodetic sets and computed the monitoring numbers of cycles (arXiv:2210.03774; first posted October 7, 2022). Haslegrave derived the fiber characterization and sharp general Cartesian-product bounds, and proved the square-torus identity \(\operatorname{meg}(C_m\square C_m)=3m\) for \(m\ge5\) (arXiv:2210.08955, Theorem 4; first posted October 17, 2022). These facts are used and credited, not claimed as new. The contribution here is that **all rectangular aspect ratios** attain the universal Cartesian-product lower bound; the balanced stretched construction and two short exceptional arrays establish this for arbitrary unequal cycle lengths. The product-network results in the 2024 article address several other graph products; its publicly available abstract does not assert this rectangular Cartesian formula.

## Limitations

Only ordinary unweighted Cartesian products of two simple cycles are classified. Nothing is claimed for twisted tori, direct or strong products, or the structure and number of *all* optimal monitoring sets. The literature comparison is limited by indexing and access: the full 2024 product-networks article was not inspected, and unindexed equivalent results cannot be ruled out. No independent mathematical review has been completed.

## References

1. S. R. Dev, S. Dey, F. Foucaud, K. Narayanan and L. Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774, first posted 2022-10-07. https://arxiv.org/abs/2210.03774 . Full text inspected: https://arxiv.org/html/2210.03774v3 .
2. J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955, first posted 2022-10-17; Discrete Applied Mathematics 340 (2023), 79–84. https://arxiv.org/html/2210.08955v3 . Theorem 1 and Theorem 4 are directly relevant.
3. *Monitoring-edge-geodetic sets in product networks*, International Journal of Parallel, Emergent and Distributed Systems 39 (2024), 264–277, DOI:10.1080/17445760.2024.2301929. The publicly accessible abstract describes join, corona, cluster, lexicographic, and direct products; the full text was not inspected.
