# Lucas-cube flux sectors in the triangular-face reversal graph of antiprisms

## Finding
For every integer \(n\ge3\), the graph of Eulerian orientations of the \(n\)-antiprism, with a move reversing a directed **triangular belt face** and with both polygonal cap faces excluded, is isomorphic to
\[
2K_1\;\sqcup\;2\Lambda_{2n}.
\]
Here \(\Lambda_m\) denotes the Lucas cube: its vertices are independent sets of the cycle \(C_m\), and edges toggle one occupied site. In particular, there are four connected components, two consisting of single orientations and two consisting of \(L_{2n}\) orientations each. The reconfiguration graph has \(2+2L_{2n}\) vertices and \(4nF_{2n-1}\) edges, where \(F_0=0,F_1=1\) and \(L_0=2,L_1=1\), both obeying the Fibonacci recurrence.

Within either nonsingleton component, the exact minimum number of triangular-face reversals between orientations corresponding to independent sets \(I,J\subseteq V(C_{2n})\) is \(|I\triangle J|\). Each component is an isometric subgraph of a \(2n\)-cube, a median graph, has diameter exactly \(2n\), and has exactly one unordered pair at that diameter.

## Assumptions and scope
Let \(A_n\) have vertices \(T_i,B_i\), for \(i\in\mathbb Z/n\mathbb Z\), and edges \(T_iT_{i+1}\), \(B_iB_{i+1}\), \(B_iT_{i+1}\), and \(T_iB_i\). These form a simple connected \(4\)-regular antiprism for \(n\ge3\). An Eulerian orientation means indegree and outdegree \(2\) at **each** of its \(2n\) vertices. The only allowed faces for a move are the \(2n\) triangles \((T_i,T_{i+1},B_i)\) and \((B_i,T_{i+1},B_{i+1})\). A move is legal if all three face edges form a directed cycle, and it reverses those three directions. The two cap cycles are never permitted as moves: for \(n=3\), their triangles remain explicitly excluded. The graph of orientations is undirected and has no self-loops.

Fix reference edge directions \(T_i\to T_{i+1}\), \(B_i\to B_{i+1}\), \(B_i\to T_{i+1}\), and \(T_i\to B_i\). Let \(t_i,b_i,d_i,v_i\in\{0,1\}\) indicate agreement with the corresponding reference direction. All indices in formulas below are cyclic.

## Proof
**1. A conserved flux and boundary sectors.** At vertices \(T_i\) and \(B_i\), the Eulerian equations are precisely
\[
t_i+v_i=t_{i-1}+d_{i-1},\qquad b_i+d_i=b_{i-1}+v_i.
\]
Their sum shows that \(j_i=t_i+b_i+d_i\) is independent of \(i\); write \(j\in\{0,1,2,3\}\) for its common value. Reversing an upper belt triangle toggles \(t_i,d_i,v_i\), while reversing a lower belt triangle toggles \(b_i,d_i,v_{i+1}\). Each toggle interchanges a \(0\) and \(1\) among \((t_i,b_i,d_i)\); hence \(j\) is a component invariant. When \(j=0\), all triples are zero and the displayed equations force every vertical bit to be zero. Similarly, \(j=3\) forces every edge bit to be one. Neither orientation permits a directed belt triangle. These give two isolated vertices.

**2. An exact cyclic-binary encoding.** Suppose \(j=1\). The triple \((t_i,b_i,d_i)\) is one of \(X=(0,0,1)\), \(Y=(0,1,0)\), or \(Z=(1,0,0)\). The first Eulerian equation forces
\[
v_i=t_{i-1}+d_{i-1}-t_i.
\]
This is a binary value for every consecutive pair of states except \(Y\) followed by \(Z\). The second Eulerian equation automatically follows from constancy of \(j\). Thus a cyclic word in \(X,Y,Z\) gives exactly one Eulerian orientation if and only if it has no cyclic occurrence of \(YZ\).

Associate to each state the two bits
\[
X\longleftrightarrow 00,\qquad Y\longleftrightarrow 01,\qquad Z\longleftrightarrow 10.
\]
Concatenate the pairs in cyclic order. The restrictions already prevent two adjacent occupied bits inside a pair; the only forbidden boundary adjacency is the second bit of a \(Y\) pair followed by the first bit of a \(Z\) pair. Consequently the cyclic words are **exactly** the binary independent-set indicators on \(C_{2n}\), including the wraparound condition. This correspondence is bijective because the vertical bits are forced by the formula above.

**3. Face reversals are precisely single-site toggles.** An upper belt-face reversal toggles the triple bits \(t_i,d_i\), hence changes \(X\leftrightarrow Z\); it is legal exactly when the previous cell is not \(Y\), which is exactly the condition for toggling the first site of cell \(i\) while retaining an independent set. A lower belt-face reversal toggles \(b_i,d_i\), hence changes \(X\leftrightarrow Y\); it is legal exactly when the next cell is not \(Z\), the condition for toggling the second site of cell \(i\). The changes to the relevant vertical bits are forced by the Eulerian equations and yield the directed-cycle condition. Hence the complete induced move graph on flux \(j=1\) is \(\Lambda_{2n}\).

Complementing every edge-orientation bit takes Eulerian orientations to Eulerian orientations and carries flux \(j\) to \(3-j\), preserves legality of face reversals, and interchanges the \(j=1\) and \(j=2\) sectors. Thus the second sector is another, disjoint copy of \(\Lambda_{2n}\), completing the component classification.

**4. Metric and enumeration.** Independent sets \(I,J\) are connected by first removing all elements of \(I\setminus J\), then adding all elements of \(J\setminus I\); each intermediate set remains independent. This uses \(|I\triangle J|\) moves, while any path must toggle every differing coordinate, so the distance is exact. The coordinatewise majority set of any three independent sets is independent: two adjacent sites cannot each occur in a majority of three sets, because those two majorities would intersect. This gives a unique median by the ambient Hamming metric. Maximum Hamming distance is \(2n\), attained only by the pair of alternating maximum independent sets, proving the diameter and unique antipodal pair claims.

The number of independent sets of \(C_m\) is the Lucas number \(L_m\). Each edge of \(\Lambda_m\) is uniquely determined by the site whose occupancy is toggled and by an independent set on the path remaining after that site and its two neighbors are deleted. That path has \(m-3\) vertices and \(F_{m-1}\) independent sets. Thus \(|E(\Lambda_m)|=mF_{m-1}\); substituting \(m=2n\) and accounting for two copies gives the displayed total counts.

## Verification
Two independently implemented exact checkers accompany this manuscript. Run `python3 verify_antiprism_transfer.py` to build all states from independent cyclic binary strings and compare their full sets of legal triangular reversals against single-site toggles for \(3\le n\le9\). Run `g++ -std=c++17 -O2 verify_antiprism_direct.cpp -o verify_antiprism_direct` followed by `./verify_antiprism_direct` to independently enumerate raw edge orientations with degree-balance pruning, construct actual face-reversal edges, and verify the component and adjacency classifications for \(3\le n\le8\). The largest checked case has \(4416\) orientations in the direct search and \(11558\) orientations in the cyclic-state checker. Their finite ranges corroborate, but do not establish, the unbounded theorem.

## Relationship to prior work
Felsner's 2004 theory establishes distributive-lattice structure for planar Eulerian orientations under **all eligible bounded face reversals**. Creed's 2007 analysis of face-reversal chains likewise permits arbitrary faces and addresses sampling, not an exact omitted-cap antiprism-sector decomposition. Because this result explicitly restricts moves to triangular belt faces, its four-component graph is not covered by those all-face connectivity statements. Munarini, Perelli Cippo and Zagaglia Salvi (2001) studied Lucas cubes and their graph parameters, so their vertex, edge and diameter properties are prior knowledge. The contribution here is the explicit flux invariant and orientation-preserving, edge-preserving bijection identifying two **antiprism-orientation flip components** with those Lucas cubes, with two further frozen orientations. Codara and D'Antona (2014) study Lucas cubes and their generalizations, without this Eulerian-orientation realization.

## Limitations
The theorem is for \(n\ge3\), exactly the specified antiprism graph, balanced edge orientations, and reversals of triangular belt faces only. Allowing polygonal cap reversals changes the component graph and is not covered. The statement does not assert a new property of Lucas cubes in isolation; their standard enumerative and metric identities are credited. No claim is made that searching indexed literature proves absolute novelty. Equivalent statements under height-function, ice-model, or other terminology may exist; independent scholarly validation has not been performed.

## References
1. S. Felsner, *Lattice Structures from Planar Graphs*, Electronic Journal of Combinatorics **11** (2004), R15, DOI `10.37236/1768` (published 2004-02-14). Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r15/pdf/ .
2. E. Munarini, C. Perelli Cippo and N. Zagaglia Salvi, *On the Lucas Cubes*, Fibonacci Quarterly **39** (2001), 12–21. Full text: https://www.fq.math.ca/Scanned/39-1/munarini.pdf .
3. P. Creed, *Sampling Eulerian orientations of triangular lattice graphs*, arXiv:`cs/0703031` (first posted 2007-03-07). Full text: https://arxiv.org/pdf/cs/0703031 .
4. P. Codara and O. D'Antona, *Generalized Fibonacci and Lucas cubes arising from powers of paths and cycles*, arXiv:`1410.4080` (first posted 2014-10-15). Full text: https://arxiv.org/abs/1410.4080 .
