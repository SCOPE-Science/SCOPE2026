# Sharp Gaussian inverse-moment thresholds for two monomial excitation features

## Finding
Let \(m,d\) be integers at least \(2\). For independent real standard Gaussians \(G_1,\ldots,G_m\), define the \(2\times m\) nonlinear feature matrix
\[
V_{m,d}=\begin{pmatrix}G_1&\cdots&G_m\\G_1^d&\cdots&G_m^d\end{pmatrix}.
\]
Write \(S_{m,d}=\sigma_{\min}(V_{m,d})\) and \(\kappa_{m,d}=\kappa_2(V_{m,d})\). The matrix has full row rank almost surely. For every real \(p>0\),
\[
\mathbb E S_{m,d}^{-p}<\infty\quad\Longleftrightarrow\quad p<m/d,
\qquad
\mathbb E\kappa_{m,d}^{p}<\infty\quad\Longleftrightarrow\quad p<\min\{m/(d-1),m-1\}.
\]
In particular, the mean spectral norm of the Moore–Penrose pseudoinverse is finite exactly when \(m>d\), despite almost-sure full rank at every \(m\ge2\).

For all \((m,d)\ne(2,2)\), there is an explicit strictly positive finite constant \(C_{m,d}\) such that
\[
\Pr\{S_{m,d}\le t\}=C_{m,d}t^{m/d}+o(t^{m/d})\qquad(t\downarrow0).
\]
Writing \(\omega^{\circ d}=(\omega_1^d,\ldots,\omega_m^d)\), \(F_d(\omega)=\|(I-\omega\omega^{\mathsf T})\omega^{\circ d}\|_2\), and denoting surface measure on \(S^{m-1}\) by \(d\omega\), the constant is
\[
C_{m,d}=\frac{1}{m(2\pi)^{m/2}}\int_{S^{m-1}}F_d(\omega)^{-m/d}\,d\omega.
\]
The exceptional quadratic two-observation case has the sharp logarithmic transition
\[
\Pr\{S_{2,2}\le t\}\sim\frac{2+\sqrt2}{\pi}\,t\log(1/t).
\]

## Assumptions and scope
All Gaussian observations are independent \(N(0,1)\), no centering/normalization of the power features is applied, and all singular values are Euclidean. Integers \(m,d\ge2\) are fixed as \(t\downarrow0\); no dimension-uniform estimate is asserted. The sampling rows represent the two nonlinear functions \(u\mapsto u\) and \(u\mapsto u^d\), giving the order-one feature-excitation block used in a two-basis Hammerstein identification problem, not a time-lag Hankel matrix.

## Proof
**1. Exact singular-product reduction.** Write the Gaussian vector as \(G=R\omega\), where \(R>0\) has the \(\chi_m\) distribution and \(\omega\) is independent uniform surface measure on \(S^{m-1}\). Let \(b=\omega^{\circ d}\) and \(F=F_d(\omega)\). The two nonzero singular values obey
\[
\sigma_{\max}\sigma_{\min}=R^{d+1}F,
\quad R^2\le\sigma_{\max}^2\le R^2+R^{2d}.
\]
For \(0<R\le1\), consequently,
\[
R^dF/\sqrt2\le\sigma_{\min}\le R^dF,
\quad\sigma_{\min}=R^dF\bigl(1+O(R^{2d-2})\bigr),
\]
where the final error is uniform over \(\omega\) wherever \(F>0\). For \(R\ge1\), \(\sigma_{\min}\ge RF/\sqrt2\). The singular-product identity also follows from the Cauchy–Binet sum \(\det(VV^{\mathsf T})=\sum_{i<j}(G_iG_j^d-G_jG_i^d)^2\).

**2. Sharp angular integrability.** The condition \(F_d(\omega)=0\) says that \(\omega_i^d=a\omega_i\) for all coordinates, where \(a=\sum_i\omega_i^{d+1}\). Thus all nonzero coordinates have equal magnitude for odd \(d\) and the same signed value for even \(d\); there are only finitely many points on the unit sphere. At every such point \(a\ne0\). For a tangent vector \(v\perp\omega\), differentiate \(b-a\omega\): its tangent linearization is diagonal, with entries \((d-1)a\) on the nonzero coordinate support and \(-a\) off it. Indeed the derivative of \(a\) along any tangent vector at a zero vanishes. This linear map is invertible on the tangent space. Hence the angular zeros are simple and
\[
\Pr_{\omega}\{F_d(\omega)\le s\}=\Theta(s^{m-1}),
\qquad \mathbb E_{\omega}F_d(\omega)^{-p}<\infty\iff p<m-1.
\]
Thus \(V_{m,d}\) is full row rank almost surely. Since \(m/d<m-1\) for all \(m,d\ge2\) other than \((2,2)\), the angular negative moment required for the constant is finite.

**3. Radial asymptotics and inverse moments.** The density of \(R\) is \(c_mr^{m-1}e^{-r^2/2}\), where \(c_m=1/(2^{m/2-1}\Gamma(m/2))\). As \(s\downarrow0\), \(\Pr\{R\le s\}\sim s^m/(2^{m/2}\Gamma(m/2+1))\). For fixed \(\omega\) with \(F>0\), the small-\(R\) expansion from Step 1 gives
\[
\lim_{t\downarrow0}t^{-m/d}\Pr\{\sigma_{\min}\le t\mid\omega\}=\frac{F^{-m/d}}{2^{m/2}\Gamma(m/2+1)}.
\]
The two-sided radial estimates in Step 1 give a dominating multiple of \(F^{-m/d}\) (split at \(R=1\)); dominated convergence and \(|S^{m-1}|=2\pi^{m/2}/\Gamma(m/2)\) yield the stated \(C_{m,d}\). For negative moments, \(\sigma_{\min}\asymp R^dF\) for \(R\le1\) and \(\sigma_{\min}\gtrsim RF\) for \(R\ge1\); the lower and upper bounds combine with the independent radial and angular factors to give the exact cutoff \(p<m/d\), with divergence at equality. Furthermore, \(\kappa=\sigma_{\max}^2/(R^{d+1}F)\), so
\[
\kappa\asymp R^{1-d}F^{-1}\quad(0<R\le1),
\qquad\kappa\asymp R^{d-1}F^{-1}\quad(R\ge1).
\]
Every positive power of \(R\) is integrable at infinity; radial integration at zero and the angular result give the claimed condition-number cutoff.

**4. The logarithmic endpoint.** If \(m=d=2\), parameterize \(\omega=(\cos\theta,\sin\theta)\). Then
\[
F_2(\omega)=|\cos\theta\sin\theta(\sin\theta-\cos\theta)|.
\]
It has six simple zeros: four with local slope \(1\), and two with local slope \(1/\sqrt2\). Therefore
\[
\Pr_\omega\{F_2\le s\}\sim\frac{4+2\sqrt2}{\pi}s.
\]
The \(\chi_2\) radial density is \(re^{-r^2/2}\). On small positive radii \(\sigma_{\min}=R^2F_2(1+O(R^2))\) uniformly; integrating the angular estimate over \(\sqrt t\ll R\ll1\) produces \((4+2\sqrt2)/(2\pi)\,t\log(1/t)\). The regions \(R=O(\sqrt t)\) and \(R\gtrsim1\), together with fixed transition annuli, contribute only \(O(t)\) after standard cutoffs; sending both cutoffs to their limits establishes the exact stated coefficient. The inverse-moment threshold in Step 3 still applies, with divergence at \(p=1\).

## Verification
The included standard-library program `verify.py` checks the Cauchy–Binet determinant identity in 1,302 randomized exact-rational cases, checks the six exceptional angular-root slopes at 18 scales, and rederives the exceptional leading coefficient. It prints `VERIFY_OK` on success. These computations do not establish the probability laws; the proof above supplies the infinite-dimensional quantifiers for each fixed \(m,d\).

## Relationship to prior work
Alsalti–Lopez–Müller (2023), arXiv:2303.08707, Section IV, develops deterministic persistent-excitation input designs for Hammerstein systems through rank conditions on nonlinear feature blocks. Coulson–van Waarde–Dörfler (2022), arXiv:2205.06636, studies quantitative excitation through singular values in data-driven control. Neither inspected source states the present exact Gaussian two-feature hard-edge law or its inverse-moment cutoff. Independent-column small-singular-value estimates such as Koltchinskii–Mendelson (2013) address broader nonasymptotic bounds but do not give this polynomial-curve exact constant. Results for Fourier Vandermonde matrices with clustered unit-circle nodes (Kunis–Nagel, 2019) are for a distinct geometry. The present result is an order-one random feature calculation, not a general Hammerstein closed-loop control theorem.

## Limitations
Only the exact real Gaussian order-one two-monomial block and its unnormalized spectral singular values are classified. General nonlinear bases, sample autocorrelation, higher-order Hankel blocks, other noise laws, and closed-loop identification errors are not covered. The probability constant is an explicit finite sphere integral rather than an elementary closed form in general. An equivalent earlier result on Gaussian power-Vandermonde or structured random-regressor inverse moments cannot be excluded without further independent literature examination.

## References
- M. Alsalti, V. G. Lopez, M. A. Müller, *On the design of persistently exciting inputs for data-driven control of linear and nonlinear systems*, arXiv:2303.08707 (first public version 2023-03-15); https://arxiv.org/abs/2303.08707.
- J. Coulson, H. J. van Waarde, F. Dörfler, *Robust Fundamental Lemma for Data-driven Control*, arXiv:2205.06636; https://arxiv.org/abs/2205.06636.
- V. Koltchinskii, S. Mendelson, *Bounding the Smallest Singular Value of a Random Matrix Without Concentration*, arXiv:1312.3580; https://arxiv.org/abs/1312.3580.
- S. Kunis, D. Nagel, *On the smallest singular value of multivariate Vandermonde matrices with clustered nodes*, arXiv:1907.07119; https://arxiv.org/abs/1907.07119.
