# Exact reflected-core profile and dimensional phase transition of centrally symmetric frusta

## Finding
Let \(m\ge1\) be an integer, let \(B\subset\mathbb R^m\) be an arbitrary full-dimensional compact convex body satisfying \(B=-B\), and let \(0\le t\le1\). Form the homothetic frustum
\[
 F_t(B)=\operatorname{conv}\bigl(B\times\{0\},\;tB\times\{1\}\bigr).
\]
For any full-dimensional convex body \(K\), define its maximal centrally symmetric core-volume fraction by
\[
 \mathcal C(K)=\max_{p\in\mathbb R^{\dim K}}
 \frac{\operatorname{vol}(K\cap(2p-K))}{\operatorname{vol}(K)}.
\]
Put \(q_m=2^{1/m}\) and \(t_m=(2q_m-1)^{-1}\). Then the following is an **exact shape-independent theorem**:
\[
\boxed{
\mathcal C(F_t(B))=
\begin{cases}
 \displaystyle\frac{2}{(2q_m-1)^m(1-t^{m+1})},&0\le t\le t_m,\\[6pt]
 \displaystyle\frac{2\left[\bigl((1+t)/2\bigr)^{m+1}-t^{m+1}\right]}{1-t^{m+1}},&t_m\le t<1,\\[6pt]
 1,&t=1.
\end{cases}}
\]
The **unique** maximizing center \(p\) is \((0,c_m(t))\), where
\[
\boxed{
c_m(t)=
\begin{cases}
\displaystyle\frac{q_m-1}{(1-t)(2q_m-1)},&0\le t\le t_m,\\[6pt]
\tfrac12,&t_m\le t\le1.
\end{cases}}
\]
At \(t=t_m\), the two center formulas agree. The symmetry fraction is strictly increasing on \([0,1]\); in particular any exact measured fraction determines \(t\) uniquely, independently of the shape of \(B\). At \(t=t_m\), the optimizing center switches from a floating interior height to the axial midpoint. The transition satisfies \(t_m=1-2\log2/m+O(m^{-2})\).

There is a sharp **dimension-dependent boundary layer**. For fixed \(0\le t<1\), \(\lim_{m\to\infty}\mathcal C(F_t(B_m))=1/2\) for any sequence of centrally symmetric bases \(B_m\subset\mathbb R^m\). For fixed \(\tau\ge0\), set \(t=1-\tau/m\) whenever \(m\ge\tau\). Then
\[
\boxed{\lim_{m\to\infty}\mathcal C(F_{1-\tau/m}(B_m))=
\begin{cases}
\displaystyle\frac{2}{1+e^{\tau/2}},&0\le\tau\le2\log2,\\[6pt]
\displaystyle\frac{1}{2(1-e^{-\tau})},&\tau\ge2\log2.
\end{cases}}
\]
The maximizing center has height tending to \(1/2\) for \(0\le\tau\le2\log2\), and to \((\log2)/\tau\) for \(\tau\ge2\log2\). Thus the fixed-parameter high-dimensional limit does not commute with the prism endpoint.

## Assumptions and scope
The ambient dimension is \(m+1\), and all volumes are Lebesgue volumes in the relevant affine space. The base is only assumed convex, full-dimensional and centrally symmetric around the origin. Neither smoothness nor a polyhedral structure is needed. The two horizontal faces are concentric homothetic copies with scale ratio \(t\). If the original base is centered at a different point, translating and shearing the frustum puts it in this normal form without altering \(\mathcal C\).

For every convex body \(K\) and center \(p\), \(K\cap(2p-K)\) is centrally symmetric, and every centrally symmetric subset of \(K\) centered at \(p\) lies in this intersection. Thus maximizing reflected overlap is exactly the largest-centrally-symmetric-subset problem; no restriction to special core shapes is imposed.

## Proof
**1. The horizontal reductions are sharp, without rotational symmetry.** Let \(r(z)=1-(1-t)z\), and set \(F=F_t(B)\). The section of \(F\) at height \(z\in[0,1]\) is \(r(z)B\). If a proposed reflection center is \((x,c)\), then its overlap section at height \(z\) is
\[
 r(z)B\cap\left(2x+r(2c-z)B\right)
\]
whenever both \(z\) and \(2c-z\) lie in \([0,1]\), and is otherwise empty. The centers of symmetry of the section bodies coincide when \(x=0\). For any two centrally symmetric convex sets of the form \(r_1B\) and \(r_2B\), their intersection at any relative translate has volume no greater than \(\min(r_1,r_2)^m\operatorname{vol}_m(B)\); that upper bound is attained when they are concentric, because then they are nested. Hence for every \(c\) the largest overlap occurs at horizontal shift \(x=0\).

The inequality is strict for \(x\ne0\) at any nondegenerate optimal height \(c\in(0,1)\): at \(z=c\) the two radii coincide and \(r(c)B\) has strictly less than full-volume overlap with its nontrivial translate \(2x+r(c)B\). This is because a full-dimensional compact convex body cannot contain a nonzero translate of itself. Continuity of the section-overlap volume in \(z\) produces strict loss on a positive-length interval. Thus the **only** maximizing horizontal shift is zero.

**2. The one-dimensional objective.** By symmetry of the reflected height interval, its intersection with \([0,1]\) is \([0,2c]\) for \(0\le c\le1/2\), and \([2c-1,1]\) for \(1/2\le c\le1\). As \(r\) decreases with height, the smaller of \(r(z)\) and \(r(2c-z)\) is the radius at the larger height. Therefore
\[
 I(c)=\max_x\operatorname{vol}_{m+1}\left(F\cap\bigl(2(x,c)-F\bigr)\right)
 =2\operatorname{vol}_m(B)\begin{cases}
\displaystyle\int_c^{2c}r(u)^m\,du,&0\le c\le1/2,\\[5pt]
\displaystyle\int_c^1r(u)^m\,du,&1/2\le c\le1.
\end{cases}
\]
This formula includes \(t=0\). The total frustum volume, for \(0\le t<1\), is
\[
\operatorname{vol}_{m+1}(F)=\operatorname{vol}_m(B)
\frac{1-t^{m+1}}{(m+1)(1-t)}.
\]

**3. Exact unique optimum and the phase transition.** When \(t<1\), the objective on \(c\ge1/2\) decreases strictly because \(I'(c)=-2\operatorname{vol}_m(B)r(c)^m<0\) for \(c<1\). On \(0<c<1/2\), Leibniz differentiation yields
\[
 I'(c)=2\operatorname{vol}_m(B)\bigl(2r(2c)^m-r(c)^m\bigr).
\]
The ratio \(r(c)/r(2c)\) increases strictly with \(c\) for \(t<1\). Consequently the derivative changes sign at most once, from positive to negative, and the potential interior maximum solves
\[
 r(c)=q_m r(2c),\qquad c=\frac{q_m-1}{(1-t)(2q_m-1)}.
\]
This critical point is at most \(1/2\) precisely when \(t\le t_m\). Otherwise \(I\) increases up to \(c=1/2\) and decreases afterward. At \(t=t_m\), its derivative vanishes only at the endpoint \(c=1/2\), still uniquely maximizing. When \(t=1\) the frustum is a centered-base prism: its reflected-overlap volume has its unique maximum at the unique full central-symmetry center \((0,1/2)\).

At the interior critical point, \(r(c)=q_m/(2q_m-1)\) and \(r(2c)=1/(2q_m-1)\). Evaluating the integral, using \(q_m^m=2\), and dividing by the total frustum volume gives the first displayed branch. At \(c=1/2\), integration from \(1/2\) to \(1\) gives the second branch. Both values and optimizing centers agree at \(t=t_m\).

**4. Strict increase in the truncation parameter.** In the first branch the denominator \(1-t^{m+1}\) decreases strictly, so \(\mathcal C\) increases strictly. In the second branch the volume ratio equals twice the probability that a variable \(U\in[0,1]\) lies in \([1/2,1]\), where \(U\) has density proportional to \([1-(1-t)u]^m\). For \(t'>t\), the ratio of the density at \(t'\) to that at \(t\), before normalization, is strictly increasing as a function of \(u\), since
\[
 \frac{d}{du}\log\frac{1-(1-t')u}{1-(1-t)u}
 =\frac{t'-t}{[1-(1-t')u][1-(1-t)u]}>0.
\]
The monotone-likelihood-ratio ordering therefore makes the upper-half probability strictly increase. The two branches join continuously at \(t_m\); moreover \(\mathcal C(F_1)=1\), proving strict monotonicity throughout the closed parameter interval.

**5. Large dimension and critical scaling.** Writing \(\ell=\log2\) gives \(q_m=e^{\ell/m}=1+\ell/m+O(m^{-2})\), so \(t_m=1-2\ell/m+O(m^{-2})\) and \((2q_m-1)^m\to4\). For each fixed \(t<1\), eventually \(t<t_m\) and \(t^{m+1}\to0\), giving limit \(1/2\). If \(t=1-\tau/m\), then \(t^{m+1}\to e^{-\tau}\) and \(((1+t)/2)^{m+1}\to e^{-\tau/2}\). In the two regimes separated by \(\tau=2\ell\), substitution into the correct finite-dimensional branch gives the displayed piecewise limiting profile. The two expressions both equal \(2/3\) at the threshold; the center limit follows by substitution in \(c_m(t)\). This proves all claims.

## Verification
The standalone `verify.py` checks exact planar threshold identities, compares the predicted ratios with independent polygon clipping for seven trapezoids, independently integrates overlap of square-based frusta for five heights with noncentral perturbations, and checks dimensional crossover and monotonicity at finite parameters. Its output is:

```
EXACT_PLANAR_THRESHOLD_AND_BRANCH_IDENTITIES_PASSED
INDEPENDENT_PLANAR_CONVEX_CLIPPING_PASSED 7
INDEPENDENT_SQUARE_BASE_VOLUME_QUADRATURE_PASSED 5
DIMENSIONAL_CROSSOVER_AND_MONOTONICITY_DIAGNOSTICS_PASSED
ALL_CHECKS_PASSED
```

These finite tests are diagnostic; the universal theorem rests on the proof above. Floating-point grids cannot detect increments below machine precision, so the numerical monotonicity test permits roundoff. Exact monotonicity is proved analytically.

## Relationship to prior work
Goenka, Moore, Sun and White discuss Kovner–Besicovitch symmetry and the established sharp triangular lower bound in the plane (arXiv:2309.12597v1, public 22 September 2023). Their main results concern axial and folding measures; the materially inspected paper does not give a homothetic-frustum reflected-core formula or optimizing-center transition. Chakerian and Stein (1965) develop general central-symmetry measures and their extremal behavior, not the full parameter profile of the present frusta.

Related published frustum work on Santaló points and volume products (public `published-finding corpus/2026`, geometric research record `3dbfdaf0b359`) establishes formulas for a **different affine functional**, involving polar volumes rather than the largest point-reflected overlap. Its full result and proof have been examined for implication overlap; neither the exact reflection-center phase transition nor the two-branch Kovner–Besicovitch profile follows from the cited polar identities without new arguments.

Prior results on asymmetric double cones with centrally symmetric equators characterize a different two-apex family; its special one-sided-cone endpoint agrees with the present \(t=0\) endpoint, which is therefore not independently claimed as a new theorem. The novelty claimed here is the **entire nonzero-top frustum family** together with its sharp transition and dimension-dependent crossover. No title-matching or absence of search results is asserted to prove priority.

## Limitations
The top and bottom faces must be concentric homothetic copies of a centrally symmetric base. The theorem does not cover asymmetric bases, tilted homothety centers unrelated by affine shear, or general prismatoids with unrelated sections. Its inverse statement assumes an exact symmetry ratio; no statistical or noise stability is established. The one-sided pyramid endpoint is a known classical special case, and specialized older literature on centrally symmetric cores could contain equivalent frustum formulas; historical priority is provisional. Independent review has not been performed.

## References
1. R. Goenka, K. Moore, W. R. Sun and E. P. White, *On Axial Symmetry in Convex Bodies*, arXiv:2309.12597v1, first posted 22 September 2023. https://arxiv.org/abs/2309.12597
2. G. D. Chakerian and S. K. Stein, *On Measures of Symmetry of Convex Bodies*, *Canadian Journal of Mathematics* **17** (1965), 497–504. DOI:10.4153/CJM-1965-049-3.
3. *Universal Santaló and volume-product laws for homothetic frusta*, published geometric research record `3dbfdaf0b359`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359 .
4. I. Fáry and L. Rédei, *Der zentralsymmetrische Kern und die zentralsymmetrische Hülle von konvexen Körpern*, *Mathematische Annalen* (1950). Historical background; full text was not accessible in this review.
