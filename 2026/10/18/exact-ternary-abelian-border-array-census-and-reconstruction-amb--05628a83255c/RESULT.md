# Exact ternary abelian-border-array census and reconstruction ambiguity

## Finding

Let \(\Sigma=\{0,1,2\}\). For a word \(w=w_1\cdots w_n\), let \(\pi(w)=(b_1,\ldots,b_n)\), where \(b_i\) is the greatest \(k\) with \(1\leq k<i\) for which the length-\(k\) prefix and suffix of \(w_1\cdots w_i\) have equal Parikh vectors; put \(b_i=0\) if no such \(k\) exists. Let \(T_3(n)\) count the distinct arrays \(\pi(w)\) for \(w\in\Sigma^n\). A *canonical generator* is the unique representative of a word under a global permutation of its alphabet, obtained by relabeling symbols \(0,1,2\) in order of first appearance.

**Exact census and ambiguity claim.** For every \(1\leq n\leq16\), the exact \(T_3(n)\) values, in increasing order of \(n\), are

\[
1,2,4,9,20,49,119,308,795,2170,5904,16702,47014,136189,391967,1151825.
\]

The attached `census_table.csv` gives, for each of these lengths, the number of distinct arrays, the total number of canonical generators, the number of arrays with one canonical generator, and the greatest canonical-generator multiplicity. The attached `ambiguity_histogram_n16.csv` is the **complete** exact distribution of canonical-generator multiplicities at \(n=16\), comprising \(353\) nonzero frequency levels. In particular, exactly \(468549\) arrays have one canonical generator; the \(1151825\) arrays have altogether \(7174454\) canonical generators.

For every \(n\geq2\), among labeled ternary words the unique largest fiber of \(\pi\) is the all-zero array and consists of exactly \(3\cdot2^{n-1}\) words. For every \(n\geq3\), the same array is also the unique largest fiber **modulo global alphabet permutations**, with exactly \(2^{n-2}\) canonical generators. At \(n=2\), two arrays tie for the largest canonical-generator fiber, though only the all-zero array is maximal among labeled words.

## Assumptions and scope

The alphabet has exactly three available symbols, but the words themselves may use one, two, or three symbols. Borders are proper and nonempty, and abelian equality requires identical counts of **each** symbol. The census concerns all prefixes of each finite word simultaneously, not just the longest border of the completed word. The finite numeric claims are restricted to lengths at most sixteen; the extremal-fiber assertions hold for all indicated lengths.

Canonical generators are restricted-growth words: the first symbol is \(0\), and each later symbol is at most one greater than the largest preceding symbol and at most \(2\). The order of letters, not just their total frequencies, matters. The histogram entries are numbers of *arrays*, classified by how many such canonical generators yield them; they are not counts of words modulo cyclic rotation or reversal.

## Proof

**Reduction to restricted-growth words.** A global permutation of the alphabet leaves every Parikh-vector equality, and therefore \(\pi(w)\), unchanged. Recording each distinct letter at its first appearance as \(0,1,2\) produces a unique restricted-growth representative. Conversely, all restricted-growth words arise, and no two represent the same global-relabelling class. Thus computing \(\pi\) on the complete restricted-growth set is an exhaustive computation of \(T_3(n)\) and its canonical-generator fiber distribution.

**Exact evaluation of a prefix entry.** Let \(P_i(a)\) count occurrences of letter \(a\) in the first \(i\) symbols. For \(1\leq k<i\), a length-\(k\) abelian border exists precisely when

\[
P_k(a)=P_i(a)-P_{i-k}(a)\quad\text{for every }a\in\{0,1,2\}.
\]

In `verify_canonical.cpp` the search from \(k=i-1\) down to \(1\) returns the greatest qualifying length, or zero. Recursive branching visits **each** canonical generator once and records its complete array. Since \(0\leq b_i\leq i-1\leq15\) in the enumerated range, four binary bits per entry give an injective sixty-four-bit encoding: \(\sum_{i=1}^n b_i2^{4(i-1)}\). Accordingly, the integer frequency map represents precisely the fibers of \(\pi\); its map size gives \(T_3(n)\), and its frequency histogram gives the claimed counts. Exhaustiveness and the entry test are independent of the values obtained.

**Independent enumeration.** `verify_labeled.cpp` instead branches over *every* ternary word with first symbol \(0\), always checking candidate border lengths in increasing order; it never imposes restricted-growth conditions. A nonconstant global-relabeling class contributes exactly two words with first symbol \(0\), corresponding to the two permutations of the remaining alphabet symbols. The sole all-constant class contributes one. Moreover, only an all-constant word can produce the array \((0,1,\ldots,n-1)\). Thus the second program converts its word frequencies to canonical-generator frequencies by division by two, with the all-constant exception, and computes the same full table and length-sixteen histogram. Byte-for-byte equality of the two independently generated outputs was checked. The histogram also satisfies

\[
\sum_{r\geq1} h_{16}(r)=1151825,\qquad
\sum_{r\geq1}r\,h_{16}(r)=7174454.
\]

The latter is the number of restricted-growth ternary words of length sixteen, namely \((3^{15}+1)/2\).

**Maximum-fiber theorem.** For any word and \(i\geq2\), the equality \(b_i=i-1\) holds exactly when \(w_i=w_1\), since a proper border of length \(i-1\) compares the word after dropping its last symbol with the word after dropping its first symbol. It follows that \(\pi(w)\) is all zero precisely when the first symbol never appears later: if it does recur, a prefix has an abelian border of length one; if it does not, every proper suffix omits a symbol present in every nonempty prefix, ruling out all positive abelian borders. There are \(3\) choices for the first symbol and \(2^{n-1}\) choices for the remainder, proving the all-zero labeled-fiber size. Every other array forces at least one later position to equal the first symbol, hence has at most \(3\cdot2^{n-2}\) labeled generators and cannot tie. Under relabeling, the all-zero words give exactly \(2^{n-2}\) representatives for \(n\geq2\); any other array with a later first-symbol occurrence has at most \(2^{n-3}\) representatives if some other symbol occurs, and the all-constant array has just one. This proves uniqueness for \(n\geq3\).

## Verification

The two independent C++17 implementations are `verify_canonical.cpp` and `verify_labeled.cpp`. Compile them separately with a conforming C++17 compiler and run each with two output path arguments, for example `./verify_canonical census.csv hist.csv`. Compare their complete CSV outputs to `census_table.csv` and `ambiguity_histogram_n16.csv`. No randomness, solver, unpublished data, or nonstandard library is needed. The programs completed and their CSV files matched byte-for-byte.

The distribution has \(353\) nonzero frequency levels, a unique largest canonical fiber of size \(16384\), and \(468549\) singleton canonical fibers. The whole-table SHA-256 is `6215d30bd35dcae5938041065415935b02c0b8cf7c98e70f4e4ea4365ced4b69`; the histogram SHA-256 is `6cd4f6d044008762b8bba80e45ad656d7de02b9eb3d5c2539fe64348157ed3b1`. These are exact decoded file hashes, not estimates of experimental error. The C++ enumeration is a finite proof, not evidence of any unspecified asymptotic law.

## Relationship to prior work

Habib, Shamil, and Rahman determine the exact binary array count \(2^{n-1}\) and give for ternary words the upper bound \(T_3(n)\leq (3^{n-1}+1)/2\), but no exact ternary census or full inverse-fiber distribution. In particular, at length sixteen the bound is \(7174454\), while the computed exact count is \(1151825\). These two quantities are conceptually distinct: the former is the number of letter-relabelling types and the latter is the number of different border arrays that those types realize.

Blanchet-Sadri, Chen, and Hawes, and earlier Christodoulakis and coauthors, study counting **binary words** by abelian-border features such as a shortest border, rather than counting distinct complete all-prefix arrays of ternary words. Their statistics do not imply the present exact ternary sequence or length-sixteen ambiguity histogram. The present result concerns exact finite enumeration and worst-case inverse ambiguity, not a new general algorithm for determining whether an arbitrary proposed array is realizable.

## Limitations

The exact ternary array counts and histogram are proved only through length sixteen. There is no asserted closed formula, recurrence, growth rate, or characterization of all ternary arrays for arbitrary length. The maximum-fiber statement is infinite in scope, but does not determine typical-fiber behavior for unbounded length. The study has not received an independent external audit. Unindexed equivalent enumerations remain a literature risk.

## References

1. M. Habib, M. S. Shamil, and M. S. Rahman, *Counting and Verifying Abelian Border Arrays of Binary Words*, arXiv:2111.00259 (first posted 2021-10-30), especially Sections 3–4. https://arxiv.org/abs/2111.00259
2. F. Blanchet-Sadri, K. Chen, and K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, arXiv:1708.06461 (first posted 2017-08-22). https://arxiv.org/abs/1708.06461
3. M. Christodoulakis, M. Christou, M. Crochemore, and C. S. Iliopoulos, *Abelian borders in binary words*, Discrete Applied Mathematics 171 (2014), 141–146. https://doi.org/10.1016/j.dam.2014.02.012
