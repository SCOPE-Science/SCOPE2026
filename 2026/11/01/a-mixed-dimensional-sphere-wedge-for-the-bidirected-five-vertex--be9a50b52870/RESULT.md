# A mixed-dimensional sphere wedge for the bidirected five-vertex wheel multipath complex

## Finding
Let \(W_5=C_4*K_1\) be the graph on vertices \(\{0,1,2,3,4\}\) with rim edges \(\{i,i+1\}\) (indices modulo four), four spokes \(\{i,4\}\), and hub vertex \(4\). Let \(D=\overleftrightarrow{W_5}\) be the directed graph obtained by replacing every undirected edge by both opposite arcs. Write \(X(D)\) for the simplicial multipath complex of all arc sets that are vertex-disjoint unions of directed simple paths (the directed-linear-forest complex \(\mathrm{Dlf}(D)\)). Then the **integral homotopy type** is
\[
\boxed{|X(D)|\simeq\bigvee^{19}S^2\vee\bigvee^{8}S^3.}
\]
In particular \(X(D)\) is connected and simply connected; its reduced integral homology is \(\mathbb Z^{19}\) in degree two and \(\mathbb Z^8\) in degree three, and is zero in every other degree. This is the complete homotopy classification of this specified five-vertex graph, not an assertion about wheels of arbitrary size.

## Assumptions and scope
All graphs are finite and loopless. The four rim indices use arithmetic modulo four; there are no parallel directed arcs. A subset of the 16 arcs is a face precisely if each vertex has at most one chosen incoming and one chosen outgoing arc, and the chosen arcs contain no directed cycle. Isolated vertices are allowed. The empty face is present as usual. The simplicial-complex vertex order is the following lexicographically declared list generated for \(i=0,1,2,3\), and for each \(j\) in the ordered pair \((i+1\pmod{4},4)\): append \((i,j)\) then \((j,i)\). This indexing uniquely determines all oriented simplicial boundaries used below.

## Proof
**1. Exhaustive face model.** The standalone program `verify.py` checks all \(2^{16}=65,536\) arc masks against the incoming-degree, outgoing-degree, and directed-cycle conditions above. Its face census, including the empty face, is
\[
(f_{-1},f_0,f_1,f_2,f_3)=(1,16,76,120,48).
\]
All possible faces are included: the deterministic algorithm iterates the complete 16-bit Boolean cube. No face can contain more than four arcs, since a directed linear forest on five vertices has at most four edges.

**2. Complete explicit acyclic matching.** Label each directed arc by its zero-based index in the declared arc ordering. Visit the labels in the fixed order
```
[1,7,14,11,12,3,9,0,6,2,5,13,8,10,4,15]
```
At each step, among the presently unmatched faces in increasing mask order, pair each face not containing the visited arc with the face obtained by adding that arc, provided both faces are still unmatched and are faces of the complex. This produces 117 pairs and 27 unmatched nonempty faces. The pair involving the empty face is then released, making its singleton a critical zero-cell; the empty simplex is excluded from the ordinary CW matching. Hence the ordinary matching has 116 pairs and its 28 critical cells consist of **one vertex, 19 triangles, and eight tetrahedra**.

To check acyclicity, for *every* codimension-one incidence of the 260 nonempty faces, orient the incidence from upper to lower except for matched incidences, which are reversed. The checker explicitly constructs all these oriented incidences and verifies that a topological sort visits every face. Thus the entire matching is acyclic, not merely a set of valid pairs. By the discrete-Morse matching theorem, \(X(D)\) is homotopy equivalent to a finite CW complex with precisely those critical cells.

**3. Signed integral attaching calculation.** Orient each simplex by increasing arc index. For any matched pair \((\ell,u)\), the coefficient \(\varepsilon\) of \(\ell\) in \(\partial u\) is \(\pm1\). Perform the exact, integer elementary cancellation
\[
\ell=-\varepsilon^{-1}\sum_{t\ne\ell}[t](\partial u)\,t
\]
recursively through the matching, where \([t](\partial u)\) denotes the signed incidence coefficient. The acyclic Hasse orientation makes this finite recursion well-founded. In each degree, matched upper cells project to zero and surviving critical cells project to themselves. For each of the eight critical three-cells, applying this projection to its oriented simplicial boundary yields the **zero integral column** in the free abelian group on the 19 critical two-cells. This is verified exhaustively, term by term, by `verify.py`; it is the signed algebraic Morse differential, rather than a mod-two approximation. No lower-dimensional Morse differentials can occur because there are no critical one-cells.

**4. Homotopy type, not just homology.** The Morse CW complex has a single zero-cell, no one-cells, and 19 two-cells, so its two-skeleton is canonically a wedge of 19 two-spheres. For this simply connected two-skeleton the Hurewicz map \(\pi_2\to H_2(-;\mathbb Z)\) is an isomorphism. The cellular boundary of every attached three-cell is precisely the integer Hurewicz image of its attaching map. All eight boundary columns vanish by Step 3; consequently every attaching map is nullhomotopic. Attaching those eight three-cells therefore adds eight wedge summands \(S^3\), proving the stated homotopy equivalence.

## Verification
Run `python verify.py` with Python 3. No nonstandard packages or external data are required. The program rebuilds the 16 arcs and all 65,536 masks, checks the exact face census, constructs the 116-pair matching, proves that all 260 nonempty faces form an acyclic reversed Hasse orientation, and computes each of the eight integral Morse-boundary columns using signed incidences and unit coefficients. Separately it checks the full simplicial boundary ranks over \(\mathbb F_2\), obtaining \((15,61,40)\) in degrees one, two, three. The direct ranks independently agree with \(\beta_2=19\) and \(\beta_3=8\). The f-vector gives reduced Euler characteristic \(19-8=11\), another check. The script must print `VERIFY_OK`; all assertions must complete.

The computer-assisted component is a **complete finite certificate** for this exact 16-arc complex, while the passage from the certificate to integral homotopy type uses discrete Morse theory and Hurewicz as explained above. Finite tests of any larger wheels are neither used nor claimed.

## Relationship to prior work
Deshpande and Sawant (2026) define directed-linear-forest complexes and study their vertex-decomposability and related combinatorial properties, asking in their Problem 6.3 for homotopy types in broader directed-cycle examples. Their treatment supplies the foundational definition but no homotopy classification of this bidirected wheel. Caputi, Collari, and Smith (2026) investigate multipath complexes of bidirected paths and polygons, including homology of bidirected polygons; adding four spokes to the four-cycle produces a graph not covered by those polygon calculations. Earlier complete-digraph cycle-free chessboard results concern a different graph, while discrete-Morse complexes of the undirected five-vertex wheel parametrize acyclic matchings and are **not** the multipath complex considered here. No theorem cited in these papers directly supplies the displayed mixed-dimensional wheel homotopy type.

## Limitations
The finding is restricted to the fully bidirected wheel with four rim vertices and five vertices total. It neither gives a formula for larger wheels nor for other arc orientations, nor does it determine natural group actions on its homology. Its originality assessment is relative to the checked sources and searchable records, not a proof that no unindexed equivalent computation exists. The homotopy proof depends on the specified full finite matching certificate, which is supplied as `verify.py`.

## References
- Priyavrat Deshpande and Rutuja Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936, first public 2026-02-16. See definition of \(\mathrm{Dlf}(D)\) and Problem 6.3.
- Luigi Caputi, Carlo Collari, and Jason P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first public 2026-01-09. See Sections 1–2 for multipath definitions and the bidirected-path/polygon results.
- Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145, for the discrete Morse theorem.
