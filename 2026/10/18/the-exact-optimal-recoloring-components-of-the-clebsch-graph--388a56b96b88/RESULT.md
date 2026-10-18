# The exact optimal recoloring components of the Clebsch graph

## Finding

Let \(C\) be the degree-five Clebsch graph (the folded five-cube). The graph of proper four-vertex-colorings of \(C\), with one-vertex recoloring as its adjacency rule, decomposes as
\[
\mathcal R_4(C)\cong 1680K_1\ \sqcup\ \bigsqcup_{j=1}^{960}F,
\]
where \(F\) is one and the same connected 28-vertex graph, with 60 edges and diameter 6. Consequently there are exactly 2,640 connected components. Under simultaneous Clebsch-graph automorphisms and palette permutations, the 960 copies of \(F\) form a single orbit; the frozen colorings form two orbits of respective sizes 1,440 and 240.

The exact degree spectrum, expressed as degree followed by multiplicity, is
\[
(0,1680),\ (2,3840),\ (4,11520),\ (5,7680),\ (6,3840).
\]
There are 28,560 colorings and 57,600 legal recoloring edges in total. **The coloring count 28,560 was already recorded as OEIS A159056; that count is not an originality claim.**

## Assumptions and scope

Use the labeled vertex set \(V(C)=\{0,1,\ldots,15\}\), represented as the four-bit binary vectors. Write \(a\oplus b\) for bitwise exclusive OR. Two distinct vertices are adjacent precisely when
\[
a\oplus b\in\{1,2,4,8,15\}.
\]
This is the folded five-dimensional cube: identify each five-bit word with its complement and choose its representative with highest bit zero. It has sixteen vertices and forty edges.

The palette \(\{0,1,2,3\}\) has **distinguished** colors. A coloring is any function from the sixteen vertices to the palette that assigns different colors to adjacent vertices. Distinct permutations of palette names are counted as distinct states. Two such functions are adjacent in \(\mathcal R_4(C)\) when they differ at exactly one vertex; the intermediate coloring, which here is the destination state, must remain proper. No Kempe-chain interchange or simultaneous multi-vertex change is permitted.

The independence number is five, as witnessed by the exhaustive subset check below; hence a proper 3-coloring would cover at most fifteen of the sixteen vertices. Since proper four-colorings exist, \(\chi(C)=4\). Thus this is recoloring at the minimum allowable palette, not above it.

## Proof

The proof is a finite exhaustive classification with a wholly specified search domain, complete recursion and graph traversal; the software in the package implements the following enumerations without external data or libraries.

**Step 1: graph identity and chromatic optimality.** Construct all sixteen neighborhoods using the five bitwise differences, and assert exactly forty undirected edges. Independently construct each vertex as an antipodal pair of five-cube vertices, joining a pair of classes when representatives differ in one bit. Both constructions yield the same graph. The first program checks all \(2^{16}\) vertex subsets by a deletion recurrence, marking a subset independent exactly if removing its highest-index vertex leaves an independent subset containing none of its neighbors. Its largest independent-set size is five. Since \(16>3\cdot5\), three colors are impossible; the enumeration below supplies four-colorings.

**Step 2: exhaust all labeled four-colorings.** Take the empty partial assignment. Recursively select one as-yet-uncolored vertex and branch over each of the four colors absent from its already-colored neighbors. Each branch either fixes that vertex or is rejected because it immediately violates properness. Induction on the number of assigned vertices shows that every valid full assignment appears in exactly one leaf and no invalid one appears. The resulting set has exactly 28,560 members. The second implementation uses *fixed numerical vertex order*, whereas the first selects the most constrained remaining vertex dynamically.

**Step 3: construct every recoloring edge.** For each coloring and each vertex, test each of the other three colors against all its neighbors. Record the destination exactly when it remains proper. An unordered edge is counted twice in the adjacency lists. The first program finds a total degree sum of 115,200, giving 57,600 edges. The second program instead generates every one-coordinate substitution and tests whether its tuple belongs to the independently generated valid-state dictionary. It obtains the same edge count and full degree histogram.

**Step 4: component census and distances.** Breadth-first search on this entire finite adjacency relation labels every component. Each program obtains precisely 1,680 singleton components and 960 components of size 28. For each 28-vertex component, the internal degree sum is 120, so it has 60 edges. Each program computes distances by breadth-first search from **every** vertex of **every** nonsingleton component; all these diameters equal six. This is not a sample of components or a partial numerical bound.

**Step 5: identify the symmetry structure.** The first program constructs explicit generators consisting of a translation of the four-bit labels, the four adjacent transpositions of the five cube coordinates descended through antipodal identification, and the three adjacent transpositions of the four palette names. It checks that each generator preserves the forty graph edges. Its induced map on colorings therefore preserves legal recoloring edges, and hence acts on connected components. Full breadth-first orbit enumeration under these generators gives exactly three component orbits:
\[
(\text{orbit size},\text{component size})
=(960,28),\ (1440,1),\ (240,1).
\]
Thus all 28-vertex components are isomorphic. The state orbits have sizes 3,840; 7,680; 7,680; 1,920; 1,920; 3,840; 1,440; 240, with the corresponding degrees in the executable output. No assumption about global uniqueness follows merely from this symmetry partition; it is the exhaustive component census combined with the checked symmetry action that establishes the stated classification.

## Verification

Run `python3 verify_core.py` and `python3 verify_alt.py` in a directory containing the two source files. They require only a standard Python 3 installation; no proprietary dataset, precomputed table or stochastic solver is used. Compare stdout against `output_core.txt` and `output_alt.txt`. Each script independently performs its own complete proper-coloring enumeration and complete recoloring-graph traversal and terminates with a `VERIFY_OK` marker after all stated assertions pass. The exact number of states, edges, component sizes, degrees and diameters are independently checked. Symmetry-orbit computations are performed in `verify_core.py`.

The exhaustive search is finite because there are sixteen vertices and four available colors; completeness follows from the full branching argument in Step 2, not from extrapolating a finite sample to an infinite assertion. The two graph constructions and the two transition-generation methods provide a cross-check against shared encoding errors.

## Relationship to prior work

Cereceda, van den Heuvel and Johnson introduced the single-vertex \(k\)-color graph and studied its connectedness generally. Their accessible author manuscript, bearing the earlier July 2005 report date, discusses general bounds and examples of frozen states, but does not give this Clebsch-specific component census. Bonsma and Cereceda studied general computational reachability and hardness of paths between colorings. McDonald's public 19 July 2015 preprint studies connectedness and Hamiltonicity for more general localized recoloring moves, but its inspected article does not specify these Clebsch graph parameters.

OEIS A159056 already records 28,560 proper labeled four-colorings of the Clebsch graph; neither the known total nor its chromatic polynomial determines the distribution into 2,640 components. The general chromatic-pairs polynomial of Asgarli and coauthors counts local recoloring edges but does not itself supply the component-size, diameter or symmetry-orbit distribution found here. The published abstract of Beier and coauthors' 2016 classification addresses which graphs can be coloring graphs, without presenting a Clebsch-specific count in the inspected material; the inaccessible full paper remains a literature-overlap risk.

## Limitations

This statement concerns only the 5-regular, 40-edge Clebsch graph, **not** its 10-regular complement; only four distinguished colors; and only single-vertex recoloring. It does not determine mixing times, component automorphism groups, connectivity for more colors, or any infinite family. The 2016 paper by Beier and collaborators could not be compared at full-text level, and equivalent unindexed earlier computations cannot be excluded. All review claims here concern the finite mathematical calculation and checked literature, not independent external validation.

## References

1. L. Cereceda, J. van den Heuvel and M. Johnson, *Connectedness of the Graph of Vertex-Colourings*, LSE-CDAM-2005-11 (July 2005); *Discrete Mathematics* 308 (2008), 913–919. DOI: `10.1016/j.disc.2007.07.028`. Accessible author manuscript: https://www.researchgate.net/publication/220194396_Connectedness_of_the_graph_of_vertex-colourings
2. P. Bonsma and L. Cereceda, *Finding Paths between Graph Colourings: PSPACE-completeness and superpolynomial distances*, CDAM Research Report LSE-CDAM-2007-12 (May 2007). Accessible text: https://doczz.net/doc/7578217/finding-paths-between-graph-colourings--pspace
3. D. C. McDonald, *Connectedness and Hamiltonicity of Graphs on Vertex Colorings*, arXiv:1507.05344, first arXiv release 19 July 2015. https://arxiv.org/abs/1507.05344
4. J. Beier, J. Fierson, R. Haas, H. M. Russell and K. Shavo, *Classifying Coloring Graphs*, *Discrete Mathematics* 339 (2016), 2100–2112. DOI: `10.1016/j.disc.2016.03.003`. Abstract: https://scholarship.richmond.edu/mathcs-faculty-publications/169/
5. A. P. Heinz, OEIS A159056, *Number of n-colorings of the Clebsch Graph*. https://oeis.org/A159056
6. S. Asgarli, S. Krehbiel, H. Levinson and collaborators, *Counting Subgraphs of Coloring Graphs*, *Graphs and Combinatorics* 41 (2025), article 82. DOI: `10.1007/s00373-025-02938-1`.
7. E. W. Weisstein, *Clebsch Graph*, MathWorld. https://mathworld.wolfram.com/ClebschGraph.html
