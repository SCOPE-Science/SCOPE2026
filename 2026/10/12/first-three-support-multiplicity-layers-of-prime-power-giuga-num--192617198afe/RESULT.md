# First three-support multiplicity layers of prime power Giuga numbers
## Finding
Let \(n\) be a prime power Giuga number with exactly three distinct prime divisors. Write \(\Omega(n)\) for the total number of prime factors counted with multiplicity. Then
\[
\Omega(n)\le 4 \quad\Longrightarrow\quad n\in\{30,306,380\}.
\]
The three values all occur. The squarefree layer is uniquely \(30=2\cdot3\cdot5\), while the first non-squarefree layer is
\[
\Omega(n)=4 \quad\Longleftrightarrow\quad n\in\{306,380\}
\]
among prime power Giuga numbers having exactly three distinct prime divisors.

## Assumptions and scope
A prime power Giuga number is a positive composite integer \(n>1\) for which
\[
G(n):=\sum_{p^k\mid n}\frac1{p^k}-\frac1n
\]
is a positive integer, where the sum is over all positive prime powers dividing \(n\). For the three-prime-support case considered here, this condition automatically forces \(G(n)=1\).

The result concerns exactly three distinct prime divisors and only the layers \(\Omega(n)\le4\). It does not classify higher multiplicity layers.

## Proof
Suppose first that \(n\) has exactly three distinct prime divisors \(p<q<r\). If \(p\ge3\), then
\[
G(n)<\frac1{p-1}+\frac1{q-1}+\frac1{r-1}\le \frac12+\frac14+\frac16=\frac{11}{12}<1,
\]
contradicting the requirement that \(G(n)\) be a positive integer. Hence \(p=2\). Also
\[
G(n)<1+\frac12+\frac14=\frac74<2,
\]
so necessarily \(G(n)=1\).

We use one local congruence consequence of this equality. If \(s^a\Vert n\) and \(m=n/s^a\), multiplying \(G(n)=1\) by \(n\) and reducing modulo \(s^a\) gives
\[
m(1+s+\cdots+s^{a-1})\equiv1\pmod{s^a}. \tag{1}
\]
Indeed, terms belonging to the other prime supports are divisible by \(s^a\), while the \(s\)-power terms contribute \(m(s^{a-1}+\cdots+1)\).

For \(\Omega(n)=3\), write \(n=2qr\). Congruence (1) at \(q\) and \(r\) yields
\[
2r\equiv1\pmod q,\qquad 2q\equiv1\pmod r.
\]
Since \(q<r\), the second congruence forces \(r=2q-1\). Substituting into the first gives \(q\mid3\), hence \(q=3\) and \(r=5\). Thus \(n=30\).

Now assume \(\Omega(n)=4\). There are three exponent patterns.

If \(n=2^2qr\), then (1) at the odd primes gives
\[
4r\equiv1\pmod q,\qquad4q\equiv1\pmod r.
\]
Thus \(4q-1=kr\) with \(k\in\{1,3\}\). If \(k=1\), substituting \(r=4q-1\) into the first congruence gives \(q\mid5\), hence \((q,r)=(5,19)\). If \(k=3\), multiplying the first congruence by \(3\) after using \(3r=4q-1\) gives \(q\mid7\); then \(q=7\) would give \(r=9\), impossible. Hence this pattern gives only \(380\).

If \(n=2q^2r\), congruence (1) gives
\[
2r(q+1)\equiv1\pmod{q^2},\qquad 2q^2\equiv1\pmod r.
\]
Put \(2q^2-1=dr\). Since \(r>q\), we have \(0<d<2q\), and \(d\) is odd. Multiplying the first congruence by \(d\) and using \(dr\equiv-1\pmod{q^2}\) gives
\[
d\equiv-2(q+1)\pmod{q^2}.
\]
For every odd prime \(q\ge5\), the least positive residue \(q^2-2q-2\) is greater than \(2q\), contradicting \(d<2q\). Therefore \(q=3\), and then \(d\equiv1\pmod9\) together with \(0<d<6\) gives \(d=1\) and \(r=17\). This yields \(306\).

Finally, if \(n=2qr^2\), congruence (1) at \(r\) gives
\[
2q(r+1)\equiv1\pmod{r^2}.
\]
The positive integer \(2q(r+1)-1\) is less than \(2r^2+2r-1<3r^2\), and its quotient by the odd number \(r^2\) must be odd. Hence the quotient would have to be \(1\), so
\[
2q(r+1)-1=r^2.
\]
But the left side is \(3\pmod4\) while \(r^2\equiv1\pmod4\), a contradiction. Thus this exponent pattern is impossible.

Direct substitution verifies the surviving values:
\[
-\frac1{30}+\frac12+\frac13+\frac15=1,
\]
\[
-\frac1{306}+\frac12+\frac13+\frac19+\frac1{17}=1,
\]
and
\[
-\frac1{380}+\frac12+\frac14+\frac15+\frac1{19}=1.
\]
This proves the classification.

## Verification
The argument is bound-free. The only case split is the complete list of exponent partitions of \(4\) across three positive exponents: \((2,1,1)\), \((1,2,1)\), and \((1,1,2)\). Each branch is closed by congruences derived directly from the defining Egyptian-fraction identity. The three displayed reciprocal identities independently verify the surviving values.

As a regression check, direct exact-rational enumeration through \(200000\) finds exactly \(30,306,380\) among three-support prime power Giuga numbers with \(\Omega(n)\le4\). This finite check is not used to prove exhaustiveness.

## Relationship to prior work
Machacek introduced prime power Giuga numbers, proved sufficient factorization constructions, and tabulated all such numbers below \(10^7\). That table contains \(30,306,380\), but the inspected paper does not state an exhaustiveness theorem for the first three-support multiplicity layers. The paper also notes that its main sufficient construction is not necessary.

OEIS A286497 lists the same three integers near the start of the prime power Giuga sequence and supplies computational-generation information. A sequence table is consistent with the theorem but does not prove that no other three-support integer can occur with \(\Omega(n)\le4\).

A closely related published database result classifies the two-prime-support case: prime power Giuga numbers with two distinct prime divisors are exactly the Mersenne family \(2^a(2^a-1)\) when \(2^a-1\) is prime. That theorem is disjoint from, and does not imply, the present exact three-support boundary classification.

## Limitations
The theorem does not address three-support examples with \(\Omega(n)\ge5\), nor prime power Giuga numbers with four or more distinct prime divisors. The originality comparison covered the focal full text, the canonical OEIS table, targeted web searches, and targeted mathematical-result database searches; unindexed or inaccessible literature remains a residual risk.

## References
1. John Machacek, “Egyptian Fractions and Prime Power Divisors,” arXiv:1706.01008v1, first submitted 2017-06-04; Journal of Integer Sequences 21 (2018), Article 18.3.7. Primary MSC 11D68.
2. OEIS A286497, “Prime power Giuga numbers,” author record dated 2017-05-27.
