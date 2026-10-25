# Strict negative covariance of every pair of part-size counts in uniform integer partitions

## Finding
Let \(\Lambda_n\) be a uniformly sampled unrestricted integer partition of an integer \(n\geq2\), and let \(C_i\) count the parts of size \(i\). For every \(1\leq i<j\leq n\),
\[
\operatorname{Cov}(C_i,C_j)<0.
\]
In particular, whenever \(A,B\) are disjoint nonempty subsets of \(\{1,\ldots,n\}\), their total part counts satisfy
\[
\operatorname{Cov}\Big(\sum_{i\in A} C_i,\sum_{j\in B} C_j\Big)<0.
\]
Thus the number of odd parts and the number of even parts have strictly negative covariance for every finite \(n\geq2\). This finite-sample sign statement is consistent with the previously established asymptotic independence of appropriately normalized odd- and even-part counts.

## Assumptions and scope
An integer partition of \(n\) is an unordered multiset of positive integers summing to \(n\). All such partitions have equal probability. Write \(p(k)\) for the unrestricted partition function, taking \(p(0)=1\) and \(p(k)=0\) for negative integers \(k\). The result concerns *multiplicities* \(C_i\), not binary events that size \(i\) is present. No assertion of negative association for arbitrary monotone events is made.

## Proof
**1. Marked-part identities.** The generating function is \(P(z)=\prod_{k\geq1}(1-z^k)^{-1}\). Marking a part of size \(i\), then a distinct part size \(j\), gives exactly
\[
\begin{aligned}
p(n)\,\mathbb E C_i&=\sum_{a=1}^{\lfloor n/i\rfloor}p(n-ai),\\
p(n)\,\mathbb E(C_iC_j)&=\sum_{a=1}^{\lfloor n/i\rfloor}\sum_{b=1}^{\lfloor n/j\rfloor}p(n-ai-bj),\qquad i\ne j.
\end{aligned}
\]
Therefore the covariance numerator is
\[
p(n)^2\operatorname{Cov}(C_i,C_j)=\sum_{a=1}^{\lfloor n/i\rfloor}\sum_{b=1}^{\lfloor n/j\rfloor}
\big[p(n)p(n-ai-bj)-p(n-ai)p(n-bj)\big]. \tag{1}
\]

**2. A partition-number rectangle lemma.** For positive integers \(t\) and integers \(a,b\geq2\),
\[
p(t+a)p(t+b)>p(t)p(t+a+b). \tag{2}
\]
To justify the nonstandard all-parameter inequality, first verify by the standard integer partition recurrence that (2) holds for \(1\leq t\leq25\) for each pair \((a,b)\) in \(\{(2,2),(2,3),(3,3)\}\). The finite checker supplies exact integer comparisons (75 in total). For \(t\geq26\), strict log-concavity of the partition function at every index exceeding 25, proved by DeSalvo and Pak [2, Theorem 1.1], says the adjacent ratios \(p(k+1)/p(k)\) strictly decrease for \(k\geq26\). Consequently (2) holds for those three pairs as well. Every integer at least two is a sum of twos and threes. Summing the strict rectangular log differences
\[
\log p(t+a)+\log p(t+b)-\log p(t)-\log p(t+a+b)
\]
over a partition of each side length into twos and threes proves (2) for arbitrary \(a,b\geq2\). This is a telescoping grid identity; all intermediate base points remain positive.

**3. Both sizes at least two.** Suppose \(2\leq i<j\leq n\). For a summand in (1), write \(u=ai\geq2\) and \(v=bj\geq2\). If \(u+v>n\), the summand is \(-p(n-u)p(n-v)<0\). If \(u+v<n\), take \(t=n-u-v\geq1\) in (2), obtaining
\[
p(n-u)p(n-v)>p(n)p(n-u-v).
\]
If \(u+v=n\geq10\), the same strict inequality is the Bessenrodt–Ono multiplicative inequality \(p(u)p(v)>p(u+v)\) for \(u,v\geq2\) and \(u+v\geq10\) [3, Theorem 2.1]. For \(n\leq9\), direct exact evaluation of (1) covers all pairs \(i,j\geq2\); every applicable numerator is negative. Thus every summand in (1) is negative when \(n\geq10\), and the finite residual cases are negative as well.

**4. The size-one boundary.** Put \(S(m)=\sum_{r=0}^mp(r)\) and \(F(m)=S(m-1)/p(m)\) for \(m\geq1\), with \(F(0)=0\). We establish
\[
F(m+1)\geq F(m)\quad(m\geq0),\qquad F(m+2)>F(m)\quad(m\geq0). \tag{3}
\]
Exact recurrence computation verifies monotonicity for \(0\leq m\leq25\); equality occurs only at \(m=1\). For \(m\geq26\), set \(r=p(m+1)/p(m)\). The same strict eventual log-concavity [2] together with the finite exact comparisons
\[
\frac{p(k)}{p(k-1)}\geq\frac{p(27)}{p(26)}\quad(2\leq k\leq26),
\qquad \frac{p(27)}{p(26)}<2
\]
shows \(p(k)/p(k-1)\geq r\) for \(2\leq k\leq m\) and \(r<2\). Using \(p(0)=p(1)=1\),
\[
S(m)-rS(m-1)=(2-r)+\sum_{k=1}^{m-1}p(k)\left(\frac{p(k+1)}{p(k)}-r\right)>0,
\]
which is equivalent to \(F(m+1)>F(m)\). Hence (3) follows. For \(j\geq2\), the marked-part identities give
\[
p(n)^2\operatorname{Cov}(C_1,C_j)
=p(n)\sum_{b=1}^{\lfloor n/j\rfloor}p(n-bj)\big[F(n-bj)-F(n)\big].
\]
Every term is strictly negative by (3), since \(bj\geq2\). This finishes all pairs.

**5. Disjoint size classes.** Bilinearity of covariance sums the pairwise strictly negative entries over \(A\times B\). For the odd/even partition, \(A\) contains size 1 and \(B\) contains size 2, ensuring both are nonempty for every \(n\geq2\).

## Verification
Run `python3 verify.py` with Python 3 and its standard library. The checker constructs integer partition numbers by a direct coin-change recurrence. It checks the 75 base rectangles, finite monotonicity and boundary-ratio inequalities, exhaustive finite covariance numerators for \(2\leq n\leq32\), and independent enumeration of individual partitions through \(n=12\) against the marked-part formulas. It also confirms that the presence indicators of parts 1 and 2 are positively correlated at \(n=3\), demonstrating why the theorem must not be overstated as negative association. One execution produced **10,716 exact integer/rational assertions passed**. These finite checks cover explicitly identified finite gaps; the infinite implications use the cited established partition-number inequalities and the algebraic arguments above, rather than numerical extrapolation.

## Relationship to prior work
Yakubovich [1, Section 8, Theorem 8.1] proves asymptotic independence in distribution of normalized odd-part and even-part counts in a uniform random partition. That limit result does not imply a finite covariance sign, whereas the present theorem gives strict negativity for every finite size and, more generally, all disjoint part-size count classes. Its proof explicitly **uses**, rather than claims to rediscover, the established partition-function log-concavity [2] and multiplicative inequality [3]. The primitive marked-part formulas are standard generating-function identities; the claimed result is their finite all-pairs sign consequence, including the size-one boundary and odd/even specialization. Literature priority for the particular covariance sign remains to be independently confirmed.

## Limitations
The result is restricted to uniform unrestricted partitions of fixed total size and linear multiplicity counts. It does not prove any numerical covariance magnitude, negative association, conditional independence, or extension to arbitrary weighted/restricted partitions. The established inequality inputs [2,3] are nontrivial imported theorems. Literature overlap searches cannot establish absolute novelty; independent mathematical assessment has not been performed.

## References
[1] Yuri Yakubovich, *Growing integer partitions with uniform marginals and the equivalence of partition ensembles*, arXiv:2303.14472, initial public version March 25, 2023, Section 8. https://arxiv.org/abs/2303.14472

[2] Stephen DeSalvo and Igor Pak, *Log-concavity of the partition function*, arXiv:1310.7982, Theorem 1.1 and Section 5. https://www.math.ucla.edu/~pak/papers/LogConcave27.pdf

[3] Christine Bessenrodt and Ken Ono, *Maximal multiplicative properties of partitions*, arXiv:1403.3352, Theorem 2.1. https://arxiv.org/abs/1403.3352
