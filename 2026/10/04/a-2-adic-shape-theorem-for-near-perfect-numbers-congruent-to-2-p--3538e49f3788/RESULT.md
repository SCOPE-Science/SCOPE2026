# A 2-adic shape theorem for near-perfect numbers congruent to \(2\pmod 4\)
## Finding
Let \(n\) be near-perfect with redundant divisor \(d\), so \(d\) is a positive proper divisor of \(n\) and \(\sigma(n)=2n+d\). If \(n=2m\equiv2\pmod4\), with \(m\) odd, then exactly one of the following occurs:

1. \(m\) is a square and \(d\) is odd.
2. There are a unique prime \(p\equiv1\pmod4\), an integer \(u\ge0\), and an odd integer \(s\) with \(p\nmid s\) such that
\[
m=p^{4u+1}s^2,
\]
and in this case \(d\equiv2\pmod4\).

Thus the odd part of any near-perfect integer with 2-adic valuation one has at most one prime occurring to an odd exponent. If such a prime occurs, both that prime and its exponent are congruent to \(1\pmod4\). The redundant divisor is odd if and only if the odd part is a square.

The known examples \(18=2\cdot3^2\), \(234=2\cdot3^2\cdot13\), and \(650=2\cdot5^2\cdot13\) illustrate both branches: their redundant divisors are respectively \(3\), \(78\), and \(2\).
## Assumptions and scope
The statement concerns ordinary near-perfect integers: \(n>1\) and there is a positive proper divisor \(d\mid n\) satisfying \(\sigma(n)=2n+d\). The only imposed arithmetic restriction is \(v_2(n)=1\). There is no restriction on the number of odd prime factors or on their sizes.

The result is necessary, not sufficient: an odd integer of one of the displayed shapes need not make \(2m\) near-perfect.
## Proof
Write \(n=2m\) with \(m\) odd. Multiplicativity of \(\sigma\) gives
\[
3\sigma(m)=\sigma(2m)=4m+d. \tag{1}
\]
For odd \(m=\prod_i p_i^{a_i}\), the factor \(\sigma(p_i^{a_i})\) is odd exactly when \(a_i\) is even, because it is a sum of \(a_i+1\) odd terms. Hence \(\sigma(m)\) is odd exactly when every \(a_i\) is even, equivalently exactly when \(m\) is a square.

Taking (1) modulo \(2\), and noting that \(4m\) is even, shows that \(d\) has the same parity as \(\sigma(m)\). Therefore \(d\) is odd if and only if \(m\) is a square. This proves the first branch and the asserted parity equivalence.

Suppose now that \(m\) is not a square. Then \(d\) is even. Since \(d\mid2m\) and \(m\) is odd, necessarily \(v_2(d)=1\). Write \(d=2e\) with \(e\) odd. Dividing (1) by \(2\) gives
\[
\frac{3\sigma(m)}2=2m+e.
\]
The right side is odd, so
\[
v_2(\sigma(m))=1. \tag{2}
\]
Because \(\sigma\) is multiplicative,
\[
v_2(\sigma(m))=\sum_i v_2(\sigma(p_i^{a_i})).
\]
Every even exponent \(a_i\) contributes zero, while every odd exponent contributes at least one. Equation (2) therefore forces exactly one exponent, say \(a\) at the prime \(p\), to be odd; all remaining exponents are even. For odd \(a\), the standard 2-adic lifting formula applied to \(p^{a+1}-1\) yields
\[
v_2(\sigma(p^a))=v_2(p+1)+v_2(a+1)-1.
\]
This value must equal one by (2). Both terms on the right before subtracting one are at least one, hence
\[
v_2(p+1)=v_2(a+1)=1.
\]
Consequently \(p\equiv1\pmod4\) and \(a\equiv1\pmod4\). Writing \(a=4u+1\) and collecting all even prime exponents into a square gives
\[
m=p^{4u+1}s^2,
\]
with \(p\nmid s\). Since already \(v_2(d)=1\), also \(d\equiv2\pmod4\). This is the second branch and completes the proof.
## Verification
A standalone exact-integer checker enumerates every integer through \(2{,}000{,}000\), computes \(\sigma(n)\) by a divisor-sum sieve, recognizes near-perfect integers directly from \(0<\sigma(n)-2n<n\) and divisibility, and tests the theorem for every recognized integer congruent to \(2\pmod4\). It finds fifty near-perfect integers in that range and exactly three in the target residue class, namely \(18,234,650\); all satisfy the theorem. This finite computation is corroborative only. The proof above is infinite and does not depend on the enumeration.
## Relationship to prior work
Pollack and Shevelev introduced near-perfect numbers, gave construction families, and singled out the odd-redundant-divisor problem; their early preprint also notes that odd squarefree integers cannot be near-perfect. Ren and Chen completely classified near-perfect integers having exactly two distinct prime factors and listed \(234\) and \(650\) among the early examples having three distinct prime factors. Tang, Ma, and Feng studied odd near-perfect integers and proved the complete four-prime-factor odd case.

The present statement is different in implication direction and scope: it imposes only \(v_2(n)=1\), allows arbitrarily many odd prime factors, and constrains the entire parity pattern of their exponents. The inspected sources do not state the equivalence between odd redundant divisor and square odd part in this slice, nor the alternative shape \(p^{4u+1}s^2\) with \(p\equiv1\pmod4\). OEIS A181595 lists the relevant examples but does not give this arbitrary-support structural restriction.
## Limitations
The theorem supplies only necessary conditions. It does not classify which squares \(m\) or which values \(p^{4u+1}s^2\) actually produce a near-perfect integer \(2m\), and it does not address integers divisible by \(4\). The finite verification bound is not used as evidence for the infinite quantifier.
## References
1. P. Pollack and V. Shevelev, *On perfect and near-perfect numbers*, Journal of Number Theory 132 (2012), 3037–3046. arXiv:1011.6160; doi:10.1016/j.jnt.2012.06.008.
2. X.-Z. Ren and Y.-G. Chen, *On near-perfect numbers with two distinct prime factors*, Bulletin of the Australian Mathematical Society 88 (2013), 520–524. doi:10.1017/S0004972713000178.
3. M. Tang, X. Ma, and M. Feng, *On near-perfect numbers*, Colloquium Mathematicum 144 (2016), 157–188. doi:10.4064/cm6588-10-2015.
4. OEIS Foundation Inc., A181595, *Near-perfect numbers*.
