# A finite divisor sieve for three-prime positive-shift Carmichael equations

## Finding

Let \(\lambda(n)\) be the exponent of the multiplicative group of units modulo \(n\). For any three odd primes \(p<q<r\), the divisibility
\[
\lambda(pqr)\mid pqr+1
\]
holds precisely when there is an integer \(d\) in \(1\le d<p\) such that
\[
\begin{aligned}
d&\mid pq+1,\\
q-1&\mid(p+1)(p+d),\\
r&=1+\frac{pq+1}{d}>q\text{ is prime},\\
p-1&\mid qr+1,\\
q-1&\mid pr+1.
\end{aligned}
\]
Here \(p\) and \(q\) must be prime, and the second line requires \(q-1\) to be a positive divisor of \((p+1)(p+d)\). In particular,
\[
q\le 2p^2+p,\qquad r\le pq+2.
\]
Thus the entire three-prime family is effectively finite for every fixed smallest prime \(p\).

The first two fibers are completely determined:
\[
\begin{aligned}
p=3 &: (p,q,r)\in\{(3,5,17),(3,17,53)\},\\
p=5 &: (p,q,r)\in\{(5,7,13),(5,7,37),(5,13,67),(5,19,97),(5,43,109)\}.
\end{aligned}
\]
Equivalently, their products are respectively \(255,2703\), and \(455,1295,4355,9215,23435\).

## Assumptions and scope

All prime variables are odd, distinct, and strictly ordered \(p<q<r\). The theorem classifies only squarefree products of exactly three odd primes; it makes no assertion about products of four or more primes. The condition is equivalently that \(p-1\), \(q-1\), and \(r-1\) each divide \(pqr+1\). In the terminology of generalized Korselt conditions, it is the \((1,-1)\)-Carmichael condition, different from ordinary Carmichael numbers (\((1,1)\)) and from Lucas–Carmichael numbers (\((-1,-1)\)).

## Proof

For a product of distinct odd primes, \(\lambda(pqr)=\operatorname{lcm}(p-1,q-1,r-1)\). Reducing the original divisibility modulo \(r-1\), where \(r\equiv1\), gives \(r-1\mid pq+1\). Define
\[
d=\frac{pq+1}{r-1}.
\]
Because distinct odd primes \(r>q\) satisfy \(r\ge q+2\), we have \(r-1\ge q+1\), and hence
\[
1\le d\le\frac{pq+1}{q+1}<p.
\]
Thus \(d\in\{1,2,\ldots,p-1\}\), and \(r=1+(pq+1)/d\).

The \(q-1\) condition is equivalent to \(q-1\mid pr+1\), since \(q\equiv1\pmod{q-1}\). Multiplying by \(d\) and substituting the formula for \(r\) yields
\[
d(pr+1)=d(p+1)+p(pq+1)\equiv(p+1)(p+d)\pmod{q-1}.
\]
Therefore \(q-1\mid(p+1)(p+d)\). Because \(d\le p-1\),
\[
q-1\le(p+1)(p+d)\le(p+1)(2p-1)=2p^2+p-1,
\]
so \(q\le2p^2+p\). Also \(d\ge1\) gives \(r=1+(pq+1)/d\le pq+2\).

Conversely, take any \(p<q\) prime and \(d\in[1,p-1]\) meeting all displayed conditions, and define the prime \(r>q\) from the formula. Then \(r-1\mid pq+1\), whence \(r-1\mid pqr+1\); the remaining two explicit divisibilities similarly imply \(p-1,q-1\mid pqr+1\). Their least common multiple divides \(pqr+1\), proving the equivalence. Note that the displayed condition \(q-1\mid(p+1)(p+d)\) is a necessary sieve and does not alone imply \(q-1\mid pr+1\) when \(d\) is not invertible modulo \(q-1\); this latter condition is deliberately retained in the exact criterion.

For \(p=3\), the only \(d\) are \(1,2\), yielding \((p+1)(p+d)=16,20\). At \(d=2\), the conditions \(q-1\mid20\) and \(q>3\) leave only a short list of odd prime \(q\); none produces a prime \(r>q\). At \(d=1\), \(q-1\mid16\) and \(q>3\) force \(q\in\{5,17\}\), producing \(r\in\{17,53\}\); direct substitutions meet every original divisibility.

For \(p=5\), inspect \(d\in\{1,2,3,4\}\), with required \(q-1\) dividing \(36,42,48,54\), respectively. Applying \(q>5\), primality of \(q,r\), and integrality of \(r=1+(5q+1)/d\), the preliminary \((q,r)\) lists by \(d\) are respectively
\[
\begin{aligned}
d=1 &: (7,37),(13,67),(19,97);\\
d=2 &: (7,19),(43,109);\\
d=3 &: (7,13),(13,23);\\
d=4 &: \varnothing.
\end{aligned}
\]
The two extra pairs \((7,19)\) and \((13,23)\) fail the \(p-1\) or \(q-1\) divisibility checks; all other pairs pass. This proves the stated exact lists without numerical cutoffs on \(n\).

## Verification

The standalone script `verify.py` uses trial-division primality tests and exact integer arithmetic. It constructs each candidate from the divisors of \((p+1)(p+d)\), applies the original Carmichael exponent equation, and independently enumerates all prime triples inside the proved \(q\)- and \(r\)-bounds for \(p=3\) and \(p=5\). Both enumerations agree on the seven triples stated above. These finite checks are a reproducibility aid; the unrestricted finiteness assertion is proved by the preceding algebra, not by a search limit.

## Relationship to prior work

The familiar Carmichael condition is \(\lambda(n)\mid n-1\), and McNew studies weakenings of that **minus-shift** condition, including the radical of the totient. Zheng's definition of \((a,b)\)-Carmichael numbers includes the present **positive-shift** condition as \((1,-1)\), but Zheng's proved infinitude theorem is for the different \((-1,1)\) condition \(p+1\mid n-1\). The displayed finite divisor sieve and the complete fixed-least-prime fibers are not consequences of the results stated in these inspected papers. The distinction is at the implication level, not merely terminological.

## Limitations

No claim is made about how many distinct smallest primes occur, or about infinitude of \((1,-1)\)-Carmichael numbers overall. The full proof uses the squarefree three-prime hypothesis. Literature coverage cannot exclude every unindexed elementary argument; the originality assessment is limited to the identified papers and searched records. The script exhaustively checks two fibers, not the infinite family.

## References

1. Nathan McNew, *Radically weakening the Lehmer and Carmichael conditions*, arXiv:1210.2001v1 (first posted 2012-10-06), especially the introduction and §§2–3. https://arxiv.org/html/1210.2001v1
2. Qi-Yang Zheng, *There are infinitely many (-1,1)-Carmichael numbers*, arXiv:2207.08641v2 (2022), Definition 1.1 and Theorem 1.1. https://arxiv.org/html/2207.08641v2
3. *Carmichael function*, Encyclopedia of Mathematics, primary MSC 11A25; definition and squarefree formula. https://encyclopediaofmath.org/wiki/Carmichael_function
