# Periodic tumble-rate landscapes preserve diffusion but shift the fourth displacement cumulant

## Finding

Consider a particle running at constant speed \(v>0\) and reversing direction at a spatially periodic positive rate \(\lambda\). The particle's position is unwrapped onto the real line, although its flip environment has period \(L>0\). The central finding is that **spatial variation leaves the effective diffusivity unchanged but contributes an exactly computable, nonnegative correction to the long-time fourth displacement cumulant**.

Let
\[
\ell=\frac1L\int_0^L\lambda(x)\,dx,\qquad
G(x)=\int_0^x(\lambda(u)-\ell)\,du,
\qquad E=\frac1L\int_0^L(G(x)-\bar G)^2\,dx,
\quad \bar G=\frac1L\int_0^LG(x)\,dx.
\]
If \(\kappa_j\) is the long-time displacement cumulant of order \(j\), divided by elapsed time, then
\[
\boxed{\kappa_2=\frac{v^2}{\ell},\qquad
\kappa_4=-\frac{3v^4}{\ell^3}+\frac{12v^2E}{\ell^3}.}
\]
Every odd cumulant rate vanishes. In particular, \(D=\kappa_2/2=v^2/(2\ell)\), while
\[
\boxed{\kappa_4(\lambda)-\kappa_4(\ell)
=\frac{12v^2E}{\ell^3}\ge0,}
\]
with equality if and only if \(\lambda\) is spatially constant almost everywhere.

A sharp spatial-frequency bound strengthens this distinction:
\[
\boxed{0\le E\le \frac{L^2}{4\pi^2}
\frac1L\int_0^L(\lambda(x)-\ell)^2\,dx.}
\]
Equality on the right occurs precisely when all nonconstant Fourier modes of \(\lambda\) have frequency one. Consequently first-harmonic landscapes provide the largest fourth-cumulant correction at fixed \(L\), \(\ell\), and spatial rate variance whenever a positive first-harmonic profile with those constraints exists.

For \(\lambda(x)=\ell[1+\varepsilon\cos(2\pi x/L)]\), where \(|\varepsilon|<1\),
\[
\boxed{\kappa_4=\frac{3v^4}{\ell^3}
\left[-1+\frac{(\ell\varepsilon L)^2}{2\pi^2v^2}\right].}
\]
Thus its sign is negative, zero, or positive according as \(\ell|\varepsilon|L/v\) is smaller than, equal to, or larger than \(\sqrt2\pi\). The positive-sign regime is feasible only when \(\ell L/v>\sqrt2\pi\), because \(|\varepsilon|<1\).

## Assumptions and scope

The state is \((x,\sigma)\in(\mathbb R/L\mathbb Z)\times\{-1,+1\}\), with deterministic movement \(\dot X_t=v\sigma_t\) between reversal events and state-dependent reversal hazard \(\lambda(X_t\bmod L)\). Assume \(0<\lambda_{\min}\le\lambda(x)\le\lambda_{\max}<\infty\); piecewise continuity is enough. Initially the circle-state distribution may be taken stationary, which has uniform position and independent equiprobable direction. The cumulant rates are independent of initial circle-state because the compact velocity-switching process mixes exponentially.

The signed position \(X_t\) is **unwrapped**, not reduced modulo \(L\). Precisely, for \(j=2,4\),
\[
\kappa_j=\lim_{t\to\infty}t^{-1}\operatorname{cum}_j(X_t-X_0).
\]
No Gaussian approximation is assumed; the fourth cumulant can have either sign even though the central-limit diffusivity is unchanged.

## Proof

**Step 1: tilted eigenproblem and Floquet trace.** The tilted backward generator acting on periodic test functions is
\[
(\mathcal L_k f)_\sigma=v\sigma(\partial_x+k)f_\sigma
+\lambda(x)(f_{-\sigma}-f_\sigma).
\]
Let \(\alpha(k)\) be its eigenvalue continuing the simple zero eigenvalue at \(k=0\). For the corresponding two components \(h_+,h_-\), define \(S=h_++h_-\), \(D=h_+-h_-\). Their equations are
\[
\alpha S=v(D'+kD),\qquad
(\alpha+2\lambda)D=v(S'+kS).
\]
After setting \(W=e^{kx}S\) and \(Z=e^{kx}D\), this becomes the first-order linear system
\[
\frac{d}{dx}\begin{pmatrix}W\\Z\end{pmatrix}
=\begin{pmatrix}0&(\alpha+2\lambda(x))/v\\
\alpha/v&0\end{pmatrix}\begin{pmatrix}W\\Z\end{pmatrix}.
\]
Its transfer matrix \(M_\alpha\) over one period has determinant one, because the coefficient matrix has trace zero. Periodicity of \(h_\pm\) imposes a Floquet multiplier \(e^{kL}\), so
\[
\boxed{\operatorname{tr}M_{\alpha(k)}=2\cosh(kL).}
\]
At \(k=0\), \(\alpha(0)=0\). Positivity and boundedness of reversal rates give a unique exponentially mixing compact-state process. Standard positive-semigroup perturbation at the isolated stationary eigenvalue shows that \(\alpha(k)\) is analytic near zero and is the scaled cumulant generating function of the unwrapped displacement. The derivative of the trace with respect to \(\alpha\) at zero is positive, so the analytic implicit-function theorem also supplies the relevant unique even solution \(\alpha(k)\) locally.

**Step 2: transfer matrix expansion.** Direct Volterra expansion of the two-by-two system yields, with \(\ell=L^{-1}\int_0^L\lambda\),
\[
\operatorname{tr}M_\alpha=2+
\frac{2\ell L^2}{v^2}\alpha
+\left(\frac{L^2}{v^2}+\frac{4I}{v^4}\right)\alpha^2
+O(\alpha^3),
\]
where the exact double integral is
\[
I=\int_{0\le u<t\le L}\lambda(u)\lambda(t)
(t-u)(L-t+u)\,du\,dt.
\]
This expansion may also be verified directly for a piecewise constant rate by multiplying Taylor-expanded exact two-by-two matrix exponentials; the accompanying program carries out this independent calculation for exact rational profiles.

**Step 3: spatial-energy identity.** The kernel \(d(L-d)\) is symmetric under \(d\mapsto L-d\) and has the absolutely convergent Fourier expansion
\[
d(L-d)=\frac{L^2}{6}-\frac{L^2}{\pi^2}
\sum_{q=1}^\infty\frac{\cos(2\pi qd/L)}{q^2}
\qquad(0\le d\le L).
\]
Symmetrizing the double integral and applying Parseval to the mean-zero periodic primitive \(G\) gives
\[
\boxed{I=\frac{\ell^2L^4}{12}-L^2E.}
\]
Consequently,
\[
\operatorname{tr}M_\alpha=2+
\frac{2\ell L^2}{v^2}\alpha
+\left(\frac{L^2}{v^2}+\frac{\ell^2L^4}{3v^4}
-\frac{4L^2E}{v^4}\right)\alpha^2+O(\alpha^3).
\]

**Step 4: compare cumulant coefficients.** Write \(\alpha(k)=a_2k^2+a_4k^4+O(k^6)\). Matching the last expansion against
\(2\cosh(kL)=2+L^2k^2+L^4k^4/12+O(k^6)\) gives
\[
a_2=\frac{v^2}{2\ell},\qquad
a_4=-\frac{v^4}{8\ell^3}+\frac{v^2E}{2\ell^3}.
\]
The cumulant-rate identities \(\kappa_2=2!a_2\) and \(\kappa_4=4!a_4\) prove the principal formulas. The trace equation is even in \(k\), so all odd rate coefficients vanish.

**Step 5: rigidity, optimal frequency, and sign boundary.** Since \(E\) is a squared norm, \(E=0\) holds precisely for a constant \(\lambda\). Writing Fourier coefficients of \(\lambda-\ell\) as \(\widehat\lambda_q\), the primitive identity becomes
\[
E=\sum_{q\ne0}\frac{L^2|\widehat\lambda_q|^2}{4\pi^2q^2}
\le\frac{L^2}{4\pi^2}\sum_{q\ne0}|\widehat\lambda_q|^2.
\]
Equality requires all modes with \(|q|\ge2\) to vanish. For the stated cosine landscape, direct integration yields
\(E=\ell^2\varepsilon^2L^2/(8\pi^2)\), completing the exact sign classification.

## Verification

The included `verify.py` is a standalone exact-arithmetic check requiring `sympy` as listed in `requirements.txt`. Run `python verify.py` in the directory containing those two files. It constructs the monodromy independently by multiplying the second-order Taylor polynomials in \(\alpha\) of exact segment transfer matrices. For 34 positive piecewise-constant flip-rate profiles (including nonsymmetric ones) with rational rates, speeds and segment widths, it independently checks both monodromy trace coefficients and both cumulant eigenvalue coefficients against the proposed formulas. The tests include a profile with strictly positive long-time fourth cumulant.

These finite checks **are not** a proof for arbitrary profiles. The infinite-domain assertion follows from the analytic trace, Fourier identity, and perturbation argument above.

## Relationship to prior work

Solon, Cates, and Tailleur introduced and compared standard run-and-tumble and active Brownian frameworks, including steady-state physics (2015 preprint, `arxiv:1504.07391v1`). Angelani, Di Leonardo, and Paoluzzi developed first-passage theory for velocity-jump particles with spatially dependent reversal parameters (`arxiv:1506.08046v1`); first-passage observables on intervals are distinct from unwrapped long-time cumulant rates in periodic media. Mallmin, Blythe, and Evans analyzed dynamical fluctuations and velocity large deviations for spatially homogeneous continuous-time lattice run-and-tumble models (`arxiv:1905.10260`); that paper's stated homogeneous dynamics does not supply the profile-dependent primitive-energy term computed here.

The specific result is the coexistence of profile-independent diffusion and the exact spatial-energy fourth-cumulant correction, including its sharp first-harmonic bound and sign threshold. These are not inferred merely from the absence of search hits; a more general prior Floquet or Markov-additive calculation could encompass them, and this remains an originality limitation.

## Limitations

The theorem concerns one noninteracting velocity-jump particle, symmetric direction reversal, fixed constant speed, one spatial dimension, and strictly positive bounded periodic flip rates. It says nothing about the full distribution at finite time, higher cumulants, position-dependent speeds, asymmetric turn rates, absorbing boundaries, or interacting-particle generalizations. Even when the fourth cumulant rate is positive, a central-limit Gaussian limit still holds on diffusive scales. The use of an initially stationary mod-period circle process simplifies notation but does not change the long-time coefficients.

## References

1. A. P. Solon, M. E. Cates, J. Tailleur, *Active Brownian Particles and Run-and-Tumble Particles: a Comparative Study*, `arxiv:1504.07391v1` (posted 2015-04-28), https://arxiv.org/abs/1504.07391.
2. L. Angelani, R. Di Leonardo, M. Paoluzzi, *First-passage time of run-and-tumble particles*, `arxiv:1506.08046v1` (posted 2015-06-26), https://arxiv.org/abs/1506.08046.
3. E. Mallmin, R. A. Blythe, M. R. Evans, *A comparison of dynamical fluctuations of biased diffusion and run-and-tumble dynamics in one dimension*, `arxiv:1905.10260` (2019), https://arxiv.org/abs/1905.10260.
4. G. H. Weiss, *Some applications of persistent random walks and the telegrapher's equation*, *Physica A* 311 (2002), 381–410.
