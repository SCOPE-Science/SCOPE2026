# Phase-independent Hankel recovery of radial Fock annulus geometry

## Finding
Consider a binary mask periodic in the squared radial coordinate of the analytic Bargmann–Fock plane. The following explicit inverse theorem recovers its *period, observed duty fraction, and angular origin in the radial variable* from the indexed monomial eigenvalue tail. Its key invariant is a two-by-two Hankel minor which eventually has a strictly negative sign even when individual leading spectral deviations repeatedly vanish.

Fix \(L>0\), \(0<\rho<1\), and \(a\in[0,L)\). For \(u\geq0\), set
\[
g_{L,\rho,a}(u)=\mathbf1_{[a,a+\rho L)\bmod L}(u).
\]
Let \(T_{L,\rho,a}\) be the Toeplitz operator with symbol \(g_{L,\rho,a}(\pi|z|^2)\) on the normalized analytic Fock space. Write \(\lambda_n\) for its eigenvalue at the monomial of degree \(n\), where \(n=0,1,2,\ldots\). Define \(\delta_n=\lambda_n-\rho\) and
\[
H_n=\delta_n\delta_{n+2}-\delta_{n+1}^{2}.
\]
Let
\[
r=\bigl(1+(2\pi/L)^2\bigr)^{-1/2},\quad
r_2=\bigl(1+(4\pi/L)^2\bigr)^{-1/2},\quad
\theta=\arctan(2\pi/L),\quad
b={\sin(\pi\rho)\over\pi}\exp\!\left[-i\left(\pi\rho+{2\pi a\over L}\right)\right].
\]
Then \(0<r_2<r<1\), \(0<\theta<\pi/2\), and \(b\ne0\). In the limit of high monomial degree,
\[
\lambda_n=\rho+2\operatorname{Re}\bigl(b(re^{i\theta})^{n+1}\bigr)+O_{L,\rho,a}(r_2^{n+1}),
\]
\[
\boxed{\displaystyle H_n=-4|b|^2\sin^2\theta\;r^{2n+4}
\left[1+O_{L,\rho,a}\bigl((r_2/r)^n\bigr)\right].}
\]
Hence \(H_n<0\) for all sufficiently large \(n\), and the index-sensitive spectrum recovers all three geometric parameters using limits:
\[
\boxed{\displaystyle
\rho=\lim_{n\to\infty}\lambda_n,\quad
R=\lim_{n\to\infty}{H_{n+1}\over H_n}=r^2,\quad
L={2\pi\over\sqrt{R^{-1}-1}}.}
\]
The finite-index ratios converge geometrically: \(H_{n+1}/H_n=R+O_{L,\rho,a}((r_2/r)^n)\). To recover placement, form
\[
X_n={\lambda_n-\rho\over r^{n+1}},\quad
\boxed{\displaystyle
b=\lim_{n\to\infty}{e^{-i(n+1)\theta}\over2}
\left[X_n+i{X_n\cos\theta-X_{n+1}\over\sin\theta}\right].}
\]
This limit has error \(O_{L,\rho,a}((r_2/r)^n)\). Finally,
\[
\boxed{\displaystyle e^{-2\pi i a/L}={\pi b\,e^{i\pi\rho}\over\sin(\pi\rho)}.}
\]
Consequently the three parameters are determined uniquely, with \(a\) understood modulo \(L\). The reconstruction works for all periods and all strictly interior duty fractions; it requires neither arithmetic nonresonance nor knowledge of the leading oscillatory phase.

## Assumptions and scope
The Fock inner product uses planar area measure and the weight \(e^{-\pi|z|^2}\), so the normalized monomials are \(e_n(z)=\pi^{n/2}z^n/\sqrt{n!}\). The parameter \(a\) denotes the left-hand endpoint of the occupied arc on the circle of circumference \(L\); wrapped arcs are allowed. Endpoints have measure zero. The input is the complete *indexed* sequence \((\lambda_n)_{n\geq0}\) in this fixed normalization; the unordered spectral set is a different inverse problem. Exclude \(\rho=0\) and \(\rho=1\): then the Fourier amplitude vanishes and the period is unidentifiable.

## Proof
**1. Exact radial diagonalization.** Integrate angularly to see that different monomials are orthogonal after multiplication by the radial mask. With \(u=\pi|z|^2\), direct radial integration gives, for every integer \(n\geq0\),
\[
\lambda_n={1\over n!}\int_0^\infty g_{L,\rho,a}(u)e^{-u}u^n\,du.
\]
This identity includes all normalization factors. It is also an expectation of the periodic mask under a shape-\(n+1\), unit-rate gamma density.

**2. Fourier–gamma representation and the first spectral pole.** The Fourier coefficients of the periodic mask in the convention \(g(u)=\sum_{m\in\mathbb Z}c_me^{2\pi imu/L}\) are
\[
c_0=\rho,\qquad
c_m={\sin(\pi m\rho)\over\pi m}\,
\exp\!\left[-i\left(\pi m\rho+{2\pi ma\over L}\right)\right]\quad(m\ne0).
\]
The formula holds for wrapped intervals by periodicity. The Laplace transform of the gamma density is
\[
{1\over n!}\int_0^\infty e^{-u}u^ne^{2\pi imu/L}\,du
=(1-2\pi i m/L)^{-n-1}=:q_m^{n+1}.
\]
One may first use Fejér means of \(g\) and then pass to the limit using bounded convergence. The resulting series is absolutely summable because \(|c_m|\leq1/(\pi|m|)\) and \(|q_m|=O_L(1/|m|)\) for large \(|m|\). Thus
\[
\lambda_n-\rho=\sum_{m\ne0}c_mq_m^{n+1}.
\]
The \(m=\pm1\) terms are exactly \(bq^{n+1}+\overline b\overline q^{n+1}\) with \(q=q_1=re^{i\theta}\). For \(|m|\geq2\), the moduli are at most \(r_2\), and
\[
\sum_{|m|\geq2}|c_m||q_m|^{n+1}
\leq r_2^n\sum_{|m|\geq2}|c_m||q_m|
=O_L(r_2^{n+1}).
\]
The finite constant may also be taken independent of \(\rho,a\) at fixed \(L\). This establishes the first claimed expansion for every \(n\geq0\).

**3. The phase-free determinant.** Put \(S_n=bq^{n+1}+\overline b\overline q^{n+1}\). Direct expansion, with all pure powers cancelling, yields the *exact* identity
\[
S_nS_{n+2}-S_{n+1}^2
=|b|^2|q|^{2n+2}(q-\overline q)^2
=-4|b|^2\sin^2\theta\,r^{2n+4}.
\]
Writing \(\delta_n=S_n+E_n\), the bound \(|E_n|\leq C r_2^{n+1}\) shows that the cross terms in \(H_n\) are \(O(r^{n+1}r_2^{n+1})\); quadratic remainder terms decay even faster. After dividing by the strictly nonzero principal term, their relative contribution is \(O((r_2/r)^n)\). This proves the stated uniform-in-index asymptotic, eventual strict negativity, and geometric ratio convergence. Crucially, the determinant does not depend on the phase of \(bq^{n+1}\).

**4. Inversion.** Since \(r<1\), the gamma eigenvalues converge to \(\rho\). Taking the determinant ratio gives \(r^2\), and the map \(L\mapsto[1+(2\pi/L)^2]^{-1}\) is strictly increasing from \((0,\infty)\) onto \((0,1)\), giving the unique reconstruction of \(L\). With \(\theta\) then known, division by \(r^{n+1}\) gives
\[
X_n=b e^{i(n+1)\theta}+\overline b e^{-i(n+1)\theta}
+O((r_2/r)^n).
\]
If \(z=b e^{i(n+1)\theta}\), the leading part of \(X_n\) equals \(2\operatorname{Re}z\), while the leading part of \(X_{n+1}\) equals \(2\operatorname{Re}(ze^{i\theta})\). Solving these two real equations yields the displayed limit for \(b\); the denominator \(\sin\theta\) is positive. Since \(\sin(\pi\rho)>0\), the phase of \(b\) determines \(a\bmod L\) by the final identity. No inverse operation introduces an additional alternative solution. This completes the proof.

## Verification
A reproducible supplementary checker, `checker.py`, carries out the two-frequency Hankel factorization symbolically; compares Fourier–gamma eigenvalues with separately integrated annular gamma tails for three parameter triples (including a wrapping arc); tests the determinant's sign and geometric ratio; reconstructs the period and first Fourier coefficient numerically; and checks an independent auxiliary trace identity. It reports `PASS 58 supplementary assertions` under Python 3 with `mpmath` and `sympy`. These finite checks supplement rather than replace the all-parameter analytical argument.

For completeness, the auxiliary trace identity (not the claimed inverse novelty) is
\[
T_{L,\rho,a}-\rho I\in S_1,\quad
\sum_{n\geq0}(\lambda_n-\rho)
=\int_0^L\left({1\over2}-{u\over L}\right)g_{L,\rho,a}(u)\,du.
\]
It follows by absolutely interchanging the Fourier–gamma series and the geometric sum in \(n\), then integrating the periodic sawtooth kernel; it is included as an additional normalization check. In particular, when \(a=0\), the right-hand side is \(L\rho(1-\rho)/2\).

## Relationship to prior work
Knutsen's 2019 time-frequency localization study supplies the radial Hermite/gamma eigenvalue framework and examines infinite periodic collections of annuli. Dewage–Ólafsson (2021) and Esmeral–Maximenko (2015) provide radial/quasi-radial Toeplitz spectral representation and operator-algebra context. Esmeral García–Maximenko (2025), Proposition 3.4, **already proves the broader abstract uniqueness fact that a bounded radial symbol is determined almost everywhere by all sufficiently high gamma moments**; basic injectivity is therefore *not* claimed here. The separate contribution here is the explicit three-parameter inversion using a sign-definite adjacent spectral determinant, a sharp leading determinant coefficient, and geometric convergence for every nontrivial duty fraction and phase. General radial uniqueness, Fourier diagonalization, and known special period-two trace formulas are prior ingredients, not new theorems.

## Limitations
This is a noiseless asymptotic inverse theorem for the *indexed* monomial spectrum. It does not guarantee well-conditioned recovery from finitely many noisy eigenvalues: for \(\rho\) close to 0 or 1, the leading Hankel determinant is very small, and for large \(L\) the relative convergence rate approaches 1. The thresholds for eventual negativity and constants in error terms depend on parameters. No assertion is made about arbitrary non-periodic masks, multiple arcs within a period, unknown radial scaling conventions, unordered spectra, or the uniqueness of the method among algorithms. Historical priority for the explicit deterministic reconstruction remains subject to independent literature review.

## References
1. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, arXiv:1907.00848 (first posted 2019-07-01); especially the gamma-eigenvalue formulas and infinite-measure periodic annuli discussion. https://arxiv.org/abs/1907.00848
2. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first posted 2021-07-03), radial eigenvalues and Toeplitz algebra. https://arxiv.org/abs/2107.01465
3. K. Esmeral and E. A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906 (2015). https://arxiv.org/abs/1505.07906
4. K. Esmeral García and E. A. Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz–Fock operators*, arXiv:2503.23276 (first posted 2025-03-30), especially Proposition 3.4 and Section 4. https://arxiv.org/abs/2503.23276
