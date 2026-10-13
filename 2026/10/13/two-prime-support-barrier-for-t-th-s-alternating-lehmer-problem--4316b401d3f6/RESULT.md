# Two-prime-support barrier for Tóth's alternating Lehmer problem
## Finding
Let \(\beta\) be the multiplicative alternating sum-of-divisors function defined on prime powers by
\[
\beta(p^a)=p^a-p^{a-1}+p^{a-2}-\cdots+(-1)^a
=\frac{p^{a+1}+(-1)^a}{p+1}.
\]
If a composite integer \(n\) satisfies
\[
\beta(n)\mid n-1
\]
and has at most two distinct prime factors, then
\[
n=4.
\]
Therefore every hypothetical composite solution other than \(4\) to the alternating analogue of Lehmer's problem posed by Tóth has at least three distinct prime factors.

## Assumptions and scope
Write \(\omega(n)\) for the number of distinct prime factors of \(n\). The theorem concerns composite \(n\) with \(\omega(n)\le2\). Exponents are unrestricted.

Two elementary facts will be used. For every prime \(p\) and integer \(a\ge1\),
\[
0<\beta(p^a)<p^a
\]
and
\[
\beta(p^a)\ge p^{a-1}(p-1),
\tag{1}
\]
with equality in (1) exactly when \(a=1\). Indeed, after multiplication by \(p+1\), inequality (1) is equivalent to
\[
p^{a+1}+(-1)^a\ge p^{a+1}-p^{a-1}.
\]

For odd \(q\), the parity of \(\beta(q^b)\) is the parity of \(b+1\), because its alternating expansion contains \(b+1\) odd summands. Also \(\beta(2^a)\) is always odd.

## Proof
First suppose \(n=p^a\) with \(a\ge2\). Put \(B=\beta(p^a)\) and \(\varepsilon=(-1)^a\). If \(B\mid p^a-1\), then
\[
p^{a+1}\equiv p\pmod B.
\]
But
\[
(p+1)B=p^{a+1}+\varepsilon,
\]
so also
\[
p^{a+1}\equiv-\varepsilon\pmod B.
\]
Hence
\[
B\mid p+\varepsilon.
\tag{2}
\]
If \(a\) is odd, then \(a\ge3\), and (1) gives \(B>p-1\), contradicting (2). If \(a\) is even and \(a\ge4\), then (1) gives \(B>p+1\), again contradicting (2). For \(a=2\), relation (2) requires
\[
p^2-p+1\le p+1,
\]
so \(p\le2\). Thus the only prime-power solution is
\[
n=2^2=4.
\]

Now suppose
\[
n=p^a q^b,
\qquad p<q,
\qquad a,b\ge1,
\]
with distinct primes \(p,q\). Put
\[
B=\beta(p^a)\beta(q^b)
\]
and, under the divisibility hypothesis, write
\[
k=\frac{n-1}{B}\in\mathbb Z_{>0}.
\]

If \(p\) and \(q\) are both odd, then \(p\ge3\) and \(q\ge5\). From (1),
\[
\frac nB
\le\frac p{p-1}\frac q{q-1}
\le\frac32\frac54
=\frac{15}{8}<2.
\]
Therefore \(k<n/B<2\), so \(k=1\). This would give \(B=n-1\). Yet each prime-power factor satisfies \(\beta(p^a)\le p^a-1\), hence
\[
B\le(p^a-1)(q^b-1)<n-1,
\]
a contradiction.

It remains to take \(p=2\) and \(q\) odd. Since \(B\mid n-1\) and \(n-1\) is odd, \(B\) is odd. Because \(\beta(2^a)\) is odd, \(\beta(q^b)\) is odd, forcing \(b\) to be even. Equality in (1) is then impossible for the \(q\)-factor, so
\[
\frac{q^b}{\beta(q^b)}<\frac q{q-1}.
\]
Together with
\[
\frac{2^a}{\beta(2^a)}\le2,
\]
this yields
\[
\frac nB<2\frac q{q-1}\le3.
\]
The integer \(k=(n-1)/B\) is odd, since both numerator and denominator are odd. Thus the positive odd integer \(k\) satisfies \(k<3\), so \(k=1\). As in the odd-odd case, this contradicts
\[
B\le(2^a-1)(q^b-1)<n-1.
\]

All cases with \(\omega(n)\le2\) are exhausted, proving the theorem.

## Verification
The accompanying checker independently factors every integer
\[
4\le n\le2{,}000{,}000,
\]
keeps the composite integers with \(\omega(n)\le2\), evaluates \(\beta\) exactly from the prime-power formula, and tests \(\beta(n)\mid n-1\). It finds only \(n=4\) among \(554175\) tested low-support composites.

The checker also verifies the prime-power inequalities and parity statements used in the proof for thousands of prime-power instances. These finite checks are corroborative only; the proof above is universal.

## Relationship to prior work
Tóth's survey defines the same multiplicative function \(\beta\) and poses as Problem 4 whether any composite \(n\ne4\) can satisfy \(\beta(n)\mid n-1\). The paper reports a Maple search through \(10^6\) with no such composite example but gives no structural exclusion by prime support.

For squarefree \(n\), one has \(\beta(n)=\varphi(n)\), so classical results on Lehmer's totient problem give much stronger restrictions within that squarefree subcase. They do not cover nonsquarefree integers, where \(\beta\) differs from \(\varphi\). The theorem here closes the entire one- and two-prime-support range, including arbitrary prime-power exponents.

A 2024 paper with a similar title studies a different alternating divisor function obtained by ordering all divisors; it is nonmultiplicative and does not imply the present statement.

## Limitations
The theorem does not address integers with three or more distinct prime factors. It therefore does not settle Tóth's Problem 4 in full.

The originality comparison used the primary full text, targeted searches for the exact divisibility condition and its low-support variants, and comparison with the classical Lehmer implication in the squarefree case. An equivalent argument in an unindexed note remains a residual risk.

## References
1. L. Tóth, “A survey of the alternating sum-of-divisors function,” arXiv:1111.4842v1, first public 21 November 2011; later *Acta Universitatis Sapientiae, Mathematica* 5 (2013), 93–107, DOI 10.2478/ausm-2014-0007.
2. M. Caragiu and K. Swieringa, “On the alternating sum-of-divisors,” *JP Journal of Algebra, Number Theory and Applications* 63 (2024), 97–110, DOI 10.17654/0972555524006. This reference concerns a different, nonmultiplicative alternating divisor function.
