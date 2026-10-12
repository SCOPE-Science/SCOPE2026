# Complete \(2^a p\) classification of the divisor-sum/totient congruence
## Finding
For every integer \(a\ge1\) and odd prime \(p\), let
\[
n=2^a p.
\]
Then
\[
\varphi(n)\mid\sigma(n)-n
\tag{1}
\]
if and only if
\[
(a,p)\in\{(1,3),(2,3)\}
\quad\text{or}\quad
p=3\cdot2^a-1.
\tag{2}
\]

Whenever \(p=3\cdot2^a-1\) is prime, one has the exact equality
\[
\sigma(n)-n=2\varphi(n).
\tag{3}
\]
The exceptional pairs \((a,p)=(1,3)\) and \((2,3)\) give respectively
\[
\frac{\sigma(n)-n}{\varphi(n)}=3\quad\text{and}\quad4.
\]

Thus for every \(a\ge3\), the congruence holds **exactly** when \(3\cdot2^a-1\) is prime and that prime is the odd cofactor. Examples with \(a\ge3\) are \(n=184,752,12224,49024,12580864\), corresponding to \(a=3,4,6,7,11\).

## Assumptions and scope
The arithmetic functions are the ordinary divisor sum \(\sigma(n)=\sum_{d\mid n}d\) and Euler's totient \(\varphi(n)\). Congruence (1) is the defining predicate for OEIS A066679. The theorem concerns precisely the two-prime-support ray \(n=2^a p\), with the odd prime occurring to exponent one. It neither classifies arbitrary \(2^a p^b\) with \(b\ge2\) nor asserts infinitely many primes of the form \(3\cdot2^a-1\).

## Proof
Put
\[
x=2^{a-1},\qquad n=2xp.
\]
Multiplicativity gives
\[
\sigma(n)=(4x-1)(p+1),\qquad
\varphi(n)=x(p-1).
\]
Subtracting \(n=2xp\) yields the exact identity
\[
\sigma(n)-n=(2x-1)(p-1)+(6x-2).
\tag{4}
\]
Consequently, (1) is equivalent to
\[
x(p-1)\mid (2x-1)(p-1)+(6x-2).
\tag{5}
\]

Divisibility in (5) first forces
\[
p-1\mid6x-2.
\]
Write the positive integer
\[
t=\frac{6x-2}{p-1}.
\]
Dividing (5) by \(p-1\) shows that the remaining necessary and sufficient condition is
\[
x\mid (2x-1)+t,
\quad\text{equivalently}\quad
t\equiv1\pmod x.
\tag{6}
\]
Conversely, any odd prime \(p\) for which \(t\) is a positive integer and (6) holds satisfies (5).

If \(a=1\), then \(x=1\) and \(6x-2=4\). Since \(p-1\ge2\) is even, \(p-1\) is \(2\) or \(4\), giving \(p=3\) or \(p=5\). These produce, respectively, \(n=6\) and \(n=10\); \(p=5=3\cdot2^1-1\) belongs to the parametric branch.

If \(a\ge2\), then \(x\) is even, \(6x-2=2(3x-1)\) has exactly one factor of \(2\), and \(p-1\) is even. Therefore \(t\) is a **positive odd divisor** of \(3x-1\). In addition, \(t\le 3x-1\), and (6) requires
\[
t\in\{1,x+1,2x+1\}.
\tag{7}
\]
For \(x=2\), the allowable divisors of \(3x-1=5\) are \(t=1\) and \(t=5\). They give \(p=11\) and \(p=3\), respectively; the latter is the exceptional pair \((2,3)\).

For \(a\ge3\), one has \(x\ge4\). If \(t=x+1\) divided \(3x-1\), it would divide
\[
(3x-1)-3(x+1)=-4,
\]
contradicting \(x+1\ge5\). If \(t=2x+1\) divided \(3x-1\), it would divide
\[
2(3x-1)-3(2x+1)=-5,
\]
contradicting \(2x+1\ge9\). Thus (7) forces \(t=1\), or equivalently
\[
p-1=6x-2,
\qquad p=6x-1=3\cdot2^a-1.
\]
The same equation describes the parametric case \(t=1\) for \(a=1,2\). Inserting \(t=1\) into (4) gives
\[
\frac{\sigma(n)-n}{\varphi(n)}
=\frac{2x-1+t}{x}=2.
\]
The other pairs give \(3\) and \(4\), as stated. This proves necessity, sufficiency, and all boundary cases.

## Verification
The attached `verify.py` checks all odd primes \(3\le p<100000\) independently for each exponent \(1\le a\le24\). It computes \(\sigma(2^a p)\), \(\varphi(2^a p)\), and the congruence using exact integers, and compares every hit to (2), including the quotient values. It also enumerates every possible \(t\) in (7) for each \(2\le a\le40\), verifying the divisor elimination. These finite calculations are corroborative; the proof is valid for every exponent and prime.

## Relationship to prior work
OEIS A066679 defines the same congruence, with an original author date of 11 January 2002. A 15 April 2006 comment records **sufficiency** of the family \(p=3\cdot2^a-1\), together with the exact multiplier \(2\), but does not state its **necessity** within all \(2^a p\) or identify the complete exceptions. The present theorem supplies the missing converse and simultaneously bounds the possible quotient to \(2,3,4\) on this ray.

D. E. Iannucci's paper on the equation \(\sigma(n)=n+\varphi(n)\) cites A066679 and studies the multiplier \(1\), rather than all integer multipliers. It establishes structural obstructions for that equality and does not imply the prime-cofactor classification at multipliers \(2,3,4\).

Cheng Linfeng's related paper concerns \(\sigma(n)\equiv0\pmod n\) and \(n\sigma(n)\equiv2\pmod{\varphi(n)}\), which are logically different modular predicates. Exact-form and alias searches found no stronger classification that subsumes (2).

## Limitations
The source already gives the nonexceptional **sufficient** construction, and elementary computations already exhibit the four lowest-multiplicity instances. The new content is the universal **only-if** direction for every \(a\ge3\), including arbitrarily large exponents. Whether there are infinitely many primes \(3\cdot2^a-1\) remains open. No assertion is made about composite odd cofactors or higher odd-prime exponents.

## References
1. OEIS Foundation, A066679, “Numbers \(n\) such that \(\sigma(n)\) is congruent to \(n\) modulo \(\varphi(n)\),” initial entry by J. L. Pe, 11 January 2002; construction comment by F. Firoozbakht, 15 April 2006.
2. D. E. Iannucci, “On the Equation \(\sigma(n)=n+\varphi(n)\),” *Journal of Integer Sequences* 20 (2017), Article 17.6.2.
3. Cheng Linfeng, “On \(\sigma(n)\equiv0\pmod n\), \(n\sigma(n)\equiv2\pmod{\varphi(n)}\) and \(\varphi(N)\mid N-1\),” *International Journal of Algebra* 3 (2009), 613–617.
