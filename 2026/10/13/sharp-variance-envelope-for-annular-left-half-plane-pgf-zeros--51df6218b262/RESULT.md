# Sharp variance envelope for annular left-half-plane PGF zeros
## Finding
Let \(X\) be a random variable supported on \(\{0,\ldots,n\}\), with \(\mathbb P(X=0)\mathbb P(X=n)>0\), and let
\[
f_X(z)=\mathbb E[z^X].
\]
Fix \(R\ge1\). Assume every zero \(\zeta\) of \(f_X\) lies in the closed left half-plane and in the annulus
\[
R^{-1}\le |\zeta|\le R.
\]
Then
\[
\operatorname{Var}(X)\ge n\,C(R),
\qquad
C(R)=\min\left\{\frac{R}{(R+1)^2},\frac{2R^2}{(R^2+1)^2}\right\}.
\]
This constant is best possible uniformly over the degree. The first branch is attained for every \(n\) by
\[
f_X(z)=\left(\frac{R+z}{R+1}\right)^n,
\]
and the second branch is attained for every even \(n\) by
\[
f_X(z)=\left(\frac{R^2+z^2}{R^2+1}\right)^{n/2}.
\]
The two branches meet at the unique \(R_c\ge1\) satisfying \(R_c+R_c^{-1}=1+\sqrt5\), namely
\[
R_c=\frac{1+\sqrt5+\sqrt{2+2\sqrt5}}2.
\]
Thus negative-real zeros are extremal for \(1\le R\le R_c\), whereas imaginary-axis pairs are extremal for \(R\ge R_c\).

## Assumptions and scope
The endpoint masses are positive, so \(f_X\) has degree exactly \(n\) and no zero at the origin. Coefficients of \(f_X\) are real and nonnegative, hence nonreal zeros occur in conjugate pairs. The left-half-plane assumption is the closed condition \(\operatorname{Re}\zeta\le0\), equivalently \(|\arg\zeta|\ge\pi/2\) for nonzero roots.

The statement is an exact refinement of the annular zero-free variance problem in the special but natural left-half-plane regime. It does not claim the corresponding sharp constant for sectors narrower than a half-plane.

## Proof
Write the zeros of \(f_X\), with multiplicity, as \(\zeta_1,\ldots,\zeta_n\). Since \(f_X(1)=1\), the cumulant generating function of \(X\) is \(t\mapsto\log f_X(e^t)\), and differentiation of the root factorization gives
\[
\operatorname{Var}(X)
=
\sum_{j=1}^n -\frac{\zeta_j}{(1-\zeta_j)^2}.
\]
For a nonreal conjugate pair \(\zeta=re^{i\theta}\), \(\bar\zeta=re^{-i\theta}\), put \(c=\cos\theta\). Its contribution is twice
\[
q(r,c)=
\operatorname{Re}\left(-\frac{\zeta}{(1-\zeta)^2}\right)
=
\frac{r\left(2r-(r^2+1)c\right)}{(r^2-2rc+1)^2}.
\]
A negative real zero \(-r\) contributes \(q(r,-1)=r/(r+1)^2\). Because the zeros lie in the closed left half-plane, always \(-1\le c\le0\).

First note the exact inversion symmetry
\[
q(r,c)=q(r^{-1},c).
\]
It therefore suffices to minimize over \(1\le r\le R\). Direct differentiation gives
\[
\frac{\partial q}{\partial r}
=
\frac{(r-1)(r+1)\left(2c^2r+c(r^2+1)-4r\right)}{(r^2-2rc+1)^3}.
\]
For \(-1\le c\le0\),
\[
2c^2r+c(r^2+1)-4r\le2r-4r<0.
\]
Hence \(q(r,c)\) is nonincreasing in \(r\) for \(r\ge1\), and every allowed root contribution is at least the corresponding value at \(r=R\).

For fixed \(R\), differentiation in \(c\) yields
\[
\frac{\partial q}{\partial c}
=-\frac{R\left(R^4-6R^2+1+2cR(R^2+1)\right)}{(R^2-2Rc+1)^3}.
\]
The bracket in the numerator is affine and strictly increasing in \(c\). Therefore the derivative can change sign at most once, and if it changes sign it goes from positive to negative. Any interior critical point is consequently a maximum, so the minimum on \([-1,0]\) occurs at an endpoint. The endpoint values are
\[
q(R,-1)=\frac{R}{(R+1)^2},
\qquad
q(R,0)=\frac{2R^2}{(R^2+1)^2}.
\]
Thus every real root contribution, and the per-root average of every nonreal conjugate pair, is at least \(C(R)\). Summing over all \(n\) roots proves
\[
\operatorname{Var}(X)\ge nC(R).
\]

Sharpness is explicit. For
\[
f_X(z)=\left(\frac{R+z}{R+1}\right)^n,
\]
all roots equal \(-R\), and \(\operatorname{Var}(X)=nR/(R+1)^2\). For even \(n\),
\[
f_X(z)=\left(\frac{R^2+z^2}{R^2+1}\right)^{n/2}
\]
is a probability generating polynomial with roots \(\pm iR\), and its variance is \(2nR^2/(R^2+1)^2\). Hence neither branch can be increased in its active region.

Finally, equality of the two branch values is equivalent to
\[
R^4-2R^3-2R^2-2R+1=0.
\]
After division by \(R^2\) and setting \(s=R+R^{-1}\), this becomes \(s^2-2s-4=0\). Since \(s\ge2\) and is strictly increasing for \(R\ge1\), there is a unique crossover, with \(s=1+\sqrt5\), giving the stated \(R_c\).

## Verification
The proof is analytic and uses only the root factorization of a probability generating polynomial and two one-variable derivative sign arguments. The boundary examples are genuine probability generating functions with nonnegative coefficients and positive endpoint masses. At \(R=1\), the formula gives \(C(1)=1/4\); as \(R\to\infty\), the active branch is \(2R^2/(R^2+1)^2\sim2R^{-2}\).

The source theorem for a sector of angle parameter \(\delta\) gives, at \(\delta=\pi/2\), a lower bound of order \(R^{-4}n\) up to an absolute constant. The exact left-half-plane envelope above instead has order \(R^{-2}n\) and identifies the sharp constant and extremal zero geometries.

## Relationship to prior work
Michelen and Sahasrabudhe established a general annular zero-free lower bound
\[
\operatorname{Var}(X)\ge cR^{-2\pi/\delta}n
\]
when all zeros avoid the sector \(|\arg z|<\delta\), and explicitly identified closing the exponent gap with their sharpness examples as an open direction. Their paper also records the root-factorization expression for the variance, but does not state or derive the exact left-half-plane annular envelope above.

Their earlier work on central limit theorems from probability-generating zeros supplies the broader zero-geometry framework and has primary MSC 2020 classification 60F05. Heerten, Sambale and Thäle later studied probabilistic limit theorems for zero-free generating polynomials and explicitly treated Hurwitz polynomials, including nonreal left-half-plane examples. That work concerns cumulant bounds and asymptotic limit theorems rather than an exact annular variance minimum.

## Limitations
The theorem uses the closed left half-plane. It does not determine the sharp variance constant for a general sector \(|\arg z|\ge\delta\) with \(0<\delta<\pi/2\). On the second branch, exact attainment is exhibited for every even degree; the claim of optimality is uniform over degrees and does not assert attainment for every odd degree. No concentration-function constant is optimized here.

## References
1. M. Michelen and J. Sahasrabudhe, *Anti-concentration of random variables from zero-free regions*, Discrete Analysis 2022:13, arXiv:2102.07699, DOI 10.19086/da.38590.
2. M. Michelen and J. Sahasrabudhe, *Central limit theorems and the geometry of polynomials*, arXiv:1908.09020; J. Eur. Math. Soc., DOI 10.4171/JEMS/1530.
3. N. Heerten, H. Sambale and C. Thäle, *Probabilistic limit theorems induced by the zeros of polynomials*, Mathematische Nachrichten, DOI 10.1002/mana.202300109.
