# Positive-kappa accuracy reversal first occurs at ten binary cases
## Finding
Consider a binary diagnostic classification problem with a fixed reference standard. There are
\[
P
\]
reference-positive cases and
\[
Q=N-P
\]
reference-negative cases.

For a classifier, write
\[
x=TP,
\qquad
P-x=FN,
\qquad
y=TN,
\qquad
Q-y=FP.
\]
Assume every cell is positive:
\[
1\le x\le P-1,
\qquad
1\le y\le Q-1.
\]

Raw accuracy is
\[
A=\frac{x+y}{N}.
\]
Cohen's kappa against the reference labels is
\[
\kappa=\frac{p_o-p_e}{1-p_e},
\]
where
\[
p_o=A
\]
and the expected agreement from the two marginal label frequencies is
\[
p_e
=
\frac{PM+Q(N-M)}{N^2},
\]
with
\[
M=x+Q-y
\]
the classifier's predicted-positive count.

Restrict attention to classifiers with
\[
\kappa>0.
\]
This removes below-chance tables and asks for a genuine disagreement between two positive agreement summaries.

For every
\[
N\le9,
\]
no two all-positive-cell classifiers having the same reference prevalence can be ranked in opposite strict orders by accuracy and Cohen's kappa.

At
\[
N=10,
\]
strict reversal occurs for the first time. Up to exchanging the positive and negative class labels, the unique first pair has
\[
P=3,
\qquad
Q=7.
\]

Classifier \(X\) has
\[
(TP,FN,TN,FP)=(1,2,5,2).
\]
Therefore
\[
A(X)=\frac{6}{10}=\frac35,
\qquad
\kappa(X)=\frac1{21}.
\]

Classifier \(Y\) has
\[
(TP,FN,TN,FP)=(2,1,3,4).
\]
Therefore
\[
A(Y)=\frac{5}{10}=\frac12,
\qquad
\kappa(Y)=\frac2{27}.
\]

Hence
\[
A(X)>A(Y)
\]
but
\[
\kappa(X)<\kappa(Y).
\]

The phenomenon is structural. For every integer
\[
N\ge10,
\]
keep
\[
P=3
\]
and define
\[
X_N=(TP,FN,TN,FP)=(1,2,N-5,2),
\]
\[
Y_N=(TP,FN,TN,FP)=(2,1,N-7,4).
\]
All four cells remain positive. Then
\[
A(X_N)=\frac{N-4}{N}
>
\frac{N-5}{N}=A(Y_N),
\]
while
\[
\kappa(X_N)
=
\frac{N-9}{3(N-3)}
<
\frac{4(N-9)}{9(N-4)}
=
\kappa(Y_N).
\]

## Assumptions and scope
The two classifiers are compared on samples with the same total size and the same reference prevalence. Their item-by-item error overlap need not be specified because each metric depends only on its own confusion table.

Every confusion-matrix cell is positive. This excludes deterministic one-class predictors and zero-cell edge cases.

Both kappas are positive. The sharp boundary therefore does not rely on a negative-kappa classifier being overtaken by a merely chance-level classifier.

Accuracy means observed agreement with the reference labels. Cohen's kappa is used as a chance-corrected agreement statistic. This does not assert that kappa is always the preferred measure of diagnostic performance; sensitivity and specificity answer different questions.

The finite cutoff is an exact small-sample structural statement, not a recommendation to estimate agreement reliably from ten observations.

## Proof
Let
\[
Q=N-P
\]
and let
\[
M=x+Q-y
\]
be the predicted-positive count.

Cohen's definition gives
\[
\kappa
=
\frac{p_o-p_e}{1-p_e}
\]
with
\[
p_o=\frac{x+y}{N}
\]
and
\[
p_e
=
\frac{PM+Q(N-M)}{N^2}.
\]
A direct simplification yields the exact integer-rational form
\[
\kappa
=
\frac{2(Qx+Py-PQ)}{P(N-M)+QM}.
\]
The denominator is positive for every nondegenerate binary table, so
\[
\kappa>0
\quad\Longleftrightarrow\quad
Qx+Py>PQ.
\]

For the finite boundary, exhaust all integers
\[
4\le N\le10,
\qquad
2\le P\le \left\lfloor\frac N2\right\rfloor,
\]
where restricting to
\[
P\le Q
\]
quotients the global exchange of positive and negative class labels. For each prevalence, exhaust
\[
1\le x\le P-1,
\qquad
1\le y\le Q-1,
\]
retain exactly the tables with positive kappa, and compare every unordered pair having the same \(P\).

The numbers of positive-kappa tables in this class-normalized domain for
\[
N=4,5,6,7,8,9,10
\]
are
\[
0,
1,
2,
5,
9,
13,
22.
\]
The corresponding numbers of strict accuracy-kappa reversals are
\[
0,
0,
0,
0,
0,
0,
1.
\]
Thus the displayed pair is the unique first reversal up to class-label exchange.

For the infinite family with \(P=3\), classifier \(X_N\) has predicted-positive count
\[
M_X=3,
\]
so its predicted prevalence equals the reference prevalence. Substitution gives
\[
\kappa(X_N)
=
\frac{N-9}{3(N-3)}.
\]
Classifier \(Y_N\) has
\[
M_Y=6,
\]
and substitution gives
\[
\kappa(Y_N)
=
\frac{4(N-9)}{9(N-4)}.
\]
For
\[
N\ge10,
\]
both are positive. After cancelling the common positive factor \(N-9\), the kappa inequality is equivalent to
\[
12(N-3)>9(N-4),
\]
which reduces to
\[
3N>0.
\]
So the reversal persists for every \(N\ge10\).

## Verification
The embedded `verify_accuracy_kappa_minimal_reversal.py` uses only the Python standard library and exact `Fraction` arithmetic.

For every admissible table it computes kappa in two independent forms:
- directly from observed and chance-expected agreement;
- from the closed rational expression
  \[
  \frac{2(Qx+Py-PQ)}{P(N-M)+QM}.
  \]

It exhausts every positive-cell table through the first boundary, retains exactly those with positive kappa, and compares every pair with the same reference prevalence.

It verifies the normalized-domain table counts
\[
0,1,2,5,9,13,22
\]
and strict-reversal counts
\[
0,0,0,0,0,0,1.
\]

It also verifies the exact witness values and the structural family for every integer
\[
10\le N\le500
\]
as a consistency check. The all-\(N\) family itself is proved algebraically above.

Run:

`python3 verify_accuracy_kappa_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Cohen introduced kappa specifically because raw observed agreement does not account for agreement expected from the marginal category frequencies. His original article defines
\[
\kappa=\frac{p_o-p_e}{1-p_e}
\]
and emphasizes that marginal disagreement can constrain attainable agreement.

Cicchetti and Feinstein later analyzed the well-known kappa paradoxes in binary concordance tables. They explain that raw agreement and kappa can move differently when marginal totals and positive-versus-negative agreement are imbalanced, and they argue that the paradoxical adjustments can be scientifically meaningful rather than merely defective arithmetic.

That literature establishes the mechanism and the practical reason to report more than one agreement summary. The result here asks a sharper finite question under deliberately nondegenerate conditions: with fixed reference prevalence, all four cells positive, and both kappas positive, what is the smallest sample on which raw accuracy and kappa can make opposite strict comparative judgments?

Targeted searches using accuracy, observed agreement, Cohen kappa, fixed prevalence, positive kappa, rank reversal, smallest sample, and exact confusion-table values did not locate the ten-case boundary, its uniqueness up to class-label exchange, or the persistent family above.

## Limitations
The theorem treats binary tables only.

The comparison fixes the reference prevalence but allows the predicted-positive margins of the two classifiers to differ; this is precisely where kappa's chance correction can change the ranking.

The all-cell-positive and positive-kappa restrictions are substantive domain choices designed to exclude degenerate reversals. Removing them permits smaller disagreements.

Kappa is an agreement statistic, not a complete diagnostic-accuracy analysis. Sensitivity, specificity, predictive values, calibration, and decision consequences remain outside the claim.

An unindexed exercise, software test, or specialized agreement-methods note could contain the same ten-case pair even though the sharp boundary statement was not located.

## References
1. J. Cohen, “A Coefficient of Agreement for Nominal Scales,” *Educational and Psychological Measurement* 20(1), 37–46, first published 1 April 1960. DOI: 10.1177/001316446002000104.
2. D. V. Cicchetti and A. R. Feinstein, “High Agreement but Low Kappa: II. Resolving the Paradoxes,” *Journal of Clinical Epidemiology* 43(6), 551–558, 1990. DOI: 10.1016/0895-4356(90)90159-M.
