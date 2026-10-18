# A five-vertex projective-plane threshold for symmetric-digraph multipath complexes

## Finding

For any finite loopless simple undirected graph \(G\), let \(\overleftrightarrow G\) be its **symmetric digraph**: each edge \(\{u,v\}\) is replaced by both arcs \(u\to v\) and \(v\to u\). Let \(X(\overleftrightarrow G)\) be the simplicial complex whose vertices are these arcs and whose faces are arc sets forming vertex-disjoint directed paths (isolated graph vertices are allowed). These are also called *multipath* or *directed-linear-forest* complexes. The forbidden configurations are a repeated incoming arc, a repeated outgoing arc, and any directed cycle, including a directed two-cycle.

**Theorem.** For every simple undirected graph \(G\) with at most five vertices, the reduced integral homology of \(X(\overleftrightarrow G)\) has torsion **if and only if** \(G\) is isomorphic to the three-page triangular book
\[
B_3=K_2\vee\overline{K}_3,
\]
where the two vertices of \(K_2\) are adjacent to each other and to three independent vertices. This is the unique graph isomorphism type of minimum order with torsion in this symmetric-digraph class. Moreover,
\[
\boxed{X(\overleftrightarrow{B_3})\simeq\mathbb{RP}^{2}\vee\bigvee^{7}S^{2}.}
\]
In particular, its unreduced integral homology is \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z/2\mathbb Z\), \(H_2\cong\mathbb Z^{7}\), and zero above degree two.

This is a graph-order minimum only **within symmetric digraphs coming from simple undirected graphs**, not within all digraphs, multigraphs, or simplicial complexes. The theorem does not assert that \(\mathbb{RP}^{2}\) *alone* is realizable as a multipath complex.

## Assumptions and scope

Every graph is finite, loopless, undirected and simple, with at most five ordinary graph vertices. Graphs need not be connected; isolated vertices do not change the multipath complex. The symmetric digraph has two distinct oriented arcs for every ordinary graph edge. Simplices are nonempty arc sets; the empty face is understood. The ordinary integral simplicial boundary uses the increasing order of arcs and coefficient signs \((-1)^i\).

A named representative of the unique torsion graph has vertices \(0,1,2,3,4\) and edges
\[
\{01,02,03,04,12,13,14\}.
\]
Vertices \(0,1\) are the common endpoints of three triangles with third vertices \(2,3,4\). The example has fourteen oriented arcs and \(14,54,60,12\) nonempty simplices in dimensions \(0,1,2,3\), respectively.

## Proof

**1. The complete small-graph torsion census.** For graph order \(n\), list the \(\binom n2\) unordered potential edges lexicographically and encode each graph by its binary adjacency mask. Under each of the \(n!\) vertex permutations, transfer the mask to the permuted unordered edge positions. The least mask in the complete orbit is a canonical isomorphism representative. Enumerating all masks and retaining one least mask per orbit produces exactly \(1,2,4,11,34\) isomorphism types at orders \(1,2,3,4,5\), respectively.

For every representative, enumerate **all** subsets of its oriented arc set of cardinalities between one and \(n-1\). A subset is a multipath precisely when (i) every vertex has incoming and outgoing degree at most one and (ii) following each selected outgoing arc never closes a directed cycle. The upper cardinality bound is rigorous: a cycle-free union of directed paths on \(n\) vertices has at most \(n-1\) arcs. No face is omitted, and all subfaces of admissible subsets are admissible.

Form every signed simplicial boundary \(\partial_k\) over \(\mathbb Z\) and compute its exact Smith normal form using integer arithmetic. Since \(\partial_{k-1}\partial_k=0\) and the image of the earlier boundary is torsion-free, the torsion of \(H_{k-1}\) is exactly the torsion detected by nonunit invariant factors of \(\partial_k\). Across the five orders the numbers of torsion-bearing isomorphism types are \(0,0,0,0,1\). The unique type is the seven-edge graph displayed above, with canonical mask \(127\). The full census and Smith computations are executable in `verify_census.py`; the exact aggregate output is recorded in `census_output.txt`.

For this graph the three nonzero boundary Smith data are
\[
\begin{aligned}
\partial_1 &: 1^{\times13},\\
\partial_2 &: 1^{\times40},\;2^{\times1},\\
\partial_3 &: 1^{\times12}.
\end{aligned}
\]
Thus the boundary ranks are \(13,41,12\). Subtracting adjacent ranks from simplex counts yields \(H_1\cong\mathbb Z/2\mathbb Z\), \(H_2\cong\mathbb Z^7\), and no higher homology. This proves the sharpness and uniqueness assertions at graph order at most five, independent of the subsequent homotopy argument.

**2. A complete acyclic discrete-Morse matching.** The second checker, `verify_homotopy.py`, enumerates the \(140\) nonempty faces *independently* as bit subsets of the fourteen oriented arcs and reads the \(65\) paired face masks from `morse_certificate.json`. Every matched pair has dimensions differing by one; its larger face is obtained by adjoining one arc to its smaller face. The certificate partitions all \(140\) faces into \(130\) matched faces and exactly ten unmatched faces: one critical zero-cell, one critical one-cell and eight critical two-cells.

For each covering relation in the face poset, orient the relation upward unless it is a matched relation, in which case orient it downward. Kahn's complete topological sort visits all \(140\) faces along \(336\) such directed covering relations; consequently the matching is acyclic. Forman's discrete-Morse theorem therefore gives a CW complex homotopy equivalent to \(X\), with precisely the ten stated cells.

**3. Integral attaching degrees.** In increasing oriented-arc order, the simplicial incidence matrices have coefficients \(\pm1\). Cancel the \(65\) verified matched face pairs successively over \(\mathbb Z\), always at a unit pivot, updating every remaining column by the exact integral Schur complement. The verifier confirms all pivots have absolute value one and checks \(\partial^2=0\) after the cancellations. The remaining one-dimensional cell is a loop based at the sole zero-cell. The boundaries of the eight remaining two-cells against it, in certificate order, are
\[
(0,0,0,-2,0,0,-2,0).
\]
These numbers are the degrees of the two-cell attaching maps in the discrete-Morse CW model. A change of basis by \(GL_8(\mathbb Z)\), geometrically implemented by elementary homotopy equivalences of the wedge of attaching circles, transforms the degree vector to \((2,0,0,0,0,0,0,0)\). The corresponding CW complex consists of the degree-two attachment to a circle, which is \(\mathbb{RP}^{2}\), and seven trivially attached two-cells, namely seven wedged two-spheres. This proves the displayed homotopy equivalence.

The consistency check is \(\chi(X)=14-54+60-12=8\), which agrees with \(\chi(\mathbb{RP}^2\vee\bigvee^{7}S^2)=8\). The Euler check is only corroborative; it is not used to infer homotopy type.

## Verification

The package contains `verify_census.py` (requires Python 3 and SymPy), `verify_homotopy.py` (Python standard library), the exact `morse_certificate.json`, and the separately recorded outputs `census_output.txt` and `homotopy_output.txt`. In the directory containing those files, execute:

```sh
python verify_census.py
python verify_homotopy.py
```

The first command exhausts all \(52\) unlabeled isomorphism types at orders one through five and computes exact integer Smith forms; the second independently reconstructs the named complex, verifies all \(65\) matching pairs and all \(336\) face-poset covering relations, and computes the final integral attaching degrees. The scripts contain their own explicit numerical assertions. A finite exhaustive census is a proof for the stated finite size bound, **not** a proof for larger graphs or general digraphs.

## Relationship to prior work

Caputi–Collari–Di Trani's paper on path posets (2023, §6.4, Question 6.15) asked for multipath complexes with homotopy types beyond wedges of spheres and mentioned projective spaces. The present construction exhibits a genuine projective-plane **summand**, not an isolated projective plane. Subsequent work already established that torsion can occur for multipath complexes via relationships with other complexes; the present theorem therefore does not claim the first torsion example in the unrestricted digraph setting.

Caputi–Collari–Smith's January 2026 paper studies bidirected paths and cycles and gives their homology, whereas this example is a three-triangle **book with a common edge** and provides an exhaustive *sharp symmetric-digraph graph-order threshold* and an exact non-wedge homotopy type. The 2024 homotopy paper covers other families, including directed paths, polygons, grids, transitive tournaments and bipartite orientations, not this seven-edge bidirected book. Directed-forest shellability results have different hypotheses and do not imply these integral Smith data. None of these statements is taken to prove bibliographic uniqueness; the originality determination is limited to the comparisons described in the accompanying review.

The comparison to the symmetric \(K_{2,3}\) digraph is instructive: adding the single edge joining its two high-degree vertices creates the triangular book and changes a torsion-free multipath complex into one with \(\mathbb Z/2\mathbb Z\) in first homology. The result is about a **change in the underlying graph**, not a known consequence of a matching-complex calculation on the same graph.

## Limitations

The uniqueness claim is exhaustive only up to **five ordinary graph vertices** and only for symmetric digraphs of simple undirected graphs. It does not classify all orientations of those graphs, all multigraphs, or graphs of order six and larger. The example's full homotopy type has an additional seven-sphere wedge; the existence of a pure \(\mathbb{RP}^2\) multipath complex is not settled here. Although related recent articles and mathematical records were compared, undetected equivalent work remains a bibliographic risk. The computation relies on exact integer arithmetic, complete finite enumeration and a checked discrete-Morse certificate; it does not require probabilistic numerical experiments.

## References

1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first posted 2026-01-09. Full HTML: https://arxiv.org/html/2601.05670.
2. L. Caputi, C. Collari and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, Journal of Algebraic Combinatorics 57 (2023), 617–658, DOI:10.1007/s10801-022-01180-9. Full text: https://link.springer.com/article/10.1007/s10801-022-01180-9.
3. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, Mathematika 70 (2024), e12235, DOI:10.1112/mtk.12235; author-postprint details: https://irep.ntu.ac.uk/id/eprint/50523/.
4. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936 (2026), https://arxiv.org/abs/2602.14936.
5. L. Caputi, D. Celoria and C. Collari, *Monotone cohomologies and oriented matchings*, Homology, Homotopy and Applications 26 (2024), 137–161, DOI:10.4310/HHA.2024.v26.n2.a7.
