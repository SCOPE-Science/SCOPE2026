# The three-clique-free complexes of the Shrikhande and rook graphs have different homotopy dimensions

## Finding
Let \(\mathrm{Sh}\) denote the Shrikhande graph and let \(R_{4,4}=K_4\square K_4\) denote the four-by-four rook graph. For a finite simple graph \(G\), define the three-clique-free simplicial complex
\[
\operatorname{CF}_3(G)=\{U\subseteq V(G):G[U]\text{ contains no triangle}\}.
\]
Then the **integral homotopy types** are
\[
\boxed{\operatorname{CF}_3(\mathrm{Sh})\simeq\bigvee^{9} S^{6},\qquad
\operatorname{CF}_3(R_{4,4})\simeq\bigvee^{15} S^{5}.}
\]
These nonisomorphic strongly regular graphs have identical parameters \((16,6,2,2)\), and each has exactly 32 triangles. Nevertheless their three-clique-free homology groups are nonzero in different degrees. In particular, their three-clique-free complexes are not homotopy equivalent, despite having identical face counts through dimension two.

## Assumptions and scope
Both graphs have vertex set \(\{0,\ldots,15\}\), where vertex \(4i+j\) represents the coordinate pair \((i,j)\) with \(0\leq i,j\leq 3\). In the Shrikhande graph, \((i,j)\) is adjacent to \((k,\ell)\) when their difference modulo four belongs to
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\]
In the rook graph, two distinct vertices are adjacent exactly when their first or their second coordinates agree. A simplicial face is any subset not containing a three-vertex clique. The empty face is included only for augmented-chain bookkeeping. The assertions concern the two specified finite graphs, not an arbitrary strongly regular graph with these parameters.

## Proof
**Complete face sets.** For either graph, enumerate its 32 triangular vertex masks and test every integer mask from zero through \(2^{16}-1\). A mask is a face precisely when it contains none of those triangle masks. The resulting augmented face numbers, listed for dimensions from \(-1\) upward, are:

| Graph | \(-1\) | \(0\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) | \(7\) | \(8\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Shrikhande | 1 | 16 | 120 | 528 | 1452 | 2496 | 2568 | 1424 | 330 | 16 |
| Rook | 1 | 16 | 120 | 528 | 1428 | 2304 | 2040 | 816 | 90 | 0 |

Thus the augmented face-posets have respectively 8,951 and 7,343 elements.

**An acyclic matching.** Starting with all augmented faces unmatched, process vertex positions \(v=0,1,\ldots,15\). At stage \(v\), pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) if this latter face is also still unmatched. Both faces are then removed from the eligible set. Sort face masks numerically within each stage to make this construction deterministic. This produces 4,466 face pairs for Shrikhande, leaving five unmatched dimension-five faces and fourteen unmatched dimension-six faces. For rook there are 3,658 pairs, leaving twenty-one unmatched dimension-five faces and six unmatched dimension-six faces.

For a completely checkable acyclicity certificate, orient every Hasse edge of the augmented face-poset **upward** if it is paired, and **downward** otherwise. The standalone verifier constructs all such edges and exhausts them by Kahn topological sorting. For Shrikhande the resulting directed graph has 8,951 vertices and 48,288 directed edges, and the sort visits all 8,951 vertices. For rook the corresponding counts are 7,343 vertices, 37,744 directed edges, and 7,343 visited vertices. Thus both matchings are acyclic. The pair involving the empty face and vertex zero is omitted when passing to ordinary (unaugmented) discrete Morse theory, leaving exactly one critical vertex and the listed higher critical cells. Omitting that pair cannot introduce a directed cycle.

**Signed integer Morse differentials.** Orient each simplex by increasing vertex index and use
\[
\partial[v_0,\ldots,v_d]=\sum_{i=0}^{d}(-1)^i[v_0,\ldots,\widehat{v_i},\ldots,v_d].
\]
The Morse differential between dimensions six and five is calculated by exact signed gradient-path elimination: critical lower faces project to their own basis vector, lower faces paired upward are eliminated using the unit incidence in the boundary of their paired upper face, and lower faces paired downward project to zero. The recurrence and its termination are explicitly implemented in `verify.py`, whose acyclicity check supplies the required well-foundedness. It yields an integer matrix of shape \(5\times14\) for Shrikhande and \(21\times6\) for rook.

With rows and columns ordered by increasing critical-face mask, the Shrikhande matrix has determinant \(+1\) in its five-by-five minor consisting of all five rows and columns numbered \(0,1,4,9,11\) (zero-based). The rook matrix has determinant \(-1\) in its six-by-six minor consisting of rows \(0,2,4,7,9,11\) and all six columns. Since these are unit minors of maximal rank, all nonzero integral Smith invariants of the respective Morse differentials equal one. Thus their reduced integral homology is respectively \(\mathbb Z^9\) in degree six only, and \(\mathbb Z^{15}\) in degree five only.

Finally, Forman's acyclic-matching theorem gives a CW model having one vertex and cells only in dimensions five and six. Its five-skeleton is a wedge of five-spheres, and the homotopy classes of its six-cell attaching maps are completely determined by their integral degree vectors: \(\pi_5(\bigvee^r S^5)\cong\mathbb Z^r\). Unimodular changes of bases and elementary cell cancellations therefore split all unit Smith factors. The unmatched high-dimensional cells are precisely nine six-cells in the first model and fifteen five-cells in the second, proving the claimed integral homotopy equivalences.

## Verification
The complete self-contained Python standard-library program `verify.py` regenerates both graphs, lists every triangle and every clique-free face, constructs the deterministic matching, checks acyclicity over the entire directed Hasse graph, evaluates the signed integral Morse boundary, and computes both displayed unit determinants with exact integer arithmetic. Independently of the Morse construction, it directly reduces every original simplicial boundary matrix modulo two, obtaining one nonzero reduced Betti number (nine in degree six for Shrikhande, fifteen in degree five for rook). The exact output from the packaged verification run is in `check_output.txt`.

## Relationship to prior work
Ghosh and Selvaraja introduced a systematic treatment of three-clique-free complexes in arXiv:2602.09623v1 (first posted February 10, 2026), proving shellability under chordality and diamond-freeness hypotheses and for graphs formed by specified clique attachments. Both graphs here have induced chordless four-cycles, so the sufficient chordal theorem does not apply; the paper's examples and statements do not specify their homotopy types. Moradi's arXiv:1712.00583v1 develops the earlier algebraic theory of clique ideals and focuses its explicit families on paths, cycles, their complements and chordal graphs. Earlier exact independence-complex calculations for the Shrikhande/rook pair concern \(\operatorname{CF}_2\), not \(\operatorname{CF}_3\), and do not imply these results. Distinct neighborhood-complex or Čech-complex calculations likewise involve nonidentical simplicial constructions.

## Limitations
Only these two 16-vertex instances and their integral homotopy types are established. The proof uses exhaustive finite combinatorics and does not establish an infinite-family theorem, an equivariant refinement, or independent external validation. Literature searches cannot exclude every unindexed treatment, especially one phrased in triangle-hypergraph or Stanley–Reisner terminology. The algorithm is transparent and reproducible, but independently repeating a computational proof is still advisable.

## References
1. Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (February 10, 2026), https://arxiv.org/pdf/2602.09623.
2. Somayeh Moradi, *\(t\)-clique ideal and \(t\)-independence ideal of a graph*, arXiv:1712.00583v1 (December 2, 2017), https://arxiv.org/pdf/1712.00583.
3. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
4. W. S. Massey, *A Basic Course in Algebraic Topology*, Springer, 1991; cellular homotopy and attaching-degree arguments.
