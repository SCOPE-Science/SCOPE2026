# A collapse from 2-cut to 3-cut complexes in unique-common-neighbor graphs

## Finding
Let \(G\) be a finite connected simple graph on \(n\ge 5\) vertices and \(e\) edges. Assume that \(G\) is triangle-free, has no \(4\)-cycle, and has diameter at most \(2\). Then
\[
\Delta_2(G)\searrow\Delta_3(G).
\]
Consequently,
\[
\Delta_3(G)\simeq\bigvee^{e-n+1}S^{n-4},
\]
where a zero-fold wedge is interpreted as contractible. In particular, for the Petersen graph \(P\),
\[
\Delta_3(P)\simeq\bigvee^6S^6.
\]

## Assumptions and scope
For a finite simple graph \(G\) with vertex set \(V\), the ordinary \(k\)-cut complex \(\Delta_k(G)\) is the simplicial complex whose facets are the complements \(V\setminus T\) of those \(k\)-element sets \(T\subseteq V\) for which the induced graph \(G[T]\) is disconnected.

The three graph hypotheses imply a useful exact local property. If \(u\) and \(v\) are nonadjacent, diameter at most \(2\) gives a common neighbor, while the absence of a \(4\)-cycle makes that common neighbor unique. Denote it by \(w(u,v)\). Triangle-freeness then says that \(u,w(u,v),v\) induce a path of length two.

The theorem concerns ordinary cut complexes, not total cut complexes. No regularity assumption is imposed. The graph may be a tree; under the stated hypotheses the tree case is a star, and the displayed zero-fold wedge means a contractible complex.

## Proof
A facet of \(\Delta_2(G)\) has the form
\[
F_{uv}=V\setminus\{u,v\}
\]
for a nonedge \(uv\). For each nonedge \(uv\), let \(w=w(u,v)\) be its unique common neighbor and put
\[
\sigma_{uv}=V\setminus\{u,v,w\}.
\]
Because \(u-w-v\) is connected, \(\sigma_{uv}\notin\Delta_3(G)\).

The face \(\sigma_{uv}\) is a free codimension-one face of \(F_{uv}\) in \(\Delta_2(G)\). Indeed, if another facet \(F_{xy}\) contains \(\sigma_{uv}\), then the nonedge \(xy\) must be a two-element subset of \(\{u,v,w\}\). The pairs \(uw\) and \(vw\) are edges, so the only possible nonedge is \(uv\). Hence \(F_{xy}=F_{uv}\). Distinct nonedges give distinct free faces: the complement of \(\sigma_{uv}\) is the three-vertex path whose unique nonedge is \(uv\).

Therefore the pairs \((\sigma_{uv},F_{uv})\), one for every nonedge \(uv\), may be removed successively by elementary simplicial collapses. It remains to identify the resulting subcomplex.

First, \(\Delta_3(G)\subseteq\Delta_2(G)\): every disconnected three-vertex induced subgraph contains a nonedge, so the complement of that triple is contained in the corresponding facet of \(\Delta_2(G)\).

Conversely, take a face \(\tau\in\Delta_2(G)\), and choose a nonedge \(uv\subseteq V\setminus\tau\). If \(V\setminus\tau=\{u,v\}\), then \(\tau=F_{uv}\) and it is removed. If \(V\setminus\tau=\{u,v,x\}\), then either \(x=w(u,v)\), in which case \(\tau=\sigma_{uv}\) and it is removed, or \(x\ne w(u,v)\), in which case the triple \(\{u,v,x\}\) is disconnected and \(\tau\in\Delta_3(G)\). Finally, if \(|V\setminus\tau|\ge4\), choose \(x\in V\setminus(\tau\cup\{u,v,w(u,v)\})\). Since \(x\) is not the unique common neighbor of \(u,v\), the induced triple \(\{u,v,x\}\) is disconnected, so again \(\tau\in\Delta_3(G)\). Thus the remainder after the elementary collapses is exactly \(\Delta_3(G)\), proving the collapse.

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue prove that for every connected triangle-free graph on \(n\) vertices and \(e\) edges, \(\Delta_2(G)\) is contractible when \(G\) is a tree and otherwise is homotopy equivalent to a wedge of \(e-n+1\) spheres of dimension \(n-4\). The collapse transfers that homotopy type to \(\Delta_3(G)\).

## Verification
The standalone program `verify.py` reconstructs the theorem's collapse pairs directly from graph definitions. It exhausts every labeled graph on five and six vertices satisfying the three hypotheses and checks, for each one, that every proposed \(\sigma_{uv}\) has exactly one containing \(\Delta_2\)-facet and that removing all pairs leaves exactly \(\Delta_3\). There are \(17\) such labeled graphs on five vertices and \(6\) on six vertices.

For the Petersen graph, the program independently reconstructs both cut complexes. Their nonempty face vectors are
\[
(10,45,120,210,252,210,120,30)
\]
for \(\Delta_2(P)\) and
\[
(10,45,120,210,252,210,90)
\]
for \(\Delta_3(P)\). Exactly \(30\) elementary collapse pairs account for the difference. As a separate check, a deterministic discrete-Morse matching on \(\Delta_3(P)\) uses \(465\) matched Hasse pairs and leaves one critical \(0\)-cell and six critical \(6\)-cells. Orienting all \(4440\) Hasse covers and topologically sorting the directed Hasse graph verifies acyclicity, independently giving \(\Delta_3(P)\simeq\bigvee^6S^6\).

## Relationship to prior work
Bayer et al. introduced the cut-complex framework used here and prove the connected triangle-free theorem for \(\Delta_2(G)\). Their Theorem 6.4 gives
\[
\Delta_2(G)\simeq\bigvee^{e-n+1}S^{n-4}
\]
for connected triangle-free non-trees, and their Corollary 6.3 gives contractibility for trees. They also state the Petersen specialization for \(\Delta_2(P)\). The present result adds an explicit simple-homotopy bridge from \(\Delta_2\) to \(\Delta_3\) under the natural diameter-two and \(4\)-cycle-free hypotheses; that bridge is what transfers the published \(2\)-cut topology to a new \(3\)-cut family.

Chauhan, Shukla, and Vinayak study ordinary \(3\)-cut complexes of squared cycle graphs, and Chauhan and Shukla later treat powers of cycles. Those results use a different graph family and shelling mechanism; they do not imply the unique-common-neighbor collapse proved here. Database comparisons also found a Petersen *total* \(3\)-cut computation and an ordinary \(3\)-cut computation for the cube. The former is a different complex, while the cube contains \(4\)-cycles and therefore lies outside the present theorem.

## Limitations
The collapse requires all three stated hypotheses. If a nonedge has two common neighbors, the proposed codimension-one face can lie in more than one \(\Delta_2\)-facet and the free-face argument breaks. The result does not classify \(\Delta_3(G)\) outside this class and does not claim shellability. The exhaustive computation is only a finite sanity check; the all-graph statement is proved by the free-face argument above, not by enumeration. A differently phrased result outside the checked literature could remain undiscovered.

## References
1. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes of Graphs*, SIAM Journal on Discrete Mathematics 38 (2024), 1630–1675, DOI 10.1137/23M1569034; first public version arXiv:2304.13675v1, 26 April 2023.
2. Pratiksha Chauhan, Samir Shukla, and Kumar Vinayak, *Shellability of \(3\)-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979v1, 4 June 2024.
3. Pratiksha Chauhan and Samir Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1, 24 March 2026.
