# Complete graph-metric Vietoris–Rips filtration of the Pappus graph
## Finding
Let \(P\) be the Pappus graph on vertices \(0,\ldots,17\), given by the LCF description \([5,7,-7,7,-7,-5]^3\), and equip its vertices with shortest-path distance. For the inclusive Vietoris–Rips complex \(\operatorname{VR}_{\le r}(P)\), for every real \(r\ge 0\),
\[
\operatorname{VR}_{\le r}(P)\simeq
\begin{cases}
\bigvee^{17}S^0,&0\le r<1,\\
\bigvee^{10}S^1,&1\le r<2,\\
\bigvee^{26}S^2,&2\le r<3,\\
\bigvee^{64}S^5,&3\le r<4,\\
\ast,&r\ge4.
\end{cases}
\]

## Assumptions and scope
The graph is the simple cubic graph obtained from the cycle edges \(i\sim i+1\pmod {18}\) together with the LCF chords specified by \([5,7,-7,7,-7,-5]^3\). Distance is unweighted graph distance. The Vietoris–Rips convention is inclusive: a finite vertex set is a simplex exactly when its diameter is at most \(r\). Since all distances are integral and the graph has diameter \(4\), only the thresholds \(0,1,2,3,4\) matter.

## Proof
At scale below \(1\), the complex is the discrete set of \(18\) vertices, hence \(\bigvee^{17}S^0\).

At scale \(1\), the Pappus graph has no triangles, so the Rips complex is the graph itself. It is connected with \(18\) vertices and \(27\) edges, hence has cycle rank \(27-18+1=10\) and is homotopy equivalent to \(\bigvee^{10}S^1\).

At scale \(2\), exhaustive face enumeration gives face vector
\[
(f_0,f_1,f_2,f_3)=(18,81,108,18).
\]
Apply successive vertex-toggle matching in the order
\[
9,6,5,11,12,17,16,13,10,14,0,2,15,8,3,7,1,4.
\]
Whenever an unmatched face \(\sigma\) does not contain the current vertex \(v\) and \(\sigma\cup\{v\}\) is also an unmatched face, pair \(\sigma\) with \(\sigma\cup\{v\}\). This produces \(99\) matched pairs. Exact orientation of the complete Hasse diagram verifies that the matching is acyclic. The only critical cells are one \(0\)-cell and \(26\) cells of dimension \(2\). Forman discrete Morse theory therefore gives
\[
\operatorname{VR}_{\le2}(P)\simeq\bigvee^{26}S^2.
\]

At scale \(3\), the only forbidden pairs are pairs at graph distance \(4\). The distance-\(4\) graph is exactly the disjoint union of the six triangles
\[
\{0,10,14\},\ \{1,11,15\},\ \{2,6,16\},\ \{3,7,17\},\ \{4,8,12\},\ \{5,9,13\}.
\]
Thus \(\operatorname{VR}_{\le3}(P)\) is the independence complex of \(6K_3\). Independence complexes turn disjoint unions into joins, and \(\operatorname{Ind}(K_3)\) is a three-point space, homotopy equivalent to \(\bigvee^2S^0\). Hence
\[
\operatorname{VR}_{\le3}(P)
=\operatorname{Ind}(6K_3)
\simeq \mathop{\ast}_{j=1}^{6}\bigl(\bigvee^2S^0\bigr)
\simeq\bigvee^{2^6}S^5
=\bigvee^{64}S^5.
\]
Finally, every pair of vertices is at distance at most \(4\), so at scale \(4\) the complex is the full \(17\)-simplex and is contractible.

## Verification
The standalone verifier `artifacts/pappus_rips_verify.py` uses only the Python standard library. It reconstructs the graph from the LCF data, computes all-pairs shortest-path distances, enumerates every Rips face at scales \(2\) and \(3\), builds the stated toggle matching, and topologically sorts the fully oriented Hasse diagram to certify acyclicity. It also computes mod-\(2\) boundary ranks independently.

The verified distance-shell pair counts are \(27,54,54,18\) at distances \(1,2,3,4\). At scale \(2\), the mod-\(2\) Betti vector is \((1,0,26,0)\). At scale \(3\), the face vector is
\[
(18,135,540,1215,1458,729)
\]
and the mod-\(2\) Betti vector is \((1,0,0,0,0,64)\). These homology computations are cross-checks; the homotopy claims use the acyclic matching at scale \(2\) and the exact six-triangle decomposition at scale \(3\).

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine complete Vietoris–Rips filtrations for the vertex sets of the Platonic solids and use combinatorial graph distance together with discrete Morse theory. Their theorem covers the five Platonic solids and does not include the Pappus graph; a full-text search of arXiv:2302.14388v1 finds no occurrence of “Pappus.” The paper explicitly points to extensions beyond the treated regular polytopes as a natural direction.

The closest indexed published-finding corpus records found concern other structured metrics: complete graph-metric filtrations of the truncated tetrahedron, scale-two Rips complexes of finite projective-plane incidence graphs, and a Euclidean cuboctahedron filtration. The finite-projective-plane theorem does not imply the present result: the Pappus configuration is not a finite projective plane, and the present claim also determines the scale-\(3\) and terminal stages. Previously published related findings give complete filtrations for the Desargues and Möbius–Kantor graphs, but neither statement implies the Pappus computation because their farthest-distance graphs and scale-\(2\) clique complexes are different.

## Limitations
This is an exact result for one finite graph metric, not a classification of cubic symmetric or distance-regular graphs. The proof determines homotopy types at every scale but does not classify the inclusion maps up to homotopy, so no stronger persistence-module statement is asserted. Literature searches cannot prove global novelty; an unindexed computation under different terminology, such as clique complexes of graph powers, remains a residual possibility.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, “Vietoris–Rips complexes of Platonic solids,” arXiv:2302.14388v1, first submitted 2023-02-28. Primary MSC 55N31.
2. Pappus graph reference data: LCF \([5,7,-7,7,-7,-5]^3\), cubic, distance-regular, diameter \(4\); Wolfram MathWorld, “Pappus Graph.”
3. M. Forman, “Morse theory for cell complexes,” Adv. Math. 134 (1998), 90–145.
