# Sharp first-loss phase diagram for finite-capacity urn overflow laws

## Finding

Place independent balls uniformly into \(n\ge2\) labeled urns of capacity \(r\ge2\). Any arrival at a full urn goes to an overflow basket. Let \(V_{m,n,r}\) be the number of overflowed balls among \(m\) arrivals. At the first horizon with two possible rejected balls, \(m=r+2\), put \(a=(r+2)(n-1)\) and \(N=n^{r+1}\). The exact probability-generating polynomial is
\[
\mathbb E[z^{V_{r+2,n,r}}]=\frac{N-a-1+az+z^2}{N}.
\]
Its mass sequence is log-concave **if and only if** one of the following holds:

- \(r=2\) and \(2\le n\le14\);
- \(r=3\) and \(2\le n\le3\);
- \(r=4\) and \(n=2\).

For all \(r\ge5\) and \(n\ge2\), it fails ordinary log-concavity already at this horizon. In contrast, the mass sequence is ultra-log-concave relative to its three-point support **only** when \((r,n)=(2,2)\). Equivalently, this generating polynomial has only real (necessarily negative) zeros **only** for \((r,n)=(2,2)\). At that exceptional pair, \(V_{4,2,2}\) is the sum of independent Bernoulli variables with parameters \(1/2\) and \(1/4\), but the next horizon has
\[
\mathbb E[z^{V_{5,2,2}}]=\frac{z(10+5z+z^2)}{16},
\]
whose quadratic discriminant is \(-15\). Thus, for every finite capacity \(r\ge2\) and \(n\ge2\), the first loss of a shifted Bernoulli-sum representation occurs exactly at \(m=r+2\), except at \((r,n)=(2,2)\), where it occurs at \(m=5\).

## Assumptions and scope

All choices are independent and uniform over precisely \(n\) labeled urns; each urn accepts its first \(r\) balls and rejects later arrivals. Ordinary log-concavity means \(p_1^2\ge p_0p_2\) for three consecutive masses; ultra-log-concavity relative to the three-point support means \(p_1^2\ge4p_0p_2\). A shifted Bernoulli sum is an integer constant plus a sum of independent \(\{0,1\}\)-valued random variables. The result makes no claim about unequal urn probabilities, time horizons beyond the specified first-failure thresholds, or any asymptotic approximation.

## Proof

**Three-point enumeration.** At \(m=r+2\), at most two balls overflow. Exactly two overflow if all \(r+2\) draws hit one urn: probability \(n/n^{r+2}=1/N\). Exactly one overflows if exactly \(r+1\) draws hit one urn and the remaining draw hits a different urn. There are \((r+2)n(n-1)\) such sequences among \(n^{r+2}\), yielding \(a/N\). The rest have no overflow, giving \((N-a-1)/N\). These masses are positive for \(n,r\ge2\).

**Exact curvature criteria.** The ordinary log-concavity inequality is
\[
 a^2\ge N-a-1\quad\Longleftrightarrow\quad N\le a^2+a+1.
\]
The strengthened three-point inequality is
\[
 a^2\ge4(N-a-1)\quad\Longleftrightarrow\quad(a+2)^2\ge4N.
\]
The latter is also precisely the nonnegative-discriminant condition for the generating quadratic; positive coefficients force any real zeros to be negative.

**Complete ordinary log-concavity classification.** Define \(R(n,r)=n^{r+1}/(a^2+a+1)\). For \(n\ge3\), it is strictly increasing in \(n\), since
\[
R(n,r)=\frac{n^{r+1}/(n-1)^2}{(r+2)^2+(r+2)/(n-1)+1/(n-1)^2},
\]
its numerator is nondecreasing for \(n\ge3,\ r\ge2\) (logarithmic derivative \(((r-1)n-(r+1))/(n(n-1))\ge0\)), and its denominator strictly decreases. For fixed \(n\ge2\), \(R(n,r)\) increases strictly in \(r\): as \(r\) rises by one, \(n^{r+1}\) multiplies by \(n\ge2\), while \(a^2+a+1\) multiplies by less than \(((r+3)/(r+2))^2\le25/16<2\). The exact boundary comparisons are
\[
\begin{array}{c|cc}
r & (n,\ N,\ a^2+a+1)\text{ on pass side}&(n,\ N,\ a^2+a+1)\text{ on fail side}\\
2&(14,2744,2757)&(15,3375,3193)\\
3&(3,81,111)&(4,256,241)\\
4&(2,32,43)&(3,243,157)\\
5&\text{none}&(2,64,57)
\end{array}
\]
Together with the direct \(r=2,n=2\) check, monotonicity proves exactly the stated table for every pair of integers \(n,r\ge2\).

**Ultra-log-concavity and real-rootedness.** For \(r=2,n\ge3\),
\[
4n^3-(4n-2)^2=4(n-1)(n^2-3n+1)>0,
\]
so the discriminant is negative. For \(r\ge3,n\ge3\), \(4n^{r-1}>(r+2)^2\) (base \(r=3,n=3\): \(36>25\), and the exponential factor dominates subsequent linear-factor ratios), hence \(4N>(r+2)^2n^2\ge(a+2)^2\). For \(n=2,r\ge3\), \(4\cdot2^{r+1}>(r+4)^2=(a+2)^2\), from the base \(r=3\) inequality \(64>49\) and induction. The remaining \((r,n)=(2,2)\) has \(N=8,a=4\), thus \((a+2)^2=36>32=4N\), with
\[
\frac{3+4z+z^2}{8}=\frac{1+z}{2}\frac{3+z}{4}.
\]
For \(m\le r\), overflow is identically zero. At \(m=r+1\), overflow is Bernoulli with success probability \(n^{-r}\). Therefore the first failure for all nonexceptional pairs is sharp in time. At the exceptional pair, elementary enumeration at \(m=5\) gives \((20,10,2)/32\) on \(\{1,2,3\}\), and the displayed quadratic has discriminant \(25-40=-15\), proving the delayed but sharp first failure.

## Verification

Run \(\texttt{python3 check.py}\) with the standalone standard-library checker embedded alongside this document. It computes the exact capped-urn law by integer dynamic programming for \(2\le n,r\le6\), reproduces the three coefficients and the exceptional five-draw distribution, and checks the sign phase diagram for \(2\le n\le150\), \(2\le r\le40\) using arbitrary-precision integers. These finite tests corroborate the displayed closed-form identities; all unrestricted quantifiers are justified by the analytic monotonicity and induction arguments above.

## Relationship to prior work

Gouet, Hitczenko and Wesołowski (arXiv:1905.06663v1, May 16, 2019) define the same capacity-\(r\) overflow statistic and prove asymptotic Poisson/normal limit results under scaling regimes, not a uniform finite-parameter log-concavity or real-zero onset classification. Classical real-rooted occupancy-count laws concern capacity-one acceptance and do not imply the capacity-at-least-two phase diagram. Badiella, del Castillo and Puig (2023) discuss ultra-log-concavity of discrete order statistics rather than capped-urn overflow. Searches for exact equivalent formulations and stronger published coverage found no proof of this all-parameter threshold; incomplete indexing remains a genuine originality risk.

## Limitations

The phase diagram concerns the earliest distribution supported on three consecutive overflow counts, not the entire later-time family. The first-loss assertion concerns shifted independent-Bernoulli decomposability, not arbitrary bounded-summand factorizations. This is an elementary closed-form shape classification; publication novelty cannot be independently certified by search alone.

## References

1. R. Gouet, P. Hitczenko and J. Wesołowski, *Asymptotics of the overflow in urn models*, arXiv:1905.06663v1 (2019), https://arxiv.org/html/1905.06663v1 .
2. L. H. Harper, *Stirling Behavior is Asymptotically Normal*, Annals of Mathematical Statistics 38 (1967), 410–414, DOI: 10.1214/aoms/1177698956 .
3. L. Badiella, J. del Castillo and P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters 201 (2023), 109900, DOI: 10.1016/j.spl.2023.109900 .
