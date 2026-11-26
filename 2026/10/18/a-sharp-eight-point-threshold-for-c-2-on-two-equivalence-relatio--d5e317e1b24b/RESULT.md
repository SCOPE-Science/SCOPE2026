# A sharp eight-point threshold for \(C^2\) on two equivalence relations

## Finding

Among finite nonempty structures with two named equivalences, all isomorphism types on at most seven elements are distinguished by two-variable first-order logic with counting, \(C^2\). At eight elements, the full family has 3,017 isomorphism types but 3,016 \(C^2\)-classes. Just one class contains more than one isomorphism type. Its members have bipartite incidence graphs \(C_8\) and \(C_4\sqcup C_4\), with named sides. In particular the least cardinality of a collision in the full family is eight. The contribution is the unrestricted census and exclusion of all other collisions through eight, not the isolated construction of the two-matching witness.

## Assumptions and scope

The signature consists of two separately named equivalence relations \(E,F\) and no other predicates. The relations may coincide or overlap; isomorphisms may not exchange their names. \(C^2\) uses equality and arbitrary counting quantifiers with two reusable variables. Comparison is within the finite class in which both relations are equivalences. A different cardinality is distinguished by a counting sentence, so the exclusion below eight also applies when the comparator is not assumed to have the same order. Allowing an empty structure would not affect the first collision.

Use a matrix \(M=(|R_i\cap S_j|)_{ij}\), where \(R_i\) runs through the \(E\)-classes and \(S_j\) through the \(F\)-classes. Its entries are nonnegative integers, its rows and columns are nonzero, and its total weight is the cardinality. Isomorphism is exactly independent row and column permutation. Equivalently an element is an incidence edge joining its two classes; an intersection of size greater than one gives parallel edges.

## Proof

**Exhaustive generation.** Start at \((1)\). Adjoining a point increments any existing cell, adds a unit in a new row and existing column, adds a unit in an existing row and new column, or creates a new row and column intersecting in a single unit. Removing a point and discarding any resulting zero row or column reverses one of these operations. Thus the recursion reaches all isomorphism types. For canonicalization, first impose ascending column-sum order, then consider the permutations within each equal-sum group, and for each such column order sort the rows lexicographically. The least outcome in that family is invariant and can only agree for matrices in the same orbit.

**Logical equivalence test.** Start with one color and refine a point by its old color and the number of points of each old color in each of the four \((E(x,y),F(x,y))\) channels. To recover the separate equality channel, remove one point of the current color from the \((1,1)\) channel and assign it to \(y=x\). All names for refined colors are synchronized across the compared structures. Each refined color is definable by a unary counting formula: conjoin its previous color formula with the exact counts for all previous color and relation channels. Conversely, an induction on formulas bounds the necessary refinement depth. At a given depth a formula evaluated on a pair depends only on its atomic pair type (with equality) and the colors of its two endpoints; binding either endpoint is evaluated by counting those types and endpoint colors while retaining the other endpoint. Thus at stabilization the multiset determines all counting sentences, and a difference of multisets is detected by counting one definable color. Refinement only splits color classes, so the synchronized procedure terminates for a finite census.

**Full census.** The exact counts are:

| Cardinality | Isomorphism types | \(C^2\)-classes | Non-singleton \(C^2\)-classes |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 0 |
| 2 | 4 | 4 | 0 |
| 3 | 10 | 10 | 0 |
| 4 | 33 | 33 | 0 |
| 5 | 91 | 91 | 0 |
| 6 | 298 | 298 | 0 |
| 7 | 910 | 910 | 0 |
| 8 | 3017 | 3016 | 1 |

The two members of the last non-singleton class are the intersection matrices
\[
\begin{pmatrix}0&0&1&1\\0&0&1&1\\1&1&0&0\\1&1&0&0\end{pmatrix},\qquad
\begin{pmatrix}0&0&1&1\\0&1&0&1\\1&0&1&0\\1&1&0&0\end{pmatrix}.
\]
They are not isomorphic: their incidence graphs have respectively two components and one. Both have the uniform channel profile \((1,1,1,5)\) in the channel order \((1,1),(1,0),(0,1),(0,0)\). Hence the indistinguishability of the explicit pair also follows directly, without the census. The census proves that this pair is the only collision at eight and that there are none at smaller orders; these conclusions range over all the matrices, not just the matrices with row and column sums two and entries at most one.

## Verification

Run `python3 verify.py` with the Python standard library. It generates the matrix families, refines all isomorphism types at each cardinality with synchronized colors, asserts the exact cardinalities and witness matrices, and ends with `VERIFIED: full sharp C2 threshold and unique first pair`. It also cross-checks the first five isomorphism counts by explicitly generating pairs of set partitions. The independent mathematical grounds for exhaustiveness, the orbit selector and the logical test are given above; equality of printed totals alone would not certify the classification.

## Relationship to prior work

OEIS A007716 records the isomorphism-count column; it counts matrix orbits modulo independent row and column permutations after padding with zero rows and columns. That column and the intersection-matrix interpretation are background, not a claim of a new enumeration formula.

The related Resultary record [4] treats structures in which both equivalences partition into pairs and their intersection is equality. It shows that the subfamily at a given size is a whole \(C^2\)-class even in the full family, and describes its isomorphism types by the lengths of alternating cycles. Its eight-point case supplies exactly the two members of the class used here. It does not exclude collisions wholly among structures outside that fibre at eight or among nonmatching structures at lower orders. No relative publication priority is inferred from the two records' shared catalog date.

Kiefer, Schweitzer and Selman [1, Theorem 27 and Corollary 29] give a structural characterization and an identification algorithm in a broader finite relational setting; this is background, not a new general characterization here. Pratt-Hartmann [2] addresses satisfiability in a much broader setting. Neither the orbit-count data nor the general algorithm provides the unrestricted order-eight logical census as table data.

## Limitations

The result is finite and restricted to two named equivalences without additional predicates. The computation is not a classification at higher orders or in stronger logics. Requiring the incidence graph to be connected would exclude one witness. Historical priority beyond the related record and consulted literature is not certified.

## References

1. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1, https://arxiv.org/abs/1503.08792.
2. I. Pratt-Hartmann, *The two-variable fragment with counting and equivalence*, *Mathematical Logic Quarterly* **61** (2015), 474–515, DOI:10.1002/malq.201400102.
3. OEIS A007716, https://oeis.org/A007716.
4. *The complete two-matching counting-logic fibre and its sharp first orbit split*, Resultary record f8a1b71171f2, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-the-complete-two-matching-counting-logic-fibre-and-its-sharp-fir--f8a1b71171f2.
