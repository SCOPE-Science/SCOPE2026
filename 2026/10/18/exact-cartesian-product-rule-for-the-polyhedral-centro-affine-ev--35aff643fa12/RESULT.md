# Exact Cartesian-product rule for the polyhedral centro-affine even spectrum

## Finding
Let \(k\ge2\). For each \(1\le i\le k\), let \(P_i\subset\mathbb R^{d_i}\) be a full-dimensional origin-symmetric convex polytope, with \(d_i\ge1\), and let \(P=P_1\times\cdots\times P_k\subset\mathbb R^n\), where \(n=\sum_i d_i\). Equip all facets with the mass and ridge-conductance normalization of Hu and Ivaki (specified below). Write \(\operatorname{Spec}^{+}_{e}(P_i)\) for its **multiset** of nonconstant antipodally even facet-network eigenvalues, and put \(\operatorname{Spec}^{+}_{e}(P_i)=\varnothing\) when its even facet space contains only constants (in particular for any segment).

Then the complete even generalized eigenvalue multiset of the product is
\[
\boxed{
\operatorname{Spec}_{e}(P)=
\{0\}\,\uplus\,\{n\}^{[k-1]}
\,\uplus\,\biguplus_{i=1}^{k}
\bigl(\operatorname{Spec}^{+}_{e}(P_i)+(n-d_i)\bigr).
}
\]
Here \(\uplus\) means union with multiplicities, \(\{n\}^{[k-1]}\) contains \(k-1\) copies, and the shift adds \(n-d_i\) to each eigenvalue. In particular, adopting \(\lambda_{1,e}(P_i)=+\infty\) when the factor has no nonconstant even facet function,
\[
\boxed{
\lambda_{1,e}(P)=\min\left\{n,\ \min_i\bigl(\lambda_{1,e}(P_i)+n-d_i\bigr)\right\}.
}
\]
Thus the bound \(\lambda_{1,e}(P_i)\ge d_i\) for every factor is equivalent to the exact saturation \(\lambda_{1,e}(P)=n\). The product always has a genuine even eigenmode of eigenvalue \(n\), independently of the factors' shapes.

An explicit family of non-parallelotope saturators is
\[
P=[-1,1]\times C_d,\qquad
C_d=\left\{x\in\mathbb R^d:\sum_{j=1}^{d}|x_j|\le1\right\},\quad d\ge3.
\]
For these \((d+1)\)-dimensional prisms,
\[
\boxed{\lambda_{1,e}([-1,1]\times C_d)=d+1,}
\]
with multiplicity one. More precisely, their complete even spectrum is \(0\) once, \(d+1\) once, and \(1+2j(d-1)\) with multiplicity \(\binom d{2j}\) for \(1\le j\le\lfloor d/2\rfloor\). For the four-dimensional octahedral prism, the even spectrum is \(\{0,4,5,5,5\}\).

## Assumptions and scope
All products are in mutually orthogonal Euclidean coordinate subspaces, all factors contain the origin in their interiors and are centrally symmetric, and every inequality in each facet description is irredundant. A segment is allowed as a one-dimensional factor; its even facet-function space consists only of constants. No local-minimizer hypothesis is imposed.

For a polytope \(K\subset\mathbb R^d\) with facet \(F_a\), outward unit normal \(u_a\), and positive support number \(h_a\), set
\[
m_a(K)=h_a\,\mathcal H^{d-1}(F_a).
\]
For distinct facets meeting in a ridge \(F_a\cap F_b\), set
\[
c_{ab}(K)=\frac{h_a h_b\,\mathcal H^{d-2}(F_a\cap F_b)}{\sin\angle(u_a,u_b)},
\]
with \(c_{ab}=0\) for nonadjacent facets. In dimension one there are no facet-adjacency edges. The normalized weighted Laplacian is
\[
(\mathcal L_K f)_a=\frac1{m_a(K)}\sum_b c_{ab}(K)(f_a-f_b),
\]
and the even space consists of \(f_{-a}=f_a\), where \(-a\) labels the opposite facet. Its eigenvalues agree with the generalized eigenvalues of the Hu--Ivaki Dirichlet and mass forms.

## Proof
**(1) Product facets and weights.** Put \(V_i=\operatorname{Vol}_{d_i}(P_i)\) and \(V=\prod_i V_i\). A facet of \(P\) is indexed by a factor \(i\) and its facet \(a\): it equals \(F_{ia}=P_1\times\cdots\times F^{(i)}_a\times\cdots\times P_k\). Orthogonality of the coordinate factors gives
\[
\boxed{m_{ia}(P)=m_a(P_i)\frac{V}{V_i}.}
\]
If two facets belong to the same factor, they meet in a ridge exactly when their factor facets do (there are none if \(d_i=1\)); their angle is unchanged, hence
\[
\boxed{c_{(ia)(ib)}(P)=c_{ab}(P_i)\frac{V}{V_i}.}
\]
If the facets belong to distinct factors \(i\ne j\), they always meet in a ridge. The outward normals are orthogonal and the ridge is the product of two factor facets and all other whole factors. Consequently
\[
\boxed{c_{(ia)(jb)}(P)=m_a(P_i)m_b(P_j)\frac{V}{V_iV_j}.}
\]
All formulas remain valid when one of the factors is a segment, because the zero-dimensional Hausdorff measure of either endpoint is one.

**(2) Exact operator identity.** By the divergence theorem applied to the position vector,
\[
\sum_a m_a(P_i)=d_iV_i.
\]
For a facet function \(f\) on the product, write \(f_i=(f_{ia})_a\) and its factor-mass average
\[
\bar f_i=\frac{\sum_a m_a(P_i)f_{ia}}{d_iV_i}.
\]
Substituting the three weight formulas above into the normalized Laplacian yields the **coordinatewise exact identity**
\[
\boxed{
(\mathcal L_Pf)_{ia}
=(\mathcal L_{P_i}f_i)_a
+\sum_{j\ne i}d_j\bigl(f_{ia}-\bar f_j\bigr).
}
\]
There is no approximation or smooth-boundary limiting argument in this identity.

**(3) Complete orthogonal decomposition.** On each factor's even facet space take a mass-orthogonal eigenbasis with the constant vector first. Extend every nonconstant eigenvector of \(P_i\) by zero onto the other facet blocks. Its factor average is zero; the operator identity makes it an eigenvector of \(P\) with eigenvalue \(\lambda+(n-d_i)\). Eigenvectors from different factor blocks are mutually orthogonal in the product mass inner product.

The remaining even functions are constant on each facet block: \(f_{ia}=b_i\). The operator identity reduces there to
\[
(\mathcal L_Pf)_{ia}=nb_i-\sum_jd_jb_j.
\]
The all-constant vector is the one-dimensional kernel. The complementary \((k-1)\)-dimensional subspace \(\sum_jd_jb_j=0\) has eigenvalue \(n\). This is mass-orthogonal to the all-constant mode and to every zero-mean factor eigenvector. The dimensions of these invariant spaces sum to the entire even facet-space dimension, so the listed spectrum is complete, with all coincidences counted with multiplicity. Taking its least positive element proves the gap formula and the saturation equivalence.

**(4) Octahedral-prism family.** For \(d\ge2\), the \(2^d\) facets of the regular cross-polytope \(C_d\) are indexed by signs in \(\{\pm1\}^d\). Each facet has mass \(1/(d-1)!\); two facets meet in a ridge exactly when one sign differs, and each such ridge has conductance \(1/[2(d-2)!]\). Thus its normalized facet Laplacian is \((d-1)/2\) times the Boolean-cube graph Laplacian. Walsh characters of degree \(r\) have eigenvalue \(r(d-1)\). Antipodal evenness keeps exactly even \(r\), yielding
\[
\operatorname{Spec}_{e}(C_d)=\{0\}\uplus\biguplus_{j=1}^{\lfloor d/2\rfloor}\{2j(d-1)\}^{[\binom d{2j}]}.
\]
The segment has one even constant mode only. The product rule therefore gives the explicit prism spectrum above. Since \(d\ge3\) implies \(2(d-1)>d\), the first positive eigenvalue is \(d+1\), with its single block-constant eigenvector. These prisms are not parallelotopes: each has triangular two-dimensional faces inherited from a cross-polytope for \(d\ge3\), whereas every two-dimensional face of a parallelotope is a parallelogram.

## Verification
The standalone `verify.py` performs exact-fraction checks on independently constructed weighted facet graphs for \(26\) products of segments and regular cross-polytopes (including three-factor products), in ambient dimensions as large as ten. It verifies the dimension-volume mass identity, the block-constant eigenvectors of eigenvalue \(n\), and every surviving even Walsh eigenvector with its exact predicted shift. Its observed output was:

`VERIFY_OK exact weighted facet graph eigenidentities 26 product networks; largest dimension 10`

The finite checks are only corroboration. All-dimensional correctness follows from the three geometric product weight identities and the complete invariant-subspace decomposition proved above.

## Relationship to prior work
Hu and Ivaki introduced the polyhedral centro-affine facet masses, weighted graph Laplacian, and first even eigenvalue, and proved a conditional gap for local minimizers. Their full-text formulas do not give a Cartesian-product spectral rule. A published parallelotope calculation obtains the even spectrum for products of segments; a published cross-polytope calculation obtains the spectrum of each cross-polytope; and a published cube--octahedron interpolation studies a different fixed-dimensional family. None states a dimension-uniform spectral factorization for arbitrary products or the spectrum of cross-polytope prisms.

The linear-algebra part resembles the familiar spectral decomposition of a graph join. The new geometric point is that an arbitrary Cartesian product of convex polytopes produces **exactly** the special mass-weighted join with cross conductances equal to products of facet masses. The block-mixing eigenvalue is then exactly the ambient dimension, and every internal even eigenvalue shifts by the complementary dimension. This yields a general closure law for the conjectural bound \(\lambda_{1,e}\ge d\) and a class of non-parallelotope equality examples. Such products and this implication are not covered by the factor-specific computations alone.

## Limitations
The result applies to the finite facet-network operator, not the smooth centro-affine Laplace--Beltrami operator. It does not establish the conjectural bound \(\lambda_{1,e}(K)\ge d\) for arbitrary indecomposable polytopes, nor that a product is a local minimizer under support perturbations. Product structure alone always provides eigenvalue \(n\), but other factor modes may lie below it. The novelty comparison identifies no equivalent published general product theorem; an unindexed weighted-graph or polyhedral spectral tensorization statement remains a bibliographic risk.

## References
1. Y. Hu and M. N. Ivaki, *Centro-affine spectral geometry of polytopes*, arXiv:2609.21670v1 (first public 18 September 2026), especially equations (1.6)--(1.11), Section 2 and Section 5. Primary MSC2020: 52B11.
2. *Complete even centro-affine facet spectrum of the regular cross-polytope*, public research record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-even-centro-affine-facet-spectrum-of-the-regular-cross--e9e118b429d9.
3. *Exact even centro-affine facet spectrum of parallelotopes*, public research record, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-even-centro-affine-facet-spectrum-of-parallelotopes--96d0f3f42485.
4. *Sharp centro-affine spectral gap along the cube--octahedron interpolation*, public research record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-centro-affine-spectral-gap-along-the-cube-octahedron-inter--4397c6b224a3.
