# A negative-Pell spine for prime--semiprime Jordan-totient collisions
## Finding
Let
\[
J_2(n)=n^2\prod_{r\mid n}\left(1-\frac1{r^2}\right)
\]
be the second Jordan totient, with the product over prime divisors of \(n\).

For primes \(p,q\), the collision
\[
J_2(p)=J_2(2q)
\tag{1}
\]
holds if and only if
\[
(p,q)=(P_t,Q_t)
\]
for an index \(t\ge1\) at which both coordinates of the Pell sequence
\[
P_t+Q_t\sqrt3=(1+\sqrt3)(2+\sqrt3)^t
\tag{2}
\]
are prime.

Equivalently, this entire prime--twice-prime collision stratum is the prime-coordinate part of
\[
P_t^2-3Q_t^2=-2.
\tag{3}
\]

The coordinates satisfy
\[
P_{t+1}=2P_t+3Q_t,
\qquad
Q_{t+1}=P_t+2Q_t,
\]
starting from
\[
(P_0,Q_0)=(1,1).
\]
There is also a periodic primality obstruction:
\[
t\equiv1\pmod3,
\qquad t>1
\]
forces
\[
5\mid P_t,
\qquad
3\mid Q_t.
\tag{4}
\]
Thus no prime-coordinate collision can occur at those indices.

The first three collisions are
\[
J_2(5)=J_2(6)=24,
\]
\[
J_2(19)=J_2(22)=360,
\]
and
\[
J_2(71)=J_2(82)=5040.
\]
Further prime-coordinate Pell indices may or may not occur; the theorem gives an exact structural reduction rather than an infinitude claim.

## Assumptions and scope
The Jordan totient of order two is the multiplicative arithmetic function
\[
J_2(n)=n^2\prod_{r\mid n}\left(1-\frac1{r^2}\right).
\]
In particular, for a prime \(p\),
\[
J_2(p)=p^2-1,
\]
and for a prime \(q\),
\[
J_2(2q)=3(q^2-1)
\]
when \(q\ne2\).

The theorem classifies collisions in the natural mixed-support slice consisting of one prime argument and one argument equal to twice a prime. It does not classify arbitrary collisions of \(J_2\), and it does not assert that infinitely many Pell indices have both coordinates prime.

## Proof
For primes \(p,q\), equation (1) is
\[
p^2-1=3(q^2-1),
\]
so it is equivalent to
\[
p^2-3q^2=-2.
\tag{5}
\]
The cases \(p=2\) or \(q=2\) give no solution directly, so every collision has odd prime coordinates.

We first classify all positive integer solutions of (5). Define
\[
P_t+Q_t\sqrt3=(1+\sqrt3)(2+\sqrt3)^t,
\qquad t\ge0.
\]
Every such pair is positive and has norm
\[
P_t^2-3Q_t^2=-2.
\]

Conversely, let \((x,y)\) be a positive integer solution of
\[
x^2-3y^2=-2.
\]
If \(y=1\), then \(x=1\). Suppose \(y\ge2\). Set
\[
x'=2x-3y,
\qquad
y'=2y-x.
\tag{6}
\]
Because
\[
x^2=3y^2-2,
\]
one has \(x<2y\), hence \(y'>0\). Also
\[
4x^2-9y^2=3y^2-8>0,
\]
so \(x'>0\). Finally \(x>y\), so
\[
0<y'<y.
\]
Multiplication by \(2-\sqrt3\) shows that
\[
x'+y'\sqrt3=(x+y\sqrt3)(2-\sqrt3),
\]
and therefore
\[
{x'}^2-3{y'}^2=-2.
\]
Repeated descent reaches \((1,1)\). Reversing the descent multiplies by \(2+\sqrt3\), proving that every positive solution is exactly one pair \((P_t,Q_t)\). This proves the equivalence between (1) and the prime-coordinate part of (2).

It remains to prove the congruence obstruction. Since
\[
(2+\sqrt3)^3=26+15\sqrt3,
\]
we have
\[
P_{t+3}=26P_t+45Q_t,
\]
\[
Q_{t+3}=15P_t+26Q_t.
\tag{7}
\]
Modulo \(5\), equation (7) gives
\[
P_{t+3}\equiv P_t\pmod5.
\]
Since
\[
P_1=5,
\]
it follows that
\[
5\mid P_t
\]
whenever \(t\equiv1\pmod3\).

Modulo \(3\), equation (7) gives
\[
Q_{t+3}\equiv2Q_t\pmod3.
\]
Since
\[
Q_1=3,
\]
it follows that
\[
3\mid Q_t
\]
for the same congruence class of indices. For \(t>1\), the coordinates exceed \(5\) and \(3\), respectively, so both are composite. This proves (4).

The examples follow from
\[
(P_1,Q_1)=(5,3),
\quad
(P_2,Q_2)=(19,11),
\quad
(P_3,Q_3)=(71,41).
\]

## Verification
The accompanying checker reconstructs the Pell orbit with exact integer arithmetic, verifies (3), and independently evaluates \(J_2\) by integer factorization.

It checks the first thirty Pell pairs, confirms the recurrence, verifies every collision whose two coordinates are prime, and checks the congruence obstruction (4) through the first one hundred indices.

As a separate bounded stress test, it enumerates all primes \(p,q\le5000\) and confirms that
\[
J_2(p)=J_2(2q)
\]
occurs exactly at the prime-coordinate Pell pairs in that window.

These computations corroborate the proof. The unbounded equivalence is established by the negative-Pell descent, not by finite search.

## Relationship to prior work
Pabhapote and Laohakosol treat the Jordan totients inside a broad generalized-Euler-totient framework. Their full article defines \(J_s\) combinatorially and studies identities and connections among totient functions; it does not discuss equal-value collisions or Pell equations.

Andrica and Piticari give a primary number-theoretic treatment of Jordan-type arithmetic functions and list subject classification \(11A25\). Their paper supplies background on the classical function rather than a collision classification.

OEIS A007434 is the exact value sequence for \(J_2\). Its initial terms visibly contain
\[
J_2(5)=J_2(6)=24
\]
and later equal values, and it records the product formula used here. The database is value-indexed; it does not identify the prime--twice-prime collision slice with a negative Pell orbit.

The Pell reduction is useful because it changes an equality of multiplicative-function values into one explicit recurrence. The additional congruence obstruction then removes an entire third of the Pell indices, apart from the first collision.

## Limitations
The theorem concerns only collisions between a prime argument and an argument of the form twice a prime. Other \(J_2\) collisions arise from different factorization patterns and are not classified here.

The theorem does not prove that infinitely many indices \(t\) have both \(P_t\) and \(Q_t\) prime. It gives an exact candidate sequence and one infinite congruence exclusion.

The closest full primary source inspected contains the definition and general theory of the Jordan totient but no collision discussion. Formula-level searches for the negative-Pell equation together with \(J_2\), and semantic searches for prime--semiprime Jordan-totient collisions, found no equivalent accessible statement. An equivalent observation may still occur in unindexed notes or recreational literature.

An older Jordan-function source from 2003 was identified with year-level bibliographic evidence and MSC \(11A25\). The structured public date uses the earliest exact calendar day verified among the inspected archival sources, 14 September 2010, rather than inventing a day for the older source.

## References
1. N. Pabhapote and V. Laohakosol, “Combinatorial Aspects of the Generalized Euler's Totient,” *International Journal of Mathematics and Mathematical Sciences* 2010, Article 648165, doi:10.1155/2010/648165.
2. D. Andrica and M. Piticari, “On Some Extensions of Jordan's Arithmetic Functions,” *Acta Universitatis Apulensis*, 2003.
3. OEIS Foundation, A007434, “Jordan function \(J_2(n)\).”
