# Complete even centro-affine facet spectrum of the regular cross-polytope
## Finding
Let
\[
C_n=\left\{x\in\mathbb R^n:\sum_{i=1}^n|x_i|\le1\right\},\qquad n\ge2,
\]
be the regular cross-polytope. Equip its facets with the masses and ridge conductances introduced by Hu and Ivaki. Then the entire generalized facet-network spectrum is
\[
\lambda_k=(n-1)k,
\qquad
\operatorname{mult}(\lambda_k)=\binom nk,
\qquad
0\le k\le n.
\]

The antipodal involution on facets sends a sign vector \(\sigma\) to \(-\sigma\). Restricting to even facet functions therefore keeps precisely the even Walsh levels. Thus the full even spectrum is
\[
\boxed{
\lambda_{2j}=2j(n-1),
\qquad
\operatorname{mult}(\lambda_{2j})=\binom n{2j},
\qquad
0\le j\le\left\lfloor\frac n2\right\rfloor .
}
\]
In particular,
\[
\boxed{\lambda_{1,e}(C_n)=2(n-1)}
\]
with multiplicity
\[
\binom n2.
\]

For \(n=3\), the regular octahedron therefore has first nonconstant even eigenvalue \(4\), of multiplicity \(3\).

## Assumptions and scope
The spectrum is the generalized spectrum associated with the Hu--Ivaki Dirichlet form
\[
\mathsf L_P(f,f)=\sum_{\{i,j\}}c_{ij}(f_i-f_j)^2
\]
and facet-mass quadratic form
\[
\sum_i m_i(f_i-\bar f)^2.
\]
The calculation uses only the definitions of facet mass, ridge conductance, and evenness from the source. It does not rely on the source's variational local-minimizer theorem, so possible issues in later nonsimple-variation arguments are irrelevant here.

The normalization is the standard cross-polytope with vertices \(\{\pm e_i\}_{i=1}^n\). Centro-affine scale invariance makes this normalization natural for the spectral computation.

## Proof
A facet is indexed by a sign vector
\[
\sigma=(\sigma_1,\ldots,\sigma_n)\in\{\pm1\}^n
\]
and is the simplex
\[
F_\sigma=\operatorname{conv}\{\sigma_1e_1,\ldots,\sigma_ne_n\}.
\]
Its supporting hyperplane is
\[
\langle x,u_\sigma\rangle=h,
\qquad
u_\sigma=\frac{\sigma}{\sqrt n},
\qquad
h=\frac1{\sqrt n}.
\]
The Gram matrix of the \(n-1\) edge vectors from one facet vertex has diagonal entries \(2\) and off-diagonal entries \(1\), hence determinant \(n\). Therefore
\[
\mathcal H^{n-1}(F_\sigma)=\frac{\sqrt n}{(n-1)!}
\]
and every facet has mass
\[
m=h\,\mathcal H^{n-1}(F_\sigma)=\frac1{(n-1)!}.
\]

Two facets are adjacent exactly when their sign vectors differ in one coordinate. If \(\sigma\) and \(\tau\) differ in one coordinate, their common ridge is an \((n-2)\)-simplex whose analogous Gram determinant is \(n-1\), so
\[
\mathcal H^{n-2}(F_\sigma\cap F_\tau)=\frac{\sqrt{n-1}}{(n-2)!}.
\]
The unit facet normals satisfy
\[
\langle u_\sigma,u_\tau\rangle=\frac{n-2}{n},
\qquad
\sin\theta_{\sigma\tau}=\frac{2\sqrt{n-1}}{n}.
\]
Consequently every edge of the facet network has the same conductance
\[
c=rac{h^2\mathcal H^{n-2}(F_\sigma\cap F_\tau)}{\sin\theta_{\sigma\tau}}
=rac1{2(n-2)!}.
\]
In particular,
\[
\frac cm=\frac{n-1}{2}.
\]

The facet-adjacency graph is therefore exactly the Boolean hypercube on \(\{\pm1\}^n\), with constant vertex mass \(m\) and constant edge conductance \(c\). For a subset \(S\subseteq\{1,\ldots,n\}\), define the Walsh character
\[
\chi_S(\sigma)=\prod_{i\in S}\sigma_i.
\]
If \(|S|=k\), flipping a coordinate in \(S\) changes the sign of \(\chi_S\), while flipping any other coordinate leaves it unchanged. Hence the unweighted hypercube Laplacian sends \(\chi_S\) to \(2k\chi_S\). After inserting the ratio \(c/m=(n-1)/2\), the generalized eigenvalue is
\[
\lambda_k=(n-1)k.
\]
There are \(\binom nk\) subsets of cardinality \(k\), and the Walsh characters form a basis, giving the complete spectrum.

Finally,
\[
\chi_S(-\sigma)=(-1)^{|S|}\chi_S(\sigma).
\]
Thus the even facet space is exactly the direct sum of the Walsh levels with even \(|S|\). Removing the constant level \(k=0\), the first surviving level is \(k=2\), which proves
\[
\lambda_{1,e}(C_n)=2(n-1)
\]
with multiplicity \(\binom n2\).

## Verification
The bundled checker reconstructs the sign-vector facet graph for dimensions \(2\) through \(8\) and verifies, with exact rational arithmetic, that every Walsh character is a generalized eigenvector with eigenvalue \((n-1)|S|\). It also checks the antipodal parity rule and the multiplicities of every even level.

The checker is a finite stress test of the closed-form proof, not the proof of the all-dimensional statement. The general result follows from the explicit facet and ridge volumes, the exact dihedral angle, and the Walsh basis identity.

## Relationship to prior work
Hu and Ivaki introduce the weighted facet network and define the first nonconstant even eigenvalue for every origin-symmetric polytope. Their paper does not discuss the cross-polytope or octahedron, and it does not compute this spectrum explicitly. The present calculation specializes their definitions to a canonical nonsimple family and obtains every generalized eigenvalue, not only the first one.

A previously published companion computation determines the even facet spectrum of parallelotopes, where every nonconstant even mode has the single eigenvalue \(n\). The cross-polytope is qualitatively different: its even spectrum forms the ladder \(0,2(n-1),4(n-1),\ldots\). For \(n\ge3\), the polar cube and regular cross-polytope therefore have different first even facet-network eigenvalues, showing that this discrete spectrum is not preserved by polarity.

Targeted searches for a centro-affine cross-polytope spectrum, a regular-octahedron computation, and a hypercube realization of the Hu--Ivaki facet network found no statement containing this formula.

## Limitations
The result computes the spectrum only for the regular cross-polytope and its linear images under the natural centro-affine equivalence. It does not classify spectra of arbitrary simplicial or unconditional polytopes, and it does not assert that the regular cross-polytope is a local extremizer of \(\lambda_{1,e}\).

The main proof uses only the source's definitions, not its local-minimizer theorem. Bibliographic novelty is assessed against the focal full text, targeted public searches, and the closest published parallelotope computation; an equivalent calculation under unrelated graph-spectral terminology remains a residual risk.

## References
1. Y. Hu and M. N. Ivaki, *Centro-affine spectral geometry of polytopes*, arXiv:2609.21670v1, 18 September 2026. Primary MSC 2020: 52B11.
