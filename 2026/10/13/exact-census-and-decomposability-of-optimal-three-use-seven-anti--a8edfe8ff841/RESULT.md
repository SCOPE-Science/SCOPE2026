# Exact census and decomposability of optimal three-use seven-antihole codes
## Finding
Let \(H\) be the graph on \(\mathbb Z/7\mathbb Z\) in which distinct symbols are confusable precisely when their cyclic difference is \(\pm2\) or \(\pm3\). Thus \(H=\overline{C_7}\), which is isomorphic to the square \(C_7^2\) of the seven-cycle. A three-use zero-error code is a set \(C\subseteq(\mathbb Z/7\mathbb Z)^3\) such that any two distinct words differ by \(\pm1\) in at least one coordinate.

The maximum code size is \(8\), as previously established for \((C_7^2)^{\boxtimes3}\). The **complete equality census** comprises exactly
\[
N_3=1{,}640{,}384{,}809
\]
labeled optimal eight-word codes. Exactly \(35{,}329\) admit a one-coordinate/two-coordinate Cartesian product decomposition, and the remaining
\[
\boxed{1{,}640{,}349{,}480}
\]
are indecomposable across every such cut. Exactly \(343\) optima are full products of three one-use codes. Translation by \((\mathbb Z/7\mathbb Z)^3\) acts freely on the eight-word optima, yielding exactly \(4{,}782{,}463\) translation classes.

For a concrete indecomposable optimum, take the eight triples
\[
\begin{gathered}
(0,0,0),\ (0,2,1),\ (1,5,2),\ (2,3,1),\\
(3,3,1),\ (3,6,2),\ (4,6,2),\ (6,2,3).
\end{gathered}
\]

## Assumptions and scope
The alphabet and its cyclic ordering are fixed and labeled. An unordered set of codewords is counted once regardless of how its eight messages might be numbered. The confusability relation for one use includes a symbol paired with itself; two distinct symbols are confusable exactly at cyclic differences \(\pm2,\pm3\). In three independent uses, two distinct words are confusable exactly when all three coordinate pairs are confusable. They are therefore distinguishable exactly when some coordinate difference is \(\pm1\).

A code is *decomposable* if, after choosing one of the three coordinate positions, its word set can be written \(A\times B\), with \(A\subseteq\mathbb Z/7\mathbb Z\) and \(B\subseteq(\mathbb Z/7\mathbb Z)^2\). Coordinate order is preserved in this definition. A code is *fully Cartesian* if it is a product of three one-coordinate codeword sets. No linearity, affine structure, or group-invariance assumption is imposed.

## Proof
**Finite optimum and complete census.** Index the \(343\) words by their base-seven coordinate expansions. Form the graph \(G\) joining two words when some coordinate difference is \(\pm1\); the zero-error codes are exactly the cliques of \(G\). The accompanying `count_ordered.cpp` uses exact 343-vertex bit masks and an increasing-vertex recursion to visit each clique containing the all-zero word exactly once. It finds exactly \(38{,}259{,}704\) eight-cliques containing zero and no nine-clique containing zero. The separate `count_coloring.cpp` rebuilds the same adjacency from the complementary three-coordinate confusability criterion, and independently reproduces these counts using a greedy-coloring upper bound and reverse-color enumeration.

An explicit size-eight product code is \(\{0,1\}^3\). Translation of all symbols independently by any element of \((\mathbb Z/7\mathbb Z)^3\) preserves confusability and is transitive on the \(343\) words. If any nine-codeword zero-error code existed, translating one of its words to zero would produce a nine-clique containing zero, which the exhaustive recursions exclude. Thus the maximum size is \(8\), consistent with the previously known result.

Let \(R=38{,}259{,}704\) be the number of eight-cliques through zero. Counting pairs consisting of a labeled optimum and one distinguished codeword in that optimum gives \(8N_3=343R\), hence \(N_3=1{,}640{,}384{,}809\).

**Decomposition.** In one use, the largest zero-error code has size \(2\), and there are exactly \(7\) such codes: the seven adjacent residue pairs. In two uses, `verify_small.py` directly checks all \(\binom{49}{4}=211{,}876\) four-word subsets, finding exactly \(1{,}715\) valid codes of size \(4\), and an independent ascending-clique recursion excludes size \(5\). Thus the two-use optimum is \(4\).

If an eight-word three-use code factors across a designated one-versus-two coordinate cut, the factors must have sizes \(2\) and \(4\), since these are the respective optimal sizes. Conversely, any product of optimal one-use and two-use codes is optimal. For each of the three coordinate cuts there are therefore exactly
\[
7\cdot1715=12{,}005
\]
decomposable optima. A code that factors across two distinct one-versus-two cuts must factor across all three coordinates. Every one-dimensional factor must then be an adjacent residue pair; these fully Cartesian codes number \(7^3=343\), and they form every pairwise and triple intersection of the three cut-classes. Inclusion–exclusion gives
\[
3(7\cdot1715)-3(343)+343=35{,}329
\]
decomposable optima, leaving \(1{,}640{,}349{,}480\) indecomposable optima. Direct pairwise checks verify the displayed witness; each of its three coordinate projections has more than two symbols, preventing any optimal Cartesian decomposition.

**Translation classes.** A nonzero element of \((\mathbb Z/7\mathbb Z)^3\) has order \(7\), and its translation acts on the word space in seven-cycles. No eight-word subset can be fixed by such a translation. Thus the translation stabilizer of every optimum is trivial, all translation orbits have size \(343\), and the class count is \(N_3/343=4{,}782{,}463\).

## Verification
Run `sh reproduce.sh` using a C++17 compiler and Python 3; no nonstandard Python packages or external data are required. The two C++ implementations use different adjacency predicates and different exhaustive clique-recursion strategies. Both count eight- and nine-cliques containing zero. The Python verifier independently enumerates every two-use four-word candidate, excludes five-word two-use codes, checks both explicit three-use witnesses, and checks all integer formulas.

The final output line is:

`VERIFY_OK root8=38259704 root9=0 N3=1640384809 decomposable=35329 indecomposable=1640349480`

The complete machine output is included in `verification_output.txt`.

## Relationship to prior work
Jurkiewicz, Kubale, and Ocetkiewicz (2015) explicitly prove \(\alpha((C_7^2)^{\boxtimes3})=8\) and give one product-type eight-word witness (p. 140), so **the maximum size and existence of an optimum are prior work**. Their paper studies independence numbers and demonstrates one witness per reported parameter; its full text does not state the total number of optimal codes, the number of factorable codes, or the translation-orbit count. The present result addresses the stronger equality-layer questions, and in particular establishes that the overwhelming majority of optima do not factor as the previously displayed construction does.

Badalyan and Markosyan (2013) determine the independence number of strong products of two cycle-powers, providing the most relevant two-use background. Their accessible abstract and metadata establish that scope, while the present two-use count \(1{,}715\) is independently checked from definitions. The distinction between the original seven-cycle \(C_7\) and its complement \(\overline{C_7}\cong C_7^2\) is essential: existing exact censuses for zero-error codes on \(C_7\) concern a different confusability graph and do not imply this one.

## Limitations
All counts are exact for precisely the seven-symbol antihole channel and exactly three uses. The Cartesian-decomposition count is relative to one-coordinate versus two-coordinate cuts, not a classification under the full automorphism group. Translation equivalence alone is treated; coordinate permutations and graph-automorphism orbits are not enumerated. No result about asymptotic Shannon capacity or larger blocklengths is asserted. Although targeted searches and directly relevant full-text comparison uncovered no prior equality census, obscure or unindexed finite enumerations remain a possible originality risk. The 2013 two-factor paper was accessible here at abstract level only, so no full-document noncoverage claim is made for it.

## References
1. M. Jurkiewicz, M. Kubale, and K. Ocetkiewicz, “On the Independence Number of Some Strong Products of Cycle-Powers,” *Foundations of Computing and Decision Sciences* **40** (2015), 133–141, DOI: 10.1515/fcds-2015-0009. First verified public online date: 2015-05-16.
2. S. H. Badalyan and S. E. Markosyan, “On the Independence Number of the Strong Product of Cycle-Powers,” *Discrete Mathematics* **313** (2013), 105–110, DOI: 10.1016/j.disc.2012.09.008.
3. C. E. Shannon, “The Zero Error Capacity of a Noisy Channel,” *IRE Transactions on Information Theory* **2** (1956), 8–19.
