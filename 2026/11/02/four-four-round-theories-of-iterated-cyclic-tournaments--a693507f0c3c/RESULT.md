# Four four-round theories of iterated cyclic tournaments

## Finding
Let \(C\) be the directed three-cycle with arcs \(0\to1\), \(1\to2\), and \(2\to0\). Define \(T_1=C\) and \(T_{h+1}=C[T_h]\), the lexicographic tournament product, for every integer \(h\ge1\). In the pure first-order language with equality and the directed arc predicate (no additional constants or predicates), the exact rank-four equivalence relation is
\[
T_h\equiv_4 T_j\quad\Longleftrightarrow\quad \min(h,4)=\min(j,4),\qquad h,j\ge1.
\]
Thus the family has exactly four rank-four theories, with representatives \(T_1,T_2,T_3,T_4\) on \(3,9,27,81\) vertices respectively. The maximum minimum representative size within this family is sharply \(81\). The result is not an assertion about quantifier ranks greater than four.

## Assumptions and scope
An arc \(x\to y\) is an irreflexive binary relation; for any distinct vertices exactly one orientation holds. A vertex of \(T_h\) is a word \((a_1,\ldots,a_h)\in\{0,1,2\}^h\). For distinct words \(a,b\), let \(\lambda(a,b)\) be their first unequal coordinate. Then \(a\to b\) holds iff \(b_{\lambda(a,b)}-a_{\lambda(a,b)}\equiv1\pmod3\). The lexicographic product \(H[G]\) has vertex set \(V(H)\times V(G)\), with arcs between different first coordinates governed by \(H\) and within a first-coordinate block by \(G\). Ordinary quantifier rank counts the maximum nesting of first-order quantifiers. No cardinality/counting quantifiers or named decomposition levels are admitted.

## Proof
**Lemma 1 (lexicographic congruence).** For any fixed finite tournament \(H\) and tournaments \(G,G'\), if \(G\equiv_qG'\), then \(H[G]\equiv_qH[G']\) for each nonnegative integer \(q\). In the \(q\)-round Ehrenfeucht--Fraisse game, match the same \(H\)-block on both sides. Within every block, Duplicator plays a separate winning \(q\)-round strategy for \(G,G'\), even if fewer than \(q\) selections occur in that block. Equality and within-block arcs are preserved by the local strategies; cross-block arcs depend only on the matched \(H\)-indices. This is a winning global strategy.

**Lemma 2 (complete ordered tuple-orbit invariant).** For each ordered tuple \(\mathbf v=(v_1,\ldots,v_r)\) of vertices of \(T_h\), including tuples with repetitions, record for each pair of positions whether their vertices are equal; otherwise record their first differing coordinate and which of the two possible arc directions occurs there. Two such tuples have the same record if and only if a tournament automorphism built from independent cyclic digit rotations at every ternary-prefix node sends one ordered tuple to the other. The forward direction holds since each rotation preserves cyclic differences. Conversely, the pair records determine, at each prefix, how the selected positions are distributed among its at most three children and the cyclic order of occupied children. Their digit labels therefore agree up to a cyclic rotation; recursively choose an independent rotation at each occupied prefix. These choices map the tuples exactly. In particular, one representative of each record suffices for computing all one-point extensions.

**Lemma 3 (exact finite rank-four certificate).** For \(h=1,2,3,4,5\), enumerate every ordered-tuple orbit of length \(0\le r\le4\) by Lemma 2. Let \(D_r\) be the atomic equality/arc diagram of a tuple, and recursively define its remaining-round type by \(S_4=D_4\) and
\[
S_r(\mathbf v)=\bigl(D_r(\mathbf v),\{S_{r+1}(\mathbf v,w):w\in V(T_h)\}\bigr)\quad(0\le r<4).
\]
The braces denote a set, not a multiset: ordinary first-order logic tests existence of extension types, not their multiplicity directly. Induction on the remaining number of rounds proves that equality of these types is exactly Duplicator's ability to preserve the selected tuple for the remaining rounds. Exhaustive integer enumeration yields, for tuple lengths \(r=0,1,2,3,4\), respectively:

| \(h\) | \(r=0\) | \(r=1\) | \(r=2\) | \(r=3\) | \(r=4\) | Rank-four theory |
|---|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 3 | 9 | 27 | I |
| 2 | 1 | 1 | 5 | 29 | 189 | II |
| 3 | 1 | 1 | 7 | 61 | 631 | III |
| 4 | 1 | 1 | 9 | 105 | 1497 | IV |
| 5 | 1 | 1 | 11 | 161 | 2931 | IV |

The four root types for \(h=1,2,3,4\) are pairwise distinct, while the root type at \(h=5\) is identical to the root type at \(h=4\). The exact independent scripts and their finite output tables are supplied in the verification package. The first program uses first-difference-depth/direction matrices; the second program independently canonicalizes recursively rotated ternary tries. Each independently obtains the partition \(\{1\},\{2\},\{3\},\{4,5\}\), and their tuple-orbit counts agree. This finite computation is exhaustive by Lemma 2, not a sample of configurations.

**Conclusion.** Lemma 3 gives \(T_4\equiv_4T_5\). Applying Lemma 1 with \(H=C\) repeatedly gives \(T_{h}\equiv_4T_{h+1}\) for every \(h\ge4\), hence all \(T_h\) with \(h\ge4\) are rank-four equivalent. Lemma 3 also proves pairwise inequivalence of \(T_1,T_2,T_3,T_4\). The asserted four classes and sharp representative bound follow.

## Verification
From the package directory, execute `python3 verify/pair_matrix_types.py` and `python3 verify/trie_orbits.py 4 5`. The first prints `FOUR_RANK4_CLASSES_AND_PUMPING_BASE_OK`, with class representatives `{1:1, 2:2, 3:3, 4:4, 5:4}`. The second independently prints the same five representatives and the same ordered-tuple orbit counts. Compare the supplied `verify/pair_matrix_types.txt` and `verify/trie_orbits.txt`. Both programs use exact integer and tuple/set operations, and both were executed on the actual packaged source paths. The infinite conclusion relies on Lemma 1, not on extrapolation from calculations at finitely many heights.

## Relationship to prior work
The 2006 paper by Bouchalaa and Boudabbous develops lexicographic sums of tournaments under a directed three-cycle and studies self-duality/reconstruction, not quantifier-rank equivalence of their iterates. The survey of Pikhurko and Verbitsky (first public preprint 2010) provides finite-model-theoretic logical-depth and Ehrenfeucht--Fraisse background but no classification of this tournament tower was identified in inspected sections. Earlier published work on graph logical complexity concerns different graph families and is used only for methods. Related current literature on lexicographic tournament flag complexes concerns topological invariants rather than first-order four-round theories. The finite-basis congruence plus exact cutoff is the new claim; general EF and lexicographic-product facts are not asserted as new.

## Limitations
Only the pure directed adjacency/equality language and exactly four rounds are classified. The bound \(81\) is sharp among representatives from this tower, not among all tournaments. The scientific comparison is not exhaustive across unpublished or unindexed results; some primary literature was inspected only in relevant sections. The computational finite certificate and mathematical pumping lemma have received self-review only; no independent mathematical validation has occurred.

## References
1. H. Bouchalaa and Y. Boudabbous, *La {-k}-autodualite des sommes lexicographiques finies de tournois suivant un 3-cycle ou un tournoi critique*, Ars Combinatoria 81 (2006), 33--64, public article dated 2006-10-31, https://combinatorialpress.com/article/ars/Volume%20081/vol-081-paper%202A.pdf.
2. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, first public arXiv version 2010-03-25, arXiv:1003.4865; Contemporary Mathematics 558 (2011), 129--180.
3. T. Bohman, A. Frieze, T. Luczak, O. Pikhurko, C. Smyth, J. Spencer, and O. Verbitsky, *First-Order Definability of Trees and Sparse Random Graphs*, Combinatorics, Probability and Computing 16 (2007), 375--400, DOI:10.1017/S0963548306008376.
