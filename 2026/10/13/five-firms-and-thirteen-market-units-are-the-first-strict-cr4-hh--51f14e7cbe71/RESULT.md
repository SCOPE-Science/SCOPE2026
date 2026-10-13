# Five firms and thirteen market units are the first strict CR4–HHI reversal
## Finding
Let a market have positive firm shares
\[
s_1\ge s_2\ge\cdots\ge s_n>0,
\qquad
\sum_i s_i=1.
\]

The four-firm concentration ratio is
\[
CR_4=\sum_{i=1}^{\min(4,n)}s_i,
\]
and the Herfindahl–Hirschman index is
\[
H=\sum_i s_i^2.
\]

For
\[
n\le4,
\]
the concentration ratio is identically
\[
CR_4=1,
\]
so it cannot make a strict comparison at all.

Now restrict to exactly five firms and rational shares. Represent two markets on a common positive-integer scale
\[
a_1+\cdots+a_5
=
b_1+\cdots+b_5
=
S,
\]
with each coordinate positive and the coordinates sorted nonincreasingly.

No strict rank reversal between \(CR_4\) and \(H\) exists for
\[
S\le12.
\]

At
\[
S=13,
\]
strict reversal occurs for the first time, and there are exactly two unordered pairs up to firm permutation:
\[
A=(5,2,2,2,2)
\quad\text{versus}\quad
B=(4,3,3,2,1),
\]
and
\[
A=(5,2,2,2,2)
\quad\text{versus}\quad
C=(3,3,3,3,1).
\]

Their concentration ratios are
\[
CR_4(A)=\frac{11}{13},
\qquad
CR_4(B)=CR_4(C)=\frac{12}{13}.
\]

Their HHI values are
\[
H(A)=\frac{41}{169},
\qquad
H(B)=\frac{39}{169},
\qquad
H(C)=\frac{37}{169}.
\]

Hence \(CR_4\) judges \(B\) and \(C\) more concentrated than \(A\), because each leaves only one thirteenth of the market outside its top four firms. HHI gives the opposite strict judgment because the \(5/13\) leader in \(A\) receives enough quadratic weight to outweigh the larger smallest-firm share.

The boundary is not isolated. For every integer
\[
x\ge5,
\]
define
\[
A_x=(x,2,2,2,2),
\]
\[
B_x=(x-1,3,3,2,1),
\]
and
\[
C_x=(x-2,3,3,3,1).
\]
All three have total
\[
x+8.
\]
Then
\[
CR_4(B_x)>CR_4(A_x),
\qquad
CR_4(C_x)>CR_4(A_x),
\]
but
\[
H(A_x)>H(B_x),
\qquad
H(A_x)>H(C_x).
\]

## Assumptions and scope
All firms have strictly positive market shares.

The finite boundary is stated for rational shares by using a common positive-integer representation. The common scale is only a way to measure rational lattice complexity; changing monetary units by a common factor does not change either concentration measure.

A strict reversal means that one index ranks market \(X\) above market \(Y\) while the other ranks \(Y\) above \(X\). Ties are not counted as reversals.

The result concerns the traditional four-firm concentration ratio and HHI as structural concentration measures. It does not assert that either statistic by itself establishes market power or an antitrust violation.

## Proof
For five firms with integer shares
\[
a_1\ge a_2\ge a_3\ge a_4\ge a_5>0,
\qquad
\sum_i a_i=S,
\]
the normalized indices are
\[
CR_4=\frac{S-a_5}{S}
\]
and
\[
H=\frac{\sum_i a_i^2}{S^2}.
\]

Thus, at fixed \(S\), \(CR_4\) ranks markets only by the negative of their smallest firm, whereas HHI ranks them by the square sum
\[
Q(a)=\sum_i a_i^2.
\]

Suppose market \(A\) is more concentrated by HHI but less concentrated by \(CR_4\) than market \(B\). Then
\[
a_5>b_5.
\]

For
\[
S<10,
\]
no five-firm positive integer profile can have smallest coordinate at least \(2\), so a reversal is impossible.

For
\[
10\le S\le12,
\]
a strict reversal would necessarily compare a profile with minimum at least \(2\) against one with minimum \(1\). Among profiles with minimum at least \(2\), convexity of the square makes the HHI numerator largest when all but one coordinate are as small as possible:
\[
A_{\max}(S)=(S-8,2,2,2,2).
\]
The corresponding numerators are
\[
20,\quad25,\quad32
\]
for \(S=10,11,12\).

Among profiles with minimum \(1\), the square sum is minimized by balancing the remaining four coordinates as evenly as possible. The minimizing profiles are
\[
(3,2,2,2,1),
\]
\[
(3,3,2,2,1),
\]
and
\[
(3,3,3,2,1),
\]
with HHI numerators
\[
22,\quad27,\quad32.
\]

Hence the most HHI-concentrated market having the larger minimum never exceeds the least HHI-concentrated market having minimum \(1\) through \(S=12\). At \(S=12\) the extremal values only tie.

At
\[
S=13,
\]
the unique maximum-HHI profile with minimum at least \(2\) is
\[
(5,2,2,2,2),
\]
with square sum
\[
41.
\]
For a strict reversal, the competing market must have minimum \(1\) and square sum below \(41\). Its other four positive coordinates sum to \(12\). The only four-part partitions of \(12\) with square sum below \(40\) are
\[
(4,3,3,2)
\]
and
\[
(3,3,3,3),
\]
with square sums \(38\) and \(36\). Appending the final \(1\) gives exactly
\[
(4,3,3,2,1)
\]
and
\[
(3,3,3,3,1).
\]
This proves the sharp boundary and the complete equality layer.

For the infinite families,
\[
CR_4(B_x)-CR_4(A_x)
=
CR_4(C_x)-CR_4(A_x)
=
\frac1{x+8}>0.
\]
Using unnormalized square sums,
\[
Q(A_x)-Q(B_x)=2x-8>0
\]
and
\[
Q(A_x)-Q(C_x)=4x-16>0
\]
for every integer \(x\ge5\). The strict reversals therefore persist indefinitely.

## Verification
The embedded `verify_cr4_hhi_minimal_reversal.py` uses only the Python standard library and exact integer arithmetic.

It independently constructs every positive five-part partition of each total
\[
5\le S\le13
\]
in two ways:
- recursive nonincreasing partition generation;
- all positive compositions followed by sorting and deduplication.

The two constructions agree exactly and give partition counts
\[
1,1,2,3,5,7,10,13,18.
\]

The verifier checks every unordered pair and confirms:
- zero strict reversals for \(S=5,\ldots,12\);
- exactly two strict reversals at \(S=13\);
- exactly the two displayed boundary pairs;
- HHI numerators \(41,39,37\) and \(CR_4\) numerators \(11,12,12\);
- the extremal lower-bound comparisons used in the proof;
- both infinite reversal families for \(5\le x\le500\) as a finite consistency check.

The infinite-family statement is proved algebraically above; the finite replay is not a substitute for that proof.

Run:

`python3 verify_cr4_hhi_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
The 1982 U.S. Department of Justice Merger Guidelines explicitly replaced reliance on the traditional four-firm concentration ratio with HHI-based screening. They explain the central structural distinction: unlike the four-firm ratio, HHI reflects the distribution of shares within the leading firms and outside the leading four, and its squaring gives larger firms disproportionate weight.

Miller's 1982 exposition likewise compares \(CR_4\) with HHI and emphasizes the move from the familiar top-four ratio to the full-distribution quadratic index.

Rhoades later gives a concise full-text account of HHI as the sum of squared market shares of all firms and explains why the index gives much heavier weight to large shares.

Sleuwaegen and Dehandschutter's paper, “The Critical Choice between the Concentration Ratio and the H-Index in Assessing Industry Performance,” is the closest located title to the present comparison. Its bibliographic record was inspected, but full text was not accessible through the open sources checked, and an institutional retrieval attempt was unavailable. That access gap remains a literature risk.

The inspected sources establish that the measures can embody different structural information. They do not, in the material available, state the smallest positive-rational five-firm lattice on which the two measures make opposite strict concentration judgments, the exact two boundary pairs, or the displayed infinite families.

## Limitations
The minimum \(S=13\) is a rational lattice-complexity statement, not an assertion that market shares are naturally measured in thirteen physical units.

The result fixes \(CR_4\). Other concentration ratios \(CR_k\) have different finite geometry.

The theorem isolates disagreement between two structural summary statistics. It does not equate a higher index value with a legal conclusion or a complete model of competition.

The inaccessible 1986 concentration-ratio versus H-index paper creates a residual bibliographic risk, although exact-vector and exact-boundary searches did not locate the stated result.

## References
1. U.S. Department of Justice, *1982 Merger Guidelines*, issued 14 June 1982.
2. R. A. Miller, “The Herfindahl-Hirschman Index as a Market Structure Variable: An Exposition for Antitrust Practitioners,” *The Antitrust Bulletin* 27(3), 593–618, 1982. DOI: 10.1177/0003603X8202700302.
3. L. Sleuwaegen and W. Dehandschutter, “The Critical Choice between the Concentration Ratio and the H-Index in Assessing Industry Performance,” *The Journal of Industrial Economics* 35(2), 193–208, 1986.
4. S. A. Rhoades, “The Herfindahl-Hirschman index,” *Federal Reserve Bulletin* 79(3), 188–189, 1993.
