# Three parties are the sharp Loosemore–Hanby–Gallagher ranking boundary
## Finding
Let
\[
v=(v_1,\ldots,v_k),\qquad s=(s_1,\ldots,s_k)
\]
be positive vote and seat shares with
\[
\sum_i v_i=\sum_i s_i=1,
\]
and define the discrepancy vector
\[
d_i=s_i-v_i.
\]

The Loosemore–Hanby index is
\[
L=\frac12\sum_i |d_i|,
\]
while the Gallagher least-squares index is
\[
G=\sqrt{\frac12\sum_i d_i^2}.
\]

With two parties the indices are identical. Indeed,
\[
d=(x,-x)
\]
forces
\[
L=|x|=G.
\]
Hence two-party elections can never be ranked in opposite strict orders by the two measures.

Three parties are sharp. Up to relabeling parties and swapping the roles of votes and seats, every nonzero three-party discrepancy vector can be written
\[
d=(a,b,-a-b),\qquad a,b\ge0.
\]
Put
\[
\ell=a+b,
\qquad
h=|a-b|.
\]
Then
\[
L=\ell
\]
and
\[
G^2=\frac{3\ell^2+h^2}{4}.
\]
Thus, at fixed Loosemore–Hanby disproportionality, Gallagher additionally records how concentrated the over- or under-representation is between the two parties on the same side of proportionality.

For two three-party elections \(A\) and \(B\) with
\[
L_A<L_B,
\]
a strict Gallagher reversal occurs exactly when
\[
3L_A^2+h_A^2>3L_B^2+h_B^2.
\]
Since
\[
0\le h\le L,
\]
every three-party election satisfies the sharp band
\[
\frac{\sqrt3}{2}L\le G\le L.
\]
Consequently, for prescribed positive Loosemore–Hanby values with
\[
L_A<L_B,
\]
some three-party discrepancy vectors can reverse their Gallagher ranking if and only if
\[
\frac{L_A}{L_B}>\frac{\sqrt3}{2}.
\]
The upper edge is attained when one party is represented exactly proportionally, while the lower edge is attained when the two parties on the same side of proportionality have equal discrepancies.

There is also a sharp positive integer-grid boundary. Suppose both vote shares and seat shares are integer multiples of
\[
\frac1N,
\]
and every party has at least one vote unit and one seat unit. Then no strict Loosemore–Hanby–Gallagher ranking reversal occurs for
\[
N\le10.
\]
At
\[
N=11,
\]
reversal first appears. Among the \(217\) realizable labeled discrepancy vectors, there are exactly \(36\) reversing unordered pairs, and every one is generated, up to party permutation and swapping votes with seats, by the two discrepancy shapes
\[
(7,-7,0)
\]
and
\[
(-8,4,4).
\]

A positive-count witness is
\[
v^A=\frac1{11}(1,8,2),
\qquad
s^A=\frac1{11}(8,1,2),
\]
and
\[
v^B=\frac1{11}(9,1,1),
\qquad
s^B=\frac1{11}(1,5,5).
\]
For election \(A\),
\[
L_A=G_A=\frac7{11}.
\]
For election \(B\),
\[
L_B=\frac8{11},
\qquad
G_B=\frac{4\sqrt3}{11}.
\]
Therefore
\[
L_A<L_B
\]
but
\[
G_A>G_B.
\]

## Assumptions and scope
Vote shares and seat shares are nonnegative vectors with common total one. The structural three-party theorem allows zero discrepancies but assumes the shares themselves can be chosen positive; sufficiently small scaling of any admissible discrepancy shape around an interior vote vector realizes that condition.

The integer-grid corollary is stricter: both vote and seat shares must lie on the same denominator-\(N\) grid and every party must receive at least one unit of votes and one unit of seats. The number \(N\) is therefore a granularity parameter, not a claim that real elections have equal numbers of voters and legislative seats.

Only opposite strict rankings are considered. Equality under one measure with separation under the other is not a reversal.

The theorem compares two disproportionality summaries, not electoral systems themselves. A lower index value does not by itself establish that an electoral rule is normatively preferable.

## Proof
Because
\[
\sum_i d_i=0,
\]
a two-party discrepancy vector has the form
\[
(x,-x).
\]
Hence
\[
L=\frac12(|x|+|-x|)=|x|
\]
and
\[
G=\sqrt{\frac12(x^2+x^2)}=|x|.
\]
This proves the two-party obstruction.

For three parties, any nonzero zero-sum discrepancy vector has either one positive and two nonpositive entries or two nonnegative and one negative entry. Multiplying by \(-1\) corresponds to swapping votes and seats and leaves both indices unchanged. After that sign choice and a permutation, write
\[
d=(a,b,-a-b),\qquad a,b\ge0.
\]
Then
\[
L=\frac12(a+b+a+b)=a+b=\ell.
\]
Also
\[
G^2
=\frac12\left(a^2+b^2+(a+b)^2\right).
\]
Since
\[
a^2+b^2=\frac{(a+b)^2+(a-b)^2}{2},
\]
we obtain
\[
G^2=\frac{3\ell^2+h^2}{4},
\qquad h=|a-b|.
\]
The exact reversal criterion follows immediately by comparing these squares.

Because
\[
0\le h\le\ell,
\]
we have
\[
\frac{3\ell^2}{4}
\le G^2\le
\ell^2,
\]
which is equivalent to
\[
\frac{\sqrt3}{2}L\le G\le L.
\]
If \(L_A<L_B\) and \(G_A>G_B\), then necessarily
\[
L_A\ge G_A>G_B\ge\frac{\sqrt3}{2}L_B,
\]
so
\[
\frac{L_A}{L_B}>\frac{\sqrt3}{2}.
\]
Conversely, if this strict inequality holds, choose an extreme shape with
\[
h_A=L_A
\]
and a balanced shape with
\[
h_B=0.
\]
Then
\[
G_A=L_A
\]
and
\[
G_B=\frac{\sqrt3}{2}L_B,
\]
so the ranking reverses. Scaling both discrepancy vectors sufficiently small makes them realizable by positive vote and seat shares.

For the common-denominator corollary, the verifier exhausts every ordered positive integer vote composition and every ordered positive integer seat composition of \(N\) into three parties. It deduplicates the induced discrepancy vectors and compares every unordered pair exactly. The numbers of realizable labeled discrepancy vectors for
\[
N=3,4,\ldots,11
\]
are
\[
1,7,19,37,61,91,127,169,217.
\]
The exact reversal counts are
\[
0,0,0,0,0,0,0,0,36.
\]
Canonicalization under global sign and party permutation shows that all \(36\) first-layer pairs have the single shape pair displayed above. This proves the denominator-\(11\) boundary and its first-layer classification.

## Verification
The embedded `verify_lh_gallagher_three_party_boundary.py` uses only the Python standard library and exact rational arithmetic.

It verifies the two-party identity over a finite family of integer discrepancies as a replay of the analytic proof, checks the three-party structural identity
\[
G^2=\frac{3L^2+h^2}{4}
\]
on more than ten thousand integer pairs \((a,b)\), and performs the complete positive common-denominator census through \(N=11\).

For each denominator it enumerates every positive composition of \(N\) into three vote counts and every positive composition into three seat counts, forms all realizable discrepancy vectors, and compares every unordered pair without floating-point arithmetic.

Run:

`python3 verify_lh_gallagher_three_party_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Loosemore and Hanby introduced their absolute-deviation index for electoral distortion. Gallagher later reviewed that index in detail and proposed the least-squares measure
\[
G=\sqrt{\frac12\sum_i(s_i-v_i)^2}.
\]
His primary paper explicitly states that when there are only two parties the least-squares and Loosemore–Hanby indices take the same value. It also motivates least squares by its stronger response to a few large discrepancies than to many small ones, and reports that different disproportionality measures can change empirical election rankings.

Later index-comparison work proves the general pointwise inequality
\[
G\le L,
\]
with equality exactly when there is one overrepresented and one underrepresented party. That inequality does not determine whether two elections can be ranked in opposite orders, nor the smallest number of parties at which that can occur.

The present result turns the qualitative distinction into a sharp structural boundary. Two parties force identity. Three parties admit the exact band
\[
\frac{\sqrt3}{2}L\le G\le L,
\]
an exact reversal criterion, and a sharp positive rational-grid threshold.

Targeted searches using both index names, least-squares and absolute-deviation aliases, ranking-reversal language, three-party language, and exact-grid terminology did not locate this theorem or the denominator-\(11\) first layer.

## Limitations
Prior literature already establishes that the indices differ, that Gallagher penalizes concentrated discrepancies more strongly, and that different disproportionality measures can change empirical rankings. The new claim is only the sharp two-versus-three-party boundary, the exact three-party geometry, and the common-denominator first layer.

The denominator-\(11\) statement depends on the artificial but mathematically transparent requirement that vote and seat shares use the same positive integer grid. Its value is as a finite benchmark, not as a literal model of electorate and legislature sizes.

The result does not compare Gallagher with ratio-based disproportionality measures such as Sainte-Laguë, and it does not identify a universally preferred normative measure.

An unindexed exercise, implementation test, or specialist note could contain an equivalent three-party construction even though the sharp boundary and exact grid classification were not located.

## References
1. J. Loosemore and V. J. Hanby, “The Theoretical Limits of Maximum Distortion: Some Analytic Expressions for Electoral Systems,” *British Journal of Political Science* 1(4), 467–477, October 1971. DOI: 10.1017/S000712340000925X.
2. M. Gallagher, “Proportionality, Disproportionality and Electoral Systems,” *Electoral Studies* 10(1), 33–51, 1991. DOI: 10.1016/0261-3794(91)90004-C.
3. G. Borisyuk, C. Rallings and M. Thrasher, “Selecting Indexes of Electoral Proportionality: General Properties and Relationships,” *Quality & Quantity* 38(1), 51–74, 2004. DOI: 10.1023/B:QUQU.0000013239.55304.98.
4. J. M. Marín, J. A. Moreno-Ternero and M. A. Montes-Rojas, “A New Quota Approach to Electoral Disproportionality,” *Economies* 7(1), 17, 2019. DOI: 10.3390/economies7010017.
