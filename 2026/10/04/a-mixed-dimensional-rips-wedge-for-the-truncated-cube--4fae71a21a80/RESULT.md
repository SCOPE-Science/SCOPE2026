# A mixed-dimensional Rips wedge for the truncated cube
## Finding
Let \(T\) be the truncated cubical graph, with vertex set
\[
V(T)=\{(x,i):x\in\mathbb F_2^3,\ i\in\{0,1,2\}\},
\]
where the three vertices \((x,0),(x,1),(x,2)\) form a triangle for each \(x\), and \((x,i)\) is adjacent to \((x+e_i,i)\). Give \(V(T)\) the shortest-path metric in \(T\), and use the inclusive Vietoris--Rips convention. Then
\[
\operatorname{VR}_{\le 3}(T)\simeq S^2\vee\bigvee^{6}S^3.
\]
Thus a natural Archimedean-solid graph already exhibits a single Rips scale whose homotopy type has sphere summands in two positive dimensions.

## Assumptions and scope
The graph above is the ordinary 1-skeleton of the truncated cube: truncating each cube vertex produces the triangle on \((x,0),(x,1),(x,2)\), while every original cube edge leaves one connecting edge of the form \((x,i)(x+e_i,i)\). The statement concerns only the graph shortest-path metric and the inclusive scale \(3\). It does not assert the complete Rips filtration of the truncated cube and does not concern the Euclidean distances of a geometric realization.

## Proof
Write \(K=\operatorname{VR}_{\le 3}(T)\). Equivalently, \(K\) is the clique complex of the third distance power \(T^3\). Label \((x,i)\) by \(3x+i\), with \(x\in\{0,\ldots,7\}\). Exact clique enumeration gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(24,156,376,372,144,20).
\]

Consider the following deterministic sequential matching on the face poset of \(K\). Process the vertices in the order
\[
0,1,23,15,11,17,19,8,9,5,6,2,3,21,4,22,10,12,7,16,20,14,13,18.
\]
At the stage for a vertex \(v\), pair every still-unmatched simplex \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever the latter is a simplex and is still unmatched. The accompanying verifier constructs the entire directed Hasse diagram, directs matched edges upward and all other codimension-one edges downward, and checks by exact topological sorting that this matching is acyclic.

Exactly eight simplices are critical:
\[
\{0\},\qquad \{2,8,19\},
\]
and the six tetrahedra
\[
\begin{aligned}
&\{2,12,14,15\},\quad \{3,7,10,11\},\quad \{5,10,17,22\},\\
&\{7,14,19,20\},\quad \{8,9,20,21\},\quad \{12,13,16,18\}.
\end{aligned}
\]
Therefore discrete Morse theory gives a CW complex homotopy equivalent to \(K\) with one \(0\)-cell, one \(2\)-cell, six \(3\)-cells, and no other cells.

It remains to determine the attaching degrees of the six \(3\)-cells. Let \(c=\{2,8,19\}\) denote the critical \(2\)-simplex. For a matched \(2\)-simplex \(\sigma\nearrow\tau\), write \([\tau:\sigma]\in\{\pm1\}\) for the standard oriented simplicial incidence number and recursively reduce \(\sigma\) to the critical \(2\)-generator by
\[
R(\sigma)=-[\tau:\sigma]^{-1}\sum_{\substack{\sigma'\prec\tau\\ \sigma'\ne\sigma}}[\tau:\sigma']R(\sigma').
\]
Set \(R(c)=1\), while a \(2\)-simplex matched downward to a \(1\)-simplex contributes \(0\). Acyclicity makes the recurrence finite. For every critical tetrahedron \(\beta\), its Morse boundary coefficient is
\[
\sum_{\sigma\prec\beta}[\beta:\sigma]R(\sigma).
\]
The exact integer replay gives coefficient \(0\) for all six critical tetrahedra. Hence the Morse differential \(C_3\to C_2\) is the zero map.

The Morse CW complex consequently has a single \(2\)-cell attached to the basepoint, so its \(2\)-skeleton is \(S^2\). Each of the six \(3\)-cell attaching maps \(S^2\to S^2\) has degree \(0\), and therefore is null-homotopic. It follows that the CW complex, and hence \(K\), is homotopy equivalent to
\[
S^2\vee\bigvee^{6}S^3.
\]

## Verification
The standalone script `verify_truncated_cube_rips3.py` reconstructs the truncated cubical graph from the cube-truncation definition, checks \(24\) vertices, \(36\) edges, cubic degree sequence, and diameter \(6\), forms the third distance power, and enumerates every clique. It reproduces the face vector above, reconstructs the sequential Morse matching from `morse_certificate.json`, checks all \(542\) matched pairs, verifies acyclicity of the full \(1092\)-simplex Hasse orientation, and performs the signed gradient reduction of the six critical \(3\)-cells to the unique critical \(2\)-cell. Every coefficient is exactly zero. The terminal line is `VERIFY_OK`.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine the Rips homotopy types of the five Platonic solids and explicitly name Archimedean solids as a conceivable generalization. Their article also uses combinatorial Morse theory as the main tool in the nontrivial dodecahedral case. The truncated cube is Archimedean rather than Platonic, so their classification does not include the complex considered here.

Adamaszek's general study of clique complexes of graph powers identifies \(\operatorname{Cl}(G^r)\) with the Rips complex of the graph metric and proves general collapse and universality results, but it does not compute the third power of the truncated cubical graph. Targeted searches for the truncated cube together with Vietoris--Rips, clique-complex, graph-power, and equivalent shortest-path formulations did not locate a statement implying the displayed wedge decomposition. This negative search is evidence for the originality check, not a proof of absolute novelty.

## Limitations
Only the scale \(3\) graph-metric complex is classified. The result does not determine the maps from adjacent filtration scales, does not classify the other Archimedean solids, and does not apply to Euclidean or spherical metrics on a geometric truncated cube. The originality search is necessarily limited by terminology and indexing, so an unnoticed equivalent finite computation remains possible.

## References
1. Nada Saleh, Thomas Titz Mite, and Stefan Witzel, *Vietoris--Rips complexes of Platonic solids*, arXiv:2302.14388, first public version 2023-02-28; published in *Innovations in Incidence Geometry* 21 (2024), 17--34.
2. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public version 2011-04-03; *Israel Journal of Mathematics* 196 (2013), 295--319.
