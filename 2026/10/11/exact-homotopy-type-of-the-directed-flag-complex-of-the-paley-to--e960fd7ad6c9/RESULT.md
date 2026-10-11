# Exact homotopy type of the directed flag complex of the Paley tournament on \(31\) vertices
## Finding
Let \(P_{31}\) be the Paley tournament on \(\mathbb Z/31\mathbb Z\), oriented by \(i\to j\) exactly when \(j-i\) is a nonzero quadratic residue modulo \(31\). Then its directed flag complex, equivalently its acyclic complex, has exact homotopy type
\[
\operatorname{dFl}(P_{31})\simeq\bigvee^{960}S^4.
\]

## Assumptions and scope
The directed flag complex of a tournament is the ordinary simplicial complex whose faces are vertex sets inducing transitive subtournaments. For \(P_{31}\), the nonzero quadratic residues are \(\{1,2,4,5,7,8,9,10,14,16,18,19,20,25,28\}\). The verifier checks directly that every vertex has outdegree \(15\), every distinct pair has common outdegree \(7\), and the orientation is a tournament. The statement concerns this single canonical tournament and does not assert a common homotopy type for all doubly regular tournaments of order \(31\).

## Proof
A tournament on a fixed vertex set is transitive exactly when its outdegree multiset is \(\{0,1,\ldots,k-1\}\), where \(k\) is the number of vertices. Exhaustive extension with this criterion gives the face vector, by dimension,
\[
(31,465,3255,9765,10695,3255,465),
\]
so there are \(27931\) nonempty faces and \(126015\) nonempty Hasse covers.

Apply repeated vertex-toggle matching in the fixed pivot order recorded in `verify.py`. The verifier checks every Hasse cover after reversing matched covers and topologically sorts the resulting directed Hasse graph, proving that the matching is acyclic. It has \(13396\) pairs and leaves exactly one critical \(0\)-cell, \(89\) critical \(3\)-cells, and \(1049\) critical \(4\)-cells.

The signed Forman boundary from the critical \(4\)-cells to the critical \(3\)-cells is therefore an integer matrix \(D\) of size \(89\times1049\). It has \(16282\) nonzero entries, all of absolute value at most \(8\). The verifier computes rank \(89\) modulo each of \(2,3,5,7,101,601\). An explicitly selected \(89\times89\) minor has determinant \(-601\). Since rank modulo \(601\) is still \(89\), some maximal minor is not divisible by \(601\). Hence the greatest common divisor of all maximal minors divides \(601\) and is coprime to \(601\), so it equals \(1\). Thus the Smith normal form of \(D\) has \(89\) nonzero diagonal entries, all equal to \(1\), and \(960\) zero columns.

Forman theory gives a homotopy-equivalent CW complex with one \(0\)-cell, \(89\) cells in dimension \(3\), and \(1049\) cells in dimension \(4\). Its \(3\)-skeleton is \(\bigvee^{89}S^3\). Because this skeleton is \(2\)-connected, Hurewicz identifies \(\pi_3\) with \(H_3\), so the attaching maps of the \(4\)-cells are classified by the columns of \(D\). Integral row and column operations giving Smith form are realized by homotopy equivalences of the source and target wedges of \(3\)-spheres. The attaching map is therefore equivalent to \([I_{89}\;0]\), whose homotopy cofiber is \(\bigvee^{960}S^4\). This proves the claim.

## Verification
Run `python3 verify.py`. It reconstructs the tournament and all faces from the stated residue rule, verifies the doubly regular parameters, checks all Hasse covers and acyclicity of the matching, reconstructs the signed Morse boundary by gradient-path cancellation, computes ranks modulo six primes, and computes the exact determinant \(-601\) by fraction-free Bareiss elimination. The stored `verification_output.txt` is the output of that run. The Euler characteristic is independently checked as \(961\), consistent with a wedge of \(960\) even-dimensional spheres.

## Relationship to prior work
Govc defines directed flag complexes of tournaments as the complexes of transitive subtournaments and gives a complete homotopy classification for the doubly regular tournaments in the cited collection only through order \(27\). In particular, Proposition 3.4 treats orders \(3,7,11,15,19,23,27\), not \(31\). The public McKay data page likewise describes the doubly regular lists as complete through \(27\) and labels the five listed order-\(31\) examples incomplete. The earlier tournaplex paper develops the surrounding directed-flag/tournaplex framework but does not supply this order-\(31\) homotopy type. Deniz's acyclic-complex results concern restricted recursively sectionable/trisectionable tournament families and do not state this exact Paley-\(31\) computation. Searches using both “directed flag complex” and the older alias “acyclic complex”, together with Paley/quadratic-residue and doubly-regular terminology, found no statement implying the displayed wedge of \(960\) spheres.

## Limitations
This is an exact finite computation for one canonical order-\(31\) tournament. It does not classify the other order-\(31\) doubly regular tournaments, establish an all-order Paley theorem, or analyze tournaplex filtrations. Literature search cannot constitute a mathematical proof of novelty; older or differently indexed computations remain a residual bibliographic risk. The scientific result has received same-model review only; no independent audit has been performed.

## References
1. D. Govc, “Computing Homotopy Types of Directed Flag Complexes,” arXiv:2006.05333v1, 2020. Proposition 3.4 and Section 3.2.
2. D. Govc, R. Levi, J. P. Smith, “Complexes of Tournaments, Directionality Filtrations and Persistent Homology,” arXiv:2003.00324v1; J. Appl. Comput. Topol. 5 (2021), 313–337.
3. Z. Deniz, “Topology of acyclic complexes of tournaments and coloring,” Appl. Algebra Eng. Commun. Comput. 26 (2015), 213–226, DOI: 10.1007/s00200-014-0245-0.
4. B. D. McKay, “Combinatorial Data: Digraphs,” public tournament data page, https://users.cecs.anu.edu.au/~bdm/data/digraphs.html.
