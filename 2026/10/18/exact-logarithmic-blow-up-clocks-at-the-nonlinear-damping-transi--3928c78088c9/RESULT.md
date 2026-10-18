# Exact logarithmic blow-up clocks at the nonlinear damping transition

## Finding

For every even integer \(n\ge 2\), consider the polynomial Liénard equation
\[
\ddot x+\eta x^n\dot x+x^{2n+1}=0,\qquad \eta>0.
\]
Write \(\eta_c=2\sqrt{n+1}\). This is the sharp boundary between winding and nonwinding dynamics: when \(0<\eta<\eta_c\), every nonzero trajectory has infinitely many transverse zero crossings in forward time, tends to the origin as \(t\to\infty\), and blows up oscillatory in finite *reverse* time. When \(\eta\ge\eta_c\), every nonzero trajectory has only finitely many position zero crossings.

More quantitatively, for \(0<\eta<\eta_c\), let \(V_j>0\) be the absolute velocity at consecutive position zero crossings in forward time, and \(t_j\) the crossing times. Put
\[
D=4(n+1)-\eta^2,\quad q=\exp\!\left(-\frac{\pi\eta}{\sqrt D}\right),\quad \alpha=\frac{n}{n+1}.
\]
Then, without asymptotic error,
\[
V_{j+1}=qV_j,\qquad t_{j+1}-t_j=C_{n,\eta}V_j^{-\alpha},
\]
where \(C_{n,\eta}>0\) is the explicit integral in the proof below. Consequently, all backward trajectories starting at a nonzero state have finite singularity time; from a crossing with speed \(V\), the remaining reverse-time lifetime is exactly
\[
T_{\mathrm{back}}(V)=\frac{C_{n,\eta}V^{-\alpha}q^{\alpha}}{1-q^{\alpha}}.
\]
For the reversed vector field, the exact, nonconstant scaled blow-up profile in logarithmic remaining time \(s=-\log(T-t)\) is antiperiodic after \(T_{\log}/2\), and has minimal period
\[
\boxed{T_{\log}=\frac{2\pi n\eta}{(n+1)\sqrt{4(n+1)-\eta^2}}}.
\]
In particular \(T_{\log}\) diverges with an inverse-square-root law at \(\eta_c\), and the ratio of successive forward passage times diverges at the essential-singularity scale
\[
\frac{t_{j+2}-t_{j+1}}{t_{j+1}-t_j}
=\exp\!\left(\frac{\pi n\eta}{(n+1)\sqrt{4(n+1)-\eta^2}}\right).
\]
The return contraction in an inverse quasi-homogeneous radial coordinate over a full turn is exactly \(q^{2/(n+1)}=\exp(-T_{\log}/n)\). The corresponding balance-profile scaling multiplier \(\exp(T_{\log})\) is a consequence of the established general correspondence; the new quantitative content is the exact parameter-dependent clock.

For the source's numerical example \(n=2\), \(\eta=1\), the closed forms are \(T_{\log}=4\pi/(3\sqrt{11})\) and inverse-radial multiplier \(\exp[-2\pi/(3\sqrt{11})]\), matching its reported period and multiplier.

## Assumptions and scope

The parameter \(n\) is an **even integer at least 2** and \(\eta>0\). The evolution is the original physical-time ODE, not a numerically time-rescaled surrogate. Crossing velocity means \(|\dot x|\) on the section \(x=0\). Reverse time is the autonomous time reversal of the same polynomial vector field. All assertions involving repeated crossings or logarithmic cycles require \(\eta<2\sqrt{n+1}\); in particular the formula is not asserted at equality. The undamped point \(\eta=0\) is a conservative center, not a finite-time blow-up case.

## Proof

**1. Energy and the sharp angular obstruction.** Writing \(v=\dot x\), the positive definite proper energy
\[
E(x,v)=\frac{v^2}{2}+\frac{x^{2n+2}}{2n+2}
\]
satisfies \(\dot E=-\eta x^n v^2\le0\), because \(n\) is even. Each positive-time solution is global and bounded. The only invariant set inside \(\{\dot E=0\}\) is the origin, so every solution tends to zero for \(\eta>0\).

Away from \(x=0\), introduce the projective coordinate \(z=v/x^{n+1}\). Direct differentiation gives
\[
\dot z=-x^n P(z),\qquad P(z)=(n+1)z^2+\eta z+1.
\]
A straight quasi-homogeneous direction \(v=kx^{n+1}\) is invariant if and only if \(P(k)=0\). Such directions exist precisely when \(\eta\ge2\sqrt{n+1}\). They partition the compact quasi-homogeneous angular circle into invariant arcs, preventing complete turns and hence repeated zero crossings. In the complementary regime \(D>0\), \(P(z)>0\) for all real \(z\), and the compactified angular field has no zero. To justify infinite turns in *physical* forward time, use \(R=(x^{2n+2}+(n+1)v^2)^{1/(2n+2)}\) and \(ds=R^n dt\). In \(s\)-time, both \(d\log R/ds\) and angular velocity are bounded, and the latter has fixed nonzero sign. Finite total \(s\)-time would keep \(R>0\) and \(dt/ds=R^{-n}\) bounded on that finite interval, contradicting physical global forward existence. Thus \(s\to\infty\) and the angular coordinate winds infinitely often. Every crossing is transverse because \(v\ne0\) at \(x=0\) on a nonzero trajectory.

**2. Exact projective quadrature.** Between a crossing with \(v=V>0\) and the next crossing, \(x>0\); the coordinate \(z\) decreases from \(+\infty\) to \(-\infty\). Since \(d\log x/dz=-z/P(z)\), one has
\[
\frac{d\log x^{n+1}}{dz}
=-\frac{P'(z)}{2P(z)}+\frac{\eta}{2P(z)}.
\]
The normalization \(zx^{n+1}\to V\) as \(z\to+\infty\) fixes the integration constant, giving
\[
x(z)^{n+1}=\frac{V\sqrt{n+1}}{\sqrt{P(z)}}
\exp\!\left(\frac{\eta}{2}\int_{+\infty}^{z}\frac{du}{P(u)}\right).
\]
Here
\[
\int_{-\infty}^{+\infty}\frac{du}{P(u)}=\frac{2\pi}{\sqrt D}.
\]
Letting \(z\to-\infty\) gives the next velocity \(-qV\), with \(q=\exp(-\pi\eta/\sqrt D)\). Because the vector field is odd under \((x,v)\mapsto(-x,-v)\) for even \(n\), the same ratio applies at each successive crossing.

Set \(\theta=\arctan([2(n+1)z+\eta]/\sqrt D)\), \(\alpha=n/(n+1)\). Then
\[
x(z)^{n+1}=\frac{2(n+1)V}{\sqrt D}\cos\theta
\exp\!\left(\frac{\eta}{\sqrt D}(\theta-\pi/2)\right),
\qquad\frac{dt}{d\theta}=-\frac{2}{\sqrt D}x^{-n}.
\]
Consequently the positive finite half-turn constant is
\[
C_{n,\eta}=\frac2{\sqrt D}\left(\frac{\sqrt D}{2(n+1)}\right)^\alpha
\int_{-\pi/2}^{\pi/2}
\frac{\exp[-\alpha\eta(\theta-\pi/2)/\sqrt D]}{(\cos\theta)^\alpha}\,d\theta.
\]
The integral converges since \(0<\alpha<1\). It proves the exact half-turn duration law. Summing a geometric sequence of backward durations proves the stated finite reverse lifetime and divergent velocity, so the reverse-time escape is genuine finite-time blow-up, not merely failure of the section construction.

**3. Exact logarithmic period.** The system is quasi-homogeneous under \((x,v,t)\mapsto(\lambda x,\lambda^{n+1}v,\lambda^{-n}t)\). Reverse-time crossing speeds grow by \(q^{-1}\), while each successive reverse flight time shrinks by \(\rho=q^{\alpha}\). Because the tail from a crossing to the finite blow-up time is a geometric sum, consecutive crossing tails differ *exactly* by \(\rho\). In the variable \(s=-\log(T-t)\), consecutive crossing phases therefore differ by \(-\log\rho\); two crossings give the log-period
\[
-2\log\rho=\frac{2\pi n\eta}{(n+1)\sqrt D}.
\]
Quasi-homogeneous uniqueness of solutions extends this discrete scaling from crossings to their entire connecting arcs. In particular the scaled state
\[
\bigl((T-t)^{1/n}X(t),\ (T-t)^{(n+1)/n}Y(t)\bigr)
\]
of the reversed vector field is exactly periodic in \(s\) and changes sign after one half-period. It cannot have a smaller period because there are exactly two position zeros per full turn. One full crossing return multiplies the inverse quasi-homogeneous radius by \(q^{2/(n+1)}\). Finally the exact formulas yield the stated singular growth as \(\eta\uparrow\eta_c\).

## Verification

A standalone numerical-algebraic checker, `verify.py`, independently evaluates the exact quadrature and integrates sample original ODE trajectories to their first zero crossing for several even degrees and damping parameters. It also matches the two numerical invariants reported for the \(n=2\), \(\eta=1\) example of the motivating source. These finite computations corroborate but do not replace the symbolic all-parameter proof. The critical roots, unbounded-time extension, and geometric lifetime claim follow analytically from the calculations above.

## Relationship to prior work

Matsue, *On Algebraic-Dynamical Correspondence of Oscillatory Blow-Up Solutions for ODEs* (2026, arXiv:2610.05354v1), proves a general relation between periodic balance profiles and dynamics at infinity, and its Example 1 reports numerical period and multipliers for the \(n=2\), \(\eta=1\) Liénard system. That general correspondence and the existence of oscillatory reverse-time blow-up at the source parameter are **prior results**. Matsue, *On blow-up solutions of differential equations with Poincaré-type compactifications* (2018; arXiv:1611.06346), already derives an angular Poincaré integral for the fixed unit-damping model and proves qualitative oscillatory blow-up. Evaluating the unit-parameter integral alone is not claimed as a separate theorem. The new assessed scope is the all-damping **exact crossing/time/log-clock law**, the sharp quantitative transition, and the explicit period and multipliers that replace the current source's numerical profile data.

The related classical study by Dumortier and Herssens, *Polynomial Liénard equations near infinity* (1999), treats broader near-infinity topological behavior. The 2026 topological classification by Zhang is likewise relevant to angular phase types but does not provide this displayed quantitative clock law in the accessible material. These sources motivate caution about priority for the *qualitative* threshold; the quantitative logarithmic profile statement is the intended contribution.

## Limitations

The system is exactly quasi-homogeneous, not a general polynomial perturbation. The theorem provides no uniform estimate for lower-order perturbations near the critical coefficient, no classification of critical-point time laws at equality, and no exact finite-parameter classification of other nonlinear damping models. The key 1999 Dumortier–Herssens primary article could not be read in full and may contain stronger implicit quantitative return formulas. The quantitative novelty claim is subject to that explicitly identified residual priority risk.

## References

1. K. Matsue, *On Algebraic-Dynamical Correspondence of Oscillatory Blow-Up Solutions for ODEs*, arXiv:2610.05354v1, first posted 2026-10-04, particularly Theorem 4.13 and Example 1, https://arxiv.org/html/2610.05354v1.
2. K. Matsue, *On blow-up solutions of differential equations with Poincaré-type compactifications*, SIAM Journal on Applied Dynamical Systems 17 (2018), 2249–2288, arXiv:1611.06346; particularly §5, https://arxiv.org/pdf/1611.06346.
3. F. Dumortier and C. Herssens, *Polynomial Liénard equations near infinity*, Journal of Differential Equations 153 (1999), 1–29, DOI:10.1006/jdeq.1998.3543.
4. J. Zhang, *Dynamics of polynomial generalized Liénard system near the origin and infinity*, Discrete and Continuous Dynamical Systems B 37 (2026), 349–376, DOI:10.3934/dcdsb.2026055.
