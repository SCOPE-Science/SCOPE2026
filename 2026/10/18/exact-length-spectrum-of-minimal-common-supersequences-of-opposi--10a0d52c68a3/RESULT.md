# Exact length spectrum of minimal common supersequences of opposite binary blocks

## Finding
For each integer \(m\ge1\), define \(A_m=0^m1^m\) and \(B_m=1^m0^m\). A binary word is a *minimal common supersequence* if it contains both inputs as subsequences but deletion of any single position destroys this property. The exact number of minimal common supersequences of length \(3m+j\) is
\[
2\binom{m+j-1}{j}^{2}\qquad(0\le j<m),
\]
and no other length occurs. The total count and its asymptotic are
\[
T_m=2\sum_{j=0}^{m-1}\binom{m+j-1}{j}^{2}\sim\frac{16^m}{6\pi m}.
\]
Thus precisely two are shortest, with length \(3m\), whereas the maximum length of a minimal common supersequence is \(4m-1\).

## Assumptions and scope
Words are finite over \(\{0,1\}\) and contain an input as a subsequence if some increasing list of positions spells that input. Minimal means minimal in the subsequence partial order, not merely of shortest possible length. Checking all one-position deletions suffices because the common-supersequence property is preserved under adding letters. The inputs have exactly two opposite blocks of equal length; no assertion concerns arbitrary pairs of words.

All minimal words are exactly the following disjoint classes, indexed by \(0\le j<m\):
\[
P1^{m-j}Q
\]
and their letterwise complements, where \(P\) and \(Q\) each contain exactly \(m\) zeros and \(j\) ones, \(P\) ends in zero, and \(Q\) begins in zero. The central run is the gap between the \(m\)-th and \((m+1)\)-st zero.

## Proof
**Embedding intersection.** Fix a minimal common supersequence \(W\), and choose embeddings \(E_A\), \(E_B\) of the two target words. Their union must cover every position of \(W\); otherwise an unused letter could be deleted. They must intersect: if disjoint, let \(a\) be the last selected zero of \(E_A\) and \(b\) the last selected one of \(E_B\). If \(a<b\), position \(b\) is an extra one after the \(m\) selected zeros of \(E_A\), and it can replace some selected one of \(E_A\). The new pair of embeddings intersects, so their union no longer covers the original word, a contradiction. If \(b<a\), instead replace one selected zero of \(E_B\) by the extra zero at position \(a\). Since disjointness forces \(a\ne b\), these cases exhaust the possibilities.

Any shared positions of two embeddings must all have the same symbol: a shared zero and a shared one would be ordered zero-before-one in \(A_m\), yet one-before-zero in \(B_m\). Complement symbols if necessary so the shared letter is one. The \(m\) zeros selected for \(A_m\) occur before the overlap and the \(m\) zeros selected for \(B_m\) occur after it. Since the union covers all positions, \(W\) has exactly \(2m\) zeros, divided into those two groups. There is a nonempty run of ones between the middle zeros. Write \(W=P1^gQ\), where \(P\) ends at the \(m\)-th zero, \(Q\) begins at the \((m+1)\)-st zero, both sides contain \(m\) zeros, and \(g\ge1\). Let \(p\) and \(s\) be their numbers of ones.

The two target embeddings require \(p+g\ge m\) and \(s+g\ge m\). If \(p+g>m\) with \(p>0\), remove a one in \(P\): the \(m\) zeros in \(P\), the \(m\) zeros in \(Q\), and the necessary ones before or after them still give both embeddings, a contradiction. If \(p=0\) with \(p+g>m\), then \(g>m\), and removing one central one also preserves both embeddings. Therefore \(p+g=m\). The symmetric argument gives \(s+g=m\). It follows that \(p=s=j=m-g\), with \(0\le j<m\), proving necessity.

**Sufficiency.** Conversely for any such \(P1^{m-j}Q\), input \(A_m\) uses all \(m\) zeros of \(P\) followed by the \(m-j\) central ones and the \(j\) ones of \(Q\); input \(B_m\) uses the \(j\) ones of \(P\), central ones, and all \(m\) zeros of \(Q\). If a zero in \(P\) is removed, any candidate embedding of \(A_m\) must take a zero from \(Q\), after which at most \(j<m\) ones remain; hence \(A_m\) is destroyed. Removing a zero from \(Q\) analogously destroys \(B_m\). Removing a one in \(P\) leaves only \(m-1\) ones before the first zero of \(Q\), and a candidate \(B_m\) embedding that takes a zero from \(P\) cannot use the later central ones and has at most \(j<m\) ones preceding it. Thus \(B_m\) is destroyed; symmetrically a removed one in \(Q\) destroys \(A_m\). Removing a central one makes both \(p+g\) and \(s+g\) equal \(m-1\), so both targets are destroyed. Every symbol is therefore essential. Complementation preserves the property.

**Counting and asymptotics.** The forced boundary zeros leave \(m+j-1\) positions in each of \(P,Q\) where their respective \(j\) ones may be chosen, giving \(\binom{m+j-1}{j}^{2}\). Complementary classes are disjoint because their symbol counts differ; different \(j\) give different lengths. For \(b_m=\binom{2m-2}{m-1}^2\), the ratio of the \(j=m-1-k\) term to \(b_m\) is
\[
\prod_{i=0}^{k-1}\left(\frac{m-1-i}{2m-2-i}\right)^2\le4^{-k}
\]
and converges to \(4^{-k}\) for each fixed \(k\). Dominated convergence yields \(T_m/b_m\to8/3\). Stirling gives \(b_m\sim16^{m-1}/(\pi m)\), whence \(T_m\sim16^m/(6\pi m)\).

## Verification
Compile `verify.c` with `cc -O3 -std=c11 verify.c -o verify` and execute `./verify`. It implements independent subsequence predicates, deletion-by-deletion minimality, the predicted shape, and exact binomial counts. It exhaustively checks every binary word at every length from \(2m\) through \(4m\), for \(1\le m\le5\): 2,235,596 words in total. The final output is `VERIFY_OK objects=2235596 minimum_supersequences=13890 n<=5`. This finite consistency check is not substituted for the general proof.

## Relationship to prior work
Sopp, Liyanage, Gong and Zhu (arXiv:2603.22591; first publicly posted March 23, 2026) give a general polynomial-delay enumeration algorithm for minimal common supersequences, but do not state this closed all-length profile in the inspected full text. Alon, Bourla, Graham, He and Kravitz (arXiv:2209.11882) study **shortest** common supersequences; their multiplicity conclusions do not determine the longer minimal words here. Fraser, Irving and Middendorf (1996) develop the classical minimal-supersequence theory; its full text could not be accessed in this review, so an unindexed special-case result there is an explicit originality risk. This finding is a structured-case formula, not a faster general algorithm.

## Limitations
The formula covers equal-length two-block binary inputs only; it makes no claims for arbitrary input words or alphabets. The computer verification exhausts \(m\le5\), not unbounded \(m\). The inaccessible full 1996 primary text and other unindexed literature may contain equivalent special cases. No independent external scientific audit has been performed.

## References
1. J. Sopp, W. Liyanage, Y. Gong and Z. Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591, first posted 2026-03-23. https://arxiv.org/abs/2603.22591
2. N. Alon, A. Bourla, R. Graham, X. He and N. Kravitz, arXiv:2209.11882 (2022), https://arxiv.org/abs/2209.11882.
3. C. Fraser, R. Irving and M. Middendorf, *Maximal Common Subsequences and Minimal Common Supersequences*, Information and Computation (1996), DOI:10.1006/inco.1996.0011.
