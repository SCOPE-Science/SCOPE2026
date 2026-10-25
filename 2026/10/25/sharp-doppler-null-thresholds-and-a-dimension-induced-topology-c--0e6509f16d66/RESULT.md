# Sharp Doppler null thresholds and a dimension-induced topology change for positive radial Gaussian polynomials

## Finding

Let \(d\ge1\) be an integer and \(c>0\). For the everywhere strictly positive radial Schwartz window
\[
g_{d,c}(x)=(|x|^2+c)e^{-|x|^2/2},\qquad x\in\mathbb R^d,
\]
define its angular-frequency centered self-ambiguity
\[
A_{d,c}(T,\omega)=\int_{\mathbb R^d}g_{d,c}(u+T/2)g_{d,c}(u-T/2)e^{-i\omega\cdot u}\,du.
\]
Write \(X=|T|^2\), \(Y=|\omega|^2\), \(Z=(T\cdot\omega)^2\), \(a=4c+2d-4\), and \(Y_0=2c+3d/2-1\). The real ambiguity transform is
\[
A_{d,c}(T,\omega)=\frac{\pi^{d/2}}{16}e^{-(X+Y)/4}\bigl[(X-Y+a)^2+4Z-16(Y-Y_0)\bigr].\tag{1}
\]

**A sharp dimensional change occurs.** In dimension one the entire real zero set comprises exactly two smooth disjoint compact embedded ovals (one at positive Doppler frequency and one at negative Doppler frequency). Every zero satisfies the sharp delay bound
\[
|T|^2\le\frac{4c+3}{2c+1}=2+\frac1{2c+1}<3,\tag{2}
\]
with equality attained. The uniform zero-free strip \(|T|\ge\sqrt3\) is optimal over all \(c>0\).

In every dimension \(d\ge2\), by contrast, the real zero set is unbounded and its projection to Doppler-frequency space is **exactly** the closed exterior of the ball \(|\omega|<\Omega_{d,c}\), where
\[
\Omega_{d,c}^{2}=
\begin{cases}
2c+\frac{3d}{2}-1,&d+4c\le6,\\[2mm]
4c+2d+4-2\sqrt{2(4c+d+2)},&d+4c\ge6.
\end{cases}\tag{3}
\]
The two expressions agree when \(d+4c=6\). When \(d+4c<6\), the minimal Doppler zero is realized at a **nonzero delay orthogonal to frequency**; when \(d+4c>6\), the minimum is realized at **zero delay**. At the transition both prescriptions coincide. For arbitrarily large \(Y\), two distinct perpendicular zero families have
\[
X_{\pm}(Y)=Y-a\pm4\sqrt{Y-Y_0},\qquad T\perp\omega.\tag{4}
\]
In particular, every unbounded sequence of zeros has \(X/Y\to1\) and \(|T\cdot\omega|/(|T||\omega|)\to0\).

In dimension one a second sharp transition governs the minimum Doppler frequency on each oval. Define \(c_*=(\sqrt3-1)/4\) and \(s_-=4c+6-2\sqrt{8c+6}\). Then
\[
\min_{A_{1,c}=0}\omega^2=
\begin{cases}
\frac{4c+1}{2c+1},&0<c<c_*,\\
s_-,&c\ge c_*.
\end{cases}\tag{5}
\]
For \(0<c<c_*\) each oval has two off-axis delay points attaining this minimum, with squared delay \((1-4c-8c^2)/(2c+1)\); for \(c>c_*\), its unique frequency-minimizing point has \(T=0\). At \(c=c_*\), the minimum touches the zero oval quartically in delay: \(\omega^2-s_-=\Theta(T^4)\) near \(T=0\).

## Assumptions and scope

All spatial vectors and frequencies are real. The Fourier phase is \(e^{-i\omega\cdot u}\), **not** \(e^{-2\pi i\xi\cdot u}\); conversion to cycles-per-unit uses \(\omega=2\pi\xi\). The unnormalized window has no effect on zeros. The statements concern the ordinary self-ambiguity integral over \(\mathbb R^d\), not an analytic continuation, a cross-ambiguity between different windows, or phase-only retrieval. The parameter \(c\) is strictly positive (so the window has no spatial zero). The first transition in (3) concerns the smallest **squared** frequency \(Y\), and the origin of the optimizing delay; it is not a stability claim.

## Proof

**1. Exact Gaussian moment calculation.** The pointwise product of the two shifted windows is
\[
e^{-|u|^2-X/4}\bigl[(|u|^2+c+X/4)^2-(u\cdot T)^2\bigr].
\]
For the normalized complex Gaussian Fourier expectation \(\mathbb E_{\omega}[F]=\pi^{-d/2}e^{Y/4}\int_{\mathbb R^d}F(u)e^{-|u|^2-i\omega\cdot u}\,du\), completing the square gives
\[
\mathbb E_{\omega}|u|^2=\frac d2-\frac Y4,\quad
\mathbb E_{\omega}|u|^4=\frac{d(d+2)}4-\frac{(d+2)Y}4+\frac{Y^2}{16},\quad
\mathbb E_{\omega}(u\cdot T)^2=\frac X2-\frac Z4.
\]
Substitution and multiplication by \(16\) give
\[
P=(X-Y)^2+4Z+(8c+4d-8)X-(8c+4d+8)Y+16c^2+16cd+4d(d+2).
\]
Completing the square yields exactly \(P=(X-Y+a)^2+4Z-16(Y-Y_0)\), proving (1). It also proves the ambiguity is real for this even window.

**2. All dimensions at least two: Doppler projection and its sharp edge.** In dimension \(d\ge2\), any pair \(X,Y\ge0\) admits vectors \(T\perp\omega\). At a zero, (1) implies \(Y\ge Y_0>0\), and \(H=X-Y\ge-Y\). For fixed \(Y\), the least possible value of \((H+a)^2+4Z\), over this feasible set, is \(0\) when \(Y\ge a\) and \((a-Y)^2\) when \(Y<a\); both are attained with perpendicular vectors. The equation has a feasible zero exactly when
\[
16(Y-Y_0)\ge (\max\{a-Y,0\})^2.
\]
If \(Y_0\ge a\), equivalently \(d+4c\le6\), the least feasible \(Y\) is \(Y_0\), attained at \(X=Y_0-a=3-2c-d/2\). If \(Y_0<a\), the least feasible \(Y\) is the smaller root of \((a-Y)^2=16(Y-Y_0)\), namely the second expression in (3), attained at \(X=0\). In either case, the feasible set of \(Y\)'s is the interval beginning at that threshold and extending to infinity; for instance \(X=Y-a+4\sqrt{Y-Y_0}\) is nonnegative throughout the interval and solves (1) with \(Z=0\). This proves the exact Doppler projection and the location of edge optimizers.

For sufficiently large \(Y\), both values in (4) are positive and define distinct perpendicular roots. Conversely, along any zero sequence escaping to infinity, (1) gives \(|X-Y+a|\le4\sqrt{Y-Y_0}\) and \(|T\cdot\omega|\le2\sqrt{Y-Y_0}\). Bounded \(Y\) would force bounded \(X\), so \(Y\to\infty\); the displayed bounds then yield \(X/Y\to1\) and the asymptotic orthogonality claim.

**3. Dimension one: exact oval parameterization.** In one dimension \(Z=XY\), so (1) reduces to
\[
P_1(X,Y)=(X+Y)^2+(8c-4)X-(8c+12)Y+16c^2+16c+12.
\]
Set \(s=X+Y\) and \(k=16c+8\). Define \(s_\pm=4c+6\pm2\sqrt{8c+6}\). Solving \(P_1=0\) for \(X\) gives exactly
\[
X(s)=\frac{(s-s_-)(s_+-s)}{k},\qquad Y(s)=s-X(s)=\frac{s^2+(8c-4)s+16c^2+16c+12}{k}.\tag{6}
\]
The numerator of \(Y(s)\) has discriminant \(-128c-32<0\), hence \(Y(s)>0\) for every real \(s\). The condition \(X\ge0\) is precisely \(s\in[s_-,s_+]\). For each sign of \(\omega\), the curves \((T,\omega)=(\pm\sqrt{X(s)},\operatorname{sign}(\omega)\sqrt{Y(s)})\) are compact closed ovals, with the two branches meeting at the endpoints \(T=0\). There are no other zeros. They are nonsingular: at an interior point both \(T\) and \(\omega\) are nonzero, while \(\partial_XP_1-\partial_YP_1=k>0\); at an endpoint, \(\partial_YP_1=\pm4\sqrt{8c+6}\ne0\) and \(\omega\ne0\). They are disjoint because the positive and negative Doppler regions are separated by a zero-free axis: \(P_1(X,0)=(X+4c-2)^2+32c+8>0\).

The parabola \(X(s)\) has a unique maximum at \(s=(s_-+s_+)/2=4c+6\), giving (2) and its attainment. Its supremum as \(c\downarrow0\) is \(3\), proving uniform sharpness. The quadratic \(Y(s)\) has vertex \(s_v=2-4c\); this lies strictly inside \([s_-,s_+]\) exactly when \(8c^2+4c-1<0\), or \(0<c<c_*\). Its value and the corresponding delay are
\[
Y(s_v)=\frac{4c+1}{2c+1},\qquad X(s_v)=\frac{1-4c-8c^2}{2c+1}.
\]
Otherwise \(Y\) increases from the left endpoint and has its minimum \(s_-\) at \(T=0\), establishing (5). At \(c=c_*\), \(s_v=s_-\), and (6) gives \(Y(s)-s_-=(s-s_-)^2/k\), while \(T^2=X(s)\) is a positive multiple of \(s-s_-\) to first order, yielding the quartic tangency.

## Verification

The accompanying standalone Python checkers use SymPy, NumPy, and mpmath; run `python checks/ambiguity_1d_checker.py` and `python checks/ambiguity_nd_checker.py`. They verify exact symbolic identities, three high-precision direct one-dimensional ambiguity integrations, five multi-dimensional tensor-Gauss-Hermite quadratures in dimensions one through three, 25 one-dimensional exact-parameter zero witnesses, and 80 perpendicular higher-dimensional zero witnesses, with the exact recorded outputs in `checks/check_output.txt`. These computations check normalization and boundary algebra; the all-degree/all-dimension statements follow from the analytical argument, not finite samples.

## Relationship to prior work

Ali, Ismail, and Shah (arXiv:1410.3908, initially public 2014-10-15) develop complex Hermite polynomials and the Wigner map, providing the natural low-Hermite background. Korevaar, Oude Alink, de Boer, Kokkeler, and Smit (2016) derive closed-form operations, including ambiguity functions, of Hermite functions; in principle those formulas give the polynomial in (1) by linear combinations. The present statement is the explicit dimension-uniform **global real zero geometry and sharp transition** derived from that polynomial, not a claim to rediscover general Hermite transforms. Gröchenig, Jaming, and Malinnikova (arXiv:1811.03937; published 2019/2020) study Wigner and time-frequency zero-free phenomena more broadly, but their examined theorems do not provide this classification. Different conventions for \(2\pi\) frequency and for interchange of Wigner/ambiguity coordinates require rescaling, not different mathematics.

## Limitations

These results concern one explicit radial quadratic-Gaussian family with \(c>0\), not arbitrary positive Schwartz windows, every Hermite combination, or arbitrary cross-ambiguity functions. The exact polynomial (1) could be implicit in older general Hermite formulas; the claimed distinction is the sharp zero-set classification and dimensional topology contrast, with a residual historical-priority risk. The frequency threshold is a uniqueness-of-nonvanishing statement, not a uniform lower stability estimate near zeros. This is not an independently audited publication-priority certificate.

## References

1. S. Twareque Ali, M. E. H. Ismail, N. M. Shah, *Deformed Complex Hermite Polynomials*, arXiv:1410.3908 (first submitted 2014-10-15). https://arxiv.org/abs/1410.3908
2. C. W. Korevaar, M. S. Oude Alink, P.-T. de Boer, A. B. J. Kokkeler, G. J. M. Smit, *Closed-Form Expressions for Time-Frequency Operations Involving Hermite Functions*, IEEE Trans. Signal Process. 64 (2016), 1383–1390. DOI:10.1109/TSP.2015.2488580.
3. K. Gröchenig, P. Jaming, E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, Rev. Mat. Complut. 33 (2020), 723–744, arXiv:1811.03937. https://arxiv.org/abs/1811.03937
