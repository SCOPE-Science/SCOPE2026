# A complete two-prime classification for divisor-gap closure

## Finding
For \(n>1\), arrange all its positive divisors as \(1=d_1<d_2<\cdots<d_{\tau(n)}=n\). Say that \(n\) has **divisor-gap closure** if \(d_{i+1}-d_i\mid n\) for every \(1\le i<\tau(n)\). Among integers with exactly two distinct prime divisors, the condition holds **exactly** for
\[
 n=2^a3^b\quad(a,b\ge1,\ a\le4\text{ or }b\le2),
\]
and
\[
 n=2^a p^b\quad(a,b\ge1,\ p\ge5\text{ prime},\ p=2^a+1).
\]
The second branch consists of Fermat-prime bases, because primality of \(2^a+1\) forces \(a\) to be a power of two. In particular, both branches contain infinite families (varying \(b\) in the first branch and in any fixed prime from the second). The exceptions \(a\ge5,b\ge3,p=3\) fail sharply already at \(a=5,b=3\).

## Assumptions and scope
All numbers are positive integers, primes are rational primes, and divisors include \(1\) and \(n\). The theorem assumes exactly two **distinct** prime divisors, with exponents unbounded. It makes no assertion about the complete class of integers having more than two distinct prime divisors. The condition concerns differences of adjacent divisors in **numerical order**, not differences across arbitrary divisor pairs.

## Proof
**Step 1: force the prime support and restrict the odd prime.** If \(n\) is odd and composite, its two smallest positive divisors are \(1\) and its least prime divisor \(q\ge3\). Their gap \(q-1\) is even and cannot divide odd \(n\). Thus any qualifying integer with two distinct prime factors must have form \(2^a p^b\) with \(a,b\ge1\) and \(p\) an odd prime. Let \(k\ge1\) be the unique integer with \(2^k<p<2^{k+1}\).

If \(a\le k\), the divisors \(2^a\) and \(p\) are consecutive: all other pure powers of two are smaller, and every divisor containing \(p\) is at least \(p\). Their gap is a positive odd number smaller than \(p\), and the only positive odd divisor of \(2^a p^b\) smaller than \(p\) is \(1\). Hence \(p-2^a=1\), forcing \(p=2^a+1\) (and necessarily \(a=k\)).

If \(a\ge k+1\), both \(2^k,p\) and \(p,2^{k+1}\) are consecutive divisor pairs: \(2p>2^{k+1}\), and all other divisors are outside these intervals. The odd gaps \(p-2^k\) and \(2^{k+1}-p\), both positive and less than \(p\), must therefore equal \(1\). Thus \(2^k+1=2^{k+1}-1\), giving \(k=1,p=3\). These cases exhaust all possibilities. If \(p=2^a+1\ge5\) is prime, writing \(a=2^t m\) with \(m>1\) odd would factor \(2^a+1\) as \(x^m+1\), divisible by \(x+1\) for \(x=2^{2^t}\); hence \(a\) is a power of two.

**Step 2: the separated-layer branch.** Suppose \(p=2^a+1\) is prime. The divisors fall into strictly ordered blocks
\[
 p^j,\ 2p^j,\ 4p^j,\ldots,\ 2^a p^j\qquad(0\le j\le b),
\]
because \(2^a p^j < p^{j+1}\). Inside one block, every adjacent gap equals \(2^i p^j\) with \(0\le i<a\), and the gap from the last entry of block \(j\) to the first of block \(j+1\) equals \(p^j(p-2^a)=p^j\). All are divisors of \(n\).

**Step 3: the unbounded-\(b\) branch at \(p=3\) with \(a\le4\).** For fixed \(1\le a\le4\), write \(D_{a,b}=\{2^i3^j:0\le i\le a,0\le j\le b\}\). At \(b=1\), the complete ascending divisor rows are
\[
\begin{array}{c|l}
a& D_{a,1}\\\hline
1&1,2,3,6\\
2&1,2,3,4,6,12\\
3&1,2,3,4,6,8,12,24\\
4&1,2,3,4,6,8,12,16,24,48
\end{array}
\]
and direct subtraction shows that every gap divides \(2^a3\).

For \(b\ge2\), the divisors below \(3^b\) already occurred at level \(b-1\); their consecutive gaps are valid by induction. The divisor immediately preceding \(3^b\) is \(2\cdot3^{b-1}\) for \(a=1,2\), and \(8\cdot3^{b-2}\) for \(a=3,4\); the bridging gaps are \(3^{b-1}\) and \(3^{b-2}\), respectively. Since \(2^a\le16<27\), all divisors from \(3^b\) upward equal \(3^{b-2}\) times the fixed row
\[
E_a=\{2^i3^j\ge9:0\le i\le a,\ 0\le j\le2\},
\]
whose successive differences are, respectively,
\[
\begin{array}{c|l}
a&\operatorname{diff}(E_a)\\\hline
1&9\\
2&3,6,18\\
3&3,6,6,12,36\\
4&3,4,2,6,12,12,24,72
\end{array}
\]
Each row difference divides \(2^a\cdot9\). After multiplying by \(3^{b-2}\), all new suffix gaps divide \(2^a3^b\). This proves sufficiency for every \(b\ge1\) when \(a\le4\).

**Step 4: the unbounded-\(a\) branch at \(p=3\) with \(b\le2\).** At \(b=1\), the ascending divisor list is \(1\), followed, for \(h=1,2,\ldots,a\), by the shell \((2^h,3\cdot2^{h-1})\), and finally \(3\cdot2^a\). Within a shell the gap is \(2^{h-1}\); the gap to the next shell is also \(2^{h-1}\), and the final gap is \(3\cdot2^{a-1}\). All divide \(2^a3\).

For \(b=2\) and \(a\ge3\), the initial divisors below \(8\) are \(1,2,3,4,6\); for every \(3\le h\le a\), the divisors in the dyadic shell \([2^h,2^{h+1})\) are exactly
\[
 2^h,\quad9\cdot2^{h-3},\quad3\cdot2^{h-1}.
\]
Within each shell, the gaps are \(2^{h-3}\) and \(3\cdot2^{h-3}\); when \(h<a\), the gap to the next shell is \(2^{h-1}\). After the final shell, the remaining divisors are
\[
9\cdot2^{a-2},\quad3\cdot2^a,\quad9\cdot2^{a-1},\quad9\cdot2^a,
\]
and the connecting and final gaps are \(3\cdot2^{a-2},3\cdot2^{a-2},3\cdot2^{a-1},9\cdot2^{a-1}\). Every listed gap divides \(9\cdot2^a\). The cases \(a=1,2\) follow from Step 3. This proves sufficiency for all \(b\le2\).

**Step 5: exclude the remaining ternary-exponent quadrant.** If \(p=3,a\ge5,b\ge3\), then \(27=3^3\) and \(32=2^5\) are consecutive divisors: there is no \(2^i3^j\) strictly between \(27\) and \(32\). Their difference is \(5\), which cannot divide \(2^a3^b\). Thus no such integer qualifies. Together, Steps 1–5 prove the claimed if-and-only-if classification.

## Verification
The independent-of-proof finite test in `verify.py` constructs divisor lists directly from their prime-power exponents, checks all adjacent gaps against the defining divisibility condition, and compares against the classification across \(11{,}323\) distinct parameter cases. It separately tests long exponent boundaries, known Fermat-prime bases, and the first forbidden adjacent pair. Run `python3 verify.py` with a standard Python 3 installation. These finite checks corroborate but do not replace Steps 1–5, which prove the theorem for all parameters.

## Relationship to prior work
OEIS A060765 records this divisor-gap closure property, including the elementary subfamilies \(2\cdot3^b\) and \(3\cdot2^a\); OEIS A060763 counts the failures and gives an equivalent zero-test. The theorem here determines **every** member with exactly two distinct prime factors and isolates the sharp \(a=4\) and \(b=2\) boundaries. Balog, Erdős and Tenenbaum's 1990 chapter analyzes reciprocal sums and distributional questions for consecutive-divisor gaps, not this exact two-prime classification. The connection is methodological only: its general quantitative gap results do not imply this structural list.

## Limitations
No classification is asserted for integers with at least three distinct prime factors. The complete two-prime classification does not assert infinitude of Fermat primes; the power \(b\) varies to give infinitely many examples for any fixed allowed odd prime. The proof does not establish global publication priority. Closely related but unlocated material on divisor-gap closure may contain an equivalent classification, despite inspection of the cited archival sequence records and relevant full text.

## References
1. Elemer Labos, OEIS A060765, 'Numbers n such that every difference between consecutive divisors ... is also a divisor', dated 24 April 2001, https://oeis.org/A060765.
2. Elemer Labos, OEIS A060763, 'Number of distinct differences between consecutive divisors ... not also divisors', dated 24 April 2001, https://oeis.org/A060763.
3. A. Balog, P. Erdős and G. Tenenbaum, 'On Arithmetic Functions Involving Consecutive Divisors', in *Analytic Number Theory*, Progress in Mathematics 85 (1990), 77–90, https://tenenb.perso.math.cnrs.fr/PPP/Arith%2Bconsec-div.pdf, doi:10.1007/978-1-4612-3464-7_6.
