# The first biconnected outerplanar counting-refinement obstructions

## Finding

For finite simple connected outerplanar graphs with at most eight vertices, ordinary synchronous one-dimensional counting colour refinement, starting with a uniform colour, produces exactly the automorphism-orbit partition except for **four** isomorphism types, all of order eight. Exactly **two** of the four are biconnected. In particular, every biconnected outerplanar graph of order at most seven is orbit-exact under colour refinement, and exactly two of the 75 biconnected types of order eight are not. This is the sharp minimum in the biconnected outerplanar family.

Equivalently, on these finite graph structures, the partition into one-free-variable types of two-variable first-order logic with counting quantifiers \(\mathrm{C}^2\) agrees with the automorphism-orbit partition in every case except the four listed below. This is a statement about *vertex types within each individual graph*, not about identification of nonisomorphic graphs.

The numbers of nonisomorphic connected outerplanar graphs on \(1,2,\ldots,8\) vertices are, respectively,
\[1,1,2,5,13,46,172,777.\]
Their orbit-refinement failure counts are
\[0,0,0,0,0,0,0,4.\]

Up to isomorphism the four counterexamples are the following explicitly labeled graphs on \(V=\{0,1,\ldots,7\}\). Within each table row, an unordered edge \(ij\) means \(\{i,j\}\); the full edge list is given, with no implicit additional edges.

| Type | Edges | Stable colour classes | Automorphism orbits | Two-connected? |
| --- | --- | --- | --- | --- |
| A (9 edges) | 04, 07, 12, 13, 25, 26, 34, 47, 56 | 013567 / 24 | 0567 / 13 / 24 | No |
| B (10 edges) | 01, 04, 14, 24, 25, 26, 27, 34, 35, 67 | 013567 / 24 | 0167 / 24 / 35 | No |
| C (10 edges) | 01, 05, 12, 16, 23, 26, 34, 45, 47, 57 | 0367 / 1245 | 03 / 1245 / 67 | Yes |
| D (11 edges) | 01, 04, 12, 14, 15, 23, 26, 27, 34, 56, 67 | 0357 / 12 / 46 | 07 / 12 / 35 / 46 | Yes |

Strings such as `013567` mean the *set* of vertices \(\{0,1,3,5,6,7\}\), not an integer or cyclic sequence. The witness catalogue carries machine-readable edge lists and the same partitions.

Type A is two disjoint triangles joined by a three-edge path. Type B is a four-cycle with a triangle attached at each of two adjacent cycle vertices. Both are cactus graphs. Type C is an eight-cycle with two noncrossing chords joining pairs of vertices separated by one intermediate vertex on the cycle; its triangle components are disjoint. Type D is an eight-cycle with three noncrossing chords, with exact edges given above. Types C and D are biconnected and not cactus graphs.

## Assumptions and scope

All graphs are finite, undirected, simple, connected and outerplanar, with at least one vertex and at most eight vertices. Colours are initially uniform and are refined by adjoining to each old colour the multiset of old colours of the neighbours, retaining multiplicities. The stable partition is compared with the full vertex-orbit partition under all graph automorphisms. Outerplanar means possessing a planar embedding with every vertex incident with the unbounded face. There is no claim for graph order nine or larger, arbitrary initial colourings, or recognition of graph isomorphism beyond an individual input.

## Proof

**A. Exhaustive generation.** A graph is outerplanar if and only if adjoining a new universal vertex produces a planar graph: place the universal vertex outside an outerplanar embedding, or conversely remove it from a planar embedding to obtain an embedding with the original vertices on one face. The predicate used by both programs is exactly this equivalence, with a standard planarity algorithm.

The NetworkX graph atlas supplies exactly one isomorphism representative of every simple graph on at most seven vertices. Filtering it by connectivity and the universal-apex test gives connected outerplanar counts \(1,1,2,5,13,46,172\). A connected outerplanar graph on eight vertices has a removable non-articulation vertex of degree at most two: take a terminal block in its block-cut tree. If that block is a bridge, its non-cut endpoint is a leaf; otherwise, a maximal outerplanar triangulation of its biconnected block has at least two degree-two ears, at least one different from the block's (possible) cut vertex. Removing that ear leaves the whole graph connected and outerplanar. Thus every eight-vertex class arises by adjoining a vertex with one or two neighbours to some seven-vertex connected outerplanar graph.

The program `enumerate_ear.py` constructs all such attachments, tests outerplanarity, and removes isomorphic repetitions by exact graph isomorphism tests within safe degree-based buckets. It finds exactly 777 distinct classes. This agrees independently with the coefficient of the connected-outerplanar generating function published by Bodirsky, Fusy, Kang and Vigerske (2005 preprint; 2007 journal article) and the OEIS sequence A111563.

The second independent program `enumerate_all_attach.py` avoids the degree-two-ear restriction entirely. Every connected graph with at least two vertices has a non-articulation vertex, so it generates all eight-vertex connected outerplanar graphs by adjoining a vertex with *any nonempty neighbourhood* to each of the 853 connected seven-vertex atlas graphs. It checks 108331 attachments, retains 5841 outerplanar candidates before deduplication, and obtains exactly the same 777 isomorphism classes. The two generation methods therefore have different completeness reductions.

**B. Exhaustive orbit comparison.** In `enumerate_ear.py`, iteration from a single initial colour stops only when no colour class splits. A signature retains the old colour and exact counts of neighbours in each old colour. For each graph, a graph-isomorphism enumerator lists every automorphism and computes its vertex orbits by exact union operations. The comparison finds zero failures on one through seven vertices and precisely four failures on eight vertices, with the edge sets and partitions in the table. Two of these four are biconnected.

Independently, `enumerate_all_attach.py` rebuilds the stable refinement partition using separately written code, then decides whether two vertices in the same cell share an orbit by testing isomorphism between the two copies of the graph with respectively one of the vertices uniquely marked. Such a pointed isomorphism exists if and only if an automorphism sends one vertex to the other. This independent criterion returns the same four exceptional structural signatures and no smaller exception.

**C. Direct witness verification.** The four listed stable partitions are equitable: the corresponding neighbour-count quotient matrices in the displayed colour-class order are, respectively,
\[
Q_A=\begin{pmatrix}1&1\\3&0\end{pmatrix},\quad
Q_B=\begin{pmatrix}1&1\\3&1\end{pmatrix},\quad
Q_C=\begin{pmatrix}0&2\\2&1\end{pmatrix},\quad
Q_D=\begin{pmatrix}0&1&1\\2&1&1\\2&1&0\end{pmatrix}.
\]
Each displayed partition is also a refinement of the degree partition, and hence equals the stable partition once its equitable nature and the recorded refinement output are checked. The automorphism groups have orders \(8,8,4,2\), respectively, and the listed orbit classes follow by explicit automorphism enumeration. In each case, one stable class contains vertices from two different automorphism orbits, proving failure. Graph types A–D are pairwise nonisomorphic, already distinguished by edge count or degree sequence.

The source programs implement every finite case of the argument, and the output files record their exact results. No numerical extrapolation to larger orders is made.

## Verification

Run with Python 3 and the package version specified in `requirements.txt`:

```sh
python enumerate_ear.py > ear_output.json
python enumerate_all_attach.py > all_attach_output.json
```

Both programs contain their own assertions. The expected structured outputs are embedded in the two files of those names. The witness catalogue `witness_catalog.json` separately lists the exact edge sets, stable cells and automorphism orbits. In particular, the independent programs agree on population 777, failure count four, absence of smaller failures, and the two biconnected exceptional degree profiles. The computation is exhaustive *because of the two completeness arguments in the proof*, not merely because it ran successfully.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky, in their 2015 preprint, define refinable graphs by equality between the stable colour-refinement partition and the automorphism-orbit partition, place the class in a hierarchy of isomorphism invariants, and prove structural and complexity results. Their full paper does not classify all small outerplanar graphs by this property. In particular, their general implications are not an enumeration of the non-refinable biconnected types of order eight.

Bodirsky, Fusy, Kang and Vigerske developed an exact enumeration of unlabeled outerplanar graphs, whose connected-class coefficient gives a separate cardinality check of 777. Their enumeration is by graph isomorphism, automorphism cycle indices and decomposition; it does not compute stable counting-colour partitions or identify the four refinability exceptions. A count of graph types alone does not imply which of them are orbit-exact.

The outerplanar biconnected case is a natural next case beyond trees and cactus graphs. The two non-biconnected examples occur among cactus graphs; the two additional biconnected examples are structurally different and show that an obstruction survives without bridges or cut vertices. Searches of published work did not identify an earlier exact four-graph outerplanar classification, but absence of a search hit is not proof of priority.

## Limitations

This is an exact finite classification for graph orders at most eight. The two exhaustive programs share the NetworkX graph-atlas and planarity implementations, though their generation methods and orbit tests differ; agreement therefore does not eliminate every possible software defect. The independent count 777 gives an external consistency check, not a direct proof of the four-way partition. A specialized earlier catalogue of colour-refinement orbits may exist. The result does not provide an asymptotic or all-order theorem, nor does it determine the minimal size of an outerplanar graph with a nontrivial fractional automorphism distinct from the orbit partition.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04; revised 2015-05-04. DOI: 10.1007/s00037-016-0147-6.
2. M. Bodirsky, É. Fusy, M. Kang, S. Vigerske, *Enumeration of Unlabeled Outerplanar Graphs*, arXiv:math/0511422, first posted 2005-11-16; *Electronic Journal of Combinatorics* 14 (2007), R66, DOI: 10.37236/984.
3. OEIS A111563, *Number of connected outerplanar graphs on n unlabeled nodes*, initial entry dated 2005-11-17, https://oeis.org/A111563.
4. NetworkX 3.6.1, graph atlas, graph isomorphism and planarity implementations, https://networkx.org/documentation/stable/.
