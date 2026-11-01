# Dedekind spectral finite parts and inverse-residue duality for balanced Hartogs concentration

## Finding

Fix relatively prime positive integers \(m,n\), and a real parameter \(0<a<1\). On the unweighted Bergman space \(A^2(H_{m,n})\), where
\[
H_{m,n}=\{(z,w)\in\mathbb C^2:|z|^m<|w|^n<1\},
\]
let \(T_a\) be the Toeplitz compression of the indicator of the balanced inner cusp core
\[
\Omega_a=\{(z,w)\in H_{m,n}: |z|<a|w|^{n/m},\ |w|<a^m\}.
\]
For \(r=1,\ldots,m\), let \(\rho_r\in\{1,\ldots,m\}\) be the representative satisfying \(\rho_r\equiv nr\pmod m\). Then \(T_a\) is positive, injective, compact, and belongs to every positive Schatten class. Its **complete eigenvalue list, including repetitions**, is
\[
\left\{a^{2(r+\rho_r+m(j+k))}:1\le r\le m,\quad j,k\in\mathbb Z_{\ge0}\right\}.
\]
In particular, for every real \(p>0\), the exact Schatten moment and its rational generating function are
\[
\operatorname{tr}(T_a^p)=F_{m,n}(a^{2p}),\qquad F_{m,n}(t)=\frac{\sum_{r=1}^m t^{r+\rho_r}}{(1-t^m)^2}\quad(0<t<1).
\]
The **finite part of the trace at the vanishing cutoff** detects the classical Dedekind sum:
\[
\boxed{F_{m,n}(t)=\frac{1}{m(1-t)^2}-\frac{2}{m(1-t)}+s(n,m)+\frac{m+3}{4m}+O_{m,n}(1-t),\quad t\uparrow1,}
\]
where
\[
s(n,m)=\sum_{r=1}^{m-1}\left(\frac rm-\frac12\right)\left(\frac{\rho_r}{m}-\frac12\right)
\]
(the sum is empty for \(m=1\)). Thus the two divergent coefficients are independent of \(n\), whereas the finite part depends on its residue modulo \(m\). Moreover \(T_a\) for \(n\) and \(n'\) have identical positive spectra whenever \(n'\equiv n\pmod m\) **or** \(n'\equiv n^{-1}\pmod m\), with each pair of Hartogs domains defined using its own exponent. The latter is a non-obvious inverse-residue isospectral duality. For example, \(m=5\) and \(n=2,3\) give equal spectra, whereas \(n=1\) has \(s(1,5)=1/5\) and \(n=2\) has \(s(2,5)=0\), distinguishing their finite parts despite identical leading divergent terms.

For each integer \(\ell\ge2\), the multiplicity of the eigenvalue \(a^{2\ell}\) is exactly
\[
h_\ell=\#\{1\le q<\ell:(n+1)q\equiv\ell\pmod m\}.
\]
If \(d=\gcd(m,n+1)>1\), entire spectral shells with \(d\nmid\ell\) are absent. Finally, the counting function of eigenvalues strictly larger than \(\varepsilon\) satisfies
\[
N_a(\varepsilon)=\frac{\log^2(1/\varepsilon)}{8m\log^2(1/a)}+O_{m,n,a}(\log(1/\varepsilon))\qquad(\varepsilon\downarrow0).
\]

## Assumptions and scope

The Bergman measure is ordinary four-dimensional Lebesgue measure; scaling it by a global positive constant does not change the compressed projection. The exponent pair \((m,n)\) is coprime and positive, and the logarithmic cutoff \(a\) lies strictly between zero and one. A positive Schatten exponent \(p\) can be any positive real, including \(p<1\), when the spectral sum \(\sum\lambda^p\) is understood as the standard Schatten quasi-norm moment. No conclusion is asserted for nonradial cutoffs or irrational Hartogs exponents. The notation \(n^{-1}\pmod m\) denotes multiplicative inversion in \((\mathbb Z/m\mathbb Z)^\times\), with \(m=1\) handled trivially.

## Proof

**1. Basis and integrability.** Laurent expansion in \(w\), Taylor expansion in \(z\), and separate circle invariance give an orthogonal complete family \(z^{q-1}w^k\) for \(q\in\mathbb Z_{\ge1}\) and \(k\in\mathbb Z\) for which the norm is finite. With \(s=m(k+1)+nq\), polar integration first in \(z\) and then in \(w\) makes that integrability condition exactly \(s\ge1\):
\[
\|z^{q-1}w^k\|_{A^2(H_{m,n})}^2
=\frac{(2\pi)^2}{2q}\int_0^1 R^{2s/m-1}\,dR
=\frac{\pi^2m}{qs},
\]
where the angular integrals contribute \(4\pi^2\) and the radial \(z\)-integral contributes \(1/(2q)\). Completeness follows by taking torus Fourier coefficients of a holomorphic square-integrable function: each coefficient is a Laurent monomial in \(w\) times a Taylor monomial in \(z\), and norm-finiteness restricts to the displayed index set.

**2. Eigenvalues.** The torus-invariant characteristic symbol makes the normalized monomial basis diagonal. Its restricted squared norm, relative to the full norm, is the product of the \(z\)-radius factor \(a^{2q}\) and the outer \(w\)-radius factor \((a^m)^{2s/m}=a^{2s}\). Hence its eigenvalue is \(a^{2(q+s)}\). The lattice consists exactly of all integers \(q,s\ge1\) with \(s\equiv nq\pmod m\), since \(k=s/m-1-nq/m\) must be an integer. Every \(q,s\) pair corresponds to exactly one monomial, so there are no hidden multiplicities.

**3. Geometric series and multiplicities.** Each congruence-lattice pair is uniquely \(q=r+jm\), \(s=\rho_r+km\), with \(1\le r\le m\) and \(j,k\ge0\). The eigenvalues thus form the announced multiset, and summing their \(p\)th powers gives the rational generating function. The exponential decay in \(j+k\) proves membership in every positive Schatten class. Fixing \(\ell=q+s\) gives \(s=\ell-q\) and hence \((n+1)q\equiv\ell\pmod m\), proving the shell count and the necessary missing-shell condition.

**4. Exact finite part.** Put \(u=1-t\), \(A_r=r+\rho_r\). Since multiplication by \(n\) permutes the nonzero residues, \(\sum_rA_r=m(m+1)\). Expand the finite numerator by the binomial theorem through \(u^2\) and the denominator via \((1-(1-u)^m)^2\):
\[
F_{m,n}(1-u)=\frac1{mu^2}-\frac2{mu}+\frac1{m^2}\sum_{r=1}^{m}r\rho_r-\frac{m^2+2m-3}{4m}+O_{m,n}(u).
\]
Direct expansion of the definition of the Dedekind sum gives
\[
\sum_{r=1}^{m}r\rho_r=m^2\left(s(n,m)+\frac{m+3}{4}\right),
\]
including the case \(m=1\). Substitution gives the claimed constant term. Because the finite numerator and denominator are polynomials, the displayed remainder holds in the stated one-sided limit without any nonuniform interchange of infinite sums.

**5. Inverse-residue isospectrality.** Replacing \(n\) by a congruent residue leaves every \(\rho_r\) unchanged. If \(n'\equiv n^{-1}\pmod m\), then the graph \(\{(r,\rho_r):r=1,\ldots,m\}\) is sent to the graph for \(n'\) by switching the two coordinates. The numerator \(\sum_rt^{r+\rho_r}\) is invariant under this swap, giving identical positive eigenvalues and multiplicities, for every \(a\).

**6. Counting.** There is one lattice point for each congruence condition \(s\equiv nq\pmod m\). For \(B\to\infty\), in each residue class \(q=r+jm\), the number of \(s\ge1\), \(s\equiv nq\pmod m\) satisfying \(q+s\le B\) differs from \((B-q)_+/m\) by at most one. Summing over \(1\le q<B\) gives \(B^2/(2m)+O_{m,n}(B)\). Taking \(B=\log(1/\varepsilon)/(2\log(1/a))\) and accounting for strict versus weak inequality changes the count by at most \(O(B)\), yielding the formula.

## Verification

The accompanying standalone `CHECK.py` independently computes the congruence spectrum against block decompositions, checks each coefficient against direct shell counting, verifies the Dedekind identity with exact rational arithmetic, tests inverse-residue spectral symmetry, checks the quadratic asymptotic estimator, and compares actual normalized monomial integrals to eigenvalue formulas. All such finite tests are supplementary: the proof above establishes the infinite-dimensional identities. Reproduce with `python CHECK.py` using Python 3 and its standard library. No numerical extrapolation is used as a proof.

## Relationship to prior work

The generalized Hartogs monomial integrability criterion and the study of radial Bergman–Toeplitz operators are established in the literature [1, 2]. Earlier articles establish Bergman kernels and \(L^p\)-regularity for monomial polyhedra [3–6]. The present object is instead the characteristic-function compression of a *balanced two-parameter cusp core*, with an exact compact spectrum; the significant additional statement is the Dedekind-sum finite part and inverse-residue isospectrality. The rational series resembles a classical cyclic-congruence Hilbert series, but recognizing it as the entire singular spectrum of a natural Toeplitz concentration operator supplies the operator-theoretic assertion. Dedekind sums and their inversion symmetry are classical: novelty is not claimed for those stand-alone arithmetic identities.

## Limitations

The finite part depends on the moduli \(m\) and \(n\bmod m\); it does not uniquely recover \(n\) because the inverse-residue isospectral pairs have identical spectra. The counting theorem gives a leading term and a first-order error, not an exact periodic remainder. No sharp eigenfunction localization beyond monomial diagonalization is asserted. Historical priority concerning spectral uses of congruence Hilbert series is not independently certified.

## References

1. Khanh, Liu and Thuc (2018), *Bergman–Toeplitz operators on fat Hartogs triangles*, arXiv:1802.09174.
2. Balay, Neutgens, Rosen, Wagner and Zeytuncu (2020), *Lp Regularity of Toeplitz Operators on Generalized Hartogs Triangles*, arXiv:2009.07260.
3. Fu, Deng and Cao (2022), *Lp regularity of the Bergman projection on generalizations of the Hartogs triangle*, arXiv:2203.06938.
4. Almughrabi (2023), *Bergman Kernels of Two Dimensional Monomial Polyhedra*, arXiv:2303.14268.
5. Chakrabarti and collaborators (2023), *Bergman kernels of monomial polyhedra*, arXiv:2308.05834.
6. Chakrabarti, Tang and Zhang (2024), *Toeplitz operators on monomial polyhedra*, DOI:10.1007/s10231-024-01495-3.
