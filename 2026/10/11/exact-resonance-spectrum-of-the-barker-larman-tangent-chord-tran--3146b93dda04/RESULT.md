# Exact resonance spectrum of the Barker–Larman tangent-chord transform
## Finding
Normalize the fixed inner disk to radius \(1\). Fix an outer radius
\[
R>1,
\]
and write
\[
S=\sqrt{R^2-1},
\qquad
\beta=\arccos(1/R)\in(0,\pi/2).
\]
For
\[
f\in C^2(S^1),
\]
consider the radial perturbation
\[
\rho_{\varepsilon,f}(\phi)
=
R+\varepsilon f(\phi).
\]
For every fixed \(f\), all sufficiently small \(\varepsilon\) give a smooth strictly convex body \(K_{\varepsilon,f}\) containing the unit disk.

For
\[
n_\theta=(\cos\theta,\sin\theta),
\]
let
\[
T(\varepsilon,f)(\theta)
=
\operatorname{length}\!\left(
K_{\varepsilon,f}
\cap
\{x:x\cdot n_\theta=1\}
\right).
\]
The line in this definition is tangent to the unit disk.

The first variation at the concentric radius-\(R\) disk is
\[
D T_R[f](\theta)
=
\frac{R}{S}
\left(
f(\theta+\beta)+f(\theta-\beta)
\right).
\]
Consequently the Fourier mode
\[
e^{ik\theta}
\]
has multiplier
\[
\lambda_k(R)
=
\frac{2R}{S}\cos(k\beta).
\]

This gives an exact arithmetic classification.

If
\[
\frac{\beta}{\pi}
\]
is irrational, the linearized transform has trivial kernel. If
\[
\frac{\beta}{\pi}=\frac ab
\]
in lowest terms and \(b\) is odd, the kernel is again trivial. If \(b\) is even, then \(a\) is odd and the kernel consists exactly of those \(C^2\) functions whose Fourier support is contained in the frequencies
\[
k=
\frac b2(2j+1),
\qquad
j\in\mathbb Z_{\ge0},
\]
and their negatives.

Equivalently, the resonant outer radii are exactly
\[
R
=
\sec\!\left(\frac{\pi a}{b}\right),
\qquad
0<a<\frac b2,
\quad
\gcd(a,b)=1,
\quad
b\ \text{even}.
\]

The first-order obstruction is not an exact nonlinear invisibility direction. At a resonant radius, take the fundamental mode
\[
k=\frac b2,
\qquad
f(\phi)=\cos(k\phi).
\]
Then
\[
T(\varepsilon,f)(\theta)
=
2S
-
\frac{\varepsilon^2}{S^3}\sin^2(k\theta)
+
O(\varepsilon^3)
\]
uniformly in \(\theta\).

## Assumptions and scope
The inner disk is the Euclidean unit disk centered at the origin. Scaling gives the corresponding statement for any concentric inner disk.

The outer body is represented by a radial function with respect to the common center. For a polar curve
\[
r=\rho(\phi),
\]
the curvature numerator is
\[
\rho^2+2(\rho')^2-\rho\rho''.
\]
At \(\varepsilon=0\) this equals \(R^2>0\), so compactness and continuity imply positive curvature for all sufficiently small \(\varepsilon\). Also
\[
R-|\varepsilon|\|f\|_\infty>1
\]
for sufficiently small \(\varepsilon\), so the unit disk remains strictly inside the body.

The theorem is a local statement about the differential, together with one explicit second-order expansion on every fundamental resonant direction. It does not prove or disprove global Barker–Larman uniqueness.

## Proof
Parameterize the tangent line
\[
x\cdot n_\theta=1
\]
by
\[
x(s)=n_\theta+s\,t_\theta,
\qquad
t_\theta=(-\sin\theta,\cos\theta).
\]
Its distance from the origin is
\[
|x(s)|=\sqrt{1+s^2},
\]
and the polar angle of \(x(s)\) is
\[
\theta+\arctan s.
\]

The two endpoints of the section are the roots of
\[
F(s,\varepsilon)
=
\sqrt{1+s^2}
-
R
-
\varepsilon
f(\theta+\arctan s)
=
0.
\]
At \(\varepsilon=0\), the roots are
\[
s_\pm(0)=\pm S.
\]
Their polar angular offsets are
\[
\pm\beta,
\]
because
\[
\cos\beta=\frac1R,
\qquad
\sin\beta=\frac SR.
\]

Since
\[
\partial_sF(\pm S,0)=\pm\frac SR\ne0,
\]
the implicit-function theorem gives smooth endpoint functions
\[
s_\pm(\varepsilon).
\]
Differentiating once gives
\[
s_+'(0)
=
\frac RS f(\theta+\beta),
\qquad
s_-'(0)
=
-\frac RS f(\theta-\beta).
\]
Therefore
\[
\begin{aligned}
D T_R[f](\theta)
&=
s_+'(0)-s_-'(0)\\
&=
\frac RS
\left(
f(\theta+\beta)+f(\theta-\beta)
\right).
\end{aligned}
\]

For
\[
f(\theta)=e^{ik\theta},
\]
this becomes
\[
D T_R[f](\theta)
=
\frac{2R}{S}\cos(k\beta)e^{ik\theta},
\]
which proves the multiplier formula.

It remains to classify its zeros. If
\[
\beta/\pi
\]
is irrational, then
\[
\cos(k\beta)\ne0
\]
for every integer \(k\), so the kernel is trivial.

Now write
\[
\frac{\beta}{\pi}=\frac ab
\]
in lowest terms. A zero multiplier is equivalent to
\[
\cos\!\left(\frac{\pi k a}{b}\right)=0,
\]
or
\[
2ka=b(2m+1)
\]
for some integer \(m\). If \(b\) is odd, parity makes this impossible. If \(b\) is even, write
\[
b=2c.
\]
Then \(a\) is odd and coprime to \(c\), and the equation becomes
\[
ka=c(2m+1).
\]
Thus \(k\) is exactly \(c\) times an odd integer:
\[
k=\frac b2(2j+1).
\]
This proves the kernel classification and the equivalent resonance-radius formula.

For the second-order statement, write
\[
f_\pm
=
f(\theta\pm\beta),
\qquad
f_\pm'
=
f'(\theta\pm\beta).
\]
Expanding the two implicit roots to second order gives
\[
T(\varepsilon,f)(\theta)
=
2S
+
\varepsilon\frac RS(f_++f_-)
+
\varepsilon^2
\left[
\frac{f_+'f_+-f_-'f_-}{S^2}
-
\frac{f_+^2+f_-^2}{2S^3}
\right]
+
O(\varepsilon^3).
\]
The remainder is uniform in \(\theta\) because the endpoint roots depend smoothly on \((\theta,\varepsilon)\) on the compact circle.

At a resonant radius, for the fundamental mode
\[
k=\frac b2,
\qquad
f(\phi)=\cos(k\phi),
\]
one has
\[
k\beta=\frac{a\pi}{2},
\]
an odd multiple of \(\pi/2\). Hence
\[
f_++f_-=0,
\]
\[
f_+'f_+-f_-'f_-=0,
\]
and
\[
f_+^2+f_-^2
=
2\sin^2(k\theta).
\]
Substitution yields
\[
T(\varepsilon,f)(\theta)
=
2S
-
\frac{\varepsilon^2}{S^3}\sin^2(k\theta)
+
O(\varepsilon^3),
\]
as claimed.

## Verification
The supplied `verify.py` symbolically reconstructs the endpoint derivatives from the implicit equation, verifies the full second-order section-length coefficient, checks the parity classification of rational resonances on a finite exact test range, and verifies the resonant simplification.

For the first resonance
\[
R=\sqrt2,
\qquad
\beta=\frac\pi4,
\qquad
k=2,
\]
the checker confirms that the linear term vanishes and the quadratic term is
\[
-\sin^2(2\theta).
\]
For the next basic example
\[
R=\frac2{\sqrt3},
\qquad
\beta=\frac\pi6,
\qquad
k=3,
\]
it confirms
\[
-\frac{\sin^2(3\theta)}{(1/3)^{3/2}}
=
-3\sqrt3\,\sin^2(3\theta).
\]

These examples are regression checks only. The all-frequency and all-radius statements follow from the exact multiplier and number-theoretic classification in the proof.

## Relationship to prior work
Barker and Larman introduced the tangent-section determination problem and conjectured uniqueness from the sectional-volume data. In the planar ball case, the data are precisely the lengths of chords lying on the tangent lines of the fixed inner disk.

Makai and Martini's 2016 work gives infinitesimal determination results in a different asymptotic regime, where the unknown body approaches the fixed inner body. Their introduction explicitly notes that the original planar ball problem remains difficult and that differentiating the moving tangent sections leads to coupled values and derivatives at two points rather than an immediate uniqueness proof.

A later survey still records the planar tangent-chord question as open even in a small neighborhood of the unit ball. The 2026 polygonal reconstruction theorem proves uniqueness in the polygonal class and explicitly identifies stability and extensions beyond the polyhedral class as further questions.

The present result does not duplicate those uniqueness theorems. It fixes a positive concentric gap between the inner and outer disks, diagonalizes the resulting first variation completely, identifies every singular radius arithmetically, and shows that the fundamental singular modes reappear at quadratic order.

Targeted literature searches for Barker–Larman linearization, tangent-chord Fourier multipliers, circle perturbations, resonance radii, and equivalent kernel formulations did not locate the displayed spectrum or second-order formula.

## Limitations
The theorem is local around a concentric outer disk and uses radial perturbations.

Injectivity of the differential is not a nonlinear local uniqueness theorem. In particular, at irrational values of
\[
\beta/\pi
\]
the multipliers can approach zero along high frequencies, so the theorem does not assert a uniform inverse estimate.

At resonant radii, the quadratic calculation rules out exact invisibility for the fundamental single harmonic, but it does not classify all nonlinear combinations inside the infinite-dimensional linear kernel.

The full Barker–Larman reconstruction problem remains outside the claim.

## References
1. J. A. Barker and D. G. Larman, *Determination of convex bodies by certain sets of sectional volumes*, Discrete Mathematics 241 (2001), 79–96. DOI: 10.1016/S0012-365X(01)00111-X.
2. E. Makai, Jr. and H. Martini, *Unique local determination of convex bodies*, arXiv:1602.00959v1, 2016-02-02; later Acta Mathematica Hungarica 150 (2016), 176–193. DOI: 10.1007/s10474-016-0640-z.
3. M. A. Alfonseca, F. Nazarov, D. Ryabogin, and V. Yaskin, *Analysis and Geometry Near the Unit Ball*, survey preprint, Problem 5.
4. B. Matthews, *Hedgehog reconstruction of polygons: Non-central sections and slabs*, Canadian Mathematical Bulletin, published online 2026-09-30. DOI: 10.4153/S0008439526102355.
