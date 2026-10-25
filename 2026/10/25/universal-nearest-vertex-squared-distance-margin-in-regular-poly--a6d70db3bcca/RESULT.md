# Universal nearest-vertex squared-distance margin in regular polytopes

## Finding
Let \(P\) be any full-dimensional regular convex Euclidean polytope of dimension \(d\ge2\) and edge length \(s>0\). Let \(X\) be uniformly distributed by volume in \(P\), and let \(D_1(X)\le D_2(X)\) be the smallest two distances from \(X\) to *distinct vertices* of \(P\), counting ties with multiplicity. Then the normalized squared-distance margin
\[
Z=\frac{D_2(X)^2-D_1(X)^2}{s^2}
\]
has the dimension-only distribution \(\operatorname{Beta}(1,d)\). In particular, for every \(0\le t\le1\),
\[
\Pr\{Z>t\}=(1-t)^d,\quad f_Z(t)=d(1-t)^{d-1},\quad
\mathbb E[Z^k]=\frac{k!\,d!}{(d+k)!}\ \ (k=0,1,\ldots).
\]
The result is independent of the combinatorial type of \(P\) and includes all regular polygons, Platonic solids, and regular higher-dimensional polytopes. It does not concern the difference of unsquared distances.

## Assumptions and scope
A regular convex polytope has transitive flags under its full Euclidean isometry group. All vertices lie on a sphere with center \(o\), and all edges have the same length \(s\). A complete flag is a chain \(F_0\subset F_1\subset\cdots\subset F_d=P\), where \(\dim F_j=j\). Write \(c_F\) for the center (equivalently, vertex centroid) of a face \(F\), and \(c_P=o\). Uniformity means normalized \(d\)-dimensional Lebesgue measure. Flag-simplex boundaries have measure zero; all conclusions and the tie-breaking issue are consequently unaffected by them.

## Proof
**Face-center lemma.** For every nonempty proper face \(F\) of a regular convex polytope, its center \(c_F\) lies on a positive outward normal ray exposing \(F\): the vertices in \(F\) are precisely the maximizers of \(\langle c_F-o,w-o\rangle\) over all vertices \(w\). To see this, take the sum of outward facet-normal vectors for the facets containing \(F\). It belongs to the relative interior of the normal cone of \(F\), and is invariant under the subgroup of Euclidean symmetries preserving \(F\). The standard flag-reflection symmetry of a regular polytope identifies the fixed ray of that subgroup directed away from the polytope center with the ray \(\mathbb R_{>0}(c_F-o)\): successive reflections in the characteristic-orthoscheme mirrors fix exactly this ray. The sum is nonzero because its scalar product with \(c_F-o\) is positive. Thus it is a positive multiple of \(c_F-o\), proving the exposure claim. Since every vertex \(w\) lies at the same squared radius from \(o\),
\[
\|c_F-w\|^2=\|c_F-o\|^2+\|w-o\|^2-2\langle c_F-o,w-o\rangle.
\]
Consequently the vertices of \(F\), and no others, are the nearest vertices to \(c_F\). At \(c_P=o\), all vertices tie.

**Characteristic simplices.** The barycentric subdivision decomposes \(P\), up to null boundaries, into characteristic simplices
\[
S_{\mathcal F}=\operatorname{conv}(c_{F_0},c_{F_1},\ldots,c_{F_d})
\]
indexed by complete flags \(\mathcal F\). Each such simplex has positive volume. Fix a flag with \(F_0=\{v\}\) and \(F_1=[v,u]\), an edge. At its first corner \(c_{F_0}=v\), \(v\) is the unique nearest vertex and \(u\) is a second-nearest vertex. Indeed, an edge is a shortest nonzero vertex-pair chord of a convex regular polytope: any other vertex is at distance at least its edge length \(s\) from \(v\). At every other corner \(c_{F_j}\), \(j\ge1\), both \(u\) and \(v\) belong to \(F_j\), hence they tie for the nearest-vertex distance by the lemma.

For any fixed vertices \(a,b\), the squared-distance difference \(x\mapsto\|x-a\|^2-\|x-b\|^2\) is affine. Evaluating these differences at the \(d+1\) characteristic-simplex corners and using the preceding nearest-site order shows throughout \(S_{\mathcal F}\) that \(v\) remains a nearest vertex and \(u\) remains a second-nearest vertex. If the point has barycentric coordinates \(x=\sum_{j=0}^{d}\lambda_jc_{F_j}\), the affine squared-distance gap is \(s^2\) at \(c_{F_0}\), zero at the other \(d\) corners, and therefore
\[
D_2(x)^2-D_1(x)^2=\|x-u\|^2-\|x-v\|^2=s^2\lambda_0.
\]

**Distribution.** Conditioned on uniform \(X\) in any one of the simplices \(S_{\mathcal F}\), its barycentric coordinate vector has the \(\mathrm{Dirichlet}(1,\ldots,1)\) law. Hence \(\lambda_0\sim\mathrm{Beta}(1,d)\). Because the conditional distribution is identical on every characteristic simplex, their volume-weighted mixture is the same law throughout \(P\). This proves the density, tail, and moment identities, including at the endpoint thresholds by continuity.

## Verification
The attached standalone `verify.py` evaluates distances to every vertex at independently sampled uniform interior points for regular polygons, simplices, cubes, cross-polytopes, the icosahedron and dodecahedron, compares sample means and median-threshold survival proportions to the exact beta law, and reports Kolmogorov–Smirnov tests. `checks.log` records actual run output. These tests only corroborate the analytic proof; they cannot prove it in untested dimensions or polytope types. The proof itself is exact and dimension-uniform.

## Relationship to prior work
Khalid and Durrani study distance distributions for randomly sampled sites in regular polygons, including nearest-*random-neighbor* order statistics. Those sites are not the fixed polygon vertices, and their formulas do not give the difference between the two smallest squared distances to those vertices. Kabluchko, Litvak and Zaporozhets study mean width and Gaussian extrema for regular polytopes, with different sampling and statistics. Standard characteristic-orthoscheme and Dirichlet-barycentric facts supply the geometric and probabilistic tools; the common first–second squared-distance margin law is the claimed combination.

## Limitations
The theorem assumes a full-dimensional *regular* convex Euclidean polytope and volume-uniform sampling. No claim is made for arbitrary convex bodies, arbitrary vertex sets, nonuniform samples, unsquared-distance gaps, or geodesic distances. Its originality is conditional on the accessible indexed literature; unindexed equivalent work cannot be excluded. No independent audit has been performed.

## References
1. Z. Khalid and S. Durrani, *Distance Distributions in Regular Polygons*, first public arXiv submission 25 July 2012, arXiv:1207.5857, https://arxiv.org/abs/1207.5857.
2. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, https://arxiv.org/abs/1511.08479.
3. H. S. M. Coxeter, *Regular Polytopes*, 3rd edition, Dover, 1973 (standard regular-polytope and characteristic-orthoscheme background; book not inspected in full).
