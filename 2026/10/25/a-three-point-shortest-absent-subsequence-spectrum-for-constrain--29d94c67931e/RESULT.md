# A three-point shortest-absent-subsequence spectrum for constrained circular binary words

## Finding
Let \(r\ge2\). In a circular binary word with exactly \(r\) ones, suppose the number of zeros between successive ones is always one or two, and no two one-zero gaps are cyclically adjacent. Denote the numbers of two-zero and one-zero gaps by \(D\) and \(S\), respectively. Then every marked rotation has shortest absent *scattered subsequences* of length \(r+1\). Across all \(N=3D+2S\) marked starting positions, the distribution of their number is exactly
\[
\#\{p:\lvert\operatorname{SAS}(w_p)\rvert=1\}=D,\qquad
\#\{p:\lvert\operatorname{SAS}(w_p)\rvert=2\}=2D,\qquad
\#\{p:\lvert\operatorname{SAS}(w_p)\rvert=3\}=2S.
\]
These are counts of cuts, not counts of distinct conjugates; coincident rotations of a periodic circular word are counted with their positions.

## Assumptions and scope
A scattered subsequence of a finite word is obtained by deleting any set of positions without changing the relative order of surviving positions. The universality index is the greatest integer \(k\) such that every binary word of length \(k\) is a scattered subsequence. The set \(\operatorname{SAS}(v)\) consists of all absent binary words of *minimum absent length* for \(v\). The circular gap tuple has \(r\ge2\) entries in \(\{1,2\}\), no cyclically adjacent entries equal to one, and at least one entry equal to two. Each of the \(N=3D+2S\) symbol positions determines a marked linear rotation \(w_p\).

## Proof
**Two comparison words.** Set \(A_r=(01)^r\). Every binary word of length \(r\) is a scattered subsequence of \(A_r\): select its successive letters from successive \(01\) blocks. An arbitrary binary word of length \(r+1\) containing an adjacent factor \(01\) is likewise embedded by using one \(01\) block for those two adjacent letters and the other \(r-1\) symbols in other blocks in their proper order. Conversely, a length-\(r+1\) word without the adjacent factor \(01\) is precisely \(1^j0^{r+1-j}\), for some \(0\le j\le r+1\); because each \(01\) block can contribute at most one letter in that nonincreasing pattern, no such word fits into \(A_r\). Thus these \(r+2\) nonincreasing words are precisely the shortest absences of \(A_r\).

Set \(B_r=0(10)^r=(01)^r0\). The word \(B_r\) contains \(A_r\). For \(0\le j\le r\), the word \(1^j0^{r+1-j}\) embeds into \(B_r\): use its first \(j\) ones and the following \(r+1-j\) zeros. Therefore the sole absent length-\(r+1\) subsequence of \(B_r\) is \(1^{r+1}\). In particular both comparison words contain all binary scattered subsequences of length \(r\).

**Cuts at a second zero.** Each of the \(D\) two-zero gaps has a distinguished *second zero*. Cutting immediately before it yields a word beginning and ending in zero. Select an initial zero, then each of the \(r\) ones and a zero following each one (including the final zero); these positions form \(B_r\) as a scattered subsequence. Thus its only absent length-\(r+1\) pattern is \(1^{r+1}\), which is indeed absent because the word has \(r\) ones. These \(D\) rotations each have exactly one shortest absent subsequence.

**Cuts at a first zero.** There are \(r\) cuts at the first zero following each one. Such a rotation begins with zero, ends with one, and contains \(A_r\) as a scattered subsequence. Hence only \(1^j0^{r+1-j}\) can be absent at length \(r+1\). Two always are absent: \(1^{r+1}\) (too many ones) and \(1^r0\) (there is no zero after the last one). The all-zero word \(0^{r+1}\) is present because the total number of zeros is \(r+D\ge r+1\). For \(1\le j\le r-1\), the greedy choice of the first \(j\) ones leaves the maximum possible number of zeros after the chosen ones. There are \(r-j\) internal gaps after those ones, each of length one or two. The required \(r+1-j\) following zeros exist exactly when at least one of those gaps is a two-zero gap. If \(j\le r-2\), at least two consecutive gaps occur, and the no-adjacent-one-gap hypothesis guarantees a two-zero gap. For \(j=r-1\), only the gap before the final one remains: an additional absence \(1^{r-1}00\) occurs precisely when this gap has length one. As the first-zero starting cut traverses all \(r\) cyclic gaps, the decisive internal gap is one-zero in exactly \(S\) cuts and two-zero in exactly \(D\) cuts. Consequently, these cuts contribute \(S\) occurrences of count three and \(D\) occurrences of count two.

**Cuts at a one.** The remaining \(r\) cuts begin at a one and end at a zero. Reversing the linear word produces a rotation-shaped word beginning at zero and ending at one, with the same cyclic gap restrictions. Reversal bijectively maps absent subsequences to absent reversed subsequences, preserving the count and minimum absent length. The preceding argument therefore gives another \(S\) cuts of count three and \(D\) cuts of count two.

Every cut contains \(A_r\) or \(B_r\), hence is \(r\)-universal, and every cut lacks \(1^{r+1}\), hence its shortest absent length is exactly \(r+1\). All \(D+2r=3D+2S\) cuts have been classified, proving the claimed distribution.

## Verification
The accompanying `verify.py` uses a next-occurrence dynamic program for minimum absent length and its number, and independently enumerates and tests every binary candidate of that minimum length. It checked all \(119\) labeled admissible cyclic gap tuples for \(2\le r\le8\), totaling \(2146\) marked cuts, with no discrepancy. The condition is substantive: for the gap tuple \((1,1,2)\), which violates the no-adjacent-one-gap assumption, counts one, two, three, and four all appear in the rotation spectrum.

To reproduce, run `python3 verify.py` with a standard Python 3 installation, from the directory containing this document and checker. The program requires no outside data or packages.

## Relationship to prior work
Generic scattered-subsequence universality and shortest-absent-subsequence algorithms provide the objects and comparison principles, but do not by themselves determine the full number-of-absences distribution across marked rotations of gap-constrained circular words. Barker and collaborators study circular universality indices, including behavior under conjugacy; this addresses universality rather than the three-point spectrum of shortest absent subsequence *counts*. Kosche and collaborators characterize general absent subsequences, but do not give this cyclic rotation histogram. Earlier automata-theoretic work on scattered subsequences is background only. The result is an exact additional specialized structural statement, not a claim that the earlier algorithms fail on this family.

## Limitations
The hypothesis of nonadjacent one-zero gaps is required for this three-point law; the excluded family can exhibit additional values. The theorem is not a classification for arbitrary circular binary words, other alphabets, or minimum absent *contiguous factors*. The computational checks cover only the stated finite range and do not replace the all-length proof. Priority cannot be certified from the inspected sources alone, and independent verification remains unperformed.

## References
- Alexander Okhotin, “On the State Complexity of Scattered Substrings and Superstrings,” *Fundamenta Informaticae*, published online April 1, 2010, DOI: 10.3233/FI-2010-252.
- Barker et al., “Scattered Factor-Universality of Words,” arXiv:2003.04629. In particular Section 4 on circular universality.
- Kosche, Koß, Manea and Siemer, “Absent Subsequences in Words,” arXiv:2108.13968. Definitions and shortest-absence results.
