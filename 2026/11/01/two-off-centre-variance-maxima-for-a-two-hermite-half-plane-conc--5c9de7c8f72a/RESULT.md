# Two off-centre variance maxima for a two-Hermite half-plane concentration fiber

## Finding
Let \(h_0(x)=\pi^{-1/4}e^{-x^2/2}\) and \(h_1(x)=\sqrt{2}\,x h_0(x)\) be the first two normalized Hermite functions in \(L^2(\mathbb R,dx)\). For every real threshold \(t\), compress multiplication by \(\mathbf1_{(t,\infty)}\) to their two-dimensional span:
\[
 A(t)_{jk}=\int_t^\infty h_j(x)h_k(x)\,dx,\qquad j,k\in\{0,1\}.
\]
Define the **fiber concentration defect**
\[
 V(t)=\operatorname{tr}\bigl(A(t)(I_2-A(t))\bigr).
\]
Set \(\varphi(t)=e^{-t^2}/\sqrt\pi\) and \(Q(t)=\operatorname{erfc}(t)/2\). The complete two-level fiber spectrum and defect are
\[
 A(t)=\begin{pmatrix}Q(t)&\varphi(t)/\sqrt2\\
 \varphi(t)/\sqrt2&Q(t)+t\varphi(t)\end{pmatrix},
\qquad
 \lambda_\pm(t)=Q(t)+\frac{\varphi(t)}2\bigl(t\pm\sqrt{t^2+2}\bigr),
\]
\[
 V(t)=\frac{1-\operatorname{erf}(t)^2}{2}
 +t\varphi(t)\operatorname{erf}(t)-(1+t^2)\varphi(t)^2.
\]
**Global extremum classification.** The only stationary thresholds of \(V\) on \(\mathbb R\) are \(0\) and \(\pm\tau\), where \(\tau>0\) is the unique solution of
\[
 \operatorname{erf}(\tau)=\frac{4\tau(1+\tau^2)}{1+2\tau^2}\frac{e^{-\tau^2}}{\sqrt\pi}.
\]
The central threshold is a strict local **minimum**, with \(V(0)=1/2-1/\pi\) and \(V''(0)=2/\pi\). The two off-centre thresholds \(\pm\tau\) are the **only global maxima**. Numerically, \(\tau=0.748111391996\ldots\) and \(V(\tau)=0.257120277198\ldots\). The limit of \(V(t)\) is zero as \(|t|\to\infty\). All assertions hold for every real \(t\), with no asymptotic parameter.

The family is the Hermite-fiber representative of the **order-two polyanalytic Gaussian Fock Toeplitz operator** with half-plane symbol \(\mathbf1_{\{\operatorname{Im}z>0\}}\). In the horizontal Fourier representation of Lee-Guzmán, Maximenko, Ramos-Vazquez and Sánchez-Nungaray (Proposition 10.4), its fiber at spectral coordinate \(\xi\) equals \(A(\xi/\sqrt2)\). Thus the double maximum describes an intrinsic two-level spectral concentration effect, not a trace of the infinite-dimensional Toeplitz operator itself.

## Assumptions and scope
The Hermite functions use physicists' polynomials and the normalization \(\int_{\mathbb R}|h_j|^2dx=1\). All functions and matrices are complex-linear, while the displayed Hermite basis and its Gram matrix are real. The full order-two polyanalytic Fock space means the Gaussian Hilbert space of functions satisfying \(\partial_{\bar z}^{\,2}f=0\), with area probability measure \(\pi^{-1}e^{-|z|^2}\,dA(z)\); it contains the analytic and first true-polyanalytic levels. The half-plane symbol is bounded, so its Toeplitz compression is a bounded self-adjoint contraction. The definition of \(V\) is a **two-by-two fiber trace**. No global Schatten trace, integral of \(V\), or finite-rank property of the full Toeplitz operator is implied.

For comparison, retaining only \(h_0\) produces a one-level defect \(Q(t)(1-Q(t))\), whose unique global maximum \(1/4\) is at \(t=0\). Therefore the off-centre split is absent in the analytic one-level case.

## Proof
**1. Explicit compression.** Write \(\varphi(x)=|h_0(x)|^2\). Its Gaussian tail is \(Q(t)=\int_t^\infty\varphi(x)\,dx\). Since \(h_0h_1=\sqrt2 x\varphi(x)\) and \(\varphi'(x)=-2x\varphi(x)\),
\[
 \int_t^\infty h_0h_1\,dx=\frac{\varphi(t)}{\sqrt2}.
\]
Integration by parts gives \(\int_t^\infty 2x^2\varphi(x)\,dx=Q(t)+t\varphi(t)\), proving the matrix identity. For any nonzero vector \(c\in\mathbb C^2\), the function \(c_0h_0+c_1h_1\) is nonzero and real analytic. Consequently its squared norm is strictly positive on each half-line, so \(0<A(t)<I_2\) for finite \(t\). The off-diagonal entry is nonzero; hence both eigenvalues are distinct and lie strictly between zero and one. The quadratic formula gives the displayed \(\lambda_\pm\).

**2. Exact defect and symmetry.** Taking the trace of \(A-A^2\) yields
\[
 V=2Q(1-Q)+t\varphi(1-2Q)-(1+t^2)\varphi^2.
\]
Since \(1-2Q=\operatorname{erf}(t)\), this is the asserted closed form. For \(S=\mathrm{diag}(1,-1)\), parity of \(h_0,h_1\) gives \(A(-t)=I_2-SA(t)S\). It follows that \(V(-t)=V(t)\). Both eigenvalues of \(A(t)\) tend to zero as \(t\to+\infty\), and to one as \(t\to-\infty\), so \(V(t)\to0\) at both ends.

**3. The only positive stationary point.** Put \(E(t)=\operatorname{erf}(t)\). Using \(E'(t)=2\varphi(t)\), \(\varphi'(t)=-2t\varphi(t)\), direct differentiation gives
\[
 V'(t)=\varphi(t)\left[4t(1+t^2)\varphi(t)-(1+2t^2)E(t)\right].
\]
For \(t>0\) its sign is that of \(R(t)-L(t)\), where
\[
 L(t)=\frac{E(t)}{2t\varphi(t)}=\int_0^1e^{t^2(1-u^2)}\,du,
\qquad R(t)=\frac{2(1+t^2)}{1+2t^2}.
\]
For every \(t>0\), the integral defining \(L(t)\) is strictly increasing with \(t\), because its integrand increases strictly for \(0\le u<1\). By contrast,
\[
 R'(t)=-\frac{4t}{(1+2t^2)^2}<0.
\]
Moreover \(L(0+)=1<R(0+)=2\), while \(L(t)\to\infty\) and \(R(t)\to1\) as \(t\to\infty\). There is therefore exactly one \(\tau>0\) with \(L(\tau)=R(\tau)\), with \(V'>0\) before and \(V'<0\) after this point. This proves existence, uniqueness, and strict global maximality on the positive half-line.

**4. The central minimum and global classification.** The exact Taylor expansion at the origin is
\[
 V(t)=\frac12-\frac1\pi+\frac{t^2}\pi-\frac{4t^4}{3\pi}+O(t^6),
\]
so \(V''(0)=2/\pi>0\). Evenness and the strict derivative signs from Step 3 leave exactly three critical points: \(0\), \(\tau\), and \(-\tau\). The latter two are the sole global maxima, and the strictly positive value at either exceeds the central value. This establishes the complete statement.

**5. Interpretation for the half-plane Toeplitz operator.** The published horizontal Fourier reduction for polyanalytic Fock spaces states, for a symbol depending only on the imaginary coordinate,
\[
 \gamma_g(\xi)_{jk}=\sqrt2\int_{\mathbb R}g(v)
 h_j\!\left(\frac{\xi+2v}{\sqrt2}\right)
 h_k\!\left(\frac{\xi+2v}{\sqrt2}\right)\,dv.
\]
For \(g(v)=\mathbf1_{\{v>0\}}\), substituting \(x=(\xi+2v)/\sqrt2\) shows \(\gamma_g(\xi)=A(\xi/\sqrt2)\). The preceding matrix analysis therefore applies to every fiber of this operator. This step uses the established unitary decomposition, rather than asserting a new general decomposition.

## Verification
The accompanying standard-library Python program `verify.py` independently integrates \(h_jh_k\) over Gaussian tails by composite Simpson quadrature, compares the results with the explicit entries, checks the quadratic eigenvalues and positivity, and verifies the symmetric defect and derivative signs on finite test grids. It computes the unique positive root by bisection on the bracket \((0.7,0.8)\). Running `python verify.py` yielded `VERIFY_OK checks=527 tstar=0.748111391996229 Vmax=0.257120277198686`. These finite diagnostics support normalization and numerical reporting; they do **not** establish the global theorem. The global uniqueness and monotonicity are proved analytically in Steps 3–4.

## Relationship to prior work
The 2018 paper of Sánchez-Nungaray, González-Flores, López-Martínez and Arroyo-Neri proves the matrix representation of horizontal-symbol Toeplitz operators and even displays step-symbol fiber integrals (Section 4, expression (53)); **that representation is prior work, not a newly claimed result**. The 2023-09-07 preprint of Lee-Guzmán, Maximenko, Ramos-Vazquez and Sánchez-Nungaray supplies a general exact Hermite fiber formula (Proposition 10.4). The new statement here is the **complete location and uniqueness classification for the extrema of the two-level spectral defect**, obtained by an additional special-function monotonicity argument. No checked section of either source asserts this two-peak variance law or its unique threshold.

A published result titled *Half-line Hermite spectral gaps: arbitrary-mask Cauchy formula and a Barnes limit* treats parity and spectral gaps at the centered threshold; its stated scope excludes shifted thresholds. That result includes overlapping centered matrix information but neither implies nor claims the global off-centre maximization theorem without the new threshold analysis. The Hermite kernel also represents the two-particle Gaussian unitary ensemble; the defect is the variance of the number of particles above a moving threshold, so equivalent random-matrix terminology is a plausible location for older coverage. The available searches did not locate a statement of this exact two-maximum classification; absence of a search hit is not proof of historical priority.

## Limitations
This is a fixed **two-mode** result: it does not describe the number or location of variance maxima for higher polyanalytic orders, arbitrary non-step symbols, finite-width strips, multidimensional half-spaces, or all choices of Hermite-level masks. The coefficient \(0.257120277198\ldots\) is numerical evaluation of a uniquely characterized transcendental quantity, not an asserted elementary closed form or a certified last-digit interval. Although the exact matrix is an elementary specialization of an established general formula, the monotone-ratio extremum classification is not explicitly stated in the inspected literature; potential equivalent formulas in finite-particle random-matrix statistics remain a historical-priority risk. Independent mathematical validation is not claimed.

## References
- A. Sánchez-Nungaray, C. González-Flores, R. Rufino López-Martínez and J. L. Arroyo-Neri, *Toeplitz Operators with Horizontal Symbols Acting on the Poly-Fock Spaces*, Journal of Function Spaces (2018), article 8031259, published 2018-07-16. https://doi.org/10.1155/2018/8031259
- E. Lee-Guzmán, E. A. Maximenko, G. Ramos-Vazquez and A. Sánchez-Nungaray, *Horizontal Fourier transform of the polyanalytic Fock kernel*, arXiv:2309.03410v1, first public 2023-09-07. https://arxiv.org/abs/2309.03410
- *Half-line Hermite spectral gaps: arbitrary-mask Cauchy formula and a Barnes limit*, publicly available mathematical result, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-half-line-hermite-spectral-gaps-arbitrary-mask-cauchy-formula-an--5e08b6020a88
