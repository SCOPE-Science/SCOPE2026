# Mime's first quadratic averaging defect appears at the third local step
## Finding

Mime was designed to make local federated updates mimic a centralized optimizer by combining a global gradient with an SVRG-style client correction. On quadratic clients, the first few local steps admit an exact closed form that pinpoints when curvature heterogeneity can first affect the averaged model.

Consider a fixed set of
\[
m\ge 1
\]
equally weighted clients with deterministic quadratic objectives
\[
f_i(y)
=
\frac12 y^\top H_i y-q_i^\top y+\mathrm{const},
\]
where each
\[
H_i=H_i^\top.
\]
At the broadcast point
\[
x,
\]
define
\[
c
=
\frac1m\sum_{i=1}^m\nabla f_i(x),
\qquad
\bar H
=
\frac1m\sum_{i=1}^m H_i.
\]

For Mime with SGD as the base optimizer, full participation, and exact local gradients, the source control variate gives the local direction
\[
g_i(y)
=
\nabla f_i(y)-\nabla f_i(x)+c
=
H_i(y-x)+c.
\]

Let every client start from
\[
y_{i,0}=x
\]
and take local steps
\[
y_{i,k+1}
=
y_{i,k}-\eta g_i(y_{i,k}),
\qquad
\eta>0.
\]
Let
\[
\bar y_k=\frac1m\sum_{i=1}^m y_{i,k}.
\]

Also let
\[
z_0=x
\]
and let
\[
z_{k+1}
=
z_k-\eta\nabla f(z_k)
\]
be centralized gradient descent on the averaged quadratic
\[
f=\frac1m\sum_i f_i.
\]

Then the first two averaged local iterates coincide exactly with the centralized trajectory:
\[
\boxed{\bar y_1=z_1}
\]
and
\[
\boxed{\bar y_2=z_2}.
\]

At the third local step, the first possible averaging defect is
\[
\boxed{
\bar y_3-z_3
=
-\eta^3V_Hc,
}
\]
where
\[
\boxed{
V_H
=
\frac1m\sum_{i=1}^m(H_i-\bar H)^2
=
\frac1m\sum_{i=1}^mH_i^2-\bar H^2.
}
\]

Because each
\[
H_i-\bar H
\]
is symmetric,
\[
c^\top V_Hc
=
\frac1m\sum_{i=1}^m
\|(H_i-\bar H)c\|^2.
\]
Hence
\[
\boxed{
c^\top(\bar y_3-z_3)
=
-\frac{\eta^3}{m}
\sum_{i=1}^m
\|(H_i-\bar H)c\|^2
\le0.
}
\]

Equality holds exactly when
\[
(H_i-\bar H)c=0
\]
for every client.

For two equally weighted clients,
\[
\boxed{
V_H
=
\frac14(H_1-H_2)^2.
}
\]

Thus Mime cancels deterministic quadratic client-curvature drift completely through two local steps. The first nonzero averaged discrepancy can appear only at the third local step, where it has an exact cubic coefficient given by the squared Hessian heterogeneity acting on the broadcast-gradient direction.

## Assumptions and scope

The result uses the defining Mime update with SGD as the base algorithm, exact local gradients, a fixed participating client set, equal client averaging, and no stochastic mini-batch noise.

The client functions are finite-dimensional quadratics with symmetric Hessians. Positive semidefiniteness is natural for convex quadratics but is not required for the algebraic identities.

The comparison is against centralized gradient descent on the average of the same participating client objectives, using the same step size
\[
\eta.
\]

The statement concerns the average client model after one, two, or three local steps within one communication round. It does not assert that the third-step correction always improves the final objective, because the vector
\[
V_Hc
\]
need not be collinear with
\[
c.
\]
The proved sign is only its inner product with the broadcast gradient.

## Proof

For a quadratic client,
\[
\nabla f_i(y)
=
H_i y-q_i.
\]
Therefore Mime's corrected local gradient is
\[
\nabla f_i(y)-\nabla f_i(x)+c
=
H_i(y-x)+c.
\]

At the first step,
\[
y_{i,1}
=
x-\eta c
\]
for every client. Hence
\[
\bar y_1
=
x-\eta c
=
z_1.
\]

At the second step,
\[
g_i(y_{i,1})
=
H_i(-\eta c)+c
=
c-\eta H_i c.
\]
Thus
\[
y_{i,2}
=
x-2\eta c+\eta^2H_i c.
\]
Averaging gives
\[
\bar y_2
=
x-2\eta c+\eta^2\bar Hc.
\]

Since the average objective has gradient
\[
\nabla f(y)=c+\bar H(y-x),
\]
the second centralized step is
\[
z_2
=
z_1-\eta\bigl(c-\eta\bar Hc\bigr)
=
x-2\eta c+\eta^2\bar Hc.
\]
Therefore
\[
\bar y_2=z_2.
\]

For the third local step,
\[
y_{i,2}-x
=
-2\eta c+\eta^2H_i c,
\]
so
\[
g_i(y_{i,2})
=
c-2\eta H_i c+\eta^2H_i^2c.
\]
Consequently
\[
y_{i,3}
=
x-3\eta c+3\eta^2H_i c-\eta^3H_i^2c.
\]
Averaging gives
\[
\bar y_3
=
x-3\eta c+3\eta^2\bar Hc
-\eta^3
\left(
\frac1m\sum_iH_i^2
\right)c.
\]

Three centralized gradient-descent steps give
\[
z_3
=
x-3\eta c+3\eta^2\bar Hc-\eta^3\bar H^2c.
\]
Subtracting yields
\[
\bar y_3-z_3
=
-\eta^3
\left(
\frac1m\sum_iH_i^2-\bar H^2
\right)c.
\]

Now
\[
\frac1m\sum_i(H_i-\bar H)^2
=
\frac1m\sum_iH_i^2-\bar H^2,
\]
because
\[
\frac1m\sum_iH_i\bar H
=
\bar H^2
\]
and
\[
\frac1m\sum_i\bar H H_i
=
\bar H^2.
\]
This proves the formula for
\[
V_H.
\]

Since each
\[
H_i-\bar H
\]
is symmetric,
\[
c^\top(H_i-\bar H)^2c
=
\|(H_i-\bar H)c\|^2.
\]
The sign identity follows immediately.

For two clients,
\[
\bar H=\frac{H_1+H_2}{2},
\]
and direct expansion gives
\[
V_H
=
\frac14(H_1-H_2)^2.
\]

## Verification

The accompanying `verify.py` reconstructs Mime's client update directly from the defining control-variate formula.

It checks random noncommuting symmetric positive-definite client Hessians and arbitrary linear terms, verifies exact equality with centralized gradient descent after one and two local steps, verifies the cubic third-step defect, and checks the gradient-alignment identity.

A scalar rational example is also checked exactly:
\[
H_1=1,
\qquad
H_2=3,
\qquad
\eta=\frac1{10},
\qquad
x=1,
\qquad
q_1=q_2=0.
\]
Here centralized three-step gradient descent gives
\[
z_3=\frac{64}{125},
\]
whereas Mime gives
\[
\bar y_3=\frac{51}{100},
\]
so the exact defect is
\[
-\frac1{500},
\]
matching
\[
-\eta^3V_Hc.
\]

The finite computations are transcription guards. The identities are proved symbolically above.

## Relationship to prior work

Karimireddy and coauthors introduce Mime as a framework for adapting centralized optimizers to cross-device federated learning. Their defining local update uses
\[
\nabla f_i(y)-\nabla f_i(x)+c
\]
and their generic reduction theorem states that Mime behaves like a centralized base optimizer plus a small perturbation. The paper emphasizes Hessian similarity as the structure that makes multiple local steps useful.

The inspected defining source does not state the exact quadratic identities
\[
\bar y_2=z_2
\]
or
\[
\bar y_3-z_3=-\eta^3V_Hc,
\]
nor the exact sign formula
\[
c^\top(\bar y_3-z_3)
=
-\frac{\eta^3}{m}
\sum_i\|(H_i-\bar H)c\|^2.
\]

The source theorem bounds the effective perturbation at order quadratic in the total local step scale. The formula here identifies an exact mechanism behind that bound on quadratics: after division by the total update scale, the first deterministic client-curvature discrepancy begins at second order, with an explicit Hessian-variance coefficient.

Focused searches for Mime quadratic dynamics, exact two-step cancellation, third-step Hessian-variance corrections, and equivalent federated control-variate identities did not identify an implication-equivalent published result. Closest indexed optimization findings concern different stochastic-gradient, spectral, and splitting recurrences.

## Limitations

The theorem is a one-round deterministic quadratic identity.

It uses full participation of the fixed client set being averaged and equal client weights.

It does not analyze mini-batch noise, client sampling, momentum or adaptive base optimizers, or more than three local steps.

The nonpositive inner product with the broadcast gradient does not imply that the third-step correction always decreases the final objective relative to centralized gradient descent.

## References

1. Sai Praneeth Karimireddy, Martin Jaggi, Satyen Kale, Mehryar Mohri, Sashank J. Reddi, Sebastian U. Stich, and Ananda Theertha Suresh, “Mime: Mimicking Centralized Stochastic Algorithms in Federated Learning,” arXiv:2008.03606v1, first submitted 2020-08-08; NeurIPS 2021.
