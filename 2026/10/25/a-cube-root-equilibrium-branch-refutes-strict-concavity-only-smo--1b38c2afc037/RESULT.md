# A cube-root equilibrium branch refutes strict-concavity-only smoothness

## Finding

Consider two players choosing actions \(x,y\in[-1,1]\), with utilities

\[
U_1(x,y;\varepsilon)=-\tfrac12(x-y)^2+\varepsilon x,
\qquad
U_2(x,y)=-\tfrac12y^2+y(x-x^3),
\]

for \(0\le\varepsilon\le\tfrac18\). Both utilities are infinitely differentiable and strictly concave in the acting player's own action. Nevertheless, the unique Nash equilibrium is

\[
(x^*(\varepsilon),y^*(\varepsilon))=(\varepsilon^{1/3},\varepsilon^{1/3}-\varepsilon).
\]

The equilibrium is unique at \(\varepsilon=0\) and for every parameter in the stated interval, but \(x^*(\varepsilon)\) is not locally Lipschitz or differentiable at zero. This is a counterexample to the sufficiency claim in Theorem 3 of De los Reyes Marín et al. (2026): smoothness and strict concavity in each player's own action do not, by themselves, imply a smooth equilibrium response.

## Assumptions and scope

The strategy sets are compact convex intervals \([-1,1]\). The perturbation parameter is nonnegative, matching the parameter direction in the cited utility-perturbation framework. A two-player complete-information game is a special case of a Bayesian game with singleton type spaces. Utilities are \(C^\infty\); their own-action second derivatives are both exactly \(-1\). The result concerns the claimed regularity of the equilibrium map, not existence: existence and uniqueness hold throughout \([0,1/8]\).

## Proof

For player 1, the derivative with respect to \(x\) is \(-x+y+\varepsilon\), and the second derivative is \(-1\). Thus the unique best response is the projection of \(y+\varepsilon\) onto \([-1,1]\). For player 2, the derivative with respect to \(y\) is \(-y+x-x^3\), and the second derivative is \(-1\); hence player 2's unique best response is \(y=x-x^3\).

For every \(x\in[-1,1]\), the value \(x-x^3\) lies in \([-2/(3\sqrt3),2/(3\sqrt3)]\). Since \(0\le\varepsilon\le1/8\), adding \(\varepsilon\) keeps this interval strictly inside \([-1,1]\). Therefore at every equilibrium player 1's best response is interior and satisfies \(x=y+\varepsilon\). Combining the two best-response equations gives

\[
x=x-x^3+\varepsilon\quad\Longleftrightarrow\quad x^3=\varepsilon.
\]

There is exactly one real solution, \(x=\varepsilon^{1/3}\), and then \(y=\varepsilon^{1/3}-\varepsilon\). For \(0\le\varepsilon\le1/8\), both actions lie in \([-1,1]\), so this solution is indeed the unique Nash equilibrium.

The local Lipschitz quotient at zero is unbounded:

\[
\frac{|x^*(\varepsilon)-x^*(0)|}{\varepsilon}=\varepsilon^{-2/3}\longrightarrow\infty\qquad(\varepsilon\downarrow0).
\]

Hence the equilibrium map is not locally Lipschitz and has no finite right derivative at zero. The joint first-order-condition map is \(F(x,y,\varepsilon)=(-x+y+\varepsilon,-y+x-x^3)\). Its Jacobian with respect to \((x,y)\) at \((0,0,0)\) is

\[
D_{(x,y)}F(0,0,0)=\begin{pmatrix}-1&1\\1&-1\end{pmatrix},\qquad\det D_{(x,y)}F(0,0,0)=0.
\]

Thus the nonsingularity needed for the usual implicit-function argument fails even though the equilibrium is unique and each own-action objective is strictly concave. This identifies the missing condition in the cited proof.

## Verification

The accompanying `verify_counterexample.py` uses only Python's standard library and exact rational arithmetic. It checks 99 parameter values \(\varepsilon=k^{-3}\), for integers \(2\le k\le100\), verifies both first-order conditions and interior feasibility exactly, and confirms that the response quotient equals \(k^2\) along this sequence. It also checks that the displayed base Jacobian determinant is zero. These finite checks are supplementary; the universal best-response and unbounded-quotient arguments above are analytical, not inferred from a finite computation.

## Relationship to prior work

The target is Theorem 3 of “Utility Perturbation Operators in Bayesian Games: Structural Stability and Equilibrium Deformation” (2026), which states that \(C^2\) utilities strictly concave in each player's own action suffice for local uniqueness and a continuous, locally Lipschitz, continuously differentiable equilibrium map. Its proof invokes a nonsingular Jacobian of the joint first-order conditions but does not include that property among the theorem's hypotheses or derive it from own-action strict concavity. The present game meets the stated hypotheses while its Jacobian is singular and its equilibrium branch has a cube-root singularity. The result is deliberately limited to this explicit counterexample; it does not claim that no earlier work discusses singular equilibrium comparative statics or that all conclusions of the cited paper fail.

## Limitations

The counterexample refutes the stated sufficiency of the hypotheses for the regularity conclusion; it does not refute the paper's equilibrium-existence or upper-hemicontinuity claims. Nonsingularity of the joint first-order-condition Jacobian is the missing condition for the specific implicit-function proof route; this finding does not claim nonsingularity is necessary for every possible differentiable equilibrium branch. The example uses a complete-information special case and one scalar perturbation.

## References

1. De los Reyes Marín, Ó.; Paz Gil, I.; Torres-Pruñonosa, J.; Gómez-Martínez, R. “Utility Perturbation Operators in Bayesian Games: Structural Stability and Equilibrium Deformation.” *Mathematics* 14 (2026), 506. First published 31 January 2026. DOI: 10.3390/math14030506.
2. Barthel, A.-C.; Hoffmann, E. “On dynamic adjustment and comparative statics via the implicit function theorem.” *Mathematical Social Sciences* 115 (2022), 52–57. DOI: 10.1016/j.mathsocsci.2021.12.004. Background only; the explicit counterexample is proved here.
