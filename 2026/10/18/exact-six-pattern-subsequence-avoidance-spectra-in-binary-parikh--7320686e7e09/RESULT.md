# Exact six-pattern subsequence avoidance spectra in binary Parikh-matrix classes

## Finding

Fix an ordered alphabet \(\{a,b\}\). Let \(A\) count \(a\)'s, \(B\) count \(b\)'s, and let \(K\) count order-preserving (scattered) subsequences \(ab\). A *Parikh-matrix class* here is precisely the set of all words with the same triple \((A,B,K)\). For a pattern \(P\), let \(N_P(A,B,K)\) be the number of members of the class for which \(P\) **does not** appear as a scattered subsequence.

For all integers \(A,B\ge1\), \(0\le K\le AB\), define
\[
F_{A,B}(K)=
\begin{cases}
1,&K=0,\\
\#\{j\in\{1,\ldots,A\}:j\mid K,\ 1\le K/j\le B\},&K>0,
\end{cases}
\]
and
\[
G_{A,B}(K)=\mathbf{1}_{0\le K\le B}
+\#\{(i,r)\in\mathbb Z^2:0\le i<B,\ 1\le r<A,\ B-i+r=K\}.
\]
Then the **complete spectrum for all six patterns with two occurrences of each letter** is
\[
\begin{array}{c|cccccc}
P&abab&baba&aabb&bbaa&abba&baab\\\hline
N_P(A,B,K)&F_{A,B}(K)&F_{A,B}(AB-K)&G_{A,B}(K)&G_{A,B}(AB-K)&1&1.
\end{array}
\]
If \(A=0\) or \(B=0\), the only possible \(K\) is zero and there is one word; it avoids all six patterns. When \(A,B\ge1\), every value \(0\le K\le AB\) defines a nonempty class.

In particular, the exact conditional probability of avoiding any one of these patterns in a uniformly sampled Parikh-matrix class is
\[
\Pr(P\npreceq W\mid A,B,K)
=\frac{N_P(A,B,K)}{[z^K]\begin{bmatrix} A+B\\ A\end{bmatrix}_z},
\]
where the Gaussian coefficient is the ordinary generating polynomial for binary words by their \(ab\)-subsequence count, and \(\preceq\) denotes scattered-subsequence containment.

## Assumptions and scope

All words are *linear*, finite, and over a two-letter alphabet. Occurrences are scattered (not necessarily contiguous). A pattern is present when at least one choice of strictly increasing positions reads that pattern. The patterns exhaust the six permutations of the multiset \(\{a,a,b,b\}\). The displayed formula is simultaneous for every admissible positive \(A,B\) and every admissible \(K\), without asymptotic or independence assumptions.

## Proof

**The \(abab\) count.** A word contains \(abab\) as a scattered subsequence if and only if its maximal constant-letter run sequence has at least four runs beginning with \(a\), or at least five beginning with \(b\). Thus an avoiding word has the unique form \(b^u a^j b^k a^v\), allowing zero-length outside runs; when \(K>0\), precisely the \(a\)-run before the internal \(b\)-run and the internal \(b\)-run must be nonempty. Therefore it can be written uniquely
\[
W=b^{B-k}a^j b^k a^{A-j},\qquad 1\le j\le A,\quad1\le k\le B.
\]
The only \(ab\) pairs have their \(a\) in the left \(a\)-run and their \(b\) in the subsequent \(b\)-run, so \(K=jk\). The number of such words is \(F_{A,B}(K)\) for \(K>0\). If \(K=0\), the unique word is \(b^B a^A\). This proves \(N_{abab}=F_{A,B}(K)\).

**The \(aabb\) count.** A word avoids \(aabb\) precisely if, after its *second* occurrence of \(a\), at most one \(b\) remains; if \(A=1\), the pattern is automatically absent. In the zero-remaining-\(b\) case, every word uniquely has the form
\[
W=b^i a b^{B-i}a^{A-1},\qquad 0\le i\le B,
\]
with \(K=B-i\). In the one-remaining-\(b\) case, every word uniquely has the form
\[
W=b^i a b^{B-i-1}a^r b a^{A-r-1},\qquad
0\le i<B,\quad1\le r<A.
\]
The first \(a\) precedes the \(B-i-1\) interior \(b\)'s and the final \(b\), while the subsequent \(r\) \(a\)'s precede that final \(b\). Thus \(K=B-i+r\). These cases are disjoint and exhaust all avoiding words. The formula is \(G_{A,B}(K)\).

**The \(abba\) count.** Avoidance means there are at most one \(b\) strictly between the first and last \(a\) (when \(A=1\), this is automatic). With no such \(b\), the word is \(b^i a^A b^{B-i}\), giving \(K=A(B-i)\). With one such \(b\), it is uniquely
\[
W=b^i a^j b a^{A-j} b^{B-i-1},\qquad
0\le i<B,\ 1\le j<A,
\]
with \(K=A(B-i-1)+j\). Division of \(K\) by \(A\) selects exactly one of these cases and exactly one word for each \(0\le K\le AB\), so \(N_{abba}=1\). This normal-form conclusion also follows from the earlier binary-amiable canonical representative construction of Atanasiu; it is included to make the six-pattern classification self-contained, not claimed as independently new.

**Symmetries.** Reversal sends \(K\) to \(AB-K\) while fixing \(A,B\), interchanging \(abab\leftrightarrow baba\) and \(aabb\leftrightarrow bbaa\). Swapping \(a\leftrightarrow b\) interchanges \(abba\leftrightarrow baab\), changes \((A,B,K)\) to \((B,A,AB-K)\), and preserves the constant count one. Therefore the other three formulas follow.

**Denominator.** Encode a word by the weakly decreasing sequence of counts of \(b\)'s to the right of its successive \(a\)'s. This is a partition in an \(A\)-by-\(B\) rectangle, and its area is exactly the number \(K\) of scattered \(ab\)'s. Hence \([z^K]\begin{bmatrix}A+B\\A\end{bmatrix}_z\) counts the full class. Every integer \(K\) in the stated range occurs, so the ratio is defined.

## Verification

`checker.py` supplies two independent finite checks. One directly enumerates words and greedily recognizes scattered patterns. Another propagates exact integer weights through a subsequence-prefix automaton, with state \((\text{used }a,\text{used }b,\text{count }ab,\text{matched-prefix length})\). Both are independently compared to the stated arithmetic expressions. `checks.txt` records 67,500 dynamic-programming-versus-formula cells at \(0\le A,B\le14\) and 4,758 direct-enumeration-versus-DP cells for \(A+B\le11\); all pass. Those finite tests corroborate but do not establish the universal theorem: the preceding run decomposition is its proof.

To replay with Python 3, place `checker.py` and `checks.txt` alongside this document and run `python3 checker.py`; its output should match `checks.txt`.

## Relationship to prior work

Fazekas, Huang and Mercaş (2026) study exactly these binary Parikh-matrix classes and give exact conditions for subsequence universality and an additive approximation scheme for occurrence probabilities of fixed scattered patterns. The present classification supplies exact arithmetic numerators for the natural six length-four patterns with balanced letter multiplicities; it does not assert any general algorithm for arbitrary patterns. The complete full text of that particularly relevant work was not obtained, so potential overlap in individual cases remains a documented risk.

Golafshan (2026), especially Corollary 5 of Section 5.2, gives the Gaussian-binomial denominator and class-size distribution. Its class-size theorem does not select or count the members avoiding a specified length-four scattered pattern. Atanasiu's *Binary Amiable Words* (2007), Theorem 5 and its normal-form construction, already provides a unique representative of a shape equivalent to the \(abba\)-avoiding normal form. Thus the unit \(abba\) and \(baab\) cases are not asserted to be independently novel. The new contribution assessed here is the joint **exact avoidance spectrum**, notably the bounded-divisor \(abab\) cases and additive-window \(aabb\) cases, for the entire natural six-pattern family and every fixed \(K\).

## Limitations

No statement is made about patterns with unequal letter multiplicities, larger alphabets, or any length-four pattern involving three or more copies of one letter. The probability formula is conditional on an exact Parikh-matrix class, not a uniform distribution over all words of a given length. The target 2026 paper's full text was inaccessible through attempted legal sources; its abstract and publication metadata were inspected, but that is not a full-text exclusion of overlap. Existing literature might contain equivalent expressions under partition terminology or in unindexed sources. Independent scientific validation has not been performed.

## References

1. S. Z. Fazekas, X. Huang, and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, Electronic Proceedings in Theoretical Computer Science 451 (2026), 140–154, DOI:10.4204/EPTCS.451.10; arXiv:2610.06717. The proceedings metadata reports public publication on 2026-08-25.
2. M. Golafshan, *Binary binomial equivalence via hyperplane arrangements*, arXiv:2606.23426 (first posted 2026-06-22), especially Sections 1 and 5.
3. A. Atanasiu, *Binary Amiable Words*, 2007, especially Theorem 5 and the canonical representative argument. An accessible text is available at https://paperzz.com/doc/8039966/january-26--2007-8-31-wspc-instruction-file-amiabile.
4. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, Theoretical Computer Science 1066 (2026), 115732, DOI:10.1016/j.tcs.2025.115732.
