# Eight rank-three theories of finite Kneser graphs, with a sharp 35-vertex testing bound

## Finding

For integers \(1\le k\le n\), let \(\mathrm{KG}(n,k)\) be the simple graph whose vertices are the \(k\)-subsets of \([n]\), with two vertices adjacent precisely when the subsets are disjoint. In the first-order language of equality and undirected adjacency, the family \(\{\mathrm{KG}(n,k):1\le k\le n\}\) has exactly **eight equivalence classes for sentences of quantifier rank at most three**. Two parameters determine the same class if and only if they fall in the same row of the following table.

| Class | Exact parameter conditions | Smallest representative | Number of vertices |
|:---|:---|:---|---:|
| A | \(n=k\) | \(\mathrm{KG}(1,1)\) | 1 |
| B | \(k<n<2k\) | \(\mathrm{KG}(3,2)\) | 3 |
| C | \(n=2k\) and \(k=1\) | \(\mathrm{KG}(2,1)\) | 2 |
| D | \(n=2k\) and \(k\ge2\) | \(\mathrm{KG}(4,2)\) | 6 |
| E | \(k=1\) and \(n\ge3\) | \(\mathrm{KG}(3,1)\) | 3 |
| F | \(k\ge2\) and \(n\ge3k\) | \(\mathrm{KG}(6,2)\) | 15 |
| G | \(k\ge2\) and \(n=3k-1\) | \(\mathrm{KG}(5,2)\) | 10 |
| H | \(k\ge3\) and \(2k+1\le n\le3k-2\) | \(\mathrm{KG}(7,3)\) | 35 |

In particular, every rank-three theory realized by a finite Kneser graph is realized on at most **35 vertices**, and 35 is optimal **within this family**. The sparse class H contains all odd graphs \(\mathrm{KG}(2k+1,k)\) with \(k\ge3\), though their orders and diameters grow without bound.

## Assumptions and scope

All graphs are finite, simple and unlabelled for logical comparison. The only nonlogical relation is adjacency, interpreted symmetrically and irreflexively; equality is available. All first-order quantifiers range over graph vertices, not the underlying ground-set elements. The rank of a formula is its maximum depth of nested quantifiers. The parameter domain includes the edgeless case \(n<2k\), the matching case \(n=2k\), and the connected case \(n\ge2k+1\). No cardinality-counting quantifiers, order, subset-incidence relation, vertex colours or named ground-set elements are present.

## Proof

**Three-move extension principle.** In any vertex-transitive simple graph, the entire three-round Ehrenfeucht--Fraisse behaviour is determined by the profiles available for a second vertex relative to a chosen first vertex. A profile records equality and adjacency of the first two vertices, together with which equality/adjacency diagrams can be realized by a third vertex. To prove this, Duplicator answers the first move arbitrarily, the second with a vertex of the same profile (possible at every base vertex by transitivity), and the third with a vertex realizing the requested diagram. This also handles repeated selections, because equality with either already selected vertex is part of the diagram. Thus two vertex-transitive graphs with the same realized two-point profiles agree on all sentences of rank at most three.

The action of the symmetric group on \([n]\) makes every Kneser graph vertex-transitive.

**Degenerate ranges.** For \(n<2k\) the graph has no edges. Its order \(\binom nk\) is one when \(n=k\), and at least three otherwise. For \(n=2k\), each \(k\)-set has the unique neighbour given by its complement; the graph is a perfect matching. It has one edge when \(k=1\), and at least three edges when \(k\ge2\). For \(k=1\) and \(n\ge3\), the graph is a complete graph on at least three vertices. Within each of these five classes, the possible three-round equality/adjacency diagrams are independent of the actual order. (In particular, a three-move game cannot count beyond three isolated vertices or three complete-graph vertices, or beyond three matching edges.)

**Connected noncomplete range.** Suppose \(k\ge2\) and \(n\ge2k+1\). Every vertex has neighbours and nonneighbours. For two distinct vertices \(A,B\), let \(t=|A\cap B|\). If they are adjacent, \(t=0\); otherwise \(1\le t\le k-1\). Any further vertex distinct from \(A,B\) can be chosen adjacent to exactly one of them, or to neither: the first two possibilities follow by selecting a \(k\)-set disjoint from one, but containing an element from the other; for the third, when \(t=0\) choose a set meeting both, and when \(t>0\) choose a different set meeting their intersection (with the elementary \(k=2\) case handled using an element outside their union). For each of these constructions \(n\ge2k+1\) leaves enough room to avoid the already selected vertices. When \(A=B\), distinct neighbours and nonneighbours both exist. Thus the only varying third-vertex extension for a pair of *distinct* vertices is whether it has a common neighbour.

There is a \(k\)-set disjoint from both \(A\) and \(B\) exactly when
\[
|[n]\setminus(A\cup B)|=n-2k+t\ge k,
\qquad\text{equivalently }n\ge3k-t.
\]
For adjacent vertices \(t=0\), the common-neighbour extension exists exactly when \(n\ge3k\). For nonadjacent vertices, every intersection size \(1\le t\le k-1\) occurs (as \(n\ge2k+1\)); the extension exists for at least one such pair, by taking \(t=k-1\). It exists for **every** nonadjacent pair exactly when \(n\ge3k-1\), since \(t=1\) is attainable. Hence the same three-round profiles occur throughout each of classes F, G and H, respectively:

* F: adjacent and all nonadjacent pairs have a common neighbour;
* G: no adjacent pair, but every nonadjacent pair, has a common neighbour;
* H: no adjacent pair has one, and some nonadjacent pairs do while others do not.

The extension principle proves rank-three equivalence within each listed row.

**Separation of the eight rows.** Each of the following graph properties is expressed by a first-order sentence of quantifier rank at most three: at least two vertices; at least three vertices; existence of an edge; existence of two distinct nonadjacent vertices; existence of a vertex with at least two distinct neighbours; existence of a triangle; existence of two distinct nonadjacent vertices with a common neighbour; and existence of two distinct nonadjacent vertices with **no** common neighbour. In the last case, an explicit sentence is
\[
\exists x\,\exists y\,[x\ne y\land\neg E(x,y)\land
\forall z\,\neg(E(x,z)\land E(y,z))].
\]
The associated eight-bit truth profiles, in the order displayed, are respectively

| Class | Rank-three truth profile |
|:---|:---|
| A | `00000000` |
| B | `11010001` |
| C | `10100000` |
| D | `11110001` |
| E | `11101100` |
| F | `11111110` |
| G | `11111010` |
| H | `11111011` |

All eight profiles are different, proving that no two rows collapse.

**Sharpness.** The smallest orders in A--G are at most 15. A graph of class H requires \(k\ge3\) and \(n\ge2k+1\), so its order is at least \(\binom{2k+1}{k}\ge\binom73=35\), attained at \((n,k)=(7,3)\). Therefore no family-wide representative cap below 35 works.

## Verification

`verify_kneser.py` generates Kneser graphs directly as bit-encoded \(k\)-subsets, then independently computes (i) full rank-three first-order types by the atomic-diagram extension recurrence on ordered triples and (ii) the eight explicitly separating rank-three sentence truth values. It checks all eight smallest representatives and 33 parameter instances covering all eight classes (maximum sampled graph order 126). Running `python3 verify_kneser.py` reproduces the attached `verification_output.txt` ending in `VERIFY_OK`.

The finite computations confirm but are not used to extrapolate the universal claim; the extension principle and subset constructions prove the result for all positive parameters.

## Relationship to prior work

Kneser graphs are a classical disjointness-graph family. Katona and Kisvölcsey's treatment of Erdős--Ko--Rado inequalities concerns independent sets and neighbourhood inequalities on the same graphs, not first-order rank-three theories. Pikhurko and Verbitsky's survey gives the Ehrenfeucht-game characterisation of graph logical depth and discusses strongly regular graphs, but does not state this eight-class classification. Merino, Mütze and Namrata classify Hamiltonicity of connected Kneser graphs, a different invariant, while identifying the same underlying \(k\)-subset family and sparse odd-graph subfamily.

The \(k=2\) subfamily can also be studied through complements of triangular (Johnson) graphs or through strongly regular graph parameters. Neither specialisation covers the new \(k\ge3\) transition between classes G and H: for those parameters, the presence of a common neighbour of nonadjacent vertices depends on their intersection size. The result here treats **all** admissible Kneser parameters, including the disconnected boundaries, in one rank-three theorem.

## Limitations

The equivalence is restricted to **quantifier rank at most three** in pure adjacency/equality logic. It does not claim equivalence in counting logic, at higher rank, in the subset-incidence language, or between arbitrary finite graphs. The sharp 35-vertex cap is only within the Kneser family. Historical research on odd graphs and non-indexed logical classifications may contain overlapping statements; a potentially relevant older full text was inaccessible and exact historical priority is not established. There is no independent audit or external certification of this finding.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, first publicly available on arXiv 2010-03-25, arXiv:1003.4865, https://arxiv.org/abs/1003.4865.
2. G. O. H. Katona and Á. Kisvölcsey, *Erdős--Ko--Rado from intersecting shadows*, Discussiones Mathematicae Graph Theory 32 (2012), 379--382, freely accessible manuscript https://real.mtak.hu/7991/1/Erdos-Ko-Rado%20from%20intersecting%20shadows.pdf.
3. N. Biggs, *Some odd graph theory*, Annals of the New York Academy of Sciences 319 (1979), 71--81, https://doi.org/10.1111/j.1749-6632.1979.tb32775.x (bibliographic page examined; complete text unavailable).
4. A. Merino, T. Mütze and Namrata, *Kneser graphs are Hamiltonian*, arXiv:2212.03918, https://arxiv.org/abs/2212.03918 (relevant later graph-theoretic comparison, not the archival date anchor).
