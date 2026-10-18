# Sharp sixth Fourier moment and complete extremizers for the five-frequency cross

## Finding
Let \(\mathbb T^2\) have normalized Haar measure and consider the centered five-point cross
\[
S=\{(0,0),(1,0),(-1,0),(0,1),(0,-1)\}\subset\mathbb Z^2.
\]
For arbitrary complex numbers \(c,a,b,d,e\), put
\[
P(z,w)=c+az+bz^{-1}+dw+ew^{-1},\qquad M=|c|^2+|a|^2+|b|^2+|d|^2+|e|^2.
\]
The exact sharp sixth-power Fourier synthesis inequality is
\[
\boxed{\int_{\mathbb T^2}|P(z,w)|^6\,dm(z,w)\le
\left(\frac{25}{8}+\frac{35\sqrt{105}}{72}\right)M^3.}
\]
The sixth-power constant is \(8.106156622341471\ldots\). Define
\[
\rho=\sqrt{\frac{3\sqrt{105}-25}{4}}=1.1980037873353\ldots.
\]
Every nonzero equality case, and no other, is
\[
\boxed{(c,a,b,d,e)=\lambda\left(\rho,\eta,\eta^{-1},\xi,\xi^{-1}\right),
\quad\lambda\in\mathbb C\setminus\{0\},\quad |\eta|=|\xi|=1.}
\]
Exactly the same constant and equality cases apply to the normalized sixth moment on the sampled square torus \(\mu_N\times\mu_N\) for every integer \(N\ge7\), where \(\mu_N=\{z\in\mathbb C:z^N=1\}\). The no-aliasing threshold is sharp for this constant: at \(N=6\), the displayed positive extremizer has a strictly larger sampled sixth moment than its continuous sixth moment.

## Assumptions and scope
All torus integrals and finite-grid sums are probability normalized. Coefficients may vanish, but equality for a nonzero coefficient vector forces all five nonzero. The coefficient energy \(M\) is the unweighted square norm; no Fourier-transform scaling is implicit. The infinite-order dual frequencies are precisely the five lattice points in \(S\). For finite grids, only the no-third-order-aliasing orders \(N\ge7\) are asserted. There is no claim of sharp values at orders \(2\) through \(6\), of other Fourier supports, or of operator norm bounds at noneven exponents.

## Proof
**1. Majorization and exact cubic convolution.** Fourier orthogonality gives
\[
\int_{\mathbb T^2}|P|^6=\sum_{v\in\mathbb Z^2}\left|\sum_{s_1+s_2+s_3=v} c_{s_1}c_{s_2}c_{s_3}\right|^2,
\]
where \(c_{(0,0)}=c\), \(c_{(1,0)}=a\), \(c_{(-1,0)}=b\), \(c_{(0,1)}=d\), and \(c_{(0,-1)}=e\). The triangle inequality bounds this by the same expression formed from the five coefficient moduli. Thus set \(c,a,b,d,e\ge0\) until the final equality analysis. Introduce
\[
k=c^2,\quad R=a^2+b^2,\quad T=d^2+e^2,\quad Z=ab,\quad W=de.
\]
Direct enumeration of the 25 distinct triple-sum frequencies and collection of the nonnegative monomials yields the exact polynomial
\[
\begin{aligned}
F={}&k^3+k^2\bigl(9(R+T)+12(Z+W)\bigr)\\
&+k\bigl(9(R^2+T^2)+36RT+18(RZ+TW)
+36(RW+TZ)+18(Z^2+W^2)+72ZW\bigr)\\
&+R^3+T^3+9RT(R+T)\\
&+6(R+3T)Z^2+6(3R+T)W^2+36(R+T)ZW.
\end{aligned}
\tag{1}
\]
This is an identity for the squared sixth moment of the nonnegative polynomial, not an empirical fit. All coefficients in (1) are nonnegative; in particular \(F\) is nondecreasing in the two products \(Z,W\) when the squared masses \(k,R,T\) are held fixed.

**2. Opposite-pair symmetrization.** Arithmetic-geometric mean gives \(0\le Z\le R/2\), \(0\le W\le T/2\), with equality, respectively, precisely when \(a=b\) and \(d=e\), unless the pair is zero. Replacing \(Z,W\) by \(R/2,T/2\) therefore does not decrease (1) and preserves \(M=k+R+T\). Write \(U=R+T\), \(v=R-T\). Substitution and exact simplification give
\[
\boxed{F_{\rm sym}=\frac14\Bigl(25U^3+135U^2k+60Uk^2+4k^3-15(U+3k)v^2\Bigr).}
\tag{2}
\]
Since \(U,k\ge0\), this is maximized at \(v=0\) when \(U>0\), proving that the two opposite-pair squared masses are equal at any nontrivial maximum involving an arm.

**3. Sharp one-variable calculation.** For \(M>0\), put \(x=k/M\in[0,1]\), so \(U/M=1-x\). Equation (2) gives
\[
\frac{F}{M^3}\le f(x):=\frac{27}{2}x^3-\frac{135}{4}x^2+15x+\frac{25}{4}.
\]
Its derivative factors as
\[
f'(x)=\frac32(27x^2-45x+10).
\]
The unique critical point in \([0,1]\) is
\[
x_*=\frac{15-\sqrt{105}}{18}.
\]
The derivative is positive before \(x_*\) and negative after \(x_*\); the second quadratic root exceeds one. Furthermore \(f(0)=25/4\), \(f(1)=1\), and
\[
f(x_*)=\frac{25}{8}+\frac{35\sqrt{105}}{72}.
\]
This proves the global sharp bound with an interior, strictly positive squared-mass profile. From \(R=T=(M-k)/2\) and equality within each pair, all arm coefficients have common modulus \(\sqrt{(M-k)/4}\). The center-to-arm modulus ratio squared equals
\[
\frac{k}{(M-k)/4}=\frac{4x_*}{1-x_*}=\frac{3\sqrt{105}-25}{4}=\rho^2.
\]

**4. Complete complex equality classification.** The unique amplitude optimizer has \(k,R,T,Z,W>0\). Strict increase of (1) in \(Z,W\) there forces \(a=b\), \(d=e\) in modulus; strict negativity of the \(v^2\) term in (2) forces \(R=T\). Equality in the original complex triangle majorization requires alignment among the nonzero cubic-convolution contributions at frequency \((0,0)\). These include \(c^3\), \(6cab\) and \(6cde\), hence necessarily
\[
\arg(a)+\arg(b)\equiv2\arg(c),\qquad
\arg(d)+\arg(e)\equiv2\arg(c)\pmod{2\pi}.
\]
Together with equal opposite-pair moduli, these conditions are exactly the displayed \(\lambda,\eta,\xi\) family. Conversely that family makes every monomial contributing to any fixed triple-sum frequency have the common phase associated with that frequency, so triangle majorization is equality throughout. This establishes necessity and sufficiency with no unexamined asymmetric or zero-coefficient cases.

**5. Sampled grids and the sharp cutoff.** Each triple-sum frequency has both coordinates in \([-3,3]\). If \(N\ge7\), reduction modulo \(N\) is injective on that square, so Fourier orthogonality yields precisely the continuous sum of the squares of the triple-convolution coefficients, including its equality classification. At \(N=6\), frequencies \((3,0)\) and \((-3,0)\) alias. For the positive optimizer, the corresponding coefficients are both strictly positive, so the sampled sixth moment is strictly larger than the continuous sixth moment. The two moments use the same \(M\), proving failure of this sharp constant at \(N=6\).

## Verification
The accompanying standard-library-only `artifacts/verify.py` independently expands the 25 triple-sum fibers with exact rational polynomial arithmetic, checks all 50 monomials of (1), confirms (2) and the cubic optimization formula symbolically, and carries out deterministic complex-coefficient and finite-grid checks. Reproduce with `python artifacts/verify.py` in this document's directory. The complete output of that run is `artifacts/verification_output.txt`. Finite grids and random test vectors corroborate the identities but do not replace the universal proof in steps 1--5.

## Relationship to prior work
Ciccone and Gonçalves (arXiv:2208.09441v1, public 2022-08-19) establish sharp Fourier extension results on the Euclidean circle under an arithmetic \(\mathrm{P}(3)\) condition. Their geometry and Bessel-integral estimates do not provide this arbitrary-coefficient sixth-moment constant for a fixed five-frequency lattice cross. Schippa (arXiv:2407.01830v1, public 2024-07-01) gives quasiperiodic Strichartz bounds using decoupling, not the exact finite-dimensional maximization and equality conditions here. Deng, Germain, Guth and Myerson (arXiv:1810.05630v1, public 2018-10-12) treat dispersive Strichartz estimates on nonrectangular two-tori, not this sharp five-coefficient static moment.

Related available sharp sixth-moment results for four consecutive integer frequencies and for three consecutive frequencies use different additive triple-sum fibers and have different constants and extremizers. A general Boolean-rectangle \(\Lambda(6)\) tensor inequality does not subsume the five-point cross: the cross is not a Boolean Cartesian product under an invertible affine lattice map. Previous fourth-moment results for a five-point cross, or for full finite-group axis unions, do not imply this sixth-moment result. Direct searches for the same five-mode cross, its centered diamond aliases, and the numerical radical constant did not locate an identical statement. Search absence is not proof of absolute priority.

## Limitations
The six-power sharp constant and complete equality family are established only for the stated five-frequency cross on the continuous torus and no-aliasing square grids. The case \(N=6\) establishes that the continuous sharp constant fails there, not its replacement optimal constant. The theorem does not determine the full sixth-moment distribution or other exponent norms. The originality assessment is best-knowledge; older or unindexed extremal-polynomial or Nikolskii inequalities may state an equivalent result in a different normalization. No independent scientific audit has been performed.

## References
1. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle under Arithmetic Constraints*, arXiv:2208.09441v1, first publicly posted 2022-08-19, https://arxiv.org/abs/2208.09441 .
2. R. Schippa, *Strichartz estimates for quasi-periodic functions and applications*, arXiv:2407.01830v1, first publicly posted 2024-07-01, https://arxiv.org/abs/2407.01830 .
3. Y. Deng, P. Germain, L. Guth and S. Myerson, *Strichartz estimates for the Schrödinger equation on non-rectangular two-dimensional tori*, arXiv:1810.05630v1, first publicly posted 2018-10-12, https://arxiv.org/abs/1810.05630 .
4. *Sharp sixth-moment Fourier norm via four-term even-moment symmetrization*, published-finding corpus research record `f3e238ebf219`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-fourier-norm-via-four-term-even-moment-symmet--f3e238ebf219 .
5. *Sharp sixth moments and the order-seven transition for three-character progressions*, published-finding corpus research record `1a8e79d7e85a`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moments-and-the-order-seven-transition-for-three-cha--1a8e79d7e85a .
6. *Sharp \(\Lambda(6)\) constant and rigidity for the Boolean rectangular spectrum*, published-finding corpus research record `c92f795fa200`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-lambda-6-constant-and-rigidity-for-the-boolean-rectangular--c92f795fa200 .
