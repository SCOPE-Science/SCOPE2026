# A sharp Mahler-volume gain from shortening one edge of an equilateral metric

## Finding

Fix an integer \(d\ge3\). On a set \(M=\{0,1,\ldots,d\}\) of \(d+1\) points, put
\[
d_t(0,1)=t,\qquad d_t(i,j)=1\quad\text{for every other distinct pair},\qquad 0<t\le1.
\]
This is a metric for every indicated parameter. Let \(P_t\) be the unit ball of the **real** \(d\)-dimensional Lipschitz-free space \(\mathcal F(M,d_t)\), in the molecule coordinates associated with base point \(0\); write \(Q_t=P_t^\circ\) for the dual Lipschitz unit ball. Their ordinary coordinate Lebesgue volumes are, exactly,
\[
\boxed{\operatorname{vol}_d(P_t)=\frac{1}{d!}\binom{2d}{d}\frac{d+(d-1)t}{(2d-1)t},\qquad
\operatorname{vol}_d(Q_t)=t\bigl(2d-(d-1)t\bigr).}
\]
Thus the affine-invariant Mahler volume product has the complete closed profile
\[
\boxed{\mathcal M_d(t)=\operatorname{vol}_d(P_t)\operatorname{vol}_d(Q_t)
=\frac{\binom{2d}{d}}{d!(2d-1)}
\bigl(d+(d-1)t\bigr)\bigl(2d-(d-1)t\bigr).}
\]
It is strictly increasing for \(0<t<\tfrac{d}{2(d-1)}\), strictly decreasing for \(\tfrac{d}{2(d-1)}<t\le1\), and consequently has the **unique** maximizing short distance
\[
\boxed{t_d^*=\frac{d}{2(d-1)}.}
\]
Relative to the equilateral value \(\mathcal M_d(1)=\frac{d+1}{d!}\binom{2d}{d}\), its exact maximum gain is
\[
\boxed{\frac{\mathcal M_d(t_d^*)}{\mathcal M_d(1)}
=1+\frac{(d-2)^2}{4(2d-1)(d+1)}>1.}
\]
The optimizing distance decreases to \(\tfrac12\), and the relative gain tends to \(\tfrac18\), as the dimension tends to infinity. In dimension \(d=2\), the same two volume formulas hold, but the unique maximizer on \((0,1]\) is the endpoint \(t=1\).

## Assumptions and scope

All spaces, norms, polars, and volumes are real. Identify signed zero-mass measures \(x=(x_0,\ldots,x_d)\), where \(\sum_i x_i=0\), with the coordinates \((x_1,\ldots,x_d)\in\mathbb R^d\) and \(x_0=-\sum_{i=1}^d x_i\). The transportation norm is the minimum cost of moving the positive part of \(x\) to its negative part at prices \(d_t(i,j)\). With \(e_0=0\) and \(e_1,\ldots,e_d\) the coordinate basis, the primal and dual balls are
\[
P_t=\operatorname{conv}\left\{\pm\frac{e_i-e_j}{d_t(i,j)}:0\le i<j\le d\right\},
\quad Q_t=\left\{f\in\mathbb R^d:\left|f_i-f_j\right|\le d_t(i,j),\ f_0=0\right\}.
\]
These are exact polars under the standard pairing in \(\mathbb R^d\). No Euclidean orthonormalization of the zero-mass subspace is performed: individual volume formulas use the displayed coordinates, whereas their product is invariant under any invertible coordinate change. At \(t=0\), two points coalesce and the dimension changes; that endpoint is expressly excluded.

## Proof

**1. The transportation norm and its orthant chambers.** For \(x\) of zero total mass, let \(m=\sum_i(x_i)_+=\sum_i(-x_i)_+\). If \(x_0\) and \(x_1\) have opposite signs, at most \(\min(|x_0|,|x_1|)\) units of mass can travel directly across the sole cheaper edge. Using this entire amount is optimal: all other transport prices are \(1\), and every unit moved on this special edge saves \(1-t\), without affecting feasibility of a residual unit-cost complete-graph transportation plan. If their signs agree, the cheaper edge does not connect a positive source to a negative sink and cannot improve the transport cost. Therefore
\[
\|x\|_{\mathcal F(M,d_t)}=
\begin{cases}
m-(1-t)\min(|x_0|,|x_1|),&x_0x_1<0,\\
m,&x_0x_1\ge0.
\end{cases}
\]
This follows equally from finite Kantorovich duality, because direct shipping in this metric satisfies the triangle inequality.

Fix a sign chamber with \(p\ge1\) positive and \(q\ge1\) negative coordinates, where \(p+q=d+1\). Write the positive masses as \(mA_1,\ldots,mA_p\) and the absolute negative masses as \(mB_1,\ldots,mB_q\), with each set of proportions summing to one. On this sign chamber, the change of variables to \(m\), \(p-1\) independent positive proportions, and \(q-1\) independent negative proportions has Jacobian \(m^{d-1}\) in the chosen \(d\) independent zero-mass coordinates. One sees the unit Jacobian coefficient by eliminating any one of the \(d+1\) signed coordinates, then one terminal coordinate from each composition; the remaining incidence transformation is unimodular. Consequently, the volume of this chamber within the all-unit-distance ball \(P_1\) is
\[
\frac1{d(p-1)!(q-1)!}=\frac1{d!}\binom{d-1}{p-1}.
\]
Indeed, the two standard composition simplices have volumes \(1/(p-1)!\) and \(1/(q-1)!\), while integrating \(m^{d-1}\) from \(0\) to \(1\) contributes \(1/d\).

**2. A universal one-edge chamber multiplier.** On a chamber where the distinguished points have opposite signs, their mass proportions \(A\) and \(B\) are independent uniform-simplex coordinates in their respective positive and negative compositions. For \(U=\min(A,B)\) and \(0\le u\le1\), the exact survival law is
\[
\Pr(U>u)=(1-u)^{p-1}(1-u)^{q-1}=(1-u)^{d-1}.
\]
This remains valid for \(p=1\) or \(q=1\), interpreting the unique composition coordinate as identically one. For \(t<1\) the radial upper limit of \(m\) becomes \(1/[1-(1-t)U]\). Since volume is homogeneous of degree \(d\), the multiplier relative to the corresponding equilateral sign chamber is
\[
\mathbb E\left[\frac1{(1-(1-t)U)^d}\right]
=(d-1)\int_0^1\frac{(1-u)^{d-2}}{(1-(1-t)u)^d}\,du=\frac1t.
\]
The last identity is exact: the derivative of \(\bigl((1-u)/(1-(1-t)u)\bigr)^{d-1}\) is \(-(d-1)t(1-u)^{d-2}/(1-(1-t)u)^d\). At \(t=1\) the multiplier is also one, by direct evaluation.

Summing all sign chambers gives the equilateral primal volume
\[
\operatorname{vol}_d(P_1)
=\frac1{d!}\sum_{p=1}^{d}\binom{d+1}{p}\binom{d-1}{p-1}
=\frac1{d!}\binom{2d}{d}=:A_d,
\]
by Vandermonde's identity. Exactly two orientations of the distinguished edge have opposite signs. For each, choosing \(k\) further positive points among the remaining \(d-1\) yields \(\binom{d-1}{k}\) chambers, each of equilateral volume \(\binom{d-1}{k}/d!\). Thus their total equilateral volume is
\[
B_d=\frac2{d!}\sum_{k=0}^{d-1}\binom{d-1}{k}^2
=\frac2{d!}\binom{2d-2}{d-1}
=A_d\frac{d}{2d-1}.
\]
The other chambers are unchanged and the opposite-sign chambers expand by the factor \(1/t\); therefore
\[
\operatorname{vol}_d(P_t)=A_d+B_d(t^{-1}-1)
=A_d\frac{d+(d-1)t}{(2d-1)t}.
\]
No finite-dimensional numerical experiment is used in this identity.

**3. The polar volume from random order gaps.** For \(t=1\), the dual unit ball consists of pointed functions whose value range on \(M\) is at most one. Every ordering of all \(d+1\) labeled values specifies a simplex. With the value at point \(0\) anchored at zero, its \(d\) successive nonnegative gaps sum to at most one and form a unit-determinant coordinate system. Thus each of the \((d+1)!\) orderings contributes volume \(1/d!\), yielding \(\operatorname{vol}_d(Q_1)=d+1\).

Consider a point chosen uniformly in \(Q_1\), and let \(D=|f_0-f_1|\). The rank difference of the two distinguished labels equals \(k\in\{1,\ldots,d\}\) with probability \(2(d+1-k)/((d+1)d)\). Conditional on this difference, \(D\) is the sum of \(k\) consecutive gaps in a uniform \(d\)-simplex. With the leftover gap this is a \((d+1)\)-component Dirichlet vector having unit parameters, so \(D\) has the beta density with parameters \((k,d+1-k)\). The unconditional density at \(0<u<1\) is consequently
\[
\begin{aligned}
\rho_d(u)
&=\sum_{k=1}^{d}\frac{2(d+1-k)}{d(d+1)}
\frac{d!}{(k-1)!(d-k)!}u^{k-1}(1-u)^{d-k}\\
&=\frac2{d+1}\sum_{j=0}^{d-1}(d-j)\binom{d-1}{j}u^j(1-u)^{d-1-j}\\
&=\frac2{d+1}\bigl(d-(d-1)u\bigr),
\end{aligned}
\]
where the last equality is the expectation of a binomial random variable of size \(d-1\) and success probability \(u\). The only extra restriction defining \(Q_t\) inside \(Q_1\) is \(D\le t\). Therefore, multiplying \(\int_0^t\rho_d(u)\,du\) by \(\operatorname{vol}_d(Q_1)=d+1\) gives
\[
\operatorname{vol}_d(Q_t)=2dt-(d-1)t^2.
\]
This argument covers all real \(0<t\le1\), with no genericity assumption on the parameter.

**4. Maximization and the dimension trend.** Multiplying the two exact volumes cancels \(t^{-1}\), giving the boxed quadratic. Differentiation yields
\[
\mathcal M_d'(t)=\frac{\binom{2d}{d}}{d!(2d-1)}(d-1)
\bigl(d-2(d-1)t\bigr).
\]
For \(d\ge3\), the sole zero lies strictly inside \((0,1)\), and the sign on both sides proves strict uniqueness. Completing the square gives the exact relative gain. Finally,
\[
\lim_{d\to\infty}t_d^*=\frac12,\qquad
\lim_{d\to\infty}\left(\frac{\mathcal M_d(t_d^*)}{\mathcal M_d(1)}-1\right)=\frac18.
\]

## Verification

The accompanying `check_one_short.py` constructs the signed elementary-molecule vertices of \(P_t\) exactly and enumerates the vertices of \(Q_t\) by exact rational solutions of active Lipschitz constraints. A convex-hull triangulation determines the boundary simplex index sets; *all simplex determinant values and accumulated volumes are evaluated as exact rational numbers*. The script compares both independently reconstructed volumes with the formulas for \(d=2,3,4\) at \(t=1/2,2/3,3/4,1\), for twelve exact cases. It additionally checks the strict gain at the proposed optimizer against three other parameter values for dimensions \(3\) through \(23\). Run `python check_one_short.py` with the dependencies specified in `requirements.txt`; its final line is `ALL 12 EXACT RATIONAL POLYTOPE-VOLUME TESTS PASSED`. The triangulation library selects combinatorial simplices numerically, but their coordinates, determinants and final volume comparisons are exact rational quantities. The proof above, not the finite checker, establishes the theorem for every dimension and every permitted real parameter.

## Relationship to prior work

Alexander, Fradelizi, García-Lirola and Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces* (arXiv:1911.10642, first publicly posted 2019-11-24), study the finite-metric volume product; their Section 5.2, Claim 5 evaluates the equilateral endpoint, and Theorem 5.8 proves a global maximizer for at least four points cannot have the nonsimplicial equilateral ball. Those results do **not** give the present two separate volume profiles, the sharp dimension-dependent exceptional distance or the asymptotic \(1/8\) gain. In fact, the present theorem is a constructive quantitative refinement of their qualitative nonmaximality observation along one specified metric direction.

A separate publicly available facet classification, *Facet enumeration for equilateral metrics with independently shortened pairs*, determines how many dual extreme points arise when several disjoint pairs are shortened; the present one-pair family is a specialization of its **metric**, but its **facet counts** do not determine either Lebesgue volume or the product, and thus do not imply the formulas here. The work *Exact Hilbert distortion along a one-edge deformation of the four-point equilateral metric* treats the identical four-point deformation but computes distance to Hilbert space rather than a volume product. These are statement-and-implication comparisons, not claims of novelty from title differences alone.

## Limitations

The claim concerns one shortened unordered pair in an otherwise equilateral **real finite metric**, with \(0<t\le1\) and \(d\ge3\) for the interior maximizing parameter. It is not a global maximality theorem among all metrics with a fixed number of points and does not cover independent shortening of multiple pairs. The pseudometric limit \(t\downarrow0\) is excluded because two points merge. A volume-product maximum along this one-dimensional deformation need not maximize any other Banach-space invariant. Independent external verification has not been performed. Exhaustive checking of all historical literature, including unindexed alternative convex-geometric presentations, is not claimed.

## References

- M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1 (first posted 2019-11-24), https://arxiv.org/abs/1911.10642; inspected PDF, notably Section 5.2 and Claim 5.
- *Facet enumeration for equilateral metrics with independently shortened pairs*, publicly available mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-facet-enumeration-for-equilateral-metrics-with-independently-sho--3bd6d7048744/RESULT.md; inspected complete result and proof.
- *Exact Hilbert distortion along a one-edge deformation of the four-point equilateral metric*, publicly available mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-hilbert-distortion-along-a-one-edge-deformation-of-the-fou--f6a1d49d869f/RESULT.md; inspected complete result and proof.
