# Sharp multiplicity bounds for longest run subsequences of two-permutation words

## Finding
Let \(m\geq 1\), let \(\pi\) be a permutation of \(\{1,\ldots,m\}\), and let \(W_\pi=12\cdots m\,\pi_1\pi_2\cdots\pi_m\). Call a subsequence a *run subsequence* if each symbol occurs in at most one contiguous run in that subsequence. Let \(L(W_\pi)\) be the maximum possible length and let \(N(\pi)\) count **distinct subsequence words**, rather than index sets, attaining this length.

For every \(\pi\), \(L(W_\pi)=m+1\). Let \(R(\pi)\) denote the positions \(t\in\{1,\ldots,m\}\) at which \(\pi_t\) exceeds every preceding value (left-to-right maxima). Then
\[
N(\pi)=\sum_{t\in R(\pi)}2^{\pi_t-t}.
\]
Consequently, for every \(m\geq1\),
\[
m\leq N(\pi)\leq 2^{m-1}.
\]
The lower equality holds **exactly** when \(\pi\) is a concatenation of increasing singleton blocks \((j)\) and adjacent decreasing pairs \((j+1,j)\), using consecutive value intervals in order. Hence precisely \(F_{m+1}\) permutations attain the lower bound, where \(F_1=F_2=1\) is the Fibonacci sequence.

For \(m\geq2\), the upper equality holds **exactly** when either \(\pi_1=m\), or \((\pi_1,\pi_2)=(m-1,m)\). Thus precisely \(m(m-2)!\) permutations attain the upper bound. At \(m=1\), the sole permutation attains both bounds.

## Assumptions and scope
All symbols are distinct labels from \(\{1,\ldots,m\}\), each appearing exactly twice in \(W_\pi\), once in increasing order and once in arbitrary permutation order. The word \(W_\pi\) is linear, not circular. An occurrence of a subsequence chooses increasing positions in the host word; two different position selections giving identical label sequences count once. The empty subsequence is permitted but is never optimal. The theorem is a word-enumeration result on this restricted family, not a polynomial-time solution for arbitrary longest-run-subsequence instances.

## Proof
**1. Optimal length.** Any run subsequence can use both copies of *at most one* label. Indeed, suppose it retains both copies of two different labels \(a,b\). Their first copies both lie in the first half of \(W_\pi\), and their second copies both lie in the second half. Whichever first copy comes first must be separated from its second copy by a retained copy of the other label, contradicting the single-run condition. Thus a run subsequence has length at most \(m+1\): at most one label twice, and every other label at most once. This length is attained by retaining the first copy of each label below \(m\) and both copies of \(m\): the resulting subsequence is \(12\cdots(m-1)mm\). Hence \(L(W_\pi)=m+1\), including \(m=1\).

**2. Exact multiplicity.** Every optimum must retain both occurrences of exactly one label \(i\) and one occurrence of each other label. Its two copies of \(i\) must be adjacent in the resulting subsequence. For each \(j>i\), the first copy of \(j\) lies between the copies of \(i\); therefore its second copy must lie after the second \(i\). This is possible for *every* such \(j\) if and only if all values larger than \(i\) occur after \(i\) in \(\pi\), equivalently \(i\) is a left-to-right record of \(\pi\). For a record \(i=\pi_t\), every \(j<i\) has a first occurrence before the first \(i\). Such a \(j\) additionally has the option of its second occurrence after the second \(i\) precisely when \(j\) follows \(i\) in \(\pi\). Since all \(t-1\) preceding values in \(\pi\) are below \(i\), exactly \(i-t\) smaller values follow it. Every subset of those \(i-t\) labels independently chooses its occurrence before or after the pair \(ii\). The resulting label words are different whenever choices differ, because each label changes sides of \(ii\). Different doubled labels also give different words. Thus the contribution of record position \(t\) is \(2^{i-t}\), proving the displayed formula.

**3. Lower bound.** Write the record positions as \(t_1<\cdots<t_r\), their values as \(i_1<\cdots<i_r=m\), and define \(d_s=i_s-t_s\geq0\). At record \(i_s\), exactly \(d_s\) smaller values have not yet occurred. Every nonrecord value \(j\) is smaller than the most recent preceding record, so \(j\) is counted among the missing smaller values of that record. It follows that \(\sum_s d_s\geq m-r\). Since \(2^d\geq 1+d\) for every integer \(d\geq0\), we obtain
\[
N(\pi)=\sum_{s=1}^r2^{d_s}\geq r+\sum_{s=1}^rd_s\geq m.
\]

If equality holds, every \(d_s\in\{0,1\}\) (the inequality \(2^d\geq1+d\) is strict for \(d\geq2\)), and no nonrecord can be counted as missing at two records. The first value \(\pi_1\) is a record with \(d_1=\pi_1-1\); hence \(\pi_1\in\{1,2\}\). If \(\pi_1=1\), remove it: the remaining suffix, after lowering labels by one, is a permutation and must also attain its lower bound, by the same formula. If \(\pi_1=2\), label \(1\) is missing at the first record. Were another record to occur before label \(1\), it would count label \(1\) again, contradicting lower equality. Every label other than \(1\) is larger than the first record, so \(\pi_2=1\). Removing \((2,1)\) and lowering the remaining labels by two again preserves the record statistic and lower equality. Induction proves that every equality permutation consists of consecutive singleton and adjacent-swapped-pair blocks. Conversely, for such a concatenation, each singleton contributes \(1\), each swapped pair contributes \(2\), and their contributions sum to \(m\). The number of decompositions into blocks of size one or two is \(F_{m+1}\).

**4. Upper bound.** Since the \(r\) record values are distinct and increasing, \(i_s\leq m-r+s\), while their positions satisfy \(t_s\geq s\). Thus \(d_s\leq m-r\), and
\[
N(\pi)\leq r2^{m-r}\leq 2^{m-1}.
\]
The second inequality holds for every integer \(r\geq1\), with equality only for \(r=1\) or \(r=2\), since \(r\leq 2^{r-1}\), strictly when \(r\geq3\). If \(r=1\), equality in the first inequality requires that the first record be \(m\), so \(\pi_1=m\). If \(r=2\), equality requires records \(m-1,m\) at positions \(1,2\), so \((\pi_1,\pi_2)=(m-1,m)\). Both forms give equality by the exact record formula. The disjoint families contain \((m-1)!\) and \((m-2)!\) permutations, respectively, totaling \(m(m-2)!\) when \(m\geq2\).

## Verification
The standalone `check.py` compares the formula to an independent index-mask enumeration of all run subsequences for **every** permutation with \(m\leq5\). This verifies that the computed multiplicity counts distinct subsequence words and not embeddings. It also exhaustively enumerates every permutation through \(m=9\), checks both inequalities, checks the exact equality families, and checks the resulting family sizes. Invoke `python3 check.py`. Those finite checks corroborate but do not replace the preceding proof for unbounded \(m\).

## Relationship to prior work
The longest run subsequence problem was introduced as a genome-scaffolding optimization task by Schrinner et al. (2020); Dondi and Sikora (2021) proved hardness even with at most two occurrences per label. Asahiro et al. (2023) investigated approximation ratios for the same bounded-occurrence setting, including a \(4/3\) approximation for two occurrences. Later Asahiro et al. (2025) sharpened approximation bounds further. Those optimization and hardness results do not themselves give the exact number of distinct optima for the concatenation of two permutations or classify the minimizers and maximizers of that number. Here the exact optimum *length* is elementary, but its word-multiplicity ranges from linear to exponential. Numerically, the maximizer-family counts equal the established integer sequence OEIS A001048 after a shift; the new claim is the interpretation and exact equality characterization for longest-run-subsequence words, not novelty of that integer sequence.

## Limitations
The classification is limited to \(W_\pi=12\cdots m\,\pi\), not arbitrary double-occurrence words, words with different multiplicities, or general alphabet arrangements. It does not imply an improvement of the approximation ratio or hardness results for the unrestricted problem. The claim concerns distinct output subsequence *words*, not number of embeddings. The originality comparison covers the cited accessible primary papers, an indexed mathematical research database, and the inspected historical claims; unindexed or otherwise inaccessible prior results could still contain an equivalent statement. Independent assessment has not been performed.

## References
1. Y. Asahiro, H. Eto, M. Gong, J. Jansson, G. Lin, E. Miyano, H. Ono, and S. Tanaka, *Approximation Algorithms for the Longest Run Subsequence Problem*, CPM 2023, DOI 10.4230/LIPIcs.CPM.2023.2, publication 2023-06-21; earlier public technical-report record 2023-05-03, https://ipsj.ixsq.nii.ac.jp/records/225660.
2. S. Schrinner et al., *The Longest Run Subsequence Problem*, WABI 2020, DOI 10.4230/LIPIcs.WABI.2020.6.
3. R. Dondi and F. Sikora, *The Longest Run Subsequence Problem: Further Complexity Results*, CPM 2021, DOI 10.4230/LIPIcs.CPM.2021.14; preprint arXiv:2011.08119.
4. Y. Asahiro et al., *Approximability of Longest Run Subsequence and Complementary Minimization Problems*, WABI 2025, DOI 10.4230/LIPIcs.WABI.2025.3.
5. OEIS Foundation, *A001048*, https://oeis.org/A001048; this records the numerical sequence, not the run-subsequence interpretation.
