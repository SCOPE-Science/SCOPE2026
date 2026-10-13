# Two-digit Niven counts and a prime base-minus-one minimum
## Finding
Let \(b\ge2\) be an integer base and put
\[
M=b-1.
\]
Let \(H_2(b)\) denote the number of base-\(b\) Niven numbers with exactly two digits. Then
\[
H_2(b)
=
M+
\sum_{\substack{v\mid M\\v\ge2}}
\ \sum_{\substack{1\le u<v\\\gcd(u,v)=1}}
\left\lfloor
\frac{M}{\max\{u,v-u\}}
\right\rfloor.
\tag{1}
\]

Consequently,
\[
H_2(b)\ge 2b-3
\]
for every \(b\ge2\).

For every
\[
b\ge4,
\]
the lower bound is sharp exactly when
\[
b-1
\]
is prime:
\[
H_2(b)=2b-3
\quad\Longleftrightarrow\quad
b-1\text{ is prime}.
\tag{2}
\]

The small bases are
\[
H_2(2)=1,\qquad H_2(3)=4.
\]
Thus base \(2\) is the sole equality exception to the prime characterization, while base \(3\) is the sole case in which a prime value of \(b-1\) does not attain the bound.

## Assumptions and scope
For a positive integer \(n\), let \(s_b(n)\) be the sum of its base-\(b\) digits. A base-\(b\) Niven number is a positive integer satisfying
\[
s_b(n)\mid n.
\]

Every two-digit base-\(b\) integer is written uniquely as
\[
n=ab+c,
\]
where
\[
1\le a\le b-1=M,
\qquad
0\le c\le b-1=M.
\]
Its digit sum is
\[
s_b(n)=a+c.
\]

The theorem counts exactly this complete two-digit stratum. It does not assert an asymptotic for Niven numbers with unrestricted digit length.

## Proof
Write
\[
n=ab+c=a(M+1)+c.
\]
The Niven condition is
\[
a+c\mid ab+c.
\]
Subtracting the digit sum gives the equivalent condition
\[
a+c\mid a(b-1)=aM.
\tag{3}
\]

First count the cases with
\[
c=0.
\]
There are exactly \(M\) of them, one for each
\[
1\le a\le M,
\]
and all are Niven because their digit sum \(a\) divides \(ab\).

Now suppose
\[
c>0.
\]
Put
\[
s=a+c,
\qquad
g=\gcd(a,s),
\qquad
a=gu,
\qquad
s=gv,
\]
so that
\[
\gcd(u,v)=1
\quad\text{and}\quad
1\le u<v.
\]
Condition (3) becomes
\[
gv\mid guM,
\]
and coprimality gives
\[
v\mid M.
\tag{4}
\]

Conversely, choose a divisor
\[
v\mid M,\qquad v\ge2,
\]
and choose
\[
1\le u<v,\qquad \gcd(u,v)=1.
\]
For a positive integer \(g\), define
\[
a=gu,\qquad c=g(v-u).
\]
Then
\[
a+c=gv
\]
and (4) implies
\[
a+c\mid aM.
\]
Thus every such digit pair is Niven.

The two digit bounds are exactly
\[
gu\le M
\quad\text{and}\quad
g(v-u)\le M.
\]
Hence
\[
1\le g\le
\left\lfloor
\frac{M}{\max\{u,v-u\}}
\right\rfloor.
\]
The decomposition by
\[
g=\gcd(a,a+c),\qquad
u=a/g,\qquad
v=(a+c)/g
\]
is unique. Adding the \(M\) zero-final-digit cases proves (1).

For the universal lower bound, two disjoint families are always present. The first consists of
\[
(ab)_b
\]
with \(1\le a\le M\), giving \(M\) numbers. The second consists of all digit pairs satisfying
\[
a+c=M,
\qquad
1\le a\le M-1.
\]
For this family,
\[
ab+c
=
a(M+1)+(M-a)
=
M(a+1),
\]
so the digit sum \(M\) divides the number. This gives another \(M-1\) numbers. Therefore
\[
H_2(b)\ge M+(M-1)=2M-1=2b-3.
\]

Now assume
\[
b\ge4.
\]
If \(M=p\) is prime, then \(p\ge3\). Let \(c>0\) and suppose
\[
a+c\mid ap.
\]
If \(a<p\), put
\[
s=a+c
\]
and
\[
d=\gcd(a,s).
\]
Then
\[
s/d\mid p.
\]
Since \(s>a\), one cannot have \(s/d=1\). Thus
\[
s/d=p.
\]
But
\[
s\le a+p<2p,
\]
so necessarily
\[
d=1
\quad\text{and}\quad
s=p.
\]
Therefore every case with \(a<p\) and \(c>0\) belongs to the universal family
\[
a+c=p.
\]

If instead \(a=p\) and \(c>0\), then
\[
p+c\mid p^2
\]
with
\[
p<p+c\le2p.
\]
The divisors of \(p^2\) are
\[
1,\ p,\ p^2,
\]
and for \(p\ge3\) one has
\[
p^2>2p.
\]
So no such \(c\) exists. Hence the two universal families are all the two-digit Niven numbers, and
\[
H_2(b)=2p-1=2b-3.
\]

Conversely, suppose \(M\) is composite. Since \(M\ge4\), choose a proper divisor
\[
d\mid M,\qquad 1<d<M.
\]
The two-digit number with digits
\[
(1,d-1)_b
\]
has digit sum \(d\), and its value is
\[
b+d-1=M+d,
\]
which is divisible by \(d\). It is not in the zero-final-digit family because \(d-1>0\), and it is not in the digit-sum-\(M\) family because \(d<M\). Therefore
\[
H_2(b)>2b-3.
\]
This proves (2).

Finally, direct evaluation gives
\[
H_2(2)=1,\qquad H_2(3)=4,
\]
which explains the two stated small-base exceptions.

## Verification
The accompanying checker independently enumerates every two-digit integer for each base
\[
2\le b\le300.
\]
For every base it compares the direct Niven count with formula (1), verifies the lower bound, and checks the equality characterization for every
\[
4\le b\le300.
\]

The checker also verifies that every composite
\[
M=b-1
\]
in this range has the explicit extra witness
\[
(1,d-1)_b
\]
constructed from its least proper divisor \(d>1\).

These finite tests corroborate the proof. Formula (1) and the prime characterization are proved for all integer bases by the preceding argument and do not rely on bounded computation.

## Relationship to prior work
Daileda, Jou, Lemke-Oliver, Rossolimo, and Treviño study generalized Niven numbers in a fixed integer base \(q\). They define the same base-\(q\) digit-sum divisibility condition and prove an asymptotic counting theorem as the size bound tends to infinity. Their primary subject classification is \(11A25\). Their complete paper treats fixed-base asymptotics; it does not state an exact count for the two-digit stratum as the base varies, and searches of the full text found no occurrence of “two-digit” or “two digits.”

The standard OEIS entry A005349 records decimal Niven numbers and references the classical counting literature. It is a decimal value sequence, not an across-base two-digit count.

The result here is complementary to fixed-base asymptotics: it gives a finite exact count for every base through the divisor lattice of \(b-1\), and the extremal value of that exact count characterizes prime \(b-1\) for all \(b\ge4\).

## Limitations
The theorem concerns exactly two-digit Niven numbers. It does not give a comparable closed count for three or more digits, where the divisibility condition has additional positional terms.

The originality comparison included the complete archival generalized-Niven paper, the standard decimal sequence database, direct statement-level searches, and searches for aliases using “Harshad” and “Niven.” A short equivalent observation could still exist in unindexed recreational or educational literature.

The exact public date attached to the archival source is its verified online publication date, 22 March 2010; earlier papers cited there have older journal years, but no earlier exact public calendar date was used without direct verification.

## References
1. R. Daileda, J. Jou, R. Lemke-Oliver, E. Rossolimo, and E. Treviño, “On the counting function for the generalized Niven numbers,” *Journal de Théorie des Nombres de Bordeaux* 21 (2009), 503–515, doi:10.5802/jtnb.685.
2. OEIS Foundation, A005349, “Niven (or Harshad) numbers: numbers that are divisible by the sum of their digits.”
