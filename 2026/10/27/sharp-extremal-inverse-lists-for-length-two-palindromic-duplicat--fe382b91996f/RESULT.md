# Sharp extremal inverse lists for length-two palindromic duplication

## Finding
Let \(\Sigma\) be any alphabet of cardinality \(q\ge2\). For a received word \(y\in\Sigma^N\), \(N\ge4\), let \(\mathcal P(y)\) be the set of distinct length-\(N-2\) parents obtainable by contracting exactly one factor \(abba\) into \(ab\). Write \(M_q(N)\) for the largest such inverse-list size. Then
\[
M_q(N)=\left\lfloor\frac{N-2}{2}\right\rfloor.
\]
The **exact number \(E_q(N)\) of received words attaining \(M_q(N)\)** is
\[
E_q(N)=\begin{cases}
q^2,&N=4,\\
2q^3-q,&N=5,\\
q(q-1),&N\ge6\text{ even},\\
q(q-1)\bigl((t+1)(q-1)+4\bigr),&N=2t+3,\ t\ge2.
\end{cases}
\]
For even \(N\ge6\), the extremizers are **exactly** the \(q(q-1)\) length-\(N\) prefixes of the periodic words \(abbaabba\cdots\) with \(a\ne b\). More generally, the sum of inverse-list sizes is
\[
\sum_{y\in\Sigma^N}|\mathcal P(y)|=(N-3)q^{N-2}-(N-4)q^{N-4}.
\]

## Assumptions and scope
The palindrome duplication operation acts on two consecutive source symbols \(ab\) by inserting the reversal \(ba\), producing \(abba\). Distinct contraction sites producing the same parent count once. Positions are zero-based, and the same alphabet symbol may occupy multiple positions; no field structure is assumed. The claim concerns **one** length-two palindromic duplication (not arbitrary-length duplication, noisy duplication, or two successive duplications).

## Proof
Define \(I(y)=\{i:0\le i\le N-4,\ y_i=y_{i+3},\ y_{i+1}=y_{i+2}\}\). A legal contraction at \(i\) deletes positions \(i+2,i+3\). Regard \(I(y)\) as a subset of the integer path \(0,\ldots,N-4\), and denote by \(c(I)\) its number of nonempty consecutive runs.

**Collision lemma.** Two legal contractions have the same output if and only if their starts lie in the same consecutive run of \(I(y)\). Consecutive legal starts \(i,i+1\) imply that \(y_i,\ldots,y_{i+4}\) are equal, so both contractions agree; transitivity gives one parent per run. Conversely, if contractions at \(i<j\) agree, comparison of the two output words at positions from \(i+2\) to \(j+1\) forces \(y_s=y_{s+2}\) for every \(i+2\le s\le j+1\). In addition, the palindrome at \(j\) forces \(y_{j+1}=y_{j+2}\). Back-propagation through the period-two identities gives equality of all letters in \(y_{i+2},\ldots,y_{j+3}\); the palindrome at \(i\) extends this equality to \(y_i,y_{i+1}\). Thus every intermediate start is legal. Hence \(|\mathcal P(y)|=c(I(y))\).

There are \(m=N-3\) candidate starts. A set of \(c\) separated runs requires at least \(2c-1\) positions. Hence \(c\le\lceil m/2\rceil=\lfloor(N-2)/2\rfloor\). Every period-four word \(abbaabba\cdots\) with \(a\ne b\) has exactly the legal starts \(0,2,4,\ldots\), attaining this bound. For even \(N\ge6\), \(m\) is odd, and equality forces exactly these even starts (all singleton runs). Overlapping four-letter palindromes at separation two force the entire word to be the stated period-four prefix. The letters must be unequal; otherwise there is one continuous run. Thus there are precisely \(q(q-1)\) such extremizers.

For odd \(N=2t+3\) with \(t\ge2\), we have \(m=2t\) and need exactly \(t\) runs. No maximizing legal-start set can contain two consecutive positions: otherwise the unique possible minimum-length run arrangement has another legal start two positions before or three positions after the consecutive pair. The corresponding three palindromes force all intervening letters equal, creating an additional legal start and merging two runs. Consequently all runs are singleton. The possible sets of \(t\) nonadjacent positions in \(\{0,\ldots,2t-1\}\) are exactly
\[
S_j=\{0,2,\ldots,2j-2\}\cup\{2j+1,2j+3,\ldots,2t-1\},\qquad0\le j\le t,
\]
with empty components permitted. These sets are disjoint alternatives because they are the complete legal-start sets of maximizing words.

For a fixed \(S_j\), the palindrome constraints identify all but three independent letter values. At \(j=0\) and \(j=t\), a free end letter and two periodic-block letters give exactly \(q^2(q-1)\) maximizing words, because the two block letters must differ. At an interior \(j\), the two blocks of overlapping palindromes meet in one letter \(x\); each is determined by \(x\) and an additional letter \(u\) or \(v\). The local bridge is, up to relabeling, \(xuuxvvx\). The two omitted starts at the junction become legal precisely when \(x=u=v\). If a block contains two or more legal starts, its periodic letters must differ, or it would also acquire unwanted adjacent legal starts. Thus for \(j=1\) or \(j=t-1\) with \(t\ge3\) there are \(q^2(q-1)\) choices, while for \(2\le j\le t-2\) there are \(q(q-1)^2\). For \(t=2\), the sole interior case \(j=1\) allows all triples except \(x=u=v\), giving \(q^3-q\). Summing gives \(q(q-1)((t+1)(q-1)+4)\) for all \(t\ge2\).

For \(N=4\), exactly the \(q^2\) palindromes \(abba\) have a parent. For \(N=5\), exactly one parent exists if either length-four window is palindromic; inclusion-exclusion gives \(2q^3-q\) received words. Finally, each candidate start contributes \(q^{N-2}\) received words with a palindrome, while each adjacent pair contributes \(q^{N-4}\) all-equal words. Since the number of runs equals the number of legal starts minus adjacent legal-start pairs, summation proves the incidence formula.

## Verification
The included `CHECK.py` independently generates every word for \((q,N)\) in the finite ranges \(q=2,\ 4\le N\le15\); \(q=3,\ 4\le N\le11\); \(q=4,\ 4\le N\le9\); and \(q=5,\ 4\le N\le7\). It explicitly constructs and deduplicates all parent words, recomputes legal-start runs, checks each bound, verifies even-length extremizer rigidity, counts all maximizers, and totals all parents. The recorded run examined **778,140** received words and passed. Finite checks corroborate but do not replace the complete symbolic proof.

## Relationship to prior work
The motivating 2026 work establishes a general upper bound of \(N-3\) for the number of single-step length-two palindromic-duplication parents of a received word of length \(N\), without the sharp extremizer census above. Lenz, Wachter-Zeh, and Yaakobi (2017) already derive exact **binary** palindromic-deletion sphere sizes and a general-alphabet upper bound using run indicators; those results, and their appendix's conditions for coincident contractions, cover important ingredients. The present claim is the exact **all-alphabet** maximizing inverse-list value together with its complete parity-dependent enumeration and even-length rigidity, not priority for the binary collision technique.

## Limitations
The exact classification concerns one fixed duplication block length two and one deletion. No conclusion is claimed for longer palindrome blocks, multiple edits, or optimal correcting-code cardinalities. The overlap test cannot exclude unindexed equivalent earlier work; the general collision conditions in prior literature make implicit specializations a particular historical-priority risk.

## References
- A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779 (first public version 2026-09-01), Section 6.
- A. Lenz, A. Wachter-Zeh, E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052 (2017), Lemmas 5–6.
- A. Lenz, A. Wachter-Zeh, E. Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345 (2017), Lemmas 14–15 and Appendix B.
