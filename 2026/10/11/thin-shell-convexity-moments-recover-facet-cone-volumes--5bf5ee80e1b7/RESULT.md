# Thin-shell convexity moments recover facet cone volumes

## Finding

Let \(d\ge 2\), let \(K\subset\mathbb R^d\) be any compact convex body with \(0\in\operatorname{int}K\), and let \(S_t=K\setminus\operatorname{int}(tK)\), for \(0<t<1\). For an integer \(q\ge 2\), draw \(q\) independent, volume-uniform points in \(S_t\). Let \(B_q(S_t)\) be the probability that **their entire convex hull** lies in \(S_t\). Thus \(B_2\) is the Beer index; \(B_{k+1}\) is the familiar \(k\)-index when \(1\le k\le d\), and the same probability makes sense for all larger \(q\).

For every facet \(F\) (a full \((d-1)\)-dimensional exposed face) of \(K\), define its normalized cone-volume weight
\[
p_F=\frac{\operatorname{Vol}_d(\operatorname{conv}(\{0\}\cup F))}{\operatorname{Vol}_d(K)}.
\]
The collection of facets is at most countable and \(\sum_Fp_F\le1\). **For every fixed integer \(q\ge2\), the exact thin-shell limit is**
\[
\boxed{L_q(K):=\lim_{t\uparrow1} B_q(S_t)=\sum_{F\ \mathrm{facet\ of}\ K}p_F^{\,q}.}
\]
In particular, the limiting Beer index is strictly positive **if and only if** the body has a facet; it vanishes for every facetless convex body, whether smooth or not.

These limits encode more than a single probability. The full sequence \((L_q(K))_{q\ge2}\) uniquely determines the **multiset of positive facet cone-volume weights, including multiplicities**, even when the body has countably many facets. Indeed the finite measure
\[
\eta_K=\sum_Fp_F^2\,\delta_{p_F}\quad\text{on }[0,1]
\]
has moments \(\int u^j\,d\eta_K(u)=L_{j+2}(K)\) for every integer \(j\ge0\), and its atoms reveal the weights and their multiplicities. No facet normal or full geometry is recovered from this sequence alone.

For a \(d\)-simplex containing the origin with positive barycentric coordinates \(\lambda_0,\dots,\lambda_d\), the result specializes to \(L_q=\sum_{i=0}^d\lambda_i^q\); consequently
\[
\boxed{(d+1)^{1-q}\le L_q<1,}
\]
with equality in the lower bound exactly at the centroid and sharp unattained upper supremum \(1\) as the anchor approaches a vertex.

For a \(d\)-parallelotope affinely represented by \([0,1]^d\), with the anchor at \((\alpha_1,\dots,\alpha_d)\in(0,1)^d\), one similarly obtains
\[
L_q=d^{-q}\sum_{i=1}^d\bigl(\alpha_i^q+(1-\alpha_i)^q\bigr),\qquad
\boxed{(2d)^{1-q}\le L_q<d^{1-q},}
\]
where the lower equality holds exactly at the center and the upper bound is the sharp unattained supremum.

## Assumptions and scope

All volume measures are \(d\)-dimensional Lebesgue measures, and the points are independent. The inner homothet \(tK\) and the cone weights use the **same fixed interior origin**; the result is not invariant under changing this anchor while keeping the shell fixed. The shell includes its inner boundary, a measure-zero convention immaterial to the sampling but useful for the containment event. Each \(q\) is fixed before taking \(t\uparrow1\). A facet is a supporting-hyperplane intersection with positive \((d-1)\)-dimensional measure. No polyhedral, differentiability, or symmetry assumption is imposed on \(K\).

## Proof

**1. Exact sampling decomposition.** Every nonzero \(x\in K\) has a unique radial representation \(x=ry\) with \(y\in\partial K\), \(0<r\le1\). Let \(\mu_K\) be the radial image on \(\partial K\) of volume-uniform measure in \(K\). In radial boundary coordinates, the volume element is
\[
r^{d-1}\langle y,\nu(y)\rangle\,dr\,d\mathcal H^{d-1}(y)
\]
at almost every boundary point, where \(\nu(y)\) is the outer unit normal. Accordingly, \(\mu_K\) has density \(\langle y,\nu(y)\rangle/(d\operatorname{Vol}_d(K))\) with respect to boundary surface area; because the anchor is interior, this density is positive and bounded. If \(Y\sim\mu_K\) and \(U\sim\operatorname{Uniform}[0,1]\) are independent, then
\[
R_t=\bigl(t^d+(1-t^d)U\bigr)^{1/d},\qquad X_t=R_tY
\]
is exactly volume-uniform on \(S_t\), and \(R_t\to1\) almost surely. This couples all shell thicknesses on a single probability space. For any facet \(F\), radial integration over its cone gives \(\mu_K(F)=p_F\). Distinct facet relative interiors are disjoint, so the facets are countable and their weights sum to at most one.

**2. Boundary averages.** Draw independent \(Y_1,\dots,Y_q\sim\mu_K\) and independent radial factors \(R_{t,i}\). Write \(\overline Y=q^{-1}\sum_iY_i\). Convexity ensures \(\overline Y\in K\). If \(\overline Y\in\operatorname{int}K\), then the coupled average \(q^{-1}\sum_iR_{t,i}Y_i\) also lies in \(\operatorname{int}(tK)\) for all sufficiently large \(t<1\): choose a small Euclidean ball about \(\overline Y\) inside \(K\), and use \(R_{t,i}Y_i\to Y_i\) and \(tK\to K\). The convex hull of the shell samples therefore enters the forbidden inner interior, so its containment indicator eventually vanishes.

If \(\overline Y\in\partial K\), choose a supporting hyperplane at \(\overline Y\). Since all \(Y_i\in K\), and their average attains equality in its support inequality, **every** \(Y_i\) belongs to that same exposed face. Conversely, points all in an exposed face have boundary average.

To evaluate the probability of this event, use the classical almost-everywhere uniqueness of the supporting hyperplane of a convex hypersurface. At \(\mu_K\)-almost every \(Y_1\), the outer normal \(\nu(Y_1)\) is unique. Therefore, conditional on such a \(Y_1\), the other points can have boundary average only if each belongs to the single exposed face \(F(Y_1)=K\cap\{x:\langle x,\nu(Y_1)\rangle=h_K(\nu(Y_1))\}\). If this face has zero surface measure it has \(\mu_K\)-measure zero. If it has positive surface measure, it is a facet and \(Y_1\) lies in its relative interior except on a \(\mu_K\)-null subset. Hence, up to a null event, **boundary average is equivalent to all \(q\) points lying in one common facet**, whose probability is
\[
\mathbb P(\overline Y\in\partial K)=\sum_F\mu_K(F)^q=\sum_Fp_F^q.
\]

**3. Exact survival on a common facet.** For a facet \(F\) with supporting normal \(u_F\) and positive support number \(h_F\), every sample whose radial endpoint is in \(F\) satisfies \(\langle u_F,R_{t,i}Y_i\rangle=R_{t,i}h_F\ge th_F\). Their entire convex hull lies in that half-space, whereas every point of \(\operatorname{int}(tK)\) satisfies \(\langle u_F,x\rangle<t h_F\). Thus all common-facet tuples are contained in \(S_t\) for **every** \(t\). Together with step 2, this gives almost-sure convergence of the containment indicator to that of the common-facet event. Dominated convergence proves the claimed formula for each fixed \(q\).

**4. Recovering the weights.** The nonnegative numbers \(p_F\) sum to at most one. Consequently \(\eta_K=\sum_Fp_F^2\delta_{p_F}\) is finite, and its complete nonnegative integer moment sequence is exactly \((L_{j+2})_{j\ge0}\). Polynomials are dense in \(C([0,1])\), so the moments uniquely determine the finite Borel measure. At each \(w>0\), its mass is \(w^2\) times the (finite) number of facets of weight \(w\), determining the multiset. The zero-weight continuous part of cone-volume measure leaves no atom in \(\eta_K\), as expected. Moreover this recovery is constructive at the level of exact limits: if any weights exist, their largest value satisfies \(p_{\max}=\lim_{q\to\infty}L_q^{1/q}\), and the multiplicity of that value is \(m_{\max}=\lim_{q\to\infty} L_q/p_{\max}^{\,q}\). Subtract \(m_{\max}p_{\max}^{\,q}\) from every moment and repeat on the remaining weights. Summability ensures every nonempty remainder has a largest weight; the multiplicity limit follows by dominated convergence after division by the largest weight, since the remaining squared normalized weights are summable. The all-zero sequence characterizes facetless bodies.

**5. Sharp model families.** In a simplex, pyramidal decomposition from the origin identifies \(p_F\) with the corresponding positive barycentric coordinate. Jensen's strict convexity for \(q>1\) gives the stated minimum; concentration of barycentric mass at one vertex approaches the supremum. For a parallelotope, each coordinate pair of opposite facets has normalized pyramid volumes \(\alpha_i/d\) and \((1-\alpha_i)/d\). The strict convexity of \(a^q+(1-a)^q\) on \((0,1)\) gives its unique minimum at \(a=1/2\) and unattained endpoint supremum; summing yields the bounds.

## Verification

The proof is analytic for all convex bodies and all fixed integers \(q\ge2\). A standalone standard-library script, `verify_shell_moments.py`, samples exact radial factorizations of planar homothetic polygon shells and independently clips segments against their inner polygons. It checks equal-facet visibility, compares empirical finite-thickness visibility with the predicted cone-moment limit, and reports `VERIFY_OK` on its deterministic examples. These finite Monte Carlo checks are diagnostics only; they neither certify arbitrary dimensions nor establish the limits, which follow from the proof above. Example limits: for a centered square \(L_2=1/4\), and for a centroid-anchored triangle \(L_2=1/3\).

## Relationship to prior work

Balko, Jelínek, Valtr, and Walczak (2014 preprint, subsequently revised) define the Beer index and the higher \(k\)-indices and study inequalities comparing them to convexity ratio. This supplies the natural statistic, **not** the facet cone-moment limit. Henk and Linke (2013 preprint) study cone-volume measures, including the standard facet-pyramid weights, without relating them to homothetic-shell visibility. Beer's earlier paper (1974) concerns the index under *outer parallel-body thickening*, which is a different geometric degeneration from removing an inner homothet.

For a Euclidean ball the present limit is zero because the ball has no facets; the theorem does not compute the finite-thickness probability in that special case. The principal result instead characterizes arbitrary convex bodies, the complete fixed-order convex-hull visibility spectrum, and inversion of facet cone-volume weights. It does **not** claim that Beer indices, cone-volume measures, or standard moment uniqueness were discovered here.

## Limitations

The limit does not provide a convergence rate, a finite-thickness closed form, uniformity in \(q\), the locations or normals of facets, or reconstruction of the full convex body. Bodies with no facets all have the same zero limiting spectrum; the continuous component of the cone-volume measure is not determined. The simplex and parallelotope sharpness statements concern the choice of *interior anchor* for a fixed combinatorial family, not optimization over all convex bodies. Historical originality remains provisional: equivalent unpublished or poorly indexed treatments may exist, and no independent assessment has been performed.

## References

1. M. Balko, V. Jelínek, P. Valtr, B. Walczak, *On the Beer index of convexity and its variants*, arXiv:1412.1769v1, first public 2014-12-04. https://arxiv.org/abs/1412.1769
2. M. Henk, E. Linke, *Cone-volume measures of polytopes*, arXiv:1305.5335v1, first public 2013-05-23. https://arxiv.org/abs/1305.5335
3. G. A. Beer, *The index of convexity and parallel bodies*, Pacific Journal of Mathematics **53** (1974), 337–345. https://msp.org/pjm/1974/53-2/pjm-v53-n2-p03-s.pdf
