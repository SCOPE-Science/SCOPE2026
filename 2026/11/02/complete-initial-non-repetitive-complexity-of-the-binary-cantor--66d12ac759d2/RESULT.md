# Complete initial non-repetitive complexity of the binary Cantor word

## Finding
Let \(\mathbf c=c_0c_1\cdots\) be the infinite fixed point beginning with \(1\) of \(\sigma(1)=101\) and \(\sigma(0)=000\). For every integer \(n\ge1\), let \(I(n)\) be the least index \(j\ge1\) for which there exists \(0\le i<j\) such that the length-\(n\) factors of \(\mathbf c\) beginning at \(i\) and \(j\) agree. Equivalently, \(I(n)\) is the number of pairwise distinct consecutive length-\(n\) factors beginning at the origin before the first repetition.

The exact function is \(I(1)=2\). For each integer \(k\ge0\) put \(m=3^k\). Then
\[
I(n)=\begin{cases}
2m,&m<n\le 2m,\\
3m+1,&2m<n<3m,\\
5m,&n=3m.
\end{cases}
\]
These cases partition all integers \(n\ge2\). The witness pairs for the first repetitions are, respectively, \((0,2m)\), \((3m,3m+1)\), and \((m,5m)\).

## Assumptions and scope
The alphabet is \(\{0,1\}\), coordinates are zero-based, and all factors are contiguous with overlaps permitted. A repeated factor means identical strings, not Abelian, cyclic, or subsequence equivalence. The word is the *infinite* Cantor fixed point, not a finite iterate. Powers \(m=3^k\) include \(m=1\). The case \(2m<n<3m\) is empty for \(m=1\).

Write \(C_k=\sigma^k(1)\), of length \(m=3^k\). The recursion \(C_{k+1}=C_k0^mC_k\) implies \(C_k\) begins and ends with \(1\), is a palindrome, and the infinite word begins, at blocks of length \(m\), with
\[
C_k\,0^m\,C_k\,0^{3m}\,C_k\,0^m\,C_k.
\]
All lower bounds below refer to genuinely distinct string factors, not to counts of candidate windows.

## Proof
**1. The Cantor support and its palindromic initial segments.** The \(2^k\) one-positions of \(C_k\), in increasing order, are \(p_0,\ldots,p_{2^k-1}\), with \(p_0=0\) and \(p_{2^k-1}=m-1\). If \(j\) has binary digits \(\epsilon_a\), then \(p_j=2\sum_{a\ge0}\epsilon_a3^a\). Direct binary carry gives, for \(1\le j<2^k\),
\[
p_j-p_{j-1}=1+3^{\nu_2(j)}.
\]
The palindrome symmetry of \(C_k\) follows also from its defining recursion. Consider the ordered gap list between the first \(t\) ones. If this list is palindromic and \(t\ge2\), let \(2^r\) be the largest power of two not exceeding \(t-1\). The unique maximal gap occurs at index \(2^r\); in a palindrome with \(t-1\) gaps its index must equal \(t/2\). Hence \(t=2^{r+1}\). The case \(t=1\) also is a power of two. Thus a palindromic initial gap list necessarily has \(t=2^r\). For \(r\le k\), the first and last \(2^r\) ones form copies of \(C_r\), of length \(\ell=3^r\).

**2. Distinct windows of length \(m+1\) at the first \(2m\) positions.** Write \(A=C_k\). The windows starting in \(0\le i<m\) are
\[
U_i=A[i:m]0^{i+1};
\]
those starting at \(j=m+h\), \(0\le h<m\), are
\[
V_h=0^{m-h}A[0:h+1].
\]
The words \(U_i\) are pairwise different since their terminal runs of zeros after the final one have lengths \(i+1\). Likewise the \(V_h\) are pairwise different since their initial runs of zeros before the first one have lengths \(m-h\).

Suppose that \(U_i=V_h\) across the two groups. Let \(t\) be their common number of ones. These are the final \(t\) ones of \(A\) in \(U_i\), and the initial \(t\) ones of \(A\) in \(V_h\). Because \(A\) is a palindrome, the final \(t\)-one gap list is the reversal of the initial \(t\)-one gap list. Equality of the windows therefore forces the initial gap list to be palindromic, hence \(t=2^r\) by Step 1. The case \(r=k\) would require \(i=0\) and \(h=m-1\); but \(U_0\) begins with \(1\), while \(V_{m-1}\) begins with \(0\). Thus \(r<k\).

Put \(\ell=3^r\). The first one of the final copy of \(C_r\) in \(A\) occurs at \(m-\ell\); the first one in the initial copy occurs at \(0\). Equality of the first-one positions within \(U_i,V_h\) forces
\[
m-\ell-i=m-h,\qquad h=i+\ell.
\]
The one immediately preceding the final copy of \(C_r\) is at \(m-2\ell-1\), whereas the one immediately following the initial copy is at \(2\ell\). For the two factors to contain exactly \(t\) ones, we require \(i\ge m-2\ell\) and \(h\le 2\ell-1\). Thus \(i\ge m-2\ell\ge\ell\), but \(i=h-\ell\le\ell-1\), a contradiction. This proves the claimed \(2m\) distinct windows for every \(k\ge0\).

**3. Two general block distinctness observations.** Fix *any* binary word \(A\) of length \(m\) that begins and ends with \(1\), and consider the block prefix \(A0^mA0^{3m}A0^m\). Internal gaps between ones in \(A\) are shorter than \(m\). Thus the pattern \(1 0^m1\) is a unique marker spanning the first two copies of \(A\); it cannot occur across the longer zero gap.

For length \(2m+1\), the windows starting at \(0\le i<m\) all contain this marker, at pairwise different relative positions \(m-1-i\). Windows with \(m\le i\le2m\) contain a complete second copy of \(A\), with distinct first-one positions \(2m-i\). Windows with \(2m<i<3m\) contain only a proper, nonempty suffix of the second \(A\), with distinct last-one positions \(3m-1-i\); they have fewer ones than the complete-copy windows. The window at \(3m\) is all zeros. None of the latter windows contains the marker. Consequently the length-\((2m+1)\) windows at all starts \(0,\ldots,3m\) are pairwise distinct.

For length \(3m\), again all windows with \(0\le i<m\) contain the unique marker at different relative positions. Windows with \(m\le i\le2m\) contain a complete second \(A\), their first-one positions ranging from \(m\) down to \(0\). Windows with \(2m<i<3m\) contain only a proper suffix of that \(A\), with all their ones in the first \(m\) relative positions. The window at \(3m\) is all zeros. Windows with \(3m<i<4m\) contain only a proper prefix of the third \(A\), with all their ones in the last \(m\) relative positions and distinct first-one positions. Finally, windows with \(4m\le i<5m\) contain a complete third \(A\), with first-one positions from \(2m\) down to \(m+1\). Full-copy windows have \(|A|_1\) ones, proper-copy windows have strictly fewer, and the early-suffix and late-prefix groups are separated by their positions of ones. Hence the length-\(3m\) windows at starts \(0,\ldots,5m-1\) are pairwise distinct.

**4. Matching upper bounds.** For \(m<n\le2m\), Step 2 implies no repetition at start smaller than \(2m\); the factors beginning at \(0\) and \(2m\) agree for the first \(2m\) letters because both start with \(A0^m\). Thus \(I(n)=2m\). For \(2m<n<3m\), Step 3 implies no repetition before start \(3m+1\); the factors at \(3m\) and \(3m+1\) are both \(0^n\), since they lie within the long run \(0^{3m}\). Thus \(I(n)=3m+1\). For \(n=3m\), Step 3 implies no repetition before \(5m\); the factors at \(m\) and \(5m\) are both \(0^m A0^m\). Thus \(I(3m)=5m\). Finally, \(I(1)=2\) from the initial symbols \(101\). The intervals form a partition, completing the proof.

## Verification
A standalone Python checker `checker.py` constructs an independent literal Cantor iterate, finds the first duplicate by storing actual factor strings, and compares its first index with the stated formula for every \(1\le n\le729\). It also checks the two universal block distinctness statements for all binary words beginning and ending in \(1\) through block length \(8\). The computation is finite corroboration only; all lengths are covered by the proof above.

## Relationship to prior work
Nicholson and Rampersad introduced and explicitly calculated initial non-repetitive complexity for Thue–Morse, Fibonacci and Tribonacci words, as well as general bounds and squarefree examples [1]. Their archived 2015 preprint does not study the binary Cantor fixed point. Work on Cantor-like factor complexity [2] establishes, in the binary case, the total number of distinct factors (\(2n-1\) for \(n\ge2\)), which does not determine the position of the first repetition in the origin-anchored factor sequence. The theorem supplies that different, order-sensitive statistic at every length. A distinct earlier theorem under other nomenclature cannot be categorically excluded.

## Limitations
This theorem concerns the specific infinite binary substitution \(1\mapsto101,0\mapsto000\), not arbitrary Cantor-like substitutions or finite iterates. Its first-repeat statistic depends on the origin; the result does not compute unrestricted non-repetitive complexity over all shifts. The computations through \(729\) do not replace the infinite proof, and priority is not independently established.

## References
[1] J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, first arXiv version 29 July 2015, arXiv:1507.08206, https://arxiv.org/abs/1507.08206. In particular, the definition and Theorems 6, 10 and 16 concern distinct substitution families.

[2] *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science 616 (2016), 100–110, DOI:10.1016/j.tcs.2015.12.022; the available article text gives \(p_{\mathbf c}(n)=2n-1\) for \(n\ge2\), a factor-count statistic rather than an anchored first-repeat statistic.
