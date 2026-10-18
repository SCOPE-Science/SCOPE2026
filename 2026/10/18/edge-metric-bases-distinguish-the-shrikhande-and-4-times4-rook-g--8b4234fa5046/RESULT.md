# Edge-metric bases distinguish the Shrikhande and \(4\times4\) rook graphs
## Finding
The Shrikhande graph \(S\) and the rook graph \(R=K_4\square K_4\) have identical strongly regular parameters \((16,6,2,2)\), yet different minimum numbers of vertex landmarks for uniquely identifying their edges:
\[
  \operatorname{edim}(S)=6,\qquad \operatorname{edim}(R)=5.
\]
Their entire minimum edge-metric-basis families have the following finite classifications.

| Invariant | Shrikhande \(S\) | Rook \(R\) |
|---|---:|---:|
| Graph vertices / graph edges | 16 / 48 | 16 / 48 |
| Edge-metric-basis size | 6 | 5 |
| Number of labeled minimum bases | 736 | 576 |
| Full automorphism group order | 192 | 1152 |
| Full-group orbit sizes | 48, 48, 64, 96, 96, 192, 192 | 576 |
| Exchange-graph connected components | 1 | 1 |
| Exchange-graph edges | 4128 | 3744 |
| Exchange-graph degree distribution | 6:64, 10:192, 11:192, 13:192, 14:96 | 13:576 |

The basis exchange graph has one vertex per minimum edge-metric basis and joins two such bases exactly when they differ by deleting one vertex and inserting one vertex. Under this precise definition, the Shrikhande exchange graph is connected but not regular, while the rook exchange graph is connected and regular. The latter minimum bases form a single automorphism orbit; the former form seven.

## Assumptions and scope
All graphs are simple, finite and undirected. Encode a vertex \((a,b)\in(\mathbb Z/4\mathbb Z)^2\) as the integer \(4a+b\), with \(0\le a,b\le3\).

The Shrikhande graph \(S\) joins distinct \((a,b)\) and \((c,d)\) when the difference \((c-a,d-b)\) modulo four belongs to
\[
D=\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}.
\]
The rook graph \(R\) joins distinct \((a,b)\) and \((c,d)\) when \(a=c\) or \(b=d\). In particular \(R\) is **not** the Cartesian square of a four-cycle, but the Cartesian square of a complete graph of order four.

For any such graph \(G\), vertex \(v\), and unordered edge \(e=\{x,y\}\), define
\[
d_G(v,e)=\min\{d_G(v,x),d_G(v,y)\}.
\]
A set \(T\subseteq V(G)\) *edge-resolves* \(G\) if for each two distinct edges \(e\ne f\), some \(v\in T\) satisfies \(d_G(v,e)\ne d_G(v,f)\). An *edge-metric basis* is an edge-resolving set of minimum cardinality. These are vertex landmarks resolving edges, not edge landmarks resolving edges in the line graph. All orbit and exchange counts are for sets of labeled vertices, not for ordered landmark lists.

## Proof
**Exact finite edge-resolution criterion.** List the 48 edges of \(G\) as lexicographically ordered pairs of endpoints. The breadth-first search from each of the 16 vertices yields every vertex-to-edge distance. For each of the \(\binom{48}{2}=1128\) unordered edge pairs \(\{e_i,e_j\}\), form the bit mask
\[
W_{ij}=\{v\in V(G):d_G(v,e_i)\ne d_G(v,e_j)\}.
\]
The defining quantifiers give the *exact equivalence*
\[
 T\text{ edge-resolves }G\quad\Longleftrightarrow\quad
 T\cap W_{ij}\ne\varnothing\ \text{for every }i<j.
\]
No probabilistic inference or extrapolation is involved. The accompanying program constructs all 1128 separator masks and checks each set \(T\) both by this hitting-set condition and, independently in its core decision predicate, by uniqueness of the 48 complete distance signatures \((d_G(v,e))_{v\in T}\). The two tests agree for every candidate examined.

**Minimality and exact counts.** Enumerate *every* vertex subset of cardinality \(k=1,2,\ldots,6\) for \(S\) (respectively \(k=1,2,\ldots,5\) for \(R\)), in increasing cardinality and lexicographic order. No smaller cardinality works in either case; at size six for \(S\), exactly 736 of the \(\binom{16}{6}=8008\) candidate subsets work, and at size five for \(R\), exactly 576 of the \(\binom{16}{5}=4368\) work. Empty sets cannot resolve 48 distinct edges. Since the enumeration exhausts all subsets of every smaller size, these statements establish the exact minima and the complete families of minimum bases.

**Full automorphism groups and orbit classification.** For \(S\), enumerate all invertible two-by-two matrices over \(\mathbb Z/4\mathbb Z\) that preserve \(D\). There are exactly 12, and each can be followed by one of 16 translations, producing 192 verified automorphisms. These are *all*: the neighborhood of vertex zero is an induced six-cycle; the nine nonneighbors are uniquely determined by their pairs of neighbors within that cycle. Hence an automorphism fixing zero embeds faithfully in the dihedral automorphism group of the six-cycle (at most 12 possibilities); vertex transitivity gives the upper bound \(16\cdot12=192\).

For \(R\), independently permute both coordinate alphabets and optionally exchange the two coordinates. These are \(2(4!)^2=1152\) verified, distinct automorphisms. They form the entire group: a vertex neighborhood is two disjoint triangles, and each of the nine nonneighbors is uniquely determined by its neighborhood inside those triangles. The vertex stabilizer therefore has order at most \(2(3!)^2=72\), yielding \(16\cdot72=1152\). Acting on every minimum basis, the full groups yield exactly the orbit sizes in the table.

For further replication, a smallest hexadecimal 16-bit vertex-set representative (bit \(v\) corresponds to vertex label \(v\)) for each \(S\)-orbit, with the corresponding orbit size, is
\[
\begin{array}{c|rrrrrrr}
\text{representative (hex)}&\mathtt{0x30f}&\mathtt{0x70b}&\mathtt{0x114b}&\mathtt{0x36c}&\mathtt{0x116c}&\mathtt{0x32e}&\mathtt{0x34b}\\
\text{orbit size}&48&48&64&96&96&192&192
\end{array}
\]
and the sole \(R\)-orbit has representative \(\mathtt{0x13c}\) and size 576. Each representative may also be decoded directly by taking the indices of set bits.

**Basis exchanges.** For each minimum-basis mask \(T\), inspect all pairs \(v\in T\), \(w\notin T\) and test whether \((T\setminus\{v\})\cup\{w\}\) belongs to the *previously exhaustively determined* minimum-basis family. This is exactly the adjacency predicate of the stated exchange graph, with no missing exchanges. The checker verifies symmetry, counts edges via degree sums, and explores every component by a full graph traversal. The computed degree histograms and component sizes are exactly those in the table: 4128 edges and one 736-vertex component for \(S\), and 3744 edges and one 576-vertex component for \(R\).

## Verification
Run the standalone Python standard-library file from this package:

```text
python3 verify_edge_metric.py
```

The program checks both graph adjacency constructions, all degrees, the \((16,6,2,2)\) common-neighbor counts, diameter-two distance shells, all edge signatures and 1128 edge-pair witness masks, exhaustive failure below each optimum, two equivalent resolution predicates on every tested subset, optimum basis counts, two full automorphism group constructions with stabilizer upper-bound certificates, orbit representatives/sizes, every basis exchange, all exchange degrees, edge counts, and connected components. It also verifies the context-only ordinary vertex-metric dimensions \(4\) for each graph. The exact final success markers begin `VERIFY_OK Shrikhande` and `VERIFY_OK Rook`; all assertions must pass. Every enumeration fits within the finite 16-vertex domain. No third-party package or downloaded dataset is required.

## Relationship to prior work
Kelenc, Tratnik and Yero introduced the vertex-to-edge edge metric dimension, including exact results for Cartesian *products of paths*, cycles and other graph families [1]. The four-by-four rook graph considered here is a Cartesian product of *complete graphs*; their grid proposition does not apply. Sane described the Shrikhande graph and its established automorphism/association-scheme structure [2]; no claim is made to rediscover these underlying graphs or their symmetry orders.

Hakanen, Junnila, Laihonen and Puertas studied the stronger \(\{2\}\)-resolving-set predicate on **all** vertex sets of size at most two, including a rook-graph section [3]. This is not edge resolution restricted to adjacent vertex pairs: a bound or classification for that stronger predicate does not enumerate edge-only minimum bases or their exchanges. Yi studied the related edge and fractional-edge dimension theory [4], with different explicit graph classes. Kuziak and Yero's broad survey [5], especially Section 8 and its Table 14, distinguishes vertex-to-edge resolution from the unrelated *line-graph* metric dimension and does not list either of the present two graphs. Indexed results comparing the same pair via independence complexes [6] concern homotopy rather than landmark separation. Published all-bases classifications for crown graphs and half graphs [7,8] use the same invariant but different graph families, with no implication covering these two sixteen-vertex graphs.

## Limitations
This is a reproducible, complete finite classification for these **two** explicitly defined graphs. It does not assert a formula for all strongly regular graphs or Hamming/Doob graph families. The connectedness and orbit claims refer to minimum edge-resolving vertex sets under the specified one-for-one exchange, not arbitrary resolving sets or other reconfiguration moves. Computational exhaustion supplies the finite proof, not an analytic family-wide classification. Identified prior sources and searchable published records support originality by statement comparison, but unindexed literature or unexamined tables remain a residual bibliographic risk; this is not an independent external audit.

## References
1. A. Kelenc, N. Tratnik and I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension* (arXiv:1602.00291v1, publicly submitted 2016-01-31), https://arxiv.org/abs/1602.00291 .
2. S. S. Sane, *The Shrikhande Graph*, Resonance (October 2015), https://people.math.binghamton.edu/zaslav/Oldcourses/510.S18/sane.shrikhande-graph.resonance2015.pdf .
3. A. Hakanen, V. Junnila, T. Laihonen and M. L. Puertas, *On the Metric Dimensions for Sets of Vertices* (arXiv:2003.02048), https://arxiv.org/abs/2003.02048 .
4. E. Yi, *On the edge dimension and fractional edge dimension of graphs* (arXiv:2103.07375), https://arxiv.org/abs/2103.07375 .
5. D. Kuziak and I. G. Yero, *Metric dimension related parameters in graphs: A survey on combinatorial, computational and applied results*, Section 8 (arXiv:2107.04877), https://arxiv.org/abs/2107.04877 .
6. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, public research record `2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187 .
7. *Edge-metric bases of crown graphs*, public research record `2026/10/4/SCOPE-edge-metric-bases-of-crown-graphs--b5b3c45f23e8`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-edge-metric-bases-of-crown-graphs--b5b3c45f23e8 .
8. *Edge-metric bases of half graphs*, public research record `2026/10/4/SCOPE-edge-metric-bases-of-half-graphs--13a0853af1d2`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-edge-metric-bases-of-half-graphs--13a0853af1d2 .
