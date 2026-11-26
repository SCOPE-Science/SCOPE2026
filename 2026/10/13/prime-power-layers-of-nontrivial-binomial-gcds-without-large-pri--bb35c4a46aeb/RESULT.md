# Prime-power layers of nontrivial binomial GCDs without large prime factors

## Finding

For every integer \(n\ge3\), put
\[
D(n-1)=\gcd_{2\le q\le n}\binom{q(n-1)}{n-1},
\]
and let \(P^+(n)\) denote the largest prime divisor of \(n\). For each fixed integer \(a\ge2\), let \(E_a(X)\) count \(3\le n\le X\) satisfying \(D(n-1)>1\) and \(P^+(n)\le\sqrt n\) for which the unique prime-power component at least \(\sqrt n\) is \(p^a\Vert n\). Then
\[
\boxed{E_a(X)\sim\frac{4a^2}{a^2-1}\frac{X^{(a+1)/(2a)}}{\log X}}
\qquad (X\to\infty).
\]
The layer classes are pairwise disjoint. In aggregate,
\[
\boxed{E(X)=\#\{3\le n\le X:D(n-1)>1,\ P^+(n)\le\sqrt n\}
\sim\frac{16}{3}\frac{X^{3/4}}{\log X}}.
\]
Thus the exceptional nontrivial binomial GCDs without a prime factor above the square-root barrier form a zero-density class, with a distinct asymptotic scale for each fixed exponent.

## Assumptions and scope

Here \(n\) is an integer at least \(3\), \(X\) is real and tends to infinity, \(a\ge2\) is held fixed in each layer asymptotic, and \(\log\) is the natural logarithm. Theorem 1 of Guo–Qiu–Cao–Feng–Gao [1], applied with \(k=n-1\), states that \(D(n-1)=1\) if and only if \(n/M(n)>M(n)\), where \(M(n)\) is the largest exact component \(p^e\Vert n\). Equivalently,
\[
D(n-1)>1\quad\Longleftrightarrow\quad M(n)^2\ge n.
\]
The prime number theorem is the other external input. No uniform asymptotic in an exponent \(a\) tending to infinity is claimed.

## Proof

**Classification and exact layer count.** By the cited binomial-GCD criterion, \(D(n-1)>1\) means that some exact prime-power component \(p^a\Vert n\) satisfies \(p^a\ge\sqrt n\). There is at most one such component: two distinct components at least \(\sqrt n\) would have product at least \(n\); as the product divides \(n\), equality would require both components to equal \(\sqrt n\), which is impossible for distinct prime bases. If the dominant component were a prime \(p\) to the first power, then \(p\ge\sqrt n\) and \(P^+(n)\le\sqrt n\) would give \(n=p^2\), contrary to exact exponent one.

Conversely, suppose \(p^a\Vert n\), \(a\ge2\), and \(p^a\ge\sqrt n\). Write \(n=p^a b\), with \(p\nmid b\). The size condition is exactly \(1\le b\le p^a\). Any other prime divisor \(q\) divides \(b\), so \(q^2\le b^2\le bp^a=n\); also \(p^2\le n\). Thus \(P^+(n)\le\sqrt n\). This identifies precisely the integers being counted.

For \(X\ge3\), define the integer bound
\[
U_a(p,X)=\min\!\left(p^a,\left\lfloor\frac{X}{p^a}\right\rfloor\right).
\]
The integer \(b\) has exactly \(U_a(p,X)-\lfloor U_a(p,X)/p\rfloor\) admissible choices, since \(p\nmid b\) is required for \(p^a\Vert n\). Therefore
\[
E_a(X)=\sum_{p^a\le X}\left(U_a(p,X)-\left\lfloor\frac{U_a(p,X)}p\right\rfloor\right),
\]
where the sum is over primes. This representation has no multiplicities, and \(p^a\ge4\) ensures that the lower limit \(n\ge3\) introduces no additional restriction.

**Fixed-exponent asymptotic.** Fix \(a\ge2\) and set \(Y=X^{1/(2a)}\). Splitting the exact formula at \(p=Y\) gives
\[
E_a(X)=\sum_{p\le Y}(p^a-p^{a-1})
+\sum_{Y<p\le X^{1/a}}\left(\left\lfloor\frac X{p^a}\right\rfloor-\left\lfloor\frac X{p^{a+1}}\right\rfloor\right).
\]
By the prime number theorem and partial summation,
\[
\sum_{p\le Y}p^a\sim\frac{Y^{a+1}}{(a+1)\log Y},
\qquad
\sum_{p>Y}p^{-a}\sim\frac{Y^{1-a}}{(a-1)\log Y}.
\]
The discarded sum \(\sum_{p\le Y}p^{a-1}\) is \(O_a(Y^a)\). In the second sum, replacing floors by their arguments costs \(O(\pi(X^{1/a}))\). The \(p^{-(a+1)}\) correction is \(O_a(XY^{-a})\), and extending the \(p^{-a}\) sum to infinity costs \(O_a(X^{1/a})\). Each error is negligible relative to \(X^{(a+1)/(2a)}/\log X\). Since \(\log Y=\log X/(2a)\), the two principal contributions are respectively
\[
\frac{2a}{a+1}\frac{X^{(a+1)/(2a)}}{\log X}
\quad\text{and}\quad
\frac{2a}{a-1}\frac{X^{(a+1)/(2a)}}{\log X}.
\]
Their sum is \(4a^2/(a^2-1)\) times the common scale.

**Summing every exponent.** Put \(E(X)=\sum_{a\ge2}E_a(X)\); only \(a\le\log_2 X\) may contribute. For each \(a\ge3\), ignoring primality and the coprimality restriction gives
\[
E_a(X)\le \sum_{m\ge2}\min\!\left(m^a,\frac X{m^a}\right).
\]
If \(Y=X^{1/(2a)}\ge2\), the contribution from \(m\le Y\) is at most \(Y^{a+1}\). Set \(L=\lfloor Y\rfloor+1\). Since \(t^{-a}\) decreases, the remaining contribution is at most
\[
X\left(L^{-a}+\int_L^\infty t^{-a}\,dt\right)
\le X\left(Y^{-a}+\frac{Y^{1-a}}{a-1}\right)
=Y^a+\frac{Y^{a+1}}{a-1}.
\]
The separate first summand accounts for the integer immediately above a possibly nonintegral splitting point. Both contributions are \(O(X^{(a+1)/(2a)})=O(X^{2/3})\) with absolute constants for \(a\ge3\). If \(Y<2\), bound the whole sum by
\[
X\left(2^{-a}+\int_2^\infty t^{-a}\,dt\right)
=X2^{-a}\left(1+\frac2{a-1}\right)<2\sqrt X.
\]
Consequently,
\[
\sum_{a\ge3}E_a(X)=O(X^{2/3}\log X)
=o\!\left(\frac{X^{3/4}}{\log X}\right).
\]
The \(a=2\) layer alone contributes \(16X^{3/4}/(3\log X)\) asymptotically, completing the total-count claim.

## Verification

The accompanying standalone verifier uses exact integer arithmetic. It compares the imported criterion with direct GCD computation for \(3\le n\le150\). It compares layer counts from trial-factorization censuses with the exact prime-power formula at \(X=10,100,1000,10000,20000\), and calculates sample counts at \(X=10^6,10^9,10^{12}\). The finite checks are not used in place of the prime number theorem or the asymptotic proof.

## Relationship to prior work

Guo, Qiu, Cao, Feng, and Gao proved the pointwise membership criterion used here (Theorem 1 and Lemma 9 of [1]). An exact valuation formula for this same GCD [4] also implies the pointwise criterion. The present result imports membership, partitions those nontrivial GCDs for which \(P^+(n)\le\sqrt n\) by the exponent of the dominant exact component, and gives an exact enumeration formula and fixed-exponent asymptotic hierarchy. The OEIS A080170 entry lists the complementary \(D(k)=1\) sequence and cites [1]; it supplies no exponent-layer count. Partial summation itself is standard; the contribution is the identified arithmetic subpopulation and its quantitative layer law.

## Limitations

The asymptotic for \(E_a(X)\) is for fixed exponent \(a\) only, not uniform when \(a\) grows with \(X\). This result does not determine the exact nontrivial GCD value, only whether it is nontrivial and its dominant prime-power exponent. It relies on the binomial-GCD criterion and the classical prime number theorem. Unindexed prior formulations of the arithmetic layer count remain possible.

## References

1. Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng, and Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1, first submitted 2026-06-22, Theorem 1 and Lemma 9.
2. OEIS A080170, *Numbers k such that gcd(C(2k,k),...,C((k+1)k,k))=1*, originally contributed by Benoit Cloitre in 2003, with the proof cited in a 2026 comment.
3. The classical prime number theorem and its standard partial-summation corollaries for fixed power-weighted prime sums.
4. *Exact prime-power factorization of the binomial progression gcd*, Resultary, https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-exact-prime-power-factorization-of-the-binomial-progression-gcd--db4eebf1aab7.
