# Seven cases are the sharp fixed-prevalence F1–balanced-accuracy strict-reversal boundary
## Finding
Consider binary classifiers evaluated on data sets with common total size
\[
N
\]
and common number of actual positives
\[
P.
\]

Require every confusion-matrix cell
\[
TP,\ FP,\ FN,\ TN
\]
to be strictly positive.

The F1 score is
\[
F_1=\frac{2TP}{2TP+FP+FN}.
\]

Balanced accuracy is
\[
B
=
\frac12\left(
\frac{TP}{P}
+
\frac{TN}{N-P}
\right).
\]

No two admissible classifiers receive opposite strict rankings from \(F_1\) and \(B\) for
\[
N\le6.
\]

At
\[
N=6,
\]
weak-order agreement first fails, but only through a tie. With
\[
P=3,
\]
compare
\[
(1,1,2,2)
\quad\text{and}\quad
(2,2,1,1),
\]
where the coordinates are
\[
(TP,FP,FN,TN).
\]
Both have
\[
B=\frac12,
\]
but
\[
F_1=\frac25
\quad\text{and}\quad
F_1=\frac47.
\]

At
\[
N=7,
\]
strict reversal appears for the first time.

For
\[
P=3,
\]
compare
\[
X=(1,1,2,3)
\]
with
\[
Y=(2,3,1,1).
\]
Then
\[
F_1(X)=\frac25<\frac12=F_1(Y),
\]
while
\[
B(X)=\frac{13}{24}>\frac{11}{24}=B(Y).
\]

Across every admissible prevalence at total seven there are exactly three unordered strict reversals. The other two occur at
\[
P=4:
\]
\[
(1,1,3,2)
\quad\text{versus}\quad
(2,2,2,1),
\]
and
\[
(2,1,2,2)
\quad\text{versus}\quad
(3,2,1,1).
\]

Thus seven observations are necessary and sufficient for a strictly positive fixed-prevalence confusion-matrix comparison in which F1 and balanced accuracy prefer opposite classifiers.

## Assumptions and scope
The positive class is fixed in advance.

Both classifiers in a comparison are evaluated at the same total sample size and the same class prevalence.

Every confusion-matrix cell is positive, excluding degenerate cases with absent errors, absent predictions, or absent classes.

Balanced accuracy weights sensitivity and specificity equally.

The result concerns ordinal comparison of fully specified binary classifiers. It does not address uncertainty from estimating performance on a finite random test sample.

## Proof
Let
\[
Q=N-P
\]
be the number of actual negatives.

Write
\[
a=TP,
\qquad
b=FP.
\]
Then
\[
FN=P-a,
\qquad
TN=Q-b.
\]

The two scores become
\[
F_1
=
\frac{2a}{P+a+b}
\]
and
\[
B
=
\frac12
\left(
1+\frac{a}{P}-\frac{b}{Q}
\right).
\]

For fixed \(N\) and \(P\), every strictly positive confusion matrix is therefore determined by the integer pair
\[
1\le a\le P-1,
\qquad
1\le b\le Q-1.
\]

The complete numbers of admissible confusion matrices, summed over all nontrivial prevalences, are
\[
1,\ 4,\ 10,\ 20
\]
for
\[
N=4,5,6,7.
\]

Exact comparison of every unordered pair at common \((N,P)\) gives no weak-order disagreement at totals four and five.

At total six there is exactly one weak disagreement and no strict reversal. It occurs at \(P=3\):
\[
(1,1,2,2)
\quad\text{versus}\quad
(2,2,1,1).
\]
Their balanced accuracies coincide at \(1/2\), while their F1 scores differ.

At total seven there are exactly three strict reversals and no additional weak-only disagreements.

For the \(P=3\) witness,
\[
F_1(1,1,2,3)=\frac25,
\qquad
F_1(2,3,1,1)=\frac12,
\]
whereas
\[
B(1,1,2,3)=\frac{13}{24},
\qquad
B(2,3,1,1)=\frac{11}{24}.
\]

The two \(P=4\) reversals are checked similarly.

Finally, multiplying all four cells by the same positive integer leaves sensitivity, specificity, precision, F1, and balanced accuracy unchanged. Hence the first \(P=3\) reversal generates reversals at every total
\[
7q.
\]

## Verification
The embedded `verify_f1_balanced_accuracy_boundary.py` uses only exact rational arithmetic from the Python standard library.

It enumerates every strictly positive binary confusion matrix for
\[
4\le N\le7
\]
and every admissible prevalence
\[
2\le P\le N-2.
\]

Within each common \((N,P)\) layer it compares every unordered pair by F1 and balanced accuracy.

It verifies the table counts
\[
1,\ 4,\ 10,\ 20,
\]
the unique first weak-order split at total six, the absence of strict reversal through six, and the exact three-pair strict layer at total seven.

It also verifies scaling persistence for the first witness.

Run:

`python3 verify_f1_balanced_accuracy_boundary.py`

The first output line must be `VERIFY_OK`.

No floating-point comparisons are used.

## Relationship to prior work
Balanced accuracy was developed for classifier evaluation under class imbalance as the equal-weight average of sensitivity and specificity.

Powers gives the binary contingency-table formulas for F1 and for the ROC quantity
\[
\frac{TPR+TNR}{2},
\]
which is balanced accuracy, and emphasizes that F-measure can rank a system above another system that is objectively worse under Informedness. Because balanced accuracy is
\[
\frac{1+\text{Informedness}}2,
\]
generic F1-versus-balanced-accuracy ranking disagreement is therefore established prior context.

The present result does not claim that such disagreement is new. It asks for the smallest strictly positive integer confusion matrices at fixed sample size and fixed prevalence where a strict reversal is possible.

Targeted searches using F1, F-measure, balanced accuracy, Informedness, Youden index, fixed prevalence, smallest confusion matrix, and the exact seven-case witness did not locate the sharp six/seven transition or the complete first strict layer.

## Limitations
The result fixes prevalence across each classifier comparison. If prevalence is allowed to differ, smaller or different effects can occur because F1 itself depends on prevalence.

The theorem uses strict positivity of all four cells. Allowing zero cells changes the finite boundary.

Balanced accuracy is affine-equivalent to Youden's informedness for binary classification, so the same boundary applies to F1 versus Youden's index.

The theorem is a discrete finite-sample boundary, not a claim that seven observations are sufficient for reliable statistical model assessment.

## References
1. K. H. Brodersen, C. S. Ong, K. E. Stephan, and J. M. Buhmann, “The Balanced Accuracy and Its Posterior Distribution,” *20th International Conference on Pattern Recognition*, 3121–3124, 2010. DOI: 10.1109/ICPR.2010.764. The conference opened 23 August 2010.
2. D. M. W. Powers, “Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation,” *Journal of Machine Learning Technologies* 2(1), 37–63, 2011; public postprint arXiv:2010.16061.
