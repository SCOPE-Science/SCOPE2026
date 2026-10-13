# FedNova has a sharp local-step-imbalance instability on exact local solves
## Finding

FedNova normalizes each client's cumulative update by its amount of local work and then rescales the aggregate by an effective local-step count. This removes the leading aggregation-weight mismatch targeted by the method. At a fixed client learning rate, however, the normalization and the server rescaling can themselves create an exact instability when local progress is sufficiently imbalanced.

Consider two equally weighted clients with scalar objectives
\[
F_i(x)=\frac{a}{2}(x-b_i)^2,
\qquad
a>0,
\qquad
i\in\{1,2\}.
\]
Client \(i\) performs
\[
\tau_i\in\mathbb N
\]
local gradient steps. Use vanilla local gradient descent with the constant client step
\[
\eta=\frac1a.
\]
Thus each client reaches its local minimizer after the first local step:
\[
x_{i,1}=b_i,
\]
and every later local gradient is zero.

For vanilla SGD, the source FedNova normalization is the average local gradient, and its default effective server scale is
\[
\tau_{\mathrm{eff}}
=
\frac{\tau_1+\tau_2}{2}.
\]
Therefore the two normalized client directions are
\[
d_i
=
\frac{x-b_i}{\eta\tau_i},
\]
and one communication round is
\[
x^+
=
x
-
\frac{\tau_1+\tau_2}{4}
\left(
\frac{x-b_1}{\tau_1}
+
\frac{x-b_2}{\tau_2}
\right).
\]

After collecting the coefficient of \(x\),
\[
\boxed{
x^+-x_{\mathrm{FN}}
=
-
\frac{(\tau_1-\tau_2)^2}{4\tau_1\tau_2}
\left(
x-x_{\mathrm{FN}}
\right),
}
\]
where
\[
\boxed{
x_{\mathrm{FN}}
=
\frac{\tau_2 b_1+\tau_1 b_2}{\tau_1+\tau_2}.
}
\]

The true minimizer of the equally weighted global objective is
\[
x^\star=\frac{b_1+b_2}{2}.
\]
Hence
\[
\boxed{
x_{\mathrm{FN}}-x^\star
=
\frac{(\tau_2-\tau_1)(b_1-b_2)}
{2(\tau_1+\tau_2)}.
}
\]

The round is linearly convergent from every initialization exactly when
\[
\frac{(\tau_1-\tau_2)^2}{4\tau_1\tau_2}<1.
\]
Equivalently,
\[
\boxed{
3-2\sqrt2
<
\frac{\tau_2}{\tau_1}
<
3+2\sqrt2.
}
\]
Thus the sharp continuous local-step-ratio frontier is
\[
3+2\sqrt2\approx5.828427
\]
up to reciprocal symmetry.

Because actual local-step counts are positive integers, exact equality at the irrational boundary cannot occur. The first imbalance of the form
\[
(\tau_1,\tau_2)=(1,m)
\]
that is unstable is
\[
m=6.
\]
Indeed,
\[
\boxed{
M_{1,6}=-\frac{25}{24}.
}
\]
So the global round diverges alternately from its affine fixed point even though both local solvers reached their own exact minimizers after one gradient step.

For the concrete shifted pair
\[
b_1=-1,
\qquad
b_2=1,
\]
the true global minimizer is
\[
x^\star=0,
\]
while
\[
x_{\mathrm{FN}}=-\frac57.
\]
Hence this same example exhibits both a fixed-point displacement and a strict round instability.

Inside the stable ratio interval, the fixed point equals the true global minimizer exactly when
\[
\tau_1=\tau_2
\]
or
\[
b_1=b_2.
\]
Thus fixed normalization removes the raw update-count weighting targeted by FedNova, but at a nonvanishing client step it does not make the exact local trajectory average equal to the gradient at the broadcast point.

## Assumptions and scope

The result uses deterministic full participation, two clients, equal client weights, vanilla local gradient descent, and the source default
\[
\tau_{\mathrm{eff}}
=
\sum_i p_i\tau_i.
\]

Both local objectives have the same positive scalar curvature. The step
\[
\eta=\frac1a
\]
is not an unstable local choice: it sends each client exactly to its own minimizer in one step.

The claim concerns a constant client step. The source convergence theorem instead chooses a learning rate that decreases with the communication horizon. Therefore the result is a finite-step dynamical boundary, not a contradiction of the published asymptotic theorem.

No claim is made for server momentum, partial participation, stochastic gradients, unequal client weights, vector-valued noncommuting Hessians, or alternative choices of
\[
\tau_{\mathrm{eff}}.
\]

## Proof

For client \(i\),
\[
\nabla F_i(x)=a(x-b_i).
\]
With
\[
\eta=\frac1a,
\]
the first local gradient step gives
\[
x-\eta\nabla F_i(x)
=
x-(x-b_i)
=
b_i.
\]
All subsequent local gradients vanish.

Vanilla FedNova forms the normalized local gradient by averaging the local gradients across the
\[
\tau_i
\]
steps. Therefore
\[
d_i
=
\frac{a(x-b_i)}{\tau_i}
=
\frac{x-b_i}{\eta\tau_i}.
\]

For equal client weights, the source default effective local-step count is
\[
\tau_{\mathrm{eff}}
=
\frac{\tau_1+\tau_2}{2}.
\]
The server update is consequently
\[
x^+
=
x-\tau_{\mathrm{eff}}\eta
\left(
\frac{d_1+d_2}{2}
\right),
\]
which simplifies to
\[
x^+
=
x
-
\frac{\tau_1+\tau_2}{4}
\left(
\frac{x-b_1}{\tau_1}
+
\frac{x-b_2}{\tau_2}
\right).
\]

The coefficient of \(x\) is
\[
M
=
1-
\frac{\tau_1+\tau_2}{4}
\left(
\frac1{\tau_1}+\frac1{\tau_2}
\right)
=
1-
\frac{(\tau_1+\tau_2)^2}{4\tau_1\tau_2}
=
-\frac{(\tau_1-\tau_2)^2}{4\tau_1\tau_2}.
\]

Solving
\[
x^+=x
\]
gives
\[
\frac{x-b_1}{\tau_1}
+
\frac{x-b_2}{\tau_2}
=
0,
\]
hence
\[
x_{\mathrm{FN}}
=
\frac{\tau_2 b_1+\tau_1 b_2}{\tau_1+\tau_2}.
\]

A scalar affine iteration converges from every initialization exactly when
\[
|M|<1.
\]
Putting
\[
q=\frac{\tau_2}{\tau_1}>0,
\]
this condition is
\[
(q-1)^2<4q,
\]
or
\[
q^2-6q+1<0.
\]
Its roots are
\[
3-2\sqrt2
\quad\text{and}\quad
3+2\sqrt2,
\]
which proves the sharp frontier.

Finally,
\[
x_{\mathrm{FN}}-\frac{b_1+b_2}{2}
=
\frac{(\tau_2-\tau_1)(b_1-b_2)}
{2(\tau_1+\tau_2)}.
\]
For
\[
(\tau_1,\tau_2)=(1,6),
\]
the multiplier is
\[
-\frac{(1-6)^2}{4\cdot1\cdot6}
=
-\frac{25}{24},
\]
so every initialization except the affine fixed point diverges in alternating sign relative to that fixed point.

## Verification

The accompanying `verify.py` reconstructs the client trajectories and the source FedNova normalization directly.

It verifies the closed round map for many integer local-step pairs, checks the sharp ratio test against the exact multiplier, and checks the exact
\[
(1,6)
\]
witness using rational arithmetic. It also verifies the fixed-point displacement for shifted local minima.

The computations are transcription guards. The stability frontier and fixed-point formula are proved algebraically above.

## Relationship to prior work

Wang and coauthors introduced FedNova to address objective inconsistency caused by heterogeneous amounts of local computation. Their method averages normalized local gradients and, for vanilla SGD, rescales the cumulative client changes by the ratio of the average local-step count to each client's own local-step count. Their convergence theorem chooses a client learning rate that decreases with the communication horizon.

The defining paper also analyzes quadratic objectives to motivate objective inconsistency, but that analysis concerns the mismatch induced by conventional aggregation. The inspected FedNova section and pseudocode do not state the constant-step affine frontier above or an instability produced by a
\[
6:1
\]
local-step imbalance when every client locally solves its own scalar quadratic exactly after one step.

Horváth and coauthors later compare FedNova with FedShuffle. They explicitly observe that FedNova can diminish the weight of a client that makes more local progress and that FedShuffle admits larger theoretical local steps. This is the closest inspected prior statement. It identifies the qualitative mechanism but does not give the exact two-client fixed point, the sharp
\[
3+2\sqrt2
\]
ratio frontier, or the exact locally solved
\[
(1,6)
\]
divergence witness.

Focused published-record searches for FedNova fixed points, scalar-quadratic divergence, local-step-ratio stability, inverse-step weighting, and the constant
\[
3+2\sqrt2
\]
did not identify an implication-equivalent exact result.

## Limitations

The result deliberately fixes the client step at
\[
\eta=\frac1a.
\]
This makes the mechanism transparent and locally benign, but it is not a full phase diagram over arbitrary learning rates.

The instability arises with the source default effective server scale. A different server scale can change the multiplier.

The theorem is deterministic and one-dimensional. It does not quantify stochastic stationary error or higher-dimensional noncommuting curvature effects.

The result does not invalidate the source convergence theorem, whose prescribed client learning rate vanishes with the horizon.

## References

1. Jianyu Wang, Qinghua Liu, Hao Liang, Gauri Joshi, and H. Vincent Poor, “Tackling the Objective Inconsistency Problem in Heterogeneous Federated Optimization,” arXiv:2007.07481v1, first submitted 2020-07-15; NeurIPS 2020.
2. Samuel Horváth, Maziar Sanjabi, Lin Xiao, Peter Richtárik, and Michael Rabbat, “FedShuffle: Recipes for Better Use of Local Work in Federated Learning,” arXiv:2204.13169v1, first submitted 2022-04-27; Transactions on Machine Learning Research, 2022.
