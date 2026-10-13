# Exact minimum zero-forcing configurations of the Desargues graph

## Finding
Let \(D\) be the twenty-vertex Desargues graph, realized as the incidence graph between the ten two-element subsets and ten three-element subsets of a fixed five-element set. Under ordinary zero forcing, initially black vertices can turn a white neighbor black if it is their only white neighbor.

**Theorem.** The zero forcing number \(Z(D)=8\) is known. Every minimum zero-forcing set contains exactly four two-element subsets and four three-element subsets. There are exactly
\[
13\,520
\]
such minimum sets. Under the full automorphism group of \(D\), they split into exactly \(67\) orbits: one of size \(20\), one of size \(60\), eighteen of size \(120\), and forty-seven of size \(240\). The accompanying CSV specifies a complete set of orbit representatives with an exact integer encoding.

The **new enumerative assertion** is the exact total \(13\,520\) and the complete \(67\)-orbit classification. The previously published value \(Z(D)=8\) is not claimed as new. The balanced-side restriction follows from an explicit signed-incidence kernel argument closely related to the previously published zero-diagonal matrix witness for this graph.

## Assumptions and scope
The ground set is \(U=\{1,2,3,4,5\}\). Its graph vertices are \(V_2=\binom U2\) and \(V_3=\binom U3\). An edge joins \(E\in V_2\) and \(T\in V_3\) precisely when \(E\subset T\). This is the Desargues graph, equivalently the generalized Petersen graph \(P(10,3)\). No weighted forcing rule or alternate positive-semidefinite/skew convention is used.

For the certificate's integer labeling, list the ten two-subsets in lexicographic order, then the ten three-subsets in lexicographic order. The subset encoded by \(m\in[0,2^{20})\) contains vertex \(i\) exactly when the binary digit of weight \(2^i\) in \(m\) is one, for \(0\le i<20\). Orbit sizes in the CSV refer to this exact labeling.

## Proof
**1. A signed-incidence lower bound and balance.** Orient each edge and triangle of the complete four-simplex on \(U\) by increasing vertex order. The simplicial boundary map from oriented triangles to oriented edges has a \(10\)-by-\(10\) integer matrix \(B\). Each column has precisely three entries \(\pm1\), supported on the two-subsets contained in the corresponding three-subset. Thus the symmetric block matrix
\[
A=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}
\]
has nonzero entries at *exactly* the edges of \(D\).

The edge-to-vertex boundary \(\partial_1\) has rank \(4\), and the triangle-to-edge boundary \(\partial_2=B\) satisfies \(\partial_1\partial_2=0\). The triangles generate the entire cycle space of the complete graph on five vertices, so \(\operatorname{im}(B)=\ker(\partial_1)\). Consequently \(\operatorname{rank}(B)=10-4=6\). Both \(\ker(B)\) and \(\ker(B^{\mathsf T})\) have dimension four.

For any real symmetric matrix with nonzero off-diagonal entries exactly on the edges of a graph, a kernel vector that vanishes on an ordinary zero-forcing set must vanish identically: whenever an already black vertex has exactly one white neighbor, its matrix equation forces the remaining coordinate to vanish. If a putative forcing set had at most three vertices in \(V_2\), one could choose a nonzero vector supported on \(V_2\), lying in \(\ker(B^{\mathsf T})\), and vanishing on these at most three prescribed coordinates. This would contradict the preceding forcing property. Swapping the sides gives at least four chosen vertices in \(V_3\) as well. Hence every forcing set has at least eight vertices, and every eight-vertex forcing set is balanced four-and-four.

**2. An eight-vertex witness.** The set
\[
\{12,13,14,15,123,124,134,234\}
\]
uses the shorthand \(12=\{1,2\}\) and \(123=\{1,2,3\}\). Its complete chronological forcing sequence is
\[
12\to125,\quad13\to135,\quad14\to145,\quad123\to23,\quad
23\to235,\quad124\to24,\quad24\to245,\quad125\to25,\quad
134\to34,\quad34\to345,\quad135\to35,\quad145\to45.
\]
Each arrow is a legal ordinary force in the order shown. Therefore eight vertices suffice, so the lower bound is sharp. More generally, for any distinct \(a,b\in U\), take the four two-subsets containing \(a\) and the four three-subsets contained in \(U\setminus\{b\}\). These \(5\cdot4=20\) configurations are forcing by ground-set symmetry. Ground-set complementation sends the configuration indexed by \((a,b)\) to that indexed by \((b,a)\); thus they form one complete orbit of size \(20\).

**3. Exact finite enumeration.** By Step 1, all minimum sets lie among the \(\binom{10}{4}^2=44\,100\) balanced eight-vertex candidates. The accompanying `verify.py` generates every candidate exactly once. Starting with its bit mask, it repeatedly applies the rule that every black vertex with exactly one white neighbor forces that neighbor. A candidate is accepted if and only if the eventual closure contains all twenty vertices. The loop tests precisely all \(44\,100\) candidates and finds exactly \(13\,520\) accepted masks. A separately implemented sequential version confirms every classification. A second implementation, `verify_gp.cpp`, constructs the graph independently as \(P(10,3)\), checks the explicit graph isomorphism edge-by-edge, and exhaustively examines all \(\binom{20}{8}=125\,970\) eight-vertex candidates. It independently obtains the same count and balance.

**4. Full symmetry and orbit census.** Any automorphism either preserves the two bipartition classes or swaps them. On \(V_2\), two distinct vertices have a common neighbor precisely when their two-subsets intersect; this auxiliary graph is the triangular graph \(T(5)\), whose automorphisms are exactly permutations of the five ground elements (its five maximal four-cliques recover the ground points). Such a permutation determines the action on \(V_3\) uniquely. Ground-set complementation swaps \(V_2\) and \(V_3\) while preserving incidences. Thus the full group has size \(2\cdot5!=240\), consisting exactly of permutations and their composites with complementation.

The verifier constructs all \(240\) actions, checks that each preserves adjacency, and repeatedly computes the group orbit of the lexicographically least remaining accepted mask. The orbits are disjoint and exhaust the accepted masks. The resulting sizes are \(20\) once, \(60\) once, \(120\) eighteen times, and \(240\) forty-seven times; their sum is \(13\,520\). The \(67\) representative masks and orbit sizes are given in `orbit_representatives.csv`; they are independently replayed, not merely tabulated without verification.

## Verification
Run `python3 verify.py` in the directory containing `verify.py` and `orbit_representatives.csv`. The program uses only the Python standard library, computes exact rational matrix ranks, confirms the simplicial boundary identity, checks the forcing closure by two implementations on every balanced candidate, constructs the full \(240\)-element group, and reconstructs the complete orbit partition.

For a graph-model-independent check, compile and execute `g++ -O2 -std=c++17 verify_gp.cpp -o verify_gp && ./verify_gp`. It generates the generalized Petersen graph from its cyclic definition and exhausts every eight-vertex candidate. All comparisons use integer masks and integer or exact rational arithmetic; the finite output is not an extrapolation to a graph family.

## Relationship to prior work
The AIM Minimum Rank–Special Graphs Work Group introduced zero forcing and its maximum-nullity connection; the original article was available online on 26 November 2007 [1]. Butler, Grout and Hall explicitly reported \(Z(D)=8\) and gave a signed symmetric matrix witness for the Desargues graph in their Section 5 and Figure 5.1 [2]. Their paper studies inertia sets and forcing variants rather than counting and classifying every optimum ordinary forcing set. Rashidi, Shajareh Poursalavati and Tavakkoli studied zero forcing of generalized Petersen graphs and derived several family bounds [3]. A later correction examines the scalar zero-forcing number on the subfamily \(P(n,3)\) [4]. These scalar claims and constructions are prior work, not claimed here.

## Limitations
The result concerns exactly the twenty-vertex Desargues graph, not a formula for arbitrary generalized Petersen graphs. The \(13\,520\) count and the \(67\) orbit partition rely on fully specified finite exhaustive computation, supported by two distinct implementations; the group proof and lower bound are symbolic. No assertion is made about unique priority in inaccessible or unindexed literature. The full text of the recent correction [4] was not available during this literature comparison, so an earlier equivalent count under other terminology remains a residual priority risk.

## References
[1] AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009. Online availability recorded 2007-11-26.

[2] S. Butler, J. Grout, H. T. Hall, *Using variants of zero forcing to bound the inertia set of a graph*, Electronic Journal of Linear Algebra 30 (2015), 1–18. DOI: 10.13001/1081-3810.2900. See Section 5, Figure 5.1, and Appendix A.

[3] S. Rashidi, N. Shajareh Poursalavati, M. Tavakkoli, *Computing the zero forcing number for generalized Petersen graphs*, Journal of Algebra Combinatorics Discrete Structures and Applications 7 (2020), 183–193. DOI: 10.13069/jacodesmath.729465.

[4] A. Krishnan, *A correction to the Zero Forcing Number of the Generalized Petersen Graphs \(P(n,3)\)*, arXiv:2607.19412 (2026); abstract inspected, complete text not accessible during the comparison.
