# Infinite near-support separation rank of polytope section profiles

## Finding

**Theorem.** Let \(d\ge2\) and let \(P\subset\mathbb R^d\) be a full-dimensional convex polytope with \(0\in\operatorname{int}P\). For a unit vector \(\theta\), write
\[
 h_P(\theta)=\max_{x\in P}\langle x,\theta\rangle,\qquad
 A_{P,\theta}(t)=\mathcal H^{d-1}(P\cap\{x:\langle x,\theta\rangle=t\}).
\]
Fix **any** edge \(E\) of \(P\), any unit vector \(\theta_0\) in the relative interior of the outer normal cone of \(E\), any neighborhood \(W\) of \(\theta_0\) on the unit sphere, and any \(\varepsilon>0\). There exist a nonempty open interval \(J\subset\mathbb R\) and infinitely many directions \(\theta_k\in W\) such that
\[
 J\subset(h_P(\theta_k)-\varepsilon,h_P(\theta_k))\quad(k=1,2,\ldots)
\]
and the functions \(A_{P,\theta_k}|_J\) are linearly independent (every finite subfamily is independent).

Consequently there are **no** positive \(\varepsilon\), finite integer \(N\), and arbitrary real-valued functions \(a_j\) on the sphere and \(b_j\) on their needed real arguments for which
\[
 A_{P,\theta}(t)=\sum_{j=1}^N a_j(\theta)b_j(t)
 \quad\text{for every unit }\theta\text{ and every }h_P(\theta)-\varepsilon<t<h_P(\theta).
\]
No continuity, measurability, or differentiability of the proposed factors is assumed.

## Assumptions and scope

The dimension is an integer at least two. The polytope has nonempty interior; the condition that the origin is interior aligns the support-function convention with near-boundary separability and ensures each vertex is nonzero. Every convex polytope has an edge. The normal cone \(N_P(E)\) means the set of linear functionals maximized at every point of \(E\); a direction in its relative interior exposes exactly \(E\). The interval \(J\) is permitted to depend on \(P,E,\theta_0,W,\varepsilon\), but it is common to the infinitely many displayed profiles. The conclusion concerns exact finite separation rank; it does not assert a lower bound for approximation by finite-rank families.

## Proof

**1. A section-spline identity, with normalization.** Choose a triangulation \(\mathcal T\) of \(P\) into nonoverlapping \(d\)-simplices using only original vertices. Such a triangulation exists by pulling the vertices. Work first with a generic unit direction \(\theta\) for which the projections \(q_u=\langle u,\theta\rangle\) of all vertices are pairwise distinct. For any simplex \(T\in\mathcal T\), the exact one-dimensional pushforward-density formula is
\[
 A_{T,\theta}(t)=d\operatorname{vol}_d(T)
 \sum_{u\in\operatorname{vert}T}
 \frac{(t-q_u)_+^{d-1}}
 {\prod_{z\in\operatorname{vert}T,\ z\ne u}(q_z-q_u)}.
\]
Here \(s_+=\max(s,0)\); the factor \(d\operatorname{vol}_d(T)\) results from differentiating the normalized simplex sublevel-volume formula and multiplying by the simplex volume. Because \(\theta\) has unit length, this density is exactly the Euclidean \((d-1)\)-dimensional section volume, without an additional Jacobian. This formula follows directly by an affine change of variables from the simplex section formula of Lasserre, Theorem 2.2 [2]. Summing the simplices gives
\[
 A_{P,\theta}(t)=\sum_{u\in\operatorname{vert}P}C_u(\theta)(t-q_u)_+^{d-1},
 \qquad
 C_u(\theta)=d\sum_{T\in\mathcal T:\,u\in T}
 \frac{\operatorname{vol}_d(T)}
 {\prod_{z\in\operatorname{vert}T,\ z\ne u}\langle z-u,\theta\rangle}.
\]
The finite sum makes each \(C_u\) rational on the complement of finitely many great subspheres. In the distributional sense on any real open interval,
\[
 D_t^d A_{P,\theta}=(d-1)!\sum_{u\in\operatorname{vert}P}C_u(\theta)\,\delta_{q_u}.
\]
Indeed, \(D_t^d(t-q)_+^{d-1}=(d-1)!\delta_q\). These identities are the full-dimensional version of the standard polytope-projection spline description [2,3].

**2. Every vertex has a generically nonzero knot coefficient.** Fix a vertex \(w\). Select a unit vector \(\phi\) strictly inside the outer normal cone of \(w\), avoiding the finite hyperplanes where other vertex projections collide. Then \(\langle z-w,\phi\rangle<0\) for every other vertex \(z\). Every summand in \(C_w(\phi)\) is nonzero and has the same sign \((-1)^d\); at least one simplex contains \(w\). Thus \(C_w(\phi)\ne0\). Clearing denominators shows that the numerator of \(C_w\) is not identically zero as a function on the sphere. Hence its zero set has empty interior on every open sphere patch on which the denominators do not vanish. This is the noncancellation step needed below, including for nonsimple vertices.

**3. An isolated moving knot immediately below support.** Write \(E=[v,w]\), and fix the given \(\theta_0\), which exposes exactly \(E\). The two heights coincide at the support height \(H\): \(q_v(\theta_0)=q_w(\theta_0)=H\). Every other vertex has strictly lower height. Move \(\theta_0\) a sufficiently small amount into the halfspace where \(q_v>q_w\). We obtain a nonempty open patch in \(W\) where \(v\) is the unique highest vertex, \(w\) the unique second-highest vertex, and
\[
 0<q_v-q_w<\varepsilon/3.
\]
By Step 2, after avoiding a proper algebraic exceptional set, choose one \(\theta_*\) in that patch with \(C_w(\theta_*)\ne0\) and all vertex heights distinct. Let \(\delta_*=q_v(\theta_*)-q_w(\theta_*)>0\). Shrink to a connected nonempty open patch \(U\) around \(\theta_*\) so that \(C_w\ne0\), all heights remain pairwise distinct, and \(v,w\) remain the top two vertices. Their positive separation, the positive gap to every other vertex, and the distance from \(q_w(\theta_*)\) to both ends of the interval \((q_v(\theta_*)-\varepsilon,q_v(\theta_*))\) permit a small common interval \(J\) containing all values \(q_w(\theta)\), \(\theta\in U\), but no values \(q_z(\theta)\) for \(z\ne w\), and satisfying
\[
 J\subset(q_v(\theta)-\varepsilon,q_v(\theta))\quad\text{for all }\theta\in U.
\]
Since \(0\in\operatorname{int}P\), the vertex \(w\) is nonzero. The map \(\theta\mapsto\langle w,\theta\rangle\) is not constant on any open sphere patch in dimension at least two. Therefore choose infinitely many \(\theta_k\in U\) with pairwise distinct \(q_w(\theta_k)\in J\).

**4. Linear independence and contradiction.** On \(J\) there is exactly one projected-vertex height for each chosen direction. Step 1 now gives
\[
 D_t^d(A_{P,\theta_k}|_J)=(d-1)!C_w(\theta_k)\delta_{q_w(\theta_k)},
 \qquad C_w(\theta_k)\ne0.
\]
Dirac distributions at distinct points are linearly independent: test against a smooth bump supported near any one point. Consequently every finite collection of the original profiles on \(J\) is linearly independent. If a finite separated representation with \(N\) terms existed on all the claimed near-support intervals, each of these profiles on the common \(J\) would belong to the span of \(b_1|_J,\ldots,b_N|_J\), contradicting the existence of \(N+1\) linearly independent profiles. This completes the proof.

## Verification

A standalone exact-rational script, `checks.py`, tests the normalized simplex-spline formula on a square triangulated into two triangles, using three distinct rational unit directions. It verifies the exact projected-density trapezoids, that each second-highest vertex has a nonzero \(D_t^2\)-atom on a shared interval, and exact zeroth and first moments. For the standard tetrahedron it separately checks exact total mass, centroid moment, and nonzero generic atom coefficients. Run with `python3 checks.py` from the extracted package directory. The script uses only Python's standard library. These finite computations are illustrations, not the proof of universal noncancellation; Step 2 establishes that for every polytope and every vertex.

## Relationship to prior work

Fish, Ryabogin, Sun, and Yaskin [1] introduced the near-boundary finite-separability condition used here. Their Theorem 4.3 identifies centered Euclidean balls under an **infinitely smooth** assumption in even dimensions, and their introduction explicitly leaves the odd-dimensional near-boundary case beyond their results. The present theorem excludes every full-dimensional polytope in **all** dimensions at least two, without regularity of the separated factors. It neither proves the smooth odd-dimensional characterization nor generalizes their full smooth-body theorem. The simplex slice formula of Lasserre [2] and the general spline-knot support property of Shapiro [3] are established ingredients. The new step is universal noncancellation of the projected-vertex coefficient together with an edge-local family of moving knots on one common near-support interval, forcing infinite separation rank.

## Limitations

This is an exact nonseparability theorem for polytopes only. It does not characterize arbitrary nonsmooth convex bodies, obtain quantitative finite-rank approximation lower bounds, determine finite-dimensional rank for finitely many fixed directions, or resolve the smooth odd-dimensional near-boundary classification. The proof is elementary once the established simplex-spline formula is available; an equivalent statement may occur in older unindexed spline or geometric-tomography literature.

## References

[1] A. Fish, D. Ryabogin, W. R. Sun, V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229, first posted 2026-10-07. https://arxiv.org/pdf/2610.10229

[2] J.-B. Lasserre, *Volume of slices and sections of the simplex in closed form*, arXiv:1412.4617, 2014, Theorem 2.2. https://arxiv.org/pdf/1412.4617

[3] B. Shapiro, *Projections of convex polytopes to a line and higher univariate Prony systems*, arXiv:2605.15917, first posted 2026-05-15, Proposition 2.1. https://arxiv.org/pdf/2605.15917
