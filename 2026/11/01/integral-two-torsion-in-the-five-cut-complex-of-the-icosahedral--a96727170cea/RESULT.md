# Integral two-torsion in the five-cut complex of the icosahedral graph

## Finding
Let \(I\) denote the standard icosahedral graph on twelve vertices. Its ordinary five-cut complex \(X=\Delta_5(I)\) has the complete reduced integral homology
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z/2,&j=4,\\
\mathbb Z^{30},&j=6,\\
0,&\text{otherwise},
\end{cases}
\qquad j\in\mathbb Z.
\]
The complex is pure of dimension six but has torsion in degree four. Therefore it is not shellable, and cannot be homotopy equivalent to any wedge of spheres.

## Assumptions and scope
The graph is the simple, undirected, twelve-vertex, thirty-edge icosahedral graph. It is specified completely by the edge list `EDGES` in `verify_icosahedral_five_cut.py`; this list is isomorphic to the standard icosahedral graph. For each five-element vertex set \(A\), let \(I[A]\) be the induced subgraph on \(A\). The facets of \(X\) are exactly \(V(I)\setminus A\) for the five-element sets \(A\) such that \(I[A]\) is disconnected. Every face is a subset of such a facet. All chains, boundaries and homology groups are over \(\mathbb Z\), unless a coefficient field is explicitly specified. Reduced homology is used throughout. The statement concerns only this graph and this cut-size parameter.

## Proof
First enumerate all \(\binom{12}{5}=792\) five-vertex sets using the explicit edge list. Exactly 300 induce disconnected subgraphs. Their complements are distinct facets of cardinality seven, so \(X\) is pure six-dimensional. Enumerating all subsets of these facets produces exactly 2,618 faces, including the empty face. In dimensions \(-1,0,1,2,3,4,5,6\), respectively, the face counts are \(1,12,66,220,495,792,732,300\). A second exhaustive construction starts with each of the 4,096 vertex subsets, tests whether its complement contains a disconnected five-subset using an independent graph search, and agrees on every face.

For each of two different total vertex orders, construct a staged element matching. At each vertex, match each currently unmatched face omitting that vertex with the corresponding currently unmatched face containing the vertex whenever both are present. The resulting complete directed Hasse graph is verified acyclic by a topological sort of all 13,224 covering incidences among nonempty faces. Hence the pairs form an acyclic discrete-Morse matching. All paired boundary coefficients are initially \(\pm1\), and in the signed integral chain elimination every pivot coefficient is independently checked to remain \(\pm1\). The algebraic cancellation formula for a pair \((\ell,h)\) replaces every other coefficient from a column \(c\) to a row \(r\) by \(d_{r,c}-d_{\ell,c}d_{\ell,h}^{-1}d_{r,h}\); it then deletes \(\ell\) and \(h\). This is an invertible change of bases followed by cancellation of a contractible chain summand, hence preserves integral homology. The verifier also tests that each resulting differential squares to zero.

For the increasing vertex order, 1,286 pairs remain after matching, leaving exactly one critical zero-cell, five critical four-cells, seven critical five-cells and 32 critical six-cells. All other positive-dimensional chain groups vanish. The integer reduced boundary \(\partial_5:\mathbb Z^7\to\mathbb Z^5\) has Smith invariant factors \((1,1,1,1,2)\). Thus \(\operatorname{coker}\partial_5\cong\mathbb Z/2\) and \(\ker\partial_5\) has rank two. The boundary \(\partial_6:\mathbb Z^{32}\to\mathbb Z^7\) has Smith invariant factors \((1,1)\), and \(\partial_5\partial_6=0\). Its rank-two image is a *primitive* sublattice of \(\mathbb Z^7\); because it lies in the rank-two kernel of \(\partial_5\), these two lattices coincide. Therefore degree-five homology vanishes, while \(\ker\partial_6\cong\mathbb Z^{30}\). Degree-four homology is \(\mathbb Z/2\), and every other reduced degree vanishes.

As an independent chain reduction, reversing the vertex order gives 1,285 matched pairs and critical-cell counts \(1,5,8,33\) in degrees \(0,4,5,6\). Its fifth boundary has exactly the same nonzero Smith factors \((1,1,1,1,2)\); its sixth boundary has three unit Smith factors. The same reasoning reproduces the integral groups. In addition, computing the *unreduced* simplicial boundaries directly over \(\mathbb F_2\) gives ranks \((11,55,165,330,461,270)\) in degrees one through six. These ranks imply reduced mod-two homology of rank one in each of degrees four and five and rank 30 in degree six, consistent with the integral calculation by the universal coefficient theorem.

Finally a shellable pure six-dimensional simplicial complex is homotopy equivalent to a wedge of six-spheres (or is contractible), so it has torsion-free reduced homology. Any wedge of spheres has torsion-free integral homology. Both conclusions contradict the nonzero \(\mathbb Z/2\) group.

## Verification
Run `python verify_icosahedral_five_cut.py` with Python 3.10 or newer and SymPy installed. It reconstructs the graph, enumerates all faces by two independent definitions, calculates complete mod-two simplicial boundary ranks, constructs two different acyclic matchings, checks all 13,224 directed Hasse incidences for each, carries out exact signed integral elimination and computes the Smith normal forms using SymPy integer normal forms. The deterministic full result, including both resulting sparse-to-dense integer boundary matrices, is in `verification_output.json`. It records `ICOSAHEDRAL_FIVE_CUT_INTEGRAL_TORSION_EXACT_VERIFIED` and all assertions pass. The matrices and code are part of this finding, not references to earlier computations.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue define and study ordinary cut complexes in *Topology of Cut Complexes of Graphs* (first public arXiv version April 26, 2023). Their Remark 4.2 obtains an example with integral torsion by realizing a minimal triangulation of the real projective plane as a cut complex on a specially constructed sixteen-vertex graph. That construction does not calculate the ordinary five-cut complex of the icosahedral graph. Their Theorem 6.1 guarantees torsion-freeness under the hypothesis of a complete codimension-one skeleton, which **does not hold here**: this complex has 732 five-dimensional faces rather than all \(\binom{12}{6}=924\). Their *Topology of Cut Complexes II* (first public arXiv version July 11, 2024) treats disjoint unions, squared paths and grids, not the icosahedral five-cut complex. An existing calculation of the icosahedral **three-cut** complex concerns a distinct parameter and does not imply the present torsion statement. The finding complements, rather than replaces, the previously known engineered torsion example.

## Limitations
This proves the precise **integral homology**, not a full integral homotopy classification, explicit geometric torsion-cycle representative or equivariant automorphism action. Numerical counts and finite integer Smith calculations do not imply any universal theorem for other cut sizes or graphs. Searches and inspected literature cannot rule out all unpublished, inaccessible or unindexed equivalent calculations. Independent external auditing has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, version 1, April 26, 2023. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, version 1, July 11, 2024. https://arxiv.org/abs/2407.08158
