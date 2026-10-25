# Sharp vertex convexification bound via planar Minkowski asymmetry

## Finding

Let \(P\subset\mathbb R^2\) be any compact full-dimensional convex polygon, and let \(V(P)\) denote its finite vertex set. With Minkowski sum denoted by \(+\), define the **vertex convexification threshold**
\[
c_V(P)=\inf\{\lambda\ge0:V(P)+\lambda P=(1+\lambda)P\}.
\]
Define its **Minkowski asymmetry** as
\[
s(P)=\min_{z\in\operatorname{int}P}\min\{s\ge1:-(P-z)\subseteq s(P-z)\}.
\]
Then
\[
\boxed{1\le c_V(P)\le s(P)\le2.}
\]
For the regular \(n\)-gon \(P_n\), \(n\ge3\), these inequalities give the exact values
\[
\boxed{c_V(P_n)=s(P_n)=
\begin{cases}
1&\text{if }n\text{ is even},\\
\sec(\pi/n)&\text{if }n\text{ is odd}.
\end{cases}}
\]
These conclusions persist under every invertible affine transformation. For odd \(n\), the excess over one is asymptotic to \(\pi^2/(2n^2)\).

## Assumptions and scope

All polygons are closed, bounded, two-dimensional, and have finitely many distinct extreme vertices. The parameter \(\lambda\) is a nonnegative scalar; \(V(P)+\lambda P\) is a union of finitely many homothetic copies of \(P\), not its convex hull. The right side \((1+\lambda)P\) is the full convex hull of that union. Minkowski asymmetry is defined after optimizing the translation center. Neither polygonal smoothness nor central symmetry is assumed. No claim concerns arbitrary compact sets or spatial polytopes, for which the edge argument does not directly cover higher-dimensional faces.

## Proof

**Lower bound.** Fix any edge \(E=[v,w]\) of \(P\), and let \(u\) expose this edge. The exposed face of \((1+\lambda)P\) in direction \(u\) is \((1+\lambda)E\). The exposed part of \(V(P)+\lambda P\) is exactly \((v+\lambda E)\cup(w+\lambda E)\); no other vertex lies in the exposed supporting line. These two intervals at the ends of \((1+\lambda)E\) leave a nonempty open gap whenever \(\lambda<1\). Hence \(c_V(P)\ge1\).

**Upper bound.** Choose a Minkowski center and translate so it is the origin, with \(-P\subseteq sP\), where \(s=s(P)\ge1\). Put \(r=s/(1+s)\ge1/2\), and for every vertex \(v\) define
\[
H_v=(1-r)v+rP=\frac{v+sP}{1+s}.
\]
Each \(H_v\) is convex and contained in \(P\). It also contains \(0\): since \(v\in P\) and \(-P\subseteq sP\), one has \(-v/s\in P\).

For every boundary edge \(E=[v,w]\), the subset \(H_v\cap E\) contains the initial portion of \(E\) of relative length \(r\), while \(H_w\cap E\) contains the terminal portion of relative length \(r\). As \(2r\ge1\), the two portions cover \(E\). Thus every boundary point of \(P\) lies in at least one \(H_v\). Every interior point \(x\in P\) lies on the segment from the interior origin to some boundary point \(y\); choose \(v\) with \(y\in H_v\). Since \(0,y\in H_v\) and \(H_v\) is convex, \(x\in H_v\). Consequently
\[
P=\bigcup_{v\in V(P)}H_v
=\frac{V(P)+sP}{1+s},
\]
so \(c_V(P)\le s(P)\). The standard planar Minkowski asymmetry inequality \(s(P)\le2\) completes the universal chain. It can be proved by placing the centroid at the origin and using the classical dimension-bound \(-P\subseteq2P\).

**Regular-polygon sharpness.** For any fixed \(s\), the feasible set of centers \(z\) satisfying \(-(P-z)\subseteq s(P-z)\) is an intersection of convex sets, since equivalently \((s+1)z\in p+sP\) for every \(p\in P\). For a regular polygon this feasible center set is rotation invariant. Averaging one feasible center over all rotational symmetries therefore shows that the origin is feasible for the minimizing \(s\).

Normalize the circumradius of \(P_n\) to one. If \(n\) is even, the opposite of each vertex is again a vertex; hence \(-P_n=P_n\) and \(s(P_n)=1\). If \(n\) is odd, the ray opposite each vertex meets the opposite edge at radius \(\cos(\pi/n)\), so its minimal dilating factor is \(\sec(\pi/n)\); by symmetry this is \(s(P_n)\).

To attain equality for the convexification threshold when \(n\) is odd, note that if \(\lambda<\sec(\pi/n)\) then for every vertex \(v\) we have \(-v/\lambda\notin P_n\); hence \(0\notin V(P_n)+\lambda P_n\), although \(0\in(1+\lambda)P_n\). This yields \(c_V(P_n)\ge\sec(\pi/n)\). Together with the upper bound it proves equality. For even \(n\), combine \(c_V(P_n)\ge1\) with \(c_V(P_n)\le s(P_n)=1\). Affine invariance follows directly because invertible affine maps commute with convex combinations, the inclusion defining asymmetry, and the corresponding Minkowski-sum identity. The Taylor expansion of \(\sec t\) gives the asymptotic statement.

## Verification

Every part of the sharp planar comparison is derived by exact inclusion arguments: an exposed-edge obstruction, a homothetic cover of the boundary followed by radial filling, and a parity-sensitive test at the origin for regular polygons. All quantifiers apply to every planar compact full-dimensional polygon; the center argument only assumes the existence of a Minkowski center, guaranteed for convex bodies. No numerical sampling, symbolic code, or unproved computational inference is required. A direct consistency check gives a triangle threshold \(2\), every parallelogram threshold \(1\), and the odd pentagon threshold \(\sec(\pi/5)\).

## Relationship to prior work

Meyer, *Finite convexification by Minkowski summation* (arXiv:2610.26744v1), characterizes when \(A+\lambda K\) becomes convex, including planar cases; its main exposed-set finiteness criteria do not state this sharp uniform inequality in terms of Minkowski asymmetry or these exact regular-polygon values. Artstein-Avidan, Falah and Slomka, *Vertex generated polytopes* (arXiv:2407.20604v1), study the equivalent vertex-generation parameter \(\theta(P)=1/(1+c_V(P))\), prove general bounds, and include the centrally symmetric planar case through zonotopes. Those results do not state the stronger shape-sensitive planar bound \(c_V(P)\le s(P)\) or the odd-order regular-polygon formula. The Geller–Misiurewicz convexity gap of polygon vertex sets and Schneider's reflection convexity points are distinct invariants and do not imply this finite Minkowski convexification result.

## Limitations

The comparison is specific to planar polygons: the edge-covering proof cannot simply be substituted for facets in higher dimensions. It gives an upper bound, not a classification of equality for every planar polygon. The regular-polygon equality family is exact, but this does not settle all minimizers or near-equality stability. Earlier vertex-generation work is closely related and may contain an implicit reformulation; literature comparison was bounded, and absolute priority is not certified. Independent external mathematical audit has not been performed.

## References

1. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1, submitted 19 October 2026, https://arxiv.org/abs/2610.26744.
2. Shiri Artstein-Avidan, Tomer Falah, Boaz A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604v1, submitted 30 July 2024, https://arxiv.org/abs/2407.20604.
3. H. Minkowski, classical bound on Minkowski asymmetry of planar convex bodies, \(s(P)\le2\), with equality for triangles (standard convex-geometry inequality).
