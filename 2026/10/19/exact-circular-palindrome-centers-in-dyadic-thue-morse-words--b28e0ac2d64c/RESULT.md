# Exact circular palindrome centers in dyadic Thue–Morse words

## Finding

For every integer \(k\ge4\), the circular Thue–Morse word of length \(N=2^k\) has an explicit maximal even-palindrome radius at *every* gap. There are precisely two gap centers supporting an even palindrome of length \(N\). Every other gap has radius at most \(N/8\) for even \(k\), and at most \(3N/16\) for odd \(k\); both bounds are sharp, with exactly four maximizing off-axis gaps. Accordingly, for each even length \(L\) strictly exceeding twice the corresponding bound and at most \(N\), there are exactly two distinct circular palindromic factors of length \(L\), and they are binary complements.

The complete center classification follows. Write \(t_m(i)\) for the parity of the binary digit sum of \(i\bmod 2^m\), and let \(R_k(c)\) denote the largest integer \(r\le N/2\) such that
\[
t_k(c-j)=t_k(c+j-1)\qquad(1\le j\le r),
\]
all indices being taken modulo \(N\). Here \(c\) is the gap between positions \(c-1\) and \(c\). The two full-radius gaps are
\[
H_k=\begin{cases}\{0,N/2\},&k\text{ even},\\\{N/4,3N/4\},&k\text{ odd}.\end{cases}
\]
For \(c\in H_k\), \(R_k(c)=N/2\). For any other \(c\), one has \(R_k(c)=0\) when \(c=0\) or when \(\nu_2(c)\) is even. Otherwise write \(v=\nu_2(c)\), \(m=k-v\ge3\), \(u=c/2^v\) (odd), and \(h=(u-1)/2\). Then
\[
\boxed{R_k(c)=2^v\left(1+2\mathbf1_{\{t_{m-1}(h-1)=t_{m-1}(h+1)\}}\right).}
\]
For even \(k\), the four off-axis centers attaining \(N/8\) are \(N/8,3N/8,5N/8,7N/8\). For odd \(k\), those attaining \(3N/16\) are \(N/16,7N/16,9N/16,15N/16\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), \(t_k(i)\) is defined at the residues \(0\le i<2^k\) and extended periodically, and a circular factor has length at most one complete circuit. The centers are gaps, not positions carrying a symbol. Thus \(R_k(c)\) is a half-length, not a word length. Every stated classification is exact for all \(k\ge4\); no claim is made about longer repeated traversals or other morphic sequences. The indicator is one when its subscripted equality holds and zero otherwise.

## Proof

**Step 1: No cyclic palindromes of odd length at least five.** The square of the Thue–Morse substitution is \(B(0)=0110\), \(B(1)=1001\), with the uniform form \(B(a)=a\,(1-a)\,(1-a)\,a\). Since \(t_k\) is the circular concatenation of these four-letter blocks for \(k\ge2\), any circular factor of length five begins at offset \(0,1,2\), or \(3\) within \(B(a)B(b)\). At offset zero, letters 2 and 4 (one-based) differ. At offset three, letters 2 and 4 differ. At offset one or two, the two palindrome equations would simultaneously require \(a=b\) and \(a=1-b\), which is impossible. These four cases cover all cyclic seams. Therefore a palindromic factor of length five cannot exist; nor can any longer odd palindrome, since its central length-five factor would be palindromic.

**Step 2: Two complementary scanners.** Define \(P_k(c)\) as the maximal even-palindrome half-radius (so \(P_k=R_k\)), and \(A_k(c)\) analogously with all mirror pairs unequal instead of equal. The binary digit-sum recursion gives \(t_k(2i)=t_{k-1}(i)\) and \(t_k(2i+1)=1-t_{k-1}(i)\). Thus the two nearest pairs at an even gap either both satisfy, or both fail, the same opposite relation at the parent gap; this continues pairwise throughout the interval. Consequently
\[
P_k(2h)=2A_{k-1}(h),\qquad A_k(2h)=2P_{k-1}(h),\qquad P_k(2h+1)=0.
\]
At an odd gap, the closest pair is always complementary. The next two mirror pairs are complementary simultaneously precisely when \(t_{k-1}(h-1)=t_{k-1}(h+1)\). A fourth complementary pair would require \(t_{k-1}(h-2)=t_{k-1}(h+2)\) as well, producing a forbidden length-five odd palindrome in the parent. Hence, for \(k\ge3\),
\[
A_k(2h+1)=1+2\mathbf1_{\{t_{k-1}(h-1)=t_{k-1}(h+1)\}}.
\]
This equality includes the cyclic boundary, by Step 1.

**Step 3: Closed formula and full axes.** At a nonzero gap \(c\), repeat the even-gap recursions exactly \(v=\nu_2(c)\) times. If \(v\) is even, the resulting odd gap has palindrome radius zero. If \(v\) is odd and \(m=k-v\ge3\), the result is \(2^v A_m(u)\) with odd \(u\); substituting the odd-gap formula yields exactly the displayed classification.

Only the cases \(m=1,2\) require bases. The circular word \(t_1=01\) has \(P_1(0)=P_1(1)=0\) and \(A_1(0)=A_1(1)=1\). The circular word \(t_2=0110\) has \(A_2(1)=A_2(3)=2\). Therefore the zero gap has full radius if and only if \(k\) is even. The gap \(N/2\) also has full radius if and only if \(k\) is even; the gaps \(N/4,3N/4\) have full radius if and only if \(k\) is odd. These exhaust the \(m\le2\) possibilities. Every remaining radius is covered by the explicit formula.

**Step 4: Off-axis maxima and their exact positions.** For even \(k\), the largest allowed odd valuation outside the full axes is \(v=k-3\). Here \(m=3\). The relevant \(t_2=0110\) comparisons at the four possible odd residues \(u=1,3,5,7\pmod8\) are all unequal, giving \(R_k(c)=2^{k-3}=N/8\) precisely at the four displayed gaps. At every smaller permitted valuation, \(R_k(c)\le3\cdot2^{k-5}<N/8\). For odd \(k\), the largest off-axis odd valuation is \(v=k-4\), where \(m=4\). The comparison in \(t_3=01101001\) is equal exactly at odd \(u\equiv1,7,9,15\pmod{16}\), producing radius \(3\cdot2^{k-4}=3N/16\) at exactly the stated gaps. Every smaller permitted valuation gives radius at most \(3\cdot2^{k-6}<3N/16\). Both maxima are therefore sharp with precisely four off-axis centers.

**Step 5: Long circular palindrome factors.** For an even length \(L\) above twice the off-axis maximal radius, the preceding classification leaves exactly the two full-axis gaps as potential centers, and both qualify. They give distinct palindromic factors: indeed \(t_k(i+N/2)=1-t_k(i)\), so half-circle translation complements every factor, including those centered at the two full-axis gaps. Their two factors are complements and hence unequal. This establishes the exact count of two at every claimed length, including \(L=N\). The absence of odd palindromes of length at least five follows from Step 1.

## Verification

The accompanying standalone `verify.py` constructs each \(t_k\) both by iterated substitution and by binary digit parity. For every \(k=4,\dots,16\), it computes every gap radius directly, compares it with the closed formula, and checks the complete full-axis sets, the four precise off-axis maximizers, all length-five cyclic factors, and the two long complementary factors at sampled lengths. This is an exhaustive computation over \(131056\) centers in the specified finite test range. Execute `python3 verify.py` and expect `VERIFY_OK`. All infinite statements are proved in Steps 1–5, independently of those computations.

## Relationship to prior work

The Thue–Morse word and its morphism, its infinite-word palindromic complexity and palindromic lacunas, and general palindromic facts concerning circular words are established objects/results. Peltomäki studies privileged versus palindromic factors of the *infinite* Thue–Morse word; Blondin Massé, Brlek and collaborators analyze ordinary and generalized palindromes in the infinite word; Blondin Massé et al. (2011) prove word equations for circular words; Simpson (2014) proves a universal bound for circular palindromic-factor counts. The present statement instead classifies the maximum radius at **each individually indexed gap** of **each finite dyadic cyclic iterate**, with parity-dependent sharp off-axis maxima and an exact long-factor count. No general bounds or aggregate factor-complexity sequence cited here alone gives these position-specific equalities.

## Limitations

The classification concerns dyadic finite Thue–Morse blocks, not arbitrary-length prefixes, all circular words, or arbitrary starting factors. The definition restricts factors to one circuit; repeated winding might change radii. Computation establishes only the tested finite range. Exact originality remains conditional on the literature comparison; inaccessible or unindexed specialized classifications may exist. This work has not undergone independent scientific audit.

## References

1. J. Peltomäki, *Privileged Factors in the Thue–Morse Word – A Comparison of Privileged Words and Palindromes*, arXiv:1306.6768 (first posted 2013-06-28). https://arxiv.org/abs/1306.6768
2. A. Blondin Massé, S. Brlek, A. Garon and S. Labbé, *Combinatorial properties of f-palindromes in the Thue–Morse sequence*, Pure Mathematics and Applications 19 (2008), 39–52.
3. A. Blondin Massé, S. Brlek and S. Labbé, *Palindromic lacunas of the Thue–Morse word*, GASCom 2008, 53–67.
4. A. Blondin Massé, S. Brlek, A. Garon and S. Labbé, *Equations on palindromes and circular words*, Theoretical Computer Science 412 (2011), 2922–2930. doi:10.1016/j.tcs.2010.07.005.
5. J. Simpson, *Palindromes in circular words*, Theoretical Computer Science 550 (2014), 66–78. doi:10.1016/j.tcs.2014.07.012.
