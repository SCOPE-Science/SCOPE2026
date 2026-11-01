# Laguerre spectral branches of radial Bergman Toeplitz covariance defects

## Finding

For every integer \(d\ge1\), real \(\alpha>-1\), and integer \(m\ge1\), set \(u(z)=1-\|z\|^2\) on the complex unit ball \(\mathbb B_d\). Write \(T_f=P M_f|_{A^2_\alpha}\) for weighted analytic Bergman Toeplitz compression. The \(m\)-channel multiplicativity defect

\[
\mathcal V_m=\big[T_{u^{i+j}}-T_{u^i}T_{u^j}\big]_{i,j=1}^m
\]

is a positive, injective compact operator on \(A^2_\alpha(\mathbb B_d)\otimes\mathbb C^m\). In the homogeneous-degree-\(n\) sector it acts as an \(m\times m\) covariance matrix \(G_n\), each eigenvalue of which has multiplicity \(h_{n,d}=\binom{n+d-1}{d-1}\). Put \(a=n+d\), \(b=\alpha+1\), and \(A=a+b\). With \((x)_j=x(x+1)\cdots(x+j-1)\) and \((x)_0=1\), the exact matrix entries and leading principal determinants are

\[
(G_n)_{ij}=\frac{(b)_{i+j}}{(A)_{i+j}}-\frac{(b)_i(b)_j}{(A)_i(A)_j},
\qquad
\det G_n[1\!:\!k,1\!:\!k]
=\prod_{j=1}^{k}\frac{j!\,(a)_j(b)_j}{(A)_{2j}(A+j-1)_j},
\quad1\le k\le m.
\]

Let \(\lambda_1(n)\ge\cdots\ge\lambda_m(n)>0\) be the ordered eigenvalues. Each branch has a *different* exact leading law:

\[
\boxed{\lim_{n\to\infty}n^{2k}\lambda_k(n)=c_k:=k!\,(\alpha+1)_k,\quad 1\le k\le m.}
\]

Define \(\mathcal V_m^{(k)}\) to be the blockwise spectral operator whose restriction to every degree-\(n\) multiplicity copy has eigenvalue \(\lambda_k(n)\) once and zero in the other \(m-1\) directions. This positive compact operator has, for its nonzero singular values in decreasing order,

\[
\boxed{s_J(\mathcal V_m^{(k)})\sim\frac{c_k}{(d!\,J)^{2k/d}}\qquad(J\to\infty).}
\]

For every \(p>0\), the sharp Schatten/quasi-Schatten criterion and critical logarithmic mass are

\[
\boxed{\mathcal V_m^{(k)}\in\mathcal S_p\ \Longleftrightarrow\ p>\frac d{2k}},
\qquad
\boxed{\lim_{J\to\infty}\frac{1}{\log J}\sum_{j=1}^J s_j(\mathcal V_m^{(k)})^{d/(2k)}=\frac{c_k^{d/(2k)}}{d!}.}
\]

In particular the entire defect is in \(\mathcal S_p\) exactly for \(p>d/2\), but its successive canonical spectral channels have the strictly lower thresholds \(d/4,d/6,\ldots,d/(2m)\).

## Assumptions and scope

The normalized measure is \(d\nu_\alpha(z)=\frac{\Gamma(d+\alpha+1)}{\pi^d\Gamma(\alpha+1)}(1-\|z\|^2)^\alpha dV(z)\). The complex Hilbert space \(A^2_\alpha\) is the analytic subspace of \(L^2(d\nu_\alpha)\), and \(P\) its orthogonal projection. All symbols above are bounded continuous radial functions. The integer \(m\) is fixed when \(n\to\infty\); no assertion is made uniformly as \(m\) or \(d\) grows. The Schatten terminology applies to \(0<p<1\) as quasi-ideals. The branch is defined intrinsically using homogeneous degree and ordered eigenvalues, even at finite-degree coincidences; basis choices within a degenerate eigenspace do not change its singular-value multiset. The only possible accumulation point of the spectrum is zero, which is not an eigenvalue.

## Proof

**1. Positive compression defect and exact blocks.** For any \(x_1,\ldots,x_m\in A^2_\alpha\), the positive quadratic form is

\[
\sum_{i,j=1}^m\langle(T_{u^{i+j}}-T_{u^i}T_{u^j})x_j,x_i\rangle
=\left\|(I-P)\sum_{j=1}^m u^j x_j\right\|_{L^2(d\nu_\alpha)}^2\ge0.
\]

A radial Toeplitz operator acts scalarly on each homogeneous polynomial subspace. For a normalized monomial of total degree \(n\), radial integration shows that \(U=1-\|z\|^2\) under its squared-modulus weighted probability measure has beta density \(U^{b-1}(1-U)^{a-1}/\mathrm B(b,a)\), \(a=n+d\), \(b=\alpha+1\). Consequently \(\mathbb E U^j=(b)_j/(a+b)_j\) and the displayed covariance blocks follow. All homogeneous subspaces have dimension \(h_{n,d}=\binom{n+d-1}{d-1}\). Since the beta law has strictly positive density on \((0,1)\), no nonconstant real or complex polynomial in \(U\) is almost surely constant; hence each covariance matrix is positive definite. This also establishes injectivity.

**2. Exact determinants from monic Jacobi norms.** For \(a,b>0\), let \(w(U)=U^{b-1}(1-U)^{a-1}\) and form the Rodrigues polynomial

\[
Q_j(U)=w(U)^{-1}\frac{d^j}{dU^j}\big[U^j(1-U)^j w(U)\big].
\]

Integrating by parts \(j\) times, using that the endpoint terms vanish for \(a,b>0\), proves orthogonality to all lower powers. Its leading coefficient equals \((-1)^j(a+b+j-1)_j\). Its monic version has squared norm

\[
H_j(a,b)=\frac{j!\,(a)_j(b)_j}{(a+b)_{2j}(a+b+j-1)_j}.
\]

Indeed, orthogonality allows the square norm to be calculated by pairing with \(U^j\); the Rodrigues integration yields \((-1)^j j!\mathrm B(b+j,a+j)/\mathrm B(b,a)\), followed by division by the leading coefficient. Gram–Schmidt of the centered powers \(U^j-\mathbb EU^j\), \(1\le j\le k\), coincides with Gram–Schmidt of \(1,U,\ldots,U^k\) after removing the constant polynomial. Therefore its Gram determinant equals \(\prod_{j=1}^k H_j(a,b)\), the claimed formula, including the boundary case \(k=1\).

**3. Distinct eigenvalue orders and Laguerre constants.** As \(a=n+d\to\infty\), the rescaled beta variable \(Y_n=nU\) converges in every fixed polynomial moment to a gamma variable \(Y\) with density \(y^{b-1}e^{-y}/\Gamma(b)\). With \(E_n=\operatorname{diag}(n^{-1},\ldots,n^{-m})\), this gives

\[
E_n^{-1}G_nE_n^{-1}\longrightarrow H,
\qquad H_{ij}=\operatorname{Cov}(Y^i,Y^j).
\]

The limiting matrix \(H\) is positive definite. Consequently for fixed \(m\) and all sufficiently large \(n\), \(cE_n^2\preceq G_n\preceq CE_n^2\) for some fixed positive \(c,C\). The min–max principle gives \(\lambda_k(n)\asymp n^{-2k}\), making consecutive eigenvalue ratios tend to zero.

For any \(k\)-element set \(I\subseteq\{1,\ldots,m\}\), its principal determinant satisfies \(\det G_n[I,I]\sim n^{-2\sum_{i\in I}i}\det H[I,I]\). In the elementary symmetric polynomial \(e_k(G_n)\), the unique dominant set is \(I=\{1,\ldots,k\}\), since it uniquely minimizes \(\sum i\). Thus \(e_k(G_n)\sim n^{-k(k+1)}\det H[1:k,1:k]\). The separation of the eigenvalues implies \(e_k(G_n)\sim\prod_{j=1}^k\lambda_j(n)\). Taking successive ratios shows

\[
n^{2k}\lambda_k(n)\to\frac{\det H[1:k,1:k]}{\det H[1:k-1,1:k-1]}.
\]

The gamma monic orthogonal polynomials are rescaled Laguerre polynomials. Rodrigues integration (or the \(a\to\infty\) limit of \(n^{2k}H_k(a,b)\)) gives their squared monic norms exactly \(k!(b)_k\), concluding the spectral hierarchy. For the zero-size determinant use the convention \(1\).

**4. Exact singular-value asymptotics.** The homogeneous multiplicity satisfies \(\sum_{n=0}^{N}h_{n,d}=\binom{N+d}{d}\sim N^d/d!\). For fixed \(k\), the previous conclusion implies that the number of branch eigenvalues exceeding small \(t>0\) obeys

\[
\#\{s_j(\mathcal V_m^{(k)})>t\}
\sim \frac{1}{d!}\left(\frac{c_k}{t}\right)^{d/(2k)}\quad(t\downarrow0).
\]

This count follows by comparing all sufficiently late degrees to \((1\pm\varepsilon)c_kn^{-2k}\), and does not assume finite-degree monotonicity. Monotone inversion gives the singular-value asymptotic. Summing the resulting sequence of regularly varying singular values yields \(\mathcal S_p\) exactly for \(2kp/d>1\); at equality the partial sum is \(c_k^{d/(2k)}(d!)^{-1}\log J+o(\log J)\). Positivity and decay of every fixed branch show compactness of the full finite-channel defect. The largest branch determines the full defect's threshold.

## Verification

The included `checks/check_laguerre.py` uses exact rational beta moments to recompute leading covariance determinants and homogeneous multiplicities in finite cases, and high-precision eigenvalues to check the predicted Laguerre constants for several real weights and dimensions. Execute with `python checks/check_laguerre.py` in an environment with `mpmath` installed. The program prints its exact finite assertion count. It is supportive numerical evidence only; the proof of the infinite family is Steps 1–4 above.

## Relationship to prior work

The radial Toeplitz diagonalization and its moment-sequence viewpoint are established tools (Grudsky–Karapetyants–Vasilevski; Bauer–Herrera Yañez–Vasilevski; Maximenko–Pacheco). Tang–Wang–Zheng establish semicommutator trace formulas on weighted Bergman balls. Dawson–Dewage–Ólafsson's 2026 paper characterizes radial Toeplitz algebras and Schatten-type approximation in its quantum harmonic analysis setting. None of the inspected statements gives the ordered **matrix** semicommutator eigenbranches, their exact monic-Jacobi Gram determinants, or all \(m\) sharp Laguerre Weyl constants. The new claim deliberately does not assert novelty for scalar radial diagonalization, basic beta moments, Jacobi/Laguerre orthogonality, or generic Toeplitz–Hankel identities.

## Limitations

The claim is for the fixed natural hierarchy of boundary-distance monomials and does not classify arbitrary radial symbols or general bounded symmetric domains. Its exact determinant and asymptotic analysis rely on an integer number of channels and the beta measure. A broader result under a polynomial-covariance, moment-matrix, or semiclassical quantization formulation might imply this specialization; a bibliographic search is not a proof of priority. Scientific correctness and originality have received self-review scrutiny only, not independent validation.

## References

1. M. Dawson, V. Dewage, G. Ólafsson, *Quantum harmonic analysis and the Differential operators on weighted Bergman spaces of bounded symmetric domains*, arXiv:2610.33428v1 (first publicly available 2026-10-24), https://arxiv.org/html/2610.33428v1 .
2. X. Tang, Y. Wang, D. Zheng, *Trace Formula of Semicommutators*, arXiv:2210.04148v1 (2022), https://arxiv.org/html/2210.04148v1 .
3. E. A. Maximenko, C. G. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, arXiv:2503.23649 (2025), https://arxiv.org/abs/2503.23649 .
4. W. Bauer, C. Herrera Yañez, N. Vasilevski, *Eigenvalue Characterization of Radial Operators on Weighted Bergman Spaces Over the Unit Ball*, Integral Equations Operator Theory 78 (2014), 271–300, DOI:10.1007/s00020-013-2101-1 .
5. S. Grudsky, A. Karapetyants, N. Vasilevski, *Toeplitz operators on the unit ball in \(\mathbb C^n\) with radial symbols*, Journal of Operator Theory 49 (2003), 325–346.
