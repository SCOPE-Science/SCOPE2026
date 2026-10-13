# Eleven cases are the sharp above-chance balanced-accuracy–G-mean strict-reversal boundary
## Finding
For a binary classifier, write sensitivity and specificity as
\[
s=\frac{TP}{P},
\qquad
c=\frac{TN}{N-P}.
\]

Balanced accuracy is
\[
B=\frac{s+c}{2},
\]
while the sensitivity-specificity geometric mean is
\[
G=\sqrt{sc}.
\]

Compare two classifiers only when they are evaluated at the same total sample size \(N\), the same actual-positive count \(P\), every cell \(TP,FP,FN,TN\) is strictly positive, and each classifier satisfies
\[
B>\frac12.
\]

Under these conditions, no pair receives opposite strict rankings from \(B\) and \(G\) for
\[
N\le10.
\]

Weak-order agreement first fails at
\[
N=8.
\]
At \(P=3\), compare
\[
(1,1,2,4)
\quad\text{and}\quad
(2,3,1,2),
\]
with coordinates \((TP,FP,FN,TN)\). Their balanced accuracies are
\[
\frac{17}{30}>\frac{8}{15},
\]
but both have
\[
G^2=\frac4{15}.
\]
The only other weak disagreement at total eight is the global positive-negative label complement of this pair.

Strict reversal first appears at
\[
N=11.
\]
At \(P=3\), compare
\[
A=(1,1,2,7)
\]
with
\[
C=(2,4,1,4).
\]
Then
\[
B(A)=\frac{29}{48}>\frac7{12}=B(C),
\]
whereas
\[
G(A)^2=\frac7{24}<\frac13=G(C)^2.
\]
Thus balanced accuracy prefers \(A\), while G-mean prefers \(C\).

Across every admissible prevalence at total eleven there are exactly six unordered strict reversals. Global interchange of the positive and negative class pairs them into exactly three classes.

## Assumptions and scope
The task is binary classification on a finite test set.

The two classifiers being compared have the same \(N\) and the same actual prevalence \(P/N\).

All four confusion-matrix cells are positive. This removes zero-sensitivity, zero-specificity, and absent-error degeneracies.

The above-chance restriction
\[
B>\frac12
\]
is equivalent to positive Youden association and to
\[
TP\,TN>FP\,FN.
\]
It excludes classifiers whose average class accuracy is chance or worse.

G-mean means the geometric mean of sensitivity and specificity, not a geometric mean involving precision.

## Proof
Put
\[
Q=N-P.
\]
For fixed \((N,P)\), every positive confusion matrix is determined by \(TP\) and \(FP\), with
\[
1\le TP\le P-1,
\qquad
1\le FP\le Q-1,
\]
and
\[
FN=P-TP,
\qquad
TN=Q-FP.
\]

Write
\[
s=\frac{TP}{P},
\qquad
c=\frac{TN}{Q}.
\]
Then
\[
B=\frac{s+c}{2},
\qquad
G^2=sc.
\]
If
\[
\delta=\frac{|s-c|}{2},
\]
then direct expansion gives
\[
G^2=B^2-\delta^2.
\]
Therefore G-mean is balanced accuracy penalized by the squared imbalance between sensitivity and specificity.

The above-chance condition also has the exact determinant form
\[
s+c-1
=
\frac{TP\,TN-FP\,FN}{PQ},
\]
so
\[
B>\frac12
\quad\Longleftrightarrow\quad
TP\,TN>FP\,FN.
\]

For the representative total-eleven pair,
\[
A=(1,1,2,7)
\]
has
\[
s_A=\frac13,
\qquad
c_A=\frac78,
\]
so
\[
B(A)=\frac{29}{48},
\qquad
G(A)^2=\frac7{24}.
\]
For
\[
C=(2,4,1,4),
\]
we have
\[
s_C=\frac23,
\qquad
c_C=\frac12,
\]
so
\[
B(C)=\frac7{12},
\qquad
G(C)^2=\frac13.
\]
Hence the two metrics strictly reverse the pair.

For minimality and completeness, enumerate every positive integer confusion matrix for \(4\le N\le11\), every \(2\le P\le N-2\), and retain precisely those with \(B>1/2\). Within each common \((N,P)\) layer, compare every unordered pair by exact rational \(B\) and exact rational \(G^2\).

The resulting counts \((\text{eligible tables},\text{pairs},\text{weak disagreements},\text{strict reversals})\) are
\[
(0,0,0,0),
(2,0,0,0),
(3,0,0,0),
(10,8,0,0),
(15,17,2,0),
(26,48,4,0),
(38,93,6,0),
(60,216,16,6)
\]
for totals \(4,5,\ldots,11\), respectively.

Thus there is no strict reversal through total ten and exactly six at total eleven.

## Verification
The embedded `verify_balanced_accuracy_gmean_boundary.py` uses only exact rational arithmetic from the Python standard library.

It regenerates every strictly positive confusion matrix for totals four through eleven, applies the above-chance condition exactly, and compares every same-prevalence pair by balanced accuracy and squared G-mean.

It checks the first weak-only layer at total eight, the absence of strict reversal through total ten, the exact six-pair strict layer at total eleven, global class-label complement symmetry, the identity
\[
G^2=B^2-\delta^2,
\]
and the determinant equivalence for the above-chance condition.

Run:

`python3 verify_balanced_accuracy_gmean_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Kubat and Matwin introduced the geometric-mean criterion for imbalanced binary classification as the geometric mean of positive- and negative-class accuracies, precisely to require good performance on both classes.

Brodersen and coauthors formalized balanced accuracy as the arithmetic mean of class-specific accuracies and motivated it as a correction for misleading ordinary accuracy under class imbalance.

Later comparative work discusses balanced accuracy and sensitivity-specificity geometric mean side by side. It records the general arithmetic-mean/geometric-mean ordering and gives examples in which equal balanced accuracy can hide different G-mean values. Thus generic non-equivalence and tie-splitting are prior context, not part of the originality claim here.

The result here is narrower and exact: after fixing both test-set size and prevalence, excluding zero-cell degeneracies, and restricting to above-chance classifiers, it determines the smallest sample size at which the two metrics can strictly prefer opposite classifiers and classifies the complete first strict layer.

Targeted searches using balanced accuracy, G-mean, sensitivity, specificity, fixed prevalence, smallest confusion matrix, rank reversal, and the exact witness values did not locate this finite boundary.

## Limitations
The theorem uses exact finite confusion matrices. It does not address uncertainty in estimated sensitivity or specificity.

Allowing zero cells, allowing chance-or-worse classifiers, changing prevalence between compared classifiers, or using a different geometric-mean convention defines a different finite problem and can change the boundary.

The complete first layer is classified only at the sharp total eleven; larger totals are not classified.

An unindexed teaching example or software test could contain one of the small witness pairs without identifying the fixed-prevalence minimality result.

## References
1. M. Kubat and S. Matwin, “Addressing the Curse of Imbalanced Training Sets: One-Sided Selection,” *Proceedings of the Fourteenth International Conference on Machine Learning*, 179–186, 1997. ICML 1997 was held 8–12 July 1997.
2. K. H. Brodersen, C. S. Ong, K. E. Stephan, and J. M. Buhmann, “The Balanced Accuracy and Its Posterior Distribution,” *20th International Conference on Pattern Recognition*, 3121–3124, 2010. DOI: 10.1109/ICPR.2010.764.
3. I. M. de Diego, A. R. Redondo, R. R. Fernández, J. Navarro, and J. M. Moguerza, “General Performance Score for classification problems,” *Applied Intelligence* 52, 12049–12063, 2022. DOI: 10.1007/s10489-021-03041-7.
