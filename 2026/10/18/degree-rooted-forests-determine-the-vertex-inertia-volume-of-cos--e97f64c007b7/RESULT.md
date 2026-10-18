# Degree-rooted forests determine the vertex-inertia volume of cosmological polytopes

## Finding

Let \(G\) be any finite connected **simple** graph with \(n\ge 2\) vertices and \(m\ge 1\) edges. Give its cosmological polytope the standard coordinate realization in \(\mathbb R^{n+m}\) and the uniform discrete measure on its \(3m\) vertices. Let \(\Sigma_G\) be the ambient covariance matrix of that measure, \(D\) the diagonal vertex-degree matrix, and \(A\) the adjacency matrix. Write \(\det{}^*\) for the product of the positive eigenvalues, with no extra determinant-normalization factor.

**The vertex-inertia determinant is exactly a graph's degree-rooted forest polynomial:**

\[
\boxed{\det{}^*\Sigma_G=\frac{n+m}{m^{n+m}}\left(\frac49\right)^n\det(2D-A).}
\]

Here \(2D-A\) is positive definite and has the equivalent positive expansion

\[
\boxed{\det(2D-A)=\sum_{F\subseteq E(G)\,\mathrm{acyclic}}\prod_{C\in\operatorname{Comp}(V(G),F)}\left(\sum_{v\in C}d_v\right).}
\]

For the star and path on \(n\ge 2\) vertices, the respective graph determinants are

\[
\det(2D_{\rm star}-A_{\rm star})=3(n-1)2^{n-2},
\qquad
\det(2D_{\rm path}-A_{\rm path})=\frac{\sqrt3}{2}\left((2+\sqrt3)^{n-1}-(2-\sqrt3)^{n-1}\right).
\]

Therefore the pseudodeterminant ratio of the path to the star is

\[
\boxed{\frac{\det{}^*\Sigma_{\rm path}}{\det{}^*\Sigma_{\rm star}}\sim\frac{1}{\sqrt3(n-1)}\left(\frac{2+\sqrt3}{2}\right)^{n-1}.}
\]

In particular the volume ratio of the respective intrinsic *vertex-inertia ellipsoids* (defined below) grows exponentially, with logarithmic growth rate

\[
\lim_{n\to\infty}\frac1n\log\frac{\operatorname{vol}(E_{\rm path})}{\operatorname{vol}(E_{\rm star})}=\frac12\log\left(\frac{2+\sqrt3}{2}\right)>0.
\]

This holds although their cosmological polytopes have equal Euclidean \((2n-2)\)-volume, \(4^{n-1}\sqrt{2n-1}/(2n-2)!\), and have their vertices on the same-radius Euclidean sphere around the all-ones coordinate center. The equality of polytope volumes follows from the established tree-volume theorem and is not asserted as new.

Even the degree sequence and the covariance trace need not determine vertex inertia. Two six-vertex trees with the same sorted degree sequence \((1,1,1,2,2,3)\) have graph determinants \(492\) and \(483\), and thus have different vertex-inertia ellipsoid volumes by the exact ratio \(\sqrt{164/161}\) despite equal trace.

## Assumptions and scope

The graph is undirected, connected, simple, and without isolated vertices; its vertices are labeled \(0,\ldots,n-1\), and its \(m\) edges are indexed. Equip \(\mathbb R^{n+m}\) with the standard Euclidean inner product, with basis \(x_v\) for graph vertices and \(y_e\) for graph edges. For an edge \(e=\{u,v\}\), use exactly the three polytope vertices

\[
p_e^0=x_u+x_v-y_e,\quad p_e^u=x_u-x_v+y_e,\quad p_e^v=-x_u+x_v+y_e.
\]

They are the distinct actual vertices of the standard cosmological polytope \(\mathcal P_G\). The affine dimension is \(n+m-1\) and the affine hull is \(\mathbf1^{\mathsf T}z=1\). Put \(K=3m\), \(N=n+m\), and \(\mu=K^{-1}\sum_{p\in\operatorname{vert}(\mathcal P_G)}p\). The covariance is

\[
\Sigma_G=\frac1K\sum_{p\in\operatorname{vert}(\mathcal P_G)}(p-\mu)(p-\mu)^{\mathsf T}.
\]

Its kernel is exactly the span of \(\mathbf1\). The *vertex-inertia ellipsoid* means the affine ellipsoid

\[
E_G=\{\mu+z:\mathbf1^{\mathsf T}z=0,\ z^{\mathsf T}\Sigma_G^+z\le1\},
\]

where \(\Sigma_G^+\) is the Moore–Penrose pseudoinverse. Its intrinsic Euclidean volume is \(\kappa_{N-1}\sqrt{\det{}^*\Sigma_G}\), where \(\kappa_d\) is the volume of the Euclidean unit \(d\)-ball. **This inertia ellipsoid is not claimed to be the John ellipsoid or the Löwner ellipsoid of the polytope**, nor is the covariance that of uniform volume measure on its interior.

## Proof

**1. The exact moment block matrix.** Let \(B\) be the unsigned \(n\times m\) edge-vertex incidence matrix. Summing the outer products of the three indicated points for each edge gives

\[
M:=\sum_p pp^{\mathsf T}=\begin{pmatrix}3D-A&-B\\-B^{\mathsf T}&3I_m\end{pmatrix}.
\]

Each point has coordinate sum one; hence \(M\mathbf1=K\mu\) and \(\mathbf1^{\mathsf T}M\mathbf1=K\). The incidence identity \(BB^{\mathsf T}=D+A\) and the Schur-complement formula yield

\[
\det M=3^m\det\left(3D-A-\frac13(D+A)\right)=3^m\left(\frac43\right)^n\det(2D-A).
\]

The matrix \(2D-A=D+(D-A)\) is positive definite because all degrees are positive and the graph Laplacian \(D-A\) is positive semidefinite. Therefore \(M\) is positive definite. Since all generating points have sum one, positive definiteness proves that their affine span is the entire stated hyperplane and the covariance has rank \(N-1\).

**2. Centering determinant identity.** For any positive-definite \(N\times N\) matrix \(M\), any nonzero vector \(h\), and \(\alpha=h^{\mathsf T}Mh\), set

\[
S=M-\frac{Mhh^{\mathsf T}M}{\alpha}.
\]

Then \(S\) is positive semidefinite with kernel \(\mathbb Rh\), and

\[
\det{}^*S=\frac{\|h\|^2\det M}{\alpha}.
\]

Indeed the coefficient of \(t\) in \(\det(S+t hh^{\mathsf T}/\|h\|^2)\) is \(\det{}^*S\). A rank-two determinant-lemma computation on \(M-Mhh^{\mathsf T}M/\alpha+t hh^{\mathsf T}/\|h\|^2\) makes that determinant equal to \(t\|h\|^2\det M/\alpha\) *exactly*, for every \(t\).

Taking \(h=\mathbf1\), \(\alpha=K\), and \(\Sigma_G=S/K\), there are \(N-1\) positive eigenvalues; therefore

\[
\det{}^*\Sigma_G=\frac{N\det M}{K^N}=\frac{n+m}{m^{n+m}}\left(\frac49\right)^n\det(2D-A).
\]

**3. The rooted-forest expansion.** Write \(L=D-A\) and choose an oriented incidence matrix \(C\), so \(L=CC^{\mathsf T}\). Then \(2D-A=L+D\) is the Gram matrix of the horizontal concatenation of \(C\) with \(\operatorname{diag}(\sqrt{d_v})\). The Cauchy–Binet formula expands its determinant over choices of columns. A choice is nonzero precisely when the selected edge columns form a forest and precisely one weighted root column is chosen in each forest component. Its squared determinant is the product of the corresponding root degrees. Sum first over roots in each component to obtain the asserted product of degree sums. This is an instance of the established weighted matrix–forest mechanism, applied here to the vertex-inertia determinant.

**4. Stars, paths, and exponential separation.** For a star, separate the degree-\(n-1\) center from its \(n-1\) leaves in the matrix \(2D-A\). Schur-complementing the leaf diagonal \(2I\) gives \(2^{n-1}(2(n-1)-(n-1)/2)=3(n-1)2^{n-2}\).

For a path, \(2D-A\) is tridiagonal, with diagonal \(2\) at the endpoints and \(4\) at interior vertices, and off-diagonal \(-1\). Its determinants \(q_n\) satisfy \(q_2=3\), \(q_3=12\), \(q_n=4q_{n-1}-q_{n-2}\) for \(n\ge4\). Solving yields the displayed closed form. All covariance prefactors are equal between the two trees for each fixed \(n\), giving the pseudodeterminant ratio and its asymptotic. The inertia-ellipsoid volume ratio is its square root, and the claimed logarithmic limit follows.

For any tree with \(n\) vertices, the established normalized volume of \(\mathcal P_T\) is \(4^{n-1}\). The standard integral lattice in its hyperplane has Euclidean covolume \(\sqrt{2n-1}\), giving the asserted common Euclidean volume. Every polytope vertex satisfies \(\|p\|^2=3\) and \(\mathbf1^{\mathsf T}p=1\); therefore all lie at squared distance \(3-1/(2n-1)\) from the point \(\mathbf1/(2n-1)\). These volume and sphere statements do not identify a common covariance: the covariance is centered at the vertex barycenter, not at that sphere center.

**5. Two degree-sequence twins.** Take the trees with edge sets

\[
\begin{aligned}
E(T_a)&=\{01,12,13,04,45\},\\
E(T_b)&=\{01,12,03,05,34\}.
\end{aligned}
\]

Both have degree multiset \(\{1,1,1,2,2,3\}\). Direct six-by-six integer determinants, reproducible in `CHECKER.py`, give \(\det(2D_a-A_a)=492\) and \(\det(2D_b-A_b)=483\). Their inertia-ellipsoid volume ratio is \(\sqrt{492/483}=\sqrt{164/161}\). Moreover \(\operatorname{tr}\Sigma_G=3-(\sum_vd_v^2+m)/(3m)^2\), so both trees have the same trace \(26/9\), completing the stronger separation.

## Verification

Run the included standalone `CHECKER.py` under Python 3.9 or later; it uses only the standard library. It builds the actual polytope vertices and computes their covariance pseudodeterminants using integer principal minors, independently of the graph-determinant identity. It also evaluates degree-rooted forest sums by enumerating acyclic edge subsets. The checker passed all 187 tested connected graphs and labeled trees (including every labeled tree on two through five vertices and every connected simple graph on three or four vertices), verified the path and star determinant recurrences through 13 vertices, and checked the degree-sequence twin pair exactly. These finite checks do not prove the infinite statements; the preceding block-matrix, Cauchy–Binet, and recurrence arguments do.

## Relationship to prior work

The graph-to-polytope vertex construction originates with Arkani-Hamed, Benincasa, and Postnikov [1]. Kühne and Monin [2] determine the face structure of cosmological polytopes and prove the tree normalized-volume formula. Juhnke-Kubitzke, Solus, and Venturello [3] establish regular unimodular triangulations and path/tree triangulation characterizations. The rooted-forest identity for Laplacian-plus-diagonal matrices belongs to established matrix–forest theory [4].

The present statement concerns **equal-vertex-weight Euclidean covariance and its pseudodeterminant**. Its graph-dependent degree-rooted forest specialization, exact tree formulas, and exponentially separated inertia-ellipsoid volumes are not consequences of the cited face, triangulation, or volume formulas without an additional Euclidean moment calculation. No covering statement was found in the examined literature; an equivalent earlier result under graph-moment terminology remains possible.

## Limitations

The theorem uses the canonical standard-coordinate Euclidean realization and equal masses at all vertices. Covariance volume is not an affine-invariant polytope volume and is not the centroidal covariance of uniform interior measure. The tree example does not assert equality of the full face vectors or the full covariance spectra. Exponential separation is proved for the named path–star families, not claimed to be a global extremal theorem over all trees. No independent audit has been performed. Novelty cannot be established solely by search failure.

## References

[1] N. Arkani-Hamed, P. Benincasa, A. Postnikov, *Cosmological Polytopes and the Wavefunction of the Universe*, arXiv:1709.02813, first posted 2017-09-08. https://arxiv.org/abs/1709.02813

[2] L. Kühne, L. Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069, first posted 2022-09-16, especially Corollary 4.2. https://arxiv.org/abs/2209.08069

[3] M. Juhnke-Kubitzke, L. Solus, L. Venturello, *Triangulations of Cosmological Polytopes*, arXiv:2303.05876, first posted 2023-03-10, especially Sections 3 and 5. https://arxiv.org/abs/2303.05876

[4] P. Chebotarev, E. Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575 (2006), established combinatorial determinant framework. https://arxiv.org/abs/math/0602575
