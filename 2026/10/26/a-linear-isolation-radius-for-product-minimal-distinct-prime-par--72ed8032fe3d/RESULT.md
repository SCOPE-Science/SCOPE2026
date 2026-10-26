# A linear isolation radius for product-minimal distinct-prime partitions

## Finding
Let \(A\ne\varnothing\) be a finite set of distinct primes, \(s=\sum_{a\in A}a\), and \(M=\prod_{a\in A}a\). Assume \(A\) is product-minimal at its sum: for every finite distinct-prime set \(C\) with \(\sum C=s\), one has \(\prod C\ge M\). Put \(H=\lceil5M/2\rceil\). If a prime \(q>\max\{s,H\}\) is the unique prime in \([q-H,q+H]\), then every distinct-prime set \(B\) with \(\sum B=s+q\) and \(\prod B\le qM\) equals \(A\cup\{q\}\). Thus adjoining \(q\) preserves product-minimality, with a sufficient isolation radius **linear** in \(M\).

## Assumptions and scope
All primes are positive ordinary rational primes. The sets are finite and have no repetitions; \(A\) is nonempty. A product of an empty set is \(1\), and the empty sum is \(0\). The isolation condition is sufficient, not necessary. Existence of arbitrarily large isolated primes for each fixed radius follows from the prime-isolation theorem attributed to Sierpiński in the cited paper; an effective bound on the least such prime is not asserted.

## Proof
**Combinatorial product–sum bound.** For any \(k\ge2\) and any \(k-1\) distinct primes \(r_1,\ldots,r_{k-1}\), write \(R=\prod_i r_i\) and \(u=\sum_i r_i\). Then
\[
\frac{k u}{R}\le\frac52.
\]
For \(k=2\), the quotient equals \(2\). For \(k=3\), it is \(3(1/r_1+1/r_2)\le3(1/2+1/3)=5/2\). For \(k\ge4\), increasing any prime among the \(k-1\) arguments decreases \(u/R\) (after holding the others fixed), so the maximum occurs at the first \(k-1\) primes. Put \(S_m=\sum_{j=1}^m p_j\), \(P_m=\prod_{j=1}^m p_j\), with \(p_j\) the \(j\)-th prime, and \(F_m=(m+1)S_m/P_m\). Here \(F_3=4/3\). For \(m\ge3\),
\[
\frac{F_{m+1}}{F_m}=\frac{m+2}{m+1}\left(\frac{1}{S_m}+\frac{1}{p_{m+1}}\right)
\le\frac54\left(\frac1{10}+\frac17\right)<1.
\]
Thus \(F_m\le F_3<5/2\) for all \(m\ge3\). This proves the bound in every case.

Now take a distinct-prime set \(B\) with \(\sum B=s+q\), \(\prod B\le qM\). Write \(k=|B|\), \(b=\max B\), \(u=\sum(B\setminus\{b\})\), and \(R=\prod(B\setminus\{b\})\). Since \(b\ge (s+q)/k\),
\[
R\le\frac{qM}{b}\le\frac{kqM}{s+q}<kM.
\]
When \(k\ge2\), the preceding bound yields \(u=(u/R)R<(5/(2k))kM=5M/2\). For \(k=1\), \(u=0\), so the same strict upper bound holds. Also \(s\le M\) (the sum of finitely many integers at least \(2\) is no greater than their product, including the singleton case). Consequently,
\[
|b-q|=|s-u|\le\max\{s,u\}<\frac{5M}{2}\le H.
\]
The prime \(b\) lies inside the stated isolation interval and therefore equals \(q\). Removing \(q\) from \(B\) leaves a distinct-prime set with sum \(s\) and product at most \(M\). Product-minimality of \(A\) forces equality of products; unique prime factorization forces \(B\setminus\{q\}=A\). This proves the stronger uniqueness assertion. Applying it to any competing product-minimizer of sum \(s+q\), whose product is at most the candidate value \(qM\), gives the stated preservation.

## Verification
The argument is entirely elementary once the explicit product–sum bound is proved. As a supplemental check, direct exact-rational enumeration over prime subsets of the first eleven primes and \(2\le k\le7\) found maximal \(ku/R=5/2\), attained when \(k=3\) and the two primes are \(2,3\). The proof, not that finite check, establishes the universal inequality. A self-contained verifier for this finite test is included; it is not used as an exhaustive infinite certificate.

## Relationship to prior work
Campbell, *On a problem on partitions into distinct primes*, arXiv:2610.19534v1 (first public version 14 October 2026), Lemma 2, uses the sufficient isolation width \(4M^2\) and establishes product-minimality after adjoining a suitably isolated prime. Its displayed intermediate bound \(R<kM\) is used above, but the new distinction is bounding the **sum** \(u\) of the other primes uniformly by \(5M/2\) rather than bounding their **product** \(R\) quadratically. An intermediate product-bound radius \(M\Lambda(M)\), with \(\Lambda(M)\) the maximum cardinality allowed by primorial comparison and \(\Lambda(M)\to\infty\), is also larger asymptotically; the linear bound is not implied by either sufficient-condition statement.

## Limitations
No optimality for the factor \(5/2\) is claimed. In particular, the displayed auxiliary inequality can be sharp at \(\{2,3\}\), but this does not show the prime-isolation radius is best possible under the extra equal-sum/product assumptions. No quantitative least-isolated-prime bound is derived. The bound is useful for the product-minimal extension lemma; it does not by itself sharpen the asymptotic size of the largest-prime-partition discrepancy established in the motivating paper.

## References
1. J. M. Campbell, *On a problem on partitions into distinct primes*, arXiv:2610.19534v1, 14 October 2026, https://arxiv.org/abs/2610.19534 .
2. W. Sierpiński, prime-isolation result (1948), as cited in Campbell, Lemma 1. The present proof invokes its existence statement only for the optional infinitely-many-primes consequence.
