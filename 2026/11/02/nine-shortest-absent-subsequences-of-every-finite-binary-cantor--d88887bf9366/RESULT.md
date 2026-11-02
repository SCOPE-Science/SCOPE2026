# Nine shortest absent subsequences of every finite binary Cantor word

## Finding
For a binary word \(w\), a scattered subsequence is obtained by deleting letters without reordering the remaining letters. Write \(\operatorname{SAS}(w)\) for the set of words of the smallest absent length, over alphabet \(\{0,1\}\).

For every integer \(n\ge2\), define \(C_0=1\) and \(C_n=C_{n-1}0^{3^{n-1}}C_{n-1}\), and put \(m=2^n\). Then
\[
\boxed{\operatorname{SAS}(C_n)=\{00,01,11\}\,1^{m-3}\,\{00,10,11\}.}
\]
The nine words all have length \(m+1\). Consequently \(C_n\) contains every binary word of length \(m\) as a scattered subsequence, so \(\iota(C_n)=m\), and \(\lvert\operatorname{SAS}(C_n)\rvert=9\).

## Assumptions and scope
The alphabet is precisely \(\{0,1\}\). Occurrences are scattered, not contiguous; distinct missing strings, not embedding multiplicities, are counted. The result applies to complete Cantor iterates \(C_n\), \(n\ge2\), with \(C_1=101\) excluded. The length and number of ones in \(C_n\) are \(3^n\) and \(m=2^n\).

## Proof
**Lemma 1 (periodic comparison).** For every integer \(h\ge2\), put \(m=2h\) and \(G_m=(101000)^{h-1}101\). Its complete shortest absent language is \(\{00,01,11\}1^{m-3}\{00,10,11\}\).

To prove this, let \(N=6(h-1)+3\) be the length of \(G_m\), and define \(q_c(p)\) as the index of the first occurrence of letter \(c\) at or after position \(p\), taking \(q_c(p)=N\) if no such occurrence exists. All positions are zero-based. Let \(d(p)\) be the minimum length of a binary word absent as a subsequence of the suffix beginning at \(p\). The exact recurrence is
\[
d(p)=1+\min_{c\in\{0,1\}}\begin{cases}d(q_c(p)+1),&q_c(p)<N,\\0,&q_c(p)=N.\end{cases}
\]
Direct backward induction from \(p=N\), using the printed period \(101000\) and tail \(101\), gives for every \(0\le b\le h-2\)
\[
\begin{array}{c|ccc}
 p &6b&6b+1,6b+2&6b+3,6b+4,6b+5\\\hline
 d(p)&2(h-b)+1&2(h-b)&2(h-b)-1
\end{array}
\]
and, for the final four positions \(6(h-1)+r\), the respective values at \(r=0,1,2,3\) are \(2,2,1,1\). In particular \(d(0)=m+1\). A length-\(d(0)\) absent word follows precisely transitions \(p\xrightarrow{c}q_c(p)+1\) satisfying \(d(q_c(p)+1)=d(p)-1\), with the terminal nonexistent occurrence assigned distance zero. Substituting the displayed distance table yields exactly the following possible labels: in the first two transitions, \(00,01,11\); then \(m-3\) forced labels \(1\); and in the last two transitions, \(00,10,11\). Indeed, starting at position zero, the first two optimal transitions reach positions \(4,3,3\) respectively; the next optimal transition from either state is \(1\), reaching position \(7\). Thereafter each optimal transition is \(1\) until the state reaches \(N-2\). The final optimal transition is \(0\) to state \(N-1\) or \(1\) to state \(N\); from the former the final absent letter must be \(0\), and from the latter it may be either \(0\) or \(1\). The table and recurrence establish that no other optimal transitions exist. This proves Lemma 1, including the asserted universality index.

**Lemma 2 (gap comparison).** In \(C_n\), index the \(m\) occurrences of \(1\) from left to right, and denote by \(g_j\) the number of intervening zeros between its \(j\)th and \((j+1)\)th ones, for \(1\le j<m\). Then \(g_j=3^{\nu_2(j)}\), where \(\nu_2(j)\) is the exponent of two dividing \(j\). This follows by induction on \(n\): each copy of \(C_{n-1}\) retains its gaps, and the new central gap has length \(3^{n-1}\) at index \(j=2^{n-1}\). In particular, the end gaps are both exactly one, each odd-indexed gap is one, and each even-indexed gap is at least three.

Therefore \(G_m\) is a scattered subsequence of \(C_n\), with the \(m\) ones matched in order: the intervening gaps in \(G_m\) alternate between one and three zeros, and the corresponding gaps of \(C_n\) are at least as long. Every length-\(m+1\) binary word present in \(G_m\) is consequently present in \(C_n\). By Lemma 1, at most the nine displayed words are missing from \(C_n\).

**Lemma 3 (nine obstructions).** Conversely all nine displayed words are absent from \(C_n\). To embed an initial two-letter pattern \(a\in\{00,01,11\}\) before the central \(m-3\) ones, at least \(\ell(a)\) initial ones must be skipped, where \(\ell(00)=2,\ell(01)=1,\ell(11)=0\). The first two cases follow because the word begins in one and there is only one zero before its second one. Analogously, for a terminal pattern \(b\in\{00,10,11\}\), at least \(r(b)\) final ones must be skipped, where \(r(00)=2,r(10)=1,r(11)=0\), using that the word ends in one and has only one zero following its next-to-last one. Since \(\lvert a\rvert_1+\ell(a)=2\) and \(\lvert b\rvert_1+r(b)=2\), embedding \(a1^{m-3}b\) would require at least \((m-3)+2+2=m+1\) distinct ones. But \(C_n\) has exactly \(m\) ones, a contradiction.

Lemmas 1–3 show that the missing language at length \(m+1\) consists of exactly these nine words. Lemma 1 also shows all shorter words occur in \(G_m\) and therefore in \(C_n\). The claim follows. \(\square\)

## Verification
The standalone checker `checker.py` computes exact greedy subsequence automata, their minimum absent lengths, and all optimal absent words. It verifies the auxiliary family for \(2\le h\le15\), Cantor iterates \(2\le n\le4\), and independently enumerates all candidate strings at ranks two and three. The proof above, not bounded computation, establishes every rank.

## Relationship to prior work
Lü, Chen, Guo and Wen study permutation and factor complexity of the Cantor-like sequence [1], not shortest scattered absences. Kosche, Koß, Manea and Siemer provide general shortest-absent-subsequence definitions, characterizations and algorithms [2], but not this Cantor-family closed language. Chen, Lü and Wu study the different invariant of contiguous \(k\)-abelian complexity [3]. General computation of shortest absent words for each finite input does not by itself state the nine-word formula for all recursive ranks; the proof exploits Cantor gaps and a small optimal-transition graph.

## Limitations
Only complete finite Cantor iterates of rank at least two are classified. Arbitrary prefixes, Cantor-like substitutions with other gap parameters, and all longer minimal absent subsequences are not classified here. Historical-priority comparison is necessarily bounded and not an independent audit.

## References
[1] X.-T. Lü, J. Chen, Y.-J. Guo and Z. Wen, “On the permutation complexity of the Cantor-like sequences,” *Theoretical Computer Science* 616 (2016), 100–110, DOI: 10.1016/j.tcs.2015.12.022.

[2] M. Kosche, T. Koß, F. Manea and S. Siemer, “Absent Subsequences in Words,” arXiv:2108.13968 (first posted 2021); *Fundamenta Informaticae* 189 (2023), 199–240.

[3] J. Chen, X.-T. Lü and W. Wu, “On the \(k\)-abelian complexity of the Cantor sequence,” arXiv:1703.04063 (2017).
