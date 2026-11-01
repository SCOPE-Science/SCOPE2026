# A critical point-mass boundary layer for sharp circular sign uncertainty

## Finding

For every integer \(m\ge2\), let \(N=m-1\). Write \(dx\) for normalized Haar measure on \(\mathbb T=\mathbb R/\mathbb Z\), let \(\delta_0\) be the unit mass at the distinguished origin, and define
\[
\mu_\tau=\frac{dx+\tau\delta_0}{1+\tau},\qquad \tau\ge0.
\]
Let \(\rho_m(\tau)\) denote the optimal radius of last sign change for nonzero, real, degree-at-most-\(N\) trigonometric polynomials \(f\) with \(\int f\,d\mu_\tau\le0\). Thus the radius of \(f\) is the infimum of \(r\ge0\) such that \(f(y)\ge0\) whenever its circular distance from the origin is at least \(r\).

**Theorem (sharp atom-concentration crossover).** Put \(t_m(\tau)=2\pi\rho_m(\tau)\). For each \(\tau>0\), \(t_m(\tau)\) is the unique point in \((0,\pi/m)\) satisfying
\[
\frac{\tan(mt_m(\tau)/2)}{\tan(t_m(\tau)/2)}=m+\frac1\tau.
\tag{1}
\]
For \(\tau=0\), \(t_m(0)=\pi/m\). The angle is strictly decreasing with \(\tau>0\).

For any sequence \(\tau_m\ge0\), the entire critical window is classified as follows:

* If \(m\tau_m\to0\), then \(m\rho_m(\tau_m)\to\tfrac12\).
* If \(m\tau_m\to c\in(0,\infty)\), then
\[
2\pi m\rho_m(\tau_m)\to x_c\in(0,\pi),\qquad
\frac{\tan(x_c/2)}{x_c/2}=1+\frac1c,
\tag{2}
\]
where the solution \(x_c\) is unique.
* If \(m\tau_m\to\infty\), then
\[
 m^{3/2}\sqrt{\tau_m}\,\rho_m(\tau_m)\longrightarrow\frac{\sqrt3}{\pi}.
\tag{3}
\]

The transition scale is exactly \(\tau_m\asymp m^{-1}\); in particular the Haar \(m^{-1}\) scale changes to \(m^{-3/2}\) for any fixed positive \(\tau\).

There is also a universal **extremizer profile**. Define the real even polynomial and its associated trigonometric extremizer by
\[
 a_m=\frac{\tau}{1+m\tau},\quad
 \Phi_m(z)=z^m-a_m\sum_{j=0}^{m-1}z^j,\quad
 B_m(z)=\frac{\Phi_m(z)+z^m\overline{\Phi_m(1/\overline z)}}2,\quad
 f_{m,\tau}(y)=\frac{|B_m(e^{2\pi iy})|^2}{\cos t_m(\tau)-\cos(2\pi y)}.
\tag{4}
\]
At the apparent poles the quotient is interpreted by continuous extension. It is a real trigonometric polynomial of degree at most \(m-1\), has zero \(\mu_\tau\)-mean, attains the sharp sign radius, and is unique up to a positive scalar.

If \(m\tau_m\to c\in[0,\infty]\), with the convention \(x_0=\pi\), \(x_\infty=0\), and \(c/(1+c)=1\) at \(c=\infty\), then locally uniformly for real \(u\),
\[
 \frac1{m^2}f_{m,\tau_m}\left(\frac{u}{2\pi m}\right)
 \longrightarrow
 \mathcal F_c(u)=\frac{2G_c(u)^2}{u^2-x_c^2},\qquad
 G_c(u)=\cos(u/2)-\frac{2c}{1+c}\frac{\sin(u/2)}u.
\tag{5}
\]
The values at zeros of the denominator are defined by removal of the singularity; \(\sin(u/2)/u\) has value \(1/2\) at the origin. Each profile changes sign only in the indicated central region.

## Assumptions and scope

The circle is parametrized by \(z=e^{2\pi iy}\). The degree bound means Fourier frequencies between \(-N\) and \(N\), inclusive. The measure is exactly normalized Haar plus a point mass at the distinguished origin; no claim is made about arbitrary singular measures. The asymptotics hold along **every** nonnegative sequence \(\tau_m\) satisfying the stated scaling, not merely along monotone sequences. The final profile depends on the explicit unnormalized extremizer (4), not on unit-norm normalization.

## Proof

**1. Exact monic orthogonal polynomial.** Multiplying a measure by a positive scalar does not change orthogonality or this extremal problem, so use \(dx+\tau\delta_0\). Set \(a=\tau/(1+m\tau)\). For \(0\le k<m\), Fourier orthogonality gives
\[
\int_{\mathbb T}\Phi_m(e^{2\pi iy})e^{-2\pi iky}(dx+\tau\delta_0)(y)
=-a+\tau(1-ma)=0.
\]
Thus \(\Phi_m\) in (4) is the monic degree-\(m\) orthogonal polynomial for this measure. Its reversed polynomial is as in (4). Orthogonal normalization only multiplies \(B_m\) by a positive scalar; it does not change its zeros or sharpness.

**2. The first paraorthogonal zero.** For \(0<t<\pi/m\), a geometric-sum identity yields the real even expression
\[
 e^{-imt/2}B_m(e^{it})
 =h_{m,a}(t):=\cos(mt/2)-a\cot(t/2)\sin(mt/2),
\tag{6}
\]
continuously extended at zero, where \(h_{m,a}(0)=1-ma=1/(1+m\tau)>0\). For \(\tau>0\) the first positive zero satisfies
\[
\frac{\tan(mt/2)}{\tan(t/2)}=\frac1a=m+\tau^{-1}.
\]
The ratio on the left strictly increases from \(m\) to infinity on \((0,\pi/m)\), since its logarithmic derivative is
\[
\frac{m}{\sin(mt)}-\frac1{\sin t}>0;
\]
the strict inequality follows from \(\sin(mt)<m\sin t\) on this interval. Hence this zero is unique and no closer zero exists. At \(\tau=0\), (6) reduces to \(\cos(mt/2)\), with first positive zero \(\pi/m\).

Theorem 1 of Ismoilov [1] states that for a symmetric nontrivial circle measure the nearest zero of the self-reciprocal orthogonal polynomial gives precisely the sharp last-sign-change radius, and its formula gives the unique extremizer up to scaling. The present measure is symmetric with full support. Applying that theorem to \(B_m\) proves the sharp radius and (4), including polynomiality, vanishing weighted mean, and uniqueness. **This general sharpness theorem is prior work, not a new claim.**

**3. Critical-window limit.** Write \(x_m=mt_m(\tau_m)\). For positive \(\tau_m\), equation (1) is equivalent to
\[
R_m(x_m)=1+\frac1{m\tau_m},\qquad
R_m(x)=\frac{\tan(x/2)}{m\tan(x/(2m))},\quad 0<x<\pi.
\tag{7}
\]
The ratio is strictly increasing, equals \(1\) in the limit at \(x=0\), and converges uniformly on compact subsets of \((0,\pi)\) to \(R_\infty(x)=\tan(x/2)/(x/2)\). This limiting function increases from \(1\) to infinity. If \(m\tau_m\to c\in(0,\infty)\), convergence of unique solutions gives equation (2). If \(m\tau_m\to0\), the right side of (7) diverges, forcing \(x_m\to\pi\); the same conclusion holds for indices with \(\tau_m=0\). These statements yield the first two regimes.

If \(m\tau_m\to\infty\), then \(x_m\to0\). Taylor expansion at zero, uniformly for all integers \(m\ge2\), gives
\[
 R_m(x)=1+\frac{1-m^{-2}}{12}x^2+O(x^4).
\]
Equation (7) therefore implies \(x_m^2\sim12/(m\tau_m)\). Since \(\rho_m=x_m/(2\pi m)\), this is exactly (3). Monotonicity in \(\tau\) follows directly from (7).

**4. Microscopic extremizer.** For fixed complex \(u\), (6) gives
\[
 h_{m,a_m}(u/m)
 =\cos(u/2)-a_m\cot(u/(2m))\sin(u/2)
 \longrightarrow G_c(u)
\tag{8}
\]
uniformly on compact \(u\)-sets whenever \(m\tau_m\to c\in[0,\infty]\), because \(ma_m=m\tau_m/(1+m\tau_m)\to c/(1+c)\). Also \(x_m\to x_c\), where \(x_\infty=0\), and
\[
 m^2\left[\cos(x_m/m)-\cos(u/m)\right]
 \longrightarrow\frac{u^2-x_c^2}{2}
\tag{9}
\]
locally uniformly. At the moving zeros \(u=\pm x_m\), (8) vanishes, so its square is divisible by \((u^2-x_m^2)^2\) as a local holomorphic function. The denominator in (9) has the matching simple zeros. Locally uniform convergence of the divided functions follows from holomorphic factorization and Cauchy's integral formula; it holds also when both zeros merge at \(0\) in the \(c=\infty\) case. Dividing the limits yields (5), with removable values supplied by continuity. This proves the full profile assertion.

## Verification

The provided standalone script \(\texttt{check_sign_uncertainty.py}\) verifies exact rational Gram orthogonality for several \((m,\tau)\), solves the finite critical-root equations at multiple values of \(m\tau\), and numerically checks the fixed-mass coefficient in (3). It returned:

`CHECK_OK: rational OPUC Gram identities, critical-window roots, fixed-mass edge scaling`

The proof of the infinite-degree assertions is analytical. Numerical root tests are not used to establish strict monotonicity, sharpness, uniqueness, or any limiting claim.

## Relationship to prior work

Ismoilov [1, Theorem 1] already solves the sharp sign-change problem for every symmetric circle measure using a paraorthogonal zero, and gives the extremizer in general form. Its Haar example [1, Section 1.6.1] supplies the \(\tau=0\) endpoint. The exact special-measure identity (1) and extremizer (4) follow from that general result and are **not claimed as independently new**. The contribution here is the **degree-dependent atom-strength transition**, including its exhaustive three regimes, the sharp non-Haar scaling constant, the nonlinear critical profile (2), and the locally uniform rescaled extremizers (5), none of which is stated in [1].

Simon's earlier rank-one paraorthogonal-zero framework [2] studies interlacing for unitary perturbations, while Wong's thesis [3] develops point-mass formulas for orthogonal-polynomial recursion coefficients. These tools motivate comparison but do not state the sharp sign-uncertainty concentration crossover or profile. A completely implicit deduction via general OPUC formulas is possible in principle; historical priority for this asymptotic is not definitively established.

## Limitations

The classification is for one mass at the distinguished point, against normalized Haar measure, and for the circle sign-uncertainty functional. Uniform error bounds beyond convergence, multiple or displaced atoms, and arbitrary singular components are not established. The base sharpness/uniqueness theorem is taken from [1], not reproved as a new theorem. No independent audit has been performed.

## References

[1] Tolibjon Ismoilov, *Sharp sign uncertainty for trigonometric polynomials*, arXiv:2606.02299v1, first public June 1, 2026, Theorem 1 and Section 1.6.1. https://arxiv.org/abs/2606.02299

[2] Barry Simon, *Rank one perturbations and the zeros of paraorthogonal polynomials on the unit circle*, arXiv:math/0606037v1 (2006), §§1–3. https://arxiv.org/abs/math/0606037

[3] Lilian Wong, *Orthogonal Polynomials, Paraorthogonal Polynomials, and Point Perturbation*, Ph.D. thesis, Caltech (2009), Chapters 2 and 5–6. https://thesis.caltech.edu/5229/
