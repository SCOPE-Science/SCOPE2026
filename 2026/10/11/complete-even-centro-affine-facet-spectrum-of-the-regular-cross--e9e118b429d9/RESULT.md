# Complete even centro-affine facet spectrum of the regular cross-polytope

## Finding
For every integer \(n\ge2\), let
\[
C_n=\left\{x\in\mathbb R^n:\sum_{i=1}^{n}|x_i|\le1\right\}.
\]
Equip its facets with the masses and ridge conductances of Hu and Ivaki. The complete generalized facet-network spectrum, including the noneven modes, is
\[
\lambda_k=(n-1)k,\qquad \operatorname{mult}(\lambda_k)=\binom nk,
\qquad k=0,1,\ldots,n.
\]
The antipodal even subspace consists exactly of the even Walsh levels. Its full generalized spectrum is therefore
\[
\boxed{\lambda_{2j}=2j(n-1),\qquad
\operatorname{mult}(\lambda_{2j})=\binom n{2j},\qquad
0\le j\le\lfloor n/2\rfloor.}
\]
In particular, the first nonconstant even eigenvalue is \(2(n-1)\), of multiplicity \(\binom n2\); for the regular octahedron in dimension three it is \(4\), of multiplicity three.

## Definitions and normalization
For a facet \(F_i\) with unit outer normal \(u_i\) and support number \(h_i>0\), put
\[
m_i=h_i\mathcal H^{n-1}(F_i).
\]
For adjacent facets \(F_i,F_j\) with common ridge and angle \(\theta_{ij}\) between their unit normals, put
\[
c_{ij}=\frac{h_i h_j\mathcal H^{n-2}(F_i\cap F_j)}{\sin\theta_{ij}};
\]
otherwise put \(c_{ij}=0\). The Dirichlet form is
\[
\mathsf L_P(f,f)=\sum_{\{i,j\}}c_{ij}(f_i-f_j)^2,
\]
where each unordered adjacent pair occurs once. Generalized eigenvalues use the facet mass form; on even functions the first positive eigenvalue is the quotient of \(\mathsf L_P\) by \(\sum_i m_i(f_i-\bar f)^2\). This is the Hu--Ivaki normalization, not a normalized random-walk Laplacian. The chosen regular cross-polytope has vertices \(\{\pm e_i\}\).

## Proof
For \(\sigma\in\{\pm1\}^n\), the facet
\[
F_\sigma=\operatorname{conv}\{\sigma_1e_1,\ldots,\sigma_ne_n\}
\]
has unit outer normal \(u_\sigma=\sigma/\sqrt n\) and support number \(h=1/\sqrt n\). The Gram matrix of its \(n-1\) edge vectors has diagonal \(2\) and off-diagonal \(1\), so its determinant is \(n\). Consequently
\[
\mathcal H^{n-1}(F_\sigma)=\frac{\sqrt n}{(n-1)!},\qquad
m_\sigma=\frac1{(n-1)!}.
\]
Two facets share a ridge exactly when their signs differ in one coordinate. The \(n-2\) ridge edge vectors have the analogous Gram determinant \(n-1\), and therefore
\[
\mathcal H^{n-2}(F_\sigma\cap F_\tau)=\frac{\sqrt{n-1}}{(n-2)!}.
\]
For \(n=2\), this uses the ordinary zero-dimensional Hausdorff measure of one ridge point. When exactly one sign differs,
\[
\langle u_\sigma,u_\tau\rangle=\frac{n-2}{n},\qquad
\sin\theta_{\sigma\tau}=\frac{2\sqrt{n-1}}n.
\]
Substitution into the conductance definition gives the same positive value on every edge:
\[
\boxed{c=\frac{h^2\mathcal H^{n-2}(F_\sigma\cap F_\tau)}{\sin\theta_{\sigma\tau}}
=\frac1{2(n-2)!},\qquad \frac{c}{m}=\frac{n-1}{2}.}
\]
Thus the facet-adjacency graph with its exact weights is the Boolean hypercube \(Q_n\), with constant mass \(m\) and edge conductance \(c\). For every subset \(S\subseteq\{1,\ldots,n\}\), define
\[
\chi_S(\sigma)=\prod_{i\in S}\sigma_i.
\]
A coordinate flip changes \(\chi_S\) precisely when that coordinate lies in \(S\). Writing \(|S|=k\), the unweighted cube graph Laplacian has
\[
(L_{Q_n}\chi_S)(\sigma)=2k\chi_S(\sigma).
\]
The generalized mass operator is \((c/m)L_{Q_n}\), so its eigenvalue is \((n-1)k\). The Walsh characters form a basis of all \(2^n\) facet functions and give multiplicity \(\binom nk\). No unlisted eigenvalues remain.

Antipodal inversion acts by
\[
\chi_S(-\sigma)=(-1)^k\chi_S(\sigma),
\]
so exactly the even values of \(k\) survive on even facet functions. The constant level \(k=0\) is simple. The first subsequent level is \(k=2\), proving all claimed formulas.

The facet mass and ridge conductance are both multiplied by \(|\det A|\) under an invertible linear map \(A\): the codimension-one and codimension-two Jacobians cancel the transformed unit-normal and angle factors. Thus the generalized spectrum is unchanged for invertible linear images of \(C_n\); this extension does not claim the same spectrum for arbitrary combinatorially equivalent simplicial polytopes.

## Verification and relationship to prior work
The included exact-rational checker tests all Walsh eigen-equations, antipodal parity, and multiplicities for \(2\le n\le8\). The all-dimensional conclusion comes from the geometric formulas and Walsh basis, not from finite enumeration.

Hu and Ivaki, *Centro-affine spectral geometry of polytopes* (arXiv:2609.21670v1, September 18, 2026), introduced these precise facet masses, ridge weights, and even spectral quotient, but did not provide this all-dimensional cross-polytope spectrum. The standard Boolean-cube graph spectrum is classical; the identified facet-network weights yield the specific centro-affine scaling. A published parallelotope computation gives even spectrum \(\{0,n\}\), contrasting with the regular cross-polytope's even ladder for \(n\ge3\). A separate three-dimensional cube--octahedron interpolation computation has a regular-octahedron boundary specialization compatible with \(\lambda_{1,e}=4\); that lower-dimensional overlap does not determine the formulas for \(n\ge4\). No novelty or chronological-priority claim is made for that octahedral specialization.

## Limitations
This is an explicit calculation for regular cross-polytopes and their invertible linear images. It does not prove a local-extremizer statement, a universal spectral bound, or a classification for arbitrary simplicial, unconditional, or combinatorially equivalent polytopes. The Hu--Ivaki variational local-minimizer theorem is not used. The formula uses the particular conductance normalization specified above; a different graph normalization gives different eigenvalues.
