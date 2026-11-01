# Exact low-degree harmonic erasure spectra of the snub 24-cell

## Finding
Let \(T\subset S^3\) be the 24 vertices of the regular 24-cell, let \(X\subset S^3\) be the containing 120-vertex 600-cell, and let \(Y=X\setminus T\) be its 96-vertex snub 24-cell. For \(0\le\ell\le5\), evaluate an arbitrary complex orthonormal basis of exact-degree \(\ell\) spherical harmonics, normalized using probability surface measure on \(S^3\), at the 96 points. Write \(E_\ell\) for the resulting \(96\times(\ell+1)^2\) evaluation matrix. The **complete Gram spectra** of \(E_\ell^*E_\ell\), with multiplicities in parentheses, are

| Degree \(\ell\) | Spectrum of \(E_\ell^*E_\ell\) | Rank |
|:--:|:--|--:|
| 0 | \(96\;(1)\) | 1 |
| 1 | \(96\;(4)\) | 4 |
| 2 | \(96\;(9)\) | 9 |
| 3 | \(72\;(8),\ 120\;(8)\) | 16 |
| 4 | \(0\;(2),\ 80\;(9),\ 120\;(14)\) | 23 |
| 5 | \(48\;(12),\ 120\;(24)\) | 36 |

Thus the degree-four sampling map is not injective (nullity two), **although degree-five sampling is injective** and has exact spectral condition number \(\kappa_2(E_5)=\sqrt{5/2}\). Degrees zero through two give tight sampling frames with Gram scalar \(96\).

## Assumptions and scope
Use the standard inner product on \(\mathbb R^4\) and \(\varphi=(1+\sqrt5)/2\). Define \(T\) explicitly as all eight signed coordinate unit vectors and all sixteen vectors \((\pm1/2,\pm1/2,\pm1/2,\pm1/2)\). Define \(Y\) as the 96 even-coordinate permutations of \((0,\pm 1/2,\pm\varphi/2,\pm(\varphi-1)/2)\), with independent choices of the three signs. These two disjoint sets make \(X=T\cup Y\). The set \(Y\) is one of the two chiral snub 24-cell vertex configurations. Any congruent copy has identical sampling spectra. Each \(\mathcal H_\ell(S^3)\) has complex dimension \((\ell+1)^2\); the statement concerns **exact degree**, not the entire bandwidth \(0\le j\le\ell\). The numerical Gram eigenvalues depend on probability-surface-measure normalization, specified here.

## Proof
The addition formula for orthonormal degree-\(\ell\) harmonics on \(S^3\) gives the reproducing kernel
\[
Z_\ell(x,y)=(\ell+1)U_\ell(\langle x,y\rangle),
\]
where \(U_0(t)=1\), \(U_1(t)=2t\), and \(U_{j+1}(t)=2tU_j(t)-U_{j-1}(t)\). Consequently the nonzero spectra of \(E_{A,\ell}^*E_{A,\ell}\) and \(E_{A,\ell}E_{A,\ell}^*\) agree, and the latter is the matrix \((Z_\ell(x,y))_{x,y\in A}\).

The 600-cell's nine distinct pairwise inner products are \(1,\varphi/2,1/2,(\varphi-1)/2,0,-(\varphi-1)/2,-1/2,-\varphi/2,-1\). Direct exact intersection-number calculations over \(\mathbb Z[\varphi]\), independently replayable by `CHECK.py`, verify that for every \(0\le\ell\le5\)
\[
\Big(U_\ell(\langle x,y\rangle)\Big)_{x,y\in X}^{\!2}
=\frac{120}{\ell+1}\Big(U_\ell(\langle x,y\rangle)\Big)_{x,y\in X}.
\]
The matrix is positive semidefinite by the addition formula. Its diagonal is \(\ell+1\) on all 120 points, so its rank is \((\ell+1)^2\). Thus
\[
E_{X,\ell}^*E_{X,\ell}=120I_{(\ell+1)^2}\qquad(0\le\ell\le5).
\]

Next restrict the zonal kernel to the 24 points of \(T\). Here all pairwise inner products belong to \(\{1,1/2,0,-1/2,-1\}\), so every matrix entry is integral and direct multiplication is exact. The matrix \(K_{T,\ell}=(U_\ell(\langle x,y\rangle))_{x,y\in T}\) satisfies \(K_{T,\ell}^2=c_\ell K_{T,\ell}\) for \(\ell=0,1,2,3,5\) with \((c_0,c_1,c_2,c_3,c_5)=(24,12,8,12,12)\). Its trace \(24(\ell+1)\) determines the nonzero multiplicity in each case. In degree four it instead satisfies
\[
K_{T,4}(K_{T,4}-8I)(K_{T,4}-24I)=0,
\quad \operatorname{tr}K_{T,4}=120,\quad
\operatorname{tr}K_{T,4}^{2}=1728.
\]
The three possible eigenvalues are \(0,8,24\); the two traces force nonzero multiplicities \(9\) for \(8\) and \(2\) for \(24\). Multiplying by \(\ell+1\) yields the nonzero eigenvalues of \(E_{T,\ell}^*E_{T,\ell}\): respectively \(24\;(1)\), \(24\;(4)\), \(24\;(9)\), \(48\;(8)\), \(40\;(9),120\;(2)\), and \(72\;(12)\). All unlisted directions in \(\mathcal H_\ell(S^3)\) have eigenvalue zero for \(E_{T,\ell}^*E_{T,\ell}\).

Finally, since \(X=T\mathbin{\dot\cup}Y\),
\[
E_{Y,\ell}^*E_{Y,\ell}
=E_{X,\ell}^*E_{X,\ell}-E_{T,\ell}^*E_{T,\ell}
=120I-E_{T,\ell}^*E_{T,\ell}.
\]
Subtracting each exact eigenvalue from \(120\), and including the complementary multiplicities, yields the six asserted spectra. In degree four the two \(120\)-eigenvectors of the deleted subgroup produce precisely two zero Gram eigenvalues; degree five has smallest eigenvalue \(48>0\).

## Verification
Run `python3 CHECK.py` from the extracted package. It constructs the 120 vertices in exact arithmetic over \(\mathbb Z[\varphi]\), checks all nine radial association-scheme intersection identities for every vertex pair, verifies the six full-set tight-frame identities, proves the 24-cell kernel polynomial identities and traces over integers, and rederives the six complementary Gram spectra. All checks are finite exact equalities, not floating-point tests. The general harmonic addition formula and the geometry of the explicit coordinates are proved independently of the checker; the checker verifies their nonstandard finite algebraic consequences.

## Relationship to prior work
Koca–Al-Ajmi–Koca (arXiv:0906.2109, first posted 2009-06-11) describe the 120-point quaternionic root configuration and its \(24+96\) subdivision; Koca–Koca–Al-Barwani (arXiv:1106.3433, 2011) analyze the snub 24-cell configuration. Bannai–Okuda–Tagami (arXiv:1308.5101, 2013) discuss the 600-cell as a harmonic-index design, including index 58, but not the present Gram spectra. Kostant's 1985 McKay correspondence develops decomposition of symmetric-power representations restricted to finite subgroups of \(SU(2)\), a powerful related framework; the complement \(Y\), however, is not a subgroup, and this precise comparative low-degree erasure spectrum is not stated in the inspected material. The analytic idea that a tight large-set frame minus a structured subgroup frame can lose injectivity at one degree and regain it at the next is the specific new calculation under bounded prior-art review.

## Limitations
The classification is for the 96-point snub 24-cell and exact degrees zero through five only. It does not establish low-pass sampling ranks, higher-degree spectra, optimality among all 96-point configurations, or arbitrary erasure robustness. The old representation-theoretic literature may yield an equivalent calculation after further specialization, so independent originality assessment is needed. This work has no independent mathematical audit or validation.

## References
- M. Koca, M. Al-Ajmi, N. O. Koca, *Quaternionic Representation of Snub 24-Cell and its Dual Polytope Derived From E8 Root System*, arXiv:0906.2109 (first version 2009-06-11), https://arxiv.org/abs/0906.2109.
- M. Koca, N. O. Koca, M. Al-Barwani, *Snub 24-Cell Derived from the Coxeter-Weyl Group W(D4)*, arXiv:1106.3433 (first version 2011-06-17), https://arxiv.org/abs/1106.3433.
- E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101 (first version 2013-08-23), https://arxiv.org/abs/1308.5101.
- B. Kostant, *The McKay correspondence, the Coxeter element and representation theory*, Astérisque S131 (1985), 209–255, https://www.numdam.org/item/AST_1985__S131__209_0/.
