# Sharp logarithmic inverse stability from rotational Minkowski-sum area fluctuations

## Finding

A fixed real-analytic, strictly positively curved planar convex body can serve as a geometric probe: the variation in area after its Minkowski addition to a uniformly rotated unknown body detects whether that unknown body is a disk. Under a natural finite curvature-energy assumption, this detection has an **optimal logarithmic stability exponent two**.

Put
\[
 h_K(\phi)=1+\frac12\sum_{n=2}^{\infty}\frac{2^{-n}}{n^2}\cos(n\phi),
 \qquad c=\frac\pi8.
\]
For any planar convex body \(L\), write
\[
 h_L(\phi)=r+a_1\cos\phi+b_1\sin\phi+
 \sum_{n\ge2}(a_n\cos(n\phi)+b_n\sin(n\phi)),
 \qquad r=\frac{P(L)}{2\pi}.
\]
Define nonnegative Fourier energies, the isoperimetric deficit, and the curvature-weighted energy by
\[
 w_n=\frac\pi2(n^2-1)(a_n^2+b_n^2),\qquad
 D=\sum_{n\ge2}w_n=\frac{P(L)^2}{4\pi}-A(L),\qquad
 H=\sum_{n\ge2}n^2w_n.
\]
Let \(\Theta\) be uniform on \([0,2\pi)\), let \(R_\theta\) be the counterclockwise planar rotation, and put
\[
 Y(\theta)=A(K+R_\theta L),\qquad V=\operatorname{Var}(Y(\Theta)),
 \qquad z=\frac{V}{2cH}.
\]
For every \(L\) with \(0<H<\infty\), the variance is positive and the following **explicit logarithmic inverse inequality** holds whenever \(z\le4^{-8}\):
\[
 \boxed{D\le\frac{16H}{[\log_4(1/z)]^2}.}
\]
The exponent two is optimal within real-analytic strictly positively curved bodies, even with fixed perimeter: for the family of support functions
\[
 h_{L_n}(\phi)=1+\frac{1}{2n^2}\cos(n\phi),\qquad n\ge2,
\]
one has
\[
 \boxed{\lim_{n\to\infty}\frac{D(L_n)}{H(L_n)}
   [\log_4(1/z_n)]^2=1.}
\]
Without the finite-energy assumption, the exact variance remains well-defined and vanishes precisely when \(L\) is a disk. Thus the measurement is rigid for every convex body, but its quantitative bound is conditional on the stated energy.

## Assumptions and scope

The words *convex body* mean compact, convex and full-dimensional in \(\mathbb R^2\). Areas and perimeters are Euclidean. No origin choice is imposed on \(L\); first Fourier harmonics represent translations and cancel in the formulas. The Fourier coefficients are those of its ordinary support function. The energy \(H\) is allowed to be infinite for general bodies; the quantitative assertion assumes \(0<H<\infty\). For a \(C^2\) body with radius of curvature \(\rho_L=h_L+h_L''\), \(H\) is comparable to the square-integral of the nonconstant curvature modes. Precisely, with \(E=\int_0^{2\pi}(\rho_L-r)^2d\phi\), one has \(\frac12E\le H\le\frac23E\); the first-harmonic part of \(\rho_L\) vanishes identically.

The defining analytic series for \(K\) converges with every derivative because its coefficients decay geometrically. Its radius of curvature satisfies
\[
 h_K+h_K''=1-\frac12\sum_{n\ge2}(1-n^{-2})2^{-n}\cos(n\phi)
 \ge1-\frac12\sum_{n\ge2}2^{-n}=\frac34>0.
\]
Thus \(K\) is a genuine strictly positively curved convex body, not a formal Fourier series.

## Proof

**1. Exact rotational spectral covariance.** For a planar convex body with support function \(h\), the weak support-area formula is
\[
 A=\frac12\int_0^{2\pi}\bigl(h(\phi)^2-h'(\phi)^2\bigr)d\phi.
\]
Every convex body's support is Lipschitz, so the formula and its polarization hold in the Sobolev space \(H^1(S^1)\), with convergence justified by Parseval or smooth approximation. Since Minkowski addition adds support functions and rotation shifts the argument, expanding the polarized formula shows
\[
 Y(\theta)-\mathbb E Y(\Theta)
 =-\pi\sum_{n\ge2}(n^2-1)
  \bigl[a_{K,n}a_{L,n}(\theta)+b_{K,n}b_{L,n}(\theta)\bigr],
\]
where \((a_{L,n}(\theta),b_{L,n}(\theta))\) is the coefficient pair of \(h_L(\phi-\theta)\). Each summand is a sinusoid of frequency \(n\), whose amplitude is \(2\sqrt{w_{K,n}w_n}\). Orthogonality in the uniformly distributed angle gives the exact formulas
\[
 \mathbb EY(\Theta)=A(K)+A(L)+\frac{P(K)P(L)}{2\pi},
\]
\[
 \operatorname{Cov}(Y(\Theta),Y(\Theta+\tau))
   =2\sum_{n\ge2}w_{K,n}w_n\cos(n\tau),
 \qquad V=2\sum_{n\ge2}w_{K,n}w_n.
\]
Both series converge absolutely, since the nonnegative support energies are summable. In particular, for the chosen probe \(K\),
\[
 w_{K,n}=c\,4^{-n}\frac{n^2-1}{n^4}>0,
 \qquad c=\frac\pi8.
\]
Therefore \(V=0\) precisely if every \(w_n\) vanishes. The weak isoperimetric support identity shows that this happens precisely when the support function has only degree zero and one harmonics, i.e. \(L\) is a translated disk.

**2. Quantitative low-/high-frequency cutoff.** Assume \(0<H<\infty\); then \(z>0\). Let
\[
 \alpha_n=4^{-n}\frac{n^2-1}{n^4},
 \qquad z=\sum_{n\ge2}\alpha_n\frac{w_n}{H},
 \qquad T=\log_4(1/z).
\]
If \(T\ge8\), choose integer \(N=\lfloor T/2\rfloor\ge4\). For each \(2\le n\le N\),
\[
 \alpha_n=4^{-n}\frac{1-n^{-2}}{n^2}
 \ge\frac34\frac{4^{-N}}{N^2}.
\]
Consequently
\[
 \sum_{2\le n\le N}w_n\le\frac43zHN^2 4^N,
 \qquad \sum_{n>N}w_n\le\frac{H}{(N+1)^2}.
\]
Because \(T\ge2N\), one has \(z4^N\le4^{-N}\). For every integer \(N\ge4\),
\[
 \frac43N^24^{-N}\le\frac3{(N+1)^2}.
\]
This last elementary inequality holds at \(N=4\); the ratio of the two sides, equivalently a constant times \(N^2(N+1)^2/4^N\), strictly decreases thereafter. Adding the two partial bounds yields
\[
 D\le\frac{4H}{(N+1)^2}<\frac{16H}{T^2},
\]
because \(N+1>T/2\). This proves the stated bound, without needing finite-mode truncation of \(L\).

**3. Optimality of the logarithmic exponent.** Take the explicitly defined \(L_n\) above. Its radius of curvature is
\[
 h_{L_n}+h_{L_n}''=1-\frac12(1-n^{-2})\cos(n\phi)\ge\frac12,
\]
so every witness is real analytic and strictly convex, of perimeter \(2\pi\). It has just one nontrivial mode, giving
\[
 \frac{D(L_n)}{H(L_n)}=\frac1{n^2},
 \qquad z_n=\frac{w_{K,n}}{cn^2}
 =4^{-n}\frac{n^2-1}{n^6}.
\]
Thus
\[
 T_n=\log_4(1/z_n)=n+\log_4\frac{n^6}{n^2-1}=n+O(\log n).
\]
It follows that \(T_n^2D(L_n)/H(L_n)\to1\), and no uniform bound proportional to \(H/[\log(1/z)]^{2+\varepsilon}\) can hold for any \(\varepsilon>0\), even within the smooth positively curved fixed-perimeter examples.

## Verification

The included Python files `verification.py` and `verification_log.py` are standalone standard-library implementations. Run them from the same directory using `python verification.py` and `python verification_log.py`. The first reconstructs Minkowski-sum areas directly by numerical support-function quadrature at 256 normal angles and 256 rotations, comparing the mean and five autocovariance shifts for each of four strictly convex trigonometric examples. The second checks the analytic probe's curvature margin, the exact high-frequency witness ratios, and the spectral cutoff inequalities on 1,223 finite mixtures. Both returned their `VERIFY_OK` completion markers. These experiments only corroborate the precise identities and normalizations; the infinite-dimensional result follows from the proof above.

## Relationship to prior work

Gardner, Hug and Weil (2013, preprint first public 2013-01-22) develop the general Minkowski and Orlicz addition framework. Xu, Zhou and Zhu (2013) derive mixed isoperimetric inequalities from kinematic containment formulas. Wang, Luo and Zhou (2016) use the classical mean-over-rotations mixed-area formula in their inequalities. In particular their equation (1.8) gives the first angular moment, not the present inverse stability estimate or sharp exponent.

Classical support-function Fourier theory already provides the mixed-area bilinear identity; it is used explicitly as a starting point, not asserted as new. The distinct statement here is a sharp order of conditional recovery of a body's isoperimetric deficit from the *single measured rotational area variance* against one noncircular analytic probe. The logarithmic cutoff and its positive-curvature optimality sequence do not appear in the inspected sources. General inverse-problem spectral-cutoff methods are conceptually related; unindexed earlier variants remain a literature risk.

## Limitations

This is a conditional exact-population variance theorem, not a guarantee from finitely many observed rotations, noisy measurements, or incomplete angular coverage. The logarithmic **exponent** is optimal, but the numerical factor \(16\) is not claimed best possible. Without finite \(H\), only zero-variance rigidity is asserted; no uniform logarithmic modulus is claimed. The area-covariance formula does not recover the Fourier phases or the full convex body. The statement concerns planar Euclidean convexity and one explicitly fixed analytic probe, not arbitrary probes or higher dimensions. Historical equivalences in classical Fourier-convexity monographs cannot be exhaustively ruled out by electronic searching.

## References

1. R. J. Gardner, D. Hug and W. Weil, *The Orlicz–Brunn–Minkowski theory: A general framework, additions, and inequalities*, arXiv:1301.5267v1 (public 2013-01-22), https://arxiv.org/abs/1301.5267 .
2. W. Xu, J. Zhou and B. Zhu, *On containment measure and the mixed isoperimetric inequality*, J. Inequal. Appl. 2013, article 540 (2013-11-19), https://doi.org/10.1186/1029-242X-2013-540 .
3. P. Wang, M. Luo and J. Zhou, *Bonnesen-style symmetric mixed inequalities*, J. Inequal. Appl. 2016, article 208 (2016-09-02), https://doi.org/10.1186/s13660-016-1146-5 .
4. F. A. Bartha, F. Bencs, K. J. Böröczky and D. Hug, *Extremizers and stability of the Betke–Weil inequality*, arXiv:2103.11672v1 (2021-03-22), https://arxiv.org/abs/2103.11672 .
