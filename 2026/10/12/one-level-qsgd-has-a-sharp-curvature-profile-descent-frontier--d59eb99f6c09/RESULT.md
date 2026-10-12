# One-level QSGD has a sharp curvature-profile descent frontier
## Finding

QSGD quantizes a vector by normalizing its coordinates by the Euclidean norm and then stochastically rounding each normalized magnitude. At its most aggressive precision parameter
\[
s=1,
\]
the quantizer has an especially simple exact law: for a nonzero vector
\[
g\in\mathbb R^d,
\]
its \(i\)-th output coordinate is
\[
Q_1(g)_i
=
\|g\|_2\,\operatorname{sign}(g_i)B_i,
\]
where the \(B_i\) are independent Bernoulli variables with
\[
\mathbb P(B_i=1)
=
\frac{|g_i|}{\|g\|_2}.
\]
Consequently,
\[
\mathbb E[Q_1(g)_i]=g_i
\]
and
\[
\mathbb E[Q_1(g)_i^2]
=
\|g\|_2|g_i|.
\]

Now let
\[
A=\operatorname{diag}(a_1,\ldots,a_d),
\qquad
a_i>0,
\]
and consider the diagonal positive-definite quadratic
\[
f(x)=\frac12x^\top A x.
\]
Write
\[
g=Ax
\]
and use the compressed-gradient update
\[
x^+=x-\eta Q_1(g),
\qquad
\eta>0.
\]

Then, for every nonzero \(x\),
\[
\boxed{
\mathbb E[f(x^+)\mid x]
=
f(x)-\eta\|g\|_2^2
+
\frac{\eta^2}{2}\|g\|_2\sum_{i=1}^d a_i|g_i|.
}
\]

It follows that QSGD at \(s=1\) has the exact curvature-profile descent frontier
\[
\boxed{
0<\eta<
\frac{2}{\|(a_1,\ldots,a_d)\|_2}.
}
\]
More precisely, strict conditional expected descent
\[
\mathbb E[f(x^+)\mid x]<f(x)
\]
holds for every nonzero \(x\) if and only if the displayed inequality holds.

The boundary is attained by a natural dense direction. Equality in the worst-case Cauchy--Schwarz step occurs when
\[
|g_i|\propto a_i,
\]
which, because
\[
g_i=a_i x_i,
\]
is exactly the family in which all coordinate magnitudes
\[
|x_i|
\]
are equal. At the boundary step the expected objective is unchanged on that direction, and for every larger step it increases.

For the isotropic quadratic
\[
A=L I,
\]
write
\[
h=\eta L.
\]
Then the exact conditional factor is
\[
\frac{\mathbb E[f(x^+)\mid x]}{f(x)}
=
1-2h+h^2\frac{\|x\|_1}{\|x\|_2}.
\]
Therefore
\[
\boxed{
\sup_{x\ne0}
\frac{\mathbb E[f(x^+)\mid x]}{f(x)}
=
1-2h+\sqrt d\,h^2.
}
\]
Uniform expected contraction holds exactly for
\[
\boxed{
0<h<\frac{2}{\sqrt d}.
}
\]
The unique minimax choice is
\[
\boxed{
h_\star=\frac1{\sqrt d},
\qquad
\rho_\star=1-\frac1{\sqrt d}.
}
\]

This gives a sharp stability tax for aggressive quantization. The uncompressed gradient-descent step
\[
h=1
\]
solves the isotropic quadratic in one step, but with one-level QSGD its worst dense-direction factor becomes
\[
\sqrt d-1.
\]
It is neutral when
\[
d=4
\]
and strictly larger than one for every
\[
d\ge5.
\]

## Assumptions and scope

The result concerns the QSGD stochastic quantizer defined in the original QSGD work, specialized to
\[
s=1.
\]

There is one deterministic gradient vector per iteration; the only randomness comes from QSGD. The update uses a scalar constant step
\[
\eta.
\]

The objective is a finite-dimensional diagonal positive-definite quadratic. The diagonal basis is the quantizer's coordinate basis; arbitrary rotations of the quadratic are not covered because QSGD is coordinate dependent.

The sharp frontier is for universal one-step expected objective descent over all nonzero states of this fixed diagonal quadratic. In the isotropic case the conditional bound iterates, so for
\[
0<h<2/\sqrt d
\]
it also gives geometric convergence in expected objective.

The theorem does not analyze finite-bit encoding overhead, stochastic-gradient noise, multiple workers, error feedback, momentum, or higher precision parameters
\[
s>1.
\]

## Proof

For
\[
s=1,
\]
the source quantization interval is
\[
[0,1].
\]
Thus the random normalized magnitude in coordinate \(i\) is a Bernoulli variable
\[
B_i\in\{0,1\}
\]
with mean
\[
\mathbb E[B_i]
=
\frac{|g_i|}{\|g\|_2}.
\]
Hence
\[
Q_1(g)_i
=
\|g\|_2\operatorname{sign}(g_i)B_i.
\]

The first two coordinate moments are therefore
\[
\mathbb E[Q_1(g)_i]
=
g_i
\]
and
\[
\mathbb E[Q_1(g)_i^2]
=
\|g\|_2^2\mathbb E[B_i]
=
\|g\|_2|g_i|.
\]

Because
\[
f(x-\eta q)
=
f(x)-\eta g^\top q+\frac{\eta^2}{2}q^\top A q,
\]
taking conditional expectation with
\[
q=Q_1(g)
\]
gives
\[
\mathbb E[f(x^+)\mid x]
=
f(x)
-
\eta\|g\|_2^2
+
\frac{\eta^2}{2}
\sum_{i=1}^d
a_i\mathbb E[Q_1(g)_i^2].
\]
Substituting the second moment yields
\[
\mathbb E[f(x^+)\mid x]
=
f(x)
-
\eta\|g\|_2^2
+
\frac{\eta^2}{2}
\|g\|_2
\sum_{i=1}^d a_i|g_i|.
\]

For a fixed nonzero gradient, strict descent is equivalent to
\[
\eta
<
\frac{2\|g\|_2}
{\sum_i a_i|g_i|}.
\]
Since every nonzero \(g\) can occur for some nonzero \(x\), the universal threshold is the infimum of this quantity. Cauchy--Schwarz gives
\[
\sum_i a_i|g_i|
\le
\|(a_1,\ldots,a_d)\|_2\|g\|_2.
\]
The bound is attained exactly when
\[
(|g_1|,\ldots,|g_d|)
\]
is proportional to
\[
(a_1,\ldots,a_d).
\]
Therefore the exact universal frontier is
\[
\eta
<
\frac{2}{\|(a_1,\ldots,a_d)\|_2}.
\]
Because
\[
g_i=a_i x_i,
\]
an attaining state has equal coordinate magnitudes.

For
\[
A=L I,
\]
we have
\[
g=Lx,
\qquad
f(x)=\frac L2\|x\|_2^2.
\]
Dividing the expected-objective identity by \(f(x)\) gives
\[
\frac{\mathbb E[f(x^+)\mid x]}{f(x)}
=
1-2h+h^2\frac{\|x\|_1}{\|x\|_2},
\qquad
h=\eta L.
\]
The sharp inequality
\[
\frac{\|x\|_1}{\|x\|_2}
\le
\sqrt d
\]
is attained by equal-magnitude dense vectors. This gives the exact worst factor
\[
1-2h+\sqrt d\,h^2.
\]
It is smaller than one exactly for
\[
0<h<2/\sqrt d,
\]
and its unique minimum occurs at
\[
h=1/\sqrt d.
\]
Substitution gives
\[
1-1/\sqrt d.
\]

Finally, at
\[
h=1
\]
the dense-direction factor is
\[
\sqrt d-1,
\]
which equals one at
\[
d=4
\]
and exceeds one for
\[
d\ge5.
\]

## Verification

The accompanying `verify.py` reconstructs the \(s=1\) QSGD distribution directly.

For dimensions up to eight it enumerates all Bernoulli support patterns, computes the exact expected quadratic objective from the discrete distribution, and compares it with the closed-form identity above.

It also checks random diagonal curvature profiles, the equality direction at the sharp threshold, strict expected descent below the threshold, expected increase above it, and the isotropic minimax factor.

These finite computations are transcription guards only. The all-dimensional frontier follows from the exact moment calculation and Cauchy--Schwarz argument in the proof.

## Relationship to prior work

Alistarh and coauthors introduced QSGD and proved unbiasedness together with a dimension-dependent variance bound for its generalized stochastic quantizer. Their analysis uses that variance control to establish convergence and communication tradeoffs. The source does not state an exact constant-step expected-objective stability frontier for deterministic diagonal quadratics.

General compressed-gradient theory later parameterized unbiased compressors by a scalar variance parameter. Applied with the sharp worst-case variance of one-level QSGD, that framework is compatible with the isotropic
\[
1/\sqrt d
\]
stepsize scale. Accordingly, the dimension-only scaling is not the originality claim here. The additional statement is the exact curvature-profile replacement
\[
\sqrt d\,L
\longrightarrow
\|(a_1,\ldots,a_d)\|_2,
\]
together with the exact equality direction and one-step objective formula. This can be much less conservative when only a few coordinates carry the largest curvature.

Matrix-smooth compressed-gradient work gives finer stepsize conditions for random linear sketches with a fixed sketch distribution. The one-level QSGD law is nonlinear and state dependent: its Bernoulli probabilities depend on the current normalized gradient magnitudes. Thus those fixed-sketch matrix conditions do not directly imply the curvature-profile identity here.

Focused searches for one-level QSGD on diagonal quadratics, exact expected-objective frontiers, curvature-profile thresholds, and isotropic square-root-dimension stability did not identify an implication-equivalent published statement.

## Limitations

The theorem is specific to
\[
s=1
\]
and to diagonal quadratics in the quantizer coordinate basis.

The universal threshold concerns expected objective after one step. Almost-sure monotonicity is neither claimed nor generally true.

The isotropic geometric rate follows by iterating the conditional expectation bound, but no claim is made that the minimax one-step step size is globally optimal among adaptive or error-feedback compressed methods.

The result does not compare end-to-end communication complexity, since QSGD's encoding cost and the number of iterations must both be considered for that question.

## References

1. Dan Alistarh, Demjan Grubic, Jerry Li, Ryota Tomioka, and Milan Vojnovic, “QSGD: Communication-Efficient SGD via Gradient Quantization and Encoding,” arXiv:1610.02132v1, first submitted 2016-10-07; NeurIPS 2017.
2. Zhize Li, Dmitry Kovalev, Xun Qian, and Peter Richtárik, “Acceleration for Compressed Gradient Descent in Distributed and Federated Optimization,” arXiv:2002.11364v1, first submitted 2020-02-26; ICML 2020.
3. Hanmin Li, Avetik Karagulyan, and Peter Richtárik, “Det-CGD: Compressed Gradient Descent with Matrix Stepsizes for Non-Convex Optimization,” arXiv:2305.12568v1, first submitted 2023-05-21.
