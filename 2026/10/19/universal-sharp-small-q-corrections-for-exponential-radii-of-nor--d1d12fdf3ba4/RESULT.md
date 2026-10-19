# Universal sharp small-\(q\) corrections for exponential radii of normalized Jackson and Hahn–Exton Bessel functions

## Finding
Fix \(0<\nu\le1\). For \(s\in\{2,3\}\) and \(0<q<1\), put
\[
\lambda_2=\frac{q^{\nu+1}}{4(1-q)(1-q^{\nu+1})},\qquad
\lambda_3=\frac{q}{(1-q)(1-q^{\nu+1})},\qquad
\kappa_2=2,\quad\kappa_3=1,
\]
\[
\epsilon_s=\frac{q^{\kappa_s}}{1+q}\frac{1-q^{\nu+1}}{1-q^{\nu+2}},\qquad
\delta=1-e^{-1}.
\]
Let \(f_\nu^{(s)},g_\nu^{(s)},h_\nu^{(s)}\) denote the standard normalized Jackson (\(s=2\)) and Hahn–Exton (\(s=3\)) \(q\)-Bessel functions. Each is of the form
\[
F_{s,m,a}(z;q)=z\,B_s(\lambda_s z^m;q)^a,
\qquad (m,a)\in\left\{(2,1/\nu),(2,1),(1,1)\right\},
\]
with the three displayed pairs corresponding, respectively, to \(f,g,h\). Here the analytic branch near zero is chosen and \(B_s(0;q)=1\).

Write \(u=ma\) and \(v=1+u\). Define the positive numbers
\[
X_\star=\frac{\delta}{\delta+u},\qquad
A=v(\delta+u),\qquad H=\delta(v+1)+u(m+1),
\]
\[
X_c=\frac{2\delta}{H+\sqrt{H^2-4A\delta}},
\]
\[
Y_\star=X_\star^2(2-X_\star),
\]
\[
Y_c=X_c\frac{(a-1)\frac{2X_c-X_c^2}{(1-X_c)^2}
 +(1+2u)\frac{2X_c-vX_c^2}{(1-vX_c)^2}}
 {(a-1)\frac{1}{(1-X_c)^2}+\frac{v}{(1-vX_c)^2}}.
\]
In particular \(0<X_c<1/v\), and all four constants \(X_\star,X_c,Y_\star,Y_c\) are strictly positive.

Let \(R_{s,m,a}^{\star}(q)\) and \(R_{s,m,a}^{c}(q)\) be the *exact exponential starlikeness and convexity radii*: the maximal radii of centered disks on which, respectively,
\[
\left|\log\left(\frac{zF'(z)}{F(z)}\right)\right|<1,
\qquad
\left|\log\left(1+\frac{zF''(z)}{F'(z)}\right)\right|<1.
\]
For either \(t\in\{\star,c\}\), as \(q\downarrow0\),
\[
\boxed{\displaystyle
\lambda_s^{1/m}R_{s,m,a}^{t}(q)
=X_t^{1/m}\left(1+\frac{Y_t}{mX_t}\epsilon_s
+O_\nu(\epsilon_s^2)\right).}
\]
Every first correction is nonzero and positive. In particular, the first relative correction for Jackson has *sharp order* \(q^2\), whereas for Hahn–Exton it has sharp order \(q\). Their underlying normalized leading radii coincide, and their *unscaled* comparison is
\[
\boxed{\displaystyle
\frac{R_{2,m,a}^{t}(q)}{R_{3,m,a}^{t}(q)}
=4^{1/m}q^{-\nu/m}\left(1-\frac{Y_t}{mX_t}q+O_\nu(q^2)\right).}
\]
These are six function normalizations, each with two radii; at \(\nu=1\), the \(f\) and \(g\) normalizations coincide.

## Assumptions and scope
The order \(\nu\) is fixed in \((0,1]\); the parameter \(q\) tends to \(0\) through positive real values. The exponent range ensures \(a\ge1\), a critical condition for the convexity factorization. All stated \(O_\nu\) bounds are for fixed \(\nu\) and one of the three specified normalization pairs; uniformity at \(\nu=0\) is not asserted. The radii are defined on the maximal centered disks of analytic continuation, not truncated at radius one.

For clarity, set \((q;q)_n=\prod_{j=1}^{n}(1-q^j)\) and \((q^{\nu+1};q)_n=\prod_{j=1}^{n}(1-q^{\nu+j})\). The normalized base is explicitly
\[
B_s(x;q)=\sum_{n=0}^{\infty}(-1)^n b_{n,s}(q)x^n,\qquad
b_{n,s}(q)=q^{\kappa_s n(n-1)/2}
\frac{[(1-q)(1-q^{\nu+1})]^n}{(q;q)_n(q^{\nu+1};q)_n}.
\]
Thus \(b_{0,s}=b_{1,s}=1\), \(b_{2,s}=\epsilon_s\), and the above \(F\) equals the standard three normalizations from the cited literature after collecting powers of \(z\).

## Proof
**1. Exact series control.** The positive coefficient ratio is
\[
\frac{b_{n+1,s}}{b_{n,s}}
=q^{\kappa_s n}\frac{(1-q)(1-q^{\nu+1})}
{(1-q^{n+1})(1-q^{\nu+n+1})}\le q^{\kappa_s n}\quad(n\ge0).
\]
For every fixed disk \(|x|\le L\) and every fixed integer derivative order \(j\ge0\), this gives
\[
B_s(x;q)=1-x+\epsilon_s x^2+O_{L,j,\nu}(q^{3\kappa_s})
\]
with the same estimate after \(j\) differentiations of the displayed terms (for \(j>2\), the polynomial derivatives vanish). Since \(\epsilon_s\sim q^{\kappa_s}\), the remainder is \(O(\epsilon_s^2)\) in every fixed \(C^j\) norm on compact sets. The identities \(\epsilon_2=q\epsilon_3\) and \(\lambda_3/\lambda_2=4q^{-\nu}\) hold *exactly*.

**2. These are the actual sharp radii, not merely candidate roots.** For \(\nu>-1\), the established order-zero Hadamard products for the normalized Jackson and Hahn–Exton \(q\)-Bessel functions have only positive zeros in the squared variable; hence \(B_s(x;q)=\prod_j(1-x/\rho_j)\), with \(\rho_j>0\) and locally uniformly convergent logarithmic derivatives. Put \(D_s=B_s+uxB_s'\). The operation \(B\mapsto B+uxB'\) preserves strictly positive real roots for finite products: the derivative of \(x^{1/u}B(x)\) has exactly one zero between consecutive positive roots and one before the first; the number of roots matches the degree. Passing to the locally uniform infinite-product limit gives the same assertion for \(D_s\), by Hurwitz's theorem; its constant term is one. In particular, for \(x\) below the first zero of the relevant factors,
\[
S_s(x)=1+ux\frac{B_s'(x)}{B_s(x)},\qquad
C_s(x)=1+mx\left[(a-1)\frac{B_s'(x)}{B_s(x)}+\frac{D_s'(x)}{D_s(x)}\right]
\]
are continuous, strictly decreasing from one, and diverge negatively at the first applicable positive pole. Both have a unique first root at \(e^{-1}\). If \(|x|\le t\) lies inside those poles, each partial fraction satisfies \(|x/(\rho-x)|\le t/(\rho-t)\), and nonnegative weights \(u\), \(m(a-1)\), \(m\) show \(|S_s(x)-1|\le1-S_s(t)\) and \(|C_s(x)-1|\le1-C_s(t)\). If the corresponding real value exceeds \(e^{-1}\), the image lies inside the disk \(|w-1|<1-e^{-1}\), itself contained in \(|\log w|<1\). At the first positive root, the logarithm has modulus exactly one. Thus these roots give the exact exponential radii after \(x=\lambda_s r^m\). This also follows directly from the exact-radius characterizations in the first reference.

**3. Limiting equations and roots.** Replacing \(B_s\) by \(B_0=1-x\), \(D_s\) by \(D_0=1-vx\) gives
\[
S_0(x)=1-\frac{ux}{1-x},\qquad
C_0(x)=1-mx\left[\frac{a-1}{1-x}+\frac{v}{1-vx}\right].
\]
Both strictly decrease on the relevant positive intervals; their equations \(S_0=e^{-1}\) and \(C_0=e^{-1}\) give \(X_\star\) and the smaller root \(X_c\) of
\[
A x^2-Hx+\delta=0.
\]
The latter lies in \((0,1/v)\). The first derivatives of both limiting functions at their roots are strictly negative, so the compact convergence from Step 1 and the implicit-function estimate locate their small-\(q\) roots uniquely near those constants.

**4. First correction and sharpness of exponent.** Temporarily write \(B_\epsilon=1-x+\epsilon x^2\) and \(D_\epsilon=1-vx+(1+2u)\epsilon x^2\). Direct differentiation at \(\epsilon=0\) gives
\[
\partial_x S_0=-\frac{u}{(1-x)^2},\quad
\partial_\epsilon S_\epsilon\big|_0=\frac{ux(2x-x^2)}{(1-x)^2},
\]
\[
\partial_x C_0=-m\left[\frac{a-1}{(1-x)^2}+\frac{v}{(1-vx)^2}\right],
\]
\[
\partial_\epsilon C_\epsilon\big|_0
=mx\left[(a-1)\frac{2x-x^2}{(1-x)^2}
 +(1+2u)\frac{2x-vx^2}{(1-vx)^2}\right].
\]
The implicit shifts \(-\partial_\epsilon S/\partial_x S\) and \(-\partial_\epsilon C/\partial_x C\) at the limiting roots are exactly \(Y_\star\) and \(Y_c\). By Step 1, the error in each root is \(O_\nu(\epsilon_s^2)\). Taking the positive \(m\)-th root yields the claimed radius expansion. Since both \(Y\)'s are strictly positive, the orders \(q^{\kappa_s}\) cannot be improved to smaller-order remainders. Finally use the exact identities \(\epsilon_2=q\epsilon_3\) and \(\lambda_3/\lambda_2=4q^{-\nu}\) and the fact \(\epsilon_3=q+O(q^2)\) to obtain the Jackson/Hahn–Exton comparison law.

## Verification
Run `python verify_qbessel_radii.py` after installing `mpmath>=1.3.0`; the script implements the exact coefficient recurrence, locates the first relevant positive roots by high-precision bisection, checks positivity of the leading and first-correction constants, and compares all three normalizations and both geometry types at three orders and three values of \(q\). It also checks the exact coefficient identity \(\epsilon_2=q\epsilon_3\). These finite computations are diagnostic only: compact uniform tail control and the positive-zero argument in the proof establish the all-parameter result.

## Relationship to prior work
Kazımoğlu, Deniz, Cotîrlă and Breaz (2026) give exact positive-root equations for the same exponential radii, and establish the necessary positive-zero factorizations. Their results determine the radii implicitly for each \(q\), but do not provide the small-\(q\) scaled polynomial limit, the twelve explicit positive first-correction coefficients, or the Jackson/Hahn–Exton comparison with its nonzero linear term. The present theorem computes these asymptotic invariants, rather than reasserting the source's root equations. Baricz, Kumar and Singh (2024) study *ordinary* starlikeness radii in the *large-order* \(\nu\to\infty\) regime, which does not imply this fixed-order \(q\to0\) exponential-radius statement. Kazımoğlu (2024) treats a distinct spirallike target. Yasin and Raza (2026) also study exact exponential radii of these families; only their abstract could be reviewed, so unnoticed equivalent asymptotics remain a literature risk.

## Limitations
The theorem is a fixed-order, small-\(q\) asymptotic statement, not a global all-\(q\) ordering, a large-order asymptotic, or a result for \(q\)-Bessel–Struve families. No convergence uniform as \(\nu\downarrow0\) is claimed. The positive-real-zero factorizations are established background, not new. In principle the known implicit root equations uniquely determine the radii, but an explicit quantitative first-correction computation and its universality are distinct claims. The numerical script does not certify any infinite statement. 
## References
1. S. Kazımoğlu, E. Deniz, L.-I. Cotîrlă and D. Breaz, *Exponential radii of starlikeness and convexity of q-special functions*, Journal of Inequalities and Applications **2026**, article 74 (first published 20 April 2026), DOI: 10.1186/s13660-026-03480-1. Open full text: https://link.springer.com/article/10.1186/s13660-026-03480-1.
2. Á. Baricz, P. Kumar and S. Singh, *Asymptotic Expansions for the Radii of Starlikeness of Normalized q-Bessel Functions*, Results in Mathematics **79**, article 248 (2024), DOI: 10.1007/s00025-024-02277-2. Open full text: https://link.springer.com/article/10.1007/s00025-024-02277-2.
3. S. Kazımoğlu, *Radii of γ-Spirallike of q-Special Functions*, Mathematics **12** (2024), 2261, DOI: 10.3390/math12142261.
4. S. Yasin and M. Raza, *Exponential radii of starlikeness and convexity of q-Bessel and q-Bessel–Struve functions*, Mathematica Slovaca (2026), DOI: 10.1515/ms-2026-0151; bibliographic abstract only inspected.
