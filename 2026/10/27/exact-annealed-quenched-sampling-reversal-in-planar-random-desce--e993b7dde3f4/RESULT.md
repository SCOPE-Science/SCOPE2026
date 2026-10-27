# Exact annealed–quenched sampling reversal in planar random descent

## Finding

Consider exact-line-search random descent for a consistent real least-squares system with two unknowns. At each iteration draw a fresh sketch direction either from the standard two-dimensional Gaussian law or from independent fair signs. The two choices can be ordered in opposite ways by **typical-path** versus **expected squared-residual** convergence, despite both algorithms converging geometrically.

Let the Gram eigenvalues be \(\lambda_1>\lambda_2>0\), with its first eigenvector at angle \(\theta\) to the sketch-coordinate axis. Define
\[
q=\frac{\sqrt{\lambda_1}-\sqrt{\lambda_2}}{\sqrt{\lambda_1}+\sqrt{\lambda_2}}\in(0,1),\qquad
u=|\cos(2\theta)|\in[0,1],\qquad
r=\frac{2qu}{\sqrt{(1-q^2)^2+4q^2u^2}}.
\]
For every deterministic nonzero starting error outside the stated exceptional sign directions, the almost-sure per-iteration geometric factors for **squared residual** are
\[
G_{\mathrm{a.s.}}=\left(\frac{1+q^2}{2}\right)^2,
\qquad S_{\mathrm{a.s.}}=r,
\]
whereas the asymptotic per-iteration factors of **expected squared residual** are
\[
G_{\mathrm{mean}}=\frac{3+q^2+\sqrt{1+14q^2+q^4}}8,
\qquad S_{\mathrm{mean}}=\frac{1+r^2}{2}.
\]
Here \(G\) denotes Gaussian sketches and \(S\) denotes fair independent-sign sketches. At \(r=0\), sign descent terminates in finitely many steps almost surely and its almost-sure factor is defined to be zero.

There is exactly one \(q_*\in(0,1)\) satisfying
\[
q_*^5+q_*^4+4q_*^3+4q_*^2+7q_*-1=0,
\qquad q_*=0.131608446856607\ldots.
\]
For every \(0<q<q_*\), sign descent is almost-surely faster for **every** angle, but Gaussian descent has the better asymptotic expected squared-residual rate for all
\[
u>u_{\mathrm{mean}}(q)=\frac{1-q^2}{2q}
\sqrt{\frac{2G_{\mathrm{mean}}-1}{2(1-G_{\mathrm{mean}})}}.
\]
For each \(q\in(0,1)\), this angular boundary belongs strictly to \((0,1)\). Equivalently, the all-angle typical-path advantage occurs when the spectral condition ratio obeys
\[
1<\lambda_1/\lambda_2<\left(\frac{1+q_*}{1-q_*}\right)^2=1.69809186069316\ldots.
\]
For larger \(q\), the typical-path crossover is governed by
\[
u_{\mathrm{a.s.}}(q)=\frac{1-q^2}{2q}\frac{G_{\mathrm{a.s.}}}{\sqrt{1-G_{\mathrm{a.s.}}^2}};
\]
if this number lies below one, sign descent is typically faster exactly for \(u<u_{\mathrm{a.s.}}\). The expected-error ordering always changes at \(u=u_{\mathrm{mean}}\), sign being better below the boundary and Gaussian better above it.

For example, for Gram matrix \(\operatorname{diag}(121,81)\), the sign factors are \(20/101\) (almost surely) and \(10601/20402\) (in expectation), while the Gaussian factors are \(10201/40000\) and \((301+\sqrt{11401})/800\), respectively. Thus sign directions converge strictly faster on typical paths but strictly slower in mean squared residual.

## Assumptions and scope

Let \(A\in\mathbb R^{m\times2}\), \(m\ge2\), have full column rank; let \(b=Av_*\) be consistent. Independently at each \(k\ge0\), draw \(\xi_{k+1}\) either as \(N(0,I_2)\) or uniformly from \(\{(-1,-1),(-1,1),(1,-1),(1,1)\}\), and update
\[
v_{k+1}=v_k-\frac{\langle A(v_k-v_*),A\xi_{k+1}\rangle}{\|A\xi_{k+1}\|^2}\xi_{k+1}.
\]
The squared residual is \(E_k=\|A(v_k-v_*)\|^2\). For the Gaussian method and every fixed \(v_0\ne v_*\), \(\lim_{n\to\infty}E_n^{1/n}=G_{\mathrm{a.s.}}\) almost surely and \(\lim_{n\to\infty}(\mathbb E E_n)^{1/n}=G_{\mathrm{mean}}\). For the sign method, the second limit always equals \(S_{\mathrm{mean}}\). The almost-sure limit equals \(S_{\mathrm{a.s.}}\) provided \(r>0\) and the initial transformed error is not parallel to either transformed signed search line; this excludes exactly two one-dimensional initial-error subspaces. If \(r=0\), finite termination holds almost surely from every initialization. Exceptional sign initializations at \(r>0\) have a positive probability of termination on the first step, precluding a deterministic strictly positive almost-sure rate on all paths. All factors concern one-step *asymptotic* rates; the first-step magnitude may depend on the initial vector.

## Proof

**Rank-one residual projections.** Set \(H=A^{\mathsf T}A\succ0\), \(y_k=H^{1/2}(v_k-v_*)\), and \(g_k=H^{1/2}\xi_k\). The update becomes
\[
y_{k+1}=\left(I-\frac{g_{k+1}g_{k+1}^{\mathsf T}}{\|g_{k+1}\|^2}\right)y_k.
\]
The parenthesized matrix is the orthogonal projector onto the line perpendicular to \(g_{k+1}\). If \(\phi_k\) denotes the angle of \(g_k\) (its perpendicular line has the same relative angles), then, after the first update,
\[
E_n=E_1\prod_{j=2}^{n}\cos^2(\phi_j-\phi_{j-1}).
\]
This is a pathwise identity, including zero factors. In the Gaussian case, no factor vanishes with positive probability.

**Gaussian typical-path factor.** Orthogonal invariance permits diagonalizing \(H\). Writing its eigenvalues as \(a^2,b^2\) with \(a>b>0\), the direction angle of \(H^{1/2}\xi\) has Poisson-kernel density
\[
p_q(\phi)=\frac{1-q^2}{2\pi(1-2q\cos(2\phi)+q^2)},
\qquad q=\frac{a-b}{a+b}.
\]
The exact Fourier coefficients are \(\mathbb E[e^{2ij\phi}]=q^{|j|}\). For independent angles \(\phi,\psi\), the integrable Fourier series for \(\log\cos^2(\phi-\psi)\), interpreted by Abel damping and dominated logarithmic-integrability limits, gives
\[
\mathbb E\log\cos^2(\phi-\psi)
=-2\log2+2\sum_{j=1}^\infty\frac{(-1)^{j+1}q^{2j}}j
=2\log\frac{1+q^2}{2}.
\]
The consecutive log-factors form a stationary ergodic one-dependent sequence. Its strong law gives \(\lim n^{-1}\log E_n=2\log((1+q^2)/2)\), yielding \(G_{\mathrm{a.s.}}\).

**Gaussian expected-energy factor.** Let \(K\) be the positive transfer operator
\[
(Kf)(\phi)=\int_0^{2\pi}\cos^2(\phi-\psi)f(\psi)p_q(\psi)\,d\psi.
\]
It maps every function after one step to the span of \(1,\cos2\phi,\sin2\phi\). Relative to \(1,\cos2\phi\), its matrix is
\[
K_{1,c}=\begin{pmatrix}1/2&q/2\\q/2&(1+q^2)/4\end{pmatrix},
\]
and its remaining eigenvalue is \((1-q^2)/4\). The strictly dominant eigenvalue of this positive rank-three kernel is
\[
\rho(K)=\frac{3+q^2+\sqrt{1+14q^2+q^4}}8.
\]
The initial nonnegative energy weight is not identically zero under the angular density, and the positive principal eigenfunction implies a nonzero Perron coefficient. Thus the expectation has geometric rate \(\rho(K)\) for every nonzero deterministic starting vector.

**Signed-sketch factors.** Up to sign, there are only two possible search lines \(g_\pm=H^{1/2}(1,\pm1)^{\mathsf T}\). Their absolute cosine is
\[
\frac{|g_+^{\mathsf T}g_-|}{\|g_+\|\|g_-\|}
=\frac{|H_{11}-H_{22}|}{\sqrt{(H_{11}+H_{22})^2-4H_{12}^2}}
=\frac{2qu}{\sqrt{(1-q^2)^2+4q^2u^2}}=r.
\]
After the first projection, each subsequent signed line independently remains the same with probability \(1/2\), multiplying energy by one, or switches with probability \(1/2\), multiplying energy by \(r^2\). The switches are independent fair Bernoulli indicators. Hence
\[
E_n=E_1r^{2N_{n-1}},\qquad
N_{n-1}\sim\operatorname{Binomial}(n-1,1/2),
\]
with the first-step energy independent of subsequent switches. Consequently \(\mathbb E E_n=\mathbb E E_1((1+r^2)/2)^{n-1}\), and the Bernoulli strong law yields almost-sure squared-residual factor \(r\) whenever the first step is nonzero. For \(r=0\), almost-surely a switch eventually occurs and sets the residual to zero permanently.

**Sharp crossing geometry.** The signed factors are strictly increasing in \(u\), whereas both Gaussian factors are independent of \(u\). At \(u=0\), \(S_{\mathrm{mean}}=1/2<G_{\mathrm{mean}}\). At \(u=1\), let \(z=q^2\), and set \(N(z)=1+17z-z^2-z^3\). Direct calculation gives
\[
N(z)^2-(1+14z+z^2)(1+z)^4
=16z(1-z)(z^3+7z^2+15z+1)>0.
\]
Since \(N(z)>0\) for \(0<z<1\), this proves \(S_{\mathrm{mean}}(q,1)>G_{\mathrm{mean}}(q)\). The unique crossover follows by monotonicity and solving \(r^2=2G_{\mathrm{mean}}-1\).

The maximal signed typical factor is \(2q/(1+q^2)\). Equating it to the Gaussian typical factor yields
\[
(1+q^2)^3-8q=(q-1)(q^5+q^4+4q^3+4q^2+7q-1)=0.
\]
The quintic factor has strictly positive derivative for \(q\ge0\), changes sign once on \((0,1)\), and therefore gives the unique strict all-angle crossover \(q_*\). Solving \(r=G_{\mathrm{a.s.}}\) yields \(u_{\mathrm{a.s.}}\). This completes the phase diagram.

## Verification

Run `python3 verify.py` with SymPy installed. The standalone script checks the transfer-matrix characteristic polynomial, the two algebraic comparison identities, uniqueness-sign polynomial factorization, an exact rational reversal witness, Gaussian angular Fourier moments, and numerical agreement of the transfer-operator dominant eigenvalue for several anisotropies. It prints `VERIFY_OK: symbolic identities, exact conflict, Fourier moments, transfer eigenvalues` on success. Finite quadrature and numerical checks only corroborate the analytic proof; the infinite-time conclusions follow from the exact formulas and probability arguments above.

## Relationship to prior work

Lorenz, Schneppe and Tondji (2023), arXiv:2306.01946, define random descent for least squares, prove general distribution-dependent linear convergence bounds and compare Gaussian and Rademacher sampling experimentally. Those bounds do not state the exact two-dimensional almost-sure and mean-squared asymptotic rates or their opposite sampling orderings. Gower and Richtárik (2015), arXiv:1506.03296, develop the general sketch-and-project framework and expected convergence bounds, not the displayed exact phase diagram. Altschuler and Parrilo (2019), arXiv:1905.07531, establish a general ergodic formula for rank-one-matrix Lyapunov exponents and explicitly treat isotropic rank-one projections; that general formula supports the typical-path approach but does not supply the anisotropic Gaussian integration, expected-energy transfer spectrum, or the Gaussian-versus-sign crossover proved here. These are comparisons of mathematical implications, not assertions of a uniqueness proof. Unlocated equivalent special-purpose calculations remain possible.

## Limitations

The result assumes a consistent full-rank two-unknown least-squares system, exact arithmetic, independent directions and exact line search, and applies to squared residuals. The typical-path sign factor has stated exceptional initial-error subspaces with positive first-step finite-termination probability. The random-dimensional phenomenon does not automatically extend to higher-dimensional systems, finite-precision implementations, noisy/inconsistent data, stochastic line searches or different sketch distributions. Neither an iteration-cost claim nor a universal statistical efficiency ordering follows.

## References

1. D. A. Lorenz, F. Schneppe, L. Tondji, *Linearly convergent adjoint free solution of least squares problems by random descent*, arXiv:2306.01946 (first posted June 2, 2023), https://arxiv.org/abs/2306.01946.
2. J. M. Altschuler, P. A. Parrilo, *Lyapunov Exponent of Rank One Matrices: Ergodic Formula and Inapproximability of the Optimal Distribution*, arXiv:1905.07531, https://arxiv.org/abs/1905.07531.
3. R. M. Gower, P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296, https://arxiv.org/abs/1506.03296.
