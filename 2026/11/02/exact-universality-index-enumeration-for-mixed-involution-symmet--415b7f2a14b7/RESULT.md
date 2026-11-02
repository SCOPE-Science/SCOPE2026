# Exact universality-index enumeration for mixed-involution symmetric words

## Finding

Let \(\Sigma\) be a labeled alphabet with \(q=f+2d\) letters, where \(f\ge1\) and \(d\ge1\) are integers. Let \(\pi:\Sigma\to\Sigma\) be an involution with exactly \(f\) fixed letters and \(d\) two-element orbits, and put \(\theta(w)=\pi(w^{\mathrm R})\). The map \(\pi\) acts letterwise and \(w^{\mathrm R}\) means reversal. A word \(w\) is \(\theta\)-symmetric when \(\theta(w)=w\). Define \(\iota(w)\) to be the largest nonnegative integer \(k\) for which every word in \(\Sigma^k\) occurs as an order-preserving, not necessarily contiguous subsequence of \(w\).

Set \(B_0(y)=1\), and, for all integers \(j\ge1\), set
\[
B_j(y)=\frac{j!y^j}{\prod_{i=1}^{j}(1-iy)},\qquad A(y)=qy B_{q-1}(y),\qquad R(y)=\sum_{j=0}^{q-1}\binom qj B_j(y).
\]
Define the two explicit correction series
\[
E(y)=\sum_{r=0}^{d-1}\binom dr2^{d-r}B_{f+d+r}(y)
\]
and
\[
O(y)=\sum_{r=0}^{d}\binom dr2^{d-r}B_{f-1+d+r}(y)
+\sum_{r=0}^{d-1}\binom dr2^{d-r}B_{f+d+r}(y).
\]
Then the complete bivariate ordinary generating function for **indexed linear words**, with no quotient by rotation or relabeling, is
\[
\boxed{\sum_{\substack{n\ge0\\k\ge0}}\#\{w\in\Sigma^n:\theta(w)=w,\ \iota(w)=k\}\,z^nu^k
=\frac{(1+fz)R(z^2)+(u-1)\bigl(E(z^2)+fzO(z^2)\bigr)}{1-u^2A(z^2)}.}
\]
All equalities are identities of formal power series with integer coefficients. In particular, for every positive integer \(k\), the minimum length \(L_k\) of a \(\theta\)-symmetric \(k\)-universal word and the number \(M_k\) of such minimum-length indexed words are
\[
\boxed{L_{2m}=2mq,\quad M_{2m}=(q!)^m\quad(m\ge1)}
\]
and
\[
\boxed{L_{2m+1}=(2m+1)q+f-1,\quad
M_{2m+1}=(q!)^m f\,2^d(d+f-1)!\quad(m\ge0).}
\]
The last two identities are consequences of the complete generating function, not separate conjectures.

## Assumptions and scope

The alphabet is finite, labeled, and of cardinality at least three. The involution contains **both** at least one fixed letter and at least one transposed pair; the result makes no new claim for either endpoint type \(f=0\) or \(d=0\). All words are finite and indexed; the empty word is included in the bivariate generating function with universality index zero. Subsequence occurrences need not be contiguous, and repeated embeddings do not change the universality index. The alphabet, the involution, and all integer parameters are held fixed when extracting coefficients.

## Proof

**1. Greedy arches.** Repeatedly remove the shortest nonempty prefix containing every letter of \(\Sigma\), until the remaining suffix omits at least one letter. Denote the complete prefixes by \(C_1,\ldots,C_t\) and the proper-support remainder by \(S\). This decomposition is unique. The universality index is exactly \(t\): each complete alphabet block can supply the next prescribed subsequence letter, while the sequence consisting of the terminal new letter of each \(C_i\), followed by a letter missing from \(S\), cannot be a scattered subsequence. Its absence also prevents universality at larger lengths.

Every complete greedy arch ends with a letter that was absent from the preceding part of that arch. For a specified length \(\ell\), its first \(\ell-1\) positions must use exactly \(q-1\) letters and its final position must be the single missing letter. The generating function of surjective words onto any specified set of \(j\) labeled letters is \(B_j(y)\), by the classical Stirling-number identity. Therefore one arch has length generating function \(A(y)=qyB_{q-1}(y)\), and all proper-support remainders have length generating function \(R(y)\). A half-word having exactly \(t\) complete arches has generating function \(A(y)^tR(y)\).

**2. Symmetric-midpoint lemma.** Write an arbitrary \(\theta\)-symmetric word as \(H\theta(H)\) if its length is even or as \(Hc\theta(H)\) if its length is odd, in which case \(c\) must be a fixed letter of \(\pi\). Write the greedy arch decomposition of \(H\) as \(C_1\cdots C_tS\). Its reflected suffix has the corresponding \(t\) complete alphabet blocks. The universality index of the whole word is either \(2t\) or \(2t+1\). Indeed, \(2t\) complete blocks are immediately present. If \(2t+2\) complete blocks existed, the first \(t+1\) blocks from the left and the last \(t+1\) from the right would have to be disjoint. But the greedily shortest first \(t+1\) blocks and the greedily shortest last \(t+1\) blocks both cross the midpoint, a contradiction. For \(2t+1\) blocks, the first \(t\) and last \(t\) greedy blocks leave a central segment which must contain the whole alphabet; conversely a complete central segment supplies the extra block. Thus the additional unit occurs precisely when
\[
\operatorname{alph}(S)\cup\pi(\operatorname{alph}(S))=\Sigma
\]
for even length, and when
\[
\operatorname{alph}(S)\cup\pi(\operatorname{alph}(S))\cup\{c\}=\Sigma
\]
for odd length.

**3. Even central-support count.** Let \(T=\operatorname{alph}(S)\) be a proper subset. To satisfy \(T\cup\pi(T)=\Sigma\), all \(f\) fixed letters must belong to \(T\), and each transposed pair must contribute at least one letter. If exactly \(r\) of the \(d\) pairs contribute both letters, there are \(\binom dr2^{d-r}\) choices of \(T\), of cardinality \(f+d+r\). Since \(T\) is proper, \(r\le d-1\). Summing the corresponding exact-support word series gives \(E(y)\).

**4. Odd central-support count.** Fix a center letter \(c\) among the \(f\) fixed letters. Now the support must contain all fixed letters other than \(c\), and at least one letter of every transposed pair. If \(c\notin T\), all \(0\le r\le d\) are allowed and \(|T|=f-1+d+r\). If \(c\in T\), propriety requires \(0\le r\le d-1\) and \(|T|=f+d+r\). This yields exactly \(O(y)\), independently of the selected fixed center.

**5. Summation.** For each integer \(t\ge0\), a half-word with \(t\) arches contributes \(u^{2t}A(y)^t(R(y)-E(y))\) or \(u^{2t+1}A(y)^tE(y)\) in the even case, with \(y=z^2\). In the odd case replace \(E\) by \(O\) and multiply by \(fz\). Summing the geometric series \(\sum_{t\ge0}u^{2t}A(y)^t\) proves the boxed generating-function identity.

**6. Extremal coefficients.** Each arch has minimum length \(q\) and exactly \(q!\) realizations at that length. For even universality index \(2m\), the empty remainder gives the unique lowest-degree contribution, at length \(2mq\), with coefficient \((q!)^m\). For odd index \(2m+1\), the smallest central support occurs with an odd fixed center and a remainder missing that center but containing every other fixed letter and one member of every transposed pair. Its minimum half-length is \(f+d-1\); it contributes \(f2^d(f+d-1)!\) choices. After \(m\) full arches on each side, this gives length \((2m+1)q+f-1\) and the stated coefficient. The shortest even-centered alternative is one symbol longer. This establishes both minimum-length identities.

## Verification

The self-contained Python scripts `verify_mixed_gf.py` and `verify_symmetry.py` use exact integer arithmetic and no third-party packages. The first independently expands the enumerator by support sizes and arch convolutions, and compares every coefficient through lengths 8–12 against exhaustive enumeration of actual \(\theta\)-symmetric words for six mixed involution types. The second exhaustively verifies the minimum lengths and counts, including all shorter lengths, for a broader selection of small alphabets and universality targets. Both return `VERIFY_OK`. The formal proof above covers every allowed alphabet and length; exhaustive checks alone would not establish the infinite assertion.

For example, when \(f=2\) and \(d=1\), so \(q=4\), one obtains \(E(y)=2B_3(y)\) and \(O(y)=2B_2(y)+3B_3(y)\). The shortest one-universal symmetric words have length \(5\), and there are exactly \(8\); the shortest three-universal ones have length \(13\), and there are exactly \(192\).

## Relationship to prior work

Barker, Fleischmann, Harwardt, Manea and Nowotka (2020), especially their arch-factorization results and Proposition 15, characterize universality in ordinary palindromes; their discussion also covers letter permutations of words. Adamson (2023) gives algorithms for counting and ranking unrestricted subsequence-universal words. Mahalingam, Maity and Pandoh (2022) study Watson–Crick involutions and palindrome behavior among conjugates. These are important adjacent results, but do not state the mixed-orbit bivariate distribution with simultaneous fixed letters and transposed pairs proved here.

The two pure orbit types—ordinary reversal (all letters fixed) and a fixed-point-free reverse-complement involution—have related exact universality enumerations. They are not claimed as new cases of this result. The mixed type requires both the even support condition \(E\) and the two distinct odd-center conditions in \(O\); neither endpoint specialization alone gives these mixed coefficients.

## Limitations

The theorem concerns formal subsequence universality, not deletion-channel correction, contiguous factor universality, or the physical stability of nucleic-acid sequences. It does not count equivalence classes under alphabet relabeling or rotation. Its originality is asserted relative to the specific sources and records inspected, not as a proof that no equivalent formula exists in all literature. The proof and computational checks have not undergone independent external validation.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629, first public version March 10, 2020, https://arxiv.org/abs/2003.04629.
2. D. Adamson, *Ranking and Unranking k-Subsequence Universal Words*, arXiv:2304.04583, April 10, 2023, https://arxiv.org/abs/2304.04583.
3. K. Mahalingam, A. Maity, and P. Pandoh, *Counting (Watson-Crick) palindromes in Watson-Crick conjugates*, Information and Computation 285 (2022), article 104863, https://doi.org/10.1016/j.ic.2021.104863.
