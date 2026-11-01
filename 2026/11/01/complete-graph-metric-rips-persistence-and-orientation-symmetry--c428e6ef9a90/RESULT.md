# Complete graph-metric Rips persistence and orientation symmetry of the McGee cage

## Finding
Let \(G\) be the McGee graph (the unique cubic \((3,7)\)-cage), with its shortest-path distance \(d_G\). For \(r\geq 0\), let \(K_r=\operatorname{VR}_{\leq r}(V(G),d_G)\), including a simplex exactly when every two of its vertices have distance at most \(r\). There are precisely five homotopy stages:
\[
K_r\simeq\begin{cases}
\bigvee^{23}S^0,&0\leq r<1,\\
\bigvee^{13}S^1,&1\leq r<3,\\
S^5,&3\leq r<4,\\
\ast,&r\geq4.
\end{cases}
\]
The equivalent **complete reduced integral persistence barcode** consists of \(23\) degree-zero intervals \([0,1)\), \(13\) degree-one intervals \([1,3)\), and one degree-five interval \([3,4)\). Every positive-degree group is torsion-free, and there are no other bars.

There is also a complete orientation character for the natural automorphism action at scale three. Let \(H\) be the graph of pairs at distance exactly four in \(G\). Its six connected components are four-cycles. Each has two bipartition classes; any \(g\in\operatorname{Aut}(G)\) permutes the six components by \(\pi_g\) and either preserves or exchanges their two classes. If \(\nu_g\) counts exchanged class pairs, using any fixed choice of class ordering in each component and transporting this choice to the target components, then
\[
\operatorname{tr}\bigl(g\mid\widetilde H_5(K_3;\mathbb Z)\bigr)=\operatorname{sgn}(\pi_g)(-1)^{\nu_g}.
\]
This is an integral one-dimensional representation. Of the \(32\) automorphisms, exactly \(16\) preserve and \(16\) reverse orientation. In particular the map \(i\mapsto i+3\pmod{24}\) reverses orientation, while \(i\mapsto i+12\pmod{24}\) preserves it. The finite-group rational quotient theorem therefore gives
\[
\widetilde H_*(|K_3|/\operatorname{Aut}(G);\mathbb Q)=0,
\qquad
\widetilde H_5(|K_3|/\ker\chi;\mathbb Q)\cong\mathbb Q,
\]
where \(\chi\) denotes this orientation character and all other reduced rational homology of the latter quotient vanishes. The second quotient statement is about the index-two orientation-preserving subgroup only, not arbitrary graph automorphism subgroups or integral quotient homology.

## Assumptions and scope
Use the labeled vertex set \(\{0,1,\ldots,23\}\) and the standard LCF description \([12,7,-7]^8\): add every cycle edge \(\{i,i+1\pmod{24}\}\) and all chords \(\{i,i+s_i\pmod{24}\}\), where the periodic list \(s_i\) is \((12,7,-7)\). Duplicate descriptions denote one undirected edge. This produces \(24\) vertices, \(36\) edges, girth \(7\), diameter \(4\) and full automorphism group of order \(32\). The sign \(-12\) for a chord is equivalent to \(12\) modulo \(24\).

Distances are integer-valued, so no filtration changes occur at noninteger scales. The graph-power convention is \(G^j=\{\{u,v\}:u\ne v,\ d_G(u,v)\leq j\}\). Thus \(K_j=\operatorname{Cl}(G^j)\) for each integer \(j\geq1\). Here \(\operatorname{Cl}\) is the flag (clique) complex and \(\operatorname{Ind}\) the independence complex.

## Proof
**1. Graph and early scale.** The LCF edge list is connected, cubic and has shortest cycle length seven. The finite all-pairs distance distribution, over unordered distinct pairs, is \(36,72,144,24\) at distances \(1,2,3,4\) respectively; it sums to \(276\). Hence \(K_0\) has \(24\) components, \(K_1\) is the triangle-free graph \(G\), and its cycle rank is \(36-24+1=13\). The diameter implies \(K_4\) is the full \(23\)-simplex.

**2. Integral deformation at radius two.** In \(G^2\), the maximal cliques are exactly the \(24\) closed neighborhoods \(N_G[v]\), each of size four. This follows from girth seven: every pair at distance two has a unique central neighbor and no cycle of length at most six can yield a second center or a clique joining incompatible centers. The exact face vector by dimensions zero through three is \((24,108,96,24)\). For each \(v\), first collapse the tetrahedron \(N_G[v]\) across the free triangular face \(N_G(v)\); then, for each pair \(\{a,b\}\subset N_G(v)\), collapse the triangle \(\{v,a,b\}\) across the newly free edge \(\{a,b\}\). Every indicated face is free when removed because a distance-two edge has its unique middle vertex. These are \(4\) elementary pairs per center and \(96\) pairs in total. The remaining complex is exactly the original graph \(G\). The inclusions \(K_1\hookrightarrow K_2\) are therefore integral homotopy equivalences. This is also a special instance of the previously published graph-power girth theorem, not an independently claimed new stability result.

**3. Six four-cycles at radius three.** Define \(H\) to have edge \(\{u,v\}\) exactly when \(d_G(u,v)=4\). The distance distribution shows that \(H\) has \(24\) edges, and direct inspection of the explicit LCF adjacency and shortest paths gives the following six components, with each parenthesized tuple written in cyclic order:
\[
(0,6,12,18),\ (1,5,13,17),\ (2,10,14,22),\
(3,9,15,21),\ (4,8,16,20),\ (7,11,19,23).
\]
Each component is an induced \(C_4\), and all \(24\) vertices appear exactly once. Because the diameter is four, the nonedges of \(G^3\) are exactly the edges of \(H\). Hence there is an **exact simplicial identity**
\[
K_3=\operatorname{Cl}(G^3)=\operatorname{Ind}(H)
=\operatorname{Ind}(C_4)^{*6}.
\]
The independence complex of a four-cycle is the disjoint union of two one-simplices, one on each opposite-vertex pair. It deformation-retracts to its two component barycenters, a discrete \(S^0\). The join of six such factors is the boundary of the six-dimensional cross-polytope, homeomorphic to \(S^5\). Therefore \(K_3\simeq S^5\). This is a proof by exact decomposition, not a guess from computed Betti numbers.

**4. Persistence maps.** The inclusion from scale one to scale two is the homotopy equivalence furnished by the explicit collapses. The next stage has no degree-one reduced homology and has a single new degree-five class; hence all thirteen first-homology classes die at scale three, and exactly one degree-five class is born. The full simplex at scale four kills that class. Connectivity at scale one kills the \(23\) reduced degree-zero classes. These deductions determine the full reduced integral persistence module, with no extension or torsion ambiguity.

**5. Symmetry.** Every automorphism of \(G\) preserves shortest-path distance and therefore preserves \(H\) and acts on its six four-cycles. The deformation retraction of the two disjoint one-simplices \(\operatorname{Ind}(C_4)\) to their barycenters is canonical under its full automorphism group. Taking six joins yields an equivariant retraction of \(K_3\) onto the cross-polytope boundary with two labeled antipodal points for each four-cycle. Its top orientation transforms by the determinant of a signed six-by-six permutation matrix, which is precisely \(\operatorname{sgn}(\pi_g)(-1)^{\nu_g}\). Direct exhaustive permutation checks on the 24-vertex LCF graph find 32 automorphisms and character multiplicities \(+1:16\) and \(-1:16\), including the stated rotation and half-turn. As a separate exact check, the signed Lefschetz alternating sum on all \(728\) nonempty simplices of the cross-polytope boundary agrees with the determinant formula for every automorphism. The rational homology of a quotient by a finite simplicial group is the invariant rational homology of the original complex, obtained after barycentric subdivision if necessary; the two assertions about quotients follow.

## Verification
Run `python3 verify_mcgee.py` from a directory containing this file and an installed compatible Python `networkx` package. The verifier reconstructs the labeled graph; independently recomputes all \(276\) unordered distances, girth, size and degree; enumerates all maximal radius-two cliques and validates **each** of the \(96\) elementary collapses as a free-face pair; confirms the six induced four-cycles at distance four and their \(117648\) nonempty independence-complex faces; enumerates all \(32\) graph automorphisms; and compares the orientation determinant with the independently computed signed fixed-face Lefschetz trace on the cross-polytope boundary for every automorphism. The file `verification_output.txt` is an output trace of a complete successful execution. The proof of the sphere stages and barcode uses the explicit collapses, join decomposition and standard quotient theorem, rather than merely extrapolating from these finite checks.

## Relationship to prior work
M. Adamaszek, *Clique complexes and graph powers* (first arXiv submission 2011-04-03), explicitly identifies graph-metric Rips complexes with clique complexes of distance powers and proves that sufficiently high girth forces early graph powers to collapse back to the graph (Proposition 2.2). That proposition applies here only at radius two: girth seven meets \(3(2)+1\) but not \(3(3)+1\). Thus the radius-two portion is prior-theorem coverage, while the radius-three identification of six far-distance four-cycles and the integral equivariant orientation calculation are not consequences of that girth bound.

The previously circulated calculation *The McGee graph independence complex is a five-sphere* concerns \(\operatorname{Ind}(G)\), not this radius-three complex \(\operatorname{Ind}(H)\). Although both are homotopy equivalent to a five-sphere, \(H\) is a disjoint union of six four-cycles and is not the McGee graph. Their equality of homotopy types alone does not identify the filtration or the automorphism characters. Likewise, the scale-three Rips calculation for the Tutte–Coxeter \((3,8)\)-cage concerns a different 30-vertex bipartite graph and gives a wedge of \(256\) three-spheres, not this 24-vertex cage.

The graph, its 1960 publication history, the 24-vertex LCF model, and its group of order 32 are already classical. The graph-specific result asserted here is the complete integral Rips barcode, the explicit radius-three sphere decomposition and the automorphism orientation/quotient distinction. Searches for the McGee cage, graph powers, distance-four complement, aliases and equivalent independence-complex formulations did not locate a covering result. Negative searches do not establish global publication priority.

## Limitations
The result concerns the shortest-path metric on the McGee graph, not a Euclidean drawing or other metric. It determines integral homology persistence and ordinary homotopy types of stages, but not persistent homotopy groups, integral quotient homology, the cohomology rings of quotients or a general formula for other cages. No independent mathematical audit has been performed. A 1960 publication of the graph is documented by historical sources, but its precise original calendar day has not been verified. Publication-priority uncertainty remains, especially for differently indexed computations of the distance-four graph.

## References
1. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first submitted 2011-04-03, Proposition 2.2 and Sections 1–3, 6. https://arxiv.org/abs/1104.0433 ; https://arxiv.org/pdf/1104.0433
2. W. F. McGee, *A Minimal Cubic Graph of Girth Seven*, Canadian Mathematical Bulletin 3 (1960), 149–152; historical citation from MathWorld; original publication day not verified.
3. John Baez, *McGee Graph*, American Mathematical Society Visual Insight, 2015-09-15. https://blogs.ams.org/visualinsight/2015/09/15/mcgee-graph/
4. Eric W. Weisstein, *McGee Graph*, MathWorld, https://mathworld.wolfram.com/McGeeGraph.html (reference for classical graph data and LCF notation; web article subsequently updated).
5. *The McGee graph independence complex is a five-sphere*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-mcgee-graph-independence-complex-is-a-five-sphere--5daca7995d97 (distinct complex; compare explicitly).
6. *The scale-three Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-scale-3-rips-complex-of-the-tutte-coxeter-graph-is-a-wedge-o--9454ecd0bd54 (distinct cage).
