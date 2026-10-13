# AngularGrad's paper angle has an exact reciprocal-amplitude phase diagram
## Finding

AngularGrad was introduced to adjust Adam's step size using an angular coefficient computed from consecutive gradients. In one dimension, the source formula can be solved exactly on the canonical persistent sign-alternating signal, and the result exposes a sharp amplitude dependence that a true direction angle would not have.

Take
\[
g_t=(-1)^{t-1}G,
\qquad
G>0.
\]
The paper defines
\[
A_t
=
\arctan
\left|
\frac{g_t-g_{t-1}}
{1+g_tg_{t-1}}
\right|,
\]
then
\[
A_{\min,t}=\min(A_{t-1},A_t),
\]
and, with the source choices
\[
\lambda_1=\lambda_2=\frac12,
\]
uses either
\[
\phi_{\cos,t}
=
\frac12\left[1+\tanh\!\left(|\cos A_{\min,t}|\right)\right]
\]
or
\[
\phi_{\tan,t}
=
\frac12\left[1+\tanh\!\left(|\tan A_{\min,t}|\right)\right].
\]

For every
\[
t\ge2,
\]
the alternating signal gives
\[
|g_t-g_{t-1}|=2G,
\qquad
1+g_tg_{t-1}=1-G^2.
\]
Thus all post-startup angles are identical:
\[
A_t=A(G)
=
\arctan\left(\frac{2G}{|1-G^2|}\right),
\qquad G\ne1,
\]
with the continuous-extension value
\[
A(1)=\frac\pi2.
\]
Therefore, for every
\[
t\ge3,
\]
the adjacent-angle minimum is exactly
\[
A_{\min,t}=A(G).
\]

Using
\[
\sqrt{(1-G^2)^2+4G^2}=1+G^2,
\]
we obtain
\[
|\cos A(G)|
=
\frac{|1-G^2|}{1+G^2}
\]
and
\[
|\tan A(G)|
=
\frac{2G}{|1-G^2|}.
\]
Hence the two steady angular coefficients are
\[
\boxed{
\phi_{\cos}(G)
=
\frac12
\left[
1+\tanh\left(\frac{|1-G^2|}{1+G^2}\right)
\right]
}
\]
and
\[
\boxed{
\phi_{\tan}(G)
=
\frac12
\left[
1+\tanh\left(\frac{2G}{|1-G^2|}\right)
\right]
},
\qquad G\ne1,
\]
with
\[
\phi_{\tan}(1)=1.
\]

Both coefficients have the exact reciprocal symmetry
\[
\phi(G)=\phi(1/G).
\]
But they are not invariant under a general positive rescaling of the gradient amplitude.

For the cosine variant,
\[
q(G)=\frac{|1-G^2|}{1+G^2}
\]
decreases strictly from \(1\) to \(0\) on \((0,1)\) and increases strictly from \(0\) to \(1\) on \((1,\infty)\). Consequently
\[
\phi_{\cos}(1)=\frac12
\]
is the unique minimum, while
\[
\lim_{G\to0}\phi_{\cos}(G)
=
\lim_{G\to\infty}\phi_{\cos}(G)
=
\frac{1+\tanh1}{2}
=
0.880797077977\ldots.
\]

For the tangent variant,
\[
r(G)=\frac{2G}{|1-G^2|}
\]
increases strictly from \(0\) to \(+\infty\) on \((0,1)\) and decreases strictly from \(+\infty\) to \(0\) on \((1,\infty)\). Hence
\[
\phi_{\tan}(1)=1
\]
is the unique maximum and
\[
\lim_{G\to0}\phi_{\tan}(G)
=
\lim_{G\to\infty}\phi_{\tan}(G)
=
\frac12.
\]

The two variants cross when
\[
\frac{2G}{|1-G^2|}
=
\frac{|1-G^2|}{1+G^2}.
\]
Since \(\tanh\) is strictly increasing, this equality is equivalent to
\[
G^4-2G^3-2G^2-2G+1=0.
\]
Dividing by \(G^2\) and setting
\[
z=G+G^{-1}
\]
gives
\[
z^2-2z-4=0,
\]
so
\[
z=1+\sqrt5.
\]
The two positive reciprocal solutions are
\[
\boxed{
G_-
=
\frac{1+\sqrt5-\sqrt{2+2\sqrt5}}{2}
=
0.346014339235\ldots
}
\]
and
\[
\boxed{
G_+
=
\frac{1+\sqrt5+\sqrt{2+2\sqrt5}}{2}
=
2.890053638264\ldots
}.
\]
Therefore
\[
\phi_{\tan}(G)>\phi_{\cos}(G)
\]
exactly for
\[
G_-<G<G_+,
\]
while
\[
\phi_{\cos}(G)>\phi_{\tan}(G)
\]
outside that interval.

The true one-dimensional direction sequence is simply
\[
+1,-1,+1,-1,\ldots,
\]
for every \(G>0\). Positive rescaling changes no direction, yet it changes the paper's angular coefficient. At the balanced amplitude \(G=1\), the two published variants are maximally separated:
\[
\phi_{\tan}(1)=1,
\qquad
\phi_{\cos}(1)=\frac12.
\]
Thus the source's scalar angle formula mixes direction change with gradient scale, and the cosine and tangent choices react in opposite ways to the same amplitude resonance.

## Assumptions and scope

The theorem concerns the one-coordinate paper-form angular coefficient in Algorithm 2 of AngularGrad.

It analyzes the source definitions of \(A_t\), the adjacent-angle minimum, and the two nonlinear choices \(\cos\) and \(\tan\), with the paper's \(\lambda_1=\lambda_2=1/2\).

The result does not require assumptions on Adam's first- or second-moment parameters because it concerns the multiplicative angular coefficient itself.

The alternating signal is an input-response diagnostic. It isolates the claimed angular mechanism and does not assert that a fixed objective necessarily generates the sequence.

The official repository implements the same scalar tangent-difference and cosine/tangent transforms but uses an additional state-selection rule for the stored angle statistic. The theorem is therefore explicitly about the displayed paper recurrence, not every implementation detail.

## Proof

For \(t\ge2\), consecutive gradients have opposite signs and equal magnitude, so
\[
g_tg_{t-1}=-G^2
\]
and
\[
|g_t-g_{t-1}|=2G.
\]
Substitution into the source formula gives the stated \(A(G)\). Since the same value occurs at every post-startup transition, \(A_{t-1}=A_t=A(G)\) for every \(t\ge3\), so the adjacent minimum is exactly \(A(G)\).

The trigonometric identities follow from
\[
1+\tan^2A
=
\frac{(1-G^2)^2+4G^2}{(1-G^2)^2}
=
\frac{(1+G^2)^2}{(1-G^2)^2}.
\]
This proves the closed forms for \(|\cos A|\) and \(|\tan A|\), hence for both angular coefficients.

Reciprocal symmetry is immediate after replacing \(G\) by \(1/G\) and multiplying numerator and denominator by \(G^2\).

On \((0,1)\),
\[
\frac{1-G^2}{1+G^2}
\]
has derivative
\[
-\frac{4G}{(1+G^2)^2}<0,
\]
while
\[
\frac{2G}{1-G^2}
\]
has derivative
\[
\frac{2(1+G^2)}{(1-G^2)^2}>0.
\]
Reciprocal symmetry gives the corresponding monotonicity on \((1,\infty)\). Since \(\tanh\) is strictly increasing, the extrema and endpoint limits follow.

For the crossover, strict monotonicity of \(\tanh\) reduces equality of the coefficients to equality of their nonnegative inputs. Clearing denominators gives the reciprocal quartic. Dividing by \(G^2\) converts it to
\[
(G+G^{-1})^2-2(G+G^{-1})-4=0,
\]
which has the admissible root \(1+\sqrt5\). Solving the reciprocal quadratic produces \(G_-\) and \(G_+\). Checking \(G=1\) fixes the inequality direction between the crossings.

## Verification

The accompanying `verify.py` checks the paper angle directly from alternating gradients, both closed angular-coefficient formulas, reciprocal symmetry, the two crossover amplitudes, the unique-extremum pattern, and the exact separation at \(G=1\).

The finite calculations are transcription guards. The phase diagram is proved algebraically above.

## Relationship to prior work

Roy, Paoletti, Haut, Dubey, Kar, Plaza, and Chaudhuri introduced AngularGrad specifically to exploit the direction and angle of consecutive gradients. Algorithm 2 defines the tangent-difference angle, takes the minimum of two adjacent angles, and multiplies the Adam-style update by an angular coefficient in the interval from one half to one. The paper develops cosine and tangent variants, proves an online regret bound, and evaluates both on one-dimensional nonconvex functions, Rosenbrock optimization, and image-classification tasks.

The source's geometric discussion interprets the coefficient as responding to the angle between consecutive gradients and analyzes the limiting cosine case near zero and right angles. The inspected full text does not state that the scalar angle depends on the common magnitude of a fixed sign-alternating direction sequence, does not give the reciprocal-amplitude symmetry, and does not derive the opposite extrema of the cosine and tangent variants.

The official implementation uses the same elementwise quantity
\[
\left|
\frac{g_{t-1}-g_t}{1+g_{t-1}g_t}
\right|
\]
and forms the cosine transform as
\[
(1+\tan^2A)^{-1/2}.
\]
It contains additional state-selection logic beyond the displayed paper minimum, so it is supporting evidence for the scale-sensitive transform rather than the object proved here.

Later angle-aware optimization work such as Torque-Aware Momentum uses a normalized cosine similarity between momentum and the current gradient. That construction is scale invariant by normalization and therefore does not imply the amplitude phase diagram for AngularGrad's tangent-difference formula.

Focused published-record and web searches for AngularGrad scale invariance, gradient rescaling, alternating gradients, reciprocal amplitude, and equivalent cosine/tangent phase diagrams did not identify an implication-equivalent result.

## Limitations

The theorem is one-dimensional and isolates the paper's angular coefficient rather than the complete Adam-style update.

The result does not determine whether the amplitude dependence is beneficial or harmful on a particular training problem.

The official repository's state-selection logic is not identical to the displayed adjacent-angle minimum, so implementation-specific trajectories require a separate analysis.

The finding is a structural boundary of the published angle formula, not a claim about every conceivable vector-angle optimizer.

## References

1. S. K. Roy, M. E. Paoletti, J. M. Haut, S. R. Dubey, P. Kar, A. Plaza, and B. B. Chaudhuri, “AngularGrad: A New Optimization Technique for Angular Convergence of Convolutional Neural Networks,” arXiv:2105.10190v1, 2021.
2. P. Malviya, G. Mordido, A. Baratin, R. B. Harikandeh, G. K. Dziugaite, R. Pascanu, and S. Chandar, “Torque-Aware Momentum,” arXiv:2412.18790v1, 2024.
