# Orientation-defect rigidity for rank-one block numerical-radius paths

## Finding
Let \(m\ge3\), let \(R\ne0\) be a rank-one operator on a complex Hilbert space, and let \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_{m-1})\in\{+,-\}^{m-1}\). The strictly upper block-bidiagonal operator \(S_\varepsilon(R)\) on \(\mathcal H^{\oplus m}\) has block \(R\) in position \((j,j+1)\) when \(\varepsilon_j=+\) and block \(R^*\) otherwise. Define \(\tau=\|R\|\) and \(r=|\operatorname{tr}R|/\tau\in[0,1]\). Here the trace is the usual finite-rank trace.

Put \(E=m-1\) and \(t_j=1\) if \(\varepsilon_j\ne\varepsilon_{j+1}\), otherwise \(t_j=r\), for \(1\le j<E\). Define real symmetric \(E\times E\) matrices \(G_{\mathrm e}\) and \(G_{\mathrm o}\), both with diagonal entries one. Their only nonzero off-diagonal entries are \((G_{\mathrm e})_{j,j+1}=(G_{\mathrm e})_{j+1,j}=t_j\) for odd \(j\), and \((G_{\mathrm o})_{j,j+1}=(G_{\mathrm o})_{j+1,j}=t_j\) for even \(j\). Then
\[
\boxed{w(S_\varepsilon(R))=\frac{\tau}{2}\sqrt{\rho(G_{\mathrm o}G_{\mathrm e})}.}
\]
All eigenvalues contributing to this spectral radius are real and nonnegative, including at the singular endpoint values \(r=0,1\). Thus an arbitrary operator word of length \(m-1\) is evaluated by two explicit Gram matrices of size \(m-1\), regardless of Hilbert-space dimension.

Write \(D(\varepsilon)=\{j:1\le j<m-1,\ \varepsilon_j=\varepsilon_{j+1}\}\). At any fixed \(0<r<1\), if \(D(\varepsilon)\subsetneq D(\eta)\), then \(w(S_\varepsilon(R))>w(S_\eta(R))\). For every \(0\le r<1\), the largest radius among orientation words is attained *only* by the two alternating words, and the smallest *only* by the two constant words. The maximum is \(\tau\cos(\pi/(m+1))\). At \(r=1\), every word attains this maximum.

At \(r=0\), let \(L(\varepsilon)\) be the maximum length (number of letters) of a consecutive alternating subword. Then
\[
\boxed{w(S_\varepsilon(R))=\tau\cos\!\left(\frac{\pi}{L(\varepsilon)+2}\right).}
\]
In particular, strict inclusion of defect sets at \(r=0\) need not give strict inequality: the longest alternating run may remain unchanged.

For each fixed word, set \(\theta=\pi/(m+1)\). The exact first-order cost of departure from a normal rank-one operator is
\[
\boxed{\frac{w(S_\varepsilon(R))}{\tau}=\cos\theta-\frac{1-r}{(m+1)\cos\theta}\sum_{j\in D(\varepsilon)}\sin(j\theta)\sin((j+2)\theta)+O((1-r)^2)}
\]
as \(r\uparrow1\). Every listed defect has a strictly positive, position-dependent first-order cost.

For example, at \(m=4\) and the word \((+,+,-)\), one obtains the exact nontrivial interpolation
\[
\frac{w(S_{++-}(R))}{\tau}=\frac12\sqrt{\frac{3+\sqrt{1+4r^2}}2},\qquad 0\le r\le1.
\]
It rises strictly from \(1/\sqrt2\) to \(\cos(\pi/5)\).

## Assumptions and scope
The Hilbert space may be finite- or infinite-dimensional, and \(R\) need not be normal or self-adjoint. Every nonzero rank-one operator is trace class and obeys \(0\le|\operatorname{tr}R|\le\|R\|\). The theorem concerns *ordinary complex-Hilbert-space numerical radius*, not semi-Hilbertian or weighted numerical radii. All words have a fixed length and use the same rank-one block \(R\) or its adjoint. A fixed complex phase multiplying \(R\) is immaterial because successive diagonal scalar-unitary conjugations can absorb the phases of the blocks along a path.

## Proof
**1. Phase normalization and rotation symmetry.** Write \(R=\tau\,u v^*\) for unit vectors \(u,v\). Multiplying \(R\) by a unit complex scalar changes the phase of \(\langle u,v\rangle\), but the resulting block path is diagonally unitarily equivalent to the original: recursively choose the scalar phase at each block node to absorb that edge's phase. We can therefore suppose \(\langle u,v\rangle=r\ge0\). A further unitary change of Hilbert coordinates puts \(u,v\) into the real canonical two-plane with \(u=(1,0)\), \(v=(r,\sqrt{1-r^2})\) whenever needed. Because the block matrix has entries on one superdiagonal only, conjugation by \(\operatorname{diag}(1,z,\ldots,z^{m-1})\) multiplies it by \(z\) for every \(|z|=1\). Its numerical range is circular, so the standard Hermitian-part characterization gives \(2w(S)=\|S+S^*\|\). Normalizing by \(\tau\) now suffices.

**2. Exact Gram reduction.** Bipartition the \(m\) path vertices into odd and even vertices. Under this reordering, \(S+S^*\) is \(\begin{psmallmatrix}0&B\\B^*&0\end{psmallmatrix}\), where \(B=P Q^*\) and the \(j\)-th columns of \(P,Q\) are the unit vectors at the odd and even ends of edge \(j\), respectively. Distinct nonadjacent edges never overlap in either column space. The two columns belonging to consecutive edges overlap only at their common vertex \(j+1\). Their inner product is \(1\) for opposite block orientations and \(r\) for equal orientations. The common vertex is even exactly when \(j\) is odd. Therefore \(P^*P=G_{\mathrm o}\) and \(Q^*Q=G_{\mathrm e}\). The nonzero spectra of \(BB^*=P G_{\mathrm e}P^*\) and \(G_{\mathrm o}G_{\mathrm e}\) agree, even when a Gram matrix is singular. Since \(BB^*\) is positive, the latter product's entire nonzero spectrum is positive real, and its spectral radius equals \(\|B\|^2\). Hence \(w(S)=\|B\|/2=\sqrt{\rho(G_{\mathrm o}G_{\mathrm e})}/2\).

**3. Ordering and endpoint classification.** Both Gram matrices are entrywise nonnegative. Their product is entrywise nondecreasing in every \(t_j\). When all \(t_j>0\), its adjacent entries are positive, hence the product is irreducible. Perron--Frobenius strict comparison shows that increasing any one \(t_j\), while keeping the others positive, strictly increases the spectral radius. Thus for \(0<r<1\) a proper inclusion of defect sets strictly *decreases* the radius. The alternating words have every \(t_j=1\), while the constant words have every \(t_j=r\); they are the unique extremizers. At \(r=1\), both Gram matrices represent the incidence of an ordinary scalar path, whose adjacency spectral radius is \(2\cos(\pi/(m+1))\). At \(r=0\), a shared vertex with equal orientations gives two orthogonal incident vectors, so the Hermitian block graph splits into scalar paths at exactly those defects. Its largest component has \(L(\varepsilon)\) edges and contributes numerical radius \(\cos(\pi/(L(\varepsilon)+2))\). This also proves uniqueness of both orientation extremizers at \(r=0\). For any nonalternating word the radius is strictly increasing from \(r=0\) to \(r=1\), by strict Perron comparison against an irreducible positive-parameter product.

**4. First-order coefficient.** Temporarily regard the overlaps \(t_j\) as independent parameters. At the all-ones point, let \(\psi_k=\sqrt{2/(m+1)}\sin(k\theta)\), with \(\theta=\pi/(m+1)\). This is the normalized Perron vector for the scalar path adjacency, with eigenvalue \(\sigma=2\cos\theta\). The odd and even restrictions each have squared norm \(1/2\). Normalize these restrictions to vectors \(f,g\) of norm one and write \(x=P^*f\), \(y=Q^*g\) for the scalar path's incidence factors. Then \(G_{\mathrm e}x=\sigma y\), \(G_{\mathrm o}y=\sigma x\) and \(y^*x=\sigma\). These are right/left Perron eigenvectors of \(G_{\mathrm o}G_{\mathrm e}\) for the simple eigenvalue \(\lambda=\sigma^2\). If the shared vertex \(j+1\) is odd, differentiating its Gram entry gives \(\partial\lambda/\partial t_j=2y_j y_{j+1}\); when even it gives \(2x_jx_{j+1}\). In either case the two corresponding incidence coordinates are the scalar-path amplitudes at vertices \(j\) and \(j+2\), giving
\[
\frac{\partial\lambda}{\partial t_j}\bigg|_{t\equiv1}=4\psi_j\psi_{j+2}.
\]
Differentiation of \(w/\tau=\sqrt\lambda/2\), together with \(t_j=r\) exactly at defects, yields the displayed coefficient. Simplicity of the top eigenvalue ensures a genuine analytic remainder of order \((1-r)^2\) for each fixed word.

**5. Three-edge example.** For \((+,+,-)\) the consecutive overlaps are \((r,1)\). The three-dimensional product \(G_{\mathrm o}G_{\mathrm e}\) has eigenvalues \(0\) and \((3\pm\sqrt{1+4r^2})/2\). Substitution into the Gram formula gives the stated radical expression.

## Verification
`verify.py` independently constructs the full \(2m\)-dimensional complex block matrix, compares its Hermitian-part largest eigenvalue with the much smaller Gram product, and tests endpoint, monotonicity, and first-variation predictions. The script requires Python 3 and NumPy, uses deterministic finite tests, and prints its completed assertion count. The analytic proof, not finite computation, establishes the theorem for all \(m\), all words, and all complex Hilbert spaces.

## Relationship to prior work
Audeh, Kittaneh and Moradi (2026), Corollary 2.1, prove the sharp \(\|R\|\cos(\pi/(m+1))\) formula for strictly alternating operator/adjoint block paths with **arbitrary** bounded block operator. This theorem credits and retains that case as a known endpoint. Its new content concerns *every* orientation word for rank-one blocks: an exact two-Gram-matrix formula, strict word ordering away from zero overlap, the orthogonal-overlap run law, unique extremizers, and a position-sensitive first-order defect coefficient. Kittaneh, Rashid and Xu (2025) develop general upper/lower numerical-radius inequalities for block matrices, not these specific equality classifications. Standard singular-value factorization and Perron--Frobenius theory are used as classical tools, not claimed as new.

## Limitations
The formula assumes rank-one blocks and an open chain: no general claim is made for higher-rank blocks, cyclic closures, distinct operators on different edges, or other numerical-radius conventions. The spectral formula is finite-dimensional but need not simplify to radicals for long words. Full publication-priority certainty is unavailable: older specialized tensor/block-path results could imply part of the rank-one case. The cited 2026 source is a preprint, and no independent validation of this result has yet been performed.

## References
1. W. Audeh, F. Kittaneh, H. R. Moradi, *Integral Representations and Sharp Numerical Radius Inequalities for Hilbert Space Operators*, arXiv:2610.15242v1, first posted 2026-10-11, especially Corollary 2.1 and its proof. https://arxiv.org/html/2610.15242v1
2. F. Kittaneh, M. H. M. Rashid, Q. Xu, *A-numerical radius inequalities for operator matrices in semi-Hilbertian spaces*, Journal of Inequalities and Applications 2025:137, DOI 10.1186/s13660-025-03380-w. https://link.springer.com/article/10.1186/s13660-025-03380-w
3. R. A. Horn and C. R. Johnson, *Matrix Analysis*, Cambridge University Press, standard singular-value and Perron--Frobenius facts (background only).
