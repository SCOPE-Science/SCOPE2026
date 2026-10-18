# Square-root bounds for strong edge-geodetic sets of cyclic clique products

## Finding

For every pair of integers \(n\ge 3\) and \(m\ge 2\), let \(G_{n,m}=C_n\mathbin{\square}K_m\) be the Cartesian product of a simple cycle and a clique. The strong edge-geodetic number of this cylindrical clique graph satisfies

\[
 m\sqrt n\ \le\ \operatorname{sg}_e(G_{n,m})\ \le\ m\min\{n,2\lceil\sqrt n\rceil+6\}.
\]

Furthermore, the lower bound is **exact on every square cycle of side at least three**:

\[
 \operatorname{sg}_e(C_{k^2}\mathbin{\square}K_m)=mk
 \qquad (k\in\mathbb Z,\ k\ge3,\ m\ge2).
\]

Uniformly in both parameters, \(\operatorname{sg}_e(G_{n,m})=\Theta(m\sqrt n)\) along sequences with \(n\to\infty\). The general explicit upper-bound construction is asymptotically a factor at most \(2+O(n^{-1/2})\) from the optimum, while a separate cyclic assignment proves exact optimality at all the square orders stated above.

## Assumptions and scope

All graphs are finite, simple, and undirected. Vertices of \(C_n\) are the residues \(\mathbb Z/n\mathbb Z\), joined when their difference is \(\pm1\) modulo \(n\); \(C_3\) is the triangle. Vertices of \(K_m\) are \(\{0,\ldots,m-1\}\). The vertex set of \(G_{n,m}\) consists of pairs \((r,j)\); an edge lies either along a cycle layer at fixed \(j\), or between two distinct clique layers at fixed \(r\). A geodesic is a shortest path. A strong edge-geodetic set is a set \(S\) of vertices for which one may choose at most one geodesic for each unordered pair of distinct vertices of \(S\), such that the union of those geodesics contains every graph edge. The minimum size is \(\operatorname{sg}_e\). In particular, two different shortest paths with identical endpoint pair cannot both be used.

## Proof

**Lower bound.** For any strong edge-geodetic set \(S\), write \(S_j=\{r:(r,j)\in S\}\) and \(a_j=|S_j|\). The Cartesian distance formula is

\[
 d_{G_{n,m}}((x,p),(y,q))=d_{C_n}(x,y)+\mathbf1_{p\ne q}.
\]

A shortest path therefore changes its clique-layer coordinate either zero times (when its endpoints have the same coordinate) or exactly once, directly from its first endpoint's layer to its second endpoint's layer. Thus, for each distinct \(p,q\), all \(n\) clique edges joining these two layers must be covered by distinct endpoint pairs, one endpoint from \(S_p\) and one from \(S_q\). A geodesic for one such pair contains just one \(p\)-to-\(q\) clique edge, giving \(a_p a_q\ge n\). Multiplying over the \(\binom m2\) pairs gives \((\prod_j a_j)^{m-1}\ge n^{m(m-1)/2}\). By arithmetic–geometric means, \(\sum_j a_j\ge m\sqrt n\).

**Balanced cyclic anchors.** Set \(k=\lceil\sqrt n\rceil\) and \(s=\min\{n,2k+6\}\). If \(s=n\), take all vertices. Assigning the length-one path to each graph edge immediately proves the claimed upper bound. Henceforth assume \(s<n\), so \(s=2k+6\), and put

\[
 T=\left\{\left\lfloor\frac{in}{s}\right\rfloor:0\le i<s\right\}\subset\mathbb Z/n\mathbb Z,
 \qquad S=T\times\{0,\ldots,m-1\}.
\]

The \(s\) residues of \(T\) are distinct. Every cyclic interval comprising \(L\) consecutive residues contains at least \(\lfloor sL/n\rfloor\) members of \(T\): lift the interval to \([a,a+L)\subset\mathbb Z\) and note that the indices of all lifted anchors \(\lfloor in/s\rfloor\) in this interval are precisely the integers in the real interval \([as/n,(a+L)s/n)\), which has length \(sL/n\). Consequently, if \(r\) is a target residue, the \(i\)-th anchor strictly clockwise after \(r\) is at distance at most \(\lceil in/s\rceil\); the analogous \(i\)-th anchor strictly counterclockwise before \(r\) has the same bound.

**Assigning the clique edges.** Let \(h=\lfloor s/2\rfloor-2=k+1\). For each \(r\) and positive indices \(i,j\) with \(i+j\le h\), choose the \(i\)-th counterclockwise anchor \(x_i\) before \(r\) and the \(j\)-th clockwise anchor \(y_j\) after \(r\). Their two distances to \(r\) obey

\[
 d^-_i+d^+_j\le\frac{(i+j)n}{s}+2\le\frac{hn}{s}+2
 \le \frac n2,
\]

because \(h=s/2-2\) and \(s\le n\). Hence the clockwise arc \(x_i\to r\to y_j\) is a shortest cycle path. The reverse oriented endpoint choice \(y_j\to r\to x_i\), along the counterclockwise arc, is also shortest. Distinct \((i,j)\) give distinct cross-layer endpoint pairs, and the two choices of orientation are distinct because both anchors lie on different sides of \(r\) at distance less than \(n/2\). Therefore every residue \(r\) offers at least

\[
 2\#\{(i,j)\in\mathbb Z_{>0}^2:i+j\le h\}
 =h(h-1)=k(k+1)\ge n
\]

**different ordered coordinate pairs** \((a,b)\in T^2\), with \(a\ne b\), whose short arc passes through \(r\).

For each unordered pair of distinct clique layers \(\{p,q\}\), visit the \(n\) residues \(r\) in any order. Greedily assign to the edge \((r,p)(r,q)\) an eligible ordered coordinate pair \((a,b)\) not used earlier for this same layer pair. This is possible since each residue has at least \(n\) choices and at most \(n-1\) have been used. Choose the geodesic starting at \((a,p)\), following the specified shortest cycle arc to \((r,p)\), changing layer to \((r,q)\), and completing that arc to \((b,q)\). It is a geodesic by the distance formula, contains the desired clique edge, and its unordered *vertex* endpoint pair has not been used earlier. Repeat for all clique-layer pairs independently: endpoints from two different unordered pairs of layers cannot coincide as vertex pairs.

**Covering the cycle edges.** For each fixed clique layer, take clockwise shortest arcs between consecutive anchors in cyclic order, including the last-to-first arc. Every gap has length at most \(\lceil n/s\rceil\le n/2\), so these are geodesics covering all cycle edges. Their endpoint pairs are distinct within a layer and differ from all cross-layer pairs. Together with the previously assigned geodesics they form a legal edge-covering assignment using the \(ms\) selected vertices, yielding the asserted upper bound. \(\square\)

**Sharp square-cycle construction.** Let \(n=k^2\) with \(k\ge3\), and select just the \(k\) equally spaced anchors \(T=\{ik:0\le i<k\}\) in each clique layer. To assign every clique edge between fixed layers \(p\) and \(q\), index all \(k^2\) ordered anchor pairs by \((i,d)\), where \(0\le i,d<k\), and put \(a=ik\) and \(b=((i+d)\bmod k)k\). For each pair assign the change-of-layer rung at

\[
 r_{i,d}=\begin{cases}
 ik,&d=0,\\
 ik+d,&1\le d\le\lfloor k/2\rfloor,\\
 ((i-1)\bmod k)k+d,&\lfloor k/2\rfloor<d<k.
 \end{cases}
\]

For \(d=0\) use the single clique edge at \(a\). For \(1\le d\le\lfloor k/2\rfloor\), the clockwise arc from \(a\) to \(b\) has length \(kd\le n/2\) and contains \(r_{i,d}\). For \(d>\lfloor k/2\rfloor\), the counterclockwise arc from \(a\) to \(b\) has length \(k(k-d)<n/2\) and contains \(r_{i,d}\). In each case follow that shortest arc and change clique layer exactly at the indicated rung. The \(k^2\) rungs \(r_{i,d}\) are all distinct: for each of the \(k\) gaps between consecutive anchors, the offset zero is supplied by \(d=0\), the offsets \(1,\ldots,\lfloor k/2\rfloor\) by the clockwise cases, and the remaining offsets by counterclockwise cases at the subsequent anchor. Thus all \(n=k^2\) clique edges of this layer pair are covered by \(k^2\) different endpoint pairs. Assign such paths separately for each pair of clique layers.

Within each fixed layer the \(k\) clockwise arcs between consecutive anchors have length \(k\le n/2\) and cover all rim edges. Since \(k\ge3\), these same-layer arcs have distinct unordered endpoint pairs, and cross-layer endpoint pairs cannot duplicate them. This is a legal strong edge-geodetic covering using only \(mk\) vertices, and the lower bound already proved gives equality. \(\square\)

## Verification

The standalone standard-library script `verify.py` constructs the explicit selected vertices and paths, checks every path's exact Cartesian-geodesic length and unique unordered endpoint pair, and confirms coverage of all edges. It tests \(260\) general-bound constructions, including \(n\) as large as \(300\), with \(81,327\) graph edges checked. It separately tests \(54\) sharp square-order constructions (all \(3\le k\le20\), \(m\in\{2,3,4\}\)), checking a further \(54,435\) graph edges. An additional \(234,952\) finite cyclic intervals were counted against the balanced-anchor lemma. Running `python3 verify.py` from the extracted package prints the captured output in `verify_output.txt`. These are finite sanity checks; the preceding symbolic proof supplies the assertion for all \(n,m\).

## Relationship to prior work

Manuel, Klavžar, Xavier, Arokiaraj, and Thomas introduced strong edge geodetic sets and general graph bounds in 2017. Xavier et al. (2020) studied product graphs, with bounds that do not entail the uniform \(O(m\sqrt n)\) estimate here. Zmazek (2021) solved several path-grid cases \(P_n\square P_j\) for small fixed \(j\). Klavžar and Zmazek (arXiv 2023; journal 2024), Theorem 3.5, determined \(\operatorname{sg}_e(P_n\square K_m)\) exactly. That theorem concerns **paths**, not cycles, and does not give the present bound: its path-based geodesics need not stay shortest when the path factor is closed into a cycle. The present general construction uses balanced cyclic anchor intervals and collision-free greedy pairing, while its sharper square-order specialization exhibits an explicit bijection between ordered anchor pairs and all cycle rungs. The square-order formula agrees numerically with the known path–clique value but requires a different shortest-path assignment on the cycle.

## Limitations

This is a sharp-order two-sided estimate with an exact infinite square-order subsequence, **not** a determination of the exact strong edge-geodetic number for every order or its sharp general leading constant. The factor near two is an upper bound on approximation, not a lower bound on the achievable approximation factor. No result is asserted for other graph products, or for the distinct vertex-covering strong geodetic number. The search and comparison of accessible literature does not exclude an equivalent result hidden in unindexed earlier publications; further external mathematical checking is desirable.

## References

1. P. Manuel, S. Klavžar, A. Xavier, A. Arokiaraj, E. Thomas, *Strong edge geodetic problem in networks*, Open Mathematics 15 (2017), 1225–1235. DOI: 10.1515/math-2017-0101.
2. D. A. Xavier, D. Mathew, S. Theresal, E. S. Varghese, *Some Results on Strong Edge Geodetic Problem in Graphs*, Communications in Mathematics and Applications 11(3) (2020), 403–413. DOI: 10.26713/cma.v11i3.1385.
3. E. Zmazek, *Strong edge geodetic problem on grids*, arXiv:2101.09259, initial public version January 22, 2021.
4. S. Klavžar, E. Zmazek, *Strong Edge Geodetic Problem on Complete Multipartite Graphs and Some Extremal Graphs for the Problem*, arXiv:2312.11199, initial public version December 18, 2023; Bulletin of the Iranian Mathematical Society 50, article 13 (2024), DOI: 10.1007/s41980-023-00849-6.
