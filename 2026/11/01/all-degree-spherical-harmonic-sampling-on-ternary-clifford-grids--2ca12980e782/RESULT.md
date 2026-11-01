# All-degree spherical-harmonic sampling on ternary Clifford grids

## Finding

For every integer \(d\ge2\), let \(\omega=e^{2\pi i/3}\) and let
\[
X_d=\left\{d^{-1/2}(\omega^{a_1},\ldots,\omega^{a_d}): a_i\in\{0,1,2\}\right\}\subset S^{2d-1}\subset\mathbb C^d\simeq\mathbb R^{2d}.
\]
Let \(E_{d,k}\) evaluate real homogeneous Euclidean spherical harmonics of **exact degree** \(k\ge0\) at all \(3^d\) points. For \(r\in(\mathbb Z/3\mathbb Z)^d\), write \(\chi_r(a)=\omega^{r\cdot a}\) and \(j(r)=\#\{i:r_i\ne0\}\). After complexification the image of \(E_{d,k}\) is exactly the span of characters with
\[
\begin{array}{ll}
 k=0:&j=0,\\
 k=1:&j=1,\\
 k=2:&j=1\text{ or }2,\\
 k\ge3:&0\le j\le\min(k,d).
\end{array}
\]
Thus its real rank is respectively \(1\), \(2d\), \(2d+4\binom d2\), and \(\sum_{j=0}^{\min(k,d)}\binom dj2^j\). In particular, exact-degree harmonics interpolate **arbitrary** real data on \(X_d\) precisely when \(k\ge\max\{d,3\}\). No greater degree has a rank defect.

The normalized Gegenbauer sampling matrix \(G_k=(P_k^{(2d)}(\langle x,y\rangle))_{x,y\in X_d}\), with \(P_k^{(2d)}(1)=1\), has eigenvalue
\[
\Lambda_{d,k,j}=\sum_{h=0}^d P_k^{(2d)}\!\left(1-\frac{3h}{2d}\right)[u^h](1-u)^j(1+2u)^{d-j}
\]
with multiplicity \(\binom dj2^j\), and this eigenvalue is strictly positive **exactly** in the corresponding listed support levels, zero elsewhere.

## Assumptions and scope

Integers satisfy \(d\ge2\) and \(k\ge0\). Harmonic means a homogeneous polynomial annihilated by the ordinary Euclidean Laplacian in \(2d\) real variables. The real vector space of their restrictions to the unit sphere is used, and complexification does not change evaluation rank. A point of \(X_d\) is indexed by \(a\in(\mathbb Z/3\mathbb Z)^d\). All sampling points have unit norm. The Gegenbauer normalization is \(P_0(t)=1\), \(P_1(t)=t\), and, for \(k\ge2\),
\[
P_k(t)=\frac{2k+2d-4}{k+2d-3}tP_{k-1}(t)-\frac{k-1}{k+2d-3}P_{k-2}(t).
\]

## Proof

**I. Fourier obstruction.** A polynomial of degree \(k\), evaluated on \(X_d\), is a linear combination of characters having at most \(k\) nonzero coordinate residues: each nonzero coordinate residue requires a factor from that coordinate plane. Thus \(j>k\) is impossible. The constant mode is unavailable for \(k=1\) because the sampling set is centered, and for \(k=2\) because its second moment is \(I_{2d}/(2d)\), so every harmonic quadratic has mean zero.

**II. All supported characters with at least two coordinates.** Write \(z_i=x_i+iy_i\). Each holomorphic or antiholomorphic monomial in mutually distinct coordinate planes is annihilated by \(4\sum_i\partial_{z_i}\partial_{\bar z_i}\). For \(j\ge2\) and \(k\ge j\), write \(k\) as a sum of \(j\) positive integers, none divisible by three: take \(j-2\) summands equal to one, and write the remaining integer \(s=k-j+2\ge2\) as a sum of two positive integers not divisible by three. This holds for \(s=2,3,4\) using \((1,1),(1,2),(2,2)\), and for every greater \(s\) by adding multiples of three to either summand. For each nonzero residue \(r_i\), select \(z_i^{m_i}\) or \(\bar z_i^{m_i}\) as appropriate. The harmonic product is exactly a nonzero scalar multiple of \(\chi_r\) on \(X_d\). This proves all levels \(2\le j\le\min(k,d)\).

**III. Easy one-coordinate and constant modes.** If \(j=1\) and \(3\nmid k\), a suitable \(z_i^k\) or \(\bar z_i^k\) samples as \(\chi_r\). If \(j=0\), and \(3\mid k\), the constant polynomial for \(k=0\) or the holomorphic monomial \(z_1^k\) for \(k>0\) samples as the constant character.

**IV. Remaining modes by null-quadric witnesses.** Fix a character \(r\). For test variables \(u_i=x_i+iy_i\), \(v_i=x_i-iy_i\), define the degree-\(k\) moment polynomial
\[
M_{r,k}(u,v)=\sum_{a\in(\mathbb Z/3\mathbb Z)^d}\overline{\chi_r(a)}\langle X_a,(x,y)\rangle^k.
\]
Up to a nonzero factor \(3^dk!/(2\sqrt d)^k\), the coefficient of \(\prod u_i^{a_i}v_i^{b_i}\) is \(\prod(a_i!b_i!)^{-1}\) when \(b_i-a_i\equiv r_i\pmod3\), and zero otherwise. Fischer decomposition of degree-\(k\) polynomials is \(\mathcal P_k=\mathcal H_k\oplus Q\mathcal P_{k-2}\), where \(Q=\sum_i u_iv_i\). Consequently, if this Fourier coefficient vanished on every degree-\(k\) harmonic, \(M_{r,k}\) would be divisible by \(Q\) and hence vanish on \(Q=0\).

Restrict to the complex null quadric using \(u_1=A\), \(v_1=Bt\), \(u_2=B\), \(v_2=-At\) and all remaining coordinates zero. The restriction satisfies \(Q=0\). For \(r=(1,0,\ldots,0)\) and \(3\mid k\), \(k\ge3\), the coefficient of \(A^{k-2}B^2t^2\), after removing the common nonzero prefactor, equals
\[
\frac{1}{2(k-2)!}-\frac{1}{(k-3)!}+\frac{\boldsymbol1_{k\ge4}}{4(k-4)!}=\frac{k^2-9k+16}{4(k-2)!}\ne0.
\]
The quadratic numerator has discriminant \(17\) and therefore no integral zero. The very same coefficient applies to \(r=0\) when \(k\equiv1\pmod3\) and \(k\ge4\). For \(r=0\), \(k\equiv2\pmod3\) and \(k\ge5\), the coefficient of \(A^{k-1}Bt\) equals
\[
\frac1{(k-1)!}-\frac1{(k-2)!}=\frac{2-k}{(k-1)!}\ne0.
\]
Thus every remaining listed character is detected by some degree-\(k\) harmonic. The apparent exceptional cases \(r=0,k=1\) and \(r=0,k=2\) were already excluded by the first two moments. Since evaluation is invariant under the full coordinatewise group \((\mathbb Z/3\mathbb Z)^d\), Fourier averaging projects any detected harmonic onto the entire one-dimensional character space. Combining I–IV establishes the asserted exact character images and ranks.

**V. Gram eigenvalues.** The addition formula for spherical harmonics identifies the positive-semidefinite kernel \(P_k^{(2d)}(\langle x,y\rangle)\) with the evaluation Gram kernel up to a positive scalar. Two ternary words at Hamming distance \(h\) have inner product \(1-3h/(2d)\). Fourier diagonalization of this translation-invariant kernel gives the displayed eigenvalues, because the character transform of a distance-\(h\) shell is \([u^h](1-u)^j(1+2u)^{d-j}\). A Gram eigenvalue is positive precisely for a character in the image, yielding strict positivity and all multiplicities.

## Verification

`checker.py` evaluates the normalized Gegenbauer recurrence and the explicit shell Fourier transforms in exact rational arithmetic for \(2\le d\le10\), \(0\le k\le24\), confirms 1,633 spectral/sign/character identities and verifies the null-quadric factorial coefficients through degree 60. Successful output: `TERNARY_HARMONIC_RANK_CHECK_OK 1633`. These computations corroborate but do not replace the above all-degree proof. The proof uses no numerical tolerance, and no external infinite-family certificate is asserted.

## Relationship to prior work

The Gegenbauer addition kernel and harmonic-index design perspective are standard, as developed for example by Bannai, Okuda and Tagami (2013), and by Zhu, Bannai, Bannai, Kim and Yu (2015). The present result concerns **exact-degree evaluation on the full Cartesian ternary phase grid**, not the finite-field polynomial Fourier band on a Hamming weight shell, classical harmonic-index design extremality, or full-space injectivity on a two-factor Hopf sampling grid. The theorem's new asserted content is the character-by-character all-degree rank and sharp surjective interpolation threshold for the specific Euclidean grid.

## Limitations

No claim is made about the optimal stability constants of interpolation or about arbitrary nonternary product grids. Literature comparisons were bounded and cannot rule out an equivalent statement in older association-scheme or spherical cubature literature. All scientific conclusions are subject to independent verification.

## References

1. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, first posted 2013-08-23. Source: https://arxiv.org/abs/1308.5101.
2. L. Zhu, E. Bannai, E. Bannai, H. Kim and W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373, first posted 2015-07-20. Source: https://arxiv.org/abs/1507.05373.
3. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388. DOI: 10.1007/BF03187604.
