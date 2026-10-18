# Shortest octahedral carriers of Möbius–Kantor matching homology

## Finding
Let \(G=GP(8,3)\) be the Möbius–Kantor graph and let \(K=\mathcal M(G)\) denote its **ordinary** matching complex. A vertex of \(K\) is an edge of \(G\). The previously computed groups are \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^8\) and \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^4\); these ranks are background, not new claims.

The **minimum number of vertices of an induced subcomplex** \(K[W]\) whose fourth homology maps nontrivially into \(\widetilde H_4(K;\mathbb Z)\) is \(10\). There are **exactly \(912\)** such ten-vertex subsets \(W\). Every \(K[W]\) is the octahedral four-sphere \((S^0)^{*5}\cong S^4\), and the image of every oriented fundamental class is a **nonzero primitive** element of \(\widetilde H_4(K;\mathbb Z)\).

The full graph automorphism group has order \(96\) and splits the \(912\) spheres into **nine orbits of size \(96\) and one orbit of size \(48\)**. In the canonical enumeration specified below, the orbit-representative indices, sizes, and ranks of their integral homology spans are:

| Representative index | Orbit size | Integral span rank |
|---:|---:|---:|
| 0 | 96 | 8 |
| 1 | 96 | 7 |
| 2 | 96 | 7 |
| 3 | 96 | 7 |
| 4 | 96 | 4 |
| 6 | 96 | 8 |
| 7 | 96 | 8 |
| 9 | 96 | 8 |
| 13 | 96 | 7 |
| 17 | 48 | 7 |

**Every orbit-generated lattice is primitive in \(\widetilde H_4(K;\mathbb Z)\)**. In particular, **each of the four orbits represented by indices \(0,6,7,9\) separately generates all of \(\widetilde H_4(K;\mathbb Z)\) integrally**. One explicitly unimodular set of eight sphere classes is given by the carrier indices \(61,450,337,64,190,261,683,408\) from orbit \(0\), with determinant \(+1\) in the integral quotient coordinates below. The result is not merely a statement about rational spanning.

## Assumptions and scope
Take graph vertices \(0,\ldots,15\), write \(u_i=i\), \(v_i=8+i\), with subscripts modulo \(8\), and take the \(24\) undirected edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+3}\). Sort graph edges lexicographically by their two endpoints and label them \(0,\ldots,23\). The matching complex consists of all sets of these labels representing pairwise vertex-disjoint graph edges. Induced support is counted in **matching-complex vertices**, not in vertices of the original graph.

For two incident graph edges with indices \(a<b\), call \((a,b)\) a path pair. There are \(48\) such pairs because each of the \(16\) cubic graph vertices is the center of three unordered pairs of incident edges. Order all path pairs lexicographically, then recursively choose, in increasing path-pair order, five path pairs with pairwise disjoint **three-vertex sets in \(G\)**. This procedure lists the \(912\) carrier supports in canonical order, indexed \(0,\ldots,911\). A selected five-tuple \(((a_1,b_1),\ldots,(a_5,b_5))\) defines the fundamental cycle \((a_1-b_1)*\cdots*(a_5-b_5)\), with the usual signed simplicial join and the ascending edge-label simplex orientation. The standalone checker reconstructs this entire convention, including every sign.

## Proof
**1. The sharp flag-support bound.** For a finite flag complex, any induced vertex support that maps nontrivially in reduced homology of degree \(d\ge0\) has at least \(2d+2\) vertices. At equality its induced complex is the boundary of the \((d+1)\)-cross-polytope. Here is an induction proof, including the equality case. Choose a nonzero ambient homology class and a vertex-minimal induced support \(W\), represented by a cycle \(z\). For any \(v\in W\), decompose \(z=v*z_v+z'\). The chain \(z_v\) is a cycle in the link of \(v\). If it bounded in that link, adding a suitable boundary would remove all simplices containing \(v\), contradicting minimality. Thus the link carries nonzero reduced \((d-1)\)-homology, and induction forces at least \(2d\) link vertices. The vertex \(v\) has at least one nonneighbor in \(W\), for otherwise \(K[W]\) would be a cone. Hence \(|W|\ge 1+2d+1\). At equality each vertex has exactly one nonneighbor, so the complement of the one-skeleton is a perfect matching; because the complex is flag, the induced complex is exactly \((S^0)^{*(d+1)}\). The base case \(d=0\) is two nonadjacent points.

For \(d=4\), this proves the lower bound \(10\). In a matching complex, the five opposite vertex pairs of an octahedral four-sphere are pairs of **incident** graph edges, and graph edges from different pairs must be pairwise disjoint. They are therefore precisely five vertex-disjoint two-edge paths in \(G\). Conversely, any such five paths give an induced octahedral four-sphere. There are \(48\) possible path pairs, and exhaustive, nonduplicating backtracking produces exactly \(912\) disjoint five-tuples.

**2. Integral ambient chain model.** Reconstruct all \(11{,}068\) matchings including the empty matching. The nonempty matching-complex face vector, by dimensions \(0\) through \(7\), is
\[
(24,228,1096,2826,3816,2444,600,33).
\]
Apply successive face-poset toggles at graph-edge indices
\[
20,22,7,0,3,15,6,21,13,23,8,17,10,12,16,18,11,4,5,9,2,1,14,19.
\]
At each stage pair an available simplex omitting the chosen index with its still-available coface containing it. The checker verifies all \(53{,}256\) face-poset covers, the absence of directed cycles after reversing the \(5{,}525\) paired covers, and the critical-cell profile: one zero-cell, ten four-cells, and six five-cells. The algorithm and the ambient homotopy type are credited to the published Möbius–Kantor matching-complex computation cited below.

For the ten critical four-cells in ascending face-mask order, integral algebraic cancellation of matching pairs gives a Morse boundary matrix whose only nonzero column vectors are
\[
 u=(0,0,0,0,0,1,0,1,0,0),\qquad
 v=(0,1,0,1,0,0,0,0,-1,0).
\]
The six columns, in ascending critical-five-cell order, are \((u,0,0,v,u,0)\). These are two independent primitive vectors, so the integral homology quotient is \(\mathbb Z^{10}/\langle u,v\rangle\cong\mathbb Z^8\), with no torsion. An explicit isomorphism onto standard integral coordinates is
\[
 q(x_0,\ldots,x_9)=(x_0,x_2,x_3-x_1,x_4,x_6,x_7-x_5,x_8+x_1,x_9).
\]

**3. Individual classes and their primitive character.** The chain projection to critical four-cells is defined recursively: a critical four-cell projects to itself; an upper member of a three-/four-dimensional matched pair projects to zero; a lower member \(s\) of a four-/five-dimensional pair \((s,t)\) is replaced by the signed sum of the other four-faces of \(t\), divided by the unit incidence \([t:s]\). An acyclic matching guarantees that this integer recursion terminates and computes the integral Morse chain equivalence. Apply it to the \(32\)-simplex signed join cycle of each of the \(912\) carriers. The checker directly verifies that each simplicial boundary vanishes, then computes its \(q\)-image. In **every** case the eight integral coordinates have greatest common divisor \(1\). Thus all \(912\) classes are nonzero and primitive; the lower bound above is realized.

**4. Full symmetry and integral orbit lattices.** Exhaustive graph-isomorphism backtracking recovers all \(96\) automorphisms of \(G\), which permute the canonically indexed carrier supports. Their ten support orbits have sizes displayed above. For each orbit, exact rational row elimination gives the displayed span rank \(r\). A further **integer** witness is recorded in `verify.py` for every orbit: the `ORBIT_WITNESSES` array specifies \(r\) carrier columns and \(r\) of the eight \(q\)-coordinate rows whose determinant is \(+1\) or \(-1\). Such a unit minor proves that the rank-\(r\) orbit span is a direct summand of \(\mathbb Z^8\), not merely a full-rank subspace over \(\mathbb Q\). Four orbits have \(r=8\); consequently each one is the whole integral homology group. In particular, the eight specified carrier indices in orbit \(0\) give determinant \(+1\).

## Verification
Run `python3 verify.py` and `python3 check_mod2.py` in the directory containing this document and the checkers. Both require only Python's standard library. The checker recomputes the graph, all faces, every cover in the Morse acyclicity test, all critical cells and the signed Morse boundary, all \(912\) signed sphere cycles and their chain boundaries, all integral quotient images, all \(96\) automorphisms, all ten orbits, all ten exact ranks, and a unit determinant for every orbit. Its terminal marker is `VERIFY_OK_MOBIUS_KANTOR_SHORTEST_CARRIERS`. The second program independently constructs the unreduced simplicial chain maps modulo two, finding ranks \(1935\) and \(1873\) for the degree-four and degree-five boundary maps, respectively; it confirms that all \(912\) cycles are separately nonboundaries and that their mod-two span has dimension \(8\). Its marker is `VERIFY_OK_DIRECT_MOD2`. Both checkers were executed successfully from the actual package paths. The integer argument, not the mod-two corroboration, proves integral primitivity.

## Relationship to prior work
Shareshian and Wachs developed foundational matching-complex homology, including integral torsion and complete-graph/chessboard classes, but do not give the present induced-support classification for \(GP(8,3)\). Donovan and Scoville compute matching-complex homotopy for paths, cycles, and Dutch windmill graphs; these objects are different. Bayer, Goeckner, and Jelić Milutinović classify manifold matching complexes; that classification neither addresses the nonmanifold full \(K\) here nor provides its minimum-support inclusion maps.

A publicly available exact computation entitled *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge* previously established \(K\simeq(\bigvee^{8}S^4)\vee(\bigvee^{4}S^5)\) and supplied the staged Morse toggle order. **That homotopy type and Morse matching are credited, not claimed as new.** Its inspected complete result and verifier calculate the ambient type, but do not classify the \(912\) shortest induced spheres, their individual primitive inclusion classes, ten symmetry orbits, or the distinct integral orbit-generated lattices. These latter statements are the contribution here and cannot be deduced from the abstract homotopy type alone.

## Limitations
This is an exact finite theorem for this specified graph, with no asserted extension to other generalized Petersen graphs. The lower bound is about induced vertex supports in the ordinary matching complex, not geometric lengths or supports after subdivision. The theorem determines minimal induced carriers for fourth homology, not the minimal supports of the separate fifth-homology classes. The complete integral orbit-lattice calculations depend on the reproducible signed simplicial and Morse reduction; a finite-field rank alone would not establish them. Searches and primary-source comparisons found no directly covering statement, but equivalent unpublished or unindexed results remain possible. An independent audit has not yet been performed.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first public version 2004-09-03; Adv. Math. 212 (2007), 525–570.
2. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, first public version 2022-07-27; NYJM 29 (2023), 1393–1412.
3. M. Bayer, B. Goeckner, and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328, first public version 2019-06-07; Mathematika 66 (2020), 973–1002.
4. *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge*, publicly indexed finding and complete verification code, published-finding corpus (2026-10-04), `2026/10/4/SCOPE-the-m-bius-kantor-matching-complex-is-a-mixed-dimensional-sphere--4bfded76792e`.
