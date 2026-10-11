# The Paley-\(29\) independence complex is \(\bigvee^{28}S^2\vee M(\mathbb Z/2,2)\)
## Finding
Let \(P_{29}\) be the Paley graph with vertex set \(\mathbb Z/29\), where distinct vertices \(a,b\) are adjacent exactly when \(a-b\) is a nonzero quadratic residue modulo \(29\). Then
\[
\operatorname{Ind}(P_{29})\simeq \bigvee^{28}S^2\vee M(\mathbb Z/2,2),
\]
where \(M(\mathbb Z/2,2)=S^2\cup_2 e^3\) is the Moore space obtained by attaching a 3-cell to \(S^2\) by a degree-2 map.

## Assumptions and scope
The claim concerns the ordinary independence complex of the finite simple graph \(P_{29}\) only. The nonzero quadratic residues modulo \(29\) are
\[
\{1,4,5,6,7,9,13,16,20,22,23,24,25,28\}.
\]
All finite enumeration and discrete-Morse data are regenerated directly from this definition. No assertion is made for other Paley graphs or for asymptotic Paley-complex families.

## Proof
Exhaustive enumeration gives no independent set of size five and gives the face vector
\[
(f_0,f_1,f_2,f_3)=(29,203,406,203).
\]
Apply staged vertex toggling in the order \(0,1,\ldots,28\): at each stage, among currently unmatched nonempty faces, pair a face \(\sigma\) not containing the stage vertex with \(\sigma\cup\{v\}\) whenever both are still unmatched. This produces 397 matched Hasse pairs. Directly orienting all 2436 Hasse covers downward except for the matched covers, which are reversed, yields an acyclic directed graph. The unmatched faces are exactly one vertex, 37 triangles, and 9 tetrahedra. Forman's discrete Morse theorem therefore gives a CW complex with one 0-cell, no 1-cells, 37 2-cells, and 9 3-cells.

Using signed simplicial incidences and algebraic cancellation along the same matched pairs gives a Morse boundary
\[
B:\mathbb Z^9\longrightarrow\mathbb Z^{37}.
\]
In the critical-cell order recorded in `MORSE_CERTIFICATE.json`, an \(8\times8\) minor has determinant \(-1\), a \(9\times9\) minor has determinant \(-2\), and \(B\) has rank 8 modulo 2. The unit 8-minor forces the first eight determinantal divisors to be 1. Mod-2 rank 8 makes every full-rank minor even, while the displayed determinant-2 minor forces the ninth determinantal divisor to be 2. Hence the Smith invariant factors of \(B\) are
\[
1,1,1,1,1,1,1,1,2.
\]
Consequently
\[
H_2\bigl(\operatorname{Ind}(P_{29});\mathbb Z\bigr)\cong \mathbb Z^{28}\oplus\mathbb Z/2,
\qquad
H_3\bigl(\operatorname{Ind}(P_{29});\mathbb Z\bigr)=0.
\]
Because there are no 1-cells, the 2-skeleton of the Morse CW complex is \(\bigvee^{37}S^2\), and the nine 3-cell attaching maps are classified by their degree vectors in \(\pi_2(\bigvee^{37}S^2)\cong H_2(\bigvee^{37}S^2;\mathbb Z)\cong\mathbb Z^{37}\). Integral basis changes in the 2-cell and 3-cell groups are realized by homotopy equivalences and cell slides. Reducing \(B\) to Smith form cancels eight degree-1 sphere/3-cell pairs; the remaining degree-2 attachment is \(M(\mathbb Z/2,2)\), while 28 2-spheres remain unattached. This proves the stated homotopy equivalence.

## Verification
`verify_paley29.py` rebuilds the graph and all independent faces, verifies the entire staged matching and all 2436 Morse-oriented Hasse covers, reconstructs the signed Morse boundary, checks the two determinant witnesses and mod-2 rank, and independently computes the original simplicial mod-2 boundary ranks as
\[
(28,175,202).
\]
Thus the original complex has reduced mod-2 Betti ranks 29 in degree 2 and 1 in degree 3, exactly as required by the Moore summand. The verifier uses only the Python standard library and terminates with `VERIFY_OK`.

## Relationship to prior work
Matsushita and Wakatsuki study exact homotopy types of independence complexes for square-grid graphs and list primary MSC 55P10; their graph family does not contain \(P_{29}\). Rinaldo and Romeo identify \(P_{17}\) as a vertex-decomposable example in their study of 2-dimensional independence complexes of circulant graphs. Their scope is independence dimension 2, whereas \(\operatorname{Ind}(P_{29})\) has dimension 3, so that result does not imply the present claim. The House of Graphs entry 51215 records the same graph under the circulant alias \(C_{29}(1,4,5,6,7,9,13)\) and gives the strongly regular parameters, but it does not provide the independence-complex homotopy type. Since Paley graphs are self-complementary, the equivalent clique-complex formulation was also included in the literature searches.

## Limitations
The proof is an exact finite calculation for \(P_{29}\), not a theorem for a Paley family. The finite certificate verifies the combinatorics and boundary algebra, while the final passage from Smith form to the wedge-plus-Moore decomposition uses standard discrete Morse theory, the Hurewicz identification \(\pi_2(\bigvee S^2)\cong H_2(\bigvee S^2;\mathbb Z)\), and standard CW cell-slide/cancellation facts. An equivalent computation may exist under an unindexed historical alias; this remains the principal originality risk.

## References
1. T. Matsushita and S. Wakatsuki, *Independence complexes of (n x 6)-grid graphs*, arXiv:2207.10363v1, first posted 2022-07-21.
2. G. Rinaldo and F. Romeo, *2-dimensional vertex decomposable circulant graphs*, arXiv:1807.05755v1, first posted 2018-07-16.
3. House of Graphs, graph 51215, Paley graph of order 29 / \(C_{29}(1,4,5,6,7,9,13)\).
