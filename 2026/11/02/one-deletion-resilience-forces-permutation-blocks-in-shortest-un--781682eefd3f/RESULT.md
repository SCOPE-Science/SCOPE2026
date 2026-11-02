# One-deletion resilience forces permutation blocks in shortest universal words

## Finding
Fix an alphabet \(\Sigma\) of \(q\ge2\) **labeled** symbols. A word \(w\) is *one-deletion-resilient \(k\)-universal* if, for each position \(j\) of \(w\), every word of length \(k\) over \(\Sigma\) occurs as a scattered subsequence of the word obtained by deleting position \(j\). All occurrences and words are indexed, rather than quotiented by rotations or symbol relabeling.

**Theorem.** For every \(q\ge2\) and \(k\ge1\), the minimum length of a one-deletion-resilient \(k\)-universal word is \(q(k+1)\). For \(k\ge2\), **all** shortest words are precisely the concatenations
\[
w=P_1P_2\cdots P_{k+1}, \qquad P_i\in\operatorname{Sym}(\Sigma),
\]
where each \(P_i\) lists all symbols of \(\Sigma\) exactly once. Consequently the number of shortest words is
\[
(q!)^{k+1}\qquad(k\ge2).
\]
Equivalently, at the shortest possible length and for \(k\ge2\), one-deletion-resilient \(k\)-universality is *equivalent* to ordinary \((k+1)\)-universality.

The exceptional case is \(k=1\): the shortest words are all arrangements with exactly two copies of each alphabet symbol, counted by
\[
\frac{(2q)!}{2^q}.
\]
For example, a binary alphabet has six shortest one-deletion-resilient \(1\)-universal words but only four concatenations of two permutations. Thus the rigidity starts sharply at \(k=2\).

## Assumptions and scope
A word \(u=u_1\cdots u_k\) is a *scattered subsequence* of \(w=w_1\cdots w_n\) when there are indices \(1\le j_1<\cdots<j_k\le n\) with \(u_i=w_{j_i}\). Each deletion removes **one position**, not all copies of a symbol. The alphabet stays fixed after deletion. The result assumes an arbitrary finite alphabet size \(q\ge2\) and each integer \(k\ge1\). It does not concern universal substrings, unknown-symbol erasures, or deletion-correcting codes.

## Proof
**1. Sharp lower bound and construction.** For any fixed \(a\in\Sigma\), the target word consisting of \(k\) consecutive copies of \(a\) must survive deleting any occurrence of \(a\). Hence each \(a\) must occur at least \(k+1\) times in \(w\). Summing over \(q\) symbols yields \(|w|\ge q(k+1)\).

Choose arbitrary permutations \(P_1,\ldots,P_{k+1}\) and set \(w=P_1\cdots P_{k+1}\). Deleting a position damages at most one of those permutation blocks, so at least \(k\) complete blocks remain in their original order. For each target \(u_1\cdots u_k\), select \(u_i\) from its own intact block, for \(1\le i\le k\). Thus the bound is attained.

**2. Exact symbol multiplicities at equality.** Suppose \(|w|=q(k+1)\) and \(w\) is resilient. The preceding lower bound applied separately to each symbol forces exactly \(k+1\) copies of each symbol. For \(a\in\Sigma\) denote the positions of these copies in increasing order by
\[
a_1<a_2<\cdots<a_{k+1}.
\]
Here a letter with a numeric subscript designates its **occurrence position**, not another alphabet symbol.

**3. Ordering constraint for adjacent occurrence levels.** Assume \(k\ge2\). Fix two distinct symbols \(a,b\in\Sigma\). We claim
\[
a_i<b_{i+1}\qquad\text{for every }1\le i\le k.
\]
For \(1\le i\le k-1\), delete the *last* \(b\), at position \(b_{k+1}\). By resilience the remaining word must contain the length-\(k\) target \(a^i b^{k-i}\). Since the retained word has precisely \(k\) copies of \(b\), an embedding can put its \(k-i\) trailing copies of \(b\) after the required \(i\) copies of \(a\) only if at least \(k-i\) copies of \(b\) follow \(a_i\). This is exactly the necessary inequality \(a_i<b_{i+1}\).

For the final case \(i=k\), delete the *first* \(a\), at position \(a_1\). The retained word must contain the length-\(k\) target \(a^{k-1}b\). Its first \(k-1\) copies of \(a\) must occupy positions no earlier than \(a_2,\ldots,a_k\). Thus at least one \(b\) must follow \(a_k\); equivalently \(a_k<b_{k+1}\). This argument requires \(k\ge2\), exactly the advertised boundary.

Interchange the roles of \(a\) and \(b\). These inequalities hold for every ordered pair of distinct symbols, while the same-symbol inequalities \(a_i<a_{i+1}\) are automatic. Hence for each \(i\), **every** \(i\)-th occurrence (of every symbol) precedes **every** \((i+1)\)-st occurrence (of every symbol):
\[
\max_{a\in\Sigma} a_i<\min_{b\in\Sigma}b_{i+1}\quad(1\le i\le k).
\]
The occurrence levels are therefore consecutive groups in \(w\), each containing each alphabet symbol once. They form the permutations \(P_1,\ldots,P_{k+1}\), proving necessity of the asserted structure.

**4. Counting and the exceptional boundary.** The \(k+1\) alphabet permutations may be selected independently. This gives exactly \((q!)^{k+1}\) labeled indexed words when \(k\ge2\), with no double counting because block boundaries have fixed length \(q\). Conversely, every such concatenation is resilient by Step 1.

If \(k=1\), the equality case gives exactly two occurrences of every symbol. Deleting any single position leaves at least one occurrence of each symbol, so **every** such arrangement is resilient. Its multinomial count is \((2q)!/(2!)^q=(2q)!/2^q\). The proof covers all claimed cases. \(\square\)

## Verification
The proof is symbolic and holds for arbitrary \(q\ge2\) and \(k\ge1\). A standalone executable checker, `verify_deletion_robust.py`, tests resilience directly by enumerating each possible one-position deletion and all length-\(k\) target patterns. It does not implement the occurrence-level inequalities above. For every word having the necessary multiplicities, it tests whether resilience matches the theorem's permutation-block characterization (or the exceptional \(k=1\) case).

The verifier exhaustively checked 413,244 multiset words across 11 parameter pairs: binary alphabets with \(1\le k\le6\), ternary alphabets with \(1\le k\le3\), and four-letter alphabets with \(k=1,2\). In particular, it checked all 369,600 twelve-letter words with three copies of each of four symbols. The largest case has exactly 13,824 resilient words, matching \((4!)^3\). Its terminal certificate is `VERIFY_OK parameter_cases=11 multiset_words=413244`.

Run using Python 3: `python3 verify_deletion_robust.py`. These finite checks support reproducibility but are not substitutes for the all-parameter proof.

## Relationship to prior work
Barker et al. [1] develop the theory of scattered-factor universality and arch factorization. Day et al. [2,3] develop algorithms for the minimum number of edits needed to change a word's subsequence-universality index, including deletions. Adamson [4] counts and ranks ordinary \(k\)-universal words, while Adamson et al. [5] study their intersection with regular languages and provide general counting algorithms. Those methods give relevant background but the inspected results do not state a sharp, all-alphabet classification of shortest words that **remain** \(k\)-universal after **every individual deletion**, including the strict \(k=1\) exception. In particular, knowing the number of ordinary \((k+1)\)-universal words at minimal length does not by itself prove that resilience forces that stronger property when \(k\ge2\).

## Limitations
Only a **single arbitrary deletion** is covered. At lengths exceeding \(q(k+1)\), resilience need not coincide with ordinary \((k+1)\)-universality; no classification or count of longer resilient words is asserted. The theorem does not address multiple deletions, substitutions, unlabeled alphabets, or rotational equivalence. The literature comparison cannot exclude an unindexed equivalent theorem or an unstated consequence in other work. Scientific review recorded here is not an independent external audit.

## References
[1] L. Barker, P. Fleischmann, K. Harwardt, F. Manea and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1 (first public 2020-03-10), https://arxiv.org/abs/2003.04629.

[2] P. Fleischmann, M. Kosche, T. Koß, F. Manea and S. Siemer, *The Edit Distance to k-Subsequence Universality*, arXiv:2007.09192v1 (first public 2020-07-17), https://arxiv.org/abs/2007.09192.

[3] J. D. Day et al., *The Edit Distance to k-Subsequence Universality*, STACS 2021, Article 25, doi:10.4230/LIPIcs.STACS.2021.25.

[4] D. Adamson, *Ranking and Unranking k-Subsequence Universal Words*, arXiv:2304.04583v1 (2023-04-10), https://arxiv.org/abs/2304.04583.

[5] D. Adamson et al., *k-Universality of Regular Languages*, arXiv:2311.10658v1 (2023-11-17), https://arxiv.org/abs/2311.10658.
