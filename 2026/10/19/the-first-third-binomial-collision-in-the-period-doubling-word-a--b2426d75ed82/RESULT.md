# The first third-binomial collision in the period-doubling word and its dyadic propagation

## Finding
Let \(p=\lim_{r\to\infty}\sigma^r(0)\) be the period-doubling word for the binary substitution \(\sigma(0)=01\), \(\sigma(1)=00\). Write \(L_n(p)\) for its distinct length-\(n\) contiguous factors, let \(P(n)=|L_n(p)|\), and let \(B_3(n)\) count classes under equality of every scattered-subsequence multiplicity for patterns of lengths one, two, or three.

**Theorem.** All distinct factors of \(p\) of length less than ten are distinguishable by these multiplicities. At length ten the sixteen distinct factors form exactly fifteen classes, with the unique nonsingleton class
\[
\{0101010001,\;1000101010\}.
\]
Thus the exact first failure of third-binomial reconstruction of period-doubling factors occurs at length ten. In addition, for every integer \(r\ge0\), the two distinct factors
\[
\sigma^r(0101010001),\qquad \sigma^r(1000101010)
\]
have the same scattered-subsequence multiplicities for all patterns of length at most three. Consequently,
\[
B_3(10\cdot2^r)<P(10\cdot2^r)\qquad(r\ge0).
\]
The seed factors are distinguished at order four; for example their counts of the scattered pattern \(0001\) are respectively \(21\) and \(15\).

## Assumptions and scope
A factor is a contiguous finite word occurring in the one-sided infinite fixed point \(p\). A scattered occurrence of \(v=v_1\dots v_j\) in \(w=w_1\dots w_n\) is a tuple of positions \(1\le i_1<\cdots<i_j\le n\) with \(w_{i_s}=v_s\). Write \(\binom{w}{v}\) for the number of these occurrences. Third-binomial equivalence means equality of \(\binom{w}{v}\) for all nonempty binary patterns \(v\) of length at most three. This result concerns ordinary, ungapped subsequences, not positional or minimum-gap statistics.

The finite boundary assertion covers all positive lengths \(1\le n\le10\) exactly. The infinite assertion covers the specific unbounded length family \(10\cdot2^r\); it does not determine \(B_3(n)\) at all lengths, the size of the deficit at later lengths, or whether four-binomial complexity always equals factor complexity.

## Proof
**1. Exhaustive finite-factor reduction.** Each substituted letter \(\sigma^4(a)\) has length sixteen. Because the two possible substitution images begin with zero, no factor \(11\) can occur in \(p\); the two-letter factors \(00,01,10\) all occur, as is seen already in \(\sigma^3(0)=01000101\). Partition \(p=\sigma^4(p)\) into aligned length-sixteen image blocks. Any factor of length at most ten intersects at most two consecutive image blocks. Conversely, each of the three possible ordered adjacent block pairs occurs. Therefore the following finite set is **exactly** the complete factor set, not an approximation from a long prefix:
\[
L_n(p)=\left\{\sigma^4(ab)[i:i+n]:ab\in\{00,01,10\},\ 0\le i<16\right\},\quad1\le n\le10,
\]
where the slice notation takes the consecutive positions with zero-based offsets. Each source block \(\sigma^4(ab)\) has length thirty-two, so every displayed slice is defined. Duplicate slices are counted once.

**2. Third-binomial finite certificate.** For each word \(w\), define its signature by the ordered fourteen counts
\[
S_3(w)=\bigl(\binom{w}{0},\binom{w}{1};\binom{w}{00},\binom{w}{01},\binom{w}{10},\binom{w}{11};\binom{w}{000},\binom{w}{001},\binom{w}{010},\binom{w}{011},\binom{w}{100},\binom{w}{101},\binom{w}{110},\binom{w}{111}\bigr).
\]
The exact finite reduction from step 1, together with the recurrence
\[
\binom{wc}{v}=\binom{w}{v}+\mathbf1_{\{v\text{ ends in }c\}}\binom{w}{v\text{ with last symbol removed}},
\]
gives the exhaustive counts below. (The empty pattern has count one.)

| Length \(n\) | \(P(n)\) | \(B_3(n)\) |
|---:|---:|---:|
| 1 | 2 | 2 |
| 2 | 3 | 3 |
| 3 | 5 | 5 |
| 4 | 6 | 6 |
| 5 | 8 | 8 |
| 6 | 10 | 10 |
| 7 | 11 | 11 |
| 8 | 12 | 12 |
| 9 | 14 | 14 |
| 10 | 16 | 15 |

At length ten the entire factor list, in lexicographic order, is:

`0001000100`, `0001000101`, `0001010100`, `0010001000`, `0010001010`, `0010101000`, `0100010001`, `0100010101`, `0101000100`, `0101000101`, `0101010001`, `1000100010`, `1000101010`, `1010001000`, `1010001010`, `1010100010`.

Among these sixteen factors, the only two with identical third-order signatures are \(u=0101010001\) and \(v=1000101010\), and their common signature in the ordering above is
\[
(6,4;15,12,12,6;20,19,22,10,19,16,10,4).
\]
The factors \(u\) and \(v\) occur in \(\sigma^4(00)=01000101010001000100010101000100\) at offsets four and one, respectively. To distinguish them at order four, direct application of the same recurrence gives \(\binom{u}{0001}=21\) and \(\binom{v}{0001}=15\).

**3. Stability under morphisms.** If finite words \(u,v\) are \(k\)-binomially equivalent and \(h\) is any monoid morphism, then \(h(u),h(v)\) are also \(k\)-binomially equivalent. Indeed, to select \(j\le k\) positions in the image \(h(w)\), group the selected positions by their parent source-letter blocks. If \(t\) distinct blocks are used, \(1\le t\le j\), their ordered source letters form a pattern of length \(t\). For fixed target pattern, its occurrence count is a fixed integer linear combination of the source counts \(\binom{w}{x}\) over patterns of length \(t\le j\): the coefficient enumerates choices within the chosen image blocks. The coefficients depend only on \(h\) and the target pattern, not on \(w\). This proves preservation.

Apply this principle repeatedly with \(h=\sigma\) and the pair \(u,v\). Each image remains a factor because \(p=\sigma^r(p)\), and the images are distinct since \(\sigma\) is an injective uniform substitution (the distinct two-letter blocks \(01\) and \(00\) uniquely decode its inputs). Their lengths are \(10\cdot2^r\), so two different factors occupy one third-binomial equivalence class at every stated length. This proves the infinite claim.

## Verification
The companion `verify.py` uses only Python's standard library. It constructs precisely the three two-block images from step 1, enumerates all possible start offsets, and computes signatures by a descending-length subsequence-count recurrence. It reproduces the factor and class counts for every length one through ten, identifies the unique collision, checks an independently generated long morphic prefix for agreement of factor sets, and tests the two iterated witnesses through the fourth iterate. Run with `python3 verify.py`; it prints `ALL CHECKS PASSED` upon success. The proof of complete finite coverage and of unlimited dyadic propagation appears above; finite iteration tests are only corroboration.

## Relationship to prior work
Rigo, Stipulanti and Whiteland (first publicly posted 2022-01-12) discuss the period-doubling word explicitly. They cite Lejeune for its second-binomial behavior and report that **computer experiments** show a strict gap between third-binomial and factor complexity, while suggesting equality at order four. The present theorem gives the exact earliest length, the unique collision at that length, and a proof of infinitely many dyadic gaps; it does not claim the general strictness observation as a new empirical discovery. Existing formulas for the Thue–Morse word concern a different substitution and do not by themselves imply this period-doubling factor classification.

## Limitations
The classification is exact through length ten only. The infinite obstruction establishes strict inequality at specified lengths without a general formula for the third-binomial complexity. The 2021 thesis of Lejeune, cited for the second-binomial result, could not be fully inspected; an unlocated equivalent seed construction remains a literature risk.

## References
- M. Rigo, M. Stipulanti, M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603 (first posted 2022-01-12), especially Section 7 on the period-doubling word, https://arxiv.org/abs/2201.04603 .
- M. Lejeune, *On the k-binomial equivalence of finite words and their applications*, doctoral thesis, Université de Liège (2021), http://hdl.handle.net/2268/259266 (full text not inspected).
- M. Lejeune, J. Leroy, M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word*, Journal of Combinatorial Theory, Series A 176 (2020), 105284, DOI:10.1016/j.jcta.2020.105284 (related substitution, different fixed point).
