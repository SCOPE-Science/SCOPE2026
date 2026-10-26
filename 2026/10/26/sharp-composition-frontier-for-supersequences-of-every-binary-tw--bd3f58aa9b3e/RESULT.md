# Sharp composition frontier for supersequences of every binary two-marker word

## Finding

For each integer \(N\ge0\), let \(\mathcal L_N\) consist of all \(\binom{N+2}{2}\) binary words \(0^a1 0^b1 0^c\) with \(a,b,c\ge0\) and \(a+b+c=N\). A word \(S\) is universal for \(\mathcal L_N\) when it contains every member as a **scattered subsequence** (not necessarily a contiguous factor).

For every \(m\ge2\), the smallest number of zeros in such a universal word having **exactly** \(m\) ones is

\[
Z_m(N)=N+\left\lfloor\frac{2N}{m-1}\right\rfloor.
\]

An optimal witness is obtained by setting \(h=N/(m-1)\), \(g_i=\lfloor(i+1)h\rfloor-\lfloor ih\rfloor\) for \(0\le i\le m\), and concatenating \(m\) ones with the \(m+1\) zero gaps \(g_0,\ldots,g_m\). Thus the entire length–composition tradeoff is determined. Minimizing also over the number of ones gives the **unrestricted** minimum supersequence length

\[
L(N)=N+1+\left\lfloor\sqrt{8N+1}\right\rfloor.
\]

For two-marker target words of length \(n=N+2\), this equals \(n-1+\lfloor\sqrt{8n-15}\rfloor\); in particular the necessary excess length grows as \(\sqrt{8n}+O(1)\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Each target contains exactly two ones and exactly \(N\) zeros; all allocations of those zeros across the three gaps are included. The source supersequence can contain arbitrarily many zeros and ones, except that the first formula fixes its number of ones at \(m\). Embeddings preserve order but may skip source positions. Repeated one-position zero counts are counted with multiplicity. The degenerate case \(N=0\) is included: \(11\) is the only target, and a source of \(m\ge2\) ones needs no zeros.

## Proof

**Lower bound at fixed \(m\).** Suppose a universal source has exactly \(m\) ones and \(Z\) zeros. Necessarily \(Z\ge N\); write \(Z=N+e\), where \(e\ge0\), and put \(Q=e+1\). Let \(t_1\le\cdots\le t_m\) be its cumulative zero counts immediately before successive ones.

Each target \(0^a11 0^{N-a}\), \(0\le a\le N\), requires two **different occurrences** of one whose zero counts belong to the integer interval \([a,a+e]=[a,a+Q-1]\). Otherwise that target could not embed. The target \(1 0^N1\) additionally requires \(t_m-t_1\ge N\).

If \(m=2k+1\) is odd, then \(N\ge kQ\) would provide \(k+1\) pairwise disjoint intervals \([jQ,(j+1)Q-1]\), \(0\le j\le k\), each requiring two distinct ones. That would demand \(2k+2>m\) ones. Hence \(N<kQ\), so \(2N<(m-1)Q\).

If \(m=2k\) is even, the same disjoint-interval argument shows \(N<kQ\). If \(N<(k-1)Q\), then already \(2N<(m-1)Q\). Otherwise set \(r=N-(k-1)Q\), so \(0\le r<Q\). The \(k\) disjoint intervals \(I_j=[jQ,(j+1)Q-1]\) and the \(k\) disjoint intervals \(J_j=[r+jQ,r+(j+1)Q-1]\), \(0\le j<k\), all have starting points at most \(N\) and each contain at least two of the \(m=2k\) one occurrences. Therefore every interval in either partition contains **exactly** two occurrences, with none outside the partition; the \(j\)-th consecutive pair of one occurrences is in \(I_j\cap J_j=[r+jQ,(j+1)Q-1]\). In particular, \(t_1\ge r\) and \(t_m\le kQ-1\). Together with \(t_m-t_1\ge N\), this gives

\[
N\le kQ-1-r=(2k-1)Q-1-N,
\]

hence \(2N<(m-1)Q\) again. Both parity cases imply \(e\ge\lfloor2N/(m-1)\rfloor\), proving the desired lower bound.

**Optimal construction.** If \(N=0\), take \(S=1^m\). Otherwise set \(h=N/(m-1)>0\), \(F(i)=\lfloor ih\rfloor\), and take zero gaps \(g_i=F(i+1)-F(i)\) for \(0\le i\le m\). All gaps are nonnegative integers. The total number of zeros is

\[
F(m+1)=N+\left\lfloor\frac{2N}{m-1}\right\rfloor,
\]

and the cumulative zero count before its \(i\)-th one is \(t_i=F(i)\), \(1\le i\le m\).

Fix any target \(0^a1 0^b1 0^c\) with \(a+b+c=N\). Choose

\[
i=\max\{1,\lceil a/h\rceil\},\qquad j=\max\{2,1+\lceil(a+b)/h\rceil\}.
\]

As \(0\le a\le a+b\le(m-1)h\), we have \(1\le i<j\le m\). Also \(ih\ge a\), so \(t_i\ge a\). The ceiling inequalities imply \((j-i)h\ge b\); since \(b\) is integral,

\[
t_j-t_i=\lfloor jh\rfloor-\lfloor ih\rfloor\ge\lfloor(j-i)h\rfloor\ge b.
\]

Likewise \((m+1-j)h\ge c\), using the exceptional case \(a+b=0\) separately with \(j=2\). Thus

\[
F(m+1)-t_j\ge\lfloor(m+1-j)h\rfloor\ge c.
\]

The target embeds at the \(i\)-th and \(j\)-th one occurrences, with enough zeros before, between, and after. This proves universality and sharpness for every \(N,m\).

**Eliminating \(m\).** Write \(k=m-1\ge1\). The best length is

\[
N+1+\min_{k\ge1}\left(k+\left\lfloor\frac{2N}{k}\right\rfloor\right).
\]

Set \(T=\lfloor\sqrt{8N+1}\rfloor\). For any positive integer \(k\), \(k(T-k)\le\lfloor T^2/4\rfloor\le2N\), implying \(k+\lfloor2N/k\rfloor\ge T\). Conversely choose a positive integer \(k\) maximizing \(k(T+1-k)\), whose maximum is \(\lfloor(T+1)^2/4\rfloor\). Since \((T+1)^2>8N+1\) and every integer square is congruent to zero or one modulo four, that maximum exceeds \(2N\). Thus \(k+\lfloor2N/k\rfloor\le T\). Both bounds yield the claimed expression for \(L(N)\). This includes \(N=0\), when \(T=k=1\).

## Verification

The standalone Python checker `checker.py` independently evaluates scattered-subsequence embeddings rather than using the proof's interval inequalities. It verifies the balanced-gap source for every \(0\le N\le80\) and \(2\le m\le21\) (1,680 cases), exhaustively tests all binary sources for fixed \(2\le m\le5\) and \(0\le N\le7\) across 144 candidate zero-count domains, and exhaustively confirms unrestricted optima through \(N=7\). It also checks the floor/square-root identity through \(N=500\). Run `python3 checker.py` from a directory containing the file. These finite checks corroborate, but do not replace, the infinite proof above.

## Relationship to prior work

The shortest-common-supersequence problem is classically difficult for arbitrary input families. Lagoutte and Tavenas, *The complexity of Shortest Common Supersequence for inputs with no identical consecutive letters* (arXiv:1309.0422, first posted 2013-09-02), introduce the general problem, describe Middendorf's hardness result even for arbitrary selected binary inputs of equal length and weight two, and prove a different lower-bound construction involving words with a **single** marker (Lemma 2). Neither the arbitrary-family hardness result nor that one-marker bound entails the exact common supersequence for the **entire** family of weight-two words at fixed length, or its sharp fixed-composition frontier. The separate all-permutations supersequence hardness problem (arXiv:1506.05079) has distinct target languages and is not a covering theorem here.

## Limitations

This theorem concerns precisely two marker symbols in every input target; it does not claim the same formula for larger fixed target weights, nonbinary alphabets, or restricted source patterns. The proof is self-contained and exact, but historical-priority comparison remains limited by unavailable full text for Middendorf's 1994 paper, DOI 10.1016/0304-3975(92)00074-2; its later descriptions concern hardness for selected subfamilies rather than an exact optimum for the full family. No independent mathematical audit has been performed.

## References

1. A. Lagoutte and S. Tavenas, *The complexity of Shortest Common Supersequence for inputs with no identical consecutive letters*, arXiv:1309.0422 (initial public posting 2013-09-02), especially Introduction and Lemma 2. https://arxiv.org/abs/1309.0422
2. M. Middendorf, *More on the Complexity of Common Superstring and Supersequence Problems*, Theoretical Computer Science 125 (1994), 205–228. https://doi.org/10.1016/0304-3975(92)00074-2
3. P. Uznański, *All Permutations Supersequence is coNP-complete*, arXiv:1506.05079 (2015). https://arxiv.org/abs/1506.05079
