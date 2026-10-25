# Resonance windows for damped-cosine geodesic kernels on the circle

## Finding
Let \(\mathbb S^1\) be the unit circle, let \(\theta(x,y)\in[0,\pi]\) be the shorter geodesic angle, and for \(a>0\), \(\omega\ge0\), define
\[
K_{a,\omega}(x,y)=e^{-a\theta(x,y)}\cos(\omega\theta(x,y)).
\]
Put \(q=e^{-\pi a}\), \(c=\cos(\pi\omega)\), \(s=\sin(\pi\omega)\), \(Y=q\omega s\), \(R=a^2+\omega^2\), \(E=a(1-qc)\), and \(O=a(1+qc)\). Then \(K_{a,\omega}\) is positive semidefinite on **every** finite point configuration on \(\mathbb S^1\) if and only if all four explicit inequalities hold:
\[
\boxed{E-Y\ge0,\qquad E+Y\ge0,\qquad O+Y\ge0,\qquad (1+R)O+(1-R)Y\ge0.}
\]
Every admissible kernel is in fact strictly positive definite on each finite configuration of pairwise distinct points, including parameter-boundary cases. Every integer \(\omega\ge0\) is admissible. For each fixed \(a>0\), let
\[
\gamma(a)=\frac{a(e^{\pi a}-1)}{\pi}.
\]
For any \(0<\epsilon<\gamma(a)\), all sufficiently large integers \(k\) satisfy: frequencies with \(|\omega-k|\le(\gamma(a)-\epsilon)/k\) are admissible, whereas those with \((\gamma(a)+\epsilon)/k\le|\omega-k|\le1/2\) are not. Thus the high-frequency admissible region consists of narrow islands centered at the integer harmonics, with leading total width \(2\gamma(a)/k\).

## Assumptions and scope
The circle has unit radius and periodic angular coordinate \(t\in\mathbb R/(2\pi\mathbb Z)\). The geodesic angle between coordinates \(t,u\) is \(\theta=\min_{j\in\mathbb Z}|t-u+2\pi j|\in[0,\pi]\). Parameters are fixed real \(a>0\), \(\omega\ge0\). Positive semidefinite means \(\sum_{j,l}c_j\overline c_l K(x_j,x_l)\ge0\) for every integer \(N\ge1\), arbitrary points \(x_j\), and arbitrary complex coefficients \(c_j\). Strictness is claimed only when the sites are pairwise distinct and the coefficient vector is nonzero. There is no assertion for higher-dimensional spheres, for \(a=0\), or for negative damping.

## Proof
**Step 1 (the exact cosine coefficients).** Since \(\theta\) is the absolute value of the representative angle in \([-\pi,\pi]\), Schoenberg's circle criterion is that \(I_n=\int_0^\pi e^{-at}\cos(\omega t)\cos(nt)\,dt\ge0\) for every integer \(n\ge0\). The constant and nonconstant Fourier coefficients differ by strictly positive normalization factors only. For each real \(v\), elementary integration gives
\[
\int_0^\pi e^{-at}\cos(vt)\,dt
=\frac{a(1-e^{-\pi a}\cos(\pi v))+v e^{-\pi a}\sin(\pi v)}{a^2+v^2}.
\]
Apply the product-to-sum identity to \(v=\omega+n\) and \(v=\omega-n\). The identities \(\sin(\pi(\omega\pm n))=(-1)^n\sin(\pi\omega)\) and \(\cos(\pi(\omega\pm n))=(-1)^n\cos(\pi\omega)\) yield
\[
I_n=\frac{X_n(R+n^2)+Y_n(R-n^2)}{(a^2+(\omega+n)^2)(a^2+(\omega-n)^2)},\quad
X_n=a(1-(-1)^n qc),\quad Y_n=(-1)^nY.
\]
The denominator is positive because \(a>0\). Consequently, for even \(n\), its numerator equals \((E-Y)n^2+(E+Y)R\), and for odd \(n\), it equals \((O+Y)n^2+(O-Y)R\).

**Step 2 (an infinite Fourier test reduces to four inequalities).** Among nonnegative even integers \(n\), the numerator is affine in \(n^2\); it is nonnegative for all \(n=0,2,4,\ldots\) exactly when its coefficient of \(n^2\) is nonnegative and its value at \(n=0\) is nonnegative, namely \(E-Y\ge0\) and \(E+Y\ge0\). Among odd positive integers the same affine argument requires its slope \(O+Y\ge0\) and its value at \(n=1\), namely \((1+R)O+(1-R)Y\ge0\). This proves both necessity and sufficiency, with equality boundaries included. The Fourier series is absolutely convergent: the displayed formula is \(O(n^{-2})\) for fixed parameters. Therefore the Fourier coefficient criterion applies without distributional subtleties.

**Step 3 (strictness at the sharp boundary).** Since \(0<q<1\), both \(E>0\) and \(O>0\). For even \(n\ge2\), the two nonnegative quantities \(E-Y\) and \(E+Y\) cannot vanish simultaneously; hence \(I_n>0\). For odd \(n\ge3\), write the numerator as \((n^2-1)(O+Y)+[(1+R)O+(1-R)Y]\). These nonnegative terms cannot both vanish: \(O+Y=0\) would give the bracket \(2RO>0\). Therefore \(I_n>0\) for every \(n\ge2\). If the quadratic form vanishes at distinct angles \(t_j\), the Fourier representation forces \(\sum_j c_j e^{int_j}=0\) for all integers \(n\ge2\). Choosing \(n=2,\ldots,N+1\) gives a Vandermonde system on distinct \(e^{it_j}\), which has only the zero solution. Thus strict positive definiteness holds.

**Step 4 (integer resonances and asymptotic windows).** At \(\omega=k\in\mathbb Z_{\ge0}\), \(Y=0\); the four inequalities are strict because \(E,O>0\), proving every integer is inside the admissible set. For arbitrary admissible large \(\omega\), the first two inequalities yield
\[
q\omega|\sin(\pi\omega)|=|Y|\le a(1-qc)\le a(1+q).
\]
It follows that the distance from \(\omega\) to its nearest integer is \(O_a(1/\omega)\). For an integer \(k\to\infty\), put \(\omega=k+u/k\), with \(u\) in any fixed compact interval, and let \(\sigma=(-1)^k\). Uniformly in such \(u\),
\[
qc=\sigma q+o(1),\quad Y=\sigma q\pi u+o(1),\quad R\to\infty.
\]
The even conditions reduce in the limit to \(|q\pi u|\le a(1-\sigma q)\). The odd slope and the odd first-mode condition divided by \(R\) reduce together to \(|q\pi u|\le a(1+\sigma q)\). Their intersection is \(|u|\le a(1-q)/(q\pi)=\gamma(a)\). Strict uniform inequalities give the admissible inner windows for every fixed \(\epsilon>0\). For the outer exclusion, the preceding bound first confines every large-frequency admissible point to \(|u|\le C_a\), after which compactness and the limiting inequalities exclude \(|u|\ge\gamma(a)+\epsilon\). This proves the stated two-sided asymptotic width claim.

## Verification
The accompanying standalone checker evaluates the explicit coefficients against direct numerical quadrature on randomly selected parameter and frequency samples, tests the finite inequalities against the first 300 Fourier modes on 180 deterministic parameter samples, and checks scaled window boundaries for four large integer frequencies. All these tests completed successfully. Symbolic expansion of the common denominator independently reproduced the coefficient numerator identity; the algebraic identity itself is displayed above and may be checked by hand. Numerical experiments are diagnostic only; the proof of every-mode positivity and the asymptotic resonance claim is analytic.

## Relationship to prior work
Schoenberg's circle criterion, as presented with the normalized Fourier coefficient formula in Gneiting (2011, Sec. 3, Eq. 14), supplies the general basis for testing isotropic kernels. Gneiting also establishes the completely monotone exponential family without oscillation (Example 1). Beatson, zu Castell and Xu (2011) investigate Pólya-type sufficient positivity criteria for spheres, but not a frequency-dependent damped cosine. Earlier exact circle classifications of \(e^{-a\theta}(1+b\cos\theta)\) test amplitude perturbations at the single integer harmonic rather than arbitrary noninteger frequencies; they neither provide these four tests nor imply the integer-centered shrinking-window law. The present statement is an explicit parameter classification that requires reducing all circle Fourier modes, not a new general characterization of positive definiteness.

## Limitations
The frequency islands are asymptotic for fixed positive damping; no uniform statement as \(a\downarrow0\) or \(a\to\infty\) is proved. The theorem only concerns the geodesic circle, not higher spheres, and does not address nongeodesic or chordal distances. It provides no closed elementary formula for each finite-frequency endpoint, though its four inequalities give a complete exact decision test. A 2016 dissertation mentioning damped-cosine correlation models was not materially accessible; a claim-level comparison with it remains an unresolved literature risk. No independent mathematical review has been performed.

## References
1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077 (first posted 2011-11-30), especially Sec. 3, Eq. (14), and Sec. 5, Example 1; https://arxiv.org/pdf/1111.7077 .
2. R. K. Beatson, W. zu Castell, Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437 (first posted 2011-10-11), especially Introduction and Theorem 1.1; https://arxiv.org/pdf/1110.2437 .
3. J. Fiedler, doctoral dissertation on positive definite spherical kernels (2016; inaccessible full text), archive record: https://archiv.ub.uni-heidelberg.de/volltextserver/22193/1/thesis-JochenFiedler.pdf . Citation is solely an access/overlap caveat, not evidence of noncoverage.
