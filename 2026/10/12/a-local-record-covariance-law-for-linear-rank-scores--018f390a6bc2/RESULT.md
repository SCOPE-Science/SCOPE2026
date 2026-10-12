# A local record covariance law for linear rank scores
## Finding
Let \(\Pi\) be uniformly distributed on \(S_n\), with \(n\ge2\). Define the upper-record indicator
\[
U_i=\mathbf 1\{\Pi(i)=\max_{1\le j\le i}\Pi(j)\},
\qquad 1\le i\le n.
\]
For arbitrary deterministic real weights \(w_1,\ldots,w_n\), put
\[
L_w=\sum_{j=1}^n w_j\Pi(j).
\]
Then every record position satisfies the exact covariance law
\[
\boxed{
\operatorname{Cov}(U_i,L_w)
=
\frac{n+1}{2i(i+1)}
\left((i-1)w_i-\sum_{j<i}w_j\right).
}
\]
Thus the dependence of a local record event on any linear rank score is controlled only by the current weight and the prefix sum of earlier weights.

For squared rank displacement
\[
D_n=\sum_{j=1}^n(\Pi(j)-j)^2
\]
and Spearman's no-ties coefficient
\[
R_n=1-\frac{6D_n}{n(n^2-1)},
\]
the specialization \(w_j=j\) gives
\[
\boxed{
\operatorname{Cov}(U_i,D_n)
=-\frac{(n+1)(i-1)}{2(i+1)}
}
\]
and
\[
\boxed{
\operatorname{Cov}(U_i,R_n)
=\frac{3(i-1)}{n(n-1)(i+1)}.
}
\]
Since \(\mathbb P(U_i=1)=1/i\) and \(\mathbb ER_n=0\),
\[
\boxed{
\mathbb E[R_n\mid U_i=1]
=\frac{3i(i-1)}{n(n-1)(i+1)}.
}
\]
For \(i>1\), the complementary conditional mean is
\[
\mathbb E[R_n\mid U_i=0]
=-\frac{3i}{n(n-1)(i+1)}.
\]
The record effect therefore grows monotonically with the record position. At \(i=n\), the record event is exactly \(\Pi(n)=n\), and the conditional mean reduces to \(3/(n+1)\).

Let
\[
Q_n=\sum_{i=1}^nU_i
\]
be the total number of upper records. Summing the local profile yields
\[
\boxed{
\operatorname{Cov}(Q_n,R_n)
=
\frac{3(n+2-2H_{n+1})}{n(n-1)},
}
\]
where \(H_n=\sum_{j=1}^n1/j\). Since the upper-record indicators of a uniform permutation are independent with \(\mathbb P(U_i=1)=1/i\),
\[
\operatorname{Var}(Q_n)=H_n-H_n^{(2)},
\qquad
H_n^{(2)}=\sum_{j=1}^n\frac1{j^2}.
\]
Together with \(\operatorname{Var}(R_n)=1/(n-1)\), this gives
\[
\boxed{
\operatorname{Corr}(Q_n,R_n)
=
\frac{3(n+2-2H_{n+1})}
{n\sqrt{(n-1)(H_n-H_n^{(2)})}}.
}
\]
Consequently
\[
\operatorname{Corr}(Q_n,R_n)
\sim
\frac3{\sqrt{n\log n}}.
\]

## Assumptions and scope
The permutation law is uniform on the full symmetric group. Records are upper left-to-right records. The general covariance theorem allows arbitrary deterministic real weights and therefore covers any linear rank score of the form \(\sum_jw_j\Pi(j)\).

The Spearman specialization assumes complete rankings without ties. The covariance identities are second-moment statements and do not imply independence.

## Proof
Fix \(i\). Conditional on \(U_i=1\), the set of values in the first \(i\) positions is a uniformly chosen \(i\)-element subset of \(\{1,\ldots,n\}\), and \(\Pi(i)\) is its maximum. Hence
\[
\mathbb E[\Pi(i)\mid U_i=1]
=\frac{i(n+1)}{i+1}.
\]
The other \(i-1\) positions in the prefix are exchangeable. A uniform \(i\)-subset has expected sum \(i(n+1)/2\), so each earlier position satisfies
\[
\mathbb E[\Pi(j)\mid U_i=1]
=\frac{i(n+1)}{2(i+1)},
\qquad j<i.
\]
The suffix positions are exchangeable over the complement of the prefix subset, whose expected total is \((n-i)(n+1)/2\). Therefore
\[
\mathbb E[\Pi(j)\mid U_i=1]
=\frac{n+1}{2},
\qquad j>i.
\]
Unconditionally every coordinate has mean \((n+1)/2\). It follows that
\[
\mathbb E[L_w\mid U_i=1]-\mathbb EL_w
=
\frac{n+1}{2(i+1)}
\left((i-1)w_i-\sum_{j<i}w_j\right).
\]
For a uniform permutation, \(\mathbb P(U_i=1)=1/i\). Because
\[
\operatorname{Cov}(U_i,L_w)
=
\mathbb P(U_i=1)
\left(\mathbb E[L_w\mid U_i=1]-\mathbb EL_w\right),
\]
the general covariance formula follows.

Now put
\[
L=\sum_{j=1}^n j\Pi(j).
\]
Permutation invariance of \(\sum_j\Pi(j)^2\) gives
\[
D_n=2\sum_{j=1}^n j^2-2L.
\]
For \(w_j=j\),
\[
(i-1)w_i-\sum_{j<i}w_j
=
\frac{i(i-1)}2.
\]
Thus
\[
\operatorname{Cov}(U_i,L)
=
\frac{(n+1)(i-1)}{4(i+1)},
\]
which immediately gives the displayed \(D_n\) and \(R_n\) covariances. The conditional means follow from \(\mathbb ER_n=0\).

Finally,
\[
\sum_{i=1}^n\frac{i-1}{i+1}
=
n+2-2H_{n+1},
\]
so summing the local Spearman covariance proves the formula for \(Q_n\). The independent-record representation yields \(\operatorname{Var}(Q_n)=H_n-H_n^{(2)}\), while the standard permutation-null calculation gives \(\operatorname{Var}(R_n)=1/(n-1)\). The exact correlation and its asymptotic form follow.

## Verification
The accompanying `checker.py` uses exact rational arithmetic. For every \(2\le n\le9\), it exhaustively enumerates all permutations and verifies every local record/Spearman covariance, the record and nonrecord conditional means, the total-record covariance, both marginal variances, and the exact correlation-squared identity.

For every \(2\le n\le8\), it also checks the general linear-score covariance law for several nonconstant signed weight sequences. A separate finite-sum check through \(n=100\) verifies the conditional expected maximum and the induced prefix-coordinate mean used in the proof.

Finite enumeration is supplementary. The conditional subset argument proves the theorem for every \(n\ge2\) and every deterministic real weight vector.

## Relationship to prior work
Gnedin develops coherent random permutations with record statistics and, for the uniform case, the classical record representation through independent initial ranks. The complete inspected article provides the natural record-statistic setting but does not introduce Spearman's coefficient, squared rank displacement, or covariance with linear rank scores.

Jiang studies dependence among metrics on symmetric groups, including the Spearman family. The article's “record map” is the cycle-to-one-line bijection used to compare class functions with permutation metrics; it is not the upper-record indicator process used here. The complete inspected Spearman section and record-map discussion do not state an upper-record-count covariance or the local profile above.

The present theorem connects the classical upper-record process to arbitrary linear rank scores. Its Spearman corollary gives a position-resolved dependence profile and an exact global decay rate that are not supplied by the inspected record or metric sources.

## Limitations
The formulas use the uniform permutation law. Biasing permutations by inversions, records, cycles, or other statistics changes the conditional prefix law.

The result concerns upper records. Lower records admit an analogous calculation after order reversal, but that separate statement is not claimed here.

Because the proof is elementary once one conditions on a record, an equivalent formula may occur in older unindexed permutation-statistics or record-theory literature under different notation.

## References
1. A. Gnedin, “Coherent random permutations with record statistics,” arXiv:math/0611538, first submitted 17 November 2006.
2. Y. Jiang, “Asymptotic correlations of metrics on the symmetric groups,” arXiv:1110.0807, first submitted 4 October 2011.
