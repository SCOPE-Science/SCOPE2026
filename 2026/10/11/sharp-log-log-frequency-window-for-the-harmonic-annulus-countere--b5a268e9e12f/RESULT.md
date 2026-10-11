# Sharp log–log frequency window for the harmonic annulus counterexample

## Finding

Fix
\[
1<s<S.
\]
Set
\[
D=s-s^{-1},
\qquad
T=S-s^{-1},
\qquad
\kappa=\frac{S-s}{S-s^{-1}},
\]
and
\[
c_{s,S}
=
\frac{SD}{4T^2}.
\]

Consider the harmonic maps from the recent annulus counterexample with boundary values
\[
h_{t,m}(e^{i\theta})=e^{i\theta}
\]
and
\[
h_{t,m}(se^{i\theta})
=
S e^{i(\theta+t\sin m\theta)},
\]
where
\[
m\ge2,
\qquad
mt<1.
\]

Suppose
\[
t\downarrow0,
\qquad
m=m(t)\to\infty,
\qquad
mt\to0,
\]
and
\[
\frac{m s^{-m}}{t}
\longrightarrow
\lambda\in[0,\infty).
\]
Then
\[
\lVert\omega_{h_{t,m}}\rVert_\infty
=
\kappa
+
c_{s,S}
\left(
2D^2\lambda-1
\right)t^2
+
o(t^2).
\]

In particular, the source construction has a sharp transition at
\[
\lambda_*=\frac{1}{2D^2}.
\]
If
\[
\lambda<\lambda_*,
\]
then
\[
\lVert\omega_{h_{t,m}}\rVert_\infty<\kappa
\]
for all sufficiently small
\[
t,
\]
and the construction still disproves the proposed annular dilatation threshold. If
\[
\lambda>\lambda_*,
\]
then
\[
\lVert\omega_{h_{t,m}}\rVert_\infty>\kappa
\]
for all sufficiently small
\[
t,
\]
so this same perturbative family no longer crosses the threshold.

Writing
\[
L=\log(1/t),
\]
the critical window can also be expressed as
\[
m\log s
=
L+\log L+C+o(1).
\]
Along such a path,
\[
\frac{
\lVert\omega_{h_{t,m}}\rVert_\infty-\kappa
}{
t^2
}
\longrightarrow
c_{s,S}
\left(
\frac{2D^2e^{-C}}{\log s}-1
\right).
\]
Therefore the exact phase boundary is
\[
C_*(s)
=
\log
\frac{
2(s-s^{-1})^2
}{
\log s
}.
\]

The transition frequency is thus
\[
m\log s
=
\log(1/t)
+
\log\log(1/t)
+
C_*(s)
+
O(1).
\]
The extra
\[
\log\log(1/t)
\]
term is the boundary-layer correction that separates successful and unsuccessful high-frequency perturbations in this family.

## Assumptions and scope

The maps
\[
h_{t,m}
\]
are exactly the harmonic extensions used in arXiv:2609.29795v1.

The annuli are
\[
A(1,s)
\]
and
\[
A(1,S),
\]
with
\[
1<s<S.
\]
The quantity
\[
\kappa
=
\frac{S-s}{S-s^{-1}}
\]
is the dilatation threshold appearing in the conjecture disproved by the source.

The result concerns the source's sinusoidal outer-boundary perturbation. It does not claim an optimal frequency threshold among all possible boundary perturbations.

The critical case
\[
\lambda=\frac{1}{2(s-s^{-1})^2}
\]
requires a higher-order expansion and is not classified here.

## Proof

The Jacobi--Anger expansion of the outer boundary data gives the source representation
\[
h(\rho e^{i\theta})
=
\left(
a(t)\rho-\frac{\beta(t)}{\rho}
\right)e^{i\theta}
+
\sum_{j\ne0}
S J_j(t)V_{p_j}(\rho)
e^{i(1+mj)\theta},
\]
where
\[
p_j=|1+mj|
\]
and
\[
V_p(\rho)
=
\frac{\rho^p-\rho^{-p}}{s^p-s^{-p}}.
\]
The first-mode coefficients are
\[
a(t)
=
\frac{SJ_0(t)-s^{-1}}{D},
\qquad
\beta(t)
=
\frac{SJ_0(t)-s}{D}.
\]
Hence
\[
a(t)-\beta(t)=1.
\]

Define
\[
P=\rho h_\rho-i h_\theta,
\qquad
Q=\rho h_\rho+i h_\theta.
\]
The source identifies
\[
|\omega_h|=\frac{|Q|}{|P|}.
\]

On the inner circle,
\[
V_p(1)=0
\]
and
\[
V_p'(1)
=
\frac{2p}{s^p-s^{-p}}.
\]
After factoring out
\[
e^{i\theta},
\]
one obtains
\[
e^{-i\theta}P
=
2a+R(\theta),
\qquad
e^{-i\theta}Q
=
2\beta+R(\theta),
\]
where
\[
R(\theta)
=
\sum_{j\ne0}
d_j e^{imj\theta}
\]
and
\[
d_j
=
\frac{
2S J_j(t)p_j
}{
s^{p_j}-s^{-p_j}
}.
\]

The pair
\[
j=\pm1
\]
determines the second-order leakage. Since
\[
J_1(t)
=
\frac t2+O(t^3)
\]
and
\[
J_{-1}(t)=-J_1(t),
\]
\[
d_1
=
S t(m+1)s^{-m-1}
+
o(t^2)
\]
and
\[
d_{-1}
=
-
S t(m-1)s^{-m+1}
+
o(t^2).
\]
All modes with
\[
|j|\ge2
\]
are
\[
o(t^2)
\]
uniformly, because
\[
m s^{-m}=O(t).
\]
Consequently
\[
R(\theta)
=
S t m s^{-m}
\left(
s^{-1}e^{im\theta}
-
s e^{-im\theta}
\right)
+
o(t^2)
\]
uniformly in
\[
\theta.
\]
The real part is maximized when
\[
\cos(m\theta)=-1,
\]
so
\[
\max_\theta
\operatorname{Re}R(\theta)
=
SD\lambda t^2+o(t^2).
\]

Because
\[
R=O(t^2),
\]
a first-order expansion in
\[
R
\]
gives
\[
\frac{|2\beta+R|}{|2a+R|}
=
\frac{\beta}{a}
+
\frac{\operatorname{Re}R}{2a^2}
+
O(|R|^2).
\]
The first-mode quotient satisfies
\[
\frac{\beta(t)}{a(t)}
=
\frac{
SJ_0(t)-s
}{
SJ_0(t)-s^{-1}
}.
\]
Using
\[
J_0(t)
=
1-\frac{t^2}{4}+O(t^4)
\]
yields
\[
\frac{\beta(t)}{a(t)}
=
\kappa
-
c_{s,S}t^2
+
O(t^4).
\]
Also
\[
a(0)=\frac{T}{D}.
\]
It follows that the inner-boundary maximum equals
\[
\kappa
+
\left(
-c_{s,S}
+
\frac{D^2}{2T^2}SD\lambda
\right)t^2
+
o(t^2).
\]
Since
\[
\frac{SD^3}{2T^2}
=
2D^2c_{s,S},
\]
this is precisely
\[
\kappa
+
c_{s,S}
\left(
2D^2\lambda-1
\right)t^2
+
o(t^2).
\]

It remains to verify that the inner boundary controls the global norm. On the outer circle, the first-mode quotient tends to
\[
\frac{\kappa}{s^2},
\]
which is strictly smaller than
\[
\kappa.
\]
The source estimates the non-first contribution there by
\[
O(mt)=o(1).
\]
Thus the outer boundary remains separated from the inner-boundary value by a fixed positive amount.

The same boundary estimates show that
\[
P
\]
has no zeros for sufficiently small
\[
t.
\]
Therefore the complex dilatation is holomorphic on the annulus, and the maximum-modulus principle reduces its norm to the two boundary circles. This proves the stated asymptotic.

Finally,
\[
\lVert\omega_h\rVert_\infty
=
\kappa+O(t^2)
<
1
\]
for sufficiently small
\[
t,
\]
so the Jacobian is positive. Since
\[
mt<1,
\]
the perturbed outer boundary map has degree one, as does the fixed inner boundary map. The topological lemma used by the source then gives an orientation-preserving harmonic diffeomorphism.

For the log--log form, if
\[
m\log s
=
L+\log L+C+o(1),
\qquad
L=\log(1/t),
\]
then
\[
s^{-m}
=
\frac{t e^{-C}}{L}
\left(
1+o(1)
\right)
\]
and
\[
\frac{m s^{-m}}{t}
\longrightarrow
\frac{e^{-C}}{\log s}.
\]
Substitution gives the phase formula and
\[
C_*(s)
=
\log
\frac{
2(s-s^{-1})^2
}{
\log s
}.
\]

## Verification

The primary source was inspected at its harmonic Fourier construction, the inner- and outer-boundary estimates for the complex dilatation, the expansion of the radial first mode, and the final diffeomorphism argument.

The source chooses
\[
m
=
\left\lceil
\frac{
3\log(1/t)
}{
\log s
}
\right\rceil
\]
so that the inner high-frequency leakage is
\[
o(t^2).
\]
The present calculation keeps that leakage at its natural second-order scale instead of discarding it.

The leading inner leakage comes only from the
\[
j=\pm1
\]
Fourier pair. Under
\[
m s^{-m}/t\to\lambda,
\]
all
\[
|j|\ge2
\]
terms are smaller than
\[
t^2.
\]
The first-mode deficit and the leakage coefficient are therefore both explicit and comparable at the transition.

As a numerical sanity check, when
\[
s=2,
\qquad
S=3,
\]
one has
\[
\kappa=0.4,
\qquad
c_{s,S}=0.18,
\qquad
\lambda_*=\frac{2}{9},
\]
and
\[
C_*(2)
=
\log
\frac{9/2}{\log2}
=
1.8705903173\ldots.
\]
Direct evaluation of the finite Fourier formula at small
\[
t
\]
agrees with the predicted sign change. The proof of the asymptotic statement itself is analytic and does not rely on numerical sampling.

## Relationship to prior work

The recent paper disproves the proposed upper Nitsche--Grötzsch-type bound by combining two effects: a quadratic improvement of the radial first mode and exponential damping of high-frequency boundary leakage.

Its proof deliberately chooses a frequency much larger than needed,
\[
m\sim
\frac{
3\log(1/t)
}{
\log s
},
\]
which makes the leakage negligible compared with the quadratic radial gain. It does not determine the transition at which those two effects balance.

The original annulus work of Iwaniec, Kovalev, and Onninen establishes the sharp radial framework and motivates the conjectural threshold, but it predates the non-radial counterexample family and therefore does not contain its frequency balance.

Targeted searches for the exact source, high-frequency annular perturbations, minimal oscillation frequency, and the scale
\[
m s^{-m}/t
\]
did not locate a statement equivalent to the log--log transition or its coefficient.

The present result therefore quantifies the mechanism of the recent counterexample: exponential damping must overcome the quadratic first-mode gain, and that balance inserts the extra
\[
\log\log(1/t)
\]
term.

## Limitations

The result is specific to the sinusoidal boundary perturbation used in the source. A different perturbation may have a different leakage profile.

The critical case
\[
\lambda=\lambda_*
\]
is not resolved because the quadratic terms cancel and fourth-order first-mode terms must be compared with finer Fourier leakage.

The integer nature of
\[
m
\]
produces an unavoidable bounded phase effect in the log--log window. The invariant formulation in terms of
\[
m s^{-m}/t
\]
removes that lattice ambiguity.

No claim is made that this is a globally minimal oscillation frequency among all harmonic annulus counterexamples.

## References

1. D. Kalaj, J. Liu, and J.-F. Zhu, *On an Iwaniec–Kovalev–Onninen Conjecture for harmonic quasiconformal annulus mappings*, arXiv:2609.29795v1, 2026.
2. T. Iwaniec, L. V. Kovalev, and J. Onninen, *Doubly connected minimal surfaces and extremal harmonic mappings*, Journal of Geometric Analysis 22 (2012), 726--762; arXiv:0912.3542.
