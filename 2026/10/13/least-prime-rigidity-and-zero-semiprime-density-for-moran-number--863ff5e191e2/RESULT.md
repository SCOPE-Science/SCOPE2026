# Least-prime rigidity and zero semiprime density for Moran numbers
## Finding
Let \(S(n)\) denote the sum of the decimal digits of \(n\). A Moran number is
an integer \(n\) for which
\[
\frac{n}{S(n)}
\]
is prime.

If a Moran number satisfies
\[
\Omega(n)=2,
\]
where prime factors are counted with multiplicity, then
\[
n=pq
\]
for distinct primes \(p<q\), and necessarily
\[
S(pq)=p.
\]
Conversely, every product of distinct primes \(p<q\) satisfying
\[
S(pq)=p
\]
is a Moran number.

Thus the least prime factor of every semiprime Moran number satisfies the
intrinsic decimal bound
\[
p\le 9\bigl(\lfloor\log_{10}n\rfloor+1\bigr).
\]
If \(M_2(x)\) denotes the number of Moran numbers \(n\le x\) with
\(\Omega(n)=2\), then
\[
M_2(x)\ll \frac{x\log\log\log x}{\log x}.
\]
Since the number of semiprimes up to \(x\) is asymptotic to
\[
\frac{x\log\log x}{\log x},
\]
Moran numbers have relative density zero inside the semiprimes.

## Assumptions and scope
All digit sums are decimal. The function \(\Omega(n)\) counts prime factors
with multiplicity, so the layer \(\Omega(n)=2\) consists of prime squares and
products of two distinct primes.

The counting estimate is asymptotic as \(x\to\infty\). Its implicit constant
is absolute. The density conclusion is relative to all integers with exactly
two prime factors counted with multiplicity.

## Proof
Suppose first that
\[
n=r^2
\]
with \(r\) prime. If \(n\) is Moran, then \(n/S(n)\) is a prime divisor of
\(r^2\), hence it must equal \(r\). Therefore
\[
S(r^2)=r.
\]
The decimal digit-sum congruence gives
\[
r^2\equiv S(r^2)=r\pmod 9.
\]
Thus either \(r=3\) or
\[
r\equiv1\pmod 9.
\]
Also
\[
r=S(r^2)
 \le 9\bigl(\lfloor\log_{10}(r^2)\rfloor+1\bigr)
 \le 9\bigl(2\log_{10}r+1\bigr).
\]
For \(r\ge41\), the reverse strict inequality holds. Indeed,
\[
f(t)=t-18\log_{10}t-9
\]
is increasing for \(t>18/\log 10\), and \(f(41)>0\). Hence \(r<41\).
The only remaining prime candidates are \(3,19,37\), but
\[
S(9)=9,\qquad S(361)=10,\qquad S(1369)=19.
\]
Therefore no Moran number with \(\Omega(n)=2\) is a prime square.

Now write
\[
n=pq
\]
with distinct primes \(p<q\). Since \(n/S(n)\) is a prime dividing \(pq\),
we must have
\[
S(n)\in\{p,q\}.
\]
We show that the larger possibility is impossible.

Assume
\[
S(pq)=q.
\]
Because \(p<q\),
\[
q=S(pq)
 \le9\bigl(\lfloor\log_{10}(pq)\rfloor+1\bigr)
 \le9\bigl(2\log_{10}q+1\bigr).
\]
The same monotonicity argument forces \(q<41\), hence \(q\le37\). The
digit-sum congruence gives
\[
q\equiv pq\pmod9,
\]
so
\[
q(p-1)\equiv0\pmod9.
\]
If \(q=3\), then \(p=2\), but \(S(6)=6\). Otherwise \(q\ne3\), so \(q\)
is invertible modulo \(9\) and
\[
p\equiv1\pmod9.
\]
With \(p<q\le37\), this forces \(p=19\) and
\[
q\in\{23,29,31,37\}.
\]
Directly,
\[
S(19\cdot23)=14,\quad
S(19\cdot29)=11,\quad
S(19\cdot31)=22,\quad
S(19\cdot37)=10,
\]
so none equals \(q\). Thus
\[
S(pq)=p.
\]
Conversely, if distinct primes \(p<q\) satisfy \(S(pq)=p\), then
\[
\frac{pq}{S(pq)}=q
\]
is prime, so \(pq\) is Moran. This proves the exact structural statement.

The least-prime bound is immediate:
\[
p=S(n)\le9\bigl(\lfloor\log_{10}n\rfloor+1\bigr).
\]
For the counting statement, put
\[
Y=9\bigl(\lfloor\log_{10}x\rfloor+1\bigr).
\]
Every Moran number counted by \(M_2(x)\) has a least prime factor at most
\(Y\). Therefore
\[
M_2(x)\le\sum_{p\le Y}\pi\!\left(\frac{x}{p}\right).
\]
Since \(Y=O(\log x)\), the standard upper bound for the prime-counting
function is uniform here and gives
\[
\pi\!\left(\frac{x}{p}\right)
 \ll \frac{x}{p\log x}
\qquad(p\le Y).
\]
Mertens' theorem for prime reciprocals then yields
\[
\sum_{p\le Y}\frac1p
 =\log\log Y+O(1)
 =O(\log\log\log x).
\]
Consequently
\[
M_2(x)\ll\frac{x\log\log\log x}{\log x}.
\]
Landau's theorem gives
\[
\#\{n\le x:\Omega(n)=2\}
 \sim\frac{x\log\log x}{\log x}.
\]
The ratio is therefore
\[
O\!\left(\frac{\log\log\log x}{\log\log x}\right)=o(1),
\]
which proves the relative-density statement.

## Verification
The proof above is unrestricted. The accompanying checker verifies the finite
exceptional cases used in the proof and independently enumerates all integers
through \(10^6\) with \(\Omega(n)=2\). It finds \(1617\) Moran numbers in
that range; every one is squarefree and its decimal digit sum is its least
prime factor.

The finite enumeration is corroborative only. It is not used to infer either
the exact infinite classification or the asymptotic estimate.

## Relationship to prior work
Witno studied precisely the class of Niven numbers for which \(n/S(n)\) is
prime. The 2010 paper gives two construction methods, finite counting data,
and open problems about infinitude and the global counting function. It does
not state a semiprime or prime-square classification.

The original Moran-number problem is attributed to Bill Moran in the 1993
*Journal of Recreational Mathematics*. OEIS A001101 records the Moran-number
sequence and the historical references but does not state the
\(\Omega(n)=2\) rigidity result or its semiprime-density consequence.

A later paper by Witno studies chains in which the prime quotient is linked to
another Moran number. The available abstract describes that chain problem,
not a multiplicative-layer classification; no whole-document noncoverage
claim is made for that source.

The estimate here is logically different from Witno's conjectural global
asymptotic for all Moran numbers. It is unconditional and concerns only the
first composite multiplicative layer.

## Limitations
The theorem does not classify Moran numbers with \(\Omega(n)\ge3\), and the
upper bound for \(M_2(x)\) is not claimed to have the correct order of
magnitude.

Bill Moran's original 1993 problem was identified bibliographically but its
full text was not available for inspection here. The later chain paper was
available only through its abstract. These are residual originality risks.

The 2010 primary paper predates the exact-day source used in metadata, but the
inspected publication evidence resolves it only to June 2010. The earliest
exact public calendar date verified for a directly relevant Moran-number
source is 23 October 2012.

## References
1. A. Witno, "Numbers Which Factor as Their Digital Sum Times a Prime",
   *International Journal of Open Problems in Computer Mathematics* 3(2)
   (2010), 132--136. Primary MSC \(11A63\); secondary MSC \(11A41\).
2. B. Moran, Problem 2074, *Journal of Recreational Mathematics* 25(3)
   (1993), 215.
3. A. Witno, "A Chain of Moran Numbers", *Pioneer Journal of Algebra,
   Number Theory and its Applications* 6(2) (2013), 45--52.
4. OEIS Foundation, A001101, "Moran numbers".
5. Math::NumSeq::Moran, release Math-NumSeq-55, published 23 October 2012.
