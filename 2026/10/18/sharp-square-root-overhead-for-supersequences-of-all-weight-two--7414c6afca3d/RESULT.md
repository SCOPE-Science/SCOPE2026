# Sharp square-root overhead for supersequences of all weight-two binary words

## Finding
For every integer \(n\ge 3\), let \(F_2(n)\) be the minimum length of a binary word that contains, as scattered subsequences, every length-\(n\) binary word having exactly two ones. Then
\[
n-3+2\sqrt{2n-2}\;\le\;F_2(n)\;\le\;n+3+2\sqrt{2n-4}.
\]
In particular,
\[
F_2(n)=n+2\sqrt{2n}+O(1),\qquad
\lim_{n\to\infty}\frac{F_2(n)-n}{\sqrt n}=2\sqrt2.
\]
Both inequalities are valid at every integer \(n\ge3\), and an explicit host realizes the displayed upper bound.

## Assumptions and scope
The alphabet is the labeled binary alphabet \(\{0,1\}\). A scattered subsequence consists of letters at strictly increasing positions and need not be contiguous. A target is precisely a word \(0^a1 0^b1 0^c\) with nonnegative integers \(a,b,c\) satisfying \(a+b+c=n-2\). The host is allowed any number of zeros and ones; only its total length is minimized. The claim determines the sharp leading excess over the target length, not the exact integer value of \(F_2(n)\) at each length.

## Proof
Put \(N=n-2\), so \(N\ge1\).

**Lower bound.** Consider an arbitrary host \(W\) containing all targets. Write \(z\) for its number of zeros and \(t\) for its number of ones. Since a target contains \(N\) zeros, \(z\ge N\). Set \(e=z-N\ge0\). Order the one positions in \(W\), and let \(x_i\) be the number of host zeros preceding the \(i\)-th one. The integers \(x_i\) are nondecreasing.

For each integer \(a\in\{0,\ldots,N\}\), the particular required target \(0^a11 0^{N-a}\) must occur. Its two selected ones are distinct; their zero coordinates both lie in the interval \([a,a+e]\). Indeed, the earlier one follows at least \(a\) zeros, while the later one precedes at least \(N-a\) zeros; hence its zero coordinate is at most \(z-(N-a)=a+e\). Thus \([a,a+e]\) contains zero coordinates of at least two *distinct* host ones.

Choose \(a=0,e+1,2(e+1),\ldots\) up to \(N\). These intervals are pairwise disjoint and number \(\lfloor N/(e+1)\rfloor+1=\lceil(N+1)/(e+1)\rceil\). Each contains at least two distinct one positions, so
\[
t\ge2\left\lceil\frac{N+1}{e+1}\right\rceil\ge\frac{2(N+1)}{e+1}.
\]
Consequently, by arithmetic-geometric mean with \(s=e+1>0\),
\[
|W|=N+e+t\ge N-1+s+\frac{2(N+1)}s
\ge N-1+2\sqrt{2(N+1)}=n-3+2\sqrt{2n-2}.
\]
This holds for every host, proving the lower bound.

**Upper bound.** Fix any integer \(g\ge1\). Divide \(N=qg+r\) with \(q=\lfloor N/g\rfloor\) and \(0\le r<g\), and put \(m=q+2\). Construct
\[
W_g=1(0^g1)^m0^r.
\]
Its one positions have zero coordinates \(0,g,2g,\ldots,mg\), and the total number of zeros is \(mg+r=N+2g\). For an arbitrary target \(0^a1 0^b1 0^c\) with \(a+b+c=N\), choose the first host one at coordinate \(ig\), where \(i=\lceil a/g\rceil\). Choose the second at coordinate \(jg\), where
\[
j=i+\max\{1,\lceil b/g\rceil\}.
\]
Then \(j>i\), the first selected one has at least \(a\) zeros before it, and at least \(b\) zeros separate the selected ones. The estimates \(ig\le a+g\) and \((j-i)g\le b+g\) give
\[
jg\le a+b+2g\le N+2g=mg+r<(m+1)g.
\]
Because \(j\) is an integer, \(j\le m\), so the chosen one exists. Moreover, at least \((N+2g)-jg\ge c\) zeros follow the second selected one. Hence every required target embeds in \(W_g\).

The host length is therefore
\[
|W_g|=N+2g+\lfloor N/g\rfloor+3.
\]
Take \(g=\lceil\sqrt{N/2}\rceil\). Since \(g\le\sqrt{N/2}+1\) and \(g\ge\sqrt{N/2}\),
\[
2g+\lfloor N/g\rfloor\le2\sqrt{2N}+2,
\]
so \(F_2(n)\le N+2\sqrt{2N}+5=n+3+2\sqrt{2n-4}\). The two bounds yield the asserted square-root asymptotic and its sharp constant.

## Verification
Run `python checker.py` with Python 3. The script exhaustively checks every binary candidate host up to the first optimum for each \(3\le n\le11\), obtaining
\[
(F_2(3),F_2(4),\ldots,F_2(11))=(5,7,9,10,12,14,15,17,18).
\]
It also checks that the explicit construction contains all \(\binom n2\) weight-two targets for every \(3\le n\le160\), and checks pairwise disjointness and counting of the lower-bound windows for \(1\le N\le160\) and every \(0\le e\le N\). These finite computations corroborate the definitions and construction; the all-length theorem follows from the two mathematical proofs above.

## Relationship to prior work
Clifford, Gotthilf, Lewenstein, and Popa investigate restricted common-supersequence optimization with a *given* host multiset and the objective of maximizing how many prescribed targets are contained; their 2010 analysis does not state the minimum unrestricted host length for all fixed-weight-two binary targets. Uznański (2015) studies universality for permutations of *distinct* symbols and the complexity of deciding whether a host contains them; this is not the fixed two-symbol, heavily repeated-content family considered here.

Ma (2025) studies shortest common supersequences and batching for the *balanced* target family of length \(2h\) with \(h\) ones, obtaining a single-batch optimum \(4h-1\). Although its analysis introduces notation for fixed-content subsequences and rearrangements of host blocks, its balanced-family statement does not imply the present sparse-weight-two asymptotic by substitution: the number of ones in the target here is fixed while the number of zeros tends to infinity.

Two subsequently published works on (i) enumeration of hosts universal for **every** binary target of a given length and (ii) insertion distance from a prescribed host to that same unrestricted universality notion concern different quantified families. Their complete publicly available claims and arguments were compared: neither states this structured shortest-common-supersequence excess or implies the sharp coefficient \(2\sqrt2\). A general ability to solve a finite instance algorithmically is not an exact asymptotic bound.

## Limitations
The bounds leave a bounded additive uncertainty in \(F_2(n)\), and do not classify all shortest hosts. The finite script is supporting evidence, not proof of the asymptotic. The originality assessment compares accessible primary work and relevant published results, but cannot exclude unindexed equivalent formulations or overlooked stronger general theorems. Independent review has not been performed.

## References
1. R. Clifford, Z. Gotthilf, M. Lewenstein, A. Popa, *Restricted Common Superstring and Restricted Common Supersequence*, first public 2010-04-03, arXiv:1004.0424, https://arxiv.org/abs/1004.0424.
2. P. Uznański, *All Permutations Supersequence is coNP-complete*, first public 2015-06-16, arXiv:1506.05079, https://arxiv.org/abs/1506.05079.
3. Y. Ma, *Batch optimization for balanced binary sequences and DNA sequences*, BMC Bioinformatics 26 (2025), article 300, DOI:10.1186/s12859-025-06336-5, https://doi.org/10.1186/s12859-025-06336-5.
4. *Closed-form law for binary subsequence universality*, publicly available RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37.
5. *Exact full-support insertion radius of subsequence universality*, publicly available RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-full-support-insertion-radius-of-subsequence-universality--967f04fec949.
