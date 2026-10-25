# Two geometric transition scales for Ehrhart-equivalent enriched two-level poset polytopes

## Finding

Let \(P_{p,q}=A_p\oplus A_q\) be the ordinal sum of two antichains, with integers \(p,q\ge2\). In the standard coordinate Euclidean metric, write \(K^{\mathrm O}_{p,q}\) and \(K^{\mathrm C}_{p,q}\) for its enriched order and enriched chain polytopes. The following results concern **one pair of canonical, Ehrhart-equivalent convex bodies**.

**Exact width defect.** For every \((u,v)\in\mathbb R^p\times\mathbb R^q\), put \(A=\|v\|_1\), \(B=\|u\|_1\), \(T=\sum_{j=1}^q v_j\). If \(w_K(z)=h_K(z)+h_K(-z)\) denotes directional Euclidean width at a not necessarily unit direction, then
\[
 w_{K^{\mathrm O}_{p,q}}(u,v)-w_{K^{\mathrm C}_{p,q}}(u,v)
 =\bigl(|T|-|A-B|\bigr)_+\ge0.
\]
Here \(x_+=\max(x,0)\). This is a pointwise comparison of widths, **not** an inclusion between the original polytopes.

**Sharp stochastic balance window.** Let \(G=(G_1,\ldots,G_p)\) and \(H=(H_1,\ldots,H_q)\) be independent vectors of independent standard normals. Let \(\Delta_{p,q}=w_{K^{\mathrm O}_{p,q}}(G,H)-w_{K^{\mathrm C}_{p,q}}(G,H)\), and set \(\mu=\sqrt{2/\pi}\) and \(\sigma^2=1-2/\pi\). For integer sequences with \(q\to\infty\) and \((p-q)/\sqrt q\to\tau\in\mathbb R\),
\[
 \frac{\Delta_{p,q}}{\sqrt q}\ \Longrightarrow\
 \left(|Z|-|\sqrt2\sigma V-\mu\tau|\right)_+,
\]
where \(Z,V\) are independent standard normals. First moments converge as well. In the exactly balanced case \(p=q\), putting \(a=\sqrt2\sigma\), the strict-width advantage has limiting probability and mean
\[
 \Pr(\Delta_{q,q}>0)\longrightarrow 1-\frac2\pi\arctan a,
 \qquad
 \frac{\mathbb E\Delta_{q,q}}{\sqrt q}
 \longrightarrow \sqrt{\frac2\pi}\bigl(\sqrt{1+a^2}-a\bigr).
\]
Both constants are strictly positive. If instead \(p/q\to\alpha\in(0,\infty)\setminus\{1\}\), then \(\Pr(\Delta_{p,q}>0)\to0\) and \(\mathbb E\Delta_{p,q}/\sqrt q\to0\).

**Distinct enclosing-sphere transition.** The enriched order polytope has the unique minimum enclosing Euclidean ball center
\[
 c_{p,q}=\left(0_p,t_{p,q}1_q\right),
 \qquad t_{p,q}=\min\left(\frac{p}{4q},1\right),
\]
and squared radius
\[
 R_{\mathrm O}(p,q)^2=
 \begin{cases}
 q+\dfrac p2+\dfrac{p^2}{16q},& p\le4q,\\[4pt]
 p,& p\ge4q.
 \end{cases}
\]
At \(p\le4q\), precisely \(2^p+1\) vertices contact that sphere; at \(p>4q\), precisely \(2^p\) vertices do. The enriched chain polytope has radius \(R_{\mathrm C}(p,q)=\sqrt{\max(p,q)}\). Therefore \(R_{\mathrm O}\ge R_{\mathrm C}\), with equality **exactly when** \(p\ge4q\). This \(4{:}1\) threshold differs from the \(1{:}1\) Gaussian-width balance window.

**Tangential metric identity.** All \(q+2pq\) facets of the enriched order polytope touch one maximal Euclidean ball, with unique center \(\bigl(0_p,\frac{3-\sqrt5}{2}1_q\bigr)\) and radius
\[
 r_{\mathrm O}=\frac{\sqrt5-1}{2}.
\]
Writing \(n=p+q\), its Euclidean boundary measure \(S\) and volume \(V\) satisfy
\[
 V(K^{\mathrm O}_{p,q})=V(K^{\mathrm C}_{p,q})
 =\frac{2^{p+q}p!q!}{(p+q)!},
 \qquad \frac{S(K^{\mathrm O}_{p,q})}{V(K^{\mathrm O}_{p,q})}
 =\frac{n(1+\sqrt5)}2.
\]
The enriched chain polytope has centered inradius \(r_{\mathrm C}=1/\sqrt2\). The shared volume is background from enriched-poset Ehrhart equivalence; the Euclidean width/radius/contact statements above are the contribution assessed here.

## Assumptions and scope

The poset has \(p\) mutually incomparable lower elements, \(q\) mutually incomparable upper elements, and every lower element is below every upper element. Coordinates are orthonormal and ordered as \(\mathbb R^p\times\mathbb R^q\). Width uses the unnormalized linear functional; the Gaussian claim is thus about Gaussian widths, not unit-sphere widths. The positive-part and all limits use the stated normalizations. The asymptotic parameter \(\tau\) is fixed, and no growing \(\tau\) crossover assertion is made. Standard Euclidean surface area means the \((n-1)\)-dimensional Hausdorff measure of the entire boundary.

By the defining signed-filter and signed-antichain constructions,
\[
 K^{\mathrm O}_{p,q}=\operatorname{conv}\left(
 \{0_p\}\times[-1,1]^q,\ [-1,1]^p\times\{1_q\}\right),
 \qquad
 K^{\mathrm C}_{p,q}=\operatorname{conv}\left(
 [-1,1]^p\times\{0_q\},\ {0_p}\times[-1,1]^q\right).
\]
The first cube's all-positive corner is **not** a vertex of the order polytope; all other cube corners are vertices. The enriched order polytope has \(2^p+2^q-1\) vertices, and its facets are exactly
\[
 y_j\le1,\qquad 2x_i-y_j\le1,\qquad -2x_i-y_j\le1
 \quad (1\le i\le p,\ 1\le j\le q).
\]
These affine inequalities specialize the previously published general facet description. No novelty is claimed for the general enriched-poset construction, facet-description theorem, or transfer-map/Ehrhart theorem.

## Proof

**1. Convex hulls and facet metric.** For \(K^{\mathrm O}_{p,q}\), the displayed halfspaces are equivalent to \(y_j\le1\) and \(y_j\ge2\|x\|_\infty-1\) for every \(j\). They force \(\lambda=\|x\|_\infty\in[0,1]\). If \(0<\lambda<1\), write
\[
 (x,y)=\lambda\,(x/\lambda,1_q)
 +(1-\lambda)\,(0_p,(y-\lambda1_q)/(1-\lambda)).
\]
Both bracketed points belong to the indicated cubes; the endpoints \(\lambda\in\{0,1\}\) follow directly. This proves the halfspace and cube-hull descriptions agree. Each displayed inequality is a genuine facet (vary the other coordinates strictly inside its induced section). The first \(q\) normals have length one; the other \(2pq\) have length \(\sqrt5\). The facet count and normals also follow from the published enriched-order facet theorem.

For any inscribed ball of center \((x,y)\) and radius \(r\), the facet inequalities require
\[
 y_j\le1-r,
 \qquad y_j\ge-1+\sqrt5r+2|x_i|\quad\text{for every }i,j.
\]
Consequently \((1+\sqrt5)r\le2\). Equality forces \(x=0_p\) and every \(y_j=(3-\sqrt5)/2\). That point attains equality at every facet, proving the asserted unique incenter and tangentiality. Since every facet has signed distance \(r_{\mathrm O}\) from the same interior point, the pyramidal divergence formula gives \(nV=r_{\mathrm O}S\). Independently, integrating the sections over \(x\) gives
\[
 V=\int_{[-1,1]^p}\bigl(2(1-\|x\|_\infty)\bigr)^q\,dx
 =2^{p+q}p\int_0^1s^{p-1}(1-s)^qds
 =\frac{2^{p+q}p!q!}{(p+q)!}.
\]
The chain polytope's support function is \(\max(\|u\|_1,\|v\|_1)\). Its centered inradius is the minimum of this support over Euclidean unit vectors, which equals \(1/\sqrt2\): the lower bound follows from \(\ell_1\ge\ell_2\), and equality is realized by one coordinate of magnitude \(1/\sqrt2\) in each block. Its circumradius is \(\max(\sqrt p,\sqrt q)\) because it is centrally symmetric and its furthest cube corners have exactly those norms. Its volume equality with the order member is also a previously established Ehrhart consequence.

**2. Outer Euclidean ball and contact classification.** Every minimum enclosing ball in Euclidean space has a unique center: the squared-distance midpoint identity strictly improves the maximum squared radius if distinct centers had the same minimal radius. The coordinate sign changes in the first block and permutations in the second block therefore force the center to be \((0_p,t1_q)\). In fact, all coordinate permutations in each block preserve the body; the first-block reflections force its zero component. The furthest squared distances to the two defining cubes are, for \(t\ge0\),
\[
 q(1+t)^2 \quad\text{and}\quad p+q(1-t)^2.
\]
For \(t<0\), moving \(t\) toward zero improves the second expression and cannot increase the optimal maximum relative to \(t=0\). On \([0,1]\) the two expressions respectively increase and decrease, meeting at \(t=p/(4q)\); above one they both increase. This proves the exact minimizing \(t\) and radius. At \(t>0\), the first cube has exactly one farthest corner, \(-1_q\), while the second cube has all \(2^p\) corners equally far. The first corner contacts the optimal sphere if and only if \(p\le4q\), proving the contact counts. Subtracting \(\max(p,q)\) from the piecewise squared radius proves the outer-radius comparison; when \(q\le p\le4q\), the difference is \((p-4q)^2/(16q)\).

**3. Exact directional support/width comparison.** With \(A=\|v\|_1\), \(B=\|u\|_1\), \(T=\sum v_j\), support optimization over the two cubes gives
\[
 h_{K^{\mathrm O}}(u,v)=\max(A,B+T),
 \qquad h_{K^{\mathrm C}}(u,v)=\max(A,B).
\]
Hence \(w_{K^{\mathrm O}}=\max(A,B+T)+\max(A,B-T)\), while \(w_{K^{\mathrm C}}=2\max(A,B)\). The elementary identity
\[
 \max(A,B+T)+\max(A,B-T)
 =A+B+\max(|A-B|,|T|)
\]
proves exactly \(w_{K^{\mathrm O}}-w_{K^{\mathrm C}}=(|T|-|A-B|)_+\). This is a deterministic identity for all real directions, including ties and zero components.

**4. The Gaussian critical window and strict contact probability.** Define \(A_q=\sum_{j=1}^q|H_j|\), \(B_p=\sum_{i=1}^p|G_i|\), and \(S_q=\sum_{j=1}^qH_j\). Then \(\Delta_{p,q}=(|S_q|-|A_q-B_p|)_+\) exactly. The random vectors \((|H_j|-\mu,H_j)\) have covariance matrix \(\operatorname{diag}(\sigma^2,1)\), because \(\mathbb E[|H_j|H_j]=0\). The two-dimensional central limit theorem yields independent Gaussian limits of the two coordinates, and the independent first block adds another independent Gaussian. Under \((p-q)/\sqrt q\to\tau\), we obtain
\[
 (S_q/\sqrt q,(A_q-B_p)/\sqrt q)
 \Longrightarrow(Z,\sigma Z_1-\sigma Z_2-\mu\tau).
\]
The continuous-mapping theorem gives the displayed positive-part limit. Since \(0\le\Delta_{p,q}\le|S_q|\) and \(\mathbb E(S_q/\sqrt q)^2=1\), the rescaled defects are uniformly integrable, proving first-moment convergence. For \(p/q\to\alpha\ne1\), the law of large numbers gives \(|A_q-B_p|/q\to\mu|1-\alpha|\), whereas \(S_q/q\to0\), so the probability of a strictly positive defect tends to zero. The same uniform-integrability bound proves the stated mean limit.

For \(p=q\), \(Z_1-Z_2\) is \(\sqrt2\) times an independent standard normal \(V\). Boundaries \(|Z|=a|V|\) have probability zero. Rotational symmetry in the \((Z,V)\)-plane gives
\[
 \Pr(|Z|>a|V|)=1-\frac2\pi\arctan a.
\]
Using polar coordinates \(Z=R\cos\theta\), \(V=R\sin\theta\), \(\mathbb E R=\sqrt{\pi/2}\), and integrating the positive part over a quadrant yields
\[
 \mathbb E(|Z|-a|V|)_+
 =\sqrt{2/\pi}\,(\sqrt{1+a^2}-a).
\]
These give the strict-advantage probability and sharp mean coefficient.

## Verification

The included standalone script `verify_enriched_metrics.py` constructs both cube strata, checks each order-polytope facet and its affine rank, recomputes convex-hull Euclidean volume and surface area, compares analytic and optimized enclosing spheres, and directly evaluates support functions in 518 deterministic pseudorandom directions. It also independently checks the exact Gaussian critical-window constants and selected Monte Carlo asymptotic diagnostics. Its completed run reported `FINITE_CHECKS_OK 14 518`, `GAUSSIAN_DIAGNOSTICS_OK`, `CRITICAL_GAP_CONSTANTS_OK`, and `VERIFY_OK`. The finite checks include several small parameter values outside the theorem's \(p,q\ge2\) range as independent boundary diagnostics; they do not enlarge the accepted claim. All unbounded-dimensional assertions follow from the written analysis, not from simulation.

## Relationship to prior work

Ohsugi and Tsuchiya introduced enriched order polytopes and supplied general signed-filter vertices and irredundant facet inequalities. Okada and Tsuchiya subsequently established an explicit enriched transfer map and unimodular triangulations, including the shared Ehrhart polynomials. Neither primary work supplies this pair's directional width difference, Gaussian critical-window law, Euclidean golden-ratio tangency, or \(4{:}1\) circumsphere contact transition. The general half-normal central limit theorem, support-function calculus, and divergence formula are known tools and are not claimed as innovations.

The corresponding two-level **unenriched** order polytope has a different mean-width formula and balance crossover; substituting that formula does not yield the present signed-enriched width defect. Previously studied Gaussian exposure probabilities for the **enriched chain** member depend on the competition \(\sum|G_i|\gtrless\sum|H_j|\), but do not give the signed common-coordinate correction \(|\sum H_j|\), the pointwise width comparison, or the present Euclidean radius profile.

## Limitations

These are standard-coordinate, unnormalized Euclidean metrics; the Gaussian-width limit is not stated for uniformly spherical directions. The two-level complete comparability is essential for the exact two-cube representation; nothing is asserted for arbitrary posets, arbitrary embeddings, or higher levels. The \(4{:}1\) sphere statement is a sharp sufficient-and-necessary threshold **for this family only**. No universal originality or independence certificate is asserted; equivalent formulations in general two-cube convex-hull or Gaussian-width literature remain possible. Verification of finitely many instances is not proof of the infinite-family claims. Independent expert mathematical validation has not been performed.

## References

1. S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271 (first public version, 27 March 2020); Annals of Combinatorics 28 (2024), 257–282. https://arxiv.org/abs/2003.12271 . Primary subject classification 52B12, explicitly declared in the preprint.
2. H. Ohsugi and A. Tsuchiya, *Enriched order polytopes and enriched Hibi rings*, arXiv:1903.00909 (first public version, 3 March 2019); European Journal of Mathematics 7 (2021), 48–68, DOI:10.1007/s40879-020-00403-2. https://arxiv.org/abs/1903.00909 .
3. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI:10.1007/BF02187680.
