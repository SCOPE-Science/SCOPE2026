# The deletion threshold for woven \(K\)-\(g\)-fusion frames needs the pseudoinverse factor on the loss

## Finding
Theorem 2.5 of Sadri--Rahimlou--Ahmadi gives a deletion criterion for a \(K\)-\(g\)-fusion woven family. For a deleted set \(I\), it defines
\[
C=\sum_{i\in[m]}\sum_{j\in I}v_{ij}^{2}\|\Lambda_{ij}\|^{2}
\]
and prints the hypothesis
\[
C<A\|K^\dagger\|^{2},
\]
with claimed lower bound
\[
A-C.
\]

That statement is false. The proof in the same paper actually obtains
\[
E_{\mathrm{remain}}(f)\ge
\bigl(A-C\|K^\dagger\|^{2}\bigr)\|K^*f\|^{2}
\]
for \(f\in R(K)\). Therefore the sufficient condition supported by the argument is
\[
C\|K^\dagger\|^{2}<A,
\]
and the resulting lower \(K\)-\(g\)-fusion woven bound is
\[
A-C\|K^\dagger\|^{2}.
\]

An exact counterexample to the printed condition is obtained on
\[
H=\mathbb C
\]
with
\[
K=\frac12I_H,\qquad J=\{0,1\},\qquad m=2.
\]
For both weave labels \(i=1,2\), put
\[
W_{i0}=W_{i1}=H,\qquad v_{i0}=v_{i1}=1,
\]
and
\[
\Lambda_{i0}=\frac12I_H,\qquad \Lambda_{i1}=0.
\]
Every weave has energy
\[
\frac14\|f\|^{2}=\|K^*f\|^{2},
\]
so the family is \(K\)-\(g\)-fusion woven with universal bounds \(A=B=1\).

Delete the proper subset
\[
I=\{0\}.
\]
Here
\[
K^\dagger=2I_H,\qquad \|K^\dagger\|^{2}=4,
\]
and
\[
C=
2\left\|\frac12I_H\right\|^{2}
=\frac12.
\]
Thus the printed hypothesis reads
\[
\frac12<4,
\]
so it is satisfied. Yet the remaining index \(j=1\) carries only the zero operator. Every remaining weave has zero energy on the nonzero space
\[
R(K)=H,
\]
and hence is not a \(K\)-\(g\)-fusion frame.

## Assumptions and scope
The example is finite-dimensional and uses two weave labels, as required by the paper's convention \(m>1\). The deleted set is a proper subset of \(J\), so the failure does not depend on deleting the entire index set.

Each original constituent family is also an ordinary \(g\)-fusion frame: its energy is \(\frac14\|f\|^{2}\). There are no convergence or measurability issues.

The repaired statement is a sufficient deletion theorem obtained from the source's own norm estimate. No claim is made that the scalar quantity \(C\) gives a necessary deletion criterion for every woven family.

## Proof
Fix a partition of the surviving indices and take \(f\in R(K)\). Since \(K\) has closed range, its Moore--Penrose inverse is bounded and
\[
f=(K^\dagger)^*K^*f.
\]
Consequently,
\[
\|f\|
\le
\|K^\dagger\|\|K^*f\|.
\]

The total energy contributed by the deleted indices is bounded by
\[
\sum_{i\in[m]}\sum_{j\in I}
v_{ij}^{2}\|\Lambda_{ij}\pi_{W_{ij}}f\|^{2}
\le
C\|f\|^{2}.
\]
Therefore
\[
\sum_{i\in[m]}\sum_{j\in I}
v_{ij}^{2}\|\Lambda_{ij}\pi_{W_{ij}}f\|^{2}
\le
C\|K^\dagger\|^{2}\|K^*f\|^{2}.
\]

Extending the chosen partition on \(J\setminus I\) by assigning the deleted indices gives a full weave, whose energy is at least
\[
A\|K^*f\|^{2}.
\]
Subtracting the deleted contribution yields
\[
E_{\mathrm{remain}}(f)
\ge
\bigl(A-C\|K^\dagger\|^{2}\bigr)\|K^*f\|^{2}.
\]
Thus
\[
C\|K^\dagger\|^{2}<A
\]
is sufficient, with lower bound
\[
A-C\|K^\dagger\|^{2}.
\]
The original upper bound \(B\) survives deletion.

For the counterexample, every full weave selects exactly one operator at each of \(j=0,1\). At \(j=0\) that operator is always \(\frac12I_H\), while at \(j=1\) it is always zero. Hence every full weave has energy
\[
\frac14\|f\|^{2}.
\]
After deleting \(j=0\), every surviving energy is zero. This proves failure of the printed theorem.

## Verification
The publisher PDF was inspected at Definition 2.1, Theorem 2.5, and the complete proof. The theorem statement prints the threshold
\[
C<A\|K^\dagger\|^{2}
\]
and the lower bound \(A-C\), while the last displayed line of the proof is
\[
\bigl(A-C\|K^\dagger\|^{2}\bigr)\|K^*f\|^{2}.
\]

The scalar counterexample was checked symbolically. No numerical approximation or finite search is used.

The paper lists primary MSC \(42C15\). The earliest verified public copy located for this work is the author-uploaded full text dated 8 July 2021.

## Relationship to prior work
Huang--Yang's 2020 paper on \(K\)-\(g\)-fusion frames uses the same Moore--Penrose estimate in the standard direction: on \(R(K)\), a \(K\)-\(g\)-fusion lower bound \(A\) yields an ordinary lower frame bound
\[
\frac{A}{\|K^\dagger\|^{2}}.
\]
That reciprocal scaling is consistent with the repaired deletion estimate.

The same 2020 paper has a different erasure theorem based on orthogonality of the deleted subspaces to \(R(K)\). It does not imply the quantitative small-deletion result considered here.

A later continuous controlled weaving paper gives a removal theorem under the stronger, directly \(K\)-scaled hypothesis that the removed energy is at most
\[
D\|K^*f\|^{2}
\]
with \(D<A\); it then obtains the lower bound \(A-D\). This is structurally consistent with the repaired estimate, but it does not state the present correction from the operator-norm quantity \(C\).

Targeted searches using the exact theorem number, title, pseudoinverse threshold, deletion terminology, and correction terms did not locate an indexed erratum or a source that supplies this counterexample and repaired constant.

## Limitations
The corrected estimate is a sufficient condition derived from the coarse bound
\[
\|\Lambda_{ij}\pi_{W_{ij}}f\|
\le
\|\Lambda_{ij}\|\|f\|.
\]
Sharper deletion criteria can depend on the actual restrictions of the operators to the woven subspaces.

The claim does not reassess other theorems or corollaries in the source.

An unindexed note or informal correction could contain the same normalization observation.

## References
1. V. Sadri, G. Rahimlou and R. Ahmadi, *K-G-Fusion Woven in Hilbert Spaces*, TWMS Journal of Applied and Engineering Mathematics 11(3) (2021), 947--958.
2. Y. Huang and Y. Yang, *K-g-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications 2020, 57, DOI 10.1186/s13660-020-02320-0.
3. P. Ghosh and T. K. Samanta, *Weaving continuous controlled K-g-fusion frames in Hilbert spaces*, arXiv:2111.03389v1.
