# A universal reflectionless boundary layer in hybrid quantum-graph vertex scattering
## Finding
For the rotationally symmetric star-vertex family introduced by Exner, Turek, and Tater, the singular corner in which the interpolation approaches the \(\delta\) endpoint while the energy grows has an exact universal scattering profile.

Fix an integer \(n\ge3\) and \(\alpha\in\mathbb R\). Let \(t\in[0,1]\) be the interpolation parameter and \(k=\sqrt E>0\) the on-shell momentum, with the normalization of arXiv:1804.01414. If
\[
t\to0^+,\qquad k\to\infty,\qquad kt\to\xi\in(0,\infty),
\]
then
\[
S_n(k,t)\longrightarrow S_n^{\mathrm{bl}}(\xi)
 =\frac1nF\,\operatorname{diag}\!\bigl(\nu_0(\xi),\ldots,\nu_{n-1}(\xi)\bigr)F^*,
\]
where \(F\) is the discrete Fourier matrix used in the source,
\[
\nu_0(\xi)=1,\qquad
\beta_j=\pi\left(\frac{2j}n-1\right),\qquad
\nu_j(\xi)=\frac{\beta_j\xi-2i}{\beta_j\xi+2i}\quad(1\le j\le n-1).
\]
The limiting matrix is independent of the \(\delta\)-strength \(\alpha\).

Because the matrix is circulant, all diagonal scattering amplitudes coincide. Write that common reflection amplitude as \(r_n(\xi)\). Pairing the Fourier modes \(j\) and \(n-j\) gives, for odd \(n\),
\[
r_n(\xi)=\frac1n\left[1+2\sum_{j=1}^{(n-1)/2}
\frac{\beta_j^2\xi^2-4}{\beta_j^2\xi^2+4}\right],
\]
and for even \(n\),
\[
r_n(\xi)=\frac2n\sum_{j=1}^{n/2-1}
\frac{\beta_j^2\xi^2-4}{\beta_j^2\xi^2+4}.
\]
Every summand is strictly increasing on \((0,\infty)\). Moreover
\[
r_n(0^+)=-\frac{n-2}n,
\]
while \(r_n(\infty)=1\) for odd \(n\) and \(r_n(\infty)=(n-2)/n\) for even \(n\). Consequently there is a unique \(\xi_n>0\) such that \(r_n(\xi_n)=0\). Since \(S_n^{\mathrm{bl}}(\xi)\) is unitary, the total transmission probability from any incoming edge is
\[
T_n(\xi)=1-|r_n(\xi)|^2,
\]
so \(T_n(\xi_n)=1\). Thus the singular crossover contains one universal asymptotically reflectionless point for every vertex degree \(n\ge3\). The first two are
\[
\xi_3=\frac{2\sqrt3}\pi,\qquad \xi_4=\frac4\pi.
\]

## Assumptions and scope
The claim concerns a single star vertex with the self-adjoint matching condition and the one-parameter unitary circulant family \(U(t)\) of arXiv:1804.01414. The integer \(n\ge3\) and real parameter \(\alpha\) are fixed. The scaling variable \(\xi\) is finite and positive; no uniform assertion is made simultaneously in \(n\), \(\alpha\), or \(\xi\) up to both endpoints.

"Reflectionless" means that the diagonal of the limiting on-shell scattering matrix vanishes. It does not assert equal transmission probabilities among the \(n-1\) outgoing edges.

## Proof
The source diagonalizes the interpolation family by the same discrete Fourier basis for every \(t\). Its eigenvalues are
\[
\lambda_0(t)=e^{-i(1-t)\gamma},\qquad
\lambda_j(t)=-e^{i\beta_j t}\quad(1\le j\le n-1),
\]
with \(\gamma\in(-\pi,\pi)\) determined by \(\alpha\). For a unitary eigenvalue \(\lambda\), the source's on-shell scattering formula gives
\[
\mu(k,\lambda)=\frac{k-1+(k+1)\lambda}{k+1+(k-1)\lambda}.
\]
If \(\lambda=e^{i\phi}\), elementary half-angle algebra rewrites this exactly as
\[
\mu(k,e^{i\phi})=
\frac{k+i\tan(\phi/2)}{k-i\tan(\phi/2)}.
\]
For \(j\ge1\), take \(\phi=\pi+\beta_j t\). Then
\[
\mu_j(k,t)=
\frac{k-i\cot(\beta_jt/2)}{k+i\cot(\beta_jt/2)}.
\]
When \(\beta_j=0\), which happens only for even \(n\) and \(j=n/2\), both the source formula and the displayed limiting formula give \(-1\). Otherwise, using
\[
\cot(\beta_jt/2)=\frac2{\beta_jt}+O(t)
\]
and \(kt\to\xi\) yields
\[
\mu_j(k,t)\longrightarrow
\frac{\beta_j\xi-2i}{\beta_j\xi+2i}.
\]
For \(j=0\), the phase \(-(1-t)\gamma\) stays strictly away from the singular phase \(\pi\) for fixed finite \(\alpha\), so its half-angle tangent remains bounded and \(\mu_0(k,t)\to1\). Fourier reconstruction proves the matrix limit.

The endpoints expose a noncommuting-limit boundary layer. At \(\xi\downarrow0\), every \(\nu_j\) with \(j\ge1\) tends to \(-1\), hence
\[
S_n^{\mathrm{bl}}(0^+)=\frac1nF\,\operatorname{diag}(1,-1,\ldots,-1)F^*=\frac2nJ-I,
\]
which is the high-energy scattering matrix of the \(\delta\) endpoint. At \(\xi\to\infty\), all nonzero \(\beta_j\) modes tend to \(1\), while the even-degree mode \(\beta_{n/2}=0\) remains \(-1\). Thus the endpoint is \(I\) for odd \(n\), and for even \(n\) it is precisely the parity-dependent matrix given by formula (23) of the source. These two iterated limits differ for every \(n\ge3\).

Finally, \(\beta_{n-j}=-\beta_j\), so paired eigenvalues are conjugate and the diagonal amplitude is real. For every \(\beta_j\ne0\),
\[
\frac{d}{d\xi}\frac{\beta_j^2\xi^2-4}{\beta_j^2\xi^2+4}
=\frac{16\beta_j^2\xi}{(\beta_j^2\xi^2+4)^2}>0.
\]
The displayed endpoint values therefore force exactly one zero of \(r_n\). Unitarity then gives total transmission one at that zero. Solving the one-term equations gives \(\xi_3=2\sqrt3/\pi\) and \(\xi_4=4/\pi\).

## Verification
The accompanying `verify.py` separately evaluates the exact finite-\(k,t\) source eigenvalue formula, checks convergence to the boundary-layer eigenvalues along several sequences, verifies the closed forms for \(r_n\), checks monotonicity numerically for representative degrees, and verifies the exact \(n=3\) and \(n=4\) reflectionless scales. These finite computations corroborate the algebra; the proof of the limit and uniqueness is analytic and does not depend on numerical sampling.

## Relationship to prior work
Exner--Turek--Tater derive the interpolation eigenvalues, the general on-shell scattering formula, and the fixed-\(t\) high-energy parity dichotomy. They do not state the singular double scaling \(kt\to\xi\), the resulting universal matrix profile, the noncommutation of the \(t\downarrow0\) and \(k\to\infty\) limits, or the unique reflectionless crossover.

Kurasov--Ogik--Rauf study reflectionless equi-transmitting matrices and general high-energy scattering limits for star-graph matching conditions. Their classification concerns energy-independent/Hermitian equi-transmitting structures and does not identify this one-parameter boundary layer in the Exner--Turek--Tater interpolation family. The 2024 Exner--Pekař paper reuses the same interpolation eigenvalues for periodic chain graphs and studies spectral bands, including their high-energy behavior, but does not analyze this star-vertex scattering crossover.

Searches over the source title, preferred-orientation terminology, reflectionless/equi-transmitting terminology, the scale \(t\sqrt E\), and equivalent statements about noncommuting high-energy/interpolation limits found no published statement covering this result.

## Limitations
The result is a vertex-scattering statement. It does not by itself imply a corresponding reflectionless theorem for a periodic or finite graph assembled from such vertices, where propagation phases and multiple scattering matter. The crossover is asymptotic: it asserts zero limiting reflection along \(kt\to\xi_n\), not an exact zero of the finite-\(k,t\) reflection amplitude for arbitrary \(\alpha\).

A residual bibliographic risk is that the same boundary-layer calculation may occur in literature using a different parametrization of the unitary matching matrix or under singular-perturbation terminology not captured by the searches.

## References
1. P. Exner, O. Turek, M. Tater, *A family of quantum graph vertex couplings interpolating between different symmetries*, arXiv:1804.01414v1 (2018); J. Phys. A: Math. Theor. 51 (2018) 285301; doi:10.1088/1751-8121/aac651.
2. P. Exner, M. Tater, *Quantum graphs with vertices of a preferred orientation*, arXiv:1710.02664 (2017); Phys. Lett. A 382 (2018) 283--287.
3. P. Kurasov, R. Ogik, A. Rauf, *On reflectionless equi-transmitting matrices*, Opuscula Math. 34 (2014) 483--501; doi:10.7494/OpMath.2014.34.3.483.
4. P. Exner, J. Pekař, *Vertex coupling interpolation in quantum chain graphs*, arXiv:2403.09457v1 (2024); J. Math. Phys. 65 (2024) 092102; doi:10.1063/5.0208361.
