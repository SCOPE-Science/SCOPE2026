# Symmetry-optimal biclique projections and the exceptional uniqueness of the square

## Finding
For every pair of integers \(m,n\ge 2\), orient the edges of the unit-edge complete bipartite graph \(K_{m,n}\) from its \(m\)-vertex class to its \(n\)-vertex class, and identify edge vectors with matrices \(X\in\mathbb F^{m\times n}\), where \(\mathbb F\) is either \(\mathbb R\) or \(\mathbb C\). Let \(Z\) be the graph cycle-flow space and \(B\) its Euclidean-orthogonal cut space. Write
\[
H_s=I_s-\frac1s\mathbf1_s\mathbf1_s^{\mathsf T},\qquad
P_Z(X)=H_mXH_n,\qquad P_B(X)=X-H_mXH_n.
\]
**Universal minimax assertion:** For *every* norm \(N\) on \(\mathbb F^{m\times n}\) unchanged by independent permutations of rows and columns, \(P_Z\) minimizes the induced operator norm over **all** linear projections onto \(Z\), and \(P_B\) simultaneously minimizes it over **all** linear projections onto \(B\). In each case this is the unique projection commuting with every independent row and column permutation. The assertion does not require unconditionality or any assumption that \(N\) arises from an entrywise \(\ell_p\) norm.

For the real or complex entrywise \(\ell_1\) norm, the two relative projection constants are exactly
\[
\lambda_1(Z)=\frac{4(m-1)(n-1)}{mn},\qquad
\lambda_1(B)=3-\frac2m-\frac2n+\frac2{mn}.
\]
The same formulas hold for the entrywise \(\ell_\infty\) norm. The *optimal* cycle-versus-cut gap is
\[
\lambda_1(Z)-\lambda_1(B)=\frac{(m-2)(n-2)-2}{mn}.
\]
Thus optimal cycle and cut norms tie precisely for \((m,n)=(3,4)\) or \((4,3)\); the cut norm is larger when \((m-2)(n-2)<2\), and the cycle norm is larger when \((m-2)(n-2)>2\). These conclusions concern the minimum over all projections, not merely the norm of a named orthogonal projection.

**Sharp optimizer rigidity for entrywise \(\ell_1\).** Although the commuting projections above are unique, they need not be the only minimizers. The projection onto \(Z\) is the **unique** minimum-norm \(\ell_1\) projection exactly when \(m=n=2\). For every other \(m,n\ge2\), there is a nonconstant real interval of distinct minimum-norm projections onto \(Z\). This is a uniqueness theorem among *all* projections, not merely the symmetric ones. The assertion holds over either scalar field.

For every entrywise exponent \(1\le p\le\infty\), a further exact tensorization identity holds:
\[
\lambda_p(Z)=\|H_m\|_{\ell_p^m\to\ell_p^m}\,\|H_n\|_{\ell_p^n\to\ell_p^n}.
\]
This identity is a reduction to two ordinary finite-dimensional centering-operator norms; no closed elementary expression for those factors at general interior exponents is asserted.

## Assumptions and scope
All graphs are finite, connected, unweighted and simple. The dimensions satisfy \(m,n\ge2\). Matrix entries represent oriented edge flows; the incidence constraints defining the cycle space are precisely zero row sums and zero column sums:
\[
Z=\{X:X\mathbf1_n=0,\ \mathbf1_m^{\mathsf T}X=0\}.
\]
The cut space \(B\) is its orthogonal complement for the **standard Euclidean** inner product, independent of the choice of ambient norm \(N\). Both spaces are nonzero, of respective dimensions \((m-1)(n-1)\) and \(m+n-1\). Given any subspace \(Y\), define \(\lambda_N(Y)=\inf\{\|T\|_{N\to N}:T^2=T,\ \operatorname{ran}T=Y\}\). The letter \(\lambda_p\) denotes \(\lambda_N\) for entrywise \(\ell_p\). The same subspace is used over either scalar field.

## Proof
**1. Canonical subspaces.** All edges have the same left-to-right orientation. The signed incidence constraints at the left vertices say that every row sum is zero, and those at the right vertices say that every column sum is zero. Hence \(Z\) is the zero-row/zero-column subspace, and direct multiplication shows that \(P_Z(X)=H_mXH_n\) is its Euclidean-orthogonal projector. Consequently \(P_B=I-P_Z\) projects onto \(B\).

**2. Four-orbit commutant lemma.** Let \(\Gamma=S_m\times S_n\) permute rows and columns separately. For any linear map \(T:\mathbb F^{m\times n}\to\mathbb F^{m\times n}\) that commutes with \(\Gamma\), the coefficient mapping input cell \((k,\ell)\) to output cell \((i,j)\) depends only on whether \(i=k\) and whether \(j=\ell\): these are the four orbits of ordered cell pairs under \(\Gamma\). Consequently every such \(T\) lies in the span of the four mutually annihilating idempotent maps
\[
X\mapsto H_mXH_n,\quad X\mapsto H_mXJ_n,\quad X\mapsto J_mXH_n,\quad X\mapsto J_mXJ_n,
\]
where \(J_s=I_s-H_s\). Their ranges form a direct sum decomposition of all matrices, with the first summand equal to \(Z\) and the other three summands making up \(B\). Each summand is nonzero for \(m,n\ge2\). A \(\Gamma\)-commuting projection onto \(Z\) must act as identity on the first summand and zero on the other three, so it equals \(P_Z\). Similarly the unique \(\Gamma\)-commuting projection onto \(B\) is \(P_B\). This proves uniqueness without assuming irreducibility or invoking any unverified representation classification.

**3. Global optimality for arbitrary invariant norms.** Fix any norm \(N\) for which each element \(U_g\) of \(\Gamma\) is an isometry. If \(T\) is any linear projection onto \(Z\), then
\[
\overline T=\frac1{|\Gamma|}\sum_{g\in\Gamma}U_g^{-1}TU_g
\]
continues to map into \(Z\) and to fix \(Z\), hence is a projection onto \(Z\). The triangle inequality and isometry give \(\|\overline T\|_{N\to N}\le\|T\|_{N\to N}\). By the four-orbit lemma, \(\overline T=P_Z\), so \(P_Z\) is globally minimal. Repeat with \(B\), which is \(\Gamma\)-invariant, to obtain \(\overline T=P_B\) and its global minimality. There is no assertion that every minimizer is unique: only the permutation-equivariant one is unique.

**4. Exact endpoint constants.** The column of \(P_Z\) corresponding to cell \((k,\ell)\) has coefficient \((\delta_{ik}-1/m)(\delta_{j\ell}-1/n)\) at cell \((i,j)\). Its absolute column sum is
\[
\left(\frac{m-1}{m}+\frac{m-1}{m}\right)
\left(\frac{n-1}{n}+\frac{n-1}{n}\right)
=\frac{4(m-1)(n-1)}{mn}.
\]
For \(P_B\), the corresponding coefficient is \(\delta_{ik}/n+\delta_{j\ell}/m-1/(mn)\). Its four cell classes contribute \((m+n-1)/(mn)\), \((n-1)(m-1)/(mn)\), \((m-1)(n-1)/(mn)\), and \((m-1)(n-1)/(mn)\), respectively, giving \((3mn-2m-2n+2)/(mn)\). Every column has the same sum by transitivity. Both projector matrices are symmetric, so absolute row sums coincide with absolute column sums; this also proves the claimed \(\ell_\infty\) constants. By Step 3 these endpoint values are *minimum* projection norms. Subtraction yields the displayed gap. Since \((m-2)(n-2)=2\) in integers \(m,n\ge2\) only for \((m,n)=(3,4)\) or \((4,3)\), the trichotomy is exact.

**5. Exceptional uniqueness versus continuous nonuniqueness.** For \(m=n=2\), the cycle subspace is the span of \(z=(1,-1,-1,1)\), whose entrywise \(\ell_1\) norm is \(4\). Every projection onto this line has the form \(T(X)=z\varphi(X)\) with \(\varphi(z)=1\), hence \(\|T\|_{1\to1}=4\max_e|\varphi(e)|\ge1\). Equality in the triangle and Hölder inequalities forces \(\varphi(e)=z_e/4\) for each cell, so the Euclidean cycle projection is the **only** minimum-norm projection (real or complex).

If \(n\ge3\), let \(z\) be the alternating \(2\times2\) flow supported on rows \(1,2\) and columns \(1,2\), with entries \(z_{11}=z_{22}=1\) and \(z_{12}=z_{21}=-1\). Let \(\varphi(X)=\sum_iX_{i3}\), the sum in column \(3\). Define \(T(X)=z\varphi(X)\). Then \(T\) maps into \(Z\) and annihilates \(Z\), because each column sum of any cycle flow vanishes. Thus \(P_Z+tT\) is a projection onto \(Z\) for every scalar \(t\). Its only changed columns are those indexed by cells in column \(3\); these cells are outside the support of \(z\). For an arbitrary cell \(e=(k,\ell)\), every entry of \(P_Z e\) is nonzero and its sign matrix is \(s_e(i,j)=(2\delta_{ik}-1)(2\delta_{j\ell}-1)\). Since \(z\) has zero row and column sums, \(\langle s_e,z\rangle=4z_e\). This is zero whenever \(e\) lies in column \(3\). If \(0<|t|<1/(mn)\) is real, none of the signs in a changed column crosses zero, and its absolute column sum therefore remains **exactly** the same. All other columns are unchanged. It follows that \(\|P_Z+tT\|_{1\to1}=\|P_Z\|_{1\to1}=\lambda_1(Z)\), furnishing a continuum of distinct minimizers. When \(n=2\) and \(m\ge3\), transpose this construction: use the sum along row \(3\) and the same upper-left \(2\times2\) alternating flow. The same reasoning gives nonuniqueness. This establishes the sharp boundary \(m=n=2\).

**6. Tensorization for all exponents.** For entrywise \(\ell_p\), apply \(H_m\) separately to columns and \(H_n\) separately to rows. The two operator norms multiply to give \(\|P_Z\|_p\le\|H_m\|_p\|H_n\|_p\). For rank-one matrices \(X=uv^{\mathsf T}\), the norm ratio is exactly \(\|H_mu\|_p/\|u\|_p\) times \(\|H_nv\|_p/\|v\|_p\); finite-dimensional maximizing vectors exist, including for \(p=1,\infty\). Thus equality holds. Step 3 converts the equality into the minimum projection constant. At \(p=2\), both complementary nonzero Euclidean orthogonal projectors have norm one.

## Verification
The accompanying `check_min_biclique.py` is executable with the Python standard library. It builds both projector matrices with exact rational arithmetic for all \(2\le m,n\le9\); checks idempotence, mutual annihilation, cycle-flow row/column constraints, exact \(\ell_1/\ell_\infty\) norms and the gap identity. For every tested biclique except the square it also constructs a **distinct** optimal cycle projection by a small rank-one perturbation. Its 64 parameter pairs comprise 1,936 rational edge columns. This finite test is corroborative: the universal minimality claim is proven by the four-orbit and averaging arguments, not inferred from enumeration.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (arXiv:2305.12582, initially public May 21, 2023) develop minimal and invariant cycle projections, including an abstract representation-theoretic uniqueness criterion (their Theorem 5) and results for discrete tori and Hamming graphs. The symmetry-averaging method and the general abstract criterion are **prior results**, not claimed here as inventions. The present concrete identification of the four-orbit commutant simultaneously for cut and cycle spaces gives a graph-specific universal norm-minimality statement, and hence the *optimal* exact biclique projection-constant comparison. The square \(K_{2,2}\) coincides with a known small Hamming graph and is not offered as a new special case.

Previous individual computations of canonical, rather than optimized, Hodge projection norms on complete multipartite graphs can supply the same endpoint **numerical formulas** on bicliques. Those formulas alone are not asserted novel here. The distinct claim is global minimality for both ranges under every row-column permutation-invariant ambient norm, including the full family of entrywise \(\ell_p\) spaces and its tensorization, the exact comparison of the resulting minima, and the sharp **all-minimizers** uniqueness classification for the cycle projection in \(\ell_1\). Related 2018 work by the same authors on Lipschitz-free spaces analyzes projection constants for recursive families, not this two-parameter optimality classification.

## Limitations
The graph is required to be a complete bipartite graph with identical edge weights. The universal norm statement requires invariance under **all** independent row and column permutations; it does not extend to arbitrary edge-weighted norms or arbitrary graphs without further argument. The endpoint rational formulas do not describe the norm of a non-orthogonal chosen projection. Tensorization for \(1<p<\infty\) is an exact reduction, not a claimed closed scalar formula. An older paper or unindexed matrix-centering treatment may imply parts of this application through general symmetry principles; absence from targeted searches is not proof of novelty. No independent mathematical audit is claimed.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582 (public May 21, 2023), https://arxiv.org/abs/2305.12582 . Theorem 5; Sections 1.4, 2.6 and 2.7.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz-Free Spaces on Finite Metric Spaces*, arXiv:1807.03814 (2018), https://arxiv.org/abs/1807.03814 . Sections 1 and 4.
