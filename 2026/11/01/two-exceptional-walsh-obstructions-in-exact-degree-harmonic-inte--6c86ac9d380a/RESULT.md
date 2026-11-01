# Two exceptional Walsh obstructions in exact-degree harmonic interpolation on the hypercube

## Finding

For every integer \(d\ge3\), let \(X_d=\{d^{-1/2}\varepsilon:\varepsilon\in\{-1,1\}^d\}\subset S^{d-1}\). Let \(\mathcal H_\ell(\mathbb R^d)\) be the complex vector space of homogeneous harmonic polynomials of degree \(\ell\), and let \(E_{d,\ell}:\mathcal H_\ell\to\mathbb C^{X_d}\) be the evaluation map. Then, for **every** integer \(\ell\ge0\),

\[
\operatorname{rank}E_{d,\ell}=\sum_{\substack{0\le k\le\min(d,\ell)\\k\equiv\ell\pmod2}}\binom dk-\mathbf1_{\{\ell=2\}}-\mathbf1_{\{\ell=d+2\}}.
\]

More precisely, identify \(\mathbb C^{X_d}\) with functions on the sign cube, with orthogonal Walsh characters \(\chi_S(\varepsilon)=\prod_{i\in S}\varepsilon_i\), indexed by \(S\subseteq\{1,\ldots,d\}\). The image of \(E_{d,\ell}\) is exactly the span of all \(\chi_S\) for which \(|S|\le\ell\) and \(|S|\equiv\ell\pmod2\), except that the constant character is absent at degree \(2\), and the full-product character \(\chi_{\{1,\ldots,d\}}\) is absent at degree \(d+2\).

Thus, for every \(d\ge3\), all parity-compatible sample data are interpolable at degree \(d\); precisely one parity-compatible direction becomes unavailable at degree \(d+2\); and all parity-compatible assignments are again interpolable for every degree \(\ell\ge d+3\). This is an exact-degree statement, not a cumulative-band statement.

## Assumptions and scope

The ambient dimension \(d\) is any integer at least \(3\); the harmonic degree \(\ell\) is any nonnegative integer. Scalar fields may be taken real by complexification and conjugation symmetry. The cube vertices lie on the unit sphere. All assertions concern restriction of a **single** homogeneous harmonic degree to all \(2^d\) vertices, with no rotation or smoothing.

## Proof

**1. Walsh sectors and harmonic moment test.** Coordinate sign changes act transitively on \(X_d\), preserve \(\mathcal H_\ell\), and diagonalize \(\mathbb C^{X_d}\) into the one-dimensional Walsh characters. Hence an individual character belongs to the evaluation image precisely when its coefficient functional on \(\mathcal H_\ell\) is nonzero. After removing the harmless scale \(d^{-\ell/2}\), this functional is

\[
L_{S,\ell}(H)=2^{-d}\sum_{\varepsilon\in\{\pm1\}^d}\chi_S(\varepsilon)H(\varepsilon).
\]

For \(z\in\mathbb C^d\), define the associated homogeneous moment polynomial

\[
M_{S,\ell}(z)=L_{S,\ell}((z\cdot x)^\ell)
=\ell!\,[t^\ell]\prod_{i\in S}\sinh(tz_i)\prod_{j\notin S}\cosh(tz_j).
\]

For any \(z\) on the complex quadratic cone \(q(z)=\sum_i z_i^2=0\), the polynomial \((z\cdot x)^\ell\) is harmonic because its Laplacian is \(\ell(\ell-1)q(z)(z\cdot x)^{\ell-2}\). Conversely, nonvanishing of the coefficient functional on any harmonic polynomial is equivalent to nonvanishing of \(M_{S,\ell}\) somewhere on this cone. To see the converse without assuming that every harmonic is one such power, use the Fischer pairing: \(\mathcal P_\ell=\mathcal H_\ell\oplus q\mathcal P_{\ell-2}\), orthogonally. A moment polynomial annihilates all harmonics precisely when it belongs to \(q\mathcal P_{\ell-2}\), which, since \(q\) is irreducible over \(\mathbb C\) for \(d\ge3\), is equivalent to vanishing identically on the null cone. Here \(\mathcal P_j\) denotes homogeneous polynomials of degree \(j\), with \(\mathcal P_j=0\) for \(j<0\).

The generating product vanishes in degrees below \(k=|S|\), and its nonzero terms have parity \(k\). This proves all the formal exclusions \(k>\ell\) or \(k\not\equiv\ell\pmod2\).

**2. Mixed Walsh weights.** Let \(1\le k\le d-1\), choose index \(1\in S\) and index \(2\notin S\), and put \(z_1=1\), \(z_2=i\sqrt{1+\sum_{j\in S\setminus\{1\}}u_j^2}\), \(z_j=u_j\) for other \(j\in S\), with all remaining entries zero. Then \(q(z)=0\). The coefficient of \(\prod_{j\in S\setminus\{1\}}u_j\) in the generating product is

\[
t^{k-1}\sinh t\cos t.
\]

Consequently, for every \(m\ge0\) and \(\ell=k+2m\), the indicated parameter coefficient of \(M_{S,\ell}/\ell!\) equals

\[
[t^{2m+1}]\sinh t\cos t=\frac{\operatorname{Re}(1+i)^{2m+1}}{(2m+1)!}\ne0.
\]

The last numerator has absolute value \(2^m\), proving presence of every allowed mixed-weight character.

**3. Constant Walsh weight.** When \(S=\varnothing\), the first degree \(\ell=0\) is present. At degree \(\ell=2\), \(M_{\varnothing,2}\) is a nonzero multiple of \(q(z)\), and so the constant character is absent. For \(\ell=2m\) with \(m\) even, take the null vector \(z=(1,i,0,\ldots,0)\). The moment generating product reduces to \(\cosh t\cos t\), and

\[
[t^{2m}]\cosh t\cos t=\frac{(-1)^{m/2}2^m}{(2m)!}\ne0.
\]

For odd \(m\ge3\), use the null vector \(z=(1,\sqrt h,i\sqrt{1+h},0,\ldots,0)\) and vary \(h\) near zero. The derivative at \(h=0\) of its generating product is

\[
\cosh t\left(\frac{t^2}2\cos t-\frac t2\sin t\right).
\]

Its coefficient of \(t^{2m}\) is exactly

\[
\frac{(-1)^{(m-1)/2}2^{m-1}(m-1)}{(2m-1)!}\ne0.
\]

Thus degree \(2\) is the **only** permitted degree at which the constant character is absent.

**4. Full-product Walsh weight.** When \(S=\{1,\ldots,d\}\), the coefficient at degree \(\ell=d\) is \(\prod_i z_i\), so the character is present. The degree-\(d+2\) coefficient is a constant multiple of \((\prod_i z_i)q(z)\); it vanishes on the null cone and hence the full-product character is absent. More generally let \(\ell=d+2m\). Choose the formal null vector

\[
z_1=1,\qquad z_2=i\sqrt{1+\sum_{j=3}^d u_j^2},\qquad z_j=u_j\ (3\le j\le d).
\]

The coefficient of \(\prod_{j=3}^d u_j\) in \(\prod_i\sinh(tz_i)\) equals \(i t^{d-2}\sinh t\sin t\). If \(m\) is even, the coefficient at total degree \(d+2m\) is nonzero since

\[
[t^{2m+2}]\sinh t\sin t=\frac{(-1)^{m/2}2^{m+1}}{(2m+2)!}\ne0.
\]

For odd \(m\ge3\), set \(u_3=\sqrt h\), take first-order coefficients in \(u_4,\ldots,u_d\) and the leading factor \(\sqrt h\), and differentiate the remaining formal power series with respect to \(h\) at zero. Apart from the nonzero factor \(i t^{d-2}\), this derivative is

\[
\sinh t\left(\frac t2\cos t+\frac{t^2}6\sin t\right).
\]

Its coefficient at degree \(2m+2\) is

\[
\frac{(-1)^{(m-1)/2}2^m(m-1)}{3(2m+1)!}\ne0.
\]

This proves the presence of the full-product character in every permitted degree except \(d+2\). Together with steps 1–3 it proves both the complete image characterization and the rank formula. The interpolation consequences follow because the sum of all binomial multiplicities of a fixed parity equals \(2^{d-1}\).

## Verification

The accompanying standalone script `cube_harmonic_rank_checker.py` computes exact rational Gegenbauer values at every Hamming inner product, then diagonalizes the evaluation Gram kernel by finite Walsh sums. It verifies the stated nonzero/zero sectors in dimensions \(3\) through \(8\) and harmonic degrees \(0\) through \(18\) (741 exact sector comparisons). No floating point thresholds are used. Symbolic Taylor expansions independently confirm the two derivative-coefficient identities in odd indices \(m=1,3,5,7\). The proof above, not these finite checks, establishes all dimensions and degrees.

## Relationship to prior work

Bannai, Okuda and Tagami develop harmonic-index spherical designs and the associated Gegenbauer reproducing kernels (2013); the vanishing constant Walsh sector at degree \(2\) is consistent with the classical cubical spherical \(3\)-design observation. Moore and Russell (2014), especially their Appendix A, give a Krawtchouk–Gegenbauer formula for the energy of an arbitrary Walsh coefficient after restriction of a randomly rotated spherical harmonic to a cube. That spectral identity is prior work, not claimed here. The present result evaluates **exactly which** of those spectral sectors vanish for **all** dimensions and harmonic degrees, supplying the uniform closed rank formula and the isolated top-parity reentrant defect. Related harmonic analysis on Boolean Hamming shells treats a different sample domain and bandwidth.

## Limitations

The theorem concerns equal-radius Boolean cube vertices only. It gives exact ranks and missing Walsh directions, not quantitative positive singular values or interpolation condition numbers. No generalization to nonsymmetric perturbed point sets is claimed. The originality assessment is bounded: equivalent rank statements in older representation-theoretic or sampling literature have not been ruled out exhaustively. No independent mathematical validation is claimed.

## References

1. E. Bannai, T. Okuda, and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1, 23 August 2013. https://arxiv.org/abs/1308.5101
2. C. Moore and A. Russell, *Heat and Noise on Cubes and Spheres: The Sensitivity of Randomly Rotated Polynomial Threshold Functions*, arXiv:1408.5425v1, 22 August 2014, especially Section 7 and Appendix A. https://arxiv.org/abs/1408.5425
