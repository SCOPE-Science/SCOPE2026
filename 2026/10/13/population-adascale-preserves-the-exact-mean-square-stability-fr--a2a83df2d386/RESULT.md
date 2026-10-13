# Population AdaScale preserves the exact mean-square stability frontier across scales
## Finding

AdaScale multiplies a base learning rate by a variance-dependent gain when several independent gradients are averaged. On a natural random-curvature quadratic, that gain has an exact stability interpretation.

Let the sample loss be
\[
f_A(x)=\frac{A}{2}x^2,
\]
where fresh curvatures satisfy
\[
A\ge0,
\qquad
\mu=\mathbb E[A]>0,
\qquad
v=\operatorname{Var}(A)<\infty.
\]
Write
\[
q=\mathbb E[A^2]=\mu^2+v.
\]
The population objective is
\[
F(x)=\frac{\mu}{2}x^2.
\]

At scale
\[
S\ge1,
\]
AdaScale averages independent sample gradients. Put
\[
\bar A_t=\frac1S\sum_{i=1}^S A_{t,i}.
\]
Then
\[
\mathbb E[\bar A_t]=\mu,
\qquad
\mathbb E[\bar A_t^2]=\mu^2+\frac{v}{S}.
\]

For this model, the source population gain becomes the state-independent constant
\[
\boxed{
r_S=
\frac{\mu^2+v}{\mu^2+v/S}
=
\frac{q}{\mu^2+v/S}.
}
\]
With constant base learning rate
\[
\alpha>0,
\]
the exact iteration is
\[
\boxed{
x_{t+1}=(1-\alpha r_S\bar A_t)x_t.
}
\]

Hence the conditional squared-error multiplier is
\[
\boxed{
Q_S(\alpha)
=
1+
\frac{q}{\mu^2+v/S}
\left(\alpha^2q-2\alpha\mu\right).
}
\]
Fresh batches are independent of the current iterate, so
\[
\boxed{
\mathbb E[x_t^2]=Q_S(\alpha)^t x_0^2
}
\]
and equivalently
\[
\boxed{
\mathbb E[F(x_t)]=Q_S(\alpha)^t F(x_0).
}
\]

The sign of
\[
Q_S(\alpha)-1
\]
is independent of
\[
S.
\]
Therefore mean-square convergence holds exactly when
\[
\boxed{
0<\alpha<\frac{2\mu}{\mu^2+v}.
}
\]
At equality the second moment is constant. Above it the expected objective grows geometrically. Thus AdaScale preserves the sharp single-batch base-rate stability frontier at every scale.

The quadratic multiplier is uniquely minimized at
\[
\boxed{
\alpha_*=\frac{\mu}{\mu^2+v},
}
\]
also independently of scale. At that rate,
\[
\boxed{
Q_S(\alpha_*)=
\frac{v}{S\mu^2+v}.
}
\]
When
\[
v>0,
\]
this decreases strictly with
\[
S
\]
and obeys
\[
Q_S(\alpha_*)
\sim
\frac{v}{S\mu^2}.
\]
Thus scale improves the best one-step expected-objective contraction without narrowing the admissible base-rate interval.

For comparison, the source linear-scaling rule uses effective learning rate
\[
\alpha S.
\]
On the same model its exact multiplier is
\[
Q_S^{\mathrm{lin}}(\alpha)
=
1-2\alpha S\mu
+
\alpha^2S^2\left(\mu^2+\frac{v}{S}\right),
\]
so linear scaling is mean-square stable exactly when
\[
\boxed{
0<\alpha<\frac{2\mu}{S\mu^2+v}.
}
\]
For every
\[
S>1,
\]
this interval is strictly smaller than the single-batch interval. AdaScale's variance gain therefore performs an exact cancellation that fixed linear scaling does not.

## Assumptions and scope

The statement concerns the population-gain AdaScale rule defined in the source, not the finite-sample moving-average estimator used by practical implementations.

The sample curvature is nonnegative, has positive mean, and has finite second moment. Fresh samples are independent across workers and iterations.

The base learning-rate schedule is constant. This removes schedule effects and isolates the scaling mechanism.

The source population gain is written as a ratio of expectations over the current training-state distribution. In this model both numerator and denominator contain the same factor
\[
\mathbb E[x_t^2],
\]
so the ratio is constant whenever that factor is positive. If the process has already reached zero almost surely, the optimization problem is already solved and the gain may be extended by the same constant without changing the iterate.

The model has multiplicative gradient noise. The source's global bounded-variance assumption used for its general convergence theorem is not satisfied on the whole real line when
\[
v>0.
\]
The result therefore analyzes the defining algorithm directly rather than invoking that theorem.

## Proof

For a fixed state
\[
x,
\]
a single sample gradient is
\[
g=A x.
\]
Its squared mean and variance are
\[
\mu_g^2(x)=\mu^2x^2,
\qquad
\sigma_g^2(x)=v x^2.
\]
The defining AdaScale gain is the ratio
\[
r_S=
\frac{\mathbb E[\sigma_g^2(x_t)+\mu_g^2(x_t)]}
{\mathbb E[S^{-1}\sigma_g^2(x_t)+\mu_g^2(x_t)]}.
\]
The common state factor cancels, giving
\[
r_S=
\frac{\mu^2+v}{\mu^2+v/S}.
\]

The averaged gradient is
\[
\bar g_t=\bar A_t x_t.
\]
The source update with constant base rate is therefore
\[
x_{t+1}=(1-\alpha r_S\bar A_t)x_t.
\]
Conditioning on
\[
x_t
\]
and using the first two moments of the batch average yields
\[
\mathbb E[x_{t+1}^2\mid x_t]
=
\left(
1-2\alpha r_S\mu
+
\alpha^2r_S^2\left(\mu^2+\frac{v}{S}\right)
\right)x_t^2.
\]
Substitution of
\[
r_S=\frac{q}{\mu^2+v/S}
\]
gives
\[
Q_S(\alpha)
=
1+
\frac{q}{\mu^2+v/S}
(\alpha^2q-2\alpha\mu).
\]
Fresh batches make the same conditional factor apply at every iteration, proving the exact geometric law.

Since
\[
\frac{q}{\mu^2+v/S}>0,
\]
strict contraction is equivalent to
\[
\alpha^2q-2\alpha\mu<0.
\]
For positive base rate this is precisely
\[
0<\alpha<\frac{2\mu}{q}.
\]
Equality gives
\[
Q_S(\alpha)=1,
\]
and supercritical rates give
\[
Q_S(\alpha)>1.
\]
This proves sharpness.

Differentiating the quadratic in
\[
\alpha
\]
shows that its unique minimizer is
\[
\alpha_*=\frac{\mu}{q}.
\]
Substitution gives
\[
Q_S(\alpha_*)
=1-
\frac{\mu^2}{\mu^2+v/S}
=
\frac{v}{S\mu^2+v}.
\]

Finally, fixed linear scaling replaces
\[
\alpha r_S
\]
by
\[
\alpha S.
\]
Repeating the one-line second-moment calculation gives
\[
Q_S^{\mathrm{lin}}(\alpha)-1
=
\alpha S
\left[
\alpha(S\mu^2+v)-2\mu
\right],
\]
which yields its stated exact stability interval.

## Verification

The accompanying `verify.py` reconstructs the source population gain and the batched update on exact two-point curvature distributions.

It enumerates the complete binomial law of each batch average, checks the closed multiplier against direct expectation, verifies the scale-independent sharp stability boundary and optimizer, verifies the optimal factor, and checks the strictly shrinking linear-scaling comparator.

These finite checks guard the transcription and algebra. The theorem for arbitrary finite-second-moment curvature distributions follows analytically from the first two moments and does not depend on finite enumeration.

## Relationship to prior work

Johnson, Agrawal, Gu, and Guestrin define AdaScale's gain as the ratio of the expected single-batch squared-gradient scale to the expected squared scale of the averaged gradient. Their theory explains why the gain interpolates between identity and linear scaling and proves a general convergence bound that preserves model quality across many scales under a bounded-variance assumption.

The defining paper also gives a separate theorem for fixed linear scaling and emphasizes that linear scaling can become unreliable at large scale. Those results motivate the question here, but the inspected paper does not state the random-curvature mean-square multiplier, the exact scale-invariant sharp base-rate frontier, or the optimal factor
\[
\frac{v}{S\mu^2+v}.
\]
Its bounded-variance convergence theorem does not apply globally to the multiplicative-curvature model when
\[
v>0.
\]

Mean-square stability for general linear systems with multiplicative noise is a classical control-theoretic subject. That broader theory supplies a language for the stability criterion, but it does not contain AdaScale's variance-gain rule or the cancellation of batch-scale dependence derived here.

Focused published-record searches for AdaScale with mean-square stability, multiplicative curvature, random quadratics, and batch-scale contraction did not identify an implication-equivalent result. The closest indexed optimization records analyze different stochastic-gradient feedback or variance-reduced recurrences.

## Limitations

The finding is for the ideal population gain, not the online exponential-moving-average gain estimator.

The model is one-dimensional and quadratic. Multidimensional random Hessians need not commute, so a scalar second-moment cancellation need not extend mode by mode.

The multiplicative-noise model has state-dependent variance and falls outside the defining paper's global bounded-variance theorem when
\[
v>0.
\]

The result classifies expected objective and mean-square behavior; it does not claim almost-sure convergence at the entire mean-square stability boundary.

## References

1. Tyler B. Johnson, Pulkit Agrawal, Haijie Gu, and Carlos Guestrin, “AdaScale SGD: A User-Friendly Algorithm for Distributed Training,” arXiv:2007.05105v1, first submitted 2020-07-09; Proceedings of the 37th International Conference on Machine Learning, PMLR 119:4911--4920, 2020.
2. Zhiguo Yan, Fangxu Su, and Zhiwei Gao, “Mean-square strong stability and stabilization of discrete-time stochastic systems with multiplicative noises,” International Journal of Robust and Nonlinear Control 32(12), 2022, DOI `10.1002/rnc.6161`.
