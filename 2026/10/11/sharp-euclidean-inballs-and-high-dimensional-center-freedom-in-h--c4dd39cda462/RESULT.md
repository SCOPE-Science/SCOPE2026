# Sharp Euclidean inballs and high-dimensional center freedom in hypercube symmetric edge polytopes

## Finding
For every integer \(d\ge2\), let \(V=\{0,1\}^d\), \(N=2^d\), and let \(Q_d\) join pairs at Hamming distance one. On the intrinsic Euclidean space
\[
H=\left\{z\in\mathbb R^V:\sum_{u\in V}z_u=0\right\},
\]
consider the symmetric edge polytope
\[
P_d=\operatorname{conv}\left\{\pm(e_u-e_v):\{u,v\}\in E(Q_d)\right\}.
\]
Define \(\chi_j(u)=(-1)^{u_j}\), \(E_1=\operatorname{span}\{\chi_1,\ldots,\chi_d\}\subset H\), and \(M=d2^{d-2}\). The radius of any largest inscribed Euclidean ball in \(P_d\) is exactly
\[
r_d=M^{-1/2}=\frac{2}{\sqrt{d2^d}}.
\]
Precisely \(2^d\) facets touch the origin-centered maximum-radius ball. Their polar normals are
\[
f_\sigma(u)=\tfrac12\sum_{j=1}^d\sigma_j\chi_j(u),\qquad \sigma\in\{-1,1\}^d.
\]
Let \(\mathcal C_d\) be the set of centers of *all* inscribed balls having radius \(r_d\). Then
\[
\operatorname{aff}(\mathcal C_d)=H\cap E_1^\perp,
\qquad \dim\mathcal C_d=2^d-d-1.
\]
In particular, every \(d\ge2\) admits a positive-dimensional family of distinct optimal centers, despite the explicit finite set of contact facets.

## Assumptions and scope
All Euclidean notions use the standard dot product on coordinates indexed by vertices of \(Q_d\), restricted to \(H\); changing coordinates by a non-isometric linear map changes the result. The graph is the ordinary unweighted Boolean cube, not the geometrical cube polytope or its graphical zonotope. All claims quantify over every integer \(d\ge2\). A facet touching the origin-centered ball means that the supporting hyperplane has distance \(r_d\) from the origin.

Let \(K_d=P_d^\circ\) denote the polar *in the space* \(H\). Since \(Q_d\) is connected and its edge-root vectors span \(H\), \(0\) lies in the interior of \(P_d\), and
\[
K_d=\{f\in H:|f_u-f_v|\le1\text{ for every }\{u,v\}\in E(Q_d)\}.
\]
A polar vertex \(f\) corresponds to a unique facet \(\langle f,z\rangle\le1\) of \(P_d\), at distance \(1/\|f\|_2\) from the origin.

## Proof
**Spectral radius bound and all equality cases.** The combinatorial Laplacian \(L\) of \(Q_d\) has Walsh-character eigenvectors \(\chi_S(u)=(-1)^{\sum_{j\in S}u_j}\), with eigenvalues \(2|S|\). Thus, for any mean-zero \(f\in H\),
\[
2\|f\|_2^2\le\langle f,Lf\rangle
=\sum_{\{u,v\}\in E(Q_d)}(f_u-f_v)^2.
\]
If \(f\in K_d\), all edge differences have absolute value at most one. There are exactly \(d2^{d-1}\) edges, hence
\[
\|f\|_2^2\le\tfrac12 d2^{d-1}=d2^{d-2}=M.
\]
Equality requires \(f\in E_1\) and equality for every edge-difference bound. Writing \(f=\sum_{j=1}^d a_j\chi_j\), the difference on any edge in coordinate \(j\) is \(\pm2a_j\). Consequently each \(|a_j|=1/2\). Conversely every \(f_\sigma\) displayed above belongs to \(K_d\) and has norm squared \(M\). Every one of its edge inequalities is tight, so the set of tight edge-root normals spans \(H\); therefore each \(f_\sigma\) is indeed a polar vertex. These are exactly the norm-maximizing polar vertices.

**Global optimal radius and contact facets.** The ball \(rB_2(H)\) centered at zero lies in \(P_d\) precisely when \(r\|f\|_2\le1\) for every polar vertex \(f\). The preceding step gives the sharp centered radius \(r_d=1/\sqrt M\), and identifies all \(2^d\) facets tangent to this ball. No off-center ball can have larger radius: for any \(f_\sigma\), the two opposite valid facet inequalities give
\[
\langle f_\sigma,c\rangle+R\sqrt M\le1,
\qquad -\langle f_\sigma,c\rangle+R\sqrt M\le1,
\]
so \(R\le1/\sqrt M\) for every proposed ball center \(c\).

**Upper bound for center freedom.** If \(c\) is a center of a ball of the sharp radius, both displayed inequalities must hold with \(R=r_d\), forcing \(\langle c,f_\sigma\rangle=0\) for every sign vector. Those \(2^d\) vectors span exactly \(E_1\): averaging against \(\sigma_j\) recovers a nonzero scalar multiple of \(\chi_j\). Therefore
\[
\mathcal C_d\subset H\cap E_1^\perp.
\]

**Sharpness of the affine dimension.** A vertex \(f\) of \(K_d\) has a set of tight graph edges whose incidence vectors span \(H\); otherwise a nonzero mean-zero perturbation orthogonal to all tight edge vectors would preserve every inequality for sufficiently small positive and negative perturbations, contradicting extremality. A spanning tree of tight edges therefore exists. Setting a root potential to zero, all values on this tree are integers, since each tight difference equals \(\pm1\). Thus \(f_u=m_u-\overline m\) for integers \(m_u\), and
\[
\|f\|_2^2=\sum_um_u^2-\frac{(\sum_um_u)^2}{N}\in\frac1N\mathbb Z.
\]
Because \(M=d2^{d-2}\) is an integer, every polar vertex other than the \(f_\sigma\) has norm squared at most \(M-1/N\). Fix \(\varepsilon=1/(2NM^{3/2})\). If \(c\in H\cap E_1^\perp\) and \(\|c\|_2\le\varepsilon\), then for each contact vertex \(f_\sigma\), \(\langle f_\sigma,c\rangle+r_d\|f_\sigma\|_2=1\). For every other polar vertex \(f\), Cauchy–Schwarz and \(\sqrt{1-t}\le1-t/2\) for \(0\le t\le1\) give
\[
\begin{aligned}
\langle f,c\rangle+r_d\|f\|_2
&\le\varepsilon\sqrt M+\sqrt{1-\tfrac1{NM}}\\
&\le\frac1{2NM}+1-\frac1{2NM}=1.
\end{aligned}
\]
All polar inequalities therefore contain \(c+r_dB_2(H)\), proving \(c\in\mathcal C_d\). Hence \(\mathcal C_d\) contains a relative Euclidean ball of positive radius in \(H\cap E_1^\perp\). This space has dimension \(N-1-d\), establishing the exact affine hull and dimension. Since \(N-1-d>0\) for every \(d\ge2\), the center is never unique. \(\square\)

## Verification
The exact-enumeration script `verify_hypercube.py` requires only Python 3's standard library. Run `python3 verify_hypercube.py`. It exhaustively generates all integer tight-edge polar potentials for \(d=2,3,4\), checks the total polar vertex counts \(6,38,990\), verifies exact squared norms, determines the \(2^d\) maximizing normals, checks the rank \(d\) of their span, and tests an explicit nonzero degree-two Walsh displacement of size \(1/1000\) against every polar facet inequality using rational arithmetic. All checks passed for each dimension. The proof above, not the three finite cases, establishes the statements for arbitrary \(d\).

## Relationship to prior work
D'Alì, Delucchi and Michałek (arXiv:1910.05193, especially Lemma 4.5 and the general facet criterion) determine key combinatorial properties and integral facet potentials of connected bipartite symmetric edge polytopes. Çelik, Jamneshan, Montúfar, Sturmfels and Venturello (arXiv:2003.06725, Section 4, Proposition 10) explicitly describe polar vertices for the cube's Hamming metric and give total counts \(6,38,990\) in the first three cases studied here; these known counts are not presented as novel. Chen, Davis and Korchevskaia (arXiv:2107.12315) study facet subgraphs in general. The present finding is the Euclidean norm optimization over those potentials and the complete affine-hull classification of all largest-ball centers. Known combinatorial descriptions supply starting data but do not, by themselves, evaluate these Euclidean quantities. A formulation through the Lipschitz polytope or finite optimal transport is mathematically equivalent and was included in the overlap search.

## Limitations
This result classifies the contact facets of the origin-centered optimum and the affine hull, not the entire face lattice, of the optimal-center set. It does not count all noncontact facets in general or assert a novel enumeration of polar vertices. The exact geometry depends on the standard unweighted coordinate Euclidean metric. Independent external assessment of originality and proof has not been performed; related work under alternative terminology may exist.

## References
1. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first posted 2019-10-11. https://arxiv.org/abs/1910.05193
2. T. Ö. Çelik, A. Jamneshan, G. Montúfar, B. Sturmfels, L. Venturello, *Wasserstein Distance to Independence Models*, arXiv:2003.06725, first posted 2020-03-15; Section 4. https://arxiv.org/abs/2003.06725
3. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first posted 2021-07-26. https://arxiv.org/abs/2107.12315
