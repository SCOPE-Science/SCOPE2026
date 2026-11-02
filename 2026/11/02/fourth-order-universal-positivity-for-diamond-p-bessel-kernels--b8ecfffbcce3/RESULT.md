# Fourth-order universal positivity for diamond \(p\)-Bessel kernels

## Finding

For the generalized \(p\)-Bessel functions of Kitajima, at the first non-Euclidean polygonal value \(p=1\) (the diamond), the **integer-order universal sign classification** is
\[
\forall m\in\mathbb Z_{\ge0}:\quad
\left[\mathcal J_{m,\varphi}^{[1]}(r)>0\text{ for all }r>0\text{ and }\varphi\in[0,2\pi)\right]
\quad\Longleftrightarrow\quad m\ge4.
\]
Moreover, strict positivity holds for **every real order** \(\omega\ge4\), not only integers. For each integer order \(m=0,1,2,3\), an explicit angle and positive radius make the kernel strictly negative. No assertion is made about the complete positivity range of nonintegral orders between zero and four.

The core identity is an exact divided difference. Write \(a=\cos^2\varphi\), \(b=\sin^2\varphi\), so \(a,b\ge0\) and \(a+b=1\). Set
\[
H_r(x)=\begin{cases}
\dfrac{1-\sin(rx)/(rx)}{x^2},&x>0,\\[3pt]
\dfrac{r^2}{6},&x=0.
\end{cases}
\]
Then for every \(r>0\),
\[
\mathcal J_{4,\varphi}^{[1]}(r)=
\begin{cases}
4\dfrac{H_r(a)-H_r(b)}{b-a},&a\ne b,\\[6pt]
-4H'_r(a),&a=b=1/2.
\end{cases}
\]
The function \(H_r\) is strictly decreasing on \([0,1]\), so both expressions are strictly positive.

## Assumptions and scope

We use the normalization and distorted-angle variable from Kitajima, *Analytic Study of \(p\)-Bessel Functions* (arXiv:2603.21072, equations (1.1)–(1.2)). In the special case \(p=1\), its series simplifies identically to
\[
\mathcal J_{\omega,\varphi}^{[1]}(r)
=4\sum_{k=0}^\infty\frac{(-1)^k r^{2k+\omega}}{\Gamma(2k+\omega+2)}
\sum_{j=0}^k a^{2j}b^{2(k-j)},\quad
\omega\ge0,\;r\ge0.
\]
The sum is absolutely convergent on every compact interval. This definition is not the classical Bessel \(J_\omega\), nor a normalization to value one at the origin. Indeed, \(\mathcal J_{0,\varphi}^{[1]}(0)=4\).

The claim concerns all real radii \(r>0\), all distorted angles, and all real orders \(\omega\ge4\), plus a complete classification at nonnegative integer orders. It does not concern other \(p\)-circles, unrestricted complex arguments, or a classification of nonintegral orders below four.

## Proof

**1. Exact order-four formula.** The source's order-raising identity at \(p=1\) reads
\[
\mathcal J_{\omega+1,\varphi}^{[1]}(r)=r\int_0^1 t\,\mathcal J_{\omega,\varphi}^{[1]}(rt)\,dt.
\]
Alternatively, directly integrating the \(p=1\) zero-order formula \(4\int_0^1\cos(ra(1-u))\cos(rbu)\,du\) and applying this identity successively gives, for \(a\ne b\),
\[
\begin{aligned}
\mathcal J_{0,\varphi}^{[1]}(r)&=\frac{4\{b\sin(rb)-a\sin(ra)\}}{r(b-a)},\\
\mathcal J_{1,\varphi}^{[1]}(r)&=\frac{4\{\cos(ra)-\cos(rb)\}}{r(b-a)},\\
\mathcal J_{2,\varphi}^{[1]}(r)&=\frac4{r(b-a)}\left(\frac{\sin(ra)}a-\frac{\sin(rb)}b\right),\\
\mathcal J_{3,\varphi}^{[1]}(r)&=\frac4{r(b-a)}\left(\frac{1-\cos(ra)}{a^2}-\frac{1-\cos(rb)}{b^2}\right),\\
\mathcal J_{4,\varphi}^{[1]}(r)&=\frac4{b-a}\{H_r(a)-H_r(b)\}.
\end{aligned}
\]
These displayed intermediate formulas are interpreted by their continuous limits at \(a=0\), \(b=0\), and \(a=b\), rather than by division by zero. The last identity also follows directly from the defining series: the divided-difference coefficient identity
\[
\frac{a^{2k+2}-b^{2k+2}}{a-b}
=(a+b)\sum_{j=0}^ka^{2j}b^{2(k-j)}
=\sum_{j=0}^ka^{2j}b^{2(k-j)}
\]
recovers every coefficient, with the derivative limit when \(a=b\).

**2. Strict decrease.** For \(x>0\), with \(t=rx\),
\[
H_r'(x)=\frac{3\sin t-t(2+\cos t)}{r x^4}.
\]
Set \(F(t)=t(2+\cos t)-3\sin t\). On \(0<t\le\pi\), one has \(F(0)=F'(0)=F''(0)=0\) and \(F'''(t)=t\sin t>0\); thus \(F(t)>0\). For \(t\ge\pi\), \(F(t)\ge t-3>0\). Therefore \(H'_r(x)<0\) for every \(x>0\). By continuity at zero, \(H_r\) decreases strictly on \([0,1]\). The divided-difference expression gives \(\mathcal J_{4,\varphi}^{[1]}(r)>0\) for every radius and angle, including the diagonal limiting case.

**3. All real higher orders.** The positive order-raising integral, for any \(\gamma>0\), is
\[
\mathcal J_{4+\gamma,\varphi}^{[1]}(r)
=\frac{r^\gamma}{\Gamma(\gamma)}\int_0^1
 t(1-t)^{\gamma-1}\mathcal J_{4,\varphi}^{[1]}(rt)\,dt.
\]
Its integrand is strictly positive for \(0<t<1\), so every real order \(\omega>4\) inherits strict positivity.

**4. Sharpness among integer orders.** There are four explicit negative values:
\[
\begin{array}{lll}
 m=0:&\varphi=0,\ r=3\pi/2,
 &\mathcal J_{0,0}^{[1]}(r)=-8/(3\pi);\\
 m=1:&\varphi=\pi/4,\ r=3\pi,
 &\mathcal J_{1,\pi/4}^{[1]}(r)=-4;\\
 m=2:&\varphi=\pi/4,\ r=4\pi,
 &\mathcal J_{2,\pi/4}^{[1]}(r)=-8;\\
 m=3:&\cos^2\varphi=2/5,\ r=5\pi,
 &\mathcal J_{3,\varphi}^{[1]}(r)=-200/(9\pi).
\end{array}
\]
These values follow by substitution in the elementary trigonometric formulas above and their continuous limits. They rule out universal nonnegativity at every smaller nonnegative integer order. This completes the integer-order classification.

## Verification

The standalone `CHECK.py` is a Python 3 standard-library supplementary checker. It checks the exact rational divided-difference coefficients at 96 combinations, compares the order-four closed form against an independently evaluated defining series at 42 angle-radius pairs, tests positive signs, and checks all four negative witness signs (184 assertions total). Run with `python3 CHECK.py` in the directory containing this file. This finite checking is **not** used to prove monotonicity on the continuum or positivity at all radii; the analytical derivative and positive raising integral are the complete proof.

## Relationship to prior work

Kitajima (2026, arXiv:2603.21072) introduced the relevant order-raising and integral formulas, studied the axis asymptotics and complex extension, but the inspected full text does not state all-angle sign positivity at order four or its exact integer-order threshold. The earlier open-access Hardy-type identity paper by Kitajima establishes the same underlying generalized Bessel functions and their differential recurrence; it does not give this positivity classification. Those definitions and structural identities are **inputs**, not claimed discoveries.

The analysis is a new strict divided-difference application and the negative witnesses identify sharpness among natural integer orders. The earlier general \(p\)-radial Bessel work of zu Castell (2008), and its connection to Berens–Xu \(\ell_1\)-radial summability, is relevant possible prior coverage; only the accessible abstract and linked discussion could be inspected, not the full restricted article. This originality assessment is provisional, not a certification of global uniqueness.

## Limitations

For noninteger orders \(0\le\omega<4\), the exact universal-sign threshold remains undetermined. The theorem concerns only the diamond case \(p=1\) and real \(r>0\). The separate all-angle positivity argument is not an assertion about zero-free complex planes or the whole \(p\)-Bessel hierarchy. No application to lattice-point discrepancy bounds is proved. Restricted older summability literature remains a material novelty risk. Independent mathematical validation has not been performed.

## References

1. M. Kitajima, *Analytic Study of \(p\)-Bessel Functions: Fractional Calculus, Integral Representations, and Complex Extensions*, arXiv:2603.21072 (first submitted 22 March 2026), especially (1.1), (1.3), Lemma 2.1. https://arxiv.org/abs/2603.21072 and https://arxiv.org/html/2603.21072
2. M. Kitajima, *Fourier-analytic derivation of Hardy-type oscillatory identity for \(p\)-circle domains by generalized Bessel functions*, Acta Mathematica Hungarica (2026), https://doi.org/10.1007/s10474-026-01632-9 (open-access full text).
3. W. zu Castell, *Generalized Bessel Functions for \(p\)-Radial Functions*, Constructive Approximation 27 (2008), 217–235, https://doi.org/10.1007/s00365-006-0666-z (restricted full text; abstract inspected).
