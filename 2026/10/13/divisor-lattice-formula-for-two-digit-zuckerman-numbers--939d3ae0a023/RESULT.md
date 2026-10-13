# Divisor-lattice formula for two-digit Zuckerman numbers
## Finding
For an integer base
\[
b\ge2,
\]
let \(Z_2(b)\) denote the number of base-\(b\) Zuckerman numbers with exactly two digits.

There is an explicit bijection between these numbers and pairs
\[
(d,a)
\]
such that
\[
d\mid b,\qquad d\ge2,
\]
and \(a\) is a proper positive divisor of
\[
d+1.
\]
If
\[
k=\frac{b}{d},
\]
the corresponding two-digit number is
\[
(a,ak)_b.
\]

Therefore
\[
Z_2(b)
=
\sum_{\substack{d\mid b\\d\ge2}}
\bigl(\tau(d+1)-1\bigr).
\tag{1}
\]

Two consequences are immediate:
\[
Z_2(b)\ge\tau(b)-1,
\tag{2}
\]
and for every
\[
b\ge3,
\]
equality in (2) holds if and only if
\[
b=4.
\tag{3}
\]

For a prime base \(p\), (1) reduces to
\[
Z_2(p)=\tau(p+1)-1.
\tag{4}
\]

## Assumptions and scope
A positive integer is a base-\(b\) Zuckerman number when it is divisible by the product of all of its base-\(b\) digits. A positive Zuckerman number cannot contain a zero digit.

Thus an exactly two-digit candidate has the unique form
\[
N=(a,c)_b=ab+c,
\]
with
\[
1\le a,c\le b-1.
\]

The result classifies this complete two-digit stratum for every integer base. It does not give a comparable closed formula for three or more digits.

## Proof
Let
\[
N=ab+c
\]
with
\[
1\le a,c\le b-1.
\]
The Zuckerman condition is
\[
ac\mid ab+c.
\tag{5}
\]

Since the left side of (5) is divisible by \(a\), condition (5) implies
\[
a\mid c.
\]
Write
\[
c=ak
\]
for an integer \(k\ge1\). Then (5) becomes
\[
a^2k\mid a(b+k),
\]
or equivalently
\[
ak\mid b+k.
\tag{6}
\]

Condition (6) implies
\[
k\mid b.
\]
Put
\[
d=\frac{b}{k}.
\]
Then (6) is equivalent to
\[
a\mid d+1.
\tag{7}
\]

The digit bound
\[
c=ak<b=dk
\]
is equivalent to
\[
a<d.
\tag{8}
\]
Since \(a\ge1\), (8) also forces
\[
d\ge2.
\]

Conversely, let
\[
d\mid b,\qquad d\ge2,
\]
put
\[
k=\frac{b}{d},
\]
and let \(a\) be any positive divisor of \(d+1\) satisfying \(a<d\). Set
\[
c=ak.
\]
Then
\[
1\le c<b
\]
and
\[
ak\mid k(d+1)=b+k.
\]
Hence
\[
a^2k\mid a(b+k)=ab+ak,
\]
so
\[
ac\mid ab+c.
\]
Thus \((a,c)_b\) is Zuckerman.

For \(d\ge2\), every proper divisor of \(d+1\) is at most
\[
\frac{d+1}{2}<d.
\]
Therefore condition (8) is automatic for every proper positive divisor \(a\) of \(d+1\). There are exactly
\[
\tau(d+1)-1
\]
such choices.

The correspondence is injective: from the digit pair \((a,c)\), one recovers
\[
k=\frac{c}{a}
\]
and then
\[
d=\frac{b}{k}.
\]
Summing over the nontrivial divisors \(d\) of \(b\) proves (1).

Each summand in (1) is at least \(1\), because
\[
\tau(d+1)\ge2.
\]
There are
\[
\tau(b)-1
\]
divisors \(d\mid b\) with \(d\ge2\), proving (2).

Equality in (2) occurs exactly when
\[
\tau(d+1)=2
\]
for every divisor
\[
d\mid b,\qquad d\ge2;
\]
equivalently, every such \(d+1\) is prime.

Assume now that
\[
b\ge3.
\]
If \(b\) were odd, then \(b+1\) would be an even integer greater than \(2\), hence composite. Therefore equality forces \(b\) to be even.

If \(b\) had an odd divisor
\[
d\ge3,
\]
then \(d+1\) would again be even and greater than \(2\), hence composite. Thus equality forces
\[
b=2^m
\]
for some \(m\ge1\).

If
\[
m\ge3,
\]
then \(8\mid b\), but
\[
8+1=9
\]
is composite. Hence \(m\le2\). Under \(b\ge3\), only
\[
b=4
\]
remains. Conversely, the nontrivial divisors of \(4\) are \(2\) and \(4\), and
\[
3,\ 5
\]
are prime, so equality indeed holds. This proves (3).

If \(p\) is prime, its only divisor at least \(2\) is \(p\), so (4) follows directly from (1).

## Verification
The accompanying checker exhaustively compares the classification with direct digit-product divisibility for every base
\[
2\le b\le500.
\]
For each base it verifies:
\[
\{(a,c):ac\mid ab+c\}
\]
equals the predicted set from divisor pairs \((d,a)\);
the direct count equals formula (1);
the lower bound (2) holds; and, for \(b\ge3\), equality occurs exactly at \(b=4\).

It also verifies the prime-base specialization for every prime base in the same range.

For base \(10\), the formula gives
\[
Z_2(10)=5
\]
and the five numbers are
\[
11,\ 12,\ 15,\ 24,\ 36,
\]
agreeing with the standard decimal sequence database.

The finite checks corroborate the proof; the theorem itself is established by the bijection above.

## Relationship to prior work
He and Sanna define base-\(b\) Zuckerman numbers, study their asymptotic counting function, and provide algorithms for counting and enumeration. Their paper defines the set of exactly \(N\)-digit Zuckerman numbers and reports large computations for bases \(3\) through \(12\). Its primary MSC 2020 classification is \(11A63\).

The inspected full text does not state formula (1): targeted searches for “two digits,” “two-digit,” \(N=2\), and the notation for the two-digit layer produced no matching statement. The algorithms can of course enumerate any fixed finite layer, but they do not supply the divisor-lattice identity above as a theorem.

OEIS A007602 is the standard decimal Zuckerman sequence. Its two-digit members are exactly
\[
11,\ 12,\ 15,\ 24,\ 36.
\]
A later sequence, A397770, records the number of decimal \(n\)-digit Zuckerman numbers and explicitly gives the two-digit count \(5\). These decimal data agree with (1) at \(b=10\) but do not imply the arbitrary-base formula.

## Limitations
The theorem addresses exactly two digits. With three or more digits, the product-divisibility condition no longer collapses to the single divisor relation in (6).

The literature comparison included the full searchable He--Sanna article, the standard decimal sequence, a decimal digit-count sequence, semantic database searches, and direct web searches using both the Zuckerman name and the defining digit-product condition. An equivalent elementary observation could still exist in unindexed recreational literature.

The decimal Zuckerman sequence has older bibliographic ancestry, including a 2005 book citation and its earlier sequence identity, but the inspected evidence did not establish an exact public calendar day for those older appearances. To avoid inventing a date, the structured metadata uses the earliest exact public day verified here: the dated Zuckerman-name comment on A007602 from 9 November 2008.

## References
1. OEIS Foundation, A007602, “Numbers that are divisible by the product of their digits.”
2. Q. He and C. Sanna, “Counting numbers that are divisible by the product of their digits,” arXiv:2403.14812, 2024; later published in *Journal of Number Theory* 272 (2025), 34–59.
3. OEIS Foundation, A397770, “Number of \(n\)-digit Zuckerman numbers.”
