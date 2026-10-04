# Circle-rotation law for multiplicative Hypergradient Descent on a quadratic
## Finding

Consider
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0,
\]
and multiplicative Hypergradient Descent with
\[
0<\beta<1.
\]
Let
\[
q_t=\lambda\alpha_t
\]
be the learning rate normalized by curvature.

For nonzero successive gradients, the multiplicative rule scales the learning rate by \(1+\beta\) when consecutive gradients have the same sign and by \(1-\beta\) when their signs differ. Since
\[
x_{t+1}=(1-q_t)x_t,
\]
the exact normalized learning-rate map is
\[
q_{t+1}
=
\begin{cases}
(1+\beta)q_t,&q_t<1,\\
(1-\beta)q_t,&q_t>1.
\end{cases}
\]
If
\[
q_t=1,
\]
then
\[
x_{t+1}=0,
\]
so the minimizer is reached exactly and the sign-normalized learning-rate rule need not be evaluated again.

Every positive nonresonant orbit reaches the invariant band
\[
[1-\beta,1+\beta]
\]
after finitely many steps. Once the band is reached,
\[
|x_{t+1}|=|1-q_t||x_t|\le\beta|x_t|.
\]
Thus the primal parameter converges geometrically even though the learning rate need not converge.

The band dynamics are exactly a rigid circle rotation. Define
\[
A=\log(1+\beta),
\qquad
C=-\log(1-\beta),
\qquad
L=A+C
=
\log\left(\frac{1+\beta}{1-\beta}\right).
\]
Identify the two endpoints of the invariant band and set
\[
z_t=\log q_t+C\pmod L.
\]
Then both branches of the learning-rate map become
\[
z_{t+1}=z_t+A\pmod L.
\]
The rotation number is therefore
\[
\theta(\beta)
=
\frac{\log(1+\beta)}
{\log((1+\beta)/(1-\beta))}.
\]

If
\[
\theta(\beta)=\frac{p}{m}
\]
is rational in lowest terms, every nonresonant band orbit has exact period \(m\). If \(\theta(\beta)\) is irrational, every nonresonant band orbit is dense in the band and the learning rate has no limit.

Both regimes occur for simple parameter values. If
\[
\beta=\frac{\sqrt5-1}{2},
\]
then
\[
1+\beta=\frac1\beta,
\qquad
1-\beta=\beta^2,
\]
so
\[
\theta=\frac13.
\]
Every nonresonant band orbit has period three.

If
\[
\beta=\frac12,
\]
then
\[
\theta
=
\frac{\log(3/2)}{\log3}.
\]
This is irrational: a rational equality \(\theta=m/n\) would imply
\[
\left(\frac32\right)^n=3^m,
\]
contradicting unique prime factorization. Hence the normalized learning rate is dense in
\[
\left[\frac12,\frac32\right],
\]
or the physical learning rate is dense in
\[
\left[\frac{1}{2\lambda},\frac{3}{2\lambda}\right],
\]
while \(x_t\) still converges to zero.

## Assumptions and scope

The theorem uses the multiplicative, gradient-correlation-normalized Hypergradient Descent rule rather than the original additive hypergradient update.

The rule is considered while successive gradients are nonzero. If \(q_t=1\), the next primal update reaches the minimizer exactly and optimization can terminate.

The objective is deterministic and scalar. Momentum, stochastic gradients, multidimensional gradient angles, and additive hypergradient updates are outside the claim.

The metadata uses the earliest verified public date of the Baydin et al. preprint, 2017-03-14, rather than the date of the later revision that contains the multiplicative form. The 2017 thesis is important supporting literature but is publicly dated only by year in the inspected source.

## Proof

Let
\[
g_t=\lambda x_t.
\]
The primal update gives
\[
x_{t+1}
=
x_t-\alpha_tg_t
=
(1-q_t)x_t.
\]
Therefore consecutive gradients have the same sign exactly when \(q_t<1\) and opposite signs exactly when \(q_t>1\), which proves the piecewise multiplicative map.

Put
\[
a=1+\beta,
\qquad
b=1-\beta.
\]
If \(q_t\le b\), repeated multiplication by \(a>1\) eventually gives a first iterate above \(b\). Since the preceding iterate was at most \(b\), the crossing value is at most
\[
ab=1-\beta^2<1,
\]
so it lies in the invariant band. If \(q_t\ge a\), repeated multiplication by \(b<1\) eventually gives a first iterate below \(a\); because the preceding iterate was at least \(a\), the crossing value is at least
\[
ab=1-\beta^2>b.
\]
Thus every positive nonresonant orbit enters the band in finite time.

The band is invariant because
\[
q\in[b,1)
\quad\Longrightarrow\quad
aq\in[ab,a),
\]
and
\[
q\in(1,a]
\quad\Longrightarrow\quad
bq\in(b,ab].
\]

Inside the band, if \(q_t<1\),
\[
z_{t+1}=z_t+A.
\]
If \(q_t>1\),
\[
z_{t+1}=z_t-C=z_t+A-L.
\]
Hence, modulo \(L\),
\[
z_{t+1}=z_t+A.
\]

The classical classification of rigid circle rotations now gives exact period \(m\) for a rational rotation number \(p/m\), and density for an irrational rotation number. Finally,
\[
|1-q_t|\le\beta
\]
throughout the invariant band, proving
\[
|x_{t+1}|\le\beta|x_t|.
\]

## Verification

The accompanying `verify.py` reconstructs the scalar recurrence, checks finite band entry over a wide range of initial learning rates, verifies the logarithmic rotation identity, confirms the period-three example, and checks finite dense coverage for the analytically proven irrational example \(\beta=1/2\).

Finite coverage is only a transcription guard. Irrationality for \(\beta=1/2\), the rigid-rotation conjugacy, and the rational-versus-irrational classification are established analytically above.

## Relationship to prior work

Baydin, Cornish, Martínez-Rubio, Schmidt, and Wood introduced Hypergradient Descent as online learning-rate adaptation through a hypergradient. Their later public version includes an alternative multiplicative rule based on normalized gradient correlation.

Martínez-Rubio's 2017 thesis derives the same multiplicative rule and proves convergence on one-dimensional convex quadratics. Its proof traps the learning rate in a curvature-scaled stable interval and establishes contraction of the primal variable. The inspected thesis does not classify the trapped learning-rate sequence as a circle rotation and contains no periodic-versus-dense theorem.

Recent work on provable online hypergradient learning-rate adaptation cites the earlier scalar quadratic convergence result but develops a different online-learning formulation. The inspected discussion does not state the rigid-rotation law for the multiplicative sign rule.

The present finding therefore does not re-prove primal convergence as a novelty claim. It resolves the asymptotic dynamics of the adaptive hyperparameter itself: the optimized parameter may converge geometrically while the learning rate is periodic or dense forever.

## Limitations

The circle law relies on one-dimensional gradient signs. In multiple dimensions, normalized inner products of successive gradients take a continuum of values.

Noise can destroy the exact rigid rotation.

The physical invariant band scales with \(1/\lambda\), so the result does not imply that one scalar learning rate can track several curvatures simultaneously.

Finite-termination resonances are excluded from the periodic and dense classifications because the gradient becomes zero.

## References

1. Atilim Gunes Baydin, Robert Cornish, David Martínez-Rubio, Mark Schmidt, and Frank Wood, “Online Learning Rate Adaptation with Hypergradient Descent,” arXiv:1703.04782v3, 2018.
2. David Martínez-Rubio, “Convergence Analysis of an Adaptive Method of Gradient Descent,” University of Oxford MSc thesis, 2017.
3. Yuxuan Chu et al., “Provable and Practical Online Learning Rate Adaptation with Hypergradient Descent,” arXiv:2502.11229, 2025.
