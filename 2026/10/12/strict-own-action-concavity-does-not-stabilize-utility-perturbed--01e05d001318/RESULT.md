# Strict own-action concavity does not stabilize utility-perturbed Bayesian equilibria
## Finding
Consider the two-player, singleton-type special case of the utility-perturbation framework in De los Reyes Marín, Paz Gil, Torres-Pruñonosa and Gómez-Martínez (2026). Let
\[
S_1=S_2=[-1,1],
\]
with baseline payoffs
\[
\pi_1(x,y)=-\frac{x^2}{2}+xy,
\qquad
\pi_2(x,y)=-\frac{y^2}{2}+(x-x^3)y.
\]
Set every perturbation intensity to zero except the second player's perceptual coefficient, and choose
\[
P_2(y)=\frac{y^2}{2},
\qquad \theta_2=b.
\]
For \(0\le b\le 1/2\), the perturbed utilities are
\[
U_1(x,y)=-\frac{x^2}{2}+xy,
\qquad
U_2(x,y;b)=-\frac{1-b}{2}y^2+(x-x^3)y.
\]
They are twice continuously differentiable and strictly concave in each player's own strategy, yet the equilibrium set changes from one point at \(b=0\) to three points for every \(b>0\). Therefore the structural-stability theorem and its local-equivalence corollary are false under the hypotheses printed in the source.

## Assumptions and scope
The type spaces are singletons with the trivial common prior, so this is a Bayesian game in the source's class with no informational uncertainty. The strategy sets are compact and convex. The only active perturbation is the continuous own-strategy function \(P_2(y)=y^2/2\), entering with nonnegative intensity \(b\). For \(0\le b\le 1/2\),
\[
\frac{\partial^2 U_1}{\partial x^2}=-1,
\qquad
\frac{\partial^2 U_2}{\partial y^2}=-(1-b)<0,
\]
so the source's twice-differentiable and strict-own-concavity assumptions hold throughout the parameter range used below.

## Proof
Player 1's first-order condition is
\[
-x+y=0,
\]
and because \(U_1\) is strictly concave in \(x\), the unique best response is \(x=y\).

Player 2's first-order condition is
\[
-(1-b)y+x-x^3=0.
\]
For \(x\in[-1,1]\),
\[
|x-x^3|\le \frac{2}{3\sqrt3}.
\]
When \(0\le b\le1/2\), this gives
\[
\left|\frac{x-x^3}{1-b}\right|
\le \frac{4}{3\sqrt3}<1,
\]
so the unconstrained maximizer lies strictly inside \([-1,1]\). Hence
\[
BR_2(x)=\frac{x-x^3}{1-b}.
\]
At equilibrium \(x=y\), and substitution gives
\[
(1-b)x=x-x^3,
\]
therefore
\[
x(x^2-b)=0.
\]
At \(b=0\), the unique equilibrium is \((0,0)\). For every \(b\in(0,1/2]\), the equilibria are exactly
\[
(0,0),\qquad (\sqrt b,\sqrt b),\qquad (-\sqrt b,-\sqrt b).
\]
Every relative neighborhood of the origin in the nonnegative perturbation orthant contains such positive values of \(b\), so no neighborhood can have a unique equilibrium for every perturbation as claimed in Theorem 3.

The proof failure can also be seen directly at the unperturbed equilibrium. The system of own-strategy first-order conditions is
\[
F(x,y;b)=
\begin{pmatrix}
-x+y\\
-(1-b)y+x-x^3
\end{pmatrix}.
\]
Its strategy Jacobian at \((0,0,0)\) is
\[
D_{(x,y)}F(0,0;0)=
\begin{pmatrix}
-1&1\\
1&-1
\end{pmatrix},
\]
with determinant zero. Strict concavity controls the diagonal own-action second derivatives but does not force the full game Jacobian to be nonsingular because cross-player derivatives can cancel them.

## Verification
The bundled `verify.py` checks the own-action Hessians, the global interior-best-response bound on \(0\le b\le1/2\), the exact equilibrium polynomial \(x(x^2-b)\), the one-versus-three equilibrium count, and the zero determinant of the unperturbed first-order-condition Jacobian. These checks are algebraic confirmations of the displayed proof rather than substitutes for it.

## Relationship to prior work
The motivating article states that twice continuous differentiability and strict concavity in each player's own strategy imply local uniqueness, smooth parameter dependence, local Lipschitz continuity, and differentiability of equilibrium, and its proof explicitly asserts that the full first-order-condition Jacobian is nonsingular. The example above satisfies the printed assumptions but violates local uniqueness for every positive perturbation scale, so it directly refutes that theorem and the following local-homeomorphism corollary.

Classical concave-game theory distinguishes own-action concavity from stronger conditions coupling players' derivatives. Rosen's uniqueness theory introduces diagonal strict concavity; his public report explicitly notes that concavity in each player's own strategy gives existence while the additional diagonal condition is used for uniqueness. That literature explains why the source's step from own-action strict concavity to a nonsingular joint Jacobian is not valid, but it does not contain this source-specific perturbation counterexample.

## Limitations
The claim concerns Theorem 3 and Corollary 1 of the motivating article as written. It does not dispute the article's equilibrium-existence result, nor the statement that accumulation points of equilibria under vanishing perturbations are equilibria of the unperturbed game. It also does not assert that structural stability cannot be recovered under an added regularity hypothesis such as nonsingularity of the equilibrium Jacobian or an appropriate diagonal-strict-concavity condition.

## References
De los Reyes Marín, Ó.; Paz Gil, I.; Torres-Pruñonosa, J.; Gómez-Martínez, R. *Utility Perturbation Operators in Bayesian Games: Structural Stability and Equilibrium Deformation*. Mathematics 14 (2026), 506. DOI: 10.3390/math14030506. First public version: 31 January 2026.

Rosen, J. B. *Existence and Uniqueness of Equilibrium Points for Concave N-Person Games*. Econometrica 33 (1965), 520–534. DOI: 10.2307/1911749. A public 1964 report is archived as NASA-CR-57255.
