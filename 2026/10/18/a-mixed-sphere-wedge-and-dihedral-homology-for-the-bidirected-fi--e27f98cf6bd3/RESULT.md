# A mixed sphere wedge and dihedral homology for the bidirected five-vertex wheel

## Finding

Let \(W\) be the five-vertex wheel \(K_1*C_4\), and let \(\overleftrightarrow W\) be obtained by replacing each undirected edge by both directed arcs. Let \(X=X(\overleftrightarrow W)\) be the multipath complex (equivalently, directed-linear-forest complex) whose simplices are directed arc sets forming disjoint unions of directed paths, with isolated vertices allowed and directed cycles forbidden. There is an integral homotopy equivalence
\[
X\simeq\bigvee^{19}S^2\vee\bigvee^{8}S^3.
\]
In particular, the only nonzero reduced integral homology groups are \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z^{19}\) and \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{8}\).

The graph automorphism group is \(D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), acting on the rim by a one-step rotation \(r\) and a reflection \(s\), and fixing the hub. The complete rational characters on reduced homology, indexed by \((1,r,r^2,r^3;s,sr,sr^2,sr^3)\), are
\[
\chi_{\widetilde H_2}=(19,-1,3,-1;1,1,1,1),\qquad
\chi_{\widetilde H_3}=(8,0,0,0;0,0,0,0).
\]
If \(\chi_{\epsilon,\delta}\) denotes the one-dimensional rational character with \(r\mapsto\epsilon\) and \(s\mapsto\delta\), and \(E\) is the rational two-dimensional geometric representation, then
\[
\widetilde H_2(X;\mathbb Q)\cong
3\chi_{+,+}\oplus2\chi_{+,-}\oplus3\chi_{-,+}\oplus3\chi_{-,-}\oplus4E,
\]
\[
\widetilde H_3(X;\mathbb Q)\cong\mathbb Q[D_4].
\]
The full-group invariant dimensions in degrees two and three are therefore three and one.

## Assumptions and scope

Fix graph vertices \(V=\{0,1,2,3,4\}\), with hub \(0\), spokes \(\{0,i\}\) for \(i=1,2,3,4\), and rim edges \(\{1,2\},\{2,3\},\{3,4\},\{4,1\}\). Each edge supplies two ordered arcs. A face is a subset of these sixteen arcs with at most one outgoing and at most one incoming arc at each graph vertex and no directed cycle. These conditions are necessary and sufficient for a directed linear forest. Arc coordinates are ordered lexicographically, and a face is encoded by the sum of the corresponding distinct powers of two; this convention fixes all signed simplicial orientations.

The statement concerns this exact five-vertex wheel. It does not assert any uniform classification for wheels with other rim lengths, any homotopy-equivariant splitting, or a decomposition of the integral automorphism lattice.

## Proof

**Finite complex and acyclic matching.** Exhaustively testing the \(2^{16}\) arc subsets with the preceding incidence and cycle conditions produces 261 faces including the empty face, with simplex counts \((f_0,f_1,f_2,f_3)=(16,76,120,48)\). The code in `verify_morse.py` enumerates them without relying on an externally supplied face table.

Keep the singleton simplex corresponding to arc index five as the sole designated critical vertex. Exclude the empty face from matching. At each subsequent stage choose the lexicographically earliest arc maximizing the number of currently available pairs \((\sigma,\sigma\cup\{e\})\), match every such pair, and delete those faces from the active set. The successive arc indices and pair counts are
\[
(5,49),\ (8,37),\ (12,13),\ (15,10),\ (0,2),\ (2,2),\ (1,1),\ (3,1).
\]
There are 115 disjoint pairs, leaving precisely one critical \(0\)-simplex, one critical \(1\)-simplex, twenty critical \(2\)-simplices and eight critical \(3\)-simplices. Orient each unmatched face-poset covering relation downward and each matched relation upward. On all 260 nonempty faces, the directed Hasse graph has 704 covering relations and admits a complete 260-vertex topological sort. Thus the matching is acyclic, and Forman's discrete Morse theory supplies a CW model with exactly these critical cells.

**Integral boundary.** Write \(\partial\) for the standard signed simplicial boundary in the fixed lexicographic arc order. For each matched lower face \(\sigma\), with matched upper face \(\tau\), recursively replace \(\sigma\) by minus the other terms of \(\partial\tau\), divided by its incidence coefficient \([\sigma](\partial\tau)=\pm1\). Project matched upper faces to zero and critical faces to themselves. Acyclicity guarantees termination and yields the integral Morse differential. The self-contained `verify_morse.py` checks every recursion and every coefficient. In the resulting critical-cell bases,
\[
C_3\cong\mathbb Z^8\xrightarrow{\,\partial^M_3=0\,}
C_2\cong\mathbb Z^{20}\xrightarrow{\,\partial^M_2\,}
C_1\cong\mathbb Z\xrightarrow{\,\partial^M_1=0\,}
C_0\cong\mathbb Z.
\]
The unique row of \(\partial^M_2\) has exactly three entries \(+1\), three entries \(-1\), and fourteen zeros. In particular, its image is primitive and surjects onto \(C_1\); the integral Morse differential from degree three is identically zero.

**Upgrade from homology to homotopy.** The Morse CW model has a unique vertex and one oriented \(1\)-cell. One \(2\)-cell has attaching degree \(+1\) or \(-1\), so the \(1\)-cell and that \(2\)-cell cancel up to CW homotopy. Its remaining \(19\) two-cells then form a wedge of \(19\) two-spheres. Each of the eight three-cell attaching maps represents an element of \(\pi_2(\bigvee^{19}S^2)\), which agrees with degree-two homology by Hurewicz. Since the Morse third differential vanishes integrally, all eight attaching maps have zero Hurewicz class and hence are nullhomotopic. This proves the displayed sphere wedge. All integral homology is therefore free as stated.

**Dihedral representation.** The action of \(D_4\) on each signed simplicial chain is obtained by permuting directed arcs and applying the orientation sign. The independent `verify_character.py` constructs the complete degree-three integral boundary matrix with 48 columns and 120 rows. It has rank 40 modulo 101 and modulo two; the already proved Morse model bounds its rational rank by 40, so the rational top kernel has dimension eight. A normalized nullspace basis over \(\mathbb F_{101}\) gives degree-three traces \((8,0,0,0;0,0,0,0)\). Every integral trace on this rank-eight group lies in \([-8,8]\), so these residues determine their unique integer values (the characteristic 101 exceeds twice this bound). With no higher chain group, the top homology is exactly this kernel. The signed reduced Lefschetz traces from all faces give \((11,-1,3,-1;1,1,1,1)\); adding the degree-three traces recovers the stated degree-two character. Inner products with the five irreducible rational \(D_4\)-characters give the two decompositions above. The full-group invariant dimensions are the trivial-character multiplicities.

## Verification

Run `python3 verify_morse.py` and `python3 verify_character.py` with a standard Python 3 interpreter; no third-party modules are required. Their recorded exact outputs are `morse_output.txt` and `character_output.txt`. The first program performs the complete face enumeration, acyclic matching, 704-covering-relation sort and integer gradient-path differential. The second uses a separately written face enumerator, exact finite-field boundary reduction, signed dihedral chain action and rational-character reconstruction. In particular the independent mod-two boundary ranks are \(15,61,40\), yielding reduced Betti numbers \((0,0,19,8)\), in agreement with the integral Morse proof. Both programs use integer arithmetic only; no numerical approximations or sampled subsets enter the proof.

## Relationship to prior work

Caputi, Collari and Smith (arXiv:2601.05670v1, public January 9, 2026) analyze the multipath complexes of bidirected paths and polygons, including their homology and connectivity. The wheel has an additional universal hub, and its multipath complex is not a bidirected path or polygon. Its mixed two- and three-sphere homotopy type, and the full dihedral characters above, do not follow from the cited path/polygon formulas.

Caputi, Collari, Di Trani and Smith (arXiv:2208.04656v1) treat the general multipath construction and compute families such as oriented paths, polygons, grids and tournaments. Their dynamical-region decomposition does not calculate this connected bidirected wheel. Deshpande and Sawant (arXiv:2602.14936v1, public February 16, 2026) call the same object a directed-linear-forest complex and study conflict graphs, shellability and classes including forests and cycles; their cited classifications do not include the wheel calculation or its dihedral homology representation. The whole-graph, cycle-free chessboard complex of a complete digraph is likewise a different object; the wheel is only an arc-restricted subcomplex, to which whole-graph homology does not automatically descend.

## Limitations

This finite classification does not establish a general formula for bidirected wheels. The symmetry identification is rational, not an asserted canonical integral-module decomposition or equivariant homotopy equivalence. The proof depends on a complete, reproducible finite enumeration and discrete-Morse computation with explicit definitions; it does not imply that small-case evidence proves larger cases. Bibliographic searches cannot exclude unindexed or unpublished equivalent results. Independent external validation has not been performed.

## References

1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (2026-01-09), https://arxiv.org/abs/2601.05670 .
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (2022-08-09), https://arxiv.org/abs/2208.04656 .
3. P. Deshpande, R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936v1 (2026-02-16), https://arxiv.org/abs/2602.14936 .
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete-Morse theorem).
