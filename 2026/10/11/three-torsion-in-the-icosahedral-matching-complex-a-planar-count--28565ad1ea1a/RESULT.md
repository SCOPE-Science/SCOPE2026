# Three-torsion in the icosahedral matching complex: a planar counterexample

## Finding
Let \(I\) be the icosahedral graph on twelve vertices and thirty edges, and let \(\mathcal M(I)\) be its **ordinary matching complex**: its vertices are the thirty edges of \(I\), and its simplices are sets of pairwise endpoint-disjoint edges. Then
\[
\boxed{\mathcal M(I)\simeq\left(\bigvee^{64}S^3\right)\vee M(\mathbb Z/3,3),}
\]
where \(M(\mathbb Z/3,3)=S^3\cup_{\deg 3}e^4\) is the mod-three Moore space with its bottom cell in dimension three. In particular,
\[
\widetilde H_j(\mathcal M(I);\mathbb Z)=
\begin{cases}\mathbb Z^{64}\oplus\mathbb Z/3,&j=3,\\0,&j\ne3.\end{cases}
\]
The graph \(I\) is planar. Therefore its matching complex is neither contractible nor homotopy equivalent to a wedge of spheres. This disproves Conjecture 11 of Bayer, Jelić Milutinović and Vega, which asserts that the matching complex of every planar graph is contractible or a wedge of spheres.

## Assumptions and scope
There are no extra graph hypotheses. Fix vertices \(0,1,\ldots,11\), with upper cycle \(u_i=1+i\) and lower cycle \(v_i=6+i\), for \(i\in\mathbb Z/5\mathbb Z\). The thirty undirected edges, indexed by sorted endpoint pairs, are
\[
\{0u_i,11v_i,u_iu_{i+1},v_iv_{i+1},u_iv_i,u_iv_{i-1}:i\in\mathbb Z/5\mathbb Z\}.
\]
The two five-cycles are staggered, with one apex joined to each; this is the twelve-vertex icosahedral graph. Its twenty triangles form a closed triangulated sphere: every vertex has a five-cycle link, each edge lies in exactly two triangles, and the Euler characteristic is \(12-30+20=2\). Thus the graph is planar. Its thirty edges, ordered lexicographically by endpoints, are the vertices of the matching complex. A face is any subset of those edges in which no two meet. The complex is abstract, finite and unaugmented for the homotopy statement; the empty simplex is used only when constructing its face poset.

## Proof
**Finite complex and acyclic matching.** The first supplied verifier enumerates every matching of \(I\), by exhaustive edge-by-edge recursion, obtaining the exact face vector (numbers of simplices in dimensions zero through five)
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(30,315,1400,2535,1482,125).
\]
There are \(5887\) nonempty simplices and \(23130\) codimension-one nonempty face incidences. For each edge index in the ordered sequence
\[
(26,16,11,10,23,1,5,29,7,20,9,28,17,13,0,19,22,6,12,21,14,15,3,8,2,24,25,27,18,4),
\]
match every currently unpaired simplex not containing that edge to its union with the edge when the latter is also currently unpaired. This prescribes \(2866\) disjoint face–coface pairs. Orient paired incidences upward and all other incidences downward. The verifier constructs the entire directed Hasse diagram and topologically sorts all \(5887\) vertices, proving that the matching is acyclic. Exactly one critical zero-cell, \(109\) critical three-cells, and \(45\) critical four-cells remain; no others do. By discrete Morse theory, \(\mathcal M(I)\) is homotopy equivalent to a CW complex with those cells.

**Integral attaching degrees.** There is one zero-cell, no one- or two-cells, and hence the three-skeleton is \(\bigvee^{109}S^3\). For each paired lower simplex, the verifier recursively eliminates it using the signed oriented simplicial boundary of its paired upper simplex. The acyclic matching makes this finite gradient-path reduction well-founded. Applied to every critical four-cell, it produces the signed integral Morse boundary matrix \(B\) of shape \(109\times45\), which is the matrix of degrees of the four-cell attaching maps into the three-skeleton (under the Hurewicz isomorphism \(\pi_3(\bigvee^{109}S^3)\cong\mathbb Z^{109}\)).

Gaussian elimination gives \(\operatorname{rank}_{\mathbb F_3} B=44\) and \(\operatorname{rank}_{\mathbb F_2} B=45\). Moreover, the explicitly selected forty-five rows recorded in `verify_morse.py` form a square submatrix whose determinant is **exactly \(3\)** by fraction-free integer elimination. Consequently \(B\) has rational rank \(45\). Every maximal minor is divisible by three, since its reduction modulo three vanishes; the displayed minor proves their greatest common divisor is exactly three. The Smith invariant factors therefore are forty-four units and one three. In a cellular basis the boundary matrix is equivalent over the integers to
\[
\operatorname{diag}(\underbrace{1,\ldots,1}_{44},3)
\]
with sixty-four additional zero rows. These unimodular basis changes in dimensions three and four can be realized by homotopy equivalences of wedges of three-spheres (on both domain and codomain of the attaching map), since homotopy classes of maps between such wedges are determined by integer degree matrices. The resulting mapping cone splits as forty-four contractible four-cell/three-cell pairs, one Moore space \(S^3\cup_{3}e^4\), and sixty-four remaining three-spheres. This establishes the asserted *integral homotopy type*, not just the homology.

**Failure of the planar wedge assertion.** A wedge of spheres has torsion-free integral homology, and a contractible space has trivial reduced homology. The demonstrated nonzero \(\mathbb Z/3\) summand in \(\widetilde H_3\) rules out both options. Since \(I\) is planar, it contradicts the universal claim of Conjecture 11.

## Verification
The two standalone Python 3 standard-library files included here reconstruct their own inputs rather than loading precomputed logs. Run `python3 verify_morse.py` and `python3 verify_modular.py` from a directory containing the files; each terminates with `ICOSAHEDRON_MORSE_PASS` or `ICOSAHEDRON_MODULAR_PASS` on success, respectively. The first independently checks graph degree counts, the twenty triangular facets, face vector, complete acyclic matching and oriented boundary reduction, finite-field ranks and exact integer determinant certificate. The second independently writes the graph as an explicit thirty-edge list and generates all matching simplices using tuples; its simplicial boundary ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) yield reduced Betti vectors
\[
\begin{aligned}
\mathbb F_2 &: (0,0,0,64,0,0),\\
\mathbb F_3 &: (0,0,0,65,1,0),\\
\mathbb F_5 &: (0,0,0,64,0,0),
\end{aligned}
\]
indexed by dimensions zero through five. The prime-three discrepancy independently corroborates the integral three-torsion, but the integral homotopy theorem rests on the full signed Morse calculation and determinant proof.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega prove that matching complexes of **outerplanar** graphs are contractible or wedges of spheres (Theorem 2), and explicitly formulate the **planar** extension as Conjecture 11. The icosahedral graph, with thirty edges, is not outerplanar: an outerplanar simple graph on twelve vertices has at most twenty-one edges. Thus their theorem does not imply this example; its conjectured extension is false. Shareshian and Wachs establish three-torsion in matching complexes of complete graphs and chessboard complexes; those complexes are not the matching complex of the icosahedron, so their torsion results neither supply this planar example nor determine its full homotopy type. Engström's work on independence complexes of claw-free graphs supplies related topological background through the identity \(\mathcal M(G)=\operatorname{Ind}(L(G))\), but does not determine this integral graph-specific calculation.

## Limitations
The proof concerns this precisely specified twelve-vertex graph and its *ordinary* matching complex; it does not classify all planar matching complexes, their minimal torsion examples, or torsion orders generally. The numerical matrix and exact minor are reconstructed by the included finite exhaustive programs. They do not substitute for formal proof checking; mathematical validity depends on the displayed combinatorial matching and the standard signed Morse-complex theorem. An equivalent graph-specific computation might exist in unindexed literature. The stated homotopy decomposition is internal to the finite CW homotopy category; no claim of simple-homotopy uniqueness or naturality with respect to graph morphisms is made.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420 (first public 2005-12-17; MSC 57M15, 05C15), https://arxiv.org/abs/math/0512420 .
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (first public 2024-11-07; Theorem 2 and Conjecture 11), https://arxiv.org/html/2411.04601v2 .
3. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first public 2004-09-03), https://arxiv.org/abs/math/0409054 .
4. *Icosahedral Graph*, MathWorld, https://mathworld.wolfram.com/IcosahedralGraph.html .
