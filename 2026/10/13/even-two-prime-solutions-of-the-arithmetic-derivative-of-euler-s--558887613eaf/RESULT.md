# Even two-prime solutions of the arithmetic derivative of Euler’s totient

## Finding
Let \(D\) be the arithmetic derivative on positive integers: \(D(1)=0\), \(D(p)=1\) for each prime, and \(D(mn)=mD(n)+nD(m)\). Let \(\varphi\) denote Euler's totient, and \(\omega\) the number of distinct prime divisors, with \(\omega(1)=0\).

**Theorem.** Let \(p\) be any odd prime, and let \(a,b\ge1\). Write \(p-1=2^t u\), where \(t\ge1\) and \(u\) is odd. Assume \(\omega(u)\le2\). Then
\[
D(\varphi(2^a p^b))=2^a p^b
\]
holds if and only if exactly one of the following applies:

1. \(p=3\), and \((a,b)\in\{(6,1),(4,4),(2,7)\}\).
2. \(p=5\), and \((a,b)\in\{(4,1),(2,6)\}\).
3. \(p=2q+1\) with \(q\ge3\) an odd prime, and \((a,b)\in\{(4,1),(2,p+1)\}\).
4. \(p=61\), and \((a,b)=(2,1)\).

Thus the family \(16p\), together with \(4p^{p+1}\), satisfies the equation whenever \(p\ge7\) is prime and \((p-1)/2\) is prime. The latter example has an exponent growing with \(p\). Among the solutions with \(\omega(u)=2\), only \(n=244\) occurs.

## Assumptions and scope
The integer \(n=2^a p^b\) has precisely two distinct prime divisors, one of which is \(2\). The supplementary assumption restricts the number of distinct odd prime factors of \(p-1\), not the size or exponents of \(n\). All assertions hold for every allowed odd prime and all positive exponents. We make no claim about solutions having three or more odd prime factors of \(p-1\), or about integers \(n\) not of this form.

## Proof
For any integer \(m=\prod_\ell\ell^{e_\ell}\), logarithmic differentiation of its prime-power factorization gives the exact identity
\[
\frac{D(m)}m=\sum_{\ell\mid m}\frac{e_\ell}{\ell}.
\]
For \(n=2^a p^b\), write \(p-1=2^t u\) with \(u\) odd. Then
\[
 m=\varphi(n)=2^{a+t-1}p^{b-1}u,
 \qquad \frac{n}{m}=\frac{2p}{p-1}=2+\frac{2}{p-1}.
\]
If \(u=\prod_{q\mid u}q^{e_q}\), applying the logarithmic derivative gives the equivalent exact equality
\[
 a+t-1+\frac{2(b-1)}p+2\sum_{q\mid u}\frac{e_q}q
 =4+\frac4{2^t u}. \tag{1}
\]
Because \(p\) is coprime to \(2u\), the only potential \(p\)-denominator in (1) is \(2(b-1)/p\). Therefore \(p\mid b-1\). Put \(b=1+kp\), \(k\ge0\).

The left-hand side of (1) now has odd denominator in lowest terms. If \(t\ge3\), the right-hand side has a nonintegral factor of \(2\) in its denominator, a contradiction. Hence \(t=1\) or \(t=2\).

If some odd \(q\) satisfies \(q^e\parallel u\) with \(e\ge2\), the \(q\)-adic valuation of the rational term \(4/(2^tu)\) is \(-e\); all other terms on the left of (1) have valuation at least \(-1\), so equality is impossible. Consequently \(u\) is squarefree.

Set \(S(u)=\sum_{q\mid u}1/q\), with \(S(1)=0\). For \(t=1\), rearranging (1) gives
\[
 a=4-2k-2\left(S(u)-\frac1u\right). \tag{2}
\]
For \(t=2\), it gives
\[
 a=3-2k-\left(2S(u)-\frac1u\right). \tag{3}
\]
Both right-hand sides must be positive integers. In (2), since the denominator of \(S(u)-1/u\) is odd, integrality of \(2(S(u)-1/u)\) implies integrality of \(S(u)-1/u\). The reductions are reversible, so (2) and (3), with these integrality conditions, provide an exact test even without the restriction on \(\omega(u)\).

Now assume \(\omega(u)\le2\). If \(t=1\) and \(u=1\), then \(p=3\) and equation (2) becomes \(a=6-2k\). Positivity gives \(k\in\{0,1,2\}\), yielding \((a,b)=(6,1),(4,4),(2,7)\). If \(t=1\) and \(u=q\) is an odd prime, then \(p=2q+1\), \(S(u)-1/u=0\), and \(a=4-2k\). Here \(k\in\{0,1\}\), giving \((a,b)=(4,1),(2,p+1)\). If \(t=1\) and \(u=qr\) with distinct odd primes \(q<r\), then
\[
 0< S(u)-\frac1u=\frac{q+r-1}{qr}<1,
\]
so (2) cannot give an integral \(a\).

If \(t=2\) and \(u=1\), then \(p=5\), equation (3) reads \(a=4-2k\), and \(k\in\{0,1\}\), yielding \((4,1),(2,6)\). If \(t=2\) and \(u=q\) is a single odd prime, then \(2S(u)-1/u=1/q\), which is not an integer.

Finally suppose \(t=2\) and \(u=qr\) with \(3\le q<r\) distinct odd primes. Equation (3) requires the positive rational
\[
 J(q,r)=\frac{2q+2r-1}{qr}
\]
to be integral. For \((q,r)=(3,5)\), it equals \(1\). For \(q=3,r\ge7\), we have \(2q+2r-1<qr\), because \(5<r\). For \(q\ge5,r\ge7\), the same strict inequality holds: \((q-2)(r-2)>3\). Thus \((3,5)\) is the sole possibility. It gives \(u=15\), \(p=4u+1=61\), \(J=1\), and \(a=2-2k\). Positivity forces \(k=0\), hence \((a,b)=(2,1)\). Every stated case satisfies (1) by reversal. This exhausts all possibilities and proves the theorem.

## Verification
A standalone Python program, `verify.py`, evaluates \(\varphi(2^a p^b)\) as an exact integer and computes its arithmetic derivative by independently factoring the resulting integer. It compares the computed equation with the classification on 15,980 tuples with odd primes \(p<501\), \(1\le a\le10\), and \(1\le b\le17\). It also tests 1,080 further parameter triples featuring the large exponents \(b=p+1\) and \(b=2p+1\). All tests passed. The verified examples include \(n=192,1296,8748,80,112,244\). This finite computation is a diagnostic check, not the proof for all exponents.

Run `python verify.py` after installing the Python package `sympy`; the script uses only exact integer and rational arithmetic.

## Relationship to prior work
OEIS A248815 records the equation \(n=D(\varphi(n))\) and an extensive numerical sequence of its solutions, but the examined entry states no prime-support classification. OEIS A217715 concerns the *reversed* composition \(n=\varphi(D(n))\) and its displayed safe-prime examples; that assertion does not imply the present classification. Grau and Oller-Marcén's 2012 study of the arithmetic derivative instead relates Giuga numbers to \(D(u)=cu+1\). Its prime-factorization formula is consistent with (1), but its theorem does not establish the totient-composition classification here. Related published results on \(D(n)\), \(D^3(n)\), and \(D(n)-(n-\varphi(n))\) likewise address different equations. The key added structure here is the exact dependence on the odd prime support of \(p-1\), including the two large-exponent families and the exceptional \(61\)-case.

## Limitations
This result does not classify solutions for \(\omega(u)\ge3\), for odd integers, or for integers with three or more prime factors. It does not assert the infinitude of primes \(p\) for which \((p-1)/2\) is prime. The classification is proved mathematically; the accompanying finite checks establish no exhaustive statement outside their listed ranges. Earlier unindexed treatments of this composition equation could overlap with the result.

## References
1. P. P. Lava, **OEIS A248815**, “Numbers equal to the arithmetic derivative of their Euler totient function,” initial sequence entry dated 2014-10-15, https://oeis.org/A248815.
2. P. P. Lava, **OEIS A217715**, “Numbers equal to the Euler totient function of their arithmetic derivative,” https://oeis.org/A217715.
3. **OEIS A003415**, “Arithmetic derivative,” https://oeis.org/A003415.
4. J. M. Grau and A. M. Oller-Marcén, “Giuga Numbers and the Arithmetic Derivative,” *Journal of Integer Sequences* **15** (2012), Article 12.4.1, https://cs.uwaterloo.ca/journals/JIS/VOL15/Oller/oller5.pdf.
