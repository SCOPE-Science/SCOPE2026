# Divisor and residue structure of two-digit cubic happy fixed points
## Finding
Let \(S_{3,b}\) denote the sum of the cubes of the base-\(b\) digits. A two-digit integer
\[
N=(a,c)_b=ab+c
\]
is a fixed point of \(S_{3,b}\) precisely when
\[
a^3+c^3=ab+c.
\]

For every trailing digit
\[
c\ge2,
\]
all such fixed points across all integer bases are parametrized exactly by the positive divisors of
\[
c^3-c=c(c-1)(c+1).
\]
More precisely, for every
\[
a\mid c(c-1)(c+1)
\]
there is exactly one base,
\[
b=a^2+\frac{c(c-1)(c+1)}a,
\tag{1}
\]
and \((a,c)_b\) is a two-digit fixed point. Conversely every two-digit cubic fixed point with \(c\ge2\) arises this way. Therefore the exact number with prescribed trailing digit \(c\) is
\[
\tau(c^3-c).
\tag{2}
\]

There is a complementary periodic description for a prescribed leading digit. Fix
\[
a\ge2
\]
and write
\[
a=2^e m,\qquad m\text{ odd}.
\]
Then the admissible trailing digits are exactly those satisfying
\[
a\mid c(c-1)(c+1).
\tag{3}
\]
Modulo \(a\), the number of admissible residue classes is
\[
R(a)=r(e)3^{\omega(m)},
\tag{4}
\]
where
\[
r(0)=1,\qquad r(1)=2,\qquad r(2)=3,\qquad r(e)=5\quad(e\ge3).
\]
Consequently the set of nonnegative trailing digits producing a two-digit cubic fixed point with leading digit \(a\) has natural density
\[
\frac{R(a)}a.
\tag{5}
\]

The boundary trailing digits form two simple rays:
\[
c=0\quad\text{or}\quad c=1
\]
gives
\[
b=a^2
\]
for every \(a\ge2\).

As a visible infinite subfamily, choosing \(c=a\ge2\) yields the repdigit fixed point
\[
(a,a)_{\,2a^2-1}.
\]

## Assumptions and scope
For an integer base \(b\ge2\), define
\[
S_{3,b}\!\left(\sum_i d_i b^i\right)=\sum_i d_i^3.
\]
A fixed point is a positive integer \(N\) satisfying
\[
S_{3,b}(N)=N.
\]

The theorem classifies exactly the fixed points having two base-\(b\) digits, while allowing the base itself to vary. It does not classify three-or-more-digit fixed points or nontrivial periodic cycles.

The leading digit satisfies
\[
1\le a<b,
\]
and the trailing digit satisfies
\[
0\le c<b.
\]

## Proof
Let
\[
N=(a,c)_b=ab+c.
\]
The fixed-point equation is
\[
a^3+c^3=ab+c.
\]
Rearranging gives
\[
a(b-a^2)=c^3-c=c(c-1)(c+1).
\tag{6}
\]

Suppose first that
\[
c\ge2.
\]
Then the right side of (6) is positive. Equation (6) implies
\[
a\mid c(c-1)(c+1)
\]
and forces the base to be exactly
\[
b=a^2+\frac{c(c-1)(c+1)}a.
\]
This proves necessity and uniqueness of the base for a given digit pair.

Conversely, take any \(c\ge2\) and any positive divisor
\[
a\mid c(c-1)(c+1),
\]
and define \(b\) by (1). The fixed-point equation follows immediately from (6). It remains only to check that \(a,c\) are valid digits.

If \(a>c\), then
\[
b\ge a^2>a>c.
\]
If \(a\le c\), then
\[
\frac{c(c-1)(c+1)}a
\ge
\frac{c(c-1)(c+1)}c
=c^2-1,
\]
so
\[
b\ge a^2+c^2-1>c
\]
and also \(b>a\). Thus every positive divisor gives a valid two-digit fixed point. Distinct divisors give distinct leading digits, hence distinct fixed points. This proves (2).

Now fix \(a\ge2\). By (6), a nonnegative trailing digit is admissible exactly when (3) holds, and the resulting base is then uniquely determined. The condition depends only on \(c\bmod a\), so it remains to count the solution classes.

For an odd prime power \(p^f\), the three integers
\[
c-1,\quad c,\quad c+1
\]
are pairwise coprime with respect to \(p\). Hence
\[
p^f\mid c(c-1)(c+1)
\]
holds exactly when
\[
c\equiv-1,0,1\pmod{p^f}.
\]
There are exactly three residue classes.

For powers of \(2\), direct valuation gives a different local count. If \(c\) is even, then \(c-1\) and \(c+1\) are odd, so
\[
2^e\mid c(c-1)(c+1)
\]
requires
\[
c\equiv0\pmod{2^e}.
\]
If \(c\) is odd, then one of \(c-1,c+1\) is divisible by \(4\) and the other has exact \(2\)-adic valuation \(1\). For \(e\ge3\), the condition is therefore equivalent to
\[
c\equiv\pm1\pmod{2^{e-1}},
\]
which gives four odd residue classes modulo \(2^e\). Together with the even class \(0\), this gives five classes. The small exponents give respectively
\[
2,\quad3
\]
classes for \(e=1,2\). This proves the values of \(r(e)\).

The Chinese remainder theorem now multiplies the local counts, giving
\[
R(a)=r(e)3^{\omega(m)}.
\]
Because admissibility is periodic modulo \(a\), its natural density is \(R(a)/a\), proving (5).

Finally, if \(c=0\) or \(c=1\), then \(c^3-c=0\), and (6) gives
\[
b=a^2.
\]
This is a valid base precisely for \(a\ge2\), producing the two boundary rays.

## Verification
The accompanying checker performs three independent finite comparisons.

First, for every base
\[
2\le b\le500,
\]
it enumerates all two-digit pairs and tests
\[
a^3+c^3=ab+c
\]
directly. Every observed pair is checked against formula (1).

Second, for every
\[
2\le c\le250,
\]
it enumerates all positive divisors of \(c^3-c\), constructs the predicted base from (1), verifies the digit bounds and fixed-point equation, and checks that the count is exactly
\[
\tau(c^3-c).
\]

Third, for every
\[
2\le a\le500,
\]
it enumerates the residues modulo \(a\) satisfying (3) and compares the count with (4).

These calculations corroborate the algebraic classification. The theorem itself is proved for all admissible integers by the divisor and Chinese-remainder arguments above.

## Relationship to prior work
Hargreaves and Siksek study the same generalized happy functions
\[
S_{e,b}
\]
and prove general cycle bounds. Their exact fixed-point enumeration specializes to the square-digit map \(S_{2,b}\); their abstract and title material state this exponent-\(2\) result explicitly, with primary subject classification \(11A63\).

Wu, Dang, and Zhang study square- and cube-digit dynamics in selected positional systems. Their full cubic section enumerates fixed and periodic points in bases \(2\) through \(16\). For example, it records the cubic fixed points
\[
9=(12)_7,\qquad16=(22)_7,
\]
and
\[
35=(32)_{11},
\]
which are the \(c=2\), \(a=1,2,3\) instances of formula (1). Their result is a finite base-by-base census, not a varying-base divisor classification.

The public sequence A193594 counts attractors of the cubic digit map by base and links the generalized-happy-number literature. It provides an exact archive of finite-base dynamics but does not parameterize two-digit fixed points across bases.

Thus the present result complements fixed-base enumeration by reversing the viewpoint: the digits are the arithmetic parameters, and the allowable base is forced by a divisor of three consecutive integers.

## Limitations
The classification is restricted to fixed points having exactly two digits. It does not count all cubic fixed points in a fixed base and does not address nontrivial cycles.

The divisor formula itself follows from one rearrangement of the fixed-point equation; the additional structural content is that every divisor is automatically digit-valid for \(c\ge2\), together with the exact divisor count and the prime-power/Chinese-remainder law for a fixed leading digit.

The full selected-base cubic census of Wu, Dang, and Zhang was inspected, including its cubic tables. The Hargreaves--Siksek exact fixed-point theorem concerns exponent \(2\), as stated in its accessible primary text. An equivalent varying-base parametrization could still occur in unindexed perfect-digital-invariant literature.

## References
1. K. Hargreaves and S. Siksek, “Cycles and Fixed Points of Happy Functions,” *Journal of Combinatorics and Number Theory* 2(3) (2010), 217–229.
2. OEIS Foundation, A193594, “Number of attractors under iteration of sum of cubes of digits in base \(b\),” authored 31 July 2011.
3. W. Wu, X. Dang, and Y. Zhang, “Periodic Points Under Iteration of Sum of Squares or Cubes of Digits in Some Positional Systems,” IC3ME 2015, doi:10.2991/ic3me-15.2015.327.
