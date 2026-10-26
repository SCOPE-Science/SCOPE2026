# Complete five-landmark distance-equalizer census of rectangular Hamming graphs

## Finding
Let \(R_{p,q}=K_p\square K_q\) be the rectangular rook graph on \([p]\times[q]\), with integers \(p,q\ge5\). A *distance-equalizer set* \(S\) satisfies: for every two distinct vertices \(u,v\notin S\), some \(s\in S\) has \(d(u,s)=d(v,s)\). Its minimum cardinality is the equidistant dimension \(\xi(R_{p,q})\). The previously established value is \(\xi(R_{p,q})=5\) throughout this range [3].

The complete set of **all** five-vertex distance-equalizer sets has precisely the following nine row-and-column isomorphism types; the last four occur only at the indicated boundary. A five-cell set is encoded by a list of row masks: a mask \(m\) indicates that the row contains a selected cell in column \(j\) exactly when bit \(j\) of \(m\) is one, using zero-based indices. Independent permutations of rows and columns are allowed.

| Row masks | Condition | Row/column automorphism order |
|---|---|---:|
| `(1,1,7)` | all \(p,q\ge5\) | 4 |
| `(1,2,7)` | all \(p,q\ge5\) | 2 |
| `(1,3,5)` | all \(p,q\ge5\) | 2 |
| `(1,3,6)` | all \(p,q\ge5\) | 1 |
| `(1,2,4,8,16)` | all \(p,q\ge5\) | 120 |
| `(1,1,1,1,1)` | \(p=5\) | 120 |
| `(1,1,1,1,2)` | \(p=5\) | 24 |
| `(31)` | \(q=5\) | 120 |
| `(1,30)` | \(q=5\) | 24 |

Equivalently, the first four types are four distinct five-edge patterns supported on three rows and three columns; the fifth is a matching of size five. The boundary patterns are five cells in one entire column, a four-plus-one split across two columns, and their transposes.

Writing \((t)_k=t(t-1)\cdots(t-k+1)\), the **exact number of minimum distance-equalizer sets**, with every board cell individually labeled, is

\[
\boxed{B(p,q)=\frac94(p)_3(q)_3+\frac{(p)_5(q)_5}{120}
+\mathbf1_{p=5}\,q(5q-4)+\mathbf1_{q=5}\,p(5p-4).}
\]

In particular, \(B(5,5)=8430\), \(B(5,6)=17076\), and \(B(6,6)=36720\). The four additional optimum shapes exist only at the thin boundary, and there are exactly five symmetry types once both sides exceed five.

## Assumptions and scope
The graph is finite, simple, connected, and has vertex set \([p]\times[q]\). Distances in the rook graph are \(0\) on identical vertices, \(1\) when precisely one coordinate differs, and \(2\) when both differ. Throughout \(p,q\) are arbitrary integers at least five, not necessarily equal. A basis is a minimum-cardinality distance-equalizer set. The known assertion that the minimum cardinality is five is taken from Proposition 2.4/Theorem 2.5 of [3]; this work establishes the new **classification and number of all bases**, not the minimum-cardinality bound. Primary subject classification: MSC2020 05C12.

## Proof
**1. Complementary incidence signatures.** Fix an arbitrary five-cell set \(S=\{s_0,\ldots,s_4\}\). For each exterior cell \(v\notin S\), form a five-bit signature \(b(v)\) by setting bit \(i\) to one precisely when \(v\) and \(s_i\) share a row or column. Since \(v\notin S\), a one-bit means distance one and a zero-bit means distance two. Therefore two exterior cells have *no* equal-distance landmark if and only if their two five-bit signatures are bitwise complementary. Thus \(S\) is a distance-equalizer set exactly when no two distinct exterior cells have complementary signatures. This is an equality of finite combinatorial predicates, not an approximation.

**2. Exhaustive finite reduction independent of board size.** The five selected cells define two partitions of \(\{0,1,2,3,4\}\): which labels share a row, and which share a column. Both are set partitions, and their common block intersections must contain at most one label (distinct selected cells cannot occupy the same coordinate pair). Conversely every such pair specifies a five-cell configuration, up to independent relabeling of rows and columns. There are exactly 52 set partitions of a five-element set, hence the two-partition generation is exhaustive. Canonicalization by sorting the row masks and minimizing over all permutations of used columns gives precisely one representative per row/column-isomorphism type.

For any representative supported on \(a\) rows and \(b\) columns, in testing whether an exterior pair fails the condition it suffices to retain the used coordinates and **at most two additional unused rows and columns**. Indeed, the two exterior cells use at most two new labels in either coordinate, and only equality or inequality with the selected row/column labels affects every signature. Consequently the uniform check may be performed on the compressed board

\[
\bigl(a+\min\{2,p-a\}\bigr)\ \times\ \bigl(b+\min\{2,q-b\}\bigr).
\]

This proves that checking all isomorphism types and all saturated availability categories is an exhaustive proof for **every** \(p,q\ge5\): it does not extrapolate from finitely many fixed board orders.

**3. Finite classification certificate.** The included standard-library program `verify.py` enumerates the 52-by-52 partition pairs, rejects coordinate collisions, and canonically reduces the 1,153 admissible pairs to exactly **34** distinct five-cell types. For each type, it enumerates all compressed exterior pairs and applies the complementary-signature equivalence. Checking \(p,q\in\{5,6,7\}\) covers all possibilities, because no pattern has more than five used labels per axis and all counts of unused labels are capped at two. Exactly nine types work when \(p=q=5\); the two whole-column types disappear when \(p>5\), the two whole-row types disappear when \(q>5\), and exactly the five core types remain for all \(p,q\ge6\). The 34 representatives, their automorphism orders, truth values, and explicit failing exterior pairs at \((5,5)\) appear in `PATTERNS.tsv`. Every line is reproducible from the program's finite logic. The complete list of nine surviving types is the table in the Finding section.

**4. Orbit counts.** For a pattern supported on \(a\) rows and \(b\) columns with \(h\) row/column-preserving automorphisms, its distinct placements in the labeled \(p\)-by-\(q\) board number \((p)_a(q)_b/h\). For the four three-by-three patterns the reciprocal automorphism orders sum to \(1/4+1/2+1/2+1=9/4\), giving the first term. The five-cell matching has automorphism order \(5!=120\), yielding the second term. If \(p=5\), a full column has \(q\) choices, while a four-plus-one column split has \(5q(q-1)\) choices; they contribute \(q(5q-4)\). The transposed patterns give \(p(5p-4)\) only when \(q=5\). These nine patterns are pairwise nonisomorphic with row and column roles fixed, so the counts add without duplication, proving the formula.

## Verification
Execute `python3 verify.py` in the directory containing this document and the attached checker. It establishes the unrestricted set-partition normal-form census, all nine saturated boundary cases, the exact stabilizer orders, and the equality between the orbit formula and the closed expression. It also performs a **separate direct enumeration** of every five-cell subset and the original pairwise-distance condition on the \(5\)-by-\(5\), \(5\)-by-\(6\), and \(6\)-by-\(6\) boards (8430, 17076, and 36720 valid sets). These direct enumerations are consistency checks; the proof of validity for every board size is the canonical-pattern reduction and exhaustive finite normal-form analysis.

## Relationship to prior work
González, Hernando, and Mora [1] introduced distance-equalizer sets (first public preprint 22 July 2021) and treated several graph families, not this minimum-basis census for two-factor Hamming graphs. Gispert-Fernández and Rodríguez-Velázquez [2] investigated the equidistant dimension of lexicographic products and complexity. Gispert-Fernández, Rodríguez-Velázquez, and Yero [3], in an openly accessible 2026 article, proved \(\xi(K_p\square K_q)=5\) for \(p,q\ge5\); its Section 2 establishes the minimum threshold and constructs a five-cell matching, but does not provide a complete basis classification or enumerator. The present result refines that already known optimum into an exhaustive nine-type classification and exact closed census; it does not claim the value five as original.

## Limitations
The theorem is limited to two-factor Hamming graphs with both factors of order at least five. It does not enumerate higher-cardinality distance-equalizer sets or bases in smaller boards. The finite normal-form proof depends on correctness of the included short exhaustive checker; its generation, compression justification, and an independent original-definition enumeration are supplied for inspection. Literature searches and inspected sources did not identify the stated classification, but absence from search results is not a mathematical proof of priority; unindexed or differently phrased results remain a possible overlap risk.

## References
[1] A. González, C. Hernando, M. Mora, *The Equidistant Dimension of Graphs*, arXiv:2107.10805, first posted 2021-07-22; *Bull. Malays. Math. Sci. Soc.* 45 (2022), 1757–1775, DOI:10.1007/s40840-022-01295-z. https://arxiv.org/abs/2107.10805

[2] A. Gispert-Fernández, J. A. Rodríguez-Velázquez, *The equidistant dimension of graphs: NP-completeness and the case of lexicographic product graphs*, *AIMS Mathematics* 9 (2024), 15325–15345, DOI:10.3934/math.2024744. https://www.aimspress.com/article/doi/10.3934/math.2024744

[3] A. Gispert-Fernández, J. A. Rodríguez-Velázquez, I. G. Yero, *Equidistant dimension of Cartesian product graphs*, *Bull. Malays. Math. Sci. Soc.* 49, article 101 (2026), first published 2026-04-20, DOI:10.1007/s40840-026-02088-4. https://link.springer.com/article/10.1007/s40840-026-02088-4
