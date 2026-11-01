# Exact spectrum tensorization for centro-affine facet networks of convex-polytope products

## Finding
Let \(r\ge2\) and let \(P_i\subset\mathbb R^{d_i}\), \(d_i\ge2\), be full-dimensional origin-symmetric convex polytopes with the origin in their interiors. Equip facets of each \(P_i\) with the Hu–Ivaki mass–conductance form, and let \(P=P_1\times\cdots\times P_r\) in the orthogonal Cartesian sum. Write \(n=\sum_i d_i\) and \(\operatorname{Spec}(P_i)\) for the complete generalized facet-network Laplacian spectrum, including one zero eigenvalue. Then, as **multisets with algebraic multiplicities**,
\[
\boxed{\operatorname{Spec}(P)=\{0\}\uplus\{n\}^{[r-1]}\uplus\biguplus_{i=1}^r\left((n-d_i)+(\operatorname{Spec}(P_i)\setminus\{0\})\right).}
\]
The displayed difference removes exactly the single constant-mode zero from each factor. For centrally symmetric factors, this decomposition respects antipodal even/odd parity. In particular,
\[
\boxed{\lambda_{1,e}(P)=\min\left\{n,\ \min_{i:\,\mathcal E_i^0\ne\{0\}}\big(n-d_i+\lambda_{1,e}(P_i)\big)\right\}\le n,}
\]
where \(\mathcal E_i^0\) denotes the mean-zero even facet space and an empty inner minimum is omitted.

For an explicit class, let each factor be a regular centrally symmetric planar \(N_i\)-gon with even \(N_i\ge4\). The full factor spectrum is
\[
\lambda_{i,k}=\frac{\sin^2(k\pi/N_i)}{\sin^2(\pi/N_i)},\qquad 0\le k<N_i,
\]
where the Fourier level is even under antipodal reflection precisely when \(k\) is even. Thus every such product in dimension \(n=2r\) has \(\lambda_{1,e}(P)=n\), with **exact multiplicity** \(r-1+s\), where \(s\) counts the square factors \(N_i=4\). Its remaining even eigenvalues are the values \(n-2+\lambda_{i,k}\) for each \(i\) and each nonzero even \(k\), counted with Fourier multiplicity.

## Assumptions and scope
For a \(d\)-polytope \(K\) whose origin is interior, label the facets \(F_a\), with outward *unit* normal \(u_a\) and positive support distance \(h_a\). Set
\[
m_a=h_a\mathcal H^{d-1}(F_a),\quad c_{ab}=\frac{h_a h_b\mathcal H^{d-2}(F_a\cap F_b)}{\sin\theta_{ab}}
\]
when distinct facets meet in a ridge, and \(c_{ab}=0\) otherwise; \(\theta_{ab}\in(0,\pi)\) is the angle of the outward normals. Define \(L_K(f,f)=\sum_{\{a,b\}}c_{ab}(f_a-f_b)^2\) and the mass norm \(\sum_a m_af_a^2\). The generalized eigenproblem is \(L_K f=\lambda M_K f\); the Rayleigh quotient of nonconstant even functions uses their mass-centered values. Eigenvalues are nonnegative, and the constant eigenspace has dimension one because the facet adjacency graph is connected.

The spectrum formula concerns this *discrete facet-network operator*, not the smooth centro-affine differential operator, the vertex graph, or a spectral limit. The product must be an orthogonal Cartesian product, not a Minkowski sum. Polytopes need not be regular or simple for the tensorization theorem.

## Proof
**1. Exact product geometry.** Let \(V_i=\operatorname{vol}_{d_i}(P_i)>0\). A product facet has the form \(F_{ia}\times\prod_{j\ne i}P_j\), hence its mass is
\[
M_{ia}=m_{ia}\prod_{j\ne i}V_j.
\]
Two such facets from the same factor \(i\) meet along a product ridge exactly when the factor facets meet along a ridge, and their normal angle is unchanged. Their product conductance is \(c_{iab}\prod_{j\ne i}V_j\). Two facets from distinct factors \(i\ne j\) meet along a ridge, their normals are orthogonal, and their product conductance is exactly
\[
C_{ia,jb}=m_{ia}m_{jb}\prod_{\ell\notin\{i,j\}}V_\ell.
\]
These are all ridges of \(P\). Minkowski's elementary pyramid-volume identity gives \(\sum_a m_{ia}=d_iV_i\).

**2. Invariant orthogonal subspaces.** In the mass inner product \(\langle f,g\rangle_P=\sum_{i,a}M_{ia}f_{ia}g_{ia}\), decompose the facet-function space as the orthogonal direct sum of (a) factor-supported functions with \(\sum_a m_{ia} f_{ia}=0\), for each \(i\), and (b) functions constant on every factor-facet block. The former have dimensions \(N_i-1\), the latter has dimension \(r\), and these dimensions sum to the full number of product facets \(\sum_iN_i\).

For a function supported on block \(i\) with factor-weighted mean zero, the cross-factor couplings into every other block vanish. Inside block \(i\), the cross-factor row sums add \(\sum_{j\ne i}d_j=n-d_i\) times the mass. Thus the restricted operator is precisely \(L_{P_i}\) in its mass-normalized form, shifted by \(n-d_i\). For a block-constant function with values \(a_i\), the operator gives on block \(i\)
\[
\sum_{j\ne i}d_j(a_i-a_j)=na_i-\sum_jd_ja_j.
\]
Consequently this \(r\)-dimensional block-constant space has eigenvalue zero on the common constant vector, and eigenvalue \(n\) on the \((r-1)\)-dimensional subspace \(\sum_i d_i a_i=0\). All stated eigenvalues, including coincidences and multiplicities, follow from the orthogonal decomposition.

**3. Parity.** Antipodal reflection of the product preserves each factor-facet block and maps a facet to its antipodal facet within that block. It commutes with each factor operator and with the block-constant operator. Hence factor even eigenvectors give product even eigenvectors (and likewise for odd vectors), while the common constant and \(n\)-eigenspace of block-constants are even. This gives the displayed first-even-gap formula.

**4. Regular polygons.** A regular \(N\)-gon with apothem \(h\) has facet length \(2h\tan(\pi/N)\), mass \(m=2h^2\tan(\pi/N)\), and adjacent-facet conductance \(c=h^2/\sin(2\pi/N)\). Therefore \(c/m=1/[4\sin^2(\pi/N)]\). Its facet graph is a cycle, so the discrete Fourier characters have eigenvalues \((2-2\cos(2\pi k/N))c/m=\sin^2(k\pi/N)/\sin^2(\pi/N)\). Antipodality sends Fourier level \(k\) to \((-1)^k\) times itself. For even \(N\ge4\), the smallest nonzero even eigenvalue is \(4\cos^2(\pi/N)\), equal to \(2\) only for \(N=4\), and strictly larger otherwise. Tensorization with each \(d_i=2\) proves the exact first-even gap and multiplicity claimed above.

## Verification
The accompanying reproducible script `verify.py` constructs product-facet operators directly from exact geometric masses and conductances for unit-area regular squares and hexagons. It checks their complete and even characteristic spectra, weighted self-adjointness, and their zero constant modes for seven products, including a three-dimensional octahedron times a square as well as six two- or three-factor square/hexagon products. All matrix entries and eigenvalue comparisons are rational and exact. Run `python verify.py` with SymPy installed.

The analytic proof establishes the full all-dimensional statement and its parity classification. The seven finite matrix checks are deliberately only independent falsification tests of the formulas and normalizations.

## Relationship to prior work
Hu and Ivaki introduced the weighted facet-network construction and proved a conditional lower bound for a locally minimizing first even eigenvalue [1]. The present claim is an exact **unconditional factorization** of every generalized eigenvalue of a product, and implies \(\lambda_{1,e}(P)\le n\), unlike their local-minimizer lower bound. Two published exact computations cover the even spectrum of parallelotopes [2] and the full regular cross-polytope spectrum [3]. The parallelotope result is a special case of the product formula when appropriate factors are squares or intervals, and is expressly not presented as a new consequence. The cross-polytope result uses a Boolean-cube facet graph and does not imply the product-facet cross-coupling identity. The ordinary spectral decomposition of a mass-weighted rank-one graph join is standard linear algebra; the geometric product-ridge mass/conductance identity is the substantive bridge needed here. Classical graph-join spectral techniques [4] are thus background, not claimed as new.

## Limitations
No claim is made about the spectrum of arbitrary Minkowski sums, nonorthogonal products, or smooth centro-affine operators. The exact value \(n\) of the first even eigenvalue for products of regular even polygons does not characterize those products among all polytopes. The focal manuscript's complete text could not be obtained during this comparison: the accessible abstract and technical extracts establish the network definitions but cannot exclude an unindexed equivalent product lemma in its sections or elsewhere. This is a material historical-priority risk.

## References
1. Y. Hu and M. N. Ivaki, *Centro-affine spectral geometry of polytopes*, arXiv:2609.21670v1, first public 2026-09-18, https://arxiv.org/abs/2609.21670.
2. *Exact even centro-affine facet spectrum of parallelotopes*, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-even-centro-affine-facet-spectrum-of-parallelotopes--96d0f3f42485.
3. *Complete even centro-affine facet spectrum of the regular cross-polytope*, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-even-centro-affine-facet-spectrum-of-the-regular-cross--e9e118b429d9.
4. S. Klee and M. T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669, 2020, https://arxiv.org/abs/2008.01669.
