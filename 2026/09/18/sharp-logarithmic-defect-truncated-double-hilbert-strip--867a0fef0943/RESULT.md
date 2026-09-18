# Sharp logarithmic defect for a truncated double-Hilbert strip

## Statement

Let
\[
{\bf H}=\mathcal H_2\mathcal H_1
\]
be the double Hilbert transform on \(L^2(\mathbb R^2)\), and for
\(0<\varepsilon<1\) let
\[
V_\varepsilon
=
\{(x_1,x_2)\in\mathbb R^2:
|x_1-x_2|<\varepsilon,\ |x_2|<1\}.
\]
Write
\[
R(\varepsilon)
=
\frac{\|({\bf H}-I)\chi_{V_\varepsilon}\|_2}
     {\|\chi_{V_\varepsilon}\|_2}.
\]

Then \(R(\varepsilon)^2\) has the convergent expansion
\[
\boxed{
R(\varepsilon)^2
=
\frac{4}{\pi^2}\varepsilon\log\frac1\varepsilon
+
\frac{10}{\pi^2}\varepsilon
-
\frac{8}{\pi^2}
\sum_{k=1}^{\infty}
\frac{\varepsilon^{2k+1}}
{2k(2k+1)^2(2k+2)}
}
\qquad(0<\varepsilon<1).
\]
In particular,
\[
\boxed{
R(\varepsilon)
\sim
\frac{2}{\pi}
\sqrt{\varepsilon\log\frac1\varepsilon}
}
\qquad(\varepsilon\downarrow0),
\]
and more precisely
\[
R(\varepsilon)^2
=
\frac{4}{\pi^2}\varepsilon\log\frac1\varepsilon
+
\frac{10}{\pi^2}\varepsilon
-
\frac{1}{9\pi^2}\varepsilon^3
+O(\varepsilon^5).
\]

Thus the logarithmic factor in the continuous truncated-strip example of
Abakumov--Domelevo--Petermichl--Poltoratski is sharp. It is not an artifact of
their upper estimate.

More generally, for \(a,L>0\),
\[
V_{\varepsilon,a,L}
=
\{(x,y): |x-a y|<\varepsilon,\ |y|<L\},
\qquad
\delta=\frac{\varepsilon}{aL},
\]
positive coordinate dilations give the exact identity
\[
\frac{\|({\bf H}-I)\chi_{V_{\varepsilon,a,L}}\|_2}
{\|\chi_{V_{\varepsilon,a,L}}\|_2}
=
R(\delta).
\]
Hence the same expansion holds with \(\varepsilon\) replaced by the
dimensionless aspect ratio \(\delta\), whenever \(0<\delta<1\).

## Context

Abakumov, Domelevo, Petermichl and Poltoratski introduced the bounded truncated
strip \(V_\varepsilon\) as an \(L^2\) approximate eigenvector for eigenvalue
\(1\) of the double Hilbert transform. Their proof gives
\[
R(\varepsilon)\lesssim
\sqrt{\varepsilon|\log\varepsilon|}.
\]
They also construct a dyadic analogue of width \(2^{-n}\) whose defect ratio is
exactly
\[
2\sqrt{2^{-n}},
\]
and explicitly point out the absence of the logarithmic term in the dyadic
model. The present calculation determines the continuous defect exactly enough
to show that this contrast is genuine.

## Fourier reduction

Use the unitary Fourier-transform normalization
\[
\widehat f(\xi)
=
\frac1{2\pi}\int_{\mathbb R^2}
f(x)e^{-ix\cdot\xi}\,dx.
\]
For the strip,
\[
\widehat{\chi_{V_\varepsilon}}(\xi_1,\xi_2)
=
\frac{2}{\pi}\,
\frac{\sin(\varepsilon\xi_1)}{\xi_1}\,
\frac{\sin(\xi_1+\xi_2)}{\xi_1+\xi_2}.
\]

The multiplier of \({\bf H}\) equals \(-1\) in the first and third quadrants
and \(+1\) in the second and fourth quadrants. Therefore
\(({\bf H}-I)\) vanishes on the opposite-sign quadrants and has multiplier
\(-2\) on the same-sign quadrants.

By symmetry, if
\[
J(\varepsilon)
=
\int_0^\infty
\frac{\sin^2(\varepsilon t)}{t^2}
K(t)\,dt,
\qquad
K(t)=
\int_t^\infty\frac{\sin^2 p}{p^2}\,dp,
\]
then the first-quadrant Fourier energy is
\[
Q_\varepsilon=\frac4{\pi^2}J(\varepsilon).
\]
Since
\[
|V_\varepsilon|=4\varepsilon,
\]
Plancherel gives
\[
\boxed{
R(\varepsilon)^2
=
\frac{8}{\pi^2\varepsilon}J(\varepsilon).
}
\]

## Exact second derivative

For \(0<\varepsilon<1\), Abel regularization (insert \(e^{-\eta t}\), then let
\(\eta\downarrow0\)) justifies differentiating and interchanging the oscillatory
integrals below. We obtain
\[
\begin{aligned}
J''(\varepsilon)
&=
2\int_0^\infty \cos(2\varepsilon t)K(t)\,dt\\
&=
\frac1{\varepsilon}
\int_0^\infty
\frac{\sin^2 p}{p^2}\sin(2\varepsilon p)\,dp\\
&=
\frac1{\varepsilon}
\int_0^\infty
\frac{(1-\cos x)\sin(\varepsilon x)}{x^2}\,dx.
\end{aligned}
\]
Set
\[
A(\varepsilon)
=
\int_0^\infty
\frac{(1-\cos x)\sin(\varepsilon x)}{x^2}\,dx.
\]
Then
\[
A'(\varepsilon)
=
\int_0^\infty
\frac{(1-\cos x)\cos(\varepsilon x)}{x}\,dx.
\]
Using
\[
\cos x\cos(\varepsilon x)
=
\frac12\cos((1-\varepsilon)x)
+
\frac12\cos((1+\varepsilon)x)
\]
and the Abel-regularized Frullani identity
\[
\int_0^\infty
\frac{\cos(ax)-\cos(bx)}{x}\,dx
=
\log\frac ba
\qquad(a,b>0),
\]
we get
\[
A'(\varepsilon)
=
\frac12\log\frac{1-\varepsilon^2}{\varepsilon^2}.
\]
Because \(A(0)=0\),
\[
A(\varepsilon)
=
-\varepsilon\log\varepsilon
+
\frac12\Big[
(1+\varepsilon)\log(1+\varepsilon)
-
(1-\varepsilon)\log(1-\varepsilon)
\Big].
\]
Consequently,
\[
\boxed{
J''(\varepsilon)
=
-\log\varepsilon
+
\frac{
(1+\varepsilon)\log(1+\varepsilon)
-
(1-\varepsilon)\log(1-\varepsilon)
}{2\varepsilon}.
}
\]

## Convergent expansion

For \(|\varepsilon|<1\),
\[
\frac{
(1+\varepsilon)\log(1+\varepsilon)
-
(1-\varepsilon)\log(1-\varepsilon)
}{2\varepsilon}
=
1-
\sum_{k=1}^{\infty}
\frac{\varepsilon^{2k}}{2k(2k+1)}.
\]
Moreover \(J(0)=J'(0)=0\). Integrating the preceding identity twice therefore
gives
\[
\boxed{
J(\varepsilon)
=
\frac12\varepsilon^2\log\frac1\varepsilon
+
\frac54\varepsilon^2
-
\sum_{k=1}^{\infty}
\frac{\varepsilon^{2k+2}}
{2k(2k+1)^2(2k+2)}.
}
\]
Substitution into
\[
R(\varepsilon)^2=\frac8{\pi^2\varepsilon}J(\varepsilon)
\]
proves the stated formula.

The first omitted term is
\[
-\frac{\varepsilon^4}{72}
\]
in \(J(\varepsilon)\), hence
\[
-\frac{\varepsilon^3}{9\pi^2}
\]
in \(R(\varepsilon)^2\).

## Positive-slope strips

Let
\[
(x,y)=(aL X,LY).
\]
Then
\[
V_{\varepsilon,a,L}
\longmapsto
\{(X,Y):|X-Y|<\delta,\ |Y|<1\},
\qquad
\delta=\frac{\varepsilon}{aL}.
\]
The Hilbert transform in each coordinate commutes, up to the corresponding
unitary normalization, with positive dilations. Therefore the normalized
\(L^2\) defect is unchanged, proving the claimed reduction to \(R(\delta)\).

## Continuous versus dyadic truncation

At matched small width \(\delta\), the continuous strip has
\[
R_{\rm cont}(\delta)
\sim
\frac2\pi\sqrt{\delta\log(1/\delta)},
\]
whereas the dyadic construction of Abakumov--Domelevo--Petermichl--Poltoratski
has the exact defect
\[
R_{\rm dyad}(\delta)=2\sqrt{\delta}
\]
at dyadic widths. Hence
\[
\frac{R_{\rm cont}(\delta)}{R_{\rm dyad}(\delta)}
\sim
\frac1\pi\sqrt{\log(1/\delta)}
\]
along dyadic \(\delta\downarrow0\). The logarithmic separation is therefore an
actual feature of these two natural truncations.

## Relation to prior work and originality boundary

The source paper proves the upper bound
\[
R(\varepsilon)\lesssim
\sqrt{\varepsilon|\log\varepsilon|}
\]
and gives the exact dyadic defect. It does not state the matching lower
asymptotic, the constant \(2/\pi\), or the convergent expansion above in the
inspected version.

The Fourier representation of the strip, Plancherel reduction, elementary
Frullani identity, and dilation covariance are standard and are not claimed as
new. The claimed contribution is the sharp evaluation of the defect for the
newly introduced truncated-strip quasi-eigenvector, including its exact
convergent small-width expansion and the resulting proof that the continuous
logarithmic loss is intrinsic.

Searches using the source title and identifier together with variants of
`sharp rate`, `strip defect`, `approximate eigenvector`, `epsilon log epsilon`,
and `double Hilbert transform` found no prior statement of this asymptotic.
Because the source preprint is very recent, an unindexed contemporaneous
observation remains a residual originality risk.

## Limitations

- The result evaluates the specific truncated-strip family above; it is not a
  stability theorem classifying arbitrary approximate invariant sets.
- The positive-slope generalization follows only from positive coordinate
  dilations of the same geometry.
- No assertion is made that the same logarithmic rate is optimal among all
  finite-measure approximate eigenvectors.
- The source preprint is recent, so contemporaneous unindexed work remains a
  residual originality risk.
- No independent validation is asserted.

## Reference

Evgeny Abakumov, Komla Domelevo, Stefanie Petermichl, and Alexei Poltoratski,
*Invariant sets of the double Hilbert transform*, arXiv:2609.15155v1 (2026).
https://arxiv.org/abs/2609.15155v1

**Same-model review: passed. Cross-model review: not yet performed.**
