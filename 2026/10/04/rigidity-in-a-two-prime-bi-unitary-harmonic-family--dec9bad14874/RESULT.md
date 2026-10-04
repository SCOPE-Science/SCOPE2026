# Rigidity in a two-prime bi-unitary harmonic family
## Finding
Let \(p\) and \(q\) be distinct primes and let \(a\ge1\). Put \(n=p^{2a}q\). Then \(n\) is bi-unitary harmonic if and only if
\[
(p,a,q)=(3,1,5).
\]
Thus the unique member of this infinite two-prime family is \(45=3^2\cdot5\).

## Assumptions and scope
For a positive integer \(m\), write \(\sigma^{**}(m)\) and \(d^{**}(m)\) for the sum and number of bi-unitary divisors. A number is bi-unitary harmonic when
\[
\sigma^{**}(m)\mid m\,d^{**}(m).
\]
For a prime power with even exponent,
\[
\sigma^{**}(p^{2a})=\sigma(p^{2a})-p^a
=\frac{(p^a-1)(p^{a+1}+1)}{p-1},
\qquad d^{**}(p^{2a})=2a.
\]
For a prime \(q\), \(\sigma^{**}(q)=q+1\) and \(d^{**}(q)=2\). The result classifies only the family \(p^{2a}q\); it does not classify every bi-unitary harmonic number with two distinct prime factors.

## Proof
Set
\[
A=\frac{p^a-1}{p-1}=1+p+\cdots+p^{a-1},
\qquad C=p^{a+1}+1.
\]
Then \(\sigma^{**}(p^{2a})=AC\). If \(p^{2a}q\) is bi-unitary harmonic, multiplicativity gives
\[
AC(q+1)\mid 4a\,p^{2a}q.
\]
Since \((AC,p)=1\) and \((q+1,q)=1\), necessarily
\[
AC\mid4aq,\qquad q+1\mid4a p^{2a}.\tag{1}
\]

First suppose \(q<p\). Then \(p\nmid q+1\): otherwise the prime \(p\) would equal \(q+1\), forcing the impossible consecutive-prime pair with difference one. Hence (1) gives \(q+1\mid4a\), so \(q<4a\). Because \(AC>p^{2a}\) and \(AC\le4aq<16a^2\), we get \(3^{2a}<16a^2\). This fails for every \(a\ge2\), so \(a=1\). Then \(q+1\mid4\), hence \(q=3\), while \(p>3\); but \(p^2+1=AC\mid4q=12\), impossible. Thus no solution has \(q<p\).

Now suppose \(p<q\). If \(q\le4a\), then \(AC\le16a^2\). Since \(AC>p^{2a}\ge4^a\), this is impossible for \(a\ge4\). For \(a=1,2,3\), the same inequality leaves only the following possibilities: \((a,p)=(1,2),(2,2),(3,2)\). Directly, \(AC\) is respectively \(5,27,119\), and none divides \(4aq\) for a prime \(q\) with \(p<q\le4a\). So no solution occurs here.

It remains that \(p<q\) and \(q>4a\). Then \(q\nmid4a\), so (1) forces \(q\mid AC\). Moreover
\[
\gcd(A,C)\mid p+1.
\]
The prime \(q\) cannot divide both \(A\) and \(C\): since \(p<q\), this would force \(q=p+1\), and the only consecutive primes differing by one are \(2,3\), incompatible with \(q>4a\). If \(q\mid A\), then \(AC/q\mid4a\) while \(C>4a\), a contradiction. Hence \(q\mid C\), and therefore \(A\mid4a\). Since \(A\ge2^a-1\), one has \(a\le4\).

The four remaining exponents close exactly.

For \(a=1\), \(A=1\) and \(C=p^2+1=tq\) with \(t\mid4\). If \(t=1\), primality forces \(p=2,q=5\), but then \(q+1\nmid4p^2\). If \(t=4\), no prime \(p\) works because \(p^2+1\) is never divisible by \(4\). If \(t=2\), then \(p\) is odd and
\[
q=\frac{p^2+1}2,
\qquad q+1=\frac{p^2+3}2\mid4p^2.
\]
For \(p\ne3\), the last divisor is coprime to \(p\), so it would divide \(4\), impossible. Thus \(p=3\), giving \(q=5\).

For \(a=2\), \(A=p+1\mid8\), hence \(p=3\) or \(7\). The corresponding \(C=p^3+1\) is \(28\) or \(344\), and no quotient \(C/q\) compatible with \(A(C/q)\mid8\) produces a prime \(q>8\).

For \(a=3\), \(A=p^2+p+1\le12\) forces \(p=2\). Then \(A=7\), \(C=17\), and the only possible \(q>12\) is \(17\), but \(AC/q=7\nmid12\).

For \(a=4\), \(A=1+p+p^2+p^3\le16\) forces \(p=2\). Then \(C=33\), which has no prime divisor exceeding \(16\).

Thus the only possible triple is \((p,a,q)=(3,1,5)\). Finally,
\[
\sigma^{**}(45)=\sigma^{**}(3^2)\sigma^{**}(5)=10\cdot6=60,
\qquad 45\,d^{**}(45)=45\cdot4=180,
\]
so \(60\mid180\). Hence \(45\) is indeed bi-unitary harmonic.

## Verification
The accompanying checker implements the defining prime-power formulas, verifies \(45\) directly, replays every finite branch left by the proof, and performs an additional bounded scan as a non-proof sanity check. The finite branch replay is exhaustive only because the proof above first reduces the infinite family to those branches.

## Relationship to prior work
Sándor introduced bi-unitary harmonic numbers and recorded the prime-power formulas used here. His 2011 paper proves several nearby low-support statements, including nonexistence for \(p^3q^2\), remarks on \(pq^4\) and \(p^3q^4\), and the isolated fact that the only number of the form \(p^2q\) is \(45\). Manea and Minculete later study different structured families such as \(2^k\) times a squarefree odd part, \(pqt^2\), and \(p^2q^2t\). The present result extends the isolated \(p^2q\) classification through every even exponent \(2a\) on that prime, without claiming a classification of arbitrary two-prime bi-unitary harmonic numbers.

## Limitations
The argument is specific to the exponent pattern \((2a,1)\). It does not settle families \(p^{2a}q^b\) with \(b>1\), nor the general two-prime problem. The bounded computational scan included with the package is corroborative only and is not used to infer the infinite theorem.

## References
1. J. Sándor, *On bi-unitary harmonic numbers*, arXiv:1105.0294, first version 2011-05-02.
2. A. Manea and N. Minculete, *Types of integer harmonic numbers (II)*, Bulletin of the Transilvania University of Braşov, Series III 9(58) (2016), 67–82.
3. OEIS A286325, *Bi-unitary harmonic numbers*, used only as a table/database cross-check.
