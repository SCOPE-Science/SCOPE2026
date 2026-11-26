# Sharp extremal inverse lists for length-two palindromic duplication

## Finding

Fix a finite alphabet of size \(q\ge2\). Contracting a factor \(abba\) of a word \(y\in\Sigma^N\) to \(ab\) gives a parent, and distinct sites yielding the same parent are counted once. Among words of length \(N\ge4\), the maximum number of parents is \(\lfloor(N-2)/2\rfloor\). The number of words attaining this maximum is
\[
E_q(N)=\begin{cases}
q^2,&N=4,\\
2q^3-q,&N=5,\\
q(q-1),&N\ge6\text{ even},\\
q(q-1)((t+1)(q-1)+4),&N=2t+3,\ t\ge2.
\end{cases}
\]
The even-length maximizers for \(N\ge6\) are exactly the period-four prefixes \(abbaabba\cdots\) with distinct \(a,b\). The maximizing odd-length words are described by the junction parametrization below. The contribution is the extremizer census, particularly its odd-length case, not a new maximum bound or a new general collision test.

## Reduction to legal-site runs

Use zero-based positions. A site \(i\in\{0,\ldots,N-4\}\) is legal if \(y_i=y_{i+3}\) and \(y_{i+1}=y_{i+2}\); the contraction deletes \(i+2,i+3\). Consecutive legal sites \(i,i+1\) require all five letters \(y_i,\ldots,y_{i+4}\) equal, so give the same parent. Conversely, if legal sites \(i<j\) give the same parent, comparison of the two outputs gives \(y_s=y_{s+2}\) for \(i+2\le s\le j+1\). The inner pair of the palindrome at \(j\) has \(y_{j+1}=y_{j+2}\), so the two parity classes merge and \(y_{i+2},\ldots,y_{j+3}\) are all equal. The equalities at \(i\) extend this to \(y_i,y_{i+1}\). Every site between \(i\) and \(j\) is legal. Thus the number of parents is the number of consecutive runs of legal sites. This calculation specializes the prior collision conditions [1, Appendix B].

There are \(m=N-3\) candidate sites. A set with \(c\) runs needs at least \(2c-1\) sites in total, including separators, which gives the maximum bound directly from the zero-column-run bound [1, Lemma 15]. The period-four prefixes with distinct period letters attain it (exactly the even sites are legal). For \(N\ge6\) even, \(m=2c-1\) at equality, so the legal sites must be exactly the even ones, all isolated. The palindrome constraints at successive even sites uniquely extend the initial \(abba\) to its period-four prefix. Equal period letters would make every site legal and give only one parent, so they are excluded.

## Odd lengths

Let \(N=2t+3\), \(t\ge2\). A maximizing set has \(t\) runs in \(2t\) positions. If there is an adjacent pair at \(i,i+1\), all slack above the minimum \(2t-1\) positions is used by that doubleton: every other run is a singleton and all separators have length one. As \(t\ge2\), at least one of \(i-2\) and \(i+3\) must be legal. From the adjacent pair, \(y_i,\ldots,y_{i+4}\) are equal. A palindrome at \(i-2\) would then extend this constant segment to the left and make \(i-1\) legal. A palindrome at \(i+3\) would extend it to the right and make \(i+2\) legal. Either merges two runs, a contradiction. Thus all runs are singletons. The possible legal-site sets are
\[
S_j=\{0,2,\ldots,2j-2\}\cup\{2j+1,2j+3,\ldots,2t-1\},\qquad 0\le j\le t,
\]
with empty components permitted. These alternatives use the single position of slack for an extra initial or terminal position or for a double separator.

At \(j=0,t\) the palindromes force a period-four block with two different letters (there are at least two sites), and leave one free end letter. The untested site at the end cannot be legal since its middle pair lies at the unequal transition of the block. Each case contributes \(q^2(q-1)\) words. At an interior \(j\), the last palindrome of the first block and the first palindrome of the second start three positions apart. They meet in a single letter \(x\) and read \(xuuxvvx\) together. Each side extends from its initial (or terminal) palindrome at spacing two. The two omitted junction sites are legal precisely when \(x=u=v\), as seen by testing their four-letter windows. If a side has at least two palindromes, its second letter must differ from \(x\), or the intermediate site between the first two on that side would also be legal. These restrictions suffice, since the only omitted sites are those inside the two periodic blocks and those at the junction.

For \(t=2\) the unique interior alternative has two single-palindrome sides and contributes \(q^3-q\), giving total \(2q^2(q-1)+q^3-q\). For \(t\ge3\) the two interior alternatives \(j=1,t-1\) each contribute \(q^2(q-1)\), and the remaining \(t-3\) alternatives each contribute \(q(q-1)^2\). The sum is \(q(q-1)((t+1)(q-1)+4)\) in both cases. For \(N=4\) the maximizers are just the \(q^2\) palindromes. For \(N=5\) each of the two windows contributes \(q^3\) words and their intersection consists of the \(q\) constant words, so the count is \(2q^3-q\).

## Prior coverage and ancillary incidence identity

The exact collision criteria in [1] and the earlier binary deletion-sphere formula in [2] precede the run reduction used here. The sharp maximum follows from the run bound and the periodic witness; [3, §6] gives a looser general upper bound. For comparison, the exact maximum and the aggregate incidence count both appear in the separate catalogue record [4], and the maximum also specializes from the all-length result [5] at duplication length two. These two catalogue comparisons are later-dated and do not settle historical priority. The incidence count itself follows at once from the per-word run formula: each of \(N-3\) legal-site indicators occurs for \(q^{N-2}\) words and each of \(N-4\) adjacent pairs for \(q^{N-4}\) words. Subtracting gives \((N-3)q^{N-2}-(N-4)q^{N-4}\). This aggregate is separate from the extremizer census. The latter needs equality patterns and local letter constraints, not just the per-word count or its sum.

The scope is one contraction of duplication length two, with no assertion about multiple edits, other block lengths or code cardinalities. The supplied finite checker corroborates the formulas over its specified finite ranges; the proof above establishes the unbounded census.

## References

1. A. Lenz, A. Wachter-Zeh, E. Yaakobi, *Duplication-Correcting Codes*, [arXiv:1712.09345](https://arxiv.org/abs/1712.09345), Lemmas 14–15 and Appendix B.
2. A. Lenz, A. Wachter-Zeh, E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, [arXiv:1707.00052](https://arxiv.org/abs/1707.00052), Lemmas 5–6.
3. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, [arXiv:2609.00779](https://arxiv.org/abs/2609.00779), Section 6.
4. *Exact inverse lists for a single length-two palindromic duplication*, [Resultary, 2026-11-02](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-inverse-lists-for-a-single-length-two-palindromic-duplicat--890e7708ebeb/RESULT.md).
5. *Sharp inverse-list maximum for a single palindromic duplication*, [Resultary, 2026-11-02](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-sharp-inverse-list-maximum-for-a-single-palindromic-duplication--47e8202dd4ba/RESULT.md).
