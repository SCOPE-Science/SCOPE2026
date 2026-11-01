# Sharp angular-offset determinant and conditioning for two spherical latitude rings

## Finding
For every integer \(L\ge2\), sampling all spherical harmonics through degree \(L\) on two symmetric regular \(2L\)-point latitude rings gives an exact, globally optimal angular staggering. The determinant of the \(4L\)-row evaluation Gram matrix obeys
\[
\det(E_\delta E_\delta^*)=\det(E_{\pi/(2L)}E_{\pi/(2L)}^*)\sin^2(L\delta),\qquad \det(E_{\pi/(2L)}E_{\pi/(2L)}^*)>0.
\]
Thus half-step staggering uniquely maximizes the determinant modulo cyclic relabeling and minimizes the row-space spectral condition number; aligned rings lose exactly one dimension of interpolation rank.

## Assumptions and scope
Let \(m=2L\), \(L\ge2\), and \(h\in(0,1)\). At colatitudes \(\arccos h\) and \(\arccos(-h)\), sample the longitudes \(2\pi j/m\) and \(\delta+2\pi j/m\), respectively, for integers \(0\le j<m\). Let \(\Pi_L(S^2)=\bigoplus_{\ell=0}^L\mathcal H_\ell(S^2)\), of dimension \((L+1)^2\). Form the unweighted \(2m\)-by-\((L+1)^2\) complex evaluation matrix \(E_\delta\) using any basis \(Y_\ell^q\) orthonormal for surface probability measure \(d\omega/(4\pi)\), for \(-\ell\le q\le\ell\). Define \(G_\delta=E_\delta E_\delta^*\). The spectral condition number is the largest singular value divided by the smallest positive singular value when \(E_\delta\) has full row rank, and infinity when it does not. Only the relative longitude \(\delta\) varies.

## Proof
Applying a unitary length-\(m\) discrete Fourier transform separately to the top and bottom rings decomposes \(G_\delta\) into \(m\) Hermitian blocks of size two. The integer Fourier orders available in \(\Pi_L\) are \(-L,-L+1,\dots,L\). Every residue modulo \(m\) has precisely one such order, except the Nyquist residue \(r=L\), which has the two orders \(q=\pm L\).

For a non-Nyquist residue, let \(q\) denote its unique order, and define
\[
a_q=\sum_{\ell=|q|}^L|Y_\ell^q(\arccos h,0)|^2,\qquad b_q=\sum_{\ell=|q|}^L(-1)^{\ell+|q|}|Y_\ell^q(\arccos h,0)|^2.
\]
The harmonic reflection parity \(Y_\ell^q(\arccos(-h),\varphi)=(-1)^{\ell+|q|}Y_\ell^q(\arccos h,\varphi)\) yields a block with eigenvalues \(m(a_q\pm|b_q|)\). These values do not involve \(\delta\). Moreover \(|q|\le L-1\), and both summands at \(\ell=|q|\) and \(\ell=|q|+1\) are strictly positive when \(0<h<1\), because the corresponding associated Legendre factors are nonzero multiples of \((1-h^2)^{|q|/2}\) and \(h(1-h^2)^{|q|/2}\). Their parities are opposite, so \(a_q>|b_q|\). Consequently all \(2(m-1)=4L-2\) eigenvalues from these blocks are strictly positive.

At the Nyquist residue, only \(\ell=L\), \(q=\pm L\) occur. Their equal squared amplitude is \(w=|Y_L^L(\arccos h,0)|^2>0\). Up to conjugation by a diagonal unitary, its block is
\[
2mw\begin{pmatrix}1&\cos(L\delta)\\ \cos(L\delta)&1\end{pmatrix},
\]
with eigenvalues \(2mw(1\pm\cos(L\delta))\). Its determinant is \((2mw)^2\sin^2(L\delta)\). Multiplying by the phase-independent determinants of the other blocks proves the stated determinant formula, exact ranks, and strict positivity at \(\delta=\pi/m\).

For fixed sum \(4mw\), the two Nyquist eigenvalues are closest when \(\cos(L\delta)=0\). At any other phase their maximum weakly increases and their minimum weakly decreases, while every other eigenvalue remains fixed and positive. Therefore the ratio of largest to smallest row-Gram eigenvalues, and hence the evaluation condition number, is minimized at every half-step phase. For the determinant, equality \(\sin^2(L\delta)=1\) holds exactly when \(\delta=(2j+1)\pi/m\); modulo cyclic relabeling of each ring these all represent \(\delta\equiv\pi/m\pmod{2\pi/m}\). This finishes the proof for all specified integers and real parameters.

## Verification
Run `python check.py` with Python, NumPy and SciPy installed. It independently constructs all spherical-harmonic evaluations using `scipy.special.sph_harm_y`, diagonalizes the full Gram numerically, and compares the eigenvalues and determinant-ratio formula with the Fourier-block prediction for a finite range of dimensions, heights and phases. These tests check implementation and boundary behavior; the preceding analytic block proof establishes the universal theorem.

## Relationship to prior work
Zu Castell, Lain Fernández and Xu (2004, arXiv:math/0407448) investigate polynomial interpolation on concentric latitude circles and specifically use half-step shifts in qualitative solvability constructions. That earlier geometry is acknowledged: neither the half-step arrangement nor its unisolvence is asserted as new. The present assertion is the exact *global angular determinant-optimality law* and the shift-independent decomposition of all but two row-Gram eigenvalues at the critical sampling bandwidth, together with a sharp one-dimensional rank-defect criterion and conditioning comparison. Khalid, Kennedy and McEwen (2014, arXiv:1403.4661) study fast optimal-dimensional iso-latitude sampling over multiple circles; Marzo (2006, arXiv:math/0611503) develops general interpolation density theory. Their different sampling scope does not imply the stated two-circle determinant ratio without further analysis.

## Limitations
Only unweighted, equally spaced, equal-sized symmetric circles at nonzero, nonpolar heights and bandwidth \(L=m/2\) are covered. The result does not optimize latitude height, sample-count allocation, weights, or arbitrary spherical designs. A phase-independent singular-value sector may make the condition-number minimum nonunique. An equivalent but differently parameterized determinant theorem may exist in unindexed interpolation literature; no independent validation is asserted.

## References
- W. zu Castell, N. Lain Fernández and Y. Xu, *Polynomial Interpolation on the Unit Sphere II*, arXiv:math/0407448 (first posted 2004-07-27), https://arxiv.org/abs/math/0407448.
- Z. Khalid, R. Kennedy and J. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661 (first posted 2014-03-19), https://arxiv.org/abs/1403.4661.
- J. Marzo, *Marcinkiewicz-Zygmund inequalities and interpolation by spherical harmonics*, arXiv:math/0611503 (first posted 2006-11-16), https://arxiv.org/abs/math/0611503.
