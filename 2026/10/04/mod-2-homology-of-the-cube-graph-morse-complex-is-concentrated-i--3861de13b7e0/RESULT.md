# Mod-\(2\) homology of the cube-graph Morse complex is concentrated in degrees \(5\) and \(6\)
## Finding
Let \(Q_3\) be the graph with vertex set \(\{0,1\}^3\), with two vertices adjacent exactly when they differ in one coordinate. For the ordinary Morse complex \(\mathcal M(Q_3)\) of acyclic discrete vector fields,
\[
\widetilde H_i(\mathcal M(Q_3);\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^4,& i=5,\\
\mathbb F_2^{139},& i=6,\\
0,& \text{otherwise}.
\end{cases}
\]
Thus the first non-cycle hypercube case has nonzero reduced mod-\(2\) homology in two adjacent dimensions. In particular, \(\mathcal M(Q_3)\) cannot be homotopy equivalent to a wedge of spheres all having one common dimension.

## Assumptions and scope
A primitive discrete vector field on a graph pairs a vertex with an incident edge. A simplex of \(\mathcal M(Q_3)\) is a set of such pairs in which no graph vertex or graph edge is used twice and there is no nontrivial closed \(V\)-path. Pairing a graph vertex \(u\) with an edge \(\{u,v\}\) is encoded as a directed edge \(u\to v\). For graphs, the compatibility condition says that every vertex has outdegree at most one, while the absence of closed \(V\)-paths is exactly the absence of directed cycles. Coefficients in the homology statement are only \(\mathbb F_2\).

## Proof
The cube has eight vertices and twelve edges. Process its twelve undirected edges in a fixed order. Each edge has exactly three states: absent, directed from its first endpoint to its second, or directed in the opposite direction. An orientation is admitted only when its tail has not appeared before and adding it creates no directed cycle. This recursion is exhaustive because these are precisely the compatibility and acyclicity conditions above.

Counting all resulting faces gives the nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)=(24,240,1296,4080,7488,7424,3072).
\]
As an independent count check, the cube Laplacian has spectrum \(0,2,2,2,4,4,4,6\), so the graph gradient-field generating identity gives
\[
\det(L+tI)=t(t+2)^3(t+4)^3(t+6)
=t^8+24t^7+240t^6+1296t^5+4080t^4+7488t^3+7424t^2+3072t,
\]
whose coefficients reproduce the same face counts.

Over \(\mathbb F_2\), the simplicial boundary of a face is the sum of all faces obtained by deleting one primitive vector-field pair. Direct exact row reduction gives augmented boundary ranks, beginning with \(C_0\to C_{-1}\),
\[
(1,23,217,1079,3001,4487,2933).
\]
Therefore
\[
\dim \widetilde H_5=7424-4487-2933=4,
\qquad
\dim \widetilde H_6=3072-2933=139,
\]
and the same rank calculation gives zero in every other degree. The reduced Euler characteristic is \(-4+139=135\), agreeing with the alternating sum of the face vector.

## Verification
The included `verify_cube_morse.py` constructs \(Q_3\) from binary XOR, enumerates the Morse-complex faces by cycle-pruned recursion, and separately checks all \(3^{12}\) edge states from scratch. It verifies every codimension-one face, checks \(\partial^2=0\) on every face, reconstructs the Laplacian polynomial, and computes each boundary rank in three ways: high-pivot column elimination, low-pivot column elimination, and elimination on the transpose. The replay ends with `VERIFY_OK` only after the face vector, boundary ranks, Betti numbers, and Euler characteristic all match the values above.

## Relationship to prior work
Donovan--Lin--Scoville compute exact Morse-complex homotopy types for several graph families, but their searchable treatment does not give the cube graph. Scoville--Zaremsky emphasize that exact Morse-complex homotopy types are known only in relatively few cases and prove general connectivity bounds. Their regular-graph example explicitly applies the bound to the hypercubes \(Q_n\); for \(Q_3\) it provides connectivity information rather than the homology ranks above. Contreras--Tawfeek identify the Laplacian characteristic polynomial as a generating function for graph gradient vector fields, which explains the independent face-count check but does not determine the simplicial boundary maps or homology.

Directed-forest terminology gives a closely related formulation. A thesis on directed forest complexes of Cayley graphs is therefore a plausible comparison source because \(Q_3\) is a Cayley graph. Its public abstract was inspectable, but its full text was unavailable during this comparison, so exact overlap with that thesis remains a bibliographic risk rather than being asserted away.

## Limitations
The claim is only about reduced homology with \(\mathbb F_2\) coefficients. It does not determine integral homology, torsion, cohomology operations, or the full homotopy type of \(\mathcal M(Q_3)\). The computation is exhaustive for this finite graph but does not assert a formula for \(Q_n\) when \(n>3\). The inaccessible full text of the directed-forest thesis is the principal unresolved coverage risk.

## References
1. C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440v1, 2019.
2. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1, 2020.
3. I. Contreras and A. R. Tawfeek, *On discrete gradient vector fields and Laplacians of simplicial complexes*, arXiv:2105.05388v1, 2021.
4. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, 2022.
5. K. Courtney, *The Directed Forest Complex of Cayley Graphs*, DOI:10.18122/td/1684/boisestate, 2020.
