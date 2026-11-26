# An all-arity product-rank law for commuting monotone-contraction idempotents

## Finding

Let \(\mathcal C_n\) be the monoid of full maps \(f:[n]\to[n]\) satisfying \(0\le f(i+1)-f(i)\le1\), and let \(\mathcal E_n\) be its set of idempotents. For positive integers \(n,m\) and \(1\le k\le n\), let \(c_{n,k}^{(m)}\) count ordered pairwise-commuting \(m\)-tuples of members of \(\mathcal E_n\) whose common product has image size \(k\). Set \(\Delta_m(r)=r^m-(r-1)^m\) for \(r\ge1\), and let \(A_m(t)\) be the ordinary Eulerian polynomial, so that \(\sum_{r\ge1}\Delta_m(r)t^{r-1}=A_m(t)/(1-t)^m\). Then
\[
c_{n,k}^{(m)}=\sum_{u=1}^{n-k+1}\Delta_m(u)\Delta_m(n-k-u+2),\qquad
\sum_{n\ge1}\sum_{k=1}^n c_{n,k}^{(m)}z^kt^n
=\frac{zt A_m(t)^2}{(1-zt)(1-t)^{2m}}.
\]
At fixed \(m\), for independent uniform draws from \(\mathcal E_n\), the probability of pairwise commutation tends to \(2^m/\binom{2m}{m}\). Conditioned on commutation, the product rank divided by \(n\) tends in distribution to \(\operatorname{Beta}(1,2m)\), with density \(2m(1-x)^{2m-1}\) on \(0<x<1\).

## Proof

**Interval background.** Each map has interval image. An idempotent fixes its entire image \([a,b]\), so monotonicity forces it to be the clamp \(e_{[a,b]}(x)=\min(b,\max(a,x))\). All such clamps are idempotent, giving \(n(n+1)/2\) possibilities. For overlapping intervals the two compositions are both the clamp to the intersection, by clipping at its left and right endpoints. For disjoint intervals, with the right endpoint \(b\) of the left interval less than the left endpoint \(c\) of the right interval, the two compositions are distinct constants \(b,c\). This proves the commutation test. Consequently any pairwise-commuting family has a common point, since maximum left endpoint does not exceed minimum right endpoint. As an interval corollary the maximal commutative subbands within \(\mathcal E_n\) are the point-stars: the intervals containing a fixed point are closed under intersection and the singleton interval at that point forces maximality. The star at \(i\) has \(i(n-i+1)\) members.

**Exact counts.** For a prescribed common intersection \([u,v]\) of size \(k\), the left endpoints must lie in \([1,u]\) with maximum \(u\), and the right endpoints in \([v,n]\) with minimum \(v\). These conditions are independent in the counting sense: every permitted left-right choice gives valid intervals since \(u\le v\). There are \(\Delta_m(u)\) and \(\Delta_m(n-v+1)\) choices, respectively. The intersection is unique for each tuple, so summing over its possible left endpoints gives the finite convolution. For fixed \(k\), the series in \(t\) is \(t^k(A_m(t)/(1-t)^m)^2\); sum \((zt)^k\) over positive \(k\) to obtain the bivariate identity.

**Asymptotics.** Write \(C_n=\sum_k c_{n,k}^{(m)}\). Setting \(z=1\) gives \(\sum_n C_n t^n=tA_m(t)^2/(1-t)^{2m+1}\). Since \(A_m(1)=m!\), the binomial coefficient expansion gives \(C_n=(m!)^2n^{2m}/(2m)!+O_m(n^{2m-1})\). Dividing by \((n(n+1)/2)^m\) proves the commuting probability limit. The finite convolution depends on \(n,k\) only through \(n-k\), so for any integer \(1\le r\le n\) the conditional tail is exactly \(\Pr(k\ge r\mid\text{commutation})=C_{n-r+1}/C_n\), by reindexing the sum over \(k\ge r\). For any fixed \(0<x<1\), taking \(r=\lceil nx\rceil\) gives the limiting tail \((1-x)^{2m}\), which identifies the stated Beta distribution on the full interval.

## Scope and prior work

The claim concerns the full finite-chain contraction monoid, uniform sampling from its idempotents, and fixed tuple length in the limit. It does not address all order-preserving maps, partial maps, arbitrary commuting elements, or growing tuple length.

The count of idempotents and their interval structure are prior work (Zubairu, Umar and Aliyu, arXiv:2205.00438, §2, Theorem 4 and Remark 5). The pairwise clamp test also follows from the more general fixed-clamp centralizer criterion in the indexed result [Centralizer profiles and a quadratic limit law](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-centralizer-profiles-and-a-quadratic-limit-law-for-idempotent-fi--22387dfffecf/RESULT.md), proof §2. The point-stars are the interval Helly corollary, not a separate novelty claim. The indexed [Product-rank renewal law for commuting monotone idempotents](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-product-rank-renewal-law-for-commuting-monotone-idempotents--7421eb043379/RESULT.md) counts pairs for all order-preserving maps and gives different pair totals; those rank aggregates do not extract the contraction subfamily. The pair total in the present setting occurs numerically in OEIS A293311 and A061926 under other interpretations, so no numerical priority is asserted for it. The finite all-arity, rank-refined law is the contribution; the asymptotic law is its consequence using standard coefficient and spacing calculations. Historical priority beyond the inspected sources is not established.

## Verification

The supplied standard-library `verify.py` tests the interval reduction and counts product ranks by direct composition in 30 finite parameter configurations (102,917 candidate tuples). The general result follows from the endpoint bijection and the exact generating function rather than these tests.
