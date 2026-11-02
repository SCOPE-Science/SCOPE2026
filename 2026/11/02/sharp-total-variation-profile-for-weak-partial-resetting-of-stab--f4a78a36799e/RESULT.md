# Sharp total-variation profile for weak partial resetting of stable Lévy motions

## Finding
Fix an index \(0<\alpha\le 2\). Let \(X^{(c)}\) have the unique stationary distribution of a symmetric \(\alpha\)-stable Lévy motion with Poisson partial resets \(x\mapsto cx\) at unit rate, where \(0<c<1\). Set
\[
\delta=1-c^\alpha,\qquad \varepsilon_c=\frac{\delta}{2-\delta},\qquad Z_c=\delta^{1/\alpha}X^{(c)}.
\]
Let \(p_{\alpha,v}\) be the symmetric stable density specified by \(\widehat p_{\alpha,v}(t)=\exp(-v|t|^\alpha)\), and let \(p_\alpha=p_{\alpha,1}\). Define
\[
K_\alpha(x)=\left.\frac{\partial^2}{\partial v^2}p_{\alpha,v}(x)\right|_{v=1}
=\frac1{2\pi}\int_{\mathbb R} e^{-itx}|t|^{2\alpha}e^{-|t|^\alpha}\,dt.
\]
The stationary normalized density \(f_c\) satisfies the **strong first-order expansion**
\[
\left\|f_c-p_\alpha-\frac{\varepsilon_c}{2}K_\alpha\right\|_{L^1(\mathbb R)}
=O_\alpha(\delta^{3/2})\qquad(c\uparrow1).
\]
Consequently the total-variation distance (defined as half the \(L^1\)-distance of densities) has the sharp asymptotic
\[
d_{\mathrm{TV}}(\mathcal L(Z_c),p_\alpha(x)\,dx)
=C_\alpha\varepsilon_c+O_\alpha(\delta^{3/2}),\qquad
C_\alpha=\frac14\|K_\alpha\|_1\in(0,\infty).
\]
The leading density correction changes sign; the formula thus describes more than weak convergence. The constants at the Cauchy and Gaussian endpoints are explicit:
\[
C_1=\frac{3\sqrt3}{8\pi},\qquad
C_2=\frac{\sqrt6}{4}\left[a\varphi(a)+b\varphi(b)\right],
\quad a=\sqrt{3-\sqrt6},\quad b=\sqrt{3+\sqrt6},
\]
where \(\varphi(x)=(2\pi)^{-1/2}e^{-x^2/2}\).

## Assumptions and scope
All results are for one real spatial dimension, a symmetric Lévy process with increments characterized by \(\mathbb E e^{it(L_s-L_0)}=\exp(-s|t|^\alpha)\), and independent unit-intensity Poisson resetting by a fixed contraction \(c\in(0,1)\). The stable law is centered under this characteristic-function normalization; for \(\alpha=2\) it is normal with variance \(2\). The index \(\alpha\) is held fixed when \(c\uparrow1\). No finite-variance assumption is imposed for \(\alpha<2\). The assertion is **not** uniform in \(\alpha\), and makes no claim about transient distributions or multidimensional anisotropy.

## Proof
**1. Stationary mixture.** At a stationary observation time, the current Poisson interarrival age and all preceding interarrival lengths are independent unit-rate exponential variables \(E_0,E_1,\ldots\). The independent Lévy increments across these backward intervals, multiplied respectively by \(1,c,c^2,\ldots\), give the stationary series in law. Conditional on the exponential lengths, stability and independent increments show that \(Z_c\) has the symmetric stable density with operational time
\[
V_\delta=\delta\sum_{j=0}^\infty(1-\delta)^jE_j.
\]
The series converges almost surely and in every \(L^r\), \(r\ge1\). Consequently \(f_c(x)=\mathbb E[p_{\alpha,V_\delta}(x)]\). This also follows from the independent-product characteristic function
\[
\widehat f_c(t)=\prod_{j=0}^\infty\bigl(1+\delta(1-\delta)^j|t|^\alpha\bigr)^{-1}.
\]
The series construction gives a stationary solution by the reset-time distributional recursion. Since reset contractions decrease differences from different initial states, the stationary law is unique.

**2. Exact operational-time moments.** Additivity and homogeneity of exponential cumulants give, for integers \(r\ge1\),
\[
\kappa_r(V_\delta)=\frac{(r-1)!\,\delta^r}{1-(1-\delta)^r}.
\]
In particular,
\[
\mathbb E V_\delta=1,\quad
\mathbb E(V_\delta-1)^2=\varepsilon_c,\quad
\mathbb E(V_\delta-1)^4=3\varepsilon_c^2+
\frac{6\delta^4}{1-(1-\delta)^4}=O(\delta^2).
\]
Therefore \(\mathbb E|V_\delta-1|^3=O(\delta^{3/2})\) and, by the fourth-moment Markov inequality, \(\Pr(|V_\delta-1|>1/2)=O(\delta^2)\).

**3. Density-valued Taylor theorem.** On the closed interval \(v\in[1/2,3/2]\), the map \(v\mapsto p_{\alpha,v}\) is three times continuously differentiable into \(L^1(\mathbb R)\), with bounded third derivative. Indeed
\[
p_{\alpha,v}(x)=v^{-1/\alpha}p_\alpha(xv^{-1/\alpha}).
\]
Differentiating the scaling identity up to three times produces finite linear combinations of dilated \(x^jp_\alpha^{(j)}(x)\), \(0\le j\le3\). For \(0<\alpha<2\), the standard stable-density derivative tail bounds \(p_\alpha^{(j)}(x)=O((1+|x|)^{-1-\alpha-j})\) ensure integrability; the Gaussian case is immediate. Thus, when \(|v-1|\le1/2\),
\[
\left\|p_{\alpha,v}-p_\alpha-(v-1)\dot p_{\alpha,1}
-\tfrac12(v-1)^2K_\alpha\right\|_1
\le M_\alpha|v-1|^3.
\]
On the complement, use the universal density bound \(\|p_{\alpha,v}-p_\alpha\|_1\le2\). The discarded first- and second-moment terms are bounded by \(O(\delta^2)\) using the fourth-moment estimate and Hölder's inequality. Average the Taylor formula, using the *exact* cancellation \(\mathbb E(V_\delta-1)=0\) and variance \(\varepsilon_c\). This gives the asserted \(O_\alpha(\delta^{3/2})\) remainder in \(L^1\), hence the total-variation expansion.

**4. Strict positivity and endpoint constants.** The Fourier transform of \(K_\alpha\) equals \(|t|^{2\alpha}e^{-|t|^\alpha}\), which is not identically zero; its \(L^1\)-norm is therefore strictly positive. At \(\alpha=1\), \(p_{1,v}(x)=v/[\pi(v^2+x^2)]\), so
\[
K_1(x)=\frac{2(1-3x^2)}{\pi(1+x^2)^3},\qquad
\|K_1\|_1=\frac{3\sqrt3}{2\pi}.
\]
For \(\alpha=2\), \(p_{2,v}\) has variance \(2v\), and
\[
K_2(x)=\frac14p_2(x)H_4(x/\sqrt2),\qquad H_4(z)=z^4-6z^2+3.
\]
Its sign changes exactly at the four points \(\pm a\sqrt2,\pm b\sqrt2\). Integrating with \((H_3\varphi)'=-H_4\varphi\), where \(H_3(z)=z^3-3z\), gives the claimed closed-form \(C_2\). Both formulas are strictly positive.

## Verification
A standalone Python checker in `verification/check.py` implements independent exponential-cumulant identities, finite characteristic-function products, direct Fourier quadrature for the second scale derivative, and exact sign-interval integrals for the Cauchy and Gaussian constants. Its deterministic execution output is recorded in `verification/check_output.txt`. The numerical assertions do not replace the continuum proof, nor do they establish the literature-priority claim. The exact first-order coefficient arises from the analytical \(L^1\) expansion.

## Relationship to prior work
Grzywny, Szczypkowski, Palmowski, and Trojan [1] formulate the same partial-reset stable process and derive its invariant density, moments, and convergence as physical time tends to infinity. Their density-mixture representation is the essential starting point here. Di Bello and collaborators [2] analyze partial versus total resetting for stable flights, including invariant formulas and spatial/transient behavior. Assefa, Keller-Ressel, and Palmowski [3] develop moment methods for affine resets. The finding here concerns a *different limit*, the reset contraction approaching unity, and derives a first-order *strong total-variation* asymptotic with explicit leading-density correction and constants. No priority claim is made for the invariant distribution, stable scaling identity, or general Taylor-expansion technique.

## Limitations
For a fixed \(\alpha\) the remainder constant is not explicitly optimized. The result does not identify finite-\(c\) exact total variation, multidimensional effects, nonsymmetric stable laws, arbitrary renewal resets, or uniformity as \(\alpha\) approaches an endpoint. Novelty relative to potentially broader abstract random-scale mixture expansion theorems is not independently certified.

## References
[1] T. Grzywny, K. Szczypkowski, Z. Palmowski, B. Trojan, *Stationary states for stable processes with partial resetting*, arXiv:2412.15626, first submitted 2024-12-20, https://arxiv.org/html/2412.15626v1 .

[2] C. Di Bello et al., *Partial versus total resetting for Lévy flights in d dimensions: similarities and discrepancies*, arXiv:2501.01139, first submitted 2025-01-02, https://arxiv.org/html/2501.01139v2 .

[3] J. Assefa, M. Keller-Ressel, Z. Palmowski, *Moments of polynomial processes under affine resetting*, arXiv:2610.01363, first submitted 2026-10-01, https://arxiv.org/abs/2610.01363 .
