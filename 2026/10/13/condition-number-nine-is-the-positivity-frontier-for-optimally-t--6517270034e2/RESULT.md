# Condition number nine is the positivity frontier for optimally tuned heavy-ball on diagonal quadratics

## Finding
Consider the positive diagonal quadratic
\[
f(x)=\frac12x^{\mathsf T}Ax-b^{\mathsf T}x,
\qquad
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\qquad
b\ge0,
\]
and initialize heavy-ball with \(x_{-1}=x_0=0\):
\[
x_{k+1}=x_k-\alpha(Ax_k-b)+\beta(x_k-x_{k-1}).
\]
Let
\[
\mu=\min_i\lambda_i,\qquad L=\max_i\lambda_i,\qquad \kappa=\frac L\mu,
\]
and use Polyak's classical optimal parameters for a strongly convex quadratic,
\[
\alpha=\frac{4}{(\sqrt L+\sqrt\mu)^2},
\qquad
\beta=\left(\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu}\right)^2.
\]

Then the nonnegative orthant contains every heavy-ball iterate for every positive diagonal \(A\) with condition number at most \(9\), and the constant \(9\) is sharp:
\[
\boxed{\text{all iterates are componentwise nonnegative for every such problem}\iff \kappa\le9.}
\]
At \(\kappa=9\), a largest-curvature coordinate may equal zero at the second iterate. For every \(\kappa>9\), a positive \(L\)-mode becomes negative already at the second iterate.

## Assumptions and scope
The Hessian is diagonal in the coordinate system in which componentwise nonnegativity is being tested. The right-hand side satisfies \(b\ge0\), so the exact minimizer
\[
x^\star=A^{-1}b
\]
is componentwise nonnegative. The initialization is \(x_{-1}=x_0=0\), and the parameters are fixed at the classical optimal quadratic heavy-ball values displayed above.

The statement is a whole-trajectory cone-invariance classification for this separable class. It does not claim the same threshold for nondiagonal positive-definite matrices, projected momentum, adaptive momentum, or other initializations.

## Proof
Put
\[
q=\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu}\in[0,1).
\]
Then \(\beta=q^2\). For \(q>0\) and one scalar mode of curvature \(\lambda\in[\mu,L]\), define
\[
t=\frac{1+q^2-\alpha\lambda}{2q}.
\]
Because \(\lambda=\mu\) gives \(t=1\) and \(\lambda=L\) gives \(t=-1\), one has
\[
t\in[-1,1].
\]

If the corresponding component \(b_i\) is zero, that coordinate remains identically zero. Assume therefore \(b_i>0\), and let \(x^\star=b_i/\lambda>0\). Normalize the scalar error by
\[
e_k=\frac{x_k-x^\star}{x^\star}.
\]
The heavy-ball recurrence gives
\[
e_{k+1}=2qt\,e_k-q^2e_{k-1},
\qquad
e_0=-1,
\qquad
e_1=q^2-2qt.
\]

Let \(U_k\) denote the Chebyshev polynomial of the second kind, with
\[
U_{-1}(t)=0,\qquad U_0(t)=1,\qquad
U_{k+1}(t)=2tU_k(t)-U_{k-1}(t).
\]
Matching the initial values and recurrence yields
\[
e_k=-q^k\left(U_k(t)-qU_{k-1}(t)\right).
\]

For \(t=\cos\theta\),
\[
U_k(t)=\frac{\sin((k+1)\theta)}{\sin\theta},
\]
with the endpoint values supplied by continuity. The elementary inequality
\[
|\sin(m\theta)|\le m|\sin\theta|
\]
therefore gives
\[
|U_k(t)|\le k+1
\qquad (-1\le t\le1).
\]
Hence, for every \(k\ge2\),
\[
|e_k|
\le q^k\bigl(k+1+qk\bigr).
\]

If \(\kappa\le9\), then \(q\le1/2\). Therefore
\[
|e_k|
\le
\frac{k+1+k/2}{2^k}
=
\frac{3k+2}{2^{k+1}}.
\]
The inequality
\[
3k+2\le2^{k+1}
\]
holds for every \(k\ge2\): it is equality at \(k=2\), and induction follows because
\[
3(k+1)+2\le2(3k+2)
\]
for \(k\ge1\). Thus \(|e_k|\le1\) for every \(k\ge2\), so
\[
x_k=x^\star(1+e_k)\ge0.
\]
Also
\[
x_1=\alpha b_i\ge0.
\]
This proves positivity of every coordinate for all \(k\).

For sharpness, use the mode \(\lambda=L\), hence \(t=-1\). Since
\[
U_2(-1)=3,\qquad U_1(-1)=-2,
\]
one obtains
\[
\frac{x_2}{x^\star}
=
1-q^2(3+2q)
=
(1-2q)(1+q)^2.
\]
Therefore the second iterate in the \(L\)-coordinate is negative exactly when \(q>1/2\). Finally,
\[
q>\frac12
\iff
\frac{\sqrt\kappa-1}{\sqrt\kappa+1}>\frac12
\iff
\sqrt\kappa>3
\iff
\kappa>9.
\]
At \(\kappa=9\), this coordinate is exactly zero.

The case \(q=0\), equivalently \(\kappa=1\), is immediate: \(\alpha=1/\mu\), \(\beta=0\), so the method reaches the minimizer in one step.

## Verification
The embedded `verify.py` performs exact rational checks of the recurrence formula, the threshold example, and the displayed rational witness.

At the boundary
\[
A=\operatorname{diag}(1,9),
\qquad
b=(1,1)^{\mathsf T},
\]
one has
\[
q=\frac12,\qquad
\alpha=\frac14,\qquad
\beta=\frac14,
\]
and the second coordinate of \(x_2\) is exactly zero.

Above the boundary, take
\[
A=\operatorname{diag}(1,16),
\qquad
b=(1,1)^{\mathsf T}.
\]
Then
\[
q=\frac35,\qquad
\alpha=\frac4{25},\qquad
\beta=\frac9{25},
\]
and the second coordinate is
\[
(x_2)_2=-\frac4{125}<0,
\]
while the exact minimizer has second coordinate \(1/16>0\). The normalized second-coordinate value is
\[
\frac{(x_2)_2}{(x^\star)_2}=-\frac{64}{125},
\]
agreeing with \((1+q)^2(1-2q)\).

These computations verify the witnesses only. The all-dimensional and all-iteration result is the analytic Chebyshev argument above.

## Relationship to prior work
Ghadimi, Feyzmahdavian, and Johansson write the heavy-ball recurrence explicitly and summarize Polyak's optimal quadratic convergence factor
\[
q=\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu}.
\]
Their full text studies global convergence and rates for smooth convex and strongly convex functions; it does not state a componentwise cone-invariance threshold for positive diagonal quadratics.

Lessard, Recht, and Packard analyze heavy-ball through integral quadratic constraints, including a nonquadratic strongly convex counterexample to global convergence with the classical quadratic tuning. Their analysis concerns stability and convergence-rate certification, not whether a positive diagonal quadratic trajectory remains in the nonnegative orthant.

Later literature explicitly emphasizes heavy-ball's oscillatory or peak behavior. Danilova and Malinovskiy motivate averaging by the peak effect of optimally tuned heavy-ball, while Orvieto studies quadratic heavy-ball through Lyapunov and oscillator structure. Those works make transient oscillation a natural object, but the inspected material does not give the sharp componentwise threshold \(\kappa=9\) for the diagonal positive cone.

The closest semantic-database records found in the comparison search concerned a real-root barrier for interval-robust heavy-ball acceleration and objective-monotonicity frontiers for other Polyak-type steps. Neither statement implies componentwise nonnegativity of every iterate, and neither has the \(\kappa=9\) cone boundary.

## Limitations
The diagonal hypothesis is essential to the proof because positivity is coordinatewise while the spectral decoupling uses the same coordinates. A nondiagonal symmetric positive-definite matrix can mix eigenmodes and coordinates, so this theorem does not classify Stieltjes matrices or arbitrary positive-definite Hessians.

The result uses the exact classical optimal quadratic parameters and the zero-velocity initialization \(x_{-1}=x_0=0\). Other momentum parameters or initial velocities can have different positivity regions.

The theorem concerns exact arithmetic and unconstrained heavy-ball. If nonnegativity is a hard feasibility requirement, projection or another safeguard may still be preferable even below the threshold.

Residual originality risk remains that older momentum or linear-recurrence literature may contain the same coordinatewise cone criterion under different terminology. No implication-equivalent statement was found in the primary texts and targeted searches inspected here.

## References
1. E. Ghadimi, H. R. Feyzmahdavian, and M. Johansson, “Global convergence of the Heavy-ball method for convex optimization.” First public version 2014-12-23, arXiv:1412.7457; Mathematics Subject Classification (2000) begins with 90C26.
2. L. Lessard, B. Recht, and A. Packard, “Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints.” First public version 2014-08-15, arXiv:1408.3595; later SIAM Journal on Optimization 26 (2016), 57–95.
3. M. Danilova and G. Malinovskiy, “Averaged Heavy-Ball Method.” First public version 2021-11-09, arXiv:2111.05430; later Computer Research and Modeling 14 (2022), 277–308.
4. A. Orvieto, “An accelerated Lyapunov function for Polyak's Heavy-ball on convex quadratics.” Optimization Letters 19 (2025), 307–328, first published online 2024-06-25.
