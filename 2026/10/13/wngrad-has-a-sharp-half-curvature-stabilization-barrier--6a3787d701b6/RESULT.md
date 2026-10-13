# WNGrad has a sharp half-curvature stabilization barrier
## Finding

WNGrad was proposed to learn a scalar learning rate from gradient observations rather than requiring the smoothness constant in advance. On an isotropic quadratic, its self-tuning mechanism admits a complete transient classification.

Let
\[
F(x)=\frac12\lambda\lVert x\rVert_2^2,
\qquad
\lambda>0,
\]
and let the current scalar scale satisfy
\[
b_k>0.
\]
The source displays the parameter step
\[
x_{k+1}=x_k-\frac{1}{b_k}\nabla F(x_k).
\]
It also displays two nearby accumulator index conventions: the defining recurrence uses
\[
b_{k+1}=b_k+\frac{\lVert\nabla F(x_k)\rVert_2^2}{b_k},
\]
while the later batch pseudocode uses the post-step gradient,
\[
b_{k+1}=b_k+\frac{\lVert\nabla F(x_{k+1})\rVert_2^2}{b_k}.
\]
The theorem below holds for either convention.

Define the dimensionless scale and radius
\[
z_k=\frac{b_k}{\lambda},
\qquad
r_k=\lVert x_k\rVert_2.
\]
Then
\[
x_{k+1}=\left(1-\frac1{z_k}\right)x_k,
\]
so whenever \(r_k>0\),
\[
\boxed{
\frac{F(x_{k+1})}{F(x_k)}
=
\left(1-\frac1{z_k}\right)^2.
}
\]
Consequently,
\[
\boxed{
F(x_{k+1})>F(x_k)
\iff
z_k<\frac12,
}
\]
with equality at \(z_k=1/2\), and strict decrease for \(z_k>1/2\).

Thus the exact objective-monotonicity barrier is
\[
\boxed{b_k=\frac{\lambda}{2}.}
\]
This is the ordinary scalar gradient-descent stability boundary expressed in WNGrad's learned scale.

The important additional fact is that WNGrad cannot remain on the unstable side. For either source indexing convention, \(z_k\) is nondecreasing. If
\[
z_0<\frac12
\]
and \(r_0>0\), define \(K\) as the first index satisfying \(z_K\ge1/2\). Then \(K\) is finite and
\[
\boxed{
K\le
\left\lceil
\frac{1/2-z_0}{2r_0^2}
\right\rceil.
}
\]
Every objective-increasing step occurs before \(K\), and no objective increase is possible afterward.

The scale itself remains bounded. Hence for every initialization
\[
x_0\in\mathbb R^d,
\qquad
b_0>0,
\]
WNGrad converges on the isotropic quadratic:
\[
\boxed{x_k\longrightarrow0.}
\]
If the method does not hit the minimizer exactly in finite time, then
\[
z_k\longrightarrow z_\infty>\frac12
\]
and
\[
\boxed{
\frac{\lVert x_{k+1}\rVert_2}{\lVert x_k\rVert_2}
\longrightarrow
\left|1-\frac1{z_\infty}\right|<1.
}
\]
So after the finite unstable prefix, the trajectory eventually has a strict linear contraction factor determined by the learned limiting scale.

This remains true even when the initial learning rate
\[
1/b_0
\]
is larger than
\[
2/\lambda,
\]
so the first steps can amplify the objective by an arbitrarily large factor. The adaptive scale confines such spikes to a finite initial transient.

## Assumptions and scope

The objective is an isotropic positive quadratic. The result therefore isolates learning-rate adaptation without curvature anisotropy.

The source contains two index conventions for the scalar accumulator. The proof treats both explicitly; it does not assume they are identical recurrences.

The result is deterministic. It does not classify persistent stochastic-gradient noise.

The finite-prefix bound is a simple explicit upper bound and is not claimed to be the smallest possible bound for every initial condition. The barrier \(b=\lambda/2\), by contrast, is exact.

## Proof

Since
\[
\nabla F(x_k)=\lambda x_k,
\]
the parameter update gives
\[
x_{k+1}
=
\left(1-\frac{\lambda}{b_k}\right)x_k
=
\left(1-\frac1{z_k}\right)x_k.
\]
The displayed objective ratio follows immediately.

For the defining recurrence, the normalized accumulator update is
\[
z_{k+1}=z_k+\frac{r_k^2}{z_k}.
\]
For the later batch pseudocode it is
\[
z_{k+1}=z_k+\frac{r_{k+1}^2}{z_k}.
\]
Both increments are nonnegative.

Suppose \(z_k<1/2\). Then
\[
\left|1-\frac1{z_k}\right|>1,
\]
so
\[
r_{k+1}>r_k.
\]
As long as the trajectory remains below the barrier, therefore,
\[
r_k\ge r_0.
\]
For the defining recurrence,
\[
z_{k+1}-z_k
=
\frac{r_k^2}{z_k}
>
2r_0^2.
\]
For the post-step accumulator,
\[
z_{k+1}-z_k
=
\frac{r_{k+1}^2}{z_k}
>
2r_0^2.
\]
Summing these strict inequalities proves finite escape and the stated ceiling for \(K\).

It remains to prove that \(z_k\) cannot diverge after entering the safe region. If it never reaches \(1\), it is already bounded. Otherwise let \(J\) be an index with \(z_J\ge1\).

For the defining recurrence,
\[
r_k^2-r_{k+1}^2
=
r_k^2\left(\frac{2}{z_k}-\frac1{z_k^2}\right)
=
\left(2-\frac1{z_k}\right)(z_{k+1}-z_k).
\]
For \(z_k\ge1\), the coefficient is at least one, so
\[
z_{k+1}-z_k
\le
r_k^2-r_{k+1}^2.
\]
The total future growth of \(z_k\) is therefore bounded by \(r_J^2\).

For the post-step accumulator, if \(z_k>1\),
\[
\frac{r_k^2-r_{k+1}^2}{z_{k+1}-z_k}
=
\frac{z_k(2z_k-1)}{(z_k-1)^2}
\ge1.
\]
If \(z_k=1\), then \(r_{k+1}=0\) and the minimizer is reached immediately. Thus the same telescoping bound applies after crossing \(1\).

Hence \(z_k\) is monotone and bounded, so it converges to a finite limit. Its increments tend to zero. In either convention this forces \(r_k\to0\), because \(z_k\) stays bounded away from zero.

For a nontrivial trajectory that does not hit the minimizer in finite time, the limiting scale is strictly larger than \(1/2\): reaching exactly \(1/2\) with nonzero radius causes a strictly positive next accumulator increment. Taking limits in
\[
\frac{r_{k+1}}{r_k}
=
\left|1-\frac1{z_k}\right|
\]
then yields the stated strict linear factor.

## Verification

The accompanying `verify.py` implements both source index conventions on isotropic quadratics.

It checks the exact objective ratio, the sharp half-curvature sign change, finite escape from the unstable region, persistence of objective monotonicity after escape, and convergence from randomly generated initial scales that include learning rates far above the ordinary gradient-descent stability ceiling.

The finite computations are transcription guards. Global convergence and the barrier theorem are proved analytically above.

## Relationship to prior work

Wu, Ward, and Bottou introduce WNGrad to make gradient descent robust to an unknown smoothness scale. Their defining recurrence increases the scalar inverse stepsize using observed gradient norms. They prove batch convergence under stated initialization conditions and show that once the learned scale becomes sufficiently large, it remains controlled.

The source also contrasts WNGrad with fixed-step gradient descent, which can oscillate or diverge when the learning rate exceeds the classical smoothness threshold. The inspected full text does not give an exact state-space boundary for when WNGrad's own objective increases, nor a finite-prefix classification of those increases on quadratics.

Ward, Wu, and Bottou later analyze AdaGrad-Norm from arbitrary initialization. That method is closely related but uses a different accumulator, with a squared scale updated by accumulated squared gradient norms and a correspondingly different step rule. Their paper explicitly treats WNGrad as a different adaptive gradient algorithm. Its arbitrary-initialization theorem therefore does not imply the WNGrad state map classified here.

The present result identifies the exact scalar-quadratic frontier
\[
b=\lambda/2,
\]
proves that WNGrad leaves the unstable side in finite time from every positive initial scale, and shows that objective spikes can occur only in one initial prefix.

Focused published-record searches for WNGrad scalar-quadratic stability, half-smoothness thresholds, finite unstable transients, and arbitrary-initialization dynamics did not identify an implication-equivalent result.

## Limitations

The theorem is for isotropic quadratics and does not address multiple curvature modes.

It concerns deterministic WNGrad and does not cover stochastic-gradient noise.

The exact transient-count bound is sufficient rather than pointwise optimal.

The source's two displayed accumulator conventions are treated separately; no claim is made that their full trajectories coincide.

## References

1. Xiaoxia Wu, Rachel Ward, and Léon Bottou, “WNGrad: Learn the Learning Rate in Gradient Descent,” arXiv:1803.02865v1, first submitted 2018-03-07.
2. Rachel Ward, Xiaoxia Wu, and Léon Bottou, “AdaGrad Stepsizes: Sharp Convergence Over Nonconvex Landscapes,” arXiv:1806.01811v1, first submitted 2018-06-05; later ICML 2019 / JMLR 2020.
