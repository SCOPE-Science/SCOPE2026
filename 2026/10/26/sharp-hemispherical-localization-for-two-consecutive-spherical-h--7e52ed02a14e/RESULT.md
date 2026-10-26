# Sharp hemispherical localization for two consecutive spherical-harmonic degrees

## Finding
For every integer \(\ell\ge0\), let \(\mathcal V_\ell=\mathcal H_\ell(S^2)\oplus\mathcal H_{\ell+1}(S^2)\), where \(\mathcal H_j\) consists of degree-exact complex spherical harmonics. Denote by \(Q_\ell\) the compression of multiplication by the northern closed hemisphere indicator to \(\mathcal V_\ell\). Then its **complete spectrum, including multiplicities**, is
\[
\sigma(Q_\ell)=\{\tfrac12+t_{\ell,|m|},\ \tfrac12-t_{\ell,|m|}:-\ell\le m\le\ell\}\ \uplus\ \{\tfrac12,\tfrac12\},
\]
where \(\uplus\) means multiset union and \(t_{\ell,m}>0\) is the explicit associated-Legendre boundary expression in the proof. All eigenvalues lie strictly between zero and one. The largest eigenvalue (and hence the sharp energy-fraction constant) is
\[
\boxed{\Lambda_\ell=\frac12+\frac{\sqrt{2\ell+3}\,\Gamma(\ell+\frac32)}{2(\ell+1)\sqrt\pi\,\Gamma(\ell+1)}}.
\]
Its eigenspace is exactly the span of the normalized waves \((Y_{\ell,m}+Y_{\ell+1,m})/\sqrt2\) for \(m=\pm\ell\) (one such wave for \(\ell=0\)). Consequently
\[
\Lambda_0=\frac{2+\sqrt3}4,\quad \Lambda_{\ell+1}<\Lambda_\ell,\quad
\lim_{\ell\to\infty}\Lambda_\ell=\frac12+\frac1{\sqrt{2\pi}}.
\]
The limiting constant is never attained at finite degree.

## Assumptions and scope
Use standard area measure \(d\omega\) on \(S^2\), and an orthonormal complex Condon–Shortley spherical-harmonic basis \(Y_{jm}\) in \(L^2(S^2,d\omega)\). Normalizing the area measure instead to a probability measure leaves every concentration fraction unchanged. Write \(x=\cos\theta\) and \(P_j^m(x)\) for the associated Legendre function with integer \(0\le m\le j\). Define
\[
\psi_{jm}(x)=\sqrt{\frac{(2j+1)(j-m)!}{2(j+m)!}}P_j^m(x),
\quad \int_{-1}^1|\psi_{jm}(x)|^2\,dx=1.
\]
The hemisphere is \(x\ge0\). All claims are for the two **exact** adjacent degrees, not the full low-pass band of degrees up to \(\ell+1\).

## Proof
**1. Orthogonal azimuthal blocks.** Integration in longitude forces equal azimuthal indices. Reflection \(x\mapsto-x\) gives hemisphere diagonal energy exactly \(1/2\) for a spherical harmonic. The two cross-degree entries at fixed \(|m|\le\ell\) equal
\[
t_{\ell,m}=\int_0^1\psi_{\ell m}(x)\psi_{\ell+1,m}(x)\,dx.
\]
Thus \(Q_\ell\) is an orthogonal sum of \(2\times2\) matrices \(\bigl(\begin{smallmatrix}1/2&t_{\ell,m}\\t_{\ell,m}&1/2\end{smallmatrix}\bigr)\), together with the one-dimensional modes \(m=\pm(\ell+1)\) of eigenvalue \(1/2\). For \(m<0\), complex conjugation supplies the same real cross entry. This already proves the spectral multiset once positivity and its ordering are established.

**2. Exact cross entries.** The associated Legendre Sturm–Liouville equations at degrees \(\ell\) and \(\ell+1\), integrated from zero to one, yield
\[
t_{\ell,m}=\frac{\psi_{\ell m}(0)\psi_{\ell+1,m}'(0)-\psi_{\ell m}'(0)\psi_{\ell+1,m}(0)}{2(\ell+1)}.
\]
For \(j+m\) even, \(P_j^m(0)=(-1)^{(j+m)/2}(j+m-1)!!/(j-m)!!\) and \((P_j^m)'(0)=0\). For \(j+m\) odd, \(P_j^m(0)=0\) and \((P_j^m)'(0)=(-1)^{(j+m-1)/2}(j+m)!!/(j-m-1)!!\). Here \((-1)!!=0!!=1\). Substitution shows every \(t_{\ell,m}>0\) and gives the exact factorial formula for the entire spectrum. Strict Cauchy–Schwarz on a proper hemisphere gives \(t_{\ell,m}<1/2\): equality would make two distinct-degree full-sphere harmonics linearly dependent on an open hemisphere, hence everywhere, contradicting orthogonality.

**3. Sharp ordering across azimuthal indices.** For \(0\le m\le\ell-2\), put
\[
B_{\ell,m}=\frac{(\ell-m)^2((\ell+m+2)^2-1)}{(\ell+m+2)^2((\ell-m)^2-1)}>1.
\]
The factorial formula implies
\[
\frac{t_{\ell,m+2}^2}{t_{\ell,m}^2}=
\begin{cases}B_{\ell,m},&\ell+m\text{ even},\\ B_{\ell,m}^{-1},&\ell+m\text{ odd}.\end{cases}
\]
Thus the even-parity order chain strictly increases toward \(m=\ell\), while the odd-parity chain strictly decreases from its smallest index, which is \(m=0\) when \(\ell\) is odd and \(m=1\) when \(\ell\) is even.

For \(\ell=2k+1\), let \(U_k=(2k+1)!!/(2k)!!\). Direct evaluation gives
\[
t_{2k+1,0}=\frac{\sqrt{(4k+3)(4k+5)}}{16(k+1)^2}U_k^2<\frac1\pi.
\]
For \(\ell=2k\) with \(k\ge1\), similarly
\[
t_{2k,1}=\frac{\sqrt{(4k+1)(4k+3)}}{4(2k+1)^2}\sqrt{\frac{k}{k+1}}\,U_k^2<\frac1\pi.
\]
Indeed strict log-convexity of \(\Gamma\) gives \(U_k^2<4(k+1)/\pi\); the first comparison uses \(\sqrt{(4k+3)(4k+5)}<4(k+1)\), and the second follows by squaring \((2k+1)^4>(4k+1)(4k+3)k(k+1)\), whose difference is \(5k^2+5k+1>0\). In contrast,
\[
t_{\ell,\ell}=\frac{\sqrt{2\ell+3}\,\Gamma(\ell+3/2)}{2(\ell+1)\sqrt\pi\,\Gamma(\ell+1)}>\frac1{\sqrt{2\pi}}>\frac1\pi.
\]
The first strict bound follows from \(\Gamma(\ell+3/2)/\Gamma(\ell+1)>(\ell+1)/\sqrt{\ell+3/2}\), another log-convexity consequence. This proves strict, global dominance of \(m=\ell\) and the claimed equality eigenspace. The special case \(\ell=0\) is immediate from the single two-dimensional block.

**4. Degree monotonicity and limit.** The closed formula implies
\[
\frac{t_{\ell+1,\ell+1}}{t_{\ell,\ell}}=
\sqrt{1-\frac1{(2\ell+4)^2}}<1.
\]
The standard gamma-ratio asymptotic gives \(t_{\ell,\ell}\to1/\sqrt{2\pi}\), establishing every remaining assertion.

## Verification
The accompanying standalone `check.py` calculates every squared cross entry as an exact rational number from the Wronskian boundary expressions and checks the parity-chain ratios, positivity, the strict \(1/2\) cap, and the unique maximum for degrees one through thirty-nine. Run `python3 check.py`. `checks.txt` records the actual output. Finite checks supplement, but do not replace, the all-degree inequalities proved above.

## Relationship to prior work
Classical spherical Slepian theory supplies general hemispherical/polar-cap concentration matrices and fixed-order block decompositions [1,2]. The present theorem solves a different, sparse two-degree packet analytically, identifies its entire spectrum and the globally extremal azimuthal indices, and proves a sharp all-degree localization law. A published half-energy parity theorem [3] already determines the multiplicity at \(1/2\) for arbitrary degree masks; its two central levels in the present packet are therefore **not claimed as new**. Its stated half-energy counting result does not by itself imply the off-center eigenvalues or the sharp norm and maximizing modes; the full text could not be inspected and remains a priority limitation.

## Limitations
No assertion is made about the spectra of full low-pass bands, arbitrary cap radii, or higher-dimensional spheres. The originality assessment is provisional, particularly because general Slepian formulas may allow specialized reconstruction of these constants and a possibly stronger published sparse-band theorem could exist. This is an analytical self-reviewed result, without independent audit or independently confirmed priority.

## References
[1] F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424 (first public 2004-08-31); also *SIAM Review* 48 (2006), 504–536.

[2] V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first public 2021-03-26), especially Theorem 3.7 and Section 3.3.

[3] *Exact half-energy multiplicities for hemispherical spherical Slepian concentration with arbitrary degree masks*, public research finding, 2026-10-11, identifier ending `0284b88cef7a`.
