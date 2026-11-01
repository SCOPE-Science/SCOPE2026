# The bidirected bowtie multipath complex is \(S^1\vee\bigvee^4 S^2\)

## Finding
Let \(B\) be the bowtie graph obtained by identifying one vertex of two triangles. If \(\overleftrightarrow B\) contains both directed arcs over each undirected edge, then its multipath complex has integral homotopy type
\[
|X(\overleftrightarrow B)|\simeq S^1\vee\bigvee^4S^2.
\]
Thus \(\pi_1(X(\overleftrightarrow B))\cong\mathbb Z\), its reduced integral homology is \(\mathbb Z\) in degree one and \(\mathbb Z^4\) in degree two, and vanishes elsewhere.

## Assumptions and scope
The vertices are \(\{0,1,2,3,4\}\), the undirected edges are \(\{01,12,20,03,34,40\}\), and both orientations of every edge are retained. The twelve arcs, indexed from zero for the certificate, are
```
((0,1),(1,2),(2,0),(0,3),(3,4),(4,0),
 (1,0),(2,1),(0,2),(3,0),(4,3),(0,4))
```
A simplicial face is an arc set in which each vertex has indegree and outdegree at most one and there is no directed cycle. This is equivalent to a vertex-disjoint union of directed simple paths, allowing isolated vertices. The empty arc set is included as the empty face. The theorem is for exactly this finite graph; no general graph-family classification is implied.

## Proof
**Face classification.** Every edge subset meeting the indegree/outdegree bounds is a disjoint union of directed paths and directed cycles. The underlying bowtie has only two simple undirected cycles, its triangles, which meet solely in vertex \(0\). Hence the forbidden directed cycles are precisely the six reciprocal two-arc cycles and the two orientations of each three-arc triangle. This produces an independent alternative membership test for every one of the \(2^{12}=4096\) subsets.

**Exhaustive simplicial certificate.** The executable file `verify.py` checks these two membership tests agree on every subset and finds exactly \(101\) faces including the empty face, with numbers of nonempty faces by dimension \(0,1,2,3\) equal to \(12,40,40,8\). In increasing order of face size and numeric mask, for each pivot in the arc-index sequence
```
(9,2,0,8,4,1,7,5,6,3,11,10)
```
pair an unmatched nonempty face \(\sigma\) not containing the pivot with \(\sigma\cup\{i\}\), when both remain unmatched. These rules completely determine \(47\) pairs and leave precisely one critical vertex, one critical edge, and four critical triangles; there are no critical tetrahedra. The critical masks and dimensions are
```
(0,512), (1,272), (2,19), (2,168), (2,1216), (2,3200).
```
The certificate constructs the entire directed Hasse graph, reversing every matched covering relation, and topologically sorts all \(100\) nonempty faces. All vertices are processed, proving absence of directed gradient cycles and therefore proving acyclicity of the matching (not merely testing individual pairs).

**Integral attaching map.** Orient every simplex by increasing arc index. For each critical triangle, expand its signed simplicial boundary and eliminate every matched edge by its paired triangle, using the unit pivot of the oriented boundary. The executable checks the induced dependency digraph is acyclic and performs every integer elimination, obtaining the exact critical degree-two-to-degree-one Morse boundary matrix
\[
\partial^{\mathrm{Morse}}_2=\begin{pmatrix}0&0&0&0\end{pmatrix}.
\]
This elimination is the standard algebraic discrete-Morse differential and is integral because all matched incidence coefficients are units. The complete face-poset matching therefore gives, by discrete Morse theory, a CW complex with one vertex, one loop, four two-cells, and no other cells. Each two-cell attaching map represents an element of \(\pi_1(S^1)\cong\mathbb Z\) determined by its degree; all four degrees are zero, so each attaching map is nullhomotopic. The CW complex is consequently \(S^1\vee\bigvee^4S^2\), completing the proof.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It exhausts all \(4096\) arc subsets, checks both independent face characterizations, constructs all face incidences and the full reversed Hasse graph, verifies the matching is acyclic, and evaluates the signed integer Morse differential. The expected first line starts `VERIFY_OK` and includes `faces=101`, `matching_pairs=47`, `critical=(1,1,4,0)`, `gradient_DAG=100` and `Morse_d2=[0, 0, 0, 0]`. The critical cells and their masks are printed on the second line. A separate reduced Euler-characteristic check gives \(3\), agreeing with \(-1+4\). No random sampling or unbounded computation is involved.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith define multipath complexes and a general dynamical-module join decomposition, and calculate them for paths, polygons, grids and tournaments. The module theorem does not supply the bowtie's homotopy type: its directed edges form a shared strongly connected cyclic region rather than two independent dynamical modules. Caputi, Collari and Smith analyze bidirected paths and single polygons, not a pair of triangles glued at a vertex. Deshpande and Sawant independently study the equivalent directed-linear-forest complex and describe conflict hypergraphs and vertex-decomposability criteria, without giving this bowtie calculation.

This graph isolates the effect of gluing two bidirected cycles at one vertex. Each bidirected triangle has a one-dimensional six-edge multipath complex homotopy equivalent to \(S^1\), so two *disjoint* bidirected triangles give their join \(S^1*S^1\simeq S^3\). Identifying a vertex changes this to \(S^1\vee\bigvee^4S^2\), producing nontrivial fundamental group and four second-homology classes. This is a concrete first shared-vertex cyclic benchmark; it is not claimed to establish a general gluing formula.

## Limitations
The exact homotopy classification applies only to the fully bidirected bowtie on five vertices. It does not determine multipath complexes for larger friendship graphs, arbitrary cactus graphs, other edge orientations, or equivariant homotopy types. The verification is an exhaustive reproducible finite proof for the specified graph; no independent external audit has been performed. Equivalent unindexed calculations cannot be excluded solely by literature searching.

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (first public January 9, 2026).
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first public August 9, 2022), *Mathematika* 70 (2024).
3. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936 (first public February 16, 2026).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete-Morse theory).
