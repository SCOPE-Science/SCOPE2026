# A reciprocal pseudoinverse error in a woven \(K\)-\(g\)-fusion deletion theorem
## Finding
Theorem 2.5 of Sadri--Rahimlou--Ahmadi, *K-G-Fusion Woven in Hilbert Spaces*, gives a sufficient condition for deleting a set of indices from a woven \(K\)-\(g\)-fusion family. With
\[
C=\sum_{i=1}^{m}\sum_{j\in I}v_{ij}^2\|\Lambda_{ij}\|^2,
\]
the theorem assumes
\[
C<A\|K^\dagger\|^2
\]
and claims that the deletion remains woven on \(R(K)\), with lower bound
\[
A-C.
\]
That quantitative statement is false.

Let
\[
H=\mathbb R^2,\qquad
K=\frac12I_H,\qquad
m=2,\qquad
J=\{1,2\},\qquad
I=\{1\}.
\]
For both source families take
\[
W_{ij}=H,\qquad v_{ij}=1,
\]
and
\[
\Lambda_{i1}=P_{\operatorname{span}\{e_1\}},
\qquad
\Lambda_{i2}=P_{\operatorname{span}\{e_2\}}.
\]
The two source families are identical, so every full weave has energy
\[
\|f\|^2.
\]
The constants
\[
A=B=3
\]
are therefore valid universal bounds because
\[
3\|K^*f\|^2=\frac34\|f\|^2
\le
\|f\|^2
\le
3\|f\|^2.
\]

Since
\[
K^\dagger=2I_H,
\qquad
C=2,
\]
the printed hypothesis reads
\[
2<3\cdot4=12.
\]
The theorem predicts the positive lower bound
\[
A-C=1.
\]

After deleting index \(1\), however, the sole remaining analysis operator in either source family is the projection onto \(\operatorname{span}\{e_2\}\). Every remaining weave has energy
\[
\|P_{\operatorname{span}\{e_2\}}f\|^2.
\]
At \(f=e_1\) this is zero, while
\[
\|K^*e_1\|^2=\frac14.
\]
Thus the deleted family is not a \(K\)-\(g\)-fusion frame.

The scale-correct sufficient condition is instead
\[
C\|K^\dagger\|^2<A,
\]
with lower bound
\[
A-C\|K^\dagger\|^2.
\]

## Assumptions and scope
The counterexample uses finite-dimensional real Hilbert space and orthogonal projections as analysis maps. The operator \(K\) has closed range and
\[
R(K)=H.
\]
There are no convergence or closure issues.

The constants \(A=B=3\) are deliberately valid, nonoptimal universal bounds for the full woven family. A frame theorem stated for arbitrary frame bounds must remain valid for such a legitimate choice.

The correction concerns the deletion criterion of Theorem 2.5. It does not claim that the coarse quantity \(C\) gives a necessary condition for deletion stability.

## Proof
Let a partition of \(J\setminus I\) among the \(m\) source families be fixed. Extend it arbitrarily to a partition of all of \(J\) by assigning every deleted index to one source family.

For \(f\in R(K)\), the energy of the full extended weaving is at least
\[
A\|K^*f\|^2.
\]
The energy contributed by the selected deleted indices is at most the sum of the corresponding energies over every source family:
\[
\sum_{i=1}^{m}\sum_{j\in I}
v_{ij}^2\|\Lambda_{ij}P_{W_{ij}}f\|^2
\le
C\|f\|^2.
\]
Because \(K\) has closed range, the Moore--Penrose inverse is bounded and, for \(f\in R(K)\),
\[
\|f\|
\le
\|K^\dagger\|\|K^*f\|.
\]
Therefore the deleted weaving energy is bounded below by
\[
\left(A-C\|K^\dagger\|^2\right)\|K^*f\|^2.
\]
If
\[
C\|K^\dagger\|^2<A,
\]
this is a positive \(K\)-lower frame bound. The upper bound remains \(B\), because deleting nonnegative energy from an extended full weave cannot increase the full weaving energy.

The counterexample violates exactly the repaired condition:
\[
C\|K^\dagger\|^2=8>3=A,
\]
while satisfying the printed condition
\[
C<A\|K^\dagger\|^2.
\]
The deleted energy at \(e_1\) is exactly zero, so no positive lower bound exists.

## Verification
The primary PDF was inspected at Theorem 2.5 and its complete proof. The theorem prints the condition
\[
C<A\|K^\dagger\|^2
\]
and the conclusion with lower bound \(A-C\).

The last estimate in the proof instead contains
\[
A-C\|K^\dagger\|^2.
\]
Thus the corrected factor is already visible in the source's own calculation.

The counterexample was checked symbolically. The full weave energy is exactly \(\|f\|^2\), the deleted constant is exactly \(C=2\), and the remaining energy is exactly the squared \(e_2\)-coordinate.

No numerical experiment or finite search is used.

## Relationship to prior work
Huang--Yang's 2020 paper *\(K\)-\(g\)-fusion frames in Hilbert spaces* contains a different deletion theorem: under geometric orthogonality of the removed subspaces to \(R(K)\), deletion preserves the original bounds. That result does not provide the norm-threshold criterion considered here.

Agheshteh Moghaddam--Arefijamaal study excess and duality for woven \(K\)-frames, including structural questions about deletions and redundancy. Their results address excess rather than the reciprocal Moore--Penrose scaling in this \(K\)-\(g\)-fusion deletion estimate.

The corrected criterion is dictated by the standard closed-range estimate
\[
\|f\|\le\|K^\dagger\|\|K^*f\|
\qquad(f\in R(K)).
\]
Scaling \(K\) makes the distinction unavoidable: the perturbation cost must be multiplied by \(\|K^\dagger\|^2\), not used to enlarge the admissible cost by the same factor.

## Limitations
The repaired condition is sufficient, not asserted necessary. The constant
\[
C=\sum_{i,j\in I}v_{ij}^2\|\Lambda_{ij}\|^2
\]
can overestimate the energy actually removed by a particular extended partition.

The result does not optimize deletion thresholds using correlations among the deleted analysis maps.

No claim is made about unrelated theorems in the source.

## References
1. V. Sadri, G. Rahimlou and R. Ahmadi, *K-G-Fusion Woven in Hilbert Spaces*, TWMS Journal of Applied and Engineering Mathematics 11(3) (2021), 947--958.
2. Y. Huang and Y. Yang, *\(K\)-\(g\)-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications 2020, Article 57, DOI 10.1186/s13660-020-02320-0.
3. E. Agheshteh Moghaddam and A. A. Arefijamaal, *New aspects of weaving \(K\)-frames: the excess and duality*, Hacettepe Journal of Mathematics and Statistics 53(3) (2024), DOI 10.15672/hujms.1008448.
