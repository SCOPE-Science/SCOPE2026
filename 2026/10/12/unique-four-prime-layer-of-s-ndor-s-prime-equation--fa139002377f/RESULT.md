# Unique four-prime layer of Sándor's prime equation
## Finding
Let \(p<q<r<s\) be distinct odd primes. Then
\[
pqrs-2(p-1)(q-1)(r-1)(s-1)=5
\]
holds if and only if
\[
(p,q,r,s)=(3,5,17,251).
\]
This is exactly the \(r=4\) layer of the prime equation posed by Sándor after reducing \(\varphi(4m)+d(4m)=m\) on the family \(m=2^r p_1\cdots p_r\). Hence within \(m=2^4pqrs\) the unique solution is
\[
m=2^4\cdot3\cdot5\cdot17\cdot251=1024080.
\]

## Assumptions and scope
The variables \(p,q,r,s\) are distinct odd primes in increasing order. The result classifies only the fixed four-prime layer of Sándor's broader prime equation; it does not settle the conjectured infinitude as the number of odd prime factors varies.

## Proof
Divide the equation by \(pqrs\). It gives
\[
2\left(1-\frac1p\right)\left(1-\frac1q\right)\left(1-\frac1r\right)\left(1-\frac1s\right)
=1-\frac5{pqrs}<1.
\]
If \(p\ge5\), then \(q\ge7\), \(r\ge11\), and \(s\ge13\), so the left side is at least
\[
2\cdot\frac45\cdot\frac67\cdot\frac{10}{11}\cdot\frac{12}{13}
=\frac{5760}{5005}>1,
\]
a contradiction. Thus \(p=3\).

With \(p=3\), if \(q\ge11\), then \(r,s>q\), and therefore the left side is greater than
\[
\frac43\left(\frac{10}{11}\right)^3=\frac{4000}{3993}>1.
\]
Hence \(q\in\{5,7}\}\).

For \(q=7\), direct expansion gives
\[
3(r-8)(s-8)=163,
\]
which is impossible modulo \(3\).

For \(q=5\), direct expansion gives
\[
(r-16)(s-16)=235=5\cdot47.
\]
If both factors were negative, then \(5<r<s<16\), hence \(|r-16|\le9\) and \(|s-16|\le5\), so their product would be at most \(45\), not \(235\). Thus both factors are positive. The positive factor pairs of \(235\) are \((1,235)\) and \((5,47)\). They yield \((r,s)=(17,251)\) and \((21,63)\), respectively; only the first pair is prime. Finally,
\[
3\cdot5\cdot17\cdot251-2(2)(4)(16)(250)=5,
\]
so the surviving quadruple indeed works.

## Verification
The accompanying `verify.py` checks the two exact rational inequalities, the modular obstruction, the factor-pair classification, and the final identity. It also performs a regression scan over the first three primes below \(500\) using the exact solved-for-\(s\) formula. The scan is not used as an infinite proof; the preceding reductions are.

## Relationship to prior work
Sándor's 2023 paper studies \(\varphi(n)+d(n)=n/4\), reduces a squarefree odd-prime family to
\[
p_1\cdots p_r-2\prod_{i=1}^r(p_i-1)=r+1,
\]
and conjectures infinitely many prime solutions as \(r\) varies. In the \(r=4\) discussion it fixes \(p_1=3\), \(p_2=5\), derives \((p_3-16)(p_4-16)=235\), and exhibits \((17,251)\); it does not prove that every four-prime solution must begin with \((3,5)\). The argument above supplies that missing global reduction and therefore closes the entire four-prime layer. The 2022 predecessor concerns the different equation \(\varphi(n)+d(n)=n/2\) and does not imply this classification.

## Limitations
This theorem is a fixed-support classification. It gives no infinitude result for the variable-\(r\) conjecture and no classification for \(r\ge5\). The literature search did not reveal another statement of the four-prime uniqueness theorem; absence from the checked sources is not a proof that no equivalent observation exists elsewhere.

## References
1. J. Sándor, "On certain equations and inequalities involving the arithmetical functions \(\varphi(n)\) and \(d(n)\) – II," Notes on Number Theory and Discrete Mathematics 29 (2023), 130–136. DOI: 10.7546/nntdm.2023.29.1.130-136. Online First: 2023-03-07.
2. J. Sándor and S. Bhattacharjee, "On certain equations and inequalities involving the arithmetical functions \(\varphi(n)\) and \(d(n)\)," Notes on Number Theory and Discrete Mathematics 28 (2022), 376–379. DOI: 10.7546/nntdm.2022.28.2.376-379.
