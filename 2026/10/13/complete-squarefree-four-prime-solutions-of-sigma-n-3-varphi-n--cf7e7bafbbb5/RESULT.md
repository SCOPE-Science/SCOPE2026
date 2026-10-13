# Complete squarefree four-prime solutions of \(\sigma(n)=3\varphi(n)\)
## Finding
The squarefree integers \(n\) with exactly four distinct prime divisors satisfying
\[
\sigma(n)=3\varphi(n)
\]
are exactly
\[
\boxed{n\in\{10659,12441,24969\}}.
\]
In fact,
\[
10659=3\cdot11\cdot17\cdot19,\quad
12441=3\cdot11\cdot13\cdot29,\quad
24969=3\cdot7\cdot29\cdot41.
\]

## Assumptions and scope
Here \(\sigma\) is the ordinary sum-of-divisors function, \(\varphi\) Euler's totient, and squarefree means that every prime has exponent one. If \(n=pqrs\), for primes \(p<q<r<s\), multiplicativity gives
\[
\frac{\sigma(n)}{\varphi(n)}
=\frac{p+1}{p-1}\frac{q+1}{q-1}\frac{r+1}{r-1}\frac{s+1}{s-1}.
\tag{1}
\]
The theorem concerns exactly the squarefree four-prime layer; no claim is made about higher support or repeated prime factors.

## Proof
Set \(R(t)=(t+1)/(t-1)\) for \(t>1\). This positive function decreases strictly and satisfies \(R(t)>1\). Suppose the ratio in (1) equals \(3\).

If \(p=2\), the product exceeds \(R(2)=3\). If \(p\ge5\), monotonicity and distinctness of the primes give
\[
R(p)R(q)R(r)R(s)\le R(5)R(7)R(11)R(13)=\frac{14}{5}<3.
\]
Therefore \(p=3\), and
\[
R(q)R(r)R(s)=\frac32.\tag{2}
\]
If \(q=5\), its factor already equals \(3/2\), making the product too large. If \(q\ge13\), the next primes are at least \(17,19\), so
\[
R(q)R(r)R(s)\le R(13)R(17)R(19)=\frac{35}{24}<\frac32.
\]
Thus \(q\in\{7,11\}\).

For \(q=7\), equation (2) gives \(R(r)R(s)=9/8\). Cross multiplication yields
\[
(r-17)(s-17)=288.\tag{3}
\]
If \(r<17\), then \(7<r<s<17\), and consequently
\[
0<(17-r)(17-s)\le6\cdot4=24<288.
\]
The case \(r=17\) is also impossible. Hence \(17<r<s\). With \(d=r-17\), we have \(d\mid288\) and \(d^2<288\), so
\[
d\in\{1,2,3,4,6,8,9,12,16\}.
\]
Primality of \(r=17+d\) reduces this to \(d\in\{2,6,12\}\), giving \((r,s)=(19,161),(23,65),(29,41)\). Only the last pair consists of primes. Hence \(n=24969\).

For \(q=11\), equation (2) gives \(R(r)R(s)=5/4\), equivalently
\[
(r-9)(s-9)=80.\tag{4}
\]
Here \(r>11\), and with \(d=r-9>0\), the inequalities \(d\mid80\), \(d^2<80\) give
\[
d\in\{1,2,4,5,8\}.
\]
The requirement that \(r=9+d>11\) be prime leaves \(d=4,8\); the corresponding prime pairs are \((r,s)=(13,29),(17,19)\). These produce \(n=12441\) and \(n=10659\).

Conversely, direct substitution in (1) verifies that all three displayed integers have \(\sigma(n)=3\varphi(n)\). The exhaustive prime-support and divisor arguments prove the classification for arbitrarily large \(n\).

## Verification
The accompanying `verify.py` checks, using exact arithmetic, all squarefree \(n\) with four distinct prime factors through \(1{,}000{,}000\), independently verifies the complete divisor branches (3) and (4), and verifies the three witnesses. The finite check only corroborates the unrestricted proof.

## Relationship to prior work
OEIS A068391 defines exactly \(\sigma(n)=3\varphi(n)\) and tabulates the three witness integers, but the finite table does not prove that other four-prime squarefree solutions cannot occur. The earlier OEIS A061367 studies the broader divisibility \(\sigma(n)-\varphi(n)\mid\sigma(n)+\varphi(n)\), of which this ratio-three equation is a special case.

Broughan and Delbourgo (2013) study integer ratios of the divisor sum and totient, principally ratio two, with finite-support bounds. The full 2014 paper by Broughan and Zhou gives an exact classification when there are at most three distinct prime factors; its Lemma 12 treats the ratio-three equation in the three-prime layer. That result does not classify squarefree integers with four distinct primes. Searches for the exact equation, its ratio-class alias, the three witnesses, and four-prime support found no published theorem that establishes the present unbounded uniqueness statement.

## Limitations
The witness values themselves were already recorded. The new assertion is that they exhaust the entire squarefree four-distinct-prime layer. An equivalent elementary proof might occur in an unindexed discussion. No assertion is made about nonsquarefree solutions or five-or-more-prime support.

## References
1. OEIS Foundation, A061367, original entry 13 February 2002.
2. OEIS Foundation, A068391, original entry 3 March 2002.
3. K. A. Broughan and D. Delbourgo, “On the Ratio of the Sum of Divisors and Euler's Totient Function I,” *Journal of Integer Sequences* 16 (2013), Article 13.8.8.
4. K. A. Broughan and Q. Zhou, “On the Ratio of the Sum of Divisors and Euler's Totient Function II,” *Journal of Integer Sequences* 17 (2014), Article 14.9.2.
