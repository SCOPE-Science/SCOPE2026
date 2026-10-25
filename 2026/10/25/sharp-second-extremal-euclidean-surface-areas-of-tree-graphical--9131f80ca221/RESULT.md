# Sharp second-extremal Euclidean surface areas of tree graphical zonotopes

## Finding

For every integer \(n\ge4\), let \(T\) be a tree with vertex set \(\{1,\ldots,n\}\) and define its centered, intrinsic \((n-1)\)-dimensional graphical zonotope
\[
Z_T=\sum_{\{i,j\}\in E(T)}[-(e_i-e_j)/2,(e_i-e_j)/2]\subset H_n=\{x\in\mathbb R^n:\textstyle\sum_i x_i=0\}.
\]
All areas and volumes use the Euclidean metric inherited by \(H_n\). Write \(\mathcal S(T)=\mathcal H^{n-2}(\partial Z_T)\) for the total facet hypersurface measure and \(\mathcal V(T)=\mathcal H^{n-1}(Z_T)\). Let \(a_e\) and \(n-a_e\) be the vertex counts of the two components of \(T-e\), and write
\[
 f_n(k)=\sqrt{k(n-k)},\quad
 A_n=2(n-1)\sqrt{n-1},\quad
 B_n=2\sum_{k=1}^{n-1}\sqrt{k(n-k)},\quad
 \Delta_n=2\bigl(\sqrt{2(n-2)}-\sqrt{n-1}\bigr)>0.
\]
Then \(\mathcal V(T)=\sqrt n\) independently of the tree, and
\[
 \boxed{\mathcal S(T)=2\sum_{e\in E(T)}f_n(a_e).}
\]
The sharp first and *second* extremal shells are as follows (all equality classes are up to tree isomorphism):

1. \(A_n\le\mathcal S(T)\le B_n\). Equality on the left occurs exactly for the star \(K_{1,n-1}\), and equality on the right exactly for the path \(P_n\).
2. For every nonstar tree, \(\mathcal S(T)\ge A_n+\Delta_n\), with equality exactly for the star on \(n-1\) vertices with one pendant edge subdivided (equivalently the double star with adjacent nonleaf vertices and smaller-side order \(2\)).
3. For every nonpath tree, \(\mathcal S(T)\le B_n-\Delta_n\), with equality exactly for the unique three-arm tree whose arms have lengths \(1,1,n-3\). At \(n=4\) this is the star, while the second-minimizer is the path.

Consequently, the two extremal gaps are *exactly equal*, namely
\[
 \min_{T\not\cong K_{1,n-1}}\mathcal S(T)-\mathcal S(K_{1,n-1})
 =\mathcal S(P_n)-\max_{T\not\cong P_n}\mathcal S(T)=\Delta_n.
\]
The disparity of the extremes increases with dimension:
\[
 \boxed{\displaystyle\frac{\mathcal S(P_n)}{\mathcal S(K_{1,n-1})}\sim\frac\pi8\sqrt n.}
\]
Thus combinatorially identical parallelotopes of identical intrinsic volume have sharply different Euclidean boundary measures, including exact nearest-extremal gap identities.

## Assumptions and scope

Trees are finite, unweighted, simple, connected, and undirected. An arbitrary orientation of each edge fixes the incidence columns but does not change \(Z_T\). The generator segments have length \(\sqrt2\); using length-normalized segments instead would multiply hypersurface measures by \(2^{-(n-2)/2}\). Surface area is intrinsic \((n-2)\)-Hausdorff measure, not ambient \((n-1)\)-Hausdorff measure on the boundary. No claim is made for graphs with cycles, weighted generators, or other Euclidean embeddings. At \(n=3\) the path and star coincide; the strict second-shell statements therefore begin at \(n=4\).

## Proof

**Exact facet areas.** Orient the edges arbitrarily and form the \(n\times(n-1)\) incidence matrix \(B\) with one column \(e_u-e_v\) for each edge. The map \(z\mapsto Bz\) carries \([-1/2,1/2]^{n-1}\) bijectively onto \(Z_T\), because tree incidence columns are linearly independent. By Cauchy–Binet and leaf elimination, each of the \(n\) full-rank \((n-1)\times(n-1)\) minors of \(B\) has determinant \(\pm1\), hence \(\det(B^{\mathsf T}B)=n\). This proves \(\mathcal V(T)=\sqrt n\).

Fix an edge \(e\), and delete its column from \(B\), obtaining \(B_{-e}\). The two components of the remaining forest have orders \(a_e\) and \(n-a_e\). A maximal minor of its incidence matrix is nonzero precisely when one row is omitted in each component, and then its determinant is \(\pm1\). There are \(a_e(n-a_e)\) such row choices. Cauchy–Binet gives \(\det(B_{-e}^{\mathsf T}B_{-e})=a_e(n-a_e)\). Each of the two parallel facets corresponding to \(e\) is the image of a unit \((n-2)\)-cube under \(B_{-e}\), and therefore has area \(\sqrt{a_e(n-a_e)}\). Summing all \(2(n-1)\) facet areas gives the asserted identity. In particular, the formula is independent of the embedding labels or orientations.

**Minimum and the first gap.** For \(1\le k\le n-1\), \(f_n(k)\ge f_n(1)=\sqrt{n-1}\), with equality exactly when \(k\in\{1,n-1\}\). A tree with every edge pendant must be a star. This proves the lower bound and rigidity. Any nonstar tree has an edge splitting off at least two vertices on *both* sides. Since \(f_n(k)\ge f_n(2)\) for \(2\le k\le n-2\), all remaining \(n-2\) edges contribute at least \(f_n(1)\); hence the first nonstar gap is at least \(\Delta_n\). Equality forces exactly one nonpendant edge, which splits \(2\) versus \(n-2\), and every other edge pendant. The only such tree is the singly subdivided star, realizing equality. In the boundary case \(n=4\) the characterization remains valid.

**Strict branch-transfer lemma.** Consider a tree containing a vertex \(v\) of degree at least three. Let \(a\le b\le c\) be the orders of three smallest components of \(T-v\). Cut the edge connecting \(v\) to the component of order \(a\), and reconnect that component's former neighbor of \(v\) to a leaf in the component of order \(b\). This is again a tree with \(n\) vertices, and its number of leaves decreases by one. The sole changed split sizes are along the old path from \(v\) to the chosen leaf in the \(b\)-component: the side away from \(v\), previously of order \(s\) with \(1\le s\le b\), now has order \(s+a\). For each such edge,
\[
 f_n(s+a)^2-f_n(s)^2=a(n-2s-a)>0,
\]
because a third component has order at least \(b\), giving \(n\ge1+a+2b>2s+a\). All other cut products remain unchanged. Consequently the transformation **strictly increases** \(\mathcal S\) and decreases the leaf number by one. Repeating until exactly three leaves proves that every nonpath is strictly dominated by a three-arm tree unless it already has three leaves. A tree with exactly three leaves necessarily has one degree-three vertex and no vertex of greater degree.

**Maximizing among three-arm trees.** Let the three edge-lengths be \(1\le a\le b\le c\), with \(a+b+c=n-1\). The sum of half of the facet areas is
\[
 F_n(a)+F_n(b)+F_n(c),\qquad F_n(r)=\sum_{k=1}^{r}f_n(k).
\]
If \(a\ge2\), transferring one edge of the shortest arm to the longest changes the sum by \(f_n(c+1)-f_n(a)>0\), since
\[
 f_n(c+1)^2-f_n(a)^2=b(c+1-a)>0.
\]
Thus a maximizer has \(a=1\). If \(b\ge2\), transferring one edge from \(b\) to \(c\) changes the sum by \(f_n(c+1)-f_n(b)>0\), since
\[
 f_n(c+1)^2-f_n(b)^2=c+1-b>0.
\]
Hence the unique nonpath maximizer has arms \((1,1,n-3)\). Its area equals
\[
 2\left(2f_n(1)+\sum_{k=1}^{n-3}f_n(k)\right)
 =2\sum_{k=1}^{n-1}f_n(k)-2(f_n(2)-f_n(1))=B_n-\Delta_n,
\]
where the second equality uses \(f_n(n-2)=f_n(2)\) and \(f_n(n-1)=f_n(1)\).

**Maximum and asymptotics.** The same branch-transfer transformation strictly increases surface area of any nonpath tree (whether or not one stops at three leaves); eventual termination at a two-leaf tree, necessarily the path, proves the unique global maximum \(B_n\). Finally \(A_n\sim2n^{3/2}\), while the Riemann-sum limit gives
\[
 \frac{B_n}{2n^2}\longrightarrow\int_0^1\sqrt{x(1-x)}\,dx=\frac\pi8.
\]
These two limits yield the ratio stated above.

## Verification

The self-contained Python 3 program `verify.py` enumerates all Prüfer sequences on four through seven vertices and canonicalizes their unlabeled tree types. It checks both sharp extremal shells and their unique equality types for each resulting unlabeled tree. Independently, integer Bareiss determinants of the actual incidence-column Gram matrices check \(\det(B^{\mathsf T}B)=n\) and every deleted-edge formula \(\det(B_{-e}^{\mathsf T}B_{-e})=a_e(n-a_e)\). Run `python3 verify.py` from this package directory. The observed terminal marker was `VERIFY_OK 136 exact_Gram_and_extremality_checks`. These finite tests corroborate; they do not substitute for the all-dimensional proof.

## Relationship to prior work

The standard graphical-zonotope construction, cubical combinatorics for trees, and incidence-matrix volume formula are classical; the paper by Padrol, Pilaud, and Poullot provides a modern systematic account of deformations. The general spanning-forest Gram-minor formula already implies the displayed facet-area identity as an elementary specialization. The new assertion assessed here is instead the **full sharp first- and second-extremal surface-area ordering, both rigid near-extremizers, and equality of the two nearest-extremal gaps**, with a direct geometric proof.

A published result on directional-width variance of the same tree graphical zonotopes gives the *opposite* path-versus-star order: width variance is minimized by the path and maximized by the star. Neither width moment nor volume determines surface area. The 2019 literature on split-size functionals treats phylogenetic *leaf* bipartitions under degree constraints and is related to the branch-transfer argument, but does not state the above Euclidean vertex-split boundary-area result or the paired second-extremal gap. Search coverage does not establish absolute novelty; see the accompanying review for residual risks.

## Limitations

The exact surface formula is a straightforward consequence of known Gram-minor and forest principles and is not claimed as a standalone original theorem. All optimization statements concern unweighted trees and the canonical Euclidean embedding. The comparison with generalized split-size indices and possible unindexed earlier formulations of the *second-extremal* classification remain bibliographic uncertainties; independent verification has not been performed.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, first public arXiv posting 2021-11-24, arXiv:2111.12422, https://arxiv.org/abs/2111.12422 (definitions, graph zonotopes, and normal fans).
2. V. Grujić, *Counting Faces of Graphical Zonotopes*, arXiv:1604.06931, https://arxiv.org/abs/1604.06931 (face combinatorics).
3. A. Dall and J. Pfeifle, *A Polyhedral Proof of the Matrix Tree Theorem*, arXiv:1404.3876, https://arxiv.org/abs/1404.3876 (incidence matrices and spanning trees).
4. *Split Sizes and Extremal Tree Shapes*, *Advances in Applied Mathematics* 104 (2019), 135–164, DOI:10.1016/j.aam.2018.12.004 (tree split functionals, especially leaf cuts).
5. *Sharp Width-Variance Extremizers Among Tree Graphical Zonotopes*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269 (contrasting width statistic).
