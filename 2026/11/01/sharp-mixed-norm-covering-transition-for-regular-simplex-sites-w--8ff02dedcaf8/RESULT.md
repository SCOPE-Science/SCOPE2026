# Sharp mixed-norm covering transition for regular simplex sites with an axial pair

## Finding

For each integer \(d\ge3\), put
\[
c_d=\sqrt{\frac{d-1}{2d}},\qquad p_d=\frac{2\log2}{\log(2d/(d-1))}\in(1,2).
\]
Let \(v_1,\ldots,v_d\) be the vertices of a regular \((d-1)\)-simplex with centroid \(g\), side length \(s>0\), and circumradius \(R=c_ds\). Consider the strictly convex, centrally symmetric body and its norm
\[
K_p=\{(x,t)\in\mathbb R^{d-1}\times\mathbb R:\|x\|_2^p+|t|^p\le1\},\qquad
N_p(x,t)=(\|x\|_2^p+|t|^p)^{1/p},\quad p>1.
\]
For \(0<a\le R\), put \(z_i=(v_i,0)\) for \(1\le i\le d\) and \(z_{d+1}=(g,a),\ z_{d+2}=(g,-a)\). The following is sharp over all positive simplex side lengths and axial separations:

**Universal covering phase:** for every \(p\ge p_d\), every \(s>0\), and every \(0<a\le R\),
\[
\bigcap_{i=1}^{d}(z_i-K_p)\ \subseteq\ (z_{d+1}-K_p)\cup(z_{d+2}-K_p).\tag{1}
\]
**Uncovered phase:** for every \(1<p<p_d\), there are explicit \(s\in(0,1)\) and \(a\in(0,R)\) for which the difference of the two sides of (1) has positive \(d\)-dimensional volume. For these configurations the Voronoi nerve (using the metric \(N_p\)) consists exactly of all nonempty subsets of the \(d+2\) sites which do **not** contain all \(d\) base indices.

More precisely, write \(\mathcal N\) for this nerve, \(U=\bigcup_{i=1}^{d+2}(z_i-K_p)\), and
\[
S_{\mathcal N}=\sum_{\varnothing\ne J\in\mathcal N}(-1)^{|J|+1}\operatorname{vol}_d\Bigl(\bigcap_{j\in J}(z_j-K_p)\Bigr).
\]
If \(E\) is the uncovered subset of the common intersection of the base translates, then
\[
\boxed{\operatorname{vol}_d(U)-S_{\mathcal N}=(-1)^{d+1}\operatorname{vol}_d(E)\ne0.}\tag{2}
\]
Thus the nerve-restricted inclusion–exclusion error alternates sign with the ambient dimension, even though the nerve has the same combinatorial description in every dimension.

## Assumptions and scope

All points and convex bodies lie in finite-dimensional Euclidean spaces. The body \(K_p\) has *one Euclidean radial block* of dimension \(d-1\) and *one axial coordinate*. The Voronoi cell of site \(z_i\) comprises all \(x\) satisfying \(N_p(x-z_i)\le N_p(x-z_j)\) for every site \(j\); its nerve indexes subfamilies with nonempty common Voronoi-cell intersection. Ties are allowed. Boundary-only covering is not misidentified with positive-volume coverage. No statement is made for arbitrary simplices, arbitrary smooth gauges, or arbitrary axial positions.

## Proof

**1. A sharp two-variable inequality.** For \(1<p\le2\) and \(u,v\ge0\),
\[
(u^p+v^p)^{2/p}\le u^2+v^2+(2^{2/p}-2)uv.\tag{3}
\]
Indeed set \(\alpha=2/p\in[1,2)\). By homogeneity and continuity it suffices to show for positive \(u,v\), with \(u^p=b e^t\), \(v^p=b e^{-t}\), that
\[
(2\cosh t)^\alpha-2\cosh(\alpha t)\le2^\alpha-2.
\]
The left side is even. Its derivative for \(t>0\) equals
\[
2\alpha\big[(2\cosh t)^{\alpha-1}\sinh t-\sinh(\alpha t)\big]\le0.
\]
To prove the sign, \(h(\xi)=\log\sinh(\xi t)\) is concave in \(\xi>0\). Interpolation between \(\xi=1\) and \(\xi=2\), using \(\sinh(2t)=2\sinh t\cosh t\), gives \(\sinh(\alpha t)\ge\sinh t(2\cosh t)^{\alpha-1}\). Multiplication by \(b^\alpha=uv\) proves (3), including zero endpoints by continuity.

**2. The regular-simplex radial bound.** For each \(q\in\mathbb R^{d-1}\), write \(r=\|q-g\|_2\). Since a regular \((d-1)\)-simplex of circumradius \(R\) has inradius \(R/(d-1)\) about its centroid, some vertex satisfies \(\langle q-g,v_i-g\rangle\le-Rr/(d-1)\). Consequently,
\[
\max_i\|q-v_i\|_2^2\ge r^2+R^2+\frac{2rR}{d-1}.\tag{4}
\]
For \(p_d\le p\le2\), the defining identity \(2^{2/p_d}-2=2/(d-1)\), (3), and (4) imply
\[
\max_i\|q-v_i\|_2^p\ge r^p+R^p.\tag{5}
\]
For \(p\ge2\), (4) and the inequality \((r^2+R^2)^{p/2}\ge r^p+R^p\) again give (5). This proves (5) for every \(p\ge p_d\).

**3. Universal coverage.** Take \(x=(q,t)\in\bigcap_{i=1}^d(z_i-K_p)\), so \(\max_i\|q-v_i\|_2^p+|t|^p\le1\). The nearest of the two axial sites has \(p\)-th power distance \(r^p+||t|-a|^p\). If \(|t|\ge a\), this is at most \(r^p+|t|^p\), which by (5) is at most one. If \(|t|<a\le R\), it is at most \(r^p+R^p\le\max_i\|q-v_i\|_2^p\le1\). Therefore (1) holds for every permitted scale and axial separation.

**4. Constructive sharpness, including positive volume.** Fix \(1<p<p_d\) and define
\[
q_*=(c_d2^{1/p})^{-1}<1,\quad
\lambda_d=\frac{\sqrt{d(d-2)}}{d-1}<1,\quad
\varepsilon=\frac14\min\{1-q_*,1-\lambda_d\},
\]
\[
s=1-\varepsilon,\quad R=c_ds,\quad a=Rs=c_ds^2.
\]
The circumradius of any facet simplex is \(r_f=\lambda_d R\), and \(r_f<a<R\) follows from \(s>\lambda_d\). The strict inequalities \(s>(1+q_*)/2\ge\sqrt{q_*}\) show
\[
h=(R^p+a^p)^{1/p}=c_d(s^p+s^{2p})^{1/p}>c_d(2q_*^p)^{1/p}=1.
\]
At \(x_0=(v_1,0)\), every base-site distance is at most \(s<1\), whereas both apex-site distances equal \(h>1\). As \(N_p(w)\le C_p\|w\|_2\) for \(C_p=2^{1/p-1/2}\), the open Euclidean ball of radius
\[
\delta=\frac{\min\{1-s,h-1\}}{C_p}>0
\]
about \(x_0\) lies inside \(E\). Hence \(\operatorname{vol}_d(E)\ge\pi^{d/2}\delta^d/\Gamma(d/2+1)>0\).

**5. Exact Voronoi nerve.** If a point \((q,t)\) belongs simultaneously to all \(d\) base Voronoi cells, the base-site distances are equal. Their identical vertical terms force \(\|q-v_i\|_2\) to be constant in \(i\), and affine independence forces \(q=g\). But when \(0<a<R\), the nearer axial site then has distance \(||t|-a|\), strictly less than the base distance \((R^p+|t|^p)^{1/p}\). Thus no face containing all base indices belongs to the nerve.

Conversely, delete one base index \(i\). Let \(m_i\) be the centroid of the other \(d-1\) vertices. All remaining base vertices are equidistant along the segment \([m_i,g]\), and the excluded vertex is strictly farther before \(g\). At \(m_i\), their common distance is \(r_f<a\), hence they are closer than the two axial sites; at \(g\), their distance is \(R>a\), hence the axial sites are closer. By continuity a point on the open segment makes all \(d-1\) retained base sites and both axial sites tie for the smallest distance. This yields a nerve face with \(d+1\) vertices for every omitted base index. Since a nerve is downward closed, its faces are exactly all nonempty subsets omitting at least one base index.

**6. Signed-volume identity.** Evaluate the nerve inclusion–exclusion indicator at an arbitrary \(x\), writing \(J_x=\{i:x\in z_i-K_p\}\). The complete nonempty simplex on \(J_x\) has alternating sum \(1\) if \(J_x\ne\varnothing\) and zero otherwise. Nerve omissions are precisely subsets containing the full base block. If \(J_x\) includes \(k\ge1\) axial indices, the omitted alternating sum vanishes by \((1-1)^k=0\). If \(J_x\) contains all bases and no axial index, the omitted sum is \((-1)^{d+1}\). Hence the nerve sum equals \(\mathbf1_U(x)-(-1)^{d+1}\mathbf1_E(x)\) pointwise. All sets are bounded Borel sets, so integration proves (2).

## Verification

The supplied standalone standard-library script `verify_simplex_phase.py` performs 456 deterministic finite checks for the strict below-threshold parameters and the scalar inequalities, for dimensions \(3,4,5,8,15,30\). Execution output: `PASS 456 deterministic mathematical parameter checks (not a universal proof)`. The infinite statements are proved in Steps 1–6; finite checks do not establish the general theorem. The appended research envelope separately records the literature comparisons and self-review.

## Relationship to prior work

Shelley and Tartakovsky's October 2026 work establishes the general Voronoi-nerve inclusion–exclusion question and gives a smooth strictly convex five-site counterexample in three dimensions, together with a higher-dimensional embedding construction. That existence counterexample and the nerve framework are prior work. The present result instead determines the sharp **dimension-dependent mixed-norm exponent for a natural symmetric simplex-plus-axial-pair family**, proves universal coverage on one side, constructs a positive-measure failure on the other, and identifies the sign of the resulting nerve error in every dimension. It does not strengthen the original general existence theorem to arbitrary gauges or arbitrary site configurations.

## Limitations

The sharp threshold is universal only within the defined regular-simplex/axial-pair family. The uncovered-region volume is bounded below, not evaluated exactly. Historical priority among unindexed \(\ell_p\) Voronoi or ball-intersection literature remains uncertain; no independent audit has been performed.

## References

1. A. Shelley and D. Tartakovsky, *Union of Translates of a Convex Body*, arXiv:2610.25841, first public 2026-10-19; in particular its Voronoi-nerve framework and Section 5 counterexample.
2. Classical regular-simplex inradius and circumradius identities (used explicitly in Step 2); these identities are standard and are not claimed as new.
