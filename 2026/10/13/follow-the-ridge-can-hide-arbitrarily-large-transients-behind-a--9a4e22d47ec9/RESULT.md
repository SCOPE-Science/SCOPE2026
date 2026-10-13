# Follow-the-Ridge can hide arbitrarily large transients behind a fixed real spectrum
## Finding

Follow-the-Ridge (FR) was designed to remove the rotational behavior of gradient descent-ascent near sequential minimax points. Its defining analysis proves that the local Jacobian has real eigenvalues after a ridge-based similarity transformation.

On the canonical scalar quadratic family, those real eigenvalues do not control transient size.

Fix
\[
h>0,\qquad c>0,\qquad b\in\mathbb R,
\]
and consider
\[
f_b(x,y)
=
\frac12\left(h-\frac{b^2}{c}\right)x^2
+
bxy
-
\frac12cy^2.
\]
The follower Hessian is
\[
\partial_{yy}^2f_b=-c<0,
\]
and the leader Schur-complement curvature is
\[
\left(h-\frac{b^2}{c}\right)-b(-c)^{-1}b=h>0.
\]
Hence
\[
(0,0)
\]
is the unique strict local minimax. The exact follower ridge is
\[
y=\frac bc x.
\]

Apply source-form FR with leader step
\[
\eta_x>0
\]
and follower step
\[
\eta_y>0.
\]
Define
\[
e_t=y_t-\frac bc x_t,
\qquad
p=1-\eta_xh,
\qquad
q=1-\eta_yc.
\]
Then the FR dynamics triangularize exactly:
\[
\boxed{e_{t+1}=q e_t,}
\]
\[
\boxed{x_{t+1}=p x_t-\eta_x b e_t.}
\]

Thus
\[
e_t=q^t e_0.
\]
If
\[
p\ne q,
\]
then
\[
\boxed{
x_t
=
p^t x_0
-
\eta_x b
\frac{p^t-q^t}{p-q}
e_0.
}
\]
At the repeated-eigenvalue resonance
\[
p=q=r,
\]
the divided difference becomes a Jordan prefactor:
\[
\boxed{
x_t
=
r^t x_0
-
\eta_xb\,t r^{t-1}e_0.
}
\]

Consequently FR converges to
\[
(0,0)
\]
from every initialization on this quadratic family if and only if
\[
\boxed{|p|<1\quad\text{and}\quad|q|<1.}
\]
Equivalently,
\[
0<\eta_xh<2,
\qquad
0<\eta_yc<2.
\]

The sharper point is transient, not asymptotic. Fix any
\[
r\in(-1,1)
\]
and choose
\[
\eta_x=\frac{1-r}{h},
\qquad
\eta_y=\frac{1-r}{c}.
\]
For every
\[
b\in\mathbb R,
\]
the two eigenvalues of the FR iteration are still exactly
\[
r,r.
\]

Initialize at
\[
z_0=(x_0,y_0)=(0,1).
\]
Then
\[
e_0=1,
\]
and one FR step gives
\[
x_1=-\frac{(1-r)b}{h},
\]
\[
y_1=r-\frac{(1-r)b^2}{hc}.
\]
Therefore
\[
\boxed{
\frac{\lVert z_1\rVert_2^2}{\lVert z_0\rVert_2^2}
=
\left(\frac{(1-r)b}{h}\right)^2
+
\left(
r-\frac{(1-r)b^2}{hc}
\right)^2.
}
\]
This diverges like
\[
\frac{(1-r)^2b^4}{h^2c^2}
\]
as
\[
|b|\to\infty,
\]
while the complete eigenvalue multiset stays fixed at
\[
\{r,r\}.
\]

Because the system is linear, scaling \(z_0\) by any positive constant leaves the amplification ratio unchanged. The phenomenon is therefore both global and arbitrarily local around the minimax point.

The defining FR paper uses the illustrative quadratic
\[
f(x,y)=-3x^2+4xy-y^2.
\]
For this example,
\[
c=2,
\qquad
b=4,
\qquad
h=2.
\]
With equal player steps
\[
\eta_x=\eta_y=\eta,
\]
one has
\[
p=q=1-2\eta.
\]
Thus the paper's own canonical example lies exactly on the repeated-eigenvalue resonance and has the polynomial prefactor
\[
t(1-2\eta)^{t-1}
\]
in its off-ridge transient.

## Assumptions and scope

The theorem concerns the exact deterministic FR iteration on a scalar quadratic sequential minimax problem.

The family is parameterized so that the follower curvature
\[
c
\]
and the leader Schur-complement curvature
\[
h
\]
remain fixed while the cross-coupling
\[
b
\]
varies.

No stochastic gradients, approximate Hessian inverses, momentum, or preconditioning are used.

The unbounded amplification statement concerns Euclidean state norm. It does not contradict asymptotic convergence when
\[
|p|<1
\quad\text{and}\quad
|q|<1.
\]

## Proof

Write
\[
a=h-\frac{b^2}{c}.
\]
Then
\[
\nabla_xf_b=ax+by,
\qquad
\nabla_yf_b=bx-cy.
\]

The source FR update is
\[
x_{t+1}
=
x_t-\eta_x\nabla_xf_b(x_t,y_t),
\]
\[
y_{t+1}
=
y_t+\eta_y\nabla_yf_b(x_t,y_t)
+
\eta_x
(\partial_{yy}^2f_b)^{-1}
(\partial_{yx}^2f_b)
\nabla_xf_b(x_t,y_t).
\]
Since
\[
(\partial_{yy}^2f_b)^{-1}(\partial_{yx}^2f_b)
=
-\frac bc,
\]
the follower correction is
\[
-\eta_x\frac bc\nabla_xf_b.
\]

Set
\[
e_t=y_t-\frac bc x_t.
\]
Then
\[
\nabla_xf_b
=
\left(a+\frac{b^2}{c}\right)x_t+be_t
=
hx_t+be_t,
\]
so
\[
x_{t+1}
=
(1-\eta_xh)x_t-\eta_xbe_t
=
p x_t-\eta_xbe_t.
\]

Also,
\[
\nabla_yf_b=-c e_t.
\]
Subtracting
\[
\frac bc x_{t+1}
\]
from the follower update cancels the FR correction exactly and gives
\[
e_{t+1}=(1-\eta_yc)e_t=q e_t.
\]

Substitution gives
\[
x_t
=
p^tx_0
-
\eta_xb
\sum_{j=0}^{t-1}
p^{t-1-j}q^j e_0.
\]
For
\[
p\ne q,
\]
the sum is
\[
\frac{p^t-q^t}{p-q}.
\]
For
\[
p=q=r,
\]
it is
\[
t r^{t-1}.
\]

The triangular coordinate system has diagonal entries
\[
p,q,
\]
so convergence to zero from every initial state holds exactly when both moduli are below one. The stated resonant amplification formula follows by inserting
\[
x_0=0,\qquad y_0=e_0=1
\]
and converting back from the ridge error.

## Verification

The accompanying `verify.py` reconstructs the original FR update from the source formula, compares it with the triangular ridge-error recurrence, checks the closed forms for distinct and repeated modal factors, and verifies the fixed-spectrum unbounded-transient family.

It also checks the parameters of the defining paper's displayed quadratic and confirms that equal player steps place it exactly on the repeated-eigenvalue resonance.

The computations are transcription guards. The identities and unboundedness statement are proved algebraically above.

## Relationship to prior work

Wang, Zhang, and Ba introduce FR and prove exact local convergence to local minimax points for suitable learning rates. Their key Jacobian calculation shows that the FR map is similar to an upper block-triangular matrix whose diagonal blocks are the follower and leader Schur-complement modes. They explicitly note that all FR eigenvalues are real and use this to explain removal of the strong rotational behavior seen in gradient descent-ascent.

The same upper-triangular formula retains an off-diagonal coupling block. The inspected defining full text does not analyze the nonnormal transient generated by that block, does not state the repeated-eigenvalue Jordan formula above, and does not note that its displayed quadratic example is resonant under equal learning rates.

Gao, Liu, Ng, and Zhou later propose HessianFR and motivate it by improved convergence and Hessian conditioning. Their full text restates the FR ridge correction and develops faster local minimax algorithms, but the inspected material does not state a fixed-real-spectrum family with unbounded FR Euclidean transient amplification.

Published-record searches for Follow-the-Ridge resonance, Jordan behavior, nonnormal transients, repeated eigenvalues, and exact quadratic ridge-error dynamics did not identify an implication-equivalent result. Generic stable Jordan-block transient results are mathematically relevant background, but they do not by themselves identify this phenomenon inside the source FR parameterization or its canonical example.

## Limitations

The family is scalar in each player and exactly quadratic.

The amplification is measured in the ordinary Euclidean norm of the player state; a coupling-dependent similarity norm can behave differently.

The construction varies the raw Hessian entries while keeping the follower curvature, leader Schur-complement curvature, learning rates, and FR eigenvalues fixed.

The result does not claim that large transients are typical in applications; it proves that real FR eigenvalues alone cannot rule them out.

## References

1. Yuanhao Wang, Guodong Zhang, and Jimmy Ba, “On Solving Minimax Optimization Locally: A Follow-the-Ridge Approach,” arXiv:1910.07512v1, first submitted 2019-10-16; ICLR 2020.
2. Yihang Gao, Huafeng Liu, Michael K. Ng, and Mingjie Zhou, “HessianFR: An Efficient Hessian-based Follow-the-Ridge Algorithm for Minimax Optimization,” arXiv:2205.11030v1, first submitted 2022-05-23.
