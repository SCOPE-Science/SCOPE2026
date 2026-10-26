# General-position polynomials of categorical products of complete graphs and an infinite nonunimodal family

## Finding
Let \(G_{p,q}=K_p\times K_q\) be the **categorical/direct** product, not the Cartesian product, of complete graphs of orders \(p,q\ge3\). Its vertices are the cells \((i,j)\in[p]\times[q]\); distinct cells are adjacent exactly when their two coordinates both differ. Let \(\Psi_{p,q}(z)=\sum_{S}z^{|S|}\), where the sum ranges over all general-position vertex subsets of \(G_{p,q}\), including the empty set. A set is in general position when no three distinct selected vertices lie on a shortest path between two of them.

Define \(R_{p,q}=\binom p2\binom q2\), and adopt \(\binom nk=0\) for \(k<0\) or \(k>n\). Then the full polynomial is
\[
\boxed{\Psi_{p,q}(z)=1+pqz+\sum_{k=2}^{\max(p,q)}\left(p\binom qk+q\binom pk\right)z^k+2R_{p,q}z^2+4R_{p,q}z^3+R_{p,q}z^4+\sum_{k=3}^{\min(p,q)}\binom pk\binom qk k!z^k.}
\]
The complete enumerator of inclusion-maximal general-position sets is
\[
\boxed{M_{p,q}(z)=pz^q+qz^p+R_{p,q}z^4+\binom{\max(p,q)}{\min(p,q)}\min(p,q)!z^{\min(p,q)}.}
\]
In particular, **for every integer \(p\ge4\)**, setting \(q=2p+4\) produces a strict coefficient valley \(a_p>a_{p+1}<a_{p+2}\) in \(\Psi_{p,q}(z)=\sum_k a_kz^k\). Thus an infinite family of connected, diameter-two, vertex-transitive graph products has nonunimodal general-position polynomials. For \((p,q)=(4,12)\), the consecutive coefficients at degrees \(4,5,6\) are \(14268,3168,3696\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The categorical graph product uses simultaneous adjacency in **both** factors; \(K_p\square K_q\) is a different graph and has different position-set counts. The hypotheses \(p,q\ge3\) ensure that distinct nonadjacent cells have a common neighbor, so \(G_{p,q}\) is connected with diameter two. Empty and singleton sets are included in the all-set polynomial. Inclusion-maximal means maximal by inclusion, not maximum cardinality. No assertion about dimensions below three is made.

## Proof
**1. Diameter-two translation.** An adjacent cell pair has distance one. Two distinct nonadjacent cells share a row or a column. With \(p,q\ge3\), choose a third row and a third column distinct from both relevant coordinates to give a two-edge walk between them. Thus their distance is two. In any diameter-two graph, three selected vertices violate general position exactly when their induced subgraph is a path with two edges: the two endpoints are nonadjacent and have a selected common neighbor. Consequently a vertex set is in general position if and only if its induced subgraph has no induced three-vertex path, equivalently if and only if it induces a disjoint union of cliques (a *cluster graph*).

**2. Complete classification.** A clique in \(G_{p,q}\) uses pairwise distinct rows and pairwise distinct columns. An independent set of at least two cells lies entirely in one row or in one column: take two cells sharing a row and having distinct columns; any cell nonadjacent to both must have that row (the column alternative cannot equal both different columns). The column case is symmetric. If a general-position set contains a clique component of size at least three, an outside component would have to be nonadjacent to all three clique cells, which is impossible: three cells use distinct rows and columns, whereas one further cell has only one row and one column. Hence that clique is the whole set.

Otherwise every nontrivial component is an edge. For an edge with endpoints \((a,b)\) and \((c,d)\), where \(a\ne c\) and \(b\ne d\), any cell nonadjacent to **both** endpoints must be one of the two opposite corners \((a,d)\) or \((c,b)\). These two corners are adjacent to one another. It follows that a set containing an edge, but not itself a clique, can contain only one of these opposite corners or both. Respectively this gives a three-cell subset of a unique \(2\times2\) coordinate rectangle (one edge plus an isolated cell), or the full rectangle (two disjoint edges). Along with the empty, singleton, independent-layer, and coordinate-transversal clique cases, these are all possible shapes. They are mutually disjoint if independent layers and transversal cliques are counted only at sizes at least two, and transversal cliques of size two are handled separately as edges.

**3. Polynomial.** There are \(pq\) singletons. Independent-layer subsets of size \(k\ge2\) number \(p\binom qk+q\binom pk\). Each two-row/two-column choice gives precisely two selected adjacent pairs, and hence \(2R_{p,q}\) edges; it also gives four distinct three-cell configurations and exactly one four-cell configuration. Transversal cliques of size \(k\ge3\) number \(\binom pk\binom qk k!\): choose the used rows and columns and biject them. Summing these disjoint cases proves the stated \(\Psi_{p,q}\).

**4. Inclusion-maximality.** An independent layer is maximal precisely when it is a full row or a full column: a proper subset admits another cell in its layer; for a full layer of length at least three, adding a cell outside creates a selected induced three-vertex path. A single transversal clique is maximal precisely when its size is \(\min(p,q)\): smaller cliques can extend using an unused row and column; at full size, an outsider is neither adjacent to every selected cell (one coordinate is used up) nor nonadjacent to every selected cell (there are at least three selected cells with distinct coordinates), so it creates a forbidden path. Every partial three-cell rectangle extends to a full four-cell rectangle. A full rectangle is maximal: any outside cell is adjacent to two nonadjacent rectangle corners, again making a selected induced three-vertex path. These are the only maximal shapes. The numbers of full rows, full columns, full rectangles, and full-size transversal cliques are, respectively, \(p,q,R_{p,q},\binom{\max(p,q)}{\min(p,q)}\min(p,q)!\), proving \(M_{p,q}\).

**5. Infinite nonunimodality.** Fix \(p\ge4\) and take \(q=2p+4\). For cardinalities strictly larger than \(p\), every general-position set must be contained in a single row (all transversal cliques have at most \(p\) vertices, and rectangle configurations have at most four). Thus
\[
a_{p+1}=p\binom q{p+1},\qquad a_{p+2}=p\binom q{p+2},\qquad \frac{a_{p+2}}{a_{p+1}}=\frac{p+3}{p+2}>1.
\]
At cardinality \(p\), the transversal cliques alone contribute \(p!\binom qp\), whence
\[
a_p\ge p!\binom qp>p\binom q{p+1}=a_{p+1}.
\]
The strict middle inequality follows because it is equivalent to \((p-1)!>(p+4)/(p+1)\), true for all \(p\ge4\). Therefore \(a_p>a_{p+1}<a_{p+2}\), contradicting unimodality. Varying \(p\) gives infinitely many distinct graph orders and proves the assertion.

## Verification
The standalone file `gp_direct_verify.py` constructs the actual product graph, computes shortest-path distances by breadth-first search, enumerates all vertex subsets for boards \((3,3),(3,4),(3,5),(3,6),(4,4)\), checks the geodesic definition independently of the counting formula, verifies every polynomial coefficient, and tests inclusion-maximality by all single-vertex extensions. These boards account for \(365056\) subsets. It additionally tests the strict-valley inequalities using exact integer arithmetic for every \(p\) from \(4\) through \(50\). All checks pass; reproducible stdout is embedded as `gp_direct_verification_output.txt`. These finite checks corroborate, but do not replace, the infinite proof.

## Relationship to prior work
Klavžar and Yero's 2019 paper (arXiv:1906.00935, Proposition 3.3) treats **maximum general-position cardinality** in direct products of complete graphs, not their all-set polynomial. Di Stefano and coauthors (arXiv:2306.09965, Theorem 5.4) obtain the **lower general-position number** and describe several relevant maximal-set constructions. Those extremal cardinalities and the underlying examples are established prior work and are not claimed as new here. Iršič and coauthors (arXiv:2401.05696) introduce general-position polynomials and study other graph families; their results do not enumerate the categorical complete-graph product. The later general-position survey (arXiv:2501.19385) treats categorical-product extremal numbers separately from general-position-polynomial examples. Rather (arXiv:2603.06930) studies explicit general-position polynomials and unimodality in other graph families. The claims assessed here are the complete all-set and maximal-set enumerators and the **infinite nonunimodality family**, not the known extremal cardinalities. A search cannot exclude every unindexed equivalent treatment of these enumerators.

## Limitations
The product is categorical rather than Cartesian. The hypotheses \(p,q\ge3\) are essential to the diameter-two argument. No unimodality classification for **all** choices of \((p,q)\) is asserted, and no assertion is made for products of more than two factors. Code verifies only finite instances. The result has undergone self-review, not independent mathematical review. Priority may be affected by unpublished or poorly indexed equivalent results.

## References
- S. Klavžar and I. G. Yero, *The general position problem and strong resolving graphs*, arXiv:1906.00935v1 (3 June 2019), especially Proposition 3.3. https://arxiv.org/abs/1906.00935
- G. Di Stefano, S. Klavžar, R. Krishnakumar, J. Tuite, and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965v1 (16 June 2023), Theorem 5.4. https://arxiv.org/abs/2306.09965
- V. Iršič, S. Klavžar, J. Rus, and J. Tuite, *General Position Polynomials*, arXiv:2401.05696v1 (11 January 2024). https://arxiv.org/abs/2401.05696
- S. Klavžar, J. Tuite, and L. S. Chandran, *The General Position Problem: A Survey*, arXiv:2501.19385v5 (2026). https://arxiv.org/abs/2501.19385
- A. H. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v3 (2026). https://arxiv.org/abs/2603.06930
