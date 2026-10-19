# Exact one-parameter flat-band design for cyclic resonator-decorated sawtooth chains

## Finding

A periodically repeated finite resonator attached to the two neighboring sites of a one-dimensional hopping backbone admits **exactly as many flat-band tuning points as resonator sites** when the attached vertex is cyclic. Each tuning point creates exactly one *isolated*, two-cell-localized flat band, and its position among the Bloch bands can be prescribed from the lowest through the next-to-highest band.

For a resonator with \(m\ge2\) sites, denote its eigenvalues \(\beta_1<\cdots<\beta_m\), and the root spectral weights by \(\rho_i>0\). Given fixed positive backbone and attachment hoppings \(a,b\), define \(E_j\) as the unique solutions of
\[
\sum_{i=1}^{m}\frac{\rho_i}{\beta_i-E_j}=\frac{a}{b^2},\qquad E_1<\beta_1,\qquad \beta_{j-1}<E_j<\beta_j\quad(2\le j\le m).
\]
Then **all and only** the onsite choices \(u_j=E_j+2a\) admit a flat band. The flat band is exactly the \(j\)-th lowest spectral branch of the \(m+1\)-band system, simple and separated from the other bands by a uniform positive gap. There are no other flat-band energies at a given onsite choice.

When the resonator is a length-\(m\) path with constant positive hopping \(c\), and is attached at an endpoint, the flat energies are the distinct real zeros of
\[
a c\,U_m(E/(2c))+b^2 U_{m-1}(E/(2c))=0,
\]
where \(U_j\) denotes the Chebyshev polynomial of the second kind. The tuning value is again \(u=E+2a\).

## Assumptions and scope

Fix an integer \(m\ge2\), a real symmetric \(m\times m\) matrix \(K\), and a real unit vector \(e\) **cyclic for \(K\)**, meaning that \(e,Ke,\ldots,K^{m-1}e\) span \(\mathbb R^m\). Let \(a,b>0\). A unit cell comprises one backbone site \(A_n\) and a copy of the resonator \(K\) with root \(e\). Adjacent backbone sites have hopping \(a\); the root couples with hopping \(b\) to each of the backbone sites on its left and right. The only adjustable parameter is the real onsite energy \(u\) on every backbone site. In the Bloch convention used here,
\[
H_u(z)=\begin{pmatrix}
u+a(z+z^{-1})&b(1+z^{-1})e^{\mathsf T}\\
b(1+z)e&K
\end{pmatrix},\qquad \lvert z\rvert=1.
\]
This defines a self-adjoint, bounded periodic tight-binding Hamiltonian on an infinite one-dimensional lattice. The hypotheses permit arbitrary finite real symmetric resonators and specialize to physical weighted paths with endpoint attachment. A flat band is an energy which is an eigenvalue of \(H_u(z)\) for *every* \(|z|=1\). A compact localized state has finitely many occupied unit cells.

## Proof

**1. Root cyclicity and poles.** The spectral theorem and cyclicity give \(m\) *distinct* eigenvalues \(\beta_1<\cdots<\beta_m\) of \(K\), with nonzero projections on \(e\): \(\rho_i=\lvert\langle e,v_i\rangle\rvert^2>0\) and \(\sum_i\rho_i=1\). Write
\[
P(E)=\det(EI-K),\qquad D(E)=e^{\mathsf T}\operatorname{adj}(EI-K)e,
\]
so that \(D(E)/P(E)=\sum_i\rho_i/(E-\beta_i)\) whenever \(E\) is not a resonator eigenvalue. In particular, at any \(\beta_i\) the polynomial \(D\) does *not* vanish: \(D(\beta_i)=\rho_i\prod_{\ell\ne i}(\beta_i-\beta_\ell)\ne0\).

**2. Exhaustive flat-band criterion.** Expanding the characteristic polynomial by its backbone row gives
\[
\det(H_u(z)-EI)=(-1)^m\big[\big(u-E+a(z+z^{-1})\big)P(E)+b^2(2+z+z^{-1})D(E)\big].
\]
If \(E=\beta_i\), the Laurent polynomial is nonconstant and nonzero because \(D(\beta_i)\ne0\) and \(b>0\); hence no resonator eigenvalue is flat. Otherwise, vanishing identically in \(z\) requires both
\[
aP(E)+b^2D(E)=0\quad\text{and}\quad (u-E)P(E)+2b^2D(E)=0.
\]
These are equivalent to
\[
G(E):=\sum_{i=1}^m\frac{\rho_i}{\beta_i-E}=\frac{a}{b^2},\qquad u=E+2a.
\]
No other flat energies or tuning values are possible.

**3. Exact count and placement.** On every open interval away from its poles, \(G'(E)=\sum_i\rho_i/(\beta_i-E)^2>0\). On \(( -\infty,\beta_1)\) it increases from \(0\) to \(+\infty\); between consecutive poles it increases from \(-\infty\) to \(+\infty\); and on \((\beta_m,\infty)\) it is negative, increasing to \(0\). Since \(a/b^2>0\), there is exactly one solution in each of the first \(m\) intervals and none above \(\beta_m\). These solutions and hence the tuning values are distinct.

At \(z=-1\), all backbone-resonator hopping terms vanish, and \(H_{u_j}(-1)=\operatorname{diag}(u_j-2a,K)=\operatorname{diag}(E_j,K)\). Hence \(E_j\) is the \(j\)-th eigenvalue in increasing order (one-based). At \(z\ne-1\), diagonalizing \(K\) turns the Bloch matrix into a Hermitian arrowhead matrix whose offdiagonal couplings have magnitudes \(b|1+z|\sqrt{\rho_i}>0\). Its characteristic eigenvalues are all simple: the secular function has strictly monotone derivative between consecutive simple poles, and no pole is an eigenvalue. At \(z=-1\), the eigenvalues \(E_j,\beta_1,\ldots,\beta_m\) are again simple. Eigenvalues depend continuously on \(z\), so their ordering cannot change. Thus the flat eigenvalue stays the \(j\)-th lowest for all \(z\), and compactness of the unit circle implies a uniform strictly positive spectral gap to its neighbors.

**4. Compact localization and minimality.** The Laurent-polynomial eigenvector
\[
\Psi_j(z)=\begin{pmatrix}1\\-b(1+z)(K-E_jI)^{-1}e\end{pmatrix}
\]
satisfies \((H_{u_j}(z)-E_j I)\Psi_j(z)=0\) identically. Its inverse Bloch transform has support on at most two neighboring unit cells and is nonzero in both because \(b>0\) and \((K-E_jI)^{-1}e\ne0\). The flat band is simple at every momentum, so any one-cell eigenvector would have a constant Bloch vector \((x,y)\) in the kernel at every \(z\). Its lower block equation reads \(b(1+z)ex+(K-E_jI)y=0\) for all \(z\), forcing \(x=0\) and then \(y=0\), a contradiction. Since any Bloch eigenfunction at fixed energy is a scalar multiple of \(\Psi_j(z)\) almost everywhere, its full point eigenspace is the closed span of the translates of the compact eigenfunction.

**5. Explicit path specialization.** For \(K=cA(P_m)\), rooted at an endpoint, the root is cyclic. The determinants obey \(P_m(E)=E P_{m-1}(E)-c^2P_{m-2}(E)\) with \(P_0=1,P_1=E\), giving \(P_m(E)=c^mU_m(E/(2c))\). The root cofactor equals \(D_m(E)=P_{m-1}(E)=c^{m-1}U_{m-1}(E/(2c))\). Substitution into \(aP+b^2D=0\) yields the displayed degree-\(m\) Chebyshev polynomial and proves that all its \(m\) roots are simple and real in the specified interlacing intervals.

## Verification

The accompanying `verify.py` checks the characteristic Laurent-polynomial identity and the path Chebyshev polynomials symbolically for path orders 1–5. Separately it diagonalizes Bloch matrices for path resonators of lengths 1–12, two positive hopping profiles, every tuning index and five momenta, checking eigenvalue position, uniqueness and the residual of the displayed compact-state Bloch eigenvector. Its recorded output is `VERIFY_OK exact_characteristic_orders= 5 tuning_spectra= 780 motif_lengths=1..12 band_ranks=1..m`. The Python checker requires NumPy, SciPy and SymPy. These finite calculations corroborate the unrestricted symbolic proof but are not a substitute for it.

## Relationship to prior work

Sabri and Youssef (2023) establish the mathematical Floquet framework for periodic-graph flat bands, compactly supported eigenvectors and the significance of potential tuning, including general flat-band generators. The 2017 and 2019 studies by Maimaiti and collaborators develop compact-localized-state flat-band generators, including arbitrary-size construction schemes; their methods motivate but do not explicitly give the **exact count of one-parameter tuning points and ordered isolated bands for this fixed arbitrary cyclic resonator**. Danieli and collaborators (2024) survey lattice flat-band tuning and sawtooth photonic realizations. Existing ordinary two-band sawtooth models give a special case, not this all-order interlacing result. General generator papers may conceivably imply the result after a nontrivial reduction; that is a residual priority risk. An earlier classification of a periodic triangle-bridge model addresses a different graph and potential locus, and a magnetic diamond-chain classification has different intercell geometry.

## Limitations

The cyclic-root hypothesis is essential for the stated exact count: uncoupled resonator eigenvectors can otherwise create additional always-flat bands. The hopping strengths \(a,b\) are strictly positive; the formula need not hold at zero coupling. The theorem concerns one-dimensional, real-Hermitian finite motifs and exactly the stated couplings, not arbitrary magnetic phases, nonlinear interactions, disorder or stability to arbitrary perturbations. Gap sizes are proved positive but no uniform lower bound over all resonator matrices is asserted. No independent audit or external priority certification has been performed.

## References

1. M. Sabri and P. Youssef, *Flat bands of periodic graphs*, arXiv:2304.06465 (first submitted 13 April 2023), especially §§2–3 and 7; primary MSC 81Q10.
2. W. Maimaiti et al., *Compact localized states and flatband generators in one dimension*, arXiv:1610.02970.
3. W. Maimaiti et al., *Universal \(d=1\) flat band generator from compact localized states*, arXiv:1810.08199.
4. C. Danieli et al., *Flat band fine-tuning and its photonic applications*, *Nanophotonics* (2024), doi:10.1515/nanoph-2024-0135.
5. A. Honecker and J. Richter, *Enhanced low-temperature entropy and flat-band ferromagnetism in the \(t\)-\(J\) model on the sawtooth lattice*, arXiv:0805.1151; a conventional sawtooth flat-band antecedent.
