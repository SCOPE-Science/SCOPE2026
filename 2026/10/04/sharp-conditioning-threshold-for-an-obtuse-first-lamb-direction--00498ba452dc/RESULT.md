# Sharp conditioning threshold for an obtuse first LAMB direction
## Finding

Consider one two-dimensional parameter layer with the deterministic SPD quadratic
\[
f(x)=\frac12x^\top Hx,
\qquad
H=H^\top\succ0.
\]
Let the spectral condition number be
\[
\kappa
=
\frac{\lambda_{\max}(H)}{\lambda_{\min}(H)}.
\]

At the first source-form LAMB iteration, with
\[
0<\beta_1,\beta_2<1,
\qquad
\varepsilon>0,
\]
zero weight decay, and zero-initialized moments, bias correction gives
\[
\widehat m_1=Hx,
\qquad
\widehat v_1=(Hx)^2
\]
coordinatewise. Therefore the Adam-preconditioned direction is
\[
r_i
=
\frac{(Hx)_i}
{|(Hx)_i|+\varepsilon}.
\]

The LAMB layer update is a positive scalar multiple of \(-r\). For any positive scalar \(a\),
\[
x^+
=
x-a r,
\]
and
\[
\|x^+\|_2^2-\|x\|_2^2
=
-2a\,x^\top r+a^2\|r\|_2^2.
\]
Hence if
\[
x^\top r<0,
\]
every positive step magnitude increases Euclidean distance to the minimizer.

There is a sharp condition-number threshold for whether this can happen:
\[
\kappa_\star
=
3+2\sqrt2.
\]

If
\[
\kappa\le\kappa_\star,
\]
then for every nonzero \(x\) and every \(\varepsilon>0\),
\[
x^\top r>0.
\]
Thus the first LAMB direction is acute with the vector from the minimizer, and a sufficiently small positive step decreases \(\|x\|_2\).

If
\[
\kappa>\kappa_\star,
\]
then for every fixed \(\varepsilon>0\) there exist an SPD matrix \(H\) with condition number exactly \(\kappa\) and a nonzero \(x\) for which
\[
x^\top r<0.
\]
For that instance, every positive LAMB step multiplier increases \(\|x\|_2\). No positive trust-ratio magnitude can repair the first-step directional error.

A simple concrete example is
\[
H=
\begin{bmatrix}
2&-5\\
-5&13
\end{bmatrix},
\qquad
x=
\begin{bmatrix}
2\\
1
\end{bmatrix}.
\]
Then
\[
Hx=
\begin{bmatrix}
-1\\
3
\end{bmatrix},
\]
and
\[
r=
\begin{bmatrix}
-\dfrac1{1+\varepsilon}\\[4pt]
\dfrac3{3+\varepsilon}
\end{bmatrix}.
\]
Therefore
\[
x^\top r
=
-\frac2{1+\varepsilon}
+
\frac3{3+\varepsilon}
=
\frac{\varepsilon-3}
{(1+\varepsilon)(3+\varepsilon)}.
\]
Thus
\[
x^\top r<0
\]
for every
\[
0<\varepsilon<3.
\]
The matrix has determinant \(1\), trace \(15\), and condition number
\[
\frac{15+\sqrt{221}}{15-\sqrt{221}}
\approx222.9955.
\]

The obstruction is directional, not a large-trust-ratio artifact. The later LAMBC proposal clips the trust-ratio magnitude, but multiplying an obtuse direction by any positive scalar still increases Euclidean distance.

## Assumptions and scope

The theorem concerns the first source-form LAMB step, one two-dimensional layer, zero weight decay, and positive denominator \(\varepsilon\).

The layer scaling function may be any positive value at the current parameter norm. The sharp threshold does not depend on the global learning rate or the positive trust-ratio magnitude.

The result concerns Euclidean distance to the unique quadratic minimizer, not one-step objective value. Since
\[
(Hx)^\top r
=
\sum_i
\frac{(Hx)_i^2}
{|(Hx)_i|+\varepsilon}
>0,
\]
the direction \(-r\) is still a strict objective-descent direction. For sufficiently small step magnitude the objective decreases even in the counterexample.

The theorem is coordinate-sensitive because Adam-style diagonal preconditioning is coordinate-sensitive. The condition number is spectral, while the existence construction also chooses an orientation of the Hessian relative to the coordinate axes.

## Proof

The first-step LAMB reduction follows from zero initialization:
\[
m_1=(1-\beta_1)g,
\qquad
v_1=(1-\beta_2)g^2,
\qquad
g=Hx.
\]
Bias correction therefore gives
\[
\widehat m_1=g,
\qquad
\widehat v_1=g^2,
\]
which proves
\[
r_i
=
\frac{g_i}{|g_i|+\varepsilon}.
\]

We need two geometric lemmas.

First, let
\[
\delta
=
\angle(x,Hx).
\]
For an SPD matrix with condition number \(\kappa\),
\[
\cos\delta
\ge
\frac{2\sqrt{\kappa}}{\kappa+1}.
\]
To prove this, scale the smallest eigenvalue to \(1\), the largest to \(\kappa\), normalize
\[
\|x\|_2=1,
\]
and let the spectral random variable \(\Lambda\in[1,\kappa]\) have probabilities equal to squared eigenbasis coordinates of \(x\). Then
\[
\cos^2\delta
=
\frac{\mathbb E[\Lambda]^2}
{\mathbb E[\Lambda^2]}.
\]
For every
\[
\lambda\in[1,\kappa],
\]
convexity against the endpoint chord gives
\[
\lambda^2
\le
(\kappa+1)\lambda-\kappa.
\]
Writing
\[
m=\mathbb E[\Lambda],
\]
we obtain
\[
\cos^2\delta
\ge
\frac{m^2}{(\kappa+1)m-\kappa}.
\]
The right side is minimized at
\[
m=\frac{2\kappa}{\kappa+1},
\]
where it equals
\[
\frac{4\kappa}{(\kappa+1)^2}.
\]

Second, define the coordinatewise saturation map
\[
T_\varepsilon(g)_i
=
\frac{g_i}{|g_i|+\varepsilon}.
\]
In two dimensions,
\[
x^\top T_\varepsilon(g)\le0
\]
with
\[
x^\top g>0
\]
implies
\[
\angle(x,g)>\frac\pi4.
\]

To see this, signed coordinate reflections let us place \(x\) in the first quadrant without changing either dot product or angle. If \(g\) is also in the first quadrant, the dot product with \(T_\varepsilon(g)\) is positive. Since \(x^\top g>0\), \(g\) cannot be in the opposite third quadrant when the transformed dot product is nonpositive. Thus \(g\) lies in the second or fourth quadrant; the cases are symmetric.

Take the second-quadrant case. Let the polar angles of \(x\), \(g\), and \(T_\varepsilon(g)\) be
\[
\theta,\qquad\phi,\qquad\psi.
\]
The map
\[
u\mapsto\frac{u}{u+\varepsilon}
\]
compresses the ratio of the two absolute coordinate magnitudes toward \(1\). Hence \(\psi\) lies between \(\phi\) and \(3\pi/4\).

If
\[
x^\top T_\varepsilon(g)\le0,
\]
then
\[
\psi-\theta\ge\frac\pi2.
\]
If \(\phi\ge\psi\), then
\[
\phi-\theta\ge\frac\pi2.
\]
If \(\phi<\psi\), then
\[
\psi\le\frac{3\pi}{4},
\]
so
\[
\theta\le\frac\pi4,
\]
while
\[
\phi>\frac\pi2.
\]
Again
\[
\phi-\theta>\frac\pi4.
\]
Thus in all cases
\[
\angle(x,g)>\frac\pi4.
\]

Now
\[
\frac{2\sqrt{\kappa}}{\kappa+1}
\ge
\frac1{\sqrt2}
\]
is equivalent to
\[
\kappa\le3+2\sqrt2.
\]
Therefore, below or at this condition number, the SPD turning-angle bound gives
\[
\angle(x,Hx)\le\frac\pi4.
\]
The second lemma then forces
\[
x^\top r>0.
\]

It remains to prove sharpness.

Fix
\[
\kappa>3+2\sqrt2
\]
and let
\[
D=
\begin{bmatrix}
1&0\\
0&\kappa
\end{bmatrix},
\qquad
y=
\begin{bmatrix}
1\\
\kappa^{-1/2}
\end{bmatrix}.
\]
The angle between \(y\) and \(Dy\) is the maximal SPD turning angle,
\[
\delta_\kappa
=
\arccos
\left(
\frac{2\sqrt{\kappa}}{\kappa+1}
\right)
>
\frac\pi4.
\]

Choose a planar rotation \(Q\) so that the angular midpoint of \(Qy\) and \(QDy\) is
\[
\frac{3\pi}{8}.
\]
Then
\[
x=Qy
\]
has polar angle
\[
\frac{3\pi}{8}-\frac{\delta_\kappa}{2}
<
\frac\pi4,
\]
while
\[
g_0=QDy
\]
has polar angle
\[
\frac{3\pi}{8}+\frac{\delta_\kappa}{2}
>
\frac\pi2.
\]
Hence
\[
x_1>x_2>0,
\qquad
(g_0)_1<0<(g_0)_2,
\]
so
\[
x^\top\operatorname{sign}(g_0)
=
-x_1+x_2
<0.
\]

For any scalar
\[
c>0,
\]
set
\[
H_c=cQDQ^\top.
\]
Its condition number is exactly \(\kappa\), and
\[
H_cx=cg_0.
\]
For fixed \(\varepsilon>0\),
\[
T_\varepsilon(cg_0)
\longrightarrow
\operatorname{sign}(g_0)
\]
as
\[
c\to\infty.
\]
Therefore, for all sufficiently large finite \(c\),
\[
x^\top T_\varepsilon(H_cx)<0.
\]
This proves sharpness.

## Verification

The accompanying `verify.py` checks the first-step LAMB reduction for arbitrary momentum coefficients, verifies the explicit rational counterexample, numerically tests the SPD turning-angle bound, reconstructs the sharp rotated family above the threshold, and confirms distance increase for many positive step magnitudes.

The numerical checks are transcription guards. The exact threshold and existence/nonexistence statements are proved analytically above.

## Relationship to prior work

You and coauthors introduced LAMB by combining Adam's coordinatewise second-moment normalization with layerwise normalization. The defining paper states that each layer update is normalized in Euclidean norm and scaled by a function of the parameter norm, and it notes that when both moment coefficients vanish the method reduces to a layer-scaled sign method. It proves nonconvex convergence under its stated assumptions but does not give a sharp conditioning threshold for first-step direction geometry on quadratics.

Fong, Chen, and Chen later proposed LAMBC because unstable and extreme trust-ratio magnitudes can degrade training, and they clip the trust ratio to limit update magnitude. Their inspected paper does not analyze a quadratic directional obstruction. The present theorem is complementary: even an arbitrarily small positive multiplier cannot reverse the Euclidean-distance increase produced by an obtuse direction.

The threshold
\[
3+2\sqrt2
\]
arises from the exact maximal turning angle of an SPD operator combined with the coordinatewise saturation inherent in Adam's first-step direction. Focused published-record searches for LAMB quadratic stability, obtuse first-step directions, trust-ratio clipping, and sign-preconditioned SPD geometry did not identify this statement or an implication-equivalent result.

## Limitations

The result is two-dimensional and first-step. Later moment history can change the direction geometry.

It concerns Euclidean distance to the minimizer, not monotonicity of the quadratic objective.

The existence construction may require scaling the Hessian relative to the fixed denominator \(\varepsilon\); the condition number is held fixed while the overall curvature scale grows.

The theorem does not imply that practical LAMB training diverges, nor does it quantify how often such coordinate orientations arise in neural networks.

## References

1. Yang You, Jing Li, Sashank Reddi, Jonathan Hseu, Sanjiv Kumar, Srinadh Bhojanapalli, Xiaodan Song, James Demmel, Kurt Keutzer, and Cho-Jui Hsieh, “Large Batch Optimization for Deep Learning: Training BERT in 76 minutes,” arXiv:1904.00962v1, 2019.
2. Jeffrey Fong, Siwei Chen, and Kaiqi Chen, “Improving Layer-wise Adaptive Rate Methods using Trust Ratio Clipping,” arXiv:2011.13584v1, 2020.
