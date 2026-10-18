# Five net occurrences and the complete repeated-prefix profile of period-doubling words

## Finding
For every integer \(n\geq3\), let \(D_n=\mu^n(0)\), where \(\mu(0)=01\) and \(\mu(1)=00\). Write \(N=2^n\) and \(h=N/8\). The word \(D_n\) has **exactly five net occurrences** of repeated nonempty factors, with the following complete list of zero-based (start, length) pairs:
\[
(0,4h-1),\quad(2h,3h-1),\quad(3h,3h-1),\quad(4h,4h-1),\quad(6h,2h).
\]
More strongly, let \(r_n(i)\) be the greatest common-prefix length of the suffix starting at position \(i\) with any other suffix of \(D_n\). Then the **complete maximal repeated-prefix profile** is
\[
r_n(i)=\begin{cases}
4h-1-i,&0\le i<2h,\\
5h-1-i,&2h\le i<3h,\\
6h-1-i,&3h\le i<4h,\\
8h-1-i,&4h\le i<6h,\\
8h-i,&6h\le i<8h.
\end{cases}
\]
In particular, every suffix has a nonempty repeated prefix. All indices are zero-based and all occurrences, including overlapping occurrences, are counted.

## Assumptions and scope
A repeated substring has at least two distinct starting positions. A *net occurrence* at \((i,\ell)\) is repeated but its one-symbol left extension, if present, and its one-symbol right extension, if present, occur only once in the same finite word. An extension beyond a boundary is regarded as unique. The result concerns precisely the complete morphic iterates \(D_n\) for integers \(n\geq3\); it does not assert the same count for arbitrary prefixes or other morphisms.

## Proof
**1. An eight-block identity and five matching ranges.** For a word \(W\), let \(\widetilde W\) be \(W\) with only its last bit complemented. The morphism satisfies \(D_{t+1}=D_t\widetilde D_t\) for all \(t\geq0\): the identity holds at \(t=0\), and morphing a word changes its last source letter only in the last output bit. Put \(X=D_{n-3}\) and \(Y=\widetilde X\). Both have length \(h\) and agree in their first \(h-1\) positions. Twice applying the identity gives
\[
D_n=X\,Y\,X\,X\,X\,Y\,X\,Y.
\]
Matching the suffix at each \(i\) to a second suffix at \(j\) supplies the five lower bounds in the displayed profile. In the corresponding five intervals, choose respectively
\[
j=i+4h,\quad j=i+h,\quad j=i-h,\quad j=i-4h,\quad j=i-6h.
\]
In the first four intervals, the compared block strings agree until their final possible \(X\)-versus-\(Y\) bit, producing matches of lengths \(4h-1-i\), \(5h-1-i\), \(6h-1-i\), and \(8h-1-i\), respectively. In the last interval, the final two blocks \(XY\) repeat the first two, yielding the entire remaining suffix, length \(8h-i\). Every bound is positive.

**2. A parity-separation lemma.** Every \(D_n\) contains no factor \(11\). Every character at an even position is \(0\); a three-character factor at an even position therefore has its first and third bits \(0\). Any three-character factor beginning at an odd position and with its first bit \(0\) must be \(001\): an odd-position \(0\) comes from a source \(1\), whose next source letter must be \(0\), because \(11\) never occurs. Thus suffixes beginning at positions of opposite parity have common-prefix length at most \(2\), including cases truncated by a word boundary.

**3. An induction giving the matching upper bound.** The base \(D_3=01000101\) has exact profile
\[
(r_3(0),\ldots,r_3(7))=(3,2,2,2,3,2,2,1),
\]
verified directly by comparing its eight suffixes. Let \(T=D_n\) have length \(N\) and the claimed profile. Write \(T'=\mu(T)=D_{n+1}\). For each old position \(a\), define \(d=r_n(a)\). Two same-parity new suffixes from different old positions agree for at most \(2d+1\) characters if they start at even positions \(2a\), and at most \(2d\) if they start at odd positions \(2a+1\): a mismatch of the next source symbols occurs in the second output character of the next morphism block, and at most its first, invariably zero, output character can still match. The opposite-parity bound from Step 2 is at most \(2\); since \(d\geq1\), it does not enlarge these estimates. Hence
\[
r_{n+1}(2a)\le2d+1,\qquad r_{n+1}(2a+1)\le2d.
\]
For \(0\le a<3N/4\), these inequalities are precisely the first four pieces of the asserted profile after doubling the indices (check even and odd indices separately). For \(3N/4\le a<N\), the inductive formula gives \(d=N-a\), the entire remaining suffix length. The actual new suffix lengths impose the sharper bounds
\[
r_{n+1}(2a)\le2(N-a),\quad r_{n+1}(2a+1)\le2(N-a)-1,
\]
which are exactly the last profile piece. Step 1 already proves equality via explicit matching partners at every index. This completes the induction for all \(n\geq3\).

**4. Net occurrences from adjacent profile entries.** Fix a finite word \(T\), and write \(r(i)\) for its longest repeated prefix length at \(i\). Any net occurrence at start \(i\) must have length exactly \(r(i)>0\): repetition requires length at most \(r(i)\), and uniqueness of the right extension requires length at least \(r(i)\) (including the boundary case). At that length, the left extension is unique precisely when \(i=0\) or \(r(i-1)<r(i)+1\), equivalently \(r(i)\ge r(i-1)\). In our piecewise-linear profile, \(r_n\) decreases by one at each interior index. The only nondecreasing steps occur at the four interval starts \(2h,3h,4h,6h\); the last of these is an equality. Together with the initial position \(0\), these give exactly the five stated net occurrences, whose lengths are the corresponding profile values.

## Verification
The standalone `check_period_net.py` independently computes a suffix array and longest-common-prefix array, derives the maximum repeated prefix for every starting position, and checks the entire piecewise formula and exact net occurrence list for each \(3\le n\le14\). Separately, a direct all-pairs suffix comparison and a direct repeated-substring/left-right-extension enumeration agree for \(3\le n\le7\). Recorded output appears in `check_period_net.log`. These finite checks corroborate but do not replace the induction proving all orders.

## Relationship to prior work
Guo and Kishi [1] introduced the exact net-occurrence classification problem for Fibonacci and Thue–Morse words and proved constants three and nine for those two families, respectively. Their full paper does not address period-doubling words. Kishi et al. [2] analyze occurrence-preserving morphisms and use minimal unique substrings for the same two families, without a period-doubling net-occurrence census. Banbara et al. [3] determine the smallest string-attractor position sets of period-doubling words, an invariant that does not specify net occurrences or the complete repeated-prefix profile. A characterization of shortest unique factors determines only shortest-length unique substrings, not every repeated-prefix length or the completeness of the five net occurrences. The claim is distinguished by its exact profile for **all** starting positions and its complete net-occurrence enumeration. The cited results do not directly imply this profile.

## Limitations
The result is restricted to finite dyadic iterates, and the external overlap search cannot establish absolute historical priority. Some equivalent characterization may be hidden under minimal-unique-substring or suffix-array terminology. No independent scientific review or machine formalization has been performed. The finite checker does not establish the infinite statement; the elementary induction does.

## References
[1] P. Guo and K. Kishi, *Net Occurrences in Fibonacci and Thue-Morse Words*, arXiv:2505.02307 (first posted 2025-05-05), CPM 2025, DOI 10.4230/LIPIcs.CPM.2025.16.

[2] K. Kishi, P. Guo, C. Urbina, and H. Bannai, *On Occurrence-Preserving Morphisms*, arXiv:2605.18034 (first posted 2026-05-18), CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.24.

[3] M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, and Y. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152 (first posted 2026-02-18); extended 2026 version.
