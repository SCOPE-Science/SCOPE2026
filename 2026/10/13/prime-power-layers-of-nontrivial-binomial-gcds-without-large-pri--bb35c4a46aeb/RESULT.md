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
Thus the exceptional nontrivial binomial GCDs without a prime factor above the square-root barrier form a zero-density class with a specific power-law scale and a hierarchy of exponent layers.

## Assumptions and scope

Here \(n\) is an integer at least \(3\), \(X\) is real and tends to infinity, \(a\ge2\) is held fixed in each layer asymptotic, and \(\log\) is the natural logarithm. The criterion imported from Guo–Qiu–Cao–Feng–Gao is an exact theorem for the displayed binomial GCD: if \(M(n)\) is the largest exact prime-power component \(p^e\Vert n\), then
\[
D(n-1)>1\quad\Longleftrightarrow\quad M(n)^2\ge n.
\]
The prime number theorem is the other external input. No uniform asymptotic in an exponent \(a\) tending to infinity is claimed.

## Proof

**Classification and exact layer count.** By the cited binomial-GCD criterion, \(D(n-1)>1\) means that some exact prime-power component \(p^a\Vert n\) satisfies \(p^a\ge\sqrt n\). There is at most one such component: two different exact prime powers at least \(\sqrt n\) would have product at least \(n\), with equality requiring two distinct prime powers to be equal, which is impossible. If the dominant component were a prime \(p\) to the first power, then \(p\ge\sqrt n\) would contradict \(P^+(n)\le\sqrt n\), apart from equality \(n=p^2\), which has exponent \(2\), not \(1\). Hence its exponent is at least \(2\).

Conversely, suppose \(p^a\Vert n\), \(a\ge2\), and \(p^a\ge\sqrt n\). Write \(n=p^a b\), with \(p\nmid b\). The size condition is exactly \(1\le b\le p^a\). Any other prime divisor \(q\) divides \(b\), so \(q\le b\le p^a\) and \(q^2\le b^2\le bp^a=n\); also \(p^2\le n\). Thus \(P^+(n)\le\sqrt n\). This identifies precisely the integers being counted.

For \(X\ge3\), define the integer bound
\[
U_a(p,X)=\min\!\left(p^a,\left\lfloor\frac{X}{p^a}\right\rfloor\right).
\]
The integer \(b\) has exactly \(U_a(p,X)-\lfloor U_a(p,X)/p\rfloor\) admissible choices, since \(p\nmid b\) is required for \(p^a\Vert n\). Therefore the exact, non-asymptotic formula is
\[
E_a(X)=\sum_{p^a\le X}\left(U_a(p,X)-\left\lfloor\frac{U_a(p,X)}p\right\rfloor\right),
\]
with the sum over primes. This is a disjoint representation, not a count with multiplicities.

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
The discarded sum \(\sum_{p\le Y}p^{a-1}\) is \(O_a(Y^a)\). In the second sum, replacing floors by their arguments costs at most \(O(\pi(X^{1/a}))\). Its \(p^{-(a+1)}\) correction is \(O_a(XY^{-a})\), and extending the \(p^{-a}\) sum to infinity costs \(O_a(X^{1/a})\). Each is negligible relative to \(X^{(a+1)/(2a)}/\log X\). Since \(\log Y=\log X/(2a)\), the two principal contributions are respectively
\[
\frac{2a}{a+1}\frac{X^{(a+1)/(2a)}}{\log X}
\quad\text{and}\quad
\frac{2a}{a-1}\frac{X^{(a+1)/(2a)}}{\log X}.
\]
Their sum is \(4a^2/(a^2-1)\) times the common scale, proving the first formula.

**Summing every exponent.** Put \(E(X)=\sum_{a\ge2}E_a(X)\); only \(a\le\log_2 X\) may contribute. For each \(a\ge3\), ignoring primality and the coprimality restriction gives
\[
E_a(X)\le \sum_{m\ge2}\min\!\left(m^a,\frac X{m^a}\right),
\]
where restricting to \(m^a\le X\) only strengthens the bound. If \(Y=X^{1/(2a)}\ge2\), splitting the sum at \(Y\) bounds the two pieces by \(Y^{a+1}\) and \(XY^{1-a}/(a-1)\), respectively; both are \(O(X^{(a+1)/(2a)})=O(X^{2/3})\), uniformly over \(a\ge3\). If \(Y<2\), the second expression alone bounds the sum by \(2X/2^a<2\sqrt X\), also \(O(X^{2/3})\). Consequently,
\[
\sum_{a\ge3}E_a(X)=O(X^{2/3}\log X)
=o\!\left(\frac{X^{3/4}}{\log X}\right).
\]
The \(a=2\) layer alone contributes \(16X^{3/4}/(3\log X)\) asymptotically, completing the total-count claim.

## Verification

The accompanying standalone verifier computes the exact prime-power component formula with integer arithmetic, independently compares it against a trial-factorization census through \(X=20000\), and tests the imported binomial-GCD criterion directly from its defining binomial coefficients for \(3\le n\le150\). It also calculates exact sample counts at \(X=10^6,10^9,10^{12}\). The finite checks are not used in place of the prime number theorem or the asymptotic proof.

## Relationship to prior work

Guo, Qiu, Cao, Feng, and Gao proved the decisive membership criterion \(D(n-1)>1\) in June 2026. Their paper studies whether the GCD is \(1\), not the distribution of nontrivial GCDs among integers with no prime factor exceeding \(\sqrt n\). The present theorem imports that criterion, partitions its square-root-smooth exceptional population by the exponent of the dominant exact prime power, and derives exact enumeration formulas and a full fixed-exponent asymptotic hierarchy. No new proof of the source's binomial-GCD criterion is claimed.

The OEIS entry A080170 lists the complementary \(D(k)=1\) sequence and cites the original criterion, but supplies no exponent-layer count. Exact-phrase, parameter, and equivalent-formulation searches in the checked literature and a mathematical-results index found no asymptotic covering this hierarchy. The analysis uses standard prime-number-theorem partial summation; the novelty claimed is the identified arithmetic subpopulation and its quantitative layer law, not a novel prime-counting technique.

## Limitations

The asymptotic for \(E_a(X)\) is for fixed exponent \(a\) only, not uniform when \(a\) grows with \(X\). The theorem does not determine the exact nontrivial GCD value, only whether it is nontrivial and its dominant prime-power exponent. It relies on the published binomial-GCD criterion and the classical prime number theorem; unindexed prior formulations of the arithmetic layer count remain a literature risk.

## References

1. Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng, and Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1, first submitted 2026-06-22, Theorem 1 and Lemma 9.
2. OEIS A080170, *Numbers k such that gcd(C(2k,k),...,C((k+1)k,k))=1*, originally contributed by Benoit Cloitre in 2003, with the proof cited in a 2026 comment.
3. The classical prime number theorem and its standard partial-summation corollaries for fixed power-weighted prime sums.
