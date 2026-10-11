# The one-inflection law for affine-focus crossing times

## Finding
Consider the real affine planar system
\[
\dot x=Tx-y,\qquad \dot y=Dx-a,
\]
where \(a>0\), \(D>0\), and \(4D>T^2\). For each initial state \((x(0),y(0))=(0,u)\) with \(u>0\), the trajectory returns for the first time to the line \(x=0\) at a physical time \(\tau(u)>0\), remaining in \(x<0\) before that return. Define
\[
h=T/2,\qquad \omega=\sqrt{D-h^2}>0,\qquad \delta=h/\omega.
\]
Then \(\tau:(0,\infty)\to(0,\pi/\omega)\) is a strictly increasing, real-analytic bijection. Its global curvature has the following exhaustive classification:

* If \(T\leq0\), then \(\tau''(u)<0\) for every \(u>0\).
* If \(T>0\), then there is exactly one \(u_*\in(0,\infty)\) satisfying \(\tau''(u_*)=0\), with \(\tau''(u)>0\) for \(0<u<u_*\) and \(\tau''(u)<0\) for \(u>u_*\).

The threshold is exactly the sign change of the linear trace. The inflection is specified without numerically solving the differential equation: let \(\theta_*\in(0,\pi)\) be the unique zero of
\[
M_\delta(\theta)=(1+\delta^2)e^{-\delta\theta}\sin^2\theta
-2\cos\theta\bigl[1-e^{-\delta\theta}(\cos\theta+\delta\sin\theta)\bigr].
\]
For \(T>0\), its section coordinate is
\[
u_*={a\over D}\left[h+\omega\,{e^{-\delta\theta_*}-\cos\theta_*\over\sin\theta_*}\right].
\]
In particular, the inflection phase \(\theta_*\) depends only on the dimensionless trace \(\delta\), while the amplitude \(a\) merely rescales the section coordinate.

## Assumptions and scope
All derivatives are taken with respect to the incoming section coordinate \(u>0\), and flight time is measured in the original differential-equation time variable. The assumption \(a>0\) puts the unique equilibrium at \((a/D,Ta/D)\), strictly on the opposite side of the section from the left excursion. The focus condition \(4D>T^2\) is essential to the stated universal first-return domain. No assertion is made for an overdamped node, for \(a\leq0\), for other switching geometries, or for return maps constructed by composing two half-flows.

## Proof
The scalar coordinate satisfies \(\ddot x-T\dot x+Dx=a\) with \(x(0)=0\) and \(\dot x(0)=-u\). Its exact solution is
\[
x(t)=-uG(t)+aH(t),\quad G(t)={e^{ht}\sin(\omega t)\over\omega},\quad H(t)=\int_0^tG(s)\,ds.
\]
Writing \(\theta=\omega t\), direct integration yields
\[
a{H(t)\over G(t)}=F_\delta(\theta):={a\over D}\left[h+\omega{e^{-\delta\theta}-\cos\theta\over\sin\theta}\right]
\quad(0<\theta<\pi).
\]
Set \(N_\delta(\theta)=1-e^{-\delta\theta}(\cos\theta+\delta\sin\theta)\). Elementary differentiation gives
\[
N_\delta(0)=0,\quad N_\delta'(\theta)=(1+\delta^2)e^{-\delta\theta}\sin\theta>0,
\quad F_\delta'(\theta)={a\omega\over D}{N_\delta(\theta)\over\sin^2\theta}>0.
\]
Thus \(F_\delta\) increases from \(0\) to \(+\infty\) on \((0,\pi)\). Since \(G(t)>0\) there and \(x(t)=G(t)(F_\delta(\omega t)-u)\), the unique zero for \(0<t<\pi/\omega\) occurs at \(u=F_\delta(\omega t)\). Before it, \(x(t)<0\). The implicit function theorem establishes the analytic increasing inverse \(\tau(u)=F_\delta^{-1}(u)/\omega\).

Differentiate twice with respect to \(\theta\):
\[
F_\delta''(\theta)={a\omega\over D}{M_\delta(\theta)\over\sin^3\theta},
\quad M_\delta=N_\delta'\sin\theta-2N_\delta\cos\theta.
\]
The inverse-function differentiation formula implies \(\operatorname{sgn}\tau''(u)=-\operatorname{sgn}M_\delta(\omega\tau(u))\). Introduce
\[
K_\delta=2N_\delta-\delta(1+\delta^2)e^{-\delta\theta}\sin\theta.
\]
Direct differentiation gives the exact factorization
\[
M_\delta'=\sin\theta\,K_\delta,
\qquad K_\delta'=(1+\delta^2)e^{-\delta\theta}
\bigl[(2+\delta^2)\sin\theta-\delta\cos\theta\bigr].
\]
For \(\delta\leq0\), positivity of \(N_\delta\) and \(\sin\theta\) implies \(K_\delta>0\), hence \(M_\delta\) increases strictly from \(M_\delta(0)=0\) and is positive everywhere inside the interval. Thus \(\tau''<0\).

For \(\delta>0\), the bracket in \(K_\delta'\) changes sign exactly once on \((0,\pi)\), from negative to positive, at
\[
\theta_0=\arctan\!\left({\delta\over2+\delta^2}\right)\in(0,\pi/2).
\]
Therefore \(K_\delta\), starting at zero, first decreases and then increases. The endpoint value \(K_\delta(\pi)=2(1+e^{-\delta\pi})>0\) proves it has exactly one interior zero. Accordingly \(M_\delta\) first decreases, then increases, with \(M_\delta(0)=0\) and \(M_\delta(\pi)=2(1+e^{-\delta\pi})>0\). It follows that \(M_\delta\) has exactly one zero in \((0,\pi)\), is negative before it and positive after it. Inverting the sign gives the stated unique-inflection law.

For completeness, expansion of \(F_\delta\) at zero and inversion give
\[
\tau(u)={2u\over a}+{2T\over3a^2}u^2+O(u^3)\quad(u\downarrow0).
\]
At the other boundary, the pole of \(F_\delta\) at \(\theta=\pi\) yields
\[
\tau(u)={\pi\over\omega}-{a\over D}\bigl(1+e^{-\pi\delta}\bigr){1\over u}+O(u^{-2})\quad(u\to\infty).
\]
When \(T=0\), the inverse simplifies exactly to \(\tau(u)=2\omega^{-1}\arctan(\omega u/a)\), which is strictly concave.

## Verification
The analytic argument uses exact elementary solutions, sign factorizations, and monotonicity; it does not extrapolate finite computation to a continuum. The standalone script `check_flight_time.py` symbolically verifies the three critical differentiated identities and the boundary expansion of \(M_\delta\). It additionally checks sign-crossing patterns for selected dimensionless traces. Install `requirements.txt` and run `python check_flight_time.py`; success prints `CHECK_OK`. Those samples are diagnostics only, not the uniqueness proof.

## Relationship to prior work
Carmona, Fernández-Sánchez, García-Medina and Novaes (arXiv:2109.12673; 2023 journal version) established the integral characterization, regularity, Taylor/Puiseux properties, and spatial-map second-derivative sign for Poincaré half-maps of planar linear flows. The system here is their left Liénard normal form restricted to \(a>0\) and focus discriminant. Their spatial half-map's curvature sign is not a classification of the distinct physical-flight-time function \(\tau(u)\). The earlier Carmona–Fernández-Sánchez integral-characterization paper (arXiv:1910.13431) likewise emphasizes eliminating flight time from return-map calculations; the separate time-curvature assertion here is not established by its abstract. Carmona–Fernández-García–Teruel (arXiv:2003.14112) computes relevant regional flight times for canard cycles in another piecewise-linear geometry, not the global unique-inflection theorem stated here. The 2026 Rezende–Santos–Torregrosa work considers a composite period map of a two-zone piecewise-linear system with a period annulus at infinity; that object is not the single-side first-return time studied here.

## Limitations
This is a theorem about affine foci, not general planar linear matrices, arbitrary perturbations, or nonlinear oscillators. It does not count periodic orbits of a glued piecewise system. General published formulae for linear flows might make the parameterization accessible by different coordinates; exhaustive publication priority and any implication from inaccessible full texts have not been established. The uniqueness proof, rather than the numerical checks, carries the global result.

## References
1. V. Carmona, F. Fernández-Sánchez, E. García-Medina, D. D. Novaes, *Properties of Poincaré half-maps for planar linear systems and some direct applications to periodic orbits of piecewise systems*, arXiv:2109.12673 (first posted 2021-09-26); Electronic Journal of Qualitative Theory of Differential Equations **2023**, no. 22, 1–18, DOI:10.14232/ejqtde.2023.1.22.
2. V. Carmona, F. Fernández-Sánchez, *Integral characterization for Poincaré half-maps in planar linear systems*, arXiv:1910.13431, Journal of Differential Equations **305** (2021), 319–346, DOI:10.1016/j.jde.2021.10.010.
3. V. Carmona, S. Fernández-García, A. E. Teruel, *Saddle-node canard cycles in planar piecewise linear differential systems*, arXiv:2003.14112 (2020).
4. A. C. Rezende, M. A. S. Santos, J. Torregrosa, *The period function of centers at infinity in planar piecewise linear systems*, Bulletin des Sciences Mathématiques **210** (2026), article 103809, DOI:10.1016/j.bulsci.2026.103809.
