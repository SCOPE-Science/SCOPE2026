# Exact quadratic tangency and cubic correction for the Koumandos–Ruscheweyh threshold

## Finding

For
\[
0<\rho\le1,
\]
define
\[
I(\mu,\rho)
=
\int_0^{(1+\rho)\pi}
t^{\mu-1}\sin(t-\rho\pi)\,dt,
\]
and let
\[
\nu(\rho)=\mu^*(\rho)
\]
be the unique zero of
\[
I(\cdot,\rho)
\]
in
\[
(0,1].
\]
The recent proof of the Koumandos–Ruscheweyh conjecture shows that this \(\nu(\rho)\) is exactly the optimal parameter for the corresponding subordination and positive-real-part inequalities.

Set
\[
J_0
=
\gamma+\log(2\pi)-\operatorname{Ci}(2\pi),
\]
where \(\gamma\) is Euler's constant and
\[
\operatorname{Ci}(x)
=
\gamma+\log x+
\int_0^x
\frac{\cos t-1}{t}\,dt.
\]
Then the optimal curve has the endpoint expansion
\[
1-\nu(\rho)
=
\frac{\pi^2}{2J_0}(1-\rho)^2
-
\frac{\pi^3\operatorname{Si}(2\pi)}
{2J_0^2}(1-\rho)^3
+
O\!\left((1-\rho)^4\right)
\]
as
\[
\rho\uparrow1,
\]
where
\[
\operatorname{Si}(x)
=
\int_0^x
\frac{\sin t}{t}\,dt.
\]

Numerically,
\[
J_0
=
2.437653393057224\ldots,
\]
\[
\frac{\pi^2}{2J_0}
=
2.024406839216634\ldots,
\]
and
\[
-\frac{\pi^3\operatorname{Si}(2\pi)}
{2J_0^2}
=
-3.699971396358804\ldots.
\]

In particular,
\[
\lim_{\rho\uparrow1}
\frac{1-\nu(\rho)}
{(1-\rho)^2}
=
\frac{\pi^2}{2J_0}.
\]
Thus the source's certified endpoint bracket
\[
1.99(1-\rho)^2
<
1-\nu(\rho)
<
2.05(1-\rho)^2
\]
has an exact limiting coefficient, and the first correction is cubic and negative.

## Assumptions and scope

The definition of
\[
\nu(\rho)
\]
and its interpretation as the optimal Koumandos–Ruscheweyh parameter are those of arXiv:2610.02285v1.

The expansion is one-sided at
\[
\rho=1.
\]
It concerns only the optimal parameter curve itself. It does not change the all-degree subordination theorem, its finite certificates, or the source's computer-assisted verification.

The functions \(\operatorname{Ci}\) and \(\operatorname{Si}\) are normalized by the displayed integral definitions. No claim is made that the fourth-order coefficient has been computed.

## Proof

Write
\[
\varepsilon=1-\rho,
\qquad
p=1-\nu(\rho).
\]
The source proves that, for all sufficiently small positive \(\varepsilon\),
\[
1.99\,\varepsilon^2
<
p
<
2.05\,\varepsilon^2.
\]
In particular,
\[
p=O(\varepsilon^2).
\]

At
\[
\mu=1,
\]
the defining integral is elementary:
\[
I(1,\rho)
=
1+\cos(\rho\pi).
\]
Therefore
\[
I(1,1-\varepsilon)
=
1-\cos(\pi\varepsilon)
=
\frac{\pi^2}{2}\varepsilon^2
-
\frac{\pi^4}{24}\varepsilon^4
+
O(\varepsilon^6).
\]

The source identifies
\[
I_\mu(1,1)
=
J_0
=
\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)
>
0.
\]

We next compute the first variation of this derivative in \(\rho\). Differentiating
\[
I_\mu(\mu,\rho)
=
\int_0^{(1+\rho)\pi}
t^{\mu-1}\log t\,
\sin(t-\rho\pi)\,dt
\]
with respect to \(\rho\), the moving-endpoint term vanishes because
\[
\sin\pi=0.
\]
Hence
\[
I_{\mu\rho}(\mu,\rho)
=
-\pi
\int_0^{(1+\rho)\pi}
t^{\mu-1}\log t\,
\cos(t-\rho\pi)\,dt.
\]
At
\[
(\mu,\rho)=(1,1),
\]
this becomes
\[
I_{\mu\rho}(1,1)
=
\pi
\int_0^{2\pi}
\log t\,\cos t\,dt.
\]
Integration by parts gives
\[
\int_0^{2\pi}
\log t\,\cos t\,dt
=
-\int_0^{2\pi}
\frac{\sin t}{t}\,dt
=
-\operatorname{Si}(2\pi).
\]
Thus
\[
I_{\mu\rho}(1,1)
=
-\pi\operatorname{Si}(2\pi).
\]

The integral is twice continuously differentiable in \(\rho\) and twice continuously differentiable in \(\mu\) on a fixed neighbourhood of
\[
(1,1).
\]
The logarithmic factors produced by differentiation are integrable at zero, while the moving upper endpoint stays away from zero. Therefore
\[
I_\mu(1,1-\varepsilon)
=
J_0
+
\pi\operatorname{Si}(2\pi)\varepsilon
+
O(\varepsilon^2).
\]

Now expand the root equation
\[
I(1-p,1-\varepsilon)=0
\]
in its first variable. The bounded second \(\mu\)-derivative used explicitly in the source's endpoint analysis gives
\[
0
=
I(1,1-\varepsilon)
-
p\,I_\mu(1,1-\varepsilon)
+
O(p^2).
\]
Since
\[
p=O(\varepsilon^2),
\]
the remainder is
\[
O(\varepsilon^4).
\]
Consequently,
\[
p
=
\frac{
I(1,1-\varepsilon)
}{
I_\mu(1,1-\varepsilon)
}
+
O(\varepsilon^4).
\]

Substituting the two expansions gives
\[
p
=
\frac{\pi^2}{2J_0}\varepsilon^2
-
\frac{
\pi^3\operatorname{Si}(2\pi)
}{
2J_0^2
}
\varepsilon^3
+
O(\varepsilon^4).
\]
Replacing
\[
\varepsilon
\]
by
\[
1-\rho
\]
proves the claim.

## Verification

The recent primary source was inspected at the definition and optimality of the root curve, the uniqueness and differentiability lemma, and the endpoint section that proves the certified quadratic bracket. In that section the source also records
\[
J_0
=
I_\mu(1,1)
=
\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)
\]
and uniform bounds on the relevant \(\mu\)-derivatives.

The only new derivative needed for the cubic term is
\[
I_{\mu\rho}(1,1)
=
-\pi\operatorname{Si}(2\pi),
\]
which follows directly by differentiation under the integral sign and one integration by parts.

As a numerical sanity check, solving the defining root equation at decreasing positive values of
\[
\varepsilon
\]
makes
\[
p/\varepsilon^2
\]
approach
\[
2.024406839216634\ldots
\]
and makes the normalized cubic residual approach
\[
-3.699971396358804\ldots.
\]
These numerical evaluations are not used as proof.

## Relationship to prior work

The 2026 primary source proves the full Koumandos–Ruscheweyh conjecture and establishes a quantitative endpoint bracket
\[
1.99(1-\rho)^2
<
1-\nu(\rho)
<
2.05(1-\rho)^2
\]
for \(\rho\) sufficiently close to \(1\). It does not state the exact quadratic coefficient or a cubic correction.

Koumandos and Lamprecht's 2010 paper treats the special parameter
\[
\rho=\frac14
\]
and develops related positive trigonometric-sum and gamma-function inequalities. It defines the same critical function
\[
\mu^*(\rho)
\]
but does not give the endpoint expansion above.

Sangal and Swaminathan's 2018 paper proves the conjecture near
\[
\rho=\frac13
\]
and records that earlier work studied analyticity and strict monotonicity of
\[
\mu^*(\rho).
\]
Its full text contains no endpoint asymptotic formula.

Targeted searches for the exact root, its endpoint deficit, the constants involving
\[
\operatorname{Ci}(2\pi)
\]
and
\[
\operatorname{Si}(2\pi),
\]
and equivalent quadratic-tangency formulations did not locate a statement implying the expansion above.

## Limitations

The expansion is local to the endpoint
\[
\rho=1.
\]
It does not provide a global closed form for
\[
\nu(\rho).
\]

Only the quadratic and cubic coefficients are identified. Higher coefficients can in principle be obtained from higher derivatives of the defining integral but are not claimed here.

A 2010 doctoral thesis cited by the 2018 paper as studying analyticity and monotonicity of
\[
\mu^*(\rho)
\]
was located bibliographically but its full text was not available in the bounded search. This remains a residual literature-access risk; the accessible papers describing that thesis do not report the endpoint expansion proved here.

## References

1. Y. Ma, *A Proof of the Koumandos–Ruscheweyh Conjecture*, arXiv:2610.02285v1, 2026.
2. S. Koumandos and M. Lamprecht, *On a conjecture for trigonometric sums and starlike functions, II*, Journal of Approximation Theory 162 (2010), 1068–1084. DOI: 10.1016/j.jat.2009.11.007.
3. P. Sangal and A. Swaminathan, *On a conjecture for trigonometric sums by S. Koumandos and S. Ruscheweyh*, arXiv:1806.06999v1, 2018.
4. S. Koumandos and S. Ruscheweyh, *On a conjecture for trigonometric sums and starlike functions*, Journal of Approximation Theory 149 (2007), 42–58.
