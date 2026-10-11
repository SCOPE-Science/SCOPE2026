# Weight normalization breaks a minimum-norm \(K\)-fusion resolution theorem

## Finding
Theorem 4.3 of Arabyani Neyshaburi--Arefijamaal claims that the Douglas reduced solution associated with a \(K\)-fusion frame minimizes an unweighted \(\ell^2\)-norm over all \(\ell^2\)-resolutions of \(K\).

The source defines an \(\ell^2\)-resolution \(\{\theta_i\}\) with respect to weights \(\{\omega_i\}\) by
\[
Kf=\sum_i\omega_i^2\theta_i f
\]
and
\[
\sum_i\omega_i^2\|\theta_i f\|^2\le B\|f\|^2.
\]
For the same fusion data, the synthesis operator is
\[
T_W\{x_i\}=\sum_i\omega_i x_i.
\]
Therefore the vector that solves
\[
T_Wx=Kf
\]
is naturally
\[
x=\{\omega_i\theta_i f\}_i,
\]
not
\[
x=\{\theta_i f\}_i.
\]

Take
\[
H=\mathbb C,\qquad K=I,\qquad I=\{1\},\qquad W_1=H,\qquad \omega_1=2.
\]
Then
\[
T_Wx=2x,
\]
so the Douglas reduced solution of
\[
T_WX=I
\]
is
\[
X_w=\frac12I.
\]

Let
\[
\theta_1=\frac14I.
\]
It is a valid \(\ell^2\)-resolution, since
\[
4\theta_1=I
\]
and
\[
4\|\theta_1f\|^2=\frac14\|f\|^2.
\]
The first inequality of Theorem 4.3 would require
\[
\frac14\|f\|^2\le\frac1{16}\|f\|^2,
\]
which fails for every nonzero \(f\).

The same example also falsifies the pseudoinverse formula in Corollary 4.4. The actual pseudoinverse is
\[
(2I)^\dagger=\frac12I,
\]
whereas the displayed formula evaluates to the identity.

## Assumptions and scope
The example uses a one-dimensional Hilbert space, one closed fusion subspace, a positive nonunit weight, and \(K=I\). Hence it lies inside the stated theorem without any convergence, closed-range, or measurability issue.

The finding concerns the weight normalization in the minimum-norm resolution statement and the directly derived pseudoinverse formula. It does not challenge the definition of \(K\)-fusion frame itself or the existence of the Douglas reduced solution.

## Proof
Let \(W=\{(W_i,\omega_i)\}\) be a \(K\)-fusion frame and let \(X_w\) be the reduced solution of
\[
T_WX=K.
\]
For an \(\ell^2\)-resolution \(\{\theta_i\}\), define
\[
\widehat\theta f=\{\omega_i\theta_i f\}_i.
\]
The resolution identity gives
\[
T_W\widehat\theta f
=
\sum_i\omega_i(\omega_i\theta_i f)
=
\sum_i\omega_i^2\theta_i f
=
Kf.
\]

By the Douglas reduced-solution property,
\[
R(X_w)\subseteq\overline{R(T_W^*)}=N(T_W)^\perp.
\]
Every other solution of
\[
T_Wx=Kf
\]
differs from \(X_wf\) by an element of \(N(T_W)\). Therefore
\[
\|X_wf\|\le\|\widehat\theta f\|,
\]
which yields
\[
\|X_wf\|^2
\le
\sum_i\omega_i^2\|\theta_i f\|^2.
\]

Also
\[
T_W^*f=\{\omega_i\pi_{W_i}f\}_i
\]
lies in \(N(T_W)^\perp\). Since
\[
\widehat\theta f-X_wf\in N(T_W),
\]
the vectors
\[
X_wf-T_W^*f
\quad\text{and}\quad
\widehat\theta f-X_wf
\]
are orthogonal. Hence
\[
\|\widehat\theta f-T_W^*f\|^2
=
\|X_wf-T_W^*f\|^2
+
\|\widehat\theta f-X_wf\|^2,
\]
and consequently
\[
\sum_i\|(X_wf)_i-\omega_i\pi_{W_i}f\|^2
\le
\sum_i\omega_i^2\|\theta_i f-\pi_{W_i}f\|^2.
\]

## Verification
The public preprint was inspected at the definition of the \(K\)-fusion synthesis operator, the definition of an \(\ell^2\)-resolution, Theorem 4.3 and its proof, and Corollary 4.4.

The critical proof line defines
\[
\theta f=\{\theta_i f\}_i
\]
and treats
\[
T_W\theta f
\]
as \(Kf\). But the source definitions give
\[
T_W\theta f=\sum_i\omega_i\theta_i f
\]
while the resolution identity is
\[
Kf=\sum_i\omega_i^2\theta_i f.
\]
The discrepancy is exact.

The one-dimensional counterexample was checked algebraically; no numerical approximation is used.

The earliest verified public version is arXiv:1705.00209v1, submitted on 29 April 2017. The journal version was published online on 24 February 2018.

## Relationship to prior work
The reduced solution of an operator factorization is a standard minimum-norm object. The issue here is not the Douglas theorem; it is that the published proof feeds the wrong weighted vector into the fusion synthesis operator.

Earlier fusion-frame minimum-solution arguments use an actual solution of the synthesis equation. They therefore do not justify dropping the weight built into this paper's \(\ell^2\)-resolution definition.

Targeted searches using the exact theorem number, arXiv identifier, DOI, weighted-resolution terminology, minimum-norm formulation, pseudoinverse language, and correction terms did not locate an indexed correction of this weight mismatch.

A nearby result about a resolution-of-identity \(g\)-fusion criterion concerns pointwise square-summability and a closed-graph argument. It neither implies nor repairs this weighted factorization error.

## Limitations
The repaired inequalities above are the direct weighted minimum-norm consequences of the source definitions. No claim is made about a complete replacement for every later formula in the paper that may depend on Theorem 4.3.

The pseudoinverse corollary is disproved by the same one-dimensional example, but a full general reformulation of that corollary is not asserted.

An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. F. Arabyani Neyshaburi and A. A. Arefijamaal, *Characterization and Construction of \(K\)-Fusion Frames and Their Duals in Hilbert Spaces*, arXiv:1705.00209v1, 29 April 2017.
2. F. Arabyani Neyshaburi and A. A. Arefijamaal, *Characterization and Construction of \(K\)-Fusion Frames and Their Duals in Hilbert Spaces*, Results in Mathematics 73 (2018), Article 47, DOI 10.1007/s00025-018-0781-1.
