# Mersenne-factor parametrization of consecutive two-support unitary-totient collisions
## Finding
Let \(\phi^*\) denote the unitary totient function. Suppose consecutive integers
\[
n,\qquad n+1
\]
each have exactly two distinct prime divisors.

Exactly one member is even. Write its exact prime-power factorization as
\[
AB,
\qquad
A=2^a,
\]
where \(a\ge1\) and \(B\) is an odd prime power. Write the odd member as
\[
CD,
\]
where \(C<D\) are odd prime powers with distinct underlying primes.

Then
\[
\phi^*(n)=\phi^*(n+1)
\]
is completely parametrized by the positive factor pairs of the Mersenne number
\[
A-1=2^a-1.
\]

If the even member comes first,
\[
AB+1=CD,
\]
then every collision is obtained from a positive factorization
\[
uv=A-1
\]
by
\[
B=A-1+v-u,
\qquad
C=A-u,
\qquad
D=A+v.
\tag{1}
\]
Conversely, every factor pair for which the three displayed quantities are valid odd prime powers, with \(C<D\) supported on distinct primes, gives a collision.

If the even member comes second,
\[
CD+1=AB,
\]
there are two branches. For
\[
1\le u<v,
\qquad
uv=A-1,
\]
one has either
\[
B=A+1+u+v,
\qquad
C=A+u,
\qquad
D=A+v,
\tag{2}
\]
or
\[
B=A+1-u-v,
\qquad
C=A-v,
\qquad
D=A-u.
\tag{3}
\]
Again, exactly the tuples in which \(B,C,D\) are valid odd prime powers are retained.

A sharp small-complexity consequence is:
if additionally
\[
\Omega(n)\le3,
\qquad
\Omega(n+1)\le3,
\]
then the unique collision is
\[
(n,n+1)=(20,21),
\qquad
\phi^*(20)=\phi^*(21)=12.
\tag{4}
\]

The first two-support collisions illustrate all three branches:
\[
20\leftrightarrow21,
\quad
35\leftrightarrow36,
\quad
143\leftrightarrow144,
\quad
208\leftrightarrow209,
\quad
2623\leftrightarrow2624,
\quad
5183\leftrightarrow5184.
\]

## Assumptions and scope
A divisor \(d\) of \(m\) is unitary when
\[
\gcd(d,m/d)=1.
\]
The unitary totient \(\phi^*(m)\) is multiplicative and satisfies
\[
\phi^*(p^e)=p^e-1
\]
for every prime power. Consequently, if
\[
m=XY
\]
is a product of two exact prime-power blocks with different underlying primes, then
\[
\phi^*(m)=(X-1)(Y-1).
\tag{5}
\]

The theorem assumes that both consecutive integers have exactly two distinct prime divisors. Exponents are unrestricted in the main classification. The final corollary imposes the additional multiplicity bound \(\Omega\le3\).

No classification is claimed when either consecutive integer has one prime support or at least three distinct prime supports.

## Proof
Suppose first that the even member comes first:
\[
n=AB,
\qquad
n+1=CD.
\]
Consecutiveness gives
\[
CD=AB+1.
\tag{6}
\]
By (5), equality of the unitary totients is
\[
(A-1)(B-1)=(C-1)(D-1).
\]
Using (6), this simplifies exactly to
\[
C+D=A+B+1.
\tag{7}
\]

Put
\[
h=D-C,
\qquad
t=B-A+1.
\]
The two odd prime powers \(C,D\) make \(h\) even, and \(B\) odd makes \(t\) even. From (6) and (7),
\[
h^2=(A+B+1)^2-4(AB+1).
\]
A direct subtraction gives
\[
h^2-t^2=4(A-1).
\tag{8}
\]
Thus \(h>|t|\). Define
\[
u=\frac{h-t}{2},
\qquad
v=\frac{h+t}{2}.
\]
Then \(u,v\) are positive integers and (8) gives
\[
uv=A-1.
\]
Solving back for \(B,C,D\) yields exactly (1).

Conversely, suppose \(uv=A-1\) and define \(B,C,D\) by (1). Then
\[
CD=(A-u)(A+v)
=A\bigl(A-1+v-u\bigr)+1
=AB+1.
\]
Also
\[
C+D=A+B+1.
\]
These two identities reverse the preceding algebra and give
\[
(A-1)(B-1)=(C-1)(D-1).
\]
Hence every prime-power-valid tuple from (1) is a genuine collision.

Now suppose the even member comes second:
\[
n=CD,
\qquad
n+1=AB.
\]
Then
\[
CD=AB-1
\tag{9}
\]
and unitary-totient equality becomes
\[
C+D=A+B-1.
\tag{10}
\]
Put
\[
h=D-C,
\qquad
t=B-A-1.
\]
Equations (9) and (10) give
\[
t^2-h^2=4(A-1).
\tag{11}
\]
Hence \(|t|>h\).

If \(t>0\), define
\[
u=\frac{t-h}{2},
\qquad
v=\frac{t+h}{2}.
\]
Then
\[
1\le u<v,
\qquad
uv=A-1,
\]
and solving gives (2).

If \(t<0\), define
\[
u=\frac{-t-h}{2},
\qquad
v=\frac{-t+h}{2}.
\]
Again
\[
1\le u<v,
\qquad
uv=A-1,
\]
and solving gives (3). The case \(t=0\) is impossible in (11).

Conversely, for branch (2),
\[
(A+u)(A+v)=A(A+1+u+v)-1,
\]
and for branch (3),
\[
(A-v)(A-u)=A(A+1-u-v)-1.
\]
Thus both branches satisfy consecutiveness. Their sum identities reverse the unitary-totient algebra, so every prime-power-valid tuple is a collision. This proves the complete parametrization.

For the final corollary, if both members also satisfy \(\Omega\le3\), then the even member \(2^aB\) has
\[
a\le2.
\]
Hence \(A\) is \(2\) or \(4\).

For \(A=2\), the only factorization of \(A-1\) is \(1\cdot1\); every branch is invalid because it gives either a unit block or identical odd prime-power blocks.

For \(A=4\), one has
\[
A-1=3.
\]
Branch (1) with \((u,v)=(1,3)\) gives
\[
(B,C,D)=(5,3,7),
\]
hence \((20,21)\). The reversed factor pair makes a block equal to \(1\). Branch (2) gives
\[
(B,C,D)=(9,5,7),
\]
hence \((35,36)\), but
\[
\Omega(36)=4.
\]
Branch (3) is invalid. Therefore (4) is the unique collision under the multiplicity bound.

## Verification
The accompanying checker independently factors every integer below
\[
10^6+1.
\]
It computes the unitary totient from the prime-power product formula and extracts every consecutive collision for which both members have exactly two distinct prime factors.

For every observed collision it reconstructs \(A,B,C,D\), identifies the correct branch, recovers \(u,v\), and checks
\[
uv=A-1
\]
together with the corresponding formulas (1), (2), or (3).

In this range the complete observed two-support list is
\[
20,\ 35,\ 143,\ 208,\ 2623,\ 5183.
\]
The checker also filters the same range by
\[
\Omega(n),\Omega(n+1)\le3
\]
and obtains only
\[
20.
\]

Finally, it directly generates all three parameter branches for every \(A=2^a\) relevant below the search bound and verifies that every prime-power-valid generated pair is a direct collision.

The finite replay is corroborative. The unrestricted classification follows from the difference-of-squares identities (8) and (11).

## Relationship to prior work
Tóth gives the standard unitary-Euler framework, including multiplicativity and the prime-power formula
\[
\phi^*(p^e)=p^e-1.
\]
His paper studies combinatorial formulas and average orders rather than consecutive equal values. Targeted full-text searches of that article for “consecutive” and “collision” produced no such statement.

OEIS A287055 is devoted exactly to the equation
\[
\phi^*(n)=\phi^*(n+1).
\]
It begins
\[
1,20,35,143,194,208,740,\ldots
\]
and explicitly records
\[
\phi^*(20)=\phi^*(21)=12.
\]
It is an exact collision database, but it does not classify the subfamily in which both members have exactly two distinct prime supports.

The present theorem explains, in one factorization of \(2^a-1\), why the low-support database terms split into three algebraic branches. For instance,
\[
20,35
\]
come from the factorization \(3=1\cdot3\), while
\[
143,208
\]
come from factor pairs of \(15\), and
\[
2623,5183
\]
from factor pairs of \(63\).

## Limitations
The theorem is restricted by distinct prime support, not by size. Collisions in which either member has three or more distinct prime factors are outside the parametrization.

The exact database already contains many such higher-support collisions, so the theorem is not a global classification of consecutive unitary-totient equalities.

The literature comparison included a full primary treatment of the unitary totient, the exact collision database, the standard unitary-totient database, semantic research-record searches, and direct statement searches. An equivalent low-support parametrization could still occur in unindexed computational notes or recreational literature.

## References
1. L. Tóth, “On the Bi-Unitary Analogues of Euler’s Arithmetical Function and the Gcd-Sum Function,” *Journal of Integer Sequences* 12 (2009), Article 09.5.2, published 23 June 2009.
2. OEIS Foundation, A047994, “Unitary totient (or unitary phi) function.”
3. OEIS Foundation, A287055, “Numbers \(n\) such that \(\phi^*(n)=\phi^*(n+1)\).”
