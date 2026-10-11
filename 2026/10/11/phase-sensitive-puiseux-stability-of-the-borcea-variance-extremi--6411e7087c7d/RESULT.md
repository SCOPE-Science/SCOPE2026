# Phase-sensitive Puiseux stability of the Borcea variance extremizer

## Finding

Fix an integer \(n\ge4\) and a complex polynomial \(Q\) of degree at most \(n-1\) with \(Q'(0)\ne0\). For real \(t>0\), let
\[
P_t(z)=z^n-1+tQ(z).
\]
For any degree-\(n\) polynomial \(P\), denote its zeros, with multiplicity, by \(a_1,\ldots,a_n\), put \(c(P)=n^{-1}\sum_{j=1}^n a_j\), and define
\[
\sigma_2(P)=\left(\frac1n\sum_{j=1}^n|a_j-c(P)|^2\right)^{1/2},
\qquad
h(P,P')=\max_{P(a)=0}\min_{P'(\zeta)=0}|a-\zeta|.
\]
The sharp Borcea variance inequality, recently established for all degrees, is \(h(P,P')\le\sigma_2(P)\); its regular-polygon model \(P_0(z)=z^n-1\) has equality.

Set
\[
\rho_t=\left(\frac{t|Q'(0)|}{n}\right)^{1/(n-1)},\qquad
\theta=\frac{\arg(-Q'(0))}{n-1},\qquad
T=\frac{2\pi}{n-1}.
\]
Define
\[
\Delta_n(\theta)=\max_{0\le j<n}
\operatorname{dist}\left(\frac{2\pi j}{n}-\theta,T\mathbb Z\right),
\qquad
\operatorname{dist}(x,T\mathbb Z)=\min_{k\in\mathbb Z}|x-kT|.
\]
Then the exact first nonzero variance deficit is
\[
\boxed{\quad
\sigma_2(P_t)-h(P_t,P_t')
=\rho_t\cos\Delta_n(\theta)+O_{n,Q}(\rho_t^2)
\quad}\qquad(t\downarrow0).
\]
Its coefficient has the sharp phase range
\[
\boxed{\quad
\cos\frac{\pi}{n-1}\le\cos\Delta_n(\theta)\le\cos\frac{\pi}{n}
\quad}.
\]
Both endpoints occur for linear perturbations: the lower coefficient for \(Q(z)=z\), the upper coefficient for \(Q(z)=e^{-i\pi/n}z\). Since \(n\ge4\), the lower coefficient is strictly positive. Thus every fixed perturbation direction with \(Q'(0)\ne0\) yields a strict inequality for sufficiently small \(t>0\), and the local defect has exact Hölder exponent \(1/(n-1)\), not an ordinary first variation.

## Assumptions and scope

All perturbation coefficients are fixed complex numbers while the real parameter \(t\) tends to zero through positive values. The degree condition keeps \(P_t\) monic; neither its roots nor the coefficients of \(Q\) need be real. The argument of \(-Q'(0)\) may be chosen in any branch, since changing \(\theta\) by an integral multiple of \(T\) leaves \(\Delta_n\) unchanged.

The condition \(Q'(0)\ne0\) is essential for this splitting regime. If \(Q'(0)=0\), the multiple critical point at the origin can split at another scale; no assertion about such directions is made. The restriction \(n\ge4\) makes the uniform lower phase coefficient strictly positive and keeps the root displacement \(O(t)\) smaller than the stated \(O(\rho_t^2)\) remainder.

The result is local along each fixed direction \(Q\), not a uniform stability theorem over all coefficients or a global classification of equality in the variance inequality.

## Proof

Write \(\omega_m=e^{2\pi i/m}\). The polynomial \(P_0(z)=z^n-1\) has \(n\) simple zeros \(\omega_n^j\), where \(0\le j<n\). The implicit-function theorem applied at these zeros yields the uniform expansions
\[
a_j(t)=\omega_n^j+O_{n,Q}(t),\qquad 0\le j<n.
\]
Consequently their centroid is \(O_{n,Q}(t)\), and
\[
\sigma_2(P_t)=1+O_{n,Q}(t).
\]

Now \(P_t'(z)=nz^{n-1}+tQ'(z)\). Put \(q_1=Q'(0)\ne0\). By construction
\[
\rho_t^{n-1}=\frac{t|q_1|}{n},\qquad
n\rho_t^{n-1}e^{i(n-1)\theta}=-tq_1.
\]
Substitute \(z=\rho_t u\) and divide the critical-point equation by \(n\rho_t^{n-1}\). For bounded \(u\), it becomes
\[
u^{n-1}+\frac{q_1}{|q_1|}
+O_{n,Q}(\rho_t)=0.
\]
The unperturbed equation has the \(n-1\) simple roots
\[
u=e^{i\theta}\omega_{n-1}^k,\qquad 0\le k<n-1.
\]
The implicit-function theorem at each such root gives all the critical points, counted with multiplicity,
\[
\zeta_k(t)=\rho_t e^{i\theta}\omega_{n-1}^k+O_{n,Q}(\rho_t^2),
\qquad 0\le k<n-1.
\]
The roots and critical points have now all been enumerated: \(n\) simple zeros and \(n-1\) simple critical points for sufficiently small positive \(t\).

Since \(t=O_{n,Q}(\rho_t^{n-1})\) and \(n\ge4\), the root displacement is \(O_{n,Q}(\rho_t^3)\), smaller than the square-order remainder. Uniformly over the finite index pairs,
\[
\begin{aligned}
|a_j(t)-\zeta_k(t)|
&=\left|\omega_n^j-\rho_t e^{i\theta}\omega_{n-1}^k+O_{n,Q}(\rho_t^2)\right|\\
&=1-\rho_t\cos\left(\frac{2\pi j}{n}-\theta-\frac{2\pi k}{n-1}\right)
+O_{n,Q}(\rho_t^2).
\end{aligned}
\]
Thus the nearest critical-point distance to the \(j\)-th zero is
\[
\min_k|a_j(t)-\zeta_k(t)|
=1-\rho_t\cos\delta_j+O_{n,Q}(\rho_t^2),
\]
where
\[
\delta_j=\operatorname{dist}\left(\frac{2\pi j}{n}-\theta,T\mathbb Z\right),
\qquad 0\le\delta_j\le\frac{T}{2}.
\]
Taking the maximum over \(j\) and using that cosine decreases on \([0,\pi]\),
\[
h(P_t,P_t')=1-\rho_t\cos\Delta_n(\theta)+O_{n,Q}(\rho_t^2).
\]
Finally \(\sigma_2(P_t)=1+O(t)=1+O(\rho_t^3)\), proving the stated defect.

It remains to prove both sharp universal phase bounds. Work modulo \(T\). The \(n\) angles
\[
\frac{2\pi j}{n}-\theta\pmod T,
\qquad 0\le j<n,
\]
are exactly an equally spaced \(n\)-point grid on a circle of circumference \(T\), since multiplying by \(n-1\) turns their normalized positions into distinct multiples of \(1/n\) modulo one. The farthest grid point from the reference origin has distance
\[
\Delta_n(\theta)=\frac T2-\varepsilon(\theta),
\]
where \(\varepsilon(\theta)\) is the distance from the antipodal position \(T/2\) to the closest point of that grid. Necessarily
\[
0\le\varepsilon(\theta)\le\frac{T}{2n}.
\]
Therefore
\[
\frac\pi n\le\Delta_n(\theta)\le\frac\pi{n-1},
\]
and the cosine inequalities follow.

The phase \(q_1=1\) gives \(\theta=\pi/(n-1)=T/2\), so one of the grid points is antipodal and \(\Delta_n(\theta)=\pi/(n-1)\). The phase \(q_1=e^{-i\pi/n}\) gives \(\theta=\pi/n\), for which the antipode is halfway between adjacent grid points and \(\Delta_n(\theta)=\pi/n\). Choosing the corresponding linear \(Q\) attains the two coefficients in the asymptotic formula and completes the proof.

## Verification

Every analytic ingredient is elementary and exact: implicit roots near the simple \(n\)-th roots of unity, scaling of the derivative near its multiplicity-\(n-1\) zero, uniform first-order distance expansion, and an equally spaced circular-grid covering-radius calculation.

For the lower endpoint \(Q(z)=z\), the leading coefficient is exactly \(\cos(\pi/(n-1))\). For the upper endpoint \(Q(z)=e^{-i\pi/n}z\), the leading coefficient is \(\cos(\pi/n)\). These are exact symbolic checks independent of numerical rootfinding.

As an independent consistency check, numerical polynomial-root calculations were performed for the fixed perturbation \(Q(z)=e^{0.43i}z+(0.37+0.30i)z^2-0.19iz^3\) in degrees \(n=4,5,7,10\) at \(t=10^{-5},10^{-7},10^{-9}\). The predicted normalized coefficients were approximately \(0.618578,0.778893,0.899605,0.947000\); the observed scaled defects approached these values as \(t\) decreased. These finite checks are not the proof.

## Relationship to prior work

Zhang's recent 2026 theorem resolves Borcea's \(2\)-variance inequality globally and observes that its best constant is sharp. His Section 7 treats hypothetical counterexamples in a special reciprocal-coordinate normalization, including a near-equality parameter region, but gives no Puiseux splitting law or phase-sensitive variance defect along \(P_t(z)=z^n-1+tQ(z)\).

The 2011 paper of Khavinson, Pereira, Putinar, Saff, and Shimorin posed the variance inequality and the associated conjecture that equality for exponents larger than one characterizes translated and scaled binomials. The present theorem supplies a quantitative local statement near one such equality family, restricted to directions with \(Q'(0)\ne0\). It does not settle the global equality conjecture at exponent two.

Miller's study of local extrema for Sendov's problem concerns polynomials constrained by a containing disk and a different objective. It does not state the variance-normalized \(t^{1/(n-1)}\) defect or its sharp angular phase bounds.

Classical Puiseux splitting of a multiple polynomial root is the proof mechanism; the extra statement is the exact effect on the nonsmooth max-min root-critical-point distance, including the two sharp phase endpoints and the full perturbation-direction stability statement.

## Limitations

The expansion is for fixed \(n\), fixed \(Q\), and \(t\to0^+\). The implied remainder constant can depend on the entire polynomial \(Q\); no uniformity is asserted as \(Q'(0)\to0\) or \(n\to\infty\).

Directions with \(Q'(0)=0\) have different critical-root Newton polygons and require a separate analysis. The restriction \(n\ge4\) makes the coefficient uniformly positive; the cubic case can have a zero leading angular coefficient.

The statement does not classify all extremizers of the global Borcea inequality, does not bound deficits away from the regular-binomial orbit, and does not claim the same phase law for higher \(p\)-variances.

## References

1. Teng Zhang, *Borcea's 2-variance conjecture*, arXiv:2610.02035v1, first posted 1 October 2026, Theorem 1.2 and Section 7.
2. Dmitry Khavinson, Rajesh Pereira, Mihai Putinar, Edward B. Saff, and Serguei Shimorin, *Borcea's variance conjectures on the critical points of polynomials*, arXiv:1010.5167v2, 2011, Section 2 (Conjectures 1 and 2) and Section 10.3.
3. Michael J. Miller, *Unexpected local extrema for the Sendov conjecture*, arXiv:math/0505424v3, 2005.
