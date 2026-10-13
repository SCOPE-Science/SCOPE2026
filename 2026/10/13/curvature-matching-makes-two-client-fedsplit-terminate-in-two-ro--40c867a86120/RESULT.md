# Curvature matching makes two-client FedSplit terminate in two rounds
## Finding

FedSplit is an operator-splitting method for distributed convex minimization. On two scalar quadratic clients its full communication-round dynamics reduce to a \(2\times2\) cross-reflection map, and that map can become nilpotent.

Let
\[
f_j(x)=\frac{a_j}{2}(x-b_j)^2,
\qquad
a_j>0,
\qquad
j\in\{1,2\}.
\]
Run exact FedSplit with proximal parameter
\[
s>0,
\]
equal client weights, and the source initialization
\[
z_1^0=z_2^0=x^0.
\]
Define
\[
r_j=\frac{1-sa_j}{1+sa_j}.
\]

For two clients the server model is
\[
x=\frac{z_1+z_2}{2},
\]
so the reflected argument presented to client \(1\) is
\[
2x-z_1=z_2,
\]
and symmetrically
\[
2x-z_2=z_1.
\]
The exact proximal map of client \(j\) is
\[
\operatorname{prox}_{s f_j}(w)
=
\frac{w+sa_jb_j}{1+sa_j}.
\]
Therefore the exact FedSplit client-state update is
\[
\boxed{
z_1^+=r_1z_2+(1-r_1)b_1,
\qquad
z_2^+=r_2z_1+(1-r_2)b_2.
}
\]

Let
\[
(z_1^\star,z_2^\star)
\]
be the unique fixed point of this affine map. Its server average is the minimizer of the original two-client objective,
\[
\boxed{
x^\star
=
\frac{z_1^\star+z_2^\star}{2}
=
\frac{a_1b_1+a_2b_2}{a_1+a_2}.
}
\]
Writing
\[
e=
\begin{bmatrix}
z_1-z_1^\star\\
z_2-z_2^\star
\end{bmatrix},
\]
one round gives
\[
e^+
=
A_s e,
\qquad
A_s=
\begin{bmatrix}
0&r_1\\
r_2&0
\end{bmatrix}.
\]
Hence
\[
\boxed{
A_s^2=r_1r_2I
}
\]
and the exact per-round spectral radius is
\[
\boxed{
\rho(s)
=
\sqrt{|r_1r_2|}
=
\sqrt{
\left|
\frac{(1-sa_1)(1-sa_2)}
{(1+sa_1)(1+sa_2)}
\right|
}.
}
\]

Because
\[
|r_j|<1
\]
for every
\[
s>0,
\]
FedSplit is linearly convergent on this family for every positive proximal parameter.

More strongly,
\[
\rho(s)=0
\]
if and only if
\[
\boxed{
s=\frac1{a_1}
\quad\text{or}\quad
s=\frac1{a_2}.
}
\]
At either matched value,
\[
A_s^2=0.
\]
Thus the full client state reaches the exact fixed point after at most two communication rounds from every common initialization, and the server model is exactly
\[
x^\star.
\]

For example, take
\[
a_1=1,
\qquad
a_2=9,
\qquad
b_1=-2,
\qquad
b_2=1,
\qquad
s=1.
\]
Then
\[
r_1=0,
\qquad
r_2=-\frac45.
\]
After one round,
\[
z_1^1=-2
\]
regardless of the starting value. After the second round both client states are at the unique FedSplit fixed point, and their average is
\[
x^\star
=
\frac{-2+9}{10}
=
\frac7{10}.
\]

This finite-communication optimum is not obtained by the symmetric geometric-mean parameter unless the curvatures agree. If
\[
a_1\ne a_2
\]
and
\[
s=\frac1{\sqrt{a_1a_2}},
\]
then
\[
r_1=-r_2
\]
up to the ordering of the two curvatures, and
\[
\boxed{
\rho(s)
=
\frac{|\sqrt{a_2}-\sqrt{a_1}|}
{\sqrt{a_2}+\sqrt{a_1}}
>0.
}
\]

Thus two-client FedSplit has a heterogeneity-assisted nilpotent regime: matching the proximal parameter to either one client's curvature annihilates one reflected mode, and the cross-coupled structure annihilates the remaining error one round later.

## Assumptions and scope

The result concerns exact FedSplit, not an inexact local proximal solver.

There are exactly two equally weighted clients and one scalar decision variable. Both objectives are strongly convex quadratics.

The proximal parameter
\[
s
\]
is constant across the two clients, as in the source algorithm.

The finite-termination statement is for the client-state fixed point and hence for the server model. It does not assert finite termination for more than two clients, nonquadratic losses, vector quadratics with noncommuting Hessians, or inexact proximal computations.

The rate comparison with the geometric-mean choice is an instancewise statement. It does not claim that curvature matching is a robust parameter rule when client curvatures are unknown or when many spectral modes must be balanced simultaneously.

## Proof

FedSplit performs, for each client,
\[
z_j^{+1/2}
=
\operatorname{prox}_{s f_j}(2x-z_j),
\]
followed by the centering update
\[
z_j^+
=
z_j+2(z_j^{+1/2}-x),
\]
and then averages the client states.

With two clients,
\[
2x-z_1=z_2,
\qquad
2x-z_2=z_1.
\]
For
\[
f_j(x)=\frac{a_j}{2}(x-b_j)^2,
\]
the exact proximal point satisfies
\[
0=a_j(u-b_j)+\frac1s(u-w),
\]
hence
\[
u=\frac{w+sa_jb_j}{1+sa_j}.
\]

For client \(1\),
\[
z_1^+
=
z_1
+
2\left(
\frac{z_2+sa_1b_1}{1+sa_1}
-
\frac{z_1+z_2}{2}
\right).
\]
The \(z_1\) terms cancel, leaving
\[
z_1^+
=
\frac{1-sa_1}{1+sa_1}z_2
+
\frac{2sa_1}{1+sa_1}b_1
=
r_1z_2+(1-r_1)b_1.
\]
The second-client formula is identical with the indices exchanged.

Since
\[
|r_1r_2|<1,
\]
the affine map has a unique fixed point. Subtracting it gives
\[
e^+
=
\begin{bmatrix}
0&r_1\\
r_2&0
\end{bmatrix}e.
\]
Squaring yields
\[
A_s^2=r_1r_2I.
\]
Thus the two eigenvalues satisfy
\[
\lambda^2=r_1r_2
\]
and have common modulus
\[
\sqrt{|r_1r_2|}.
\]

The global minimizer follows by differentiating
\[
f_1(x)+f_2(x):
\]
\[
a_1(x-b_1)+a_2(x-b_2)=0.
\]
The FedSplit source proves that the server average of a fixed point is an optimum; direct substitution into the two affine fixed-point equations gives the same expression.

The spectral radius is nonnegative. It vanishes exactly when
\[
r_1r_2=0,
\]
which, because
\[
a_j>0
\quad\text{and}\quad
s>0,
\]
is equivalent to
\[
s=\frac1{a_1}
\quad\text{or}\quad
s=\frac1{a_2}.
\]
At either value,
\[
A_s^2=0,
\]
so every initial error is annihilated in at most two rounds.

For
\[
s=\frac1{\sqrt{a_1a_2}},
\]
put
\[
u=\sqrt{a_1},
\qquad
v=\sqrt{a_2}.
\]
Then
\[
r_1=\frac{v-u}{v+u},
\qquad
r_2=-\frac{v-u}{v+u},
\]
up to swapping the client indices, which gives the displayed nonzero factor when
\[
a_1\ne a_2.
\]

## Verification

The accompanying `verify.py` reconstructs the exact FedSplit client update from the proximal subproblem and the centering step.

It verifies the closed cross-reflection formula for random positive curvatures, centers, proximal parameters, and common initializations. It checks the matrix identity
\[
A_s^2=r_1r_2I,
\]
the spectral-radius expression, the exact fixed-point average, and two-round termination under either curvature-matched parameter.

It also checks the exact rational example
\[
(a_1,a_2,b_1,b_2,s)
=
(1,9,-2,1,1)
\]
and verifies that the second-round average is exactly
\[
7/10.
\]

The computations are transcription guards only. Finite termination follows from the exact nilpotency identity.

## Relationship to prior work

Pathak and Wainwright introduced FedSplit as an operator-splitting framework for federated convex minimization, proved that its fixed points correspond to optima, characterized convergence rates, and analyzed inexact proximal computation.

The inspected defining source gives the exact proximal-reflection update used here, but it does not state the two-client scalar cross-reflection reduction, the exact rate
\[
\rho(s)=\sqrt{|r_1r_2|},
\]
or the nilpotent curvature-matching rule
\[
s\in\{1/a_1,1/a_2\}.
\]

General Douglas--Rachford and Peaceman--Rachford literature contains tight contraction analyses and finite-convergence results for other problem classes. The closest inspected finite-convergence result concerns feasibility geometry, not a two-client strongly convex quadratic whose reflected proximal map is nilpotent. General contraction-rate results do not imply that matching one local curvature annihilates the complete two-client FedSplit error in two communications.

Focused indexed searches for FedSplit finite termination, scalar quadratic exact rates, nilpotent reflected proximal maps, and curvature matching did not identify an implication-equivalent published result.

## Limitations

The effect is specific to exactly two clients. With more clients, the reflected argument is no longer simply the other client's state.

The scalar quadratic proximal map has a single curvature, so a single parameter can make one reflection coefficient exactly zero. Multidimensional clients generally contain several curvature modes and cannot all be annihilated by one scalar parameter.

Exact proximal computation is essential for literal finite termination. Inexact local solves replace the nilpotent map by a perturbed one.

The result is an instancewise structural benchmark, not a recommendation to estimate one client's curvature and use its reciprocal in heterogeneous production systems.

## References

1. Reese Pathak and Martin J. Wainwright, “FedSplit: An algorithmic framework for fast federated optimization,” arXiv:2005.05238v1, first submitted 2020-05-11; NeurIPS 2020.
2. Pontus Giselsson and Stephen Boyd, “Linear Convergence and Metric Selection for Douglas-Rachford Splitting and ADMM,” IEEE Transactions on Automatic Control 62 (2017), 532–544.
3. Ernest K. Ryu, Adrien B. Taylor, Carolina Bergeling, and Pontus Giselsson, “Operator Splitting Performance Estimation: Tight Contraction Factors and Optimal Parameter Selection,” SIAM Journal on Optimization 30 (2020), 2251–2271.
