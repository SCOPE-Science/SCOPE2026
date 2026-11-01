# First-order Schatten spectra and Jordan-rate constants for affine Fock iterates

## Finding

Fix a positive integer \(d\) and let \(\mathcal F_d\) be the complex Bargmann--Fock Hilbert space with
\[
\|f\|_{\mathcal F_d}^{2}=\pi^{-d}\int_{\mathbb C^d}|f(z)|^{2}e^{-|z|^{2}}\,dV(z),\qquad K_w(z)=e^{z\cdot\overline w}.
\]
Write \(\mathcal S_p\) for the Schatten ideal with \(1\le p<\infty\), and interpret \(\mathcal S_\infty\) as the operator norm. Every matrix norm without an ideal subscript is the Euclidean operator norm. For \(u\in\mathbb C^d\) put
\[
P_uf=f(u)\boldsymbol1,\qquad G_u=I_d+\overline u\,u^{\mathsf T}.
\]
Here \(u\) is a column, so \(G_u\) is positive Hermitian; \(B^{\mathsf T}\) is the ordinary **transpose**, not the adjoint.

**Local finite-rank Schatten law.** There are constants \(\eta_{d,u}>0\) and \(K_{d,u}<\infty\) such that, whenever \(B\in\mathbb C^{d\times d}\) and \(\|B\|\le\eta_{d,u}\), the composition operator associated with \(z\mapsto u+B(z-u)\) satisfies
\[
C_{u+B(\cdot-u)}-P_u=L_{B,u}+R_{B,u},\qquad \|R_{B,u}\|_{\mathcal S_1}\le K_{d,u}\|B\|^2,
\]
where the rank-at-most-\(d\) operator is
\[
(L_{B,u}f)(z)=\sum_{i,j=1}^d B_{ij}(z_j-u_j)\,\partial_i f(u).
\]
Its nonzero singular values, padded to length \(d\), are **exactly**
\[
s_j(L_{B,u})=e^{|u|^2/2}\,s_j\!\left(G_u^{1/2}B^{\mathsf T}G_u^{1/2}\right),\qquad 1\le j\le d.
\]
Consequently, for \(1\le j\le d\),
\[
\left|s_j(C_{u+B(\cdot-u)}-P_u)-e^{|u|^2/2}s_j(G_u^{1/2}B^{\mathsf T}G_u^{1/2})\right|\le K_{d,u}\|B\|^2,
\]
while \(s_j(C_{u+B(\cdot-u)}-P_u)\le K_{d,u}\|B\|^2\) for \(j>d\). Moreover, simultaneously for every \(1\le p\le\infty\),
\[
\left|\|C_{u+B(\cdot-u)}-P_u\|_{\mathcal S_p}-e^{|u|^2/2}\|G_u^{1/2}B^{\mathsf T}G_u^{1/2}\|_{\mathcal S_p}\right|\le K_{d,u}\|B\|^2.
\]
In particular the entire first-order singular spectrum is finite-dimensional, and the tail beyond dimension \(d\) is quadratically small in trace norm.

**Sharp iteration law.** If \(A\in\mathbb C^{d\times d}\) satisfies \(\|A\|<1\), and \(\phi(z)=Az+(I_d-A)u\), then \(C_\phi^n\to P_u\) in every \(\mathcal S_p\) norm, \(1\le p\le\infty\). For all sufficiently large integers \(n\),
\[
\left|\|C_\phi^n-P_u\|_{\mathcal S_p}-e^{|u|^2/2}\|G_u^{1/2}(A^n)^{\mathsf T}G_u^{1/2}\|_{\mathcal S_p}\right|\le K_{d,u}\|A^n\|^2.
\]
The preceding individual-singular-value estimates also apply with \(B=A^n\).

Suppose further that \(A\) has a **unique** eigenvalue \(\lambda\ne0\) whose modulus \(r=|\lambda|\) equals its spectral radius, and let \(k\) be the size of the largest Jordan block belonging to \(\lambda\). Let \(P_\lambda\) denote its Riesz spectral projection, and set
\[
D_\lambda=(A-\lambda I_d)^{k-1}P_\lambda\ne0.
\]
For every \(1\le p\le\infty\) the exact normalized limit is
\[
\boxed{\lim_{n\to\infty}\frac{\|C_\phi^n-P_u\|_{\mathcal S_p}}{n^{k-1}r^{n-k+1}}
=\frac{e^{|u|^2/2}}{(k-1)!}\big\|G_u^{1/2}D_\lambda^{\mathsf T}G_u^{1/2}\big\|_{\mathcal S_p}.}
\]
This positive coefficient records both the nonnormal Jordan geometry and the displacement of the fixed point. No unique-eigenvalue hypothesis is needed for the general finite-dimensional matrix formula. If \(A\) is nilpotent, then \(C_\phi^n=P_u\) for all sufficiently large \(n\).

For illustration, let \(d=2\) and \(A=\begin{psmallmatrix}\lambda&t\\0&\lambda\end{psmallmatrix}\) with \(t\ne0\), \(0<|\lambda|\) and \(|\lambda|+|t|<1\). Then every Schatten norm has the same sharp leading constant:
\[
\boxed{\lim_{n\to\infty}\frac{\|C_\phi^n-P_u\|_{\mathcal S_p}}{n|\lambda|^{n-1}}=|t|e^{|u|^2/2}\sqrt{(1+|u_1|^2)(1+|u_2|^2)}.}
\]
Thus a nonnormal two-dimensional linear symbol yields a genuine polynomial-times-exponential convergence law, rather than a pure geometric rate.

## Assumptions and scope

The base field is complex. The Fock normalization is explicitly given above and is essential for the coefficient \(e^{|u|^2/2}\); a convention with reproducing kernel \(e^{z\cdot\bar w/2}\) changes the constants. The local theorem holds in every fixed finite dimension \(d\). The iteration theorem assumes \(\|A\|<1\), which ensures the affine symbol induces a bounded compact composition operator; it is not asserted for all symbols with spectral radius below one. Results in \(\mathcal S_p\) are asserted only for \(p\ge1\). The existence of a simple asymptotic limit after a scalar geometric-polynomial rescaling is asserted only when there is a unique dominant eigenvalue; multiple co-dominant eigenvalues can cause oscillations.

## Proof

**1. A trace-norm Taylor expansion.** Fix \(u\). For \(B\ne0\), put \(b=\|B\|\) and \(\psi_t(z)=u+tB(z-u)\). Choose \(\delta=1/4\). On the complex disk \(|t|\le\delta/b\), \(\|tB\|\le\delta<1\), so \(C_{\psi_t}\) is Hilbert--Schmidt. Let \(e_\alpha(z)=z^\alpha/\sqrt{\alpha!}\) denote the orthonormal monomials. Summing their squared images and using Gaussian integration yields
\[
\|C_{\psi_t}\|_{\mathcal S_2}^2=\pi^{-d}\int_{\mathbb C^d}\exp\bigl(|u+tB(z-u)|^2-|z|^2\bigr)\,dV(z).
\]
For \(\|tB\|\le\delta\), the integrand is dominated by a constant times \(\exp(-(1-\delta^2)|z|^2+2\delta(1+\delta)|u|\,|z|)\). Hence the Hilbert--Schmidt norms on the disk are bounded by a constant \(M_{d,u}\) independent of \(B\) and \(t\). Each monomial matrix coefficient is entire in \(t\); local Hilbert--Schmidt boundedness upgrades this to a Hilbert--Schmidt-valued holomorphic map. Its Taylor coefficient of degree \(m\) is
\[
(T_m(B)f)(z)=\frac1{m!}D^m f(u)[B(z-u),\ldots,B(z-u)].
\]
It has rank at most \(N_m=\binom{d+m-1}{m}\), because its output is homogeneous of degree \(m\) in \(z-u\). Hilbert--Schmidt Cauchy estimates give \(\|T_m(B)\|_{\mathcal S_2}\le M_{d,u}(b/\delta)^m\). Since \(\operatorname{rank}T_m(B)\le N_m\),
\[
\|T_m(B)\|_{\mathcal S_1}\le\sqrt{N_m}\,M_{d,u}(b/\delta)^m.
\]
For \(0\le b\le\delta/2\), the series of trace norms over \(m\ge2\) is bounded by \(K_{d,u}b^2\) for a finite constant \(K_{d,u}\); the polynomial growth of \(N_m\) makes the series converge. Here \(T_0(B)=P_u\) and \(T_1(B)=L_{B,u}\). This proves the trace-class Taylor expansion, including \(B=0\) by continuity.

**2. Singular values of the differential.** Let \(V:\mathbb C^d\to\mathcal F_d\), \((Vc)(z)=\sum_jc_j(z_j-u_j)\), and \(W:\mathcal F_d\to\mathbb C^d\), \((Wf)_i=\partial_i f(u)\). With the Fock inner product linear in the first variable, the kernel vectors for these derivative functionals are \(z_i e^{z\cdot\bar u}\). Direct integration or coefficient summation gives the exact Gram identities
\[
V^*V=G_u,\qquad WW^*=e^{|u|^2}G_u.
\]
The differential factors as \(L_{B,u}=VB^{\mathsf T}W\). Since \(G_u>0\), the polar factorizations of \(V\) and \(W\) identify all nonzero singular values of this operator with those of \(e^{|u|^2/2}G_u^{1/2}B^{\mathsf T}G_u^{1/2}\). In particular its rank is at most \(d\). The trace-norm bound for the remainder implies the individual singular-value estimates by the singular-value perturbation inequality, and the \(\mathcal S_p\)-norm bounds by the reverse triangle inequality and \(\|R\|_{\mathcal S_p}\le\|R\|_{\mathcal S_1}\) for \(p\ge1\).

**3. Affine iteration.** The affine fixed-point identity yields \(\phi^{[n]}(z)=u+A^n(z-u)\). Because \(\|A\|<1\), the local Taylor expansion applies to \(B=A^n\) for every sufficiently large \(n\), and its trace-norm bound implies \(C_\phi^n-P_u\to0\) in all the stated ideals. The matrix singular-value formula and its error term follow immediately.

**4. Dominant Jordan block and sharpness.** Under the stated spectral assumptions, ordinary finite-dimensional Jordan theory gives
\[
A^n=\binom{n}{k-1}\lambda^{n-k+1}(A-\lambda I)^{k-1}P_\lambda+o(n^{k-1}r^{n-k+1})
\]
in matrix operator norm. (Contributions from lower powers of the nilpotent part have lower polynomial order, and all other eigenvalues have strictly smaller modulus.) Divide the matrix formula in part 3 by \(n^{k-1}r^{n-k+1}\), use continuity and phase invariance of Schatten norms, and note that \(\|A^n\|^2=o(n^{k-1}r^{n-k+1})\). This yields the displayed exact limit with \((k-1)!\) in the denominator. Since \(G_u\) is invertible and \(D_\lambda\ne0\), the constant is strictly positive, proving sharpness. In the two-dimensional Jordan example, \(A^n=\lambda^nI+n\lambda^{n-1}tE_{12}\); the leading matrix \(G_u^{1/2}E_{21}G_u^{1/2}\) has rank one and unique positive singular value \(\sqrt{(1+|u_1|^2)(1+|u_2|^2)}\), giving the explicit coefficient for every \(p\).

## Verification

The standalone Python program `VERIFY.py` checks the exact finite-dimensional monomial coefficients of \(C_{u+B(\cdot-u)}-P_u\) against the first differential, confirms quadratic remainder scaling at three perturbation sizes, checks the derivative Gram identities via truncated Fock expansions, and compares direct matrix powers with the Jordan formula. Execute with `python3 VERIFY.py`; it uses only the Python standard library. This is a finite consistency check; the uniform trace-norm bound, singular-value identification, and all infinite-dimensional statements are proved analytically above.

## Relationship to prior work

Bayart, Wang, and Yao (arXiv:2610.26349, first public October 19, 2026), Theorem 2.1, prove qualitative operator-norm convergence of affine Fock composition powers in several variables and characterize the limit. Chalendar and Partington (arXiv:2106.00427), Theorem 2.2, prove the analogous qualitative one-variable convergence. The affine boundedness criterion and operator-norm formula are classical results of Carswell, MacCluer, and Schuster (2003). Stochel and Stochel (2017) develop a Fock model for **linear symbols**, covering important special cases at the origin; this result does not claim novelty for the unshifted second-quantization description. Tien and Khoi (arXiv:1708.06924) study boundedness, compactness, and essential norms of differences of weighted Fock composition operators. Carroll and Gilmore (arXiv:1911.07254), Section 4, analyze pointwise and orbit asymptotics of weighted Fock composition powers, particularly noncompact weighted operators. Those results do not state the present **trace-norm first-variation formula, full rank-\(d\) leading singular spectrum, or exact nonnormal Jordan-block Schatten-rate constants**. The present contribution isolates the **explicit displaced-point singular spectrum with a uniform quadratic trace-norm remainder** and sharp Schatten rates for nonnormal affine iterates. Its proof is self-contained given elementary Fock integration and finite-dimensional Jordan theory.

## Limitations

The literature comparison supports best-knowledge originality, not a proof of publication priority. General reproducing-kernel perturbation principles or operator-ideal formulations could implicitly cover pieces of the local Taylor argument. Earlier Fock-difference papers, especially Choe--Izuchi--Koo (2010), could not be examined completely; their published abstracts address boundedness, compactness, and Schatten membership of linear sums and therefore pose a residual priority risk for the more quantitative statements here. This work does not claim the qualitative Schatten-class membership or unshifted linear-model theory as new. The limit theorem does not classify co-dominant eigenvalue interference, does not treat infinite-dimensional symbol spaces, and does not claim a single asymptotic coefficient outside the unique-dominant-eigenvalue case. The trace-class remainder is only an upper estimate and is not claimed to have an optimal universal coefficient. No independent scientific audit has been performed.

## References

1. F. Bayart, M. Wang, X. Yao, *Semigroup of composition operators on the Fock space of several complex variables*, arXiv:2610.26349 (original submission October 19, 2026), https://arxiv.org/abs/2610.26349.
2. I. Chalendar, J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, arXiv:2106.00427 (2021), https://arxiv.org/abs/2106.00427.
3. T. Carroll, C. Gilmore, *Weighted composition operators on Fock spaces and their dynamics*, arXiv:1911.07254 (2019), https://arxiv.org/abs/1911.07254.
4. B. J. Carswell, B. D. MacCluer, A. Schuster, *Composition operators on the Fock space*, Acta Sci. Math. (Szeged) 69 (2003), 871--887, https://acta.hu/download.phtml?id=2759.
5. J. Stochel, J. B. Stochel, *Composition operators on Hilbert spaces of entire functions with analytic symbols*, J. Math. Anal. Appl. 454 (2017), 1019--1066, https://doi.org/10.1016/j.jmaa.2017.05.021.
6. P. T. Tien, L. H. Khoi, *Differences of weighted composition operators between the Fock spaces*, arXiv:1708.06924 (2017), https://arxiv.org/abs/1708.06924.
7. B. R. Choe, K. H. Izuchi, H. Koo, *Linear sums of two composition operators on the Fock space*, J. Math. Anal. Appl. 369 (2010), 112--119, https://doi.org/10.1016/j.jmaa.2010.02.029.
