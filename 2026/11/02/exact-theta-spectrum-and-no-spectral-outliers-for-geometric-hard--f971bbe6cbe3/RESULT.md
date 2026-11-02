# Exact theta-spectrum and no spectral outliers for geometric Hardy kernel chains

## Finding

For arbitrary \(0<q<1\) and \(0<c<2\), the geometric boundary-approach sequence
\[
r_n=1-cq^n\quad(n=0,1,2,\ldots)
\]
consists of distinct points in \((-1,1)\). In the classical Hardy space \(H^2(\mathbb D)\), take the normalized Szegő kernels
\[
e_n(z)=\frac{\sqrt{1-r_n^2}}{1-r_n z}.
\]
Their Gram operator \(G\) on \(\ell^2(\mathbb N_0)\) has entries
\[
G_{nm}=\frac{\sqrt{(1-r_n^2)(1-r_m^2)}}{1-r_nr_m}.
\]
Write \(t=\sqrt q\) and set
\[
\vartheta_3(t)=\sum_{j\in\mathbb Z}t^{j^2},\qquad
\vartheta_4(t)=\sum_{j\in\mathbb Z}(-1)^jt^{j^2}.
\]
Then the **complete spectral interval** is
\[
\boxed{\sigma(G)=\sigma_{\mathrm{ess}}(G)=
[\vartheta_4(t)^2,\vartheta_3(t)^2].}
\]
Equivalently, for every finitely supported complex coefficient sequence \((a_n)\),
\[
\vartheta_4(t)^2\sum_n|a_n|^2\le
\left\|\sum_n a_ne_n\right\|_{H^2}^2\le
\vartheta_3(t)^2\sum_n|a_n|^2,
\]
and **both constants are sharp for every \(c\)**. In particular, no isolated eigenvalue can lie outside the stated interval, even when the initial point approaches either end of the diameter. The optimal squared Riesz condition number is \((\vartheta_3(t)/\vartheta_4(t))^2\).

## Assumptions and scope

The only parameters are \(0<q<1\) and \(0<c<2\); indices start at zero. The Szegő kernel normalization is \(K(z,w)=(1-z\overline w)^{-1}\), with \(\|K(\cdot,w)\|^2=1/(1-|w|^2)\). The Gram acts on the coefficient space, not the entire Hardy function space. Because \(\sum_n(1-r_n)<\infty\) and all but finitely many points are positive, this is a Blaschke sequence; therefore the kernel family is not complete in \(H^2\). No claim about a basis of all of \(H^2\) is made.

## Proof

**1. Toeplitz comparison.** Put \(x_n=cq^n\), so \(0<x_n<2\), and define
\[
H_{nm}=\frac{2\sqrt{x_nx_m}}{x_n+x_m}
=\operatorname{sech}\!\left(\frac{(n-m)|\log q|}{2}\right).
\]
Thus \(H\) is a bounded positive half-line Toeplitz matrix, independent of \(c\), with absolutely summable coefficients. Directly from the normalized kernel formula,
\[
G_{nm}=\frac{\sqrt{x_n(2-x_n)x_m(2-x_m)}}{x_n+x_m-x_nx_m}.
\]
Set \(d_n=\sqrt{1-x_n/2}\) and \(u_n=x_n^{-1}-1/2>0\). Then the exact identity
\[
G_{nm}=d_nd_mH_{nm}\left(1+\frac{1}{u_n+u_m}\right)
\]
holds for all indices, including the diagonal. Let \(R_{nm}=d_nd_m(1+(u_n+u_m)^{-1})\). It is a normalized positive correlation matrix: \(R_{nn}=1\), and
\[
R_{nm}=\langle d_n(1,e^{-u_n s}),
 d_m(1,e^{-u_m s})\rangle_{\mathbb C\oplus L^2(0,\infty)}.
\]
Consequently \(G=H\circ R\), with \(\circ\) denoting entrywise Schur multiplication. This Schur map is unital and positive on bounded operators (first on finite matrices, then by bounded operator limits). In particular, every operator-order bound \(aI\le H\le bI\) transfers to \(aI\le G\le bI\).

**2. Trace-class difference.** The matrix \(J_{nm}=(u_n+u_m)^{-1}\) is positive, since it is the Gram matrix of \(s\mapsto e^{-u_n s}\). Moreover,
\[
\sum_nJ_{nn}=\sum_n\frac{x_n}{2-x_n}<\infty,
\]
so \(J\) is positive trace class. As \(H\) is positive with diagonal entries one, \(H\circ J\) is positive trace class with trace equal to the same convergent sum. If \(D=\operatorname{diag}(d_n)\), then
\[
G=D\big(H+H\circ J\big)D.
\]
Also \(D-I\) is trace class because \(\sum_n(1-d_n)<\infty\). Therefore \(G-H\) is trace class. In particular their essential spectra agree.

**3. Exact Toeplitz endpoints.** Put \(L=|\log q|\), \(t=e^{-L/2}=\sqrt q\). The Fourier symbol of \(H\) is the continuous positive real function
\[
f(\theta)=\sum_{m\in\mathbb Z}
\operatorname{sech}(mL/2)e^{im\theta}
=1+4\sum_{m\ge1}\frac{t^m}{1+t^{2m}}\cos(m\theta).
\]
The classical Jacobi \(\operatorname{dn}\) Fourier expansion (DLMF 22.11.3) and theta-constant identities yield
\[
f(\theta)=\frac{2K(k)}{\pi}
\operatorname{dn}\!\left(\frac{K(k)\theta}{\pi},k\right),\quad
\frac{2K(k)}{\pi}=\vartheta_3(t)^2,\quad
k'=\sqrt{1-k^2}=\frac{\vartheta_4(t)^2}{\vartheta_3(t)^2}.
\]
Here \(t=\exp(-\pi K(k')/K(k))\) uniquely determines \(0<k<1\). The Jacobi function \(\operatorname{dn}\) decreases from one at zero to \(k'\) at its real quarter-period \(K(k)\). Consequently,
\[
\min_{\theta\in[0,2\pi]}f(\theta)=\vartheta_4(t)^2>0,
\qquad \max_{\theta\in[0,2\pi]}f(\theta)=\vartheta_3(t)^2.
\]
Fourier transformation on \(\ell^2(\mathbb Z)\) gives those bounds for the compressed half-line Toeplitz matrix \(H\). Conversely, long truncated plane-wave vectors, translated to indices tending to infinity, form Weyl sequences for every value in \(f([0,2\pi])\); the absolute summability of the coefficients controls their boundary errors. Hence
\[
\sigma(H)=\sigma_{\mathrm{ess}}(H)=
[\vartheta_4(t)^2,\vartheta_3(t)^2].
\]

**4. No outliers and sharpness.** The unital positive Schur representation from Step 1 transfers the two sharp Toeplitz order bounds to \(G\), so its spectrum is contained in the same closed interval. Step 2 gives equality of essential spectra, hence every point of the interval already belongs to \(\sigma(G)\). The spectral equality follows. The best upper and lower Riesz constants are the spectral endpoints by the quadratic-form characterization, so they are sharp and independent of \(c\).

## Verification

A standalone finite-matrix checker is supplied in `check_geometric_hardy.py`. It independently computes normalized Gram matrices, the exact Schur factorization, positive Cauchy and correlation matrices, and the theta endpoint estimates across several values of \(q\), \(c\), and the truncation size. It also checks the Fourier-endpoint identities. These finite checks test formulas and numeric consequences; they do **not** establish infinite-dimensional spectrum, trace-class membership, or bibliographic priority. Those statements rest on the displayed proof and source comparisons.

## Relationship to prior work

Baranov–Batenev study representing systems of Szegő kernels and related reproducing kernels; their main results concern existence and representation, not sharp Riesz constants or spectral sets for a single geometric chain. Pushnitski studies different Hardy-kernel matrices indexed by ordinary integers and demonstrates that spectral outliers can occur; his spectral theorems do not directly cover the present normalized geometric Szegő Gram matrix. Standard Toeplitz and Jacobi elliptic-function identities supply important known ingredients, which are not claimed as original. The additional point is the exact correlation-Schur factorization, its trace-class comparison, and the resulting *full*, starting-point-independent spectrum with no outliers.

## Limitations

The theorem concerns one diameter and exact geometric boundary approach. Arbitrary perturbations of the nodes, non-geometric radial spacing, non-collinear configurations, and weighted Bergman analogues are not classified. Although the full spectral set is determined, spectral type beyond the inherited absolutely continuous component is not classified. Independent review and historical-priority verification remain outstanding.

## References

1. A. Baranov and T. Batenev, *Representing systems of reproducing kernels in spaces of analytic functions*, arXiv:2207.08985, first public version July 18, 2022, Sections 1–6. https://arxiv.org/abs/2207.08985
2. A. Pushnitski, *The spectral density of Hardy kernel matrices*, arXiv:2103.12642, first public version March 23, 2021, especially Sections 1–3. https://arxiv.org/abs/2103.12642
3. NIST Digital Library of Mathematical Functions, §22.11.3 (Jacobi \(\operatorname{dn}\) Fourier series), §§20.2 and 20.4 (theta series and theta constants). https://dlmf.nist.gov/22.11 ; https://dlmf.nist.gov/20.4
