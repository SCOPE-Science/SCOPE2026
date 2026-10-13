# No two-digit doubling two-cycle for the cubic happy map
## Finding
For an integer base \(b\ge2\), let
\[
S_{3,b}(n)
\]
denote the sum of the cubes of the base-\(b\) digits of \(n\).

There is no positive integer \(X\) such that both \(X\) and \(2X\) have exactly two base-\(b\) digits and
\[
S_{3,b}(X)=2X,
\qquad
S_{3,b}(2X)=X.
\]

Equivalently, the cubic digit-sum map has no two-cycle of the form
\[
X\longleftrightarrow 2X
\]
whose two members are both two-digit in the same base.

## Assumptions and scope
Write
\[
X=ab+c,
\]
with
\[
1\le a<b,\qquad 0\le c<b.
\]
The hypothesis that both \(X\) and \(2X\) have exactly two base-\(b\) digits means
\[
b\le X<2X<b^2.
\]

The result concerns exponent \(3\), exact ratio \(2\), and the two-digit stratum. It makes no claim about cubic happy-map two-cycles of another ratio or about doubling cycles involving a member with three or more digits.

## Proof
Suppose first that doubling the lower digit causes no carry:
\[
2c<b.
\]
Because \(2X<b^2\), doubling also leaves the leading digit below \(b\), so the base-\(b\) digits of \(2X\) are
\[
2a,\quad 2c.
\]
Therefore
\[
S_{3,b}(2X)
=
(2a)^3+(2c)^3
=
8(a^3+c^3)
=
8S_{3,b}(X).
\]
The first cycle equation gives
\[
S_{3,b}(X)=2X,
\]
so the preceding identity becomes
\[
S_{3,b}(2X)=16X,
\]
contradicting the second cycle equation
\[
S_{3,b}(2X)=X.
\]
Thus a carry is necessary:
\[
2c\ge b.
\]

Now use only the first cycle equation. Since
\[
2X<b^2,
\]
we have
\[
a=\left\lfloor\frac{X}{b}\right\rfloor<\frac b2.
\]
Hence
\[
a\le \frac{b-1}{2}.
\]
Also
\[
c\le b-1.
\]
From
\[
a^3+c^3=2X=2ab+2c
\]
we obtain
\[
c^3
=
2ab+2c-a^3
\le
2ab+2c
\le
b(b-1)+2(b-1)
=
b^2+b-2.
\]
The forced carry gives
\[
c\ge\frac b2,
\]
and therefore
\[
\frac{b^3}{8}\le c^3\le b^2+b-2.
\tag{1}
\]

For every real \(b\ge9\),
\[
b^3-8b^2-8b+16>0.
\]
Indeed its value at \(b=9\) is \(25\), and its derivative
\[
3b^2-16b-8
\]
is positive for \(b\ge9\). Thus
\[
\frac{b^3}{8}>b^2+b-2
\]
for every integer \(b\ge9\), contradicting (1).

It remains to check
\[
2\le b\le8.
\]
For each of these bases we enumerate exactly the digit pairs
\[
1\le a<b,\qquad 0\le c<b
\]
for which both \(X=ab+c\) and \(2X\) are two-digit. There are only \(68\) such pairs in total. The exact finite certificate is:

\[
\begin{array}{c|c|c}
b & \text{admissible pairs }(a,c) & \text{solutions of }a^3+c^3=2(ab+c)\\
\hline
2&0&\varnothing\\
3&2&\varnothing\\
4&4&\varnothing\\
5&8&\varnothing\\
6&12&\varnothing\\
7&18&\varnothing\\
8&24&\{(3,3)\}
\end{array}
\]

For the sole survivor,
\[
b=8,\qquad X=3\cdot8+3=27,
\]
and indeed
\[
S_{3,8}(27)=3^3+3^3=54=2X.
\]
But
\[
2X=54=(66)_8,
\]
so
\[
S_{3,8}(54)=6^3+6^3=432\ne27.
\]
Hence no base remains.

## Verification
The accompanying `verify.py` independently reproduces the finite certificate. It enumerates every admissible two-digit digit pair for
\[
2\le b\le8,
\]
checks both cycle equations directly from the digits, and asserts that the unique solution of the first equation is
\[
(b,a,c,X)=(8,3,3,27),
\]
which fails the second equation.

The same program also checks the analytic cutoff inequality for a wide integer range as a corroborative test. The infinite exclusion for
\[
b\ge9
\]
comes from the displayed proof, not from that finite test.

## Relationship to prior work
Hargreaves and Siksek define the general happy functions \(S_{e,b}\), prove general bounds on periodic points, and treat the square-digit fixed-point problem in detail. Their paper has primary subject classification \(11A63\).

Wu, Dang, and Zhang give explicit finite-base censuses for iteration of sums of squares and cubes of digits. Their cubic table covers bases \(2\) through \(16\). In particular it records no cubic two-cycle in bases \(2\) through \(6\) or base \(8\), while base \(7\) has four cubic two-cycles, none of ratio \(2\). Their work is a finite-base census and does not state an arbitrary-base obstruction to a doubling two-cycle.

The public sequence A193594 records the number of attractors for the cubic digit map by base and cites the generalized-happy-number literature. It counts attractors rather than classifying a ratio inside a two-cycle.

For exponent \(2\), later work gives an infinite family of two-digit two-cycles with the larger member exactly twice the smaller. The cubic result here is a contrasting rigidity statement: under the same digit-length and ratio constraints, exponent \(3\) admits none.

## Limitations
The theorem does not rule out cubic two-cycles of ratios other than \(2\), and it does not address a hypothetical doubling two-cycle in which at least one member has three or more digits.

The finite part of the proof is an exhaustive check of only \(68\) explicitly delimited digit pairs. It is independently reproducible from the attached checker and certificate.

The 2010 Hargreaves--Siksek publication is earlier than the dated database entry used in the structured metadata, but the inspected publication evidence gives only year/month-level public dating rather than a verified calendar day. To avoid inventing a day, the metadata uses the exact 31 July 2011 public date of A193594.

## References
1. K. Hargreaves and S. Siksek, “Cycles and Fixed Points of Happy Functions,” *Journal of Combinatorics and Number Theory* 2(3) (2010), 217–229.
2. OEIS Foundation, A193594, “Number of attractors under iteration of sum of cubes of digits in base \(b\),” authored 31 July 2011.
3. W. Wu, X. Dang, and Y. Zhang, “Periodic Points Under Iteration of Sum of Squares or Cubes of Digits in Some Positional Systems,” IC3ME 2015, doi:10.2991/ic3me-15.2015.327.
4. E. G. Goedhart, Y. Gurtas, and P. E. Harris, “A Tree Approach to the Happy Function,” *La Matematica* 4 (2025), 419–432, doi:10.1007/s44007-025-00157-x.
