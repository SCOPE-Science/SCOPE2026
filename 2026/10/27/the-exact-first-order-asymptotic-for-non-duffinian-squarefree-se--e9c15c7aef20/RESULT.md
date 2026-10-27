# The exact first-order asymptotic for non-Duffinian squarefree semiprimes

## Finding
For every real \(x\ge 1\), let \(E(x)\) be the number of integers \(n\le x\) expressible uniquely as a product \(n=pq\) with distinct primes \(p<q\), for which \(\gcd(n,\sigma(n))>1\), where \(\sigma\) is the ordinary divisor-sum function. Then
\[
 E(x)\sim C\,\frac{x}{\log x},\qquad
 C=\frac12+\sum_{\substack{p\ge3\\p\text{ prime}}}\frac{1}{p(p-1)}.
\]
The prime series converges absolutely. In particular, \(0.773156601<C<0.773157602\). The positive constant gives the exact leading-order frequency of failure of the Duffinian condition among squarefree semiprimes.

## Assumptions and scope
Primes \(p,q\) in the definition are distinct and always ordered \(p<q\). Prime squares are excluded, and no restriction is imposed on the sizes of the individual prime factors beyond their product bound. Throughout, \(x\to\infty\) through real values. An integer \(pq\) is Duffinian exactly when \(\gcd(pq,\sigma(pq))=1\). Classical inputs are the prime number theorem for primes in any fixed reduced residue class and the Brun–Titchmarsh inequality, in its standard upper-bound form for a prime modulus smaller than the counting endpoint.

## Proof
Since \(\sigma(pq)=(p+1)(q+1)\), and \(q>p\), a common prime divisor of \(pq\) and \(\sigma(pq)\) must be \(p\mid q+1\), with the single additional possibility \(p=2\). Indeed \(q\nmid p+1\) because \(p+1<q\) for distinct odd primes \(p<q\); if \(p=2\), then \(2\mid q+1\) for every odd \(q\). Consequently
\[
 E(x)=\#\{q\le x/2:q\text{ an odd prime}\}
 +\sum_{\substack{3\le p<\sqrt x\\p\text{ prime}}}
 \#\{q:p<q\le x/p,\ q\equiv-1\pmod p,\ q\text{ prime}\}.
\]
For odd \(p\ge5\), any prime \(q<p\) in the indicated residue class would equal \(p-1\), an even composite integer. For \(p=3\), the only such excluded prime is \(q=2\). Therefore, letting \(\pi(y;k,a)\) denote the number of primes not exceeding \(y\) in residue class \(a\pmod k\), we have the exact asymptotic decomposition
\[
 E(x)=\pi(x/2)+\sum_{\substack{3\le p\le\sqrt x\\p\text{ prime}}}\pi(x/p;p,-1)+O(1).
\]
(The \(O(1)\) accounts only for excluding \(q=2\), excluding the prime \(2\) from the first term, and inconsequential endpoint conventions.)

For each **fixed odd prime** \(p\), the prime number theorem in arithmetic progressions yields
\[
 \pi(x/p;p,-1)\sim\frac{1}{p-1}\operatorname{Li}(x/p)
 \sim \frac{x}{p(p-1)\log x}.
\]
Also \(\pi(x/2)\sim x/(2\log x)\).

The sum over growing prime moduli can be controlled uniformly. Fix an integer \(Y\ge3\). For primes \(Y<p\le x^{1/4}\), Brun–Titchmarsh gives
\[
 \pi(x/p;p,-1)\le\frac{2x/p}{(p-1)\log(x/p^2)}
 \le\frac{4x}{p(p-1)\log x}
\]
for sufficiently large \(x\). Therefore, the part of the normalized sum in this range is bounded above by \(4\sum_{p>Y}1/[p(p-1)]\), which tends to zero as \(Y\to\infty\).

For \(x^{1/4}<p\le\sqrt x\), a trivial count of all integers (not just primes) congruent to \(-1\pmod p\) up to \(x/p\) gives
\[
 \pi(x/p;p,-1)\le\frac{x}{p^2}+1.
\]
Even if the prime condition on \(p\) is dropped, summation gives
\[
 \sum_{x^{1/4}<p\le\sqrt x}\pi(x/p;p,-1)
 \le x\sum_{m>x^{1/4}}\frac1{m^2}+\sqrt x
 =O(x^{3/4}+\sqrt x)=o(x/\log x).
\]
Thus the normalized limsup of the tail beyond \(Y\) is at most \(4\sum_{p>Y}1/[p(p-1)]\). Since \(Y\) is arbitrary and the fixed-prime terms converge individually, the entire series of normalized contributions tends to \(\sum_{p\ge3}1/[p(p-1)]\). Adding \(p=2\) proves the claimed limit.

## Verification
A standalone Python 3 program `verify.py` independently checks the congruence criterion against \(\gcd(pq,(p+1)(q+1))\) for all squarefree semiprimes not exceeding \(10^6\). The exact exceptional counts are \(145,1059,8170,65886\) at \(x=10^3,10^4,10^5,10^6\), respectively. The checker also sums the constant to one million and bounds the omitted tail above by \(10^{-6}\); it returns `VERIFY_OK`. Enumeration is finite corroboration, not a proof of the limiting asymptotic. The universal proof above uses the prime number theorem in arithmetic progressions and Brun–Titchmarsh.

## Relationship to prior work
The original Duffinian-number literature defines the condition and gives divisibility criteria; Zbiek's 1983 survey restates a general structural criterion and studies elementary qualitative distribution. Pollack's 2011 paper studies the distribution of \(\gcd(n,\sigma(n))\) across all integers and contains Brun–Titchmarsh-based estimates; its statements are not the particular exact semiprime asymptotic above. The existing published result *Almost all squarefree semiprimes are Duffinian* proves the local criterion and the bound \(E(x)=O(x/\log x)\), and explicitly does not claim a leading constant. That bound does not determine the value of \(\lim_{x\to\infty}E(x)\log x/x\). The current result supplies this natural missing constant. OEIS A003624 tabulates Duffinian integers but does not supply this semiprime asymptotic.

## Limitations
The theorem addresses squarefree products of **two distinct primes only**; it does not determine an analogous constant for products of three or more primes, repeated prime powers, or the full set of positive integers. It proves an asymptotic equivalence, not a quantified remainder term beyond \(o(x/\log x)\). Duffy's 1979 original article and Luca's 2007 density article were identified as relevant but their full text could not be verified in this review; a semiprime-specific result therein or in unlocated literature remains an originality risk. The prior 1979 work is year-dated in accessible records, while the earliest located source with an exact calendar-day bibliographic timestamp is the OEIS A003624 entry dated September 19, 1994; the latter date is used in the accompanying metadata and is not represented as the date of Duffy's original research.

## References
1. L. Richard Duffy, *The Duffinian numbers*, Journal of Recreational Mathematics 12 (1979), 112–115 (bibliographic identification; original full text not inspected).
2. Rose Mary Zbiek, *What Can We Say About the Duffinian Numbers?*, The Pentagon 42(2) (Spring 1983), 99–109, https://www.kappamuepsilon.org/Pentagon/Vol_42_Num_2_Spring_1983.pdf (full article inspected).
3. Paul Pollack, *On the Greatest Common Divisor of a Number and Its Sum of Divisors*, Michigan Mathematical Journal 60 (2011), 199–214, https://www.pollack-math.net/combined3.pdf (full article inspected).
4. OEIS Foundation, A003624, *Duffinian numbers*, https://oeis.org/A003624 (sequence and metadata inspected).
5. *Almost all squarefree semiprimes are Duffinian*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-almost-all-squarefree-semiprimes-are-duffinian--15a95ebe2dc2 (full RESULT.md inspected).
6. Florian Luca, *On the densities of some subsets of integers*, Missouri Journal of Mathematical Sciences 19(3) (2007), 167–170, DOI 10.35834/mjms/1316032973 (metadata inspected, full text inaccessible).
