# Sharp radial-defect strengthening of the boundary Tang--Zhang inequality

## Finding

Let \(p\) be a polynomial of degree \(n\ge2\) whose zeros lie in the closed unit disk. Let \(a\) be a simple zero of \(p\) with
\[
|a|=1.
\]
Write the remaining zeros, counted with multiplicity, as
\[
z_1,\ldots,z_{n-1},
\]
and let
\[
\zeta_1,\ldots,\zeta_{n-1}
\]
be the critical points of \(p\), also counted with multiplicity.

Define the boundary radial defect
\[
\Delta_a(p)
=
\sum_{k=1}^{n-1}
\frac{1-|z_k|^2}{|a-z_k|^2}.
\]
Every summand is nonnegative. Then
\[
\sum_{j=1}^{n-1}
\frac{1}{|a-\zeta_j|^2}
\ge
\frac{(n-1+\Delta_a(p))^2}{n-1}.
\]
Equivalently,
\[
\sum_{j=1}^{n-1}
\frac{1}{|a-\zeta_j|^2}
\ge
(n-1)+2\Delta_a(p)
+
\frac{\Delta_a(p)^2}{n-1}.
\]

The inequality is sharp. Equality holds exactly when there are constants \(C\ne0\) and \(0<r\le1\) such that
\[
p(z)
=
C\left((z-(1-r)a)^n-(ra)^n\right).
\]
Thus the equality configurations are regular \(n\)-gons of zeros obtained by translating and radially shrinking the unit-circle extremizer while keeping the distinguished vertex \(a\) fixed.

As a direct consequence,
\[
\min_{1\le j\le n-1}|a-\zeta_j|
\le
\frac{n-1}{n-1+\Delta_a(p)}.
\]
This is strictly stronger than the unit Sendov radius whenever at least one companion zero lies strictly inside the unit disk.

## Assumptions and scope

The distinguished boundary zero is assumed simple. If \(a\) is also a critical point, the reciprocal-distance sum in the quadratic Tang--Zhang inequality is infinite, so that case has a different trivial normalization and is not included in the finite defect formula above.

The defect
\[
\Delta_a(p)
=
\sum_{k=1}^{n-1}
\frac{1-|z_k|^2}{|a-z_k|^2}
\]
is conformally natural for this boundary calculation: after rotating \(a\) to \(1\), each summand is exactly the excess in the elementary identity
\[
2\operatorname{Re}\frac{1}{1-w}
=
1+rac{1-|w|^2}{|1-w|^2}.
\]

No claim is made here for an interior distinguished zero \(|a|<1\). The theorem is a boundary refinement of the recent quadratic Tang--Zhang inequality.

## Proof

Factor
\[
p(z)=(z-a)Q(z),
\qquad
Q(z)=C\prod_{k=1}^{n-1}(z-z_k).
\]
Since \(a\) is simple,
\[
Q(a)=p'(a)\ne0.
\]
Differentiating the factorization at \(a\) gives
\[
\frac{p''(a)}{p'(a)}
=
2\frac{Q'(a)}{Q(a)}
=
2\sum_{k=1}^{n-1}\frac{1}{a-z_k}.
\]
On the other hand, because
\[
p'(z)=B\prod_{j=1}^{n-1}(z-\zeta_j)
\]
for some \(B\ne0\), its logarithmic derivative gives
\[
\frac{p''(a)}{p'(a)}
=
\sum_{j=1}^{n-1}\frac{1}{a-\zeta_j}.
\]
Therefore
\[
\sum_{j=1}^{n-1}\frac{a}{a-\zeta_j}
=
2\sum_{k=1}^{n-1}\frac{a}{a-z_k}.
\]

For each companion zero put
\[
w_k=\overline a z_k.
\]
Since \(|a|=1\), one has \(|w_k|=|z_k|\) and
\[
\frac{a}{a-z_k}
=
\frac{1}{1-w_k}.
\]
The exact identity
\[
2\operatorname{Re}\frac{1}{1-w_k}
=
1+rac{1-|w_k|^2}{|1-w_k|^2}
\]
then yields
\[
2\operatorname{Re}\frac{a}{a-z_k}
=
1+rac{1-|z_k|^2}{|a-z_k|^2}.
\]
Summing gives the boundary communication identity
\[
\operatorname{Re}
\sum_{j=1}^{n-1}\frac{a}{a-\zeta_j}
=
n-1+\Delta_a(p).
\]

Now set
\[
u_j=\frac{a}{a-\zeta_j}.
\]
Because \(|a|=1\),
\[
|u_j|=\frac{1}{|a-\zeta_j|}.
\]
Cauchy--Schwarz and the preceding exact real-part identity give
\[
\sum_{j=1}^{n-1}|u_j|^2
\ge
\frac1{n-1}
\left|\sum_{j=1}^{n-1}u_j\right|^2
\ge
\frac1{n-1}
\left(
\operatorname{Re}\sum_{j=1}^{n-1}u_j
\right)^2.
\]
Hence
\[
\sum_{j=1}^{n-1}\frac1{|a-\zeta_j|^2}
\ge
\frac{(n-1+\Delta_a(p))^2}{n-1}.
\]

For the nearest-critical-point consequence, the largest reciprocal distance is at least the root-mean-square reciprocal distance:
\[
\max_j\frac1{|a-\zeta_j|}
\ge
\left(
\frac1{n-1}
\sum_{j=1}^{n-1}\frac1{|a-\zeta_j|^2}
\right)^{1/2}
\ge
\frac{n-1+\Delta_a(p)}{n-1}.
\]
Taking reciprocals gives the claimed radius bound.

It remains to classify equality. Equality in the two inequalities above requires all \(u_j\) to be equal and their common value to be a positive real number. Write
\[
u_1=\cdots=u_{n-1}=u>0.
\]
Then all critical points coincide at
\[
c=a\left(1-\frac1u\right),
\]
so
\[
p'(z)=B(z-c)^{n-1}
\]
and therefore
\[
p(z)=C\left((z-c)^n-(a-c)^n\right).
\]
Put
\[
r=\frac{a-c}{a}=\frac1u>0.
\]
Then
\[
c=(1-r)a
\]
and
\[
p(z)=C\left((z-(1-r)a)^n-(ra)^n\right).
\]
Its zeros are
\[
a\bigl((1-r)+r\omega\bigr),
\qquad
\omega^n=1.
\]
For every \(n\)-th root of unity \(\omega\),
\[
\left|(1-r)+r\omega\right|^2
=
1-2r(1-r)(1-\operatorname{Re}\omega).
\]
If \(0<r\le1\), every zero lies in the closed unit disk. If \(r>1\), every nontrivial root of unity produces modulus strictly larger than one. Thus the disk condition is equivalent to
\[
0<r\le1,
\]
and the equality classification is complete.

## Verification

The proof is entirely algebraic and uses no numerical approximation.

The critical normalization was independently checked in two ways. First, the identity
\[
\frac{p''(a)}{p'(a)}
=
2\sum_{k=1}^{n-1}\frac1{a-z_k}
=
\sum_{j=1}^{n-1}\frac1{a-\zeta_j}
\]
follows from the two factorizations of \(p\) and \(p'\). Second, for the equality family the unique critical point is
\[
(1-r)a
\]
with multiplicity \(n-1\), so the left side is
\[
\frac{n-1}{r^2}.
\]
The exact boundary identity then forces
\[
n-1+\Delta_a(p)=\frac{n-1}{r},
\]
and the right side of the theorem is again
\[
\frac{n-1}{r^2}.
\]

The disk containment of the equality family is exact from
\[
\left|(1-r)+r\omega\right|^2
=
1-2r(1-r)(1-\operatorname{Re}\omega).
\]
No finite experiment is used as evidence for the infinite statement.

## Relationship to prior work

Zhang's 2026 quadratic Tang--Zhang theorem proves, for every zero \(a\) of a polynomial whose zeros lie in the closed unit disk,
\[
\sum_{j=1}^{n-1}\frac1{|a-\zeta_j|^2}
\ge n-1,
\]
with equality only for a scalar multiple of a rotated binomial \(z^n-\omega\). Its boundary proof invokes the classical Meir--Sharma real-part inequality and then applies Cauchy--Schwarz. The paper does not retain the positive excess contributed by zeros lying strictly inside the unit disk.

The present result keeps that discarded excess exactly. The elementary identity
\[
2\operatorname{Re}\frac1{1-w}
=
1+rac{1-|w|^2}{|1-w|^2}
\]
turns the boundary real-part estimate into an equality with defect \(\Delta_a(p)\). This produces both the strengthened quadratic bound and a larger equality family consisting of inward-translated regular polygons. When \(r=1\), the defect vanishes and the family reduces to the equality case of Zhang's global theorem.

Meir and Sharma's 1969 argument is the classical source of the boundary mean-real-part inequality used in the recent paper. The inspected formula gives the nonnegative boundary contribution after taking real parts, but the quadratic defect refinement and its translated-polygon equality classification are not stated there in the inspected material.

Tao's 2026 exposition of the Sendov proof also derives the boundary logarithmic-derivative communication identity, but uses only the coarser estimate
\[
\operatorname{Re}\frac1{1-z}\ge\frac12
\]
for \(|z|\le1\). The defect term retained here is the exact amount lost in that final inequality.

## Limitations

The theorem applies only to a simple distinguished boundary zero. It is not an interior-zero refinement of the full quadratic Tang--Zhang theorem.

The nearest-critical-point consequence is sharp on the displayed equality family, but no further geometric localization of the remaining critical points is claimed.

Older boundary Sendov literature contains several refined localization theorems. Targeted comparison found no statement equivalent to the defect-corrected reciprocal-square inequality, but differently phrased historical coverage remains a residual literature risk.

## References

1. T. Zhang, *Beyond Sendov's conjecture: the quadratic Tang--Zhang inequality*, arXiv:2609.19126v1, 2026.
2. A. Meir and A. Sharma, *On Ilyeff's conjecture*, Pacific Journal of Mathematics 31 (1969), 459--467, DOI:10.2140/pjm.1969.31.459.
3. T. Tao, *A digestion of the proof of Sendov's conjecture*, 2026.
