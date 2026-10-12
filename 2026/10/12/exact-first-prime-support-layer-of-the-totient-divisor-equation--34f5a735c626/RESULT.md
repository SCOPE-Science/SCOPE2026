# Exact first-prime-support layer of the totient–divisor equation

## Finding
For every positive integer \(m\), the equation
\[
\varphi(4m)+\tau(4m)=m
\]
has no solution with \(\omega(m)\le 3\), and its complete \(\omega(m)=4\) layer is
\[
\boxed{m\in\{1980,3900,4680\}.}
\]
Equivalently, the solutions of \(\varphi(n)+\tau(n)=n/4\) having exactly four distinct prime factors are
\[
\boxed{n\in\{7920,15600,18720\}.}
\]
All minimal-support solutions have prime support \(\{2,3,5,r\}\), with \(r\in\{11,13\}\) and \(\nu_r(m)=1\). The three displayed integers and their special-exponent form were already given by Sándor [1, Theorem 7]. The new assertion is completeness among **all** integers of prime support four, without an assumed prime support or an assumed exponent of the last prime.

## Assumptions and scope
Throughout, \(m\) is a positive integer, \(\varphi\) denotes Euler's totient, \(\tau\) counts positive divisors, and \(\omega\) counts distinct prime divisors (so \(\omega(1)=0\)). No numerical upper bound on \(m\), its primes, or its exponents is assumed. The equality is for \(\varphi(4m)+\tau(4m)=m\), not the related equations with denominator two or with squared divisor count.

## Proof
**1. No odd \(m\).** Suppose \(m\) is odd. Then \(2\varphi(m)+3\tau(m)=m\). Parity makes \(\tau(m)\) odd, so \(m=t^2\), with \(t\) odd and positive. Using \(\varphi(t^2)=t\varphi(t)\),
\[
t\bigl(t-2\varphi(t)\bigr)=3\tau(t^2).
\]
For every odd prime \(p\) and exponent \(a\ge1\), \(p^a\ge2a+1\), with equality only for \((p,a)=(3,1)\). Hence \(\tau(t^2)\le t\), with equality only at \(t=1,3\). The positive, odd integer \(t-2\varphi(t)\) is at most three, so it is one or three. If it is three, equality \(\tau(t^2)=t\) forces \(t=1\) or \(t=3\); in each case \(t-2\varphi(t)\neq3\).

If \(t-2\varphi(t)=1\), then \(t=3\tau(t^2)\), so
\[
\prod_{p^a\parallel t}\frac{p^a}{2a+1}=3.
\]
Each factor is increasing both in \(p\) and in its positive exponent \(a\). Three or more distinct odd primes yield product at least \((3/3)(5/3)(7/3)=35/9>3\). Two primes not including three yield product at least \((5/3)(7/3)>3\). If the smallest prime is three and the other is at least eleven, their product exceeds three. For supports \(\{3,7\}\), the first factor is one at exponent one, \(9/5\) at exponent two, and at least \(27/7\) thereafter; the second is at least \(7/3\), so no product equals three. For support \(\{3,5\}\), the unique product-three exponents are \((2,1)\), making \(t=45\), but \(45-2\varphi(45)=-3\neq1\). Finally, for a single prime, primes \(p\ge 11\) make the ratio greater than three; for \(p=3,5,7\), the consecutive ratios \(p^a/(2a+1)\) strictly increase and straddle three (for three: \(9/5<3<27/7\); for five and seven: \(p/3<3<p^2/5\)). Thus no odd \(m\) works.

**2. No even \(m\) with \(\omega(m)\le3\).** As \(m\) is even, the prime two occurs in \(m\). Euler's product gives
\[
\frac{\varphi(4m)}m=2\prod_{p\mid m,\ p\text{ odd}}\left(1-\frac1p\right).
\]
For at most two odd primes, the product is at least \((2/3)(4/5)\); thus \(\varphi(4m)/m\ge16/15>1\), contradicting \(\varphi(4m)+\tau(4m)=m\).

**3. The support-four primes are forced.** Write the three odd prime divisors as \(3\le p<q<r\). Necessarily \(\varphi(4m)/m<1\). If \(p\ge5\), the ratio is at least \(2(4/5)(6/7)(10/11)>1\); hence \(p=3\). If \(q\ge7\), it is at least \(2(2/3)(6/7)(10/11)>1\); hence \(q=5\). If \(r\ge17\), it is at least \(2(2/3)(4/5)(16/17)=256/255>1\); hence \(r\in\{7,11,13\}\).

**4. The final prime occurs once.** Write
\[
m=2^a3^b5^cr^d,\qquad a,b,c,d\ge1,\quad r\in\{7,11,13\}.
\]
The defining equality is equivalent, by the elementary product formulas for \(\varphi\) and \(\tau\), to
\[
(16-r)2^a3^{b-1}5^{c-1}r^{d-1}=(a+3)(b+1)(c+1)(d+1). \tag{1}
\]
The three ratios \(2^a/(a+3)\), \(3^{b-1}/(b+1)\), \(5^{c-1}/(c+1)\) are increasing for positive integer exponents and each is at least \(1/2\). If \(d\ge2\), then \(r^{d-1}/(d+1)\ge r/3\), so the left-to-right ratio of (1) is at least
\[
\frac{r(16-r)}{24}>1\quad(r\in\{7,11,13\}),
\]
a contradiction. Hence \(d=1\).

**5. Finite, proved search region.** With \(d=1\), (1) becomes
\[
(16-r)\frac{2^a}{a+3}\frac{3^{b-1}}{b+1}\frac{5^{c-1}}{c+1}=2.
\]
Every one of the three increasing ratios is at most \(8/(16-r)\le8/3\), as the other two are at least \(1/2\). The strict inequalities \(2^5/8=4>8/3\), \(3^3/5=27/5>8/3\), and \(5^2/4=25/4>8/3\) force
\[
1\le a\le4,\quad1\le b\le3,\quad1\le c\le2.
\]
The resulting **seventy-two** integer triples over the three candidate primes can be checked directly by (1); the only successes, displayed in the order \((r,a,b,c)\), are \((11,2,2,1)\), \((13,2,1,2)\), and \((13,3,2,1)\). They yield respectively \(m=1980,3900,4680\). Directly, the corresponding values of \((\varphi(4m),\tau(4m))\) are \((1920,60)\), \((3840,60)\), and \((4608,72)\), each summing to \(m\). This proves both directions of the classification.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The exact-integer program enumerates **all seventy-two** cases allowed by the proved bounds, independently computes totients and divisor counts from prime factorization, verifies the critical rational comparisons, and performs a supplemental brute-force regression for \(m\le50000\). The recorded output is in `verification_output.txt`. The direct regression is not a proof of the unbounded claim: completeness comes from Steps 1–5 and the seventy-two exact checks.

## Relationship to prior work
Sándor [1, Theorem 6] establishes that any solution has \(m\) even and \(\omega(m)\ge4\). His Theorem 7 determines solutions **provided** \(m=2^a3^b5^cp\) with the final prime to exponent one; its three numbers agree with those above. The present classification proves that **every** solution with \(\omega(m)=4\) must satisfy those previously imposed prime-support and exponent hypotheses. The related earlier paper [2] studies the equation with right-hand side \(n/2\), not the one-fourth equation. The completeness statement does not follow solely from Theorem 6 or the conditional Theorem 7.

## Limitations
The classification is restricted to exactly the minimum possible number of distinct prime factors. It does not classify solutions with five or more distinct prime factors or resolve conjectured infinitude. An independent audit has not been performed, and unindexed equivalent work cannot be ruled out by literature searches alone.

## References
[1] József Sándor, “On certain equations and inequalities involving the arithmetical functions \(\varphi(n)\) and \(d(n)\) – II”, *Notes on Number Theory and Discrete Mathematics* **29**(1), 130–136 (2023). Online First 2023-03-07. DOI: 10.7546/nntdm.2023.29.1.130-136; https://nntdm.net/papers/nntdm-29/NNTDM-29-1-130-136.pdf. See Theorems 6 and 7, pp. 134–136.

[2] József Sándor and Saunak Bhattacharjee, “On certain equations and inequalities involving the arithmetical functions \(\varphi(n)\) and \(d(n)\)”, *Notes on Number Theory and Discrete Mathematics* **28**(2), 376–379 (2022). Online First 2022-06-14. DOI: 10.7546/nntdm.2022.28.2.376-379; https://nntdm.net/papers/nntdm-28/NNTDM-28-2-376-379.pdf.
