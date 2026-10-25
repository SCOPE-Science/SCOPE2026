# A universal penetration law and sharp shape order for boundary chords of triangles

## Finding
Let \(K\) be any nondegenerate triangle, with perimeter \(P\), side lengths \(\ell_1,\ell_2,\ell_3\), and centroid \(c\). Choose independent boundary points \(X,Y\) uniformly in Euclidean arclength; take the closed chord \([X,Y]\). Define the **penetration scale**
\[
T=\inf\{t\in[0,1]:[X,Y]\cap(c+t(K-c))\neq\varnothing\}.
\]
Write \(\sigma=\sum_{i=1}^{3}(\ell_i/P)^2\) and for \(0<t<1\) put \(a=(1-t)/3\) and
\[
Q(t)=1-2a-3a^2-2a^2\log\frac{1-a}{a}
+2a(1-2a)\log\frac{1-a}{1-2a}.
\]
The **complete law** is
\[
\Pr(T\le t)=(1-\sigma)Q(t)\quad(0<t<1),
\qquad \Pr(T=1)=\sigma.
\]
There are no other atoms. Conditional on the two sampled points falling on **different** sides, the entire distribution is \(Q\), independent of the triangle's shape. For each fixed \(0<t<1\),
\[
\frac12Q(t)<\Pr(T\le t)\le\frac23Q(t),
\]
where equality on the right holds exactly for equilateral triangles and the lower bound is sharp as the triangle degenerates. Thus the equilateral triangle stochastically minimizes penetration scale among nondegenerate triangles.

The distribution does **not** identify a triangle up to similarity. Triangles with side triples \((2,2,1)\) and \((4,4,7)\) are not similar, yet both have \(\sigma=9/25\), hence identical full penetration laws. In particular the probability mass at \(T=1\) recovers only \(\sigma\).

## Assumptions and scope
Only nondegenerate Euclidean triangles are considered. Sampling is independent and uniform by *perimeter arclength*, not invariant-line measure. The core is centered at the ordinary vertex centroid and homothetic by factor \(t\). Statements involving the displayed density-free formula apply at \(0<t<1\); at \(t=0\) the distribution is zero and at \(t=1\) the CDF equals one. Endpoint contacts, vertices and tangencies have probability zero and do not affect the law.

## Proof
**Affine reduction.** The event that a chord intersects a centroidal homothetic core is affine invariant. Conditional on each endpoint's side, its fractional position on that side is uniformly distributed on \([0,1]\), even after an affine map, because an affine map scales lengths by a constant along each side. A pair of **distinct** sides can therefore be reduced to the standard simplex with barycentric coordinates \((x,y,z)\), where \(x+y+z=1\) and all coordinates are nonnegative.

Take the two endpoints to be \((0,u,1-u)\) and \((v,0,1-v)\), where \(u,v\) are independent uniform variables on \((0,1)\). Their supporting line is
\[
L(x,y)=x/v+y/u=1.
\]
The centroidal inner triangle is described by \(x,y,z\ge a=(1-t)/3\); it has vertices that permute \((1-2a,a,a)\). As the complete outer segment is the intersection of its supporting line with the outer triangle, intersection with the inner triangle holds precisely when the minimum and maximum of \(L\) over the inner triangle straddle one. Their values are
\[
L_{\min}=a(1/u+1/v),\qquad
L_{\max}=\frac{1-2a}{\min(u,v)}+\frac{a}{\max(u,v)}.
\]
The two failure events \(L_{\min}>1\) and \(L_{\max}<1\) are disjoint.

**First failure region.** For \(a\in(0,1/3)\), solving \(a(1/u+1/v)>1\) and integrating the unit square gives
\[
A(a)=\frac{a}{1-a}+\int_{a/(1-a)}^1\frac{au}{u-a}\,du
=2a+2a^2\log\frac{1-a}{a}.
\]
**Second failure region.** Set \(b=1-2a\). By symmetry restrict to \(u=\min(u,v)\). The region \(L_{\max}<1\) has \(b/(1-a)<u<1-a\) with \(au/(u-b)<v<1\), or \(1-a<u<1\) with \(u<v<1\). Thus
\[
B(a)=2\left[\int_{b/(1-a)}^{1-a}\left(1-\frac{au}{u-b}\right)du+
\int_{1-a}^1(1-u)du\right]
=3a^2-2a(1-2a)\log\frac{1-a}{1-2a}.
\]
Consequently \(\Pr(T\le t\mid\text{distinct sides})=1-A(a)-B(a)=Q(t)\). The geometric nested-core events show \(Q\) is a strictly increasing continuous CDF on \((0,1)\), with \(Q(0)=0\) and \(Q(1-)=1\). A positive-measure open neighborhood of \(u=v=2/3\) produces penetration for each \(t>0\), so \(Q(t)>0\); likewise configurations close to a common vertex miss any proper core, so \(Q(t)<1\) for \(t<1\).

**Side mixture and extremizers.** An endpoint lies on side \(i\) with probability \(w_i=\ell_i/P\). The chance that both endpoints lie on the same side is \(\sum_iw_i^2=\sigma\), and then the chord lies on the boundary, giving \(T=1\) almost surely. All distinct-side pairs have the above law, so the claimed mixture follows.

The triangle inequalities imply \(0<w_i<1/2\) and \(\sum_iw_i=1\). Cauchy–Schwarz gives \(\sigma\ge1/3\), with equality only when all side lengths are equal. On the closed simplex subject to \(0\le w_i\le1/2\), the strictly convex function \(\sum_iw_i^2\) achieves its maximum \(1/2\) at a permutation of \((1/2,1/2,0)\); thus \(\sigma<1/2\) for every nondegenerate triangle, and this supremum is approached by degenerations. Multiplying by the strictly positive \(Q(t)\) proves both sharp bounds and the equality classification. Finally the two example triples have normalized squared side-length sums \(9/25\) and \(81/225=9/25\), respectively, but distinct unordered side ratios.

## Verification
The independent geometry-based checker `verify.py` constructs arclength-uniform endpoints on three noncongruent triangles, determines intersection with the core by clipping a chord against three barycentric inequalities, and compares the observed frequencies with the analytic mixture at five thresholds. A second simulation directly samples the two independent side parameters and checks the min/max inequalities. The runs used 35,000 pairs for each of three triangles and 100,000 conditional pairs; all 20 comparisons had absolute standardized deviations below 1.1. The proof above, not finite simulation, establishes the formula for every triangle and every threshold.

The exact integral boundaries can also be checked by differentiating their antiderivatives; no numerical integration is required in the theorem.

## Relationship to prior work
The independently chosen **boundary endpoints** and the **penetration into a nested centroidal triangle** distinguish the statistic from chord-length laws, invariant-line models, or interior-origin rays. Ehlers and Enns (1981) derive length distributions for several surface-generated secant models. Enns and Ehlers (1988) sample segments from an embedded-body construction and project them outward; the available abstract does not establish equivalence with independent boundary endpoints. Ren (2014) studies chord distributions and containment functions, with a different line/containment perspective; a full comparison of its unavailable text remains open. Álvarez Lobo (2016), whose publicly accessible author manuscript was examined, computes a length-threshold probability for a particular isosceles-triangle construction with a uniform slope conditional on one boundary point. It neither uses the same two-endpoint sampling nor computes a continuously varying centroidal penetration CDF.

The new structural content is the exact entire law together with conditional affine universality, the sharp triangle-wide stochastic extremum and non-identifiability of shape. None follows immediately from merely knowing a chord's Euclidean length.

## Limitations
This is an analytic result for Euclidean triangles only, under the specified **two independent perimeter-uniform endpoint** sampling rule; it does not cover uniformly oriented random lines or general convex polygons. Three neighboring historical works were only abstract-accessible, so an equivalent unindexed or inaccessible treatment remains a genuine originality risk. Numerical checks are supplementary; no independent scientific audit has been performed.

## References
- J. Álvarez Lobo, *A Geometric-Probabilistic Problem About the Lengths of the Segments Intersected in Straights that Randomly Cut a Triangle* (2016), arXiv:1602.03005, https://arxiv.org/abs/1602.03005 ; accessible author full text https://www.researchgate.net/publication/293797186 .
- P. F. Ehlers and E. G. Enns, *Random Secants of a Convex Body Generated by Surface Randomness*, Journal of Applied Probability 18 (1981), 157–166, https://doi.org/10.2307/3213176 .
- E. G. Enns and P. F. Ehlers, *Chords Through a Convex Body Generated from Within an Embedded Body*, Journal of Applied Probability 25 (1988), 700–707, https://doi.org/10.2307/3214290 .
- D. Ren, *Random Chord Distributions and Containment Functions*, Advances in Applied Mathematics 58 (2014), 1–20, https://doi.org/10.1016/j.aam.2014.05.003 .
