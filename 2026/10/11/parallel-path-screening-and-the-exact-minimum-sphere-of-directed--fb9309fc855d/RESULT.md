# Parallel-path screening and the exact minimum sphere of directed edge polytopes

## Finding

Let \(r\ge 2\), and choose positive integers \(\ell_1,\ldots,\ell_r\) with at most one \(\ell_i=1\) and \(L:=\max_i\ell_i\ge2\). Form a simple directed two-terminal graph \(G\) with common source \(s\), common sink \(t\), and \(r\) internally vertex-disjoint directed paths from \(s\) to \(t\), the \(i\)-th of length \(\ell_i\). Write its successive vertices as \(v_{i,0}=s,v_{i,1},\ldots,v_{i,\ell_i}=t\). Each internal vertex is distinct from all vertices on the other paths. Let
\[
P_G=\operatorname{conv}\{e_u-e_v:u\to v\text{ is an edge of }G\}\subset\mathbb R^{V(G)}
\]
with the standard Euclidean inner product. Put
\[
N=\frac{L^2}{2}+\frac1{12}\sum_{i=1}^r\ell_i(\ell_i-1)(\ell_i-2).
\]
Then the unique minimum enclosing Euclidean ball of \(P_G\) has squared radius
\[
\boxed{R(G)^2=2-\frac1N}
\]
and center \(c=z/N\), where
\[
z_s=L/2,\qquad z_t=-L/2,\qquad
z_{v_{i,j}}=\ell_i/2-j\quad(1\le j<\ell_i).
\]
All these statements hold in the ambient Euclidean space and, since \(c\in P_G\), also intrinsically in the affine span of the polytope.

The contacting polytope vertices are **exactly** the roots corresponding to all edges of the paths of maximum length \(L\), together with the nonterminal edges \(v_{i,j-1}\to v_{i,j}\) with \(2\le j\le\ell_i-1\) on every shorter path. Thus the exact number of contacts is
\[
\boxed{\sum_{\ell_i=L}\ell_i+\sum_{\ell_i<L}\max\{\ell_i-2,0\}.}
\]
All vertices contact if and only if all paths have the same length. On any path with \(2\le\ell_i<L\), its first and last edge-root vertices lie strictly inside the optimal ball, each with squared-radius deficit \((L-\ell_i)/N\). A shorter direct edge \(s\to t\) has squared-radius deficit \(2(L-1)/N\).

In particular, adding any number of fresh internally disjoint length-two paths (subject to maintaining a simple graph) **leaves the minimum enclosing radius unchanged** and leaves the old center coordinates unchanged (the new internal center coordinates are zero). Each new root is strictly inside the ball if \(L>2\), while it contacts the ball if \(L=2\). This gives a sharp contact-screening transition despite the strict enlargement of the polytope in the naturally enlarged coordinate space.

## Assumptions and scope

A length is the number of edges in a directed source-to-sink path, not the number of internal vertices. The graph has \(2+\sum_i(\ell_i-1)\) vertices and \(\sum_i\ell_i\) distinct edges. There are no other edges. At most one path has length one so no parallel edges occur. The coordinate vectors \(e_u\) are orthonormal, so every directed edge root has squared norm exactly \(2\). The smallest ball is taken over all possible Euclidean centers, not restricted a priori by graph symmetries or by the affine hull. The polytope need not be full dimensional in the zero-sum hyperplane: when all path lengths agree, it has an additional affine rank-function equation.

## Proof

**1. A feasible unit-gap potential.** Define \(z\) as in the theorem. Along every longest path its consecutive potential gaps are \(1\). On a shorter path of length \(\ell\ge2\), every internal edge (neither first nor last) has gap \(1\), while its first and last edges have gap
\[
1+\frac{L-\ell}{2}>1.
\]
If \(\ell=1\), the sole edge has gap \(L>1\). Hence \(z_u-z_v\ge1\) for every directed edge \(u\to v\), with the equality set described above.

**2. Exact nonnegative primal weights.** Let \(k=\#\{i:\ell_i=L\}\) and put \(\alpha_i=L/(2k)\) on a longest path and \(\alpha_i=0\) on a shorter one. Give its \(j\)-th directed edge the weight
\[
\lambda_{i,j}=\alpha_i+\frac{(j-1)(\ell_i-j)}2,
\qquad 1\le j\le\ell_i.
\]
These weights are nonnegative. A positive weight occurs exactly on an edge whose \(z\)-gap is \(1\): all the longest-path edges have strictly positive \(\alpha_i\), while on shorter paths the weights are positive exactly when \(2\le j\le\ell_i-1\). The signed incidence identity is
\[
\boxed{z=\sum_{i=1}^r\sum_{j=1}^{\ell_i}
\lambda_{i,j}(e_{v_{i,j-1}}-e_{v_{i,j}}).}
\]
Indeed, the source coordinate on the right is \(\sum_i\lambda_{i,1}=kL/(2k)=L/2\), the sink coordinate is its negative, and at an internal vertex \(v_{i,j}\) the coordinate is \(\lambda_{i,j+1}-\lambda_{i,j}=\ell_i/2-j\).

The polynomial identity
\[
\sum_{j=1}^{\ell}\frac{(j-1)(\ell-j)}2
=\frac{\ell(\ell-1)(\ell-2)}{12}
\]
shows that \(\sum_{i,j}\lambda_{i,j}=N\). Dotting the incidence identity with \(z\), and using that every positively weighted edge has gap \(1\), gives \(\|z\|^2=N\) independently. Consequently
\[
c=\frac zN=\sum_{i,j}\frac{\lambda_{i,j}}N(e_{v_{i,j-1}}-e_{v_{i,j}})
\]
is a convex combination of the edge roots, and \(\|c\|^2=1/N\).

**3. Exact containment and global optimality.** For any edge root \(a=e_u-e_v\),
\[
\|a-c\|^2=2+\frac1N-\frac{2(z_u-z_v)}N
\le2-\frac1N.
\]
Equality holds precisely when \(z_u-z_v=1\). Thus the proposed ball contains every vertex and hence the entire polytope.

Conversely, give each edge root probability \(\lambda_{i,j}/N\); its mean is \(c\). For an arbitrary proposed ball center \(y\in\mathbb R^{V(G)}\), the maximum squared distance over vertices is at least their weighted mean squared distance, namely
\[
\sum_{i,j}\frac{\lambda_{i,j}}N\|e_{v_{i,j-1}}-e_{v_{i,j}}-y\|^2
=2-\frac1N+\|y-c\|^2.
\]
This is at least \(2-1/N\), with equality possible only at \(y=c\). The ball found above is therefore globally minimal and its center is unique.

**4. Contacts, deficits, and invariance.** A vertex's squared-radius deficit is exactly
\[
R(G)^2-\|a-c\|^2=\frac{2(z_u-z_v-1)}N.
\]
The explicit gaps from Step 1 establish the complete contact list and the stated boundary-edge deficits. A newly added path of length two contributes \(2(2-1)(2-2)/12=0\) to \(N\), its one new coordinate of \(z\) equals \(2/2-1=0\), and the maximum length remains \(L\). Its two edge-root gaps equal \(L/2\), proving the claimed invariant radius and the sharp \(L=2\) contact threshold. The new root vertices are outside the old polytope's coordinate subspace, so the enlargement is strict.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic throughout. It reconstructs the graph, candidate potential, nonnegative edge weights, every incidence-coordinate equality, the norm and weight-sum identities, all vertex-distance inequalities, all claimed contacts and boundary deficits, and the invariance under adding a fresh length-two path. Its exhaustive parameter checks cover \(1{,}360\) admissible ordered path-length lists with two to four paths and lengths at most six, accounting for \(18{,}925\) edge-root instances. A further \(252\) exact tests check the length-two-path invariance. All passed. Separate constrained Euclidean quadratic minimizations on additional mixed-length instances agreed with the closed formula numerically; these are auxiliary cross-checks, not a proof in arbitrary dimensions. The general proof is the explicit feasible-potential and positive-weight certificate in the preceding section.

To reproduce the exact checks from a directory containing the file, execute `python3 verify.py`; it requires only the standard Python library. The output starts `EXACT_OK` and reports the instance, edge, contact and invariance counts.

## Relationship to prior work

Numata, Takahashi and Tamaki introduced the directed-edge-polytope definition used here and characterized its facets and dimensions using subquivers and rank functions [1]. Their 2022 primary publication does not evaluate minimum Euclidean enclosing spheres or the influence of source-to-sink path lengths. Kálmán and Tóthmérész study directed-graph root polytopes, focusing on semibalanced orientations and Ehrhart-theoretic dissections [2]. That framework includes the equal-length case but does not calculate the metric center or radius.

An independently published exact Ehrhart-polynomial calculation for arbitrarily oriented cycles [3] includes the two-path cycle special case of the present graphs. It determines lattice counts from directional edge counts; it does not assert minimum-enclosing Euclidean radius, path-screening, or the full multi-path contact locus. In particular, lattice equivalence and Euclidean congruence are different questions. Likewise, earlier minimum-sphere calculations for a transitive tournament and for a path with a reversed edge concern distinct underlying directed graphs and do not imply the arbitrary parallel-path theorem. When every path has the same length, the directed graph is graded, and the common-sphere calculation also follows from the standard graded-incidence potential and nonnegative-flow criterion; that covered special case is not presented as novel. Unequal lengths destroy the global unit-gap rank function, and the present formula resolves the resulting exact center, radius, and contact screening for every admissible length list. The equal-norm projection/dual-potential argument itself is a standard optimization principle; originality is claimed only for its explicit mixed-length evaluation and contact-screening classification on this family.

## Limitations

The theorem applies only to a simple two-terminal network consisting of internally disjoint directed paths with all arrows pointing from the same source to the same sink. It does not give the minimum sphere for general acyclic digraphs, networks with shared interior vertices, or arbitrary orientations of theta graphs. It treats the standard unweighted Euclidean metric on the incidence-coordinate vectors, not arbitrary edge lengths or weighted coordinate metrics. Published coverage of the same formula under discrete isotonic regression, maximum-margin graph embeddings, or optimization terminology cannot be categorically excluded; the targeted comparisons provide evidence, not an independent priority guarantee. The finite verification is not an exhaustive proof of the infinite-family claim.

## References

1. Y. Numata, Y. Takahashi, and D. Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1, first public version 2022-03-28, primary MSC2020 52B05, https://arxiv.org/abs/2203.14521.
2. T. Kálmán and L. Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960v1, first public version 2021-05-03; *Mathematika* 68 (2022), 1176–1220, https://arxiv.org/abs/2105.00960.
3. *Exact Ehrhart polynomials of oriented cycle root polytopes*, published published-finding corpus research record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ehrhart-polynomials-of-oriented-cycle-root-polytopes--e32575b66377.
