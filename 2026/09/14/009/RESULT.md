# Third-order destruction of the rotation-1/3 caustic for r(theta)=1+epsilon cos(5 theta)

## Setup

Consider the analytic polar deformation
\[
\gamma(\theta;\epsilon)=(1+\epsilon\cos 5\theta)(\cos\theta,\sin\theta),
\]
which is strictly convex for sufficiently small \(|\epsilon|\).

For a reflection-axis apex \(A\in\{0,\pi/5\}\), let
\[
L(A,t;\epsilon)
 =2|\gamma(A)-\gamma(A+t)|
  +|\gamma(A+t)-\gamma(A-t)|.
\]
At \(\epsilon=0\), \(t_0=2\pi/3\) is a nondegenerate critical point:
\(L_{tt}(A,t_0;0)=-3\sqrt3/2\).
Reflection symmetry and the implicit-function theorem therefore give a genuine symmetric 3-periodic billiard orbit
\(t=t_A(\epsilon)\) near each axis. Put
\[
\ell_A(\epsilon)=L(A,t_A(\epsilon);\epsilon).
\]

## Result

There is \(\epsilon_0>0\) such that, for
\(0<|\epsilon|<\epsilon_0\), the billiard has no smooth convex caustic of rotation number \(1/3\).

The two symmetric branches satisfy
\[
\ell_0(\epsilon)
=3\sqrt3+\frac{111\sqrt3}{4}\epsilon^2
 +\frac{855\sqrt3}{2}\epsilon^3+O(\epsilon^4),
\]
and
\[
\ell_{\pi/5}(\epsilon)
=3\sqrt3+\frac{111\sqrt3}{4}\epsilon^2
 -\frac{855\sqrt3}{2}\epsilon^3+O(\epsilon^4).
\]
Hence
\[
\Delta(\epsilon)
=\ell_{\pi/5}(\epsilon)-\ell_0(\epsilon)
=-855\sqrt3\,\epsilon^3+O(\epsilon^4),
\]
which is nonzero for all sufficiently small nonzero \(\epsilon\).

## Exact coefficient calculation

For one chord, writing
\(q=q_0+\epsilon q_1+\epsilon^2q_2+\epsilon^3q_3+O(\epsilon^4)\),
the exact expansion is
\[
q_1=\frac{Q_1}{2q_0},\quad
q_2=\frac{Q_2}{2q_0}-\frac{Q_1^2}{8q_0^3},\quad
q_3=\frac{Q_1^3}{16q_0^5}-\frac{Q_1Q_2}{4q_0^3}.
\]
At \(t_0=2\pi/3\), exact symbolic differentiation gives, with the upper sign for \(A=0\),
\[
F_1=\pm63/4,\quad F_2=-81/32,\quad
G_0=-3\sqrt3/2,\quad G_1=\pm183\sqrt3/8,\quad
H_0=3/4,
\]
as well as the higher coefficients archived in `artifacts/ls_data.py`.
Lyapunov-Schmidt elimination yields
\[
u_1=\pm7\sqrt3/2,\qquad u_2=447\sqrt3/8
\]
and the two reduced-action expansions above.

The 2026-09-29 independent audit rederived these coefficients symbolically and recovered exactly
\(K_2=111\sqrt3/4\) and \(K_3=\pm855\sqrt3/2\).

## Why unequal actions rule out the resonant caustic

The relevant implication is a perturbative variational one, not the false statement that every period-3 orbit of an arbitrary table must have the same perimeter.

For an exact twist map, persistence of the rational \(1/3\) invariant circle forces the resonant Lyapunov-Schmidt reduced action (equivalently the appropriate high-order resonant Melnikov/Bialy-Mironov obstruction) to be constant in phase. This is the necessary high-order persistence condition developed in the cited Koudjinan-Ramírez-Ros theory. The two reflection-symmetric branches are critical points of that same reduced action. Their third-order critical values differ by \(855\sqrt3\epsilon^3+O(\epsilon^4)\), so the reduced action is not constant. Therefore the \(1/3\) resonant caustic cannot persist for sufficiently small nonzero \(\epsilon\).

This corrected argument uses the two branch values as a nonconstancy certificate; it does not claim that unrelated period-3 orbits outside a hypothetical invariant circle have a common action.

## Reproducibility

Run `artifacts/ls_data.py` for the exact coefficients and
`artifacts/newton_check.py` for numerical continuation of the two true symmetric branches.

## Scope and literature context

Koudjinan and Ramírez-Ros give necessary and sufficient high-order persistence conditions and explicitly note that checking the first nonzero resonant harmonic at the next order can be difficult. The retained contribution is the explicit \(n=5,q=3\) third-order evaluation above, not a new general perturbation theory.

## References

- C. E. Koudjinan, R. Ramírez-Ros, “High-order persistence of resonant caustics in perturbed circular billiards,” arXiv:2503.07488.
- Standard exact-twist variational/Aubry-Mather theory as cited there.
