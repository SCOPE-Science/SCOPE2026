# Strict Minkowski concavity and canonical centering of critical covariogram transition bodies

## Finding

**Theorem (strict recentering and translation Hessian).** Let \(n\ge 2\), let \(\beta>0\), and let \(K\subset\mathbb R^n\) be a convex body with \(C^3\) boundary and everywhere positive Gaussian curvature. The surface-area measure of \(K\) on \(S^{n-1}\) is denoted by \(S_K\), and its support function by \(h_K\). Define the admissible translation domain
\[
\mathcal D_K=\{a\in\mathbb R^n:0\in\operatorname{int}(K+a)\}=-\operatorname{int}K,
\qquad h_a(v)=h_K(v)+a\cdot v>0.
\]
For \(a\in\mathcal D_K\), define
\[
F_a(y)=\int_{S^{n-1}}h_a(v)\log\cosh\!\left(\frac{y\cdot v}{2h_a(v)}\right)\,dS_K(v),
\qquad T_{a,\beta}=\{y:F_a(y)\le\beta\}.
\]
The following statements are parts of one centering theorem.

1. **Strict Minkowski interpolation.** For any two *distinct* admissible translations \(a_0,a_1\) and every \(0<\lambda<1\), setting \(a_\lambda=(1-\lambda)a_0+\lambda a_1\),
\[
(1-\lambda)T_{a_0,\beta}+\lambda T_{a_1,\beta}
\ \subset\ \operatorname{int} T_{a_\lambda,\beta}.
\]
Consequently \(a\mapsto\operatorname{vol}_n(T_{a,\beta})^{1/n}\) is strictly concave on \(\mathcal D_K\). In particular, it has at most one maximizer in that open domain.

2. **Strict centering for symmetric bodies.** If \(K=-K\), then the origin is the unique maximizer of the level-body volume for every \(\beta>0\). In fact, for any \(c\ne0\) and \(0\le s<t\) with \(tc\in\mathcal D_K\),
\[
T_{tc,\beta}\subset\operatorname{int} T_{sc,\beta}.
\]
Thus *every* radial direction contracts as the symmetry center is displaced, not merely the total volume.

3. **Exact translation second variation.** Suppose \(K=-K\). For \(u\in S^{n-1}\), let \(\rho(u)>0\) be the unique solution of \(F_0(\rho(u)u)=\beta\), and put
\[
D(u)=\frac12\int_{S^{n-1}}(u\cdot v)
\tanh\!\left(\frac{\rho(u)(u\cdot v)}{2h_K(v)}\right)\,dS_K(v)>0,
\]
\[
N(u;c)=\int_{S^{n-1}}
\frac{(c\cdot v)^2\rho(u)^2(u\cdot v)^2}{4h_K(v)^3}
\operatorname{sech}^{2}\!\left(\frac{\rho(u)(u\cdot v)}{2h_K(v)}\right)\,dS_K(v)>0
\quad(c\ne0).
\]
Then for fixed \(c\) and \(t\to0\),
\[
\operatorname{vol}_n(T_{tc,\beta})
=\operatorname{vol}_n(T_{0,\beta})
-\frac{t^2}{2}\,H_{K,\beta}(c)+O_{K,\beta,c}(t^4),
\]
where the **positive-definite quadratic form** is
\[
H_{K,\beta}(c)=\int_{S^{n-1}}\rho(u)^{n-1}
\frac{N(u;c)}{D(u)}\,d\sigma(u)>0\qquad(c\ne0).
\]
Here \(\sigma\) is ordinary surface measure on the direction sphere, distinct from \(S_K\).

## Assumptions and scope

The theorem applies simultaneously to every dimension \(n\ge2\), every \(\beta>0\), and every body with the stated regularity and positive curvature. The translation must retain the origin in the interior. The integrals over normal directions use the *unchanged* surface-area measure \(S_K\): translation changes \(h_a\), not that measure. The restriction \(K=-K\) is used only in assertions 2 and 3. There is no claim about nonsmooth bodies, boundary choices of origin, or \(\beta=0\).

The transition body at \(\beta=1\) is the critical \(\log\cosh\) limit body introduced by Haddad, Jiménez, and Resende (2026); their scaling remark motivates all positive levels. The classical covariogram is translation invariant, while the radial smoothing responsible for this critical body refers to a distinguished origin. The centering question therefore probes an actual geometric choice, not a reparameterization of a translation-invariant observable.

## Proof

**Existence, radial uniqueness, and compactness.** Let \(\varphi(z)=\log\cosh(z/2)\). Then \(\varphi(0)=0\), \(\varphi''(z)=\operatorname{sech}^2(z/2)/4>0\), and \(\varphi\) is even. The measure \(S_K\) has full support and positive continuous density on the sphere under the curvature hypotheses. The function \(F_a\) is even, strictly convex in \(y\), continuous, and vanishes only at \(0\). The bound
\[
\log\cosh t\ge |t|-\log2
\]
gives
\[
F_a(y)\ge \frac12\int|y\cdot v|\,dS_K(v)
-(\log2)\int h_a(v)\,dS_K(v).
\]
The first integral is bounded below by a positive constant times \(\lVert y\rVert\), while the last is \(n\operatorname{vol}_n(K)\), independent of \(a\), by the surface-area equilibrium identity. Therefore every \(T_{a,\beta}\) is a compact centrally symmetric convex body with nonempty interior, and \(r\mapsto F_a(ru)\) increases strictly from zero to infinity for each unit \(u\). All radial solutions below exist uniquely.

**Joint convexity with its equality case.** The scalar perspective
\[
P(h,z)=h\varphi(z/h),\qquad h>0,
\]
is jointly convex. Its two-point Jensen inequality is strict unless the two ratios \(z_0/h_0\) and \(z_1/h_1\) agree. Because \(h_a(v)\) is affine in \(a\), integration proves joint convexity of \((a,y)\mapsto F_a(y)\). Suppose there is equality for endpoints \((a_0,y_0)\), \((a_1,y_1)\). Since \(S_K\) has full support, strict convexity and continuity force
\[
\frac{y_0\cdot v}{h_K(v)+a_0\cdot v}
=\frac{y_1\cdot v}{h_K(v)+a_1\cdot v}
\quad\text{for every }v\in S^{n-1}.
\]
Writing this equation for both \(v\) and \(-v\) and subtracting yields
\[
((y_0-y_1)\cdot v)\big(h_K(v)+h_K(-v)\big)=0.
\]
Every width \(h_K(v)+h_K(-v)\) is positive; hence \(y_0=y_1=y\). The original equation then forces \((y\cdot v)((a_1-a_0)\cdot v)=0\) for every \(v\), so either \(y=0\) or \(a_0=a_1\). Thus if \(a_0\ne a_1\), joint Jensen is strict whenever the two endpoint vectors are not both zero. If both are zero, the interpolated point has \(F_{a_\lambda}(0)=0<\beta\). Every point of the Minkowski interpolation in assertion 1 therefore satisfies \(F_{a_\lambda}(y)<\beta\). The interpolated set is compact, so it lies within the *interior* of \(T_{a_\lambda,\beta}\). Brunn–Minkowski and strict volume containment give
\[
\operatorname{vol}_n(T_{a_\lambda,\beta})^{1/n}
>(1-\lambda)\operatorname{vol}_n(T_{a_0,\beta})^{1/n}
+\lambda\operatorname{vol}_n(T_{a_1,\beta})^{1/n}.
\]

**Symmetric-body radial rigidity.** For \(K=-K\), the support function and surface-area measure are even in the normal. Consequently \(F_{tc}(y)=F_{-tc}(y)\). Differentiate the perspective twice with respect to the support variable:
\[
\frac{\partial^2}{\partial h^2}
\left[h\log\cosh\!\left(\frac{z}{2h}\right)\right]
=\frac{z^2}{4h^3}\operatorname{sech}^{2}\!\left(\frac{z}{2h}\right).
\]
For \(c\ne0\) and \(y\ne0\), the set of normals satisfying both \(c\cdot v\ne0\) and \(y\cdot v\ne0\) has positive \(S_K\)-measure. Hence \(t\mapsto F_{tc}(y)\) is strictly convex and even on its admissible interval, so it increases strictly for \(t>0\). For \(0\le s<t\) and \(y\in T_{tc,\beta}\setminus\{0\}\), we obtain \(F_{sc}(y)<F_{tc}(y)\le\beta\); the origin also lies in the interior. This proves strict inclusion in assertion 2 and unique maximality at \(0\).

**Differentiation of the radial body.** Write \(\rho_t(u)\) for the solution to \(F_{tc}(\rho_t(u)u)=\beta\). Its defining derivative in the radial variable at \(t=0\) equals \(D(u)>0\) as displayed above. Evenness in \(t\) yields \(\rho'_0(u)=0\), and twice differentiating the implicit equation yields
\[
\rho''_0(u)=-\frac{N(u;c)}{D(u)}.
\]
The integrals defining \(F_{tc}\) are real analytic in \(t\) on sufficiently small compact parameter intervals because all denominators remain uniformly positive; the implicit radial solutions and their derivatives are uniform over the compact sphere. They are even in \(t\). The polar integration formula
\[
\operatorname{vol}_n(T_{tc,\beta})
=\frac1n\int_{S^{n-1}}\rho_t(u)^n\,d\sigma(u)
\]
therefore has second derivative \(-H_{K,\beta}(c)\) at zero and no odd powers through order three, proving the claimed \(O(t^4)\) expansion. Positivity of the integrands where \((c\cdot v)(u\cdot v)\ne0\) proves that \(H_{K,\beta}\) is positive definite. All quantifiers and the boundary exclusions stated above are used in this argument.

## Verification

A self-contained Python 3 program, `verify.py`, numerically checks the scalar perspective curvature, strict interpolation and radial contraction for translated unit disks, and the exact integral expression for the area-loss Hessian at level \(\beta=1\). Execute `python3 verify.py` from the extracted package. Its expected marker is `CRITICAL_TRANSITION_RECENTERING_CHECKS_OK`.

The disk check gives radial length approximately \(1.659084806166\) and Hessian-area loss coefficient approximately \(3.170423103194\). Translation finite-difference loss coefficients at displacements \(0.02\), \(0.04\), and \(0.08\) converge as expected to that coefficient. These tests check computations; the all-dimensional statements follow solely from the analytic arguments above.

## Relationship to prior work

Haddad, Jiménez, and Resende, *A Smooth Covariogram and the Transition Between Projection Bodies* (arXiv:2610.11700, first public October 8, 2026), define the critical functional \(F_0\), establish its place between classical projection bodies and polar \(L_2\) projection bodies, and note its general level scaling. The recentering geometry of this body and its translation Hessian are not results of their inspected article.

Lutwak, Yang, and Zhang, *Orlicz Projection Bodies* (2010), establish the general Orlicz modular and Orlicz–Petty inequalities. Their elementary convex perspective inequality supplies a starting tool here, but the main global theorem optimizes over shapes and does not state strict set-valued recentering or this quantitative fixed-shape translation Hessian. Zhou, Ye, and Zhang (arXiv:2501.07565) treat higher-order Orlicz bodies and global isoperimetric inequalities, not the particular fixed-body translation variation. This comparison does not preclude a different unindexed treatment of the same implications.

## Limitations

This theorem does **not** assert existence of a maximizing origin in the interior for an arbitrary nonsymmetric body; strict concavity gives *at most one* such maximizer. It excludes singular boundary-origin choices, degenerate curvature, and \(\beta=0\). The coefficient in the translation expansion is an exact positive integral, not an elementary closed form for general \(K\). The finite verifier covers a disk in dimension two only; no finite experiment establishes an infinite-dimensional or all-body claim. The prior-literature search is not a proof of historical novelty, and independent scientific audit has not been performed.

## References

1. J. Haddad, C. H. Jiménez, M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1, October 8, 2026. https://arxiv.org/html/2610.11700v1
2. E. Lutwak, D. Yang, G. Zhang, *Orlicz Projection Bodies*, Advances in Mathematics **223** (2010), 220–242. Author-hosted full text: https://cims.nyu.edu/~yangd/papers/orlicz_projection_body.pdf
3. X. Zhou, D. Ye, Z. Zhang, *The mth order Orlicz projection bodies*, arXiv:2501.07565, January 13, 2025. https://arxiv.org/pdf/2501.07565
