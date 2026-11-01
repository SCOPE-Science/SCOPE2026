# The first Fefferman–Szegő kernel zeros on quartic eggs occur in complex dimension eleven

## Finding
Let \(E_{n,2}=\{(z,w)\in\mathbb C^{n-1}\times\mathbb C:\|z\|^2+|w|^4<1\}\) and let \(S_{n,2}\) be the Fefferman-boundary-measure Szegő kernel described in [1]. For every integer \(2\le n\le10\), this kernel is zero-free on the Cartesian square of the egg. In the first subsequent dimension, \(n=11\), it has zeros. More precisely, its scalar auxiliary numerator has **exactly two simple zeros in the open unit disk**, a nonreal conjugate pair. Hence complex dimension eleven is the **first failure of zero-freeness** for the quartic-egg family.

## Assumptions and scope
The boundary measure is the Fefferman measure \(d\mu_F=M(\rho)^{1/(n+1)}d\sigma/|\nabla\rho|\), with \(\rho(z,w)=\|z\|^2+|w|^4-1\). The reproducing kernel and its normalization are those of Pendyala [1], not the Euclidean-surface Szegő kernel or the Bergman kernel. The integer dimension satisfies \(2\le n\le11\); no assertion concerns higher dimensions or exponents other than two.

Write \(k=n-1\), \(\mu=(n+2)/(2(n+1))\), and define
\[
X=\frac{w\overline\eta}{(1-\langle z,\zeta\rangle)^{1/2}},\qquad
P_n(X)=(1-X)^{k+1}\sum_{j=0}^{\infty}(\mu+j/2)_k X^j,
\]
where \((a)_k=\prod_{\ell=0}^{k-1}(a+\ell)\), and the square root uses the principal branch. By [1, Theorem 4.2], \(P_n\) is a real polynomial of degree at most \(k\) and
\[
S_{n,2}((z,w),(\zeta,\eta))
=C_{n,2}(1-\langle z,\zeta\rangle)^{-k-\mu}
\frac{P_n(X)}{(1-X)^n},\qquad C_{n,2}>0.
\]
The outer factors do not vanish at interior pairs.

## Proof
**1. The auxiliary disk is exactly the realizable scalar domain.** For two points of the egg, \(|w|^4<1-\|z\|^2\) and \(|\eta|^4<1-\|\zeta\|^2\). Cauchy–Schwarz for the ball gives
\[
|1-\langle z,\zeta\rangle|^2\ge(1-\|z\|^2)(1-\|\zeta\|^2),
\]
so \(|X|<1\). Conversely, any \(X\) in the unit disk is obtained by taking \(z=\zeta=0\), \(w=\sqrt{|X|}e^{i\arg X}\), and \(\eta=\sqrt{|X|}\) (with zero used for \(X=0\)). Thus kernel zeros are equivalent to unit-disk zeros of \(P_n\).

**2. Exact finite polynomials.** Put \(F_j=\prod_{\ell=0}^{k-1}(\mu+j/2+\ell)\). The generating-function formula in [1] gives
\[
P_n(X)=\sum_{r=0}^{k}c_rX^r,
\quad
c_r=\sum_{j=0}^{r}(-1)^{r-j}\binom{k+1}{r-j}F_j.
\]
All coefficients are rational, obtained without truncating an infinite series. Define the Cayley-transformed polynomial
\[
H_n(u)=(1+u)^kP_n\!\left(\frac{1-u}{1+u}\right).
\]
Because \(|(1-u)/(1+u)|<1\) exactly when \(\operatorname{Re}u>0\), counting open-unit-disk roots of \(P_n\) equals counting right-half-plane roots of \(H_n\), including multiplicity. There is no extraneous root at \(u=-1\): its value is \(2^kc_k\ne0\) for every dimension in the table below, and the transform preserves degree for these polynomials.

**3. An exact Routh–Hurwitz certificate.** Apply the classical Routh array to the coefficients of each \(H_n\), in descending degree. The first row contains alternating even-position coefficients and the second row the intervening coefficients; if successive rows are \(A,B\), the next row has entries \((B_0A_{j+1}-A_0B_{j+1})/B_0\). The all-rational computation gives the following complete first-column sign patterns (the lengths are \(n\)):

| \(n\) | First-column signs | Right-half-plane zero count |
|---:|:---:|---:|
| 2 | `++` | 0 |
| 3 | `+++` | 0 |
| 4 | `++++` | 0 |
| 5 | `+++++` | 0 |
| 6 | `++++++` | 0 |
| 7 | `+++++++` | 0 |
| 8 | `++++++++` | 0 |
| 9 | `+++++++++` | 0 |
| 10 | `++++++++++` | 0 |
| 11 | `++++++-++++` | 2 |

Every first-column pivot is strictly nonzero. Additionally, for each \(n\), the two real polynomials \(\operatorname{Re}H_n(iy)\) and \(\operatorname{Im}H_n(iy)\), in \(y\), have rational-polynomial greatest common divisor one. Thus **no imaginary-axis root** invalidates the classical Routh root count. The embedded `verify.py` constructs all coefficient arrays using exact rational fractions, checks every sign, and computes the ten polynomial gcds by exact Euclidean division. This supplies a finite, reproducible certificate, not an inference from approximate root samples.

**4. The first two interior zeros are nonreal and simple.** In dimension eleven, the numerator, up to a positive rational scalar, is
\[
\begin{aligned}
&6155307508685335 X^{10}-80947489858106014 X^9
+483519687000958179 X^8\\
&-1734339838473256872 X^7+4155117040406542782 X^6
-6983176482536683572 X^5\\
&+8388746524065666990 X^4-7166011355404282920 X^3
+4204932837187239531 X^2\\
&-1548326453534752606 X+275614142102538031.
\end{aligned}
\]
For \(0\le X<1\), the defining convergent series has strictly positive terms, hence \(P_{11}(X)>0\). All displayed coefficients alternate strictly, so \(P_{11}(-t)>0\) for every \(t\ge0\). Thus neither of the two disk roots is real. Real coefficients force them to be conjugate. Exact polynomial Euclidean division gives \(\gcd(P_{11},P_{11}')=1\), so both are simple. For orientation only, their approximations are \(X\approx0.5390488777\pm0.8174415443i\), with modulus approximately \(0.97917535\); their existence and count do not depend on these decimals.

This proves all assertions.

## Verification
Run `python3 verify.py` with Python 3 and no external dependencies. The program reconstructs \(P_n\), makes the Cayley transform, verifies all ten Routh sign arrays, checks the absence of roots on the imaginary axis by rational-polynomial gcd, verifies squarefreeness of \(P_{11}\), and checks the dimension-two normalization. Successful replay prints `EXACT_CERTIFICATE_OK`. This is an exact finite certificate paired with the analytical kernel identification and standard Routh root-count theorem.

## Relationship to prior work
Pendyala [1] establishes the Fefferman measure, monomial expansion, and rational auxiliary kernel formula for every integer dimension and axial exponent. The present result uses **that known formula** but identifies a previously unclassified interior zero geometry in its first nontrivial quartic family. In [1], complex polynomial zeros arise in curvature-rigidity arguments, which require only their existence somewhere in the complex plane; this does **not** imply an interior-disk root or locate the first dimension of nonvanishing failure.

Bhatnagar and Fan [2, Theorem 1.2] give an explicit two-dimensional Fefferman–Szegő formula; for the quartic case its numerator is proportional to \(4-X\), consistent with the zero-free \(n=2\) entry. Beberok [3] studies zeros of **Bergman**, rather than Fefferman–Szegő, kernels for intersections of ellipsoids, so its zero classifications do not imply this assertion.

## Limitations
Only the ten integers \(2\le n\le11\) and exponent \(m=2\) are certified. The two zeros are counted in the scalar auxiliary variable; the theorem does not enumerate pairs of points realizing them. Other exponents, dimensions \(n\ge12\), multiplicity behavior of more distant roots, and arbitrary boundary measures remain open here. Novelty comparison is based on the accessible sources and searches, not a proof of exhaustive historical uniqueness. No independent external mathematical audit has been performed.

## References
[1] V. S. Pendyala, *Fefferman–Szegő kernels and finite-type rigidity on egg domains*, arXiv:2607.04100, version 1, posted 2026-07-05. In particular, Theorems 3.2 and 4.2, Lemma 4.1, and Section 6. https://arxiv.org/abs/2607.04100

[2] A. Bhatnagar and J. Fan, *The invariant Szegő metric on Egg domains*, arXiv:2606.24452, version 1, posted 2026-06-23. In particular, Theorem 1.2 and Section 3.2. https://arxiv.org/abs/2606.24452

[3] T. Beberok, *The Bergman kernel: Explicit formulas, deflation, Lu Qi-Keng problem and Jacobi polynomials*, Czechoslovak Mathematical Journal 67 (2017), 537–549. https://doi.org/10.21136/CMJ.2017.0073-16
