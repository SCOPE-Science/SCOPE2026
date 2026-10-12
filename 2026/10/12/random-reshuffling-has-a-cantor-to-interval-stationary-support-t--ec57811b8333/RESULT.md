# Random reshuffling has a Cantor-to-interval stationary-support transition
## Finding

Consider constant-step random-reshuffling SGD on two equally weighted scalar components
\[
F_+(x)=\frac a2(x-b)^2,
\qquad
F_-(x)=\frac a2(x+b)^2,
\qquad
a,b>0.
\]
Their average objective is
\[
F(x)=\frac a2(x^2+b^2),
\]
whose unique minimizer is
\[
x^\star=0.
\]

Let
\[
h=\eta a\in(0,2)
\]
be the normalized local step, and reshuffle the two components independently and uniformly at every epoch. If
\[
X_k
\]
denotes the iterate at the start of epoch \(k\), then one complete epoch has the exact form
\[
\boxed{
X_{k+1}=rX_k+\delta\xi_k,
\qquad
r=(1-h)^2,
\qquad
\delta=h^2b,
}
\]
where
\[
\mathbb P(\xi_k=1)=\mathbb P(\xi_k=-1)=\frac12
\]
and the \(\xi_k\) are independent across epochs.

Since
\[
0\le r<1,
\]
this affine Markov chain has a unique stationary law,
\[
\boxed{
X_\infty
\overset d=
\delta\sum_{j=0}^{\infty}r^j\xi_j.
}
\]
Thus the epoch-start invariant law is exactly a scaled Bernoulli convolution.

Its second moment is
\[
\boxed{
\operatorname{Var}(X_\infty)
=
\frac{\delta^2}{1-r^2}
=
\frac{h^4b^2}{1-(1-h)^4}.
}
\]
Accordingly,
\[
\mathbb E\!\left[F(X_\infty)-F(0)\right]
=
\frac{ab^2h^4}{2\left(1-(1-h)^4\right)}.
\]
This moment formula agrees with the defining random-reshuffling paper's exact quadratic steady-state expression at two samples. The additional structure lies in the full stationary support.

If
\[
r>\frac12,
\]
then the stationary support is the full interval
\[
\boxed{
\operatorname{supp}(X_\infty)
=
\left[
-\frac{\delta}{1-r},
\frac{\delta}{1-r}
\right].
}
\]

If
\[
r=\frac12,
\]
then more is true:
\[
\boxed{
X_\infty
\sim
\operatorname{Uniform}[-2\delta,2\delta].
}
\]

If
\[
0<r<\frac12,
\]
then the support is a self-similar Cantor set satisfying the open-set condition. Its Hausdorff dimension is
\[
\boxed{
\dim_H\operatorname{supp}(X_\infty)
=
\frac{\log 2}{\log(1/r)}.
}
\]
Moreover, the minimizer lies in a sharp central gap:
\[
\boxed{
(-g,g)
\cap
\operatorname{supp}(X_\infty)
=
\varnothing,
\qquad
g=
\delta\frac{1-2r}{1-r}.
}
\]
Both endpoints
\[
\pm g
\]
belong to the support, so the gap is exact.

At the exceptional value
\[
r=0,
\]
equivalently
\[
h=1,
\]
each component step is an exact local solve and
\[
\operatorname{supp}(X_\infty)=\{-b,b\}.
\]

Because
\[
r=(1-h)^2,
\]
the support avoids the true strongly convex minimizer exactly when
\[
\boxed{
1-\frac1{\sqrt2}
<
h
<
1+\frac1{\sqrt2}.
}
\]
At the two boundary steps
\[
h=1\pm\frac1{\sqrt2},
\]
the invariant law is exactly uniform on an interval containing the minimizer. Outside this band, but still within the stable range
\[
0<h<2,
\]
the stationary support is a full interval.

Thus a constant-step random-reshuffling process can have zero stationary mean and small mean-square error while its epoch-start stationary support is nevertheless disconnected and separated by a positive gap from the exact minimizer.

## Assumptions and scope

The result uses two scalar, equal-curvature, equally weighted strongly convex quadratic components with opposite minimizers.

A fresh uniform permutation of the two components is drawn independently at every epoch. The step size is constant and satisfies
\[
0<h=\eta a<2,
\]
which is exactly the contraction range for the two-step epoch coefficient
\[
r=(1-h)^2.
\]

The support statements concern epoch-start iterates. Inner-epoch iterates have a different two-phase law and are not classified here.

For
\[
r>\frac12,
\]
only the support is asserted to be an interval. The Bernoulli-convolution measure itself may be singular for exceptional contraction parameters, so no general absolute-continuity claim is made.

The result is distributional and does not change the already-known exact steady-state mean-square formula for quadratic random reshuffling.

## Proof

Write
\[
q=1-h.
\]
A gradient step on the component centered at
\[
+b
\]
maps
\[
x
\mapsto
qx+hb,
\]
while a step on the component centered at
\[
-b
\]
maps
\[
x
\mapsto
qx-hb.
\]

For the order
\[
(+,-),
\]
one epoch therefore gives
\[
x
\mapsto
q(qx+hb)-hb
=
q^2x-h^2b.
\]
For the opposite order
\[
(-,+),
\]
the epoch map is
\[
x
\mapsto
q(qx-hb)+hb
=
q^2x+h^2b.
\]
The two orders are equiprobable and independent across epochs. Hence
\[
X_{k+1}=rX_k+\delta\xi_k
\]
with
\[
r=q^2=(1-h)^2,
\qquad
\delta=h^2b.
\]

Since
\[
0\le r<1,
\]
iteration gives
\[
X_k
=
r^kX_0
+
\delta\sum_{j=0}^{k-1}r^j\xi_{k-1-j}.
\]
The deterministic term converges to zero, and the random series converges absolutely. This proves convergence in distribution to the unique invariant law
\[
X_\infty
\overset d=
\delta\sum_{j=0}^{\infty}r^j\xi_j.
\]

Independence and zero mean give
\[
\operatorname{Var}(X_\infty)
=
\delta^2\sum_{j=0}^{\infty}r^{2j}
=
\frac{\delta^2}{1-r^2}.
\]

Let
\[
K=\operatorname{supp}(X_\infty).
\]
It is the unique nonempty compact set satisfying
\[
K=(rK-\delta)\cup(rK+\delta).
\]
Put
\[
M=\frac{\delta}{1-r}.
\]
Every signed series lies in
\[
[-M,M].
\]

If
\[
r\ge\frac12,
\]
the two images of the interval
\[
[-M,M]
\]
overlap or touch:
\[
rM-\delta
\ge
-rM+\delta.
\]
Their union is therefore the whole interval
\[
[-M,M].
\]
By uniqueness of the compact invariant set,
\[
K=[-M,M].
\]

At
\[
r=\frac12,
\]
the two images are the two half-intervals
\[
[-2\delta,0]
\quad\text{and}\quad
[0,2\delta].
\]
The uniform probability measure on
\[
[-2\delta,2\delta]
\]
is invariant under the equally weighted two-map system. Uniqueness of the stationary law proves the exact uniform distribution.

If
\[
0<r<\frac12,
\]
the two images are disjoint. The standard self-similar open-set condition therefore applies, giving
\[
\dim_H K
=
\frac{\log 2}{\log(1/r)}.
\]

For the central gap, write a stationary point as
\[
x
=
\delta\left(
\xi_0+\sum_{j=1}^{\infty}r^j\xi_j
\right).
\]
The tail has magnitude at most
\[
\frac{r}{1-r}.
\]
Since
\[
r<\frac12,
\]
the first sign dominates, and
\[
|x|
\ge
\delta\left(
1-\frac{r}{1-r}
\right)
=
\delta\frac{1-2r}{1-r}
=
g.
\]
Equality is attained by choosing the first sign one way and every later sign the opposite way. Hence
\[
\pm g\in K
\]
and
\[
(-g,g)\cap K=\varnothing.
\]

Finally,
\[
r<\frac12
\iff
|1-h|<\frac1{\sqrt2},
\]
which gives the stated minimizer-avoidance interval.

## Verification

The accompanying `verify.py` reconstructs both possible two-step epoch maps directly from the component gradients.

It checks the affine recurrence for random parameter choices, the exact variance identity, the source-paper two-sample quadratic MSD formula, the central-gap endpoints, finite-depth Cantor separation for
\[
r<\frac12,
\]
and the exact interval tiling at
\[
r=\frac12.
\]

The finite checks are transcription guards. The infinite stationary-law and support classifications follow from the contraction and self-similar-set arguments in the proof.

## Relationship to prior work

Ying, Yuan, Vlaski, and Sayed analyze constant-step random reshuffling for strongly convex finite sums. They prove the improved steady-state neighborhood scaling, derive an exact steady-state mean-square expression for quadratic risks, and explain periodic within-epoch behavior. For their orthonormal quadratic model, their exact expression specializes at two samples to the variance formula above. Their paper does not classify the invariant law or its support.

Domingo-Enrich later studies stationary variances of shuffled stochastic-gradient methods through power-spectral-density calculations, including quadratic experiments. That work is likewise second-order: its stated objects are stationary covariance and variance rather than the full invariant distribution.

Classical Bernoulli-convolution theory studies random series of the form
\[
\sum_{j\ge0}\pm r^j.
\]
In particular, the support is Cantor-like for
\[
r<1/2
\]
and is an interval for
\[
r\ge1/2.
\]
The use of that theory here is explicit rather than claimed as new. The new optimization statement is the exact identification of the two-sample random-reshuffling epoch chain with a Bernoulli convolution and the resulting sharp step-size phase diagram, including the explicit minimizer-avoidance gap.

Focused searches for random-reshuffling stationary laws, Bernoulli convolutions, Cantor support, and fractal invariant distributions did not identify a published random-reshuffling result with this support classification.

## Limitations

The complete support classification uses the special two-component equal-curvature scalar geometry.

The source's general quadratic mean-square theory is much broader than this example. The finding does not improve that moment formula.

For
\[
r>1/2,
\]
the stationary support is an interval but the invariant measure can have subtle regularity; no density classification is attempted.

The result concerns a constant step size. Diminishing-step random reshuffling converges to the optimizer under standard conditions and does not retain this stationary support.

## References

1. Bicheng Ying, Kun Yuan, Stefan Vlaski, and Ali H. Sayed, “Stochastic Learning under Random Reshuffling with Constant Step-sizes,” arXiv:1803.07964v1, first submitted 2018-03-21; IEEE Transactions on Signal Processing 67(2), 2019.
2. Carles Domingo-Enrich, “Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis,” arXiv:2206.00632v1, first submitted 2022-06-01.
3. Simon Baker, Henna Koivusalo, Sascha Troscheit, and Xintian Zhang, “On the Fourier transform of random Bernoulli convolutions,” Journal of the London Mathematical Society 113(4), first published 2026-04-09.
