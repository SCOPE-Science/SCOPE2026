# Logarithmic directional response hidden by scalar calibration for anisotropic Gaussian polar updates

## Finding
Consider the normalized row-polar map \(P(z)=z/\|z\|_2\) for nonzero \(z\in\mathbb R^2\), with \(P(0)=0\). Let \(U,V\) be independent standard Gaussians, \(Z_r=(rU,V)\), and \(F_r(h)=\mathbb E[P(Z_r+h)]\). For every \(r\ge1\), the response \(D F_r(0)\) is diagonal, \(J_r=\operatorname{diag}(a_r,b_r)\). Define
\[
k_r=\sqrt{1-r^{-2}},\quad K(k)=\int_0^{\pi/2}\frac{d\phi}{\sqrt{1-k^2\sin^2\phi}},\quad E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2\phi}\,d\phi.
\]
For every \(r>1\), its exact coefficients are
\[
a_r=\sqrt{\frac2\pi}\frac{r^2E(k_r)-K(k_r)}{r(r^2-1)},\qquad b_r=\sqrt{\frac2\pi}\frac{r[K(k_r)-E(k_r)]}{r^2-1}.
\]
At \(r=1\), \(a_1=b_1=\sqrt{\pi/2}/2\). For every \(r>1\), \(0<a_r<b_r\). More sharply,
\[
a_r\sim\sqrt{\frac2\pi}\,r^{-1},\qquad b_r=\sqrt{\frac2\pi}\,r^{-1}(\log(4r)-1+o(1)),\qquad\frac{b_r}{a_r}=\log(4r)-1+o(1)
\]
as \(r\to\infty\). Hence for each fixed \(c>1\) and all sufficiently large \(r\), the positive signal \(h=(c,1)\) has a **strict component-order reversal**: \(h_1>h_2\), yet \(F_r(\varepsilon h)_2>F_r(\varepsilon h)_1\) for every sufficiently small \(\varepsilon>0\).

At the same time, let \(\Sigma_r=\operatorname{diag}(r^2,1)\) and define the optimal scalar response approximation and its relative noise-weighted error by
\[
s_r^*=\underset{s\in\mathbb R}{\operatorname{argmin}}\;\mathbb E\|(J_r-sI)Z_r\|_2^2,\qquad
\delta_r=\frac{\min_{s\in\mathbb R}\mathbb E\|(J_r-sI)Z_r\|_2^2}{\mathbb E\|J_rZ_r\|_2^2}.
\]
These have the exact laws
\[
s_r^*=\frac{r^2a_r+b_r}{r^2+1},\qquad\delta_r=\frac{r^2(a_r-b_r)^2}{(r^2+1)(r^2a_r^2+b_r^2)},\qquad
\delta_r\sim\frac{(\log r)^2}{r^2}\longrightarrow0.
\]
Thus the same family has an unbounded directional-gain ratio while the optimum global scalar-fit criterion tends to zero. The phenomenon is an explicit quantitative failure mode for interpreting a small noise-weighted scalar fit as directional response matching; the scalar-fit functional itself is pre-existing.

## Assumptions and scope
All expectations refer to independent real standard normal \(U,V\). The parameter range is \(1\le r<\infty\); covariance \(\Sigma_r\) is positive definite for every finite \(r\). The noise is centered, the matrix is a single real \(1\times2\) row, and its polar factor is exact. The local derivative holds with \(r\) held fixed as \(h\to0\), while asymptotic statements take \(r\to\infty\) only after the derivative. A scalar fit is chosen over \(s\in\mathbb R\); the optimum is automatically positive, hence identical if restricted to positive scalar rates. The order reversal is a local mean-response statement, not an assertion about sample-path ordering or optimization loss.

## Proof
**Step 1 (well-defined local response).** Since \(P\) is bounded and the centered Gaussian density with covariance \(\Sigma_r\) is smooth with all derivatives integrable, the convolution \(F_r(h)=\mathbb E[P(Z_r+h)]\) is smooth. Differentiating the density gives the Gaussian score identity
\[
D F_r(0)=\mathbb E[P(Z_r)Z_r^{\mathsf T}]\Sigma_r^{-1}.
\]
An independent derivation uses \(D P(z)=\|z\|_2^{-1}I-\|z\|_2^{-3}zz^{\mathsf T}\), whose entries are bounded by \(1/\|z\|_2\). This is integrable for a nondegenerate centered planar Gaussian; dominated differentiation is valid. Reflection symmetry makes the off-diagonals zero and gives
\[
a_r=\mathbb E\frac{V^2}{(r^2U^2+V^2)^{3/2}},\qquad
b_r=\mathbb E\frac{r^2U^2}{(r^2U^2+V^2)^{3/2}}.
\]
Both are finite and strictly positive. For \(r=1\), rotational symmetry and the Rayleigh reciprocal mean \(\mathbb E(1/\sqrt{U^2+V^2})=\sqrt{\pi/2}\) give \(a_1=b_1=\sqrt{\pi/2}/2\).

**Step 2 (complete elliptic integrals).** Write \((U,V)=R(\cos\phi,\sin\phi)\), where \(R\) is Rayleigh, \(\phi\) is uniform on \([0,2\pi)\), and they are independent. Let
\[
L(r)=\int_0^{2\pi}\frac{d\phi}{\sqrt{r^2\cos^2\phi+\sin^2\phi}}=\frac{4K(k_r)}r.
\]
Differentiation under this finite integral gives
\[
a_r=\frac{\sqrt{\pi/2}}{2\pi}[L(r)+rL'(r)],\qquad b_r=-\frac{\sqrt{\pi/2}}{2\pi}rL'(r).
\]
The standard identity \(dK(k)/dk=E(k)/(k(1-k^2))-K(k)/k\), together with \(dk_r/dr=1/(k_rr^3)\), yields the stated formulas for \(r>1\). The \(r=1\) values are their continuous limits.

**Step 3 (strict gain inversion).** The elementary Gamma-integral identity \(q^{-3/2}=2\pi^{-1/2}\int_0^\infty t^{1/2}e^{-tq}\,dt\) and Gaussian Laplace moments show that the positive integrands for \(a_r\) and \(b_r\) are, apart from their common constant,
\[
f_a(t)=\frac{t^{1/2}}{(1+2r^2t)^{1/2}(1+2t)^{3/2}},\qquad
f_b(t)=\frac{r^2t^{1/2}}{(1+2r^2t)^{3/2}(1+2t)^{1/2}}.
\]
For every finite \(t>0\) and \(r>1\), \(f_b(t)/f_a(t)=r^2(1+2t)/(1+2r^2t)>1\). Therefore \(b_r>a_r\), with no numerical or asymptotic assumption. Classical complementary-modulus expansions for \(K\) and \(E\), with complementary modulus \(1/r\), give \(K(k_r)=\log(4r)+O(r^{-2}\log r)\) and \(E(k_r)=1+O(r^{-2}\log r)\); substitution yields the exact leading behavior above, including the constant term \(-1\) in \(b_r\). For fixed \(c>1\), choose \(r\) so that \(b_r/a_r>c\). Differentiability and \(F_r(0)=0\) give \(F_r(\varepsilon(c,1))=\varepsilon(a_rc,b_r)+o(\varepsilon)\), proving the strict order reversal for sufficiently small positive \(\varepsilon\).

**Step 4 (the scalar-diagnostic blind spot).** For any real \(s\), independence and centeredness give
\[
\mathbb E\|(J_r-sI)Z_r\|_2^2=r^2(a_r-s)^2+(b_r-s)^2.
\]
Completing the square produces the unique optimizer \(s_r^*>0\), minimum \(r^2(a_r-b_r)^2/(r^2+1)\), and normalized error formula in the statement. Writing \(C=\sqrt{2/\pi}\), the preceding asymptotics imply \(a_r=C/r(1+o(1))\), \(b_r=C/r(\log r+O(1))\). The denominator of \(\delta_r\) is \(C^2r^2(1+o(1))\), and the numerator is \(C^2(\log r)^2(1+o(1))\). Thus \(\delta_r\sim(\log r)^2/r^2\) even as \(b_r/a_r\to\infty\). No interchange of large-\(r\) and small-\(h\) limits is used.

## Verification
Run `python verify.py` in an environment with NumPy, SciPy and mpmath. The script compares closed elliptic formulas with independent angular quadratures, checks positivity/order and the exact scalar least-squares identity, verifies large-anisotropy expansions at high precision, and performs independent Gaussian-score Monte Carlo checks of the response coefficients. The observed run returned `PASS: 88 deterministic high-precision/quadrature/formula/Monte-Carlo tolerance assertions`; for \(r=10\) it gave \(a_r=0.078904913486\), \(b_r=0.215964285940\), \(b_r/a_r=2.737019488387\), and \(\delta_r=0.027791679403\). These finite checks are corroborating diagnostics, **not proofs** of universal or limiting statements; those rest on the preceding analytical derivation.

## Relationship to prior work
Xie, *Muon Under Gradient Noise and the Limits of Orthogonalization Near Optima* (2026), Theorem 4.1, gives the **general Gaussian response-score identity** under arbitrary covariance; this is prior work and not asserted as new. Appendix C.3 already derives the **optimal scalar noise-weighted fitting formula**, and warns qualitatively that weak-noise directions can escape scalar diagnostics. The contribution here is the special **explicit anisotropic polar-response calculation**, the strict direction-gain order reversal, the sharp logarithmic divergence of the ratio, and a **quantified realization** in which the precise pre-existing scalar metric tends to zero while directional mismatch grows unbounded. Herrera-Esposito and Burge (2025) develop projected-normal moments and approximations, including isotropic exact moments and anisotropic general approximations. The NIST DLMF §19.31 already provides general Gaussian quadratic-form expectations in symmetric elliptic integrals; mere elliptic reducibility is **not** an originality claim. The specialized coupled response-order and scalar-diagnostic asymptotics are not present in the inspected relevant passages. Older directional-statistics special-function identities might imply equivalent formulas; this is a bibliographic residual risk.

## Limitations
This is an exact \(1\times2\) real Gaussian row-polar benchmark. It concerns local expected response and a one-step fitting criterion, not convergence of a stochastic optimizer, a matrix of higher row rank, correlated non-Gaussian noise, or exact loss floors. The formulas hold at finite \(r\); their asymptotics do not assert uniformity of the linear response remainder as \(r\to\infty\). No claim of new general Gaussian score identity, new scalar matching principle, or new elliptic integral identities is made. Searches cannot establish global uniqueness; comparable formulas may appear under directional-statistics terminology.

## References
- X. Xie, *Muon Under Gradient Noise and the Limits of Orthogonalization Near Optima*, arXiv:2609.32861v1, first posted 2026-09-26, especially Section 4 and Appendix C.3. https://arxiv.org/pdf/2609.32861
- D. Herrera-Esposito and J. Burge, *Projected Normal Distribution: Moment Approximations and Generalizations*, arXiv:2506.17461, first posted June 2025, especially Sections 2.2 and 2.2.3. https://arxiv.org/pdf/2506.17461
- NIST Digital Library of Mathematical Functions, §19.31, *Probability Distributions*, Gaussian quadratic-form identities and elliptic integrals. https://dlmf.nist.gov/19.31
