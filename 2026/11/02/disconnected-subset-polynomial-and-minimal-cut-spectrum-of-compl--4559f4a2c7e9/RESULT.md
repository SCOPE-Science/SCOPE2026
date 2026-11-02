# Disconnected-subset polynomial and minimal-cut spectrum of complete-graph tensor products

## Finding
For integers \(m,n\ge3\), let \(G_{m,n}=K_m\times K_n\) be the categorical (tensor, direct, Kronecker) product. Its vertices are cells \((i,j)\in[m]\times[n]\), and distinct cells are adjacent exactly when both coordinates differ. Let \(D_{m,n}(t)\) enumerate vertex subsets \(U\) for which the induced graph \(G_{m,n}[U]\) is disconnected, by the number of surviving vertices. As usual, the empty graph and singleton induced graphs are **not** counted as disconnected. Then
\[
\begin{aligned}
D_{m,n}(t)={}&m\big((1+t)^n-1-nt\big)
+n\big((1+t)^m-1-mt\big)\\
&+mn\,t\big((1+t)^{m-1}-1\big)\big((1+t)^{n-1}-1\big)
+\binom m2\binom n2t^4.
\end{aligned}
\]
The polynomial enumerating **inclusion-minimal vertex cutsets** by the number of deleted vertices is
\[
M_{m,n}(z)=mn\,z^{(m-1)(n-1)}+\binom m2\binom n2z^{mn-4}.
\]
Consequently, the two cutset sizes differ by \(m+n-5\), so their gap grows without bound. Every minimum cut is the open neighborhood of a vertex, while every other inclusion-minimal cut is the complement of a \(2\times2\) cell rectangle. Moreover, every vertex cut leaving at least two components **without isolated surviving vertices** is exactly such a rectangle complement, so the super-connectivity in that convention is \(mn-4\).

If vertices survive independently with probability \(p\), and the operational network requires a **nonempty connected** surviving induced graph, its exact residual node reliability is
\[
\operatorname{Rel}_{m,n}(p)=1-(1-p)^{mn}\left[1+D_{m,n}\left(\frac{p}{1-p}\right)\right],\qquad 0\le p<1,
\]
with \(\operatorname{Rel}_{m,n}(1)=1\). Thus the same polynomial determines the full vertex-failure distribution, not just extremal cuts.

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled. Integers \(m,n\ge3\) are arbitrary, including the nonsquare case. A **vertex cutset** is a deleted set \(S\) such that \(G_{m,n}-S\) has at least two connected components. A vertex cutset is **inclusion-minimal** if none of its proper subsets is a cutset (different from being merely of minimum cardinality). A **super vertex cutset** leaves a disconnected graph without isolated vertices. The subset polynomial distinguishes labeled subsets; no quotient under row/column symmetries is taken. The probability formula assumes independent, identically distributed vertex survival and perfectly reliable edges.

## Proof
**Lemma (four mutually exclusive forms).** A vertex subset \(U\) induces a disconnected graph if and only if it has exactly one of the following forms:

1. At least two cells of one row and no other cells.
2. At least two cells of one column and no other cells.
3. A center cell \((i,j)\), a nonempty set of other cells in row \(i\), and a nonempty set of other cells in column \(j\), with no further cells.
4. Exactly the four cells of a \(2\times2\) rectangle on two different rows and two different columns.

Each form is disconnected: forms 1–2 are independent sets, form 3 has an isolated center and a connected complete-bipartite remainder, and form 4 induces two disjoint edges.

For the converse, first suppose that \(G_{m,n}[U]\) has an isolated vertex \(v=(i,j)\). Since every cell differing from \(v\) in both coordinates is adjacent to it, all of \(U\) lies in the union of row \(i\) and column \(j\). If \(U\) meets only one of these lines, it is form 1 or 2. If it meets both away from \(v\), it is form 3. There is no ambiguity in form 3: every noncentral cell has a neighbor in the opposite arm, so the center is the unique isolated vertex. In forms 1–2 the occupied row or column is unique because \(|U|\ge2\).

Suppose instead that \(G_{m,n}[U]\) is disconnected **and has no isolated vertices**. A component has an edge between \(x=(i,j)\) and \(y=(k,\ell)\), where \(i\ne k\) and \(j\ne\ell\). Every vertex in another component must be nonadjacent to both \(x\) and \(y\), so it lies in the two-element set \(\{(i,\ell),(k,j)\}\). As there are no isolated vertices, both of these cross-corners must occur, and together they form an edge. Conversely, every vertex of the first component is nonadjacent to both cross-corners, forcing it to be in \(\{x,y\}\). Hence \(U\) consists of exactly the four rectangle cells. This establishes the classification for all \(m,n\ge3\).

**Enumeration.** Row-only subsets contribute \(m((1+t)^n-1-nt)\), and column-only subsets contribute \(n((1+t)^m-1-mt)\). For form 3, independently choose its center (\(mn\) ways), a nonempty subset of the remaining \(n-1\) cells in its row, and a nonempty subset of the remaining \(m-1\) cells in its column; the center adds one to the size. This yields the product term. Form 4 contributes \(\binom m2\binom n2t^4\). Uniqueness of the four forms proves no double counting.

**Maximal disconnected survivors and minimal cuts.** Deletion-complementation reverses inclusion: \(S\) is an inclusion-minimal cut precisely when \(U=V(G_{m,n})\setminus S\) is inclusion-maximal among disconnected induced subsets. In forms 1–3, \(U\) can be enlarged, retaining its isolated center, until it equals the full cross \(X_{ij}=\{(i,b):b\in[n]\}\cup\{(a,j):a\in[m]\}\). A full cross is maximal disconnected: adding any outside cell \((a,b)\) connects its isolated center to the remainder, because \(m,n\ge3\) give a row-arm or column-arm cell adjacent to \((a,b)\). The remainder itself is complete bipartite and connected. The full \(2\times2\) rectangle is also maximal disconnected: any outside cell is adjacent to at least one vertex of each of its two diagonal-edge components. Thus there are exactly \(mn\) full crosses and \(\binom m2\binom n2\) rectangles, with no coincidences, and their complements have sizes \(mn-(m+n-1)=(m-1)(n-1)\) and \(mn-4\). Since \(mn-4-(m-1)(n-1)=m+n-5>0\), the stated two-term polynomial and cut-gap follow. The complement of \(X_{ij}\) is exactly the open neighborhood of \((i,j)\). The only disconnected survivors without isolates are full rectangles, proving the super-cut assertion.

**Reliability.** A survivor set of cardinality \(k\) has probability \(p^k(1-p)^{mn-k}\). Summing over disconnected survivor sets gives \((1-p)^{mn}D_{m,n}(p/(1-p))\) for \(0\le p<1\). The empty survivor set has probability \((1-p)^{mn}\); every other state is nonempty connected. Subtracting the two disjoint failure events proves the reliability identity. At \(p=1\) all vertices survive and the original graph is connected because it is not among the four disconnected forms.

## Verification
The standalone, standard-library-only `verify.py` independently constructs the product graph using its original adjacency rule, uses graph search to test disconnectedness of each induced subset, and tests inclusion-maximality by adding every missing vertex. It compares the complete cardinality distribution to the binomial formula and compares the exact collection of maximal disconnected subsets to the predicted cross and rectangle family. For the parameter pairs \((3,3)\), \((3,4)\), \((3,5)\), \((4,4)\), \((4,5)\), all **1,151,488** induced subsets passed. Commands: `python verify.py`. The unrestricted statements are proved above; finite checks are independent corroboration, not an infinite certificate.

## Relationship to prior work
Wang and Shan (2011, arXiv:1105.1567, Theorems 1 and 3) prove the general minimum-connectivity and super-connectedness framework for products with a complete graph. In particular, their theorem already implies that the minimum cuts of \(K_m\times K_n\) are vertex neighborhoods; that fact is **not** claimed as new. Soliemany, Ghasemi and Varmazyar (published online 2022-08-18, DOI:10.1051/ro/2022085, primary MSC 05C40) study super vertex cuts in direct products; their Theorem 2.5 and references include the \(K_3\times K_n\) scalar \(3n-4\), also not claimed as new. Their general development concerns scalar bounds and specific factors rather than the full disconnected-induced-subset enumeration. Anand, Balakrishnan, Changat and Peterin (2012, DOI:10.2298/AADM111230001A, especially their direct-product Theorem 5.12) classify **clique** separators of graph products; for complete factors of order at least three they furnish no such clique separators. Their stated restriction to clique separators does not classify the larger nonclique vertex cutsets or disconnected subsets here. The classical residual node-reliability framework concerns connected induced operational sets. OEIS A360873 counts connected induced subsets of the **Cartesian** rook graph, not of its categorical-product complement. The assessed additional content is the four-form all-subset classification, exact complete reliability polynomial, and entire two-tier inclusion-minimal cutset spectrum (not merely its first tier).

## Limitations
Novelty has not been independently audited; literature searches may miss results stated in the language of complements of line graphs, vertex reliability, minimal separators, or graph product connectivity. The 2025 general node-reliability paper at https://www.nas.ewi.tudelft.nl/people/Piet/papers/IEEE_TNSM2025_Node_reliability_polynomial.pdf was identified but unavailable for full inspection during this investigation. The proof makes no claims for factors of order two, for edge failures, for directed products, or for nonuniform survival probabilities. Ordinary node reliability depends on the convention for zero surviving vertices, which is fixed explicitly above.

## References
1. H. Wang and E. Shan, *On the super connectivity of Kronecker products of graphs*, arXiv:1105.1567, publicly available 2011-05-09. https://arxiv.org/pdf/1105.1567
2. F. Soliemany, M. Ghasemi and R. Varmazyar, *On the super connectivity of direct product of graphs*, RAIRO Operations Research 56 (2022), 2767–2773; first published online 2022-08-18, DOI:10.1051/ro/2022085. https://www.numdam.org/item/10.1051/ro/2022085.pdf
3. K. Sutner, A. Satyanarayana and C. Suffel, *The complexity of the residual node connectedness reliability problem*, SIAM Journal on Computing 20 (1991). https://doi.org/10.1137/0220009
4. B. S. Anand, K. Balakrishnan, M. Changat and I. Peterin, *Atoms and clique separators in graph products*, Applicable Analysis and Discrete Mathematics 6 (2012), 46–62, DOI:10.2298/AADM111230001A. https://doi.org/10.2298/AADM111230001A
5. OEIS A360873, *Connected induced subgraphs in Cartesian rook graphs*, https://oeis.org/A360873 (a different graph family, for comparison).
