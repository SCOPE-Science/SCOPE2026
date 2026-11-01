# Sharp surface–interior squared-distance gap on simplices and the dimension-four reversal

## Finding
Let \(T=\operatorname{conv}(v_0,\ldots,v_d)\) be any nondegenerate Euclidean \(d\)-simplex, \(d\ge2\). Let \(X,X'\) be independent uniform points in its interior (normalized volume), and \(Y,Y'\) independent uniform points on its boundary (normalized facet hyperarea). Write
\[
 g=\frac1{d+1}\sum_{i=0}^{d}v_i,\quad S(T)=\sum_{i=0}^{d}\|v_i-g\|^2,
 \quad p_i=\frac{\operatorname{vol}_{d-1}(F_i)}{\sum_j\operatorname{vol}_{d-1}(F_j)},
\]
where \(F_i\) is the facet opposite \(v_i\). Then the **exact identity** is
\[
 \mathbb E\|Y-Y'\|^2-\mathbb E\|X-X'\|^2
 =\frac{4S(T)}{d(d+1)(d+2)}-\frac2{d^2}\left\|\sum_i p_i(v_i-g)\right\|^2.
\]
In every dimension the following best-possible constant holds:
\[
\boxed{\frac{\mathbb E\|Y-Y'\|^2-\mathbb E\|X-X'\|^2}{S(T)}
>c_d=\frac{-d^2+3d+2}{d^2(d+1)(d+2)}.}
\]
Its infimum over nondegenerate \(d\)-simplices equals \(c_d\), without attainment. In particular, \(c_2=1/12\), \(c_3=1/90\), and \(c_4=-1/240\). Every triangle and every tetrahedron thus has strictly larger **surface-to-surface** expected squared distance than its **interior-to-interior** expected squared distance, while in **every dimension \(d\ge4\)** there are nondegenerate simplices for which the reverse inequality holds.

## Assumptions and scope
All norms and hyperareas are Euclidean. A nondegenerate simplex has positive \(d\)-dimensional volume and all \(d+1\) facet hyperareas are positive. The second moment concerns **independent endpoints with the same sampling law** in each pair, not one interior and one boundary point. The normalization \(S(T)>0\) is translation-invariant and quadratic under dilation. The assertions have integer quantifier \(d\ge2\), with a sharp nonattained infimum over every nondegenerate simplex in each fixed dimension.

## Proof
**Step 1: Exact moments of volume and facets.** A uniform point in a \(k\)-simplex with vertices \(a_0,\ldots,a_k\) satisfies
\[
 \mathbb EZ=\frac1{k+1}\sum_j a_j,\qquad
 \mathbb E\|Z\|^2=\frac{\sum_j\|a_j\|^2+\|\sum_j a_j\|^2}{(k+1)(k+2)},
\]
by the Dirichlet \((1,\ldots,1)\) barycentric moments. Put \(w_i=v_i-g\); then \(\sum_i w_i=0\). Taking \(k=d\) gives \(\mathbb EX=g\), \(\mathbb E\|X-g\|^2=S(T)/[(d+1)(d+2)]\), hence
\[
\mathbb E\|X-X'\|^2=\frac{2S(T)}{(d+1)(d+2)}.
\]
On the \(i\)-th facet, the mean relative to \(g\) is \(-w_i/d\), and the mean squared distance to \(g\) is
\[
\frac{\sum_{j\ne i}\|w_j\|^2+\|\sum_{j\ne i}w_j\|^2}{d(d+1)}
=\frac{S(T)}{d(d+1)},
\]
which is independent of the facet. Since normalized boundary measure is the mixture with facet probabilities \(p_i\), we obtain
\[
\mathbb E(Y-g)=-\frac1d\sum_i p_iw_i,
\quad\mathbb E\|Y-g\|^2=\frac{S(T)}{d(d+1)}.
\]
Using \(\mathbb E\|Z-Z'\|^2=2(\mathbb E\|Z-g\|^2-\|\mathbb EZ-g\|^2)\) yields the displayed exact gap identity.

**Step 2: Universal bound.** Let \(A_i>0\) be the facet hyperareas and \(n_i\) their outward unit normals. The standard equilibrium identity \(\sum_i A_in_i=0\) follows by integrating a constant vector field over the simplex. Thus \(A_i\le\sum_{j\ne i}A_j\), hence \(0<p_i\le1/2\). Consequently \(\sum_i p_i^2\le (\max_i p_i)\sum_i p_i\le1/2\), with strict inequality for every genuine simplex (all other normals cannot be parallel to the opposite normal, and all \(p_i>0\)). The Cauchy–Schwarz inequality in the direct-sum Hilbert space gives
\[
\left\|\sum_i p_iw_i\right\|^2
=\left\|\sum_i\left(p_i-\frac1{d+1}\right)w_i\right\|^2
\le S(T)\left(\sum_i p_i^2-\frac1{d+1}\right)
<\frac{d-1}{2(d+1)}S(T).
\]
Substitution in the identity gives
\[
\frac{4}{d(d+1)(d+2)}-\frac{d-1}{d^2(d+1)}
=\frac{-d^2+3d+2}{d^2(d+1)(d+2)}=c_d.
\]

**Step 3: Sharpness in every dimension.** For \(t>0\), with \(e_1,\ldots,e_d\) an orthonormal basis, take
\[
 v_0=0,\quad v_1=t^2e_2,\quad v_2=e_1,\quad v_j=e_1+te_j\ (3\le j\le d).
\]
The simplex is nondegenerate. Its \(d+1\) facet hyperareas, up to the common positive factor \(t^{d-2}/(d-1)!\), are
\[
 \sqrt{1+t^4},\quad 1,\quad t\sqrt{d-2+t^2},\quad
 \underbrace{t,\ldots,t}_{d-2\text{ entries}}.
\]
This follows by subtracting a facet base vertex and computing orthogonal wedge-product lengths; it also holds when \(d=2\), with the empty final block. Hence \((p_0,p_1,p_2,\ldots,p_d)\to(1/2,1/2,0,\ldots,0)\). As \(t\downarrow0\), the vertices converge to two copies of \(0\) and \(d-1\) copies of \(e_1\). Therefore
\[
 S(T)\longrightarrow\frac{2(d-1)}{d+1},\qquad
 \left\|\sum_i p_i(v_i-g)\right\|^2\longrightarrow
 \left(\frac{d-1}{d+1}\right)^2,
\]
and the squared ratio of these limits equals \((d-1)/(2(d+1))\), proving the strict bound is the infimum.

**Step 4: A completely explicit dimensional reversal.** The numerator \(-d^2+3d+2\) is positive at \(d=2,3\) and negative for each integer \(d\ge4\). The family in Step 3 therefore yields an actual reversal for all sufficiently small \(t>0\) in each dimension \(d\ge4\). For a fixed rational witness already in dimension four, set \(t=1/100\) in the displayed vertices. Let \(P\) be the total normalized facet weight of vertices \(v_2,v_3,v_4\); the facet formula gives
\[
P=\frac{t(\sqrt{2+t^2}+2)}{\sqrt{1+t^4}+1+t(\sqrt{2+t^2}+2)}<2t=\frac1{50}.
\]
The centroid's first coordinate equals \(3/5\), so the first coordinate of \(\mathbb E(Y-g)\) is \((3/5-P)/4>29/200\). Directly, \(S(T)=6/5+(8/5)t^2+(4/5)t^4\). The exact moment identity now gives the **rigorous rational certificate**
\[
\mathbb E\|Y-Y'\|^2-\mathbb E\|X-X'\|^2
<\frac{S(T)}{30}-2\left(\frac{29}{200}\right)^2
=-\frac{2555833}{1250000000}<0.
\]
This exhibits reversal by a nondegenerate simplex with rational coordinates; no limiting degeneration is used for this counterexample.

## Verification
The standalone standard-library Python file `check_simplex_moments.py` verifies the symbolic sharp coefficients (including \(c_2,c_3,c_4\)), the exact rational four-dimensional negative-gap certificate, and 52 independent dimension/scale numerical examples using 70-digit decimal arithmetic in dimensions 2 through 14. Its verified output includes a dimension-four gap of approximately \(-0.00251312745\), below the rational upper bound \(-0.0020446664\). These finite checks are diagnostics; the proof above is the basis of the universal statements.

## Relationship to prior work
Tokmachev (arXiv:2607.08869, 9 July 2026) proves distance-moment comparisons from convex order for planar bodies with matching surface and volume centroids, and certain circumscribed polytopes with a common center. That does not cover arbitrary higher-dimensional simplices, whose normalized boundary and volume centroids need not agree. Shen (arXiv:2608.06470, 6 August 2026) addresses the first moment for planar bodies and six-vertex non-simplex higher-dimensional counterexamples; its accessible abstract does not imply the present sharp squared-moment constant or simplex threshold. Lotnikov (arXiv:2608.14848, 14 August 2026), especially Theorem 8 in the full manuscript, gives second-moment identities for *projective* boundary measures and a result for circumscribed bodies; these are related exact-moment methods but do not provide the extremal facet-weight inequality or dimensional classification above. A separately indexed exact triangle squared-moment comparison is acknowledged; the triangle case here is a consistency check, not the claimed novel contribution. The new claims are the **sharp universal all-dimensional normalized simplex bound** and the **dimension-four simplicial reversal threshold**, together with the explicit witness.

## Limitations
The comparison is for the second power of Euclidean pairwise distance, not first moments or arbitrary exponents. The sharp bound is normalized by \(S(T)\), not diameter or volume. The infimum is approached by degenerating simplices and is not attained by a full-dimensional simplex. Originality is based on explicit comparisons with inspected and indexed accessible literature, not a proof of global priority; independent review is not yet available. The complete text of Shen's paper was not inspected, leaving some residual unindexed-priority uncertainty.

## References
1. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869, version first public 2026-07-09.
2. E. Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470, first public 2026-08-06.
3. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848, first public 2026-08-14; especially Section 10 and Theorem 8.
4. *Exact second-moment boundary gap for arbitrary Euclidean triangles*, indexed public mathematics finding `2026/10/4/SCOPE-exact-second-moment-boundary-gap-for-arbitrary-euclidean-triangl--d886b40f95a8` (the overlapping two-dimensional special case).
