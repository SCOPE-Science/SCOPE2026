# An exact incidence-angle essential spectrum and glancing limit for weighted Bergman chord traces

## Finding
Let \(\alpha>-1\) and \(0\le d<1\). On the normalized analytic weighted Bergman space \(A^2_\alpha(\mathbb D)\), consider the positive chord-trace operator \(T_{\alpha,d}=R_d^*R_d\), where \(R_d\) is restriction to any straight chord \(\Gamma_d\) at Euclidean distance \(d\) from the origin, with target measure \((1-|z|^2)^{\alpha+1}\,ds\) (Euclidean arc length). Put \(b=(\alpha+2)/2\), \(\phi=\arcsin d\), and
\[
M_{\alpha}(\xi)=\frac{2^{\alpha+1}}{\Gamma(\alpha+2)}|\Gamma(b+i\xi)|^2,\qquad
C_\alpha(d)=(\cos\phi)^{\alpha+1}\max_{\xi\in\mathbb R}e^{2\phi\xi}M_\alpha(\xi).
\]
Then \(T_{\alpha,d}\) is bounded and positive, with exact Fredholm essential spectrum and exact essential norm
\[
\boxed{\sigma_{\mathrm{ess}}(T_{\alpha,d})=[0,C_\alpha(d)],\qquad \|T_{\alpha,d}\|_{\mathrm{ess}}=C_\alpha(d).}
\]
Moreover the very short, nearly tangent chords have a *nonzero* limiting essential norm:
\[
\boxed{\lim_{d\uparrow1}C_\alpha(d)=\frac{2\pi}{\Gamma(\alpha+2)}\left(\frac{\alpha+1}{e}\right)^{\alpha+1}.}
\]
For the unweighted space \(\alpha=0\), the centered diameter has \(C_0(0)=2\), whereas \(\lim_{d\uparrow1}C_0(d)=2\pi/e\). The restriction maps themselves have essential norm \(\sqrt{C_\alpha(d)}\).

## Assumptions and scope
The Hilbert norm is
\[
\|f\|_\alpha^2=(\alpha+1)\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,\frac{dx\,dy}{\pi},
\]
so the reproducing kernel is \(K_\alpha(z,w)=(1-z\overline w)^{-(\alpha+2)}\). Any chord \(\Gamma_d\) is the open intersection of the unit disk with a Euclidean straight line at distance \(d\) from the origin. At each fixed \(d<1\), the endpoints are distinct and both are transverse to the circle; the singular limit \(d=1\) is **not** included in the theorem. The essential spectrum is the Fredholm spectrum of a bounded operator. All powers of the nonzero complex denominator are taken by analytic continuation from the Bergman kernel (the principal branch on \(\Re(1-z\overline w)>0\)). The maximum defining \(C_\alpha(d)\) is finite and attained for fixed \(d<1\).

## Proof
**1. Reduce to a weighted chord kernel.** Initially on polynomials, define \(R_d f=f|_{\Gamma_d}\). On the unweighted arc-length space, its formal product \(R_dR_d^*\) is the integral operator with Hermitian kernel
\[
H_d(z,w)=\frac{(1-|z|^2)^{(\alpha+1)/2}(1-|w|^2)^{(\alpha+1)/2}}{(1-z\overline w)^{\alpha+2}}.
\]
Split the chord into short endpoint pieces and a compact interior part. Kernel pieces with one coordinate in the interior are Hilbert--Schmidt: point evaluations remain uniformly bounded there, and the other endpoint weight is integrable. Cross terms between opposite endpoint pieces are Hilbert--Schmidt because the two distinct boundary endpoints imply \(|1-z\overline w|\) is bounded below. Thus modulo a Hilbert--Schmidt operator, the positive chord kernel is a direct sum of its two same-endpoint pieces.

**2. Boundary tangent model with a quantitative compact remainder.** Parametrize one endpoint by \(z(t)=\zeta-vt\), \(0<t<\varepsilon\), where \(|\zeta|=|v|=1\). Write \(c=v\overline\zeta=e^{i\vartheta}\), where \(|\vartheta|<\pi/2\) and \(\cos\vartheta=\sqrt{1-d^2}\). Exactly,
\[
1-|z(t)|^2=2t\cos\vartheta-t^2,\qquad
1-z(t)\overline{z(s)}=ct+\overline c\,s-ts.
\]
Set \(a=(\alpha+1)/2>0\). Since \(|ct+\overline c\,s|\ge(\cos\vartheta)(t+s)\), a first-order expansion for small \(s,t\) shows that the actual endpoint kernel differs from
\[
h_{\alpha,\vartheta}(t,s)=\frac{(2\cos\vartheta)^{\alpha+1}(ts)^a}{(ct+\overline c\,s)^{\alpha+2}}
\]
by at most \(C_{\alpha,d}\,(ts)^a/(t+s)^{2a}\). This bound is uniformly finite since \(a>0\), so the difference is Hilbert--Schmidt on the endpoint square. No convergence of a finite matrix is being used to establish compactness.

**3. Mellin diagonalization.** Apply the unitary change \(t=e^{-u}\), \((Uf)(u)=e^{-u/2}f(e^{-u})\). The homogeneous operator on \(0<t<\varepsilon\) becomes Wiener--Hopf convolution, restricted to a logarithmic half-line, with kernel (up to reversing \(u-v\))
\[
\ell_{\alpha,\vartheta}(v)=\frac{(\cos\vartheta)^{\alpha+1}}{2\cosh^{\alpha+2}(v/2+i\vartheta)}.
\]
Contour translation within the zero-free strip \(|\Im v|<\pi\), followed by the beta-integral Fourier transform of \(\cosh^{-(\alpha+2)}\), gives the positive multiplier
\[
m_{\alpha,\vartheta}(\xi)=(\cos\vartheta)^{\alpha+1}e^{-2\vartheta\xi}\frac{2^{\alpha+1}}{\Gamma(\alpha+2)}|\Gamma(b+i\xi)|^2.
\]
(The sign of \(\xi\) reverses if the logarithmic coordinate is oriented oppositely, without changing the spectral range.) For every fixed \(|\vartheta|<\pi/2\), Stirling's formula gives exponential decay of this multiplier at both frequency ends. Its image and closure are \([0,C_\alpha(d)]\), with the same maximum at the two chord endpoints, whose incidence parameters have opposite signs.

**4. Essential-spectrum equality.** The full-line convolution has norm \(C_\alpha(d)\), hence the half-line compression is bounded with spectrum contained in \([0,C_\alpha(d)]\). For each \(\xi\in\mathbb R\), translated long normalized plane-wave packets supported far to the right in the logarithmic half-line form weakly null approximate eigenvectors at \(m_{\alpha,\vartheta}(\xi)\): first let packet length tend to infinity, then translate its support to infinity. Thus the whole multiplier range lies in the Fredholm essential spectrum, and the range is the stated interval. Hilbert--Schmidt endpoint reductions preserve essential spectra. The nonzero Fredholm essential spectra of \(R_dR_d^*\) and \(R_d^*R_d\) coincide by the polar decomposition. Zero belongs to the essential spectrum of \(R_d^*R_d\): normalized Bergman kernels approaching any boundary point other than the chord endpoints are weakly null and have chord traces tending to zero. This proves the assertion and also establishes boundedness of \(R_d\) by the kernel bound. The essential norm of \(R_d\) follows by the Calkin \(C^*\)-identity.

**5. Grazing limit.** Put \(s=\alpha+1>0\), \(\delta=\pi-2\phi\). The evenness of \(M_\alpha\) reduces the maximum to \(y\ge0\) in
\[
C_\alpha(d)=(\cos\phi)^s\max_{y\ge0}e^{2\phi y}M_\alpha(y).
\]
As \(y\to\infty\), Stirling gives, with a relative error tending to zero,
\[
M_\alpha(y)=\frac{2^{s+1}\pi}{\Gamma(s+1)}y^s e^{-\pi y}(1+o(1)).
\]
Also \(\cos\phi\sim\delta/2\). Bounded \(y\) contribute \(o(1)\); on large \(y\), uniform two-sided Stirling bounds and the identity \(\max_{y\ge0}y^se^{-\delta y}=(s/(e\delta))^s\) squeeze the maximum to
\[
\frac{2\pi}{\Gamma(s+1)}\left(\frac{s}{e}\right)^s.
\]
This proves the exact grazing-chord limit, without taking any operator limit at the degenerate chord.

## Verification
The standalone script `verify_chord.py` independently evaluates the beta/gamma normalization, the Fourier-transform multiplier, and the variational glancing limit for several weight exponents; it reports `CHECK_OK`. These finite numerical tests are independent sanity checks only: the Hilbert--Schmidt reductions, Weyl sequences, spectral assertion, and grazing asymptotic are analytic proofs above.

## Relationship to prior work
Halder and Kumar (arXiv:2607.13543v1, 15 July 2026) establish weighted Bergman inequalities on convex curves and on two diameters, motivating the chord trace but not a Fredholm essential-spectrum formula or the grazing-chord constant. Earlier Riesz--Fejér/Frazer work concerns trace inequalities, not the incidence-angle multiplier. Ma, Lu and Zu (arXiv:2608.22882v1, Sections 1 and 3) treat weighted Hankel spectral models and their Mellin multipliers; this classical Mellin mechanism is prior input, not claimed new. Their additive Hankel model has a symmetric real denominator; it does not supply the incidence-phase multiplier of an oblique chord or the near-tangent limit. Standard Hilbert-matrix spectra are also prior background (Bellavita--Daskalogiannis--Stylogiannis, arXiv:2411.00187v1). The centered-diameter case \(d=0\) is already covered in other recent spectral research and is not independently claimed novel; the substantive result is the incidence-angle family \(0<d<1\) and its sharp nonzero grazing limit.

## Limitations
Only Hilbert-space exponent two, analytic weighted Bergman spaces, and straight chords are treated. The theorem gives the **essential** spectrum and norm, not the full operator norm or discrete eigenvalue spectrum. For each \(d<1\) the chord is transverse; the limiting constant as \(d\uparrow1\) does not assert that the degenerate tangent segment carries nonzero measure. No independent audit or global historical-priority certification has been performed.

## References
1. H. Halder and R. Kumar, *Gabriel's and Frazer's problems for weighted Bergman spaces and their applications*, arXiv:2607.13543v1 (15 July 2026), https://arxiv.org/abs/2607.13543.
2. T. Ma, Y. Lu and C. Zu, *Helson Forms and Integral Operators on Bergman Spaces of Dirichlet Series*, arXiv:2608.22882v1 (24 August 2026), https://arxiv.org/abs/2608.22882.
3. C. Bellavita, V. Daskalogiannis and G. Stylogiannis, *On the Hilbert matrix operator: a brief survey*, arXiv:2411.00187v1, https://arxiv.org/html/2411.00187v1.
