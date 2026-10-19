# Stable shortest-absent subsequence spectra of Cantor-like morphic words

## Finding
Let \(r\ge 1\) be an integer and let the binary uniform morphism be
\[\mu_r(1)=1\,0^r\,1,\qquad \mu_r(0)=0^{r+2}.\]
For every integer \(k\ge2\), put \(W_{r,k}=\mu_r^k(1)\) and \(m=2^k\). Let \(\operatorname{SAS}(w)\) denote the set of shortest binary words that are **not** scattered subsequences of \(w\), and let \(\iota(w)\) be the largest length at which every binary word occurs as a scattered subsequence. Then
\[\boxed{\iota(W_{r,k})=m.}\]
Moreover, the entire shortest-absent-subsequence set is
\[
\boxed{
\operatorname{SAS}(W_{r,k})=
\begin{cases}
\{a\,1^{m-3}b:a\in\{\texttt{00},\texttt{01},\texttt{11}\},\ b\in\{\texttt{00},\texttt{10},\texttt{11}\}\},&r=1,\\[2mm]
\{x\,1^{m-1}y:x,y\in\{0,1\}\},&r\ge2.
\end{cases}
}
\]
The two sets contain exactly nine and four distinct words, respectively. All these missing words have length \(2^k+1\). Thus the number of shortest absent subsequences is independent of \(k\), but changes sharply between the ordinary Cantor word and all larger-zero-block Cantor-like words.

## Assumptions and scope
A scattered subsequence is formed by retaining letters at strictly increasing positions; the retained letters need not be adjacent. The alphabet for universality is \(\{0,1\}\), even when other symbols do not occur in some short boundary example. The theorem concerns the **initial full morphic block** of length \((r+2)^k\), not arbitrary factors, rotations, or intermediate prefix lengths. All statements quantify over every integer \(r\ge1\) and every integer \(k\ge2\).

The morphism fixes a one-sided binary word beginning in \(1\), and \(W_{r,k}\) is its prefix of length \((r+2)^k\). In particular \(W_{1,k}\) is the classical Cantor-word prefix of length \(3^k\). The prefix has exactly \(2^k\) ones, since every \(1\) produces two ones and \(0\) produces none. It satisfies the exact concatenation identity
\[
W_{r,k+1}=W_{r,k}\,0^{r(r+2)^k}\,W_{r,k}.
\]

## Proof
**Finite initial step.** Direct greedy subsequence matching against the thirty-two binary five-letter words gives:
\[
\begin{aligned}
W_{1,2}&=\texttt{101000101},\\
W_{2,2}&=\texttt{1001000000001001}.
\end{aligned}
\]
Both contain all sixteen binary words of length four. Their respective missing words of length five are exactly
\[
\begin{aligned}
\operatorname{SAS}(W_{1,2})&=
\{\texttt{00100},\texttt{00110},\texttt{00111},\texttt{01100},\texttt{01110},\texttt{01111},\texttt{11100},\texttt{11110},\texttt{11111}\},\\
\operatorname{SAS}(W_{2,2})&=\{\texttt{01110},\texttt{01111},\texttt{11110},\texttt{11111}\}.
\end{aligned}
\]
For \(r\ge2\), the word \(W_{2,2}\) is a scattered subsequence of \(W_{r,2}=1\,0^r1\,0^{r(r+2)}1\,0^r1\), since all three zero blocks are at least as long as those at \(r=2\). Thus every binary four-letter word occurs in \(W_{r,2}\), while every five-letter word occurring in \(W_{2,2}\) also occurs in \(W_{r,2}\). Each of the four remaining candidates \(x1^3y\) is absent from every \(W_{r,2}\): an initial \(0\) skips the first \(1\), a final \(0\) skips the last \(1\), and the candidate demands one more occurrence of \(1\) than can remain. This gives the stated four-word set for all \(r\ge2\).

**Inductive universality.** Assume the full claim at exponent \(k\ge2\) and write \(A=W_{r,k}\), \(m=2^k\), and \(H=r(r+2)^k\). Every binary length-\(2m\) word can be split into two length-\(m\) words, each a subsequence of \(A\); consequently it is a subsequence of \(A0^H A=W_{r,k+1}\). Since this concatenated word has only \(2m\) ones, the word \(1^{2m+1}\) is absent. Hence \(\iota(W_{r,k+1})=2m\).

**Restriction to two forbidden halves.** Let \(v\) be any absent binary word of length \(2m+1\) from \(A0^H A\). Its first \(m+1\) letters must be absent from \(A\); otherwise these letters could be embedded in the left copy and the remaining \(m\) letters in the right copy. Similarly, its last \(m+1\) letters must be absent from \(A\). The two forbidden halves overlap in the single central letter \(v_m\) (zero-based indexing).

**Larger-zero-block case \(r\ge2\).** By induction, each forbidden half is of the form \(x1^{m-1}y\), with the two boundary letters freely chosen from \(\{0,1\}\). The overlap forces
\[v=x\,1^{m-1}z\,1^{m-1}y\quad (x,z,y\in\{0,1\}).\]
If \(z=0\), embed the first \(m\) letters in the left \(A\), the central zero in \(0^H\), and the final \(m\) letters in the right \(A\). If \(z=1\), then \(v=x1^{2m-1}y\). Such a word is absent: if \(x=0\), the first one of \(A0^HA\) must be skipped; if \(y=0\), its last one must be skipped. The number of remaining ones is at most \(2m-2+x+y\), whereas \(v\) demands \(2m-1+x+y\) ones (interpreting \(x,y\) numerically). These four candidates are therefore precisely the absent words.

**Ordinary Cantor case \(r=1\).** Set \(L=\{\texttt{00},\texttt{01},\texttt{11}\}\) and \(R=\{\texttt{00},\texttt{10},\texttt{11}\}\). The two forbidden halves must belong to \(L1^{m-3}R\), forcing
\[v=a\,1^{m-3}T\,1^{m-3}b,\qquad a\in L,\quad b\in R,\]
where the overlapping middle triple \(T\) is one of \(\texttt{000},\texttt{001},\texttt{100},\texttt{101},\texttt{111}\): the first two bits of \(T\) belong to \(R\), and the final two bits belong to \(L\).

Every candidate with a zero in the middle triple embeds in \(A0^H A\), since \(H\ge3\). For \(T=\texttt{000}\), use the left and right universal copies for words of lengths \(m-1\) and \(m-1\), with \(\texttt{000}\) in the central zero block. For \(T=\texttt{001}\), use lengths \(m-1\) and \(m\), with \(\texttt{00}\) centrally; for \(T=\texttt{100}\), use lengths \(m\) and \(m-1\), with \(\texttt{00}\) centrally; and for \(T=\texttt{101}\), use lengths \(m\) and \(m\), with \(\texttt{0}\) centrally. Each end word of length at most \(m\) embeds by induction.

Only \(T=\texttt{111}\) remains; these nine candidates form \(a1^{2m-3}b\). Each \(W_{1,j}\) for \(j\ge2\) begins and ends in \(\texttt{101}\). Matching \(a\in L\) necessarily omits at least \(2-|a|_1\) of the first two ones, while matching \(b\in R\) necessarily omits at least \(2-|b|_1\) of the last two ones (here \(|a|_1\) counts ones). These four boundary ones are distinct. Consequently at most \(2m-4+|a|_1+|b|_1\) ones can be retained, but \(a1^{2m-3}b\) requires \(2m-3+|a|_1+|b|_1\). All nine candidates are absent. This proves the complete induction. \(\square\)

## Verification
The standalone `verify.py` performs independent morphic and positional-digit constructions. For each sampled pair \((r,k)\), it checks the word length, one-count, greedy arch count, absence of every formula-listed word, and the **exact number** of missing words of length \(2^k+1\). The exact number is computed by dynamic programming over the earliest-occurrence deterministic subsequence automaton, not by sampling candidate words. For the two finite base words, it directly tests all \(2^5=32\) possible five-letter words.

Executed checks: \(r=1\) through \(k=8\); \(r=2\) through \(k=6\); \(r=3\) through \(k=5\); \(r=4,5\) through \(k=4\); and \(r=7\) through \(k=3\), in all cases beginning at \(k=2\). The program exits with `VERIFY_OK`. The proof, rather than finite extrapolation, establishes every exponent and parameter.

## Relationship to prior work
Lü, Chen, Guo, and Wen (available online 29 December 2015) analyze **ordinary contiguous-factor and permutation complexity** of Cantor-like words, including exactly the substitutions considered here. Their complexity functions do not specify which binary words fail to occur as **scattered** subsequences of a finite morphic prefix.

Kosche, Koß, Manea, and Siemer (arXiv:2108.13968, first posted 31 August 2021) develop the general framework of subsequence universality, arch factorization, and minimal/shortest absent subsequences; in particular their structural and algorithmic principles are prior work. Their inspected full text does not state the present explicit all-parameter Cantor-like formula. The new contribution is the exact generation-by-generation classification, including the nine-to-four phase transition. General upper bounds, algorithms, or extremal enumerations for arbitrary words do not alone specify this morphic family's exact forbidden sets.

## Limitations
This result concerns the finite complete morphic blocks \(\mu_r^k(1)\) for \(k\ge2\). It does not classify non-morphic prefix lengths, arbitrary factors, or **all** minimal absent subsequences, which can be longer than the shortest. The formula is not asserted at \(k=1\), where exceptional short-word behavior occurs. No independent scientific review is claimed. A possible equivalent result in incompletely indexed literature remains an originality risk.

## References
- X.-T. Lü, J. Chen, Y.-J. Guo, Z.-X. Wen, “On the permutation complexity of the Cantor-like sequences,” *Theoretical Computer Science* 616 (2016), 100–110; available online 2015-12-29. DOI: 10.1016/j.tcs.2015.12.022.
- M. Kosche, T. Koß, F. Manea, S. Siemer, “Absent Subsequences in Words,” *Fundamenta Informaticae* 189 (2023), 199–240. arXiv:2108.13968 (first version 2021-08-31); DOI: 10.46298/fi.9221.
