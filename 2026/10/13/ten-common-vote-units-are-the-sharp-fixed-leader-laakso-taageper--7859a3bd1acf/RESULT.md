# Ten common vote units are the sharp fixed-leader Laakso–Taagepera–Golosov ranking boundary
## Finding
Represent a party system by a nonincreasing positive-integer profile
\[
x_1\ge x_2\ge\cdots\ge x_k>0,
\qquad
N=\sum_i x_i.
\]

Compare only systems having the same total \(N\), the same actual party count \(k\), and the same leading-party count \(x_1\). Put
\[
p_i=\frac{x_i}{N}.
\]

The Laakso–Taagepera effective number is
\[
N_{LT}=\frac{1}{\sum_i p_i^2},
\]
and the Golosov effective number is
\[
N_G=\sum_i\frac{p_i}{p_i+p_1^2-p_i^2}.
\]

For every positive-integer profile with
\[
N\le9,
\]
the two indices induce the same weak ordering under these controls.

At
\[
N=10,
\]
a strict reversal appears for the first time. The complete first layer consists of exactly one unordered pair:
\[
(4,4,2)
\quad\text{versus}\quad
(4,3,3).
\]

Both systems have three parties and the same leading-party share
\[
p_1=\frac25.
\]

Laakso–Taagepera gives
\[
N_{LT}(4,4,2)=\frac{25}{9}
<
\frac{50}{17}=N_{LT}(4,3,3),
\]
so it regards \((4,3,3)\) as more fragmented.

Golosov gives
\[
N_G(4,4,2)=\frac{21}{8}
>
\frac{97}{37}=N_G(4,3,3),
\]
so it regards \((4,4,2)\) as more fragmented. The reversal is exact but narrow:
\[
\frac{21}{8}-\frac{97}{37}=\frac{1}{296}.
\]

## Assumptions and scope
All party counts are strictly positive integers and profiles are identified up to relabeling, so they are written in nonincreasing order.

The comparison fixes total votes or seats, the actual number of represented parties, and the size of the largest party. This deliberately removes differences caused merely by a different number of components or a different dominant-party share.

Higher values of either index are interpreted as greater effective party-system fragmentation.

The theorem is a finite-resolution result. It does not claim that the ten-unit profile is empirically typical, nor that either index is normatively preferable.

## Proof
For an integer profile, the Laakso–Taagepera index has the exact form
\[
N_{LT}
=
\frac{N^2}{\sum_i x_i^2}.
\]

For the Golosov index,
\[
N_G
=
\sum_i
\frac{x_iN}{x_iN+x_1^2-x_i^2}.
\]
Thus every comparison on the finite integer grid is rational and requires no floating-point approximation.

For the first profile,
\[
(4,4,2),
\]
we have
\[
N_{LT}
=
\frac{100}{16+16+4}
=
\frac{25}{9},
\]
and
\[
N_G
=
1+1+\frac{20}{20+16-4}
=
\frac{21}{8}.
\]

For the second profile,
\[
(4,3,3),
\]
we have
\[
N_{LT}
=
\frac{100}{16+9+9}
=
\frac{50}{17},
\]
and
\[
N_G
=
1+2\frac{30}{30+16-9}
=
\frac{97}{37}.
\]

The opposite inequalities follow by exact cross multiplication:
\[
25\cdot17=425<450=50\cdot9,
\]
while
\[
21\cdot37=777>776=97\cdot8.
\]

For sharpness, enumerate every positive integer partition of each total \(N\) from \(2\) through \(10\), discard the one-party partition, and group the remaining profiles by the pair \((k,x_1)\). Only profiles in the same group are comparable under the theorem's controls.

The numbers of admissible profiles for totals \(2,3,\ldots,10\) are
\[
1,2,4,6,10,14,21,29,41,
\]
and the corresponding numbers of same-\((k,x_1)\) unordered comparisons are
\[
0,0,0,0,0,1,2,5,11.
\]
Exact comparison finds no weak-order disagreement through total nine and exactly one disagreement at total ten, the pair above. Since it is strict in opposite directions, the same computation proves both minimality and completeness of the first layer.

Finally, multiplying every count by a common positive integer leaves every share \(p_i\) unchanged. Hence the reversal persists for
\[
(4q,4q,2q)
\quad\text{versus}\quad
(4q,3q,3q)
\]
for every positive integer \(q\).

## Verification
The embedded `verify_effective_party_boundary.py` uses exact `Fraction` arithmetic only.

It constructs every integer partition through total ten in two independent ways: a recursive nonincreasing-partition generator and a combinations-with-replacement generator. The two profile sets are asserted equal before any metric comparison.

It then groups profiles by common party count and common leading-party count, compares every unordered pair under both indices, checks the profile and pair-count census, proves absence of any weak disagreement through total nine, and verifies that the unique total-ten reversal is exactly
\[
(4,4,2)
\quad\text{versus}\quad
(4,3,3).
\]

Run:

`python3 verify_effective_party_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Laakso and Taagepera introduced the effective-number construction and selected the quadratic member
\[
N_{LT}=\frac{1}{\sum_i p_i^2}
\]
as their preferred practical measure. Their formulation interprets the effective number as the number of equally sized hypothetical parties producing the same degree of fragmentation.

Golosov later proposed a different effective-number index after arguing that the Laakso–Taagepera measure can be misleading, especially in party systems dominated by a large component. His full derivation gives
\[
N_G=\sum_i\frac{p_i}{p_i+p_1^2-p_i^2},
\]
and explicitly compares the two indices on multiple hypothetical and empirical party constellations.

That literature establishes that the two measures can assign different numerical effective-party counts and motivates comparing their behavior. The result here is narrower: it identifies the smallest common integer resolution at which they can reverse an ordinal fragmentation comparison even when both the actual party count and the leading-party share are held fixed, and it classifies the entire first reversal layer.

Targeted searches using both index names, fixed leading-party share, common party count, ranking reversal, and the exact profiles did not locate this finite boundary.

## Limitations
The integer total \(N\) should be read as a common vote/seat resolution, not as a claim that real elections have only ten voters or seats.

The first reversal is numerically small under Golosov's index, with gap \(1/296\). Its value is structural: it proves an ordinal distinction after the leading-party share and the actual number of parties have already been controlled.

The result does not establish how frequently such reversals occur in empirical election data and does not assess which effective-number index is substantively superior.

## References
1. M. Laakso and R. Taagepera, “Effective Number of Parties: A Measure with Application to West Europe,” *Comparative Political Studies* 12(1), 3–27, first published 1 April 1979. DOI: 10.1177/001041407901200101.
2. G. V. Golosov, “The Effective Number of Parties: A New Approach,” *Party Politics* 16(2), 171–192, first published online 10 September 2009. DOI: 10.1177/1354068809339538.
3. S. L. Feld and B. Grofman, “The Laakso-Taagepera Index in a Mean and Variance Framework,” *Journal of Theoretical Politics* 19(1), 101–106, 2007. DOI: 10.1177/0951629807071021.
