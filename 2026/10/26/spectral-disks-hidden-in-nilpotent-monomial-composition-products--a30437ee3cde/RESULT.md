# Spectral disks hidden in nilpotent monomial-composition products

## Finding

Let \(m,n\ge 2\) be distinct coprime integers. Let \((c_k)_{k\ge0}\) be a strictly positive sequence with \(c_0=1\) that is regularly varying with real index \(\beta\), meaning that for each real \(s>0\), \(c_{\lfloor sk\rfloor}/c_k\to s^\beta\) as \(k\to\infty\). Let \(\mathcal H_c\) be the analytic coefficient Hilbert space on the unit disk in which \(e_k(z)=c_k z^k\), \(k\ge0\), is an orthonormal basis. Write \(C_d f(z)=f(z^d)\) and \(T=C_m C_n^*\). Set \(\rho=(mn)^{-\beta}\).

Both composition operators are bounded. Their product satisfies the following exact spectral classification:

\[
\sigma(T)=\{1\}\cup\{\lambda\in\mathbb C:|\lambda|\le\rho\},\qquad
\sigma_{\mathrm{ess}}(T)=\{\lambda\in\mathbb C:|\lambda|\le\rho\},\qquad
\sigma_{\mathrm p}(T)=\{0,1\}.
\]

Here \(\sigma_{\mathrm{ess}}\) is the Fredholm essential spectrum and \(\sigma_{\mathrm p}\) is the point spectrum. The eigenvalue \(1\) is simple, while \(0\) has infinite multiplicity. Every \(\lambda\) with \(0<|\lambda|\le\rho\) and \(\lambda\ne1\) belongs to the continuous spectrum in the sense that \(T-\lambda I\) is injective with dense, nonclosed range. The essential norm is exact:

\[
\|T\|_{\mathrm{ess}}=\rho.
\]

Consequently, the index \(\beta>0\) yields an isolated simple eigenvalue \(1\) outside an essential spectral disk of radius less than one; at \(\beta=0\), the eigenvalue lies on the disk boundary; and at \(\beta<0\), it is embedded in the interior.

## Assumptions and scope

The regular-variation hypothesis is imposed on positive coefficients, with no monotonicity assumption. It implies \(c_k^{1/k}\to1\) and \(c_{dk}/c_k\to d^\beta\) for every fixed positive integer \(d\). Therefore the coefficient series define analytic functions throughout \(\mathbb D\). The Hilbert norm is

\[
\left\|\sum_{k=0}^\infty a_k z^k\right\|_c^2
=\sum_{k=0}^\infty\frac{|a_k|^2}{c_k^2},
\]

and is understood only for finite right-hand side. The theorem concerns the orientation \(C_m C_n^*\). Reversing the factors takes the Hilbert-space adjoint, hence preserves the two spectral sets but interchanges point and residual behavior; no assertion about the reversed product's fine spectrum is needed here. Coprimality is used to create arbitrarily long **finite** paths with no periodic or infinite components; the theorem does not purport to cover pairs with a common divisor.

The classical weighted Bergman spaces \(A^2_\alpha(\mathbb D)\), \(\alpha>-1\), have \(c_k=\bigl[\Gamma(k+\alpha+2)/(\Gamma(\alpha+2)\Gamma(k+1))\bigr]^{1/2}\), and therefore \(\beta=(\alpha+1)/2\). In particular, on ordinary Bergman space \(\rho=(mn)^{-1/2}\). On Hardy \(H^2\), \(c_k=1\), so \(\rho=1\). On the coefficient Dirichlet space with \(c_k=(k+1)^{-1/2}\), one has \(\rho=(mn)^{1/2}\).

## Proof

**1. Exact action and boundedness.** Since \(C_d e_k=(c_k/c_{dk})e_{dk}\) and \(C_d^*e_{dk}=(c_k/c_{dk})e_k\), orthogonality of the monomial basis gives

\[
Te_0=e_0,\qquad
Te_{nk}=w_k e_{mk}\quad(k\ge1),\qquad
Te_j=0\quad(j\ge1,\ n\nmid j),
\]

where

\[
w_k=\frac{c_k^2}{c_{mk}c_{nk}}>0,\qquad
\lim_{k\to\infty}w_k=\rho.
\]

The same regular-variation ratios show \(\sup_k c_k/c_{dk}<\infty\) for each \(d\), proving boundedness of \(C_m,C_n\), and hence \(T\).

**2. Finite-path decomposition.** On positive monomial indices the sole possible directed edge is \(nk\longrightarrow mk\), of weight \(w_k\). Both indegree and outdegree are at most one. If there are \(q\) consecutive forward edges from a positive integer \(j\), then \(n^q\mid j\); the coprimality of \(m,n\) is essential for this implication. Thus forward paths terminate. Likewise \(m^q\mid j\) is necessary for \(q\) consecutive reverse edges, so reverse paths terminate too. Every connected component is a finite directed path (possibly one vertex); its span reduces \(T\). There are no nonzero eigenvalues on this nonconstant subspace because a coordinatewise eigenvector would have to be a nonzero eigenvector of a finite nilpotent block, impossible at a nonzero eigenvalue. The constant vector is the only eigenvector for eigenvalue \(1\). All positive indices not divisible by \(n\) lie in \(\ker T\), so this kernel is infinite-dimensional. It follows that \(\sigma_{\mathrm p}(T)=\{0,1\}\), with \(1\) simple. Applying the same finite-path argument to the adjoint gives \(\sigma_{\mathrm p}(T^*)=\{0,1\}\).

**3. The essential norm.** Apart from the rank-one constant summand, the operator is a weighted partial permutation with mutually orthogonal nonzero column images. Truncating the columns \(e_{nk}\) for \(k<N\) gives a finite-rank approximation whose remaining operator norm is \(\sup_{k\ge N}w_k\to\rho\). Conversely \(e_{nk}\rightharpoonup0\), so every compact \(K\) satisfies \(\|Ke_{nk}\|\to0\). Thus \(\|T-K\|\ge\limsup_{k\to\infty}\|Te_{nk}\|=\rho\). Together, these bounds prove \(\|T\|_{\mathrm{ess}}=\rho\).

**4. A spectral disk from arbitrarily long nilpotent blocks.** For each integer \(L\ge1\), consider the \(L+1\) basis vectors

\[
f_{L,h}=e_{m^h n^{L-h}},\qquad h=0,1,\ldots,L.
\]

They form an entire reducing finite path: its beginning is not divisible by \(m\), its end is not divisible by \(n\), and the intermediate edges go from \(f_{L,h}\) to \(f_{L,h+1}\). Their weights are \(w_{m^h n^{L-h-1}}\), \(0\le h<L\). All their indices tend to infinity uniformly as \(L\to\infty\), because \(m^h n^{L-h-1}\ge\min(m,n)^{L-1}\). Consequently the maximum difference of these weights from \(\rho\) tends to zero. Paths for distinct lengths \(L\) are mutually orthogonal: unique prime-divisor arithmetic implies the equality \(m^h n^{L-h}=m^{h'}n^{L'-h'}\) forces \(h=h'\) and \(L=L'\).

Fix \(\lambda\) with \(0<|\lambda|\le\rho\). On the length-\(L\) path let

\[
 v_L=\frac{\sum_{h=0}^{L}(\overline\lambda/\rho)^h f_{L,h}}
 {\bigl(\sum_{h=0}^{L}(|\lambda|/\rho)^{2h}\bigr)^{1/2}}.
\]

The adjoint is the backward weighted shift on each path. Replacing all its weights by \(\rho\) would cancel \((T^*-\overline\lambda I)v_L\) at every component except the terminal one, whose norm is

\[
 |\lambda|\frac{(|\lambda|/\rho)^L}
 {\bigl(\sum_{h=0}^{L}(|\lambda|/\rho)^{2h}\bigr)^{1/2}}\to0.
\]

For \(|\lambda|<\rho\) this tends to zero geometrically, while on \(|\lambda|=\rho\) it is \(\rho/\sqrt{L+1}\). The true-weight error is bounded by \(\max_{0\le h<L}|w_{m^h n^{L-h-1}}-\rho|\to0\). Thus \(\|(T^*-\overline\lambda I)v_L\|\to0\). The unit vectors \(v_L\) are supported on pairwise orthogonal reducing blocks and are weakly null. For \(\lambda=0\), the unit vectors \(f_{L,0}\) are orthogonal elements of \(\ker T^*\). Hence \(T^*-\overline\lambda I\), and equivalently \(T-\lambda I\), is not Fredholm for **every** \(|\lambda|\le\rho\). This proves

\[
\{\lambda:|\lambda|\le\rho\}\subseteq\sigma_{\mathrm{ess}}(T).
\]

**5. No other essential or ordinary spectral values.** For any \(\varepsilon>0\), finitely many finite path components contain all basis indices below a sufficiently large threshold. Removing these finite-dimensional reducing components and the constants leaves a reducing summand \(R_\varepsilon\) satisfying \(\|T|_{R_\varepsilon}\|\le\rho+\varepsilon\). Indeed, every remaining nonzero edge comes from a source \(nk\) with large \(k\), and all its weights are below \(\rho+\varepsilon\). On the finite-dimensional complement the spectrum consists only of \(0\) and \(1\). Therefore, for \(|\lambda|>\rho\) with \(\lambda\ne1\), choose \(\varepsilon<|\lambda|-\rho\); the Neumann series inverts \(T-\lambda I\) on \(R_\varepsilon\), while the finite-dimensional complement is invertible because its only eigenvalues are \(0,1\). Thus \(\sigma(T)\subseteq\{1\}\cup\{\lambda:|\lambda|\le\rho\}\). Together with step 4 and the constant eigenvector this yields the two asserted spectral sets.

**6. Fine spectrum and index threshold.** For \(\lambda\ne0,1\) the finite-path argument proves both \(\ker(T-\lambda I)=\{0\}\) and \(\ker(T^*-\overline\lambda I)=\{0\}\), so the range is dense. At \(0<|\lambda|\le\rho\), the range cannot be closed: an injective operator with closed dense range would be invertible, contrary to step 4. At \(\lambda=1\), the kernel is exactly the one-dimensional constant subspace. Finally, \(\rho<1\), \(\rho=1\), or \(\rho>1\) precisely as \(\beta>0\), \(\beta=0\), or \(\beta<0\), giving the stated phase transition.

## Verification

The self-contained script `check_monomial_spectrum.py` executes \(9096\) exact integer and rational assertions for five coprime degree pairs, four coefficient exponents, finite arithmetic-path decompositions, and coefficient-ratio checks. It verifies finite cases only. No finite computation is used to infer the spectral assertions: regular variation, finite-path termination, uniform long-path weight convergence, Fredholm singular sequences, and the exterior resolvent argument are proved above.

Reproduce with `python check_monomial_spectrum.py` using the Python standard library only.

## Relationship to prior work

Leng and Zhao [1] study Schatten membership of mixed composition-adjoint products on Hardy and Bergman spaces, including inner and finite Blaschke symbols. Their published theorems do not assert an exact ordinary or Fredholm essential spectral set for distinct coprime power symbols. The exact degree-weight arithmetic above shows why all nonconstant reducing blocks are individually nilpotent despite a full essential spectral disk.

Clifford and Zheng [2] derive compactness criteria and an essential-norm upper bound for analogous products on weighted Bergman spaces; their Theorems 1.1–1.3 do not furnish an ordinary or essential spectral classification. Clifford, Dabkowski, Wiggins, and Zeytuncu [3] investigate compactness, finite rank, and adjoint ranges for Blaschke products on Hardy space; only the abstract was accessible during this comparison, so precise historical exclusion is not asserted. Accessible excerpts of Chalendar and Partington [4] treat monomial operators on a different underlying \(L^2(0,1)\) model, chiefly boundedness and compactness. They offer no apparent implication to the present mixed-product result; the complete article was not inspected.

The finite nilpotent-path mechanism is related to general direct-sum operator theory; the precise natural function-space identification and sharp three-regime essential-radius law are the conclusions proved here. A previously published equivalent finite-block direct-sum theorem or obscure special-case spectral calculation could still establish historical coverage; neither was identified in the comparisons undertaken.

## Limitations

The hypothesis that \(m,n\) be coprime and distinct is essential to this proof; common-divisor pairs may have infinite paths or other component structures. Regular variation is sufficient, not claimed necessary. The theorem does not classify weighted composition symbols beyond pure powers, and does not assert a Riesz basis of generalized eigenvectors for the operator's spectral points (there is only a direct sum of finite nilpotent blocks). Its originality assessment is self-review only and is not an independently certified priority determination.

## References

[1] Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1, posted 11 October 2026, https://arxiv.org/html/2610.15472v1.

[2] J. H. Clifford and D. Zheng, *Composition Operators on Bergman Spaces*, Chinese Annals of Mathematics, Ser. B 24 (2003), 433–448, DOI:10.1142/S0252959903000438, https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=24B404&flag=1.

[3] J. H. Clifford, M. Dabkowski, A. Wiggins and Y. E. Zeytuncu, *The operator \(C_\phi^* C_\psi\) when \(\phi\) is a Blaschke product*, Advances in Operator Theory 11 (2026), article 3, DOI:10.1007/s43036-025-00476-4.

[4] I. Chalendar and J. R. Partington, *Boundedness and compactness of weighted composition operators and monomial operators*, Archiv der Mathematik 121 (2023), 707–714, DOI:10.1007/s00013-023-01909-3.
