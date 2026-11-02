# Rotation-by-rotation shortest absent subsequences of constrained binary cycles

## Finding
Let \(W\) be a nonempty binary circular word with \(m\ge2\) occurrences of \(1\). Suppose the successive cyclic numbers of \(0\)'s between consecutive \(1\)'s are \(g_1,\ldots,g_m\in\{1,2\}\), and no two neighboring gaps (including \(g_m,g_1\)) are both \(1\). Put \(t=|\{i:g_i=2\}|\); necessarily \(t\ge1\). A *root* means a length-\(|W|\) linearization at one of its indexed starting positions, without wrapping subsequence matches. For a root \(w\), let \(S(w)\) denote the shortest absent subsequences over \(\{0,1\}\): words absent as order-preserving scattered subsequences of \(w\), of the least possible length.

Every root has shortest absent length exactly \(m+1\), and its complete absent set is as follows. The expressions are ordinary concatenation, with exponent \(0\) denoting an empty block.

1. If \(w\) begins in \(1\), write \(h\in\{1,2\}\) for the number of zeros before its second \(1\). Then
   \[
   S(w)=\{1^{m+1},\ 0 1^m\}\cup
   \begin{cases}\{00 1^{m-1}\},&h=1,\\\varnothing,&h=2.\end{cases}
   \]
2. If \(w\) begins in \(0\) and ends in \(1\), let \(h\) be the zeros between its penultimate and final \(1\). Then
   \[
   S(w)=\{1^{m+1},\ 1^m0\}\cup
   \begin{cases}\{1^{m-1}00\},&h=1,\\\varnothing,&h=2.\end{cases}
   \]
3. If \(w\) begins and ends in \(0\), then \(S(w)=\{1^{m+1}\}\).

Consequently, among all \(2m+t\) indexed roots, the number having exactly \(j\) shortest absent subsequences is
\[
(N_1,N_2,N_3)=(t,\ 2t,\ 2(m-t)),
\]
with no other cardinality possible. This is a complete root profile depending only on the numbers of single- and double-zero gaps, not on their arrangement. For periodic circular words, indexed roots are counted with multiplicity.

**Fibonacci specialization.** Define \(F_0=0\), \(F_1=01\), and \(F_k=F_{k-1}F_{k-2}\) for \(k\ge2\). Let \(f_0=0, f_1=1, f_{k+2}=f_{k+1}+f_k\) be numerical Fibonacci numbers. For every \(k\ge3\), the circular word represented by \(F_k\) satisfies the hypotheses, has \(f_k\) ones and length \(f_{k+2}\), and has precisely
\[
\bigl(f_{k-1},\ 2f_{k-1},\ 2f_{k-2}\bigr)
\]
indexed roots with respectively one, two, and three shortest absent subsequences, all of length \(f_k+1\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). A scattered subsequence preserves relative order but need not be contiguous. No matching is allowed across the endpoint of a chosen root. The circular gap restrictions are equivalent to forbidding cyclic occurrences of \(11\), \(000\), and \(10101\), interpreting cyclic occurrences in the bi-infinite periodic extension. The theorem concerns *indexed* starting positions, and \(m\ge2\). No assertion is made for alphabet sizes exceeding two, for unrestricted gaps, or for the number of minimal (rather than shortest) absent subsequences of all lengths.

## Proof
**Pair universality.** Each cyclic gap is positive. If a root begins in \(1\), every one is followed by a zero within the linear root, so \((10)^m\) is an order-preserving subsequence. If it begins in \(0\), every one is preceded by a zero, so \((01)^m\) is a subsequence. Either alternating word contains every binary word of length \(m\): from the \(i\)-th ordered pair select its \(0\) or \(1\) as desired. But \(1^{m+1}\) is absent because the entire root has only \(m\) ones. Thus the shortest absent length is \(m+1\).

**Pair-merging lemma.** A word of length \(m+1\) containing an adjacent \(10\) is a subsequence of \((10)^m\). Merge one such adjacent pair into one of the \(m\) disjoint \(10\) blocks, placing each other letter into a separate block; every individual letter occurs in its selected block. Symmetrically, every length-\(m+1\) word containing an adjacent \(01\) is a subsequence of \((01)^m\). Hence any absent word for a root beginning in \(1\) must be \(0^a1^{m+1-a}\); any absent word for a root beginning in \(0\) must be \(1^a0^{m+1-a}\).

**Roots beginning in \(1\).** Number their ones from first to last. For \(1\le a\le m\), the most zeros obtainable before selecting \(m+1-a\) ones are those preceding one number \(a\); this is exactly \(g_1+\cdots+g_{a-1}\) in the root's forward gap ordering. Thus \(0^a1^{m+1-a}\) occurs precisely when that sum is at least \(a\). For \(a=1\), the sum is zero, giving the absent word \(01^m\). For \(a=2\), the condition is \(g_1=2\). For each \(3\le a\le m\), two or more consecutive gaps occur in the sum. Since no two consecutive gaps equal \(1\), at least one is \(2\), so the sum is at least \(a\). For \(a=m+1\), the proposed word is all zeros and occurs because the root has \(m+t\ge m+1\) zeros. The case \(a=0\) is \(1^{m+1}\), already known absent. This proves the first set.

**Roots beginning in \(0\) and ending in \(1\).** Reverse the root. Its reversal begins in \(1\), has the same admissible cyclic gaps in reverse order, and its first forward gap is the original gap immediately preceding the final one. Reversal preserves the subsequence relation after reversing the candidate word. The first case therefore proves the second set.

**Roots beginning and ending in \(0\).** The root contains both \((01)^m\) (one zero before each one) and \((10)^m\) (one zero after each one). Any nonconstant binary word has an adjacent transition, either \(01\) or \(10\), and so, if its length is \(m+1\), the pair-merging lemma embeds it. The constant-zero word of this length is present because there are \(m+t\ge m+1\) zeros. The constant-one word is absent. This proves the third set.

**Counting roots.** Each double gap contributes exactly one root starting and ending in zero (its second zero); there are \(t\) such roots. There are exactly \(m\) roots beginning in one, of which \(t\) have next gap two and \(m-t\) next gap one. There are exactly \(m\) roots beginning in zero and ending in one, one per gap; their preceding-final-one gaps also traverse every cyclic gap once, so they contribute another \(t\) roots of cardinality two and \(m-t\) of cardinality three. The asserted profile follows and sums to \(2m+t\).

**Fibonacci specialization.** For \(k\ge2\), \(F_{k+1}=\mu(F_k)\), where \(\mu(0)=01\) and \(\mu(1)=0\). The circular word \(F_3=01001\) avoids the three forbidden cyclic patterns. A cyclic input avoiding \(11\) and \(000\) has an image under \(\mu\) avoiding \(11\), \(000\), and \(10101\): every image one is immediately preceded by zero and followed by the first zero of the next image; an image occurrence of \(000\) would require consecutive input ones, and an image occurrence of \(10101\) would require three consecutive input zeros (each displayed one is the terminal symbol of an input-zero image, with no intervening input-one image). This also holds across cyclic seams. Induction proves the forbidden-pattern property for all \(k\ge3\). The elementary recurrences give \(|F_k|=f_{k+2}\) and \(|F_k|_1=f_k\); therefore \(t=|F_k|-2|F_k|_1=f_{k-1}\) and \(m-t=f_{k-2}\). Substitute in the general theorem.

## Verification
The included standalone `verify_rotations.py` requires Python 3 and no external dependencies. Execute `python3 verify_rotations.py`. It enumerates every ordered cyclic gap tuple satisfying the hypotheses for \(2\le m\le10\), and every indexed root; it compares the proposed absent set with direct greedy subsequence membership for all \(2^{m+1}\) length-\(m+1\) binary candidates. Independently it counts missing strings with a dynamic program on greedy first-match states. It also verifies the Fibonacci specialization for all indexed roots with \(3\le k\le11\). The observed output was `VERIFY_OK gap_cycles= 318 gap_roots= 7359 tested_length_m_plus_1_words= 9484688 fibonacci_roots= 602`. These finite checks corroborate, but do not replace, the all-length proof.

## Relationship to prior work
Rittaud and Vivier (2011) studied circular words subject to Fibonacci-motivated restrictions; their arithmetic and circular-group results do not concern scattered-subsequence absence. Fici, Restivo, and Rizzo (2017) gave the minimal forbidden **contiguous factors** of circular Fibonacci words and discussed their factor automata; scattered subsequences constitute a different language. Kosche, Koß, Manea, and Siemer (first arXiv version 2021) gave general combinatorial characterizations and algorithms for shortest absent subsequences of arbitrary linear words. Adamson and collaborators (first arXiv version 2024) bounded absent-scattered-factor numbers for arbitrary words at a fixed universality index. Neither of those general studies was found to state this root-by-root restricted-cycle law or the exact Fibonacci rotation multiplicities. The general characterizations permit algorithmic tests; they do not in themselves supply the present closed-form root classification without the gap and pair-merging argument. Scientific-literature comparisons did not identify an equivalent or stronger statement. Historical priority remains provisional.

## Limitations
The proof treats indexed roots of cyclic binary words satisfying all three forbidden-factor restrictions. Removing the nonadjacent-single-gap condition invalidates the five-pattern conclusion in general. The finite checker is not a proof at unbounded length, and independent review and comprehensive unpublished-literature checks have not been performed. The formulas do not imply new general lower bounds for all binary words with the same length or universality index.

## References
- B. Rittaud and L. Vivier, *Circular words and applications*, arXiv:1108.3618v1, first public version 2011-08-18, https://arxiv.org/abs/1108.3618.
- G. Fici, A. Restivo, and L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450v1, first public version 2017-07-14, https://arxiv.org/abs/1707.04450.
- M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, first public version 2021-08-31, https://arxiv.org/abs/2108.13968.
- D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, and M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599v1, first public version 2024-07-26, https://arxiv.org/abs/2407.18599.
