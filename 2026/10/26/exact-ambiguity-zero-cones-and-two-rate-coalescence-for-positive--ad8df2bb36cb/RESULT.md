# Exact ambiguity-zero cones and two-rate coalescence for positive Gaussian superpositions

## Finding

For arbitrary real parameters \(0<p<q\) and \(c>0\), define the strictly positive even Schwartz function
\[
g(t)=e^{-pt^2/2}+c e^{-qt^2/2},
\qquad
A(T,\omega)=\int_{\mathbb R}g(u+T/2)g(u-T/2)e^{-i\omega u}\,du.
\]
Here \(\omega\) is angular frequency. Both \(g\) and its Fourier transform are strictly positive on the real line. Nevertheless \(A\) has infinitely many real zeros, all away from the coordinate axes. Their **exact asymptotic directional cone** is
\[
\boxed{p\le |\omega/T|\le q.}
\]
Precisely, every fixed positive ray \(\omega=rT\) with \(p<r<q\) contains infinitely many simple radial zeros; for every \(\eta>0\), all sufficiently distant zeros have \(p-\eta<|\omega/T|<q+\eta\), with \(T\ne0\). The endpoint ray \(r=p\) contains infinitely many zeros exactly when \(c>\sqrt{(p+q)/(8p)}\), and has no zeros when the reverse weak inequality holds. The endpoint ray \(r=q\) contains infinitely many zeros exactly when \(c<\sqrt{8q/(p+q)}\), and has none for the reverse weak inequality. The same assertions hold in the other sign quadrants.

Write \(h=(q-p)/(4(p+q))\), \(\kappa=2h\), and
\[
u=\frac1c\sqrt{\frac{p+q}{8p}},\qquad
v=c\sqrt{\frac{p+q}{8q}},\qquad
\alpha_r=h\frac{r^2-p^2}{p},\qquad
\gamma_r=h\frac{q^2-r^2}{q}.
\]
For each fixed \(r\in(p,q)\), the sufficiently large positive roots on that ray can be indexed one per cosine node, by \(k\in\mathbb N\), with \(t_k=T_k^2\) and \(t_k^{(0)}=(k+1/2)\pi/(\kappa r)\):
\[
\kappa r t_k=(k+\tfrac12)\pi+(-1)^k\bigl(u e^{-\alpha_r t_k^{(0)}}+v e^{-\gamma_r t_k^{(0)}}\bigr)+O_{p,q,c,r}\!\left(e^{-2\min(\alpha_r,\gamma_r)t_k^{(0)}}\right).
\]
Consequently the number of distinct positive-ray roots with \(0<T\le R\) is
\[
\boxed{N_r(R)=\frac{\kappa r}{\pi}R^2+O_{p,q,c,r}(1).}
\]
The asymptotic directional cone is sharp: every interior direction occurs infinitely often, and both boundary directions occur as limits of zero directions.

A second, singular-perturbation statement concerns the **first root on the balanced ray** \(\omega=\sqrt{pq}\,T\). Write \(T_1>0\) for its smallest positive root, set \(\beta=\kappa\sqrt{pq}\), \(\delta=(q-p)^2/(4(p+q))\), and \(B=u+v>1\). There is an exact global bracket
\[
\boxed{\frac{\log B}{\delta}\le T_1^2\le\frac{\log B}{\delta}+\frac{2\pi}{\beta}.}
\]
For fixed \(p>0\), fixed \(c>0\), and \(q=p+\varepsilon\downarrow p\), two distinct rates arise:
\[
\boxed{\begin{aligned}
\varepsilon T_1^2&\longrightarrow4\pi&&\text{if }c=1,\\
\varepsilon^2 T_1^2&\longrightarrow8p\log\!\left(\frac{c+c^{-1}}2\right)&&\text{if }c\ne1.
\end{aligned}}
\]
Thus infinitesimal variance contrast produces zero escape of order \(\varepsilon^{-1/2}\) for equal amplitudes, but order \(\varepsilon^{-1}\) for every fixed unequal amplitude. At the degenerate parameter \(q=p\), or when one component is absent, the ambiguity function is zero-free.

## Assumptions and scope

All three parameters are real with \(0<p<q\), \(c>0\). The Fourier convention is \(\widehat f(\omega)=\int_{\mathbb R}f(t)e^{-i\omega t}\,dt\), so conversion to cyclic frequency requires \(\omega=2\pi\nu\). A radial zero is *simple* when the derivative along its specified ray with respect to \(T\) is nonzero. The asymptotic cone concerns directions of unbounded sequences of real zeros; it does not assert that the zero set fills the cone. In the coalescence statement, \(p\) and \(c\) are fixed independently of \(\varepsilon\).

## Proof

**1. Exact Gaussian identity.** Gaussian integration of the four terms in the correlation product gives
\[
\begin{aligned}
A(T,\omega)={}&\sqrt{\frac\pi p}e^{-pT^2/4-\omega^2/(4p)}
+c^2\sqrt{\frac\pi q}e^{-qT^2/4-\omega^2/(4q)}\\
&+2c\sqrt{\frac{2\pi}{p+q}}e^{-pqT^2/(2(p+q))-\omega^2/(2(p+q))}\cos(\kappa T\omega).
\end{aligned}
\]
The coefficient of the cosine is strictly positive. Divide by it and call the positive quotient \(C(T,\omega)\). Then exactly
\[
\boxed{\frac{A(T,\omega)}{C(T,\omega)}=
\cos(\kappa T\omega)+u e^{h(pT^2-\omega^2/p)}+v e^{h(-qT^2+\omega^2/q)}.}\tag{1}
\]
Directly, \(A(T,0)>0\) and \(A(0,\omega)>0\). Also
\(\widehat g(\omega)=\sqrt{2\pi/p}e^{-\omega^2/(2p)}+c\sqrt{2\pi/q}e^{-\omega^2/(2q)}>0\).

**2. Directional exclusion and sharpness.** On \(\omega=rT\), put \(t=T^2\). Formula (1) becomes
\[
F_r(t)=\cos(\kappa r t)+u e^{-\alpha_r t}+v e^{-\gamma_r t}.
\tag{2}
\]
If \(p<r<q\), both rates are positive. On any fixed narrow interval about a sufficiently large cosine zero \(t_k^{(0)}\), the last two terms and their first derivatives tend exponentially to zero. The cosine has nonzero derivative there. The intermediate value theorem, monotonicity within that narrow interval, and the bound away from zero outside such intervals show that exactly one simple root lies near each sufficiently large node, and that no other sufficiently large ray roots occur. Taylor expansion at that node yields the stated phase correction with quadratic error in the sum of exponentials. Counting consecutive nodes gives \(N_r(R)=\kappa rR^2/\pi+O(1)\).

For \(|\omega|\le(p-\eta)|T|\), the first exponential in (1) grows at least like \(\exp(a_\eta(T^2+\omega^2))\) when the region is nonempty. For \(|\omega|\ge(q+\eta)|T|\), the second grows similarly, even when \(T=0\). The positive sum in (1) eventually exceeds one uniformly in either exterior sector, so cancellation with the cosine is impossible. Conversely all interior slopes support unbounded zero sequences; taking interior slopes tending to an endpoint and choosing successively farther-out roots realizes both limiting boundary directions.

**3. Boundary rays.** On \(r=p\), (2) is \(\cos(\kappa pt)+u+v\exp(-h(q^2-p^2)t/q)\). If \(u\ge1\), it is everywhere positive; if \(u<1\), its values at arbitrarily large alternating cosine maxima and minima have opposite signs, giving infinitely many roots. The corresponding upper-ray statement follows with \(v\) in place of \(u\). The displayed weight thresholds are precisely \(u<1\) and \(v<1\). Symmetry proves the other-quadrant assertions.

**4. Exact balanced-ray bracket.** For \(r=\sqrt{pq}\), both exponential rates equal \(\delta\) and (2) becomes \(F(t)=\cos(\beta t)+B e^{-\delta t}\). AM–GM yields \(B\ge\sqrt{(p+q)/(2\sqrt{pq})}>1\). A root requires \(B e^{-\delta t}\le1\), hence \(t\ge t_*=\log(B)/\delta\). At \(t_*\), \(F(t_*)\ge0\). The first subsequent cosine minimum occurs less than \(2\pi/\beta\) later, where \(F<0\) unless the endpoint itself is already a root. Continuity establishes the bracket and existence of a smallest positive root.

**5. Two coalescence rates.** Let \(q=p+\varepsilon\) with \(\varepsilon\downarrow0\). Then
\[
\delta=\frac{\varepsilon^2}{8p}(1+O(\varepsilon)),\qquad
\beta=\frac\varepsilon4(1+O(\varepsilon)).
\]
For fixed \(c\ne1\), \(B\to(c+c^{-1})/2>1\); multiplying the bracket by \(\varepsilon^2\) proves the second limit. For \(c=1\), direct expansion gives \(\log B=3\varepsilon^2/(32p^2)+O_p(\varepsilon^3)\) and \(\delta/\beta=\varepsilon/(2\sqrt{pq})\). In the phase coordinate \(\theta=\beta t\), \(\cos\theta+B\exp[-(\delta/\beta)\theta]\to1+\cos\theta\) uniformly on compact \(\theta\)-intervals. The expression stays positive on \([0,\pi-\eta]\) for every fixed \(\eta>0\), while at \(\theta=\pi\) it is negative for all sufficiently small \(\varepsilon\), because \(\log B-\pi\delta/\beta<0\). Hence the first positive root has \(\beta T_1^2\to\pi\), implying \(\varepsilon T_1^2\to4\pi\).

## Verification

The accompanying standalone `CHECKER.py` uses high-precision numerical integration independently of the closed Gaussian formula at three parameter points, verifies four large ray zeros and their exponentially accurate phase corrections, checks the two exact endpoint weight tests, and probes both coalescence scalings. Execute `python CHECKER.py` after installing `mpmath` as specified in `requirements.txt`; an example output is in `CHECK_OUTPUT.txt`. These finite checks are consistency evidence only. The quantified global claims follow from the preceding analytic proof.

## Relationship to prior work

Nicacio–Maia–Toscano–Vallejos (2010) analyze Wigner interference in arbitrary Gaussian superpositions and exhibit a hyperbolic phase for unequal squeezing. Their characteristic-function representation is an important equivalent language, but the inspected analysis does not identify the exact self-ambiguity-zero directional cone, its raywise zero density, endpoint-amplitude thresholds, or the two competing first-zero escape exponents. Gröchenig–Jaming–Malinnikova (2018) give the Gaussian cross-ambiguity formula and study zero-free Wigner and short-time Fourier transforms; its formula is a starting identity here, not a proof of the nonlinear zero geometry for an unequal-width positive sum. Alonso (2011) reviews Wigner interference and the ambiguity/characteristic-function correspondence; portions of the review were accessible, but not its complete text. These antecedents materially limit any claim to being first to observe hyperbolic Gaussian interference. The claimed result is only the explicit zero-cone/escape theorem proved above.

## Limitations

No statement is made for arbitrary mixtures of three or more Gaussian widths, complex or signed amplitudes, unequal centers, higher-dimensional covariance matrices, or all finite zero components. The raywise roots are not globally isolated planar zeros: they lie on real smooth curves wherever the radial derivative is nonzero. The stated literature comparison is not a proof of publication priority; earlier equivalent phase-space calculations could cover the theorem. The exact amplitude thresholds are for the two cone-boundary rays, not a parameter classification of all finite zeros. No independent mathematical audit has been conducted.

## References

1. F. Nicacio, R. N. P. Maia, F. Toscano, R. O. Vallejos, *Phase Space Structure of Generalized Gaussian Cat States*, first arXiv version 11 February 2010, arXiv:1002.2248v1, https://arxiv.org/abs/1002.2248.
2. M. A. Alonso, *Wigner functions in optics: describing beams as ray bundles and pulses as particle ensembles*, Advances in Optics and Photonics 3 (2011), 272–365, https://doi.org/10.1364/AOP.3.000272.
3. K. Gröchenig, P. Jaming, E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937v1 (9 November 2018), https://arxiv.org/abs/1811.03937; later Rev. Mat. Complut. 33 (2020), 723–744.
