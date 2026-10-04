# A power-of-two exponent obstruction for bi-unitary harmonic numbers
## Finding
For distinct primes \(p,q\) and every integer \(t\ge 1\), the integer \(p^3q^{2^{t+1}}\) is not bi-unitary harmonic.

## Assumptions and scope
For a positive integer \(n\), let \(\sigma^{**}(n)\) and \(\tau^{**}(n)\) denote the sum and number of bi-unitary divisors. The integer \(n\) is bi-unitary harmonic when
\[
\sigma^{**}(n)\mid n\tau^{**}(n).
\]
For a prime power \(r^a\), the standard formulas are
\[
\sigma^{**}(r^a)=\sigma(r^a)\quad(a\text{ odd}),\qquad
\sigma^{**}(r^{2m})=\sigma(r^{2m})-r^m,
\]
and
\[
\tau^{**}(r^a)=a+1\quad(a\text{ odd}),\qquad
\tau^{**}(r^{2m})=2m.
\]
The finding concerns exactly the two-prime family \(n=p^3q^{2^{t+1}}\) with \(p\ne q\) and \(t\ge1\).

## Proof
Put \(b=2^t\), so \(b\ge2\) is even and \(n=p^3q^{2b}\). Define
\[
A=(p+1)(p^2+1),\qquad B=\sum_{j=0}^{2b}q^j-q^b.
\]
The prime-power formulas give
\[
\sigma^{**}(n)=AB,\qquad \tau^{**}(n)=8b.
\]
Thus bi-unitary harmonicity would imply
\[
AB\mid 8bp^3q^{2b}. \tag{1}
\]
Because \(b\) is a power of two, the right-hand side of (1) has prime support contained in \(\{2,p,q\}\).

First, \(\gcd(A,p)=1\), so every odd prime divisor of \(A\) must be \(q\). If \(p=2\), then \(A=15\) has the two distinct odd prime divisors \(3\) and \(5\), impossible. Hence \(p\) is odd. Then \(v_2(p^2+1)=1\) and
\[
\gcd(p+1,p^2+1)=2.
\]
Since \(p^2+1>2\), its odd prime divisors are all \(q\), while no odd divisor can be shared with \(p+1\). Therefore there are integers \(u,v\ge1\) such that
\[
p+1=2^u,\qquad p^2+1=2q^v. \tag{2}
\]
In particular \(q\) is odd. From \(p^2\equiv-1\pmod q\), the residue class of \(p\) has order \(4\) modulo \(q\), hence
\[
q\equiv1\pmod4. \tag{3}
\]

Next, \(B\equiv1\pmod q\), so \(\gcd(B,q)=1\). By (1), every odd prime divisor of \(B\) must therefore be \(p\). Since \(b\) is even, substituting \(q\equiv-1\pmod{q+1}\) yields
\[
B\equiv\sum_{j=0}^{2b}(-1)^j-(-1)^b=1-1=0\pmod{q+1}.
\]
Thus \(q+1\mid B\). By (3), \(v_2(q+1)=1\), so for some integer \(s\ge1\),
\[
q+1=2p^s. \tag{4}
\]

Equations (2) and (4) force \(p,q\) completely. From (2),
\[
q^v=\frac{p^2+1}{2}<p^2.
\]
If \(s\ge2\), then (4) gives \(q=2p^s-1>p^2\), a contradiction. Hence \(s=1\) and \(q=2p-1\). If \(v\ge2\), then
\[
q^2=(2p-1)^2>\frac{p^2+1}{2},
\]
again contradicting (2). Therefore \(v=1\), and
\[
p^2+1=2q=4p-2,
\]
so \((p-1)(p-3)=0\). Since \(p\) is prime, \(p=3\) and then \(q=5\).

For this forced pair, \(\gcd(B,5)=1\), so (1) requires
\[
B\mid 8b\cdot3^3=216b. \tag{5}
\]
But \(B>5^{2b}=25^b\). At \(b=2\), \(25^b=625>432=216b\), and \(25^b/b\) is strictly increasing for \(b\ge2\). Hence \(B>216b\), contradicting (5). The assumed bi-unitary harmonic number cannot exist.

## Verification
The proof uses only exact divisibility, prime support, and congruence arguments. The accompanying `verify.py` independently implements \(\sigma^{**}\) and \(\tau^{**}\), checks the displayed formulas, exhaustively finds no counterexample for distinct primes below \(2000\) and \(1\le t\le5\), and checks the terminal size inequality for \(1\le t\le11\). Running

`python3 verify.py`

prints `VERIFY_OK`. These finite computations are supplementary checks; the infinite statement is established by the proof above.

## Relationship to prior work
Sándor's 2011 paper introduces bi-unitary harmonic numbers, proves that no number of the form \(p^3q^2\) is bi-unitary harmonic, and remarks that the same holds for \(p^3q^4\). Manea and Minculete's 2016 paper repeats those exclusions while studying other fixed factorization patterns. The present argument gives a single infinite obstruction
\[
p^3q^{2^{t+1}}\quad(t\ge1),
\]
whose first case is the previously stated \(p^3q^4\) exclusion and whose higher cases are not implied by the cited fixed-exponent statements. The new mechanism is the combination of prime-support forcing with the divisibility \(q+1\mid\sigma^{**}(q^{2b})\) when \(b\) is even.

## Limitations
The theorem is restricted to the exponent sequence \(2^{t+1}\) on the second prime. It does not classify all bi-unitary harmonic numbers with two prime factors, nor all numbers of the form \(p^3q^{2b}\) for arbitrary \(b\). Literature searches cannot rule out unindexed or inaccessible prior statements; the originality assessment is relative to the inspected primary sources, current published-finding corpus records, OEIS, and targeted web searches.

## References
1. J. Sándor, "On bi-unitary harmonic numbers," arXiv:1105.0294v1, 2 May 2011. https://arxiv.org/abs/1105.0294
2. A. Manea and N. Minculete, "Types of integer harmonic numbers (II)," Bulletin of the Transilvania University of Brașov, Series III, 9(58), no. 1, 2016, 67–82. https://webbut.unitbv.ro/index.php/Series_III/article/download/1820/1566/3270
3. OEIS A286325, "Bi-unitary harmonic numbers." https://oeis.org/A286325
