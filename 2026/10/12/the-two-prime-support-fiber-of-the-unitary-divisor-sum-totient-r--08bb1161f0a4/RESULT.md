# The two-prime-support fiber of the unitary divisor sum–totient ratio
## Finding
For every positive integer \(n\) having at most two distinct prime factors,
\[
\sigma^*(n)=2\varphi(n)\quad\Longleftrightarrow\quad n\in\{3,35,99\}.
\]
Furthermore, no even positive integer satisfies the equality, irrespective of its number of prime factors. The support threshold is sharp: \(1045=5\cdot11\cdot19\) satisfies the equality and has three distinct prime factors.

## Assumptions and scope
Here \(d\parallel n\) means \(d\mid n\) and \(\gcd(d,n/d)=1\), and \(\sigma^*(n)=\sum_{d\parallel n}d\). For the canonical factorization \(n=\prod p^a\),
\[
\sigma^*(n)=\prod_{p^a\parallel n}(1+p^a),\qquad
\varphi(n)=\prod_{p^a\parallel n}p^{a-1}(p-1).
\]
The convention is \(\omega(1)=0\), \(\sigma^*(1)=\varphi(1)=1\). All assertions are exact and independent of a numerical search bound.

## Proof
For a prime \(p\) and positive integer \(a\), define the local ratio
\[
R_p(a)=\frac{\sigma^*(p^a)}{\varphi(p^a)}
=\frac p{p-1}(1+p^{-a}).
\]
It is strictly decreasing with \(a\), always exceeds \(p/(p-1)\), and obeys
\[
R_p(a)\le R_p(1)=\frac{p+1}{p-1}.
\]
Products of these local ratios give \(\sigma^*(n)/\varphi(n)\). Since \(R_2(a)>2\) for every \(a\ge1\) and every other local ratio exceeds \(1\), every even integer fails. The integer \(1\) fails because its ratio is \(1\).

For an odd prime power, the equality becomes
\[
p^a+1=2p^{a-1}(p-1),\qquad
p^{a-1}(p-2)=1.
\]
Thus \(p=3\) and \(a=1\), giving \(n=3\).

Now let \(n=p^a q^b\), where \(3\le p<q\) are odd primes and \(a,b\ge1\). If \(p\ge5\), then \(q\ge7\), and
\[
R_p(a)R_q(b)\le\frac{6}{4}\frac{8}{6}=2.
\]
Strict decrease in both primes and both exponents makes equality possible only for \((p,q,a,b)=(5,7,1,1)\), giving \(35\).

Suppose \(p=3\). If \(a=1\), then \(R_3(1)=2\) and \(R_q(b)>1\), so equality is impossible. Assume \(a\ge2\). If \(q\ge11\), monotonicity gives
\[
R_3(a)R_q(b)\le R_3(2)R_{11}(1)=\frac53\frac65=2.
\]
Equality holds only for \((a,q,b)=(2,11,1)\), giving \(99\).

For \(q=7\), if \(b=1\), then
\[
R_3(a)R_7(1)>\frac32\frac43=2.
\]
If \(b\ge2\), then
\[
R_3(a)R_7(b)\le\frac53\frac{25}{21}=\frac{125}{63}<2.
\]
Thus \(q=7\) yields no solutions.

For \(q=5\), if \(b=1\), the product exceeds \((3/2)(3/2)>2\). If \(b\ge2\), multiply out the defining equality:
\[
(3^a+1)(5^b+1)=16\cdot3^{a-1}5^{b-1}.
\]
Modulo \(5\), this forces \(3^a\equiv-1\pmod5\), hence \(a\equiv2\pmod4\). If \(a=2\), then
\[
R_3(2)R_5(b)>\frac53\frac54=\frac{25}{12}>2.
\]
Otherwise \(a\ge6\), and
\[
R_3(a)R_5(b)\le R_3(6)R_5(2)
=\frac{949}{486}<2.
\]
This exhausts all two-prime cases. Finally, direct multiplication gives \(\sigma^*(3)=4=2\varphi(3)\), \(\sigma^*(35)=48=2\varphi(35)\), and \(\sigma^*(99)=120=2\varphi(99)\). At \(1045=5\cdot11\cdot19\),
\[
\sigma^*(1045)=6\cdot12\cdot20=1440
=2(4\cdot10\cdot18)=2\varphi(1045).
\]
All boundary equalities and inequalities are therefore exact.

## Verification
Run \(\texttt{python3 verify.py}\) in the extracted package. The standard-library-only program uses a smallest-prime-factor sieve and computes \(\varphi\), \(\sigma^*\), and \(\omega\) from independent integer factorizations for every \(1\le n\le10^6\). It checks all \(367461\) integers in that range with at most two prime supports; their exact equality hits are \(3,35,99\). It also independently evaluates the three-prime boundary example \(1045\). This exhaustive finite range check is corroboration, not the proof of the unrestricted theorem.

## Relationship to prior work
OEIS A034448 defines the unitary sum \(\sigma^*\), while OEIS A062699 lists the distinct, ordinary divisor-sum equation \(\sigma(n)=2\varphi(n)\). Broughan and Delbourgo (2013, Theorem 11) determine its solutions with at most three prime supports as \(3,35,1045\); Broughan and Zhou (2014) continue the ordinary divisor-sum/totient divisibility classification. These sources agree for squarefree inputs because \(\sigma^*(n)=\sigma(n)\) there, but do not imply the present statement for nonsquarefree integers: \(99\) is a unitary solution whereas \(\sigma(99)\ne2\varphi(99)\). Trudgian (first available arXiv version in 2013) proves global upper bounds for the unitary sum and studies its comparison with the exponential divisor sum, not this exact totient fiber.

## Limitations
This theorem classifies only the \(\omega(n)\le2\) fiber and excludes even solutions at every support size. It does not classify odd solutions with three or more prime factors, establish their finiteness, or assert that the sequence \(3,35,99,1045,\ldots\) is exhaustive beyond the stated support restriction. The available comparison search cannot rule out unindexed equivalent work; independent external review has not been performed.

## References
1. OEIS A034448, *Sum of unitary divisors*, https://oeis.org/A034448.
2. OEIS A062699, *Numbers \(n\) with \(\sigma(n)=2\varphi(n)\)*, original entry dated July 11, 2001, https://oeis.org/A062699.
3. K. A. Broughan and D. Delbourgo, *On the Ratio of the Sum of Divisors and Euler's Totient Function I*, Journal of Integer Sequences 16 (2013), Article 13.8.8, https://cs.uwaterloo.ca/journals/JIS/VOL16/Broughan/broughan26.pdf.
4. K. A. Broughan and Q. Zhou, *On the Ratio of the Sum of Divisors and Euler's Totient Function II*, Journal of Integer Sequences 17 (2014), Article 14.9.2, https://cs.uwaterloo.ca/journals/JIS/VOL17/Broughan/bro32.pdf.
5. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, version 1 submitted December 17, 2013, https://arxiv.org/abs/1312.4615.
