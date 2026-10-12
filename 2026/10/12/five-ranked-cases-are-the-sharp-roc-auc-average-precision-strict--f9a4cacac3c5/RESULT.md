# Five ranked cases are the sharp ROC-AUC–average-precision strict-reversal boundary
## Finding
Consider binary scoring rules evaluated on a common set size
\[
N
\]
with a common number
\[
P
\]
of positive cases.

Assume all scores are distinct. After sorting a rule from highest to lowest score, encode the class labels as a binary word, with \(1\) denoting a positive case.

Let
\[
A
\]
be the area under the receiver-operating-characteristic curve, and let
\[
\mathrm{AP}
\]
be classical average precision.

No two rankings receive opposite strict orderings from \(A\) and \(\mathrm{AP}\) for
\[
N\le4.
\]

At
\[
N=4,
\]
weak-order agreement first fails, but only through an AUC tie. With
\[
P=2,
\]
compare
\[
1001
\quad\text{and}\quad
0110.
\]
Both have
\[
A=\frac12,
\]
while their average precisions are
\[
\frac34
\quad\text{and}\quad
\frac7{12}.
\]

At
\[
N=5,
\]
strict reversal appears for the first time.

For
\[
P=2,
\]
the pair
\[
10001
\quad\text{versus}\quad
01100
\]
satisfies
\[
A:\quad \frac12<\frac23,
\]
but
\[
\mathrm{AP}:\quad \frac7{10}>\frac7{12}.
\]

For
\[
P=3,
\]
the pair
\[
10011
\quad\text{versus}\quad
01110
\]
satisfies
\[
A:\quad \frac13<\frac12,
\]
but
\[
\mathrm{AP}:\quad \frac7{10}>\frac{23}{36}.
\]

Across every nontrivial prevalence at total five, these are exactly the two unordered strict reversals.

## Assumptions and scope
The same total number of cases and the same positive-class prevalence are used when two scoring rules are compared.

Scores have no ties, so each scoring rule induces a strict ranking.

Average precision means the classical discrete quantity obtained by averaging precision at each rank occupied by a positive case. It is not an arbitrarily interpolated geometric area under a precision-recall curve.

ROC-AUC is the ordinary empirical AUC, equivalently the fraction of positive-negative pairs ordered with the positive case above the negative case.

The result concerns exact ranked labels. It does not address uncertainty in AUC or average-precision estimates from a sampled population.

## Proof
Let the positive cases occupy ranks
\[
1\le r_1<r_2<\cdots<r_P\le N
\]
in decreasing score order, and put
\[
Q=N-P.
\]

For the positive case at rank \(r_j\), the number of negative cases above it is
\[
r_j-j.
\]

Hence the total number of positive-negative inversions is
\[
I=\sum_{j=1}^{P}(r_j-j).
\]

There are
\[
PQ
\]
positive-negative pairs in total, so
\[
A
=
1-\frac{I}{PQ}
=
1-\frac1{PQ}\sum_{j=1}^{P}(r_j-j).
\]

Thus ROC-AUC depends only on the total displacement of positive cases from the ideal top-\(P\) ranking.

At rank \(r_j\), exactly \(j\) positives have appeared, so the precision at that positive rank is
\[
\frac{j}{r_j}.
\]

Therefore
\[
\mathrm{AP}
=
\frac1P
\sum_{j=1}^{P}\frac{j}{r_j}.
\]

Average precision is consequently sensitive not merely to total displacement but to how that displacement is distributed across the ranked list.

For
\[
N=4,\qquad P=2,
\]
the words \(1001\) and \(0110\) have positive-rank vectors
\[
(1,4)
\quad\text{and}\quad
(2,3).
\]
Both have total displacement \(2\), hence equal AUC \(1/2\), but
\[
\mathrm{AP}(1001)=\frac12\left(1+\frac24\right)=\frac34,
\]
whereas
\[
\mathrm{AP}(0110)=\frac12\left(\frac12+\frac23\right)=\frac7{12}.
\]

For
\[
N=5,\qquad P=2,
\]
the positive-rank vectors
\[
(1,5)
\quad\text{and}\quad
(2,3)
\]
have displacement totals \(3\) and \(2\), respectively. Therefore
\[
A(10001)=\frac12<\frac23=A(01100),
\]
but
\[
\mathrm{AP}(10001)
=
\frac12\left(1+\frac25\right)
=
\frac7{10}
>
\frac12\left(\frac12+\frac23\right)
=
\frac7{12}
=
\mathrm{AP}(01100).
\]

For
\[
N=5,\qquad P=3,
\]
the corresponding positive-rank vectors are
\[
(1,4,5)
\quad\text{and}\quad
(2,3,4),
\]
giving the second stated reversal.

Exhaustive exact enumeration of every binary ranking with both classes present for
\[
2\le N\le5
\]
shows no weak disagreement through three cases, exactly one weak-only split at four cases, no strict reversal through four cases, and exactly the two stated strict reversals at five cases.

## Verification
The embedded `verify_auc_average_precision_boundary.py` uses only the Python standard library and exact rational arithmetic.

For each
\[
2\le N\le5
\]
and every
\[
1\le P\le N-1,
\]
it enumerates every possible distinct-score binary ranking.

The total numbers of rankings checked at each total are
\[
2,\ 6,\ 14,\ 30.
\]

Within each common \((N,P)\) layer, every unordered pair is compared by exact ROC-AUC and exact average precision.

The verifier checks the unique first weak disagreement at \(N=4\), absence of strict reversal through \(N=4\), and exactly two strict reversals at \(N=5\).

Run:

`python3 verify_auc_average_precision_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Average precision is a classical ranked-retrieval measure. Kishida gives its finite-list definition as the mean of precision values at the positions occupied by relevant items and emphasizes that relevant items near the top of a ranking contribute more strongly.

Davis and Goadrich prove a structural correspondence between ROC and precision-recall curves, while also stressing that optimizing area under ROC does not guarantee optimizing area under a precision-recall curve.

In biological and medical classifier evaluation, Saito and Rehmsmeier show that ROC and precision-recall summaries can support materially different interpretations, especially under class imbalance, and compare classifier rankings under the two views.

Those results establish that ROC and precision-recall evaluation are not interchangeable. The present result isolates the smallest fixed-prevalence, no-tie ranked data set on which empirical ROC-AUC and classical average precision strictly prefer opposite scoring rules, and completely classifies that first layer.

Targeted searches using ROC-AUC, average precision, precision-recall, fixed prevalence, rank reversal, smallest ranked list, and the exact five-case words did not locate this finite boundary.

## Limitations
The theorem assumes distinct scores. Tied-score conventions can change both metrics and may produce smaller or different finite effects.

The positive prevalence is fixed within each comparison. Average precision has a prevalence-dependent baseline, so cross-prevalence comparisons are a different question.

The theorem concerns classical average precision, not every possible convention for numerically integrating a precision-recall curve.

An unindexed teaching example or software test could contain one of the five-case ranking pairs without identifying the sharp fixed-prevalence boundary.

## References
1. K. Kishida, “Property of Average Precision and its Generalization: An Examination of Evaluation Indicator for Information Retrieval Experiments,” NII Technical Report NII-2005-014E, publicly listed 29 September 2005.
2. J. Davis and M. Goadrich, “The Relationship Between Precision-Recall and ROC Curves,” *Proceedings of the 23rd International Conference on Machine Learning*, 233–240, 2006. DOI: 10.1145/1143844.1143874.
3. T. Saito and M. Rehmsmeier, “The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets,” *PLOS ONE* 10(3):e0118432, published 4 March 2015. DOI: 10.1371/journal.pone.0118432.
