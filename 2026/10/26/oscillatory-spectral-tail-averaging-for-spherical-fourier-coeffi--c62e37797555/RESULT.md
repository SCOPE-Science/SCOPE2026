# Oscillatory spectral-tail averaging for spherical Fourier coefficients

## Finding

**Theorem (fixed-frequency oscillatory-tail transfer).** Let \(d\ge2\) be an integer, \(p>d\), and \(L:[r_0,\infty)\to(0,\infty)\) a measurable, eventually positive slowly varying function. Let \(f:[0,\infty)\to[0,\infty)\) be measurable, with \(\int_0^\infty f(r)r^{d-1}\,dr<\infty\). Suppose that, for real \(c_0>0\), finite \(J\ge0\), positive fixed frequencies \(\omega_j\), real amplitudes \(a_j,b_j\), and a measurable error \(e(r)\to0\),
\[
f(r)=r^{-p}L(r)\left(c_0+\sum_{j=1}^{J}[a_j\cos(\omega_j r)+b_j\sin(\omega_j r)]+e(r)\right)
\quad(r\to\infty).
\]
Assume only that the full right side is nonnegative, not that its oscillatory amplitudes vanish. Let \(\Phi:\mathbb R^d\to\mathbb C\) be the inverse unitary Fourier transform of the radial spectral density \(f(|\xi|)\):
\[
\Phi(x)=(2\pi)^{-d/2}\int_{\mathbb R^d}e^{i x\cdot\xi}f(|\xi|)\,d\xi.
\]
Let \(\Lambda_m\) be the eigenvalue on spherical harmonics of degree \(m\) of the chordal restriction kernel \(K(x,y)=\Phi(x-y)\) on \(S^{d-1}\), where the integral operator uses **unnormalized area measure** \(d\sigma(y)\). Put \(\nu_m=m+(d-2)/2\). Then
\[
\boxed{\Lambda_m\sim(2\pi)^{d/2}\,c_0\,A_p\,\nu_m^{1-p}L(\nu_m),\qquad
A_p=\frac{\Gamma(p-1)}{2^{p-1}\Gamma(p/2)^2}
=\frac{\Gamma((p-1)/2)}{2\sqrt\pi\Gamma(p/2)}.}
\]
In particular, **every fixed nonzero-frequency oscillatory spectral-tail component is eliminated at leading order** by restriction to the sphere, although that component need not be small pointwise relative to the mean tail.

**Wendland application.** For the generalized Wendland kernels \(\psi_{\mu,\alpha}^{(\epsilon)}\) as normalized in Hubbert–Jäger, with integer \(d\ge2\), \(\alpha>0\), \(\lambda=(d+1)/2+\alpha\), \(\mu\ge\lambda\), and their admissible scale \(\epsilon>0\), the stated Euclidean spectral asymptotics in that source imply, for all \(d\), including even \(d\),
\[
\widehat{\psi_{\mu,\alpha}^{(\epsilon)}}(m)
\sim (2\pi)^{(d-1)/2}\frac{2^{\lambda-1/2}\Gamma(\lambda-1/2)\mu\epsilon^{2\alpha+1}}{\sqrt{2\pi}}\left(m+\frac{d-1}{2}\right)^{1-2\lambda}.
\]
The even-\(d\) asymptotic is also the statement posed as Conjecture 5.10 in the published 2023 source; the distinct, broader finding here is the stated transfer principle for slowly varying *and* nonvanishing oscillatory spectral tails.

## Assumptions and scope

Slow variation means \(L(cr)/L(r)\to1\) for each fixed \(c>0\) as \(r\to\infty\). The asymptotic error is ordinary scalar \(o(1)\); no derivatives or monotonicity of \(L\) or \(e\) are required. The frequency set is finite and independent of \(m\); allowing frequencies to approach zero with \(m\) is **not claimed**. The area-measure convention is essential: for probability-normalized sphere measure divide \(\Lambda_m\) by \(|S^{d-1}|\). The Fourier-transform normalization is stated above; \(f\) is a spectral density, not the physical radial basis function.

## Proof

**1. Spherical restriction identity.** Fourier inversion, the spherical plane-wave/Funk–Hecke identity, and orthogonality yield, for \(m\ge0\),
\[
\Lambda_m=(2\pi)^{d/2}\int_0^\infty r J_{\nu_m}(r)^2f(r)\,dr.
\tag{1}
\]
Fubini is justified by \(\int_0^\infty r^{d-1}f(r)\,dr<\infty\). This is the same normalization as formula (2.15) of Hubbert–Jäger.

**2. Exact squared-Bessel moment.** Put \(M_{\nu,p}=\int_0^\infty r^{1-p}J_\nu(r)^2\,dr\). For \(p>1\), \(\nu>p/2-1\), the Weber–Schafheitlin integral (DLMF 10.22.57) gives
\[
M_{\nu,p}=\frac{\Gamma(p-1)\Gamma(\nu+1-p/2)}{2^{p-1}\Gamma(p/2)^2\Gamma(\nu+p/2)}
\sim A_p\nu^{1-p}.
\tag{2}
\]
The last asymptotic is the gamma-ratio formula.

**3. Where the moment lives.** Consider the probability measures \(dQ_\nu(r)=M_{\nu,p}^{-1}r^{1-p}J_\nu(r)^2\,dr\), \(\nu\to\infty\). Under \(y=r/\nu\) they converge weakly to
\[
dQ_p(y)=\frac{\mathbf1_{y>1}y^{1-p}}{\pi A_p\sqrt{y^2-1}}\,dy.
\tag{3}
\]
To verify (3), fix \(1+\delta\le y\le B\). The uniform oscillatory Debye formula gives
\[
J_\nu(\nu y)=\left(\frac{2}{\pi\nu\sqrt{y^2-1}}\right)^{1/2}
\big(\cos(\nu\Phi(y)-\pi/4)+O_{\delta,B}(\nu^{-1})\big),
\quad\Phi(y)=\sqrt{y^2-1}-\arccos(1/y).
\]
Squaring and integrating any smooth compactly supported test function yields the density in (3), since \(\Phi'(y)=\sqrt{y^2-1}/y>0\). The integral of that density is one:
\[
\frac1{\pi A_p}\int_1^\infty\frac{y^{1-p}}{\sqrt{y^2-1}}\,dy=1.
\]
Together with (2), compact-interval convergence and the equality of total masses imply tightness, mass convergence across the turning point \(y=1\), and (3). For \(0<\eta<p-1\), the exact moment ratio further implies
\[
\lim_{\nu\to\infty}\int (r/\nu)^{\pm\eta}\,dQ_\nu(r)
=\frac{A_{p\mp\eta}}{A_p}<\infty.
\tag{4}
\]
Thus the tails at \(y\downarrow0\) and \(y\to\infty\) are uniformly negligible after a Potter-type weight \(y^{\pm\eta'}\) with \(0<\eta'<\eta\).

**4. Removing slow variation and oscillations.** By uniform convergence of slowly varying functions on compact \(y\)-intervals and Potter bounds, (3)–(4) imply
\[
\int_0^\infty r^{1-p}J_\nu(r)^2L(r)\,dr\sim M_{\nu,p}L(\nu).
\tag{5}
\]
The region below a fixed large \(r_0\) is negligible, by the power-series upper bound on \(J_\nu(r)\) and the integrability of \(f\). For each fixed \(\omega>0\), the same splitting and Debye formula show
\[
\int_0^\infty r^{1-p}J_\nu(r)^2 L(r)e^{i\omega r}\,dr=o(M_{\nu,p}L(\nu)).
\tag{6}
\]
Indeed on \(1+\delta\le y\le B\), replace \(L(\nu y)/L(\nu)\) uniformly by one. Expanding \(\cos^2\) leaves the phases \(\nu\omega y\) and \(\nu(\omega y\pm2\Phi(y))\). The first is nonstationary; for the latter, \(\Phi''(y)=1/(y^2\sqrt{y^2-1})>0\), so the van der Corput second-derivative estimate gives a vanishing integral, even at possible isolated stationary points. Equations (3)–(4) and Potter bounds make the omitted ends arbitrarily small. The \(o(1)\) term in the spectral hypothesis is similarly negligible by dominated weighted moment bounds. Combining (1), (2), (5), and (6) proves the theorem.

**5. Generalized Wendland substitution.** Hubbert–Jäger's Euclidean Fourier asymptotic gives \(p=2\lambda\), \(L\equiv1\), and
\[
c_0=\frac{2^\lambda\Gamma(\lambda)\mu\epsilon^{2\alpha+1}}{\sqrt{2\pi}}.
\]
For \(\mu>\lambda\) the leading modulation is constant. For \(\mu=\lambda\), their displayed endpoint formula also contains a fixed-frequency cosine of nonvanishing relative size, covered by (6). Substitution into the general constant and \(\Gamma(\lambda-1/2)/(2\sqrt\pi\Gamma(\lambda))=A_{2\lambda}\) yields the announced coefficient. Replacing \(m+(d-2)/2\) with \(m+(d-1)/2\) changes the asymptotic by a factor \(1+o(1)\), not the leading constant.

## Verification

A standalone reproducibility script, `check_transfer.py`, tests the exact Bessel-square moment against independent numerical quadrature and compares the asymptotic prediction with positive radial spectral densities having persistent cosine factors and either constant or logarithmically slowly varying envelopes. Its finite tests corroborate but cannot prove the all-index theorem. The all-index proof relies on the exact moment formula and uniform Bessel asymptotics detailed above. All assertions in the included checker passed when executed for this package.

## Relationship to prior work

Hubbert and Jäger's arXiv version of 19 October 2021 states an even-dimensional asymptotic among its claims. Their later peer-reviewed 2023 paper, however, proves the precise asymptotic for odd Euclidean dimensions and **explicitly poses the even-dimensional case as Conjecture 5.10**. Accordingly, the Wendland coefficient asymptotic itself is **not claimed as a never-before-stated formula**. The new claim is a separately proved, general transfer principle for arbitrary slowly varying envelopes and persistent oscillatory tails, which in particular settles that later conjectural case by a different method. The older general radial-restriction estimates cited in their paper provide upper and lower decay bounds rather than this precise, oscillatory-tail-independent leading coefficient. The Weber–Schafheitlin moment and Debye asymptotic are classical ingredients; neither is being claimed new.

## Limitations

The spectral density is assumed radial, integrable with its Euclidean radial weight, and nonnegative; the power exponent is \(p>d\). The oscillatory frequencies must be fixed nonzero real constants and finite in number. We do not assert rates of convergence, uniformity in dimension or frequency, conclusions for rapidly moving frequency scales, or uniqueness in the historical literature. No claim of independent validation is made.

## References

1. S. Hubbert and J. Jäger, *Generalised Wendland functions for the sphere*, arXiv:2110.09835v1 (first public 2021-10-19), https://arxiv.org/html/2110.09835v1 .
2. S. Hubbert and J. Jäger, *Generalised Wendland functions for the sphere*, Advances in Computational Mathematics 49:3 (2023), DOI 10.1007/s10444-022-10005-z, open-access version https://jlupub.ub.uni-giessen.de/bitstreams/244d2cc7-912c-4b95-8c4e-849521692acf/download .
3. NIST Digital Library of Mathematical Functions, §10.22.57 (Weber–Schafheitlin integral), https://dlmf.nist.gov/10.22.E57 ; and §10.19 (uniform Bessel asymptotic regime), https://dlmf.nist.gov/10.19 .
4. Q. T. Le Gia, I. H. Sloan and H. Wendland, *Multiscale Analysis in Sobolev Spaces on the Sphere*, SIAM J. Numer. Anal. (2010), DOI 10.1137/090774550.
