# Two-prime-support rigidity for square-prime-factor fixed points

## Finding
For an integer \(n\ge2\), write
\[
n=\prod_{p^e\parallel n}p^e
\]
and define
\[
T_2(n)=\sum_{p^e\parallel n} e p^2.
\]
Thus \(T_2(n)\) is the sum of the squares of the prime factors of \(n\), counted with multiplicity.

If
\[
T_2(n)=n
\]
and \(\omega(n)\le2\), then
\[
n\in\{16,27\}.
\]
Conversely,
\[
T_2(16)=16,
\qquad
T_2(27)=27.
\]
Hence the complete fixed-point set with at most two distinct prime factors is
\[
\{16,27\}.
\]
In particular, every other fixed point of \(T_2\) must have at least three distinct prime factors.

## Assumptions and scope
The domain is the set of integers \(n\ge2\). The notation \(\omega(n)\) denotes the number of distinct prime divisors of \(n\).

The theorem classifies the fixed points of \(T_2\) only under the structural hypothesis \(\omega(n)\le2\). It does not classify fixed points with three or more distinct prime divisors and does not address whether infinitely many fixed points exist.

## Proof
First suppose \(n=p^m\) is a prime power. Then
\[
T_2(n)=mp^2,
\]
so a fixed point must satisfy
\[
p^m=mp^2,
\qquad
m=p^{m-2}.
\]
For \(m=3\), this gives \(p=3\) and hence \(n=27\). For \(m=4\), this gives \(p=2\) and hence \(n=16\). The cases \(m=1,2\) are impossible, while for \(m\ge5\),
\[
p^{m-2}\ge2^{m-2}>m.
\]
Thus the only prime-power fixed points are \(16\) and \(27\).

Now suppose \(n\) has exactly two distinct prime factors.

First consider two odd primes:
\[
n=p^a q^b,
\qquad p\ne q.
\]
Since \(n\) is odd while
\[
T_2(n)\equiv a+b\pmod2,
\]
we must have \(a+b\) odd. Relabeling the two primes if necessary, write
\[
a=2A,
\qquad
b=2B+1,
\]
with \(A\ge1\) and \(B\ge0\).

If \(B=0\), then
\[
p^{2A}q=2Ap^2+q^2.
\]
Regarded as a quadratic equation in \(q\), its discriminant must be a square. Thus for some nonnegative integer \(r\),
\[
r^2=p^{4A-2}-8A.
\]
Therefore
\[
\bigl(p^{2A-1}-r\bigr)\bigl(p^{2A-1}+r\bigr)=8A.
\]
Both factors are positive even integers. The first is at least \(2\), so the second is at most \(4A\), and consequently
\[
p^{2A-1}\le4A.
\]
For \(A\ge2\), however,
\[
p^{2A-1}\ge3^{2A-1}>4A,
\]
a contradiction. If \(A=1\), then \(p\le4\), so \(p=3\); the quadratic becomes
\[
q^2-9q+18=0,
\]
whose roots are \(3\) and \(6\), neither a distinct odd prime. Hence this branch has no solution.

Now let \(B\ge1\). The fixed-point equation is
\[
p^{2A}q^{2B+1}=2Ap^2+(2B+1)q^2.
\]
Reducing modulo \(q^2\) gives
\[
q^2\mid A,
\]
and reducing modulo \(p^2\) gives
\[
p^2\mid 2B+1.
\]
Write
\[
A=q^2C,
\qquad
2B+1=p^2D,
\]
with \(C,D\ge1\). Dividing the fixed-point equation by \(p^2q^2\) yields
\[
p^{2q^2C-2}q^{p^2D-2}=2C+D.
\]
Because \(p,q\ge3\),
\[
p^{2q^2C-2}q^{p^2D-2}
\ge
3^{16C+7D}
>
2C+D,
\]
a contradiction. Therefore no fixed point has exactly two odd prime divisors.

It remains to treat
\[
n=2^k p^a,
\]
where \(p\) is odd and \(k,a\ge1\). The equation
\[
2^kp^a=4k+ap^2
\]
shows by parity that \(a\) is even; write \(a=2B\), with \(B\ge1\). Reducing modulo \(p^2\) gives
\[
p^2\mid k.
\]
Write \(k=p^2C\), with \(C\ge1\). After division by \(2p^2\),
\[
2^{p^2C-1}p^{2B-2}=2C+B.
\]
The left side satisfies
\[
2^{p^2C-1}p^{2B-2}
\ge
2^{8C}3^{2B-2}
\ge
256CB
>
2C+B,
\]
again a contradiction.

All two-prime-support cases are therefore impossible, while the one-prime-support cases are exactly \(16\) and \(27\).

## Verification
The accompanying `verify.py` independently checks the defining equation over a broad finite grid of prime powers and two-prime-support integers. It also tests the inequalities used in each proof branch over a finite range of the auxiliary exponents.

The finite replay is regression evidence only. The classification for all integers with \(\omega(n)\le2\) is proved symbolically above.

## Relationship to prior work
Hurd and McCranie define the functions \(T_s\), prove a complete prime-power criterion, and devote a section to eliminating possible elements of \(T^*(2)\). They show that \(16\) and \(27\) are fixed, rule out several exponent patterns, and obtain strong divisibility conditions for odd two-prime candidates. Their 2019 conclusion conjectures that these two values are the entire fixed-point set.

That global conjecture was later disproved: current OEIS records three additional fixed points with more than one hundred digits. The present theorem does not revive the global conjecture. Instead, it completes the low-support classification: no fixed point supported on exactly two primes exists, so every later or future nontrivial fixed point necessarily has at least three distinct prime divisors.

The closest older literature of De Koninck and Luca studies sums of powers of distinct prime factors, with multiplicity ignored. That is a different equation and does not imply the present multiplicity-weighted classification.

Targeted semantic and exact-formulation searches for \(T_2\)-fixed points, A067666, A068916, two-prime support, and the multiplicity-weighted square-prime-factor equation did not locate a prior complete \(\omega(n)\le2\) theorem.

## Limitations
The theorem does not classify fixed points with three or more distinct prime divisors. In particular, it does not address the known very large counterexamples to the old two-element conjecture beyond proving that they cannot have support size at most two.

The originality search cannot exclude an unindexed note or informal derivation of the same low-support classification. The strongest residual risk is that the final contradiction could have been regarded as an unstated continuation of the necessary divisibility conditions in the 2019 paper.

## References
1. Spencer P. Hurd and Judson S. McCranie, “Integers That Are Sums of Uniform Powers of All Their Prime Factors: The Sequence A068916,” Journal of Integer Sequences 22 (2019), Article 19.3.4.
2. OEIS A067666, “Sum of squares of prime factors of \(n\) (counted with multiplicity).”
3. OEIS A338093, “Composite numbers which are multiples of the sum of the squares of their prime factors (taken with multiplicity).”
4. OEIS A339062, prime entries occurring in prime Markoff--Hurwitz seven-tuples connected with later large fixed points.
5. Jean-Marie De Koninck and Florian Luca, “Partial Sums of Powers of Prime Factors,” Journal of Integer Sequences 10 (2007), Article 07.1.6.
