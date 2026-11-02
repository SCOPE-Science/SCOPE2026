# A sharp dimension-four threshold for approximate smoothness in cube–crosspolytope norm interpolations

## Finding
For every integer \(n\ge2\) and real \(s>0\), let \(X_{n,s}\) be real \(\mathbb R^n\) with norm
\[
\|x\|_{n,s}=\max\big\{\|x\|_\infty,\,\|x\|_1/s\big\}.
\]
Write \(J(x)=\{f\in X_{n,s}^*:\|f\|_*=1,\ f(x)=\|x\|_{n,s}\}\) for each nonzero \(x\), and define the global approximate-smoothness coefficient
\[
E(X_{n,s})=\sup_{\|x\|_{n,s}=1}\operatorname{diam}_{X_{n,s}^*}J(x).
\]
Its exact, dimension- and parameter-dependent value is
\[
\boxed{E(X_{n,s})=
\begin{cases}
\dfrac{1+(s-1)^2}{s},&n=2,\quad 1<s<2,\\[4pt]
\dfrac{2}{s},&n=3,\quad 1<s<2,\\[4pt]
2,&\text{otherwise}.
\end{cases}}
\]
In particular, these norms are approximately smooth (there exists \(\varepsilon<2\) for which the space is \(\varepsilon\)-smooth) exactly in dimensions two and three for \(1<s<2\). Every dimension at least four has the maximal defect \(2\) throughout the entire interpolation. In dimension two the coefficient has jump discontinuities at both \(s=1\) and \(s=2\). In dimension three it has a jump at \(s=2\), but approaches the endpoint value \(2\) continuously as \(s\) decreases to one.

## Assumptions and scope
The scalar field is \(\mathbb R\), the dimension is finite with \(n\ge2\), and \(s>0\) is arbitrary. The dual operator norm is the norm induced by \(\|\cdot\|_{n,s}\). No differentiability or strict convexity is assumed. Approximate smoothness here is the norming-functional-diameter notion introduced by Chmieliński–Khurana–Sain; it is not the classical differentiability notion nor the modulus of smoothness. For \(1<s<2\) the unit ball is the intersection of the cube with the dilated cross-polytope,
\[
B_{n,s}=[-1,1]^n\cap\{x:\textstyle\sum_i|x_i|\le s\}.
\]
The result neither concerns complex scalars nor quantitative smoothness of other interpolating norms.

## Proof
**1. Vertex classification in the interior parameter regime.** Fix \(1<s<2\) and write \(a=s-1\in(0,1)\). Every vertex of \(B_{n,s}\) has the form of a signed coordinate permutation of
\[
v=(1,a,0,\ldots,0).
\]
To see this without assuming a polytope enumeration, work first in a closed sign orthant. A point with strict inequalities in the cube and sum constraints can be perturbed. A point where only one coordinate reaches modulus one has \(\ell_1\)-sum at most one unless another coordinate is nonzero; without an active sum constraint, it can again be perturbed. At a point on the active sum constraint with at least two nonzero coordinates strictly below one, transfer a sufficiently small amount of modulus between those two coordinates, maintaining the sum; hence it is not extreme. Thus any extreme point must have one coordinate of modulus one and all remaining positive modulus \(a\) in exactly one other coordinate. Conversely, \(v\) is extreme: the coordinate constraint \(x_1\le1\), the sum constraint in the orthant with \(x_1,x_2\ge0\), and both signs of each zero coordinate force \(x_1=1\), \(x_2=a\), and all other coordinates to vanish. Signed permutations give all vertices.

**2. The dual support identity.** For any functional with coefficient vector \(h\in\mathbb R^n\), arrange the moduli as \(b_1\ge b_2\ge\cdots\ge b_n\ge0\). Linear optimization over \(B_{n,s}\) first assigns modulus one to a coordinate of weight \(b_1\), then assigns the remaining budget \(a\) to a coordinate of weight \(b_2\). Swapping any assigned mass to a higher-weight coordinate cannot decrease the objective, so the fractional-knapsack argument gives the exact identity
\[
\|h\|_{X_{n,s}^*}=b_1+a b_2.\tag{1}
\]
The same formula follows by maximizing over the classified vertices.

**3. Reduction to a vertex and its incident facets.** Any unit-sphere point belongs to a proper face containing some vertex \(v\) of the polytope. Its norming set is a subset of the norming set at that vertex: if \(x\) lies in the relative interior of a face \(F\), every supporting hyperplane containing \(x\) contains \(F\), hence also its vertices. Therefore it suffices to take the maximum over vertices. Symmetry reduces the computation to the displayed \(v\). Its active facet functionals are exactly the first coordinate functional \(e_1^*\) and all
\[
f_\sigma=\frac1s\big(e_1^*+e_2^*+\sum_{j=3}^n\sigma_j e_j^*\big),\qquad \sigma_j\in\{-1,1\}.
\]
Indeed, the dual ball is the convex hull of the coordinate functionals \(\pm e_i^*\) and the sign-functionals \(s^{-1}\sum_i\varepsilon_i e_i^*\). Each displayed active functional has dual norm one by (1), and the norming face \(J(v)\) is their convex hull. Their pairwise dual distances determine its diameter by convexity.

**4. Dimensions two and three.** If \(n=2\), only \(e_1^*\) and \(f=(e_1^*+e_2^*)/s\) are active. Their difference has coefficient moduli \(1/s\) and \(a/s\). Thus (1) gives
\[
E(X_{2,s})=\|e_1^*-f\|_*=(1+a^2)/s.
\]
If \(n=3\), the active functionals are \(e_1^*\) and \(f_\pm=s^{-1}(e_1^*+e_2^*\pm e_3^*)\). Their distances are
\[
\|f_+-f_-\|_*=2/s,\qquad
\|e_1^*-f_\pm\|_*=(1+a)/s=1.
\]
Because \(1<s<2\), the maximum is \(2/s\). Every other vertex is a signed permutation, so these values give the global coefficients.

**5. The dimension-four obstruction.** For \(n\ge4\), at \(v\) choose two active sign functionals that agree in coordinates one and two and have opposite signs in coordinates three and four (agreeing elsewhere). Their difference equals \(2(e_3^*+e_4^*)/s\) up to signs. Applying (1) gives dual distance \(2(1+a)/s=2\). No two norm-one functionals can be farther apart than two, establishing \(E(X_{n,s})=2\) for all \(n\ge4\) and \(1<s<2\).

**6. Endpoints and exterior parameters.** If \(s\le1\), the norm is exactly \(\|x\|_1/s\). At the unit vector \(s e_1\), two norm-one functionals taking opposite maximal values on the second coordinate have dual distance two, so \(E=2\). If \(s\ge2\), \(e_1+e_2\) is a unit vector normed by both \(e_1^*\) and \(e_2^*\); the unit vector \(e_1-e_2\) witnesses \(\|e_1^*-e_2^*\|_*=2\). This again gives \(E=2\). The bound \(E\le2\) is automatic, completing every parameter and dimension case.

## Verification
The standalone `artifacts/verify.py` uses exact rational arithmetic to enumerate every signed two-support vertex, each candidate facet functional, and every active pair of facet functionals, and maximizes all dual distances over the full list of vertices. It passes 20 complete finite instances: dimensions \(2,3,4,5\) and parameters \(9/8,4/3,3/2,7/4,15/8\). Run `python3 artifacts/verify.py`; the expected output is `VERIFY_OK 20 full-polytope exact-rational cases`. The checker is corroborative: the proof's vertex, knapsack, support-face and endpoint arguments establish the result for all quantified dimensions and real parameters, not merely the checked rational samples.

## Relationship to prior work
Chmieliński, Khurana and Sain introduced the dual-face-diameter notion of approximate smoothness and gave a generic extreme-functional formula for polyhedral spaces (their Theorem 4.3). That general formula is used in spirit here, but does not provide the full dimension-and-parameter classification, the strict dimension-four obstruction, or the endpoint jumps for this specific family. Deza, Hiriart-Urruty and Pournin studied the same cube–crosspolytope interpolation bodies, including combinatorics and volumes, but not the global norming-functional diameter. The source's explicit polar identification ensures that this family is canonical rather than an arbitrary renorming. At \(n=2,\ s=\sqrt2\), the unit ball is a regular octagon and the formula reduces to \(2(\sqrt2-1)\), agreeing with the known regular-octagon computation in Chmieliński–Khurana–Sain, Example 4.1. That special parameter instance is not claimed as new.

Other related treatments of these interpolation bodies determine their Mahler products, graph distances, illumination numbers, or different quantitative invariants. These invariants do not imply the displayed coefficient without a new comparison of incident dual facets and their distances. Searches under cube–crosspolytope, vector top-\(k\), CVaR, polyhedral approximate smoothness, and norming-face diameter terminology found no explicit equivalent classification in the accessible literature. This is a literature-based comparison, not a proof of historical novelty.

## Limitations
The theorem is strictly about the displayed real norm family and the coefficient \(E\); it does not determine alternative smoothness moduli, complex-scalar analogues, or the corresponding values in other CVaR normalizations. The finite checker is not a proof for the continuum of parameters or unbounded dimensions. Although the most relevant original full texts were inspected, older or poorly indexed equivalent formulations remain a bibliographic risk. Only self-review has been performed; there is no independent mathematical audit.

## References
1. J. Chmieliński, D. Khurana, D. Sain, *Approximate smoothness in normed linear spaces*, arXiv:2109.11884, first posted 2021-09-24, especially §4 and Theorem 4.3, https://arxiv.org/abs/2109.11884.
2. A. Deza, J.-B. Hiriart-Urruty, L. Pournin, *Polytopal balls arising in optimization*, arXiv:2011.05607, first posted 2020-11-11, especially §1–2 on polar interpolation bodies, https://arxiv.org/abs/2011.05607.
3. *Exact Mahler products for cube–cross-polytope intersections and their three-dimensional phase diagram*, publicly indexed mathematical result, 2026, with full RESULT.md inspected; distinct volume-product invariant.
4. *Exact shortest-path metric of the cube–cross-polytope intersection balls*, publicly indexed mathematical result, 2026, with full RESULT.md inspected; distinct graph-distance invariant.
