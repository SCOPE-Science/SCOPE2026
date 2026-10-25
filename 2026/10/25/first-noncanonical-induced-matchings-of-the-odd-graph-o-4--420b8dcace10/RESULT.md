# First noncanonical induced matchings of the odd graph \(O_4\)

## Finding
Let \(O_4=KG(7,3)\) denote the odd graph on the three-element subsets of \([7]=\{0,1,\ldots,6\}\), with adjacency given by disjointness. An induced matching is a family of edges whose endpoints induce exactly that matching. The seven-point set has a natural edge coloring: the edge joining disjoint triples \(A,B\) receives the unique omitted point \(\ell(A,B)=[7]\setminus(A\cup B)\).

**Sharp mixing threshold.** Every induced matching of at least eight edges is monochromatic for the omitted-point labeling, whereas mixed-label induced matchings of size seven exist. Exactly \(5{,}580\) mixed-label induced matchings of size seven exist. Under permutations of the seven ground points they constitute five orbits, each determined by its edge-label multiplicity profile.

| Label multiplicities, sorted decreasingly | Number of seven-edge induced matchings | Number of \(S_7\)-orbits |
| --- | ---: | ---: |
| \((7)\) (monochromatic) | \(840\) | \(2\) |
| \((6,1)\) | \(420\) | \(1\) |
| \((4,2,1)\) | \(2{,}520\) | \(1\) |
| \((4,1,1,1)\) | \(1{,}680\) | \(1\) |
| \((2,2,2,1)\) | \(840\) | \(1\) |
| \((1,1,1,1,1,1,1)\) | \(120\) | \(1\) |
| **All seven-edge matchings** | **\(6{,}420\)** | **\(7\)** |

There are precisely \(315\) induced matchings of eight edges, all monochromatic. The canonical labeling has seven classes of ten edges, each an induced matching, as known from work on strong edge coloring of odd graphs.

## Assumptions and scope
Graphs are simple, undirected, and finite. Distinct edges \(AB,CD\) of \(O_4\) are compatible in an induced matching exactly when all four intersections \(A\cap C\), \(A\cap D\), \(B\cap C\), and \(B\cap D\) are nonempty. Ground-set permutations act on triples, edges, and induced matchings. The assertion is specific to \(KG(7,3)\); no unproved extension to larger odd graphs is asserted. The classification is of actual edge-subsets, not only isomorphism types.

## Proof
First enumerate the \(35=\binom{7}{3}\) vertices as triples in increasing lexicographic order. Form the \(70\) unordered disjoint triple-pairs as graph edges. For each edge \(e\), form a \(70\)-bit compatibility mask \(C(e)\) containing precisely the other edges satisfying the four-intersection condition above. This condition is an exact equivalence: disjoint endpoints cannot be the same vertex and cannot be adjacent in the disjointness graph; conversely, if any endpoint intersection is empty, the chosen edges have an unwanted adjacency. Thus an induced matching is exactly a clique in this compatibility relation.

For a positive integer \(k\), enumerate all increasing \(k\)-tuples of edge indices by the following recursive procedure. Choose the first index \(i\) and begin with the indices greater than \(i\) compatible with edge \(i\). At each node, choose the smallest available index \(j\), recurse on the remaining available indices greater than \(j\) that lie in \(C(j)\), and repeat on the other available choices. Prune a node only if fewer candidates remain than the number of edges still needed. Every increasing compatible tuple appears exactly once (induction on tuple length), no incompatible tuple appears, and the prune condition excludes only impossible completions. Therefore this is a finite exhaustive enumeration, not a sampling argument.

The included checker implements that mask recursion and independently implements a second recursion using the original triple-set intersections rather than compatibility masks. For \(k=7\), the two enumerators find exactly \(642\) choices containing lexicographically first edge. Their sorted label-multiplicity profiles have counts \(84,42,252,168,84,12\), respectively in the table's order. Direct enumeration over every first edge gives exactly the table's total \(6{,}420\) and its six row counts. As a cross-check using the transitive \(S_7\) action on the \(70\) edges, the anchored count \(642\) must give \(642\cdot70/7=6{,}420\). For \(k=8\), the independent recursions both find \(36\) choices containing the first edge, all with profile \((8)\). Direct enumeration gives precisely \(315\) eight-edge matchings, all monochromatic, again in agreement with \(36\cdot70/8=315\).

The permutation action is enumerated independently using all \(7!=5{,}040\) relabelings. Applying them to each enumerated seven-edge induced matching and partitioning into equivalence classes gives two monochromatic orbits of size \(420\) and one orbit each of sizes \(420\), \(2{,}520\), \(1{,}680\), \(840\), \(120\) with mixed profiles \((6,1)\), \((4,2,1)\), \((4,1,1,1)\), \((2,2,2,1)\), \((1,1,1,1,1,1,1)\), respectively. These orbit sizes sum to \(6{,}420\) and disjointly exhaust all enumerated matchings; the displayed classification follows.

A rainbow seven-edge witness, each pair written as two disjoint triples and with the seven distinct omitted points, is
\[
\begin{aligned}
&(012,345),\ (013,246),\ (024,156),\ (036,125),\\
&(045,236),\ (056,134),\ (146,235).
\end{aligned}
\]
The four-intersection criterion verifies compatibility of every pair of these edges. Hence seven is achievable with more than one label. If any induced matching with more than eight edges contained two labels, one could select an eight-edge submatching containing two differently labeled edges, contradicting the complete eight-edge census. This proves the mixing threshold for every cardinality.

## Verification
Run `python3 verify.py` with Python 3; it uses the standard library only. It checks both independently implemented anchored enumerations for sizes seven and eight, the complete labelled profile distributions, the eight-edge monochromatic property, every ground-point permutation, all seven ground-permutation orbits, and the consistency of their sizes. A successful run terminates with `VERIFY_OK`. The critical proof of exhaustion is the explicit lexicographic-recursion invariant above, coupled with the executable finite computation. No infinite assertion is inferred from finite test cases.

## Relationship to prior work
Wang and Zhao's 2014 manuscript studies odd graphs and their strong edge colorings; its omitted-point coloring provides the seven ten-edge induced matchings. Lužar, Mačajová, Škoviera and Soták (2021) prove rigidity of optimal strong edge colorings in the relevant Kneser setting. Thus **neither the maximum induced-matching size ten nor uniqueness of the optimal strong coloring is claimed as novel here**. The contribution is instead the exact first threshold permitting more than one omitted-point label and the complete seven-edge multiplicity and orbit census.

The literature on almost-intersecting uniform set families is relevant via the alternative description of the endpoints as a three-uniform family partitioned into disjoint pairs. Its general extremal statements do not state the target near-maximum, labeled-orbit census. The specific full 2012 article listed below was not accessible for complete inspection, so overlap risk is retained rather than dismissed.

## Limitations
This is an exact **finite** classification for \(KG(7,3)\). Its proof depends on reproducible exhaustive enumeration of \(70\) candidate edges and all \(5{,}040\) ground-set permutations, not on a closed-form infinite-family structural theorem. The 2012 primary article on almost-intersecting set families could not be checked in full, leaving the possibility of earlier unindexed coverage of this precise finite classification. The result has received no independent audit or external validation.

## References
- Tao Wang and Xiaodan Zhao, *Odd graph and its applications to the strong edge coloring*, first arXiv posting 2014-12-29, arXiv:1412.8358, https://arxiv.org/abs/1412.8358 .
- Borut Lužar, Erika Mačajová, Martin Škoviera and Roman Soták, *Strong edge colorings of graphs and the covers of Kneser graphs*, arXiv:2101.04768, https://arxiv.org/abs/2101.04768 .
- M. Alishahi and A. Taherkhani, work on induced subgraphs and Kneser graphs, arXiv:1801.03972, https://arxiv.org/abs/1801.03972 .
- P. Frankl and A. Kupavskii, work on almost-intersecting families, arXiv:2004.08714, https://arxiv.org/abs/2004.08714 .
- D. Gerbner and collaborators, *Almost Intersecting Families of Sets*, 2012 preprint / SIAM Journal on Discrete Mathematics, DOI:10.1137/120878744 (full text not inspected).
