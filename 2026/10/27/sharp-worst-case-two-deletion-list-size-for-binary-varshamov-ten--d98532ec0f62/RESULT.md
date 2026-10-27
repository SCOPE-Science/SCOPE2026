# Sharp worst-case two-deletion list size for binary Varshamov–Tenengolts codes

## Finding
For every integer \(n\geq 2\), every syndrome \(a\in\{0,\ldots,n\}\), and every binary word \(y\) of length \(n-2\),
\[
\left|\{x\in\operatorname{VT}_a(n): y\preceq x\}\right|\leq \left\lfloor\frac n2\right\rfloor+1,
\]
where \(y\preceq x\) denotes the subsequence relation. This bound is exactly sharp simultaneously for every \(n\) when \(a=0\) and \(y=0^{n-2}\). Hence the maximum two-deletion list size, maximized over all syndrome classes and received words of length \(n-2\), is precisely \(\lfloor n/2\rfloor+1\).

## Assumptions and scope
The alphabet is binary. The code is the classical VT checksum class
\[
\operatorname{VT}_a(n)=\left\{x\in\{0,1\}^n:\sum_{i=1}^n ix_i\equiv a\pmod{n+1}\right\}.
\]
Every received word is obtained by **exactly two deletions** (and no substitutions). Codewords, not deletion-position choices, are counted. No bound on the complexity of computing this list is asserted. The standard fact that each VT syndrome class uniquely corrects one deletion is used; a concise justification is given in the proof.

## Proof
**1. The intermediate insertion layer.** Fix \(n\ge3\), put \(m=n-2\), and fix \(y\in\{0,1\}^m\). Let \(Z\) be its set of distinct one-insertion supersequences of length \(m+1=n-1\). There are exactly \(m+2=n\) such words: the \(2(m+1)\) nominal insertions have exactly \(m\) adjacent equal-symbol collisions, counted with their multiplicities within runs. For a length-\(n\) two-insertion supersequence \(x\), let \(A_x\subseteq Z\) consist of the length-\(n-1\) words obtained by one deletion from \(x\) that still contain \(y\) as a subsequence. This set is nonempty.

For two different members \(x,x'\) of the same VT checksum class, \(A_x\cap A_{x'}=\varnothing\): otherwise some \(z\) of length \(n-1\) would be a one-deletion descendant of both codewords, contradicting the single-deletion property of a VT checksum class. Therefore, writing \(L\) for the size of the two-deletion decoding list and \(s\) for the number of its members with \(|A_x|=1\),
\[
 n=|Z|\ge \sum_x|A_x|\ge s+2(L-s)=2L-s.
\]

For completeness, the single-deletion property follows directly from the checksum. Inserting a bit \(b\) after the first \(k\) positions of a length-\(n-1\) word \(z\) changes its *integer* checksum by \(s_k+(k+1)b\), where \(s_k\) is the number of ones strictly after gap \(k\). For gaps \(k<\ell\), the difference between these increments is \(s_k-s_\ell+(k+1)b-(\ell+1)d\). If \(b=d=0\), this difference vanishes exactly when the intervening symbols are all zero, in which case both insertions give the same word; for \(b=d=1\), vanishing likewise means all intervening symbols are one and the inserted words coincide. If \(b\ne d\), the difference is a nonzero integer of absolute value at most \(n\). Thus distinct inserted words have distinct checksums modulo \(n+1\).

**2. One-intermediate candidates.** Suppose \(|A_x|=1\). Choose two positions of \(x\) whose deletion produces \(y\). Removing either of these positions first produces two elements of \(A_x\), hence the same length-\(n-1\) word. For a binary word, deleting positions \(i<j\) gives identical descendants only when all letters from position \(i\) through \(j\) are equal: compare the shifted letters in positions \(i,\ldots,j-1\). Hence the two removed positions lie in one constant run. Equivalently, \(x\) is produced by inserting a block \(cc\) into \(y\), either enlarging an existing \(c\)-run or creating a new length-two \(c\)-run where neighboring original symbols, if present, are \(1-c\). These descriptions yield a canonical finite set of potential singleton words: extend each existing run at its end; insert an opposite pair at every interior equal-letter gap; insert an opposite pair at each terminal gap. The count is \(r+(m-r)+2=m+2=n\), where \(r\) is the number of runs of \(y\). Every singleton-intermediate word belongs to this set; we do not need the converse.

**3. No checksum class contains three singleton candidates.** Index the gap of each canonical insertion by the number \(k\) of original symbols to its left, \(0\le k\le m\), and let \(c\) denote the inserted bit. If \(s_k\) is the number of ones strictly to the right of that gap, the difference between ordinary *integer* checksums of the inserted word and \(y\) is
\[
 \Delta(k,c)=2s_k+(2k+3)c.
\]
For \(c=0\), this equals \(2s_k\). It is distinct for different canonical zero-pair insertions: if two distinct insertion gaps had the same number of ones to their right, all symbols between the gaps would be zero, but among consecutive gaps separated only by zeros, only one can be a canonical zero-pair insertion (the end of the containing zero-run). For \(c=1\), if \(z_k\) denotes the number of zeros to the left of the gap and \(w\) is the number of ones in \(y\), then
\[
 \Delta(k,1)=2(w+z_k)+3.
\]
These values are likewise distinct, since among gaps separated only by ones there is at most one canonical one-pair insertion. Values from the two cases have opposite parity, so **all canonical checksum increments are different integers**. Furthermore,
\[
 0\le\Delta(k,c)\le 2m+3=2n-1.
\]
No residue modulo \(n+1\) can occur more than twice among distinct integers in this interval. Since a candidate \(x\) and \(y\) have the same fixed difference between their integer checksums up to \(\Delta\), at most two singleton-intermediate candidates can belong to a given VT syndrome: \(s\le2\).

**4. Upper bound and attainment.** The intermediate count now gives \(2L\le n+2\), whence \(L\le\lfloor n/2\rfloor+1\). To attain it, take \(y=0^{n-2}\) and syndrome zero. Its all-zero supersequence is in \(\operatorname{VT}_0(n)\). Every other length-\(n\) supersequence of \(y\) in this syndrome has precisely two ones at positions \(i<j\) satisfying \(i+j=n+1\). There are exactly \(\lfloor n/2\rfloor\) such pairs. The possible one-one supersequences have nonzero checksum modulo \(n+1\). Thus the list size is \(\lfloor n/2\rfloor+1\). Finally, for \(n=2\), the received word is empty and the two words \(00,11\) lie in \(\operatorname{VT}_0(2)\); the upper bound of two is automatic. This completes the proof.

## Verification
The accompanying standalone Python file `verify_vt_two_deletion.py` independently constructs both insertion layers as **sets** of distinct words and computes every checksum class. It checks every received word at lengths \(2\) through \(11\), then 24 reproducibly sampled received words at each of lengths \(12,15,20,26,35,45\); 1,167 received words in total. Besides the list bound and sharp witness, the checks cover pairwise-disjoint intermediate sets, the canonical singleton description and all checksum-increment identities. The output file `verification_output.txt` records a successful completion marker. This is finite corroboration; the preceding argument proves all lengths.

## Relationship to prior work
Wachter-Zeh, *List Decoding of Insertions and Deletions* (arXiv:1701.02612, Section VI), describes an exact two-deletion list decoder and the general upper bound of \(n\) candidate words for VT codes. Banerjee, Con, Wachter-Zeh and Yaakobi, *On the Average List Size of VT Codes under Two Insertions or Two Deletions* (arXiv:2610.15767, first submitted 2026-10-11, especially Section IV), give an average-case lower bound of \(n/2-10\) over the checksum classes and received words. The present exact *worst-case* extremum is logically distinct from that average lower bound, and sharpens the earlier worst-case upper bound. The classical single-deletion property of VT codes is used, not claimed as new.

## Limitations
The maximum is over all syndrome classes; equality for every individual syndrome is not asserted. The result is limited to binary alphabets and exactly two deletions. It does not improve the decoding time bound, and priority relative to every unindexed or unavailable publication is not certified. Independent verification has not been performed.

## References
1. A. Wachter-Zeh, *List Decoding of Insertions and Deletions*, arXiv:1701.02612 (first publicly submitted 2017-01-10), Section VI. https://arxiv.org/abs/1701.02612
2. A. Banerjee, R. Con, A. Wachter-Zeh, E. Yaakobi, *On the Average List Size of VT Codes under Two Insertions or Two Deletions*, arXiv:2610.15767 (first publicly submitted 2026-10-11), Section IV. https://arxiv.org/abs/2610.15767
3. V. I. Levenshtein, *Binary codes capable of correcting deletions, insertions, and reversals*, Soviet Physics Doklady 10 (1966), classical single-deletion background.
