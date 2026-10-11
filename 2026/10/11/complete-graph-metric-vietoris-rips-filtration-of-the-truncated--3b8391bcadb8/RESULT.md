# Complete graph-metric Vietoris--Rips filtration of the truncated octahedral graph
## Finding
Let \(T\) be the 24-vertex truncated-octahedral graph whose vertices are the signed coordinate permutations of \((0,1,2)\), with two vertices adjacent exactly when their squared Euclidean distance is \(2\), and give \(V(T)\) the shortest-path metric. For the inclusive Vietoris--Rips complex \(\operatorname{VR}_{\le r}(T)\), the complete homotopy filtration is \(\bigvee^{23}S^0\) for \(0\le r<1\), \(\bigvee^{13}S^1\) for \(1\le r<2\), \(\bigvee^{9}S^2\) for \(2\le r<3\), \(S^2\) for \(3\le r<4\), \(\bigvee^{5}S^4\vee\bigvee^{2}S^5\) for \(4\le r<5\), \(S^{11}\) for \(5\le r<6\), and a point for \(r\ge6\).

The scale-\(4\) stage is therefore genuinely mixed-dimensional:
\[
\operatorname{VR}_{\le 4}(T)\simeq \bigvee^{5}S^4\vee\bigvee^{2}S^5.
\]

## Assumptions and scope
The vertex set is
\[
V(T)=\{(x_1,x_2,x_3): (|x_1|,|x_2|,|x_3|)\text{ is a permutation of }(0,1,2)\}.
\]
Two vertices are joined when their squared Euclidean distance is \(2\). This gives the standard 24-vertex, 36-edge, cubic truncated-octahedral graph. Distances used in the Rips construction are graph shortest-path distances, not ambient Euclidean distances. The convention is inclusive: a finite vertex set is a simplex of \(\operatorname{VR}_{\le r}(T)\) exactly when its graph-metric diameter is at most \(r\).

## Proof
Graph distances are integral and the graph diameter is \(6\), so only the integer thresholds \(1,2,3,4,5,6\) matter.

At scale \(1\), the complex is the connected graph \(T\) itself. Its cycle rank is \(36-24+1=13\), hence it is homotopy equivalent to \(\bigvee^{13}S^1\).

At scale \(2\), exhaustive clique enumeration followed by a repeated-vertex discrete-Morse matching leaves one critical \(0\)-simplex and nine critical \(2\)-simplices, with no other critical cells. A direct acyclicity check on the entire oriented Hasse diagram verifies that this is a discrete gradient. Therefore
\[
\operatorname{VR}_{\le2}(T)\simeq\bigvee^9S^2.
\]
At scale \(3\), an independently specified repeated-vertex matching leaves one critical \(0\)-simplex and one critical \(2\)-simplex, again with the complete Hasse orientation acyclic, so
\[
\operatorname{VR}_{\le3}(T)\simeq S^2.
\]

At scale \(4\), the fourth graph power has \(228\) edges and \(218\) maximal cliques: \(52\) of size \(6\), \(24\) of size \(7\), \(30\) of size \(8\), and \(112\) of size \(9\). The Rips complex has face vector
\[
(24,228,1112,3042,4848,4592,2592,822,112),
\]
so it contains \(17372\) nonempty simplices and \(93480\) Hasse covers. The certified matching contains \(8682\) pairs and leaves exactly one critical \(0\)-cell, five critical \(4\)-cells, and two critical \(5\)-cells. The full oriented Hasse graph is acyclic. Exact signed reduction of the two critical \(5\)-cell boundaries to the five critical \(4\)-cells gives the zero \(2\times5\) Morse boundary matrix.

Thus the Morse CW model has one \(0\)-cell, five \(4\)-cells and two \(5\)-cells. Its \(4\)-skeleton is \(\bigvee^5S^4\). Because this space is \(3\)-connected, Hurewicz identifies \(\pi_4\) with \(H_4\); the zero Morse boundary says both \(5\)-cell attaching maps have zero Hurewicz class, hence are null-homotopic. This proves
\[
\operatorname{VR}_{\le4}(T)\simeq\bigvee^5S^4\vee\bigvee^2S^5.
\]

At scale \(5\), the only missing edges are the twelve antipodal pairs \(v,-v\). Therefore the clique complex is the join of twelve copies of \(S^0\), equivalently the boundary of the 12-dimensional cross-polytope, and is \(S^{11}\). At scale \(6\), every pair is adjacent and the complex is the full simplex, hence contractible. The interval statement follows because graph distances are integers.

## Verification
Run `verify.py` with a standard Python 3 interpreter. It reconstructs the coordinate graph, all graph distances, the relevant clique complexes, the three discrete-Morse matchings, and the complete Hasse orientations. For scale \(4\) it also performs the signed integral Morse reduction. It checks the face vector, all \(8682\) matched pairs, all \(93480\) Hasse covers, the critical-cell counts, the zero Morse boundary, the twelve antipodal pairs at scale \(5\), and the diameter \(6\). The bundled `verification_output.txt` ends with `VERIFY_OK`; `certificate.json` records the reconstructed finite data.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine the Vietoris--Rips homotopy types of all five Platonic solids and explicitly identify Archimedean solids as a natural direction for generalization. Their theorem does not include the truncated octahedron. Their dodecahedral calculation also illustrates that symmetry can complicate discrete-Morse arguments, motivating exact finite certificates for highly symmetric polyhedral graphs.

Adamaszek identifies graph-metric Vietoris--Rips complexes with clique complexes of graph powers and develops general results for such complexes, including a complete calculation for powers of cycles. Those general theorems do not determine the fourth power, or the full filtration, of the truncated-octahedral graph. Searches under the equivalent formulations “truncated octahedron Vietoris--Rips”, “truncated octahedral graph fourth power clique complex”, and the exact mixed wedge did not locate a prior statement implying this filtration. The closest located computations concern different solids or different metrics.

## Limitations
The theorem concerns the shortest-path metric on the one-skeleton, not the Euclidean or spherical metric on the geometric vertices. It classifies homotopy types but not the equivariant homotopy types under the full symmetry group, nor the simple-homotopy classes of the filtration maps. The originality search is necessarily limited by indexing and terminology, so a poorly indexed equivalent finite computation remains a residual risk.

## References
1. Nada Saleh, Thomas Titz Mite, and Stefan Witzel, *Vietoris--Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public version 2023-02-28; primary MSC 55N31.
2. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1, first public version 2011-04-03.
