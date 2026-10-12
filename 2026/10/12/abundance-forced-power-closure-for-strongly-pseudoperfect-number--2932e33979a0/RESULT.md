# Abundance-forced power closure for strongly pseudoperfect numbers
## Finding
Let \(n>1\) be strongly pseudoperfect and put \(A=\sigma(n)-2n\). In every strongly pseudoperfect representation, each omitted nonsquare complementary divisor pair \(\{d,n/d\}\), with \(d<n/d\), satisfies \(d+n/d\le A\). Hence, when \(A\ge2\sqrt n\), its smaller member lies in \([\,(A-\sqrt{A^2-4n})/2,\sqrt n\,)\); when \(A<2\sqrt n\), no nonsquare complementary pair can be omitted. In particular, if \(\sigma(n)\le3n\), then \((1,n)\) occurs in every strongly pseudoperfect representation, so Wang--Zelinsky Theorem 5 implies that \(n^k\) is strongly pseudoperfect for every integer \(k\ge1\). Moreover, \(720\) is the least positive integer admitting a strongly pseudoperfect representation that omits \((1,n)\): for \(720\), the omitted pairs may be \((1,720),(10,72),(16,45),(18,40),(20,36)\), whose entries sum to \(978=\sigma(720)-1440\), while exhaustive complement-pair subset enumeration rules this out for every \(2\le n<720\).

## Assumptions and scope
A strongly pseudoperfect representation of an integer \(n>1\) is a subset \(S\) of the positive divisors of \(n\) such that \(d\in S\) if and only if \(n/d\in S\), and \(\sum_{{d\in S}}d=2n\). Put \(A=\sigma(n)-2n\). The complement of \(S\) in the divisor set is called the omitted set. A nonsquare complementary pair means \(\{{d,n/d}}\) with \(d<n/d\); when \(n\) is a square, the self-complementary divisor \(\sqrt n\) is not covered by the two-element pair inequality.

## Proof
Because the omitted divisors are exactly the complement of \(S\), their total sum is
\[
\sigma(n)-2n=A.
\]
The omitted set is also closed under \(d\mapsto n/d\). Therefore, if a nonsquare pair \(\{{d,n/d}}\) is omitted, its positive contribution is at most the whole omitted sum:
\[
d+\frac nd\le A.
\]
For \(0<d<\sqrt n\), this is equivalent to
\[
d^2-Ad+n\le0.
\]
Real solutions require \(A^2\ge4n\). When \(A\ge2\sqrt n\), the smaller divisor must therefore satisfy
\[
d\ge \frac{A-\sqrt{{A^2-4n}}}{2},
\]
and of course \(d<\sqrt n\). If \(A<2\sqrt n\), no nonsquare complementary pair can be omitted.

Now suppose \(\sigma(n)\le3n\). Then \(A\le n<n+1\). The complementary pair \((1,n)\) has sum \(n+1>A\), so it cannot be omitted from any strongly pseudoperfect representation. Wang and Zelinsky's Theorem 5 states that a strongly pseudoperfect integer having a representation containing \((1,n)\) has every positive power strongly pseudoperfect. Hence \(n^k\) is strongly pseudoperfect for every integer \(k\ge1\).

For the finite boundary statement, \(\sigma(720)=2418\), so \(A=978\). The five complementary pairs
\[
(1,720),\ (10,72),\ (16,45),\ (18,40),\ (20,36)
\]
have total sum \(721+82+61+58+56=978\). Omitting exactly those pairs leaves a complement-closed divisor set of sum \(2418-978=1440=2\cdot720\), so it is a strongly pseudoperfect representation omitting \((1,720)\). For each \(2\le n<720\), the attached exact verifier enumerates the complementary divisor-pair weights and checks, by integer subset-sum dynamic programming, that no omitted set containing \((1,n)\) has total \(\sigma(n)-2n\). This is exhaustive because every complement-closed omitted set is uniquely a subset of those pair-orbits, with the square-root singleton treated as a one-element orbit.

## Verification
`verify.py` performs the exact finite enumeration for every \(2\le n\le720\), checks the displayed witness for \(720\), and independently checks the divisor-sum identity. The infinite forced-pair and power-closure statements are proved algebraically above; the computation is used only for the least-escape assertion.

## Relationship to prior work
Wang and Zelinsky introduced the current structural study of strongly pseudoperfect representations, define omitted divisors, prove Theorem 5 giving power closure when a representation contains \((1,n)\), and explicitly ask whether every strongly pseudoperfect integer has all positive powers strongly pseudoperfect. Their Proposition 15 uses the lower bound \(d+n/d\ge2\sqrt n\) to exclude a different narrow-abundance regime for nonsquares, but does not give the forced-pair band, the \(\sigma(n)\le3n\) power-closure criterion, or the least representation that can omit \((1,n)\). OEIS A334405 records \(720\) as strongly pseudoperfect, but the checked entry does not state the omitted-pair witness or its leastness. Semantic searches also found results on low prime-factor counts and the dyadic \(60\) family, neither of which implies this abundance criterion or the exact first escape.

## Limitations
The criterion \(\sigma(n)\le3n\) is sufficient, not necessary, for power closure. The result does not resolve whether every strongly pseudoperfect integer has some representation containing \((1,n)\), nor Wang--Zelinsky Question 19 in full. The central-band assertion concerns two-element complementary pairs; a square-root singleton, when present, is governed only by its own contribution \(\sqrt n\le A\) if omitted. The least-\(720\) statement concerns the existence of a representation omitting \((1,n)\), not the absence of another representation containing it.

## References
1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068v1, first public 2026-09-28; primary MSC 11A25.
2. OEIS A334405, strongly pseudoperfect numbers.
