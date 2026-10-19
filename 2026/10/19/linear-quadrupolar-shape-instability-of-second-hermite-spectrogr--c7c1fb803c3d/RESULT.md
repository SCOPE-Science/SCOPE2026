# Linear quadrupolar shape instability of second-Hermite spectrogram concentration

## Finding
Fix the normalized second Hermite function \(h_2\) as the analysis window of the short-time Fourier transform. Write
\[
\mathcal M(\Omega)=\sup_{\|f\|_2=1}\int_\Omega |V_{h_2}f(x,\omega)|^2\,dx\,d\omega.
\]
The centered disk \(D=\{(x,\omega):\pi(x^2+\omega^2)<2\}\), of area two, has
\[
\mathcal M(D)=1-5e^{-2},
\]
with a three-dimensional maximizing eigenspace \(\operatorname{span}\{h_0,h_1,h_2\}\) and a spectral gap of \(2e^{-2}/3\) to its next eigenvalue.

Let \(b\) be any real \(C^2\), periodic, mean-zero function and let \(\Omega_\varepsilon\) be a family of bounded smooth star-shaped planar regions of *exact area two* with polar boundary
\[
\pi r^2=2+\varepsilon b(\theta)+O(\varepsilon^2)
\]
in the \(C^1\) norm as \(\varepsilon\to0\). Put \(\widehat b(2)=(2\pi)^{-1}\int_0^{2\pi}b(\theta)e^{-2i\theta}\,d\theta\). Then the sharp operator-norm shape variation is
\[
\boxed{\mathcal M(\Omega_\varepsilon)=1-5e^{-2}+\sqrt2\,e^{-2}|\widehat b(2)|\,|\varepsilon|+O(\varepsilon^2).}
\]
In particular the equal-area ellipses
\[
E_\varepsilon=\{(x,\omega):e^{-\varepsilon}x^2+e^{\varepsilon}\omega^2<2/\pi\}
\]
satisfy
\[
\boxed{\mathcal M(E_\varepsilon)=1-5e^{-2}+\sqrt2\,e^{-2}|\varepsilon|+O(\varepsilon^2).}
\]
Consequently, the area-two disk is **not** even a local maximizer of time-frequency concentration for the fixed second Hermite window. At first order, only the quadrupolar shape Fourier mode matters.

## Assumptions and scope
Normalize \(h_0(t)=2^{1/4}e^{-\pi t^2}\) and let \(h_m\), \(m\ge0\), be the orthonormal Hermite basis in \(L^2(\mathbb R)\), with the standard real phase convention. Set
\[
V_gf(x,\omega)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\omega t}\,dt,
\qquad H_\Omega=V_{h_2}^*\mathbf1_\Omega V_{h_2}.
\]
Here \(\mathcal M(\Omega)=\|H_\Omega\|\) because \(H_\Omega\) is positive trace-class on bounded measurable \(\Omega\). The \(O(\varepsilon^2)\) remainder may depend on the fixed \(b\) and the stated boundary family; no uniformity over unbounded families of perturbations is asserted. The result is a *local* shape variation, not a classification of global maximizers.

## Proof
**1. Exact disk spectrum.** Put \(u=\pi(x^2+\omega^2)\). With polar angle \(\theta\), planar area is \(du\,d\theta/(2\pi)\). The Hermite-window ambiguity formula, equivalently the polyanalytic Bargmann transform identity of Abreu–Gröchenig [1, §2], shows that the radial disk localization matrix is diagonal on the Hermite basis. Its eigenvalues are
\[
\lambda_m=\int_0^2 e^{-u}\frac{\min(m,2)!}{\max(m,2)!}u^{|m-2|}
\left[L_{\min(m,2)}^{(|m-2|)}(u)\right]^2du,\qquad m\ge0.
\]
The first three densities are respectively \(e^{-u}u^2/2\), \(e^{-u}u(2-u)^2/2\), and \(e^{-u}(1-2u+u^2/2)^2\). Integration gives the common value \(1-5e^{-2}\). For \(m\ge2\) put
\[
Q_m(u)=u^2-2mu+m(m-1),\qquad
1-\lambda_m=e^{-2}P_m(2),
\]
where \(P_m\) is the unique polynomial solving
\[
P_m(u)-P'_m(u)=\frac{u^{m-2}Q_m(u)^2}{2m!}.
\]
This polynomial represents the normalized tail of the density, hence its value at the disk boundary determines \(1-\lambda_m\). A direct differentiation and expansion, followed by the fact that a polynomial solution of \(P-P'=G\) is unique, gives for every integer \(m\ge3\)
\[
P_m(u)-P_{m-1}(u)=\frac{u^{m-2}Q_{m-1}(u)Q_m(u)}{2m!}.
\]
Indeed, applying \(1-d/du\) to both sides yields the difference of their two Laguerre densities; uniqueness completes this algebraic identity. As \(Q_j(2)=(j-1)(j-4)\), the recurrence yields
\[
P_2(2)=5,\quad P_3(2)=P_4(2)=P_5(2)=17/3,
\quad P_{m}(2)>P_{m-1}(2)\quad(m\ge6).
\]
Thus the top three eigenvalues coincide and all remaining eigenvalues are at most \(1-(17/3)e^{-2}\). The claimed spectral gap follows, with equality for \(m=3,4,5\). Positivity and compactness show that no continuous spectrum can exceed this top value.

**2. Trace-norm first variation.** Write the domain boundary as \(u=R_\varepsilon(\theta)\), where \(R_\varepsilon(\theta)=2+\varepsilon b(\theta)+O(\varepsilon^2)\). For a phase-space point \(z\), let \(\Phi_z=\pi(z)h_2\) be its unit time-frequency translate. Since the map from \((u,\theta)\) to the rank-one operator \(|\Phi_z\rangle\langle\Phi_z|\) is smooth in trace norm near \(u=2\), integration over a thin radial annulus gives
\[
H_{\Omega_\varepsilon}=H_D+\varepsilon K_b+O_1(\varepsilon^2),\qquad
K_b=\frac1{2\pi}\int_0^{2\pi}b(\theta)
|\Phi_{(\sqrt{2/\pi},\theta)}\rangle\langle\Phi_{(\sqrt{2/\pi},\theta)}|\,d\theta.
\]
Here \(O_1\) denotes trace norm. In particular it is also an operator-norm expansion.

**3. The quadrupolar compression.** Let \(\Pi\) be the orthogonal projection onto \(\operatorname{span}\{h_0,h_1,h_2\}\). The standard Hermite STFT formula on the circle \(u=2\) gives, modulo a common phase and fixed unimodular basis phases,
\[
V_{h_2}h_0=\sqrt2 e^{-1}e^{\pm 2i\theta},\qquad
V_{h_2}h_1=0,\qquad
V_{h_2}h_2=-e^{-1}.
\]
Because \(\widehat b(0)=0\), the diagonal of \(\Pi K_b\Pi\) vanishes. All entries touching \(h_1\) vanish as well. The only possibly nonzero entries connect \(h_0\) and \(h_2\) and have magnitude \(\sqrt2e^{-2}|\widehat b(2)|\). Thus its eigenvalues are
\[
-\sqrt2e^{-2}|\widehat b(2)|,\quad0,\quad
+\sqrt2e^{-2}|\widehat b(2)|.
\]
The isolated top eigenvalue of the unperturbed compact operator has finite multiplicity three and a positive gap. The usual self-adjoint spectral-subspace perturbation estimate, or a block-Schur complement with the uniform complementary inverse bounded by the reciprocal gap, implies that the three eigenvalues near the top are \(\lambda_*+\varepsilon\mu_j+O(\varepsilon^2)\), where \(\mu_j\) are exactly these three compressed eigenvalues. Maximizing over them gives the asserted absolute-value cusp for both signs of \(\varepsilon\).

**4. Equal-area ellipses.** The ellipse has area \(\pi(\sqrt{2/\pi}e^{\varepsilon/2})(\sqrt{2/\pi}e^{-\varepsilon/2})=2\). Its polar boundary is
\[
R_\varepsilon(\theta)=\frac{2}{e^{-\varepsilon}\cos^2\theta+e^{\varepsilon}\sin^2\theta}
=2+2\varepsilon\cos(2\theta)+O(\varepsilon^2).
\]
Hence \(b(\theta)=2\cos(2\theta)\) and \(|\widehat b(2)|=1\). The linear gain is strictly positive, proving local instability. \(\square\)

## Verification
The standalone symbolic checker `CHECK.py` recalculates the three disk eigenvalues, verifies the Laguerre tail recurrence for indices \(3\le m\le25\), checks the boundary Fourier coefficient of the exact-area ellipse, and diagonalizes the compressed first-variation matrix. These finite exact checks corroborate, but do not replace, the all-index polynomial identity and the operator perturbation argument proved above. The linear coefficient is \(\sqrt2e^{-2}=0.1913929930208\ldots\).

## Relationship to prior work
Abreu–Gröchenig [1] gives the Hermite-window transform and Laguerre framework; it does not derive this area-two triple spectral crossing or the optimal-norm shape variation. Abreu–Gröchenig–Romero [2] formulates general concentration operators and derives asymptotic eigenvalue-distribution results for arbitrary windows; its inspected results do not give the claimed fixed-radius first variation. Abreu–Dörfler [3] treats an inverse localization problem with the *Gaussian* window. Nicola–Tilli [4] proves disk optimality for the *Gaussian* analysis window, so that theorem neither covers nor contradicts this result for \(h_2\). This claim is not an extension of a first-Hermite disk eigenvalue computation, because it relies on the three-way degeneracy and its nonzero off-diagonal boundary matrix at a different radius. Prior-equivalence risk remains for implicit higher-Landau-level shape calculations.

## Limitations
Only the stated second Hermite analysis window, area-two disk, and local smooth area-preserving perturbations are treated. No uniqueness or existence result for a global optimal set at area two is claimed. The proof is mathematical, not an independent external audit. An implicit equivalent statement in broader work on higher-Landau-level Toeplitz shape optimization remains possible.

## References
[1] L. D. Abreu and K. Gröchenig, *Banach Gabor frames with Hermite functions: polyanalytic spaces from the Heisenberg group*, arXiv:1012.4283v1 (first public: 2010-12-20), especially §2 and Eq. (2.4), https://arxiv.org/pdf/1012.4283.

[2] L. D. Abreu, K. Gröchenig, and J. L. Romero, *On accumulated spectrograms*, arXiv:1404.7713 (first public: 2014-04-30), §1, https://arxiv.org/pdf/1404.7713.

[3] L. D. Abreu and M. Dörfler, *An inverse problem for localization operators*, arXiv:1202.5841 (first public: 2012-02-27), §§1–2, https://arxiv.org/pdf/1202.5841.

[4] F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423 (first public: 2021), Theorem 1.1, https://arxiv.org/pdf/2106.03423.
