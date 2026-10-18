# Exact cyclic palindromic-deletion spectrum of binary order-five de Bruijn cycles

## Finding
Let \(\mathcal B_5\) denote the binary de Bruijn cycles of order five modulo circular rotation. For \(B\in\mathcal B_5\), let \(B^{(r)}\) denote the 32-letter linearization at cut \(r\), and let \(\operatorname{LPS}(w)\) be the maximum length of a palindromic **scattered subsequence** of a linear word \(w\). Define
\[
L(B)=\max_{0\le r<32}\operatorname{LPS}(B^{(r)}).
\]
The complete value distribution over the \(2048\) cycles is
\[
\#\{B:L(B)=k\}=\begin{cases}
76&k=25,\\
114&k=26,\\
1380&k=27,\\
286&k=28,\\
192&k=29,\\
0&\text{otherwise}.
\end{cases}
\]
Consequently, the sharp smallest and largest cyclic longest-palindromic-subsequence lengths are \(25\) and \(29\). Their attaining cycle counts are \(76\) and \(192\), respectively. If a cycle is chosen uniformly from \(\mathcal B_5\),
\[
\mathbb E[L]=\frac{13925}{512},\qquad
\operatorname{Var}(L)=\frac{178215}{262144}.
\]
The equivalent minimum number of deletions required to turn *some* linearization of the cycle into a palindrome is \(32-L(B)\), hence takes values \(7,6,5,4,3\) with these corresponding frequencies. After identifying rotations, reversal, and bit complementation, the number of symmetry orbits of sizes two and four in each level is, respectively, \((4,17),(1,28),(22,334),(5,69),(0,48)\) for levels \(25,26,27,28,29\). Thus there are exactly \(528\) such orbits.

## Assumptions and scope
A binary de Bruijn cycle of order five is a circular binary word of length \(32\) in which each length-five binary word appears exactly once as a cyclic factor. Rotations are identified, but not a priori reversals or bit complements. A subsequence may omit letters, but the retained letters respect the linear order of exactly one length-32 cut of the cycle. No symbol can be used twice and no traversal longer than one circumference is allowed. This is **not** a problem about contiguous palindromic factors, multiple windings, or freely permuting symbols.

## Proof
**Complete parametrization.** Form the order-four binary de Bruijn directed graph. Its sixteen vertices are four-bit words and its thirty-two edges are five-bit words. Edge \(e\), labeled by integer \(0\le e<32\), leaves vertex \(\lfloor e/2\rfloor\) and enters vertex \(e\bmod 16\). Each vertex has exactly two incoming and two outgoing edges. An Eulerian tour makes, at every vertex, a bijective pairing between the two incoming edges and the two outgoing edges. There are precisely two such pairings per vertex, so all possible tours are covered by \(2^{16}=65536\) local assignments. Starting at the unique edge labeled `00000`, follow the successor of each incoming edge. The assignment specifies a de Bruijn cycle if and only if the resulting edge permutation is one cycle of length \(32\). Conversely, any order-five de Bruijn cycle induces exactly this pairing assignment and admits a unique rooted word at `00000`. Therefore accepted assignments enumerate all rotation classes exactly once.

**Palindrome optimization.** For an arbitrary linearization \(w\), define \(F_w(i,j)\) for a nonempty interval as the longest palindromic subsequence length. Set \(F_w(i,i)=1\), and regard an empty interval as zero. For \(i<j\), the standard end-pair recurrence is
\[
F_w(i,j)=\begin{cases}
2+F_w(i+1,j-1),&w_i=w_j,\\
\max\{F_w(i+1,j),F_w(i,j-1)\},&w_i\ne w_j.
\end{cases}
\]
In the mismatch case, any palindrome must omit one endpoint. In the matching case, there exists a longest palindrome using both matching ends, so the first case is optimal. Induction on interval length proves the recurrence. Applying it to all \(32\) cuts yields exactly \(L(B)\). The implementation independently compares every result with the length of the longest common subsequence of the same linearization and its reversal, by a separate two-dimensional LCS recurrence.

**Exhaustion and arithmetic.** The attached `verify.py` implements both the local-pairing enumeration just proved complete and a second generator that traverses unused outgoing edges by depth-first Eulerian search with the `00000` edge fixed first. The resulting canonical sets are equal and each contains exactly \(2048\) words. It evaluates the two independent palindrome-length recurrences on all \(32\) cuts of every word, groups the exact results, and checks the accompanying `spectrum.csv` row for each cycle. This gives precisely the five multiplicities stated in the finding. Exhaustively taking the reversal/complement orbit of each canonical word gives the five pairs of symmetry-orbit counts. Summing the multiplicities and their first and second powers gives the displayed exact moments. As every valid cycle is present exactly once, no additional order-five values or cycles are excluded by sampling.

For concrete minimum and maximum representatives, in each case rooted at `00000`, take respectively `00000100011001111101101010010111` and `00000100011001010111110110100111`. The verifier proves their optimal cyclic lengths are \(25\) and \(29\); the full enumeration proves that no more extreme values occur.

## Verification
Run `python3 verify.py` with `spectrum.csv` beside it. The program rebuilds the cycles independently by two constructions, evaluates independent dynamic programs across all \(65536\) rooted cuts, checks every CSV entry, and verifies exact multiplicities, moments, and reversal/complement orbit counts. The verification output begins `VERIFY_OK cycles=2048 pairings=65536 DFS=2048 independent_LPS_methods=2` and reports the five exact frequencies. The CSV specifies every canonical cycle, cyclic longest-palindromic-subsequence length, and equivalent minimum deletion count. No random sampling, floating-point arithmetic, external packages, or precomputed external data are used.

## Relationship to prior work
The longest-palindromic-subsequence and longest-common-subsequence problems are classical. Chowdhury and collaborators develop algorithms for palindromic subsequences in 2011; Brodal, Fagerberg, and Rysgaard clarify the relation to LCS with reversal. Neither derives a frequency distribution over de Bruijn cycles. OEIS A318916 records the unrestricted minimum circular palindromic-subsequence length for binary circles, with its length-32 entry equal to \(24\). That *unrestricted* minimum does not determine the present de Bruijn-constrained minimum \(25\), much less the complete frequency spectrum. Results counting distinct **contiguous** palindromic factors are logically different from optimization over scattered subsequences after deletions. The classification here concerns the exact finite family only.

## Limitations
Only binary order-five cycles are classified; no formula for arbitrary de Bruijn orders or arbitrary alphabets is asserted. The finite classification relies on the stated exhaustive computation and on the independently checkable completeness arguments for the enumerators and recurrences. The mathematical literature comparison does not eliminate the possibility of an older unindexed numerical census. The OEIS unrestricted benchmark is contextual, not an independently re-proved general theorem here.

## References
1. S. R. Chowdhury, M. M. Hasan, S. Iqbal, and M. S. Rahman, *Computing a Longest Common Palindromic Subsequence*, arXiv:1110.5296, first submitted 2011-10-24. https://arxiv.org/abs/1110.5296
2. G. S. Brodal, R. Fagerberg, and C. M. Rysgaard, *On Finding Longest Palindromic Subsequences Using Longest Common Subsequences*, ESA 2024, DOI:10.4230/LIPIcs.ESA.2024.35. https://doi.org/10.4230/LIPIcs.ESA.2024.35
3. J. Shallit and contributors, OEIS A318916, *Minimum length of longest palindromic subsequence over binary circular words*. https://oeis.org/A318916
