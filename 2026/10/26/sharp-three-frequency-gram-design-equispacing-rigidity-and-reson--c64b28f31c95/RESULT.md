# Sharp three-frequency Gram design: equispacing rigidity and resonant nonuniformity

## Finding
For \(\varepsilon>0\) and \(-1\le t\le1\), take the three real frequencies \((-\varepsilon,\varepsilon t,\varepsilon)\). Equip \(L^2([-1,1],dx/2)\) with its probability norm, and let \(G_{\varepsilon,t}\) be the Gram matrix of \(e^{i\omega x}\) at these frequencies. Define the optimal lower Riesz bound
\[
M(\varepsilon)=\max_{-1\le t\le1}\lambda_{\min}(G_{\varepsilon,t}).
\]
There is an absolute \(\varepsilon_0>0\) such that, for every \(0<\varepsilon<\varepsilon_0\), the **unique** maximizing middle position is \(t=0\), and
\[
M(\varepsilon)=1+\frac{\operatorname{sinc}(2\varepsilon)}2-\sqrt{\frac{\operatorname{sinc}^2(2\varepsilon)}4+2\operatorname{sinc}^2\varepsilon}
=\frac{2\varepsilon^4}{135}+\frac{2\varepsilon^6}{1701}+O(\varepsilon^8).
\]
Here \(\operatorname{sinc}(u)=\sin(u)/u\), with \(\operatorname{sinc}(0)=1\).

For **every** \(\varepsilon>0\), the bound \(M(\varepsilon)\le1\) is sharp exactly at the resonant apertures
\[
M(\varepsilon)=1\quad\Longleftrightarrow\quad \varepsilon=m\pi/2\text{ for some integer }m\ge2.
\]
At such an aperture all, and only, maximizers are
\[
t=-1+\frac{2k}{m},\qquad k=1,\ldots,m-1.
\]
Consequently a symmetric optimizer occurs in this exact-orthogonality regime precisely when \(m\) is even; when \(m\) is odd, **every** optimizer is nonuniform. The first symmetry-breaking resonance is \(\varepsilon=3\pi/2\), where the two optimizers are \(t=\pm1/3\), whereas the equal-gap choice has least eigenvalue \(1-2\sqrt2/(3\pi)<1\).

## Assumptions and scope
The observation interval is exactly \([-1,1]\) with measure \(dx/2\); frequency is measured in reciprocal interval units. The outer frequencies are fixed at \(\pm\varepsilon\), and only the middle frequency \(\varepsilon t\) varies. Repeated frequencies at \(t=\pm1\) are allowed in the compact optimization domain, but their least Gram eigenvalue is zero. Matrix eigenvalues are not square-rooted: \(M\) is the **squared** lower singular value of the three-column synthesis map. The expansion holds as \(\varepsilon\downarrow0\) with the stated normalization; no claim about all intermediate apertures is made.

## Proof
**1. Gram reduction.** Direct integration gives \(\langle e^{i\omega_j x},e^{i\omega_k x}\rangle=\operatorname{sinc}(\omega_j-\omega_k)\). With \(u=\operatorname{sinc}(\varepsilon(1+t))\), \(v=\operatorname{sinc}(\varepsilon(1-t))\), and \(w=\operatorname{sinc}(2\varepsilon)\),
\[
G_{\varepsilon,t}=\begin{pmatrix}1&u&w\\u&1&v\\w&v&1\end{pmatrix}.
\]
This Gram matrix is positive semidefinite with trace three. Hence its smallest eigenvalue is at most one, with equality if and only if \(G_{\varepsilon,t}=I_3\).

**2. Uniform small-aperture spectral expansion.** Set \(p_2=3-u^2-v^2-w^2\) (sum of principal minors) and \(p_3=1+2uvw-u^2-v^2-w^2\) (determinant). Taylor expansion of \(\sin z/z\), with polynomial coefficients uniform for \(t\in[-1,1]\), yields
\[
p_2=\frac{2}{3}(3+t^2)\varepsilon^2+O(\varepsilon^4),\qquad
p_3=\frac4{135}(1-t^2)^2\varepsilon^6+O(\varepsilon^8).
\]
The characteristic equation is \(\lambda^3-3\lambda^2+p_2\lambda-p_3=0\). Put \(\lambda=\varepsilon^4 y\), divide by \(\varepsilon^6\), and extend analytically in \(\varepsilon^2\). At zero the resulting equation is
\[
\frac23(3+t^2)y-\frac4{135}(1-t^2)^2=0.
\]
Its derivative in \(y\) is uniformly positive. The analytic implicit-function theorem, uniformly on the compact \(t\)-interval, therefore gives a unique root \(\lambda=\varepsilon^4(c(t)+O(\varepsilon^2))\), with uniform derivatives of every fixed order in \(t\), where
\[
c(t)=\frac{2(1-t^2)^2}{45(3+t^2)}.
\]
The other roots tend to three and have order \(\varepsilon^2\), respectively; the latter has leading coefficient \(2(3+t^2)/9>0\). Thus the constructed root is the least eigenvalue for sufficiently small positive \(\varepsilon\), uniformly even at the repeated-node endpoints (where it is zero).

**3. Uniqueness of the optimal placement.** The even function \(c\) has a unique maximum \(c(0)=2/135\) on \([-1,1]\) and \(c''(0)=-28/405<0\). Select a small neighborhood of zero on which \(c''<0\). Uniform \(C^2\) convergence makes the rescaled least eigenvalue strictly concave there for sufficiently small \(\varepsilon\). On its complement the strict gap beneath \(c(0)\), together with uniform convergence, precludes maximizing points. Symmetry forces derivative zero at \(t=0\), so this point is the unique global optimizer.

**4. Sharp two-term constant.** At \(t=0\) the antisymmetric endpoint vector has eigenvalue \(1-w\); the other two eigenvalues are \(1+w/2\pm\sqrt{w^2/4+2u^2}\). For sufficiently small \(\varepsilon\), the minus sign is the least eigenvalue. Its Taylor expansion gives precisely \(2\varepsilon^4/135+2\varepsilon^6/1701+O(\varepsilon^8)\).

**5. Complete resonance classification.** Equality \(M(\varepsilon)=1\) requires all off-diagonal sinc values to vanish. Since \(\operatorname{sinc}(z)=0\) for real nonzero \(z\) exactly at nonzero integer multiples of \(\pi\), first \(2\varepsilon=m\pi\) for a positive integer \(m\). The two strictly positive consecutive gaps must equal \(k\pi\) and \((m-k)\pi\) for integers \(1\le k\le m-1\). This is possible exactly when \(m\ge2\) and forces \(t=-1+2k/m\); conversely these gaps make the Gram matrix the identity. The parity claim and first odd resonance follow immediately. At \(\varepsilon=3\pi/2,t=0\), the two nearest-neighbor Gram entries are \(-2/(3\pi)\) and the endpoint entry vanishes, giving the stated least eigenvalue.

## Verification
Run the embedded `check.py` using Python with `sympy`, `numpy` and `mpmath`. It independently expands the determinant and principal-minor polynomial, checks \(c(0)\) and \(c''(0)\), verifies the two-term symmetric eigenvalue series, tests finite sample grids, and tests the two exact resonant configurations. Its finite computations are checks, not a substitute for the compactness and analytic-implicit-function proof above.

## Relationship to prior work
The continuous sinc Gram matrix is the generalized prolate matrix in Batenkov–Demanet–Goldman–Yomdin (arXiv:1809.00658), and its single-cluster eigenvalue scaling is investigated further by Batenkov–Goldman (arXiv:2107.09326). Equispaced small-aperture spectra belong to the older Slepian/prolate theory, and that **equispaced specialization and its leading constant are not claimed as independently new**. The present assertion optimizes the *location of an unconstrained middle frequency at fixed outer endpoints*, proves unique equispaced optimality for every sufficiently small aperture, and classifies all exact orthogonality apertures and optimizer positions. These optimizer statements do not follow solely from the quoted order bounds or from computing the spectrum at a prescribed equispaced configuration. Batenkov–Diab (arXiv:2203.11923) studies confluent sampling with a different operator and grid-based superresolution rates. Historical overlap in optimal experiment design remains possible.

## Limitations
The existence proof for \(\varepsilon_0\) is qualitative; it does not specify the largest interval of equispacing optimality or classify all optimizers at nonresonant intermediate apertures. A source-specific priority risk remains for older work on optimal designs of nonharmonic exponential frames and prolate matrices. The statement concerns three prescribed-frequency exponentials and their *linear* lower Riesz bound, not general nonlinear superresolution recovery error.

## References
1. D. Batenkov, G. Goldman, *Single-exponential bounds for the smallest singular value of Vandermonde matrices in the sub-Rayleigh regime*, arXiv:2107.09326 (first posted 2021-07-20), especially Definition 2.4, Theorem 2.3 and Section 3.
2. D. Batenkov, L. Demanet, G. Goldman, Y. Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes*, arXiv:1809.00658, especially Sections 2–3 and the generalized prolate construction.
3. D. Batenkov, B. Diederichs, G. Goldman, Y. Yomdin, *The spectral properties of Vandermonde matrices with clustered nodes*, arXiv:1909.01927, especially Sections 1–2.
4. D. Batenkov, N. Diab, *Super-resolution of generalized spikes and spectra of confluent Vandermonde matrices*, arXiv:2203.11923, especially Sections 1–3.
