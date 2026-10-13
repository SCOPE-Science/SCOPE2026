# Seven excess market units are the sharp HHI–entropy reversal boundary
## Finding
Fix an integer
\[
k\ge3
\]
and consider markets with exactly \(k\) firms, each holding a positive integer number of common market units:
\[
n_1,\ldots,n_k\ge1,
\qquad
\sum_{i=1}^k n_i=N.
\]

Write
\[
r=N-k
\]
for the number of units left after assigning one mandatory unit to every firm.

The Herfindahl concentration index is
\[
H_2
=
\sum_{i=1}^k
\left(\frac{n_i}{N}\right)^2.
\]

The entropy index is
\[
E
=
-\sum_{i=1}^k
\frac{n_i}{N}
\log\left(\frac{n_i}{N}\right).
\]
Entropy varies inversely with concentration, so a smaller \(E\) means a more concentrated market.

For every fixed
\[
k\ge3,
\]
no two positive-integer markets receive opposite strict concentration rankings from \(H_2\) and \(E\) when
\[
r\le6.
\]

At
\[
r=6,
\]
the two indices can cease to induce the same weak order because a Herfindahl tie can be split by entropy, but strict reversal is still impossible.

At
\[
r=7,
\]
strict reversal appears for the first time. Up to permutation of firm labels, the first reversing pair is unique:
\[
A=(\underbrace{1,\ldots,1}_{k-2},4,5)
\]
and
\[
B=(\underbrace{1,\ldots,1}_{k-3},2,2,6).
\]

Both have total size
\[
N=k+7.
\]

Their Herfindahl numerators are
\[
\sum_i n_i^2
=
k+39
\]
for \(A\) and
\[
\sum_i n_i^2
=
k+41
\]
for \(B\). Hence
\[
H_2(A)<H_2(B),
\]
so Herfindahl says \(B\) is more concentrated.

For entropy, fixed \(N\) gives the exact identity
\[
E
=
\log N
-
\frac1N
\log\left(\prod_i n_i^{n_i}\right).
\]

The two products are
\[
\prod_i n_i^{n_i}
=
4^4 5^5
=
800000
\]
for \(A\) and
\[
\prod_i n_i^{n_i}
=
2^2 2^2 6^6
=
746496
\]
for \(B\). Therefore
\[
E(A)<E(B),
\]
so entropy says \(A\) is more concentrated.

Thus the two concentration measures make opposite strict judgments exactly seven excess units above the one-unit-per-firm floor.

For three firms, the sharp witness is
\[
A=(1,4,5),
\qquad
B=(2,2,6),
\]
on a common ten-unit market grid.

## Assumptions and scope
The result compares markets with the same fixed number of firms and the same total market size.

Every firm has a strictly positive integer market size. The integer units can represent any common indivisible accounting unit, such as customers, contracts, or standardized capacity blocks, provided all markets being compared use the same unit.

Firm labels do not matter; profiles are compared up to permutation.

The entropy logarithm base is irrelevant to ranking because changing bases multiplies entropy by a positive constant.

The theorem is about ordinal concentration ranking. It does not assert that either index is economically preferable in a particular antitrust or industrial-organization application.

## Proof
Write
\[
n_i=1+y_i,
\qquad
y_i\ge0,
\qquad
\sum_i y_i=r.
\]

For fixed \(k\) and \(r\),
\[
\sum_i n_i^2
=
\sum_i(1+y_i)^2
=
k+2r+\sum_i y_i^2.
\]
Therefore Herfindahl ranking depends only on
\[
Q(y)=\sum_i y_i^2.
\]

For entropy,
\[
E
=
-\sum_i \frac{n_i}{N}\log\frac{n_i}{N}
=
\log N
-
\frac1N\sum_i n_i\log n_i.
\]
Hence, at fixed \(N\), entropy decreases strictly with
\[
W(y)
=
\prod_i(1+y_i)^{1+y_i}.
\]

Zero excess coordinates contribute neither to \(Q\) nor to \(W\). Consequently the problem for all values of \(k\) reduces to ordinary integer partitions of the excess total \(r\).

The verifier enumerates every partition of
\[
r=0,1,\ldots,7
\]
and compares every unordered pair using the exact integer quantities \(Q\) and \(W\).

The strict-reversal counts are
\[
0,0,0,0,0,0,0,1.
\]

Thus no strict reversal is possible through six excess units.

At six excess units there are Herfindahl ties split by entropy. One universal example, available for every \(k\ge3\), comes from excess partitions
\[
(3,3)
\]
and
\[
(1,1,4).
\]
They satisfy
\[
Q=18
\]
on both sides, while
\[
W(3,3)=4^4 4^4=65536
\]
and
\[
W(1,1,4)=2^2 2^2 5^5=50000.
\]

At seven excess units there is exactly one reversing pair of excess partitions:
\[
(3,4)
\]
and
\[
(1,1,5).
\]
For these,
\[
Q(3,4)=25<27=Q(1,1,5),
\]
but
\[
W(3,4)=800000>746496=W(1,1,5).
\]
This gives the displayed universal first-layer pair after padding with zero excess coordinates, equivalently with unit-size firms.

For two firms no strict reversal is possible at any resolution. Writing the larger market share as
\[
p\in\left[\frac12,1\right],
\]
Herfindahl is
\[
p^2+(1-p)^2,
\]
which increases with \(p\), while binary entropy
\[
-p\log p-(1-p)\log(1-p)
\]
decreases with \(p\). Thus they induce exactly the same concentration ordering.

## Verification
The embedded `verify_hhi_entropy_excess_boundary.py` uses only exact integer arithmetic.

It enumerates every integer partition of each excess total
\[
0\le r\le7
\]
and compares every unordered pair using
\[
Q(y)=\sum_i y_i^2
\]
for Herfindahl ordering and
\[
W(y)=\prod_i(1+y_i)^{1+y_i}
\]
for entropy ordering.

It verifies strict-reversal counts
\[
0,0,0,0,0,0,0,1.
\]

It verifies that the unique first reversing excess pair is
\[
(1,1,5)
\]
versus
\[
(3,4).
\]

It separately reconstructs fixed-\(k\) profiles and checks the theorem for every
\[
3\le k\le100.
\]
That finite replay is only a consistency check: the proof for all \(k\ge3\) follows because zero excess coordinates leave both exact comparison quantities unchanged.

Run:

`python3 verify_hhi_entropy_excess_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Hart's classical study treats entropy as a business-concentration measure and compares information-theoretic concentration with other statistical and traditional concentration measures.

Acar and Sankaran explicitly compare the Herfindahl index and the entropy measure, including their decomposability and inversion properties. Their analysis confirms that the two indices encode concentration differently; the existence of different mathematical behavior is therefore prior work.

Bikker and Haaf give a full side-by-side treatment of concentration indices in banking. They describe HHI as a benchmark summary concentration measure,
\[
H_2=\sum_i s_i^2,
\]
and entropy as
\[
E=-\sum_i s_i\log s_i,
\]
with entropy varying inversely with concentration. Their full text also emphasizes that HHI places relatively greater weight on larger firms, while entropy attaches logarithmic weights.

These sources establish the two measures, their economic interpretation, and their differing weighting structures. They do not state the fixed-firm positive-integer theorem above: six excess units permit only tie splitting, seven are necessary and sufficient for strict reversal, and the first reversing pair is unique up to firm permutation.

Targeted searches using Herfindahl, entropy, ranking reversal, fixed firm count, integer market shares, excess units, the exact profiles, and majorization language did not locate this boundary.

## Limitations
The sharp threshold is for positive integer market units and fixed firm count.

If zero-share firms are permitted, they are economically absent and should normally be removed before fixing the number of firms.

If market shares are treated as arbitrary real numbers rather than a common integer grid, three firms already suffice for strict reversal; the ten-unit three-firm witness displayed here is one rational example.

The theorem concerns ranking by concentration measures, not welfare, market power, merger legality, or pricing behavior.

The full text of Hart's 1971 article was not available through the checked lawful routes; its journal summary was inspected. The full Bikker–Haaf article and the detailed Acar–Sankaran abstract were inspected and provide the direct formula and comparison evidence used here.

An unindexed teaching exercise or specialist concentration note could contain the same small integer witness even though the universal excess-unit boundary was not located.

## References
1. P. E. Hart, “Entropy and Other Measures of Concentration,” *Journal of the Royal Statistical Society, Series A* 134(1), 73–85, 1971. DOI: 10.2307/2343975.
2. W. Acar and K. Sankaran, “The myth of the unique decomposability: specializing the Herfindahl and entropy measures?,” *Strategic Management Journal* 20(10), 969–975, first published 28 September 1999. DOI: 10.1002/(SICI)1097-0266(199910)20:10<969::AID-SMJ57>3.0.CO;2-0.
3. J. A. Bikker and K. Haaf, “Measures of Competition and Concentration in the Banking Industry: a Review of the Literature,” *Economic & Financial Modelling* 9, 53–98, 2002.
