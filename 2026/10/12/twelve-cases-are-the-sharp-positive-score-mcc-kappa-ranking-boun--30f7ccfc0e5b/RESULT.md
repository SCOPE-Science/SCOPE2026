# Twelve cases are the sharp positive-score MCC–kappa ranking boundary
## Finding
Consider two binary classifiers evaluated at a common sample size
\[
N
\]
and a common actual-positive count
\[
P.
\]

Require every confusion-matrix cell
\[
TP,\ FP,\ FN,\ TN
\]
to be strictly positive, and restrict to positive association
\[
TP\,TN>FP\,FN.
\]
For such tables, both the Matthews correlation coefficient and Cohen's kappa are positive.

No pair of classifiers receives opposite strict rankings from the Matthews correlation coefficient
\[
M
\]
and Cohen's kappa
\[
\kappa
\]
for
\[
N\le11.
\]

Weak-order agreement first fails at
\[
N=10.
\]
With
\[
P=3,
\]
compare
\[
(1,1,2,6)
\quad\text{and}\quad
(2,3,1,4),
\]
where coordinates are
\[
(TP,FP,FN,TN).
\]
Both have
\[
M=\frac1{\sqrt{21}},
\]
but their kappa values are
\[
\frac4{19}>\frac15.
\]
Thus the first weak disagreement is a Matthews-correlation tie split by kappa.

The sharp strict boundary is
\[
N=12.
\]
Across every admissible prevalence there are exactly two unordered strict reversals, and they are related by global exchange of the positive and negative class labels.

A representative occurs at
\[
P=4:
\]
\[
A=(2,3,2,5),
\qquad
B=(3,5,1,3).
\]
Their kappa values satisfy
\[
\kappa(A)=\frac2{17}>\frac1{10}=\kappa(B),
\]
whereas their Matthews correlations satisfy
\[
M(A)=\frac1{\sqrt{70}}<\frac18=M(B).
\]

Both tables have the same positive determinant
\[
TP\,TN-FP\,FN=4.
\]
The reversal is therefore caused entirely by the different predicted-class margins.

## Assumptions and scope
The reference positive class is fixed in advance.

Both classifiers in a comparison are evaluated on the same number of cases and the same actual-positive prevalence.

All four cells are positive, excluding degenerate tables with an absent outcome combination.

Only positively associated tables are compared. This deliberately removes the negative-score regime, where large differences between MCC and kappa are already well documented.

The result concerns ordinal comparison of two summary statistics. It does not assert that either statistic is preferable for every scientific decision problem.

## Proof
Put
\[
Q=N-P,
\qquad
R=TP+FP,
\qquad
S=FN+TN=N-R,
\]
and define the cross-product determinant
\[
\Delta=TP\,TN-FP\,FN.
\]

The Matthews correlation coefficient is
\[
M
=
\frac{\Delta}{\sqrt{PQRS}}.
\]

For a binary table, Cohen's kappa simplifies to
\[
\kappa
=
\frac{2\Delta}{PS+QR}.
\]

Consequently both statistics have the sign of
\[
\Delta.
\]
For fixed true margins \(P,Q\) and fixed predicted margins \(R,S\), the two statistics are positive multiples of the same determinant and therefore induce the same ordering. Any reversal must involve different predicted margins.

For the twelve-case witness
\[
A=(2,3,2,5),
\qquad
B=(3,5,1,3),
\]
we have
\[
P=4,
\qquad
Q=8,
\qquad
\Delta(A)=\Delta(B)=4.
\]

For \(A\),
\[
R=5,
\qquad
S=7,
\]
so
\[
\kappa(A)
=
\frac{8}{4\cdot7+8\cdot5}
=
\frac2{17},
\]
and
\[
M(A)
=
\frac4{\sqrt{4\cdot8\cdot5\cdot7}}
=
\frac1{\sqrt{70}}.
\]

For \(B\),
\[
R=8,
\qquad
S=4,
\]
so
\[
\kappa(B)
=
\frac8{4\cdot4+8\cdot8}
=
\frac1{10},
\]
and
\[
M(B)
=
\frac4{\sqrt{4\cdot8\cdot8\cdot4}}
=
\frac18.
\]

Since
\[
\frac2{17}>\frac1{10}
\]
but
\[
\frac1{\sqrt{70}}<\frac18,
\]
the rankings are opposite.

For sharpness, every strictly positive binary confusion matrix with positive determinant was generated for totals through twelve. Within each common \((N,P)\) layer every unordered classifier pair was compared using exact rational arithmetic for kappa and exact squared-algebraic comparisons for MCC.

No strict reversal occurs through total eleven. At total twelve exactly the stated pair and its global class-label complement reverse.

## Verification
The embedded `verify_mcc_kappa_positive_boundary.py` uses only exact integer and rational arithmetic.

It enumerates all strictly positive binary confusion matrices for
\[
4\le N\le12
\]
and all nontrivial actual-positive counts.

Only positive-determinant tables are retained, which is equivalent to requiring positive MCC and positive kappa.

The verifier checks every unordered pair at common \((N,P)\). It proves complete weak-order agreement through nine cases, the first weak-only split at ten cases, no strict reversal through eleven cases, and exactly two complement-related strict reversals at twelve cases.

Through total eleven it compares
\[
382
\]
eligible classifier pairs.

Run:

`python3 verify_mcc_kappa_positive_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Matthews introduced the correlation coefficient now bearing his name in a biological classification setting. Cohen's kappa was introduced earlier as a chance-corrected agreement statistic.

Chicco, Warrens, and Jurman directly compare MCC with Cohen's kappa for binary classification. They prove and discuss the pointwise inequality that kappa is no more extreme than MCC and note that positive MCC and kappa values are generally concordant, while their largest discrepancies arise in the negative-score regime. Their examples therefore establish the scientific relevance of comparing the two metrics, but they do not give a smallest positive-score pairwise ranking reversal at fixed sample size and fixed true prevalence.

The present result sharpens that positive-regime discussion. It shows that pointwise closeness and the inequality
\[
|M|\ge|\kappa|
\]
do not imply ordinal agreement across classifiers. The first strict failure requires twelve cases under the stated nondegeneracy and fixed-prevalence conditions.

Targeted searches using Matthews correlation coefficient, Cohen kappa, fixed prevalence, positive-score ranking reversal, smallest confusion matrix, and the exact witness tables did not locate this finite boundary.

## Limitations
The positive-score and positive-cell restrictions are substantive. If negative associations or zero cells are allowed, different and smaller disagreement phenomena can occur.

The result fixes the actual prevalence but allows the two classifiers to have different predicted prevalences. If predicted prevalence is also fixed, the two scores are proportional and cannot reverse.

Cohen's original article was verified as first published in April 1960, but the checked bibliographic source did not establish an exact publication day. The exact archival day used in the metadata is therefore the verified 20 October 1975 publication date of Matthews's paper.

An unindexed teaching example or software test could contain the twelve-case pair without identifying the sharp positive fixed-prevalence boundary.

## References
1. B. W. Matthews, “Comparison of the predicted and observed secondary structure of T4 phage lysozyme,” *Biochimica et Biophysica Acta* 405(2), 442–451, published 20 October 1975. DOI: 10.1016/0005-2795(75)90109-9.
2. J. Cohen, “A coefficient of agreement for nominal scales,” *Educational and Psychological Measurement* 20(1), 37–46, first published April 1960. DOI: 10.1177/001316446002000104.
3. D. Chicco, M. J. Warrens, and G. Jurman, “The Matthews correlation coefficient (MCC) is more informative than Cohen's kappa and Brier score in binary classification assessment,” *IEEE Access* 9, 78368–78381, published 26 May 2021. DOI: 10.1109/ACCESS.2021.3084050.
