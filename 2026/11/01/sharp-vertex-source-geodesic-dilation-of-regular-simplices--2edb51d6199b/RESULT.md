# Sharp vertex-source geodesic dilation of regular simplices

## Finding
Let \(T\subset\mathbb R^n\) be a regular Euclidean \(n\)-simplex with edge length \(a>0\), where \(n\ge2\), and equip its boundary with the intrinsic shortest-path metric \(d_{\partial T}\). Fix any vertex \(v\). Then for every \(p\in\partial T\),
\[
\|v-p\|_2\le d_{\partial T}(v,p)\le \sqrt{\frac{n+1}{n-1}}\,\|v-p\|_2.
\]
The constant is best possible for every dimension and is attained, for \(p\ne v\), **only** at the barycenter \(G\) of the facet opposite \(v\). In particular, the sharp fixed-vertex chord--arc distortion equals \(\sqrt{(n+1)/(n-1)}\), tending to one as dimension increases.

A stronger facetwise estimate also holds. Put \(R=a(n+1)/\sqrt{2n(n-1)}\). For every point \(p\) in the facet opposite \(v\),
\[
d_{\partial T}(v,p)^2\le R^2+\|p-G\|_2^2,
\]
with equality only at \(p=G\).

## Assumptions and scope
Dimension \(n\) is an arbitrary integer at least two. All intrinsic lengths lie in the polyhedral boundary of the solid simplex, including its facets and their shared ridges. The ambient norm is the standard Euclidean norm in \(\mathbb R^n\). The ratio is evaluated only for \(p\ne v\); the inequality itself also holds at \(p=v\). Edge length \(a>0\) is arbitrary and cancels from the distortion ratio. No claim is made for nonregular simplices, arbitrary source points, or the unrestricted two-point distortion of the boundary.

## Proof
Scale to \(a=1\). Write \(F=\operatorname{conv}\{b_1,\ldots,b_n\}\) for the facet opposite \(v\), with centroid \(G\). The distance from \(v\) to the affine hull of \(F\) is
\[
H=\sqrt{\frac{n+1}{2n}}.
\]
The altitude of a regular facet of dimension \(n-1\), from one vertex to its opposite ridge, is \(h_f=\sqrt{n/[2(n-1)]}\). The inradius of \(F\), namely the distance from \(G\) to its boundary, is \(r_f=h_f/n=1/\sqrt{2n(n-1)}\). Set
\[
R=h_f+r_f=\frac{n+1}{\sqrt{2n(n-1)}},\qquad \frac{R^2}{H^2}=\frac{n+1}{n-1}.
\]
These identities follow directly from the orthogonal coordinate realization \(b_j=e_j/\sqrt2\), \(v=e_0/\sqrt2\) of a unit-edge regular simplex in an affine \(n\)-plane of \(\mathbb R^{n+1}\).

For each index \(i\), let \(F_i\) be the ridge of \(F\) opposite \(b_i\), and let \(u_i=(b_i-G)/\|b_i-G\|_2\) be the unit vector from \(G\) toward \(b_i\) inside \(\operatorname{aff}(F)\). Unfold the adjacent facet \(\operatorname{conv}(\{v\}\cup F_i)\) across \(F_i\) into \(\operatorname{aff}(F)\). The unfolded source is \(v_i'=G-Ru_i\), because the projection of \(b_i\) and the projection of the unfolded source onto \(\operatorname{aff}(F_i)\) are both the ridge centroid, on opposite sides of \(F_i\).

For every \(p\in F\), the straight segment joining \(v_i'\) to \(p\) crosses \(F_i\) at a point inside that ridge. Indeed, the orthogonal projection of every vertex of \(F\) onto \(F_i\) lies in the ridge (the projected omitted vertex is the ridge centroid); by convexity the same holds for every point of \(F\). The segment from the unfolded source to \(p\) therefore crosses the ridge in the convex hull of two points of \(F_i\). Folding back yields an admissible path on two facets of length \(\|p-v_i'\|_2\). Consequently,
\[
d_{\partial T}(v,p)^2\le \min_{1\le i\le n}\|p-G+Ru_i\|_2^2
 =R^2+\|p-G\|_2^2+2R\min_i\langle p-G,u_i\rangle.
\]
Symmetry gives \(\sum_i u_i=0\), and these normals span the \((n-1)\)-dimensional facet plane. Hence \(\min_i\langle p-G,u_i\rangle\le0\), with strict inequality unless \(p=G\). This proves the stronger estimate and its strictness away from \(G\). Since the ambient orthogonal projection of \(v\) onto \(\operatorname{aff}(F)\) is \(G\),
\[
\|v-p\|_2^2=H^2+\|p-G\|_2^2.
\]
Together with \(R^2=[(n+1)/(n-1)]H^2\) and \((n+1)/(n-1)>1\), the displayed upper bound proves the desired chord--arc inequality, strictly for \(p\in F\setminus\{G\}\). For \(p\) lying on any facet incident to \(v\), the straight segment inside that facet has length \(\|v-p\|_2\), so the intrinsic distance equals the chord and the upper inequality is strict for \(p\ne v\).

It remains to establish equality at \(G\). Any surface path from \(v\) to \(G\) first enters the opposite facet \(F\) at some boundary point \(q\in\partial F\). The portion before this first entry has length at least \(\|v-q\|_2=\sqrt{H^2+\|q-G\|_2^2}\); the remaining portion has length at least \(\|q-G\|_2\). Because \(\|q-G\|_2\ge r_f\) and \(s\mapsto\sqrt{H^2+s^2}+s\) is strictly increasing for \(s\ge0\), every such path has length at least \(\sqrt{H^2+r_f^2}+r_f=h_f+r_f=R\). Conversely, the segment through the centroid of any ridge \(F_i\) follows an altitude in the adjacent facet and then an altitude in \(F\), giving an explicit surface path of length \(h_f+r_f=R\). Therefore \(d_{\partial T}(v,G)=R\), attaining the claimed ratio. Rescaling completes the proof.

## Verification
The bundled `verify_simplex_dilation.py` requires Python, SymPy and NumPy; run `python verify_simplex_dilation.py`. It checks exact symbolic altitude, inradius and distortion identities, and 22,000 seeded barycentric samples over dimensions 2 through 23. The universal inequality, admissibility of unfolded paths, uniqueness of equality and sharpness are proved above for every dimension; numerical sampling is not used as an infinite proof.

## Relationship to prior work
Miller and Pak (2003, arXiv:math/0312253v1) developed general cut-locus and source-unfolding methods for convex polyhedral boundaries. Davis, Dods, Traub and Yang (2015, arXiv:1508.03546v1) describe geodesic trajectories on regular tetrahedra and cubes, including vertex-source developments. Those papers motivate the intrinsic metric but the inspected sections do not state the sharp all-dimensional fixed-vertex intrinsic/ambient distortion ratio or its unique equality locus. The result concerns chord--arc distortion rather than a geodesic count, a cut locus, an intrinsic radius, or a Euclidean simplex altitude alone. An earlier unindexed equivalent derivation remains possible; historical uniqueness is not certified.

## Limitations
The result is restricted to *regular* Euclidean simplices and a source at a vertex. It does not determine the supremum over two arbitrary boundary points. The proof is self-contained and analytic; the finite checker is supplementary. A historical-priority assessment is not an independent comprehensive literature audit.

## References
1. E. Miller and I. Pak, *Metric combinatorics of convex polyhedra: cut loci and nonoverlapping unfoldings*, 2003 preprint, arXiv:math/0312253v1, https://arxiv.org/abs/math/0312253.
2. D. Davis, V. Dods, C. Traub and J. Yang, *Geodesic trajectories on regular polyhedra*, 2015 preprint, arXiv:1508.03546v1, https://arxiv.org/abs/1508.03546.
3. R. Dyer, G. Vegter and M. Wintraecken, *Riemannian simplices and triangulations*, 2015, https://doi.org/10.1007/s10711-015-0069-5 (background on distinct intrinsic-simplex concepts; not an implication of this finding).
