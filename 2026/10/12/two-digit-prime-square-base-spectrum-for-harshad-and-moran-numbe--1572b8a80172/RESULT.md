# Two-digit prime-square base spectrum for Harshad and Moran numbers
## Finding
Let \(p\) be prime and let \(B\) satisfy
\[
p<B\le p^2.
\]
Equivalently, \(p^2\) has exactly two digits in base \(B\).

Then \(p^2\) is a base-\(B\) Moran number if and only if
\[
B=pd+1
\]
for some positive divisor
\[
d\mid p-1.
\]
For such a divisor \(d\), the base-\(B\) expansion is
\[
p^2=
\left(\frac{p-1}{d}\right)B
+
\left(p-\frac{p-1}{d}\right),
\]
so the two digits sum to \(p\), and
\[
\frac{p^2}{S_B(p^2)}=p.
\]

Consequently, a fixed prime square \(p^2\) is Moran in exactly
\[
\tau(p-1)
\]
two-digit bases.

The corresponding Harshad classification is also exact. Among bases \(p<B\le p^2\), the prime square \(p^2\) is base-\(B\) Harshad in exactly
\[
\tau(p-1)+1
\]
bases: the \(\tau(p-1)\) Moran bases above, plus the exceptional base
\[
B=p^2,
\]
where
\[
p^2=10_B
\]
has digit sum \(1\).

## Assumptions and scope
For an integer base \(B\ge2\), write \(S_B(n)\) for the sum of the base-\(B\) digits of \(n\).

A base-\(B\) Harshad number is a positive integer \(n\) satisfying
\[
S_B(n)\mid n.
\]
A base-\(B\) Moran number is a Harshad number for which
\[
n/S_B(n)
\]
is prime.

The theorem concerns prime squares \(p^2\) only in their two-digit regime
\[
p<B\le p^2.
\]
It does not classify smaller bases \(B\le p\), where \(p^2\) can have three or more digits.

## Proof
Write the two-digit expansion as
\[
p^2=aB+b,
\]
with
\[
1\le a<B,\qquad 0\le b<B.
\]
Because \(B>p\),
\[
a=\left\lfloor\frac{p^2}{B}\right\rfloor<p.
\]

Suppose first that \(p^2\) is Moran. Then
\[
\frac{p^2}{a+b}
\]
is prime. Since the only prime divisor of \(p^2\) is \(p\), necessarily
\[
a+b=p.
\]
Substituting \(b=p-a\) into the digit expansion gives
\[
p^2=aB+p-a,
\]
hence
\[
p(p-1)=a(B-1).
\]
Now \(1\le a<p\) and \(p\) is prime, so
\[
\gcd(a,p)=1.
\]
Therefore \(a\mid p-1\). Put
\[
d=\frac{p-1}{a}.
\]
Then
\[
B-1=pd,
\]
or
\[
B=pd+1,
\]
with \(d\mid p-1\).

Conversely, let \(d\mid p-1\), and set
\[
a=\frac{p-1}{d},
\qquad
B=pd+1,
\qquad
b=p-a.
\]
Because \(1\le d\le p-1\),
\[
p<B=pd+1\le p(p-1)+1<p^2.
\]
Also
\[
0\le b<p<B.
\]
A direct calculation gives
\[
aB+b
=
\frac{p-1}{d}(pd+1)
+
p-\frac{p-1}{d}
=
p^2.
\]
Thus the base-\(B\) digit sum is
\[
a+b=p,
\]
and the quotient is the prime \(p\). This proves the Moran classification. Distinct divisors \(d\mid p-1\) give distinct bases, so there are exactly
\[
\tau(p-1)
\]
such bases.

For the Harshad statement, if \(p^2\) is Harshad then
\[
a+b\mid p^2.
\]
Hence
\[
a+b\in\{1,p,p^2\}.
\]
The case
\[
a+b=p^2
\]
is impossible, because subtracting \(a+b=p^2\) from \(aB+b=p^2\) yields
\[
a(B-1)=0.
\]
If
\[
a+b=p,
\]
the preceding argument gives exactly the Moran bases.

Finally,
\[
a+b=1
\]
forces
\[
a=1,\qquad b=0,
\]
so
\[
B=p^2.
\]
Conversely, in base \(p^2\) one has \(p^2=10_B\), which is Harshad but not Moran because the quotient is \(p^2\), not a prime.

## Verification
The accompanying checker exhaustively verifies the theorem for every prime
\[
p\le500.
\]
For each such prime it tests every base
\[
p<B\le p^2
\]
directly from the two base-\(B\) digits, compares the observed Moran bases with
\[
\{pd+1:d\mid p-1\},
\]
and compares the observed Harshad bases with that set together with \(p^2\).

The checker also verifies the asserted digit formula for every predicted Moran base. These finite checks corroborate the algebraic proof; they are not used to establish the infinite theorem.

## Relationship to prior work
Witno studies decimal Niven numbers whose quotient by the decimal digit sum is prime, the class now commonly called Moran numbers. The paper explicitly notes that Niven numbers are commonly studied in bases other than \(10\), but its constructions and tables are decimal. Its subject classification is headed by \(11A63\).

An exact public implementation of Moran numbers with an arbitrary radix parameter appeared in the Math-NumSeq distribution. This verifies that the base-dependent Moran notion itself was already in public use; the release date of version \(55\) is 23 October 2012.

The decimal OEIS entry A001101 records Moran numbers and cites the earlier literature, but does not state a prime-square base spectrum.

The result here does not claim the definitions of Harshad or Moran numbers as new. Its content is the complete two-digit classification of the bases in which a fixed prime square is Harshad or Moran, together with the exact counts
\[
\tau(p-1)+1
\quad\text{and}\quad
\tau(p-1).
\]

## Limitations
The theorem does not classify bases
\[
B\le p,
\]
where \(p^2\) may have three or more digits and the digit-sum equation no longer reduces to one linear relation.

The oldest inspected mathematical paper on this Moran-type condition is dated only to June 2010, without an exact public calendar day in the inspected copy. To avoid inventing a day, the metadata uses the earliest exact public release date verified here, 23 October 2012, from the arbitrary-radix implementation.

A short equivalent observation may exist in unindexed recreational or digit-sum literature; no such statement was found in the targeted database, exact-sequence, implementation, and web searches used here.

## References
1. A. Witno, “Numbers Which Factor as Their Digital Sum Times a Prime”, *International Journal of Open Problems in Computer Science and Mathematics* 3(2) (2010), 132–136.
2. Math::NumSeq::MoranNumbers, Math-NumSeq version 55, public release 23 October 2012; the documented `radix` parameter gives the base-dependent Moran predicate.
3. OEIS Foundation, A001101, “Moran numbers: \(k\) such that \(k\)/(sum of digits of \(k\)) is prime.”
