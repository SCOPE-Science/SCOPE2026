# Weight-uniform Frazer bounds across the full weighted Bergman range

## Finding

Let
\[
1<p<\infty,
\qquad
-1<\alpha<\infty,
\]
and let
\[
f=h+\overline g\in a_\alpha^p(\mathbb D)
\]
be canonically normalized by
\[
g(0)=0
\]
and satisfy
\[
f(0)=0.
\]
Let \(D_0,D_1\) be two diameters meeting at an acute angle
\[
0\le\theta\le\frac{\pi}{2}.
\]

Then
\[
\sum_{j=0}^1
\int_{D_j}
|f(z)|^p(1-|z|^2)^{\alpha+1}\,|dz|
\le
\widetilde A_p(\theta)\,
\|f\|_{a_\alpha^p}^p,
\]
where
\[
\widetilde A_p(\theta)
=
\frac{2^{1+p/2}\pi}
{
\bigl(
\sin(\theta/2)+\cos(\theta/2)
\bigr)
\bigl(
1-|\cos(\pi/p)|
\bigr)^{p/2}
}.
\]

The bound is independent of the weight parameter \(\alpha\). In the range
\[
\alpha\ge0,
\]
the 2026 weighted harmonic Frazer theorem gives the same expression multiplied by
\[
2^\alpha.
\]
Thus the new estimate removes that entire exponential weight loss. It also extends the two-diameter inequality to the natural remaining range
\[
-1<\alpha<0.
\]

The mechanism is the sharp radial-kernel inequality
\[
\int_\rho^1
(1-u^2)^\alpha\,du
\ge
\frac{
(1-\rho^2)^{\alpha+1}
}{
2(\alpha+1)
},
\qquad
0\le\rho<1.
\]

## Assumptions and scope

The normalized weighted area measure is
\[
dA_\alpha(z)
=
(\alpha+1)
(1-|z|^2)^\alpha
\,dA(z),
\]
where \(dA\) is normalized planar area measure. The weighted harmonic Bergman norm is
\[
\|f\|_{a_\alpha^p}^p
=
\int_{\mathbb D}
|f(z)|^p\,dA_\alpha(z).
\]

The sum over \(D_0,D_1\) uses the same two-diameter multiplicity convention as Frazer's inequality. When the two diameters coincide, the resulting statement is equivalent to the corresponding one-diameter estimate after dividing by two.

The theorem gives a strictly better explicit upper constant and a larger weight range. It does not assert that the displayed constant is the exact operator norm.

## Proof

The source proof reduces the weighted two-diameter problem to a one-dimensional radial kernel. We keep that reduction and sharpen only the kernel step.

For
\[
-1<\alpha<\infty
\]
and
\[
0\le\rho<1,
\]
define
\[
\kappa_\alpha(\rho)
=
\int_\rho^1
(1-u^2)^\alpha\,du.
\]
Set
\[
H_\alpha(\rho)
=
\kappa_\alpha(\rho)
-
\frac{
(1-\rho^2)^{\alpha+1}
}{
2(\alpha+1)
}.
\]
Differentiation gives
\[
H_\alpha'(\rho)
=
-(1-\rho^2)^\alpha
+
\rho(1-\rho^2)^\alpha
=
-(1-\rho)(1-\rho^2)^\alpha
<
0
\]
for
\[
0\le\rho<1.
\]
Moreover,
\[
\lim_{\rho\uparrow1}
H_\alpha(\rho)
=
0.
\]
Hence
\[
H_\alpha(\rho)>0
\]
for every
\[
0\le\rho<1,
\]
which proves
\[
\kappa_\alpha(\rho)
\ge
\frac{
(1-\rho^2)^{\alpha+1}
}{
2(\alpha+1)
}.
\]

The constant is best possible. Indeed, l'Hospital's rule gives
\[
\lim_{\rho\uparrow1}
\frac{
\kappa_\alpha(\rho)
}{
(1-\rho^2)^{\alpha+1}
}
=
\frac1{2(\alpha+1)}.
\]

Now follow the source's notation. Let
\[
F(z)
=
\bigl(
|h(z)|+|g(z)|
\bigr)^p
\]
and let \(I\) be the auxiliary radial integral obtained after multiplying Frazer's boundary estimate by
\[
r(1-r^2)^\alpha
\]
and integrating in \(r\). The source's Fubini change of variables yields
\[
I
=
\sum_{j=0}^1
\left[
\int_0^1
F(\rho\xi_j)\kappa_\alpha(\rho)\,d\rho
+
\int_{-1}^0
F(\rho\xi_j)\kappa_\alpha(-\rho)\,d\rho
\right].
\]
Applying the sharp kernel bound to both signs gives
\[
I
\ge
\frac1{2(\alpha+1)}
\sum_{j=0}^1
\int_{-1}^1
F(\rho\xi_j)
(1-\rho^2)^{\alpha+1}
\,d\rho.
\]
Since
\[
|f|
\le
|h|+|g|,
\]
we obtain
\[
I
\ge
\frac1{2(\alpha+1)}
\sum_{j=0}^1
\int_{D_j}
|f(z)|^p
(1-|z|^2)^{\alpha+1}
\,|dz|.
\]

On the other hand, the weighted Frazer reduction preceding this kernel step gives
\[
I
\le
\frac{
\pi
}{
(\alpha+1)
\bigl(
\sin(\theta/2)+\cos(\theta/2)
\bigr)
}
\int_{\mathbb D}
\bigl(
|h|+|g|
\bigr)^p
\,dA_\alpha.
\]
Combining the last two estimates cancels the factor \(\alpha+1\):
\[
\sum_{j=0}^1
\int_{D_j}
|f(z)|^p
(1-|z|^2)^{\alpha+1}
\,|dz|
\le
\frac{
2\pi
}{
\sin(\theta/2)+\cos(\theta/2)
}
\int_{\mathbb D}
\bigl(
|h|+|g|
\bigr)^p
\,dA_\alpha.
\]

For all complex numbers \(a,b\),
\[
(|a|+|b|)^p
\le
2^{p/2}
(|a|^2+|b|^2)^{p/2}.
\]
The weighted harmonic Riesz estimate used in the source gives
\[
\int_{\mathbb D}
(|h|^2+|g|^2)^{p/2}
\,dA_\alpha
\le
\frac1{
\bigl(
1-|\cos(\pi/p)|
\bigr)^{p/2}
}
\int_{\mathbb D}
|h+\overline g|^p
\,dA_\alpha.
\]
Substitution gives exactly
\[
\widetilde A_p(\theta)
=
\frac{2^{1+p/2}\pi}
{
\bigl(
\sin(\theta/2)+\cos(\theta/2)
\bigr)
\bigl(
1-|\cos(\pi/p)|
\bigr)^{p/2}
}.
\]

Every step remains valid for
\[
-1<\alpha<0:
\]
the radial weight is integrable, the weighted Bergman norm and the weighted Riesz estimate are defined on the full range
\[
-1<\alpha<\infty,
\]
and the sharp kernel inequality above holds without any sign restriction on \(\alpha\) beyond integrability.

## Verification

The central kernel inequality is exact. Its derivative defect is
\[
-(1-\rho)(1-\rho^2)^\alpha,
\]
which has a fixed sign throughout the stated range. Its constant is certified by the endpoint ratio
\[
\frac1{2(\alpha+1)}.
\]

The primary source was inspected through the statement and proof of its weighted harmonic two-diameter theorem. Its proof introduces the same kernel
\[
\kappa_\alpha(\rho)
=
\int_\rho^1
(1-u^2)^\alpha\,du
\]
and bounds it below by
\[
\frac{
(1-\rho^2)^{\alpha+1}
}{
(\alpha+1)2^{\alpha+1}
}
\]
after using an inequality that is restricted to nonnegative \(\alpha\). Replacing exactly that step by the sharp bound above changes no other part of the argument.

The source's remaining ingredients were checked in the same full text: the two-diameter Hardy/Frazer reduction and the weighted harmonic Riesz estimate. No numerical experiment or asymptotic extrapolation is used to prove the theorem.

## Relationship to prior work

Halder and Kumar's 2026 paper establishes Gabriel and Frazer inequalities in weighted analytic and harmonic Bergman spaces. Its two-diameter harmonic theorem is stated for
\[
\alpha\ge0
\]
and its proof yields a constant containing the factor
\[
2^\alpha.
\]
The present result identifies that factor as an artifact of a nonsharp radial-kernel comparison. The optimal kernel constant removes it and simultaneously restores the entire natural Bergman range
\[
-1<\alpha<\infty.
\]

The authors' companion weighted Riesz–Fejér paper already treats weighted harmonic Bergman spaces for
\[
-1<\alpha<\infty
\]
and supplies the weight-independent harmonic Riesz estimate used here. That one-diameter theory does not itself imply a two-diameter Frazer estimate, because the latter requires the angular Frazer reduction and the radial kernel.

Classical Frazer inequalities and their harmonic Hardy analogues contain the angular factor
\[
\bigl(
\sin(\theta/2)+\cos(\theta/2)
\bigr)^{-1}
\]
but do not contain the weighted radial kernel. Targeted searches using the source identifier, weighted two-diameter terminology, the kernel \(\kappa_\alpha\), and the removal of the \(2^\alpha\) factor did not locate a published statement of this weight-uniform improvement.

## Limitations

The sharpness proved here is the sharpness of the radial-kernel constant, not of the full two-diameter Bergman operator constant.

The theorem retains the source assumptions
\[
1<p<\infty
\]
and
\[
f(0)=0.
\]
No endpoint claim for
\[
p=1
\]
is made.

The argument is specific to the two-diameter Frazer reduction and does not automatically sharpen the arbitrary-convex-curve Gabriel constant.

## References

1. H. Halder and R. Kumar, *Gabriel's and Frazer's problems for weighted Bergman spaces and their applications*, arXiv:2607.13543v1, 2026.
2. H. Halder and R. Kumar, *Riesz Theorem and Riesz-Fejér inequality for weighted harmonic Bergman spaces with applications to Möbius invariant spaces*, arXiv:2607.11795v1, 2026.
3. H. G. Frazer, classical two-diameter extension of the Riesz–Fejér inequality, as stated and used in the primary source.
