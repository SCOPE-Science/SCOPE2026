# Circuit-hyperplane relaxation adds a sphere bouquet to matroid basis-graph flag complexes

## Finding
Let \(M\) be a rank-\(r\) matroid with ground set \(E\) of cardinality \(n\), and let \(H\) be a circuit-hyperplane. Let \(B(M)\) denote the *basis-exchange graph*: its vertices are bases and its edges join bases that differ in exactly one element. Define \(K(M)=\operatorname{Cl}(B(M))\), the clique (flag) complex of this graph. Let \(M^H\) be the matroid obtained by relaxing \(H\), so that its bases consist of all bases of \(M\) together with \(H\).

**Relaxation theorem.** Suppose \(r\ge2\), \(n-r\ge2\), and \(K(M)\) is simply connected. Then
\[
K(M^H)\simeq K(M)\vee\bigvee^{(r-1)(n-r-1)}S^2.
\]

For the rank-three binary Fano matroid \(F_7\) and its non-Fano relaxation \(F_7^-\), the exact integral homotopy types are
\[
K(F_7)\simeq\bigvee^{13}S^2,\qquad K(F_7^-)\simeq\bigvee^{19}S^2.
\]

## Assumptions and scope
Every graph is finite and simple. A matroid circuit-hyperplane is simultaneously a circuit and a hyperplane, hence has exactly \(r\) elements; its complement has \(s=n-r\) elements. A clique complex includes all nonempty cliques and their faces. The theorem requires *simple connectivity of the old flag complex*; no such hypothesis is claimed to hold for arbitrary matroids. The values \(13\) and \(19\) are homotopy ranks, not just rational Betti numbers.

For the finite example, label the Fano ground set by \(1,\dots,7\) and declare precisely the seven triples \(\{a,b,a\mathbin{\mathrm{xor}}b\}\), with distinct nonzero three-bit vectors \(a,b\in\{1,\dots,7\}\), to be the nonbases. Explicitly, these triples are \((123),(145),(167),(246),(257),(347),(356)\). All other triples are bases. Relax the line \(H=\{1,2,3\}\) to obtain the non-Fano matroid.

## Proof
**Step 1: Identify the attaching link.** The newly added vertex \(H\) of \(B(M^H)\) is adjacent precisely to old bases \(B_{h,e}=(H\setminus\{h\})\cup\{e\}\), indexed by \(h\in H\) and \(e\in E\setminus H\). Such sets are indeed bases of \(M\): the circuit-hyperplane \(H\) has rank \(r-1\), and any element outside its closure raises the rank to \(r\). Distinct neighbors \(B_{h,e}\) and \(B_{h',e'}\) exchange one element exactly when \(h=h'\) or \(e=e'\). Consequently the graph induced on the \(rs\) neighbors is the \(r\)-by-\(s\) rook graph, equivalently the line graph of the complete bipartite graph \(K_{r,s}\). Therefore the simplicial link \(L=\operatorname{Lk}_{K(M^H)}(H)\) is precisely the clique complex of that rook graph.

**Step 2: Compute the link's homotopy type.** For \(r,s\ge2\), the maximal cliques of the rook graph are its \(r\) entire rows and its \(s\) entire columns. In the clique complex these are simplices; each row simplex intersects each column simplex in one vertex, distinct row simplices are disjoint, and distinct column simplices are disjoint. This is a good cover by contractible subcomplexes with nerve the ordinary bipartite graph \(K_{r,s}\). The simplicial nerve lemma gives
\[
L\simeq K_{r,s}\simeq\bigvee^{rs-r-s+1}S^1
=\bigvee^{(r-1)(s-1)}S^1.
\]

**Step 3: Attach the new star.** No simplex of \(K(M)\) changes when \(H\) is added as a new graph vertex. The enlarged flag complex is precisely \(K(M^H)=K(M)\cup_L (H*L)\), where \(H*L\) is the cone on \(L\). Since \(L\) is homotopy equivalent to a bouquet of circles and \(K(M)\) is simply connected, the attaching map \(L\hookrightarrow K(M)\) is null-homotopic. Its mapping cone thus splits as \(K(M)\vee\Sigma L\), proving the relaxation theorem and the displayed number of two-spheres. No assertion of a preferred simplicial collapse is needed for this general splitting.

**Step 4: Explicit integral Fano witness.** The companion executable `verify.py` constructs all \(28\) Fano bases, forms the clique complex, enumerates every nonempty simplex, and constructs a Forman acyclic face matching with exactly one critical zero-simplex and \(13\) critical two-simplices. This matching is rigorously checked by orienting all Hasse incidences downward except matched incidences, which are oriented upward; a topological sort visits every face and verifies no directed cycle exists. Forman's discrete-Morse theorem then gives a CW complex with one vertex and \(13\) two-cells and no cells in other positive dimensions. Each two-cell necessarily has a constant attaching map to the point, giving \(K(F_7)\simeq\bigvee^{13}S^2\). In particular \(K(F_7)\) is simply connected and Step 3 applies with \(r=3\), \(s=4\), giving exactly six additional two-spheres. An independently enumerated perfect acyclic matching of \(K(F_7^-)\) leaves one zero-cell and \(19\) two-cells, directly verifying the second homotopy classification.

## Verification
Running `python3 verify.py` with Python's standard library prints one JSON object ending in `"verification":"VERIFY_OK"`. The saved `verification_output.json` records the exact output. The Fano flag complex has face vector \((28,126,140,28)\): \(322\) nonempty faces, \(784\) codimension-one incidences, and \(154\) matched pairs, leaving a single vertex and \(13\) triangles. The relaxed complex has face vector \((29,138,170,44,3)\): \(384\) faces, \(977\) incidences, and \(182\) matched pairs, leaving one vertex and \(19\) triangles. All incidences and all matched pairs are exhaustively checked. The complete acyclicity check establishes the infinite-homotopy claims through the finite discrete-Morse theorem; mere simplex enumeration is not used in place of proof.

The same verifier checks the entire induced neighbor graph at the relaxed basis and confirms that it is the \(3\)-by-\(4\) rook graph, with \(12\) vertices and nerve \(K_{3,4}\) of cycle rank \(6\). It does not claim a computational classification of all matroids or a theorem about all basis-exchange graphs without the simple-connectivity hypothesis.

## Relationship to prior work
The basis graph and circuit-hyperplane relaxation are classical matroid constructions. Chalopin, Chepoi and Osajda's paper *On two conjectures of Maurer concerning basis graphs of matroids* treats the triangle-square \(2\)-complex of a basis graph, which fills both triangles and graph squares. That complex is **not** the clique/flag complex studied here; filling every square can alter homotopy. Ferroni's discussion of circuit-hyperplane relaxation and its rook-graph neighborhood explains the local combinatorics used in Step 1, but does not determine the present homotopy-cofiber splitting or these Fano and non-Fano homotopy types. Standard matroid independence or external-activity complexes are likewise different simplicial constructions.

## Limitations
The relaxation theorem applies only when the pre-relaxation exchange-flag complex is simply connected. The Fano computations are exact for the specified seven-element matroids, and no conjectural extension to other matroids is asserted. The equivalence is nonequivariant. The two finite certificates provide self-contained reproducibility but are not independent peer review. Although comparison with accessible primary text and indexed results found no implication covering the claim, uncatalogued equivalent computations remain possible; historical original basis-graph articles were not fully available for text inspection.

## References
- J. Chalopin, V. Chepoi and D. Osajda, *On two conjectures of Maurer concerning basis graphs of matroids*, arXiv:1212.6879, original public version dated 2012-12-31. In particular, distinguish its triangle-square complex from a flag complex.
- L. Ferroni, *On the Ehrhart Polynomial of Minimal Matroids*, *Discrete & Computational Geometry*, 2021; section on circuit-hyperplane relaxation and the rook-graph induced neighborhood.
- S. B. Maurer, *Matroid Basis Graphs. I*, *Journal of Combinatorial Theory, Series B*, 1973, foundational graph context (historical paper not inspected in full).
- R. Forman, *Morse Theory for Cell Complexes*, *Advances in Mathematics* 134 (1998), 90–145 (discrete Morse theorem).
