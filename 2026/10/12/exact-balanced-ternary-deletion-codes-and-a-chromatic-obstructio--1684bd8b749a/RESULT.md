# Exact balanced ternary deletion codes and a chromatic obstruction

## Finding
Let \(X\) be the set of length-six words over \(\{0,1,2\}\) containing exactly two occurrences of each symbol. Join two different words when they have a common length-five subsequence obtained by deleting one coordinate, and denote the resulting *single-deletion confusability graph* by \(G\). Then
\[
 |X|=90,\qquad \alpha(G)=18,\qquad \omega(G)=5,\qquad \chi(G)=6.
\]
Exactly **eight** subsets of \(X\) attain the independent-set maximum of \(18\). All eight have the same twelve words and are obtained by three independent binary choices of two-word blocks, displayed below. Thus every two maximum codes intersect in at least twelve words, and a maximum code cannot be one color class in a five-color partition of \(X\).

## Assumptions and scope
The alphabet consists of *three distinct labeled symbols*, written `0`, `1`, `2`; coordinates are ordered, and codeword sets are not identified under any symmetry. A code \(C\subseteq X\) corrects one deletion precisely when its single-deletion output sets
\[
 D(w)=\{w_1\cdots w_{i-1}w_{i+1}\cdots w_6:1\leq i\leq 6\}
\]
are pairwise disjoint. A received output is the length-five word, without its deletion position. The theorem concerns precisely the composition \((2,2,2)\), not unrestricted ternary codes or other block lengths. The independence number, clique number and chromatic number are those of the described confusability graph, not of its complement.

The twelve universal core words are

`001122 002211 010212 020121 101202 110022 112200 121020 202101 212010 220011 221100`.

For each row of the following table choose **either** the first block **or** the second block, and adjoin all six chosen words to the common core. The three choices are independent; the eight combinations are all the maximum codes.

| Choice | First two-word block | Second two-word block |
|:--|:--|:--|
| A | `012210 102201` | `012201 102210` |
| B | `021120 201102` | `021102 201120` |
| C | `120012 210021` | `120021 210012` |

## Proof
**Upper bound by a deletion-output transversal.** Consider the following eighteen length-five words:

`00112 00221 01012 01120 02021 02210 10012 10120 11022 11200 12102 12201 20021 20210 21102 21201 22011 22100`.

Call this set \(T\). For **every** \(w\in X\), the set \(D(w)\cap T\) has cardinality exactly one. This is a finite identity, checked for all ninety words by the independent enumeration in the attached `verify.py`. One can reproduce it directly by generating all permutations of `001122` and their six deletions. Moreover, every \(t\in T\) has exactly five distinct superwords in \(X\). Therefore these five superwords form a clique in \(G\), and the eighteen cliques partition \(X\). A deletion-correcting code contains at most one word from each clique, whence \(\alpha(G)\leq18\).

**Complete equality classification.** For a code of size eighteen, exactly one word must be chosen from each of the eighteen five-element sets \(\{w\in X:t\in D(w)\}\). The attached self-contained `verify.py` enumerates all such selections. At each recursive node it chooses an unfilled group with the fewest candidates still compatible with previously chosen words, then recursively examines **every** available candidate; a branch is pruned only if some group is empty. Compatibility is recomputed from the six literal deletions of each word. This finite exhaustive proof visits 368 recursive nodes and yields exactly eight independent sets of size eighteen. Comparing these eight sets with the displayed core and blocks establishes that they are exactly the eight claimed constructions. Direct pairwise checks show that every displayed set is deletion-correcting. Together with the transversal bound, this proves \(\alpha(G)=18\) and the complete classification.

**Coloring obstruction.** Suppose \(G\) had a proper coloring with five colors. The five parent words of each \(t\in T\) are mutually adjacent, so each such clique would use each color once. As the eighteen cliques partition the vertices, every color class would contain exactly eighteen words. But each of the eight maximum independent sets contains the same twelve-word core. Two disjoint color classes could not both contain this core. Thus \(\chi(G)\geq6\).

To attain six colors, assign to each word the *descent syndrome*
\[
 s(w)=\sum_{i=1}^{5}i\,\mathbf{1}\{w_i>w_{i+1}\}\pmod 6.
\]
The verifier tests all confusable pairs of the ninety words and finds none with equal syndrome; hence this is a proper six-coloring, proving \(\chi(G)=6\). Its color-class sizes are \(16,14,16,14,16,14\), in residue order. This is a finite exhaustive verification of the fixed-length claim and does not assert a new general decoding theorem.

Finally, the verifier enumerates every maximal clique of the confusability graph by Bron--Kerbosch recursion: 272 maximal cliques occur, of which 96 have size five and none is larger. The five-parent cliques already give \(\omega(G)\geq5\); the enumeration gives \(\omega(G)\leq5\).

## Verification
Run `python3 verify.py` using Python 3.10 or later and the standard library only. No network, solver, published code, or external data file is required. The script checks the exact input and output sets, the eighteen-output transversal and five-parent partition, enumerates *all* eighteen-code candidates, compares their precise core-and-block classification, verifies the six-color descent syndrome on every confusable pair, and enumerates all maximal cliques. Expected last line:

`VERIFY_OK inputs=90 outputs=90 transversal=18 max_code=18 max_code_sets=8 common_core=12 search_nodes=368 clique_max=5 clique5=96 maximal_cliques=272 chromatic=6`

The optional JSON file `CODEBOOKS.json` is a machine-readable statement of the eight solutions; the program independently reconstructs all eight without reading it. Exhaustiveness follows from the loop bounds over all \(3^6\) words restricted by the composition condition and from the full branch coverage of the eighteen independent choices of five candidates; no random trials, timeouts, or solver statuses are used as proof.

## Relationship to prior work
Cullina, Kulkarni and Kiyavash (arXiv:1211.4056v1, 2012) formulate the single-deletion confusability graph and prove optimal colorings for **binary constant-weight** layers. Their theorem does not imply the ternary constant-composition equality classification, and the present \(\chi(G)=6>\omega(G)=5\) shows that analogous minimum-clique-size coloring can fail in this nonbinary layer. Cullina and Kiyavash (arXiv:1302.6562v1, 2013) establish general-alphabet deletion-code bounds, not the eight equality cases or this chromatic separation. Cullina's 2014 master's thesis, publicly deposited in January 2015, treats constant-composition codes and is a particularly relevant source; only its bibliographic record and abstract were accessible for review. The thesis's uninspected details remain an originality risk, rather than evidence of noncoverage. The known nonbinary descent-syndrome coding method motivates the upper six-color bound; the exact equality census and impossibility of five colors are the claimed contribution.

## Limitations
All results concern one precisely specified finite graph of ninety vertices and make no assertion about general ternary block lengths, other symbol multiplicities, nonlinear capacity asymptotics, or optimality under a different channel model. No claim is made that a failed literature search proves global novelty. The 2014 thesis full text was not inspected because the repository PDF could not be retrieved; its contents, as well as unindexed earlier classifications, remain residual originality risks. The verification is an explicit finite proof whose correctness requires scrutiny of the embedded enumeration, not an independent external audit.

## References
1. Daniel Cullina, Ankur A. Kulkarni and Negar Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056v1, 2012-11-16. https://arxiv.org/abs/1211.4056
2. Daniel Cullina and Negar Kiyavash, *An Improvement to Levenshtein's Upper Bound on the Cardinality of Deletion Correcting Codes*, arXiv:1302.6562v1, 2013-02-26. https://arxiv.org/abs/1302.6562
3. Daniel Cullina, *Constant Composition Deletion Correcting Codes*, Master's thesis, University of Illinois, 2014; repository issue date 2015-01-21. https://hdl.handle.net/2142/72914
4. G. Tenengolts, *Nonbinary codes, correcting single deletion or insertion*, IEEE Transactions on Information Theory 30 (1984), 766--769.
