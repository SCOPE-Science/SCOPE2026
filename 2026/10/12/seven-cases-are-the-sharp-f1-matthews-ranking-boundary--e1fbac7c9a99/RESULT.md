# Seven cases are the sharp F1–Matthews ranking boundary
## Finding
Consider a binary classifier evaluated on a data set of size
\[
N.
\]
Write its confusion matrix as
\[
(TP,FP,FN,TN),
\]
and suppose all four cells are positive.

For two classifiers to be compared, require that they are evaluated on the same data set in the sense that they have the same number of actual positives
\[
P=TP+FN
\]
and hence the same number of actual negatives
\[
Q=TN+FP=N-P.
\]

The \(F_1\) score is
\[
F_1=\frac{2TP}{2TP+FP+FN}.
\]

The Matthews correlation coefficient is
\[
M=
\frac{TP\,TN-FP\,FN}
{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}.
\]

No pair of positive-cell confusion matrices with common \(N\) and common \(P\) is ranked in opposite strict orders by \(F_1\) and \(M\) for
\[
N\le6.
\]

At
\[
N=7,
\]
strict reversal occurs for the first time. Across all admissible fixed-prevalence comparisons, exactly three unordered pairs reverse.

A first-layer witness in which both classifiers have positive Matthews correlation is
\[
A=(2,1,2,2)
\]
and
\[
B=(3,2,1,1).
\]
Both have
\[
P=4,
\qquad
Q=3.
\]
Their \(F_1\) scores are
\[
F_1(A)=\frac47
<
\frac23=F_1(B).
\]
Their Matthews coefficients are
\[
M(A)=\frac{2}{\sqrt{144}}=\frac16
\]
and
\[
M(B)=\frac{1}{\sqrt{120}}.
\]
Since
\[
\frac1{36}>\frac1{120},
\]
one has
\[
M(A)>M(B).
\]
Thus \(F_1\) ranks \(B\) higher while Matthews correlation ranks \(A\) higher.

The disagreement is not confined to the seven-case boundary. For every integer
\[
N\ge7,
\]
there is a same-prevalence pair with all cells positive and both Matthews coefficients positive that reverses.

For odd sizes
\[
N=2k+7,
\qquad k\ge0,
\]
use
\[
A_k=(k+2,1,2,k+2),
\qquad
B_k=(k+3,2,1,k+1).
\]
For even sizes
\[
N=2k+8,
\qquad k\ge0,
\]
use
\[
A_k=(k+3,1,2,k+2),
\qquad
B_k=(k+4,2,1,k+1).
\]
In both cases the two matrices have the same actual-positive and actual-negative totals, \(F_1(B_k)>F_1(A_k)\), and \(M(A_k)>M(B_k)>0\).

## Assumptions and scope
The result concerns hard binary classifications summarized by integer confusion matrices.

Every cell is positive. This excludes degenerate rows or columns and ensures that both metrics are defined by their ordinary formulas without conventions for zero marginals.

Pairwise comparisons keep both the total sample size and class prevalence fixed. This removes a major source of metric variation: neither classifier is being advantaged by being tested on a data set with a different positive-class frequency.

The theorem concerns strict ordinal rankings of point estimates. It does not address uncertainty in the estimated performance, threshold selection, calibration, area-under-curve summaries, or multiclass averaging.

The first-layer count of three includes Matthews coefficients of either sign. The displayed witness is stronger for interpretation because both coefficients are positive.

## Proof
For fixed
\[
N
\]
and
\[
P,
\]
every admissible confusion matrix is determined by integers
\[
1\le TP\le P-1
\]
and
\[
1\le FP\le N-P-1.
\]
The remaining cells are
\[
FN=P-TP,
\qquad
TN=N-P-FP.
\]
Thus the domain through \(N=7\) is finite and can be exhausted exactly.

The verifier enumerates every positive-cell matrix for each fixed prevalence and compares every unordered pair at that prevalence. The numbers of matrices for
\[
N=4,5,6,7
\]
are
\[
1,4,10,20.
\]
The numbers of within-prevalence unordered pairs are
\[
0,2,12,42.
\]
Exact comparison gives strict-reversal counts
\[
0,0,0,3.
\]
Hence \(N=7\) is the sharp boundary.

The three first-layer pairs, written as \((TP,FP,FN,TN)\), are
\[
(1,1,2,3)\ \text{versus}\ (2,3,1,1),
\]
\[
(1,1,3,2)\ \text{versus}\ (2,2,2,1),
\]
and
\[
(2,1,2,2)\ \text{versus}\ (3,2,1,1).
\]
The last pair is the positive-Matthews witness displayed above.

For the infinite family, first consider odd
\[
N=2k+7.
\]
The two matrices have common
\[
P=k+4
\]
and
\[
Q=k+3.
\]
Their \(F_1\) difference is
\[
F_1(B_k)-F_1(A_k)
=
\frac{6}{(2k+7)(2k+9)}>0.
\]

Let \(n_A,n_B\) denote the numerators of the two Matthews coefficients and let \(d_A,d_B\) denote their squared denominators. Direct substitution gives
\[
n_A=k^2+4k+2,
\qquad
n_B=k^2+4k+1,
\]
with both positive, and
\[
n_A^2d_B-n_B^2d_A
=
(k+3)(k+4)(2k+7)(3k^2+11k+4)>0.
\]
Because both Matthews coefficients are positive, this proves
\[
M(A_k)>M(B_k).
\]

For even
\[
N=2k+8,
\]
the same calculation gives
\[
F_1(B_k)-F_1(A_k)
=
\frac{6}{(2k+9)(2k+11)}>0,
\]
and
\[
n_A^2d_B-n_B^2d_A
=
4(k+3)(k+4)^2(k+5)(3k+2)>0.
\]
Again both Matthews numerators are positive, so
\[
M(A_k)>M(B_k)>0.
\]
This proves persistence for every \(N\ge7\).

## Verification
The embedded `verify_f1_mcc_minimal_reversal.py` uses only the Python standard library and exact integer or rational arithmetic.

It enumerates all positive-cell confusion matrices for every fixed prevalence through \(N=7\), compares \(F_1\) as an exact rational number, and compares Matthews coefficients exactly by sign and cross-multiplication of squared values.

It reproduces the matrix counts
\[
1,4,10,20,
\]
the within-prevalence pair counts
\[
0,2,12,42,
\]
and the reversal counts
\[
0,0,0,3.
\]
It also verifies the complete three-pair first layer.

For the persistent family, the verifier checks the displayed polynomial factorizations coefficient-by-coefficient and then replays every sample size from \(7\) through \(500\) as an additional consistency check.

Run:

`python3 verify_f1_mcc_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Matthews introduced the correlation coefficient now carrying his name in the setting of comparing predicted and observed protein secondary structure. The coefficient is a correlation-style summary that uses all four entries of a binary contingency table.

Chicco and Jurman give the modern confusion-matrix formulas for Matthews correlation and \(F_1\), emphasize that \(F_1\) ignores true negatives whereas Matthews correlation uses all four cells, and explicitly report many settings in which the two measures disagree. Their genomics experiment also gives different rankings of classifiers under Matthews correlation and \(F_1\). Thus the existence of ranking disagreement is established prior work and is not claimed here.

The present statement is a finite structural boundary under a stronger comparison protocol: the classifiers are evaluated with the same \(N\), the same actual-positive count \(P\), and strictly positive cells. Targeted searches for a minimum sample size, the seven-case boundary, fixed-prevalence reversal, and the exact witness matrices did not locate this result.

The prior literature therefore explains the mechanism—especially the fact that \(F_1\) omits \(TN\)—but does not imply the universal exclusion through six cases, the complete first reversal layer, or the all-larger-size same-prevalence family.

## Limitations
The theorem applies to hard binary predictions only.

It fixes class prevalence between the classifiers being compared. If classifiers are evaluated on different data sets, additional disagreement mechanisms are possible.

The all-cells-positive condition is deliberate; allowing zero cells creates different finite boundary questions and may require conventions for undefined Matthews denominators.

The theorem identifies the smallest combinatorial domain in which the two metrics can disagree strictly. It does not assert that seven observations are enough for reliable empirical model selection.

General disagreement between Matthews correlation and \(F_1\) is well known. The claimed contribution is only the sharp fixed-prevalence positive-cell boundary, its complete first layer, and the persistent exact family.

An unindexed exercise, test fixture, or specialized note could contain the same seven-case witness even though the sharp boundary was not located.

## References
1. B. W. Matthews, “Comparison of the predicted and observed secondary structure of T4 phage lysozyme,” *Biochimica et Biophysica Acta* 405(2), 442–451, 1975. DOI: 10.1016/0005-2795(75)90109-9.
2. D. Chicco and G. Jurman, “The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation,” *BMC Genomics* 21, 6, 2020. DOI: 10.1186/s12864-019-6413-7.
