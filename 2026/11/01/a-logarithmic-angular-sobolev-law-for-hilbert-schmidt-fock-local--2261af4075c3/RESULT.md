# A logarithmic angular-Sobolev law for Hilbert–Schmidt Fock localization

## Finding
Let \(\mathcal F^2\) be the analytic Bargmann–Fock space with norm \(\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\), and let \(P\) be the orthogonal projection. For \(R>0\) and \(A\in L^2(\mathbb T)\), with normalized Fourier coefficients \(a_k=(2\pi)^{-1}\int_0^{2\pi} A(\theta)e^{-ik\theta}\,d\theta\), put
\[
\sigma_{R,A}(re^{i\theta})=\mathbf1_{\{r<R\}}A(\theta),\qquad L_{R,A}=P M_{\sigma_{R,A}}\vert_{\mathcal F^2}.
\]
The compactly supported \(L^2\) symbol defines a Hilbert–Schmidt Toeplitz operator via its densely defined sesquilinear form and Hilbert–Schmidt extension. Write \(L_R=L_{R,1}\) and \(\|A\|_{2,\mathbb T}^2=(2\pi)^{-1}\int |A|^2\). Then the nonnegative deficit has the exact extended-real logarithmic limit
\[
\boxed{\lim_{R\to\infty}\frac{\|A\|_{2,\mathbb T}^2\|L_R\|_{\mathcal S_2}^2-\|L_{R,A}\|_{\mathcal S_2}^2}{\log R}=\frac12\sum_{k\in\mathbb Z}k^2|a_k|^2\in[0,+\infty].}
\]
Thus the limit is finite if and only if \(A\in H^1(\mathbb T)\). In particular, a phase vortex \(A(\theta)=e^{ik\theta}\) has sharp deficit \((k^2/2)\log R+O_k(1)\), for every nonzero integer \(k\).

## Assumptions and scope
The Gaussian and disk-radius normalization above are fixed throughout. The angular profile is an arbitrary complex-valued \(L^2(\mathbb T)\) equivalence class, not necessarily bounded or unimodular. Toeplitz operators for unbounded \(A\) are defined by extension from polynomial matrix elements; compact support and the Gaussian kernel make this extension Hilbert–Schmidt. The asymptotic variable is the Euclidean radius \(R\to\infty\), not the disk area. The term \(\log R\) therefore has coefficient one half of the angular Sobolev energy.

## Proof
**1. The Hilbert–Schmidt formula and angular diagonalization.** The reproducing kernel is \(K(z,w)=e^{z\bar w}\). For every compactly supported \(\sigma\in L^2(\mathbb C)\), polynomial-density approximation gives
\[
\|T_\sigma\|_{\mathcal S_2}^2=\frac1{\pi^2}\iint_{\mathbb C^2}\overline{\sigma(z)}\sigma(w)e^{-|z-w|^2}\,dA(z)dA(w).
\]
The identity holds first for bounded \(\sigma\), by a trace calculation using the kernel, then for \(L^2\) symbols because Gaussian convolution is a bounded positive operator on \(L^2\) and because the coefficient forms converge. Rotating both variables proves that distinct Fourier modes of \(A\) yield Hilbert–Schmidt-orthogonal Toeplitz operators. Put \(S_k(R)=\|L_{R,e^{ik\theta}}\|_{\mathcal S_2}^2\) (\(S_{-k}=S_k\)). Then
\[
\|L_{R,A}\|_{\mathcal S_2}^2=\sum_{k\in\mathbb Z}|a_k|^2S_k(R),\qquad D_k(R):=S_0(R)-S_k(R)\ge0.
\]
Indeed
\[
D_k(R)=\frac1{\pi^2}\iint_{|z|,|w|<R}e^{-|z-w|^2}\bigl(1-\cos(k(\arg w-\arg z))\bigr)\,dA(z)dA(w),
\]
which is manifestly nonnegative. The elementary inequality \(1-\cos(k\phi)\le k^2(1-\cos\phi)\) gives \(0\le D_k(R)\le k^2D_1(R)\) for every integer \(k\) and \(R\).

**2. Exact monomial singular values.** Let \(e_n(z)=z^n/\sqrt{n!}\). For \(k\ge0\), the angular Toeplitz operator shifts \(e_n\) to the \(e_{n+k}\) direction with positive coefficient
\[
 w_{n,k}(x)=\frac{\gamma(n+1+k/2,x)}{\sqrt{\Gamma(n+1)\Gamma(n+k+1)}},\quad x=R^2.
\]
Here \(\gamma(s,x)=\int_0^x t^{s-1}e^{-t}\,dt\) and \(Q_s(x)=\gamma(s,x)/\Gamma(s)\). Consequently
\[
S_k(R)=\sum_{n=0}^\infty b_{n,k}^2Q_{n+1+k/2}(x)^2,\quad b_{n,k}^2=\frac{\Gamma(n+1+k/2)^2}{\Gamma(n+1)\Gamma(n+k+1)},
\]
while \(S_0(R)=\sum_{n\ge0}Q_{n+1}(x)^2\). All displayed series converge: the incomplete gamma factors decay superexponentially as \(n\to\infty\) for fixed \(x\).

**3. The logarithmic coefficient.** The gamma shape distribution increases stochastically with its shape. Thus, for fixed nonnegative integer \(k\),
\[
0\le\sum_{n\ge0}\bigl(Q_{n+1}(x)^2-Q_{n+1+k/2}(x)^2\bigr)\le\sum_{n\ge0}\bigl(Q_{n+1}(x)^2-Q_{n+k+1}(x)^2\bigr)\le k.
\]
The last series telescopes exactly to \(\sum_{n=0}^{k-1}Q_{n+1}(x)^2\). By the classical fixed-shift asymptotic for gamma ratios (or two applications of Stirling's expansion),
\[
1-b_{n,k}^2=\frac{k^2}{4n}+O_k(n^{-2})\quad(n\to\infty).
\]
Also, for every fixed \(c>0\),
\[
\sum_{n\ge1}\frac{Q_{n+c}(x)^2}{n}=\log x+O_c(1)\qquad(x\to\infty).
\]
For completeness, split at \(x/2\) and \(2x\): gamma Chernoff bounds give \(Q_{n+c}(x)=1+O(e^{-\delta x})\) uniformly below \(x/2\) and \(Q_{n+c}(x)=O(e^{-\delta n})\) uniformly above \(2x\), with appropriate fixed positive \(\delta\). The middle interval contributes at most \(\sum_{x/2<n<2x}1/n=O(1)\); the lower interval gives \(\log x+O(1)\). Substituting into the two nonnegative pieces of \(S_0-S_k\) proves
\[
D_k(R)=\frac{k^2}{4}\log(R^2)+O_k(1)=\frac{k^2}{2}\log R+O_k(1).
\]
This includes \(k=0\), for which \(D_0=0\).

**4. All angular profiles, including the infinite limit.** Fourier-mode orthogonality gives
\[
\|A\|_{2,\mathbb T}^2 S_0(R)-\|L_{R,A}\|_{\mathcal S_2}^2=\sum_k|a_k|^2D_k(R).
\]
For fixed \(k\), \(D_k(R)/\log R\to k^2/2\). If \(\sum k^2|a_k|^2<\infty\), domination by \(k^2D_1(R)/\log R\), whose scalar factor is bounded for sufficiently large \(R\), yields the claimed limit by dominated convergence. Otherwise the nonnegative-series Fatou lemma gives limit inferior \(+\infty\), and therefore the limit is infinite. This proves the claimed if-and-only-if sharp Sobolev threshold.

## Verification
The standalone `checker.py` evaluates exact gamma-function shift coefficients, checks direct quadratures, and compares the logarithmic deficit increments over three radius scales for four angular charges. It passed 26 supplementary numerical assertions on the actual packaged code path. These finite computations are not used to establish the infinite-dimensional limit, which is proved above.

## Relationship to prior work
Kisil's Fock–Segal–Bargmann cross-Toeplitz calculus (arXiv:2108.13710, 2021) develops the coherent-state and convolutional operator framework, but does not state the present disk-growing, angular-Sobolev logarithmic Hilbert–Schmidt law. Galbis (arXiv:2102.02031, 2021) studies Fock Toeplitz norm bounds for bounded *radial selfadjoint* symbols, and thus does not determine the charge-dependent Schatten deficit. Rodriguez Rodriguez (arXiv:2206.11557, 2022) treats quasi-radial/pseudo-homogeneous symbols on *ball Bergman spaces* and their operator algebras; the logarithmic Fock disk defect is a separate statement. The Gaussian Hilbert–Schmidt identity itself is standard and is not claimed as new. Related angular Sobolev logarithmic leakage results in harmonic Fock-type spaces do not imply the analytic Fock Schatten comparison, although they signal a related regularity mechanism.

## Limitations
The result is a self-review mathematical proof and supplementary computation, not an independent review. Historical priority is provisional: general nonlocal quadratic-form or Toeplitz semiclassical asymptotic theorems might imply the logarithmic law indirectly. It applies to concentric *Euclidean disks*, the Gaussian analytic Fock space, and angular profiles independent of radius. It does not prove analogous sharp coefficients for arbitrary localization domains, higher-dimensional vortices, or general radial weights. The logarithmic law is not a bound on the operator norm and does not assert a quantitative rate for arbitrary \(L^2\) angular profiles.

## References
- V. V. Kisil, *Cross-Toeplitz Operators on the Fock–Segal–Bargmann Spaces and Two-Sided Convolutions on the Heisenberg Group*, arXiv:2108.13710 (first posted 2021-08-31), https://arxiv.org/abs/2108.13710.
- A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (2021), https://arxiv.org/abs/2102.02031.
- M. A. Rodriguez Rodriguez, *Commutative Banach Algebras Generated by Toeplitz Operators on the Bergman Space*, arXiv:2206.11557 (2022), https://arxiv.org/abs/2206.11557.
- V. Dewage and G. Ólafsson, *Toeplitz Operators on the Fock Space with Quasi-Radial Symbols*, Complex Anal. Oper. Theory 16 (2022), doi:10.1007/s11785-022-01208-9.
