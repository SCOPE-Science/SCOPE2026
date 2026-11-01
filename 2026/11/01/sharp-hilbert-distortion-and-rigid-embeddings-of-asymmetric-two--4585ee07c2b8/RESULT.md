# Sharp Hilbert distortion and rigid embeddings of asymmetric two-cluster metrics

## Finding
Let \(A\) and \(B\) be disjoint, of sizes \(m,n\ge2\). Fix \(0<u,v\le2\), assign distance \(u\) to distinct points of \(A\), distance \(v\) to distinct points of \(B\), and distance \(1\) to every cross pair. Write
\[
L=\frac{m-1}{2m}u^2+\frac{n-1}{2n}v^2.
\]
The least Hilbert bi-Lipschitz distortion of this metric is precisely
\[
c_2(A\sqcup B)=\max\{1,\sqrt L\}.
\]
Every optimal embedding is uniquely determined up to a common positive scaling and Euclidean congruence. In the normalization where its minimum pairwise stretch equals one, the within-cluster distances remain \(u\) and \(v\), while every cross distance is \(\max\{1,\sqrt L\}\). The two clusters form mutually orthogonal regular simplices. The cluster centroids coincide for \(L\ge1\); for \(L<1\) their separation is exactly \(\sqrt{1-L}\), perpendicular to both simplex spans. The minimal affine Euclidean dimension among optimal embeddings equals \(m+n-2\) for \(L\ge1\) and \(m+n-1\) for \(L<1\).

For the natural graph metric of a complete split graph, comprising an independent set of size \(m\) fully joined to a clique of size \(n\), take \(u=2\), \(v=1\). Then
\[
c_2^2=\frac52-\frac2m-\frac1{2n}>1,
\]
and every optimal realization is an orthogonal pair of simplices centered at one point, in affine dimension \(m+n-2\). This evaluates an infinite family of non-distance-regular graph metrics.

## Assumptions and scope
All cardinalities are finite integers \(m,n\ge2\), the parameters are real \(0<u,v\le2\), and the target is a real Hilbert space of arbitrary dimension. The distance prescriptions satisfy the triangle inequality, because a within-cluster pair has an alternative path through the other cluster of length \(2\). For an injective map \(f\), its distortion is the ratio between maximum and minimum of \(\|f(x)-f(y)\|/d(x,y)\) over unequal points. Translating and scaling a map does not change distortion. We call the affine dimension the dimension of the affine span of its image, rather than its ambient Hilbert dimension.

## Proof
**Lower bound.** Normalize any Hilbert embedding with least pairwise stretch equal to one. Its maximum stretch is some \(C\ge1\). Denote the images of the clusters by \(x_1,\ldots,x_m\) and \(y_1,\ldots,y_n\), their centroids by \(\bar x,\bar y\), and their mean squared fluctuations by
\[
V_A=\frac1m\sum_i\|x_i-\bar x\|^2
=\frac1{m^2}\sum_{i<j}\|x_i-x_j\|^2
\ge\frac{m-1}{2m}u^2,
\]
\[
V_B=\frac1n\sum_j\|y_j-\bar y\|^2
\ge\frac{n-1}{2n}v^2.
\]
The variance identity holds in every real Hilbert space. Expanding the squared cross distances and using both centroid cancellations gives
\[
\frac1{mn}\sum_{i,j}\|x_i-y_j\|^2
=V_A+V_B+\|\bar x-\bar y\|^2
\ge L.
\]
Each cross distance originally equals one, so every squared term on the left is at most \(C^2\). Therefore \(C^2\ge L\), and normalization also yields \(C^2\ge1\).

**Attainment.** Construct a centered regular \(m\)-simplex of side length \(u\) in an \((m-1)\)-dimensional Euclidean subspace, and a centered regular \(n\)-simplex of side length \(v\) in an orthogonal \((n-1)\)-dimensional subspace. Their common squared circumradius sum is \(L\). If \(L\ge1\), give the simplices the same centroid. If \(L<1\), translate one centroid by \(\sqrt{1-L}\) along a further axis perpendicular to both subspaces. Every within-cluster distance remains \(u\) or \(v\), and every cross distance is \(\sqrt{\max\{1,L\}}\). Hence the distortion is exactly \(\max\{1,\sqrt L\}\). The construction has the asserted affine dimensions.

**Rigidity and minimum dimension.** Suppose an embedding attains the bound, scaled to minimum stretch one. For \(L\le1\), its distortion equals one; hence it reproduces all original distances, so both cluster simplices are regular and all cross distances equal one. For \(L>1\), equality must hold at every stage in the displayed chain \(C^2\ge V_A+V_B+\|\bar x-\bar y\|^2\ge L\): every within-cluster pair realizes its lower stretch, \(\bar x=\bar y\), and every cross pair realizes its upper stretch. Thus again both simplices are regular and all cross distances are constant.

To identify relative position, write \(a_i=x_i-\bar x\), \(b_j=y_j-\bar y\), and \(h=\bar x-\bar y\). For any four indices, the equality of cross squared distances implies
\[
0=\|x_i-y_j\|^2-\|x_k-y_j\|^2
-\|x_i-y_\ell\|^2+\|x_k-y_\ell\|^2
=-2\langle a_i-a_k,b_j-b_\ell\rangle.
\]
Thus the two within-cluster difference spans are orthogonal. Since each regular simplex has equal circumradius, the equality of cross distances as one index varies yields \(\langle h,a_i-a_k\rangle=\langle h,b_j-b_\ell\rangle=0\). Finally, the cross squared distance equals \(L+\|h\|^2\). Therefore \(\|h\|^2=\max\{0,1-L\}\), and the two regular simplices and their center displacement are unique up to global orthogonal isometry. Their difference spans have dimensions \(m-1\) and \(n-1\) and are perpendicular; if \(L<1\), their nonzero center displacement contributes exactly one additional perpendicular dimension. This proves the asserted minimum dimension and complete rigidity.

**Split-graph corollary.** The independent class has pairwise graph distances two, the clique has pairwise distances one, and all joining pairs have distance one. Thus \(L=4(m-1)/(2m)+(n-1)/(2n)=5/2-2/m-1/(2n)\). This exceeds one for every \(m,n\ge2\) (its smallest value occurs at \(m=n=2\), giving \(L=5/4\)). The formula and dimension statement follow.

## Verification
The included standalone Python program `verify_two_cluster_distortion.py` tests exact rational variance identities, the squared-distance Gram ranks of constructed optimal configurations in hundreds of small parameter instances, the three-dimensional parameter regimes, and the split-graph corollary. It requires only the Python standard library. Finite tests corroborate but do not replace the universal proof above.

## Relationship to prior work
The work of Sánchez on supremal negative type provides early context for Hilbert embeddability of finite metrics, and Robertson's Theorem 4.3 explicitly treats Hilbert distortion of ordinary complete bipartite graph metrics (a symmetric diagonal subfamily with equal same-part distances). That result uses orthogonal simplices, a related proof mechanism. It neither covers independently variable within-cluster distances nor derives the universal optimizer-rigidity and affine-dimension bifurcation for this asymmetric family. Vallentin's work addresses distance-regular graphs by a different semidefinite/spectral method; complete split graphs are generally not distance-regular. Deza and Grishukhin analyze two-distance hypermetric spaces, a separate exact-distance question; the current asymmetric family generally has three nonzero distance values. These antecedents are acknowledged, and a literature search cannot rule out all differently formulated equivalent results.

## Limitations
All clusters are internally equidistant and all cross distances equal one, with at least two points per cluster. The conclusion does not classify arbitrary cluster geometries, varying cross distances, distortions into non-Hilbert targets, or Banach–Mazur distances of associated Lipschitz-free spaces. Rigidity refers to optimal finite point configurations, not uniqueness of linear extensions outside their affine hull. The numerical checks are finite diagnostics only.

## References
1. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (publicly posted August 2, 2011), https://arxiv.org/abs/1108.0451.
2. Gavin Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, arXiv:2309.16070v1 (publicly posted September 27, 2023), Theorem 4.3, https://arxiv.org/abs/2309.16070.
3. Frank Vallentin, *Optimal Embeddings of Distance Regular Graphs into Euclidean Spaces*, arXiv:math/0509716v1 (posted September 30, 2005), https://arxiv.org/abs/math/0509716.
4. Michel Deza and Viatcheslav Grishukhin, *Hypermetric Two-Distance Spaces* (2000), https://micheldeza.altervista.org/withSlava/two-dist/htd.pdf.
