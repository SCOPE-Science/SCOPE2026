# Additivity of ordinary and fractional illumination for \(\ell_1\)-sums of normed balls

## Finding
For every integer \(r\ge1\) and every collection of nonzero finite-dimensional real normed spaces \(X_1,\dots,X_r\) with closed unit balls \(B_j\), set
\[
 B=\bigl\{(x_1,\ldots,x_r):\sum_{j=1}^r\|x_j\|_j\le1\bigr\}
 =\operatorname{conv}\biggl(\bigcup_{j=1}^r\iota_j B_j\biggr).
\]
Here \(\iota_j\) embeds the \(j\)-th ball in its coordinate subspace. The exact ordinary and fractional illumination identities are
\[
\boxed{\ I(B)=\sum_{j=1}^r I(B_j),\qquad I^*(B)=\sum_{j=1}^r I^*(B_j).\ }
\]
If each \(B_j\) is an origin-centered Euclidean ball of real dimension \(d_j\ge1\), and \(d=\sum_jd_j\), then
\[
\boxed{\ I(B)=d+r,\qquad I^*(B)=2r.\ }
\]
In particular, for the complex \(\ell_1\)-ball viewed in real dimension \(2r\),
\[
 \boxed{I(\{z\in\mathbb C^r:\sum_j|z_j|\le1\})=3r,\quad
 I^*(\{z\in\mathbb C^r:\sum_j|z_j|\le1\})=2r.}
\]
The structural reason is that a direction capable of illuminating a boundary point concentrated in one coordinate block must strictly dominate the sum of the other block norms; no direction can do this for two distinct blocks.

## Assumptions and scope
Each \(X_j\) is a nonzero finite-dimensional **real** normed space, with symmetric unit ball \(B_j\); \(r\) is finite. Ordinary illumination: a nonzero direction \(v\) illuminates a point \(x\in\partial C\) when \(x+tv\in\operatorname{int} C\) for some real \(t>0\). The minimum finite size of a covering direction family is \(I(C)\). Fractional illumination \(I^*(C)\) is the infimum of total weight over finite families of directions bearing nonnegative weights, where every boundary point receives illuminating weight at least one, following Naszódi. Allowing finite Borel measures gives the same value here: the lower argument applies to all such measures; the upper argument uses finite approximants of each summand. Positive normalization of directions does not affect illumination. Both definitions refer to every boundary point, not only extreme points.

The displayed \(\ell_1\)-sum is a *free sum*, i.e. a convex hull of balls supported in complementary subspaces; it is **not** the Cartesian/direct vector sum (Minkowski sum of balls in complementary subspaces). These operations have different illumination behavior. Central symmetry (norm balls) is essential to the dominance argument; no analogous identity is claimed for an arbitrary off-center choice of convex bodies.

## Proof
**Step 1: Strict derivative criterion.** For a convex function \(g(t)\) on \([0,\infty)\) with finite one-sided derivative at zero, there exists \(t>0\) with \(g(t)<g(0)\) if and only if \(g'_+(0)<0\). Indeed, convexity makes every secant slope at least the right derivative, while a strictly negative right derivative gives decrease for sufficiently small positive steps. Norms along lines are convex and have finite one-sided derivatives.

Put \(s_j=\|v_j\|_j\), \(S=\sum_js_j\). For a boundary point \(y\in\partial B_j\), place \(y\) in coordinate block \(j\) and zeros elsewhere: \(\iota_jy\in\partial B\). Along \(v=(v_1,\ldots,v_r)\), the sum norm is
\[
 g(t)=\|y+tv_j\|_j+t\sum_{k\ne j}\|v_k\|_k
 \qquad(t\ge0).
\]
By the reverse triangle inequality, \(\|y+tv_j\|_j\ge1-ts_j\), so \(g'_+(0)\ge -s_j+(S-s_j)\). If \(v\) illuminates \(\iota_jy\), then \(g'_+(0)<0\), hence
\[
 s_j>\sum_{k\ne j}s_k. \tag{1}
\]
Also \(\|y+tv_j\|_j<1\) for sufficiently small \(t\), so the projected direction \(v_j\) illuminates \(y\) in \(B_j\). Define
\[
 C_j=\bigl\{v:s_j>\sum_{k\ne j}s_k\bigr\}.
\]
The cones \(C_j\) are pairwise disjoint: two strict inequalities of this form would give \(s_i+s_j>S\), impossible because \(S\ge s_i+s_j\). Thus every direction illuminating a pure-block boundary point of block \(j\) belongs to \(C_j\), and its projection illuminates the corresponding factor.

**Step 2: Ordinary lower bound.** Let \(V\) be any finite illuminating family for \(B\). Fix \(j\). For each \(y\in\partial B_j\), at least one \(v\in V\cap C_j\) illuminates \(\iota_jy\); its projection \(v_j\) illuminates \(y\). Hence the projected directions \(\{v_j:v\in V\cap C_j\}\) illuminate \(B_j\), and \(|V\cap C_j|\ge I(B_j)\). Disjointness of the cones yields \(|V|\ge\sum_j I(B_j)\).

**Step 3: Fractional lower bound.** Let \((v^a,w_a)_{a=1}^m\) be any weighted illumination family for \(B\), where \(w_a\ge0\). For each \(j\), retain only indices with \(v^a\in C_j\), projecting their directions to \(X_j\) and retaining their weights. For every \(y\in\partial B_j\), the global illumination constraint at \(\iota_jy\) has total weight at least one, and every contributing global direction is in \(C_j\) and projects to an illuminating direction. Therefore the resulting projected weighted family illuminates \(B_j\), with weight \(W_j=\sum_{a:v^a\in C_j}w_a\ge I^*(B_j)\). Since the cones are disjoint, \(\sum_aw_a\ge\sum_j W_j\ge\sum_j I^*(B_j)\). The same proof for finite Borel measures applies using restriction to each disjoint open cone and push-forward by coordinate projection.

**Step 4: Both upper bounds.** Take illuminating directions \(V_j\) for \(B_j\), and extend each to a direction supported only in block \(j\). Let \(x=(x_1,\ldots,x_r)\in\partial B\), so \(\sum_j\|x_j\|_j=1\). Pick any index with \(a_j=\|x_j\|_j>0\). Since \(x_j/a_j\in\partial B_j\), some \(u_j\in V_j\) illuminates \(x_j/a_j\). By positive homogeneity, \(\|x_j+ta_ju_j\|_j<a_j\) for a suitable \(t>0\). All other block norms are unchanged; hence the extended direction \(\iota_ju_j\) illuminates \(x\) in \(B\). Thus \(I(B)\le\sum_j I(B_j)\), which together with Step 2 gives equality.

For the fractional upper bound, for each \(j\) choose a finite weighted illuminating family of total weight at most \(I^*(B_j)+\varepsilon/r\), embed all its directions into block \(j\), and keep their weights. At the same nonzero coordinate of each boundary point \(x\), every direction illuminating \(x_j/a_j\) also illuminates \(x\); the total illuminating weight is at least one. The combined family has total mass at most \(\sum_jI^*(B_j)+\varepsilon\). Let \(\varepsilon\downarrow0\), completing the fractional equality.

**Step 5: Euclidean factors.** The ordinary illumination number of the Euclidean unit ball in real dimension \(d_j\) is \(d_j+1\): inward directions illuminate exactly the open hemispheres, and at most \(d_j\) open hemispheres cannot cover the sphere (their direction vectors admit a nonzero vector having nonnegative inner products with all of them); directions forming a regular \(d_j\)-simplex centered at the origin suffice.

The fractional number of a Euclidean ball is \(2\): integrate the weighted illumination constraints against the uniform probability distribution of boundary points; each fixed nonzero direction illuminates exactly half of that sphere, giving total weight at least two. Conversely, the rotation-invariant direction measure of total mass two illuminates every boundary point with weight one. If only finite weighted families are admitted, approximate that measure as follows. For every \(\eta>0\), choose \(\delta>0\) such that its measure of the uniformly rotated strict cap \(\{u:\langle u,x\rangle<-\delta\}\) is at least \(1-\eta\) for all unit \(x\); partition the direction sphere into finitely many Borel cells of diameter below \(\delta\), move each cell's mass to a representative, and rescale weights by \((1-\eta)^{-1}\). The resulting finite family illuminates every boundary point with total weight at least one and has total mass \(2/(1-\eta)\to2\). In real dimension one, the two antipodal directions with weight one each attain two exactly. Summing \(I(B_j)=d_j+1\) and \(I^*(B_j)=2\) yields the stated formulas. Taking each \(d_j=2\) identifies \(\mathbb C\) with a real Euclidean plane and gives \(3r\) and \(2r\) for the complex \(\ell_1\)-ball. \(\square\)

## Verification
The proof is valid for every finite \(r\) and every real dimension tuple \((d_1,\ldots,d_r)\) with positive entries, without a computation or asymptotic hypothesis. The necessary strict inequality in (1), pairwise disjointness of dominant-block cones, projection of fractional weights, and normalized-coordinate upper covering have been checked separately. The key boundary issue is strictness: directions with \(\|v_j\|_j=\sum_{k\ne j}\|v_k\|_k\) do not illuminate pure-block points because the right derivative is nonnegative. For \(r=1\) both identities are tautologies. For \(r=2\) with real one-dimensional blocks, \(B\) is a planar diamond and the formulas give \(I=I^*=4\). For a Euclidean planar disk plus a line, the three-dimensional double cone has \(I=5\) and \(I^*=4\). For two complex coordinates, the values are \(I=6\) and \(I^*=4\). These checks are illustrations, not substitutes for the all-dimensional proof.

## Relationship to prior work
Naszódi (2009) introduced the weighted invariant and proved universal symmetric-body upper bounds. Gorodzha (20 September 2026, arXiv:2609.23913v1) proves the sharp universal bound \(I^*(K)\le2^d\) and characterizes its equality case; that theorem does not calculate the fractional invariant under free-sum construction. Rotem, Schejter and Slomka (15 October 2024 preprint) calculate the ordinary and fractional invariants of **Cartesian products** of complex disks, giving \(2^{r+1}-1\) and \(2^r\), respectively; their 2026 published paper supplies relevant definitions. The present free sum of \(r\) disks instead has the additive laws \(3r\) and \(2r\). The publicly documented calculation for a complex two-coordinate \(\ell_1\)-block multiplied by disks already gives fractional value four for the two-coordinate factor but does not assert arbitrary-summand additivity or the general classical formula.

The earlier Boltyanski–Martini (2007) and Wu–Fan–He (2020) *direct vector sums* are Cartesian products (their decomposition is unique \(x=x_1+x_2\) with \(x_i\in K_i\)); they cannot be identified with the convex-hull free sum in the present theorem. Wu–Lv–Zhang–He (2022) provides covering-functional inequalities for convex hulls; its inspected statements do not imply the exact **weighted** illumination identity here. A 2025 paper by Lyu, Gao, Chen and Wu titled *Covering the unit balls of direct sums* is potentially relevant but its full text could not be obtained; whether it has a related classical formula is unresolved. That caveat is not treated as evidence of novelty.

## Limitations
The theorem is for finite sums of centrally symmetric unit balls, not arbitrary convex bodies. It does not address \(\ell_p\)-sums with \(p>1\), Cartesian products, infinite-dimensional Banach spaces, quantitative covering functionals at a fixed homothety ratio, or the full Hadwiger conjecture. The fractional equality uses an infimum; it does not assert a finitely supported optimal fractional measure for smooth Euclidean factors. No claim is made to priority over inaccessible literature, notably the 2025 direct-sum covering paper, or over differently indexed versions of a free-sum identity.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4(2), 2009, doi:10.55016/ojs/cdm.v4i2.62022.
2. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1, initially publicly posted 20 September 2026, https://arxiv.org/html/2609.23913.
3. L. Rotem, A. Schejter, B. A. Slomka, *The Complex Illumination Problem*, arXiv:2410.12021v1 (first public 15 October 2024), https://arxiv.org/html/2410.12021v1; Combinatorica 46, 2026, doi:10.1007/s00493-025-00195-7.
4. V. Boltyanski and H. Martini, *Illumination of direct vector sums of convex bodies*, Studia Sci. Math. Hungar. 44(3), 367–376 (2007), doi:10.1556/SScMath.44.2007.3.6.
5. S. Wu, B. Fan and C. He, *Covering functionals of Minkowski sums and direct sums of convex bodies*, Math. Inequal. Appl. 23(3), 1145–1154 (2020), doi:10.7153/mia-2020-23-88; https://files.ele-math.com/articles/mia-23-88.pdf.
6. S. Wu, Y. Lv, K. Zhang and C. He, *Covering convex hulls of compact convex sets with smaller homothetic copies*, Math. Inequal. Appl. 25(2), 369–377 (2022), doi:10.7153/mia-2022-25-22; https://files.ele-math.com/articles/mia-25-22.pdf.
7. Y. Lyu, S. Gao, F. Chen and S. Wu, *Covering the unit balls of direct sums*, Scientia Sinica Mathematica (2025), doi:10.1360/ssm-2025-0162 (full text not obtained).
