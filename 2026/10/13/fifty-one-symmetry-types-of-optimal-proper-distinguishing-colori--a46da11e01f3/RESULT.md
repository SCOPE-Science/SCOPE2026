# Fifty-one symmetry types of optimal proper distinguishing colorings of the Heawood graph

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, the point–line incidence graph of the Fano plane. A **proper distinguishing coloring** assigns colors to vertices so that adjacent vertices have different colors and no nonidentity graph automorphism preserves every color class individually. Then its distinguishing chromatic number is \(\chi_D(H)=4\). More precisely:

* There are exactly \(328608\) proper distinguishing colorings using a fixed, labelled palette of four colors, and each uses all four colors.
* On forgetting the names of the colors, these are exactly \(13692\) partitions into four nonempty independent color classes.
* The full graph automorphism group, of order \(336\), has exactly \(51\) orbits on those partitions. The orbit-size multiset is \(\{56^1,84^1,112^1,168^{16},336^{32}\}\), where an exponent denotes the number of orbits of that size.

The accompanying `orbit_representatives.csv` records one canonical four-class partition for each orbit, its exact orbit size, color-class-size profile and residual symmetry group acting **by permuting** the color classes. The exceptional orbit sizes \(56\), \(84\) and \(112\) correspond respectively to residual partition-stabilizer orders \(6\), \(4\) and \(3\). These are not violations of distinguishingness: no nonidentity automorphism fixes **each** named color class.

## Assumptions and scope

Use nonzero three-bit vectors \(P=\{1,\ldots,7\}\) to represent points of \(\mathbf F_2^3\). Represent lines by the seven lexicographically ordered sets \(\{a,b,a\oplus b\}\) for unequal nonzero vectors \(a,b\); the resulting order is \((123),(145),(167),(246),(257),(347),(356)\). Here \(\oplus\) is bitwise XOR. Number the fourteen vertices as the seven points \(1,\ldots,7\), followed by these seven lines in the stated order. A point is adjacent to its three incident lines, and there are no other edges.

A color-class partition is encoded as a restricted-growth word \((c_0,\ldots,c_{13})\), where \(c_0=0\), and, for later indices, \(0\le c_i\le 1+\max(c_0,\ldots,c_{i-1})\). Each symbol labels one class by order of first appearance. Only partitions into nonempty classes and proper colorings are counted; a palette is called *labelled* when its colors are distinguishable symbols.

## Proof

**The automorphisms.** An automorphism of connected bipartite \(H\) either preserves both sides or exchanges them. A side-preserving automorphism sends Fano points and lines to points and lines, respecting collinearity. Because every pair of distinct nonzero vectors lies on \(\{a,b,a\oplus b\}\), its point permutation preserves XOR of distinct points, hence is induced by an invertible linear map of \(\mathbf F_2^3\). Conversely each such map induces a side-preserving graph automorphism. There are \((2^3-1)(2^3-2)(2^3-2^2)=168\) such maps. The incidence-reversing polarity associating a nonzero vector \(p\) to its orthogonal line \(\{q:p\cdot q=0\}\), and conversely, is a side-exchanging involution. Every side-exchanging automorphism is its composition with a side-preserving one. Thus \(|\operatorname{Aut}(H)|=336\). The verifier constructs all \(336\) permutations from these two generators and checks all \(21\) edges for each permutation.

**Exhaustive, exact partition computation.** Enumerate all restricted-growth words for \(14\) vertices with at most four symbols by processing vertices in fixed order. For every position, try every old symbol and at most one new symbol, and reject any symbol already used on an adjacent earlier vertex. This bijectively enumerates all proper vertex partitions into at most four color classes: every partition has a unique restricted-growth encoding, and every rejected extension violates properness. Counts classified by number of classes are exactly

\[
\begin{array}{c|ccc}
\text{classes}&2&3&4\\\hline
\text{proper partitions}&1&350&29610
\end{array}.
\]

For each complete partition, compare its fourteen color symbols with their images under all \(335\) nonidentity graph automorphisms. It is distinguishing precisely when every comparison differs in at least one position. This gives zero proper distinguishing partitions with two or three classes, and exactly \(13692\) with four classes. As an additional reproducible lower-bound certificate, `three_color_obstructions.csv` contains one representative from each of the ten automorphism orbits of proper three-class partitions, its orbit size and a *nonidentity color-preserving graph automorphism* written as a fourteen-entry image list. These ten orbits cover all \(350\) three-class partitions; the single two-class partition also has a nontrivial color-preserving automorphism. Consequently three colors do not suffice, whereas the enumerated four-class partitions prove \(\chi_D(H)=4\).

For four classes, each unlabelled partition admits exactly \(4!=24\) assignments of four distinct palette names, yielding \(13692\cdot24=328608\) distinct proper distinguishing colorings on the fixed labelled four-color palette. For an orbit calculation, apply each of the \(336\) graph automorphisms to the fourteen positions of a restricted-growth word, normalize the symbols again by first occurrence, collect the resulting words and remove the orbit. This partitions the \(13692\) successful words into the \(51\) orbits and orbit-size multiset asserted. Each orbit representative in the CSV is checked against the automorphisms; no unenumerated partitions remain.

The cardinality-weighted symmetry classification can be checked independently from its eight color-class-size profiles, in descending order: \((4,4,3,3):5208\), \((4,4,4,2):1568\), \((5,3,3,3):1120\), \((5,4,3,2):4032\), \((5,5,2,2):420\), \((5,5,3,1):336\), \((6,3,3,2):672\), and \((6,4,2,2):336\). These totals sum to \(13692\).

## Verification

`verify.py` is a Python standard-library implementation of the exact restricted-growth partition enumeration and generates the two CSV certificates with `python verify.py --csv orbit_representatives.csv three_color_obstructions.csv`. It constructs the automorphism group directly from linear maps and polarity. `enumerate_cpp.cpp` is an independent labelled-palette enumeration: it first assigns four colors to the seven points, then assigns each line a color avoiding its three incident point colors, and compares the resulting full coloring against all automorphisms. Compile with `g++ -std=c++17 -O2 enumerate_cpp.cpp -o enumerate_cpp` alongside `heawood_aut.h`, then run `./enumerate_cpp 4`; running `./enumerate_cpp 3` independently excludes three-color solutions. The C++ header contains a complete literal automorphism array, not an external runtime dependency.

The C++ enumerator returns \(719052\) proper labelled four-palette colorings in total and \(328608\) distinguishing ones. Independently the Python verifier gives \(\sum_r (4)_r N_r=719052\), for \(N_2=1\), \(N_3=350\), \(N_4=29610\), where \((4)_r\) is the number of injective names for \(r\) classes. Agreement with the known chromatic polynomial at palette sizes two through four provides an external cross-check of ordinary proper coloring counts, not the symmetry-breaking conclusion. These are finite exhaustive algorithms with explicit short source code, not sampling.

## Relationship to prior work

Collins and Trenk introduced the distinguishing chromatic number and its graph-coloring framework in 2006. Cranston's 2018 girth-at-least-five paper explicitly exhibits a proper distinguishing four-coloring of the Heawood graph (Figure 3); that construction is credited as earlier four-color *existence*, not as an enumeration. Alikhani and Soltani study upper bounds for bipartite high-girth graphs; bounds do not imply multiplicities or partition orbits. Shirdareh and collaborators' distinguishing polynomial counts colorings without the additional **properness** requirement in other families, and likewise does not supply this Heawood calculation. The ordinary Heawood chromatic polynomial counts every proper coloring, including those fixed by nontrivial automorphisms, and cannot on its own imply the counts above.

## Limitations

This result concerns only the fourteen-vertex Heawood graph, its ordinary vertex colorings, and the full graph automorphism group. It does not classify proper distinguishing colorings of arbitrary incidence graphs or all palettes. The 51-orbit classification is an exact finite computation accompanied by two reproducible methods; it is not an independent external mathematical audit. Earlier unindexed enumerations under alternative terminology remain a possible priority risk. The catalog of 51 representatives is part of the result and is necessary for the stated full orbit classification; it is not a table imported from existing literature.

## References

1. K. L. Collins and A. N. Trenk, “The Distinguishing Chromatic Number,” *Electronic Journal of Combinatorics* **13** (2006), R16, DOI: `10.37236/1042`. First public publication: 2006-02-15. Full text: `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r16/pdf/`.
2. D. W. Cranston, “Proper Distinguishing Colorings with Few Colors for Graphs with Girth at Least 5,” *Electronic Journal of Combinatorics* **25** (2018), P3.5, DOI: `10.37236/7170`. Full text: `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i3p5/pdf/`.
3. S. Alikhani and S. Soltani, “The distinguishing chromatic number of bipartite graphs of girth at least six,” arXiv:`1709.10021`, `https://arxiv.org/pdf/1709.10021`.
4. S. Shirdareh and collaborators, “Distinguishing Polynomials of Graphs,” arXiv:`2403.19264`, `https://arxiv.org/pdf/2403.19264`.
5. E. W. Weisstein, “Heawood Graph,” *MathWorld*, `https://mathworld.wolfram.com/HeawoodGraph.html` (ordinary chromatic polynomial cross-check only).
