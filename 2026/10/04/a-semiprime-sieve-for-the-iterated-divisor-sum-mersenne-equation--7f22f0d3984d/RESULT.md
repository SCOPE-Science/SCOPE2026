# A semiprime sieve for the iterated divisor-sum Mersenne equation
## Finding
Consider the equation
\[
\sigma(\sigma(n))=2n+1.
\]
Mersenne primes satisfy this equation, and a public 2005 problem asks whether
these are all of its solutions.

Let \(n>1\) be a **composite** solution with
\[
\Omega(n)\le2,
\]
where \(\Omega\) counts prime factors with multiplicity. Then
\[
n=pq
\]
for distinct odd primes
\[
37\le p<q.
\]
Put
\[
M=\sigma(n)=(p+1)(q+1).
\]
Then:

1. \(M\) is a square or twice a square;
2. \(\gcd(M,105)=1\);
3. for each \(r\in\{p,q\}\), if
   \[
   R(r)=\prod_{\substack{\ell\ {
m odd\ prime}\\v_\ell(r+1)\ {
m odd}}}\ell,
   \]
   then
   \[
   2(r+1)R(r)\mid M
   \]
   and
   \[
   \frac{\sigma(2(r+1)R(r))}{2(r+1)R(r)}
   <\frac{2r}{r+1}.
   \]

Thus there is no composite prime-square solution and no even semiprime
solution. Any composite solution in the first almost-prime layer is forced
into a sparse odd squarefree-semiprime regime with least prime at least
\(37\) and an explicit local square-kernel obstruction.

## Assumptions and scope
The ordinary divisor-sum function is
\[
\sigma(m)=\sum_{d\mid m}d,
\]
and the abundancy index is
\[
I(m)=\frac{\sigma(m)}m.
\]
The theorem concerns only composite solutions with \(\Omega(n)\le2\). It
does not classify prime solutions and does not settle the full conjecture that
all solutions of \(\sigma(\sigma(n))=2n+1\) are Mersenne primes.

Two standard elementary facts are used.

First,
\[
\sigma(t)\text{ is odd}
\quad\Longleftrightarrow\quad
t\text{ is a square or twice a square}.
\]
Indeed, for an odd prime \(\ell\), the factor
\(1+\ell+\cdots+\ell^e\) is odd exactly when \(e\) is even, while the
corresponding factor for \(2^e\) is always odd.

Second, abundancy is monotone under divisibility:
\[
a\mid b\quad\Longrightarrow\quad I(a)\le I(b).
\]
This follows from the prime-power product formula, because every local factor
\(1+1/\ell+\cdots+1/\ell^e\) increases with \(e\), and adding a new prime
factor multiplies the index by a number greater than one.

## Proof
Assume throughout that \(n>1\) is composite,
\(\Omega(n)\le2\), and
\[
\sigma(\sigma(n))=2n+1.
\]

There are only two composite shapes: a prime square or a product of two
distinct primes.

Suppose first that
\[
n=p^2.
\]
Then
\[
M=\sigma(n)=p^2+p+1
\]
is odd, while the defining equation says
\[
\sigma(M)=2p^2+1,
\]
which is also odd. Hence \(M\) must be a square. But
\[
p^2<p^2+p+1<(p+1)^2,
\]
so this is impossible. Therefore no prime-square solution exists.

Now write
\[
n=pq,
\qquad p<q
\]
with distinct primes. If \(p=2\), then
\[
M=\sigma(2q)=3(q+1),
\]
so \(6\mid M\). By abundancy monotonicity,
\[
I(M)\ge I(6)=2.
\]
On the other hand, the equation gives
\[
I(M)=\frac{4q+1}{3(q+1)}<2,
\]
a contradiction. Hence \(p,q\) are both odd.

For odd \(p,q\),
\[
M=(p+1)(q+1)
\]
and
\[
\sigma(M)=2pq+1
\]
is odd. Therefore \(M\) is a square or twice a square. In particular, every
odd prime occurs in \(M\) to an even exponent.

Also
\[
I(M)=\frac{2pq+1}{(p+1)(q+1)}<2. \tag{1}
\]
If one of \(3,5,7\) divided \(M\), then its exponent in \(M\) would be at
least two; moreover \(4\mid M\) because both \(p+1\) and \(q+1\) are even.
Thus, for \(\ell\in\{3,5,7\}\) dividing \(M\),
\[
4\ell^2\mid M.
\]
But
\[
I(4\cdot3^2)=\frac{91}{36}>2,
\qquad
I(4\cdot5^2)=\frac{217}{100}>2,
\qquad
I(4\cdot7^2)=\frac{57}{28}>2,
\]
contradicting (1). Hence
\[
\gcd(M,105)=1. \tag{2}
\]

We now exclude every possible least prime below \(37\). The odd primes below
\(37\) are
\[
3,5,7,11,13,17,19,23,29,31.
\]
For
\[
p\in\{5,11,13,17,19,23,29\},
\]
the number \(p+1\) is divisible by at least one of \(3,5,7\), contradicting
(2).

The remaining three primes are eliminated by their forced power of two. If
\(p=3\), then \(8\mid M\), so
\[
I(M)\ge I(8)=\frac{15}{8}.
\]
But more sharply than (1),
\[
I(M)=\frac{2pq+1}{(p+1)(q+1)}<\frac{2p}{p+1}, \tag{3}
\]
and for \(p=3\) the right side is \(3/2\), a contradiction.

If \(p=7\), then \(16\mid M\), and
\[
I(M)\ge\frac{31}{16}>\frac74=\frac{2p}{p+1}.
\]
If \(p=31\), then \(64\mid M\), and
\[
I(M)\ge\frac{127}{64}>\frac{31}{16}=\frac{2p}{p+1}.
\]
Thus
\[
p\ge37.
\]

Finally fix \(r\in\{p,q\}\) and define the odd squarefree kernel of the
odd-valuation part of \(r+1\) by
\[
R(r)=\prod_{\substack{\ell\ {
m odd\ prime}\\v_\ell(r+1)\ {
m odd}}}\ell.
\]
Every odd valuation of \(M\) is even. Hence if
\(v_\ell(r+1)\) is odd, the other factor among \(p+1,q+1\) contains at
least one additional factor \(\ell\). The other factor is also even. Therefore
\[
2(r+1)R(r)\mid M. \tag{4}
\]
Abundancy monotonicity and (3), applied with \(r=p\) or \(r=q\), now give
\[
I(2(r+1)R(r))
\le I(M)
<\frac{2r}{r+1}.
\]
This is the claimed local sieve.

## Verification
The proof is unrestricted and symbolic. The accompanying checker performs
four independent finite sanity checks:

- the parity characterization of odd divisor sums on an initial interval;
- the three exact abundancy inequalities excluding odd factors \(3,5,7\);
- the complete list of primes below \(37\) and the stated exclusion mechanism
  for each;
- direct evaluation of \(\sigma(\sigma(n))\) for all
  \(n\le200000\) with \(\Omega(n)\le2\).

The finite sweep finds the familiar Mersenne-prime solutions
\[
3,7,31,127,8191,131071
\]
in that interval and no composite solution. The sweep is corroborative only;
no bounded computation is used to establish the theorem.

## Relationship to prior work
OEIS A000668 records the exact open question, dated 19 August 2005: every
Mersenne prime satisfies
\[
\sigma(\sigma(n))=2n+1,
\]
and asks whether the Mersenne primes give all solutions. The entry does not
state a semiprime reduction or a lower bound for the least prime of a
composite solution.

Sándor's 2005 paper studies compositions of arithmetic functions, including
\(\sigma\circ\sigma\), and places the topic under primary MSC 11A25. Its
introduction treats superperfect numbers and neighboring almost/quasiperfect
relations, but the inspected material does not supply the ordinary
\(\sigma(\sigma(n))=2n+1\) semiprime classification proved here.

Fang's paper on the neighboring equation
\[
\sigma(\sigma(n))=2n-1
\]
proves square/parity restrictions by related divisor-sum methods and is also
classified primarily under MSC 11A25. Its full theorem statements and proofs
concern the opposite sign and do not imply the present plus-one semiprime
sieve.

OEIS A051027 tabulates the iterated divisor sum \(\sigma(\sigma(n))\) and
records the classical superperfect relation \(\sigma(\sigma(n))=2n\), but it
does not give the plus-one low-complexity theorem.

## Limitations
The theorem does not exclude odd semiprime solutions with least prime at least
\(37\), nor does it classify prime solutions. It therefore does not solve the
2005 Mersenne-prime conjecture for the equation.

The closest composition literature is broad, and older material is not
uniformly searchable. An equivalent low-complexity observation may exist under
different terminology; this remains the principal originality risk. The
result should be read as a rigorous structural sieve, not as a proof of the
full conjecture.

The exact public date used in metadata is the dated 19 August 2005 OEIS
problem statement. Earlier literature on compositions of divisor functions is
historically relevant, but no earlier exact-day public source for this specific
plus-one problem was verified.

## References
1. OEIS Foundation, A000668, "Mersenne primes"; comment by Farideh
   Firoozbakht dated 19 August 2005 asking whether all solutions of
   \(\sigma(\sigma(n))=2n+1\) are Mersenne primes.
2. József Sándor, "On the Composition of Some Arithmetic Functions, II",
   *Journal of Inequalities in Pure and Applied Mathematics* 6 (2005),
   Article 73. MSC2000 11A25, 11N37.
3. Jin-Hui Fang, "On Almost Superperfect Numbers", *The Fibonacci Quarterly*
   46/47 (2008/2009), no. 2, 111--114,
   DOI 10.1080/00150517.2008.12428167. MSC2000 11A25, 11A51, 11D41.
4. OEIS Foundation, A051027, "\(a(n)=\sigma(\sigma(n))\)".
