# Complete optimal feedback-vertex-set classification for cycle prisms

## Finding

For each integer \(n\ge3\), let \(Y_n=C_n\square K_2\) have two labeled rails \(a_i,b_i\), with indices in \(\mathbb Z/n\mathbb Z\), and edges \(a_ia_{i+1}\), \(b_ib_{i+1}\), and \(a_ib_i\). A *feedback vertex set* (or *decycling set*) is a set \(F\subseteq V(Y_n)\) for which \(Y_n-F\) is a forest. Write \(k_n\) for the minimum such cardinality, and write \(N_n\), \(T_n\), and \(Q_n\) for the numbers of minimum sets whose complements are, respectively, a forest, a connected tree, and a forest with two components.

**Theorem.** For odd \(n=2r+1\) (\(r\ge1\)),
\[
k_n=r+1,\qquad (N_n,T_n,Q_n)=\big((2r+1)2^r,(2r+1)2^r,0\big).
\]
For even \(n=2r\) (\(r\ge2\)),
\[
k_n=r+1,\qquad
(N_n,T_n,Q_n)=\big((3r^2+2r)2^{r-1},\;2r(r+1)2^{r-1},\;r^2 2^{r-1}\big).
\]
No minimum decycling set has a complement with three or more components. Thus maximum induced forests have \(2n-k_n\) vertices, and the same maximum cardinality is attained by induced trees; \(T_n\) counts all such maximum induced trees.

There is also an if-and-only-if structural description. Let \(C=\{i:F\cap\{a_i,b_i\}\ne\varnothing\}\) be the *occupied deletion columns*. A deleted column may contain one deleted vertex (*singleton*) or both (*double*). Two adjacent singleton columns form a **cut** if their deleted vertices belong to opposite rails.

* For \(n=2r+1\), a minimum set consists of singleton deletions on one of the \(n\) minimum vertex covers \(C\) of \(C_n\), with its unique adjacent pair of occupied columns forming a cut.
* For \(n=2r\), a minimum set is exactly one of two types: (i) an alternating vertex cover of \(C_n\) of size \(r\), with a double deletion in exactly one occupied column and singleton deletions in the other \(r-1\) columns; or (ii) a vertex cover \(C\) of \(C_n\) of size \(r+1\), with singleton deletions in all occupied columns and at least one cut among the two adjacent pairs of occupied columns.

For even \(n\), type (i) always leaves a tree. Type (ii) leaves a tree when exactly one of the two adjacent pairs is a cut, and leaves exactly two tree components when both pairs are cuts.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled. The cycle convention requires \(n\ge3\); the graph has \(2n\) vertices. All counts distinguish different subsets of labeled vertices and do not identify rotations or reflections. "Minimum" means smallest cardinality, not merely inclusion-minimal. The induced tree and forest statements concern induced subgraphs on vertex complements of minimum feedback sets; no assertion is made for larger-width cylindrical grids.

## Proof

**1. Square obstruction and column covers.** Every pair of consecutive columns gives a square \(a_i a_{i+1}b_{i+1}b_i a_i\). Deleting a vertex from at least one of those two columns is necessary to break the square. Therefore \(C\) is a vertex cover of the column cycle \(C_n\); in particular \(|F|\ge |C|\ge\lceil n/2\rceil\).

**2. Exact contraction criterion.** Suppose the occupied deletion columns form a vertex cover. Every column not occupied by \(F\) contains its rung \(a_ib_i\), and every singleton deletion column contains one remaining vertex. Two consecutive columns cannot both be unoccupied by \(F\). Thus if neither column is double-deleted, there is *at most one* surviving rail edge between them. Contract each surviving rung to a single vertex. The result is the graph of remaining columns with its consecutive-column edges, except that (a) all edges incident with a double-deleted column disappear, and (b) the edge between two adjacent singleton columns disappears exactly when the deleted vertices are on opposite rails. These disappearances are precisely the cuts defined above. Since each contraction removes an edge without changing cycle rank, and no parallel edges are created, the original induced graph is acyclic precisely when this column graph is acyclic. In particular, with no double-deleted column it is a cycle with one edge removed per cut: it is a forest if and only if there is at least one cut, with the number of components then equal to the number of cuts. If a double-deleted column exists and no other cuts occur, the remaining column graph is a path, hence the induced graph is a tree.

**3. Odd orders.** Put \(n=2r+1\). A vertex cover of \(C_n\) has size at least \(r+1\), so a deletion set with \(r+1\) vertices must have precisely one deleted vertex in every occupied column. The complements of minimum vertex covers are maximum independent sets of the odd cycle, of which there are exactly \(2r+1\); each such cover has exactly one adjacent pair of occupied columns. The contraction criterion forces this pair to be a cut. It imposes one binary inequality on the \(r+1\) rail choices, leaving \(2^r\) assignments. Each complement is a connected tree. This constructs the claimed optimum, proves the full characterization, and gives the odd-order counts.

**4. Even-order lower bound and two structural types.** Put \(n=2r\). If \(|F|=r\), then \(C\) has exactly \(r\) columns, necessarily one of the two alternating minimum covers of \(C_n\). Every deletion is a singleton, and no adjacent pair of occupied columns exists. There is consequently no cut, and the contraction criterion leaves a cycle. Hence \(k_n\ge r+1\). At size \(r+1\), the cover \(C\) either has size \(r\), causing exactly one double deletion, or has size \(r+1\), causing only singleton deletions. In the first case \(C\) is alternating, so deleting the entire chosen column leaves a path of surviving columns, and the contraction criterion proves the complement is a tree. In the second case every such cover has exactly two adjacent pairs of occupied columns. Its complement is a forest precisely when at least one of these two pairs is a cut. The constructions show \(k_n=r+1\) and prove the advertised classification.

**5. Enumeration by component number.** In the even case, alternating covers give \(2\cdot r=2r\) choices of the double-deletion column. Every other occupied column has an independent choice of deleted rail, so this contributes \(2r\,2^{r-1}\) tree complements. Covers of size \(r+1\) correspond to independent subsets of size \(r-1\) in \(C_{2r}\). The standard cyclic-gap count is
\[
\frac{2r}{r+1}\binom{r+1}{r-1}=r^2.
\]
For each such cover, the graph on its occupied columns induced by the column-cycle edges has exactly two edges and no cycle (because the cover is proper and \(r\ge2\)). Choosing a rail for every occupied column gives \(2^{r+1}\) assignments. Independently specifying whether each of the two neighboring-deletion pairs uses the same or opposite rails leaves \(2^{r-1}\) assignments for each of the four possibilities. Exactly three possibilities have one or two cuts, contributing \(3r^2 2^{r-1}\) forests. Of those, \(2r^2 2^{r-1}\) have one cut and hence are trees, while \(r^2 2^{r-1}\) have two cuts and hence have two components. Adding the two structural types gives all three even-order formulas. The odd-order component conclusion was proved in step 3.

## Verification

The included standalone `verify.py` uses only the Python standard library. Run `python3 verify.py`. It enumerates every deletion set of the optimal size and every set one vertex smaller for each order from \(3\) through \(12\), tests acyclicity directly using a disjoint-set data structure on the undeleted vertices, and independently tests the structural prediction from deletion-column patterns. These \(656{,}077\) candidate sets agree with the claimed if-and-only-if classification, optimum sizes, and exact one- and two-component multiplicities. The resulting total counts for orders \(3\) through \(12\) are \(6,32,20,132,56,448,144,1360,352,3840\). The finite check corroborates, but does not substitute for, the unrestricted proof above.

## Relationship to prior work

Bau and Beineke [1] describe the general decycling-number framework and degree bounds, not an all-optimal-set enumeration for cycle prisms. Verma and Binwal [2] establish the minimum decycling number of \(C_n\square P_2\) and present minimum examples; their result is credited here. It does not state the classification of *all* minimum sets or the split of maximum induced forests by connected-component number. The case \(n=3\) is also the rook graph \(K_2\square K_3\); an enumeration for the broader rectangular rook-graph family can cover that individual boundary case but not the full cycle-prism family. The genuinely additional assertion here is the uniform optimal-set classification and the exact multiplicities for all admissible orders, including the tree versus two-component split.

## Limitations

The proof and formulas are restricted to \(C_n\square K_2\) with \(n\ge3\). The number of *all* feedback vertex sets of nonminimum sizes is not computed. Literature searches and full-text comparisons do not rule out an equivalent older result under different terminology such as maximum induced forests or two-neighbor conversion sets; independent priority review remains appropriate. No independent mathematical audit has been performed.

## References

[1] S. Bau and L. W. Beineke, *The Decycling Number of Graphs*, arXiv:math/0703544v1, publicly posted 2007-03-19. https://arxiv.org/html/math/0703544v1

[2] V. K. Verma and J. Binwal, *Study of Decycling Number Problem in Prism Graph*, Advanced Engineering Science 55(1) (2023), 551–556; full text https://www.researchgate.net/publication/374030403_STUDY_OF_DECYCLING_NUMBER_PROBLEM_IN_PRISM_GRAPH (also https://advancedengineeringscience.com/article/2023/551.html).
