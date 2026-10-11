# Uniform dimension-bandwidth crossover for zonal hemispherical spectral determinants

## Finding
Fix a real parameter \(\beta>-1\). In the real Hilbert space
\[
\mathcal H_\beta=L^2([-1,1],(1-x^2)^\beta\,dx),
\]
let \(\mathcal V_m\) be the polynomials of degree at most \(2m-1\), where \(m\ge1\), and let \(P_m\) be orthogonal projection onto this \(2m\)-dimensional subspace. Define the half-interval concentration operator on \(\mathcal V_m\) by
\[
C_{m,\beta}=P_mM_{\mathbf1_{(0,1)}}P_m\big|_{\mathcal V_m},\qquad
Q_m(\beta)=\prod_{\lambda\in\operatorname{spec}(C_{m,\beta})}|2\lambda-1|,
\]
where eigenvalues are counted with algebraic multiplicity (equivalently, geometric multiplicity because the operator is self-adjoint). Let \(G\) denote the Barnes function normalized by \(G(1)=1\) and \(G(z+1)=\Gamma(z)G(z)\), and put \(K=\sqrt\pi\,G(1/2)^2\).

**Theorem.** For every \(\beta>-1\) and integer \(m\ge1\), the concentration spectrum has no eigenvalue \(1/2\), and its eigenvalues occur in complementary pairs. The exact spectral-gap product is
\[
\boxed{Q_m(\beta)=
\prod_{j=0}^{m-1}\frac{\Gamma(j+1)^2}{\Gamma(j+1/2)\Gamma(j+3/2)}
\prod_{j=0}^{m-1}\frac{\Gamma(m+j+\beta+1/2)\Gamma(m+j+\beta+3/2)}
{\Gamma(m+j+\beta+1)^2}.}
\]
For every fixed \(m\), this product is strictly decreasing in \(\beta\), and its limit as \(\beta\to\infty\) is the first displayed gamma product alone. As \(m\to\infty\), **uniformly over the entire range \(\beta>-1\)**,
\[
\boxed{Q_m(\beta)=K\,m^{-1/4}
\left(\frac{2m+\beta+1}{m+\beta+1}\right)^{1/4}
\left(1+O(m^{-1})\right).}
\]
The implied constant in \(O(m^{-1})\) does not depend on \(\beta\). In particular, for any sequence \(\beta_m>-1\) such that \(\beta_m/m\to\rho\in[0,\infty]\),
\[
\lim_{m\to\infty}m^{1/4}Q_m(\beta_m)
=K\left(\frac{\rho+2}{\rho+1}\right)^{1/4},
\]
where the last factor is defined as one for \(\rho=\infty\). The two iterated limits therefore differ by precisely \(2^{1/4}\): taking bandwidth large before the parameter tends to infinity gives \(2^{1/4}K\), while taking the parameter to infinity first gives \(K\). Numerically, \(K\approx0.645002448509577\) and \(2^{1/4}K\approx0.767041500961765\).

## Assumptions and scope
The weighted measure is finite and positive for every \(\beta>-1\). The multiplication operator uses the indicator of the positive half-interval; a single endpoint of measure zero is immaterial. The polynomial degree bound is exactly \(2m-1\), so the subspace has equal dimensions of even and odd polynomials. For the zonal subspace of scalar spherical harmonics on the standard sphere \(S^d\), one has \(\beta=(d-2)/2\) and \(x\) is the cosine of colatitude; the theorem concerns that zonal subspace, **not** the full spherical-harmonic space. The theorem also applies to every real \(\beta>-1\), not just spherical dimensions. All integrals use the same unnormalized weight; overall scaling of the weight does not change the concentration spectrum.

## Proof
**1. Parity, Gram matrices, and the spectral determinant.** On \(\mathcal V_m\), the centered concentration operator is \(T=2C_{m,\beta}-I=P_mM_{\operatorname{sgn}(x)}P_m\). Reflection \(Uf(x)=f(-x)\) preserves \(\mathcal V_m\), is unitary for the even weight, and satisfies \(UTU=-T\). Therefore nonzero eigenvalues of \(T\) occur in \(\pm\) pairs; corresponding eigenvalues of \(C_{m,\beta}\) add to one.

Use the nonorthonormal polynomial basis with even monomials \(1,x^2,\ldots,x^{2m-2}\), followed by odd monomials \(x,x^3,\ldots,x^{2m-1}\). Write \(H_m(\alpha,\beta)\) for the determinant of the \(m\)-by-\(m\) beta-moment matrix
\[
H_m(\alpha,\beta)=\det_{0\le i,j<m}\left[\int_0^1t^{i+j+\alpha}(1-t)^\beta\,dt\right]
=\det_{0\le i,j<m}B(i+j+\alpha+1,\beta+1),\qquad \alpha>-1.
\]
The positive Gram matrix of the Hilbert-space inner product is block diagonal, with determinants \(H_m(-1/2,\beta)\) and \(H_m(1/2,\beta)\). The bilinear form for \(T\) is block off-diagonal: its two cross-blocks are both the beta-moment matrix with determinant \(H_m(0,\beta)\). Indeed, the change of variable \(t=x^2\) gives, for example,
\[
2\int_0^1x^{2i+2j+1}(1-x^2)^\beta dx
=\int_0^1t^{i+j}(1-t)^\beta dt.
\]
All three Hankel matrices are strictly positive definite: they are Gram matrices of distinct monomials for positive measures on \((0,1)\). Thus the centered operator is invertible and \(1/2\) is absent from the concentration spectrum. In a nonorthonormal basis the matrix of \(T\) is the Gram-inverse times its bilinear-form matrix; taking determinants yields the exact identity
\[
\boxed{Q_m(\beta)=\left|\det T\right|
=\frac{H_m(0,\beta)^2}{H_m(-1/2,\beta)H_m(1/2,\beta)}.}
\]
There is no additional factor of two: it was absorbed in \(2C-I=M_{\operatorname{sgn}(x)}\).

**2. Exact Jacobi moment determinants.** For \(\alpha,\beta>-1\), the monic polynomials orthogonal for the weight \(t^\alpha(1-t)^\beta\) are normalized shifted Jacobi polynomials. Their squared norms, obtained from the standard Rodrigues formula followed by integration by parts and division by the leading coefficient, satisfy the following formula for \(j\ge1\):
\[
h_j(\alpha,\beta)=\frac{j!\,\Gamma(j+\alpha+1)\Gamma(j+\beta+1)\Gamma(j+\alpha+\beta+1)}{(2j+\alpha+\beta+1)\Gamma(2j+\alpha+\beta+1)^2}.
\]
For degree zero one has \(h_0(\alpha,\beta)=B(\alpha+1,\beta+1)\); this avoids a removable singularity in the displayed higher-degree gamma expression when \(\alpha+\beta+1=0\). The determinant of a moment Gram matrix is the product of squared norms of its monic orthogonalization. Multiplication and gamma-function cancellation yield the equivalent Jacobi/Selberg evaluation
\[
H_m(\alpha,\beta)=\frac1{m!}\prod_{j=0}^{m-1}
\frac{\Gamma(j+\alpha+1)\Gamma(j+\beta+1)\Gamma(j+2)}{\Gamma(m+j+\alpha+\beta+1)}.
\]
Substitution into the determinant ratio in Step 1 cancels every factor common to the three determinants and gives precisely the two gamma products in the theorem. This proves the finite formula for every \(\beta>-1\), not merely the integer cases.

**3. Strict parameter monotonicity and Gaussian endpoint.** Write the first gamma product as \(F_m\) and the second as \(R_m(\beta)\). Put
\[
u(t)=\log\Gamma(t-1/2)+\log\Gamma(t+1/2)-2\log\Gamma(t),\qquad t>1/2.
\]
Then \(\log R_m(\beta)=\sum_{j=0}^{m-1}u(m+j+\beta+1)\). The digamma function \(\psi=(\log\Gamma)'\) is strictly concave on the positive axis, because \(\psi''(t)=-2\sum_{k=0}^\infty(t+k)^{-3}<0\). Consequently
\[
\frac{d}{d\beta}\log R_m(\beta)
=\sum_{j=0}^{m-1}\left[\psi(t_j-1/2)+\psi(t_j+1/2)-2\psi(t_j)\right]<0,
\]
where \(t_j=m+j+\beta+1\). Also \(u(t)\to0\) as \(t\to\infty\); for fixed \(m\), therefore, \(R_m(\beta)\to1\) as \(\beta\to\infty\).

**4. Uniform two-parameter limit.** From the Barnes recursion,
\[
F_m=\sqrt\pi\,G(1/2)^2\frac{G(m+1)^2}{G(m+1/2)G(m+3/2)}.
\]
The standard large-argument expansion of \(\log G\) (or its second finite difference) gives
\[
F_m=K m^{-1/4}\left(1+O(m^{-1})\right).
\]
A symmetric Taylor expansion of \(\log\Gamma\) and the trigamma asymptotic \(\psi'(t)=t^{-1}+O(t^{-2})\) yield
\[
u(t)=\frac1{4t}+O(t^{-2})\quad(t\ge1).
\]
For all \(\beta>-1\), the arguments \(t_j=m+j+\beta+1\) are at least \(m\). Uniformly in \(\beta\),
\[
\sum_{j=0}^{m-1}u(t_j)
=\frac14\sum_{j=0}^{m-1}\frac1{m+j+\beta+1}+O(m^{-1})
=\frac14\log\frac{2m+\beta+1}{m+\beta+1}+O(m^{-1}).
\]
The final equality is the integral comparison for the decreasing reciprocal function; its endpoint error is bounded by a constant times \(m^{-1}\) uniformly in \(\beta>-1\). Exponentiating and multiplying by the Barnes factor proves the stated uniform asymptotic formula. The crossover profile and the two noncommuting iterated limits follow directly, with no assumption that \(\beta\) is fixed while \(m\) grows.

## Verification
The accompanying standalone `verify.py` derives finite beta moments by binomial expansion for integer \(\beta\), computes exact rational Hankel determinants, independently computes the Selberg gamma-product expressions using rational rising factorials, and compares the resulting spectral products to the theorem. It additionally checks nonintegral parameters numerically and, when a multiprecision library is installed, independently evaluates the Barnes constant and selected finite products. The analytic proof above supplies the all-parameter and uniform-in-parameter statements; a finite computation by itself would not establish either.

For the Legendre case \(\beta=0\), the first spectral product is \(Q_1(0)=3/4\); for \(\beta=1/2\), corresponding to zonal harmonics on \(S^3\), it is \(Q_1(1/2)=64/(9\pi^2)\). These independent normalization checks agree with the formula. The long-bandwidth fixed-dimensional constant is \(2^{1/4}K\), whereas the fixed-bandwidth Gaussian-weight limit is the smaller \(K\).

## Relationship to prior work
Simons, Dahlen, and Wieczorek (2004) formulate sphere-based Slepian concentration, including azimuthal-order blocks and polar caps; their spectral operator supplies the natural context for the \(\beta=0\) zonal case. Bates, Khalid, and Kennedy (2016) develop analytical concentration matrices for other spherical regions. Standard shifted Jacobi norm/Selberg determinants provide the exact moment evaluations used in Step 2. Deift, Its, and Krasovsky (2011) study asymptotic Hankel determinants with Fisher–Hartwig singularities; their Theorem 1.20 assumes interior jump parameters and their Remark 1.22 describes extra corrections at boundary jumps. Those general results are relevant to alternative derivations of fixed-symbol asymptotics, but do not state this finite hemisphere spectral determinant, strict parameter ordering, or a **uniform growing-parameter-to-bandwidth crossover**. In particular, the large-parameter uniformity in the theorem is established directly from the finite gamma product rather than inferred from a fixed-symbol asymptotic theorem.

## Limitations
Only the complete product of centered concentration eigenvalues is evaluated; the individual eigenvalues and eigenvectors are not classified. The claim is for the zonal (one-variable) projection, not the determinant of the complete spherical-harmonic concentration matrix in higher dimensions. The uniform asymptotic error is a proved order bound rather than a numerically optimized explicit remainder constant. The Jacobi/Selberg determinant identities and Barnes asymptotics are classical inputs, not themselves claimed as novel. Equivalent spectral-determinant formulas may exist under different Jacobi, Toeplitz–Hankel, or signed-moment terminology; the comparison of searched and inspected sources does not establish exhaustive novelty or independent validation.

## References
1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, first public preprint 31 August 2004, arXiv:math/0408424v1, especially Sections 4–5. Primary MSC 42B05.
2. A. P. Bates, Z. Khalid, and R. A. Kennedy, *Slepian spatial-spectral concentration problem on the sphere: Analytical formulation for limited colatitude-longitude spatial region*, arXiv:1608.03031v1 (2016), especially Sections II–IV.
3. P. Deift, A. Its, and I. Krasovsky, *Asymptotics of Toeplitz, Hankel, and Toeplitz+Hankel determinants with Fisher–Hartwig singularities*, arXiv:0905.0443v3 (2011), Theorem 1.20 and Remarks 1.21–1.22.
4. NIST Digital Library of Mathematical Functions, Chapter 18, §18.2, orthogonal-polynomial moments and Hankel determinants; Jacobi polynomial norms as in classical Rodrigues orthogonality formulas.
