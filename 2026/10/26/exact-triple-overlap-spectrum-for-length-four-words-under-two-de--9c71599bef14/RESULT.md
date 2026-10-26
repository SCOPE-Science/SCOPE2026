# Exact triple-overlap spectrum for length-four words under two deletions

## Finding

Let \(q\ge2\) be an integer, and let \(\Sigma_q\) be an alphabet of size \(q\). For a length-four word \(x=(x_1,x_2,x_3,x_4)\), its **exact-two-deletion shadow** is the *set* of distinct received pairs
\[
\mathcal D_2(x)=\{(x_i,x_j):1\le i<j\le4\}\subseteq\Sigma_q^2.
\]
For every unordered triple \(X=\{x,y,z\}\subseteq\Sigma_q^4\) of **three distinct centers**, let \(h(X)=|\mathcal D_2(x)\cap\mathcal D_2(y)\cap\mathcal D_2(z)|\). Define \(H_s(q)\) as the number of such triples with \(h(X)=s\).

**Theorem.** Write \((q)_{\underline k}=q(q-1)\cdots(q-k+1)\) for \(0\le k\le q\), and put \((q)_{\underline k}=0\) for \(k>q\). For \(1\le s\le4\),
\[
H_s(q)=\frac16\sum_{k=2}^{8}a_{k,s}(q)_{\underline k},
\]
where the exact integer coefficients are

| \(k\) | \(a_{k,1}\) | \(a_{k,2}\) | \(a_{k,3}\) | \(a_{k,4}\) |
|---:|---:|---:|---:|---:|
|2|672|432|132|12|
|3|28038|7200|1466|72|
|4|113890|11868|1936|18|
|5|114600|4304|688|0|
|6|39720|384|64|0|
|7|5184|0|0|0|
|8|216|0|0|0|

Moreover, \(H_0(q)=\binom{q^4}{3}-\sum_{s=1}^4H_s(q)\), and \(H_s(q)=0\) for every \(s\ge5\). In particular,
\[
\max_{|X|=3}h(X)=4,\qquad
H_4(q)=2(q)_{\underline2}+12(q)_{\underline3}+3(q)_{\underline4}.
\]
Every alphabet has a maximizing triple: over two distinct symbols named \(0,1\), the centers \(0101\), \(0110\), and \(1001\) have common shadow \(\{00,01,10,11\}\). Every maximizing triple uses at most four different alphabet symbols.

For the four-symbol alphabet, the full distribution \((H_0,H_1,H_2,H_3,H_4)\) is
\[
(2103072,569056,77136,13872,384),
\]
whose sum is \(\binom{4^4}{3}=2763520\).

## Assumptions and scope

The alphabet is labeled and has any fixed integer cardinality \(q\ge2\). Centers are ordered words of exactly four symbols; triples of centers are **unordered**, with all three centers pairwise distinct. The deletion channel removes **exactly two** positions and retains the order of the surviving pair. Identical outputs from different deletion positions are counted once. The overlap count is the cardinality of the intersection of three resulting *sets*. There is no distance requirement on the centers beyond distinctness.

## Proof

**Canonical reduction valid for every alphabet.** Concatenate an *ordered* triple \((x,y,z)\) into a twelve-position list. The equality relation on these twelve symbol positions uniquely determines whether its three four-position blocks are distinct and uniquely determines all ordered length-two subsequences of each block, up to one-to-one relabeling. The equality classes form a set partition of twelve labeled positions. Each such partition has precisely one **restricted-growth encoding** \(a_1,\ldots,a_{12}\): \(a_1=0\), and \(a_i\) is an integer between \(0\) and \(1+\max_{j<i}a_j\), inclusive. The number \(k\) of its classes is one plus the maximum encoded entry. Conversely, this recurrence generates every set partition exactly once. Hence the universal problem for *all* alphabet sizes reduces to a finite, exhaustive set of equality patterns, not to testing finitely many alphabet sizes.

**Exact exhaustive pattern count.** The accompanying standalone source `verification/enumerate.cpp` traverses the complete restricted-growth recursion on twelve positions; there are \(B_{12}=4213597\) patterns in all. It excludes a pattern precisely when two of its consecutive four-position blocks are equal, leaving \(4201207\) admissible patterns of ordered, pairwise-distinct center triples. For each remaining pattern, it sets one bit for each of the at most six index pairs \((i,j)\) with \(1\le i<j\le4\) in each word; pair \((a,b)\) has bit index \(12a+b\), with \(0\le a,b\le11\), in three 64-bit limbs. The bitwise intersection of the three masks contains exactly the common ordered length-two outputs; a bit population count therefore equals \(h(X)\), with no dependence on the labeling of alphabet symbols.

The exact \(k\)-by-overlap enumeration is the displayed coefficient table for positive overlap. For completeness, the zero-overlap counts for \(k=1,\ldots,12\) are
\[
(0,432,46864,478688,1256658,1282686,622128,158808,22275,1705,66,1).
\]
Every count at overlap at least five vanishes. The algorithm contains the full recursion, all counting rules, the expected full integer table, and consistency assertions; its finite state space has been justified by the canonical-partition correspondence. It thus constitutes an exhaustive computation of *every possible equality case* for arbitrary alphabets, rather than a numerical sample of four-letter words for a few \(q\).

**Transfer from equality patterns to every \(q\).** A canonical pattern with exactly \(k\) classes admits precisely \((q)_{\underline k}\) injective assignments of distinct labeled alphabet symbols to its classes, and none if \(k>q\). Thus the sum of its pattern counts weighted by \((q)_{\underline k}\) counts all **ordered** triples of distinct centers over \(\Sigma_q\). Each **unordered** triple has exactly six orders, so division by \(6\) proves the formulas for \(H_1,\ldots,H_4\). Every three-center set lies in one of these categories or has overlap zero, proving the stated expression for \(H_0\). The exhaustive absence of intersection sizes at least five gives the universal upper bound. The displayed binary witness supplies sharpness for all \(q\ge2\). Only the positive \(s=4\) entries with \(k\le4\) survive, which proves the extremizer population formula and the four-symbol support bound.

**Independent first-moment identity.** A fixed received pair \((a,b)\) occurs as a subsequence of exactly
\[
U_q=q^4-(q-1)^4-4(q-1)^3=1+4(q-1)+6(q-1)^2
\]
four-letter words: a word fails to contain \((a,b)\) exactly if its greedy scan never completes the two-symbol target, giving \((q-1)^4+4(q-1)^3\) failures. Counting each common received pair and the three centers containing it gives
\[
\sum_{s=0}^4 s H_s(q)=q^2\binom{U_q}{3}.
\]
The independently generated direct enumerations and this identity agree with the coefficient table. This is a cross-check of the enumeration; the canonical reduction and exhaustive table establish the theorem.

## Verification

From a clean directory containing `verification/enumerate.cpp` and `verification/direct_check.py`, run

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verification/enumerate.cpp -o enumerator
./enumerator
python3 verification/direct_check.py
```

The C++ checker exhausts all \(4213597\) partitions, checks the admissible count \(4201207\), compares every \(k,s\) cell (including all zero cells) against the recorded table, and checks the universal maximum four. The structurally separate Python checker constructs every actual shadow and exhausts all \(\binom{q^4}{3}\) unordered center triples for \(q\in\{2,3,4,5\}\). It additionally checks the first-moment and total-count identities for \(2\le q\le14\). Both reported `VERIFY_OK`; the recorded outputs are in `verification/check_output.txt`. The direct small-alphabet checks are corroboration only, not the proof for arbitrary \(q\).

## Relationship to prior work

Fengxing Zhu, *Sequence Reconstruction over the Deletion Channel* (initial public preprint 2025-11-02; revised 2026), proves the maximum intersection of at least three **binary** deletion balls for the admissible lengths; Section 4 explicitly poses the arbitrary-alphabet problem. In particular, the binary value four in the present parameters follows from that paper, and is **not** claimed as new. The contribution here is an exact all-alphabet, three-center, length-four/two-deletion theorem, with the complete overlap-population polynomials and sharp extremizer count.

Junnila, Laihonen and Lehtilä, *Levenshtein's Sequence Reconstruction Problem and Results for Larger Alphabet Sizes* (2025), investigate larger alphabets but focus their principal explicit intersection results on substitution/erasure/Hamming channels; their deletion discussion includes large-alphabet retrieval probabilities, not the present triple-shadow polynomial. Abu-Sini and Yaakobi (2024) study multiple deletion/insertion balls for binary inputs; the accessible abstract is binary-specific. Previously published exact one-deletion confusability-edge and binary multi-deletion pairwise results address different center counts or deletion radii, and do not imply the present all-alphabet distribution.

## Limitations

This theorem concerns only three distinct length-four centers and exactly two deletions, not arbitrary lengths, deletion counts or larger lists. The enumeration is mathematically exhaustive for its finite set of equality types, but it has not been independently audited. No claim is made about improved code redundancy, decoding algorithms or biological performance. Although inspected primary papers and searchable research records did not supply the same spectrum, equivalent coverage in unindexed literature remains possible; full text of one older binary-focused multiple-ball paper was not available for a conclusive whole-document comparison.

## References

1. F. Zhu, *Sequence Reconstruction over the Deletion Channel*, arXiv:2511.01071 (first public 2025-11-02), https://arxiv.org/html/2511.01071v3 (especially Theorem 1 and Section 4).
2. V. Junnila, T. Laihonen, T. Lehtilä, *Levenshtein's Sequence Reconstruction Problem and Results for Larger Alphabet Sizes*, arXiv:2504.13342 (2025), https://arxiv.org/html/2504.13342v1.
3. M. Abu-Sini and E. Yaakobi, *On the Intersection of Multiple Insertion (or Deletion) Balls and its Application to List Decoding Under the Reconstruction Model*, IEEE Transactions on Information Theory **70** (2024), 3262–3297, https://doi.org/10.1109/TIT.2023.3319608.
