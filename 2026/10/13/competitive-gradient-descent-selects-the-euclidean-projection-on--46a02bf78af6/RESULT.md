# Competitive Gradient Descent selects the Euclidean projection onto the bilinear Nash set
## Finding

Competitive Gradient Descent (CGD) was introduced to stabilize two-player gradient dynamics by solving a regularized bilinear local game at every step. On a bilinear zero-sum game, the defining update is globally linear and can be solved exactly even when the game matrix is rectangular or rank deficient.

Let
\[
f(x,y)=x^\top C y,
\qquad
g(x,y)=-f(x,y),
\]
with
\[
C\in\mathbb R^{m\times n}.
\]
The unconstrained Nash set is
\[
\mathcal N
=
\ker(C^\top)\times\ker(C).
\]
Apply exact source-form CGD with an arbitrary fixed step
\[
\eta>0.
\]
Then the update simplifies to
\[
x^+
=
(I+\eta^2CC^\top)^{-1}(x-\eta Cy),
\]
\[
y^+
=
(I+\eta^2C^\top C)^{-1}(y+\eta C^\top x).
\]
Both inverses exist for every positive step.

Let the positive singular values of \(C\) be
\[
\sigma_1,\ldots,\sigma_r.
\]
On the two-dimensional singular plane corresponding to \(\sigma_j\), define
\[
q_j=\eta\sigma_j.
\]
The exact modal update is
\[
\begin{bmatrix}
a_j^+\\
b_j^+
\end{bmatrix}
=
\frac{1}{1+q_j^2}
\begin{bmatrix}
1&-q_j\\
q_j&1
\end{bmatrix}
\begin{bmatrix}
a_j\\
b_j
\end{bmatrix}.
\]
Therefore each active singular plane is a rotation through
\[
\theta_j=\arctan(q_j)
\]
followed by the exact Euclidean contraction
\[
\boxed{
r_j=\frac{1}{\sqrt{1+\eta^2\sigma_j^2}}.
}
\]
The squared norm on that plane is multiplied by
\[
\boxed{
\frac{1}{1+\eta^2\sigma_j^2}.
}
\]

In contrast, the components
\[
P_{\ker(C^\top)}x
\qquad\text{and}\qquad
P_{\ker(C)}y
\]
are fixed exactly by every CGD step. Hence CGD has a complete equilibrium-selection law:
\[
\boxed{
(x_k,y_k)
\longrightarrow
\bigl(P_{\ker(C^\top)}x_0,\,P_{\ker(C)}y_0\bigr)
}
\]
for every initialization and every
\[
\eta>0.
\]
The limit is precisely the Euclidean orthogonal projection of the initial strategy pair onto the Nash set.

More strongly, if \(a_j,b_j\) denote the initial coordinates in the active left/right singular directions, then
\[
\boxed{
\operatorname{dist}((x_k,y_k),\mathcal N)^2
=
\sum_{j=1}^r
\frac{a_j^2+b_j^2}
{(1+\eta^2\sigma_j^2)^k}.
}
\]
If \(r>0\) and \(\sigma_{\min}^+\) is the smallest positive singular value, the sharp worst-case distance factor per outer step is
\[
\boxed{
\rho
=
\frac{1}{\sqrt{1+\eta^2(\sigma_{\min}^+)^2}}.
}
\]

Thus the source observation that stronger player interactions improve CGD convergence has an exact global form on bilinear games: every positive singular mode contracts faster as its singular value grows. At the same time, step size does not change equilibrium selection. It changes the transient rotation and contraction of active modes, but the nullspace component—and therefore the selected Nash point—is an invariant of the dynamics.

## Assumptions and scope

The game is unconstrained, bilinear, and zero sum. The interaction matrix may be rectangular and rank deficient.

The update uses the exact inverse appearing in the defining CGD algorithm. Inexact inner linear solves can perturb both the exact modal factors and the invariant-nullspace statement.

The Euclidean projection statement uses the standard product Euclidean norm on the two players' strategy spaces.

If
\[
C=0,
\]
then every strategy pair is a Nash equilibrium and the CGD map is the identity, which is consistent with the projection statement. The displayed sharp rate uses
\[
r>0.
\]

## Proof

For the bilinear zero-sum game,
\[
\nabla_x f=Cy,
\qquad
\nabla_y g=-C^\top x,
\]
while the mixed Hessian blocks are
\[
D_{xy}^2f=C,
\qquad
D_{yx}^2g=-C^\top.
\]
Substituting into the defining CGD update gives
\[
x^+
=
x-\eta(I+\eta^2CC^\top)^{-1}(Cy+\eta CC^\top x).
\]
Using
\[
I-\eta^2(I+\eta^2CC^\top)^{-1}CC^\top
=
(I+\eta^2CC^\top)^{-1},
\]
we obtain
\[
x^+
=
(I+\eta^2CC^\top)^{-1}(x-\eta Cy).
\]
The formula for \(y^+\) is analogous.

Take a singular value decomposition. For a positive singular value \(\sigma_j\), let \(u_j,v_j\) be paired singular vectors satisfying
\[
Cv_j=\sigma_j u_j,
\qquad
C^\top u_j=\sigma_j v_j.
\]
Writing the active coordinates as
\[
a_j=u_j^\top x,
\qquad
b_j=v_j^\top y,
\]
gives
\[
a_j^+
=
\frac{a_j-\eta\sigma_j b_j}{1+\eta^2\sigma_j^2},
\]
\[
b_j^+
=
\frac{b_j+\eta\sigma_j a_j}{1+\eta^2\sigma_j^2}.
\]
Hence
\[
(a_j^+)^2+(b_j^+)^2
=
\frac{a_j^2+b_j^2}{1+\eta^2\sigma_j^2}.
\]
The normalized numerator matrix is a planar rotation, which yields the stated phase and contraction factor.

Now take
\[
x_\perp\in\ker(C^\top).
\]
Then
\[
CC^\top x_\perp=0.
\]
Also the coupling term \(Cy\) lies in \(\operatorname{range}(C)\), which is orthogonal to \(\ker(C^\top)\). Therefore
\[
P_{\ker(C^\top)}x^+
=
P_{\ker(C^\top)}x.
\]
The same argument gives
\[
P_{\ker(C)}y^+
=
P_{\ker(C)}y.
\]
Every active singular mode contracts strictly for every positive step, while these null components are invariant. This proves convergence to the orthogonal projection onto \(\mathcal N\).

Iterating the exact squared modal factor and summing orthogonal singular components proves the distance identity. Its worst nonzero modal factor is attained at the smallest positive singular value, proving sharpness of the displayed global linear rate.

## Verification

The accompanying `verify.py` builds random rectangular matrices with prescribed positive and zero singular values. It compares the full CGD matrix update with the closed singular-plane formula, checks exact preservation of both Nash-nullspace projections, verifies the distance identity over multiple iterations, and confirms that changing the step changes the transient but not the limiting projected Nash point.

The computations are transcription guards. The convergence, selection law, and sharp rate follow from the singular-value proof above.

## Relationship to prior work

Schäfer and Anandkumar introduce CGD as the exact Nash solution of a regularized bilinear local game. Their defining algorithm contains the matrix inverses used above. Their theoretical results give local exponential convergence under smooth zero-sum assumptions, and their bilinear experiments emphasize that CGD remains stable as interaction strength grows. The paper explicitly states that stronger interactions improve its convergence guarantees.

The inspected defining paper does not state the arbitrary-rank global equilibrium-selection law above. Its displayed bilinear experiment uses a scalar interaction with a unique equilibrium, so it does not expose the nullspace invariant that determines which equilibrium is selected when the Nash set is non-singleton.

Anagnostides and Penna later give a frequency-domain framework for bilinear games and derive tight stability results for Optimistic Gradient Descent/Ascent and finite-memory historical methods. They explicitly describe convergence to the space of Nash equilibria and note that square nonsingular game matrices are a simplifying assumption for their main stability analysis. Their inspected framework does not include the inverse-preconditioned CGD update and does not state a CGD projection-selection rule.

Focused searches for Competitive Gradient Descent together with rank-deficient bilinear games, nullspaces, equilibrium selection, orthogonal projection, exact singular-mode rates, and implicit bias did not identify an implication-equivalent published statement.

## Limitations

The theorem is specific to exact CGD on unconstrained bilinear zero-sum games.

Approximate inner solves can break exact nullspace preservation unless their residuals respect the same subspaces.

The result does not describe nonlinear equilibrium selection near a manifold of Nash equilibria.

The exact rate is per outer CGD iteration and does not account for the computational cost of the inverse-vector products.

## References

1. Florian Schäfer and Anima Anandkumar, “Competitive Gradient Descent,” arXiv:1905.12103v1, first submitted 2019-05-28; NeurIPS 2019.
2. Ioannis Anagnostides and Paolo Penna, “A Robust Framework for Analyzing Gradient-Based Dynamics in Bilinear Games,” arXiv:2010.03211v1, first submitted 2020-10-07.
