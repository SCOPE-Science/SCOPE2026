# Exhaustive doubling two-cycles of the square-digit happy map
## Finding
For an integer base \(b\ge2\), let \(S_b(n)\) be the sum of the squares of the base-\(b\) digits of \(n\). Suppose \(X\) and \(2X\) are both two-digit base-\(b\) integers and satisfy
\[
S_b(X)=2X
\]
and
\[
S_b(2X)=X.
\]
Then there is a unique integer \(t\ge1\) for which
\[
b=5t+3,
\]
\[
X=t b+(3t+2),
\]
and
\[
2X=(2t+1)b+(t+1).
\]

Conversely, for every integer \(t\ge1\), these formulas give a two-cycle of \(S_b\). Thus the familiar family in bases
\[
b\equiv3\pmod5
\]
is not merely a construction: it is the complete family of two-digit square-digit two-cycles whose larger member is exactly twice the smaller.

## Assumptions and scope
For \(n=\sum_i d_i b^i\) with digits \(0\le d_i<b\), define
\[
S_b(n)=\sum_i d_i^2.
\]
A two-cycle means two distinct positive integers \(X,Y\) with
\[
S_b(X)=Y,\qquad S_b(Y)=X.
\]

The theorem assumes
\[
Y=2X
\]
and that both \(X\) and \(Y\) have exactly two base-\(b\) digits. It does not classify two-cycles with another ratio, or cycles containing a one-digit or three-or-more-digit member.

## Proof
Write
\[
X=ab+c,
\]
where
\[
1\le a<b,\qquad 0\le c<b.
\]
Because \(X\) is two-digit, \(a\ge1\).

First suppose doubling the low digit causes no carry:
\[
2c<b.
\]
Since \(2X\) is also two-digit, its digits are then \(2a,2c\), with \(2a<b\). Hence
\[
S_b(2X)=4a^2+4c^2=4S_b(X)=8X,
\]
contradicting
\[
S_b(2X)=X.
\]
Therefore a carry is necessary:
\[
2c\ge b.
\]

The two digits of \(2X\) are consequently
\[
2a+1,\qquad 2c-b,
\]
and the hypothesis that \(2X\) remains two-digit gives
\[
2a+1<b.
\]
The two cycle equations are
\[
a^2+c^2=2ab+2c
\tag{1}
\]
and
\[
(2a+1)^2+(2c-b)^2=ab+c.
\tag{2}
\]

Subtracting four times (1) from (2) gives
\[
(7b+4)a+(7-4b)c+b^2+1=0,
\]
so, since \(4b-7>0\),
\[
c=\frac{(7b+4)a+b^2+1}{4b-7}.
\]
Substituting this expression into (1) and clearing the positive denominator \((4b-7)^2\) yields
\[
(b^2+1)(5a-b+3)(13a-b+5)=0.
\]
Because \(b^2+1>0\), there are two algebraic branches.

If
\[
b=5a+3,
\]
the displayed linear formula for \(c\) gives
\[
c=3a+2.
\]
This branch is compatible with the required carry, since
\[
2c-b=a+1>0.
\]

If
\[
b=13a+5,
\]
the same formula gives
\[
c=5a+2.
\]
But then
\[
2c=10a+4<13a+5=b,
\]
contradicting the already proved necessity of a carry. Thus only the first branch survives.

Putting
\[
t=a
\]
gives
\[
b=5t+3,\qquad c=3t+2.
\]
The doubled digits are
\[
2t+1,\qquad 2c-b=t+1,
\]
so
\[
X=t b+(3t+2)
\]
and
\[
2X=(2t+1)b+(t+1).
\]
Since \(a=t\ge1\), one has \(t\ge1\), and \(t\) is unique because it is the leading digit of \(X\).

Conversely, let \(t\ge1\) and set
\[
b=5t+3.
\]
All four displayed digits lie in the required range. Direct calculation gives
\[
t^2+(3t+2)^2
=
10t^2+12t+4
=
(2t+1)b+(t+1)
=
2X,
\]
and
\[
(2t+1)^2+(t+1)^2
=
5t^2+6t+2
=
tb+(3t+2)
=
X.
\]
Thus the formulas indeed produce a two-cycle for every \(t\ge1\).

## Verification
The accompanying checker exhaustively enumerates all bases
\[
2\le b\le400
\]
and every two-digit \(X\) for which \(2X\) is also two-digit. It directly tests
\[
S_b(X)=2X,\qquad S_b(2X)=X
\]
and compares every hit with the theorem's formula.

It separately verifies the constructed family for every
\[
1\le t\le10000.
\]
These finite checks corroborate the algebraic classification. They are not used as a proof of the infinite statement.

## Relationship to prior work
Hargreaves and Siksek study the same generalized happy map and give cycle bounds together with a complete fixed-point count for the square-digit map. Their paper has primary subject classification \(11A63\). The accessible title-page and abstract material does not state the present two-cycle classification.

The public sequence A193585 counts cycles of the square-digit map by base and cites the earlier generalized-happy-number literature. It is a cycle-count table rather than a classification by digit shape or ratio.

Wu, Dang, and Zhang enumerate square-digit periodic points in selected bases. Their table contains the doubling examples
\[
(13,26)
\]
in base \(8\) and
\[
(34,68)
\]
in base \(13\), the first two members of the family above, but it does not derive an all-base converse.

Goedhart, Gurtas, and Harris later give the explicit construction
\[
b=5t+3,\quad
X=(t,3t+2)_b,\quad
Y=(2t+1,t+1)_b
\]
and explicitly note
\[
Y=2X.
\]
Their statement is presented as a formula generating such pairs. The finding here supplies the converse under the natural two-digit and doubling hypotheses: no other base or digit pattern is possible.

## Limitations
The classification is deliberately restricted to two-digit cycles with ratio exactly \(2\). Other two-cycles can occur and are not addressed.

The complete body of the 2010 Hargreaves--Siksek paper was not available through the inspected access path. Its title page, abstract, subject classification, and indexed metadata were available; this incomplete access remains the main literature risk. The full 2025 construction section, the 2015 periodic-point tables, and the public cycle-count database were inspectable.

The earliest older journal sources encountered during comparison are dated only to a year or month in the accessible metadata. To avoid inventing a calendar day, the structured date uses the earliest exact public date verified among the inspected archival sources, the 31 July 2011 creation date of A193585.

## References
1. K. Hargreaves and S. Siksek, “Cycles and Fixed Points of Happy Functions,” *Journal of Combinatorics and Number Theory* 2(3) (2010), 217–229.
2. OEIS Foundation, A193585, “Number of cycles under iteration of sum of squares of digits in base \(b\),” entry authored 31 July 2011.
3. W. Wu, X. Dang, and Y. Zhang, “Periodic Points Under Iteration of Sum of Squares or Cubes of Digits in Some Positional Systems,” IC3ME 2015, doi:10.2991/ic3me-15.2015.327.
4. E. G. Goedhart, Y. Gurtas, and P. E. Harris, “A Tree Approach to the Happy Function,” *La Matematica* 4 (2025), 419–432, doi:10.1007/s44007-025-00157-x.
