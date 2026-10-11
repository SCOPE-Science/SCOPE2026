# Sharp stability of mixed-norm metric projection onto the Euclidean disk

## Finding
Let \(B_2=\{y\in\mathbb R^2:\|y\|_2\le1\}\) be the closed Euclidean disk, and for each real \(1<p<\infty\) let \(P_p(x)\) be the unique \(y\in B_2\) minimizing \(\|x-y\|_p\). Writing \(q=p/(p-1)\), the exact global Lipschitz constant measured in \(\ell_p^2\) on both input and output is
\[
\operatorname{Lip}(P_p)=\max_{0\le t\le1}\frac{(1+t^p)^{1/p}(1+t^{q(q-1)})^{1/q}}{1+t^q}.
\]
In particular, the quartic ambient norm has the exact closed-form amplification
\[
\operatorname{Lip}(P_4)^4=1+\frac2{\sqrt3},\qquad
\operatorname{Lip}(P_4)\approx1.211565031277261.
\]
Moreover, \(\operatorname{Lip}(P_p)=1\) exactly when \(p=2\); for every other \(p\) the projection amplifies some perturbations.

## Assumptions and scope
Throughout, scalars are real, \(1<p<\infty\), and \(\|x\|_p=(|x_1|^p+|x_2|^p)^{1/p}\). The target is **not** the ambient norm ball: it is the fixed Euclidean disk \(B_2\). The projection exists and is unique because \(B_2\) is compact and convex and the objective \(\|x-y\|_p^p\) is strictly convex in \(y\). The global Lipschitz constant is the supremum over **all distinct** \(x,x'\in\mathbb R^2\), not merely exterior or boundary inputs. The displayed maximum includes \(t=0,1\) and is finite.

## Proof
**1. Explicit exterior normal coordinates.** Inside \(B_2\), \(P_p\) is the identity. Let \(x\notin B_2\), set \(y=P_p(x)\in\partial B_2\), and write \(q=p/(p-1)\). First-order optimality of \(\|x-y\|_p^p\) under the constraint \(\|y\|_2\le1\) yields a positive multiplier and
\[
x=y+s\,w(y),\qquad w(y)_i=\operatorname{sgn}(y_i)|y_i|^{q-1},\quad s>0.
\]
Indeed \(\operatorname{sgn}(x_i-y_i)|x_i-y_i|^{p-1}\) is a common positive multiple of \(y_i\). Conversely, any such \(y\) on the Euclidean unit circle and any \(s>0\) obey the convex KKT sufficiency conditions, hence give \(P_p(x)=y\). Coordinate signs of \(x\) and \(y\) coincide; sign changes and coordinate permutations reduce the derivative calculation to \(y=(a,b)\) with \(a,b>0\), \(a^2+b^2=1\).

**2. Exact derivative norm.** Parameterize the circle by its unit Euclidean tangent \(v=(-b,a)\). Differentiating the map \((y,s)\mapsto x\) in tangent and outward directions gives \(dx=Dv\,d\theta+w\,ds\), where
\[
D=\operatorname{diag}\bigl(1+s(q-1)a^{q-2},\ 1+s(q-1)b^{q-2}\bigr),\quad
w=(a^{q-1},b^{q-1}).
\]
The Jacobian is invertible because
\[
|\det(Dv,w)|=a^q+b^q+s(q-1)(a^{q-2}b^q+a^qb^{q-2})>0.
\]
Solving the two-by-two linear system, the derivative of \(P_p\) is the rank-one map
\[
h\longmapsto v\,\frac{w_1h_2-w_2h_1}{a^q+b^q+s(q-1)(a^{q-2}b^q+a^qb^{q-2})}.
\]
Hölder duality, including equality in the norm of the displayed linear functional, gives
\[
\|DP_p(x)\|_{p\to p}
=\frac{(a^p+b^p)^{1/p}(a^{q(q-1)}+b^{q(q-1)})^{1/q}}{a^q+b^q+s(q-1)(a^{q-2}b^q+a^qb^{q-2})}.
\]
The denominator is strictly increasing with \(s\). Thus the supremum of exterior derivative norms equals its one-sided boundary limit \(s\downarrow0\). Setting \(t=b/a\) gives the formula in the Finding section. Exchanging \(a,b\) maps \(t\) to its reciprocal, so \(0\le t\le1\) suffices, with endpoints interpreted by continuity.

**3. Local norms give the exact global norm.** The projection is continuous: any convergent inputs have convergent minimizing points by compactness and uniqueness. On each exterior open quadrant, the inverse-function theorem applies to the coordinates above, and the derivative is bounded by the claimed maximum. On the interior of \(B_2\), the derivative is the identity, whose norm is one; the maximum in the formula is at least one (take \(t=0\)). Every line segment not contained in a coordinate axis meets the axes and the Euclidean circle at finitely many points. Integrate the derivative bound separately over the intervening open intervals, then use continuity at endpoints. A segment contained in an axis is treated directly: there the projection is scalar clipping to the interval \([-1,1]\), hence is one-Lipschitz. This proves the global upper bound. Conversely, at each \(a,b>0\) and every \(s>0\), the derivative operator norm is a lower bound for the global Lipschitz constant. Letting \(s\downarrow0\), and then optimizing the direction, yields equality.

**4. Closed-form quartic evaluation.** For \(p=4\), \(q=4/3\), and \(z=t^{4/9}\), the fourth power of the expression to maximize becomes
\[
R(z)=\frac{(1+z^9)(1+z)^3}{(1+z^3)^4}
=\frac{1-z^3+z^6}{(1-z+z^2)^3},\qquad0\le z\le1.
\]
For \(0<z\le1\), set \(u=z+z^{-1}\ge2\). Then
\[
R(z)=\frac{u^3-3u-1}{(u-1)^3},\qquad
\frac{dR}{du}=-\frac{3((u-1)^2-3)}{(u-1)^4}.
\]
The function strictly increases on \([2,1+\sqrt3]\) and decreases thereafter; both endpoint limits are one. Its unique maximum occurs at \(u=1+\sqrt3\), where \(R=1+2/\sqrt3\). The corresponding pair has ratio
\[
\frac ba=\left(\frac{1+\sqrt3-\sqrt{(1+\sqrt3)^2-4}}2\right)^{9/4}.
\]
A sequence of arbitrarily close exterior inputs near this boundary direction asymptotically attains the global Lipschitz constant.

**5. Sharp nonexpansivity boundary.** At \(p=2\) the general expression is identically one, recovering ordinary Hilbert-space metric projection. For \(p>2\), \(q(q-1)<q\) and \(q(q-1)<p\); as \(t\downarrow0\), the positive numerator contribution of order \(t^{q(q-1)}\) dominates the denominator's contribution of order \(t^q\), so the quotient is greater than one for small positive \(t\). For \(1<p<2\), the positive \(t^p\) term dominates the negative \(t^q\) term because \(p<q\), again giving strict expansion. This settles every exponent.

## Verification
Run `python3 verify.py` from the directory containing this file and `verify.py`. It uses only the Python standard library; its deterministic checks include an exact integer-polynomial derivative identity, 200 pairs evaluated by an independent angular minimization of the quartic objective, and three exterior tangential finite differences compared against the analytic Jacobian. The output is `VERIFY_OK polynomial_identity=1 random_pairs=200 tangential_derivatives=3` followed by the numerical constant. These checks are supplementary; the infinite input domain, general exponents, and global optimization are proved above.

## Relationship to prior work
Zhang and Liu (2014), *The Representations and Continuity of the Metric Projections on Two Classes of Half-Spaces in Banach Spaces*, study representations and continuity for half-space and subspace projections; a curved Euclidean disk measured in a different ambient norm is not among their target sets. Li (2024), *Fréchet differentiability of the metric projection operator in Banach spaces*, treats derivatives of projections onto balls of the **same ambient Banach norm**, cylinders, and cones (see its Section 3 and Example 3.2). Those radial norm-ball results neither give the present cross-norm disk map nor its sharp global Lipschitz constant. These comparisons do not rule out an undiscovered equivalent historical computation.

## Limitations
The exact closed form \((1+2/\sqrt3)^{1/4}\) is established for the two-dimensional real \(\ell_4\) ambient norm. For arbitrary \(1<p<\infty\), the stated one-variable maximization is exact but is not evaluated in elementary closed form. No result is claimed for higher dimensions, endpoints \(p=1,\infty\), or complex scalars. No independent external mathematical validation has occurred.

## References
1. Z. Zhang and C. Liu, *The Representations and Continuity of the Metric Projections on Two Classes of Half-Spaces in Banach Spaces*, Abstract and Applied Analysis (2014), Article 908676, first published 2014-02-17. DOI: `10.1155/2014/908676`. Full text: https://onlinelibrary.wiley.com/doi/full/10.1155/2014/908676
2. J. Li, *Fréchet differentiability of the metric projection operator in Banach spaces*, arXiv:2401.01480, first submitted 2024-01-03. https://arxiv.org/abs/2401.01480
