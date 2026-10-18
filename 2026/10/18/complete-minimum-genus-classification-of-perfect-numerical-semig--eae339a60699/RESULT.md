# Complete minimum-genus classification of perfect numerical semigroups

## Finding

For every integer \(F\ge 3\), the least genus among perfect numerical semigroups with Frobenius number \(F\) is
\[
\beta(F)=\left\lfloor\frac F2\right\rfloor+2.
\]
All minimizers admit the following explicit classification; intervals with lower endpoint greater than upper endpoint are understood to be empty. Put \(k=\lfloor F/2\rfloor\).

If \(F=2k+1\), the unique minimizer is
\[
U_F=\{0\}\cup[k+1,F-2]\cup[F+1,\infty)\cap\mathbb Z.
\]
If \(F=2k\) with \(k\ge2\), the minimizers are \(U_F\) and precisely the semigroups
\[
S_{F,a}=\{0\}\cup[a,k-1]\cup[F+1-a,F-2]\cup([F+1,\infty)\cap\mathbb Z),
\qquad \left\lceil\frac{F+1}{3}\right\rceil\le a\le k-1.
\]
Thus their number is exactly one for odd \(F\), and \(1+\lfloor(k-1)/3\rfloor\) for even \(F=2k\). These are all semigroups attaining the minimum, not merely selected examples. In the notation of Moreno-Frías and Rosales, the minimum genus \(\beta(F)\) among maximal perfect semigroups has the same value, since every minimum-genus member is maximal by inclusion.

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid \(S\subseteq\mathbb Z_{\ge0}\). Its Frobenius number \(F(S)\) is its largest gap; its genus \(g(S)\) is the number of positive gaps. A gap \(h\) is *isolated* when both \(h-1\) and \(h+1\) belong to \(S\). The semigroup is *perfect* if it has no isolated gaps. The theorem applies to every integer \(F\ge3\), with no assumptions on multiplicity or embedding dimension. The values \(F=3\) and \(F=4\) have the unique minimizers \(\{0\}\cup([F+1,\infty)\cap\mathbb Z)\).

## Proof

**1. Reflection bound.** A perfect semigroup with Frobenius number \(F\) omits both \(F\) and \(F-1\): otherwise \(F\) would be an isolated gap, as \(F+1\in S\). Partition \(S\cap[0,F]\) into its \(r\) maximal consecutive integer blocks \([u_j,v_j]\), the first of which is \([0,0]\). Between consecutive retained blocks there are at least two missing integers, because a singleton gap would be isolated. If \(s\in S\cap[0,F]\), then \(F-s\notin S\) and \(F-1-s\notin S\); otherwise adding \(s\) would place \(F\) or \(F-1\) in \(S\). Therefore each retained block \([u_j,v_j]\) forces an interval of gaps
\[
[F-v_j-1,F-u_j],
\]
with \(v_j-u_j+2\) members. These forced intervals are pairwise disjoint: the separation of at least two gaps between retained blocks leaves at least one integer between their reversed forced intervals. Writing \(n=|S\cap[0,F]|\) and \(g=g(S)\), we have \(n+g=F+1\). Counting the forced gaps yields
\[
g\ge n+r,\qquad 2g\ge F+1+r. \tag{1}
\]
If \(S\ne\{0\}\cup([F+1,\infty)\cap\mathbb Z)\), then \(r\ge2\). Hence \(g\ge\lceil(F+3)/2\rceil=\lfloor F/2\rfloor+2\). The exceptional all-gap semigroup has genus \(F\), also at least this bound when \(F\ge3\).

**2. Existence.** For odd \(F=2k+1\), the set \(U_F\) has \(k-1\) positive elements below \(F\), so its genus is \(k+2\). For even \(F=2k\), \(U_F\) has \(k-2\) such elements, giving genus \(k+2\). Its positive elements below \(F\) are at least \(k+1\), so their sums exceed \(F\); the cofinite tail makes it closed under addition. Its gap blocks are \([1,k]\) (for odd \(F\)) or \([1,k]\) (for even \(F\)), followed by \([F-1,F]\) whenever the earlier interval is nonempty; the small cases \(F=3,4\) consist entirely of gaps below the conductor. In particular no gap is isolated. Thus the lower bound is sharp.

**3. Odd \(F\): uniqueness.** Put \(F=2k+1\). When \(k=1\), the only semigroup of genus \(3\) and Frobenius number \(3\) is the all-gap member. For \(k\ge2\), a minimizer has \(g=k+2\) and \(n=k\), so it has positive elements below \(F\). Inequality (1) gives \(r\le2\), hence \(r=2\) and equality holds in (1). Write the retained blocks as \([0,0]\) and \([a,b]\). Their forced gap intervals exactly cover the two actual gap intervals \([1,a-1]\) and \([b+1,F]\). The upper forced interval \([F-1,F]\) equals \([b+1,F]\), so \(b=F-2\); the lower forced interval \([F-b-1,F-a]\) equals \([1,a-1]\), giving \(F-a=a-1\). Consequently \(a=k+1\), and the unique minimizer is \(U_F\).

**4. Even \(F\): classification.** Let \(F=2k\). For \(k=2\), a minimum genus of four forces all of \(1,2,3,4\) to be gaps, leaving only \(U_F\). Assume \(k\ge3\). A minimizer has \(n=k-1>1\), so \(2\le r\le3\) by (1).

If \(r=2\), write \(S\cap[0,F]=\{0\}\cup[a,b]\). The \(k-2\) positive retained integers give \(b=a+k-3\), while \(F-1\) is a gap and hence \(b\le F-2\). Closure forces \(2a>F\): otherwise the entire interval \([2a,2b]\) of sums contains an integer in the forbidden gap interval \([b+1,F]\). Thus \(a\ge k+1\), and the bound on \(b\) forces \(a\le k+1\). This is exactly \(U_F\).

If \(r=3\), equality holds in (1). Write the retained blocks as \([0,0],[a,b],[c,d]\) with \(c\ge b+3\). The three reversed forced gap intervals, in increasing order,
\[
[F-d-1,F-c],\quad[F-b-1,F-a],\quad[F-1,F],
\]
exhaust the three actual gap blocks
\[
[1,a-1],\quad[b+1,c-1],\quad[d+1,F].
\]
The endpoints therefore force \(d=F-2\), \(c=F+1-a\), and \(b=k-1\). The first retained block of positive integers has sums filling \([2a,F-2]\). Since this entire interval must avoid the intervening gap \([k,c-1]\), necessarily \(2a\ge c\), equivalently \(3a\ge F+1\). Separation of the middle gap requires \(a\le k-1\). Hence the only possible semigroups are precisely \(S_{F,a}\) in the stated range.

Conversely, for each integer in that range, the two positive blocks of \(S_{F,a}\) have no isolated intervening or exterior gaps: the gap blocks are \([1,a-1]\), \([k,F-a]\), and \([F-1,F]\), all of length at least two. The sum of two elements of the first positive block belongs to the second positive block, since \(2a\ge F+1-a\) and the largest such sum is \(F-2\); any sum involving an element of the second block is at least \(a+(F+1-a)=F+1\). Thus each \(S_{F,a}\) is a perfect numerical semigroup of genus \(k+2\). The parameter range contains exactly \(k-\lceil(F+1)/3\rceil=\lfloor(k-1)/3\rfloor\) integers. This proves completeness and the enumeration.

## Verification

The accompanying standard-library script `verify.py` enumerates all subsets of \(\{1,\ldots,F-2\}\), checks additive closure and absence of isolated gaps directly, and compares every minimum-genus instance with the claimed classification for each \(3\le F\le20\). It also tests every explicitly constructed minimizer for \(21\le F\le300\). These tests provide reproducible finite cross-checks; the proof of the unbounded theorem is the block-reflection argument above.

## Relationship to prior work

Moreno-Frías and Rosales, *The covariety of perfect numerical semigroups with fixed Frobenius number* (first publicly posted 2023), introduced an algorithm to compute the genus threshold \(\beta(F)\) through maximal members and gave \(\beta(11)=7\). The present theorem gives a closed formula for every \(F\) and classifies and counts every genus minimizer. Their earlier 2019 study introduced perfect-semigroup operations and algorithms. The 2026 paper *Perfect numerical semigroups of type two* establishes a general gap-to-nongap injection and a genus inequality for semigroups missing \(F-1\). That inequality is related to (1), but the complete parity-dependent equality classification and enumeration above require the interval analysis. Singhal's 2022 work addresses genus distributions over all numerical semigroups, rather than the extremal perfect family.

## Limitations

This is a theorem about minimum genus at fixed Frobenius number, not a classification of all perfect numerical semigroups, nor of all maximal elements of the associated covariety. The genus lower bound alone follows readily from known gap-injection ideas; the additional result is the explicit and exhaustive equality classification and exact count. Relevant type-two and general numerical-semigroup literature has been compared, but an unindexed equivalent classification remains possible. No independent audit has been performed.

## References

1. M. A. Moreno-Frías and J. C. Rosales, *The covariety of perfect numerical semigroups with fixed Frobenius number*, arXiv:2305.14967 (first public version 2023-05-24), later Czechoslovak Mathematical Journal 74 (2024), 697–714. DOI: 10.21136/CMJ.2024.0379-23. https://arxiv.org/abs/2305.14967
2. M. A. Moreno-Frías and J. C. Rosales, *Perfect numerical semigroups*, Turkish Journal of Mathematics 43 (2019), 1742–1754. DOI: 10.3906/mat-1901-111. https://journals.tubitak.gov.tr/math/vol43/iss3/47/
3. M. A. Moreno-Frías and J. C. Rosales, *Perfect numerical semigroups of type two*, Congressus Numerantium 237 (2026), 99–112. DOI: 10.61091/cn237-07. https://combinatorialpress.com/cn-articles/volume-237/perfect-numerical-semigroups-of-type-two/
4. D. Singhal, *Distribution of genus among numerical semigroups with fixed Frobenius number*, Semigroup Forum 104 (2022), 704–723. DOI: 10.1007/s00233-022-10282-6. https://link.springer.com/article/10.1007/s00233-022-10282-6
