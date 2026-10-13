# Twelve market units are the sharp HHI–Hall–Tideman strict-reversal boundary
## Finding
Consider a market with
\[
k\ge2
\]
firms, strictly positive integer firm sizes, and total market size
\[
N.
\]
Firm labels are ignored.

Let
\[
s_i=\frac{n_i}{N}
\]
be market shares. The Herfindahl–Hirschman index is
\[
H=\sum_{i=1}^k s_i^2.
\]

For the Hall–Tideman index, rank firms from largest to smallest, so the largest firm has rank \(1\). If
\[
d_1\ge d_2\ge\cdots\ge d_k
\]
are the integer firm sizes in descending order, then
\[
\mathrm{HTI}
=
\frac{1}{2\sum_{i=1}^k i(d_i/N)-1}
=
\frac{N}{2\sum_{i=1}^k i d_i-N}.
\]

For every
\[
N\le9,
\]
the two indices induce the same weak concentration ordering on every profile set with common \(k\) and common \(N\).

At
\[
N=10,
\]
weak-order agreement first fails, but only through a tie:
\[
(1,4,5)
\quad\text{and}\quad
(2,2,6)
\]
have equal Hall–Tideman index
\[
\frac5{11},
\]
while their HHI values are
\[
\frac{21}{50}<\frac{11}{25}.
\]

No opposite strict ranking occurs for
\[
N\le11.
\]

At
\[
N=12,
\]
strict reversal appears for the first time. Across all possible firm counts there is exactly one unordered reversing pair up to firm permutation:
\[
(1,2,4,5)
\quad\text{versus}\quad
(2,2,2,6).
\]

Their HHI values are
\[
\frac{23}{72}<\frac13,
\]
while their Hall–Tideman values are
\[
\frac6{17}>\frac13.
\]

Thus HHI ranks
\[
(2,2,2,6)
\]
as more concentrated, while Hall–Tideman ranks
\[
(1,2,4,5)
\]
as more concentrated.

## Assumptions and scope
Every firm has strictly positive integer size. Profiles are compared only when the firm count \(k\) and total market size \(N\) are both fixed.

The Hall–Tideman convention used here assigns rank \(1\) to the largest firm. Tied firm sizes may be placed in either order because equal sizes contribute the same total to the rank-weighted sum.

The theorem concerns concentration rankings, not welfare, competition policy thresholds, or market definition.

The total \(N\) is a discrete resolution parameter. Common scaling of a profile preserves both HHI and Hall–Tideman, so the integer cutoff is not an absolute economic-size threshold for continuously divisible market shares.

## Proof
At fixed total
\[
N,
\]
HHI is
\[
H
=
\frac{1}{N^2}\sum_i n_i^2.
\]

Define
\[
Q(n)=\sum_i n_i^2.
\]
At fixed \(N\), HHI therefore increases exactly with the integer \(Q\).

For Hall–Tideman, sort the profile in descending order
\[
d_1\ge\cdots\ge d_k
\]
and define the rank sum
\[
R(n)=\sum_{i=1}^k i d_i.
\]

Then
\[
\mathrm{HTI}
=
\frac{N}{2R(n)-N}.
\]
At fixed \(N\), Hall–Tideman therefore decreases exactly with the integer \(R\).

A strict ranking reversal occurs precisely when \(Q\) and \(R\) move in the same direction: the larger \(Q\) profile has the larger \(R\), so HHI rises while Hall–Tideman falls.

Every unlabeled positive-integer market profile of total \(N\) and firm count \(k\) is an integer partition of \(N\) into exactly \(k\) parts.

The verifier generates each fixed-\((k,N)\) profile set in two independent ways: directly as nondecreasing integer partitions, and from all positive ordered compositions followed by sorting and deduplication. The two generators agree at every layer.

Aggregated over all firm counts, the numbers of profiles for
\[
N=2,\ldots,12
\]
are
\[
1,2,4,6,10,14,21,29,41,55,76.
\]

The numbers of unordered within-\((k,N)\) profile pairs are
\[
0,0,1,2,7,13,30,56,109,190,354,
\]
for a cumulative total of
\[
762
\]
comparisons.

There is no weak-order disagreement through \(N=9\). At \(N=10\), the unique disagreement is the tie-splitting pair
\[
(1,4,5)
\quad\text{and}\quad
(2,2,6),
\]
with
\[
Q=42,\ 44
\]
and
\[
R=16,\ 16.
\]

There is no strict reversal through \(N=11\).

At \(N=12\), exactly one strict reversal occurs:
\[
a=(1,2,4,5),
\qquad
b=(2,2,2,6).
\]

Their integer invariants are
\[
Q(a)=46<48=Q(b)
\]
and
\[
R(a)=23<24=R(b).
\]

Therefore HHI ranks \(b\) higher in concentration, whereas Hall–Tideman, which decreases with \(R\), ranks \(a\) higher. Substitution gives the exact values stated above.

## Verification
The embedded `verify_hhi_hti_boundary.py` uses only the Python standard library and exact integer or rational arithmetic.

It enumerates every admissible profile for
\[
2\le N\le12,\qquad 2\le k\le N,
\]
using two independent generators and checks all
\[
762
\]
within-\((k,N)\) unordered profile pairs.

It verifies:
\[
\text{weak-order agreement for }N\le9,
\]
the unique tie split at \(N=10\),
\[
\text{no strict reversal for }N\le11,
\]
and exactly the stated strict reversal at \(N=12\).

Run:

`python3 verify_hhi_hti_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Hall and Tideman introduced a concentration measure that incorporates the ranks of all firms and compared it analytically and empirically with established concentration measures including Herfindahl.

Bikker and Haaf review HHI and Hall–Tideman together. Their treatment makes the structural distinction explicit: HHI weights firms by their own market shares, while Hall–Tideman uses firm ranks and is designed to reflect the number of firms as well as relative position in the size distribution.

Anbarci and Katzman likewise discuss HHI as a standard concentration index and Hall–Tideman as an alternative with different weighting structure.

Those sources establish that HHI and Hall–Tideman are distinct and need not have identical numerical behavior. The claim here is narrower: under common firm count, common total, and positive integer firm sizes, it identifies the exact first weak disagreement, the exact first strict reversal, and the complete strict-reversal layer at the sharp total.

Targeted searches using both index names, the Rosenbluth alias, fixed-total integer profiles, ranking-reversal language, and the exact witness profiles did not locate this finite boundary.

## Limitations
The twelve-unit cutoff belongs to the positive-integer grid and is not a scale-dependent antitrust threshold.

The theorem does not classify all reversals for larger totals or continuously divisible market shares.

The original Hall–Tideman article was available through abstract and bibliographic records in the checked route, but a verified full article PDF was not obtained after open-access and authorized institutional attempts. Its formula and interpretation were therefore independently checked in later full-text literature, and no whole-document noncoverage claim is made for the original article.

An unindexed exercise, spreadsheet, or software test could contain one of the small profile pairs even though the sharp boundary was not located in the checked literature.

## References
1. M. Hall and N. Tideman, “Measures of Concentration,” *Journal of the American Statistical Association* 62, 162–168, 1967. DOI: 10.1080/01621459.1967.10482897.
2. J. A. Bikker and K. Haaf, “Measures of Competition and Concentration in the Banking Industry: a Review of the Literature,” *Economic & Financial Modelling* 9, 53–98, 2002.
3. N. Anbarci and B. Katzman, “A New Industry Concentration Index,” *Economic Papers* 34, 222–228, 2015. DOI: 10.1111/1759-3441.12122.
