# Shape-uniform logistic crossover for difference bodies of homothetic frusta

## Finding

Let \(m\ge1\), let \(B\subset\mathbb R^m\) be a compact convex body with nonempty interior, and let \(0\le t\le1\). Define its height-one homothetic frustum and its affine-invariant difference-body quotient by
\[
F_t(B)=\operatorname{conv}(B\times\{0\},\,tB\times\{1\}),\qquad
\mathcal R_m(B,t)=\frac{\operatorname{vol}_{m+1}(F_t(B)-F_t(B))}{\operatorname{vol}_{m+1}(F_t(B))}.
\]
Write \(A=\operatorname{vol}_m(B)\), and use the standard normalized mixed volume
\(v_j=V_m(B[j],(-B)[m-j])/A\) for \(0\le j\le m\). Then, for \(0\le t<1\),
\[
\boxed{\mathcal R_m(B,t)=
\frac{2(m+1)}{1-t^{m+1}}
\sum_{j=0}^m\binom mj v_j\frac{1-t^{j+1}}{j+1}.}
\]
At \(t=1\), the continuous extension equals \(2\operatorname{vol}_m(B-B)/A\). For every fixed \(B\), the quotient is **strictly decreasing** on \([0,1]\).

For \(0\le t<1\), define
\[
L_m(t)=\frac{2\bigl(2^{m+1}-(1+t)^{m+1}\bigr)}{1-t^{m+1}},\qquad
U_m(t)=\frac{2(m+1)}{1-t^{m+1}}\sum_{j=0}^m\binom mj^2\frac{1-t^{j+1}}{j+1}.
\]
Their continuous endpoint values are \(L_m(1)=2^{m+1}\) and \(U_m(1)=2\binom{2m}{m}\). The **sharp complete range** at every fixed \(m\) and \(t\) is
\[
\boxed{L_m(t)\le\mathcal R_m(B,t)\le U_m(t).}
\]
For \(m\ge2\), lower equality holds exactly for centrally symmetric bases, and upper equality exactly for simplicial bases; every intermediate number occurs for some convex base. For \(m=1\) both bounds coincide. The pyramid endpoint recovers \(L_m(0)=2(2^{m+1}-1)\) and \(U_m(0)=\binom{2m+2}{m+1}\), while the prism endpoint has \(2^{m+1}\le\mathcal R_m(B,1)\le2\binom{2m}{m}\).

**Dimension-uniform boundary layer.** Let \(B_m\subset\mathbb R^m\) be *any* sequence of full-dimensional convex bodies, with no common regularity, symmetry, or normalization assumptions. For every fixed \(\tau\ge0\),
\[
\boxed{\lim_{m\to\infty}\frac{\mathcal R_m(B_m,1-\tau/m)}{\mathcal R_m(B_m,1)}
=\frac{2}{1+e^{-\tau/2}}.}
\]
For every fixed \(T>0\), the convergence is uniform for \(0\le\tau\le T\), with error at most \(C_T/m\) for all sufficiently large \(m\), where \(C_T\) depends only on \(T\), not on the bodies. The exact-scale transition interpolates between \(1\) at the prism and \(2\) just outside the shrinking boundary layer. It is independent of the base shapes, even when they vary arbitrarily with dimension.

In three-dimensional frusta (\(m=2\)), setting \(c=(\operatorname{area}(B-B)/A-2)/2\in[1,2]\) reduces the formula to
\[
\boxed{\mathcal R_2(B,t)=2+\frac{6[1+c(1+t)]}{1+t+t^2}.}
\]
Thus a single quotient measured at known \(t\) exactly reconstructs the planar base's Rogers--Shephard difference-body ratio. This last statement does **not** reconstruct the base up to affine equivalence.

## Assumptions and scope

All volumes are Lebesgue volumes in the stated dimensions; \(B[j]\) means \(j\) copies of \(B\) as arguments of the symmetric multilinear mixed-volume functional. The upper face is homothetic to the lower with a common center; a vertical shear can adjust the homothety center without changing any quotient. The case \(t=0\) is a pyramid and \(t=1\) a prism. Convex bases may be nonsymmetric, nonsmooth, and nonpolyhedral. The dimension-uniform assertion concerns the ratio to the prism quotient for the **same** base in each dimension. It does not prescribe the growth of that unnormalized prism quotient.

## Proof

**1. Exact sections of the difference body.** Translate the base so that \(0\in\operatorname{int}B\); this changes the frustum only by an affine shear. Put \(q=1-t\). The horizontal section at height \(z\in[0,1]\) of the frustum is \((1-qz)B\). At axial difference \(h\in[0,1]\), the horizontal difference-body section is the union over \(0\le u\le1-h\) of
\[
(1-q(h+u))B-(1-qu)B.
\]
Both coefficients decrease with \(u\), and, because \(0\in B\), these Minkowski sums are nested and largest at \(u=0\). The entire section is therefore
\[
(1-qh)B-B.
\]
Reflection gives the sections for \(h<0\). Consequently,
\[
\operatorname{vol}_{m+1}(F_t(B)-F_t(B))
=2\int_0^1\operatorname{vol}_m((1-qh)B-B)\,dh.
\]
The frustum itself has volume \(\int_0^1(1-qz)^m A\,dz\). After the substitution \(s=1-qh\), their ratio, for \(t<1\), is
\[
\boxed{\mathcal R_m(B,t)=
\frac{2\int_t^1\operatorname{vol}_m(sB-B)\,ds}
{A\int_t^1s^m\,ds}.}\tag{1}
\]
When \(t=1\), direct prism geometry gives \(\mathcal R_m(B,1)=2\operatorname{vol}_m(B-B)/A\). This agrees with the limit in (1).

**2. Exact mixed-volume polynomial and strict monotonicity.** Minkowski multilinearity gives
\[
f(s):=\frac{\operatorname{vol}_m(sB-B)}A
=\sum_{j=0}^m\binom mjv_j s^j.
\]
Inserting this into (1) proves the first formula. Moreover \(f(s)/s^m=\operatorname{vol}_m(B-s^{-1}B)/A\), which is strictly decreasing as \(s\in(0,1]\) increases: after translating \(B\) to contain the origin, a strictly larger negative dilation gives strict volume inclusion. Thus (1) is twice the \(s^m\)-weighted mean of a strictly decreasing function on \([t,1]\), so \(\mathcal R_m(B,t)\) decreases strictly as its left endpoint \(t\) moves toward \(1\).

**3. Sharp all-dimensional bounds and equality.** Brunn--Minkowski gives \(f(s)\ge(1+s)^m\), with equality at any \(s>0\) exactly when \(B\) is centrally symmetric up to translation. Integration yields \(L_m\). The now-proved Godbersen mixed-volume inequality asserts \(v_j\le\binom mj\) for every \(j\); inserting those coefficientwise bounds yields \(U_m\). For \(m\ge2\), equality in the upper integral forces equality for an interior mixed-volume index, which, by the established equality theorem for Godbersen's inequality, characterizes simplices. Conversely all simplices realize equality in every index. For \(m=1\) each interval is simultaneously a simplex and centrally symmetric. To see that no value between the bounds is missing, take a continuous Minkowski interpolation from a centrally symmetric full-dimensional base to a simplex. The quotient is a continuous function on this path, so the intermediate value theorem fills the interval. The endpoint expressions follow by direct substitution or the binomial identities \(\sum_j\binom mj^2=\binom{2m}m\) and \(2(m+1)\sum_j\binom mj^2/(j+1)=\binom{2m+2}{m+1}\).

**4. A shape-uniform mixed-volume concentration estimate.** Mixed-volume reflection symmetry gives \(v_j=v_{m-j}\); Alexandrov--Fenchel gives \(v_j^2\ge v_{j-1}v_{j+1}\) for interior indices. All \(v_j\) are positive. Hence the sequence \(v_j\) is nonincreasing with the distance \(|j-m/2|\). Define a probability distribution on \(\{0,\ldots,m\}\) by
\[
p_j=\frac{\binom mjv_j}{\sum_{k=0}^m\binom mkv_k}.
\]
It is a symmetric binomial distribution reweighted by a nonincreasing function of \(|j-m/2|\). For any increasing function \(g\) of that distance, the elementary negative-covariance inequality for oppositely ordered functions gives
\[
\sum_jp_jg(|j-m/2|)\le2^{-m}\sum_j\binom mjg(|j-m/2|).
\]
Applying this to the square gives the *shape-uniform bound*
\[
\mathbb E_pJ=m/2,\qquad
\operatorname{Var}_p(J)\le m/4.\tag{2}
\]
This conclusion uses the mixed-volume log-concavity, not a claim of independence between indices.

**5. Universal logistic profile and quantitative convergence.** With \(r=1-u/m\), the preceding polynomial gives
\[
\frac{f(r)}{f(1)}=\mathbb E_p r^J.
\]
For \(0\le u\le T\) and \(m\ge2T\), put \(\ell=\log(1-u/m)\). Taylor's theorem in the real exponent, the zero centered first moment, and (2) imply
\[
\bigl|\mathbb E_p e^{\ell J}-e^{\ell m/2}\bigr|
\le\frac{\ell^2}{2}\operatorname{Var}_p(J)
\le\frac{u^2}{2m}.
\]
Indeed the second derivative of \(x\mapsto e^{\ell x}\) is bounded by \(\ell^2\) for \(x\ge0\). The elementary logarithmic estimate \(|\ell+u/m|\le u^2/m^2\) also gives
\[
\bigl|e^{\ell m/2}-e^{-u/2}\bigr|\le\frac{u^2}{2m},
\qquad
\bigl|(1-u/m)^m-e^{-u}\bigr|\le\frac{u^2}{m}.
\]
Therefore \(f(1-u/m)/f(1)=e^{-u/2}+O_T(1/m)\), uniformly for all bases and \(0\le u\le T\). Rewriting (1) and dividing by the prism value yields, for \(\tau>0\),
\[
\frac{\mathcal R_m(B_m,1-\tau/m)}{\mathcal R_m(B_m,1)}
=\frac{\int_0^\tau f(1-u/m)/f(1)\,du}
{\int_0^\tau(1-u/m)^m\,du}.
\]
Both integrands have uniform error at most \(u^2/m\), while the denominator is at least \(\tau e^{-2T}\). Integrating and comparing the two ratios produces \(O_T(1/m)\), uniformly for \(0<\tau\le T\). The limiting ratio equals
\[
\frac{\int_0^\tau e^{-u/2}\,du}{\int_0^\tau e^{-u}\,du}
=\frac{2}{1+e^{-\tau/2}}.
\]
The conclusion extends continuously to \(\tau=0\), where the ratio is identically \(1\). This proves both the universal limit and the dimension-uniform error claim.

**6. Dimension three.** For \(m=2\), the mixed-volume polynomial is \(f(s)=1+2cs+s^2\), with \(c=(\operatorname{area}(B-B)/A-2)/2\). Inserting it into (1) produces the stated rational formula, and the planar Brunn--Minkowski and Rogers--Shephard bounds yield \(1\le c\le2\). The formula determines \(c\) from any given \(t\) and \(\mathcal R_2\); its exact inverse is \(c=((\mathcal R_2-2)(1+t+t^2)/6-1)/(1+t)\).

## Verification

Run `python verify.py` using only the Python 3 standard library. It checks exact rational endpoint and three-dimensional formulas, the pyramid binomial identities, the mixed-volume-binomial concentration inequality in symmetric and simplex cases, and high-dimensional convergence for these extremal families and intermediate symmetric log-concave coefficient profiles. Run `python check_polytope.py` with Python 3, NumPy, and SciPy for a separate direct convex-hull test of twenty three-dimensional frusta, comparing the 3D polytope difference-body volume to the independently computed planar difference-body area. These are finite corroborations. The general section identity, strict monotonicity, all-dimensional equality classification, and dimension-uniform convergence are proved above, using the cited Brunn--Minkowski, Aleksandrov--Fenchel, and Godbersen results.

## Relationship to prior work

The 2023 work of Langharst, Putterman, Roysdon, and Ye develops difference bodies and their geometric inequalities in a general framework, without this exact homothetic-frustum section law or the dimension-uniform boundary layer. The 2026 Godbersen theorem of Kotrbatý and Mouamine supplies the **already-known coefficientwise mixed-volume upper inequality** used here; Friedland, Putterman, and Szusterman supply its **already-known equality characterization**. No new universal Godbersen inequality or independent proof of it is claimed. The sharp upper bound for a frustum is an application of these established deep results together with the explicit section formula, not a new general bound for arbitrary convex bodies.

An existing exact analysis of the Santaló point and affine volume product of homothetic frusta treats a different invariant. A separate exact mixed-volume analysis of simplex truncations handles the simplicial upper-equality family in detail, but not the mixed-volume concentration and logistic limit uniformly over arbitrary sequences of nonsymmetric bases. The current contribution is the **shape-uniform high-dimensional crossover**, the exact difference-body section reduction, and the resulting complete sharp frustum profile, not the known general inequalities or their simplex cases. Historical priority for an equivalent specialized frustum calculation is not independently established.

## Limitations

The upper sharp classification relies on recently proved Godbersen and equality theorems, rather than proving them afresh. The universal crossover is normalized by the shape-dependent prism quotient and holds for a height-one **homothetic** frustum; no assertion is made for skew prismatoids, unrelated parallel slices, or a prescribed absolute difference-body volume growth across dimensions. The error constant depends on the compact \(\tau\)-interval, and the theorem does not assert dimension-uniform convergence for \(\tau\) growing with \(m\). An equivalent unindexed result in older convex-geometry literature remains a residual priority risk.

## References

1. D. Langharst, E. Putterman, M. Roysdon, and D. Ye, *On the mth-Order Weighted Projection Body Operator and Related Inequalities*, arXiv:2305.00479v1, first publicly posted 30 April 2023; especially §1 on difference bodies and Rogers--Shephard bounds. https://arxiv.org/abs/2305.00479
2. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the Lp-Rogers-Shephard inequality*, arXiv:2607.20387v2, Theorem 1.1, 14 September 2026. https://arxiv.org/abs/2607.20387
3. O. Friedland, E. Putterman, and M. Szusterman, *The equality case in Godbersen's inequality and its generalizations*, arXiv:2610.04527v2, Theorem 3 and Theorem 8, 7 October 2026. https://arxiv.org/abs/2610.04527
4. R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, 2nd expanded edition, Cambridge University Press (2014), chapters on mixed volumes and Aleksandrov--Fenchel inequalities.
5. *Universal Santaló and volume-product laws for homothetic frusta*, published geometric record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359
6. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, published geometric record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949
