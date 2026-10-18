# Sharp section complexity and generic vertex spectrum of cross-polytope prisms

## Finding
For every integer \(d\ge2\), let \(C_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\subset\mathbb R^d\) be the coordinate cross-polytope and let \(P_d=C_d\times[-1,1]\subset\mathbb R^{d+1}\). Among **all affine hyperplanes** \(H\), including supporting and nongeneric ones, the sharp vertex count is
\[
\boxed{\max_H f_0(P_d\cap H)=2d(d-1)+2.}
\]

There is also an exact classification of the **generic vertex-count spectrum** (generic means that \(H\) avoids all vertices of \(P_d\)). Define
\[
 g_d(s)=s(2d-s)-\min\{s,2d-s\}\qquad (0\le s\le2d).
\]
Then the complete set of positive vertex counts of nonempty generic sections is
\[
\boxed{\mathcal S_d=\{g_d(k)+g_d(\ell)+k-\ell:\ 0\le\ell\le k\le2d,\quad g_d(k)+g_d(\ell)+k-\ell>0\}.}
\]
Each integer pair in this formula is attained by a generic affine hyperplane, even if distinct pairs give the same count. After switching the prism's two levels if necessary so that the normal's last coordinate is nonnegative, every maximizing generic hyperplane has exactly \(d+1\) positive vertices at the upper level and \(d-1\) at the lower level. Conversely, every generic hyperplane with these two counts maximizes.

For example, \(\mathcal S_2=\{3,4,5,6\}\), while \(\mathcal S_3=\{5,6,8,9,10,11,12,13,14\}\): the value \(7\) is absent from the generic spectrum of the octahedral prism. The unrestricted maximum cut of the graph of \(P_d\) is \(2d^2+2d-2(d\bmod2)\), so its graph-cut maximum exceeds the maximum geometrically realizable by a generic affine hyperplane by \(4d-2-2(d\bmod2)\).

## Assumptions and scope
Hyperplanes are arbitrary affine codimension-one subspaces of \(\mathbb R^{d+1}\); empty intersections contribute zero vertices. All faces and vertices are Euclidean convex-polytope faces. A generic hyperplane contains no vertex of \(P_d\), but may otherwise be arbitrarily oriented or translated. The full \(\mathcal S_d\) statement is **only for generic sections**; the numerical maximum applies to all affine sections. Dimension parameter \(d\) is any integer at least \(2\). The cross-polytope and segment are in the exact coordinates above; affine equivalence preserves all stated face counts.

## Proof
**1. Edge-graph reduction.** The \(2d\) vertices of \(C_d\) form the graph \(K_{2d}\) with its \(d\) antipodal-pair edges removed: two distinct vertices are adjacent unless opposite. The graph of \(P_d\) comprises two copies of this graph plus \(2d\) vertical edges pairing equal vertices at the two levels. A generic section has one vertex in the relative interior of each original edge whose endpoints are strictly on opposite sides of \(H\), and no other vertices. Thus its vertex number equals the number of sign-changing original edges.

**2. A cross-polytope level.** Consider affine functional values \(a_i-b\) and \(-a_i-b\) at the pair \(\pm e_i\), with none zero, and suppose that \(s\) of all \(2d\) values are positive. If \(b>0\), at most one vertex of each antipodal pair is positive, so \(s\le d\) and exactly \(s\) antipodal pairs are split. If \(b<0\), at most one vertex of each pair is negative, so exactly \(2d-s\) pairs are split; for \(b=0\) every pair is split, giving \(s=d\). Among all \(s(2d-s)\) opposite-sign pairs in the complete graph, precisely \(\min\{s,2d-s\}\) are its deleted antipodal pairs. Therefore the number of crossed edges within this level is \(g_d(s)\).

**3. Exact prism count.** Write the hyperplane as \(\sum_{i=1}^d a_i x_i+t z=c\). Exchange the two levels if needed so that \(t\ge0\), and denote the positive-vertex counts on \(z=+1\) and \(z=-1\) by \(k\) and \(\ell\). Monotonicity of the functional in \(z\) gives \(0\le\ell\le k\le2d\). Precisely \(k-\ell\) of the vertical edges change sign. By step 2,
\[
 f_0(P_d\cap H)=g_d(k)+g_d(\ell)+k-\ell\qquad\text{for generic }H.
\]
This proves containment in the displayed spectrum, pending realizability.

**4. Sharp bound and generic equality.** For integers \(0\le s\le2d\), put \(A_d(s)=g_d(s)+s\) and \(B_d(s)=g_d(s)-s\). On \(s\le d\) one has
\[
 A_d(s)=s(2d-s)\le d^2,\qquad B_d(s)=s(2d-s-2)=d(d-2)+1-(s-d+1)^2.
\]
On \(s=d+p\), \(0\le p\le d\), one has
\[
 A_d(s)=d^2+1-(p-1)^2,\qquad B_d(s)=d(d-2)-p^2.
\]
It follows that the unique integer maximizer of \(A_d\) is \(s=d+1\), with \(A_d=d^2+1\), and the unique maximizer of \(B_d\) is \(s=d-1\), with \(B_d=d(d-2)+1\). Since the section count is \(A_d(k)+B_d(\ell)\), its sharp bound and generic equality criterion follow.

The hyperplane
\[
 H_* =\{(x,z):2\sum_{i=2}^d x_i+z=0\}
\]
avoids all vertices and has \((k,\ell)=(d+1,d-1)\), proving attainment for every \(d\ge2\).

**5. Every ordered count-pair occurs.** Fix integers \(0\le\ell\le k\le2d\). Use \(a_1,\ldots,a_d\ge0\) to denote the coordinates of the normal to the cross-polytope factor. The following four mutually exhaustive cases give an explicit choice of \((a_1,\ldots,a_d;t;c)\). Here \([q]^r\) means a list consisting of \(r\) copies of the integer \(q\), with empty lists allowed, and consecutive lists are concatenated.

* If \(k\le d\), use \(a=[6]^\ell[4]^{k-\ell}[2]^{d-k}\), \(t=1\), \(c=4\).
* If \(\ell\ge d\), use \(a=[2]^{\ell-d}[4]^{k-\ell}[6]^{2d-k}\), \(t=1\), \(c=-4\).
* If \(\ell<d<k\) and \((k-d)+\ell\le d\), put \(A=k-d\), \(B=\ell\), use \(a=[2]^A[4]^{d-A-B}[6]^B\), \(t=4\), \(c=1\).
* If \(\ell<d<k\) and \((k-d)+\ell>d\), put \(A=k-d\), \(B=\ell\), use \(a=[2]^{d-B}[4]^{A+B-d}[6]^{d-A}\), \(t=4\), \(c=-1\).

Every vertex functional value is a nonzero integer. Direct comparison with the two thresholds \(c-t\) and \(c+t\) yields exactly \(k\) and \(\ell\) positive vertices, respectively. Hence every pair (and all positive section counts it generates) is realized by a generic hyperplane. All four cases include their boundary integer parameters as written, so no hidden limit argument is needed.

**6. Nongeneric and supporting hyperplanes.** If a hyperplane contains original vertices, one can translate it sufficiently slightly toward a side containing some vertices of the polytope. Every previously cut edge remains cut; each original vertex in the section contributes a distinct, newly cut incident edge into the chosen side. Consequently the perturbed section has at least as many vertices and avoids the original vertices. This perturbation lemma is standard (De Loera–Lopez-Campos–Torres, Lemma 2.1), and applies as well to supporting sections by translating toward the interior. Thus the generic sharp upper bound also governs every nongeneric section.

**7. Comparison with abstract graph cuts.** In each base layer, the graph is \(K_{2d}\) minus a perfect matching. Its largest cut has exactly \(d^2-(d\bmod2)\) edges: a balanced split gives at most \(d^2\) complete-graph crossings and has at least one split antipodal pair for odd \(d\), whereas balanced groups of whole antipodal pairs yield equality for even \(d\); a balanced split with exactly one split pair yields equality for odd \(d\). The vertical matching adds at most \(2d\) crossings, and complementary balanced maximizing splits on the two levels attain all \(2d\) simultaneously. Hence \(\operatorname{MaxCut}(G(P_d))=2d^2+2d-2(d\bmod2)\), as stated.

## Verification
Run `python3 check_cross_prism.py` with Python 3 (standard library only). It reconstructs the prism's graph independently; compares raw edge-crossing counts with the closed formula for thousands of nondegenerate integer hyperplanes; verifies all \((k,\ell)\)-realization constructions in dimensions \(2\) through \(8\); tests the sharp maximizers; and checks many additional random exact-integer functionals through dimension \(10\). It also independently reconstructs the graph-cut benchmark in dimensions \(2\) through \(4\). Its finite checks corroborate, but do not replace, the general proof.

## Relationship to prior work
Ziegler's *Lectures on Polytopes* (first print editions released 29 November 1994) develops polytope graphs and products. Khovanskii (2006) studies combinatorics of hyperplane sections and general estimates for simple polytopes; his prism example concerns average face degrees of an ordinary polygonal prism, not the sharp section count of the cross-polytope prism. De Loera, Lopez-Campos and Torres (2024, later revised) study general upper bounds, section vertex sequences and especially cyclic polytopes and hypercubes; their Lemma 2.1 is used explicitly above. Birkemeyer, Brose, Brandenburg and Prün (2026), Proposition 3.6, show that affine sections of a prism correspond combinatorially to slabs of its base (or prisms over sections of its base). That general description does not state an all-dimensional sharp number or generic vertex spectrum for the cross-polytope base; the explicit signed-antipodal cut analysis here supplies those claims.

## Limitations
The full vertex-count spectrum is proved only for hyperplanes avoiding original prism vertices; nongeneric section spectra are not classified. The maximum, by contrast, includes all affine hyperplanes. There is no classification of face vectors beyond vertices, nor of metric section volumes. A historical equivalent of the explicit result could occur in older polytope or combinatorial optimization literature not inspected here; bibliographic priority is not independently certified. The finite checker establishes only its finite tests, not the infinite-dimensional statements.

## References
1. G. M. Ziegler, *Lectures on Polytopes*, Springer GTM 152, initial print release 1994-11-29, DOI: https://doi.org/10.1007/978-1-4613-8431-1 .
2. A. Khovanskii, *Combinatorics of Sections of Polytopes and Coxeter Groups in Lobachevsky Spaces* (2006), author-hosted: https://www.math.toronto.edu/askold/2006%20Coxeter%20Legacy.pdf .
3. J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419 (first posted 2024-12-17), https://arxiv.org/abs/2412.12419 .
4. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial Slicing Problems of Polytopes: How (Not) to Reconstruct a Polytope from Its Slices*, arXiv:2609.16195 (2026-09-14), https://arxiv.org/abs/2609.16195 .
