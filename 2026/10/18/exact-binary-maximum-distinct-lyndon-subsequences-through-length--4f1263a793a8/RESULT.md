# Exact binary maximum distinct Lyndon subsequences through length twenty

## Finding

Write \(\Sigma=\{0<1\}\). For a finite word \(w\in\Sigma^*\), let \(\mathcal L(w)\) consist of all **distinct**, **nonempty**, scattered subsequences that are Lyndon words. A nonempty word is Lyndon when it is strictly lexicographically smaller than each nonidentity cyclic rotation. Define
\[
D(n)=\max_{w\in\Sigma^n}|\mathcal L(w)|.
\]
For every integer \(1\le n\le20\), exhaustive classification yields
\[
\big(D(1),\ldots,D(20)\big)=
(1,3,4,6,8,13,18,28,41,63,96,141,225,335,538,803,1292,1941,3132,4701).
\]
The corresponding numbers of maximizers are
\[
(2,1,2,1,4,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1).
\]
Every maximizing word is listed in `data/maxima.tsv`; no equivalence under complement, reversal, or rotation is imposed. At length twenty the maximum is \(4701\) and the unique maximizer is `00010101010101101011`.

## Assumptions and scope

The alphabet is binary and ordered \(0<1\); Lyndon status depends on this order. Occurrences of the same subsequence at different sets of positions contribute **once**, not with multiplicity. The ambient objects are linear words, not cyclic words. Words with only one of the two symbols are included among candidates. Only integer lengths \(1\le n\le20\) are classified.

## Proof

**Lemma 1 (complete subsequence recursion).** Let \(E(w)\) be the set of distinct scattered subsequences of \(w\), including the empty word \(\varepsilon\). For \(c\in\Sigma\),
\[
E(\varepsilon)=\{\varepsilon\},\qquad
E(wc)=E(w)\cup\{uc:u\in E(w)\}.
\]
Indeed, a subsequence of \(wc\) either omits its last position or uses that position, in which case its preceding letters form a subsequence of \(w\). Both inclusions hold, and set union eliminates duplicate occurrences.

**Lemma 2 (collision-free encoding and test).** Assign \(h(\varepsilon)=1\) and \(h(uc)=2h(u)+c\), interpreting the letters as digits. Then \(h\) is injective on binary words and every word of length at most \(n\) has \(1\le h(u)<2^{n+1}\). For \(|u|=1\), the word is Lyndon. For \(|u|\ge2\), a word is Lyndon exactly when its binary integer encoding is strictly less than the encoding of every nontrivial cyclic rotation of the same length. Equal-length numeric and lexicographic comparisons agree; a periodic word fails the strict test.

**Exhaustive classification.** The standalone `verify/census.cpp` traverses the full binary word tree to depth twenty. At each node its `seen` array marks exactly the values \(h(u)\) for \(u\in E(w)\) and its list contains each marked value exactly once. Both invariants hold at the root, by Lemma 1 and the injective encoding. To extend by a letter, the algorithm scans the old list only, marks previously unmarked children \(2h(u)+c\), and increments its Lyndon count only for newly marked Lyndon words (Lemma 2). All newly added marks are undone on backtracking. Thus the stored count at every word-tree node equals \(|\mathcal L(w)|\), without undercounting or counting repeated occurrences.

The traversal branches on both letters at every level, so at depth \(n\) it examines each of the \(2^n\) distinct binary words exactly once, without pruning. It records the maximum, its number of ties, and every maximizing word for the data table. The loop bounds, recursion invariants, and complete branch coverage prove that the exhaustive finite output gives exact upper and lower bounds for all the stated lengths. The depth-twenty census visits \(1,048,576\) words at its final level. The expected values are asserted in the checker, so disagreement makes the program fail rather than silently printing a result.

## Verification

Compile `verify/census.cpp` with a standard C++17 compiler and run it with argument `20`. It returns `CENSUS_OK n=1..20` only when all maximum values, tie counts, and \(2^n\) depth counts agree. Compile `verify/independent.cpp` separately: it constructs all Lyndon candidates directly and uses a greedy next-occurrence automaton to test subsequence inclusion. That distinct algorithm exhaustively corroborates every word through length fifteen and checks the reported maximizing witnesses at lengths sixteen through twenty. The two packaged sources were compiled and executed before delivery. The exact maximizing-word table is `data/maxima.tsv`.

## Relationship to prior work

Hirakawa, Nakashima, Inenaga, and Takeda explicitly leave the maximum number of **distinct Lyndon subsequences** open (their \(\operatorname{MDS}(\sigma,n)\)), while computing the maximum number counted with multiplicity and expected counts. Their extremizer for the maximum total count differs already at length six: `000111` has eleven distinct Lyndon subsequences, whereas `001011` has thirteen. The later algorithms of Bannai and collaborators compute a **longest** Lyndon subsequence, not the count of all distinct Lyndon subsequences. The OEIS entry A290743 concerns **contiguous Lyndon factors** and therefore solves a different invariant. These results do not imply the present exact finite maxima or optimizer lists.

## Limitations

This is a complete, computationally proved **finite** classification through length twenty, not a formula for arbitrary lengths. The census, whose invariant and coverage are proved above, is the exhaustive part of the argument; the independent checker for longer lengths corroborates winners but does not independently prove maximality there. The first-public priority of these exact finite figures has not been independently certified; an unindexed equivalent table may exist. No conjectured extension beyond length twenty is asserted.

## References

1. R. Hirakawa, Y. Nakashima, S. Inenaga, M. Takeda, *Counting Lyndon Subsequences*, arXiv:2106.01190, version 1 publicly released 2021-06-02. See the maximum-distinct entry in Table 2 and Section 3. https://arxiv.org/abs/2106.01190
2. H. Bannai, T. I., T. Kociumaka, D. Köppl, S. J. Puglisi, *Computing Longest Lyndon Subsequences and Longest Common Lyndon Subsequences*, Algorithmica 86 (2024), 735–756, first published online 2023-05-06, doi:10.1007/s00453-023-01125-z. https://doi.org/10.1007/s00453-023-01125-z
3. OEIS A290743, *Maximum number of distinct Lyndon factors ... binary*, a comparison for contiguous factors only. https://oeis.org/A290743
