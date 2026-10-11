# A scalar counterexample to a controlled \(K\)-\(g\)-frame perturbation theorem

## Finding
Theorem 4.1 of Forughi--Osgooei--Rahimi--Javahernia asserts that a family of operators remains a \(CC'\)-controlled \(K\)-\(g\)-frame under a componentwise perturbation involving
\[
\left(C^*\Lambda_i^*\Lambda_iC'-C^*\Theta_i^*\Theta_iC'\right)^{1/2}.
\]
Writing
\[
\eta=\sum_i c_i^2,
\]
the theorem uses \(\eta\), rather than \(\sqrt{\eta}\), in its claimed frame bounds.

The theorem is false already for one scalar coefficient. Let
\[
H=H_1=\mathbb C,\qquad I=\{1\},\qquad C=C'=K=I_H,
\]
and define
\[
\Lambda_1=\frac12 I_H,\qquad \Theta_1=0.
\]
Then
\[
\|\Lambda_1f\|^2=\frac14\|f\|^2=\frac14\|K^*f\|^2,
\]
so \(\Lambda\) is a controlled \(K\)-\(g\)-frame with exact bounds
\[
A_{CC'}=B_{CC'}=\frac14.
\]

Choose
\[
\lambda_1=\lambda_2=0,\qquad c_1=\frac12.
\]
Then
\[
\eta=c_1^2=\frac14
\]
and the source's perturbation hypothesis holds with equality:
\[
\left\|
\left(\Lambda_1^*\Lambda_1-\Theta_1^*\Theta_1\right)^{1/2}f
\right\|
=
\frac12\|f\|
=
c_1\|K^*f\|.
\]
The claimed lower bound is
\[
\left(\sqrt{\frac14}-\frac14\right)^2
=
\frac1{16}.
\]
But the perturbed family is zero:
\[
\|\Theta_1f\|^2=0.
\]
Thus it has no positive lower \(K\)-\(g\)-frame bound. Proposition 4.1 of the same paper is the case \(\lambda_1=\lambda_2=0\), so the same example refutes that proposition as well.

## Assumptions and scope
The counterexample uses the ordinary-frame specialization of the source definitions. All spaces are one-dimensional, all operators under square roots are positive, and there is only one coefficient. Hence there are no convergence, measurability, domain, or noncommutativity issues.

This choice also isolates the coefficient-aggregation error. In this example,
\[
\left(\Lambda_1^*\Lambda_1-\Theta_1^*\Theta_1\right)^{1/2}
=
\left(\Lambda_1^*\Lambda_1\right)^{1/2}
-
\left(\Theta_1^*\Theta_1\right)^{1/2},
\]
so the separate square-root additivity defect in the published proof is not needed to produce the contradiction.

A safe general replacement uses direct differences of the component square roots, rather than square roots of operator differences.

## Proof
For positive operators
\[
A_i=C^*\Lambda_i^*\Lambda_iC',
\qquad
B_i=C^*\Theta_i^*\Theta_iC',
\]
suppose that
\[
\|A_i^{1/2}f-B_i^{1/2}f\|
\le
\lambda_1\|A_i^{1/2}f\|
+
\lambda_2\|B_i^{1/2}f\|
+
c_i\|K^*f\|
\]
for every \(i\) and \(f\). Put
\[
\eta=\sum_i c_i^2.
\]
Define
\[
X(f)=
\left(\sum_i\|A_i^{1/2}f\|^2\right)^{1/2},
\qquad
Y(f)=
\left(\sum_i\|B_i^{1/2}f\|^2\right)^{1/2}.
\]
Taking the \(\ell^2\)-norm over \(i\) and using Minkowski's inequality gives
\[
\left(
\sum_i
\|A_i^{1/2}f-B_i^{1/2}f\|^2
\right)^{1/2}
\le
\lambda_1X(f)+\lambda_2Y(f)+\sqrt{\eta}\,\|K^*f\|.
\]

The triangle inequality in the direct sum yields
\[
Y(f)\le X(f)+
\left(
\sum_i
\|A_i^{1/2}f-B_i^{1/2}f\|^2
\right)^{1/2},
\]
and therefore
\[
(1-\lambda_2)Y(f)
\le
(1+\lambda_1)X(f)+\sqrt{\eta}\,\|K^*f\|.
\]
If \(\Lambda\) has upper bound \(B\), then
\[
X(f)\le \sqrt B\,\|f\|,
\qquad
\|K^*f\|\le\|K\|\,\|f\|,
\]
so
\[
Y(f)\le
\frac{(1+\lambda_1)\sqrt B+\sqrt{\eta}\,\|K\|}
{1-\lambda_2}
\|f\|.
\]

Likewise,
\[
X(f)\le Y(f)+
\left(
\sum_i
\|A_i^{1/2}f-B_i^{1/2}f\|^2
\right)^{1/2}
\]
implies
\[
(1+\lambda_2)Y(f)
\ge
(1-\lambda_1)X(f)-\sqrt{\eta}\,\|K^*f\|.
\]
Using
\[
X(f)\ge\sqrt A\,\|K^*f\|
\]
gives
\[
Y(f)\ge
\frac{(1-\lambda_1)\sqrt A-\sqrt{\eta}}
{1+\lambda_2}
\|K^*f\|.
\]
Hence, whenever
\[
(1-\lambda_1)\sqrt A>\sqrt{\eta},
\]
the perturbed family is a controlled \(K\)-\(g\)-frame with the squared lower and upper constants displayed in the finding.

For the source theorem's scalar example, the correct margin is
\[
\sqrt A-\sqrt{\eta}
=
\frac12-\frac12
=
0,
\]
so this valid criterion correctly gives no positive lower bound.

## Verification
The publisher PDF was inspected at the complete statement and proof of Theorem 4.1 and at Proposition 4.1. The theorem defines
\[
\eta=\sum_i c_i^2
\]
but inserts \(\eta\) directly into the claimed norm-level bounds. Its proof also writes the square root of an operator difference as though it were a difference of square roots, an identity that does not hold for general positive operators.

The scalar witness was checked directly from the definitions. Every source hypothesis used in the counterexample is satisfied exactly, while the conclusion fails for every nonzero vector.

The paper lists primary MSC \(42C15\). The earliest public full-text source verified to a calendar day is the author-uploaded copy dated 1 June 2020. The journal issue metadata gives only a coarser 2020 publication label, so it is not used to invent an earlier day-level date.

## Relationship to prior work
Najati--Faroughi--Rahimi's 2008 stability theorem for \(g\)-frames uses a global perturbation estimate at the synthesis-operator level and a genuine smallness condition. Its proof preserves the square-root scale of the frame lower bound. That theorem does not contain the source-specific component-square-root hypothesis or the erroneous use of \(\eta=\sum_i c_i^2\) as a norm-level quantity.

Classical frame perturbation results of Casazza--Christensen likewise compare perturbation size with the square root of the lower frame bound. The controlled \(K\)-frame literature also treats quantitative perturbation as a norm-level problem.

A separate result already known for the same 2020 paper concerns a complex inner-product identity in its dual-frame section. That statement is logically independent of the perturbation theorem here: neither the earlier identity correction nor its proof implies the scalar perturbation counterexample or the corrected \(\sqrt{\eta}\) aggregation.

Targeted searches using the exact title, DOI, theorem number, proposition number, perturbation terminology, and \(\eta\)-aggregation language did not locate an indexed correction of Theorem 4.1.

## Limitations
The direct-square-root-difference theorem proved here is a safe replacement, not a claim that the source's original square-root-of-difference hypothesis can always be repaired merely by replacing \(\eta\) with \(\sqrt{\eta}\). Without additional order or commutation assumptions, a square root of an operator difference is not the difference of the two square roots.

No claim is made about unrelated theorems in the source.

An unindexed erratum, thesis remark, or informal correction may contain the same counterexample or diagnosis.

## References
1. M. Forughi, E. Osgooei, A. Rahimi and M. Javahernia, *Operators on controlled \(K\)-\(g\)-frames in Hilbert spaces*, Proceedings of the Institute of Mathematics and Mechanics 46(1) (2020), 102--114, DOI 10.29228/proc.21.
2. A. Najati, M. H. Faroughi and A. Rahimi, *\(g\)-frames and stability of \(g\)-frames in Hilbert spaces*, Methods of Functional Analysis and Topology 14(3) (2008), 271--286.
3. P. G. Casazza and O. Christensen, *Perturbation of operators and application to frame theory*, Journal of Fourier Analysis and Applications 3(5) (1997), 543--557.
4. D. Hua and Y. Huang, *Controlled \(K\)-\(g\)-Frames in Hilbert Spaces*, Results in Mathematics 72 (2017), 1227--1238, DOI 10.1007/s00025-016-0613-0.
