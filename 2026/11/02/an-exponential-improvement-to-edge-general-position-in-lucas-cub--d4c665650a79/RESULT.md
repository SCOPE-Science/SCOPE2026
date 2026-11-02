# An exponential improvement to edge general position in Lucas cubes

## Finding
For every integer \(n\ge5\), let \(\Lambda_n\) be the Lucas cube: its vertices are binary cyclic words \((x_0,\ldots,x_{n-1})\) containing no cyclically consecutive pair of ones; two vertices are adjacent exactly when one coordinate differs. Let \(\operatorname{gp}_{\mathrm e}(G)\) denote the largest number of edges of \(G\) such that no shortest path contains three selected edges. Write \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and \(L_0=2\), \(L_1=1\), \(L_{j+2}=L_{j+1}+L_j\).

**Theorem (constructive lower bound).** For every \(n\ge5\),
\[
\operatorname{gp}_{\mathrm e}(\Lambda_n)\ \ge\ L_{n-1}
=F_{n-1}+2F_{n-2}=2F_{n-1}+F_{n-4}.
\]
The construction is explicit for every dimension; no general equality or upper bound of \(L_{n-1}\) is asserted. The improvement over the \(2F_{n-1}\) lower bound established in the reference is \(F_{n-4}\), which grows exponentially with \(n\). For \(n=5\), the bound agrees with the already-known exact value \(\operatorname{gp}_{\mathrm e}(\Lambda_5)=7\).

## Assumptions and scope
All graphs are finite, simple, and undirected. Indices are taken modulo \(n\). A shortest path (geodesic) has minimum length between its endpoints; edge-general-position prohibits any three selected edges on one geodesic, irrespective of their order. The theorem applies to all integers \(n\ge5\), not merely to the computational checks below.

For each coordinate \(j\), write \(\Theta_j\) for the edges that change coordinate \(j\). Define three **disjoint** families:
\[
\begin{aligned}
A&=\Theta_0,\\
B&=\{uv\in\Theta_1:u_{n-1}=v_{n-1}=0\},\\
C&=\{uv\in\Theta_{n-1}:u_1=v_1=0\}.
\end{aligned}
\]
The witness is \(S_n=A\cup B\cup C\).

## Proof
**1. Distances.** Regard each Lucas vertex as an independent set of the cycle on \(n\) coordinate positions. Given any vertices \(u,v\), first delete coordinates in \(u\setminus v\), and then add coordinates in \(v\setminus u\). Every intermediate set is independent; hence this is a path of length exactly the Hamming distance \(d_H(u,v)\). Every graph edge changes one coordinate, so no shorter path exists. Therefore \(d_{\Lambda_n}(u,v)=d_H(u,v)\). Consequently every geodesic changes any fixed coordinate at most once.

**2. Three-spoke obstruction.** Project each vertex onto the three coordinates \((0,1,n-1)\). Since coordinates \(1\) and \(n-1\) are each adjacent to coordinate \(0\) on the underlying cycle, the only allowed projected triples are \(000,100,010,001,011\). For an edge of \(A\), the projected edge is \(000\leftrightarrow100\): a change of coordinate \(0\) forces both its neighbors to zero. For an edge of \(B\), the projected edge is \(000\leftrightarrow010\); for an edge of \(C\), it is \(000\leftrightarrow001\). These are three different edges incident with one projected vertex, \(000\).

Project a geodesic of \(\Lambda_n\) to these three coordinates and erase consecutive repeated triples caused by changes of other coordinates. Step 1 shows each of the three remaining coordinates can change at most once, so no projected triple can be visited twice. The projected walk is therefore a simple path in the five-vertex projected graph. A simple path cannot traverse all three distinct edges incident with one vertex: traversing three spokes would force a repeated visit to \(000\). Since each of \(A,B,C\) uses a different coordinate, the original geodesic contains at most two edges of \(S_n\). Hence \(S_n\) is edge-general-position.

**3. Cardinality.** An edge in \(A\) has its two neighbors (coordinates \(1,n-1\)) fixed to zero. The \(n-3\) remaining positions form a path; their independent sets are counted by \(F_{n-1}\), giving \(|A|=F_{n-1}\). An edge in \(B\) has coordinates \(0,2,n-1\) fixed to zero. The \(n-4\) free positions \(3,\ldots,n-2\) form a path, giving \(|B|=F_{n-2}\). By cyclic reflection, \(|C|=F_{n-2}\). The three families have distinct changing coordinates and are disjoint. Thus
\[
|S_n|=F_{n-1}+2F_{n-2}=L_{n-1}.
\]
The standard Fibonacci recurrence gives \(L_{n-1}-2F_{n-1}=F_{n-4}\). The construction establishes the asserted lower bound for every \(n\ge5\). \(\square\)

## Verification
The standalone standard-library program `verify.py` reconstructs every Lucas graph \(\Lambda_n\) for \(5\le n\le9\), computes all-pairs shortest-path distances by breadth-first search, checks their equality with Hamming distances, constructs \(S_n\) directly from its edge-membership predicates, enumerates **all shortest paths** between all unordered vertex pairs, and checks that each contains at most two chosen edges. Running `python3 verify.py` yields:

| \(n\) | Vertices | Edges | \(|S_n|\) | Enumerated geodesics |
| --- | ---: | ---: | ---: | ---: |
| 5 | 11 | 15 | 7 | 110 |
| 6 | 18 | 30 | 11 | 558 |
| 7 | 29 | 56 | 18 | 2534 |
| 8 | 47 | 104 | 29 | 15224 |
| 9 | 76 | 189 | 47 | 86742 |

The run ends with `ALL_CHECKS_PASSED`. These are finite consistency checks, not a substitute for the proof for arbitrary \(n\).

## Relationship to prior work
Klavžar and Tan, *Edge General Position Sets in Fibonacci and Lucas Cubes* (first publicly available on arXiv, 20 April 2023), establish in Theorem 4.6 the infinite lower bound \(\operatorname{gp}_{\mathrm e}(\Lambda_n)\ge2F_{n-1}\) via two complete coordinate classes, and prove the exact exceptional \(n=5\) value \(7\) in Proposition 4.7. The new construction replaces those two classes by one complete coordinate class and two **restricted** neighboring classes; their three projections share a single zero-centered star. It yields a uniform strictly stronger bound in every dimension \(n\ge5\), not merely another realization of the known \(n=5\) example.

Manuel, Prabha, and Klavžar's *Generalization of edge general position problem* (arXiv:2207.07357; 2025 journal version) gives general edge-geodesic inequalities and results for hypercubes, tori, and Beneš networks. Its relevant sections do not provide this cyclic Lucas-cube three-class construction or the \(L_{n-1}\) lower bound. Finite Fibonacci-cube cases concern a different graph family and do not establish this Lucas-cube bound.

## Limitations
The theorem is a constructive lower bound, **not** a determination of \(\operatorname{gp}_{\mathrm e}(\Lambda_n)\) for all dimensions and not an optimality assertion. The known five-dimensional equality is credited, not claimed as new. Exhaustive checking stops at dimension nine. Indexed literature and mathematical databases are incomplete; a different prior formulation of the same three-class construction remains a priority risk.

## References
1. S. Klavžar and E. Tan, *Edge General Position Sets in Fibonacci and Lucas Cubes*, arXiv:2304.10114 (first posted 2023-04-20), https://arxiv.org/abs/2304.10114; *Bulletin of the Malaysian Mathematical Sciences Society* **46** (2023), Article 120, https://doi.org/10.1007/s40840-023-01517-y. See Section 4, especially Proposition 4.1(ii), Theorem 4.6, and Proposition 4.7.
2. P. Manuel, R. Prabha, and S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357 (first posted 2022-07-15), https://arxiv.org/abs/2207.07357; *The Art of Discrete and Applied Mathematics* **8** (2025), Article P1.02, https://doi.org/10.26493/2590-9770.1745.5f4. See Sections 1, 2, 4, and 6.
