# Two and only two smallest orbit-refinement obstructions among connected cactus graphs

## Finding
For every finite, undirected, simple, connected cactus graph on at most seven vertices, ordinary one-dimensional counting colour refinement (\(1\)-WL) starting from the **uniform** vertex colouring produces precisely the vertex-orbit partition under the full automorphism group. Among the \(188\) isomorphism classes on exactly eight vertices, precisely **two** do not have this property. Consequently the minimum order of a connected cactus graph that is not refinable is exactly \(8\). The two order-eight exceptions are unique up to graph isomorphism and are described below.

The first exception has two disjoint triangles whose distinguished vertices are joined by a path of length three (two new interior path vertices). It has \(9\) edges, degree multiset \(\{3,3,2,2,2,2,2,2\}\), and one-dimensional refinement cells of sizes \(2,6\). The second is a four-cycle with a triangle glued at each of two *adjacent* four-cycle vertices. It has \(10\) edges, degree multiset \(\{4,4,2,2,2,2,2,2\}\), and the same refinement-cell sizes. Both have true automorphism-orbit sizes \(2,2,4\); each of their stable cells of size six contains two distinct automorphism orbits.

## Assumptions and scope
A *cactus* means a finite, connected, simple graph in which any edge belongs to at most one simple cycle (equivalently, each nontrivial biconnected block is a single cycle). The initial vertex colour is uniform, and each synchronous refinement step recolours a vertex by its old colour and the **multiset** of its neighbours' old colours. A graph is *refinable* if the eventual stable colour partition equals its automorphism-orbit partition. Graphs are counted up to unlabeled isomorphism. The assertion stops at eight vertices and does not classify larger cacti or individualised starting colourings.

## Proof
**Step 1 (complete exhaustive family).** Represent an \(n\)-vertex labelled graph by its \(n\) neighbour bitmasks. Initialise the family on one vertex. From each retained graph on \(n-1\) vertices, add a new vertex adjacent to every nonempty subset of the existing vertices, and retain the augmentation precisely when each edge has at most one alternative simple path between its endpoints with that edge deleted. The latter condition is equivalent to an edge belonging to at most one simple cycle, so it tests exactly the cactus condition on these connected augmentations.

Every connected graph on at least two vertices has a non-cut vertex (for example, an endpoint of a longest path in a spanning tree can be chosen as a leaf, whose removal leaves a connected graph). Deleting such a vertex from any connected cactus leaves a connected cactus. Consequently every isomorphism type on \(n\) vertices occurs among the augmentations of some type on \(n-1\) vertices. Retaining precisely one representative of each isomorphism class therefore gives a complete, nonredundant census by induction.

**Step 2 (exact isomorphism and orbit tests).** The dependency-free certificate `census_stdlib.py` compares graphs by an exhaustive bijection search preserving adjacency. Vertex degree together with sorted neighbour degrees is used only to prune impossible bijections: every accepted bijection is checked against each already mapped adjacency, and all remaining candidates are explored. The same exact bijection routine, with one vertex image fixed, decides whether any automorphism takes vertex \(u\) to vertex \(v\). Therefore the computed automorphism-orbit relation is exact, not a numerical approximation. Canonical-looking degree data are *never* used as a substitute for graph isomorphism.

**Step 3 (exact colour-refinement and conclusion).** The certificate implements synchronous stable multiset refinement by building for each vertex the ordered pair of its current colour and the sorted list of all neighbours' colours, assigning one new colour to each distinct signature. It stops precisely when equality of colours is unchanged. This condition is valid because subsequent iterations cannot split an already stable equitable partition. The generated counts for orders \(1\) through \(8\) are respectively
\[
1,\ 1,\ 2,\ 4,\ 9,\ 23,\ 63,\ 188.
\]
The respective numbers with stable classes strictly larger than automorphism orbits are
\[
0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 2.
\]
The final two edge lists, refinement cells, and exact automorphism orbits are output explicitly in `census_stdlib_output.json`. One exception has nine edges, and the other ten. Direct inspection of their edge lists identifies the two claimed glued-cycle shapes. Because all 188 types are tested, there are no other eight-vertex exceptions.

The degree quotient independently explains the failure: in the first graph the two degree-three vertices do not meet, each sees three degree-two neighbours, and every degree-two vertex sees one vertex of each degree. In the second the degree-four vertices are adjacent and each has three degree-two neighbours, again with every degree-two vertex seeing one neighbour of each degree. Thus these degree partitions are equitable, and \(1\)-WL cannot split the six degree-two vertices; the nontrivial distinction within that class is visible to automorphism orbits. These observations give a human-checkable witness, while the exhaustive census proves global minimality and uniqueness.

## Verification
Run `python3 census_stdlib.py` with standard-library Python \(3\). The program produces the complete JSON census and checks all order and exception counts and both orbit-size patterns via assertions. Compare the output byte-for-byte or as parsed JSON against `census_stdlib_output.json`. Independently, `python3 census_networkx.py` (NetworkX \(\ge2.8\), tested with \(3.6.1\)) starts from the published NetworkX graph atlas for orders at most seven, uses a distinct biconnected-component cactus test and NetworkX's independent isomorphism algorithm, constructs order eight by all vertex augmentations, and repeats stable refinement and pointed automorphism tests. Its separately recorded output is `census_networkx_output.json`. Both paths agree: exactly \(188\) order-eight connected cactus types and exactly two exceptional types, with edge counts \(9\) and \(10\).

The standard-library program is itself a terminating, exhaustive finite proof certificate. The independent checker is an error-detection cross-check, not a claim about unbounded order. Enumeration of all graphs of order beyond eight was neither performed nor required.

## Relationship to prior work
Arvind, Köbler, Rattan and Verbitsky introduced the systematic relationship between colour refinement, graph isomorphism, and *refinable* graphs; their general hierarchy does not provide the explicit first cactus counterexample threshold or both minimal witnesses. Related results on colour-refinement identification of unicyclic graphs address graph identification against other graphs, which differs from equivalence of stable cells and vertex orbits **within** a fixed cactus. A previously recorded order-eight example arising as a line graph of a tree matches the **nine-edge** witness; the newly established conclusion is the complete cactus cutoff and the **second**, ten-edge, exception. The finite cactus isomorphism counts agree with published cactus graph sequence A000083; that table lists graph counts, not the refinement-orbit obstruction classes.

## Limitations
The claim is an exact finite cutoff and classification through eight vertices, not a general theorem about larger cacti or rooted/individually coloured cacti. The two verification programs share the mathematical specification but use substantially different libraries, cactus tests, and isomorphism engines; a shared conceptual error is possible. Specialized earlier literature may contain an equivalent finite classification; absence from searched sources does not prove publication priority. No independent scientific audit has been performed.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first posted 2015-02-04), https://arxiv.org/abs/1502.01255.
2. V. Arvind et al., *Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:1606.04383 (first posted 2016-06-14), https://arxiv.org/abs/1606.04383.
3. OEIS A000083, number of connected unlabeled cactus graphs (independent check of the graph-count sequence), https://oeis.org/A000083.
4. *Canonical Labeling of Sparse Random Graphs*, STACS 2025, background on colour refinement of unicyclic components; not a result on the complete cactus orbit-refinement cutoff.
