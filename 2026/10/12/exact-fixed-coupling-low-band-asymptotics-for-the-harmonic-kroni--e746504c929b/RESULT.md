# Exact fixed-coupling low-band asymptotics for the harmonic Kronig–Penney model
## Finding
Consider
\[
\mathcal L_{a,\gamma}=-\frac{d^2}{dx^2}+[x^2-1]_{2a}+2\gamma\sum_{m\in\mathbb Z}\delta(x-(2m+1)a),
\]
with fixed \(\gamma\in\mathbb R\). For every fixed integer \(n\ge0\), there is, for all sufficiently large \(a\), a unique spectral band \(B_n(a,\gamma)\) converging to the harmonic-oscillator level \(2n\). Put
\[
C_n=\frac{2^{n+2}}{\sqrt\pi\,n!}.
\]
If \(E_n^D(a)\) is the edge obtained from the zero of the parity-matched Weber-Hermite function and \(E_n^R(a,\gamma)\) is the edge obtained from the corresponding Robin condition, then
\[
E_n^D(a)=2n+C_n a^{2n+1}e^{-a^2}\left(1+O(a^{-2})\right),
\]
\[
E_n^R(a,\gamma)=2n-C_n a^{2n+1}e^{-a^2}\left(1-\frac{2\gamma}{a}+O(a^{-2})\right).
\]
Hence, for fixed \((n,\gamma)\),
\[
|B_n(a,\gamma)|=\frac{2^{n+3}}{\sqrt\pi\,n!}a^{2n+1}e^{-a^2}\left(1-\frac{\gamma}{a}+O(a^{-2})\right),\qquad a\to\infty.
\]
In particular, the leading tunnelling constant is independent of the fixed delta strength \(\gamma\); the first dependence on \(\gamma\) appears at relative order \(a^{-1}\).

## Assumptions and scope
The integer \(n\) and the real coupling \(\gamma\) are fixed while \(a\to\infty\). The parity-matched solution is \(W_+\) for even \(n\) and \(W_-\) for odd \(n\). The result concerns only the low band converging to the fixed level \(2n\). The constants hidden in the error terms may depend on \((n,\gamma)\). No statement is made for \(n\) growing with \(a\), for \(\gamma\) growing with \(a\), or for high-energy bands.

## Proof
Gibbons and Veselov show that band edges are the union of the Dirichlet conditions \(W_\pm(a,E)=0\) and the Robin conditions
\[
W_\pm'(a,E)+\gamma W_\pm(a,E)=0.
\]
For the level \(E=2n\), choose the parity matching \(n\). Their Kummer representations are
\[
W_+(a,E)=e^{-a^2/2}{}_1F_1\!\left(-\frac E4;\frac12;a^2\right)
\]
for even parity and
\[
W_-(a,E)=\sqrt2\,a e^{-a^2/2}{}_1F_1\!\left(\frac{2-E}{4};\frac32;a^2\right)
\]
for odd parity.

Write \(E=2n+\varepsilon\). At \(\varepsilon=0\), the first Kummer parameter is a non-positive integer, so the solution is a polynomial times \(e^{-a^2/2}\). The large-positive-argument Kummer expansion has a growing term proportional to \(e^{a^2}/\Gamma(A)\). Since \(1/\Gamma(A)\) has a simple zero at each non-positive integer, differentiating with respect to \(E\) produces the dominant growing contribution.

For \(n=2m\), direct extraction of the leading polynomial and growing coefficients gives
\[
W_+(a,2n)=(-1)^m\frac{2^{2m}m!}{(2m)!}a^{2m}e^{-a^2/2}\left(1+O(a^{-2})\right),
\]
\[
\partial_EW_+(a,2n)=(-1)^{m+1}\frac{\sqrt\pi\,m!}{4}a^{-2m-1}e^{a^2/2}\left(1+O(a^{-2})\right).
\]
For \(n=2m+1\), the corresponding coefficients are
\[
W_-(a,2n)=(-1)^m\frac{2^{2m+1/2}m!}{(2m+1)!}a^{2m+1}e^{-a^2/2}\left(1+O(a^{-2})\right),
\]
\[
\partial_EW_-(a,2n)=(-1)^{m+1}\frac{\sqrt{2\pi}\,m!}{8}a^{-2m-2}e^{a^2/2}\left(1+O(a^{-2})\right).
\]
Both parities therefore yield the same Newton quotient
\[
-\frac{W(a,2n)}{\partial_EW(a,2n)}=C_n a^{2n+1}e^{-a^2}\left(1+O(a^{-2})\right).
\]
Uniformity of the Kummer expansion in a fixed energy neighborhood, together with analyticity in \(E\), makes the quadratic Taylor remainder exponentially smaller than the retained algebraic relative error. Thus the unique nearby Dirichlet root has the stated expansion for \(E_n^D\).

For the Robin root, the logarithmic derivatives at \(E=2n\) are
\[
\frac{W'(a,2n)}{W(a,2n)}=-a+\frac na+O(a^{-3}),
\]
\[
\frac{\partial_EW'(a,2n)}{\partial_EW(a,2n)}=a-\frac{n+1}{a}+O(a^{-3}).
\]
Linearizing \(W'+\gamma W\) in energy and comparing with the Dirichlet quotient gives
\[
E_n^R-2n=(E_n^D-2n)\frac{-a+\gamma+n/a+O(a^{-3})}{a+\gamma-(n+1)/a+O(a^{-3})}.
\]
For fixed \(\gamma\), the ratio is
\[
-1+\frac{2\gamma}{a}+O(a^{-2}),
\]
which proves the Robin expansion. The two roots converge to \(2n\), whereas the nearest roots attached to the opposite oscillator levels remain separated by order one. Standard one-dimensional Sturm-Liouville interlacing therefore identifies these two roots as the unique band edges near \(2n\) for sufficiently large \(a\). Subtracting the two edge expansions gives the band-width formula.

## Verification
The coefficient extraction uses only the source's Kummer representation, the simple zero of \(1/\Gamma(A)\) at \(A=-m\), and the standard large-positive-argument Kummer expansion. The included coefficient checker independently simplifies the even- and odd-parity prefactors to \(C_n=2^{n+2}/(\sqrt\pi\,n!)\) for a finite range of symbolic integer cases and checks the first-order Robin quotient expansion numerically. That finite check is corroborative; the proof above is the all-\(n\) argument.

High-precision direct root calculations performed during verification for fixed \(\gamma=0.7\) and several \(n\) show convergence of the measured width to the displayed asymptotic as \(a\) increases. Those computations are not used as a proof.

## Relationship to prior work
Gibbons and Veselov give the exact Weber-Hermite characterization of periodic and antiperiodic band edges and explicitly identify \(a\to\infty\) with fixed \(\gamma\) as an interesting asymptotic regime. They also state that low bands are expected to shrink exponentially to harmonic-oscillator levels while precise asymptotics require further investigation. The present result supplies the fixed-coupling exact leading constant and first relative coupling correction for every fixed oscillator level.

Moore and Marsiglio analyze a different Kronig-Penney geometry: truncated harmonic wells separated by flat barrier regions. Their exact dispersion relations and tight-binding discussion confirm exponential low-band flattening in that different model, but do not imply the Weber-Hermite/delta-boundary coefficient above. Vawter studies finite-wall shifts of a confined harmonic oscillator, which is relevant to the Dirichlet-edge mechanism but not to the periodic delta matching or the resulting band width. Connor, Uzer, Marcus, and Smith derive general semiclassical band-width formulas for periodic potentials and apply them to Mathieu-type problems; the accessible material does not specialize their formula to this nonsmooth periodic parabola with point interactions or provide the fixed-\(\gamma\) correction displayed here.

## Limitations
The theorem is an asymptotic statement for fixed \(n\) and fixed \(\gamma\). It does not give a uniform estimate over many bands, does not address the scaling \(\gamma\sim a\), and does not classify the entire spectrum. A residual literature risk remains that an older general semiclassical formula, after nontrivial specialization to the cusp-and-delta cell boundary, may reproduce the leading constant. No such specialization was found in the inspected sources; the source paper itself treats this asymptotic regime as open.

## References
1. J. Gibbons and A. P. Veselov, “On spectrum of the harmonic Kronig-Penney model,” arXiv:2610.00879v1, 2026.
2. C. Moore and F. Marsiglio, “Analytical solution to the Kronig–Penney model with harmonic oscillator wells: insights to tight-binding,” arXiv:2605.08032v1; Scientific Reports, 2026, DOI: 10.1038/s41598-026-67469-y.
3. J. N. L. Connor, T. Uzer, R. A. Marcus, and A. D. Smith, “Eigenvalues of the Schrödinger equation for a periodic potential with nonperiodic boundary conditions: A uniform semiclassical analysis,” Journal of Chemical Physics 80 (1984), DOI: 10.1063/1.446581.
4. R. Vawter, “Effects of Finite Boundaries on a One-Dimensional Harmonic Oscillator,” Physical Review 174 (1968), DOI: 10.1103/PhysRev.174.749.
5. NIST Digital Library of Mathematical Functions, §13.7, large-argument asymptotics for Kummer functions.
