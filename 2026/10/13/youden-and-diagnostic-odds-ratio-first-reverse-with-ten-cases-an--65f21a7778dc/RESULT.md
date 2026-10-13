# Youden and diagnostic odds ratio first reverse with ten cases and ten controls
## Finding
Consider a binary diagnostic test evaluated on a balanced case-control sample with exactly
\[
m
\]
diseased subjects and
\[
m
\]
controls.

Write the \(2\times2\) table as
\[
(TP,FN,TN,FP)
=
(a,m-a,d,m-d),
\]
and assume every cell is positive:
\[
1\le a,d\le m-1.
\]

Youden's index is
\[
J
=
\mathrm{sensitivity}
+
\mathrm{specificity}
-
1
=
\frac{a+d-m}{m}.
\]

The diagnostic odds ratio is
\[
\mathrm{DOR}
=
\frac{TP\cdot TN}{FP\cdot FN}
=
\frac{ad}{(m-a)(m-d)}.
\]

Restrict to positively discriminating tests,
\[
J>0,
\]
equivalently
\[
a+d>m.
\]
For positive cells this is also equivalent to
\[
\mathrm{DOR}>1.
\]

No pair of such tests is ranked in opposite strict orders by \(J\) and \(\mathrm{DOR}\) for
\[
m\le9.
\]

At
\[
m=10,
\]
strict reversal occurs for the first time. There are
\[
36
\]
positively discriminating tables, and exactly
\[
6
\]
unordered pairs reverse.

A simple witness is
\[
X=(TP,FN,TN,FP)=(3,7,9,1)
\]
and
\[
Y=(6,4,7,3).
\]

Their Youden indices are
\[
J(X)=\frac15
<
\frac3{10}
=
J(Y).
\]

Their diagnostic odds ratios are
\[
\mathrm{DOR}(X)
=
\frac{3\cdot9}{1\cdot7}
=
\frac{27}{7},
\]
while
\[
\mathrm{DOR}(Y)
=
\frac{6\cdot7}{3\cdot4}
=
\frac72.
\]

Thus Youden's index ranks \(Y\) higher, but the diagnostic odds ratio ranks \(X\) higher.

The reversal is structural rather than isolated. For every integer
\[
m\ge10,
\]
define
\[
X_m=(3,m-3,m-1,1)
\]
and
\[
Y_m=(6,m-6,m-3,3).
\]
Then
\[
J(X_m)=\frac2m
<
\frac3m
=
J(Y_m),
\]
whereas
\[
\mathrm{DOR}(X_m)
=
\frac{3(m-1)}{m-3}
>
\frac{2(m-3)}{m-6}
=
\mathrm{DOR}(Y_m).
\]

## Assumptions and scope
The theorem concerns binary diagnostic tests with a binary reference standard.

The study design is balanced: the number of diseased subjects equals the number of controls. This removes sample-prevalence imbalance from the comparison and focuses entirely on how the two global discrimination summaries aggregate sensitivity and specificity.

Every confusion-matrix cell is positive, so the diagnostic odds ratio is finite without a continuity correction.

Only positively discriminating tables are compared:
\[
J>0.
\]
This is equivalent, under the stated assumptions, to
\[
\mathrm{DOR}>1.
\]

The cutoff is a finite integer-sample boundary. It is not a recommendation to evaluate real diagnostic tests on samples this small.

## Proof
Let
\[
s=a+d.
\]
Then
\[
J=\frac{s-m}{m},
\]
so at fixed \(m\), Youden's ranking is exactly the ranking by
\[
s=TP+TN.
\]

For the diagnostic odds ratio, set
\[
p=ad.
\]
Because
\[
(m-a)(m-d)
=
m^2-ms+p,
\]
we have
\[
\mathrm{DOR}
=
\frac{p}{p-m(s-m)}.
\]

On the positively discriminating region
\[
s>m,
\]
the constant
\[
m(s-m)
\]
is positive. Therefore, for fixed \(s\), the diagnostic odds ratio is strictly decreasing in
\[
p=ad.
\]

This gives the mechanism behind reversal. At a fixed Youden level, a more imbalanced sensitivity-specificity pair has a smaller product \(ad\) and hence a larger diagnostic odds ratio.

For any fixed
\[
s>m,
\]
the maximum diagnostic odds ratio occurs at the most imbalanced feasible pair,
\[
(a,d)
=
(m-1,s-m+1)
\]
up to exchange, while the minimum occurs at the most balanced feasible pair,
\[
(a,d)
=
\left(
\left\lfloor\frac{s}{2}\right\rfloor,
\left\lceil\frac{s}{2}\right\rceil
\right).
\]

The finite lower bound is then an exact lattice comparison. The verifier enumerates every pair
\[
1\le a,d\le m-1,\qquad a+d>m,
\]
for
\[
2\le m\le10.
\]
The numbers of admissible tables are
\[
0,1,3,6,10,15,21,28,36,
\]
and the corresponding strict-reversal counts are
\[
0,0,0,0,0,0,0,0,6.
\]
Thus no strict reversal exists through \(m=9\), and \(m=10\) is sharp.

For the infinite family,
\[
X_m=(a,d)=(3,m-1)
\]
has
\[
J(X_m)=\frac2m
\]
and
\[
\mathrm{DOR}(X_m)
=
\frac{3(m-1)}{m-3}.
\]

The second table
\[
Y_m=(a,d)=(6,m-3)
\]
has
\[
J(Y_m)=\frac3m
\]
and
\[
\mathrm{DOR}(Y_m)
=
\frac{2(m-3)}{m-6}.
\]

Cross multiplication gives
\[
\mathrm{DOR}(X_m)>\mathrm{DOR}(Y_m)
\]
exactly when
\[
3(m-1)(m-6)
>
2(m-3)^2,
\]
which reduces to
\[
m(m-9)>0.
\]
Hence the reversal holds for every integer
\[
m\ge10.
\]

## Verification
The embedded `verify_youden_dor_minimal_reversal.py` uses only the Python standard library and exact rational arithmetic.

For every balanced study size through the first boundary it:
- generates every positive-cell table;
- retains exactly the tables with positive Youden discrimination;
- computes \(J\) both directly from sensitivity and specificity and from the reduced formula;
- computes \(\mathrm{DOR}\) directly from all four confusion-matrix cells;
- verifies that \(J>0\) is equivalent to \(\mathrm{DOR}>1\);
- compares every unordered pair exactly;
- verifies the fixed-\(J\) diagnostic-odds-ratio extrema used in the proof.

The exact strict-reversal counts for
\[
m=2,\ldots,10
\]
are
\[
0,0,0,0,0,0,0,0,6.
\]

The replay also verifies the explicit family for every
\[
10\le m\le500
\]
as a finite consistency check. The all-\(m\) family is proved algebraically above.

Run:

`python3 verify_youden_dor_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Youden introduced his index specifically to reduce a diagnostic-test \(2\times2\) table to one objective performance number. In the original paper,
\[
J
=
\mathrm{sensitivity}
+
\mathrm{specificity}
-
1,
\]
and the index is explicitly independent of the relative sizes of diseased and control groups.

Glas and coauthors later presented the diagnostic odds ratio as another single, prevalence-independent indicator for comparing diagnostic tests. Their paper places Youden's index and the diagnostic odds ratio side by side among global test-performance summaries, gives
\[
\mathrm{DOR}
=
\frac{TP\cdot TN}{FP\cdot FN},
\]
and notes that the diagnostic odds ratio rises steeply as sensitivity or specificity approaches perfection.

A later review likewise treats Youden's index and the diagnostic odds ratio as distinct global measures of diagnostic discrimination. It emphasizes that Youden's index can assign the same value to tests with substantially different sensitivity and specificity.

Those sources establish the measures and the reason their aggregation behavior can differ. The inspected literature does not state the balanced finite-sample ordering theorem above, the sharp ten-cases-ten-controls threshold, the six-pair first layer, or the explicit all-\(m\) reversal family.

Targeted searches using Youden, diagnostic odds ratio, ranking reversal, balanced sensitivity and specificity, competing diagnostic tests, and exact finite confusion-matrix language did not locate those statements.

## Limitations
The sharp cutoff assumes equal numbers of diseased subjects and controls.

The theorem excludes zero cells rather than applying a continuity correction to the diagnostic odds ratio.

The finite boundary concerns integer confusion matrices and strict ranking reversal, not sampling uncertainty or statistical significance of a difference between tests.

Both Youden's index and the diagnostic odds ratio collapse sensitivity and specificity into one number. Clinical choice between tests can require asymmetric consequences for false negatives and false positives, which neither global ranking captures.

An unindexed exercise, software test, or specialist methodological note could contain the same small-table witness even though the sharp boundary theorem was not located.

## References
1. W. J. Youden, “Index for rating diagnostic tests,” *Cancer* 3(1), 32–35, 1950. DOI: 10.1002/1097-0142(1950)3:1<32::AID-CNCR2820030106>3.0.CO;2-3.
2. A. S. Glas, J. G. Lijmer, M. H. Prins, G. J. Bonsel and P. M. M. Bossuyt, “The diagnostic odds ratio: a single indicator of test performance,” *Journal of Clinical Epidemiology* 56(11), 1129–1135, 2003. DOI: 10.1016/S0895-4356(03)00177-X.
3. A.-M. Šimundić, “Measures of Diagnostic Accuracy: Basic Definitions,” *EJIFCC* 19(4), 203–211, 2009. PMCID: PMC4975285.
