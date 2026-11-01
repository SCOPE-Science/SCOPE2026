# A frequency-linear boundary correction for balanced Sobolev orthogonal polynomials on the circle

## Finding
Fix an integer \(m\geq1\), a complex number \(a\) with \(0\leq |a|<1/2\), and \(\lambda>0\). For each integer \(n\geq1\), let \(P_n\) be the unique monic polynomial of degree \(n\) minimizing
\[
\mathcal E_n(p)=\int_0^{2\pi}|p(e^{i\theta})|^2\,\frac{d\theta}{2\pi}
+\frac{\lambda}{n^2}\int_0^{2\pi}|p'(e^{i\theta})|^2
\bigl(1+a e^{im\theta}+\overline a e^{-im\theta}\bigr)\,\frac{d\theta}{2\pi}.
\]
Write \(\sigma_n^2=\mathcal E_n(P_n)\), \(d=1+\lambda\), and \(\Delta=\sqrt{d^2-4|a|^2\lambda^2}\). Then
\[
\boxed{\sigma_n^2=\frac{d+\Delta}{2}+\frac{2m|a|^2\lambda^2}{\Delta^2}\frac1n+O_{m,a,\lambda}(n^{-2}).}
\]
The leading term is independent of the harmonic index \(m\) and phase of \(a\), whereas the **first nonzero finite-degree correction grows exactly linearly with \(m\)**. For \(a\ne0\) this correction is strictly positive. For \(a=0\) the equality \(\sigma_n^2=1+\lambda\) is exact for every \(n\).

## Assumptions and scope
The integrals use normalized Haar measure on the unit circle; \(p'\) is the complex derivative, not differentiation in \(\theta\). The weight \(1+2\operatorname{Re}(a e^{im\theta})\) is strictly positive because \(|a|<1/2\). The parameters \(m,a,\lambda\) are fixed as \(n\to\infty\). This is a norm-squared asymptotic, not an assertion about individual zeros or uniformity when \(m\) increases with \(n\). The natural primary classification is MSC2020 42C05 (orthogonal functions and polynomials).

## Proof
**1. Exact Gram reduction.** For \(0\leq j,k\leq n\), the Gram matrix in the monomial basis is Hermitian and has diagonal entries \(1+\lambda j^2/n^2\); its only nonzero off-diagonals connect indices differing by \(m\), with modulus \(|a|\lambda jk/n^2\). Consequently, residue classes modulo \(m\) are orthogonal. The unique monic minimizer has no component in the residue classes other than that containing \(n\).

Let \(r\in\{0,\ldots,m-1\}\) be the residue of \(n\) modulo \(m\), and let \(h_j\) denote the minimal squared norm of a monic degree-\(j\) polynomial restricted to the chain of exponents \(r,r+m,\ldots,j\), using the same \(n\)-dependent inner product. Schur complementation of the tridiagonal Gram block gives the exact, positive recurrence
\[
h_r=1+\lambda r^2/n^2,\qquad
h_j=1+\lambda j^2/n^2-
\frac{|a|^2\lambda^2j^2(j-m)^2}{n^4h_{j-m}}\quad(j=r+m,r+2m,\ldots,n),
\]
with \(\sigma_n^2=h_n\). This recurrence is also an independent rational-arithmetic certificate for every finite degree when the parameters are rational.

**2. Uniform positivity and contraction.** Put \(x=j/n\) and \(D(x)=1+\lambda x^2\). By induction, \(h_j\geq D(j/n)/2\): the statement is clear at \(j=r\), and if it holds at \(j-m\), then the quantity subtracted at the next step is at most
\[
2|a|^2\lambda^2\frac{(j/n)^2((j-m)/n)^2}{1+\lambda((j-m)/n)^2}
\leq 2|a|^2\lambda(j/n)^2\leq\tfrac12\lambda(j/n)^2.
\]
Define \(T(x)=|a|\lambda x^2\),
\[
\Delta(x)=\sqrt{D(x)^2-4T(x)^2},\qquad
H(x)=\frac{D(x)+\Delta(x)}2.
\]
These are smooth on \([0,1]\), \(\Delta(x)>0\), and \(H(x)\geq D(x)/2\). In the comparison of the exact recurrence at step \(j\) with a positive approximate value at step \(j-m\), the Lipschitz coefficient is at most
\[
4|a|^2\left(\frac{\lambda (j/n)((j-m)/n)}{1+\lambda((j-m)/n)^2}\right)^2
\leq 4|a|^2\left(1+\frac{\sqrt\lambda m}{2n}\right)^2.
\]
Since \(4|a|^2<1\), this is bounded by some \(\rho<1\) for all sufficiently large \(n\), uniformly in every step.

**3. Adiabatic expansion.** The stable fixed-point identity is
\[
H(x)=D(x)-T(x)^2/H(x),\qquad
1-T(x)^2/H(x)^2=\Delta(x)/H(x).
\]
Set
\[
E_m(x)=\frac{2m|a|^2\lambda^2x^3}{\Delta(x)^2},\qquad
F_{j,n}=H(j/n)+E_m(j/n)/n.
\]
Taylor expansion on the compact interval \([0,1]\), including its endpoints, shows uniformly in the chain that
\[
D(j/n)-\frac{|a|^2\lambda^2j^2(j-m)^2}{n^4F_{j-m,n}}
=F_{j,n}+O_{m,a,\lambda}(n^{-2}).
\]
For completeness, if \(x=j/n\), the first-order term on the left is
\[
\frac{2m|a|^2\lambda^2x^3}{H(x)}+
\frac{T(x)^2}{H(x)^2}\bigl(E_m(x)-mH'(x)\bigr).
\]
Its equality to \(E_m(x)\) follows on differentiating the fixed-point identity; equivalently, using \(D(x)=1+\lambda x^2\), one checks
\[
H(x)-\frac{x}{2}H'(x)=\frac12\left(1+\frac{D(x)}{\Delta(x)}\right).
\]
The initial discrepancy satisfies \(F_{r,n}-h_r=O(n^{-4})\), because \(r<m\) is fixed, \(H(x)-D(x)=O(x^4)\), and \(E_m(x)=O(x^3)\) near zero.

**4. Error propagation.** Both the true pivots and the approximate pivots are bounded below by \(D(j/n)/2\), since \(E_m\geq0\). Subtracting their recurrences and applying the contraction from step 2 gives
\[
|h_j-F_{j,n}|\leq\rho|h_{j-m}-F_{j-m,n}|+C n^{-2}.
\]
Iteration yields \(|h_n-F_{n,n}|\leq C(1-\rho)^{-1}n^{-2}+O(n^{-4})\). Substituting \(x=1\) proves the boxed formula. The phase of \(a\) disappears at the Schur-complement step, so the proof covers complex \(a\) without a rotation argument.

## Verification
The standalone `check.py` compares the recurrence with a separately implemented exact rational Gram-matrix minimization in 120 small cases (including negative real Fourier coefficients). It also checks the predicted \(n^{-1}\) term for 12 fixed parameter triples using three increasing degrees. The checker prints `EXACT_GRAM_VS_SCHUR 120 ASYMPTOTIC_FINITE_TESTS 12 PASS`. These finite computations test the normalization and recurrence only; the \(O(n^{-2})\) statement follows from the contraction proof above.

## Relationship to prior work
Majumder and Swaminathan, *Sobolev Orthogonal Polynomials on the unit circle with varying inner product*, arXiv:2610.31994 (first posted 2026-10-22), study general pairs of circle measures with the same critical degree-dependent scaling. Their Proposition 1 provides bounds for critical squared norms and Theorem 3.2 provides strong outer polynomial asymptotics, but the inspected paper does not state a coefficient-resolved \(n^{-1}\) expansion or its exact linear dependence on the Fourier harmonic number. The present theorem does not claim either the general strong asymptotic framework or the classical Schur-complement method as new. Earlier articles on fixed Sobolev inner products and coherent measure pairs concern related but distinct parameters; see References.

## Limitations
The perturbing measure has one Fourier harmonic; extension to arbitrary positive densities may require a nontrivial matrix or multiband recurrence. The harmonic index and parameters are fixed; the estimate is not uniform in \(m\), or at the degenerate boundary \(|a|=1/2\). The claim is self-reviewed only and has not undergone an independent mathematical audit. Literature indexing and incomplete access to some older papers leave a residual possibility of equivalent prior coverage.

## References
1. S. Majumder and A. Swaminathan, *Sobolev Orthogonal Polynomials on the unit circle with varying inner product*, arXiv:2610.31994 (2026), Sections 1–3, Proposition 1 and Theorems 3.1–3.3.
2. K. Castillo, L. E. Garza and F. Marcellán, *Asymptotic behaviour of Sobolev orthogonal polynomials on the unit circle*, Integral Transforms and Special Functions 24 (2013), 23–38, doi:10.1080/10652469.2011.649751.
3. F. Marcellán and Y. Xu, *On Sobolev orthogonal polynomials*, Expositiones Mathematicae 33 (2015), 308–352, arXiv:1403.6249.
4. *Sobolev orthogonal polynomials on the unit circle and coherent pairs of measures of the second kind* (2017), Universidad Carlos III research portal: https://researchportal.uc3m.es/display/act474202.
