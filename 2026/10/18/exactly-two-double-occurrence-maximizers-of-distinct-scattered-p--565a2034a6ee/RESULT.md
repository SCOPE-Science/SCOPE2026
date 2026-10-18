# Exactly two double-occurrence maximizers of distinct scattered palindromes

## Finding

Let \(q\ge 2\), and let \(\Sigma=\{a_1,\ldots,a_q\}\) consist of \(q\) distinct labeled letters. Among length-\(2q\) words in which every letter occurs exactly twice, the maximum number of **distinct nonempty palindromic subsequence values** is \(2^{q+1}-2\). Exactly \(2q!\) labeled words attain this bound: after renaming letters in their order of first appearance, they are precisely
\[
 U_q=a_1a_2\cdots a_q\,a_q a_{q-1}\cdots a_1,
 \qquad
 V_q=a_1a_2\cdots a_q\,a_{q-1}a_q a_{q-2}\cdots a_1.
\]
For \(q=2\), the suffix \(a_{q-2}\cdots a_1\) is empty. The unique \(q=1\) word is \(a_1a_1\), with two palindromic subsequences. For \(q\ge2\), exactly \(q!\) maximizing words are palindromes (type \(U_q\)); the remaining \(q!\) are nonpalindromes (type \(V_q\)).

There is also an exact length-spectrum refinement. Write \(N_j(w)\) for the number of distinct palindromic subsequence values of length \(j\). For \(1\le k\le q\),
\[
 N_{2k-1}(U_q)=N_{2k}(U_q)=\binom qk,
\]
\[
 N_{2k-1}(V_q)=\binom qk+\binom{q-2}{k-2},\qquad
 N_{2k}(V_q)=\binom qk-\binom{q-2}{k-2},
\]
where \(\binom{q-2}{k-2}=0\) when \(k<2\). Every other positive length has zero count. Thus the two extremal forms have equal totals but different odd/even spectra.

## Assumptions and scope

A subsequence is obtained by selecting increasing positions; two selected position sets producing the same letter sequence count **once**, not twice. Every alphabet symbol occurs exactly twice in the host word. The theorem concerns **all integers** \(q\ge2\), rather than a finite search. The initial upper bound \(2^{q+1}-2\) was established more generally in the cited 2021 source, including words not required to have two occurrences of every symbol. The new assertion here is the complete equality classification in the balanced double-occurrence class and the parity-resolved spectrum.

For a symbol \(x\), call the interval between its first and second occurrences \(I_x=[\ell_x,r_x]\). These endpoints are distinct across different symbols.

## Proof

**Lemma 1 (two palindromes per support).** For every nonempty symbol set \(S\subseteq\Sigma\), at most two distinct palindromic subsequences have set of occurring symbols exactly \(S\).

Indeed, in such a palindrome every symbol other than a possible center occurs twice, and so uses both of its positions. When two distinct symbols \(x,y\) both occur in mirrored pairs, their intervals must be strictly nested, because their four occurrences appear in the order \(x,y,y,x\) or \(y,x,x,y\). Consequently, an even palindrome with support \(S\) requires all \(I_x\), \(x\in S\), to form a nested chain, and its letter sequence is then uniquely forced. When this chain exists, the only possible center of an odd palindrome is its innermost letter (both occurrences of every other letter are outside the innermost interval). Hence there are at most one even and one odd palindrome.

If the chain does not exist, no even palindrome is possible. For any prescribed odd central symbol \(c\in S\), the other intervals must form a nested chain, which uniquely fixes the palindrome. There cannot be three different admissible central symbols: if \(c,d,e\) were three, then for **any** pair \(x,y\in S\), one of \(c,d,e\) is distinct from both. The palindrome centered at that third symbol would force \(I_x\) and \(I_y\) to be nested. Thus all pairs of intervals would be nested, contradicting the assumption that the chain does not exist. There are at most two odd palindromes. This proves the lemma.

Summing Lemma 1 over the \(2^q-1\) nonempty supports yields the bound \(2^{q+1}-2\). The word \(U_q\) attains it: for each nonempty support \(S\), the interval pairs are nested and give exactly one even palindrome and the odd palindrome whose center is the innermost letter.

**Lemma 2 (first and second halves).** Suppose a double-occurrence word \(w\) attains the bound. Equality in Lemma 1 must hold separately for every nonempty support. For any two distinct letters \(x,y\), disjoint intervals \(I_x,I_y\) would permit no palindrome containing both letters: one of the letters would need to occur as a mirrored pair around an occurrence of the other, or the two pairs would need to nest. Both are impossible for disjoint intervals. Thus every pair of intervals intersects strictly. Intervals on a line have the pairwise-intersection property, so \(\max_x\ell_x<\min_x r_x\). Therefore the first \(q\) positions are all first occurrences, and the last \(q\) positions all second occurrences. Relabeling by first appearance gives \(w=a_1\cdots a_q\,a_{\pi(1)}\cdots a_{\pi(q)}\) for a permutation \(\pi\).

**Lemma 3 (two possible permutation tails).** Equality for full support \(S=\Sigma\) gives two palindromes using all symbols. An even palindrome on full support uses every position of \(w\), so its existence means that \(w\) itself is a palindrome. This forces the tail to be \(a_q a_{q-1}\cdots a_1\), namely \(U_q\).

Otherwise both full-support palindromes are odd, with distinct central symbols \(c,d\). When the center is \(c\), the other \(q-1\) symbols must have their second occurrences in precisely the reverse order of their first occurrences; the same holds with \(d\) as center. Consequently, every pair of symbols except possibly \(\{c,d\}\) is in reverse order in the second half. If \(c,d\) were also reversed, then the entire tail would be reversed and the even full-support palindrome would exist. Hence \(c,d\) occur in the **same** relative order in both halves. They must be adjacent in first-appearance order: a symbol strictly between them would have to occur after the larger and before the smaller in the second half, contradicting their shared order.

Moreover, their adjacent pair must be \(\{a_{q-1},a_q\}\). Otherwise the letter \(a_q\) lies later than each of \(c,d\) in the first half and earlier than each in the second half. The whole interval of \(a_q\) would then be strictly inside both center candidates' intervals. Neither occurrence of either candidate could lie between the two occurrences of \(a_q\), even though \(a_q\) is a mirrored pair in both odd full-support palindromes. This is impossible. Thus \(\{c,d\}=\{a_{q-1},a_q\}\), and the second half is reverse order with these two highest first-appearance letters swapped: it is the tail of \(V_q\).

**Lemma 4 (sufficiency and length spectrum).** In \(V_q\), any support \(S\) missing at least one of \(a_{q-1},a_q\) has its second occurrences in reverse first-occurrence order. It therefore gives one even and one odd palindrome, with lengths \(2|S|\) and \(2|S|-1\). If \(S\) contains both of these letters, its two odd palindromes have centers \(a_q\) (using that letter's first occurrence) and \(a_{q-1}\) (using that letter's second occurrence). All other symbols pair in nested order, and no even palindrome is possible. Thus every support contributes exactly two distinct palindromes, and the upper bound is attained. Among the \(\binom qk\) supports of size \(k\), exactly \(\binom{q-2}{k-2}\) contain both special letters. The displayed length-spectrum identities follow directly.

Finally, there are \(q!\) ways to assign the labeled alphabet to the distinct first appearances of each canonical form. For \(q\ge2\) the two forms are distinct (one is a palindrome and the other is not), proving exactly \(2q!\) labeled maximizers.

## Verification

The standalone `check_scattered_palindromes.py` uses two independent methods. Directly forming all distinct subsequences and testing reversibility, it exhaustively checks all perfect matchings of \(2q\) positions for \(1\le q\le5\); this covers all balanced words up to symbol relabeling. A separate interval-and-support calculation agrees with every direct count and every length histogram. Exhaustive second-half-permutation scans for \(q=6,7\) check the only-two-extremizers conclusion for \(720\) and \(5040\) tails. This is finite corroboration; the proof above establishes the theorem for all \(q\).

Run `python3 check_scattered_palindromes.py` from the directory containing that file. The expected final line is `ALL_SCATTERED_PALINDROME_CHECKS_PASSED`.

## Relationship to prior work

Mahalingam and Pandoh [1], Proposition 5.1 and Theorem 5.4, prove the relevant maximum \(2^{q+1}-2\) at length \(2q\) and exhibit the fully nested word. Their concluding discussion explicitly proposes characterizing maximally scattered-palindromic-rich words; the inspected proof and discussion do not give an exhaustive classification of double-occurrence equality cases. The present result does **not** claim novelty for the upper bound or the nested example; it classifies all balanced equality cases, discovers the second nonpalindromic family, and resolves the length spectra. Müllner and Ryzhikov [2] study longest palindromic subsequences and circular balance, not the count of distinct palindromic subsequence values. Holub and Saari [3] study highly palindromic binary words and reconstruction properties, rather than the displayed double-occurrence equality classification.

## Limitations

No classification is asserted for length-\(2q\) words with \(q\) distinct letters but **unequal** letter multiplicities, or for words at any other length. The pre-existing upper bound for those larger classes is not reproved as a new theorem. The exact classification is subject to independent review for correctness and bibliographic originality; no independent audit has been performed. The full text of [3] was not inspected, although its indexed abstract was checked.

## References

[1] K. Mahalingam and P. Pandoh, *Counting Scattered Palindromes in a Finite Word*, arXiv:2108.02729v1, first posted 2021-08-05. https://arxiv.org/pdf/2108.02729 (Proposition 5.1, Theorem 5.4, Section 6).

[2] C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502v1, 2019. https://arxiv.org/pdf/1901.07502.

[3] Š. Holub and K. Saari, *On Highly Palindromic Words*, Discrete Applied Mathematics 157 (2009), 953–959. DOI:10.1016/j.dam.2008.03.039. Indexed abstract consulted; complete text not inspected.
